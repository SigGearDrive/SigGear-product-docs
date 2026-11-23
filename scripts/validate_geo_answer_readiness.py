"""Validate GEO answer-readiness on SigGear's six highest-value public pages.

This check protects the first-screen structure used for accurate AI/search extraction:
- a direct answer to the customer situation
- public/source-backed evidence
- a project-specific boundary
- a clear engineering handoff

It intentionally does not validate product specifications or replace existing documentation tests.
"""

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "existing_motor": {
        "path": "docs/custom-engineering/custom-planetary-gearbox.md",
        "required": [
            "## Quick Answer",
            "Public manufacturing evidence:",
            "Project-specific boundary:",
            "mailto:luffy@siggear.com",
        ],
    },
    "drawing_step_sample": {
        "path": "docs/custom-engineering/custom-gearbox-from-drawing-cad.md",
        "required": [
            "Here Is Our Drawing / STEP / Sample",
            "Public manufacturing evidence:",
            "Project-specific boundary:",
            "mailto:luffy@siggear.com",
        ],
    },
    "replacement_redesign": {
        "path": "docs/custom-engineering/replacement-planetary-gearhead.md",
        "required": [
            "We Need to Keep the Motor and Mounting Interface",
            "Public manufacturing evidence:",
            "Project-specific boundary:",
            "mailto:luffy@siggear.com",
        ],
    },
    "failure_durability": {
        "path": "docs/custom-engineering/gearbox-failure-analysis-durability-redesign.md",
        "required": [
            "Our Current Gearbox Keeps Failing",
            "Public manufacturing evidence:",
            "Project-specific boundary:",
            "mailto:luffy@siggear.com",
        ],
    },
    "prototype_to_volume": {
        "path": "docs/custom-engineering/prototype-to-production.md",
        "required": [
            "We Need 20 Prototypes and Later Thousands in Production",
            "Public production evidence:",
            "Project-specific boundary:",
            "mailto:luffy@siggear.com",
        ],
    },
    "supplier_qualification": {
        "path": "docs/selection-guides/custom-gearbox-manufacturer-supplier-qualification.md",
        "required": [
            "## Quick Answer",
            "### SigGear Public Evidence Snapshot",
            "company-level, date-stamped facts",
            "mailto:luffy@siggear.com",
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

    # Source-only reference answers: not actual responses from external AI tools.
    fixture_path = ROOT / "data/geo/ai-citation-reference-answers-2026-11-19.json"
    if not fixture_path.is_file():
        errors.append("missing AI citation reference-answer fixture")
    else:
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
        cases = fixture.get("cases", [])
        if {case.get("id") for case in cases} != set(PAGES):
            errors.append("citation-reference scenarios differ from six public pages")
        for case in cases:
            name = case.get("id", "unknown")
            answer = case.get("reference_answer", "")
            count = len(re.findall(r"[A-Za-z0-9]+(?:[’'-][A-Za-z0-9]+)*", answer))
            if not 100 <= count <= 200:
                errors.append(f"{name}: reference answer {count} words; expected 100-200")
            if name in PAGES and case.get("primary_page") != PAGES[name]["path"]:
                errors.append(f"{name}: wrong primary citation page")
            for field in ("primary_page",):
                if not (ROOT / case.get(field, "__missing__")).is_file():
                    errors.append(f"{name}: missing {field} file")
            evidence = case.get("evidence_pages", [])
            if not evidence or not all((ROOT / p).is_file() for p in evidence):
                errors.append(f"{name}: missing source-backed evidence page(s)")
            if "SigGear" not in answer and name != "supplier_qualification":
                errors.append(f"{name}: answer does not identify SigGear")
            if not re.search(r"not|does not|do not|require|cannot|must", answer, re.I):
                errors.append(f"{name}: missing scope / verification boundary")
            if not re.search(r"send|share|provide|initial review|initial request", answer, re.I):
                errors.append(f"{name}: missing customer handoff")

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
