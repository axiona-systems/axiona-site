# AXIONA Master Logo Package V1

Status: **CANONICAL MASTER LOGO PACKAGE**

This package is derived from the AXIONA logo explicitly approved on 2026-09-06.
The authoritative source is:

`axiona-master-horizontal-fullcolor.svg`

All other assets in this directory are derivatives for specific rendering contexts.
They must not be edited independently. Regenerate them from the master SVG or the approved symbol SVG.

## Canonical logo colors

- Deep petrol: `#082830`
- Orange: `#E06838`
- Golden yellow: `#E8B038`
- Warm beige: `#D0C8B0`
- AXIONA paper background: `#F1EEE6`
- Reverse warm white: `#FBFAF6`

## Master files

- `axiona-master-horizontal-fullcolor.svg` — authoritative vector master
- `axiona-master-horizontal-fullcolor.pdf` — print/vector interchange
- `axiona-master-horizontal-fullcolor.png` — high-resolution transparent raster master
- `axiona-symbol-fullcolor.svg` — authoritative standalone symbol vector
- `axiona-symbol-fullcolor.pdf` — standalone symbol print/vector interchange

## Derived horizontal variants

- `axiona-horizontal-fullcolor-paper.svg/png` — full-color logo on AXIONA paper
- `axiona-horizontal-fullcolor-dark.svg/png` — reverse full-color logo on deep petrol
- `axiona-horizontal-monochrome-petrol.svg/png` — one-color petrol
- `axiona-horizontal-monochrome-white.svg/png` — one-color white/reverse

## Symbol exports

Transparent PNG: 1024, 512, 256, 192, 180, 128, 64, 48, 32, 16 px.
Paper-background PNG: 1024, 512, 192, 180 px.

These sizes cover common app/PWA, Apple touch, social/profile, favicon and document use. Runtime bindings are **not changed by this package**; changing the live site to consume these assets is a separate migration.

## Invariants

- Do not redraw the logo.
- Do not add the previously rejected small inner triangle.
- Do not change symbol geometry, wordmark proportions or relative spacing without a new explicit brand decision.
- Do not recolor the master. Use the supplied derived variants instead.
- Consumer repositories must pin the source commit/blob or release and verify checksums.
