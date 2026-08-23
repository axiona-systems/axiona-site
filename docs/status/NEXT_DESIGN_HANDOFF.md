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

## Accepted public-surface releases

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
Exact tested PR #75 head: `b01ff884e25ca9ef42f1f1db4a365652d1554fb5`
Exact squash-merge SHA: `678fbf152a9b6356f92740f5df8149cb91724663`
Final exact-head checks passed: Guard, Policy Visual Contract, Browser Quality Audit, Lighthouse, axe/WCAG.

### R125 — Keeper alignment + hardening
Exact tested PR #76 head: `e727c60f745e635685707502b1b5eeb15bc054f9`
Exact squash-merge SHA: `bb19fa77c304b467e8e9aae029a530a4fcb47176`
Final exact-head checks passed: Guard, Keeper Visual Contract, Browser Quality Audit, Lighthouse, axe/WCAG.

### R126 — Localized 404 recovery
Exact tested PR #77 head: `f0aa422bab5a9fe9dd3a3d2fcb649710dccb7ebf`
Exact squash-merge SHA: `25c7ffba4e9790f6b0ee951a682df3e80975a1f6`
Final exact-head checks passed: Guard, Not Found Visual Contract, Browser Quality Audit, Lighthouse, axe/WCAG.

Root `404.html` is the visual/runtime SSOT:
- `/assets/not-found-r126.css?release=R126`
- `/assets/js/not-found-r126.js?release=R126`
- HU fallback, `/en/...` English, `/de/...` German;
- `noindex,follow`;
- no new tracking/storage/data flow.

### R127 — Utility 404 source consolidation
Exact tested PR #78 head: `4a99777d3421d1287e3b499f5c33958583a58ea0`
Exact squash-merge main SHA: `7f0ead903aefd203a5fefb1b51c7f674ebb12c5d`
Final exact-head checks passed: Public Surface Guard, Utility R127 Route Contract, Browser Quality Audit, Lighthouse, axe/WCAG.

### R128 — Public Surface Invariants
Exact tested PR #79 head: `0515993c441547cfe3f9a2c615fc618792d3f1a5`
Exact squash-merge main SHA: `ad55f09f97ab27d85623d8fda1c7b59af3b4dd64`

R128 enforces exact physical HTML inventory, matching `<html lang>`, canonical + HU/EN/DE/x-default hreflang, release-family parity, direct current release binding, same-host reference integrity, root R126 404 invariants, sitemap URL membership, robots/security.txt existence and repository secret/public-email checks. The stronger Guard exposed and remediated a real metadata defect across 12 Systems/Process/Security/Solutions localized pages.

Final exact-head checks passed: Public Surface Guard, R128 Contract, Systems/Process/Security/Solutions visual contracts, Browser Quality Audit, Lighthouse, axe/WCAG.

### R129 — Browser Audit Coverage Matrix
Exact tested PR #80 head: `bd354caac78ede77acce718043fdd1315811b55c`
Exact squash-merge main SHA: `b97e2120254d910c5f1591e7b0abd1b9044baf1d`

Accepted browser matrix:
- Lighthouse: 12 representative routes — all 10 HU page families + EN home + DE home;
- `numberOfRuns=1` remains cost-controlled;
- axe/WCAG: exhaustive 30 active HU/EN/DE routes;
- `scripts/verify_browser_audit_matrix.py` fails fast before browser setup if either matrix drifts;
- `.github/workflows/axiona-browser-r129-coverage-contract.yml` proves missing Lighthouse or axe coverage fails closed.

Final exact-head checks passed: Public Surface Guard, Browser R129 Coverage Contract, Browser Quality Audit, 12-route Lighthouse budgets, 30-route axe/WCAG.

### R130 — Sitemap Hreflang Invariants
Exact tested PR #81 head: `e1dc295be713e24febbfa57235e238b0a34a0282`
Exact squash-merge main SHA: `cfa47f55b3b1f3c76f740cfe61ff4001c6d3c60b`

R130 enforces:
- exactly 30 declared sitemap URL entries;
- one `<loc>` per entry with no duplicate locations;
- exactly four alternates per entry: `hu`, `en`, `de`, `x-default`;
- no duplicate hreflang keys;
- exact route-family targets with `x-default` bound to HU;
- focused negative contract for target drift and duplicate hreflang.

Final exact-head checks passed:
- AXIONA Public Surface Guard — SUCCESS;
- AXIONA Sitemap R130 Invariants Contract — SUCCESS.

No browser-visible source changed in R130.

## R131 — RFC 9116 security.txt invariants in progress

Starting exact main SHA:
`cfa47f55b3b1f3c76f740cfe61ff4001c6d3c60b`

Feature branch:
`feature/security-txt-invariants-r131`

Audit finding:
- `.well-known/security.txt` exists and its current values are sound;
- the central Guard previously checked only file existence;
- malformed, stale or semantically broken vulnerability-disclosure metadata could therefore pass CI.

R131 adds:
- `scripts/verify_security_txt.py`;
- UTF-8/size/basic field-format validation;
- required valid Contact URI;
- exactly one RFC3339 Expires, future-dated and no more than 366 days ahead under AXIONA policy;
- exact HTTPS Canonical and Security Policy URLs;
- exact HU/EN/DE Preferred-Languages set;
- Public Surface Guard binding;
- `.github/workflows/axiona-security-txt-r131-contract.yml` negative proof;
- `.github/workflows/axiona-security-txt-r131-live-proof.yml` live HTTPS + `text/plain` + body verification.

Release document:
- `docs/status/R131_SECURITY_TXT_INVARIANTS.md`

No public page UI changes. R131 is not accepted until the exact PR head passes Public Surface Guard and Security.txt R131 Invariants Contract and is squash-merged with `expected_head_sha`.

## Canonical documentation

Read before subsequent public-surface changes:
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
15. `docs/status/R128_PUBLIC_SURFACE_INVARIANTS.md`
16. `docs/status/R129_BROWSER_AUDIT_MATRIX.md`
17. `docs/status/R130_SITEMAP_HREFLANG_INVARIANTS.md`
18. `docs/status/R131_SECURITY_TXT_INVARIANTS.md`
19. `docs/r114-cache-proof-note.md`

## Next step after R131 acceptance

Continue whole-site consistency/regression audit. Highest-value remaining areas:
- navigation/footer semantic parity;
- social/Open Graph/Twitter metadata consistency;
- webmanifest/favicon/static metadata consistency;
- stale unused assets/workflows only when removal can be proven safe;
- deployment/live-proof observability.

Create another release only for a concrete finding. If no meaningful public inconsistency remains, keep the accepted UI stable and rely on regression-hardening contracts.

## Required delivery discipline

For every public-surface or public-quality change:
- re-resolve exact `main` SHA;
- create feature branch before every write;
- explicitly target that branch for every write;
- preserve accepted content and UX unless the task requires otherwise;
- update languages together where applicable;
- run Public Surface Guard + the relevant focused contract;
- run Browser Quality Audit/Lighthouse/axe only when browser-visible source is affected or a browser-quality contract changes;
- no gate weakening;
- re-resolve exact PR head and main immediately before merge;
- squash merge using `expected_head_sha`;
- exact production convergence proof only when actual evidence is available.
