# AXIONA Website Maintenance Baseline

Status: **Premium hardening P0 / P2 / P3 / P4 + public copy baseline + Keeper preview R87**
Effective date: **2026-08-19**
Repository: `axiona-systems/axiona-site`
Public site: `https://axiona.systems/`

This file is the canonical maintenance and release checklist for future AXIONA public website changes. A website change is not complete until the applicable repository, browser and live-deployment proofs below are green.

The active HU / EN / DE public copy was reviewed as one language system on 2026-08-19. Keep the writing direct, concrete and human: avoid abstract product language, inflated claims, generic AI-style slogans and literal cross-language translations. Hungarian uses direct informal address where the visitor is addressed personally; English uses natural personal business language; German uses consistent formal `Sie` address. Preserve meaning across languages rather than forcing sentence-by-sentence translation.

## 1. Active public language set

The active public language versions are:

- Hungarian: `/`
- English: `/en/`
- German: `/de/`

The legacy `fr/`, `es/` and `it/` directories are **not** part of the current public language set and have been removed. Do not restore them, add them to the language switch or add them to the sitemap unless a complete, intentionally maintained release for those languages is explicitly approved.

## 2. Canonical active route matrix

Every active route exists as a HU / EN / DE triplet:

| Purpose | HU | EN | DE |
| --- | --- | --- | --- |
| Overview | `/` | `/en/` | `/de/` |
| System design | `/systems.html` | `/en/systems.html` | `/de/systems.html` |
| Process design | `/process.html` | `/en/process.html` | `/de/process.html` |
| Security | `/security.html` | `/en/security.html` | `/de/security.html` |
| Solutions | `/solutions.html` | `/en/solutions.html` | `/de/solutions.html` |
| AXIONA Keeper | `/keeper.html` | `/en/keeper.html` | `/de/keeper.html` |
| Contact | `/contact.html` | `/en/contact.html` | `/de/contact.html` |
| Privacy | `/privacy.html` | `/en/privacy.html` | `/de/privacy.html` |
| Legal | `/legal.html` | `/en/legal.html` | `/de/legal.html` |
| Support | `/support.html` | `/en/support.html` | `/de/support.html` |

## 3. Legacy public route policy

The following old HU / EN / DE page names are **not active site pages**:

- `applications.html`
- `automation.html`
- `case-study.html`
- `company.html`
- `impact.html`
- `practical-tips.html`
- `services.html`

They remain only as lightweight `noindex,follow` redirect shells so old bookmarks and search-engine links do not land on obsolete AXIONA layouts.

Current redirect mapping:

- `applications.html` → `solutions.html`
- `automation.html` → `solutions.html`
- `case-study.html` → `process.html`
- `company.html` → the matching language root
- `impact.html` → `systems.html`
- `practical-tips.html` → `process.html`
- `services.html` → `solutions.html`

Rules:

1. Do not restore old navigation, old hero layouts or old page styling inside these shells.
2. Do not add the legacy routes back to the active sitemap.
3. Do not link active pages to the legacy routes.
4. A future route migration must preserve a visitor-safe redirect path instead of silently reviving an old public page.

Unused legacy CSS/icon generations removed during P0 must not be restored without an explicit dependency proof.

## 4. P1 reference / case-study layer is intentionally deferred

The premium benchmark identified client proof, references and case studies as a future improvement, but **P1 is deliberately out of scope for the current baseline**.

Until at least one AXIONA application is genuinely ready to be presented as a completed reference, do not add:

- fabricated customer logos
- invented testimonials
- invented customer counts
- invented efficiency or performance percentages
- project outcomes that cannot be demonstrated
- a case study that presents an unfinished prototype as a completed product

P1 may be reopened only when a real AXIONA application is production-ready enough to be shown honestly. At that point the proof layer should be designed from verifiable facts, not marketing placeholders.

### 4.1 AXIONA Keeper public preview is not a completed reference

`/keeper.html`, `/en/keeper.html` and `/de/keeper.html` are an explicitly labelled **product-in-development preview**, not a completed reference or case study. Publishing this preview does not reopen P1.

Keeper publication rules:

1. The page must state clearly that Keeper is in active development and is not yet publicly available.
2. Planned capabilities — including automatic folder/case organisation — must be described as planned until they are genuinely available in the public product.
3. Do not publish a purchase button, App Store badge, price, release date or availability claim before those facts are real and approved.
4. Do not turn internal architecture or engineering terminology into public product copy. Explain the user problem and the expected behaviour in ordinary language.
5. Security and privacy claims must remain within demonstrated product boundaries. Avoid absolute claims such as “unbreakable”, “100% secure” or equivalent.
6. The public examples are explanatory scenarios, not customer testimonials or claims that a named external customer is already using Keeper.
7. HU / EN / DE Keeper pages must stay semantically aligned. Preserve natural language in each locale rather than literal translation.

## 5. Contact intake privacy invariant

The HU / EN / DE contact pages use a structured project-intake interface.

Mandatory behavior:

