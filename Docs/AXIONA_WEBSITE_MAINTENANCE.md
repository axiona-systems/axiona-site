# AXIONA Website Maintenance Baseline

Status: **R77 SEO / indexing baseline**
Effective date: **2026-08-17**
Repository: `axiona-systems/axiona-site`
Public site: `https://axiona.systems/`

This file is the release checklist for future AXIONA public website changes. A website change is not complete until the applicable items below are checked.

## 1. Active public language set

The active public language versions are:

- Hungarian: `/`
- English: `/en/`
- German: `/de/`

The legacy `fr/`, `es/` and `it/` directories are **not** part of the current public language set. Do not add them to the language switch or sitemap unless a complete, intentionally maintained release for those languages is restored.

## 2. Canonical active route matrix

Every active route exists as a HU / EN / DE triplet:

| Purpose | HU | EN | DE |
| --- | --- | --- | --- |
| Overview | `/` | `/en/` | `/de/` |
| System design | `/systems.html` | `/en/systems.html` | `/de/systems.html` |
| Process design | `/process.html` | `/en/process.html` | `/de/process.html` |
| Security | `/security.html` | `/en/security.html` | `/de/security.html` |
| Solutions | `/solutions.html` | `/en/solutions.html` | `/de/solutions.html` |
| Contact | `/contact.html` | `/en/contact.html` | `/de/contact.html` |
| Privacy | `/privacy.html` | `/en/privacy.html` | `/de/privacy.html` |
| Legal | `/legal.html` | `/en/legal.html` | `/de/legal.html` |
| Support | `/support.html` | `/en/support.html` | `/de/support.html` |

Legacy pages such as `applications.html`, `automation.html`, `impact.html`, `services.html`, `company.html`, `practical-tips.html` and `case-study.html` are not part of the active sitemap. Do not re-add them accidentally.

## 3. Search / indexing invariants

The following rules are mandatory:

1. The HU, EN and DE homepages have a self-referencing canonical URL.
2. The HU, EN and DE homepages expose reciprocal `hreflang` links for `hu`, `en`, `de` and `x-default`; `x-default` points to the Hungarian root.
3. `sitemap.xml` is the canonical full cross-language route graph for all active public pages. Every listed URL must expose the same HU / EN / DE / x-default alternate set.
4. `robots.txt` must contain exactly the canonical sitemap location: `Sitemap: https://axiona.systems/sitemap.xml`.
5. Every active page needs a non-empty `<title>` and meta description and must remain indexable unless there is a deliberate documented decision to change that.
6. `lastmod` is only changed when the page itself changed materially. Never use a fake current date merely to attract recrawling.
7. A renamed, added or removed public page requires the route matrix, sitemap and automated verifier to be changed in the same release.
8. Visible copy, title and meta description must describe the same current positioning. Do not leave search metadata on an old product or company description after changing the page.

`privacy.html` and `legal.html` maintain page-level canonical / hreflang metadata. Support pages maintain self-canonical URLs. The sitemap still carries the complete language relationship for all active routes.

## 4. Automated release gate

Run before every website release:

```bash
python3 scripts/verify_seo.py
```

The verifier fails closed if the active route set and sitemap drift apart, a homepage canonical / hreflang mapping is broken, a required page loses basic search metadata, support loses its canonical URL, an inactive language or legacy route returns to the sitemap, or the robots sitemap pointer changes.

The same verifier is executed by `.github/workflows/axiona-repo-guard.yml` on pull requests and pushes to `main`.

## 5. Mandatory release sequence

1. Make the intended page changes and decide whether they affect HU only or the full HU / EN / DE triplet.
2. If a route, language relationship, title or search description changes, update the matching SEO metadata and sitemap in the same work unit.
3. Run `python3 scripts/verify_seo.py` locally.
4. Preview the changed pages and check desktop/mobile navigation and the language switch.
5. Open a pull request and wait for the repository guard to pass.
6. Merge only after the checks are green.
7. Verify the live deployment, not only the repository:

```bash
curl -fsSL https://axiona.systems/ | grep -Ei 'canonical|hreflang|<title>|description'
curl -fsSL https://axiona.systems/en/ | grep -Ei 'canonical|hreflang|<title>|description'
curl -fsSL https://axiona.systems/de/ | grep -Ei 'canonical|hreflang|<title>|description'
curl -fsSL https://axiona.systems/sitemap.xml | head -80
curl -fsSL https://axiona.systems/robots.txt
```

8. When homepage title/description/positioning changes, use Google Search Console URL Inspection for `/`, `/en/` and `/de/` and request indexing. When the route structure changes, inspect/resubmit `sitemap.xml` in Search Console as well.

## 6. Google result expectations

Deployment and Google Search results are separate states. A successful site deployment does **not** immediately replace Google's cached title or snippet. Recrawling and re-indexing are asynchronous, and Google may generate a search snippet from visible page content instead of using the meta description verbatim.

Therefore a release is considered technically complete when the repository checks and live proof are correct. Search Console indexing requests can accelerate discovery but cannot guarantee an immediate or verbatim SERP update.

## 7. Change-control rule

Do not treat `sitemap.xml`, canonical URLs, language alternates or `robots.txt` as incidental files. They are part of the public website contract and must be reviewed whenever the site structure or positioning changes.
