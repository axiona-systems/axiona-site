# AXIONA Master Logo Package V1

Status: **CANONICAL MASTER LOGO PACKAGE**

This package is derived from the AXIONA logo explicitly approved on 2026-09-06.

## Authoritative sources

`axiona-master-horizontal-fullcolor.svg`

Role: **CANONICAL AXIONA MASTER LOGO / VECTOR SOURCE OF TRUTH**

`axiona-symbol-fullcolor.svg`

Role: **CANONICAL AXIONA SYMBOL MASTER**

These two SVG files are the editable/vector authorities. Do not redraw them from PNGs, screenshots, favicon files or other downstream assets.

## Deterministic export system

`EXPORT_SPEC_V1.md` defines every standard derivative AXIONA may need.

`build_exports.py` generates the complete derivative package from the two canonical SVG sources. The GitHub workflow `.github/workflows/brand-master-package.yml` executes the same generator and publishes the package as the workflow artifact `axiona-brand-master-v1`.

The package includes:

- transparent high-resolution horizontal PNG;
- paper-background and dark-inverse horizontal SVG/PNG;
- petrol and white monochrome SVG/PNG;
- vector PDF exports;
- standalone symbol SVG/PDF;
- transparent symbol PNGs at 1024, 512, 256, 192, 180, 128, 64, 48, 32 and 16 px;
- paper-background symbol PNGs at 1024, 512, 192 and 180 px;
- multi-size ICO;
- `PACKAGE_MANIFEST.json` and `CHECKSUMS.sha256`;
- complete `axiona-brand-master-v1.zip`.

Derived files are outputs, not independent sources of truth. They are intentionally regenerated from the canonical SVGs instead of being manually maintained as competing binary masters.

## Canonical logo colors

- Deep petrol: `#082830`
- Orange: `#E06838`
- Golden yellow: `#E8B038`
- Warm beige: `#D0C8B0`
- AXIONA paper background: `#F1EEE6`
- Reverse warm white: `#FBFAF6`

## Runtime boundary

This package does **not** change current public website, favicon, PWA, Apple touch or social-preview bindings. Migrating runtime consumers to master-derived assets is a separate tested change.

## Invariants

- Do not redraw the logo.
- Do not add the previously rejected small inner triangle.
- Keep the center of the symbol open.
- Do not change symbol geometry, wordmark proportions or relative spacing without a new explicit brand decision.
- Do not recolor the master; use an approved export variant.
- Consumer repositories must pin the source commit/blob or release and verify checksums.
