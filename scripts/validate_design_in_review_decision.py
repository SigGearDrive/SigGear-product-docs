from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "engineering-center" / "design-in-checklist.md"
DESIGN_JS = ROOT / "docs" / "assets" / "javascripts" / "design-in-review.js"
SAMPLE_JS = ROOT / "docs" / "assets" / "javascripts" / "sample-validation.js"

REQUIRED_PAGE_IDS = [
    "sg-design-in-review",
    "sg-design-in-decision-status",
    "sg-design-in-email",
]

REQUIRED_AUTOMATED_STATES = [
    "continue_evaluation",
    "engineering_revision_required",
    "design_in_review_ready",
]

FORBIDDEN_AUTOMATED_STATES = [
    "design_frozen",
    "pilot_preparation_ready",
]

page = PAGE.read_text(encoding="utf-8")
design_js = DESIGN_JS.read_text(encoding="utf-8")
sample_js = SAMPLE_JS.read_text(encoding="utf-8")

for element_id in REQUIRED_PAGE_IDS:
    if f'id="{element_id}"' not in page:
        raise ValueError(f"Missing Design-In review element: {element_id}")

for state in REQUIRED_AUTOMATED_STATES:
    if state not in design_js:
        raise ValueError(f"Missing automated Design-In routing state: {state}")

for state in FORBIDDEN_AUTOMATED_STATES:
    if state in design_js:
        raise ValueError(f"Manual-only milestone must not be an automated JS state: {state}")

if "source=sample_validation" not in sample_js:
    raise ValueError("Sample workflow must identify the Design-In handoff source.")

if "planetary-ratio-stage-data.json" not in design_js:
    raise ValueError("Design-In review must revalidate the candidate against current published data.")

if "Human confirmation required" not in page:
    raise ValueError("Design-In page must preserve manual milestone boundaries.")

print("Design-In review decision layer validated.")
