# AXIONA Site — Next Design Handoff

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Canonical branch: `main`

## Current accepted design baseline

Homepage direction remains accepted after R115 and R116.

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
- informational rows no longer look clickable;
- Share + Copy link returned on HU/EN/DE overview pages;
- rendered desktop/mobile UX contract added.

## R118 systems-page release

R118 applies the accepted R115/R116 language to the system-design page family:
- `systems.html`
- `en/systems.html`
- `de/systems.html`

R118 preserves the existing system-design depth instead of reducing the detail page.
The page family uses Keeper-derived work/document surfaces, stable informational rows and a contained petrol verification/release/operation chapter.

R118 explicitly removes fake `OPERATIONS / 024` / `LIVE STATE` presentation from the system example and presents it as an example workflow instead.

R118 direct bindings:
- `/assets/systems-r118.css?release=R118`
- `/assets/js/systems-r118.js?release=R118`

R118 has its own rendered visual contract and post-merge live-binding proof.
Canonical release details are documented in:
- `docs/status/R118_SYSTEMS_PAGE_REDESIGN.md`

R118 must not be treated as complete until its exact tested PR head is squash-merged and exact GitHub Pages production convergence is proven.

## Canonical documentation

Before designing the next page, read:
1. `docs/AXIONA_WEB_VISUAL_UX_RULES.md`
2. `docs/AXIONA_VISUAL_RELEASE_CHECKLIST.md`
3. `docs/status/R115_VISUAL_REFERENCE.md`
4. `docs/status/R116_CHANGELOG.md`
5. `docs/status/R118_SYSTEMS_PAGE_REDESIGN.md`
6. `docs/r114-cache-proof-note.md`

These documents supersede older experimental visual directions where they conflict.

## Next design target after R118 acceptance

Proceed to the next secondary page only; do not redesign the accepted homepage again unless new feedback specifically requires it.

Recommended order:
1. `process.html` — Folyamattervezés
2. `security.html` — Biztonság
3. `solutions.html` — Megoldások

Each page must be redesigned across HU/EN/DE as one coherent release.

## Secondary-page design principles

- Keep process/security/solutions substantive; do not make detail views contain less useful information than the homepage entry points.
- Maintain the human, engineering-led tone.
- Do not over-promote website/webshop work; system design and process design remain primary.
- Use Keeper-derived visual grammar without turning pages into fake application dashboards.
- Technical visuals must explain actual content.
- Keep major surfaces calm and stable.
- Any visual cue that looks clickable must perform an action.
- Persistent utilities, language parity, footer/legal links and sharing must survive structural redesign.
- Preserve R118's lesson: example operational surfaces must be clearly illustrative, not presented as fake live telemetry.

## Required delivery discipline

For every next-page release:
- re-resolve exact `main` SHA at start;
- create feature branch before any write;
- write only to that branch;
- bind new visual release directly from HTML with a new release query;
- render desktop + mobile evidence;
- test HU/EN/DE parity;
- run Public Surface Guard / applicable repository guards;
- add/update page-specific visual contract;
- run Browser Quality Audit, Lighthouse and axe/WCAG;
- exact-head squash merge;
- prove exact GitHub Pages commit and live bindings after merge.

## R118 canonical start

R118 starting main SHA:
`5c9dece444ebc5ae296afa504fbd7cdff0418f8b`

R118 feature branch:
`feature/systems-page-r118`
