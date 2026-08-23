# R126 — Localized 404 Recovery Surface

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `bb19fa77c304b467e8e9aae029a530a4fcb47176`
Feature branch: `feature/not-found-r126`

## Purpose

R126 closes the last concrete visual/release-age gap found in the public-surface inventory: `404.html` was still on release marker R81 and showed Hungarian copy even when the missing URL was under `/en/` or `/de/`.

## Scope

- rebuild `404.html` as a calm AXIONA recovery sheet;
- preserve `noindex,follow` error-page semantics;
- add direct cache-safe R126 CSS/JS binding;
- localize the recovery experience from the requested URL prefix:
  - default/HU;
  - `/en/...` → English;
  - `/de/...` → German;
- keep locale-correct links for main navigation, recovery routes and footer utilities;
- add transform-only repeatable motion with opacity fixed at `1`;
- add a dedicated real-404 browser contract and post-merge live proof.

## Visual model

- warm paper reading field;
- contained deep-petrol recovery sheet;
- restrained orange/cyan routing signals;
- acid only as the compact recovery status marker;
- real links may use pointer/hover affordance;
- no fake telemetry, diagnostics dashboard, scanner, glow or pseudo-controls.

## Direct bindings

- `/assets/not-found-r126.css?release=R126`
- `/assets/js/not-found-r126.js?release=R126`
- `meta[name=axiona-release]=R126`

## Localization behavior

The page remains a single GitHub Pages `404.html`. Client-side code reads only `window.location.pathname`; it sends no data and creates no new storage or tracking. The URL prefix selects HU/EN/DE copy and locale-correct routes.

HU is the fallback for paths without `/en/` or `/de/`.

## Render contract

`.github/workflows/axiona-not-found-r126-visual-contract.yml`

The contract uses a local static server that returns the actual `404.html` with HTTP 404 for unknown routes. It verifies:
- `/missing-r126` → HU;
- `/en/missing-r126` → EN;
- `/de/missing-r126` → DE;
- HTTP status 404;
- release bindings and asset markers;
- one semantic `h1`;
- one recovery sheet;
- three recovery routes;
- locale-correct solutions link and active language indicator;
- `noindex,follow` semantics;
- no horizontal overflow;
- accepted warm-paper/petrol surfaces;
- real-link pointer affordance;
- opacity fixed at `1`;
- desktop and mobile screenshots for all three locales.

## Post-merge proof

`.github/workflows/axiona-not-found-r126-live-proof.yml`

The live proof requests real unknown HU/EN/DE paths, requires HTTP 404, verifies direct R126 HTML bindings and checks the deployed CSS/JS markers. Exact production convergence is accepted only when the proof is actually observable.

## Acceptance

R126 is accepted only when the exact PR head passes:
- AXIONA Public Surface Guard;
- AXIONA Not Found R126 Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse;
- axe/WCAG;

Then re-resolve exact `main` + PR head and squash merge using `expected_head_sha`.
