#!/usr/bin/env python3
"""Cross-check engineering-confirmed 8P-42P continuous input-speed range."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = ("8p", "10p", "12p", "14p", "16p", "20p", "22p", "24p", "28p", "32p", "36p", "42p")
RANGE = "1,000–20,000 rpm"
DATA = ROOT / "docs/assets/data/planetary-ratio-stage-data.json"

def check(path: Path, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if RANGE not in text:
        raise ValueError(f"{label} has no confirmed continuous input-speed range: {path}")
    # Do not accidentally republish the deprecated 8,000 rpm continuous ceiling.
    if re.search(r"(?:≤|<=)\\s*8,000\\s*rpm", text):
        raise ValueError(f"{label} still has an obsolete 8,000 rpm input-speed limit: {path}")

def main() -> None:
    obj = json.loads(DATA.read_text(encoding="utf-8"))
    bounds = obj.get("continuous_input_speed_rpm") or {}
    assert (bounds.get("min"), bounds.get("max")) == (1000, 20000), bounds
    assert bounds.get("operating_mode") == "continuous"
    assert bounds.get("confirmed_on") == "2026-10-15"
    assert [m.get("model", "").lower() for m in obj["models"]] == list(MODELS)

    for model in MODELS:
        check(ROOT / f"docs/products/planetary-gearboxes/{model}-planetary-gearbox.md", "Product page")
        check(ROOT / f"docs/engineering-resources/{model}/datasheet.md", "Datasheet")
        check(ROOT / f"data/products/{model}-planetary-gearbox.yml", "Product master record")
    for relative in (
        "docs/selection-guides/miniature-planetary-gearbox-selection-guide.md",
        "docs/engineering-resources/42p/mechanical-interface.md",
        "docs/engineering-resources/32p/motor-integration.md",
        "docs/engineering-resources/42p/motor-integration.md",
        "docs/engineering-resources/32p/design-in-pack.md",
        "docs/engineering-resources/42p/design-in-pack.md",
        "docs/custom-engineering/motor-gearbox-integration.md",
        "data/external-catalogs/platforms/directindustry-first-batch-2026-10-14.md",
    ):
        check(ROOT / relative, "Supplemental technical source")

    # Across public text, the old ceiling must not survive as an active limit.
    for base in (ROOT / "docs", ROOT / "data"):
        for path in base.rglob("*"):
            if path.suffix.lower() not in {".md", ".yml", ".yaml", ".json", ".js", ".txt"}:
                continue
            if re.search(r"(?:≤|<=)\\s*8,000\\s*rpm", path.read_text(encoding="utf-8")):
                raise ValueError(f"Outdated public speed rating remains: {path}")

    js = (ROOT / "docs/assets/javascripts/ratio-stage-selector.js").read_text(encoding="utf-8")
    assert "motorSpeed < speedBounds.min || motorSpeed > speedBounds.max" in js
    assert "speed_above_engineering" in js and "speed_below_engineering" in js
    print("Continuous 1,000–20,000 rpm input-speed range verified in 12 models and public resources.")

if __name__ == "__main__":
    main()
