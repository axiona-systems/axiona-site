# AXIONA Systems Website

Public website for AXIONA Systems.

https://axiona.systems/

This is a static website published through GitHub Pages.

## Local preview

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080/
```

## Release and maintenance

The canonical website maintenance and SEO/indexing checklist is:

`Docs/AXIONA_WEBSITE_MAINTENANCE.md`

Before every release run:

```bash
python3 scripts/verify_seo.py
```

Keep public pages simple, accurate and visitor-facing. Navigation, active language versions, canonical URLs, hreflang relationships, sitemap and robots configuration must remain consistent with the documented route matrix.

## Ownership

Design and development: Asztalos Zoltán / AXIONA Systems.

All rights reserved.
