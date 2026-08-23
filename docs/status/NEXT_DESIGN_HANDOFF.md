# AXIONA Site — Next Design Handoff

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Canonical branch: `main`

## Accepted design baseline

R115/R116 remain the visual and interaction baseline:
- warm paper/off-white dominant field;
- contained deep-petrol work/control surfaces;
- restrained orange;
- acid green only for small status/control signals;
- cyan only as a secondary technical accent;
- thin borders and solid offset shadows;
- Keeper-derived product/work-surface representation;
- generous negative space and stable surfaces;
- no CAD/relation-map identity, scanner/glow/particles, fake telemetry or hero pointer tilt;
- informational rows must not look clickable;
- repeatable restrained motion;
- Share + Copy link + fallback sharing retained.

## R118 — System design

Targets:
- `systems.html`
- `en/systems.html`
- `de/systems.html`

Direct bindings:
- `/assets/systems-r118.css?release=R118`
- `/assets/js/systems-r118.js?release=R118`

Release document:
- `docs/status/R118_SYSTEMS_PAGE_REDESIGN.md`

Exact squash-merge main SHA:
`9b3027076e0a48efb9ebda20039d8249bc4fe796`

## R119 — Process design

Targets:
- `process.html`
- `en/process.html`
- `de/process.html`

R119 preserves the substantive process journey and uses a process-dossier / working-sheet composition. Motion is transform-only with opacity always `1`.

Direct bindings:
- `/assets/process-r119.css?release=R119`
- `/assets/js/process-r119.js?release=R119`

Release document:
- `docs/status/R119_PROCESS_PAGE_REDESIGN.md`

Exact squash-merge main SHA:
`05f55b49d82dbe0349529b3c82f0ca44936fd65a`

Independent production Pages convergence was not exposed through the available connector and must not be treated as proven evidence.

## R120 — Security

Targets:
- `security.html`
- `en/security.html`
- `de/security.html`

R120 preserves the security substance: data minimization, role/task access, backup/recovery, traceability, maintained dependencies, licensing/handover, realistic failure modes and trust-proof content. It uses a security-dossier / control-sheet composition rather than a fake security console.

Direct bindings:
- `/assets/security-r120.css?release=R120`
- `/assets/js/security-r120.js?release=R120`

Release document:
- `docs/status/R120_SECURITY_PAGE_REDESIGN.md`

Starting main SHA:
`05f55b49d82dbe0349529b3c82f0ca44936fd65a`

Feature branch:
`feature/security-page-r120`

Exact tested PR head:
`896edb6731bd9b08d486a1efd0cb609fa2aee400`

PR #71 exact-head checks passed:
- AXIONA Public Surface Guard;
- AXIONA Security R120 Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse;
- axe/WCAG.

Exact squash-merge main SHA:
`0c5e9c25bf189b24d74415a628aa07abde663dcd`

The GitHub connector returned no push/check status entries for the merge SHA, so exact production Pages convergence remains unproven through this interface and must not be inferred.

## R121 — Solutions

Targets:
- `solutions.html`
- `en/solutions.html`
- `de/solutions.html`

R121 uses a solution-brief / option-matrix composition. It preserves:
- implementation forms;
- four problem-to-direction examples;
- five system layers;
- the technology-neutral first-conversation message;
- the AXIONA Keeper own-product section;
- sharing, footer/legal/support and visit-counter bindings.

Websites/webshops remain one possible implementation form rather than the primary positioning.

Direct bindings:
- `/assets/solutions-r121.css?release=R121`
- `/assets/js/solutions-r121.js?release=R121`

R121 motion is transform-only and keeps reveal opacity at `1`. Informational problem cards, system-layer rows and Keeper process rows remain default-cursor, stable surfaces.

Release document:
- `docs/status/R121_SOLUTIONS_PAGE_REDESIGN.md`

Starting main SHA:
`0c5e9c25bf189b24d74415a628aa07abde663dcd`

Feature branch:
`feature/solutions-page-r121`

Page-specific render contract:
- `.github/workflows/axiona-solutions-r121-visual-contract.yml`

Post-merge live proof:
- `.github/workflows/axiona-solutions-r121-live-proof.yml`

R121 is not accepted until its exact tested PR head passes all required gates and is squash-merged with `expected_head_sha`.

## Canonical documentation

Before the next design release, read:
1. `docs/AXIONA_WEB_VISUAL_UX_RULES.md`
2. `docs/AXIONA_VISUAL_RELEASE_CHECKLIST.md`
3. `docs/status/R115_VISUAL_REFERENCE.md`
4. `docs/status/R116_CHANGELOG.md`
5. `docs/status/R118_SYSTEMS_PAGE_REDESIGN.md`
6. `docs/status/R119_PROCESS_PAGE_REDESIGN.md`
7. `docs/status/R120_SECURITY_PAGE_REDESIGN.md`
8. `docs/status/R121_SOLUTIONS_PAGE_REDESIGN.md`
9. `docs/r114-cache-proof-note.md`

These documents supersede older experimental visual directions where they conflict.

## Next likely design target after R121 acceptance

Review the remaining secondary public pages as one inventory first. The likely next coherent family is:
- `contact.html`
- `en/contact.html`
- `de/contact.html`

Do not redesign the accepted homepage again unless new feedback specifically requires it. Start any next release from the then-current exact `main` SHA on a new feature branch.

## Required delivery discipline

For every visual release:
- re-resolve exact `main` SHA;
- create feature branch before all writes;
- explicitly target that branch on every write;
- bind versioned CSS/JS directly from HU/EN/DE HTML;
- preserve persistent utilities and content depth;
- render desktop/mobile evidence and verify language parity;
- run Public Surface Guard, page-specific visual contract, Browser Quality Audit, Lighthouse and axe/WCAG;
- never weaken a gate merely to pass it;
- re-resolve exact PR head and `main` immediately before merge;
- squash merge with `expected_head_sha`;
- prove exact production convergence when the connector exposes sufficient evidence, otherwise record the limitation explicitly.
