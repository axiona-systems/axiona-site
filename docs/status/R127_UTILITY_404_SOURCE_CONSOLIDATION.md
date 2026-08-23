# R127 — Utility 404 Source Consolidation

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `25c7ffba4e9790f6b0ee951a682df3e80975a1f6`
Feature branch: `feature/utility-route-consistency-r127`

## Finding

The post-R126 public route inventory found two legacy physical pages:
- `en/404.html`
- `de/404.html`

They were not part of the current AXIONA visual/navigation system. They still used the old dark AXIONA CORE presentation and referenced obsolete routes including `impact.html`, `applications.html`, `automation.html`, `company.html`, `case-study.html` and `practical-tips.html`.

## Decision

Do not create three independently maintained custom 404 pages.

GitHub Pages custom 404 behavior is sourced from the publishing source `404.html`. R126 already provides a single root recovery SSOT with runtime locale selection from `window.location.pathname`.

Therefore R127 removes the two legacy duplicate locale files rather than visually rebuilding them.

## Resulting model

Physical source:
- `404.html` only.

Runtime behavior:
- ordinary missing path → HU fallback;
- `/en/...` missing path → English recovery copy and EN routes;
- `/de/...` missing path → German recovery copy and DE routes;
- `/en/404.html` and `/de/404.html` themselves become real missing paths and fall through to the same root SSOT.

R126 remains the visual/runtime release of the recovery page:
- `/assets/not-found-r126.css?release=R126`
- `/assets/js/not-found-r126.js?release=R126`
- `meta[name=axiona-release]=R126`

R127 is a source-consolidation and route-integrity release; it intentionally does not create a duplicate visual asset version when no visual behavior changes.

## Privacy/security

No new data flow is introduced. Locale selection uses only the current URL path and stores/sends nothing.

## Proof

`.github/workflows/axiona-utility-r127-route-contract.yml`

The contract verifies:
- exactly one physical 404 source remains;
- the obsolete locale files do not exist;
- legacy dead-route references are absent from the remaining 404 source;
- a 404-aware local server returns actual HTTP 404 for locale aliases and arbitrary missing paths;
- `/en/404.html` and `/de/404.html` fall through to the root R126 recovery SSOT;
- HU/EN/DE localization, solutions route, active locale, `noindex,follow`, R126 asset bindings and overflow remain correct.

Post-merge live proof:
- `.github/workflows/axiona-utility-r127-live-proof.yml`

## Acceptance

R127 is accepted only when its exact PR head passes:
- AXIONA Public Surface Guard;
- AXIONA Utility R127 Route Contract;
- AXIONA Browser Quality Audit;
- Lighthouse;
- axe/WCAG;

Then re-resolve exact PR head + `main` and squash merge with `expected_head_sha`.
