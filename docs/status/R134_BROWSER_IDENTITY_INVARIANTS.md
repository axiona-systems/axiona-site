# R134 — Browser Identity Invariants

Date: 2026-08-23
Repository: `axiona-systems/axiona-site`
Starting canonical main SHA: `9d5ecb2c823621b29787e4f5aec9b9afa4634473`
Feature branch: `feature/browser-identity-r134`
PR: #86

## Finding

The repository already contained browser/application identity assets, but the public HTML did not bind them consistently:

- `site.webmanifest` existed but no active public page referenced it with `rel="manifest"`;
- `apple-touch-icon.png` existed but no active public page referenced it with `rel="apple-touch-icon"`;
- `favicon.svg` existed but was not bound as the primary scalable favicon;
- pages still used the legacy `rel="shortcut icon"` form;
- the manifest declared `assets/brand/axiona-icon-512.png` as `512x512`, while the actual PNG was `512x474`.

The last point was exposed by the new verifier during branch remediation and was not bypassed.

## Remediation

R134 standardizes browser identity on the complete physical HTML surface:

- 30 active HU/EN/DE pages;
- root `404.html`.

Every page now binds exactly:

```html
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link rel="icon" href="/favicon-32x32.png" type="image/png" sizes="32x32"/>
<link rel="icon" href="/favicon-16x16.png" type="image/png" sizes="16x16"/>
<link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180"/>
<link rel="manifest" href="/site.webmanifest"/>
```

Legacy `shortcut icon` bindings are removed.

The existing 512×474 manifest icon was repaired without stretching: its decoded RGBA pixels were preserved and centered on a transparent 512×512 canvas. The manifest continues to reference the same path.

## Fail-closed verifier

`scripts/verify_browser_identity.py` validates:

- exactly the five expected identity links on all 31 physical public HTML pages;
- no legacy `shortcut icon` relation;
- actual PNG dimensions:
  - `favicon-16x16.png` → 16×16;
  - `favicon-32x32.png` → 32×32;
  - `apple-touch-icon.png` → 180×180;
  - manifest 192 icon → 192×192;
  - manifest 512 icon → 512×512;
- valid `favicon.svg` source;
- exact manifest identity/application fields;
- exact manifest icon declarations.

The verifier is bound into `.github/workflows/axiona-repo-guard.yml`.

## Negative contract

`.github/workflows/axiona-browser-identity-r134-contract.yml` proves fail-closed behavior for:

- missing manifest link;
- reintroduced legacy `shortcut icon`;
- duplicate manifest link;
- manifest icon declaration drift;
- physical PNG dimension drift.

## Live proof

`.github/workflows/axiona-browser-identity-r134-live-proof.yml` runs after relevant `main` pushes and verifies:

- all 30 active routes expose the exact identity bindings;
- a real missing route returns HTTP 404 using the same manifest + Apple touch binding;
- `site.webmanifest` is live;
- manifest icon declarations are exact;
- live 192 and 512 PNG dimensions match their declarations.

## Scope

R134 changes browser/application identity metadata and one manifest icon canvas only.

It does **not** change:

- page copy;
- rendered layout;
- navigation;
- application behavior;
- tracking/data flow;
- existing page release markers;
- social preview images or social metadata.

## Acceptance

R134 is accepted only when its final exact PR head:

- contains no branch-local remediation workflow;
- passes AXIONA Public Surface Guard;
- passes AXIONA Browser Identity R134 Contract;
- passes all existing invariant contracts triggered by the change;
- passes all page visual contracts triggered by the 31 HTML changes;
- passes Browser Quality Audit, Lighthouse and axe/WCAG;
- is then squash-merged using `expected_head_sha` after re-resolving both PR head and `main`.

Production/live convergence is claimed only from actual post-merge live-proof evidence.
