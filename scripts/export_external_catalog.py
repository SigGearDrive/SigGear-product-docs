#!/usr/bin/env python3
"""Export platform-neutral SigGear planetary catalog data to CSV.

Technical values are read from data/products/*.yml. The external catalog
definition stores naming, classification and release policy only.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from urllib.parse import quote

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "external-catalogs" / "planetary-gearboxes.yml"

FIELDS = [
    "brand",
    "manufacturer",
    "catalog_reference",
    "ordering_status",
    "external_name",
    "market_size_class",
    "product_type",
    "nominal_outer_diameter",
    "gearbox_length_range",
    "reduction_ratio_range",
    "rated_allowable_torque_range",
    "maximum_momentary_torque_range",
    "efficiency_range",
    "backlash_at_no_load",
    "maximum_continuous_speed",
    "adapted_motor_power",
    "product_page_url",
    "datasheet_url",
    "mechanical_interface_url",
    "public_step_url",
    "public_cad_configuration",
    "public_cad_use",
    "controlled_cad_status",
    "inquiry_email",
    "inquiry_url",
]


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def public_url(base: str, docs_path: str) -> str:
    rel = docs_path.removeprefix("docs/")
    if rel.endswith(".md"):
        rel = rel[:-3] + "/"
    return base.rstrip("/") + "/" + rel.lstrip("/")


def build_rows() -> list[dict]:
    catalog = load_yaml(CATALOG)
    base = catalog["url_base"]
    shared = catalog["shared_classification"]
    manufacturer = catalog["manufacturer"]
    rows = []

    for entry in catalog["records"]:
        source = ROOT / entry["source_record"]
        product = load_yaml(source)
        specs = product.get("published_specifications", {})
        cad = product.get("cad_control", {})
        model = product["model"]
        resource_slug = model.lower()

        product_url = public_url(base, product["canonical_page"])
        datasheet_url = public_url(
            base, f"docs/engineering-resources/{resource_slug}/datasheet.md"
        )
        mechanical_url = public_url(
            base, f"docs/engineering-resources/{resource_slug}/mechanical-interface.md"
        )

        step_path = cad.get("public_simplified_step_path", "")
        step_url = base.rstrip("/") + "/" + step_path.removeprefix("docs/") if step_path else ""

        subject = quote(f"{model} Planetary Gearbox Engineering Review")
        inquiry_url = f"mailto:{manufacturer['contact_email']}?subject={subject}"

        rows.append(
            {
                "brand": catalog["brand"],
                "manufacturer": manufacturer["legal_name"],
                "catalog_reference": entry["catalog_reference"],
                "ordering_status": "series reference; final configuration dependent",
                "external_name": entry["external_name"],
                "market_size_class": entry["market_size_class"],
                "product_type": shared["product_type"],
                "nominal_outer_diameter": specs.get("nominal_outer_diameter", ""),
                "gearbox_length_range": specs.get("gearbox_length_range", ""),
                "reduction_ratio_range": specs.get("reduction_ratio_range", ""),
                "rated_allowable_torque_range": specs.get("rated_allowable_torque_range", ""),
                "maximum_momentary_torque_range": specs.get("maximum_momentary_torque_range", ""),
                "efficiency_range": specs.get("efficiency_range", ""),
                "backlash_at_no_load": specs.get("backlash_at_no_load", ""),
                "maximum_continuous_speed": specs.get("maximum_continuous_speed", ""),
                "adapted_motor_power": specs.get("adapted_motor_power", ""),
                "product_page_url": product_url,
                "datasheet_url": datasheet_url,
                "mechanical_interface_url": mechanical_url,
                "public_step_url": step_url,
                "public_cad_configuration": shared["cad_configuration_public"],
                "public_cad_use": shared["cad_use"],
                "controlled_cad_status": catalog["distribution_scope"]["controlled_cad_policy"],
                "inquiry_email": manufacturer["contact_email"],
                "inquiry_url": inquiry_url,
            }
        )

    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="exports/external-catalogs/siggear-planetary-gearboxes.csv",
    )
    args = parser.parse_args()

    output = ROOT / args.output
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

    print(f"Exported {len(rows)} planetary catalog records to {display_output}")


if __name__ == "__main__":
    main()
