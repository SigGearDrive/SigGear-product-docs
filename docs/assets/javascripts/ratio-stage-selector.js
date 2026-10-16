(function () {
  var form = document.getElementById("siggear-ratio-stage-selector");
  if (!form) return;

  var results = document.getElementById("sg-ratio-stage-results");
  var summary = document.getElementById("sg-ratio-stage-summary");

  var speedBounds = null;
  var dataPromise = fetch(new URL("../../assets/data/planetary-ratio-stage-data.json", window.location.href))
    .then(function (response) {
      if (!response.ok) throw new Error("Unable to load published ratio-stage data.");
      return response.json();
    })
    .then(function (payload) {
      var bounds = payload && payload.continuous_input_speed_rpm;
      if (!payload || !Array.isArray(payload.models) || !bounds ||
          !Number.isFinite(bounds.min) || !Number.isFinite(bounds.max) ||
          bounds.min <= 0 || bounds.max <= bounds.min) {
        throw new Error("Published ratio-stage or input-speed data is invalid.");
      }
      speedBounds = bounds;
      return payload.models;
    });

  // Safe application categories shared with the online engineering project brief.
  // Only a known category slug travels through URLs; never customer project text.
  var supportedApplications = {
    electric_pruning_shears: "Electric pruning shears",
    electric_curtain_blind: "Electric curtain / blind / window opener",
    smart_toilet_bidet: "Smart toilet / bidet mechanism",
    dexterous_hand_gripper: "Dexterous hand / robot gripper"
  };
  var selectorApplication = "";
  try {
    var appSlug = new URL(window.location.href).searchParams.get("app") || "";
    if (Object.prototype.hasOwnProperty.call(supportedApplications, appSlug)) {
      selectorApplication = appSlug;
    }
  } catch (error) {
    // Invalid or unrecognized application identifiers cannot alter selection.
  }
  var appContextLabel = document.getElementById("sg-selector-application-context");
  if (appContextLabel && selectorApplication) {
    appContextLabel.hidden = false;
    appContextLabel.textContent = "Application: " + supportedApplications[selectorApplication] +
      ". The published parameters below determine candidates; your application context will also appear in the engineering project brief.";
  }

  var KGF_CM_TO_NM = 0.0980665;
  function torqueUnit() {
    var input = document.getElementById("sg-selector-torque-unit");
    return input && input.value === "kgfcm" ? "kgfcm" : "nm";
  }
  function toPublishedTorque(value) {
    return value === null ? null : (torqueUnit() === "nm" ? value / KGF_CM_TO_NM : value);
  }
  function torqueDisplay(value) {
    return torqueUnit() === "nm" ? fmt(value * KGF_CM_TO_NM, 3) + " N·m" : fmt(value, 2) + " kgf·cm";
  }
  function selectorContext(motorSpeed, outputSpeed, continuous, peak, maxDiameter, maxLength) {
    var params = "";
    if (selectorApplication) params += "&app=" + encodeURIComponent(selectorApplication);
    if (motorSpeed !== null) params += "&selector_motor_speed=" + encodeURIComponent(motorSpeed);
    if (outputSpeed !== null) params += "&selector_output_speed=" + encodeURIComponent(outputSpeed);
    if (continuous !== null) params += "&selector_continuous_nm=" + encodeURIComponent((continuous * KGF_CM_TO_NM).toFixed(5));
    if (peak !== null) params += "&selector_peak_nm=" + encodeURIComponent((peak * KGF_CM_TO_NM).toFixed(5));
    if (maxDiameter !== null && maxDiameter > 0) params += "&selector_max_diameter=" + encodeURIComponent(maxDiameter);
    if (maxLength !== null && maxLength > 0) params += "&selector_max_gearbox_length=" + encodeURIComponent(maxLength);
    return params;
  }
  function selectionParams(item, motorSpeed, outputSpeed, continuous, peak, maxDiameter, maxLength) {
    return "&selection=ratio_stage_selector&candidate_stage=" +
      encodeURIComponent(item.stage) + "&candidate_ratio=" + encodeURIComponent(item.ratio) +
      selectorContext(motorSpeed, outputSpeed, continuous, peak, maxDiameter, maxLength);
  }
  function customReviewLink(reason, motorSpeed, outputSpeed, continuous, peak, maxDiameter, maxLength) {
    return "../../request-cad-sample-quote/?path=not_sure&selection=selector_engineering_review" +
      "&selector_review_reason=" + encodeURIComponent(reason) +
      selectorContext(motorSpeed, outputSpeed, continuous, peak, maxDiameter, maxLength);
  }
  function customReviewAction(reason, motorSpeed, outputSpeed, continuous, peak, maxDiameter, maxLength) {
    return "<p><a class=\"md-button md-button--primary\" href=\"" +
      esc(customReviewLink(reason, motorSpeed, outputSpeed, continuous, peak, maxDiameter, maxLength)) +
      "\">Request Custom Engineering Review</a></p>";
  }
  function numberValue(id) {
    var el = document.getElementById(id);
    if (!el || !el.value.trim()) return null;
    var n = Number(el.value);
    return Number.isFinite(n) ? n : null;
  }

  function fmt(value, digits) {
    return Number(value).toLocaleString(undefined, {
      maximumFractionDigits: digits,
      minimumFractionDigits: 0
    });
  }

  function esc(value) {
    return String(value).replace(/[&<>"']/g, function (ch) {
      return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[ch];
    });
  }

  function itemKey(item) {
    return item ? [item.model, item.stage, item.ratio].join("|") : "";
  }

  function track(configurationCount, frameCount, top, smallest, shortest) {
    if (typeof window.gtag !== "function") return;
    window.gtag("event", "ratio_stage_selector_run", {
      page_path: window.location.pathname,
      used_diameter_filter: numberValue("sg-selector-diameter") !== null ? 1 : 0,
      used_length_filter: numberValue("sg-selector-length") !== null ? 1 : 0,
      used_torque_filter: numberValue("sg-selector-torque") !== null ? 1 : 0,
      used_ratio_tolerance_filter: numberValue("sg-selector-ratio-tolerance") !== null ? 1 : 0,
      inquiry_application: selectorApplication || "not_specified",
      result_count: configurationCount,
      candidate_frame_count: frameCount,
      top_candidate_model: top ? top.model : "none",
      top_candidate_stage: top ? String(top.stage) : "none",
      smallest_candidate_model: smallest ? smallest.model : "none",
      shortest_candidate_model: shortest ? shortest.model : "none"
    });
  }

  function candidateLink(item, label) {
    var slug = item.model.toLowerCase();
    return "<a href=\"../../products/planetary-gearboxes/" + slug + "-planetary-gearbox/\">" +
      esc(label || item.model) + "</a>";
  }

  function benchmarkCard(title, item, detail) {
    if (!item) return "";
    return "<div class=\"siggear-candidate-card\">" +
      "<strong>" + esc(title) + "</strong>" +
      "<span>" + candidateLink(item, item.model + " · " + item.stage + "-stage · " + fmt(item.ratio, 2) + ":1") + "</span>" +
      "<small>" + esc(detail) + "</small>" +
      "</div>";
  }

  // Product detail links may suggest a known frame diameter without forcing a final model.
  // Keep this optional, editable and distinct from engineering verification.
  function prefillDiameterFromProductPage() {
    try {
      var suggested = new URL(window.location.href).searchParams.get("max_diameter");
      var allowed = ["8","10","12","14","16","20","22","24","28","32","36","42"];
      if (allowed.indexOf(suggested) === -1) return;
      var input = document.getElementById("sg-selector-diameter");
      if (input && !input.value.trim()) input.value = suggested;
    } catch (error) {
      // Invalid optional query values must not block normal selection.
    }
  }
  prefillDiameterFromProductPage();

  var unitInput = document.getElementById("sg-selector-torque-unit");
  if (unitInput) {
    var previousUnit = torqueUnit();
    unitInput.addEventListener("change", function () {
      var newUnit = torqueUnit();
      if (previousUnit === newUnit) return;
      ["sg-selector-torque", "sg-selector-peak-torque"].forEach(function (id) {
        var input = document.getElementById(id);
        if (!input || !input.value.trim()) return;
        var value = Number(input.value);
        if (!Number.isFinite(value) || value < 0) return;
        var converted = newUnit === "nm" ? value * KGF_CM_TO_NM : value / KGF_CM_TO_NM;
        input.value = String(Number(converted.toPrecision(9)));
      });
      previousUnit = newUnit;
    });
  }

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    var gearboxes;
    try {
      gearboxes = await dataPromise;
    } catch (error) {
      summary.textContent = "Published ratio-stage data could not be loaded. Open the Datasheet or send the project for engineering review.";
      results.innerHTML = "";
      return;
    }

    var motorSpeed = numberValue("sg-selector-motor-speed");
    var outputSpeed = numberValue("sg-selector-output-speed");
    var maxDiameter = numberValue("sg-selector-diameter");
    var maxLength = numberValue("sg-selector-length");
    var requiredTorqueInput = numberValue("sg-selector-torque");
    var peakTorqueInput = numberValue("sg-selector-peak-torque");
    var requiredTorque = toPublishedTorque(requiredTorqueInput);
    var peakTorque = toPublishedTorque(peakTorqueInput);
    var maxRatioDiff = numberValue("sg-selector-ratio-tolerance");

    if (!motorSpeed || motorSpeed <= 0 || !outputSpeed || outputSpeed <= 0) {
      summary.textContent = "Enter a motor operating speed and a target output speed greater than zero.";
      results.innerHTML = "";
      return;
    }

    if ((requiredTorque !== null && requiredTorque < 0) ||
        (peakTorque !== null && peakTorque < 0) ||
        (requiredTorque !== null && peakTorque !== null && peakTorque < requiredTorque)) {
      summary.textContent = "Torque values must be non-negative, and peak torque must not be lower than continuous torque.";
      results.innerHTML = "";
      return;
    }

    // Use the published machine-readable input-speed range (engineering-confirmed 2026-10-15).
    if (motorSpeed < speedBounds.min || motorSpeed > speedBounds.max) {
      var reason = motorSpeed > speedBounds.max ? "speed_above_engineering" : "speed_below_engineering";
      var speedRange = fmt(speedBounds.min, 0) + "–" + fmt(speedBounds.max, 0) + " rpm";
      summary.textContent = motorSpeed > speedBounds.max ?
        "This project exceeds the standard continuous input-speed range of " + speedRange + ". Custom feasibility review is required." :
        "This project is below the standard continuous input-speed range of " + speedRange + ". Custom feasibility review is required.";
      results.innerHTML = customReviewAction(reason, motorSpeed, outputSpeed, requiredTorque, peakTorque, maxDiameter, maxLength);
      track(0, 0, null, null, null);
      return;
    }
    var targetRatio = motorSpeed / outputSpeed;
    var ratioToleranceActive = maxRatioDiff !== null && maxRatioDiff >= 0;
    var candidates = [];
    var exclusions = [];

    gearboxes.forEach(function (gearbox) {
      if (maxDiameter !== null && maxDiameter > 0 && gearbox.diameter > maxDiameter) {
        exclusions.push({
          model: gearbox.model,
          reason: "Diameter " + fmt(gearbox.diameter, 0) + " mm exceeds the entered maximum."
        });
        return;
      }

      var lengthEligible = gearbox.stages.filter(function (stage) {
        return maxLength === null || maxLength <= 0 || stage.length <= maxLength;
      });

      if (!lengthEligible.length) {
        exclusions.push({
          model: gearbox.model,
          reason: "No published stage fits the entered maximum gearbox body length."
        });
        return;
      }

      var torqueEligible = lengthEligible.filter(function (stage) {
        return requiredTorque === null || requiredTorque <= 0 || stage.rated >= requiredTorque;
      });

      if (!torqueEligible.length) {
        exclusions.push({
          model: gearbox.model,
          reason: "No remaining stage meets the entered continuous torque using published rated allowable torque."
        });
        return;
      }

      var peakEligible = torqueEligible.filter(function (stage) {
        return peakTorque === null || stage.momentary >= peakTorque;
      });
      if (!peakEligible.length) {
        exclusions.push({model: gearbox.model, reason: "No remaining stage meets requested peak torque against published momentary limits; peak duration and frequency require review."});
        return;
      }
      var frameCandidates = [];
      peakEligible.forEach(function (stage) {
        stage.ratios.forEach(function (ratio) {
          var predictedOutput = motorSpeed / ratio;
          var errorPct = Math.abs(ratio - targetRatio) / targetRatio * 100;
          frameCandidates.push({
            model: gearbox.model,
            diameter: gearbox.diameter,
            stage: stage.stage,
            length: stage.length,
            ratio: ratio,
            rated: stage.rated,
            momentary: stage.momentary,
            efficiency: stage.efficiency,
            predictedOutput: predictedOutput,
            errorPct: errorPct
          });
        });
      });

      if (ratioToleranceActive) {
        frameCandidates = frameCandidates.filter(function (item) {
          return item.errorPct <= maxRatioDiff;
        });
      }

      if (!frameCandidates.length) {
        exclusions.push({
          model: gearbox.model,
          reason: "No published ratio remains within the entered maximum ratio difference."
        });
        return;
      }

      candidates = candidates.concat(frameCandidates);
    });

    candidates.sort(function (a, b) {
      if (a.errorPct !== b.errorPct) return a.errorPct - b.errorPct;
      if (a.diameter !== b.diameter) return a.diameter - b.diameter;
      if (a.length !== b.length) return a.length - b.length;
      return a.stage - b.stage;
    });

    summary.innerHTML =
      "<strong>Preliminary target ratio: " + fmt(targetRatio, 2) + ":1.</strong> " +
      "The tool first applies the limits you entered, then compares the remaining published configurations. " +
      (ratioToleranceActive ?
        "A maximum ratio difference of " + fmt(maxRatioDiff, 2) + "% is active. " :
        "No maximum ratio-difference filter is active. ") +
      "Continuous torque is checked against published rated limits" +
      (requiredTorque !== null ? " (" + torqueDisplay(requiredTorque) + ")" : "") + ". " +
      (peakTorque !== null ? "Peak torque uses published momentary limits (" + torqueDisplay(peakTorque) + "); duration and frequency remain unverified. " : "") +
      "No safety factor or final motor compatibility has been assumed.";

    if (!candidates.length) {
      var noResultDetails = exclusions.length ?
        "<ul>" + exclusions.map(function (item) {
          return "<li><strong>" + esc(item.model) + ":</strong> " + esc(item.reason) + "</li>";
        }).join("") + "</ul>" : "";

      results.innerHTML =
        "<p>No published standard configuration remains after the current filters. A custom ratio, load, or interface may still be feasible after engineering assessment.</p>" +
        customReviewAction("no_published_match", motorSpeed, outputSpeed, requiredTorque, peakTorque, maxDiameter, maxLength) +
        noResultDetails;
      track(0, 0, null, null, null);
      return;
    }

    var bestByModel = {};
    candidates.forEach(function (item) {
      if (!bestByModel[item.model]) bestByModel[item.model] = item;
    });

    var frameCandidates = Object.keys(bestByModel).map(function (model) {
      return bestByModel[model];
    });

    var closest = candidates[0];

    var smallest = frameCandidates.slice().sort(function (a, b) {
      if (a.diameter !== b.diameter) return a.diameter - b.diameter;
      if (a.errorPct !== b.errorPct) return a.errorPct - b.errorPct;
      return a.length - b.length;
    })[0];

    var shortest = frameCandidates.slice().sort(function (a, b) {
      if (a.length !== b.length) return a.length - b.length;
      if (a.errorPct !== b.errorPct) return a.errorPct - b.errorPct;
      return a.diameter - b.diameter;
    })[0];

    var closestKey = itemKey(closest);
    var smallestKey = itemKey(smallest);
    var shortestKey = itemKey(shortest);

    frameCandidates.sort(function (a, b) {
      if (a.diameter !== b.diameter) return a.diameter - b.diameter;
      if (a.errorPct !== b.errorPct) return a.errorPct - b.errorPct;
      return a.length - b.length;
    });

    var cards =
      "<div class=\"siggear-candidate-cards\">" +
      benchmarkCard("Closest Ratio", closest,
        fmt(closest.errorPct, 2) + "% ratio difference · estimated " + fmt(closest.predictedOutput, 2) + " rpm") +
      benchmarkCard("Smallest Surviving Frame", smallest,
        fmt(smallest.diameter, 0) + " mm diameter · " + fmt(smallest.errorPct, 2) + "% ratio difference") +
      benchmarkCard("Shortest Surviving Gearbox", shortest,
        fmt(shortest.length, 2) + " mm gearbox body · " + fmt(shortest.errorPct, 2) + "% ratio difference") +
      "</div>";

    var frameRows = frameCandidates.map(function (item) {
      var signals = [];
      var key = itemKey(item);
      if (key === closestKey) signals.push("Closest ratio");
      if (key === smallestKey) signals.push("Smallest frame");
      if (key === shortestKey) signals.push("Shortest gearbox");

      var slug = item.model.toLowerCase();
      return "<tr>" +
        "<td>" + candidateLink(item, item.model) + "</td>" +
        "<td>" + fmt(item.diameter, 0) + " mm</td>" +
        "<td>" + item.stage + "</td>" +
        "<td>" + fmt(item.ratio, 2) + ":1</td>" +
        "<td>" + fmt(item.errorPct, 2) + "%</td>" +
        "<td>" + fmt(item.length, 2) + " mm</td>" +
        "<td>" + torqueDisplay(item.rated) + "</td>" +
        "<td>" + fmt(item.efficiency, 0) + "%</td>" +
        "<td>" + (signals.length ? esc(signals.join(" · ")) : "Candidate") + "</td>" +
        "<td><a href=\"../../engineering-resources/" + slug + "/datasheet/\">Datasheet</a><br>" +
        "<a href=\"../../engineering-resources/" + slug + "/mechanical-interface/\">Interface</a><br>" +
        "<a href=\"../../engineering-resources/planetary-gearboxes/candidate-design-in-pack/?model=" +
        encodeURIComponent(item.model) + "&stage=" + encodeURIComponent(item.stage) +
        "&ratio=" + encodeURIComponent(item.ratio) + "\">Design-In pack</a><br>" +
        "<a href=\"../../request-cad-sample-quote/?model=" +
        encodeURIComponent(item.model) +
        selectionParams(item, motorSpeed, outputSpeed, requiredTorque, peakTorque, maxDiameter, maxLength) + "\">Project brief</a></td>" +
        "</tr>";
    }).join("");

    var excludedHtml = "";
    if (exclusions.length) {
      excludedHtml =
        "<h3>Excluded by Current Filters</h3>" +
        "<div class=\"siggear-selector-table-wrap\"><table class=\"siggear-exclusion-table\">" +
        "<thead><tr><th>Model</th><th>Reason</th></tr></thead><tbody>" +
        exclusions.map(function (item) {
          return "<tr><td>" + esc(item.model) + "</td><td>" + esc(item.reason) + "</td></tr>";
        }).join("") +
        "</tbody></table></div>";
    }

    var visible = candidates.slice(0, 12);
    var configurationRows = visible.map(function (item) {
      var slug = item.model.toLowerCase();
      return "<tr>" +
        "<td>" + candidateLink(item, item.model) + "</td>" +
        "<td>" + fmt(item.diameter, 0) + " mm</td>" +
        "<td>" + item.stage + "</td>" +
        "<td>" + fmt(item.ratio, 2) + ":1</td>" +
        "<td>" + fmt(item.predictedOutput, 2) + " rpm</td>" +
        "<td>" + fmt(item.errorPct, 2) + "%</td>" +
        "<td>" + fmt(item.length, 2) + " mm</td>" +
        "<td>" + torqueDisplay(item.rated) + "</td>" +
        "<td>" + fmt(item.efficiency, 0) + "%</td>" +
        "<td><a href=\"../../engineering-resources/" + slug + "/datasheet/\">Datasheet</a><br>" +
        "<a href=\"../../engineering-resources/planetary-gearboxes/candidate-design-in-pack/?model=" +
        encodeURIComponent(item.model) + "&stage=" + encodeURIComponent(item.stage) +
        "&ratio=" + encodeURIComponent(item.ratio) + "\">Design-In pack</a><br>" +
        "<a href=\"../../request-cad-sample-quote/?model=" +
        encodeURIComponent(item.model) +
        selectionParams(item, motorSpeed, outputSpeed, requiredTorque, peakTorque, maxDiameter, maxLength) + "\">Project brief</a></td>" +
        "</tr>";
    }).join("");

    results.innerHTML =
      "<h3>Candidate Frame Comparison</h3>" +
      "<p>Each frame appears once using its closest published ratio after the active filters. These labels are comparison signals, not final recommendations.</p>" +
      cards +
      "<div class=\"siggear-selector-table-wrap\"><table>" +
      "<thead><tr>" +
      "<th>Model</th><th>Diameter</th><th>Best stage</th><th>Closest ratio</th>" +
      "<th>Ratio difference</th><th>Gearbox length</th><th>Rated torque</th>" +
      "<th>Published stage efficiency</th><th>First-check signal</th><th>Next</th>" +
      "</tr></thead><tbody>" + frameRows + "</tbody></table></div>" +
      excludedHtml +
      "<h3>Closest Published Configurations</h3>" +
      "<div class=\"siggear-selector-table-wrap\"><table>" +
      "<thead><tr>" +
      "<th>Model</th><th>Diameter</th><th>Stage</th><th>Published ratio</th>" +
      "<th>Estimated output</th><th>Ratio difference</th><th>Gearbox length</th>" +
      "<th>Rated torque</th><th>Published stage efficiency</th><th>Next</th>" +
      "</tr></thead><tbody>" + configurationRows + "</tbody></table></div>" +
      "<p class=\"siggear-selector-note\">The continuous-torque filter uses published rated allowable torque only. " +
      "Maximum momentary torque is never used as a continuous rating. Smallest frame, shortest gearbox and closest ratio answer different questions; none proves final suitability. " +
      "Published stage efficiency is a reference value; ratio-dependent efficiency has not been separately verified. " +
      "Final selection still requires duty cycle, peak load, motor operating point, shaft loads, mechanical interface and configuration review.</p>" +
      customReviewAction("custom_configuration", motorSpeed, outputSpeed, requiredTorque, peakTorque, maxDiameter, maxLength);

    track(candidates.length, frameCandidates.length, closest, smallest, shortest);
  });
})();