"""Validate GEO answer-readiness on SigGear's six highest-value public pages.

This check protects the first-screen structure used for accurate AI/search extraction:
- a direct answer to the customer situation
- public/source-backed evidence
- a project-specific boundary
- a clear engineering handoff

It intentionally does not validate product specifications or replace existing documentation tests.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "existing_motor": {
        "path": "docs/custom-engineering/custom-planetary-gearbox.md",
        "required": [
            "## Quick Answer",
            "Public manufacturing evidence:",
            "Project-specific boundary:",
            "request-cad-sample-quote.md",
        ],
    },
    "drawing_step_sample": {
        "path": "docs/custom-engineering/custom-gearbox-from-drawing-cad.md",
        "required": [
            "Here Is Our Drawing / STEP / Sample",
            "Public manufacturing evidence:",
            "Project-specific boundary:",
            "request-cad-sample-quote.md?start=drawing_cad",
        ],
    },
    "replacement_redesign": {
        "path": "docs/custom-engineering/replacement-planetary-gearhead.md",
        "required": [
            "We Need to Keep the Motor and Mounting Interface",
            "Public manufacturing evidence:",
            "Project-specific boundary:",
            "request-cad-sample-quote.md?start=failing_gearbox",
        ],
    },
    "failure_durability": {
        "path": "docs/custom-engineering/gearbox-failure-analysis-durability-redesign.md",
        "required": [
            "Our Current Gearbox Keeps Failing",
            "Public manufacturing evidence:",
            "Project-specific boundary:",
            "request-cad-sample-quote.md?start=failing_gearbox",
        ],
    },
    "prototype_to_volume": {
        "path": "docs/custom-engineering/prototype-to-production.md",
        "required": [
            "We Need 20 Prototypes and Later Thousands in Production",
            "Public production evidence:",
            "Project-specific boundary:",
            "request-cad-sample-quote.md",
        ],
    },
    "supplier_qualification": {
        "path": "docs/selection-guides/custom-gearbox-manufacturer-supplier-qualification.md",
        "required": [
            "## Quick Answer",
            "### SigGear Public Evidence Snapshot",
            "company-level, date-stamped facts",
            "request-cad-sample-quote.md",
        ],
    },
}


def main() -> None:
    errors: list[str] = []

    for name, spec in PAGES.items():
        path = ROOT / spec["path"]
        if not path.exists():
            errors.append(f"{name}: missing page {spec['path']}")
            continue

        text = path.read_text(encoding="utf-8")
        for token in spec["required"]:
            if token not in text:
                errors.append(f"{name}: missing answer-readiness token: {token!r}")

        first_screen = "\n".join(text.splitlines()[:70])
        if "SigGear" not in first_screen:
            errors.append(f"{name}: first screen does not identify SigGear")

    if errors:
        raise SystemExit(
            "GEO answer-readiness validation failed:\n- " + "\n- ".join(errors)
        )

    print(
        "GEO answer-readiness validated for existing motor, drawing/STEP/sample, "
        "replacement/redesign, failure/durability, prototype-to-volume and supplier qualification."
    )


if __name__ == "__main__":
    main()
