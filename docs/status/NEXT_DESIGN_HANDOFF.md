# AXIONA Site — Next Design Handoff

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Canonical branch: `main`

## Accepted design baseline

R115/R116 remain canonical visual/interaction guidance:
- warm paper/off-white dominant field;
- contained deep-petrol work/control surfaces;
- restrained orange;
- acid green only for compact status/control signals;
- cyan as secondary technical accent;
- thin borders, solid offset shadows and generous negative space;
- Keeper-derived working/document surfaces;
- no CAD/relation-map identity, fake telemetry, scanner/glow/particles or pseudo-controls;
- informational surfaces must not look clickable;
- restrained repeatable motion; opacity-sensitive accessibility regressions are prohibited.

## Accepted secondary-page releases

### R118 — System design
Targets: `systems.html`, `en/systems.html`, `de/systems.html`

Direct bindings:
- `/assets/systems-r118.css?release=R118`
- `/assets/js/systems-r118.js?release=R118`

Exact squash-merge main SHA:
`9b3027076e0a48efb9ebda20039d8249bc4fe796`

### R119 — Process design
Targets: `process.html`, `en/process.html`, `de/process.html`

Direct bindings:
- `/assets/process-r119.css?release=R119`
- `/assets/js/process-r119.js?release=R119`

Exact squash-merge main SHA:
`05f55b49d82dbe0349529b3c82f0ca44936fd65a`

### R120 — Security
Targets: `security.html`, `en/security.html`, `de/security.html`

Direct bindings:
- `/assets/security-r120.css?release=R120`
- `/assets/js/security-r120.js?release=R120`

Exact tested PR #71 head:
`896edb6731bd9b08d486a1efd0cb609fa2aee400`

Exact squash-merge main SHA:
`0c5e9c25bf189b24d74415a628aa07abde663dcd`

### R121 — Solutions
Targets: `solutions.html`, `en/solutions.html`, `de/solutions.html`

R121 uses a solution-brief / option-matrix composition and preserves implementation forms, four problem-to-direction examples, five system layers, technology-neutral first-conversation guidance, Keeper, sharing and footer/legal/support bindings.

Direct bindings:
- `/assets/solutions-r121.css?release=R121`
- `/assets/js/solutions-r121.js?release=R121`

Exact tested PR #72 head:
`c0f5928130373db371a449db9b6ad0ffb55af41f`

Exact-head checks passed:
- AXIONA Public Surface Guard;
- AXIONA Solutions R121 Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse;
- axe/WCAG.

Exact squash-merge main SHA:
`4600eaabaa1e174cdcc199830c1b97672b913bed`

The GitHub connector returned `statuses=[]` for the merge SHA, so production Pages convergence is not independently proven through this interface.

## R122 — Contact in progress

Targets:
- `contact.html`
- `en/contact.html`
- `de/contact.html`

Starting exact main SHA:
`4600eaabaa1e174cdcc199830c1b97672b913bed`

Feature branch:
`feature/contact-page-r122`

R122 is a first-conversation brief + privacy-minimal mail-preparation sheet. It preserves the existing local `mailto:` flow rather than introducing a form database.

Functional content retained:
- technology-neutral problem description;
- explicit no-separate-form-database explanation;
- four practical starting-point examples;
- support route for existing users;
- direct `hello@axiona.systems` path;
- six structured fields, two required;
- sensitive-data warning;
- `assets/js/contact-intake.js` behavior;
- footer/legal/privacy/security/support and visit counter.

Direct bindings:
- `/assets/contact-r122.css?release=R122`
- `/assets/js/contact-r122.js?release=R122`

Page-specific proof:
- `.github/workflows/axiona-contact-r122-visual-contract.yml`

Post-merge live proof:
- `.github/workflows/axiona-contact-r122-live-proof.yml`

Release document:
- `docs/status/R122_CONTACT_PAGE_REDESIGN.md`

R122 is not accepted until the exact tested PR head passes Public Surface Guard, R122 visual/interaction contract, Browser Quality Audit, Lighthouse and axe/WCAG, then squash-merges with `expected_head_sha`.

## Canonical documentation

Read before subsequent visual releases:
1. `docs/AXIONA_WEB_VISUAL_UX_RULES.md`
2. `docs/AXIONA_VISUAL_RELEASE_CHECKLIST.md`
3. `docs/status/R115_VISUAL_REFERENCE.md`
4. `docs/status/R116_CHANGELOG.md`
5. `docs/status/R118_SYSTEMS_PAGE_REDESIGN.md`
6. `docs/status/R119_PROCESS_PAGE_REDESIGN.md`
7. `docs/status/R120_SECURITY_PAGE_REDESIGN.md`
8. `docs/status/R121_SOLUTIONS_PAGE_REDESIGN.md`
9. `docs/status/R122_CONTACT_PAGE_REDESIGN.md`
10. `docs/r114-cache-proof-note.md`

## Next step after R122

Inventory remaining public surfaces before selecting the next coherent release family. Keeper, Support and privacy/legal utility/detail pages must not be redesigned blindly as one visual class because their information/interaction roles differ.

## Required delivery discipline

Every visual release:
- re-resolve exact `main` SHA;
- create feature branch before every write;
- explicitly target that branch for every write;
- update HU/EN/DE together;
- direct versioned HTML-level asset binding;
- preserve persistent utilities and content depth;
- desktop/mobile rendered evidence and language parity;
- Public Surface Guard + page-specific contract + Browser Quality Audit + Lighthouse + axe/WCAG;
- no gate weakening;
- re-resolve exact PR head and main immediately before merge;
- squash merge using `expected_head_sha`;
- exact production convergence proof only when actual evidence is available.
