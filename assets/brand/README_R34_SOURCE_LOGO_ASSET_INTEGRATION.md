# AXIONA R34 Source Logo Asset Integration

R34 fixes the R32/R33 issue:
- No redrawn inline A.
- Header uses the actual source logo icon asset:
  `assets/brand/axiona-source-icon-r34.png`
- Header text remains live HTML: `AXIONA Systems`.

App/browser icons:
- r34 cache-busted favicon / Apple / PWA icons are generated directly from the source icon asset.
- If a browser still shows the old "Open in app" icon, remove/reinstall the saved web app because the browser may cache installed app icons separately.
