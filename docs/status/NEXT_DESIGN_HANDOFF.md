# AXIONA Site — Next Design Handoff

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Canonical branch: `main`

## Current accepted state

Homepage direction is accepted after R115 and R116.

R115 established the current AXIONA visual language:
- warm paper/off-white dominant;
- contained deep-petrol work/control surfaces;
- restrained orange;
- acid green only for small status/control signals;
- thin borders and solid offset shadows;
- Keeper-derived product/work-surface representation;
- no CAD/relation-map identity;
- no scanner/glow/particles;
- stable System Story surfaces;
- restrained repeatable scroll reveal;
- no hero pointer tilt.

R116 corrected UX regressions:
- problem-type rows are clearly informational and no longer look clickable;
- Share + Copy link returned on HU/EN/DE overview pages;
- rendered desktop/mobile UX contract added.

## Canonical documentation

Before designing the next page, read:
1. `docs/AXIONA_WEB_VISUAL_UX_RULES.md`
2. `docs/AXIONA_VISUAL_RELEASE_CHECKLIST.md`
3. `docs/status/R115_VISUAL_REFERENCE.md`
4. `docs/status/R116_CHANGELOG.md`
5. `docs/r114-cache-proof-note.md`

These documents supersede older experimental visual directions where they conflict.

## Next design target

Proceed to the next secondary page only; do not redesign the accepted homepage again unless new feedback specifically requires it.

Recommended order:
1. `systems.html` — Rendszerépítés
2. `process.html` — Folyamattervezés
3. `security.html` — Biztonság
4. `solutions.html` — Megoldások

Each page must be redesigned across HU/EN/DE as one coherent release.

## Secondary-page design principles

- Keep systems/process/security as substantive pages; do not make their detail views contain less useful information than the homepage entry points.
- Maintain the human, engineering-led tone.
- Do not over-promote website/webshop work; system design and process design remain primary.
- Use Keeper-derived visual grammar without turning pages into fake application dashboards.
- Technical visuals must explain actual content.
- Keep major surfaces calm and stable.
- Any visual cue that looks clickable must perform an action.
- Persistent utilities, language parity, footer/legal links and sharing must survive structural redesign.

## Required delivery discipline

For the next page release:
- re-resolve exact `main` SHA at start;
- create feature branch before any write;
- write only to that branch;
- bind new visual release directly from HTML with a new release query;
- render desktop + mobile evidence;
- test HU/EN/DE parity;
- run Public Surface Guard;
- add/update page-specific visual contract;
- run Browser Quality Audit, Lighthouse and axe/WCAG;
- exact-head squash merge;
- prove exact GitHub Pages commit and live bindings after merge.

## Current production baseline before R117 documentation merge

R116 production merge:
`bcb55ae1235e94a888b840b4704c1c84b67e29ff`

R117 is documentation-only and must not alter public rendering.
