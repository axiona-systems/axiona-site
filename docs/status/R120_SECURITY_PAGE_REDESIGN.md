# R120 — Security page redesign

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Release: `R120`
Target pages:
- `security.html`
- `en/security.html`
- `de/security.html`

## Canonical start

R120 started from the exact canonical R119 main SHA:
`05f55b49d82dbe0349529b3c82f0ca44936fd65a`

Feature branch:
`feature/security-page-r120`

The branch existed before every R120 repository write. All R120 writes explicitly target that branch.

## Design intent

The security page must communicate trust through understandable operating controls rather than theatrical security styling.

R120 uses a security-dossier / control-sheet visual language:
- warm paper/off-white as the dominant reading field;
- stable evidence and control rows on off-white document surfaces;
- deep petrol only as contained framing and deliberate chapter surfaces;
- restrained orange for editorial emphasis;
- acid green only for compact status/control labels;
- cyan as a secondary technical accent;
- one-pixel borders and solid offset shadows;
- no dashboard identity, CAD decoration, relation-map graphics, glow, scanner lines or particles;
- no fake telemetry, coordinates or pseudo-operational counters;
- no misleading click affordances on informational controls or evidence rows.

The composition intentionally reads as a controlled engineering dossier rather than a fake security console.

## Content contract

R120 preserves the existing security depth in HU/EN/DE, including:
1. necessary-data minimization;
2. role- and task-based access;
3. backup and restore discipline;
4. traceable changes;
5. maintained software and dependency handling;
6. licenses and handover clarity;
7. six practical trust/control cards;
8. six realistic threat or failure cases;
9. six trust-proof items;
10. realistic security pledge without claiming that systems are unbreakable or impossible to attack;
11. Share / Copy link / fallback sharing utility;
12. footer, support, privacy, legal and related navigation.

The six practical threat/failure cases remain explicit:
- unauthorized access;
- accidental deletion or overwrite;
- faulty release;
- lost history;
- outdated component;
- external service failure.

The opening heading is promoted to one semantic `<h1>` in all languages.

## Direct release binding

Every target HTML page binds:
- `/assets/security-r120.css?release=R120`
- `/assets/js/security-r120.js?release=R120`
- `meta[name="axiona-release"] = R120`
- `page-security-r120` body scope.

The R120 CSS is page-scoped and does not redesign the accepted homepage, R118 systems page or R119 process page.

## Motion contract

Motion is progressive enhancement and repeatable on return scroll.

R120 keeps all reveal surfaces at `opacity: 1` in every state and uses only a restrained transform. This keeps automated accessibility contrast stable and avoids the reveal-opacity regression already identified in earlier releases.

`prefers-reduced-motion: reduce` removes reveal transforms and transitions.

## Interaction contract

The following are informational surfaces and must remain visibly non-clickable:
- security checks;
- principles;
- trust/control cards;
- threat/failure rows;
- trust-proof rows.

They use the default cursor, receive no hover shift and do not acquire button-like background transitions. Only real links and buttons retain action affordances.

## Page-specific render proof

Workflow:
`.github/workflows/axiona-security-r120-visual-contract.yml`

It must prove HU/EN/DE on desktop and mobile:
- R120 release/direct bindings;
- exactly one main `<h1>`;
- one security baseline/control-sheet surface;
- 6 checks;
- 6 principles;
- 6 trust/control cards;
- 6 threat/failure rows;
- 6 trust-proof items;
- one realistic pledge surface;
- Share host and footer preserved;
- no horizontal overflow;
- expected warm-paper, off-white and contained petrol surface colors;
- informational rows remain non-clickable;
- reveal surfaces remain fully opaque;
- repeatable reveal behavior;
- screenshot evidence for all language/viewport combinations and focused HU security chapters.

## Repository quality gates

R120 is not mergeable unless the exact PR head is green for all applicable checks, including:
- AXIONA Public Surface Guard;
- AXIONA Security R120 Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse quality budgets;
- axe/WCAG audit.

No gate may be weakened to make the release pass.

## Production convergence

Post-merge workflow:
`.github/workflows/axiona-security-r120-live-proof.yml`

It verifies live HU/EN/DE HTML, CSS and JS with cache-busting proof keys and records the exact `GITHUB_SHA` being validated.

R120 is complete only after:
- exact tested PR head squash merge;
- canonical main SHA is recorded;
- GitHub Pages source converges to that exact SHA;
- live HU/EN/DE R120 bindings and asset markers are proven.

If the connector cannot independently enumerate the production Pages proof, that limitation must be recorded rather than treating production convergence as proven.

## Next design target

After R120 acceptance:
`solutions.html` / `en/solutions.html` / `de/solutions.html`.
