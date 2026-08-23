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
- restrained repeatable motion with opacity kept WCAG-stable.

## Accepted secondary-page releases

### R118 — System design
Targets: `systems.html`, `en/systems.html`, `de/systems.html`
Exact squash-merge SHA: `9b3027076e0a48efb9ebda20039d8249bc4fe796`

### R119 — Process design
Targets: `process.html`, `en/process.html`, `de/process.html`
Exact squash-merge SHA: `05f55b49d82dbe0349529b3c82f0ca44936fd65a`

### R120 — Security
Targets: `security.html`, `en/security.html`, `de/security.html`
Exact tested PR #71 head: `896edb6731bd9b08d486a1efd0cb609fa2aee400`
Exact squash-merge SHA: `0c5e9c25bf189b24d74415a628aa07abde663dcd`

### R121 — Solutions
Targets: `solutions.html`, `en/solutions.html`, `de/solutions.html`
Exact tested PR #72 head: `c0f5928130373db371a449db9b6ad0ffb55af41f`
Exact squash-merge SHA: `4600eaabaa1e174cdcc199830c1b97672b913bed`

### R122 — Contact
Targets: `contact.html`, `en/contact.html`, `de/contact.html`
Exact tested PR #73 head: `135b003722170f317f4af44a6d0e8de7752e6008`
Exact squash-merge SHA: `fdefa75eb21c7ce277e04db6ce98ff9385f91f6d`

### R123 — Support
Targets: `support.html`, `en/support.html`, `de/support.html`

R123 preserves the four support categories, direct support email, minimum-necessary-data guidance, sensitive-data warning, useful-first-message guidance and support/new-project routing distinction.

Direct bindings:
- `/assets/support-r123.css?release=R123`
- `/assets/js/support-r123.js?release=R123`

Exact tested PR #74 head:
`dfa3e9f1dd88fcac6948b613b5452eef9de6f558`

Final exact-head checks passed:
- AXIONA Public Surface Guard;
- AXIONA Support R123 Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse;
- axe/WCAG.

Exact squash-merge main SHA:
`4f969b640f21fdc3b0d3f923d2c88e42d4442597`

The GitHub connector returned `statuses=[]` for the R123 merge SHA, so production Pages convergence is not independently proven through this interface.

## R124 — Privacy + Legal in progress

Targets:
- `privacy.html`
- `legal.html`
- `en/privacy.html`
- `en/legal.html`
- `de/privacy.html`
- `de/legal.html`

Starting exact main SHA:
`4f969b640f21fdc3b0d3f923d2c88e42d4442597`

Feature branch:
`feature/privacy-legal-r124`

R124 is visual/interaction work only. Existing privacy/legal statements, ordering, dates, named services, qualifications and legal claims are preserved.

Visual model:
- controlled document ledger;
- warm paper opening;
- contained petrol summary sheet;
- soft neutral long-form reading field;
- eight stable off-white policy rows;
- Privacy uses restrained cyan document/data marking;
- Legal uses restrained orange document/legal marking;
- no fake legal-tech dashboard, telemetry or pseudo-controls.

Direct bindings on all six pages:
- `/assets/policy-r124.css?release=R124`
- `/assets/js/policy-r124.js?release=R124`

Page-specific proof:
- `.github/workflows/axiona-policy-r124-visual-contract.yml`

Post-merge live proof:
- `.github/workflows/axiona-policy-r124-live-proof.yml`

Release document:
- `docs/status/R124_PRIVACY_LEGAL_REDESIGN.md`

R124 is not accepted until its exact tested PR head passes Public Surface Guard, R124 Visual Contract, Browser Quality Audit, Lighthouse and axe/WCAG and is squash-merged with `expected_head_sha`.

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
10. `docs/status/R123_SUPPORT_PAGE_REDESIGN.md`
11. `docs/status/R124_PRIVACY_LEGAL_REDESIGN.md`
12. `docs/r114-cache-proof-note.md`

## Next likely surface after R124 acceptance

Inventory the public Keeper product page separately:
- `keeper.html`
- `en/keeper.html`
- `de/keeper.html`

Keeper is an own-product surface and already informs the accepted AXIONA visual language, so it must not be blindly redesigned. First compare its current implementation against the R115–R124 rules and change only genuine inconsistencies or regressions.

## Required delivery discipline

Every visual release:
- re-resolve exact `main` SHA;
- create feature branch before every write;
- explicitly target that branch for every write;
- update HU/EN/DE together;
- direct versioned HTML-level asset binding;
- preserve content depth, navigation and utilities;
- desktop/mobile rendered evidence and language parity;
- Public Surface Guard + page-specific contract + Browser Quality Audit + Lighthouse + axe/WCAG;
- no gate weakening;
- re-resolve exact PR head and main immediately before merge;
- squash merge using `expected_head_sha`;
- exact production convergence proof only when actual evidence is available.
