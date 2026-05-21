# AXIONA CI P1 Adoption Pointer

Status: active
Repository: axiona-systems/axiona-site
Central governance repository: axiona-systems/AXIONA_CI

AXIONA_CI_ADOPTION_POINTER=TRUE
CENTRAL_GOVERNANCE_REPO=axiona-systems/AXIONA_CI
AXIONA_CI_RULES_INDEX=Docs/Rules/00_AXIONA_RULES_INDEX.md
NO_LOCAL_RULE_DUPLICATION=TRUE

## Purpose

This repository adopts AXIONA_CI as the central governance and rule source of truth.
Product repositories must not copy AXIONA_CI tools, schemas, or config locally.

## Closed authority boundary

NO_LOCAL_AXIONA_CI_TOOL_COPY
NO_LOCAL_AXIONA_CI_SCHEMA_COPY
NO_LOCAL_AXIONA_CI_CONFIG_COPY
NO_BRANCH_PROTECTION_MUTATION
NO_AUTO_REPAIR
NO_AUTO_ROLLBACK
NO_AUTONOMOUS_APPLY
NO_RELEASE_AUTHORITY
NO_DEPLOY_AUTHORITY
NO_SECRET_ACCESS_AUTHORITY
NO_MULTI_AGENT_EXECUTION_GRAPH

## Final marker

OK_SITE_AXIONA_CI_P1_ADOPTION_POINTER_V0_1
