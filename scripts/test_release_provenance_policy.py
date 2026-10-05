#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("verify_release_provenance_policy.py")
SPEC = importlib.util.spec_from_file_location("verify_release_provenance_policy", MODULE_PATH)
assert SPEC and SPEC.loader
POLICY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(POLICY)


class ReleaseProvenancePolicyTests(unittest.TestCase):
    def test_repository_policy_is_valid(self) -> None:
        result = POLICY.verify()
        self.assertEqual(len(result["identity_sha256"]), 64)
        self.assertEqual(len(result["product_policy_sha256"]), 64)
        self.assertEqual(len(result["trust_policy_sha256"]), 64)

    def test_private_key_or_caller_selected_key_cannot_be_admitted(self) -> None:
        trust = POLICY.load(POLICY.TRUST_PATH)
        changed = copy.deepcopy(trust)
        changed["caller_selected_keys"] = True
        with self.assertRaises(POLICY.PolicyError):
            POLICY.validate_trust(changed)
        changed = copy.deepcopy(trust)
        changed["private_key_in_repository"] = True
        with self.assertRaises(POLICY.PolicyError):
            POLICY.validate_trust(changed)

    def test_key_digest_and_algorithm_drift_fail_closed(self) -> None:
        trust = POLICY.load(POLICY.TRUST_PATH)
        changed = copy.deepcopy(trust)
        changed["keys"][0]["public_key_der_sha256"] = "0" * 64
        with self.assertRaises(POLICY.PolicyError):
            POLICY.validate_trust(changed)
        changed = copy.deepcopy(trust)
        changed["keys"][0]["algorithm"] = "RSA"
        with self.assertRaises(POLICY.PolicyError):
            POLICY.validate_trust(changed)

    def test_production_and_release_mutation_stay_closed(self) -> None:
        policy = POLICY.load(POLICY.POLICY_PATH)
        changed = copy.deepcopy(policy)
        changed["admitted_environments"] = ["NON_PRODUCTION", "PRODUCTION"]
        with self.assertRaises(POLICY.PolicyError):
            POLICY.validate_policy(changed)
        changed = copy.deepcopy(policy)
        changed["release_mutation_authority"] = True
        with self.assertRaises(POLICY.PolicyError):
            POLICY.validate_policy(changed)


if __name__ == "__main__":
    unittest.main()
