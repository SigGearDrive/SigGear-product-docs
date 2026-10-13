from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "engineering-center" / "production-release-review.md"
PRODUCTION_JS = ROOT / "docs" / "assets" / "javascripts" / "production-release.js"
PILOT_JS = ROOT / "docs" / "assets" / "javascripts" / "pilot-preparation.js"

REQUIRED_IDS = [
    "sg-production-release",
    "sg-production-pilot-confirmation",
    "sg-production-pilot-result",
    "sg-production-configuration-change",
    "sg-production-drawing-revision",
    "sg-production-bom-revision",
    "sg-production-inspection-result",
    "sg-production-deviations",
    "sg-production-packaging-freeze",
    "sg-production-forecast",
    "sg-production-test-plan",
    "sg-production-change-control",
    "sg-production-open-items",
    "sg-production-readiness-status",
    "sg-copy-production-summary",
    "sg-email-production-summary",
]

REQUIRED_AUTOMATED_STATES = [
    "need_pilot_result_confirmation",
    "engineering_change_or_revalidation_required",
    "production_release_review_incomplete",
    "ready_to_submit_for_production_release_review",
]

FORBIDDEN_AUTO_STATES = [
    "pilot_build_accepted",
    "production_released",
    "mass_production_approved",
    "manufacturing_started",
]

page = PAGE.read_text(encoding="utf-8")
production_js = PRODUCTION_JS.read_text(encoding="utf-8")
pilot_js = PILOT_JS.read_text(encoding="utf-8")

for element_id in REQUIRED_IDS:
    if f'id="{element_id}"' not in page:
        raise ValueError(f"Missing production-release element: {element_id}")

for state in REQUIRED_AUTOMATED_STATES:
    if state not in production_js:
        raise ValueError(f"Missing production-release routing state: {state}")

for state in FORBIDDEN_AUTO_STATES:
    if state in production_js:
        raise ValueError(f"Manual-only production milestone must not be an automated JS state: {state}")

if "planetary-ratio-stage-data.json" not in production_js:
    raise ValueError("Production review must revalidate the candidate against current published data.")

if "ready_to_submit_for_pilot_preparation_review" not in pilot_js or "sg-pilot-production-review" not in pilot_js:
    raise ValueError("Pilot page must gate the production-release handoff.")

if "Human confirmation required" not in page:
    raise ValueError("Production-release page must preserve manual milestone boundaries.")

print("Production-release readiness layer validated.")
