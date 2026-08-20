#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "de/keeper.html"
text = p.read_text(encoding="utf-8")
replacements = (
    (
        "Ein späterer automatischer Vorschlag darf eine bereits von Ihnen korrigierte Angabe nicht still überschreiben.",
        "Ein späterer automatischer Vorschlag darf Ihre Korrektur nicht still überschreiben.",
    ),
    (
        "AXIONA Keeper befindet sich in Entwicklung und kann noch nicht heruntergeladen werden. Die erste geplante öffentliche Veröffentlichung erfolgt über den Apple App Store. Diese Seite beschreibt die angestrebte Produkterfahrung und stellt die App nicht als fertig dar.",
        "AXIONA Keeper befindet sich in Entwicklung und steht noch nicht zum Download bereit. Die erste geplante öffentliche Veröffentlichung erfolgt über den Apple App Store. Diese Seite beschreibt das geplante Produkterlebnis und stellt die App nicht als fertig dar.",
    ),
)
for old, new in replacements:
    if old not in text:
        raise SystemExit(f"prep text missing: {old[:90]!r}")
    text = text.replace(old, new, 1)
p.write_text(text, encoding="utf-8")
print("OK_KEEPER_R97_PREP")
