# AXIONA R31 Logo/Icon Integration

Active header strategy:
- Header uses `axiona-mark-r31.svg` + live text `AXIONA Systems`.
- This fixes visibility issues caused by full wordmark SVG sizing.

Cache-busted app/icon strategy:
- New manifest icon paths use r31 filenames:
  - `/assets/brand/axiona-icon-r31-192.png`
  - `/assets/brand/axiona-icon-r31-512.png`
  - `/assets/brand/maskable-icon-r31-192.png`
  - `/assets/brand/maskable-icon-r31-512.png`
- New linked favicon/touch paths:
  - `/favicon-r31.svg`
  - `/favicon-r31.ico`
  - `/apple-touch-icon-r31.png`

Important:
- Already installed iOS home-screen/PWA icons may still be cached by the device.
- For those, remove the old saved home-screen app and add it again after deploy.
