# AXIONA R32 Header Brand Hardening

R32 fixes the failed R30/R31 logo integration direction.

Header strategy:
- The header no longer depends on an external logo image.
- The header uses inline SVG mark + live text: `AXIONA Systems`.
- This guarantees the brand remains visible on the home page and all subpages.

Icon strategy:
- Favicon / Apple touch / PWA icons use r32 cache-busted filenames.
- Already installed iOS home-screen icons may still need removal/re-add.
