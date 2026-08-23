# R132 — Social Metadata Invariants

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `e2550e2f1ad3f7e59588f0a65227d9b5156f8537`
Feature branch: `feature/social-metadata-invariants-r132`

## Why this release exists

Whole-site metadata audit found a real parity defect in the accepted R123/R124 page families. Support, Privacy and Legal already carried the correct language-specific social preview image, but all HU/EN/DE members were missing the core Open Graph and Twitter text/URL metadata used by Facebook, LinkedIn, X and similar link-preview consumers.

Affected pages: 9 total.
- `support.html`, `en/support.html`, `de/support.html`
- `privacy.html`, `en/privacy.html`, `de/privacy.html`
- `legal.html`, `en/legal.html`, `de/legal.html`

The rendered UI, legal/privacy wording, support copy and existing preview images remain unchanged.

## Source remediation

For each affected page R132 restores:
- `og:site_name = AXIONA Systems`
- `og:title` from the existing document title
- `og:description` from the existing page description
- `og:type = website`
- `og:url` from the existing canonical URL
- `twitter:card = summary_large_image`
- `twitter:title` from the existing document title
- `twitter:description` from the existing page description

The existing language-specific `og:image`, `og:image:secure_url`, dimensions/type and `twitter:image` values are preserved.

## Whole-site invariant

`scripts/verify_social_metadata.py` validates all 30 active HU/EN/DE pages, not only the 9 repaired pages.

It requires exactly one non-empty core Open Graph/Twitter field, exact same-page `og:url` + canonical identity, language-correct R92 preview image, 1200×630 PNG metadata, `summary_large_image`, and actual 1200×630 IHDR dimensions for all six general/Keeper social image assets.

The verifier is bound into `AXIONA Public Surface Guard` so future social metadata drift fails before merge.

## Negative contract

`.github/workflows/axiona-social-r132-invariants-contract.yml`

The contract proves fail-closed behavior for:
1. missing `og:title`;
2. wrong `og:url`;
3. wrong Twitter card type;
4. wrong language-specific preview image;
5. corrupt preview image dimensions.

## Live proof

`.github/workflows/axiona-social-r132-live-proof.yml`

After merge, it cache-busts and fetches the 9 remediated live routes and requires the restored Open Graph/Twitter markers on every page. It emits the exact source SHA only on successful convergence.

Production convergence must only be claimed when that actual push-run evidence is visible.

## Acceptance

The final exact R132 PR head must pass:
- AXIONA Public Surface Guard;
- AXIONA Social Metadata R132 Invariants Contract;
- any existing page/browser checks triggered by the 9 HTML metadata changes.

Because the changed source is HTML head metadata rather than visual layout, no new visual design contract is introduced. Existing triggered Browser Quality Audit/page contracts remain authoritative regression evidence.

Then re-resolve exact `main` + PR head and squash merge with `expected_head_sha`.
