# AXIONA R143 repository hygiene, hardening and optimization closeout

Date: 2026-08-23

## Result

R143 completed the repository cleanup and replaced the accumulated release-specific CI history with a smaller canonical verification surface.

Primary implementation merge:
- PR: `#87`
- merge commit: `a00b43f5fbe8c6bcedf196afc47bbfbeafde85b1`
- merge method: squash
- GitHub signature: verified

## Before → after

| Area | Before R143 | After R143 |
| --- | ---: | ---: |
| GitHub Actions workflows | 40 | 4 |
| Release-numbered historical workflows | 36 | 0 |
| Public HTML files | 31 | 31 |
| R135/R136 stale UX override files | 2 | 0 |
| R105/R108 motion compatibility shims | 2 | 0 |
| Canonical repository-policy guards | fragmented | consolidated |

The two PWA icon files originally reported as possible orphan candidates were retained because `site.webmanifest` references them. They were not dead assets.

## Canonical workflows

Only these workflows remain under `.github/workflows/`:

1. `axiona-repo-guard.yml`
   - public-source invariants
   - sitemap / hreflang
   - RFC 9116 `security.txt`
   - social metadata
   - retired routes
   - browser identity metadata
   - runtime asset graph
   - Actions hardening
   - whitespace check

2. `axiona-browser-audit.yml`
   - Lighthouse quality budgets
   - axe WCAG audit
   - pinned browser-audit dependencies

3. `axiona-render-contract.yml`
   - current route/render contract
   - desktop/mobile overflow checks
   - canonical R137/R142 bindings
   - navigation state
   - Systems geometry
   - bidirectional motion behavior

4. `axiona-pages-rebuild.yml`
   - exact-main GitHub Pages rebuild
   - exact build commit verification
   - live canonical route verification
   - live `security.txt` verification

## Cleanup completed

Removed:
- stale `assets/r135-ux-fixes.css`
- stale `assets/r136-ux-fixes.css`
- superseded `assets/motion-r105.css`
- superseded `assets/motion-r108.css`
- old release-specific visual/live-proof workflows
- obsolete R140 diagnostic text
- transient candidate validation proof log
- accidental `candidate` gitlink left by a temporary validation checkout

Dependency-chain cleanup:
- `assets/multipage-r78.css` no longer references the missing `multipage-r74.css` entrypoint;
- multipage/perspective layers bind their required R109 compatibility layer directly;
- `assets/js/share-r86.js` no longer injects the obsolete R108 stylesheet at runtime;
- browser audit uses `axe-core@4.13.0`;
- npm audit-tool installation continues to use `--ignore-scripts --no-audit --no-fund`.

## Hardening added

`verify_asset_references.py` now fails closed on missing local runtime asset references.

`verify_workflow_hardening.py` now enforces the current Actions policy, including:
- immutable 40-character action SHA pins;
- explicit workflow permissions;
- least-privilege validation permissions;
- checkout credential persistence disabled where credentials are not required.

The canonical verification workflows passed on exact candidate head `8b336e334b2bc844b293c72150b16374e78af3ef` before merge:
- Public Surface Guard: PASS
- Render Contract: PASS
- Browser Quality Audit: PASS
- Lighthouse 12-route matrix: PASS
- axe WCAG audit: PASS

## Motion conflict found and corrected

The repository review found a real layering conflict between the accepted R115 overview stylesheet and the current R142 motion coordinator.

R115 still contained a historical 18 px `!important` transform for overview story steps. R142 specified the current 7 px desktop / 5 px mobile movement, but the older higher-specificity rule could still win for those elements.

R142 is now explicitly authoritative for the affected overview reveal states while preserving the accepted R115 visual composition. The current tuning remains:
- desktop: 7 px / 900 ms
- mobile: 5 px / 760 ms
- reduced-motion: transform and transition disabled

The corrected state passed the full render contract before merge.

## Public runtime check

After merge, the public AXIONA routes remained reachable, including the overview, Systems, Process, Security, Solutions and Contact surfaces. The canonical Pages workflow itself also contains exact-main build matching and live-route convergence checks so future publication is not treated as successful merely because a push completed.

## Remaining repository-setting hardening

One item is outside the repository source itself:

**GitHub `main` branch protection is currently disabled.**

The source-level guards are in place, but the repository should additionally use GitHub branch protection / rulesets so `main` cannot be changed without the intended PR/check policy. The currently available GitHub connection does not expose a branch-protection write action, so R143 does not silently simulate this protection in source code.

## Final assessment

R143 repository state: **CLEAN / HARDENED / CANONICAL CI CONSOLIDATED**

No public-content redesign was introduced by this cleanup. R137 layout/navigation behavior and the intended R142 motion tuning remain the accepted public baseline.
