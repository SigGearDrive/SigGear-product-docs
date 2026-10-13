(function () {
  var container = document.getElementById("sg-planetary-sample-validation");
  if (!container) return;

  var status = document.getElementById("sg-sample-validation-status");
  var content = document.getElementById("sg-sample-validation-content");
  var candidateName = document.getElementById("sg-sample-candidate-name");
  var candidateDetail = document.getElementById("sg-sample-candidate-detail");
  var form = document.getElementById("sg-sample-validation-form");
  var readiness = document.getElementById("sg-sample-readiness-status");
  var copyButton = document.getElementById("sg-copy-sample-summary");
  var emailButton = document.getElementById("sg-email-sample-summary");
  var actionStatus = document.getElementById("sg-sample-action-status");
  var datasheetLink = document.getElementById("sg-sample-datasheet");
  var interfaceLink = document.getElementById("sg-sample-interface");

  var validModels = ["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"];
  var candidate = null;

  function value(id) {
    var el = document.getElementById(id);
    return el ? (el.value || "").trim() : "";
  }

  function fmt(value, digits) {
    return Number(value).toLocaleString(undefined, {
      maximumFractionDigits: digits,
      minimumFractionDigits: 0
    });
  }

  function labelForStatus(value) {
    if (value === "pass") return "Pass";
    if (value === "issue") return "Issue";
    return "Not checked";
  }

  function labelForOutcome(value) {
    var labels = {
      not_decided: "Not decided yet",
      keep_current_configuration: "Keep current configuration for next review",
      change_ratio: "Review a different ratio / stage",
      change_motor_or_input: "Review motor / input-side configuration",
      revise_mechanical_interface: "Revise mounting / shaft / interface",
      more_testing_required: "More testing required",
      ready_for_design_in_review: "Submit current configuration for Design-In review"
    };
    return labels[value] || labels.not_decided;
  }

  function validationState() {
    var steps = [
      value("sg-sample-config-status"),
      value("sg-sample-fit-status"),
      value("sg-sample-noload-status"),
      value("sg-sample-functional-status"),
      value("sg-sample-application-status")
    ];

    if (steps.indexOf("issue") !== -1) return "engineering_iteration_required";
    if (steps.every(function (item) { return item === "pass"; })) {
      return "ready_to_submit_for_design_in_review";
    }
    return "validation_in_progress";
  }

  function updateReadiness() {
    var state = validationState();
    if (state === "engineering_iteration_required") {
      readiness.textContent =
        "Engineering Iteration Required — at least one validation step is marked as an issue. Review the affected configuration or test condition before Design-In submission.";
    } else if (state === "ready_to_submit_for_design_in_review") {
      readiness.textContent =
        "Ready to Submit for Design-In Review — all five sample-validation steps are marked Pass. This means the sample evidence is ready for engineering review; it is not final Design-In approval.";
    } else {
      readiness.textContent =
        "Validation in Progress — record each step before submitting the configuration for Design-In review.";
    }
  }

  function buildSummary() {
    if (!candidate) return "";

    var state = validationState();
    var lines = [
      "SigGear Planetary Gearbox Sample Validation Summary",
      "",
      "Validated candidate: " + candidate.model + " / " + candidate.stage + "-stage / " +
        fmt(candidate.ratio, 4) + ":1",
      "Published gearbox body length: " + fmt(candidate.length, 2) + " mm",
      "",
      "1. Configuration received: " + labelForStatus(value("sg-sample-config-status")),
      "2. Mechanical fit: " + labelForStatus(value("sg-sample-fit-status")),
      "3. No-load / free-rotation check: " + labelForStatus(value("sg-sample-noload-status")),
      "4. Functional test: " + labelForStatus(value("sg-sample-functional-status")),
      "5. Representative application-load test: " + labelForStatus(value("sg-sample-application-status")),
      "",
      "Validation status: " +
        (state === "engineering_iteration_required" ? "Engineering Iteration Required" :
         state === "ready_to_submit_for_design_in_review" ? "Ready to Submit for Design-In Review" :
         "Validation in Progress"),
      "Engineering outcome: " + labelForOutcome(value("sg-sample-outcome")),
      "",
      "Test operating condition / evidence: " + (value("sg-sample-test-condition") || "Not provided"),
      "Issue / observation notes: " + (value("sg-sample-notes") || "Not provided"),
      "",
      "Note: This is a customer-side sample evaluation summary. A recorded Pass does not by itself constitute SigGear production approval or final Design-In approval."
    ];

    return lines.join("\n");
  }

  function track(name) {
    if (typeof window.gtag !== "function" || !candidate) return;
    window.gtag("event", name, {
      page_path: window.location.pathname,
      inquiry_model: candidate.model,
      selector_candidate_stage: String(candidate.stage),
      sample_validation_status: validationState(),
      sample_validation_outcome: value("sg-sample-outcome") || "not_decided"
    });
  }

  async function copySummary() {
    var summary = buildSummary();
    if (!summary) return;

    try {
      await navigator.clipboard.writeText(summary);
      actionStatus.textContent = "Sample validation summary copied.";
    } catch (e) {
      var area = document.createElement("textarea");
      area.value = summary;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      document.execCommand("copy");
      document.body.removeChild(area);
      actionStatus.textContent = "Sample validation summary copied.";
    }
    track("sample_validation_summary_copy");
  }

  function prepareEmail() {
    var summary = buildSummary();
    if (!summary || !candidate) return;
    track("sample_validation_prepare_email");
    var subject = candidate.model + " - " + candidate.stage + "-stage " +
      fmt(candidate.ratio, 4) + ":1 - Sample Validation Review";
    window.location.href = "mailto:wangwanrong@siggear.com?subject=" +
      encodeURIComponent(subject) + "&body=" + encodeURIComponent(summary);
  }

  async function init() {
    var params = new URLSearchParams(window.location.search);
    var model = (params.get("model") || "").toUpperCase();
    var stage = Number(params.get("stage"));
    var ratio = Number(params.get("ratio"));

    if (validModels.indexOf(model) === -1 ||
        !Number.isInteger(stage) || stage < 1 || stage > 4 ||
        !Number.isFinite(ratio) || ratio <= 0) {
      return;
    }

    container.hidden = false;

    try {
      var response = await fetch(new URL("../../assets/data/planetary-ratio-stage-data.json", window.location.href));
      if (!response.ok) throw new Error("Unable to load published ratio-stage data.");
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
          "This model / stage / ratio combination no longer matches the current published SigGear ratio-stage data. Run the Selection Tool again before recording a sample validation.";
        return;
      }

      candidate = {
        model: model,
        stage: stage,
        ratio: Number(matchedRatio),
        length: stageData.length
      };

      var slug = model.toLowerCase();
      candidateName.textContent = model + " / " + stage + "-stage / " + fmt(matchedRatio, 4) + ":1";
      candidateDetail.textContent = modelData.diameter + " mm frame · published gearbox body length " +
        fmt(stageData.length, 2) + " mm";

      datasheetLink.href = "../../engineering-resources/" + slug + "/datasheet/";
      interfaceLink.href = "../../engineering-resources/" + slug + "/mechanical-interface/";

      status.hidden = true;
      content.hidden = false;
      updateReadiness();

      if (typeof window.gtag === "function") {
        window.gtag("event", "sample_validation_candidate_view", {
          page_path: window.location.pathname,
          inquiry_model: model,
          selector_candidate_stage: String(stage)
        });
      }
    } catch (e) {
      status.textContent =
        "The current candidate data could not be loaded. Use the Datasheet / Mechanical Interface and contact SigGear before recording a configuration-specific sample result.";
    }
  }

  if (form) {
    form.addEventListener("change", updateReadiness);
    form.addEventListener("input", updateReadiness);
  }
  if (copyButton) copyButton.addEventListener("click", copySummary);
  if (emailButton) emailButton.addEventListener("click", prepareEmail);

  init();
})();