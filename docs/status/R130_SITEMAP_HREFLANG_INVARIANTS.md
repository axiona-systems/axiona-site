# R130 — Sitemap Hreflang Invariants

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `b97e2120254d910c5f1591e7b0abd1b9044baf1d`
Feature branch: `feature/sitemap-hreflang-invariants-r130`

## Why this release exists

The whole-site audit found that `sitemap.xml` currently contains the expected HU/EN/DE/x-default alternate families, but the repository guard only verified the set of `<loc>` URLs. A future regression could therefore keep all 30 URLs present while silently corrupting one language alternate, duplicating a hreflang, or removing part of a locale family.

R130 makes the sitemap localization structure a fail-closed public-surface invariant. No sitemap content change is required because the current source already matches the intended model.

## Invariant model

New verifier:

`scripts/verify_sitemap_hreflang.py`

It requires:
- the standard sitemap `<urlset>` namespace;
- exactly the declared 30 active public URLs;
- exactly one non-empty `<loc>` per `<url>` entry;
- no duplicate `<loc>` values;
- every `<loc>` belongs to one of the ten HU/EN/DE route families;
- exactly four XHTML alternate links per URL entry;
- every alternate uses `rel="alternate"`;
- exactly one each of `hu`, `en`, `de`, and `x-default`;
- no duplicate hreflang key;
- the HU/EN/DE targets point to the corresponding route-family members;
- `x-default` points to the HU member of the same family.

Success evidence reports:
- `OK_AXIONA_SITEMAP_HREFLANG`
- `SITEMAP_URLS=30`
- `SITEMAP_HREFLANG_LINKS=120`

The verifier supports `--root` so isolated negative fixtures can be tested without mutating the checkout.

## Guard integration

`.github/workflows/axiona-repo-guard.yml` now runs both:
1. `python3 scripts/verify_site.py`
2. `python3 scripts/verify_sitemap_hreflang.py`

This keeps the sitemap locale model inside the central Public Surface Guard and adds no browser/runtime dependency.

## Negative contract

Workflow:

`.github/workflows/axiona-sitemap-r130-invariants-contract.yml`

The contract first requires the current sitemap baseline to pass, then proves fail-closed behavior with isolated mutations:
1. change the English Systems alternate to the German target → must fail with `sitemap hreflang mismatch`;
2. duplicate an English home hreflang entry → must fail with `duplicate sitemap hreflang`.

## Scope boundary

R130 changes verification only. It does not alter public HTML, sitemap content, CSS, JavaScript, tracking, routing or rendered UI. Because no browser-visible source changes, R130 does not trigger a redundant Lighthouse/axe cycle; the R129 browser matrix remains the accepted browser-quality baseline.

## Acceptance

The exact R130 PR head must pass:
- AXIONA Public Surface Guard, including the new sitemap verifier;
- AXIONA Sitemap R130 Invariants Contract.

Then re-resolve exact `main` + PR head and squash merge with `expected_head_sha`.
