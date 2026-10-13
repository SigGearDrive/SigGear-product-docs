#!/usr/bin/env python3
"""Validate public Controlled CAD review readiness wiring."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORM = ROOT / "docs" / "request-cad-sample-quote.md"
INQUIRY_JS = ROOT / "docs" / "assets" / "javascripts" / "inquiry-form.js"
PACK_JS = ROOT / "docs" / "assets" / "javascripts" / "candidate-design-in-pack.js"

FORM_IDS = [
    "sg-output-interface",
    "sg-duty-cycle",
    "sg-shaft-loads",
    "sg-cad-readiness",
    "sg-cad-readiness-status",
    "sg-cad-readiness-gates",
]

GATE_TOKENS = [
    "candidate",
    "motor_interface",
    "output_interface",
    "load_duty",
    "envelope",
]


def main() -> None:
    form = FORM.read_text(encoding="utf-8")
    inquiry = INQUIRY_JS.read_text(encoding="utf-8")
    pack = PACK_JS.read_text(encoding="utf-8")

    for element_id in FORM_IDS:
        if f'id="{element_id}"' not in form:
            raise ValueError(f"Project Brief is missing required CAD-readiness element: {element_id}")

    if '"ready_for_cad_review"' not in inquiry or '"need_more_information"' not in inquiry:
        raise ValueError("Inquiry form must preserve normalized CAD-readiness statuses.")

    for token in GATE_TOKENS:
        if token not in inquiry:
            raise ValueError(f"Inquiry form is missing CAD-readiness gate token: {token}")

    if "next_step=cad_review" not in pack:
        raise ValueError("Candidate Design-In Pack must prefill the Project Brief for CAD review.")

    if "controlled CAD has been approved or released" not in form:
        raise ValueError("Project Brief must preserve the boundary between review readiness and CAD approval/release.")

    print("Controlled CAD request readiness wiring validated.")


if __name__ == "__main__":
    main()
