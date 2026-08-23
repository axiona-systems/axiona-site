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
Root `404.html` remains the visual/runtime 404 SSOT with R126 bindings, HU fallback, `/en/...` English, `/de/...` German and `noindex,follow`.

### R127 — Utility 404 source consolidation
Exact tested PR #78 head: `4a99777d3421d1287e3b499f5c33958583a58ea0`
Exact squash-merge main SHA: `7f0ead903aefd203a5fefb1b51c7f674ebb12c5d`
Final exact-head checks passed: Public Surface Guard, Utility R127 Route Contract, Browser Quality Audit, Lighthouse, axe/WCAG.

### R128 — Public Surface Invariants
Exact tested PR #79 head: `0515993c441547cfe3f9a2c615fc618792d3f1a5`
Exact squash-merge main SHA: `ad55f09f97ab27d85623d8fda1c7b59af3b4dd64`
R128 enforces exact physical HTML inventory, `<html lang>`, canonical + HU/EN/DE/x-default hreflang, release-family parity, direct current release binding, same-host reference integrity, root R126 404 invariants, sitemap URL membership, robots/security.txt existence and repository secret/public-email checks. The stronger Guard exposed and remediated a real metadata defect across 12 Systems/Process/Security/Solutions localized pages.
Final exact-head checks passed: Public Surface Guard, R128 Contract, Systems/Process/Security/Solutions visual contracts, Browser Quality Audit, Lighthouse, axe/WCAG.

### R129 — Browser Audit Coverage Matrix
Exact tested PR #80 head: `bd354caac78ede77acce718043fdd1315811b55c`
Exact squash-merge main SHA: `b97e2120254d910c5f1591e7b0abd1b9044baf1d`
Accepted browser matrix: Lighthouse on all 10 HU families + EN home + DE home; axe/WCAG on all 30 active routes; fail-closed matrix verifier and negative contract.
Final exact-head checks passed: Public Surface Guard, Browser R129 Coverage Contract, Browser Quality Audit, Lighthouse, axe/WCAG.

### R130 — Sitemap Hreflang Invariants
Exact tested PR #81 head: `e1dc295be713e24febbfa57235e238b0a34a0282`
Exact squash-merge main SHA: `cfa47f55b3b1f3c76f740cfe61ff4001c6d3c60b`
R130 enforces exactly 30 sitemap URL entries, unique locs, exactly four alternates (`hu`, `en`, `de`, `x-default`), no duplicate hreflang keys, exact route-family targets and HU x-default.
Final exact-head checks passed: Public Surface Guard and Sitemap R130 Invariants Contract.

### R131 — RFC 9116 security.txt invariants
Exact tested PR #83 head: `2a1b8ae079708f6f162b37e153543b7de4fc77a0`
Exact squash-merge main SHA: `e2550e2f1ad3f7e59588f0a65227d9b5156f8537`
R131 validates UTF-8/size/field format, valid Contact, exactly one future RFC3339 Expires within 366 days, exact HTTPS Canonical/Policy, exact HU/EN/DE Preferred-Languages, and adds source + live proof contracts.
Final exact-head checks passed: Public Surface Guard, Security.txt R131 Invariants Contract, Sitemap R130 Contract.
Production push-run convergence was not independently visible through the connector.

### R132 — Social Metadata Invariants
Exact tested PR #84 head: `def53da157efbfd77b12a560a241c2ed7db512d9`
Exact squash-merge main SHA: `62ef0fb2cd25b518695f6938d506e362c9564a82`
R132 repaired a real 9-page social metadata defect across Support and Privacy/Legal HU/EN/DE by restoring core Open Graph/Twitter title/description/type/url/card fields while preserving existing page copy, canonical URLs and language-specific R92 images.
Whole-site hardening: `scripts/verify_social_metadata.py` validates all 30 active pages, exact OG/Twitter core metadata and same-page URL identity, language-correct general/Keeper R92 preview images and actual six social PNG assets at 1200×630.
Final exact-head checks passed: Public Surface Guard, Social Metadata R132 Invariants Contract, Support R123 Visual Contract, Policy R124 Visual Contract, Sitemap R130 Contract, Security.txt R131 Contract, Browser Quality Audit, Lighthouse, axe/WCAG.
Production push-run convergence must not be claimed without actual push-run evidence.

