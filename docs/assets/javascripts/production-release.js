(function () {
  var container = document.getElementById("sg-production-release");
  if (!container) return;

  var status = document.getElementById("sg-production-release-status");
  var content = document.getElementById("sg-production-release-content");
  var candidateName = document.getElementById("sg-production-candidate-name");
  var candidateDetail = document.getElementById("sg-production-candidate-detail");
  var form = document.getElementById("sg-production-release-form");
  var readinessStatus = document.getElementById("sg-production-readiness-status");
  var readinessGates = document.getElementById("sg-production-readiness-gates");
  var copyButton = document.getElementById("sg-copy-production-summary");
  var emailButton = document.getElementById("sg-email-production-summary");
  var actionStatus = document.getElementById("sg-production-action-status");
  var datasheetLink = document.getElementById("sg-production-datasheet");
  var interfaceLink = document.getElementById("sg-production-interface");

  var validModels = ["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"];
  var context = null;

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

  function readiness() {
    var pilotConfirmed = value("sg-production-pilot-confirmation") ===
      "confirmed_completed_by_responsible_team";
    var pilotResult = value("sg-production-pilot-result");
    var configuration = value("sg-production-configuration-change");

    var gates = {
      pilot_result_confirmation: pilotConfirmed && pilotResult !== "not_recorded",
      configuration_continuity: configuration === "unchanged_from_pilot",
      final_configuration: !!(value("sg-production-drawing-revision") &&
        value("sg-production-bom-revision")),
      inspection_evidence: !!value("sg-production-inspection-result"),
      deviation_disposition: !!value("sg-production-deviations"),
      packaging_freeze: value("sg-production-packaging-freeze") !== "not_confirmed",
      forecast: !!value("sg-production-forecast"),
      production_test_plan: !!value("sg-production-test-plan"),
      change_control: !!value("sg-production-change-control"),
      open_items_disposition: !!value("sg-production-open-items")
    };

    var statusValue = "need_pilot_result_confirmation";

    if (pilotConfirmed && pilotResult !== "not_recorded") {
      if (pilotResult === "issues_require_revision" ||
          configuration === "changed_after_pilot") {
        statusValue = "engineering_change_or_revalidation_required";
      } else {
        var allRequired = gates.configuration_continuity &&
          gates.final_configuration &&
          gates.inspection_evidence &&
          gates.deviation_disposition &&
          gates.packaging_freeze &&
          gates.forecast &&
          gates.production_test_plan &&
          gates.change_control &&
          gates.open_items_disposition;

        statusValue = allRequired ?
          "ready_to_submit_for_production_release_review" :
          "production_release_review_incomplete";
      }
    }

    return {
      status: statusValue,
      pilotResult: pilotResult,
      configuration: configuration,
      gates: gates
    };
  }

  function gateLabel(label, complete) {
    return (complete ? "✓ " : "○ ") + label + (complete ? " — provided" : " — more information needed");
  }

  function statusLabel(value) {
    if (value === "engineering_change_or_revalidation_required") {
      return "Engineering Change / Revalidation Required";
    }
    if (value === "production_release_review_incomplete") {
      return "Production Release Review Incomplete";
    }
    if (value === "ready_to_submit_for_production_release_review") {
      return "Ready to Submit for Production Release Review";
    }
    return "Need Pilot Result Confirmation";
  }

  function updateReadiness() {
    var current = readiness();

    if (current.status === "need_pilot_result_confirmation") {
      readinessStatus.textContent =
        "Need Pilot Result Confirmation — the responsible project / engineering / quality team must complete and review the pilot build before production-release review.";
    } else if (current.status === "engineering_change_or_revalidation_required") {
      readinessStatus.textContent =
        "Engineering Change / Revalidation Required — the pilot result or post-pilot configuration changed. Return the affected configuration to engineering review before production release.";
    } else if (current.status === "production_release_review_incomplete") {
      readinessStatus.textContent =
        "Production Release Review Incomplete — the pilot is reported accepted, but one or more release-package gates still need information.";
    } else {
      readinessStatus.textContent =
        "Ready to Submit for Production Release Review — the release package is complete enough for human review. This is not Production Released or mass-production approval.";
    }

    readinessGates.innerHTML = [
      gateLabel("Pilot build / result confirmation", current.gates.pilot_result_confirmation),
      gateLabel("Configuration unchanged from accepted pilot", current.gates.configuration_continuity),
      gateLabel("Final drawing + configuration / BOM revision", current.gates.final_configuration),
      gateLabel("Pilot inspection / acceptance evidence", current.gates.inspection_evidence),
      gateLabel("Deviation / concession disposition", current.gates.deviation_disposition),
      gateLabel("Packaging / labeling freeze", current.gates.packaging_freeze),
      gateLabel("Forecast / expected annual volume", current.gates.forecast),
      gateLabel("Production inspection / test plan", current.gates.production_test_plan),
      gateLabel("Change-control agreement", current.gates.change_control),
      gateLabel("Remaining risks / open-item disposition", current.gates.open_items_disposition)
    ].map(function (item) {
      return "<li>" + item + "</li>";
    }).join("");
  }

  function buildSummary() {
    if (!context) return "";

    var current = readiness();
    var lines = [
      "SigGear Production Release Review Summary",
      "",
      "Validated candidate: " + context.model + " / " + context.stage + "-stage / " +
        fmt(context.ratio, 4) + ":1",
      "Production release checklist status: " + statusLabel(current.status),
      "",
      "Pilot build / result confirmation: " +
        (value("sg-production-pilot-confirmation") === "confirmed_completed_by_responsible_team" ?
          "Reported completed and confirmed by responsible team" : "Not confirmed"),
      "Pilot result: " + (value("sg-production-pilot-result") || "Not recorded"),
      "Configuration after pilot: " + (value("sg-production-configuration-change") || "Not confirmed"),
      "Final controlled drawing revision: " + (value("sg-production-drawing-revision") || "Not provided"),
      "Final configuration / BOM revision: " + (value("sg-production-bom-revision") || "Not provided"),
      "Pilot inspection / acceptance evidence: " + (value("sg-production-inspection-result") || "Not provided"),
      "Approved deviations / concessions: " + (value("sg-production-deviations") || "Not provided"),
      "Packaging / labeling freeze: " + (value("sg-production-packaging-freeze") || "Not confirmed"),
      "Forecast / expected annual volume: " + (value("sg-production-forecast") || "Not provided"),
      "Production inspection / test plan: " + (value("sg-production-test-plan") || "Not provided"),
      "Change-control agreement: " + (value("sg-production-change-control") || "Not provided"),
      "Remaining risks / open items: " + (value("sg-production-open-items") || "Not provided"),
      "Production-release documentation / traceability: " + (value("sg-production-documentation") || "Not provided"),
      "",
      "Note: This summary is preparation material for human production-release review. It does not by itself approve the pilot result, Production Release, mass production or manufacturing start."
    ];

    return lines.join("\n");
  }

  function track(name) {
    if (typeof window.gtag !== "function" || !context) return;
    var current = readiness();
    window.gtag("event", name, {
      page_path: window.location.pathname,
      inquiry_model: context.model,
      selector_candidate_stage: String(context.stage),
      production_release_review_status: current.status,
      production_gate_pilot_result: current.gates.pilot_result_confirmation ? 1 : 0,
      production_gate_configuration_continuity: current.gates.configuration_continuity ? 1 : 0,
      production_gate_final_configuration: current.gates.final_configuration ? 1 : 0,
      production_gate_inspection_evidence: current.gates.inspection_evidence ? 1 : 0,
      production_gate_deviation_disposition: current.gates.deviation_disposition ? 1 : 0,
      production_gate_packaging_freeze: current.gates.packaging_freeze ? 1 : 0,
      production_gate_forecast: current.gates.forecast ? 1 : 0,
      production_gate_test_plan: current.gates.production_test_plan ? 1 : 0,
      production_gate_change_control: current.gates.change_control ? 1 : 0,
      production_gate_open_items: current.gates.open_items_disposition ? 1 : 0
    });
  }

  async function copySummary() {
    var summary = buildSummary();
    if (!summary) return;

    try {
      await navigator.clipboard.writeText(summary);
    } catch (error) {
      var area = document.createElement("textarea");
      area.value = summary;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      document.execCommand("copy");
      document.body.removeChild(area);
    }

    actionStatus.textContent = "Production release review summary copied.";
    track("production_release_summary_copy");
  }

  function prepareEmail() {
    if (!context) return;
    var summary = buildSummary();
    var subject = context.model + " - " + context.stage + "-stage " +
      fmt(context.ratio, 4) + ":1 - Production Release Review";

    actionStatus.textContent = "Opening your email client with the production-release review summary...";
    track("production_release_prepare_email");

    window.location.href = "mailto:wangwanrong@siggear.com?subject=" +
      encodeURIComponent(subject) + "&body=" + encodeURIComponent(summary);
  }

  async function init() {
    var params = new URLSearchParams(window.location.search);
    if ((params.get("source") || "") !== "pilot_preparation_review") return;

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
          "This model / stage / ratio combination no longer matches the current published SigGear data. Return to the pilot / Design-In review before preparing a production-release package.";
        return;
      }

      context = {
        model: model,
        stage: stage,
        ratio: Number(matchedRatio)
      };

      var candidateLabel = model + " / " + stage + "-stage / " + fmt(matchedRatio, 4) + ":1";
      candidateName.textContent = candidateLabel;
      candidateDetail.textContent = modelData.diameter + " mm frame · published gearbox body length " +
        fmt(stageData.length, 2) + " mm";

      var slug = model.toLowerCase();
      datasheetLink.href = "../../engineering-resources/" + slug + "/datasheet/";
      interfaceLink.href = "../../engineering-resources/" + slug + "/mechanical-interface/";

      status.hidden = true;
      content.hidden = false;
      updateReadiness();
      track("production_release_review_view");
    } catch (error) {
      status.textContent =
        "The current candidate data could not be loaded. Use the production-release checklist manually and contact SigGear before any production-release decision.";
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