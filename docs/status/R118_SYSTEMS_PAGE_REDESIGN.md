# R118 — Systems page redesign

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Release: `R118`
Target pages:
- `systems.html`
- `en/systems.html`
- `de/systems.html`

## Canonical start

R118 was started only after re-resolving canonical `main`.

Exact starting main SHA:
`5c9dece444ebc5ae296afa504fbd7cdff0418f8b`

Feature branch:
`feature/systems-page-r118`

No repository write for R118 was performed before the feature branch existed. All R118 writes explicitly targeted that branch.

## Design basis

R118 inherits the accepted AXIONA public visual language from R115 and the interaction corrections from R116.

Required characteristics:
- warm paper / off-white dominant field;
- contained deep-petrol work and control surfaces;
- restrained orange emphasis;
- acid green only for compact status/control signals;
- cyan only as a secondary technical accent;
- one-pixel borders;
- solid offset shadows;
- Keeper-derived document/work surfaces;
- calm editorial hierarchy and generous negative space;
- technical representation only where it explains the operation.

Explicitly rejected for this page:
- CAD/dashboard identity;
- relation-map or node-network decoration;
- scanner lines;
- glow or particle effects;
- fake coordinates or telemetry;
- pointer tilt;
- full-card scroll color switching;
- misleading click affordances on informational elements.

## Content contract

R118 is a visual and structural redesign, not a content reduction.

The existing systems-page depth remains intact in HU/EN/DE:
1. operational-first system design introduction;
2. example workflow and system-design explanation;
3. six system layers;
4. verification, release and operation controls;
5. AXIONA long-term operability principle;
6. four customer-facing outcomes;
7. links to Process Design and Security;
8. Share / Copy link / fallback sharing utility;
9. footer, legal/support/security navigation and visit-counter binding.

The hero heading is promoted to a semantic `<h1>` in all three languages.

The old decorative labels `OPERATIONS / 024` and `LIVE STATE` are removed. The workflow surface is explicitly presented as an example rather than fake live telemetry.

## R118 implementation

New directly bound assets:
- `/assets/systems-r118.css?release=R118`
- `/assets/js/systems-r118.js?release=R118`

Every HU/EN/DE systems page contains:
- `meta[name="axiona-release"] = R118`;
- the direct R118 CSS binding;
- the direct R118 JS binding;
- `page-systems-r118` body scope.

The R118 CSS is page-scoped and does not redesign the accepted homepage.

## Motion contract

Motion is progressive enhancement.

- content remains visible if JavaScript does not run;
- IntersectionObserver adds and removes reveal state as content enters and leaves the viewport;
- returning to a section replays the restrained reveal;
- `prefers-reduced-motion: reduce` disables transforms/transitions and leaves content visible.

## Interaction contract

System layers, control cards and outcome surfaces are informational.
They use default cursor behavior and receive no arrow, hover movement or button-like interaction treatment.

Only real anchors/buttons retain action affordances.

## Render and quality evidence

Page-specific workflow:
`.github/workflows/axiona-systems-r118-visual-contract.yml`

It must prove for HU/EN/DE on desktop and mobile:
- release and direct asset bindings;
- one semantic main heading;
- 4 example workflow rows;
- 6 system layers;
- 3 control cards;
- 4 outcome surfaces;
- share host and footer preserved;
- no horizontal overflow;
- no rejected fake telemetry;
- Keeper-derived stable surface colors;
- informational rows remain non-clickable;
- repeatable reveal behavior;
- screenshot artifacts for all language/viewport combinations plus focused HU sections.

Repository-wide browser quality workflow must also remain green:
- Lighthouse budgets;
- axe/WCAG audit.

Other applicable repository/public-surface checks must remain green without weakening their contract.

## Production convergence

Post-merge live-proof workflow:
`.github/workflows/axiona-systems-r118-live-proof.yml`

It is bound to `main` pushes affecting the R118 systems release and proves:
- live HU/EN/DE HTML all expose R118 direct bindings;
- live CSS contains the R118 contract marker;
- live JS contains the R118 repeatable-motion marker;
- `.ax-share` remains present on all three pages;
- rejected fake telemetry does not reappear;
- the proof run records the exact `GITHUB_SHA` it is validating.

Release completion additionally requires the GitHub Pages build/deployment source commit to equal the exact merged canonical SHA.

## Definition of done

R118 is complete only when:
- PR checks are green;
- page-specific desktop/mobile evidence is green;
- Public Surface Guard / repository guard checks are green as applicable;
- Browser Quality Audit, Lighthouse and axe/WCAG are green;
- the tested exact PR head is squash-merged;
- canonical `main` SHA is recorded;
- GitHub Pages converges to that exact SHA;
- live HU/EN/DE R118 bindings and assets are proven.
