# AXIONA R116 — Overview UX affordance and sharing fix

Date: 2026-08-23

## Scope

R116 is a narrow UX correction on top of the accepted R115 homepage visual system. It does not redesign the homepage or secondary pages.

## Problem-field affordance

The six rows under the problem-type section are informational, not navigation. The previous hover treatment shifted the row and exposed a right arrow, which visually implied clickability without providing an action.

R116 therefore:
- removes the right-side action arrow from the rendered view;
- keeps a normal/default cursor;
- removes hover movement, background switching and other link-like emphasis;
- preserves the existing content and scroll reveal behavior.

## Sharing utility

The existing privacy-minimal sharing implementation remained in `assets/share-r86.css` and `assets/js/share-r86.js`, but the overview share component itself had been removed during the structural homepage redesign.

R116 restores the overview share strip for Hungarian, English and German. The restored component provides:
- native Share/Teilen/Megosztás where supported;
- Copy link / Link kopieren / Link másolása;
- the existing email, LinkedIn and WhatsApp fallback paths.

The R116 bootstrap creates the localized share markup before `share-r86.js` executes, so the existing sharing implementation remains the single behavior layer.

## Cache binding

The three overview pages directly bind:
- `/assets/visual-r116.css?release=R116`
- `/assets/js/overview-r116.js?release=R116`

This avoids relying on an older cached parent stylesheet or script to discover the hotfix.

## Verification

The dedicated R116 overview UX contract checks HU/EN/DE at desktop and mobile widths. It fails if:
- the six problem rows expose an action arrow or pointer-style affordance;
- hover changes their position, padding or background;
- the share component is missing or duplicated;
- localized Share and Copy Link controls are missing;
- the Share control is not wired to the existing fallback behavior;
- the page introduces horizontal overflow.
