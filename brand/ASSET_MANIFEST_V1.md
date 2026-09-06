# AXIONA Brand Asset Manifest V1

Status: **CANONICAL INVENTORY**
Baseline repository commit: `620720f125ce39845328a7a0ac2715377626d578`

This manifest assigns one explicit role to every currently accepted AXIONA identity asset. It is intended to eliminate ambiguous ownership and accidental drift.

## 1. Primary brand identity

| Asset | Git blob SHA | Role | Canonical status | Notes |
| --- | --- | --- | --- | --- |
| `assets/axiona-mark.png` | `5de4420e0ef416a1102a1a170d4d3e0e2d3e0925` | Primary AXIONA public brand mark | **CANONICAL** | 96×96 PNG. Used by the live public header. This is the current public mark authority. |

### Resolved decision

There is currently **no separately accepted vector master logo** and **no separately accepted flattened AXIONA + SYSTEMS wordmark image**.

The live AXIONA header lockup is composed from the canonical mark plus the text `AXIONA` and `SYSTEMS`.

Do not invent, redraw or promote another asset to master-logo status merely because it is vector or higher resolution.

## 2. Browser / application identity

| Asset | Git blob SHA | Role | Canonical status | Notes |
| --- | --- | --- | --- | --- |
| `favicon.svg` | `ca747cb66b233fedec5ff0c84f97bb4631c05dbf` | Primary scalable browser icon | **CANONICAL FOR BROWSER IDENTITY** | Blue four-part geometric SVG. It is not declared to be the master vector source of the public PNG mark. |
| `favicon-32x32.png` | `e13cdc79ffc1051b604ad9f173d8d463eb38dd8e` | Browser PNG fallback | **CANONICAL DERIVED RUNTIME ASSET** | 32×32 binding. |
| `favicon-16x16.png` | `e40e6797361a35ca6fe32db49f524db5462902ab` | Browser PNG fallback | **CANONICAL DERIVED RUNTIME ASSET** | 16×16 binding. |
| `favicon.ico` | `a0ac1f92dd3a605a44c64d759dd7e6b090b83f5f` | Legacy browser compatibility icon | **CANONICAL RUNTIME ASSET** | Keep while compatibility value exists. |
| `apple-touch-icon.png` | `26835b79b35c3411f1c894fbab6d56d92dccb329` | Apple touch identity | **CANONICAL RUNTIME ASSET** | 180×180 binding. |
| `assets/brand/axiona-icon-192.png` | `ef6c3a95a0bb44935e0fb48708ea6bfb175df820` | PWA/application icon | **CANONICAL RUNTIME ASSET** | Verified 192×192 by current browser identity contract. |
| `assets/brand/axiona-icon-512.png` | `3f9372a5c4464082df4fc8ec87fc17e3b5af31fa` | PWA/application icon | **CANONICAL RUNTIME ASSET** | Current accepted version is 512×512. |

### Resolved decision

Browser/PWA assets are **consumer identity assets**, not competing sources of brand truth. Their presence does not change the authority of `assets/axiona-mark.png` for the current public AXIONA mark.

No claim is made that every browser/PWA asset was generated pixel-for-pixel from the primary PNG. That relationship is not required for current runtime correctness and must not be guessed.

## 3. Social preview identity

### General AXIONA

| Asset | Git blob SHA | Locale | Status |
| --- | --- | --- | --- |
| `assets/social/axiona-social-preview-r92-hu.png` | `2451b6f0f80522665f8c56fa716605e82b159143` | HU | **CANONICAL CURRENT SOCIAL PREVIEW** |
| `assets/social/axiona-social-preview-r92-en.png` | `02cfec82551dfa7473909a02366e7fc650d6e348` | EN | **CANONICAL CURRENT SOCIAL PREVIEW** |
| `assets/social/axiona-social-preview-r92-de.png` | `d78adf43d0c5e6930e03c5a554cf916995cbbfe5` | DE | **CANONICAL CURRENT SOCIAL PREVIEW** |

### AXIONA Keeper