1. The intake remains **local-only** in the browser.
2. It must not submit form data to a new AXIONA database or third-party form backend.
3. `assets/js/contact-intake.js` may prepare a structured `mailto:` message in the visitor's own mail application.
4. The form must not gain a network-submission `fetch`, `XMLHttpRequest` or server `action` without an explicit architecture, privacy and legal review.
5. The first-message warning must continue to tell visitors not to send passwords, tokens, private keys, banking data or sensitive personal documents.
6. Direct `hello@axiona.systems` contact remains available as a fallback.
7. If the intake architecture changes later, the Privacy page and automated quality gate must change in the same work unit.

This is a deliberate reliability and privacy decision: the current contact UX is improved without introducing another data processor, form database or hidden failure mode.

## 6. Security publication invariant

The public security contact contract includes:

- `/.well-known/security.txt`
- `/security.html`
- repository `SECURITY.md`

`/.well-known/security.txt` currently publishes:

- security contact email
- expiry date
- preferred languages: `hu, en, de`
- canonical security.txt URL
- public security-policy URL

Rules:

1. Renew the `Expires` date before it lapses.
2. Keep the contact route current.
3. Never request credentials, tokens, private keys or personal documents in an initial vulnerability report.
4. Security reports must not be directed to public GitHub issues.

## 7. Search / indexing invariants

The following rules are mandatory:

1. The HU, EN and DE homepages have a self-referencing canonical URL.
2. The HU, EN and DE homepages expose reciprocal `hreflang` links for `hu`, `en`, `de` and `x-default`; `x-default` points to the Hungarian root.
3. `sitemap.xml` is the canonical full cross-language route graph for all active public pages. Every listed URL must expose the same HU / EN / DE / x-default alternate set.
4. `robots.txt` must contain the canonical sitemap location: `Sitemap: https://axiona.systems/sitemap.xml`.
5. Every active page needs a non-empty `<title>` and meta description and must remain indexable unless there is a deliberate documented decision to change that.
6. `lastmod` is only changed when the page itself changed materially. Never use a fake current date merely to attract recrawling.
7. A renamed, added or removed public page requires the route matrix, sitemap and automated verifiers to be changed in the same release.
8. Visible copy, title and meta description must describe the same current positioning. Do not leave search metadata on an old product or company description after changing the page.
9. Inactive FR / ES / IT URLs and legacy redirect routes must not re-enter the active sitemap.
10. The Keeper triplet must expose self-referencing canonicals and reciprocal HU / EN / DE / x-default alternates.

## 8. Static fail-closed release gates

Run locally before a website release:

```bash
python3 scripts/verify_seo.py
python3 scripts/verify_public_quality.py
```

`verify_seo.py` protects the active route graph, sitemap, canonical URLs, language relationships, page metadata and robots sitemap pointer.

`verify_public_quality.py` protects, among other things:

- inactive-language removal
- legacy redirect-shell invariants
- removed legacy assets
- active local links and assets
- forbidden old public markers
- local-only contact-intake behavior
- compact mobile-navigation behavior
- Keeper status/planned-feature markers and entry-point links
- `security.txt`
- current manifest references

Both are executed by `.github/workflows/axiona-repo-guard.yml`.

The repository guard also checks for:

- legacy global rule anchors
- junk artifacts
- obvious private-key material
- diff whitespace errors

The gate fails closed: a blocked invariant must be fixed instead of being bypassed for a routine website release.

## 9. Browser-level quality gate

`.github/workflows/axiona-browser-audit.yml` provides a real-browser quality check on relevant pull requests.

### Lighthouse baseline

Representative HU routes:

- `/`
- `/systems.html`
- `/process.html`
- `/security.html`
- `/solutions.html`
- `/keeper.html`
- `/contact.html`

Current thresholds:

- Performance: `>= 0.80` — warning during baseline adoption
- Accessibility: `>= 0.90` — blocking
- Best Practices: `>= 0.90` — blocking
- SEO: `>= 0.90` — blocking

### axe WCAG baseline

The axe audit covers the core HU routes, the EN and DE homepages, and all three Keeper language pages. Critical or serious WCAG findings are blocking.

The first real browser run found genuine contrast defects in badges, navigation and security/system metadata. Those defects were corrected. The final validation run passed both Lighthouse and axe.

Do not lower the browser thresholds merely to make a failing pull request green. Fix the underlying regression unless a documented standards decision justifies a threshold change.

## 10. CI security baseline

The browser and repository workflows are part of the software supply chain and must be treated as production code.

Current hardening rules:

1. Use job-level least-privilege GitHub Actions permissions.
2. Checkout is pinned to a full action commit SHA.
3. Checkout credentials are not persisted.
4. The browser audit avoids unnecessary external setup actions.
5. Browser-audit npm packages are version-pinned.
6. npm lifecycle scripts are disabled for the audit installation with `--ignore-scripts`.
7. Browser audit reports remain inside CI and are not uploaded to a public third-party storage target by the workflow.

The final P0 / P2 / P3 / P4 validation passed the SonarQube Cloud Quality Gate with **0 Security Hotspots**. Sonar reported one non-blocking new issue at that validation point; a future maintenance pass may address it, but it did not fail the configured quality gate.

