# AXIONA SITE R70 — Apple Privacy Notice / App Store URL preparation

Date: 2026-05-03
Package: AXIONA_SITE_PUBLIC_R70_APPLE_PRIVACY_NOTICE.zip
CSS version: styles.css?v=70

## Purpose

R70 replaces the short privacy page with a real public privacy notice suitable as an App Store Privacy Policy URL for AXIONA apps that link to it.

## What changed

- Rebuilt HU privacy.html as a full privacy notice.
- Rebuilt EN privacy.html as Privacy Policy.
- Rebuilt DE privacy.html as Datenschutzerklärung.
- Added app/software scope, controller contact, website logs, support data, local-first app data, diagnostics, App Store/payment handling, legal bases, retention, service providers, user rights, privacy request route and security note.
- Global cache bump applied to styles.css?v=70.
- No backend form submission introduced.
- No analytics/tracking script introduced.
- No internal engineering details exposed.

## App Store use

Recommended Privacy Policy URL for App Store Connect:

https://axiona.systems/privacy.html

Optional User Privacy Choices URL:

https://axiona.systems/privacy.html#privacy-requests

## Required operational follow-up

Before every App Store submission, App Store Connect privacy answers must match the actual app build, including third-party SDKs and Apple/Xcode privacy report. If accounts, cloud sync, payments, subscriptions, crash SDKs or network features are added, update both this page and the App Store privacy answers.

## Proof markers

- OK_R70_PRIVACY_HU
- OK_R70_PRIVACY_EN
- OK_R70_PRIVACY_DE
- OK_NO_FORM_POST
- OK_NO_AD_TRACKING_SCRIPT
- OK_CSS_V70
