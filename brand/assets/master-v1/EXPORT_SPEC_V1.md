# AXIONA Master Logo Export Specification V1

Status: **CANONICAL DERIVATIVE CONTRACT**

All derivatives are generated from either:

- `axiona-master-horizontal-fullcolor.svg` for complete AXIONA SYSTEMS lockups; or
- `axiona-symbol-fullcolor.svg` for symbol-only assets.

Derived assets must preserve geometry exactly. No manual redraw, proportional change, added detail or independent recoloring is allowed.

The canonical generator is:

`build_exports.py`

It produces a checksumed package and is executed by `.github/workflows/brand-master-package.yml`.

## 1. Horizontal lockup

Required standard variants:

| Variant | Background | Foreground |
| --- | --- | --- |
| Full color transparent | transparent | canonical full-color symbol + deep-petrol wordmark |
| Full color paper | `#F1EEE6` | canonical full-color symbol + deep-petrol wordmark |
| Inverse full color dark | `#082830` | orange/yellow/beige accents + reverse structural stroke/wordmark |
| Monochrome petrol | transparent | `#082830` only |
| Monochrome white | transparent | `#FFFFFF` only |

Preferred high-resolution raster export: **2172×724 PNG** with alpha where the variant is transparent.

Print/interchange export: **PDF generated from the canonical SVG**, retaining vector geometry.

## 2. Standalone symbol

Transparent PNG sizes:

- 1024×1024
- 512×512
- 256×256
- 192×192
- 180×180
- 128×128
- 64×64
- 48×48
- 32×32
- 16×16

Paper-background PNG sizes:

- 1024×1024
- 512×512
- 192×192
- 180×180

Compatibility icon:

- multi-size ICO containing 16×16, 32×32 and 48×48 symbol renders

Symbol print/interchange export: PDF from `axiona-symbol-fullcolor.svg`.

## 3. Intended consumer mapping

- 1024/512: application stores, high-resolution profile/application use
- 512/192: PWA/application identity
- 180: Apple touch icon source
- 128/64/48/32/16: compact UI and favicon derivation
- ICO: legacy/browser compatibility source
- horizontal transparent: documents, headers, compositing
- horizontal paper: AXIONA light-surface presentation
- horizontal dark: AXIONA deep-petrol surfaces
- monochrome petrol/white: constrained printing, embossing, engraving or one-color placements

## 4. Geometry invariants

Every export must retain:

- the four approved symbol components;
- the open center;
- **no small inner triangle**;
- the same relative symbol/wordmark proportions;
- the `AXIONA` + secondary `SYSTEMS` lockup arrangement for horizontal derivatives.

## 5. Color invariants

Canonical full-color palette:

- deep petrol `#082830`
- orange `#E06838`
- golden yellow `#E8B038`
- warm beige `#D0C8B0`

Surface/reverse colors:

- AXIONA paper `#F1EEE6`
- reverse warm white `#FBFAF6`
- pure-white monochrome reverse `#FFFFFF`

The dark inverse changes only the deep-petrol structural/wordmark paths to reverse warm white; the three warm accent modules remain unchanged.

## 6. Reproducibility and integrity

The generator emits:

- `PACKAGE_MANIFEST.json` with SHA-256 hashes and raster dimensions;
- `CHECKSUMS.sha256` for the complete output directory;
- `axiona-brand-master-v1.zip` containing the full derivative package.

Generated files are build outputs, not additional design authorities.

## 7. Runtime rule

This export contract defines what may be generated; it does not automatically authorize replacing existing production assets. Each runtime consumer migration must independently prove dimensions, binding, rendering and regression behavior before switching to a master-derived output.
