# R122 — Contact page redesign

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Release: `R122`
Targets:
- `contact.html`
- `en/contact.html`
- `de/contact.html`

## Canonical start

R122 started from exact canonical R121 main SHA:
`4600eaabaa1e174cdcc199830c1b97672b913bed`

Feature branch:
`feature/contact-page-r122`

The feature branch existed before every R122 write and all repository writes explicitly target it.

## Design intent

R122 turns the contact page into a first-conversation brief and privacy-minimal mail-preparation sheet. It intentionally avoids a generic marketing form and preserves the existing local-mail workflow.

Visual language:
- warm paper/off-white dominant field;
- contained petrol form frame;
- stable off-white input/work surfaces;
- restrained orange for the real submit action;
- cyan for the privacy/data-flow note;
- acid only as a compact form-state label;
- one-pixel borders and solid offset shadows;
- no dashboard/CAD identity, fake telemetry, scanner lines, glow, particles or pseudo-controls.

## Functional/content contract

R122 preserves:
1. technology-neutral first-conversation message;
2. explicit explanation that form data is not submitted to a separate AXIONA form database;
3. four practical examples of a useful starting point;
4. support route for existing AXIONA users;
5. direct `hello@axiona.systems` mail link;
6. six structured intake fields;
7. required email and problem fields;
8. explicit warning not to send passwords, tokens, keys, banking data or sensitive documents in the first message;
9. `assets/js/contact-intake.js` mailto-based behavior;
10. footer, legal/privacy/security/support links and visit counter.

The opening heading is promoted to one semantic `<h1>` in HU/EN/DE.

## Direct release binding

Each target HTML page binds:
- `/assets/contact-r122.css?release=R122`
- `/assets/js/contact-r122.js?release=R122`
- `meta[name="axiona-release"] = R122`
- `page-contact-r122` body scope.

The functional mail-preparation script remains `/assets/js/contact-intake.js` and is explicitly covered by the R122 browser contract.

## Interaction contract

The submit control is a real semantic `<button>` and retains action hover/focus behavior. The support/direct-mail paths remain real links.

The four starting-point rows are informational and remain default-cursor stable surfaces.

Submitting valid required fields must prepare a `mailto:hello@axiona.systems?...` fallback and update the live status text. No separate AXIONA contact database is introduced by this release.

## Motion contract

R122 reveal motion is progressive enhancement, repeatable on return scroll and transform-only. Reveal opacity remains `1` in every state. `prefers-reduced-motion` disables the transform/transition.

## Page-specific proof

Workflow:
`.github/workflows/axiona-contact-r122-visual-contract.yml`

It verifies HU/EN/DE desktop/mobile:
- direct R122 CSS/JS binding and asset markers;
- 1 main h1;
- 4 informational fit rows;
- 1 intake form;
- 6 intake fields / 2 required fields;
- safety, direct-email and support paths;
- footer preservation;
- no horizontal overflow;
- warm-paper, off-white, petrol, privacy and safety surface colors;
- informational default cursor / opacity 1;
- repeatable reveal behavior;
- actual mailto preparation/fallback behavior on the HU desktop path;
- screenshot evidence.

## Required gates

The exact PR head must pass:
- AXIONA Public Surface Guard;
- AXIONA Contact R122 Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse quality budgets;
- axe/WCAG audit.

No gate may be weakened to make the release pass.

## Production convergence

Post-merge workflow:
`.github/workflows/axiona-contact-r122-live-proof.yml`

It verifies cache-busted live HU/EN/DE R122 bindings, the intake script, form host and R122 CSS/JS markers against the exact `GITHUB_SHA`.

If the GitHub connector does not expose the push-triggered run, exact production convergence remains unproven rather than inferred.

## Next step

After R122 acceptance, inventory the remaining public pages (Keeper, support, privacy/legal and other utility/detail surfaces) before choosing the next coherent release family.
