# AXIONA Brand Asset Manifest V1

Status: **CANONICAL INVENTORY**

This manifest assigns explicit authority to the accepted AXIONA master logo while preserving the distinction between master design sources and proven runtime consumer assets.

## 1. Master logo authority

| Asset | Role | Canonical status |
| --- | --- | --- |
| `brand/assets/master-v1/axiona-master-horizontal-fullcolor.svg` | Authoritative complete AXIONA SYSTEMS vector master | **CANONICAL MASTER / SSOT** |
| `brand/assets/master-v1/axiona-symbol-fullcolor.svg` | Authoritative standalone AXIONA symbol vector | **CANONICAL SYMBOL MASTER** |
| `brand/assets/master-v1/axiona-brand-master-v1.zip` | Complete master-derived export archive | **CANONICAL EXPORT PACKAGE** |
| `brand/assets/master-v1/MANIFEST.json` | Exact archive inventory, SHA-256 checksums and dimensions | **CANONICAL PACKAGE MANIFEST** |

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

## 2. Complete export archive

`brand/assets/master-v1/axiona-brand-master-v1.zip` contains the complete derivative set:

- master horizontal SVG/PDF/high-resolution transparent PNG;
- full-color horizontal paper-background SVG/PNG;
- full-color dark-background reverse SVG/PNG;
- monochrome petrol SVG/PNG;
- monochrome white SVG/PNG;
- standalone symbol SVG/PDF;
- transparent standalone symbol PNG sizes 1024, 512, 256, 192, 180, 128, 64, 48, 32 and 16 px;
- paper-background symbol PNG sizes 1024, 512, 192 and 180 px.

The two authoritative SVG sources remain directly browsable in GitHub. The ZIP exists to keep all raster/print exports together without turning each derived export into a competing source of truth.

`MANIFEST.json` records the SHA-256 checksum and dimensions of every archive member.

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
- `brand/assets/master-v1/README.md` — master-package usage and invariants
- `brand/assets/master-v1/MANIFEST.json` — exact export manifest
- `docs/AXIONA_WEB_VISUAL_UX_RULES.md` — durable public visual/UX guidance
- accepted R115/R116/R137/R142/R143 lineage documentation

## 6. Authority hierarchy

When sources appear to disagree, use this order:

1. Explicit current brand acceptance and master-logo invariants.
2. `brand/assets/master-v1/axiona-master-horizontal-fullcolor.svg`.
3. `brand/assets/master-v1/axiona-symbol-fullcolor.svg` for symbol-only usage.
4. `brand/` authority documentation and package manifest.
5. Current proven runtime consumer assets and bindings.
6. Historical release assets and documentation.
7. Copies in other AXIONA repositories.

## 7. Drift policy

A consumer repository may copy a brand asset only when packaging/runtime isolation requires it. The copy must be traceable to the source repository, source path and pinned Git commit/blob or release. Unexplained divergence is drift.

Runtime migration should use exact checksums and regression validation rather than manual visual replacement.
