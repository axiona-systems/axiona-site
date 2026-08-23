# R114 cache-proof visual binding

R114 corrected a browser-visible release problem: the repository and GitHub Pages could contain the new visual layer while a browser still rendered the previous design because the new stylesheet was discovered only through an older cached parent stylesheet.

The durable rule is therefore broader than R114:

- every visual release must change a direct HTML-level CSS/JS URL or query string;
- HU, EN and DE pages must bind the release explicitly;
- do not rely on a new `@import` added inside an older asset as the only release-discovery path;
- repository state alone is not proof of production convergence;
- after merge, verify the exact Pages build commit and fetch the live HTML/assets with cache-busting proof parameters.

R114 originally bound R110, R112, R113 and R113 tuning directly from HU/EN/DE HTML with `release=R114` query strings. R115 and R116 retained the same principle with their own versioned direct bindings.

See `docs/AXIONA_VISUAL_RELEASE_CHECKLIST.md` for the required release proof sequence.
