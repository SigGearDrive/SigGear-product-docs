(function () {
  var container = document.getElementById("sg-pilot-preparation");
  if (!container) return;

  var status = document.getElementById("sg-pilot-preparation-status");
  var content = document.getElementById("sg-pilot-preparation-content");
  var candidateName = document.getElementById("sg-pilot-candidate-name");
  var candidateDetail = document.getElementById("sg-pilot-candidate-detail");
  var form = document.getElementById("sg-pilot-preparation-form");
  var readinessStatus = document.getElementById("sg-pilot-readiness-status");
  var readinessGates = document.getElementById("sg-pilot-readiness-gates");
  var copyButton = document.getElementById("sg-copy-pilot-summary");
  var emailButton = document.getElementById("sg-email-pilot-summary");
  var actionStatus = document.getElementById("sg-pilot-action-status");
  var datasheetLink = document.getElementById("sg-pilot-datasheet");
  var interfaceLink = document.getElementById("sg-pilot-interface");
  var productionReviewLink = document.getElementById("sg-pilot-production-review");

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
    var gates = {
      design_freeze: value("sg-pilot-design-freeze") === "confirmed_by_responsible_team",
      controlled_configuration: !!(value("sg-pilot-drawing-revision") && value("sg-pilot-bom-revision")),
      quantity_schedule: !!(value("sg-pilot-quantity") && value("sg-pilot-schedule")),
      inspection: !!value("sg-pilot-inspection"),
      packaging: !!value("sg-pilot-packaging"),
      change_control: !!value("sg-pilot-change-control"),
      acceptance_plan: !!value("sg-pilot-acceptance-plan")
    };

    var allAfterFreeze = gates.controlled_configuration &&
      gates.quantity_schedule &&
      gates.inspection &&
      gates.packaging &&
      gates.change_control &&
      gates.acceptance_plan;

    var normalizedStatus = "need_design_freeze_confirmation";
    if (gates.design_freeze) {
      normalizedStatus = allAfterFreeze ?
        "ready_to_submit_for_pilot_preparation_review" :
        "pilot_review_incomplete";
    }

    return {
      status: normalizedStatus,
      gates: gates
    };
  }

  function gateLabel(label, complete) {
    return (complete ? "✓ " : "○ ") + label + (complete ? " — provided" : " — more information needed");
  }

  function statusLabel(value) {
    if (value === "ready_to_submit_for_pilot_preparation_review") {
      return "Ready to Submit for Pilot Preparation Review";
    }
    if (value === "pilot_review_incomplete") {
      return "Pilot Review Incomplete";
    }
    return "Need Design Freeze Confirmation";
  }

  function updateProductionHandoff(current) {
    if (!productionReviewLink || !context) return;

    if (current.status === "ready_to_submit_for_pilot_preparation_review") {
      productionReviewLink.href = "../production-release-review/?model=" +
        encodeURIComponent(context.model) +
        "&stage=" + encodeURIComponent(context.stage) +
        "&ratio=" + encodeURIComponent(context.ratio) +
        "&source=pilot_preparation_review";
      productionReviewLink.hidden = false;
    } else {
      productionReviewLink.hidden = true;
      productionReviewLink.removeAttribute("href");
    }
  }

  function updateReadiness() {
    var current = readiness();

    if (current.status === "need_design_freeze_confirmation") {
      readinessStatus.textContent =
        "Need Design Freeze Confirmation — the responsible engineering / project team must confirm Design Freeze before this checklist can be treated as pilot-review ready.";
    } else if (current.status === "pilot_review_incomplete") {
      readinessStatus.textContent =
        "Pilot Review Incomplete — Design Freeze is reported as confirmed, but one or more pilot-preparation gates still need information.";
    } else {
      readinessStatus.textContent =
        "Ready to Submit for Pilot Preparation Review — the checklist is complete enough for a human pilot-preparation review. This is not Pilot Preparation Ready or production approval.";
    }

    readinessGates.innerHTML = [
      gateLabel("Design Freeze confirmation", current.gates.design_freeze),
      gateLabel("Controlled drawing + configuration / BOM revision", current.gates.controlled_configuration),
      gateLabel("Pilot quantity + schedule", current.gates.quantity_schedule),
      gateLabel("Critical inspection / acceptance characteristics", current.gates.inspection),
      gateLabel("Packaging / labeling requirement", current.gates.packaging),
      gateLabel("Change-notification expectation", current.gates.change_control),
      gateLabel("Pilot acceptance / validation plan", current.gates.acceptance_plan)
    ].map(function (item) {
      return "<li>" + item + "</li>";
    }).join("");

    updateProductionHandoff(current);
  }

  function buildSummary() {
    if (!context) return "";

    var current = readiness();
    var lines = [
      "SigGear Pilot Preparation Review Summary",
      "",
      "Validated candidate: " + context.model + " / " + context.stage + "-stage / " +
        fmt(context.ratio, 4) + ":1",
      "Pilot preparation checklist status: " + statusLabel(current.status),
      "",
      "Design Freeze confirmation: " +
        (current.gates.design_freeze ? "Reported confirmed by responsible engineering / project team" : "Not confirmed"),
      "Controlled drawing revision: " + (value("sg-pilot-drawing-revision") || "Not provided"),
      "Configuration / BOM revision: " + (value("sg-pilot-bom-revision") || "Not provided"),
      "Pilot quantity: " + (value("sg-pilot-quantity") || "Not provided"),
      "Target pilot schedule: " + (value("sg-pilot-schedule") || "Not provided"),
      "Critical inspection / acceptance characteristics: " + (value("sg-pilot-inspection") || "Not provided"),
      "Packaging / labeling requirement: " + (value("sg-pilot-packaging") || "Not provided"),
      "Change-notification expectation: " + (value("sg-pilot-change-control") || "Not provided"),
      "Pilot acceptance / validation plan: " + (value("sg-pilot-acceptance-plan") || "Not provided"),
      "Project-specific documentation: " + (value("sg-pilot-documentation") || "Not provided"),
      "",
      "Note: This summary is preparation material for human review. It does not by itself confirm Design Freeze, Pilot Preparation Ready, pilot build approval or Production Release."
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
      pilot_review_status: current.status,
      pilot_gate_design_freeze: current.gates.design_freeze ? 1 : 0,
      pilot_gate_controlled_configuration: current.gates.controlled_configuration ? 1 : 0,
      pilot_gate_quantity_schedule: current.gates.quantity_schedule ? 1 : 0,
      pilot_gate_inspection: current.gates.inspection ? 1 : 0,
      pilot_gate_packaging: current.gates.packaging ? 1 : 0,
      pilot_gate_change_control: current.gates.change_control ? 1 : 0,
      pilot_gate_acceptance_plan: current.gates.acceptance_plan ? 1 : 0
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

    actionStatus.textContent = "Pilot preparation review summary copied.";
    track("pilot_preparation_summary_copy");
  }

  function prepareEmail() {
    if (!context) return;
    var summary = buildSummary();
    var subject = context.model + " - " + context.stage + "-stage " +
      fmt(context.ratio, 4) + ":1 - Pilot Preparation Review";

    actionStatus.textContent = "Opening your email client with the pilot-preparation review summary...";
    track("pilot_preparation_prepare_email");

    window.location.href = "mailto:wangwanrong@siggear.com?subject=" +
      encodeURIComponent(subject) + "&body=" + encodeURIComponent(summary);
  }

  async function init() {
    var params = new URLSearchParams(window.location.search);
    if ((params.get("source") || "") !== "design_in_review") return;

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
          "This model / stage / ratio combination no longer matches the current published SigGear data. Return to Design-In Review before preparing a pilot checklist.";
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
      track("pilot_preparation_review_view");
    } catch (error) {
      status.textContent =
        "The current candidate data could not be loaded. Use the pilot-preparation checklist manually and contact SigGear before planning the pilot build.";
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