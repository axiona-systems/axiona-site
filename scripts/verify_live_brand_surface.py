#!/usr/bin/env python3
"""Verify the AXIONA R147 brand surface against the exact checked-out source."""
from __future__ import annotations

import argparse
import hashlib
import http.client
import ssl
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADER = "/assets/brand/axiona-horizontal-fullcolor.svg"
FOOTER = "/assets/brand/axiona-horizontal-monochrome-white.svg"
SYMBOL = "/assets/brand/axiona-symbol-fullcolor.svg"
LIVE_HOST = "axiona.systems"
LOCAL_HOST = "127.0.0.1"
LOCAL_PORT = 4176

ROOT_ROUTES = (
    "/",
    "/systems.html",
    "/process.html",
    "/security.html",
    "/solutions.html",
    "/contact.html",
    "/support.html",
    "/keeper.html",
    "/privacy.html",
    "/legal.html",
)
EN_ROUTES = tuple("/en/" if route == "/" else "/en" + route for route in ROOT_ROUTES)
DE_ROUTES = tuple("/de/" if route == "/" else "/de" + route for route in ROOT_ROUTES)
PUBLIC_ROUTES = ROOT_ROUTES + EN_ROUTES + DE_ROUTES + ("/404.html",)
KEEPER_ROUTES = {"/keeper.html", "/en/keeper.html", "/de/keeper.html"}

ACTIVE_ASSETS = (
    "/assets/brand/axiona-horizontal-fullcolor.svg",
    "/assets/brand/axiona-horizontal-monochrome-white.svg",
    "/assets/brand/axiona-symbol-fullcolor.svg",
    "/favicon.svg",
    "/favicon-16x16.png",
    "/favicon-32x32.png",
    "/favicon.ico",
    "/apple-touch-icon.png",
    "/assets/brand/axiona-icon-192.png",
    "/assets/brand/axiona-icon-512.png",
    "/assets/social/axiona-social-preview-r147-hu.png",
    "/assets/social/axiona-social-preview-r147-en.png",
    "/assets/social/axiona-social-preview-r147-de.png",
    "/assets/social/axiona-keeper-social-preview-r147-hu.png",
    "/assets/social/axiona-keeper-social-preview-r147-en.png",
    "/assets/social/axiona-keeper-social-preview-r147-de.png",
    "/site.webmanifest",
)

STALE_ASSETS = (
    "/assets/axiona-mark.png",
    "/assets/social/axiona-social-preview-r92-hu.png",
    "/assets/social/axiona-social-preview-r92-en.png",
    "/assets/social/axiona-social-preview-r92-de.png",
    "/assets/social/axiona-keeper-social-preview-r92-hu.png",
    "/assets/social/axiona-keeper-social-preview-r92-en.png",
    "/assets/social/axiona-keeper-social-preview-r92-de.png",
)


def fail(message: str) -> None:
    print(f"STOP_AXIONA_LIVE_BRAND_SURFACE: {message}")
    raise SystemExit(1)


def local_bytes(route: str) -> bytes:
    path = ROOT / route.lstrip("/")
    if not path.is_file():
        fail(f"local reference missing: {route}")
    return path.read_bytes()


def verified_tls_context() -> ssl.SSLContext:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_default_certs(ssl.Purpose.SERVER_AUTH)
    return context


def new_connection(mode: str) -> http.client.HTTPConnection:
    if mode == "live":
        return http.client.HTTPSConnection(
            LIVE_HOST,
            443,
            timeout=15,
            context=verified_tls_context(),
        )
    return http.client.HTTPConnection(LOCAL_HOST, LOCAL_PORT, timeout=15)


def fetch(mode: str, route: str, key: str, *, expected_status: int = 200) -> bytes:
    target = f"{route}?axiona_verify={key}"
    last_error: Exception | None = None
    for attempt in range(1, 4):
        connection = new_connection(mode)
        try:
            connection.request(
                "GET",
                target,
                headers={
                    "Cache-Control": "no-cache",
                    "Pragma": "no-cache",
                    "User-Agent": "AXIONA-Pages-Brand-Verifier/1.2",
                },
            )
            response = connection.getresponse()
            status = response.status
            body = response.read()
            if status != expected_status:
                raise RuntimeError(f"status={status} expected={expected_status}")
            return body
        except Exception as exc:  # noqa: BLE001 - network boundary is intentionally broad
            last_error = exc
        finally:
            connection.close()
        if attempt < 3:
            time.sleep(1)
    fail(f"fetch failed: {route}: {last_error}")
    return b""


def expected_social(route: str) -> str | None:
    if route == "/404.html":
        return None
    if route.startswith("/en/"):
        locale = "en"
    elif route.startswith("/de/"):
        locale = "de"
    else:
        locale = "hu"
    keeper = route in KEEPER_ROUTES
    stem = "axiona-keeper-social-preview-r147" if keeper else "axiona-social-preview-r147"
    return f"/assets/social/{stem}-{locale}.png"


def verify_primary_identity(route: str, html: str) -> None:
    if f'src="{HEADER}"' not in html:
        fail(f"header brand missing: {route}")
    if f'src="{FOOTER}"' not in html:
        fail(f"footer brand missing: {route}")
    if "/assets/axiona-mark.png" in html or "r92-" in html:
        fail(f"legacy brand binding present: {route}")


def verify_symbol_placement(route: str, html: str) -> None:
    has_symbol = f'src="{SYMBOL}"' in html
    if route in KEEPER_ROUTES and not has_symbol:
        fail(f"Keeper standalone symbol missing: {route}")
    if route not in KEEPER_ROUTES and has_symbol:
        fail(f"unexpected standalone symbol placement: {route}")


def verify_social_binding(route: str, html: str) -> None:
    social = expected_social(route)
    if social and social not in html:
        fail(f"locale social card mismatch: {route} expected={social}")


def verify_html(mode: str, key: str) -> None:
    for route in PUBLIC_ROUTES:
        html = fetch(mode, route, key).decode("utf-8", errors="strict")
        verify_primary_identity(route, html)
        verify_symbol_placement(route, html)
        verify_social_binding(route, html)
    print(f"OK_AXIONA_LIVE_BRAND_HTML routes={len(PUBLIC_ROUTES)}")


def verify_asset_bytes(mode: str, key: str) -> None:
    for route in ACTIVE_ASSETS:
        expected = local_bytes(route)
        actual = fetch(mode, route, key)
        expected_hash = hashlib.sha256(expected).hexdigest()
        actual_hash = hashlib.sha256(actual).hexdigest()
        if actual_hash != expected_hash:
            fail(f"asset hash mismatch: {route} expected={expected_hash} actual={actual_hash}")
    print(f"OK_AXIONA_LIVE_BRAND_ASSET_HASHES assets={len(ACTIVE_ASSETS)}")


def verify_stale_absent(mode: str, key: str) -> None:
    for route in STALE_ASSETS:
        fetch(mode, route, key, expected_status=404)
    print(f"OK_AXIONA_LIVE_BRAND_STALE_ABSENT assets={len(STALE_ASSETS)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("local", "live"), required=True)
    args = parser.parse_args()
    key = f"r147-{time.time_ns()}"

    verify_html(args.mode, key)
    verify_asset_bytes(args.mode, key)
    verify_stale_absent(args.mode, key)
    print(f"AXIONA_LIVE_BRAND_SURFACE=PASS mode={args.mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
