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

Permanent rule: visual affordance must match semantic behavior. An informational element must not look like a link or button unless it actually performs an action.

## Sharing utility

The existing privacy-minimal sharing implementation remained in `assets/share-r86.css` and `assets/js/share-r86.js`, but the overview share component itself had been removed during the structural homepage redesign.

Root cause: the structural rewrite replaced the previous homepage DOM and omitted the `.ax-share` host section. The behavior layer still existed but no component remained for it to initialize against.

R116 restores the overview share strip for Hungarian, English and German. The restored component provides:
- native Share/Teilen/Megosztás where supported;
- Copy link / Link kopieren / Link másolása;
- the existing email, LinkedIn and WhatsApp fallback paths.

The R116 bootstrap creates the localized share markup before `share-r86.js` executes, so the existing sharing implementation remains the single behavior layer.

Permanent rule: structural redesigns must include a regression inventory for persistent utilities, not only the major visual sections.

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

R116 also passed the existing Public Surface Guard, Overview Visual Contract and Browser Quality Audit including Lighthouse and axe/WCAG.

Production convergence was separately proven against exact merge commit `bcb55ae1235e94a888b840b4704c1c84b67e29ff` on HU/EN/DE.

## Related canonical documentation

- `docs/status/R116_CHANGELOG.md` — root cause, safeguards and production evidence
- `docs/AXIONA_WEB_VISUAL_UX_RULES.md` — durable visual/interaction rules
- `docs/AXIONA_VISUAL_RELEASE_CHECKLIST.md` — required release and production-proof sequence
- `docs/status/NEXT_DESIGN_HANDOFF.md` — current baseline for the next page redesign
