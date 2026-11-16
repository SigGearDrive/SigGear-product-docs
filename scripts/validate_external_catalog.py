#!/usr/bin/env python3
"""Validate SigGear external planetary catalog references and public CAD policy."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "external-catalogs" / "planetary-gearboxes.yml"
EXPECTED_MODELS = ["8P", "10P", "12P", "14P", "16P", "20P", "22P", "24P", "28P", "32P", "36P", "42P"]


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def fail(message: str) -> None:
    raise SystemExit(f"External catalog validation failed: {message}")


def main() -> None:
    if not CATALOG_PATH.is_file():
        fail(f"missing catalog definition: {CATALOG_PATH.relative_to(ROOT)}")

    catalog = load_yaml(CATALOG_PATH)
    records = catalog.get("records") or []
    if len(records) != len(EXPECTED_MODELS):
        fail(f"expected {len(EXPECTED_MODELS)} planetary records, found {len(records)}")

    seen = []
    for entry in records:
        source_rel = entry.get("source_record")
        reference = entry.get("catalog_reference")
        if not source_rel or not reference:
            fail("each record requires source_record and catalog_reference")

        source = ROOT / source_rel
        if not source.is_file():
            fail(f"{reference}: source record does not exist: {source_rel}")

        product = load_yaml(source)
        model = product.get("model")
        if model != reference:
            fail(f"{reference}: source model is {model!r}")

        if product.get("product_family") != "planetary_gearbox":
            fail(f"{reference}: source is not a planetary_gearbox record")
        if product.get("public_page_status") != "published":
            fail(f"{reference}: canonical product page is not published")

        canonical = product.get("canonical_page")
        if not canonical or not (ROOT / canonical).is_file():
            fail(f"{reference}: canonical product page is missing")

        resource_slug = reference.lower()
        for rel in [
            f"docs/engineering-resources/{resource_slug}/datasheet.md",
            f"docs/engineering-resources/{resource_slug}/mechanical-interface.md",
        ]:
            if not (ROOT / rel).is_file():
                fail(f"{reference}: required engineering resource is missing: {rel}")

        cad = product.get("cad_control") or {}
        if cad.get("public_simplified_step_status") != "released":
            fail(f"{reference}: public simplified STEP is not released")
        if cad.get("public_simplified_step_configuration") != "4-stage reference":
            fail(f"{reference}: unexpected public CAD configuration")

        step_rel = cad.get("public_simplified_step_path")
        if not step_rel or not (ROOT / step_rel).is_file():
            fail(f"{reference}: released STEP path is missing: {step_rel!r}")
        public_raw = cad.get("public_raw_assembly_step")
        full_step_rel = cad.get("public_full_assembly_step_path")
        full_step_status = cad.get("public_full_assembly_step_status")
        if public_raw is True:
            if full_step_status != "released" or not full_step_rel:
                fail(f"{reference}: public full-assembly STEP requires released status and a path")
            if not (ROOT / full_step_rel).is_file():
                fail(f"{reference}: public full-assembly STEP is missing: {full_step_rel}")
        elif public_raw is False:
            if full_step_rel or full_step_status:
                fail(f"{reference}: non-public full-assembly record must not publish a download path")
        else:
            fail(f"{reference}: public_raw_assembly_step must be an explicit boolean")

        seen.append(reference)

    if seen != EXPECTED_MODELS:
        fail(f"catalog model order differs from controlled 8P-42P sequence: {seen}")

    print("External catalog validation passed: 12 planetary references, simplified STEP files and model-specific full-assembly release states are valid.")


if __name__ == "__main__":
    main()
