#!/usr/bin/env python3
"""Export SigGear 8P-42P data to TraceParts Smart-Publishing field names.

This produces a CSV mapping for the TraceParts Products_en sheet. It does not
pretend to be the final TraceParts XLS template because the official template
and Classification_Category_ID are supplied by TraceParts / Smart-Publishing.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "external-catalogs" / "planetary-gearboxes.yml"
TRACEPARTS_PATH = ROOT / "data" / "external-catalogs" / "platforms" / "traceparts.yml"

FIELDS = [
    "Product_ID",
    "Product_Name",
    "Product_Short_Description",
    "Product_Keywords_List",
    "Classification_Category_ID",
    "Product_Large_Picture_FileName",
    "Product_Document_URL_1",
    "Product_Document_URL_Title_1",
    "Product_Document_URL_2",
    "Product_Document_URL_Title_2",
    "Product_Document_URL_3",
    "Product_Document_URL_Title_3",
    "Part_Number_ID",
    "Part_Number",
    "Part_Number_CAD_FileName",
    "Part_Number_Description",
    "Nominal_Outer_Diameter",
    "Gearbox_Length_Range",
    "Reduction_Ratio_Range",
    "Rated_Allowable_Torque_Range",
    "Maximum_Momentary_Torque_Range",
    "Efficiency_Range",
    "Backlash_At_No_Load",
    "Maximum_Continuous_Input_Speed",
    "Adapted_Motor_Power",
]


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def docs_url(base: str, path: str) -> str:
    rel = path.removeprefix("docs/")
    if rel.endswith(".md"):
        rel = rel[:-3] + "/"
    return base.rstrip("/") + "/" + rel.lstrip("/")


def validate_text(value: str, limit: int, field: str, model: str) -> None:
    if len(value) > limit:
        raise ValueError(f"{model}: {field} exceeds {limit} characters")


def build_rows(classification_category_id: str) -> list[dict]:
    if not classification_category_id:
        raise ValueError("Classification_Category_ID is required for TraceParts export")

    catalog = load_yaml(CATALOG_PATH)
    tp = load_yaml(TRACEPARTS_PATH)
    base = catalog["url_base"]
    prefix = tp["traceparts_field_policy"]["product_id_prefix"]
    keywords = ";".join(tp["keywords"])

    if len(keywords) > 255:
        raise ValueError("TraceParts keyword list exceeds 255 characters")
    for keyword in tp["keywords"]:
        if len(keyword) > 30:
            raise ValueError(f"TraceParts keyword exceeds 30 characters: {keyword}")

    rows = []
    for entry in catalog["records"]:
        product = load_yaml(ROOT / entry["source_record"])
        model = product["model"]
        specs = product.get("published_specifications", {})
        cad = product.get("cad_control", {})

        product_id = f"{prefix}{model}"
        if not re.fullmatch(r"[A-Za-z0-9_.]+", product_id):
            raise ValueError(f"{model}: invalid TraceParts Product_ID {product_id!r}")

        product_name = entry["external_name"]
        short_description = (
            f"{entry['external_name']}; 1-4 stage planetary gearbox family with "
            f"published ratio range {specs.get('reduction_ratio_range', '')} and "
            f"rated allowable torque range {specs.get('rated_allowable_torque_range', '')}."
        )
        part_description = (
            f"{model} series reference. Public CAD is a simplified 4-stage reference "
            "for preliminary Design-In; final stage, ratio and interface are configuration-dependent."
        )

        validate_text(product_name, 255, "Product_Name", model)
        validate_text(short_description, 255, "Product_Short_Description", model)
        validate_text(part_description, 255, "Part_Number_Description", model)

        slug = model.lower()
        product_url = docs_url(base, product["canonical_page"])
        datasheet_url = docs_url(base, f"docs/engineering-resources/{slug}/datasheet.md")
        mechanical_url = docs_url(base, f"docs/engineering-resources/{slug}/mechanical-interface.md")

        step_path = cad.get("public_simplified_step_path", "")
        step_name = Path(step_path).name if step_path else ""

        rows.append(
            {
                "Product_ID": product_id,
                "Product_Name": product_name,
                "Product_Short_Description": short_description,
                "Product_Keywords_List": keywords,
                "Classification_Category_ID": classification_category_id,
                "Product_Large_Picture_FileName": "",
                "Product_Document_URL_1": product_url,
                "Product_Document_URL_Title_1": f"{model} Product Page",
                "Product_Document_URL_2": datasheet_url,
                "Product_Document_URL_Title_2": f"{model} Technical Datasheet",
                "Product_Document_URL_3": mechanical_url,
                "Product_Document_URL_Title_3": f"{model} Mechanical Interface",
                "Part_Number_ID": 1,
                "Part_Number": model,
                "Part_Number_CAD_FileName": step_name,
                "Part_Number_Description": part_description,
                "Nominal_Outer_Diameter": specs.get("nominal_outer_diameter", ""),
                "Gearbox_Length_Range": specs.get("gearbox_length_range", ""),
                "Reduction_Ratio_Range": specs.get("reduction_ratio_range", ""),
                "Rated_Allowable_Torque_Range": specs.get("rated_allowable_torque_range", ""),
                "Maximum_Momentary_Torque_Range": specs.get("maximum_momentary_torque_range", ""),
                "Efficiency_Range": specs.get("efficiency_range", ""),
                "Backlash_At_No_Load": specs.get("backlash_at_no_load", ""),
                "Maximum_Continuous_Input_Speed": specs.get("maximum_continuous_speed", ""),
                "Adapted_Motor_Power": specs.get("adapted_motor_power", ""),
            }
        )

    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--classification-category-id",
        required=True,
        help="TraceParts Classification_Category_ID from the official Smart-Publishing template.",
    )
    parser.add_argument(
        "--output",
        default="exports/external-catalogs/traceparts-products-en.csv",
    )
    args = parser.parse_args()

    rows = build_rows(args.classification_category_id)
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    try:
        display_output = output.relative_to(ROOT)
    except ValueError:
        display_output = output
    print(f"Exported {len(rows)} TraceParts product rows to {display_output}")


if __name__ == "__main__":
    main()
