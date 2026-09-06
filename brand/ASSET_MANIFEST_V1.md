# AXIONA Brand Asset Manifest V1

Status: **CANONICAL INVENTORY**

This manifest assigns explicit authority to the accepted AXIONA master logo while preserving the distinction between master design sources, generated derivatives and proven runtime consumer assets.

## 1. Master logo authority

| Asset | Role | Canonical status |
| --- | --- | --- |
| `brand/assets/master-v1/axiona-master-horizontal-fullcolor.svg` | Authoritative complete AXIONA SYSTEMS vector master | **CANONICAL MASTER / SSOT** |
| `brand/assets/master-v1/axiona-symbol-fullcolor.svg` | Authoritative standalone AXIONA symbol vector | **CANONICAL SYMBOL MASTER** |
| `brand/assets/master-v1/EXPORT_SPEC_V1.md` | Standard derivative/export contract | **CANONICAL EXPORT SPECIFICATION** |
| `brand/assets/master-v1/MANIFEST.json` | Machine-readable authority declaration and invariants | **CANONICAL MASTER MANIFEST** |
| `brand/assets/master-v1/build_exports.py` | Deterministic derivative/package generator | **CANONICAL EXPORT BUILDER** |
| `.github/workflows/brand-master-package.yml` | CI validation and export artifact publisher | **CANONICAL BUILD PATH** |

### Accepted master-logo invariants

- four-part symbol: deep petrol, orange, golden yellow, warm beige;
- open center;
- no small inner triangle;
- horizontal lockup text is `AXIONA` with secondary `SYSTEMS`;
- master geometry is not to be reconstructed from downstream raster assets.

Canonical master-logo palette:

- `#082830` deep petrol
- `#E06838` orange
- `#E8B038` golden yellow
- `#D0C8B0` warm beige
- `#F1EEE6` paper background
- `#FBFAF6` reverse warm white

## 2. Standard derivatives

`brand/assets/master-v1/build_exports.py` generates the complete standard derivative set defined by `EXPORT_SPEC_V1.md`, including:

- horizontal full-color transparent;
- horizontal full-color paper-background;
- horizontal inverse full-color dark;
- monochrome petrol and monochrome white;
- print/vector PDF derivatives;
- standalone symbol SVG/PDF;
- transparent symbol PNG sizes from 1024 px down to 16 px;
- paper-background symbol PNG sizes for application/touch usage;
- multi-size ICO;
- SHA-256 checksum file and generated package manifest;
- complete `axiona-brand-master-v1.zip`.

GitHub publishes these derivatives as the workflow artifact `axiona-brand-master-v1`. Generated files are outputs, not independent sources of brand truth, and are not maintained as competing binary masters in Git.

## 3. Current public/runtime identity assets

The following files remain canonical for their current runtime roles until a separate migration replaces their bindings:

- `assets/axiona-mark.png` — current public header consumer asset;
- `favicon.svg` — current scalable browser icon;
- `favicon-32x32.png` and `favicon-16x16.png` — browser PNG fallbacks;
- `favicon.ico` — legacy browser compatibility;
- `apple-touch-icon.png` — Apple touch runtime identity;
- `assets/brand/axiona-icon-192.png` and `assets/brand/axiona-icon-512.png` — current PWA/application runtime icons.

These runtime assets no longer outrank the accepted master SVG as design authority. They remain proven consumers until migrated and revalidated.

## 4. Social preview identity

Current publishing assets remain:

- `assets/social/axiona-social-preview-r92-hu.png`
- `assets/social/axiona-social-preview-r92-en.png`
- `assets/social/axiona-social-preview-r92-de.png`
- Keeper-specific R92 social-preview variants.

Social previews are publishing assets, not logo masters.

## 5. Canonical design documentation

- `brand/README.md` — brand authority entry point
- `brand/AXIONA_BRAND_SYSTEM_V1.md` — accepted visual-system reference
- `brand/ASSET_MANIFEST_V1.md` — this inventory
- `brand/assets/master-v1/README.md` — master-logo package usage and invariants
- `brand/assets/master-v1/MANIFEST.json` — machine-readable master declaration
- `brand/assets/master-v1/EXPORT_SPEC_V1.md` — standard derivative contract
- `brand/assets/master-v1/build_exports.py` — deterministic derivative builder
- `.github/workflows/brand-master-package.yml` — generated-package CI path
- `docs/AXIONA_WEB_VISUAL_UX_RULES.md` — durable public visual/UX guidance
- accepted R115/R116/R137/R142/R143 lineage documentation

## 6. Authority hierarchy

When sources appear to disagree, use this order:

1. Explicit current brand acceptance and master-logo invariants.
2. `brand/assets/master-v1/axiona-master-horizontal-fullcolor.svg`.
3. `brand/assets/master-v1/axiona-symbol-fullcolor.svg` for symbol-only usage.
4. `brand/` authority documentation and machine-readable manifest.
5. Deterministically generated CI artifacts.
6. Current proven runtime consumer assets and bindings.
7. Historical release assets and documentation.
8. Copies in other AXIONA repositories.

## 7. Drift policy

A consumer repository may copy a brand asset only when packaging/runtime isolation requires it. The copy must be traceable to the source repository, source path and pinned Git commit/blob or release. Unexplained divergence is drift.

Runtime migration should use generated checksums, exact source identity and regression validation rather than manual visual replacement.
