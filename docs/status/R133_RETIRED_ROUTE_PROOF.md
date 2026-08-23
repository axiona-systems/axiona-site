# R133 — Retired Route Production Proof

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `62ef0fb2cd25b518695f6938d506e362c9564a82`
Feature branch: `feature/retired-route-live-proof-r133`

## Finding

R127 removed obsolete locale 404 files and proved generic missing routes fall through to the root R126 recovery SSOT. Its production proof did not, however, name the historical routes that the stale pages used to advertise.

The repository history identifies six retired route basenames:
- `impact.html`
- `applications.html`
- `automation.html`
- `company.html`
- `case-study.html`
- `practical-tips.html`

Because the stale locale 404 pages used relative links, R133 treats all HU/root, EN and DE variants as retired. It also retains `/en/404.html` and `/de/404.html` in the retired set.

Total retired registry: 20 routes.

## Source contract

`scripts/verify_retired_routes.py` is the single registry and source verifier.

It fails if any retired route:
- exists again as a physical repository path;
- appears as a sitemap `<loc>`;
- is linked by an active HTML page.

The script also exposes `--print-routes` so the live proof consumes the same registry instead of duplicating the route list.

The verifier is bound into AXIONA Public Surface Guard.

## Negative contract

`.github/workflows/axiona-retired-routes-r133-contract.yml`

It proves fail-closed behavior for:
1. resurrected physical `/impact.html`;
2. active link to `/en/automation.html`;
3. sitemap reintroduction of `/de/company.html`.

## Production proof

`.github/workflows/axiona-retired-routes-r133-live-proof.yml`

On relevant main pushes it fetches all 20 named retired routes and requires:
- real HTTP 404 status;
- root R126 recovery CSS binding;
- root R126 recovery JS binding;
- `axiona-release=R126` recovery marker.

The workflow retries briefly to accommodate Pages deployment convergence and emits the exact source SHA only after every named retired route passes.

## Scope boundary

R133 changes no public HTML/CSS/JS content or route implementation. It adds source prevention + production observability for routes that are already retired.

## Acceptance

The final exact R133 PR head must pass:
- AXIONA Public Surface Guard;
- AXIONA Retired Routes R133 Contract;
- existing static invariant contracts triggered by Guard changes.

No Browser Quality Audit/Lighthouse/axe run is required unless an independently browser-visible source changes.

Then re-resolve exact `main` + PR head and squash merge with `expected_head_sha`.
