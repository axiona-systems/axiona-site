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
Exact squash-merge SHA: `9b3027076e0a48efb9ebda20039d8249bc4fe796`

### R119 — Process design
Exact squash-merge SHA: `05f55b49d82dbe0349529b3c82f0ca44936fd65a`

### R120 — Security
Exact tested PR #71 head: `896edb6731bd9b08d486a1efd0cb609fa2aee400`
Exact squash-merge SHA: `0c5e9c25bf189b24d74415a628aa07abde663dcd`

### R121 — Solutions
Exact tested PR #72 head: `c0f5928130373db371a449db9b6ad0ffb55af41f`
Exact squash-merge SHA: `4600eaabaa1e174cdcc199830c1b97672b913bed`

### R122 — Contact
Exact tested PR #73 head: `135b003722170f317f4af44a6d0e8de7752e6008`
Exact squash-merge SHA: `fdefa75eb21c7ce277e04db6ce98ff9385f91f6d`

### R123 — Support
Exact tested PR #74 head: `dfa3e9f1dd88fcac6948b613b5452eef9de6f558`
Exact squash-merge SHA: `4f969b640f21fdc3b0d3f923d2c88e42d4442597`

### R124 — Privacy + Legal
Targets: `privacy.html`, `legal.html`, and EN/DE equivalents.
Exact tested PR #75 head: `b01ff884e25ca9ef42f1f1db4a365652d1554fb5`
Exact squash-merge SHA: `678fbf152a9b6356f92740f5df8149cb91724663`
Final exact-head checks passed: Guard, Policy Visual Contract, Browser Quality Audit, Lighthouse, axe/WCAG.
Production Pages convergence was not independently observable through the connector (`statuses=[]`).

### R125 — Keeper alignment + hardening
Targets: `keeper.html`, `en/keeper.html`, `de/keeper.html`.
R125 intentionally preserved the accepted Keeper composition and product copy; it added cache-safe current bindings, affordance/palette alignment, transform-only motion and a dedicated current Keeper render contract.

Direct bindings:
- `/assets/keeper-r125.css?release=R125`
- `/assets/js/keeper-r125.js?release=R125`

Exact tested PR #76 head:
`e727c60f745e635685707502b1b5eeb15bc054f9`

Final exact-head checks passed:
- AXIONA Public Surface Guard;
- AXIONA Keeper R125 Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse;
- axe/WCAG.

Exact squash-merge main SHA:
`bb19fa77c304b467e8e9aae029a530a4fcb47176`

Production Pages convergence was not independently observable through the connector (`statuses=[]`).

## R126 — Localized 404 recovery in progress

Target:
- `404.html`

Starting exact main SHA:
`bb19fa77c304b467e8e9aae029a530a4fcb47176`

Feature branch:
`feature/not-found-r126`

Reason for release:
- the public 404 surface was still marked R81;
- EN/DE missing URLs received Hungarian error copy;
- the utility surface had no current exact render contract or cache-safe release binding.

R126 behavior:
- one GitHub Pages `404.html` remains the source;
- requested URL prefix selects HU/EN/DE client-side copy;
- HU is the fallback;
- navigation, recovery actions and footer routes remain locale-correct;
- URL-path locale selection creates no storage, tracking or new data flow;
- `noindex,follow` remains intact.

Visual model:
- warm paper recovery field;
- contained deep-petrol recovery sheet;
- restrained orange/cyan accents;
- acid only as compact recovery status;
- only real links receive interactive affordance;
- no fake diagnostics/telemetry UI.

Direct bindings:
- `/assets/not-found-r126.css?release=R126`
- `/assets/js/not-found-r126.js?release=R126`

Page-specific proof:
- `.github/workflows/axiona-not-found-r126-visual-contract.yml`

Post-merge live proof:
- `.github/workflows/axiona-not-found-r126-live-proof.yml`

Release document:
- `docs/status/R126_NOT_FOUND_RECOVERY.md`

R126 is not accepted until its exact tested PR head passes Public Surface Guard, R126 Visual Contract, Browser Quality Audit, Lighthouse and axe/WCAG and is squash-merged with `expected_head_sha`.

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
12. `docs/status/R125_KEEPER_ALIGNMENT.md`
13. `docs/status/R126_NOT_FOUND_RECOVERY.md`
14. `docs/r114-cache-proof-note.md`

## Next step after R126 acceptance

Do not start another redesign by release number alone. Re-inventory the public tree and distinguish:
- already accepted current surfaces;
- redirects/static machine files that do not need visual work;
- any genuinely stale or unproved public UI.

If no meaningful public visual gap remains, switch from redesign releases to a whole-site consistency/regression audit instead of changing accepted pages unnecessarily.

## Required delivery discipline

Every visual release:
- re-resolve exact `main` SHA;
- create feature branch before every write;
- explicitly target that branch for every write;
- update languages together where applicable;
- direct versioned HTML-level asset binding;
- preserve content depth, navigation and utilities;
- desktop/mobile rendered evidence and language parity;
- Public Surface Guard + page-specific contract + Browser Quality Audit + Lighthouse + axe/WCAG;
- no gate weakening;
- re-resolve exact PR head and main immediately before merge;
- squash merge using `expected_head_sha`;
- exact production convergence proof only when actual evidence is available.
