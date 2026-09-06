# AXIONA Brand Consumer Boundary

Status: **CURRENT CONSUMER PROVENANCE**

`axiona-systems/axiona-site` is a public presentation/runtime consumer of AXIONA identity. It is not the authority for AXIONA master brand geometry, brand rules, export tooling, or system-level brand governance.

## System authority

The canonical system-level brand authority is the private repository:

`axiona-systems/AXIONA_BRAND`

Authority-migration baseline:

`aebf0f112bd5f4e589ef58f337a55d9be861b493`

Canonical source object identities at that baseline:

- complete master SVG Git blob: `374cc2f8738cb0abd519016cac2759b1cc43be0d`
- standalone symbol SVG Git blob: `1fbe0628bf1d6240495da75dfab2b51a28aac391`

The byte-identical authority move from this repository is recorded in the private authority repository. Historical `axiona-site` commits remain immutable migration evidence only; they are not active brand authority.

## Public runtime boundary

The site must retain only assets required for its public runtime, browser identity, PWA identity, social previews, and presentation surface. Current runtime bindings remain unchanged by the authority migration.

Examples of current runtime consumer assets include:

- `assets/axiona-mark.png`
- `favicon.svg`
- `favicon-16x16.png`
- `favicon-32x32.png`
- `favicon.ico`
- `apple-touch-icon.png`
- `assets/brand/axiona-icon-192.png`
- `assets/brand/axiona-icon-512.png`

These files are consumer/runtime assets. They do not become master sources merely because the public site needs to serve them.

## Separation invariants

The public site repository must not contain an active AXIONA master-authority directory, master-logo export workflow, or master-authority verifier. Brand generation and master validation belong to `AXIONA_BRAND`.

A future replacement of current site runtime assets with derivatives from the new master is a separate tested consumer migration. That change must preserve browser/public-surface behavior and is not implied by this authority move.
