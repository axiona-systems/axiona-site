# AXIONA Site — Release Ready R1

Static website source package for `https://axiona.systems`.

## Contents

- Clean static HTML pages
- Shared `styles.css` and `site.js`
- Stable language handling with CSS fallback and JS state
- Contact, Support, Privacy, Legal pages
- `sitemap.xml`, `robots.txt`, `site.webmanifest`, `CNAME`
- Clean assets folder

## Deployment target

GitHub Pages or any static host.

## Release checks included in this package

- No `.git`, `__MACOSX`, or `.DS_Store` in the release ZIP
- No dead internal links detected by local source check
- No disabled public nav item
- Contact navigation points to `contact.html`, not a fragile direct mailto-only route
- Email buttons are generated client-side from data attributes
- Per-page canonical URL and OpenGraph metadata

Build date: 2026-04-30
