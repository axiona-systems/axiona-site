# AXIONA Brand Consumer Boundary

Status: **R147 CANONICAL RUNTIME MIGRATION**

`axiona-systems/axiona-site` remains a public presentation/runtime consumer of AXIONA identity. It is not the authority for master brand geometry, brand rules, master export tooling or system-level brand governance.

## System authority

Canonical authority repository: `axiona-systems/AXIONA_BRAND`

Pinned authority commit: `aebf0f112bd5f4e589ef58f337a55d9be861b493`

Canonical source identities:

- horizontal master Git blob: `374cc2f8738cb0abd519016cac2759b1cc43be0d`
- standalone symbol Git blob: `1fbe0628bf1d6240495da75dfab2b51a28aac391`
- deterministic export artifact digest: `sha256:3fbd354301b45ff0fe2e4edff425003eed300b812d228a82ddf798af40ebae0d`
- authority workflow run: `34063542627`
- authority artifact: `9998217611` (`axiona-brand-master-v1`)

The site does not regenerate or redefine these masters. It consumes exact approved derivatives from the pinned authority package.

## R147 public runtime mapping

The previous blue/teal site identity has been fully retired from the active public runtime. R147 maps each placement to the appropriate canonical or approved derivative:

| Public placement | Runtime asset | Authority role |
| --- | --- | --- |
| Header / navigation | `assets/brand/axiona-horizontal-fullcolor.svg` | exact canonical horizontal master copy |
| Footer / dark surface | `assets/brand/axiona-horizontal-monochrome-white.svg` | exact approved monochrome-white derivative |
| Browser SVG favicon | `favicon.svg` | exact canonical symbol SVG copy |
| 16 px favicon | `favicon-16x16.png` | exact deterministic symbol derivative |
| 32 px favicon | `favicon-32x32.png` | exact deterministic symbol derivative |
| Legacy/browser ICO | `favicon.ico` | exact deterministic 16/32/48 multi-size ICO |
| Apple touch icon | `apple-touch-icon.png` | exact 180 px paper-background symbol derivative |
| PWA icon | `assets/brand/axiona-icon-192.png` | exact 192 px paper-background symbol derivative |
| PWA icon | `assets/brand/axiona-icon-512.png` | exact 512 px paper-background symbol derivative |
| Social preview cards | `assets/social/*r147-*.png` | R92 composition retained, old identity replaced by the canonical horizontal lockup, fresh cache-busting URLs |

The site manifest now uses the canonical AXIONA paper (`#F1EEE6`) and deep petrol (`#082830`) colors.

## Completeness

All 31 public HTML documents bind the full-color horizontal lockup in the header and the monochrome-white lockup in the footer. All 30 indexable HU/EN/DE pages bind locale-correct R147 social cards. The 404 page carries the same header/footer and browser identity.

The following legacy identity is prohibited after R147:

- `assets/axiona-mark.png`
- any `assets/social/*r92-*.png` file
- any HTML reference to `/assets/axiona-mark.png` or `r92-` social cards

## Machine verification

`assets/brand/AXIONA_BRAND_RUNTIME_V1.json` records the pinned authority, placement mapping and exact SHA-256 hashes of every active brand/browser/social runtime asset.

`scripts/verify_brand_consumer_boundary.py` fails closed on:

- reintroduction of system-level master authority into this repository;
- provenance drift;
- hash drift in canonical runtime assets;
- missing or wrong header/footer lockups;
- legacy mark or R92 social-card reappearance;
- public page-count drift.

`verify_browser_identity.py`, `verify_social_metadata.py`, `verify_asset_references.py` and the browser render contract provide independent dimension, binding and layout checks.
