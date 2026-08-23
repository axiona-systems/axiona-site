# R119 — Process page redesign

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Release: `R119`
Target pages:
- `process.html`
- `en/process.html`
- `de/process.html`

## Canonical start

R119 started from the exact canonical R118 main SHA:
`9b3027076e0a48efb9ebda20039d8249bc4fe796`

Feature branch:
`feature/process-page-r119`

The branch existed before every R119 repository write. All R119 writes explicitly target that branch.

## Design intent

The process page must remain substantive and distinct from the systems page.

R119 uses a process-dossier / working-sheet visual language:
- warm paper/off-white as the dominant field;
- stable document-like rows for stages, signals and decisions;
- deep petrol only as contained framing and one deliberate handoff chapter;
- restrained orange for current-state emphasis and editorial markers;
- acid green only for compact status/control labels;
- cyan as a secondary technical accent;
- one-pixel borders and solid offset shadows;
- no decorative network maps, CAD identity, glow, scanner lines or particles;
- no fake telemetry;
- no misleading click affordances on informational surfaces.

The composition intentionally does not copy the R118 systems-page layout. The page reads as a process dossier: current journey, failure signals, clarity questions, resulting operating model and delivery method.

## Content contract

R119 preserves the existing process-design depth in HU/EN/DE:
1. four-stage example journey;
2. example status sheet;
3. six signals that a process needs attention;
4. six practical questions that remove ambiguity;
5. explicit boundary around human judgement versus automation;
6. four concrete outcomes from process design;
7. link back to System Design;
8. four-step AXIONA working method;
9. direct author/ownership surface;
10. Share / Copy link / fallback sharing utility;
11. footer, support, privacy, legal and security navigation.

The opening heading is promoted to one semantic `<h1>` in all languages.

The old pseudo-operational labels are removed:
- `ÁLLAPOTLAP / 024`
- `STATUS SHEET / 024`
- `STATUSBLATT / 024`

The visual is explicitly an example status, not live telemetry.

## Direct release binding

Every target HTML page binds:
- `/assets/process-r119.css?release=R119`
- `/assets/js/process-r119.js?release=R119`
- `meta[name="axiona-release"] = R119`
- `page-process-r119` body scope.

The R119 CSS is page-scoped and does not redesign the accepted homepage or the R118 systems release.

## Motion contract

Motion is progressive enhancement and repeatable on return scroll.

R119 deliberately keeps reveal surfaces at `opacity: 1` in every state. Only a restrained vertical transform is used. This preserves WCAG contrast stability during automated axe auditing and avoids repeating the R118 opacity regression.

`prefers-reduced-motion: reduce` removes reveal transforms and transitions.

## Interaction contract

The following are informational surfaces:
- process stages;
- process-problem signals;
- clarity questions;
- handoff outcomes;
- method steps.

They use default cursor behavior and receive no hover shift or button-like interaction treatment. Only real links and buttons retain action affordances.

## Page-specific render proof

Workflow:
`.github/workflows/axiona-process-r119-visual-contract.yml`

It must prove HU/EN/DE on desktop and mobile:
- R119 release/direct bindings;
- exactly one main `<h1>`;
- 4 stages;
- 4 status rows;
- 6 process signals;
- 6 clarity questions;
- 4 handoff outcomes;
- 4 method steps;
- Share host and footer preserved;
- no horizontal overflow;
- rejected pseudo-telemetry absent;
- expected Keeper-derived stable surface colors;
- informational rows remain non-clickable;
- reveal surfaces remain fully opaque;
- repeatable reveal behavior;
- screenshot evidence for all language/viewport combinations and focused HU chapters.

## Repository quality gates

R119 is not mergeable unless the exact PR head is green for all applicable checks, including:
- AXIONA Public Surface Guard;
- AXIONA Process R119 Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse quality budgets;
- axe/WCAG audit.

No gate may be weakened to make the release pass.

## Production convergence

Post-merge workflow:
`.github/workflows/axiona-process-r119-live-proof.yml`

It verifies live HU/EN/DE HTML, CSS and JS with cache-busting proof keys and records the exact `GITHUB_SHA` being validated.

R119 is complete only after:
- exact tested PR head squash merge;
- canonical main SHA is recorded;
- GitHub Pages source converges to that exact SHA;
- live HU/EN/DE R119 bindings and asset markers are proven.

## Next design target

After R119 acceptance:
`security.html` / `en/security.html` / `de/security.html`.