### R133 — Retired Route Production Proof
Exact tested PR #85 head: `f1faf489a6cfb3c84ec3f721b6c41392d19a34e1`
Exact squash-merge main SHA: `9d5ecb2c823621b29787e4f5aec9b9afa4634473`
R133 establishes one 20-route retirement registry covering six historical basenames across root/HU, EN and DE plus the retired `/en/404.html` and `/de/404.html` aliases. Source resurrection, sitemap reintroduction and active HTML links now fail closed; the post-merge live workflow requires every named retired route to return real HTTP 404 with the R126 recovery bindings.
Final exact-head checks passed: Public Surface Guard, Retired Routes R133 Contract, Sitemap R130 Contract, Security.txt R131 Contract and Social Metadata R132 Contract.
Production push-run convergence must not be claimed without actual push-run evidence.

## R134 — Browser Identity Invariants in progress

Starting exact main SHA:
`9d5ecb2c823621b29787e4f5aec9b9afa4634473`

Feature branch:
`feature/browser-identity-r134`

PR:
`#86`

Audit findings:
- `site.webmanifest` existed but active pages did not bind it;
- `apple-touch-icon.png` existed but active pages did not bind it;
- `favicon.svg` existed but active pages did not use it as the scalable icon;
- legacy `shortcut icon` relations remained;
- the manifest declared `assets/brand/axiona-icon-512.png` as 512×512 while the physical PNG was 512×474.

R134 remediation:
- all 30 active HU/EN/DE pages plus root `404.html` now bind exactly SVG favicon, 32×32 PNG fallback, 16×16 PNG fallback, 180×180 Apple touch icon and `/site.webmanifest`;
- legacy `shortcut icon` bindings are removed;
- the 512×474 manifest icon is centered without stretching on a transparent 512×512 canvas;
- `scripts/verify_browser_identity.py` validates all 31 HTML pages, physical icon dimensions and exact manifest identity/icon fields;
- Public Surface Guard calls the new verifier;
- `.github/workflows/axiona-browser-identity-r134-contract.yml` proves key regressions fail closed;
- `.github/workflows/axiona-browser-identity-r134-live-proof.yml` checks all 30 live active routes, a real 404, live manifest and live 192/512 icon dimensions.

The branch-local remediation workflow successfully validated Public Surface + Social Metadata + Browser Identity, committed the HTML/icon remediation, and removed itself. It must remain absent from the final PR diff.

Release document:
- `docs/status/R134_BROWSER_IDENTITY_INVARIANTS.md`

R134 is not accepted until its final exact PR head passes Public Surface Guard, Browser Identity R134 Contract, all existing triggered visual/invariant checks and Browser Quality Audit/Lighthouse/axe, then is squash-merged with `expected_head_sha` after re-resolving PR head and `main`.

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
19. `docs/status/R132_SOCIAL_METADATA_INVARIANTS.md`
20. `docs/status/R133_RETIRED_ROUTE_PROOF.md`
21. `docs/status/R134_BROWSER_IDENTITY_INVARIANTS.md`
22. `docs/r114-cache-proof-note.md`

## Next step after R134 acceptance

Continue whole-site consistency/regression audit only for concrete findings. Highest-value remaining areas:
- navigation/footer semantic parity;
- stale unused assets/workflows only when removal can be proven safe;
- deployment/live-proof observability.

Do not redesign accepted pages without a real finding.

## Required delivery discipline

For every public-surface or public-quality change:
- re-resolve exact `main` SHA;
- create feature branch before every write;
- explicitly target that branch for every write;
- preserve accepted content and UX unless the task requires otherwise;
- update languages together where applicable;
- run Public Surface Guard + the relevant focused contract;
- run Browser Quality Audit/Lighthouse/axe when browser-visible source is affected or a browser-quality contract changes;
- no gate weakening;
- re-resolve exact PR head and main immediately before merge;
- squash merge using `expected_head_sha`;
- exact production convergence proof only when actual evidence is available.
