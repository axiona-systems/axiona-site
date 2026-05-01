# AXIONA R36 Header PNG Icon Fix

Fix:
- R35 used SVG A-mark in the header. Size was correct, but the image could disappear due to SVG rendering/path issues.
- R36 uses pre-rendered PNG A tile from the logo pack:
  `assets/brand/axiona-header-a-r36.png`
- The header still shows only the A icon + live `AXIONA Systems` text.
- No source photo/large image is squeezed into the small icon frame.
- No inline fake A.

App/fav/PWA:
- r36 cache-busted favicon, Apple touch, manifest, maskable icons and OG image.
