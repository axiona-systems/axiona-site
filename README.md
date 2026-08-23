# AXIONA Systems Website

Public website source for AXIONA Systems.

https://axiona.systems/

This repository contains the static source and public quality controls required to publish the AXIONA website through GitHub Pages.

## Local preview

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080/
```

## Public repository boundary

Only visitor-facing website source, public quality checks and publication-related configuration belong in this repository.

Internal governance, private infrastructure details, credentials, customer data and operational secrets are intentionally kept outside the public repository.

## Canonical website state

The repository `main` branch is the source of truth for the public website.

Current cross-site correction layers:
- `assets/r137-ux-fixes.css` — canonical navigation and Systems section layout correction
- `assets/motion-r138.css` + `assets/js/motion-r138.js` — current restrained bidirectional motion; public HTML is cache-busted as R142

Older release-numbered design/status documents remain historical evidence only. They are not active CI contracts and must not override the current public source.

## Quality and release controls

The active workflow surface is intentionally small:
- `axiona-repo-guard.yml` — static public-surface, metadata, asset-graph and workflow-hardening checks
- `axiona-browser-audit.yml` — Lighthouse and axe quality audit for pull requests
- `axiona-render-contract.yml` — current desktop/mobile render, navigation, Systems geometry and motion contract
- `axiona-pages-rebuild.yml` — exact-main GitHub Pages publication and live canonical verification

GitHub Actions dependencies are pinned to immutable full commit SHAs and validation workflows run with read-only repository permissions. The Pages publisher is the only workflow allowed a Pages write scope.

Dependabot tracks GitHub Actions updates weekly through `.github/dependabot.yml`.

## Design and release documentation

Current public-site design and UX baseline:
- `docs/AXIONA_WEB_VISUAL_UX_RULES.md`

Required visual release / cache / production-proof checklist:
- `docs/AXIONA_VISUAL_RELEASE_CHECKLIST.md`

Current next-design handoff:
- `docs/status/NEXT_DESIGN_HANDOFF.md`

Repository hygiene / hardening audit:
- `docs/status/R143_REPO_AUDIT.md`

## Security

Please do not publish vulnerability reports or sensitive data in GitHub issues.

See `SECURITY.md` and `/.well-known/security.txt` for the public reporting route.

## Ownership

Design and development: AXIONA Systems.

All rights reserved.
