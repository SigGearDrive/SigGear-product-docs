from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "selector": ROOT / "docs/assets/javascripts/ratio-stage-selector.js",
    "pack": ROOT / "docs/assets/javascripts/candidate-design-in-pack.js",
    "inquiry": ROOT / "docs/assets/javascripts/direct-contact.js",
    "sample": ROOT / "docs/assets/javascripts/sample-validation.js",
    "design": ROOT / "docs/assets/javascripts/design-in-review.js",
    "pilot": ROOT / "docs/assets/javascripts/pilot-preparation.js",
    "production": ROOT / "docs/assets/javascripts/production-release.js",
    "measurement": ROOT / "data/sales/inquiry-measurement-schema.yml",
    "weekly": ROOT / "data/sales/weekly-attribution-review-sop.yml",
    "inquiry_css": ROOT / "docs/assets/stylesheets/direct-contact.css",
    "selector_css": ROOT / "docs/assets/stylesheets/ratio-stage-selector.css",
    "design_css": ROOT / "docs/assets/stylesheets/design-in-review.css",
}

TEXT = {name: path.read_text(encoding="utf-8") for name, path in FILES.items()}

def require(name: str, needle: str, message: str) -> None:
    if needle not in TEXT[name]:
        raise ValueError(message)

def forbid(name: str, needle: str, message: str) -> None:
    if needle in TEXT[name]:
        raise ValueError(message)

# Relative-path, direct-email and technical handoff contracts.\nrequire("inquiry", "mailto:luffy@siggear.com?subject=", "Landing pages must create direct email to Luffy.")\nrequire("inquiry", "URLSearchParams", "Known product model context must survive legacy inquiry URLs.")
require("selector", "../../engineering-resources/planetary-gearboxes/candidate-design-in-pack/?model=", "Selection -> candidate-pack target is missing or changed.")
require("selector", "mailto:luffy@siggear.com?subject=", "Selection -> direct email target is missing.")
require("selector", "item.model + \" - \" + item.ratio", "Selection -> direct email must preserve model/ratio context.")

require("pack", "mailto:luffy@siggear.com?subject=", "Candidate pack -> direct email target is missing.")
require("pack", "SigGear Controlled CAD / Engineering Inquiry", "Candidate pack must name controlled CAD in direct-email subject.")
require("pack", "../../../engineering-center/sample-validation-workflow/?model=", "Candidate pack -> Sample Validation target is missing.")
require("pack", "&sample=planetary_candidate", "Candidate pack -> Sample Validation marker is missing.")

require("sample", "../design-in-checklist/?model=", "Sample Validation -> Design-In Review target is missing.")
require("sample", "&sample_status=", "Sample -> Design-In normalized status is missing.")
require("sample", "&sample_outcome=", "Sample -> Design-In normalized outcome is missing.")
require("sample", "&source=sample_validation", "Sample -> Design-In source marker is missing.")

require("design", 'decisionState === "design_in_review_ready"', "Pilot handoff must remain gated by Design-In Review Ready.")
require("design", "../pilot-preparation-review/?model=", "Design-In -> Pilot target is missing.")
require("design", "&source=design_in_review", "Design-In -> Pilot source marker is missing.")

require("pilot", 'current.status === "ready_to_submit_for_pilot_preparation_review"', "Production handoff must remain gated by pilot-review readiness.")
require("pilot", "../production-release-review/?model=", "Pilot -> Production Release target is missing.")
require("pilot", "&source=pilot_preparation_review", "Pilot -> Production Release source marker is missing.")

require("production", '(params.get("source") || "") !== "pilot_preparation_review"', "Production Release must require the pilot-preparation source marker.")

# Every downstream candidate-specific surface must revalidate against the same published data asset.
for name in ("pack", "sample", "design", "pilot", "production"):
    require(name, "planetary-ratio-stage-data.json", f"{name} no longer revalidates against published ratio-stage data.")

# Funnel event coverage in code and the public-safe measurement schema.
events = {
    "selector": ["ratio_stage_selector_run"],
    "pack": ["candidate_design_in_pack_view"],

    "sample": ["sample_validation_candidate_view", "sample_validation_prepare_email"],
    "design": ["design_in_review_candidate_view", "design_in_review_prepare_email"],
    "pilot": ["pilot_preparation_review_view", "pilot_preparation_prepare_email"],
    "production": ["production_release_review_view", "production_release_prepare_email"],
}
for source, names in events.items():
    for event in names:
        require(source, event, f"Missing funnel event in {source}: {event}")
        require("measurement", event, f"Measurement schema is missing funnel event: {event}")

# High-risk private fields must never be embedded in cross-page handoff URLs.
forbidden_handoff_tokens = {
    "sample": ["sg-sample-test-condition", "sg-sample-notes"],
    "design": ["customer_test_notes", "measured_torque", "measured_speed", "temperature"],
    "pilot": ["sg-pilot-drawing-revision", "sg-pilot-bom-revision", "sg-pilot-quantity", "sg-pilot-schedule"],
}
# Check only the URL-building portions, not the full files where form fields legitimately exist.
sample_url = TEXT["sample"][TEXT["sample"].find('designInReviewLink.href'):TEXT["sample"].find('function updateReadiness')]
design_url = TEXT["design"][TEXT["design"].find('pilotReviewLink.href'):TEXT["design"].find('status.hidden = true')]
pilot_url = TEXT["pilot"][TEXT["pilot"].find('productionReviewLink.href'):TEXT["pilot"].find('productionReviewLink.hidden = false') + 40]
for token in forbidden_handoff_tokens["sample"]:
    if token in sample_url:
        raise ValueError(f"Private sample field leaked into Design-In handoff URL: {token}")
for token in forbidden_handoff_tokens["design"]:
    if token in design_url:
        raise ValueError(f"Private sample data leaked into Pilot handoff URL: {token}")
for token in forbidden_handoff_tokens["pilot"]:
    if token in pilot_url:
        raise ValueError(f"Private pilot field leaked into Production handoff URL: {token}")

# Responsive/mobile contracts used by the funnel.
require("inquiry_css", ".siggear-direct-email", "Large direct-contact email styling is missing.")
require("inquiry_css", "overflow-wrap: anywhere", "Large email must wrap on narrow screens.")
require("inquiry_css", "@media (max-width: 44rem)", "Shared form-grid mobile breakpoint is missing.")
require("inquiry_css", ".siggear-direct-send.md-button", "Direct email button is missing.")
require("selector_css", ".siggear-selector-table-wrap", "Wide selector tables need a scroll wrapper.")
require("selector_css", "overflow-x: auto", "Wide selector tables must scroll horizontally.")
require("selector_css", "@media (max-width: 54rem)", "Candidate-card mobile breakpoint is missing.")
require("design_css", "@media (max-width: 54rem)", "Manual milestone cards need a mobile breakpoint.")

# Weekly review must include the engineering lifecycle and preserve interpretation boundaries.
for event in [
    "ratio_stage_selector_run",
    "candidate_design_in_pack_view",
    "sample_validation_candidate_view",
    "design_in_review_candidate_view",
    "pilot_preparation_review_view",
    "production_release_review_view",
]:
    require("weekly", event, f"Weekly Attribution Review is missing lifecycle event: {event}")

print("End-to-end planetary funnel contracts validated.")
