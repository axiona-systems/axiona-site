# AXIONA Systems Website

Public website source for AXIONA Systems.

https://axiona.systems/

This repository contains the static assets required to publish the public website through GitHub Pages.

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

## Design and release documentation

Current public-site design and UX baseline:
- `docs/AXIONA_WEB_VISUAL_UX_RULES.md`

Required visual release / cache / production-proof checklist:
- `docs/AXIONA_VISUAL_RELEASE_CHECKLIST.md`

Current next-design handoff:
- `docs/status/NEXT_DESIGN_HANDOFF.md`

R115 is the accepted visual baseline; R116 contains the current overview UX corrections. When older experimental documentation conflicts with the canonical files above, the canonical files above take precedence.

## Security

Please do not publish vulnerability reports or sensitive data in GitHub issues.

See `SECURITY.md` for the public reporting route.

## Ownership

Design and development: AXIONA Systems.

All rights reserved.
