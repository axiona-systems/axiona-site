# AXIONA R143 candidate validation

- candidate: `agent/r143-repo-cleanup-hardening`
- expected head: `58cc64a90c6eb4f6b291f5996e45ae69f198dc63`
- result: **FAIL**

```text
CANDIDATE_HEAD=58cc64a90c6eb4f6b291f5996e45ae69f198dc63
=== verify_site ===
OK_AXIONA_PUBLIC_SURFACE
PASS verify_site
=== verify_sitemap ===
OK_AXIONA_SITEMAP_HREFLANG
SITEMAP_URLS=30
SITEMAP_HREFLANG_LINKS=120
PASS verify_sitemap
=== verify_security_txt ===
OK_AXIONA_SECURITY_TXT_RFC9116
PASS verify_security_txt
=== verify_social ===
OK_AXIONA_SOCIAL_METADATA_R132
PASS verify_social
=== verify_retired_routes ===
OK_AXIONA_RETIRED_ROUTES_R133=20
PASS verify_retired_routes
=== verify_browser_identity ===
OK_AXIONA_BROWSER_IDENTITY_R134=31
PASS verify_browser_identity
=== verify_asset_references ===
STOP_AXIONA_ASSET_REFERENCES
- assets/js/share-r86.js: missing local asset assets/motion-r108.css
- assets/multipage-r78.css: missing local asset assets/multipage-r74.css
- assets/multipage-r78.css: missing local asset assets/motion-r105.css
FAIL verify_asset_references exit=1
=== verify_workflow_hardening ===
OK_AXIONA_WORKFLOW_HARDENING workflows=4 actions=immutable permissions=least-privilege
PASS verify_workflow_hardening
=== diff_check ===
fatal: ambiguous argument 'HEAD~1': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
FAIL diff_check exit=128
PASS chrome_runtime=/usr/bin/google-chrome-stable
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated glob@7.2.3: Old versions of glob are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me
npm warn deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
npm warn deprecated rimraf@2.7.1: Rimraf versions prior to v4 are no longer supported
npm warn deprecated uuid@8.3.2: uuid@10 and below is no longer supported.  For ESM codebases, update to uuid@latest.  For CommonJS codebases, use uuid@11 (but be aware this version will likely be deprecated in 2028).

added 331 packages in 11s
PASS npm_runtime
✅  .lighthouseci/ directory writable
✅  Configuration file found
✅  Chrome installation found
⚠️   GitHub token not set
Healthcheck passed!

Started a web server on port 42647...
Running Lighthouse 1 time(s) on http://localhost:42647/
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/systems.html
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/process.html
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/security.html
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/solutions.html
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/keeper.html
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/contact.html
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/support.html
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/privacy.html
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/legal.html
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/en/
Run #1...done.
Running Lighthouse 1 time(s) on http://localhost:42647/de/
Run #1...done.
Done running Lighthouse!

Checking assertions against 12 URL(s), 12 total run(s)

All results processed!

Dumping 12 reports to disk at /home/runner/work/axiona-site/axiona-site/candidate/.lighthouseci/reports...
Done writing reports to disk.

Done running autorun.
PASS lighthouse
file:///home/runner/work/axiona-site/axiona-site/candidate/scripts/verify_render_contract.mjs:5
if (!chromePath) throw new Error('STOP_AXIONA_RENDER_CHROME_MISSING');
                       ^

Error: STOP_AXIONA_RENDER_CHROME_MISSING
    at file:///home/runner/work/axiona-site/axiona-site/candidate/scripts/verify_render_contract.mjs:5:24
    at ModuleJob.run (node:internal/modules/esm/module_job:343:25)
    at async onImport.tracePromise.__proto__ (node:internal/modules/esm/loader:681:26)
    at async asyncRunEntryPointWithESMLoader (node:internal/modules/run_main:117:5)

Node.js v22.23.2
FAIL render_contract exit=1
STOP_AXIONA_AXE_CHROME_PATH_MISSING
FAIL axe exit=2
RESULT=FAIL
```
