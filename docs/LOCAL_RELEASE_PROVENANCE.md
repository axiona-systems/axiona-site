# Local release provenance for isolated HTTP proof

This repository may publish **public trust metadata** for the isolated
non-production HTTP proof without publishing private signing material or private
infrastructure details.

The candidate policy is:

`.axiona/release-provenance-policy.v1.json`

It binds exactly:

- product identity `axiona-systems/axiona-site` / `axiona-site`;
- source `ee17a4cddb08073613d5ddf7c1dd6283e3f9c51e`;
- `STATIC_BUNDLE` artifact semantics;
- the product-owned `./scripts/verify-all.sh` verifier;
- the already-reviewed local public-artifact recipe by exact repository,
  revision, path and Git blob identity;
- one public Ed25519 provenance key.

The public key is trust metadata. The private key is deliberately absent from
this repository and from ordinary provenance/request payloads. Possession of the
private key alone grants no release, deployment or production authority.

A signed CF-C12 provenance statement remains evidence only until an independent
Verifier resolves this exact policy, authenticates the source and referenced
proofs, verifies the Ed25519 signature, and emits the separately admitted
candidate-evidence context.

This policy is intentionally scoped to the isolated non-production proof.
GitHub Pages publication, DNS/TLS, live-site mutation and production activation
are outside this policy.

`PRODUCTION_ACTIVATION=BLOCKED`