## 11. Mandatory release sequence

1. Start from current `origin/main`.
2. Make one bounded, reviewable change set.
3. If a route, language relationship, title or search description changes, update the matching SEO metadata and sitemap in the same work unit.
4. Run:

```bash
python3 scripts/verify_seo.py
python3 scripts/verify_public_quality.py
```

5. Preview changed pages on desktop and mobile when the change is visual or interactive.
6. Open a pull request.
7. Require AXIONA Repo Guard to pass.
8. For changes covered by the browser-audit path filters, require Lighthouse + axe to pass.
9. Do not merge a SonarQube security failure. Investigate and correct the root cause.
10. Merge only after the applicable gates are green.
11. Verify `main` contains the exact intended files after merge.
12. Verify the live deployment separately. Repository success is not deployment proof.

## 12. Live deployment proof

After merge, verify the public edge directly. Minimum proof set:

```bash
curl -fsSL https://axiona.systems/ | grep -Ei 'canonical|hreflang|<title>|description'
curl -fsSL https://axiona.systems/en/ | grep -Ei 'canonical|hreflang|<title>|description'
curl -fsSL https://axiona.systems/de/ | grep -Ei 'canonical|hreflang|<title>|description'
curl -fsSL https://axiona.systems/keeper.html | grep -E 'AXIONA KEEPER|FEJLESZTÉS ALATT|keeper.html'
curl -fsSL https://axiona.systems/en/keeper.html | grep -E 'AXIONA KEEPER|IN DEVELOPMENT|keeper.html'
curl -fsSL https://axiona.systems/de/keeper.html | grep -E 'AXIONA KEEPER|IN ENTWICKLUNG|keeper.html'
curl -fsSL https://axiona.systems/contact.html | grep -F 'Írd le, mi működik nehezen. A technológiát ráérünk később kiválasztani.'
curl -fsSL https://axiona.systems/.well-known/security.txt
curl -fsSL https://axiona.systems/applications.html | grep -F 'https://axiona.systems/solutions.html'
curl -fsSL https://axiona.systems/sitemap.xml | grep -F 'keeper.html'
curl -fsSL https://axiona.systems/robots.txt
```

A release is **not live-proof complete** until the public site returns the expected current content. A stale CDN/cache/web-fetch result must be reported as unverified instead of being called a successful deploy.

### 12.1 Pages publishing-source incident — 2026-08-19

During the HU / EN / DE copy-hardening release, the repository `main` passed all required gates and contained the intended pages, but the public edge continued to return older HTML. The live Hungarian overview and Contact content matched the obsolete `feature/r86-premium-sharing` branch exactly, while `main` already contained the newer release.

Operational repair performed:

1. The previous `feature/r86-premium-sharing` tip was preserved as `archive/r86-pages-source-pre-copy-20260819`.
2. `feature/r86-premium-sharing` was then synchronized to the validated `main` merge commit as a reversible deployment bridge.
3. `main` remains the only canonical source of truth. Do not develop, edit or treat the R86 branch as a second source of truth.

Permanent release rule:

- GitHub Pages should be configured to publish directly from `main` (or from a GitHub Actions Pages deployment whose source is `main`).
- Until that repository Pages setting is explicitly corrected, any release is incomplete if the public edge still reflects the old R86 deployment state.
- Do not solve future stale deployments by editing old public branches independently. First prove the deployment source, preserve any old ref that must be retained, and keep the published content aligned with validated `main`.

## 13. Google result expectations

Deployment and Google Search results are separate states. A successful site deployment does **not** immediately replace Google's cached title or snippet. Recrawling and re-indexing are asynchronous, and Google may generate a search snippet from visible page content instead of using the meta description verbatim.

When homepage title/description/positioning changes, use Google Search Console URL Inspection for `/`, `/en/` and `/de/` and request indexing. When the route structure changes, inspect/resubmit `sitemap.xml` in Search Console as well. Keeper is a new indexable route triplet, so the updated sitemap should be resubmitted after the live release is proven.

## 14. Change-control rule

Do not treat the following as incidental files or presentation details:

- `sitemap.xml`
- canonical URLs
- language alternates
- Keeper development-status wording
- `robots.txt`
- legacy redirect shells
- contact-intake privacy behavior
- `security.txt`
- CI workflow permissions and action pinning
- Lighthouse / axe thresholds
- Pages publishing source

They are part of the AXIONA public website contract and must be reviewed whenever the relevant site structure, behavior or deployment architecture changes.

## 15. Current continuation point

Canonical continuation point after this hardening pass:

- repository: `axiona-systems/axiona-site`
- branch: `main`
- completed scope: **P0 + P2 + P3 + P4 + HU/EN/DE public copy hardening + Keeper R87 product preview**
- deferred scope: **P1 completed references / case studies**

P1 stays deferred until a genuinely presentable completed AXIONA application exists. The Keeper preview is intentionally labelled as in development and must not be treated as a completed reference until the product actually reaches that state.
