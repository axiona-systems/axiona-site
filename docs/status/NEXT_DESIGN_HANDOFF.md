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
- stable large surfaces;
- restrained repeatable scroll reveal;
- no hero pointer tilt.

R116 corrected UX regressions:
- informational rows no longer look clickable;
- Share + Copy link returned on HU/EN/DE overview pages;
- rendered desktop/mobile UX contract added.

## R118 systems-page release

R118 applies the accepted language to:
- `systems.html`
- `en/systems.html`
- `de/systems.html`

It preserves system-design depth, uses Keeper-derived work/document surfaces and removes fake `OPERATIONS / 024` / `LIVE STATE` presentation.

Direct bindings:
- `/assets/systems-r118.css?release=R118`
- `/assets/js/systems-r118.js?release=R118`

Canonical details:
- `docs/status/R118_SYSTEMS_PAGE_REDESIGN.md`

R118 exact squash-merge main SHA:
`9b3027076e0a48efb9ebda20039d8249bc4fe796`

## R119 process-page release

R119 redesigns:
- `process.html`
- `en/process.html`
- `de/process.html`

The content remains substantive: 4-stage journey, example status sheet, 6 process signals, 6 clarity questions, human/automation boundary, 4 outcomes and the 4-step AXIONA working method.

R119 uses a process-dossier / working-sheet composition rather than copying the systems page.

The old pseudo-operational labels are removed:
- `ÁLLAPOTLAP / 024`
- `STATUS SHEET / 024`
- `STATUSBLATT / 024`

Direct bindings:
- `/assets/process-r119.css?release=R119`
- `/assets/js/process-r119.js?release=R119`

R119 motion keeps `opacity: 1` in every reveal state and uses transform-only motion so accessibility contrast remains stable.

Canonical release details:
- `docs/status/R119_PROCESS_PAGE_REDESIGN.md`

R119 exact squash-merge main SHA:
`05f55b49d82dbe0349529b3c82f0ca44936fd65a`

Independent production Pages convergence was not proven through the available connector surface and must not be treated as proven evidence.

## R120 security-page release

R120 redesigns:
- `security.html`
- `en/security.html`
- `de/security.html`

The existing security substance remains intact: necessary-data minimization, role/task-based access, backup and restore, traceable changes, maintained software/dependencies, licenses and handover, six practical trust controls, six realistic threat/failure cases, six trust-proof items and a realistic security pledge.

R120 uses a security-dossier / control-sheet composition rather than a dashboard or fake security console.

Visual rules:
- warm paper/off-white dominant reading field;
- contained deep-petrol chapter surfaces;
- restrained orange;
- acid green only for compact status/control labels;
- cyan secondary;
- stable evidence rows;
- no CAD/relation maps, scanner lines, glow, particles, fake telemetry, coordinates or pseudo-controls.

Direct bindings:
- `/assets/security-r120.css?release=R120`
- `/assets/js/security-r120.js?release=R120`

R120 motion is transform-only and keeps all reveal surfaces at `opacity: 1`.

Canonical release details:
- `docs/status/R120_SECURITY_PAGE_REDESIGN.md`

R120 starting main SHA:
`05f55b49d82dbe0349529b3c82f0ca44936fd65a`

R120 feature branch:
`feature/security-page-r120`

R120 must not be treated as accepted until its exact tested PR head is squash-merged. Exact production Pages convergence must be proven if the available connector surface exposes that evidence; otherwise record the limitation explicitly.

## Canonical documentation

Before designing the next page, read:
1. `docs/AXIONA_WEB_VISUAL_UX_RULES.md`
2. `docs/AXIONA_VISUAL_RELEASE_CHECKLIST.md`
3. `docs/status/R115_VISUAL_REFERENCE.md`
4. `docs/status/R116_CHANGELOG.md`
5. `docs/status/R118_SYSTEMS_PAGE_REDESIGN.md`
6. `docs/status/R119_PROCESS_PAGE_REDESIGN.md`
7. `docs/status/R120_SECURITY_PAGE_REDESIGN.md`
8. `docs/r114-cache-proof-note.md`

These documents supersede older experimental visual directions where they conflict.

## Next design target after R120 acceptance

Proceed to the next secondary page only; do not redesign the accepted homepage again unless new feedback specifically requires it.

Next target:
- `solutions.html` — Megoldások
- `en/solutions.html`
- `de/solutions.html`

Treat all three languages as one coherent R121 release.

## Secondary-page design principles

- Keep security/solutions substantive; detail views must not contain less useful information than homepage entry points.
- Maintain the human, engineering-led tone.
- Do not over-promote website/webshop work; system design and process design remain primary.
- Use Keeper-derived visual grammar without turning pages into fake application dashboards.
- Technical visuals must explain actual content.
- Keep major surfaces calm and stable.
- Any visual cue that looks clickable must perform an action.
- Persistent utilities, language parity, footer/legal links and sharing must survive structural redesign.
- Example operational surfaces must be clearly illustrative, never presented as fake live telemetry.
- Reveal motion must remain repeatable without reducing text opacity below WCAG-stable contrast.

## Required delivery discipline

For every next-page release:
- re-resolve exact `main` SHA at start;
- create feature branch before any write;
- write only to that branch;
- bind the new release directly from HTML with a versioned query;
- render desktop + mobile evidence;
- test HU/EN/DE parity;
- run Public Surface Guard / applicable repository guards;
- add/update a page-specific visual contract;
- run Browser Quality Audit, Lighthouse and axe/WCAG;
- exact-head squash merge;
- prove exact GitHub Pages commit and live bindings after merge when the connector exposes sufficient production evidence.
