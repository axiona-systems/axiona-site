# AXIONA Web — Visual Release Checklist

Status: required checklist for public visual/UX releases
Last updated: 2026-08-23

## 1. Repository safety

Before any write:
- re-resolve `main` and record the exact SHA;
- create a feature branch from that exact SHA;
- verify every write targets the feature branch explicitly;
- never rely on a connector/tool default branch for a write.

Important incident: during R116 preparation, a temporary marker file was accidentally written to `main` because the write did not specify an existing feature branch. It was immediately reverted, but it changed the canonical commit history. Permanent rule: branch creation must precede every repository write, and every write call must name the branch.

## 2. Release binding and cache safety

A visual change is not considered deployed merely because the repository contains a new CSS/JS file.

For every visual release:
- update the HTML-level asset URL/query to the new release identifier;
- do this directly in HU/EN/DE HTML;
- do not depend on a newly added `@import` inside an older stylesheet to make the browser discover the release;
- verify the live HTML contains the expected versioned URLs.

Why: R113 was correctly deployed in GitHub, but browsers could keep an older cached parent stylesheet and never discover the new imported visual layer. R114 fixed this by binding versioned assets directly from HTML.

## 3. Semantic affordance check

For every hover/focus state ask: does this element actually perform an action?

Informational element:
- default cursor;
- no action arrow;
- no button/link-style hover shift;
- no misleading focus behavior.

Interactive element:
- semantic anchor/button;
- working target/action;
- keyboard focus state;
- touch-safe behavior.

R116 exists because the problem-type rows visually advertised clickability without an action.

## 4. Regression inventory

Before merge verify that structural redesigns have not silently removed persistent utilities or content blocks. At minimum check:
- navigation;
- language switch;
- primary CTA;
- Keeper reference/case section where applicable;
- share utility;
- footer/legal/support links;
- visit-counter script binding where applicable;
- required structured data / social metadata.

R116 restored the share component after the structural homepage rewrite had dropped its host markup while leaving the supporting CSS/JS in place.

## 5. Rendered evidence

Every meaningful visual release requires rendered evidence, not CSS inspection alone.

Required minimum:
- HU desktop;
- HU mobile;
- EN structural parity;
- DE structural parity;
- focused screenshots of modified sections;
- horizontal-overflow check.

For interaction changes also prove the actual browser behavior, not just markup presence.

## 6. Quality gates

Before merge require green results for the applicable checks:
- AXIONA Public Surface Guard;
- AXIONA Overview Visual Contract or page-specific visual contract;
- AXIONA Browser Quality Audit;
- Lighthouse quality budgets;
- axe/WCAG audit;
- release-specific interaction/render contract when the change warrants one.

Do not weaken a gate to make a release pass. Fix the implementation or improve observability.

## 7. Exact-head merge discipline

Before merge:
- re-fetch PR metadata;
- confirm PR is mergeable;
- confirm the exact head SHA equals the tested SHA;
- squash merge with `expected_head_sha`;
- record the resulting canonical `main` SHA.

## 8. Production convergence proof

After merge, do not infer that GitHub Pages is current.

Prove:
1. latest Pages build status is `built`;
2. Pages build commit equals the exact merge SHA;
3. live HU/EN/DE HTML contains the expected release bindings;
4. live CSS/JS contains the release marker;
5. the modified interaction or visual behavior is present in the rendered live page.

Disposable production-proof branches/PRs must be closed without merge after successful proof.

## 9. Design baseline

Unless explicitly superseded by an accepted redesign:
- R115 defines the current AXIONA visual direction;
- R116 defines the current interaction/affordance corrections;
- `docs/AXIONA_WEB_VISUAL_UX_RULES.md` is the canonical design/UX rule set.

## 10. Definition of done

A visual change is done only when:
- the intended design is rendered correctly;
- semantic interaction matches appearance;
- HU/EN/DE are in parity;
- all gates are green;
- exact-head merge is complete;
- exact production convergence is proven;
- relevant status/handoff documentation is updated.
