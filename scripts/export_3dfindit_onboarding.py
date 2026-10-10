#!/usr/bin/env python3
"""Export a CADENAS / 3Dfindit onboarding matrix for SigGear planetary families.

This is a manufacturer-review package, not an assumed 3Dfindit import schema.
CADENAS determines the final eCATALOG/configurator implementation after reviewing
the product data, part-number logic and CAD assets.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "external-catalogs" / "planetary-gearboxes.yml"

FIELDS = [
    "Brand",
    "Manufacturer",
    "Series_Reference",
    "External_Name",
    "Market_Size_Class",
    "Nominal_Outer_Diameter",
    "Stage_Range",
    "Gearbox_Length_Range",
    "Reduction_Ratio_Range",
    "Rated_Allowable_Torque_Range",
    "Maximum_Momentary_Torque_Range",
    "Efficiency_Range",
    "Backlash_At_No_Load",
    "Maximum_Continuous_Input_Speed",
    "Adapted_Motor_Power",
    "Public_STEP_FileName",
    "Public_STEP_URL",
    "Public_CAD_Configuration",
    "Product_Page_URL",
    "Datasheet_URL",
    "Mechanical_Interface_URL",
    "Ordering_Logic",
    "Configurator_Review_Needed",
]


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def docs_url(base: str, path: str) -> str:
    rel = path.removeprefix("docs/")
    if rel.endswith(".md"):
        rel = rel[:-3] + "/"
    return base.rstrip("/") + "/" + rel.lstrip("/")


def build_rows() -> list[dict]:
    catalog = load_yaml(CATALOG_PATH)
    base = catalog["url_base"]
    manufacturer = catalog["manufacturer"]["legal_name"]
    rows = []

    for entry in catalog["records"]:
        product = load_yaml(ROOT / entry["source_record"])
        specs = product.get("published_specifications", {})
        cad = product.get("cad_control", {})
        model = product["model"]
        slug = model.lower()

        step_path = cad.get("public_simplified_step_path", "")
        step_name = Path(step_path).name if step_path else ""
        step_url = base.rstrip("/") + "/" + step_path.removeprefix("docs/") if step_path else ""

        rows.append(
            {
                "Brand": catalog["brand"],
                "Manufacturer": manufacturer,
                "Series_Reference": model,
                "External_Name": entry["external_name"],
                "Market_Size_Class": entry["market_size_class"],
                "Nominal_Outer_Diameter": specs.get("nominal_outer_diameter", ""),
                "Stage_Range": "1-4 stages",
                "Gearbox_Length_Range": specs.get("gearbox_length_range", ""),
                "Reduction_Ratio_Range": specs.get("reduction_ratio_range", ""),
                "Rated_Allowable_Torque_Range": specs.get("rated_allowable_torque_range", ""),
                "Maximum_Momentary_Torque_Range": specs.get("maximum_momentary_torque_range", ""),
                "Efficiency_Range": specs.get("efficiency_range", ""),
                "Backlash_At_No_Load": specs.get("backlash_at_no_load", ""),
                "Maximum_Continuous_Input_Speed": specs.get("maximum_continuous_speed", ""),
                "Adapted_Motor_Power": specs.get("adapted_motor_power", ""),
                "Public_STEP_FileName": step_name,
                "Public_STEP_URL": step_url,
                "Public_CAD_Configuration": "simplified 4-stage reference",
                "Product_Page_URL": docs_url(base, product["canonical_page"]),
                "Datasheet_URL": docs_url(base, f"docs/engineering-resources/{slug}/datasheet.md"),
                "Mechanical_Interface_URL": docs_url(
                    base, f"docs/engineering-resources/{slug}/mechanical-interface.md"
                ),
                "Ordering_Logic": (
                    "Series reference only; final stage, ratio, shaft/interface and motor "
                    "configuration require engineering review."
                ),
                "Configurator_Review_Needed": "yes",
            }
        )

    if len(rows) != 12:
        raise ValueError(f"Expected 12 planetary series records, found {len(rows)}")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="exports/external-catalogs/3dfindit-onboarding-matrix.csv",
    )
    args = parser.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)

    rows = build_rows()
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    try:
        display_output = output.relative_to(ROOT)
    except ValueError:
        display_output = output
    print(f"Exported {len(rows)} 3Dfindit onboarding rows to {display_output}")


if __name__ == "__main__":
    main()
