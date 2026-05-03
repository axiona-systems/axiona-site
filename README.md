# AXIONA Systems Website

Public website for AXIONA Systems.

Live site: https://axiona.systems/

## Scope

This repository contains the public static website and public metadata only.

Included:

- static HTML and CSS
- public page structure
- sitemap and robots configuration
- GitHub Pages custom-domain configuration

Not included:

- private operational notes
- credentials or secrets
- customer data
- internal system architecture
- local backups or generated deployment archives

## Local preview

```bash
python3 -m http.server 8080
```

Open:

```text
http://localhost:8080/
```

## Deployment

The production site is published from the `main` branch through GitHub Pages.

Before publishing, check that:

- public pages contain only visitor-facing information
- navigation and sitemap are aligned
- language versions are consistent
- no private paths, notes, credentials or temporary files are committed

## Ownership

Design and development: Asztalos Zoltán / AXIONA Systems.

All rights reserved unless a separate written agreement states otherwise.
