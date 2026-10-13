from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "engineering-center" / "sample-validation-workflow.md"
JS = ROOT / "docs" / "assets" / "javascripts" / "sample-validation.js"
PACK = ROOT / "docs" / "engineering-resources" / "planetary-gearboxes" / "candidate-design-in-pack.md"
PACK_JS = ROOT / "docs" / "assets" / "javascripts" / "candidate-design-in-pack.js"

IDS = [
    "sg-planetary-sample-validation",
    "sg-sample-config-status",
    "sg-sample-fit-status",
    "sg-sample-noload-status",
    "sg-sample-functional-status",
    "sg-sample-application-status",
    "sg-sample-outcome",
    "sg-copy-sample-summary",
    "sg-email-sample-summary",
]

STATES = [
    "validation_in_progress",
    "engineering_iteration_required",
    "ready_to_submit_for_design_in_review",
]

page = PAGE.read_text(encoding="utf-8")
js = JS.read_text(encoding="utf-8")
pack = PACK.read_text(encoding="utf-8")
pack_js = PACK_JS.read_text(encoding="utf-8")

for element_id in IDS:
    if f'id="{element_id}"' not in page:
        raise ValueError(f"Missing sample-validation element: {element_id}")

if 'id="sg-pack-sample-validation"' not in pack:
    raise ValueError("Missing sample-validation handoff button.")

if "sample=planetary_candidate" not in pack_js:
    raise ValueError("Missing planetary sample handoff marker.")

if "planetary-ratio-stage-data.json" not in js:
    raise ValueError("Missing ratio-stage data validation source.")

for state in STATES:
    if state not in js:
        raise ValueError(f"Missing sample-validation state: {state}")

print("Sample-validation handoff structure validated.")
