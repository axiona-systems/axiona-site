# AXIONA Site — R123 Support Page Redesign

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `fdefa75eb21c7ce277e04db6ce98ff9385f91f6d`
Feature branch: `feature/support-page-r123`

## Scope

R123 redesigns the support family:
- `support.html`
- `en/support.html`
- `de/support.html`

The existing support substance remains intact:
- four support categories: usage, unexpected behaviour, access, security/privacy;
- direct `hello@axiona.systems` support route;
- minimum-necessary-data guidance;
- explicit warning not to send passwords, sign-in codes, API keys or other secrets;
- four-item guidance for a useful first message;
- screenshot guidance with unnecessary personal/confidential data removed;
- distinction between support and new-project contact;
- footer/legal/privacy/security links and visit counter.

## Visual direction

R123 uses a human support dossier rather than inheriting the Process page identity:
- warm paper opening field;
- off-white stable support-category rows;
- one contained deep-petrol support-contact panel;
- soft neutral first-message chapter with off-white guidance rows;
- warm final direct-support block;
- restrained orange for action emphasis;
- acid only as a compact support-state badge;
- cyan as a secondary support/data-safety cue;
- no fake ticket console, telemetry, CAD, scanner, glow or pseudo-controls.

Informational rows remain default-cursor stable surfaces. Motion is repeatable, transform-only and keeps opacity at `1`.

## Direct release bindings

Each HU/EN/DE HTML page binds directly to:
- `/assets/support-r123.css?release=R123`
- `/assets/js/support-r123.js?release=R123`

Release metadata:
- `meta[name="axiona-release"] = R123`

## Semantic/accessibility changes

- Opening support title is a semantic `h1` in all three languages.
- Informational support and first-message rows do not advertise clickability.
- Real support e-mail remains a semantic link.
- `prefers-reduced-motion` disables reveal transforms.
- Reveal motion never reduces text opacity.

## Verification

Page-specific contract:
- `.github/workflows/axiona-support-r123-visual-contract.yml`

It verifies:
- HU/EN/DE desktop and mobile rendering;
- exact R123 CSS/JS bindings and markers;
- semantic h1;
- 4 support categories;
- 1 support contact panel;
- 4 first-message guidance rows;
- direct support mailto link;
- footer preservation;
- no horizontal overflow;
- expected surface colors;
- default cursor and opacity 1 for informational rows;
- repeatable viewport reveal behaviour;
- rendered screenshot evidence.

Repository-wide required checks remain:
- AXIONA Public Surface Guard;
- AXIONA Browser Quality Audit;
- Lighthouse quality budgets;
- axe/WCAG.

## Production proof

Post-merge workflow:
- `.github/workflows/axiona-support-r123-live-proof.yml`

It is designed to prove that live HU/EN/DE support HTML and R123 assets converge on the merge SHA. If the connector does not expose the push workflow run, that limitation must be recorded rather than inferring deployment.
