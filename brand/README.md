# AXIONA Brand Authority

Status: **CANONICAL / V1**

This directory is the single entry point for the accepted AXIONA visual identity and brand assets.

## Canonical master logo

The AXIONA master logo was explicitly approved on 2026-09-06 and is physically stored under:

`brand/assets/master-v1/`

Authoritative source:

`brand/assets/master-v1/axiona-master-horizontal-fullcolor.svg`

Role: **CANONICAL AXIONA MASTER LOGO / VECTOR SOURCE OF TRUTH**

The standalone symbol vector is:

`brand/assets/master-v1/axiona-symbol-fullcolor.svg`

These two SVG files are the only editable logo geometry authorities. PNG, PDF, background, monochrome, icon-size and ZIP files are generated derivatives and must not redefine the master.

The approved mark has four components: deep-petrol structural stroke, orange upper module, golden-yellow lower-left module and warm-beige lower-right module. The center remains open. The previously rejected small inner triangle is not part of the master logo.

## Canonical logo palette

- Deep petrol: `#082830`
- Orange: `#E06838`
- Golden yellow: `#E8B038`
- Warm beige: `#D0C8B0`
- AXIONA paper background: `#F1EEE6`
- Reverse warm white: `#FBFAF6`

These values describe the accepted master logo. Product UI design tokens remain governed by `AXIONA_BRAND_SYSTEM_V1.md` and the accepted public-site visual lineage.

## Deterministic exports

`brand/assets/master-v1/build_exports.py` derives all required web, app, print and icon variants from the two canonical SVGs. `.github/workflows/brand-master-package.yml` validates this on GitHub and publishes the complete `axiona-brand-master-v1` artifact, including PNG, PDF, variant SVG, checksums, manifest and ZIP outputs.

Derived binaries are intentionally not committed to Git, preventing binary drift and preserving a single editable source of truth.

## Runtime boundary

The current public website runtime assets are not silently replaced by this change. Existing favicon, PWA, social-preview and header bindings remain at their proven runtime paths until a separate migration validates exact consumer behavior and browser/public-surface regression gates.

The historical public header asset `assets/axiona-mark.png` therefore remains a **canonical current runtime consumer asset**, but it is no longer the master design source. Future logo derivatives originate from `brand/assets/master-v1/axiona-master-horizontal-fullcolor.svg`.

## Brand design authority

Current accepted AXIONA visual grammar continues to derive from R115 visual direction, R116 UX corrections, R137 layout/navigation behavior, R142 motion tuning and R143 repository cleanup/hardening. Durable public visual rules remain in `docs/AXIONA_WEB_VISUAL_UX_RULES.md`.

## Canonicality rules

1. New AXIONA logo work starts from the master SVG, never from a screenshot or downstream PNG.
2. Do not redraw, distort or independently edit generated variants.
3. Do not add the rejected small inner triangle.
4. Project-specific identity may extend the brand but must not silently redefine the master mark.
5. Copies in other repositories are consumers, not authorities.
6. Consumer copies should pin a source commit/release and verify generated checksums.
7. Runtime replacement of existing web/app/browser assets is a separate tested migration.

## Authority files

- `README.md` - brand authority and ownership rules
- `AXIONA_BRAND_SYSTEM_V1.md` - accepted visual system
- `ASSET_MANIFEST_V1.md` - canonical asset inventory and role assignment
- `assets/master-v1/README.md` - master-logo source and export rules
- `assets/master-v1/MANIFEST.json` - canonical source declaration and export matrix
- `assets/master-v1/build_exports.py` - deterministic derivative builder
