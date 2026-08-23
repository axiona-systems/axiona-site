# R129 — Browser Audit Coverage Matrix

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `ad55f09f97ab27d85623d8fda1c7b59af3b4dd64`
Feature branch: `feature/browser-audit-matrix-r129`

## Why this release exists

The whole-site regression audit found a coverage asymmetry in the shared Browser Quality Audit:

- axe/WCAG already audits all 30 active HU/EN/DE public pages;
- Lighthouse audited only 7 Hungarian routes;
- Hungarian Support, Privacy and Legal were not in Lighthouse;
- no EN or DE route was represented in Lighthouse.

R129 closes that gap without multiplying Lighthouse cost to all 30 pages.

## Coverage model

### Lighthouse — 12 representative routes

The Lighthouse matrix now covers:

1. `/`
2. `/systems.html`
3. `/process.html`
4. `/security.html`
5. `/solutions.html`
6. `/keeper.html`
7. `/contact.html`
8. `/support.html`
9. `/privacy.html`
10. `/legal.html`
11. `/en/`
12. `/de/`

This gives every public page family one full Lighthouse representative while also exercising the English and German localized shell. `numberOfRuns` remains `1` to keep Actions/runtime cost controlled.

### axe/WCAG — 30 active routes

The existing axe matrix remains the exhaustive accessibility tier:
- 10 HU routes;
- 10 EN routes;
- 10 DE routes.

The localized secondary pages share the same structural page families and are still audited individually by axe, while R128 statically enforces canonical/hreflang/release parity across languages.

## Fail-fast matrix verifier

New script:

`scripts/verify_browser_audit_matrix.py`

It verifies:
- exact Lighthouse representative route list and ordering;
- only localhost audit origins, with no query/fragment drift;
- no duplicate Lighthouse route;
- exact 30-route axe matrix;
- no duplicate/missing axe route;
- all ten public route families remain represented in Lighthouse.

The normal Browser Quality Audit runs this verifier before npm installation or Chrome work so coverage drift fails cheaply.

## Negative coverage contract

Workflow:

`.github/workflows/axiona-browser-r129-coverage-contract.yml`

The contract first requires the real repository baseline to pass, then proves fail-closed behavior with two isolated mutations:

1. remove `/legal.html` from Lighthouse → verifier must fail with `Lighthouse coverage mismatch`;
2. remove `/de/legal.html` from axe → verifier must fail with `axe coverage mismatch`.

## Scope boundary

R129 changes engineering verification coverage only. It does not alter public HTML, CSS, JavaScript, content, tracking, routing or production behavior.

## Acceptance

The exact R129 PR head must pass:
- AXIONA Public Surface Guard;
- AXIONA Browser R129 Coverage Contract;
- AXIONA Browser Quality Audit;
- Lighthouse budgets on the 12-route representative matrix;
- axe/WCAG on all 30 active routes.

Then re-resolve exact `main` + PR head and squash merge with `expected_head_sha`.
