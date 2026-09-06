# AXIONA Brand Authority

Status: **CANONICAL / V1**

This directory is the single entry point for the currently accepted AXIONA visual identity and brand assets.

It does **not** redesign AXIONA and it does **not** relocate live runtime assets. Runtime paths remain unchanged until a separate migration can prove zero regression.

## Canonical baseline

Repository baseline at creation:

`620720f125ce39845328a7a0ac2715377626d578`

Current accepted visual lineage:

- R115: accepted visual direction;
- R116: accepted UX corrections;
- R137: accepted current layout/navigation behavior;
- R142: accepted current motion tuning;
- R143: repository cleanup/hardening preserving the accepted public design.

The durable visual rules remain in `docs/AXIONA_WEB_VISUAL_UX_RULES.md` and are summarized here for brand-wide use.

## Identity authority

### Primary public brand mark

Canonical live mark:

`/assets/axiona-mark.png`

Role: **PRIMARY BRAND MARK**

This is the mark rendered in the live AXIONA header. Until a separately approved vector master is introduced, this PNG is the authoritative public mark. Do not replace it from an inferred or reconstructed source.

### AXIONA wordmark / lockup

The current website does not use a flattened AXIONA wordmark image. The live lockup is composed from:

1. `/assets/axiona-mark.png`
2. text `AXIONA`
3. text `SYSTEMS`

Therefore no other image should be called the canonical AXIONA wordmark unless it is explicitly accepted later.

### Browser identity

These are canonical browser/runtime identity assets, but they are **not automatically treated as the master logo source**:

- `/favicon.svg`
- `/favicon-32x32.png`
- `/favicon-16x16.png`
- `/favicon.ico`
- `/apple-touch-icon.png`
- `/assets/brand/axiona-icon-192.png`
- `/assets/brand/axiona-icon-512.png`

Their exact roles are listed in `ASSET_MANIFEST_V1.md`.

### Social identity

Current general AXIONA social preview family:

- `/assets/social/axiona-social-preview-r92-hu.png`
- `/assets/social/axiona-social-preview-r92-en.png`
- `/assets/social/axiona-social-preview-r92-de.png`

Keeper has its own accepted social-preview variants and is listed separately in the manifest.

## Brand design authority

The currently accepted AXIONA visual grammar is:

- warm paper / off-white dominant field;
- deep petrol for contained control/work surfaces;
- restrained orange for active/control emphasis;
- acid green only for compact status/control signals;
- cyan only as a secondary technical accent;
- thin one-pixel borders;
- solid offset shadows instead of soft glow;
- generous negative space;
- calm editorial / engineering composition;
- technical diagrams only when they communicate real structure.

Explicitly rejected as brand identity:

- full-page dark dashboard styling;
- decorative CAD/relation-map identity;
- fake telemetry;
- scanner lines;
- glow/particle effects;
- excessive motion;
- pseudo-controls that look interactive but are not.

Exact tokens and usage rules are in `AXIONA_BRAND_SYSTEM_V1.md`.

## Canonicality rules

1. New AXIONA visual work starts here.
2. A project-specific visual may extend the brand, but must not silently redefine it.
3. Copies in other repositories are consumers, not authorities.
4. If a copy differs from this authority, the difference must be intentional and documented; otherwise it is drift.
5. Never overwrite the primary mark based on a guessed relationship between PNG, SVG, favicon or social assets.
6. Runtime asset relocation requires its own tested migration.
7. Historical release CSS is implementation history, not independent brand authority.

## Files in this authority layer

- `README.md` — authority and ownership rules
- `AXIONA_BRAND_SYSTEM_V1.md` — current visual system
- `ASSET_MANIFEST_V1.md` — exact canonical asset inventory and roles

## Next safe consolidation step

A later migration may move the physical master assets into a dedicated brand repository or package and make product repositories consume pinned releases. That should only be done with checksum-based validation and consumer migration; this V1 intentionally avoids breaking current public runtime paths.
