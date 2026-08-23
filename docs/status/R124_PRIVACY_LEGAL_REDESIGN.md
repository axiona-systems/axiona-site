# AXIONA Site — R124 Privacy + Legal Redesign

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `4f969b640f21fdc3b0d3f923d2c88e42d4442597`
Feature branch: `feature/privacy-legal-r124`

## Scope

R124 applies one restrained controlled-document visual family to:
- `privacy.html`
- `legal.html`
- `en/privacy.html`
- `en/legal.html`
- `de/privacy.html`
- `de/legal.html`

This release is visual and interaction work only. The existing privacy/legal statements, ordering, update dates, named services, legal framing and claims are preserved. R124 does not perform legal-content revision.

## Visual direction

Both page types use:
- warm paper opening field;
- contained deep-petrol summary frame;
- off-white stable summary rows;
- soft neutral long-form reading field;
- eight off-white document-ledger rows;
- thin borders and solid offset shadows;
- stable informational surfaces with default cursor;
- transform-only repeatable reveal motion with opacity fixed at `1`.

Page distinction:
- Privacy uses restrained cyan as the document/data marker.
- Legal uses restrained orange as the document/legal marker.

Neither page is presented as an application, dashboard, legal-tech console or fake telemetry surface.

## Direct release bindings

All six HTML pages bind directly to:
- `/assets/policy-r124.css?release=R124`
- `/assets/js/policy-r124.js?release=R124`

Release metadata:
- `meta[name="axiona-release"] = R124`

## Content preservation

The following were intentionally not changed by R124:
- privacy/legal paragraph wording;
- order and number of policy sections;
- named third-party services;
- contact addresses;
- legal qualification language;
- update dates;
- canonical/hreflang relationships;
- footer navigation;
- visit-counter binding.

## Verification

Page-specific rendered contract:
- `.github/workflows/axiona-policy-r124-visual-contract.yml`

It verifies all six routes at desktop and mobile sizes, including:
- exact R124 asset binding and release marker;
- one semantic h1;
- one summary with three rows;
- eight policy ledger rows;
- policy-wide notice and metadata block;
- footer preservation;
- no horizontal overflow;
- expected warm-paper/petrol/off-white/soft-neutral surfaces;
- distinct Privacy and Legal wide-note surfaces;
- default cursor and opacity `1` for informational rows;
- no decorative hero background;
- repeatable viewport reveal behavior;
- rendered screenshot evidence.

Repository-wide required checks remain:
- AXIONA Public Surface Guard;
- AXIONA Browser Quality Audit;
- Lighthouse quality budgets;
- axe/WCAG.

## Production proof

Post-merge workflow:
- `.github/workflows/axiona-policy-r124-live-proof.yml`

It is designed to prove exact live HU/EN/DE Privacy/Legal R124 bindings and asset markers for the merge SHA. If the available connector does not expose the push workflow result, production convergence must remain recorded as unproven rather than inferred.
