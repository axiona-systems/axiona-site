#!/usr/bin/env python3
"""Validate AXIONA's /.well-known/security.txt contract against RFC 9116 + local policy."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
SECURITY_PATH = Path(".well-known/security.txt")
EXPECTED_CANONICAL = "https://axiona.systems/.well-known/security.txt"
EXPECTED_POLICY = "https://axiona.systems/security.html"
EXPECTED_LANGUAGES = {"hu", "en", "de"}
MAX_BYTES = 32 * 1024
MAX_EXPIRY_HORIZON = timedelta(days=366)
RFC3339 = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$"
)
FIELD_NAME = re.compile(r"^[A-Za-z0-9-]+$")


def parse_rfc3339(value: str) -> datetime | None:
    if not RFC3339.fullmatch(value):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def valid_contact(value: str) -> bool:
    parsed = urlsplit(value)
    scheme = parsed.scheme.lower()
    if scheme == "mailto":
        address = parsed.path
        return bool(address and "@" in address and address.rsplit("@", 1)[1].lower() == "axiona.systems")
    if scheme == "tel":
        return bool(parsed.path)
    if scheme == "https":
        return bool(parsed.hostname)
    return False


def parse_fields(text: str) -> tuple[dict[str, list[str]], list[str]]:
    fields: dict[str, list[str]] = {}
    errors: list[str] = []
    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"malformed field line {number}")
            continue
        name, value = line.split(":", 1)
        name = name.strip()
        value = value.strip()
        if not name or not FIELD_NAME.fullmatch(name):
            errors.append(f"invalid field name line {number}")
            continue
        if not value:
            errors.append(f"empty field value: {name}")
            continue
        fields.setdefault(name.lower(), []).append(value)
    return fields, errors


def verify(root: Path, now: datetime) -> list[str]:
    root = root.resolve()
    path = root / SECURITY_PATH
    errors: list[str] = []

    if not path.is_file():
        return ["missing .well-known/security.txt"]

    raw = path.read_bytes()
    if len(raw) > MAX_BYTES:
        errors.append(f"security.txt exceeds {MAX_BYTES} bytes")
    if b"\x00" in raw:
        errors.append("security.txt contains NUL byte")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return errors + ["security.txt is not valid UTF-8"]

    fields, parse_errors = parse_fields(text)
    errors.extend(parse_errors)

    contacts = fields.get("contact", [])
    if not contacts:
        errors.append("security.txt Contact missing")
    else:
        for value in contacts:
            if not valid_contact(value):
                errors.append(f"security.txt invalid Contact URI: {value}")

    expires_values = fields.get("expires", [])
    if len(expires_values) != 1:
        errors.append(f"security.txt Expires count: {len(expires_values)}, expected 1")
    else:
        expires = parse_rfc3339(expires_values[0])
        if expires is None:
            errors.append(f"security.txt invalid Expires RFC3339: {expires_values[0]}")
        else:
            now_utc = now.astimezone(timezone.utc)
            if expires <= now_utc:
                errors.append(f"security.txt expired: {expires_values[0]}")
            if expires - now_utc > MAX_EXPIRY_HORIZON:
                errors.append(f"security.txt Expires too far in future: {expires_values[0]}")

    canonicals = fields.get("canonical", [])
    if canonicals != [EXPECTED_CANONICAL]:
        errors.append(f"security.txt Canonical mismatch: {canonicals or '<missing>'}")
    elif urlsplit(canonicals[0]).scheme.lower() != "https":
        errors.append("security.txt Canonical must use https")

    policies = fields.get("policy", [])
    if policies != [EXPECTED_POLICY]:
        errors.append(f"security.txt Policy mismatch: {policies or '<missing>'}")
    elif urlsplit(policies[0]).scheme.lower() != "https":
        errors.append("security.txt Policy must use https")

    preferred = fields.get("preferred-languages", [])
    if len(preferred) != 1:
        errors.append(f"security.txt Preferred-Languages count: {len(preferred)}, expected 1")
    else:
        languages = [item.strip().lower() for item in preferred[0].split(",") if item.strip()]
        if len(languages) != len(set(languages)):
            errors.append("security.txt Preferred-Languages contains duplicates")
        if set(languages) != EXPECTED_LANGUAGES:
            errors.append(
                "security.txt Preferred-Languages mismatch: " + ", ".join(languages or ["<empty>"])
            )

    for field in ("expires", "canonical", "policy", "preferred-languages"):
        if len(fields.get(field, [])) > 1 and field != "expires":
            errors.append(f"security.txt duplicate singleton field: {field}")

    return errors


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    cli.add_argument(
        "--now",
        default=None,
        help="RFC3339 UTC/reference time for deterministic contract tests; defaults to current UTC time.",
    )
    args = cli.parse_args()

    if args.now:
        now = parse_rfc3339(args.now)
        if now is None:
            print(f"STOP_AXIONA_SECURITY_TXT: invalid --now RFC3339: {args.now}", file=sys.stderr)
            return 2
    else:
        now = datetime.now(timezone.utc)

    errors = verify(args.root, now)
    if errors:
        for error in errors:
            print(f"STOP_AXIONA_SECURITY_TXT: {error}", file=sys.stderr)
        return 1
    print("OK_AXIONA_SECURITY_TXT_RFC9116")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
