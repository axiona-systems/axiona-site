# R131 — Navigation and Footer Parity Invariants

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `cfa47f55b3b1f3c76f740cfe61ff4001c6d3c60b`
Feature branch: `feature/navigation-parity-invariants-r131`

## Why this release exists

The whole-site audit found that internal links are individually protected by R128, but semantic parity between the 30 active localized pages was not yet enforced. A link could still point to an existing AXIONA page while being the wrong navigation target for that position or language.

R131 protects the navigation model itself. No public markup change is intended; the verifier is designed to expose a real current drift if one exists rather than normalize pages silently.

## Accepted navigation model

For every HU/EN/DE active page:

### Brand
The AXIONA brand link returns to the current locale home:
- HU `/`
- EN `/en/`
- DE `/de/`

### Desktop and mobile primary navigation
Both surfaces must expose the same ordered six routes in the current locale:
1. Overview
2. Systems
3. Process
4. Security
5. Solutions
6. Contact

The active state must correspond to the current page when that page is one of these six primary routes. Keeper, Privacy, Legal and Support intentionally have no primary-nav active item.

### Header language switch
The three language links are route-preserving, not home-only. For example:
- `/systems.html`
- `/en/systems.html`
- `/de/systems.html`

Exactly the current language link is active.

### Footer
The footer has seven semantic routes in this exact order:
1. Support in current locale
2. Privacy in current locale
3. Legal in current locale
4. Security in current locale
5. HU home
6. EN home
7. DE home

Footer language links intentionally go to language home pages rather than preserving the current route.

## Verifier

New script:

`scripts/verify_navigation_parity.py`

It parses all 30 active public HTML files and checks:
- localized brand route;
- desktop primary route list and ordering;
- mobile primary route list and ordering;
- desktop/mobile parity;
- primary-nav active-state semantics;
- route-preserving header language switch;
- language-switch active state;
- localized footer utility targets;
- footer home-language targets and ordering.

Success evidence reports:
- `OK_AXIONA_NAVIGATION_PARITY`
- `NAVIGATION_PAGES=30`
- `PRIMARY_NAV_LINKS=360`
- `LANGUAGE_SWITCH_LINKS=90`
- `FOOTER_LINKS=210`

The verifier supports `--root` for isolated negative fixtures.

## Guard integration

AXIONA Public Surface Guard now runs:
1. public-surface invariants;
2. sitemap locale-family invariants;
3. navigation/footer parity invariants;
4. diff whitespace.

No browser dependency is added.

## Negative contract

Workflow:

`.github/workflows/axiona-navigation-r131-parity-contract.yml`

It proves fail-closed behavior for:
1. wrong English Process primary-nav target → `desktop nav mismatch`;
2. broken German Privacy route-preserving language switch → `language switch mismatch`;
3. wrong Keeper footer utility destination → `footer route mismatch`.

## Scope boundary

R131 is static verification only unless its baseline identifies a genuine current navigation drift. No public HTML/CSS/JS is intentionally modified. Browser/Lighthouse/axe are not required unless CI exposes a real HTML remediation.

## Acceptance

The exact R131 PR head must pass:
- AXIONA Public Surface Guard including navigation parity;
- AXIONA Navigation R131 Parity Contract.

If baseline verification exposes a current defect, fix the source and then require fresh exact-head checks; do not weaken the invariant.
