#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

python3 scripts/verify_site.py
python3 scripts/verify_sitemap_hreflang.py
python3 scripts/verify_security_txt.py
python3 scripts/verify_social_metadata.py
python3 scripts/verify_retired_routes.py
python3 scripts/verify_browser_identity.py
python3 scripts/verify_asset_references.py
python3 scripts/verify_workflow_hardening.py

if git rev-parse --verify HEAD~1 >/dev/null 2>&1; then
  git diff --check HEAD~1 HEAD
fi

echo "AXIONA_SITE_VERIFY_ALL_OK"
