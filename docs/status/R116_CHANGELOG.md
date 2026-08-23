# R116 changelog

Date: 2026-08-23

## User-visible corrections

- Removed false click affordance from the six overview problem-type rows.
- Removed the rendered right-arrow cue from those informational rows.
- Removed hover movement/background treatment that implied navigation.
- Restored normal/default cursor behavior for the rows.
- Restored the overview Share + Copy link utility in Hungarian, English and German.
- Preserved the existing privacy-minimal native-share / email / LinkedIn / WhatsApp fallback behavior.

## Root causes

### False problem-row affordance
The structural/visual redesign retained action-like styling on informational `<article>` rows. The visual language suggested a target even though no `<a>` or `<button>` existed.

### Missing sharing section
The R112 structural homepage rewrite replaced the previous homepage DOM and omitted the `.ax-share` section. The supporting `share-r86.css` and `share-r86.js` remained present, so the capability existed in the codebase but had no component host on the overview page.

## Permanent safeguards

- Informational rows may not use pointer cursors, action arrows or link-like hover transforms.
- Persistent page utilities must be part of structural-regression inventory during redesign.
- HU/EN/DE overview parity is mandatory.
- Visual releases must use direct HTML-level release binding.
- Rendered interaction contracts must test the behavior that caused the regression.

## Verification

R116 added `.github/workflows/axiona-r116-overview-ux-contract.yml`, validating desktop/mobile behavior and multilingual presence.

All release gates passed:
- AXIONA Public Surface Guard;
- AXIONA Overview Visual Contract;
- AXIONA Browser Quality Audit;
- Lighthouse quality budgets;
- axe/WCAG;
- AXIONA R116 Overview UX Contract.

Production proof confirmed that GitHub Pages served exact merge commit:
`bcb55ae1235e94a888b840b4704c1c84b67e29ff`

The production proof also confirmed live HU/EN/DE sharing controls and the absence of false problem-row arrows/click affordance.

## Process incident during preparation

A temporary marker write accidentally targeted `main` before the feature branch existed. It was immediately reverted. No intended website content remained from the temporary commit, but canonical history advanced.

Permanent safeguard: create the feature branch before any repository write and explicitly name that branch on every write operation.
