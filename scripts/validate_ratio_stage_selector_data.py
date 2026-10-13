#!/usr/bin/env python3
"""Validate the public planetary ratio-stage selector data against published Datasheet tables."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "docs" / "assets" / "data" / "planetary-ratio-stage-data.json"
MODELS = ["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"]


def number(text: str) -> float:
    match = re.search(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    if not match:
        raise ValueError(f"Cannot parse numeric value from {text!r}")
    return float(match.group(0))


def ratio_list(text: str) -> list[float]:
    return [float(part.strip()) for part in text.split("/")]


def close(a: float, b: float) -> bool:
    return math.isclose(a, b, rel_tol=0.0, abs_tol=1e-9)


def parse_datasheet(model: str) -> list[dict]:
    slug = model.lower()
    path = ROOT / "docs" / "engineering-resources" / slug / "datasheet.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    header = "| Stages | Gearbox body length L | Available ratios | Rated allowable torque | Maximum momentary torque | Efficiency |"

    try:
        start = lines.index(header)
    except ValueError as exc:
        raise ValueError(f"{model}: stage table header not found in {path}") from exc

    rows: list[dict] = []
    for line in lines[start + 2 : start + 6]:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            raise ValueError(f"{model}: expected 6 table cells, got {len(cells)} in {line!r}")
        rows.append(
            {
                "stage": int(cells[0]),
                "length": number(cells[1]),
                "ratios": ratio_list(cells[2]),
                "rated": number(cells[3]),
                "momentary": number(cells[4]),
                "efficiency": number(cells[5]),
            }
        )
    return rows


def main() -> None:
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    models = payload.get("models", [])
    if [item.get("model") for item in models] != MODELS:
        raise ValueError("Selector JSON must contain the 12 published models in canonical order.")

    for item in models:
        model = item["model"]
        published = parse_datasheet(model)
        selected = item.get("stages", [])

        if len(selected) != 4:
            raise ValueError(f"{model}: selector must contain exactly four published stages.")

        for expected, actual in zip(published, selected):
            for key in ("stage", "length", "rated", "momentary", "efficiency"):
                if key == "stage":
                    if expected[key] != actual.get(key):
                        raise ValueError(f"{model} stage mismatch: {expected[key]} != {actual.get(key)}")
                elif not close(expected[key], float(actual.get(key))):
                    raise ValueError(f"{model} stage {expected['stage']} {key} mismatch: {expected[key]} != {actual.get(key)}")

            actual_ratios = [float(value) for value in actual.get("ratios", [])]
            if len(expected["ratios"]) != len(actual_ratios):
                raise ValueError(f"{model} stage {expected['stage']} ratio count mismatch.")
            for a, b in zip(expected["ratios"], actual_ratios):
                if not close(a, b):
                    raise ValueError(f"{model} stage {expected['stage']} ratio mismatch: {a} != {b}")

    print("Planetary ratio-stage selector data matches all 12 published Datasheet stage tables.")


if __name__ == "__main__":
    main()
