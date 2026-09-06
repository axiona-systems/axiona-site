# AXIONA Master Logo Package V1

Status: **CANONICAL MASTER LOGO PACKAGE**

This package is derived from the AXIONA logo explicitly approved on 2026-09-06.

## Authoritative sources

`axiona-master-horizontal-fullcolor.svg`

Role: **CANONICAL AXIONA MASTER LOGO / VECTOR SOURCE OF TRUTH**

`axiona-symbol-fullcolor.svg`

Role: **CANONICAL AXIONA SYMBOL MASTER**

These two SVG files are the editable/vector authorities. Do not redraw them from PNGs, screenshots, favicon files or other downstream assets.

## Export contract

`EXPORT_SPEC_V1.md` defines every standard derivative AXIONA may need: horizontal full-color, light/dark backgrounds, monochrome/reverse, print PDF, standalone symbol and the standard icon sizes for web/PWA/Apple/favicons.

Derived files are outputs, not independent sources of truth. They should be regenerated from the canonical SVGs when needed and verified against the export specification.

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
