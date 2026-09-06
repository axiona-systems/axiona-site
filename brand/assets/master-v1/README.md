# AXIONA Master Logo Package V1

Status: **CANONICAL MASTER LOGO SOURCE**

This directory contains the AXIONA logo explicitly approved on 2026-09-06.

## Vector source of truth

Primary master:

`axiona-master-horizontal-fullcolor.svg`

Role: **CANONICAL AXIONA MASTER LOGO / VECTOR SOURCE OF TRUTH**

Standalone symbol:

`axiona-symbol-fullcolor.svg`

These SVGs are the authoritative geometry. Do not redraw the logo from PNGs, screenshots, favicons or historical runtime assets.

## Generated export package

Raster, PDF, background, monochrome and packaged ZIP variants are **build outputs**, not additional sources of truth.

Run:

```bash
python brand/assets/master-v1/build_exports.py --output dist/axiona-brand-master-v1
```

The GitHub workflow `.github/workflows/brand-master-package.yml` runs the same builder and publishes the complete package as a workflow artifact named `axiona-brand-master-v1`.

Generated outputs include:

- high-resolution transparent horizontal PNG;
- full-color paper-background horizontal SVG/PNG;
- full-color dark-background horizontal SVG/PNG;
- petrol and white monochrome horizontal SVG/PNG;
- horizontal master PDF;
- standalone symbol PDF;
- paper-background standalone symbol SVG;
- transparent symbol PNGs at 1024, 512, 256, 192, 180, 128, 64, 48, 32 and 16 px;
- paper-background symbol PNGs at 1024, 512, 192 and 180 px;
- generated `MANIFEST.json` and `CHECKSUMS.sha256`;
- `axiona-brand-master-v1.zip` as the complete export artifact.

Derived binaries are intentionally not committed to Git. This prevents binary drift and keeps one editable source of truth.

## Canonical logo colors

- Deep petrol: `#082830`
- Orange: `#E06838`
- Golden yellow: `#E8B038`
- Warm beige: `#D0C8B0`
- AXIONA paper background: `#F1EEE6`
- Reverse warm white: `#FBFAF6`

## Invariants

- Do not redraw the logo.
- Do not add the previously rejected small inner triangle.
- Keep the symbol center open.
- Do not distort the symbol or wordmark proportions.
- Do not alter relative spacing without a new explicit brand decision.
- Do not recolor the master; generate/use the supplied variants.
- Consumer repositories must pin a source commit/release and verify the generated package manifest/checksums.

## Runtime boundary

This source package does **not** replace current website, favicon, PWA, Apple touch or social-preview runtime bindings. Runtime migration is a separate tested change.
