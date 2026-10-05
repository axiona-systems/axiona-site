#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / ".axiona/release-provenance-policy.v1.json"


class ReleaseProvenancePolicyTests(unittest.TestCase):
    def load(self) -> dict:
        return json.loads(POLICY.read_text(encoding="utf-8"))

    def test_policy_is_exact_nonproduction_and_non_authorizing(self) -> None:
        value = self.load()
        self.assertEqual(
            set(value),
            {
                "schema_version",
                "policy_id",
                "subject_id",
                "repository",
                "scope",
                "signing",
                "private_key_repository_custody",
                "private_key_payload_custody",
                "release_authority",
                "deployment_authority",
                "production_activation",
                "authority_effect",
            },
        )
        self.assertEqual(value["schema_version"], "axiona.site.nonproduction-provenance-policy.v1")
        self.assertEqual(value["policy_id"], "axiona-site-isolated-http-proof-v1")
        self.assertEqual(value["subject_id"], "axiona-site")
        self.assertEqual(value["repository"], "axiona-systems/axiona-site")
        self.assertFalse(value["private_key_repository_custody"])
        self.assertFalse(value["private_key_payload_custody"])
        self.assertEqual(value["release_authority"], "NONE")
        self.assertEqual(value["deployment_authority"], "NONE")
        self.assertEqual(value["production_activation"], "BLOCKED")
        self.assertEqual(value["authority_effect"], "PRODUCT_POLICY_ONLY")

        scope = value["scope"]
        self.assertEqual(scope["environment"], "NON_PRODUCTION")
        self.assertEqual(scope["source_sha"], "ee17a4cddb08073613d5ddf7c1dd6283e3f9c51e")
        self.assertEqual(scope["artifact_kind"], "STATIC_BUNDLE")
        self.assertEqual(scope["product_verifier"], "./scripts/verify-all.sh")

    def test_public_ed25519_key_is_exact_and_private_material_absent(self) -> None:
        value = self.load()
        signing = value["signing"]
        self.assertEqual(signing["algorithm"], "ED25519")
        self.assertEqual(signing["public_key_id"], "axiona-site-provenance-v1")
        self.assertEqual(signing["public_key_format"], "SPKI_DER_BASE64")
        self.assertEqual(signing["status"], "ACTIVE")
        self.assertEqual(signing["revocation_state"], "NOT_REVOKED")
        raw = base64.b64decode(signing["public_key_der_base64"], validate=True)
        self.assertEqual(
            hashlib.sha256(raw).hexdigest(),
            signing["public_key_der_sha256"],
        )
        text = POLICY.read_text(encoding="utf-8")
        for forbidden in (
            "BEGIN PRIVATE KEY",
            "BEGIN OPENSSH PRIVATE KEY",
            "private-key.pem",
            "/Users/",
            "Hetzner",
            "91.99.",
        ):
            self.assertNotIn(forbidden, text)

    def test_artifact_recipe_binding_is_exact_git_blob(self) -> None:
        recipe = self.load()["scope"]["artifact_recipe"]
        self.assertEqual(recipe["repository"], "axiona-systems/axiona-site")
        row = subprocess.check_output(
            [
                "git",
                "-C",
                str(ROOT),
                "ls-tree",
                recipe["revision"],
                "--",
                recipe["path"],
            ],
            text=True,
        ).strip()
        fields = row.split()
        self.assertGreaterEqual(len(fields), 4)
        self.assertEqual(fields[0], "100755")
        self.assertEqual(fields[1], "blob")
        self.assertEqual(fields[2], recipe["git_blob_sha1"])


if __name__ == "__main__":
    unittest.main()
