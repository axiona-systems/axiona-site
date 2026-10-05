#!/usr/bin/env python3
"""Verify public release/provenance policy for axiona-site; no secret access."""
from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDENTITY_PATH = ROOT / ".axiona" / "release-subject-identity.v1.json"
POLICY_PATH = ROOT / ".axiona" / "release-policy.v1.json"
TRUST_PATH = ROOT / ".axiona" / "release-provenance-trust.v1.json"

ED25519_SPKI_PREFIX = bytes.fromhex("302a300506032b6570032100")


class PolicyError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PolicyError(message)


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"{path.name}: object required")
    return value


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_keys(value: dict, keys: set[str], label: str) -> None:
    require(set(value) == keys, f"{label}: unknown or missing fields")


def validate_identity(value: dict) -> None:
    exact_keys(value, {
        "schema_version", "subject_id", "repository", "product_truth_capability",
        "artifact_kind", "product_verifier", "authority_effect",
        "production_activation",
    }, "identity")
    require(value["schema_version"] == "axiona.site.release-subject-identity.v1", "identity schema")
    require(value["subject_id"] == "axiona-site", "identity subject")
    require(value["repository"] == "axiona-systems/axiona-site", "identity repository")
    require(value["product_truth_capability"] == "public-site-product-truth", "identity capability")
    require(value["artifact_kind"] == "STATIC_BUNDLE", "identity artifact kind")
    require(value["product_verifier"] == "./scripts/verify-all.sh", "identity verifier")
    require(value["authority_effect"] == "IDENTITY_ONLY", "identity authority")
    require(value["production_activation"] == "BLOCKED", "identity production")


def validate_trust(value: dict) -> None:
    exact_keys(value, {
        "schema_version", "product_repository", "contract", "keys",
        "caller_selected_keys", "private_key_in_repository",
        "authority_effect", "production_activation",
    }, "trust")
    require(value["schema_version"] == "axiona.site.release-provenance-trust.v1", "trust schema")
    require(value["product_repository"] == "axiona-systems/axiona-site", "trust repository")
    require(value["contract"] == {
        "id": "axiona.release-provenance.v1",
        "release": "0.1.0",
    }, "trust contract")
    require(value["caller_selected_keys"] is False, "caller key selection")
    require(value["private_key_in_repository"] is False, "private key repository boundary")
    require(value["authority_effect"] == "PUBLIC_TRUST_POLICY_ONLY", "trust authority")
    require(value["production_activation"] == "BLOCKED", "trust production")
    require(isinstance(value["keys"], list) and len(value["keys"]) == 1, "one provenance key required")
    key = value["keys"][0]
    exact_keys(key, {
        "public_key_id", "algorithm", "public_key_der_base64",
        "public_key_der_sha256", "scope", "state",
    }, "trust key")
    require(key["public_key_id"] == "axiona-site-provenance-v1", "key id")
    require(key["algorithm"] == "ED25519", "key algorithm")
    require(key["scope"] == "RELEASE_PROVENANCE_ONLY", "key scope")
    require(key["state"] == "ACTIVE", "key state")
    try:
        raw = base64.b64decode(key["public_key_der_base64"], validate=True)
    except ValueError as exc:
        raise PolicyError("public key base64") from exc
    require(
        len(raw) == len(ED25519_SPKI_PREFIX) + 32
        and raw.startswith(ED25519_SPKI_PREFIX),
        "public key is not canonical Ed25519 SubjectPublicKeyInfo",
    )
    require(
        hashlib.sha256(raw).hexdigest() == key["public_key_der_sha256"],
        "public key digest mismatch",
    )
    require(
        key["public_key_der_sha256"]
        == "ae70cadecfa3e6e0eaefb6f45512dbb50c42f285f0cad02a498411bb8474962c",
        "admitted public key digest drift",
    )


def validate_policy(value: dict) -> None:
    exact_keys(value, {
        "schema_version", "subject_id", "repository", "candidate_artifact_kind",
        "source_identity", "product_verifier", "provenance_contract",
        "provenance_trust_policy", "admitted_environments",
        "production_human_authority_required", "release_mutation_authority",
        "authority_effect", "production_activation",
    }, "release policy")
    require(value["schema_version"] == "axiona.site.release-policy.v1", "policy schema")
    require(value["subject_id"] == "axiona-site", "policy subject")
    require(value["repository"] == "axiona-systems/axiona-site", "policy repository")
    require(value["candidate_artifact_kind"] == "STATIC_BUNDLE", "policy artifact")
    require(value["source_identity"] == "EXACT_GIT_COMMIT_REQUIRED", "policy source")
    require(value["product_verifier"] == "./scripts/verify-all.sh", "policy verifier")
    require(value["provenance_contract"] == "axiona.release-provenance.v1@0.1.0", "policy contract")
    require(value["provenance_trust_policy"] == ".axiona/release-provenance-trust.v1.json", "policy trust path")
    require(value["admitted_environments"] == ["NON_PRODUCTION"], "policy environment")
    require(value["production_human_authority_required"] is True, "policy human boundary")
    require(value["release_mutation_authority"] is False, "policy cannot grant mutation")
    require(value["authority_effect"] == "PRODUCT_POLICY_ONLY", "policy authority")
    require(value["production_activation"] == "BLOCKED", "policy production")


def verify() -> dict[str, str]:
    identity = load(IDENTITY_PATH)
    policy = load(POLICY_PATH)
    trust = load(TRUST_PATH)
    validate_identity(identity)
    validate_policy(policy)
    validate_trust(trust)
    joined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (IDENTITY_PATH, POLICY_PATH, TRUST_PATH)
    )
    for forbidden in (
        "BEGIN PRIVATE KEY",
        "BEGIN OPENSSH PRIVATE KEY",
        "private_key_path",
        "/Users/",
        "credential",
        "secret_value",
        "91.99.",
        "hetzner",
    ):
        require(forbidden.casefold() not in joined.casefold(), f"forbidden private/infra material: {forbidden}")
    return {
        "identity_sha256": file_sha256(IDENTITY_PATH),
        "product_policy_sha256": file_sha256(POLICY_PATH),
        "trust_policy_sha256": file_sha256(TRUST_PATH),
    }


def main() -> int:
    try:
        result = verify()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"STOP_AXIONA_SITE_RELEASE_PROVENANCE_POLICY: {exc}")
        return 1
    print(f"AXIONA_SITE_RELEASE_SUBJECT_IDENTITY_SHA256={result['identity_sha256']}")
    print(f"AXIONA_SITE_RELEASE_PRODUCT_POLICY_SHA256={result['product_policy_sha256']}")
    print(f"AXIONA_SITE_RELEASE_PROVENANCE_TRUST_SHA256={result['trust_policy_sha256']}")
    print("AXIONA_SITE_RELEASE_PROVENANCE_PUBLIC_KEY_DER_SHA256=ae70cadecfa3e6e0eaefb6f45512dbb50c42f285f0cad02a498411bb8474962c")
    print("AXIONA_SITE_RELEASE_PROVENANCE_POLICY_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
