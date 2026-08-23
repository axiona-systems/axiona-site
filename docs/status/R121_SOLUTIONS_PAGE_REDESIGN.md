# R121 — Solutions page redesign

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Release: `R121`
Target pages:
- `solutions.html`
- `en/solutions.html`
- `de/solutions.html`

## Canonical start

R121 started from exact canonical R120 main SHA:
`0c5e9c25bf189b24d74415a628aa07abde663dcd`

Feature branch:
`feature/solutions-page-r121`

The branch existed before every R121 write. All writes explicitly target it.

## Design intent

R121 treats the page as a solution brief / option matrix rather than a product catalogue or fake software dashboard.

Visual language:
- warm paper/off-white dominant field;
- off-white working surfaces for solution choices and evidence;
- contained deep-petrol frames for system composition and Keeper;
- restrained orange editorial emphasis;
- acid green only for compact control/status signals;
- cyan only as a secondary technical accent;
- one-pixel borders and solid offset shadows;
- no CAD identity, decorative relation maps, scanner lines, glow, particles, coordinates or fake telemetry.

## Content contract

R121 preserves the existing substantive HU/EN/DE content:
1. implementation forms / technology follows the job;
2. four problem-to-direction examples;
3. five system layers: process, data, logic, interface and operations;
4. the explicit message that the client does not need to choose technology first;
5. first-conversation CTA based on understanding the current workflow;
6. AXIONA Keeper own-product section;
7. five Keeper processing rows;
8. Share / Copy link / fallback sharing utility;
9. footer, support, privacy, legal, security and visit-counter bindings.

Websites and webshops remain possible implementation forms, not the primary positioning.

The opening heading is one semantic `<h1>` in every language.

## Direct release binding

Every target page binds directly:
- `/assets/solutions-r121.css?release=R121`
- `/assets/js/solutions-r121.js?release=R121`
- `meta[name="axiona-release"] = R121`
- `page-solutions-r121` body scope.

## Motion and interaction contract

Reveal motion is progressive enhancement, repeatable on return scroll and transform-only. Reveal opacity remains `1` in every state.

Informational surfaces — problem cards, system-layer rows and Keeper process rows — use the default cursor and receive no fake action affordance. Real links remain semantic links with actual targets.

## Page-specific render proof

Workflow:
`.github/workflows/axiona-solutions-r121-visual-contract.yml`

It verifies HU/EN/DE on desktop and mobile, including:
- direct R121 bindings and markers;
- exactly one main `<h1>`;
- 1 solution brief;
- 4 problem/direction cards;
- 5 system-layer rows;
- 1 first-conversation panel;
- 1 Keeper card with 5 processing rows;
- Share host and footer;
- no horizontal overflow;
- accepted warm-paper/off-white/petrol surface contract;
- informational cursor behavior;
- opacity-stable repeatable motion;
- screenshot evidence.

## Quality gates

The exact PR head must be green for:
- AXIONA Public Surface Guard;
- AXIONA Solutions R121 Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse quality budgets;
- axe/WCAG audit.

No gate may be weakened to make the release pass.

## Production convergence

Post-merge workflow:
`.github/workflows/axiona-solutions-r121-live-proof.yml`

It verifies live HU/EN/DE HTML and R121 CSS/JS markers with cache-busted requests and records the exact `GITHUB_SHA` it validates.

If the available GitHub connector cannot expose the push-triggered production proof run, production convergence must remain explicitly unproven rather than inferred.

## Next design target

After R121 acceptance, review the remaining secondary public pages as a coherent set. The next likely page family is Contact (`contact.html`, `en/contact.html`, `de/contact.html`), but it must start as a separate release from the then-current exact `main` SHA.
