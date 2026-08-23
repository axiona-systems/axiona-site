# R128 — Public Surface Invariants

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `7f0ead903aefd203a5fefb1b51c7f674ebb12c5d`
Feature branch: `feature/public-surface-invariants-r128`

## Why this release exists

R127 exposed a structural gap in the repository-level Public Surface Guard. The guard validated the explicitly listed 30 HU/EN/DE active pages, but an extra physical public HTML file outside that list could still be published without being inspected. That is how the legacy `en/404.html` and `de/404.html` surfaces survived until the route inventory found them.

R128 changes the verification model from “check the pages we remembered to list” to “prove the whole published HTML surface matches the declared public model”.

This is regression hardening, not a visual redesign.

## Strengthened invariants

`scripts/verify_site.py` now verifies:

1. **Complete physical HTML inventory**
   - expected: 30 active localized pages plus the single root `404.html`;
   - any missing expected HTML fails;
   - any extra `.html` anywhere in the published repository tree fails.

2. **Language identity**
   - each active HU/EN/DE page must expose the matching `<html lang>`.

3. **Canonical identity**
   - each active page must have exactly one canonical URL;
   - the canonical must equal its declared AXIONA public URL.

4. **Hreflang family parity**
   - every active page must expose exactly the expected `hu`, `en`, `de`, and `x-default` alternate mapping;
   - `x-default` resolves to the HU member of the same route family;
   - duplicate hreflang entries fail.

5. **Release-family parity**
   - every active page must contain exactly one non-empty `meta[name=axiona-release]`;
   - HU/EN/DE members of the same route family must carry the same release marker;
   - each page must directly bind at least one same-site asset with `?release=<its release marker>`.
   - older compatibility layers may remain bound with older query versions; R128 does not require every asset query to equal the page release.

6. **Same-host absolute link integrity**
   - `https://axiona.systems/...` and protocol-relative AXIONA references are treated as local public references;
   - a missing same-host destination fails just like a missing relative link;
   - references escaping the repository root fail closed.

7. **Root 404 invariants**
   - one physical root `404.html` only;
   - initial `lang=hu` fallback;
   - release marker `R126`;
   - `robots=noindex,follow`;
   - direct R126 release binding;
   - no canonical/hreflang publication from the error page.

Existing sitemap, robots, security.txt, sensitive-material and non-public-email checks remain in force.

## Testability refactor

The verifier now supports:

```text
python3 scripts/verify_site.py --root <repository-copy>
```

The normal Public Surface Guard still runs it without arguments. The optional root exists so the invariant contract can build isolated mutated repository fixtures without altering the PR checkout.

## Negative-test contract

`.github/workflows/axiona-public-invariants-r128-contract.yml`

The contract first requires the untouched repository baseline to pass. It then creates five independent faulty copies and proves that each is rejected:

1. extra `en/stale-r128.html` → `unexpected public html`;
2. wrong EN systems canonical → `canonical mismatch`;
3. wrong DE hreflang target on EN systems → `hreflang mismatch`;
4. EN systems release marker changed to `R999` → `language release mismatch`;
5. dead absolute `https://axiona.systems/...` link → `broken local reference`.

A negative fixture unexpectedly passing is itself a contract failure.

## Scope boundary

R128 does not change accepted page content, visual composition, tracking behavior or production routing. If the stronger verifier exposes a genuine current defect during CI, fix that defect rather than weakening the invariant.

## Acceptance

The exact R128 PR head must pass:
- AXIONA Public Surface Guard using the strengthened verifier;
- AXIONA Public Invariants R128 Contract;
- AXIONA Browser Quality Audit;
- Lighthouse;
- axe/WCAG.

Then re-resolve exact `main` + PR head and squash merge with `expected_head_sha`.
