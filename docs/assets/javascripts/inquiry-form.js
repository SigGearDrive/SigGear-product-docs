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

  function value(id) {
    var el = document.getElementById(id);
    return el ? (el.value || "").trim() : "";
  }

  function selectedText(id) {
    var el = document.getElementById(id);
    if (!el || el.selectedIndex < 0) return "";
    return (el.options[el.selectedIndex].text || "").trim();
  }

  function originGroup() {
    try {
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

    return {
      inquiry_origin: originGroup(),
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

      if (hasContext && !window.location.hash) {
        window.requestAnimationFrame(function () {
          form.scrollIntoView({ block: "start" });
        });
      }
    } catch (e) {
      // Leave default selections when the URL cannot be parsed.
    }
  }

  function updateConditionalFields() {
    var selected = path.value;
    existingMotorFields.hidden = selected === "motor_gearbox";
    voltageField.hidden = selected === "gearbox_only";
  }

  function buildBrief() {
    var selectedPath = path.value;
    var lines = [
      "SigGear Planetary Gearbox Project Brief",
      "",
      "Model reference: " + (value("sg-model") || "Not sure yet"),
      "Project path: " + selectedText("sg-path"),
      "Application / what needs to move: " + (value("sg-application") || "Not provided")
    ];

    if (selectedPath !== "motor_gearbox") {
      lines.push("Existing motor model / drawing reference: " + (value("sg-motor-model") || "Not provided"));
      lines.push("Motor speed: " + (value("sg-motor-speed") || "Not provided"));
      lines.push("Motor shaft / usable length: " + (value("sg-motor-shaft") || "Not provided"));
      lines.push("Motor mounting / locating pilot: " + (value("sg-motor-mount") || "Not provided"));
    }

    lines.push("Required output speed or ratio: " + (value("sg-output") || "Not provided"));
    lines.push("Load / torque: " + (value("sg-load") || "Not provided"));
    lines.push("Maximum diameter / length: " + (value("sg-size") || "Not provided"));

    if (selectedPath !== "gearbox_only") {
      lines.push("Operating voltage: " + (value("sg-voltage") || "Not provided"));
    }

    lines.push("Project stage: " + (selectedText("sg-project-stage") || "Not specified"));
    lines.push("Prototype quantity: " + (value("sg-prototype-qty") || "Not provided"));
    lines.push("Estimated annual volume: " + (value("sg-annual-volume") || "Not provided"));
    lines.push("Company / country: " + (value("sg-company-country") || "Not provided"));
    lines.push("Requested next step: " + selectedText("sg-next-step"));
    lines.push("");
    lines.push("I can attach a motor drawing, mechanism sketch or CAD screenshot if needed.");

    return lines.join("\n");
  }

  function subjectLine() {
    var m = value("sg-model");
    var subjectParts = [];
    if (m) subjectParts.push(m);
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

  applyQueryPrefill();
  updateConditionalFields();
})();