# AXIONA Brand Asset Manifest V1

Status: **CANONICAL INVENTORY**

This manifest assigns explicit authority to the accepted AXIONA master logo while preserving the distinction between master design sources, generated exports and proven runtime consumer assets.

## 1. Master logo authority

| Asset | Role | Canonical status |
| --- | --- | --- |
| `brand/assets/master-v1/axiona-master-horizontal-fullcolor.svg` | Authoritative complete AXIONA SYSTEMS vector master | **CANONICAL MASTER / SSOT** |
| `brand/assets/master-v1/axiona-symbol-fullcolor.svg` | Authoritative standalone AXIONA symbol vector | **CANONICAL SYMBOL MASTER** |
| `brand/assets/master-v1/MANIFEST.json` | Canonical source declaration and export matrix | **CANONICAL SOURCE MANIFEST** |
| `brand/assets/master-v1/build_exports.py` | Deterministic generator for all derivatives | **CANONICAL EXPORT BUILDER** |
| `.github/workflows/brand-master-package.yml` | CI validation and artifact publisher | **CANONICAL BUILD PATH** |

### Accepted master-logo invariants

- four-part symbol: deep petrol, orange, golden yellow, warm beige;
- open center;
- no small inner triangle;
- horizontal lockup text is `AXIONA` with secondary `SYSTEMS`;
- master geometry is not reconstructed from downstream raster assets.

Canonical master-logo palette:

- `#082830` deep petrol
- `#E06838` orange
- `#E8B038` golden yellow
- `#D0C8B0` warm beige
- `#F1EEE6` paper background
- `#FBFAF6` reverse warm white

## 2. Generated export package

The master builder generates the complete derivative set without committing duplicate binary sources:

- master horizontal high-resolution transparent PNG and PDF;
- full-color horizontal paper-background SVG/PNG;
- full-color dark-background reverse SVG/PNG;
- monochrome petrol SVG/PNG;
- monochrome white SVG/PNG;
- standalone symbol PDF and paper-background SVG;
- transparent standalone symbol PNG sizes 1024, 512, 256, 192, 180, 128, 64, 48, 32 and 16 px;
- paper-background symbol PNG sizes 1024, 512, 192 and 180 px;
- generated package `MANIFEST.json` and `CHECKSUMS.sha256`;
- `axiona-brand-master-v1.zip`.

The GitHub workflow publishes these outputs as the `axiona-brand-master-v1` workflow artifact. Derived binaries are not Git authorities and are regenerated from the master sources.

## 3. Current public/runtime identity assets

The following files remain canonical for their current runtime roles until a separate migration replaces their bindings:

- `assets/axiona-mark.png` - current public header consumer asset;
- `favicon.svg` - current scalable browser icon;
- `favicon-32x32.png` and `favicon-16x16.png` - browser PNG fallbacks;
- `favicon.ico` - legacy browser compatibility;
- `apple-touch-icon.png` - Apple touch runtime identity;
- `assets/brand/axiona-icon-192.png` and `assets/brand/axiona-icon-512.png` - current PWA/application runtime icons.

These runtime assets no longer outrank the accepted master SVG as design authority. They remain proven consumers until migrated and revalidated.

## 4. Social preview identity

Current publishing assets remain:

- `assets/social/axiona-social-preview-r92-hu.png`
- `assets/social/axiona-social-preview-r92-en.png`
- `assets/social/axiona-social-preview-r92-de.png`
- Keeper-specific R92 social-preview variants.

Social previews are publishing assets, not logo masters.

## 5. Canonical design documentation

- `brand/README.md` - brand authority entry point
- `brand/AXIONA_BRAND_SYSTEM_V1.md` - accepted visual-system reference
- `brand/ASSET_MANIFEST_V1.md` - this inventory
- `brand/assets/master-v1/README.md` - master-source usage and invariants
- `brand/assets/master-v1/MANIFEST.json` - canonical source/export manifest
- `docs/AXIONA_WEB_VISUAL_UX_RULES.md` - durable public visual/UX guidance
- accepted R115/R116/R137/R142/R143 lineage documentation

## 6. Authority hierarchy

When sources appear to disagree, use this order:

1. Explicit current brand acceptance and master-logo invariants.
2. `brand/assets/master-v1/axiona-master-horizontal-fullcolor.svg`.
3. `brand/assets/master-v1/axiona-symbol-fullcolor.svg` for symbol-only usage.
4. `brand/` authority documentation and source manifest.
5. Generated CI export artifacts.
6. Current proven runtime consumer assets and bindings.
7. Historical release assets and documentation.
8. Copies in other AXIONA repositories.

## 7. Drift policy

A consumer repository may copy a brand asset only when packaging/runtime isolation requires it. The copy must be traceable to the source repository, source path and pinned Git commit/blob or release. Unexplained divergence is drift.

Runtime migration should use generated checksums and regression validation rather than manual visual replacement.
