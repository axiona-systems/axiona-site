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
R125 preserved the accepted Keeper composition and product copy and added cache-safe bindings, affordance/palette alignment, transform-only motion and a dedicated current Keeper render contract.

Direct bindings:
- `/assets/keeper-r125.css?release=R125`
- `/assets/js/keeper-r125.js?release=R125`

Exact tested PR #76 head: `e727c60f745e635685707502b1b5eeb15bc054f9`
Exact squash-merge main SHA: `bb19fa77c304b467e8e9aae029a530a4fcb47176`
Final exact-head checks passed: Guard, Keeper Visual Contract, Browser Quality Audit, Lighthouse, axe/WCAG.
Production Pages convergence was not independently observable through the connector (`statuses=[]`).

### R126 — Localized 404 recovery
Target: root `404.html`.

R126 replaced the stale R81 utility surface with a single localized recovery SSOT:
- HU fallback;
- `/en/...` → English;
- `/de/...` → German;
- locale-correct navigation/recovery/footer routes;
- `noindex,follow` preserved;
- no storage/tracking/new data flow.

Direct bindings:
- `/assets/not-found-r126.css?release=R126`
- `/assets/js/not-found-r126.js?release=R126`

Exact tested PR #77 head: `f0aa422bab5a9fe9dd3a3d2fcb649710dccb7ebf`
Exact squash-merge main SHA: `25c7ffba4e9790f6b0ee951a682df3e80975a1f6`
Final exact-head checks passed: Guard, Not Found R126 Visual Contract, Browser Quality Audit, Lighthouse, axe/WCAG.
Production Pages convergence was not independently observable through the connector (`statuses=[]`).

## R127 — Utility 404 source consolidation in progress

Starting exact main SHA:
`25c7ffba4e9790f6b0ee951a682df3e80975a1f6`

Feature branch:
`feature/utility-route-consistency-r127`

Post-R126 route inventory found two legacy physical duplicate pages:
- `en/404.html`
- `de/404.html`

Those files still used the obsolete dark AXIONA CORE-era UI and stale routes such as `impact.html`, `applications.html`, `automation.html`, `company.html`, `case-study.html` and `practical-tips.html`.

R127 decision:
- delete the two duplicate locale 404 files;
- keep root `404.html` as the only physical custom-404 SSOT;
- let `/en/404.html`, `/de/404.html` and arbitrary missing EN/DE paths fall through as real HTTP 404 responses to the root R126 recovery implementation;
- do not create a redundant R127 visual asset copy because no recovery UI behavior changes.

R126 remains the visual/runtime binding:
- `/assets/not-found-r126.css?release=R126`
- `/assets/js/not-found-r126.js?release=R126`

Page/route proof:
- `.github/workflows/axiona-utility-r127-route-contract.yml`

Post-merge live proof:
- `.github/workflows/axiona-utility-r127-live-proof.yml`

Release document:
- `docs/status/R127_UTILITY_404_SOURCE_CONSOLIDATION.md`

R127 is not accepted until the exact PR head passes Public Surface Guard, R127 Route Contract, Browser Quality Audit, Lighthouse and axe/WCAG and is squash-merged with `expected_head_sha`.

## Canonical documentation

Read before subsequent visual/utility releases:
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
14. `docs/status/R127_UTILITY_404_SOURCE_CONSOLIDATION.md`
15. `docs/r114-cache-proof-note.md`

## Next step after R127 acceptance

Continue the whole-site consistency/regression audit rather than redesigning accepted pages. Audit:
- HU/EN/DE file parity;
- canonical/hreflang parity;
- current navigation/footer route integrity;
- release-binding consistency;
- stale public files and dead internal links;
- utility/static public surfaces.

Create another release only for a concrete finding. If no meaningful public inconsistency remains, stop the redesign sequence and keep the site under regression-hardening contracts.

## Required delivery discipline

For every public-surface change:
- re-resolve exact `main` SHA;
- create feature branch before every write;
- explicitly target that branch for every write;
- update languages together where applicable;
- preserve accepted content and UX unless the task requires otherwise;
- desktop/mobile rendered evidence where UI is affected;
- Public Surface Guard + relevant page/route contract + Browser Quality Audit + Lighthouse + axe/WCAG;
- no gate weakening;
- re-resolve exact PR head and main immediately before merge;
- squash merge using `expected_head_sha`;
- exact production convergence proof only when actual evidence is available.
