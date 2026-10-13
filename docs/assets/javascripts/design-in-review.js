(function () {
  var container = document.getElementById("sg-design-in-review");
  if (!container) return;

  var status = document.getElementById("sg-design-in-review-status");
  var content = document.getElementById("sg-design-in-review-content");
  var candidateName = document.getElementById("sg-design-in-candidate-name");
  var candidateDetail = document.getElementById("sg-design-in-candidate-detail");
  var candidateCell = document.getElementById("sg-design-in-candidate-cell");
  var sampleStatusCell = document.getElementById("sg-design-in-sample-status");
  var sampleOutcomeCell = document.getElementById("sg-design-in-sample-outcome");
  var decisionStatus = document.getElementById("sg-design-in-decision-status");
  var emailButton = document.getElementById("sg-design-in-email");
  var datasheetLink = document.getElementById("sg-design-in-datasheet");
  var interfaceLink = document.getElementById("sg-design-in-interface");
  var pilotReviewLink = document.getElementById("sg-design-in-pilot-review");
  var actionStatus = document.getElementById("sg-design-in-action-status");

  var validModels = ["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"];
  var validSampleStatuses = [
    "validation_in_progress",
    "engineering_iteration_required",
    "ready_to_submit_for_design_in_review"
  ];
  var validSampleOutcomes = [
    "not_decided",
    "keep_current_configuration",
    "change_ratio",
    "change_motor_or_input",
    "revise_mechanical_interface",
    "more_testing_required",
    "ready_for_design_in_review"
  ];

  var context = null;

  function fmt(value, digits) {
    return Number(value).toLocaleString(undefined, {
      maximumFractionDigits: digits,
      minimumFractionDigits: 0
    });
  }

  function sampleStatusLabel(value) {
    var labels = {
      validation_in_progress: "Validation in Progress",
      engineering_iteration_required: "Engineering Iteration Required",
      ready_to_submit_for_design_in_review: "Ready to Submit for Design-In Review"
    };
    return labels[value] || "Unknown";
  }

  function outcomeLabel(value) {
    var labels = {
      not_decided: "Not decided yet",
      keep_current_configuration: "Keep current configuration for next review",
      change_ratio: "Review a different ratio / stage",
      change_motor_or_input: "Review motor / input-side configuration",
      revise_mechanical_interface: "Revise mounting / shaft / interface",
      more_testing_required: "More testing required",
      ready_for_design_in_review: "Submit current configuration for Design-In review"
    };
    return labels[value] || "Unknown";
  }

  function decision(sampleStatus, sampleOutcome) {
    if (sampleStatus === "engineering_iteration_required") {
      return "engineering_revision_required";
    }

    if (sampleStatus === "validation_in_progress") {
      return "continue_evaluation";
    }

    if (sampleStatus === "ready_to_submit_for_design_in_review") {
      if (["change_ratio","change_motor_or_input","revise_mechanical_interface"].indexOf(sampleOutcome) !== -1) {
        return "engineering_revision_required";
      }
      if (sampleOutcome === "keep_current_configuration" ||
          sampleOutcome === "ready_for_design_in_review") {
        return "design_in_review_ready";
      }
    }

    return "continue_evaluation";
  }

  function decisionLabel(value) {
    var labels = {
      continue_evaluation: "Continue Evaluation",
      engineering_revision_required: "Engineering Revision Required",
      design_in_review_ready: "Design-In Review Ready"
    };
    return labels[value] || "Continue Evaluation";
  }

  function decisionDescription(value) {
    if (value === "engineering_revision_required") {
      return "The sample context indicates that the current configuration or test condition needs engineering revision before Design-In review.";
    }
    if (value === "design_in_review_ready") {
      return "The validated candidate and sample workflow are ready to be submitted for formal Design-In review. This is not Design-In approval or Design Freeze.";
    }
    return "Keep the project in engineering evaluation until the sample evidence and next-direction decision are complete enough for formal Design-In review.";
  }

  function track(name) {
    if (typeof window.gtag !== "function" || !context) return;
    window.gtag("event", name, {
      page_path: window.location.pathname,
      inquiry_model: context.model,
      selector_candidate_stage: String(context.stage),
      sample_validation_status: context.sampleStatus,
      sample_validation_outcome: context.sampleOutcome,
      design_in_decision_status: context.decision
    });
  }

  function prepareEmail() {
    if (!context) return;

    var lines = [
      "SigGear Planetary Gearbox Design-In Review Request",
      "",
      "Validated candidate: " + context.model + " / " + context.stage + "-stage / " +
        fmt(context.ratio, 4) + ":1",
      "Sample validation status: " + sampleStatusLabel(context.sampleStatus),
      "Sample engineering outcome: " + outcomeLabel(context.sampleOutcome),
      "Automated preliminary decision: " + decisionLabel(context.decision),
      "",
      decisionDescription(context.decision),
      "",
      "Please review the exact controlled configuration, drawing revision, validated operating condition, interfaces and remaining risks before confirming any Design Freeze or pilot-preparation milestone.",
      "",
      "Note: Design Frozen and Pilot Preparation Ready require human engineering / project confirmation and are not automatically approved by this website."
    ];

    track("design_in_review_prepare_email");
    actionStatus.textContent = "Opening your email client with the Design-In review context...";

    var subject = context.model + " - " + context.stage + "-stage " +
      fmt(context.ratio, 4) + ":1 - Design-In Review";

    window.location.href = "mailto:wangwanrong@siggear.com?subject=" +
      encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join("\n"));
  }

  async function init() {
    var params = new URLSearchParams(window.location.search);
    if ((params.get("source") || "") !== "sample_validation") return;

    var model = (params.get("model") || "").toUpperCase();
    var stage = Number(params.get("stage"));
    var ratio = Number(params.get("ratio"));
    var sampleStatus = params.get("sample_status") || "";
    var sampleOutcome = params.get("sample_outcome") || "";

    if (validModels.indexOf(model) === -1 ||
        !Number.isInteger(stage) || stage < 1 || stage > 4 ||
        !Number.isFinite(ratio) || ratio <= 0 ||
        validSampleStatuses.indexOf(sampleStatus) === -1 ||
        validSampleOutcomes.indexOf(sampleOutcome) === -1) {
      return;
    }

    container.hidden = false;

    try {
      var response = await fetch(new URL("../../assets/data/planetary-ratio-stage-data.json", window.location.href));
      if (!response.ok) throw new Error("Unable to load published data.");
      var payload = await response.json();
      var modelData = (payload.models || []).find(function (item) {
        return item.model === model;
      });
      var stageData = modelData && (modelData.stages || []).find(function (item) {
        return item.stage === stage;
      });
      var matchedRatio = stageData && (stageData.ratios || []).find(function (item) {
        return Math.abs(Number(item) - ratio) < 1e-9;
      });

      if (matchedRatio === undefined) {
        status.textContent =
          "This model / stage / ratio combination no longer matches the current published SigGear data. Return to the Selection Tool or Sample Validation Workflow before continuing.";
        return;
      }

      var decisionState = decision(sampleStatus, sampleOutcome);
      context = {
        model: model,
        stage: stage,
        ratio: Number(matchedRatio),
        sampleStatus: sampleStatus,
        sampleOutcome: sampleOutcome,
        decision: decisionState
      };

      var candidateLabel = model + " / " + stage + "-stage / " + fmt(matchedRatio, 4) + ":1";
      candidateName.textContent = candidateLabel;
      candidateDetail.textContent = modelData.diameter + " mm frame · published gearbox body length " +
        fmt(stageData.length, 2) + " mm";

      candidateCell.textContent = candidateLabel;
      sampleStatusCell.textContent = sampleStatusLabel(sampleStatus);
      sampleOutcomeCell.textContent = outcomeLabel(sampleOutcome);
      decisionStatus.textContent = decisionLabel(decisionState) + " — " + decisionDescription(decisionState);

      var slug = model.toLowerCase();
      datasheetLink.href = "../../engineering-resources/" + slug + "/datasheet/";
      interfaceLink.href = "../../engineering-resources/" + slug + "/mechanical-interface/";

      if (pilotReviewLink && decisionState === "design_in_review_ready") {
        pilotReviewLink.href = "../pilot-preparation-review/?model=" + encodeURIComponent(model) +
          "&stage=" + encodeURIComponent(stage) +
          "&ratio=" + encodeURIComponent(matchedRatio) +
          "&source=design_in_review";
        pilotReviewLink.hidden = false;
      }

      status.hidden = true;
      content.hidden = false;

      track("design_in_review_candidate_view");
    } catch (error) {
      status.textContent =
        "The current published candidate data could not be loaded. Use the Design-In Checklist manually and contact SigGear before freezing the configuration.";
    }
  }

  if (emailButton) emailButton.addEventListener("click", prepareEmail);

  init();
})();