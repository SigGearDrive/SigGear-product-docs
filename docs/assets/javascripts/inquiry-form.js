(function () {
  var form = document.getElementById("siggear-engineering-brief");
  if (!form) return;

  var validModels = ["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"];
  var applicationPrefills = {
    electric_pruning_shears: "Electric pruning shears",
    electric_curtain_blind: "Electric curtain / blind / window opener",
    smart_toilet_bidet: "Smart toilet / bidet mechanism",
    dexterous_hand_gripper: "Dexterous hand / robot gripper",
    smart_lock_access_control: "Smart lock / access-control mechanism",
    pump_valve_fluid: "Pump / valve / dosing mechanism",
    optical_positioning: "Camera module / focus / zoom / sensor positioning",
    coffee_equipment: "Coffee / beverage / dosing / dispensing equipment"
  };
  var prefilledApplicationType = "not_specified";
  var model = document.getElementById("sg-model");
  var path = document.getElementById("sg-path");
  var existingMotorFields = document.getElementById("sg-existing-motor-fields");
  var voltageField = document.getElementById("sg-voltage-field");
  var copyButton = document.getElementById("sg-copy-brief");
  var status = document.getElementById("sg-brief-status");
  var selectorCandidateBox = document.getElementById("sg-selector-candidate");
  var selectorCandidateSummary = document.getElementById("sg-selector-candidate-summary");
  var selectorCandidateStage = document.getElementById("sg-selector-candidate-stage");
  var selectorCandidateRatio = document.getElementById("sg-selector-candidate-ratio");
  var cadReadinessBox = document.getElementById("sg-cad-readiness");
  var cadReadinessStatus = document.getElementById("sg-cad-readiness-status");
  var cadReadinessGates = document.getElementById("sg-cad-readiness-gates");
  var nextStep = document.getElementById("sg-next-step");
  var selectorCandidate = null;
  var selectorReviewReason = "";
  var reviewReasons = {
    speed_above_engineering: "Continuous input speed above the standard 20,000 rpm maximum; custom feasibility review requested",
    speed_below_engineering: "Continuous input speed below the standard 1,000 rpm minimum; custom feasibility review requested",
    no_published_match: "No published standard configuration meets the specified filters; custom evaluation requested",
    custom_configuration: "Customer requests a customized gearbox or motor integration review"
  };

  function value(id) {
    var el = document.getElementById(id);
    return el ? (el.value || "").trim() : "";
  }

  function selectedText(id) {
    var el = document.getElementById(id);
    if (!el || el.selectedIndex < 0) return "";
    return (el.options[el.selectedIndex].text || "").trim();
  }

  function activeSelectorCandidate() {
    return selectorCandidate && model.value === selectorCandidate.model ? selectorCandidate : null;
  }

  function formatRatio(value) {
    return Number(value).toLocaleString(undefined, {
      maximumFractionDigits: 4,
      minimumFractionDigits: 0
    });
  }

  function clearSelectorCandidate() {
    selectorCandidate = null;
    if (selectorCandidateBox) selectorCandidateBox.hidden = true;
    if (selectorCandidateSummary) selectorCandidateSummary.textContent = "";
    if (selectorCandidateStage) selectorCandidateStage.value = "";
    if (selectorCandidateRatio) selectorCandidateRatio.value = "";
  }

  function cadReadiness() {
    var selectedPath = value("sg-path") || "not_sure";
    var candidate = activeSelectorCandidate();

    var gates = {
      candidate: !!candidate,
      motor_interface: selectedPath === "gearbox_only" ?
        !!(value("sg-motor-model") && value("sg-motor-shaft") && value("sg-motor-mount")) :
        false,
      output_interface: !!value("sg-output-interface"),
      load_duty: !!(value("sg-load") && value("sg-duty-cycle")),
      envelope: !!value("sg-size")
    };

    var relevant = !!candidate || value("sg-next-step") === "CAD / STEP review";
    var ready = relevant &&
      gates.candidate &&
      gates.motor_interface &&
      gates.output_interface &&
      gates.load_duty &&
      gates.envelope;

    return {
      relevant: relevant,
      ready: ready,
      status: relevant ? (ready ? "ready_for_cad_review" : "need_more_information") : "not_applicable",
      gates: gates,
      selected_path: selectedPath
    };
  }

  function readinessGateLabel(key, state) {
    var labels = {
      candidate: "Candidate configuration",
      motor_interface: "Motor / drive-side interface",
      output_interface: "Output interface",
      load_duty: "Load / duty",
      envelope: "Installation envelope"
    };
    return (state ? "✓ " : "○ ") + labels[key] + (state ? " — provided" : " — more information needed");
  }

  function updateCadReadiness() {
    if (!cadReadinessBox || !cadReadinessStatus || !cadReadinessGates) return;

    var readiness = cadReadiness();
    cadReadinessBox.hidden = !readiness.relevant;
    if (!readiness.relevant) return;

    cadReadinessStatus.textContent = readiness.ready ?
      "Ready for CAD Review — enough information is present for SigGear engineering to begin a configuration-specific CAD review." :
      "Need More Information — complete the missing gates below before treating the request as CAD-review ready.";

    if (readiness.selected_path === "motor_gearbox" && !readiness.gates.motor_interface) {
      cadReadinessStatus.textContent += " For a complete motor + gearbox project, the drive-side interface remains open until SigGear confirms the motor / adapter configuration.";
    }

    cadReadinessGates.innerHTML = [
      readinessGateLabel("candidate", readiness.gates.candidate),
      readinessGateLabel("motor_interface", readiness.gates.motor_interface),
      readinessGateLabel("output_interface", readiness.gates.output_interface),
      readinessGateLabel("load_duty", readiness.gates.load_duty),
      readinessGateLabel("envelope", readiness.gates.envelope)
    ].map(function (item) {
      return "<li>" + item + "</li>";
    }).join("");
  }

  function originGroup() {
    try {
      if (activeSelectorCandidate()) return "selection_tool";
      if (prefilledApplicationType !== "not_specified") return "application";
      var ref = document.referrer ? new URL(document.referrer) : null;
      if (!ref || ref.hostname !== window.location.hostname) return "direct_or_external";
      var refPath = ref.pathname || "";
      if (refPath.indexOf("/engineering-resources/") !== -1) return "engineering_resource";
      if (/\/products\/planetary-gearboxes\/\d{1,2}p-planetary-gearbox\//i.test(refPath)) return "product_model";
      if (refPath.indexOf("/products/planetary-gearboxes/") !== -1) return "planetary_series";
      if (refPath.indexOf("/applications/") !== -1) return "application";
      if (refPath === "/" || /\/SigGear-product-docs\/$/.test(refPath)) return "homepage";
      return "internal_other";
    } catch (e) {
      return "unknown";
    }
  }

  function briefMetrics() {
    var selectedPath = value("sg-path") || "not_sure";
    var hasMotorInfo = selectedPath === "motor_gearbox" ?
      !!value("sg-voltage") :
      !!(value("sg-motor-model") || value("sg-motor-speed") || value("sg-motor-shaft") || value("sg-motor-mount"));

    var checks = [
      !!value("sg-application"),
      !!value("sg-output"),
      !!value("sg-load"),
      !!value("sg-size"),
      hasMotorInfo,
      !!(value("sg-prototype-qty") || value("sg-annual-volume")),
      !!value("sg-company-country")
    ];

    var coverage = checks.filter(function (item) { return item; }).length;
    var band = coverage >= 5 ? "5_plus" : (coverage >= 3 ? "3_4" : "0_2");

    var candidate = activeSelectorCandidate();
    var readiness = cadReadiness();

    return {
      inquiry_origin: originGroup(),
      selector_handoff: candidate ? 1 : 0,
      selector_candidate_stage: candidate ? String(candidate.stage) : "none",
      cad_readiness_status: readiness.status,
      cad_gate_candidate: readiness.gates.candidate ? 1 : 0,
      cad_gate_motor_interface: readiness.gates.motor_interface ? 1 : 0,
      cad_gate_output_interface: readiness.gates.output_interface ? 1 : 0,
      cad_gate_load_duty: readiness.gates.load_duty ? 1 : 0,
      cad_gate_envelope: readiness.gates.envelope ? 1 : 0,
      project_stage: value("sg-project-stage") || "not_specified",
      requested_next_step: value("sg-next-step") || "not_specified",
      field_coverage_count: coverage,
      field_coverage_band: band,
      has_model_selection: value("sg-model") ? 1 : 0,
      has_application: value("sg-application") ? 1 : 0,
      has_output_requirement: value("sg-output") ? 1 : 0,
      has_load_requirement: value("sg-load") ? 1 : 0,
      has_size_limit: value("sg-size") ? 1 : 0,
      has_motor_or_voltage_info: hasMotorInfo ? 1 : 0,
      has_quantity_info: (value("sg-prototype-qty") || value("sg-annual-volume")) ? 1 : 0,
      has_company_country: value("sg-company-country") ? 1 : 0
    };
  }

  function track(name, extraParams) {
    if (typeof window.gtag !== "function") return;
    var params = Object.assign({
      inquiry_model: value("sg-model") || "not_specified",
      inquiry_type: value("sg-path") || "not_sure",
      inquiry_application: prefilledApplicationType,
      page_path: window.location.pathname
    }, extraParams || {});
    window.gtag("event", name, params);
  }

  function applyQueryPrefill() {
    try {
      var params = new URLSearchParams(window.location.search);
      var hasContext = false;
      var queryModel = (params.get("model") || "").toUpperCase();
      if (validModels.indexOf(queryModel) !== -1) {
        model.value = queryModel;
        hasContext = true;
      }

      var queryApplication = (params.get("app") || "").toLowerCase();
      if (Object.prototype.hasOwnProperty.call(applicationPrefills, queryApplication)) {
        prefilledApplicationType = queryApplication;
        hasContext = true;
        if (!value("sg-application")) {
          document.getElementById("sg-application").value = applicationPrefills[queryApplication];
        }
      }

      var queryPath = (params.get("path") || "").toLowerCase().replace(/-/g, "_");
      if (queryPath === "gearbox_only" || queryPath === "motor_gearbox" || queryPath === "not_sure") {
        path.value = queryPath;
        hasContext = true;
      }

      // Prefill only non-sensitive operating requirements from the selector.
      var selectionSource = (params.get("selection") || "");
      if (selectionSource === "ratio_stage_selector" || selectionSource === "selector_engineering_review") {
        if (selectionSource === "selector_engineering_review") {
          var requestedReason = params.get("selector_review_reason") || "";
          selectorReviewReason = Object.prototype.hasOwnProperty.call(reviewReasons, requestedReason) ?
            reviewReasons[requestedReason] : "Customer requests a project-specific engineering review";
        }
        var inputSpeed = Number(params.get("selector_motor_speed"));
        var outputSpeed = Number(params.get("selector_output_speed"));
        var continuousNm = Number(params.get("selector_continuous_nm"));
        var peakNm = Number(params.get("selector_peak_nm"));
        if (params.has("selector_motor_speed") && Number.isFinite(inputSpeed) && inputSpeed > 0 && inputSpeed <= 1000000) {
          var motorSpeedField = document.getElementById("sg-motor-speed");
          if (motorSpeedField && !motorSpeedField.value) motorSpeedField.value = inputSpeed + " rpm (operating)";
        }
        if (params.has("selector_output_speed") && Number.isFinite(outputSpeed) && outputSpeed > 0) {
          var outputField = document.getElementById("sg-output");
          if (outputField && !outputField.value) outputField.value = outputSpeed + " rpm";
        }
        var loads = [];
        if (params.has("selector_continuous_nm") && Number.isFinite(continuousNm) && continuousNm >= 0)
          loads.push("Continuous: " + continuousNm + " N·m");
        if (params.has("selector_peak_nm") && Number.isFinite(peakNm) && peakNm >= 0)
          loads.push("Peak: " + peakNm + " N·m (duration unverified)");
        if (loads.length) {
          var loadField = document.getElementById("sg-load");
          if (loadField && !loadField.value) loadField.value = loads.join("; ");
        }
        var maxDiameter = Number(params.get("selector_max_diameter"));
        var maxGearboxLength = Number(params.get("selector_max_gearbox_length"));
        var envelope = [];
        if (params.has("selector_max_diameter") && Number.isFinite(maxDiameter) && maxDiameter > 0)
          envelope.push("Maximum gearbox diameter: " + maxDiameter + " mm");
        if (params.has("selector_max_gearbox_length") && Number.isFinite(maxGearboxLength) && maxGearboxLength > 0)
          envelope.push("Maximum gearbox body length: " + maxGearboxLength + " mm");
        if (envelope.length) {
          var sizeField = document.getElementById("sg-size");
          if (sizeField && !sizeField.value) sizeField.value = envelope.join("; ");
        }
      }

      var queryNextStep = (params.get("next_step") || "").toLowerCase();
      if (queryNextStep === "cad_review" && nextStep) {
        nextStep.value = "CAD / STEP review";
        hasContext = true;
      }

      if (hasContext && !window.location.hash) {
        window.requestAnimationFrame(function () {
          form.scrollIntoView({ block: "start" });
        });
      }
    } catch (e) {
      // Leave default selections when the URL cannot be parsed.
    }
  }

  async function validateSelectorCandidate() {
    var params;
    try {
      params = new URLSearchParams(window.location.search);
    } catch (e) {
      return;
    }

    if ((params.get("selection") || "") !== "ratio_stage_selector") return;

    var queryModel = (params.get("model") || "").toUpperCase();
    var queryStage = Number(params.get("candidate_stage"));
    var queryRatio = Number(params.get("candidate_ratio"));

    if (validModels.indexOf(queryModel) === -1 ||
        !Number.isInteger(queryStage) || queryStage < 1 || queryStage > 4 ||
        !Number.isFinite(queryRatio) || queryRatio <= 0) {
      clearSelectorCandidate();
      status.textContent = "The preliminary selection-tool candidate could not be validated. Please choose a model or send the project details for engineering review.";
      return;
    }

    try {
      var response = await fetch(new URL("../assets/data/planetary-ratio-stage-data.json", window.location.href));
      if (!response.ok) throw new Error("Unable to load selector data.");
      var payload = await response.json();
      var modelData = (payload.models || []).find(function (item) {
        return item.model === queryModel;
      });
      var stageData = modelData && (modelData.stages || []).find(function (item) {
        return item.stage === queryStage;
      });
      var matchedRatio = stageData && (stageData.ratios || []).find(function (ratio) {
        return Math.abs(Number(ratio) - queryRatio) < 1e-9;
      });

      if (matchedRatio === undefined) {
        clearSelectorCandidate();
        status.textContent = "The preliminary selection-tool candidate no longer matches the current published ratio-stage data. Please run the selector again or send the project details for engineering review.";
        return;
      }

      model.value = queryModel;
      selectorCandidate = {
        model: queryModel,
        stage: queryStage,
        ratio: Number(matchedRatio)
      };

      if (selectorCandidateStage) selectorCandidateStage.value = String(queryStage);
      if (selectorCandidateRatio) selectorCandidateRatio.value = String(matchedRatio);
      if (selectorCandidateSummary) {
        selectorCandidateSummary.textContent =
          queryModel + " / " + queryStage + "-stage / " + formatRatio(matchedRatio) + ":1";
      }
      if (selectorCandidateBox) selectorCandidateBox.hidden = false;

      updateCadReadiness();

      track("selector_candidate_handoff_validated", {
        selector_handoff: 1,
        selector_candidate_stage: String(queryStage),
        inquiry_origin: "selection_tool"
      });
    } catch (e) {
      clearSelectorCandidate();
      status.textContent = "The preliminary selection-tool candidate could not be rechecked. You can still send the project brief; SigGear will confirm the model, stage and ratio during engineering review.";
    }
  }

  function updateConditionalFields() {
    var selected = path.value;
    existingMotorFields.hidden = selected === "motor_gearbox";
    voltageField.hidden = selected === "gearbox_only";
    updateCadReadiness();
  }

  function buildBrief() {
    var selectedPath = path.value;
    var lines = [
      "SigGear Planetary Gearbox Project Brief",
      "",
      "Model reference: " + (value("sg-model") || "Not sure yet")
    ];

    var candidate = activeSelectorCandidate();
    if (selectorReviewReason) {
      lines.push("Selector review request: " + selectorReviewReason);
      lines.push("No published standard configuration is approved by this request; engineering confirmation required.");
    }
    if (candidate) {
      lines.push(
        "Preliminary selector candidate: " +
        candidate.model + " / " + candidate.stage + "-stage / " + formatRatio(candidate.ratio) +
        ":1 (validated against current published ratio-stage data; final engineering confirmation required)"
      );
    }

    lines.push(
      "Project path: " + selectedText("sg-path"),
      "Application / what needs to move: " + (value("sg-application") || "Not provided")
    );

    if (selectedPath !== "motor_gearbox") {
      lines.push("Existing motor model / drawing reference: " + (value("sg-motor-model") || "Not provided"));
      lines.push("Motor speed: " + (value("sg-motor-speed") || "Not provided"));
      lines.push("Motor shaft / usable length: " + (value("sg-motor-shaft") || "Not provided"));
      lines.push("Motor mounting / locating pilot: " + (value("sg-motor-mount") || "Not provided"));
    }

    lines.push("Required output speed or ratio: " + (value("sg-output") || "Not provided"));
    lines.push("Load / torque: " + (value("sg-load") || "Not provided"));
    lines.push("Duty cycle / peak duration: " + (value("sg-duty-cycle") || "Not provided"));
    lines.push("External shaft loads: " + (value("sg-shaft-loads") || "Not provided"));
    lines.push("Maximum diameter / length: " + (value("sg-size") || "Not provided"));
    lines.push("Output shaft / mounting requirement: " + (value("sg-output-interface") || "Not provided"));

    if (selectedPath !== "gearbox_only") {
      lines.push("Operating voltage: " + (value("sg-voltage") || "Not provided"));
    }

    lines.push("Project stage: " + (selectedText("sg-project-stage") || "Not specified"));
    lines.push("Prototype quantity: " + (value("sg-prototype-qty") || "Not provided"));
    lines.push("Estimated annual volume: " + (value("sg-annual-volume") || "Not provided"));
    lines.push("Company / country: " + (value("sg-company-country") || "Not provided"));
    lines.push("Requested next step: " + selectedText("sg-next-step"));

    var readiness = cadReadiness();
    if (readiness.relevant) {
      lines.push("");
      lines.push("Controlled CAD review readiness: " +
        (readiness.ready ? "Ready for CAD Review" : "Need More Information"));
      lines.push("CAD gate — candidate configuration: " + (readiness.gates.candidate ? "Provided" : "Missing"));
      lines.push("CAD gate — motor / drive-side interface: " + (readiness.gates.motor_interface ? "Provided" : "Missing"));
      lines.push("CAD gate — output interface: " + (readiness.gates.output_interface ? "Provided" : "Missing"));
      lines.push("CAD gate — load / duty: " + (readiness.gates.load_duty ? "Provided" : "Missing"));
      lines.push("CAD gate — installation envelope: " + (readiness.gates.envelope ? "Provided" : "Missing"));
      lines.push("Readiness means enough information for engineering CAD review; controlled CAD release still requires SigGear confirmation.");
    }

    lines.push("");
    lines.push("I can attach a motor drawing, mechanism sketch or CAD screenshot if needed.");

    return lines.join("\n");
  }

  function subjectLine() {
    var m = value("sg-model");
    var subjectParts = [];
    var candidate = activeSelectorCandidate();
    if (m) subjectParts.push(m);
    if (candidate) {
      subjectParts.push(candidate.stage + "-stage " + formatRatio(candidate.ratio) + ":1");
    }
    if (prefilledApplicationType !== "not_specified" && applicationPrefills[prefilledApplicationType]) {
      subjectParts.push(applicationPrefills[prefilledApplicationType]);
    }
    var prefix = subjectParts.length ? subjectParts.join(" - ") + " - " : "";
    if (path.value === "gearbox_only") return prefix + "Gearbox Only Engineering Review";
    if (path.value === "motor_gearbox") return prefix + "Motor + Gearbox Engineering Review";
    return prefix + "Planetary Gearbox Project Review";
  }

  async function copyBrief() {
    var brief = buildBrief();
    try {
      await navigator.clipboard.writeText(brief);
      status.textContent = "Project brief copied. You can paste it into email, WhatsApp or another message.";
      track("engineering_brief_copy", briefMetrics());
    } catch (e) {
      var area = document.createElement("textarea");
      area.value = brief;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      document.execCommand("copy");
      document.body.removeChild(area);
      status.textContent = "Project brief copied.";
      track("engineering_brief_copy", briefMetrics());
    }
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (!form.reportValidity()) return;

    var href = "mailto:wangwanrong@siggear.com?subject=" +
      encodeURIComponent(subjectLine()) +
      "&body=" + encodeURIComponent(buildBrief());

    track("engineering_brief_prepare_email", briefMetrics());
    status.textContent = "Opening your email client with the project brief...";
    window.location.href = href;
  });

  copyButton.addEventListener("click", copyBrief);
  path.addEventListener("change", updateConditionalFields);
  if (nextStep) nextStep.addEventListener("change", updateCadReadiness);

  ["sg-motor-model","sg-motor-shaft","sg-motor-mount","sg-output-interface","sg-load","sg-duty-cycle","sg-size"].forEach(function (id) {
    var el = document.getElementById(id);
    if (el) el.addEventListener("input", updateCadReadiness);
  });

  model.addEventListener("change", function () {
    if (selectorCandidate && model.value !== selectorCandidate.model) {
      clearSelectorCandidate();
      status.textContent = "Model changed. The previous selection-tool candidate was cleared and will not be included in the project brief.";
      updateCadReadiness();
    }
  });

  applyQueryPrefill();
  updateConditionalFields();
  validateSelectorCandidate();
})();