| Asset | Git blob SHA | Locale | Status |
| --- | --- | --- | --- |
| `assets/social/axiona-keeper-social-preview-r92-hu.png` | `2b70223ee5e696c8299b729fc32c2a1b5a8d8343` | HU | **CANONICAL PRODUCT SOCIAL PREVIEW** |
| `assets/social/axiona-keeper-social-preview-r92-en.png` | `a45ee43b5913937e3eb5f9572280916cf4a40aed` | EN | **CANONICAL PRODUCT SOCIAL PREVIEW** |
| `assets/social/axiona-keeper-social-preview-r92-de.png` | `f44f8f494aa96e5767634e429a8986026f338fcb` | DE | **CANONICAL PRODUCT SOCIAL PREVIEW** |

Social previews are publishing assets. They are not primary logo masters.

## 4. Canonical design documentation

| Document | Git blob SHA | Authority role |
| --- | --- | --- |
| `brand/README.md` | branch-local | Brand authority entry point and ownership rules |
| `brand/AXIONA_BRAND_SYSTEM_V1.md` | branch-local | Consolidated current visual-system reference |
| `brand/ASSET_MANIFEST_V1.md` | branch-local | Exact identity asset inventory and role assignment |
| `docs/AXIONA_WEB_VISUAL_UX_RULES.md` | `7e42dbaff6d5b1515eb2992fe9284a2f59b45e3e` | Durable accepted public visual/UX guidance |
| `docs/status/R115_VISUAL_REFERENCE.md` | `c0241e4849145abc09dd243b8b4524e81a9be10e` | Accepted visual baseline reference |
| `docs/status/R116_CHANGELOG.md` | `93f4af25af38d5af61acf2677e927f9ac26057e6` | Accepted UX correction lineage |
| `docs/status/R143_REPO_AUDIT.md` | `f9ccc40d52ea14d466f7eaa75eefc133a995ba5f` | Current cleanup/hardening closeout preserving R137/R142 behavior |

## 5. Runtime implementation layers

The following files materially implement the current design but are **not separate brand authorities**:

- `assets/styles-r71.css` — base design tokens and structural primitives;
- `assets/visual-r115.css` — accepted R115 visual composition layer;
- `assets/visual-r116.css` — accepted R116 correction layer;
- `assets/r137-ux-fixes.css` — current accepted UX/layout correction layer;
- `assets/motion-r138.css` — current motion implementation, with R142 tuning made authoritative by the R143 cleanup;
- page-specific current CSS (`systems-r118.css`, `process-r119.css`, `security-r120.css`, `solutions-r121.css`, `contact-r122.css`, `support-r123.css`, `policy-r124.css`, `keeper-r125.css`, `not-found-r126.css`).

These files remain in their runtime locations. The brand authority documents describe what is canonical; they do not duplicate the whole runtime implementation.

## 6. Authority hierarchy

When sources appear to disagree, use this order:

1. Explicit current acceptance / hardening state in canonical documentation.
2. This `brand/` authority layer.
3. Current live runtime references on canonical `main`.
4. Current runtime implementation assets.
5. Historical release documents and superseded implementation history.
6. Copies in other AXIONA repositories.

A lower layer must not silently override a higher layer.

## 7. Drift policy

A consumer repository may copy an asset only when necessary for packaging/runtime isolation. Such a copy must be traceable to:

- source repository;
- source path;
- source Git blob SHA or pinned release;
- intended consumer role.

An unexplained changed copy is drift.

For future automated distribution, prefer a pinned brand release/package plus checksum verification over manually copied files.

## 8. Open items intentionally fixed as policy, not guessed as data

### Vector master

**State:** no accepted master vector exists in the current public authority.

**Policy:** `favicon.svg` remains browser identity only. A future master vector requires explicit acceptance against the current public mark.

### Flattened wordmark

**State:** no accepted flattened `AXIONA SYSTEMS` image was found in the current live authority.

**Policy:** the composed live lockup remains canonical.

### Physical centralization

**State:** live identity assets are still located at their proven runtime paths.

**Policy:** do not relocate them merely for tidiness. `brand/` is the canonical index/authority now; physical relocation is a separate migration requiring consumer inventory, checksums and regression proof.

## 9. Future dedicated repository target

If AXIONA reaches the point where multiple products need independently versioned brand consumption, the recommended dedicated repository name is:

`axiona-systems/AXIONA_BRAND`

That repository should become authoritative only through an explicit migration. Until then, this directory in `axiona-site` is the canonical brand authority and current live asset inventory.
