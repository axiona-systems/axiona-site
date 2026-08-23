# AXIONA Web — Visual & UX Rules

Status: canonical public-site design guidance
Last updated: 2026-08-23
Baseline: accepted R115 visual direction + R116 UX corrections

## 1. Purpose

This document is the durable visual and interaction reference for AXIONA public web work. It exists to prevent later page redesigns from drifting back toward styles or interaction patterns that were explicitly rejected during the R112–R116 homepage work.

The current homepage is the primary live reference. Secondary pages should inherit its visual grammar without mechanically copying its layout.

## 2. AXIONA visual character

Use:
- warm paper / off-white as the dominant page field;
- deep petrol as a contained product, control or evidence surface;
- restrained orange for active/control emphasis;
- acid green only for small status/control signals;
- cyan only as a secondary technical accent;
- thin one-pixel borders;
- solid offset shadows rather than soft glows;
- generous negative space and calm editorial composition;
- product/work-surface layouts, document-like rows and controlled information panels;
- technical diagrams only when they genuinely explain something.

Avoid:
- full-page dark UI as the default language;
- CAD/dashboard styling as the brand identity;
- node-network / relation-map graphics used only for decoration;
- scanner lines, glowing effects, particles, floating coordinates or fake telemetry;
- excessive animation or pointer tilt;
- full-card background color flipping during scroll;
- dense visual noise that competes with the message.

## 3. Keeper reference direction

The Keeper public visual language is the strongest current reference for AXIONA representation:
- large simple planes;
- warm outer field;
- off-white working surface;
- contained petrol control areas;
- small, deliberate status accents;
- clear hierarchy instead of decorative technical complexity.

The homepage R115 hero and System Story are an adaptation of this direction. Future pages should use the same design family, not reproduce the old relation-map/CAD grammar.

## 4. Information versus interaction

A visual affordance must match a real action.

If an element is informational:
- use the default cursor;
- do not add a right-arrow action cue;
- do not shift it laterally on hover;
- do not switch to a button-like background on hover;
- do not give it link-like emphasis unless there is an actual target.

If an element is interactive:
- use a semantic `<a>` or `<button>`;
- provide a visible focus state;
- make hover/focus treatment consistent with the action;
- ensure touch and keyboard use are both valid.

R116 was required because the six problem-type rows violated this rule: they looked clickable while being informational.

## 5. Motion

Motion is structural, restrained and repeatable.

Allowed:
- small vertical/opacity reveal on viewport entry;
- replay when the user leaves and re-enters a section;
- subtle state emphasis when it communicates current context.

Avoid:
- one-time motion that leaves the page permanently frozen when the intended behavior is scroll-reactive;
- large transforms;
- hover/pointer perspective tilt on major page surfaces;
- looping decorative motion;
- scanner/glow/particle effects.

Always respect `prefers-reduced-motion`.

## 6. Stable surfaces

Scroll state must not cause large background-color jumps between adjacent cards. R115 corrected System Story so all steps remain on the same off-white surface inside one shared petrol frame; the current step is indicated only by a restrained accent.

Use state changes at the edge, marker, badge or small control level rather than repainting the entire card.

## 7. Sharing utility

The overview sharing utility is a secondary convenience, not a primary CTA.

Rules:
- keep it visually subordinate to project/contact conversion;
- retain native Share when available;
- retain Copy link;
- retain privacy-minimal fallback paths already implemented in `assets/js/share-r86.js`;
- do not silently remove the component during structural redesigns;
- test HU/EN/DE independently.

R116 restored this component after the R112 structural rewrite had removed its HTML host while leaving its CSS/JS implementation in the repository.

## 8. Multilingual parity

Every visual/UX release affecting the overview must be checked on:
- `/`
- `/en/`
- `/de/`

Changes must preserve structural parity, localized copy, navigation and sharing behavior. A fix is not complete if only the Hungarian page is correct.

## 9. Page redesign rule

For secondary pages (`systems.html`, `process.html`, `security.html`, `solutions.html`):
- preserve the existing content intent unless the task explicitly includes content editing;
- redesign one coherent page family at a time;
- use the R115/R116 homepage as the visual baseline;
- do not introduce a new competing design system;
- prefer clear storytelling and evidence over ornamental technical graphics;
- render desktop and mobile evidence before merge.

## 10. Accepted baseline

Accepted visual baseline: R115.
Accepted UX correction baseline: R116.

The next design work starts from these rules, not from earlier R112/R113 experiments in isolation.
