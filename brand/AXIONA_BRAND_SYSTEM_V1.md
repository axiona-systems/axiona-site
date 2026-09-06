# AXIONA Brand System V1

Status: **CANONICAL REFERENCE**

This document records the AXIONA visual system that is currently accepted and physically represented by the public site. It is a brand reference, not a new redesign specification.

## 1. Brand character

AXIONA should read as an engineering/work-system brand rather than a generic SaaS dashboard.

Primary characteristics:

- structured;
- restrained;
- technical without decorative pseudo-technical noise;
- calm rather than flashy;
- functional hierarchy over ornament;
- visible system logic where it actually helps comprehension.

## 2. Canonical color tokens

Current live root tokens from `assets/styles-r71.css`:

| Token | Value | Role |
| --- | --- | --- |
| `paper` | `#f1eee6` | dominant page field |
| `paper-2` | `#e5dfd3` | secondary warm surface |
| `ink` | `#111917` | primary text / dark foreground |
| `muted` | `#5f665f` | secondary text |
| `line` | `#c8c2b7` | thin borders / separators |
| `navy` | `#0b1e25` | deep petrol control surface |
| `navy-2` | `#102c33` | secondary petrol surface |
| `cyan` | `#54d4ca` | secondary technical accent |
| `acid` | `#d7ef55` | compact status/control signal |
| `orange` | `#ef6b43` | active/control emphasis |
| `white` | `#fbfaf6` | light foreground / working surface |

Maximum main content width currently used by the base system: `1480px`.

### Color discipline

- Paper/off-white is the default field.
- Petrol is contained, not the default full-page background.
- Orange is deliberate and sparse.
- Acid green is a signal, not a general theme color.
- Cyan is secondary and technical.
- Avoid introducing additional brand colors without an explicit reason.

## 3. Typography

Current base sans-serif stack:

`Helvetica Neue, Aptos, Segoe UI, Arial, sans-serif`

Current editorial/contrast serif use:

`Georgia, Times New Roman, serif`

Current technical labels frequently use the platform `monospace` stack.

### Typography rules

- Main UI/body text stays sans-serif.
- Serif is used selectively for editorial/document contrast, not as the default UI font.
- Monospace is for compact technical metadata, coordinates, identifiers or status-style labels.
- Uppercase micro-labels use restrained tracking and must remain subordinate to content.
- Do not replace the current system with a fashionable display font without a measured reason and full surface validation.

## 4. Primary identity

### Brand mark

Canonical public mark: `/assets/axiona-mark.png`

Known physical dimensions: **96 × 96 px**.

The live header renders it at **40 × 40 px** with a small radius.

Until a separately approved vector master exists, this file is the public mark authority.

### Wordmark / header lockup

Current live lockup structure:

- brand mark;
- `AXIONA` in bold uppercase text;
- `SYSTEMS` below it with increased tracking.

This is a composed lockup. There is currently no separate flattened master wordmark file in the accepted public runtime.

### Browser mark

`favicon.svg` is the primary scalable browser icon and currently uses a blue four-part geometric mark.

It is a browser identity source. Do **not** assume that it is an exact vector reconstruction of `/assets/axiona-mark.png` unless this is separately proven and accepted.

## 5. Surfaces and geometry

Use:

- 1 px structural borders;
- rectangular/document-like surfaces;
- restrained corner rounding;
- solid offset shadows where depth is required;
- clear grids and rows;
- generous whitespace;
- contained work/control panels;
- clear state markers rather than repainting whole surfaces.

Avoid:

- soft neon glows;
- glassmorphism as the main identity;
- floating decorative panels without information structure;
- excessive rounded-card UI;
- gratuitous depth effects.

## 6. Interaction semantics

Visual affordance must match real behavior.

Informational elements:

- default cursor;
- no fake CTA arrows;
- no button-like hover fill;
- no lateral hover shift that implies navigation.

Interactive elements:

- semantic link or button;
- visible focus state;
- consistent hover/focus behavior;
- valid keyboard and touch behavior.

## 7. Motion

Current accepted public tuning after R143 conflict correction:

- desktop reveal movement: **7 px / 900 ms**;
- mobile reveal movement: **5 px / 760 ms**;
- reduced-motion: transforms and transitions disabled where required.

Motion must be structural and restrained.

Allowed:

- small reveal movement;
- opacity/state emphasis;
- repeatable viewport-entry behavior where useful.

Rejected:

- large transforms;
- pointer-tilt hero surfaces;
- looping decorative motion;
- scanner/glow/particle effects;
- motion that competes with reading.

## 8. Technical graphics

Technical diagrams are allowed only when they explain actual relationships, states, workflow or system structure.

Do not use CAD/relation-map graphics, coordinates, fake telemetry, node webs or scanner-style visuals simply to make a screen look technical.

## 9. Product-specific extensions

AXIONA products may have their own contained visual layer when that layer communicates product function. A product extension must:

- inherit the core identity;
- keep the AXIONA mark intact;
- preserve the core palette relationship unless there is a documented reason;
- avoid creating a competing global AXIONA brand system;
- document any deliberate exception.

Keeper is currently the strongest accepted reference for contained product/work-surface treatment.

## 10. Change control

Any proposal that changes one of the following is a brand-system change, not a routine page tweak:

- primary mark;
- wordmark construction;
- core palette;
- base typography stack;
- dominant surface language;
- motion character;
- global interaction semantics.

Such changes should be reviewed independently from ordinary product/page implementation.
