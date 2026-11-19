#!/usr/bin/env python3
"""Validate the current planetary gearhead input-speed policy.

SigGear no longer applies one universal 1,000-20,000 rpm continuous
input-speed range across every 8P-42P gearhead. Permissible input speed
must be reviewed with the selected motor, gearhead configuration, duty
cycle and operating point. The current 12P engineering data separately
confirms 1,000-50,000 rpm.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = ("8p", "10p", "12p", "14p", "16p", "20p", "22p", "24p", "28p", "32p", "36p", "42p")
LEGACY_RANGE = "1,000–20,000 rpm"
GENERIC_POLICY = "Motor/configuration dependent; confirm selected operating point"
RANGE_12P = "1,000–50,000 rpm"
DATA = ROOT / "docs/assets/data/planetary-ratio-stage-data.json"


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> None:
    obj = json.loads(text(DATA))
    policy = obj.get("input_speed_policy") or {}
    assert policy.get("rule") == "motor_and_configuration_dependent", policy
    assert policy.get("confirmed_on") == "2026-11-19", policy

    model_specific = policy.get("model_specific_confirmed_ranges") or {}
    p12 = model_specific.get("12P") or {}
    assert (p12.get("min_rpm"), p12.get("max_rpm")) == (1000, 50000), p12
    assert [m.get("model", "").lower() for m in obj["models"]] == list(MODELS)

    for model in MODELS:
        page = text(ROOT / f"docs/products/planetary-gearboxes/{model}-planetary-gearbox.md")
        ds = text(ROOT / f"docs/engineering-resources/{model}/datasheet.md")
        master = text(ROOT / f"data/products/{model}-planetary-gearbox.yml")

        expected = RANGE_12P if model == "12p" else GENERIC_POLICY
        for label, value in (("Product page", page), ("Datasheet", ds), ("Product master", master)):
            if expected not in value:
                raise ValueError(f"{label} does not carry the current input-speed policy for {model}")
            if LEGACY_RANGE in value:
                raise ValueError(f"{label} still carries obsolete universal input-speed range for {model}")

    # The obsolete range must not survive as an active public/data rule.
    for base in (ROOT / "docs", ROOT / "data"):
        for path in base.rglob("*"):
            if path.suffix.lower() not in {".md", ".yml", ".yaml", ".json", ".js", ".txt"}:
                continue
            value = text(path)
            if LEGACY_RANGE in value:
                raise ValueError(f"Obsolete universal input-speed range remains: {path}")
            if re.search(r"(?:≤|<=)\s*8,000\s*rpm", value):
                raise ValueError(f"Outdated 8,000 rpm speed limit remains: {path}")

    js = text(ROOT / "docs/assets/javascripts/ratio-stage-selector.js")
    assert "speedBounds" not in js
    assert "speed_above_engineering" not in js
    assert "speed_below_engineering" not in js

    print("Configuration-dependent input-speed policy verified across 8P-42P; 12P 1,000-50,000 rpm range retained.")


if __name__ == "__main__":
    main()
