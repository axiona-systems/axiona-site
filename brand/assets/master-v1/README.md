# AXIONA Master Logo Package V1

Status: **CANONICAL MASTER LOGO PACKAGE**

This package is derived from the AXIONA logo explicitly approved on 2026-09-06.

## Authoritative source

`axiona-master-horizontal-fullcolor.svg`

Role: **CANONICAL AXIONA MASTER LOGO / VECTOR SOURCE OF TRUTH**

The standalone symbol vector is:

`axiona-symbol-fullcolor.svg`

These two SVG files are stored directly in GitHub and are the authoritative editable/vector sources. Do not redraw them from PNGs or screenshots.

## Complete export archive

`axiona-brand-master-v1.zip`

The ZIP is the complete reproducible export package. `MANIFEST.json` describes its contents and SHA-256 checksums.

It contains:

- master horizontal SVG, PDF and high-resolution transparent PNG;
- full-color paper-background horizontal SVG/PNG;
- full-color dark-background reverse SVG/PNG;
- monochrome petrol horizontal SVG/PNG;
- monochrome white horizontal SVG/PNG;
- standalone symbol SVG/PDF;
- transparent symbol PNG exports at 1024, 512, 256, 192, 180, 128, 64, 48, 32 and 16 px;
- paper-background symbol PNG exports at 1024, 512, 192 and 180 px.

The files inside the archive are derivatives of the accepted master geometry. They must not be edited independently.

## Canonical logo colors

- Deep petrol: `#082830`
- Orange: `#E06838`
- Golden yellow: `#E8B038`
- Warm beige: `#D0C8B0`
- AXIONA paper background: `#F1EEE6`
- Reverse warm white: `#FBFAF6`

## Runtime boundary

This package does **not** change the current public website, favicon, PWA, Apple touch or social-preview bindings. Migrating runtime consumers to the new master-derived assets is a separate tested change.

## Invariants

- Do not redraw the logo.
- Do not add the previously rejected small inner triangle.
- Keep the center of the symbol open.
- Do not change symbol geometry, wordmark proportions or relative spacing without a new explicit brand decision.
- Do not recolor the master. Use the supplied variants.
- Consumer repositories must pin the source commit/blob or release and verify checksums.
