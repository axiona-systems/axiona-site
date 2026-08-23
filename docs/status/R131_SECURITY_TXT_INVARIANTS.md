# R131 — security.txt Invariants

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `cfa47f55b3b1f3c76f740cfe61ff4001c6d3c60b`
Feature branch: `feature/security-txt-invariants-r131`

## Why this release exists

The central Public Surface Guard previously verified only that `.well-known/security.txt` existed. A stale, malformed or semantically broken vulnerability-disclosure file could therefore remain publishable while all other site checks stayed green.

R131 hardens that static security metadata against RFC 9116 requirements and AXIONA's current disclosure policy. It does not change public page content, UI, tracking or routing.

Reference specification: RFC 9116 — A File Format to Aid in Security Vulnerability Disclosure.

## Source invariants

`scripts/verify_security_txt.py` verifies:

1. `.well-known/security.txt` exists and is valid UTF-8;
2. the file is bounded to 32 KiB and contains no NUL byte;
3. at least one valid `Contact` URI is present;
4. `mailto:` contacts must use the `axiona.systems` domain;
5. exactly one `Expires` field exists;
6. `Expires` is timezone-aware RFC3339, is still in the future, and is no more than 366 days ahead under AXIONA policy;
7. `Canonical` is exactly `https://axiona.systems/.well-known/security.txt`;
8. `Policy` is exactly `https://axiona.systems/security.html`;
9. `Preferred-Languages` appears once and declares exactly `hu`, `en`, and `de` without duplicates;
10. malformed or empty field lines fail closed.

The existing public file already satisfies this contract; R131 is regression hardening, not a content rewrite.

## Guard binding

`.github/workflows/axiona-repo-guard.yml` now runs:

```text
python3 scripts/verify_security_txt.py
```

alongside the existing whole-site and sitemap invariants.

## Negative contract

`.github/workflows/axiona-security-txt-r131-contract.yml`

The contract proves fail-closed behavior for:
- missing Contact;
- duplicate Expires;
- expired Expires;
- Expires more than 366 days ahead;
- wrong/insecure Canonical;
- wrong Preferred-Languages set;
- invalid Contact URI scheme.

The baseline is evaluated at a fixed RFC3339 reference time so the negative test remains deterministic.

## Live delivery proof

`.github/workflows/axiona-security-txt-r131-live-proof.yml`

After a main push affecting the security.txt contract, it:
- retrieves `https://axiona.systems/.well-known/security.txt` over HTTPS with a cache-busting proof query;
- requires a successful response;
- requires `Content-Type: text/plain`;
- validates the downloaded body with `scripts/verify_security_txt.py`;
- verifies the canonical and policy lines;
- emits the exact source SHA as proof metadata.

Production convergence must only be claimed when this actual push-run evidence is visible.

## Acceptance

The final exact R131 PR head must pass:
- AXIONA Public Surface Guard;
- AXIONA Security.txt R131 Invariants Contract.

Browser Quality Audit/Lighthouse/axe are not required because R131 changes no browser-rendered source or browser-quality contract.

Then re-resolve exact `main` + PR head and squash merge with `expected_head_sha`.
