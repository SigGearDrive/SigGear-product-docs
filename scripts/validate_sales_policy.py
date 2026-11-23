#!/usr/bin/env python3
"""Validate the public-safe sales policy used for inquiry handling."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "data" / "sales" / "public-sales-policy.yml"
KEY_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")

REQUIRED_FIELDS = {
    "schema_version",
    "policy_id",
    "scope",
    "public_contacts",
    "response_sequence",
    "essential_qualification",
    "conditional_qualification",
    "prohibited_claims",
    "private_only_information",
    "approved_outcomes",
}

REQUIRED_PROHIBITIONS = {
    "invent_or_transfer_product_specification",
    "treat_peak_torque_as_continuous",
    "present_optional_component_as_standard",
    "promise_unconfirmed_interface_protocol_or_control_mode",
    "invent_price_discount_moq_tooling_fee_or_lead_time",
    "expose_another_customer_project_or_commercial_terms",
}

REQUIRED_PRIVATE_ITEMS = {
    "customer_identity_and_contact_details",
    "customer_messages_requirements_and_drawings",
    "prices_discounts_costs_margins_and_internal_moq_rules",
    "private_quotations_payment_and_shipping_terms",
    "controlled_drawings_test_reports_and_nda_material",
}


def validate_key_list(data: dict, field: str, errors: list[str]) -> set[str]:
    values = data.get(field)
    if not isinstance(values, list) or not values:
        errors.append(f"{field} must be a non-empty list")
        return set()

    result: set[str] = set()
    for value in values:
        if not isinstance(value, str) or not KEY_RE.fullmatch(value):
            errors.append(f"{field} contains an invalid snake_case value: {value}")
            continue
        if value in result:
            errors.append(f"{field} contains a duplicate value: {value}")
        result.add(value)
    return result


def main() -> int:
    errors: list[str] = []
    if not POLICY_PATH.exists():
        print(f"Sales policy validation failed: missing {POLICY_PATH.relative_to(ROOT)}")
        return 1

    try:
        data = yaml.safe_load(POLICY_PATH.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        print(f"Sales policy validation failed: invalid YAML: {exc}")
        return 1

    if not isinstance(data, dict):
        print("Sales policy validation failed: policy must be a YAML mapping")
        return 1

    missing = sorted(REQUIRED_FIELDS - data.keys())
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")

    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if data.get("policy_id") != "public-sales-policy":
        errors.append("policy_id must be public-sales-policy")
    if data.get("scope") != "public_and_preliminary_sales_support":
        errors.append("scope must preserve the public preliminary-sales boundary")

    contacts = data.get("public_contacts")
    if not isinstance(contacts, list) or "luffy@siggear.com" not in contacts:
        errors.append("public_contacts must include the approved company email")

    for field in (
        "response_sequence",
        "essential_qualification",
        "conditional_qualification",
        "approved_outcomes",
    ):
        validate_key_list(data, field, errors)

    prohibited = validate_key_list(data, "prohibited_claims", errors)
    missing_prohibitions = sorted(REQUIRED_PROHIBITIONS - prohibited)
    if missing_prohibitions:
        errors.append(f"missing required prohibited claims: {', '.join(missing_prohibitions)}")

    private_items = validate_key_list(data, "private_only_information", errors)
    missing_private = sorted(REQUIRED_PRIVATE_ITEMS - private_items)
    if missing_private:
        errors.append(f"missing required private-only items: {', '.join(missing_private)}")

    if errors:
        print("Sales policy validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Sales policy validation passed: response sequence, qualification fields, "
        "prohibited claims and private-data boundaries checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
