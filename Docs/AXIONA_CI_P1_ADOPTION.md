# AXIONA CI P1 Adoption

Status: active pointer
Repository: axiona-systems/axiona-site
Central source: axiona-systems/AXIONA_CI

This repository adopts the central AXIONA_CI P1 report-only safety foundation by reference.

Central guide:

```text
AXIONA_CI/Docs/Guides/AXIONA_CI_P1_PRODUCT_REPO_ADOPTION_GUIDE_v0_1.md
```

Central accepted baseline:

```text
P1_REPORT_ONLY_FOUNDATION=ACCEPTED
GITHUB_MAIN_BASELINE=OK
TRUSTED_LOCAL_MAC_PROOF=OK
```

Rules:

```text
CENTRAL_AXIONA_CI_TOOLS_REQUIRED=TRUE
NO_LOCAL_TOOL_COPY_BY_DEFAULT=TRUE
P1_REPORT_ONLY_FOUNDATION_ACTIVE=TRUE
NO_AUTOMATIC_REPAIR_AUTHORITY=TRUE
NO_AUTOMATIC_ROLLBACK_AUTHORITY=TRUE
NO_RELEASE_DEPLOY_RUNTIME_AUTHORITY_FROM_P1=TRUE
```
