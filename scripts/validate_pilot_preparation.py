from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "engineering-center" / "pilot-preparation-review.md"
PILOT_JS = ROOT / "docs" / "assets" / "javascripts" / "pilot-preparation.js"
DESIGN_JS = ROOT / "docs" / "assets" / "javascripts" / "design-in-review.js"

REQUIRED_IDS = [
    "sg-pilot-preparation",
    "sg-pilot-design-freeze",
    "sg-pilot-drawing-revision",
    "sg-pilot-bom-revision",
    "sg-pilot-quantity",
    "sg-pilot-schedule",
    "sg-pilot-inspection",
    "sg-pilot-packaging",
    "sg-pilot-change-control",
    "sg-pilot-acceptance-plan",
    "sg-pilot-readiness-status",
    "sg-copy-pilot-summary",
    "sg-email-pilot-summary",
]

REQUIRED_AUTOMATED_STATES = [
    "need_design_freeze_confirmation",
    "pilot_review_incomplete",
    "ready_to_submit_for_pilot_preparation_review",
]

FORBIDDEN_AUTO_STATES = [
    "pilot_preparation_ready",
    "pilot_build_approved",
    "production_released",
]

page = PAGE.read_text(encoding="utf-8")
pilot_js = PILOT_JS.read_text(encoding="utf-8")
design_js = DESIGN_JS.read_text(encoding="utf-8")

for element_id in REQUIRED_IDS:
    if f'id="{element_id}"' not in page:
        raise ValueError(f"Missing pilot-preparation element: {element_id}")

for state in REQUIRED_AUTOMATED_STATES:
    if state not in pilot_js:
        raise ValueError(f"Missing pilot-preparation routing state: {state}")

for state in FORBIDDEN_AUTO_STATES:
    if state in pilot_js:
        raise ValueError(f"Manual-only pilot milestone must not be an automated JS state: {state}")

if "planetary-ratio-stage-data.json" not in pilot_js:
    raise ValueError("Pilot review must revalidate the candidate against current published data.")

if "design_in_review_ready" not in design_js or "sg-design-in-pilot-review" not in design_js:
    raise ValueError("Design-In page must gate the pilot-preparation handoff.")

if "Human confirmation required" not in page:
    raise ValueError("Pilot page must preserve manual milestone boundaries.")

print("Pilot-preparation and change-control layer validated.")
