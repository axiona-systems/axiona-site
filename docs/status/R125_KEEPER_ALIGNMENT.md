# AXIONA Site — R125 Keeper Alignment + Hardening

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `678fbf152a9b6356f92740f5df8149cb91724663`
Feature branch: `feature/keeper-page-r125`

## Why this is not a full redesign

The Keeper public page already defines much of the accepted AXIONA visual grammar used by later R115–R124 work: warm outer fields, off-white work surfaces, contained deep-petrol control areas, small status accents and product/workflow-oriented presentation.

R125 therefore does not replace the Keeper composition or rewrite its product story. It is an alignment and hardening release.

## Preserved product substance

R125 preserves the existing HU/EN/DE Keeper wording and structure, including:
- in-development product status;
- planned-experience wording on the hero workcard;
- five-step incoming-document workcard;
- four core questions;
- six processing steps;
- five basic-storage-vs-Keeper comparison rows;
- four practical document examples;
- four trust/control principles;
- first-target-platform development status;
- Share + Copy link + fallback sharing;
- footer/legal/support links and visit counter.

No product capability claim was strengthened or rewritten by R125.

## Actual fixes

### Cache-safe direct release binding

The Keeper page previously reported release R98 while its Keeper stylesheets were older unversioned assets. R125 adds a current direct HTML-level release layer in all three languages:
- `/assets/keeper-r125.css?release=R125`
- `/assets/js/keeper-r125.js?release=R125`
- `meta[name="axiona-release"] = R125`

This follows the cache-safety rule established after R113/R114.

### Current visual-token alignment

R125 scopes the accepted current palette onto the existing Keeper composition:
- warm paper `#f1eee6`;
- off-white work surfaces;
- soft-neutral information fields;
- deep petrol controlled surfaces;
- restrained orange;
- acid only for compact status/control cues;
- cyan as secondary accent.

The existing layout remains intact.

### R116 affordance alignment

Informational Keeper rows/cards explicitly remain default-cursor stable surfaces. They do not gain action arrows, hover shifts or pseudo-button behavior.

### Motion hardening

R125 adds repeatable progressive-enhancement viewport reveal motion using transform only. Text opacity remains `1` in all states, and `prefers-reduced-motion` disables transforms.

The old decorative grid is also suppressed if the legacy matter-preview component is present.

## Verification

Page-specific rendered contract:
- `.github/workflows/axiona-keeper-r125-visual-contract.yml`

It verifies HU/EN/DE on desktop and mobile, including:
- direct R125 CSS/JS binding and release metadata;
- one semantic h1;
- 1 hero workcard / 5 work rows;
- 4 core questions;
- 6 processing steps;
- 5 comparison rows;
- 4 examples;
- 4 trust cards;
- development status;
- share/footer preservation;
- product status and planned-experience text remain present;
- no horizontal overflow;
- expected accepted AXIONA surface colors;
- default cursor and opacity `1` for informational surfaces;
- repeatable reveal behavior;
- full-page and focused screenshot evidence.

Repository-wide required checks remain:
- AXIONA Public Surface Guard;
- AXIONA Browser Quality Audit;
- Lighthouse quality budgets;
- axe/WCAG.

## Production proof

Post-merge workflow:
- `.github/workflows/axiona-keeper-r125-live-proof.yml`

It is designed to prove exact live HU/EN/DE R125 bindings and asset markers for the merge SHA. If the available connector does not expose that push workflow, production convergence must remain recorded as unproven rather than inferred.
