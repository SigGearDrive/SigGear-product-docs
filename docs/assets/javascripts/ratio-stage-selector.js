(function () {
  var form = document.getElementById("siggear-ratio-stage-selector");
  if (!form) return;

  var results = document.getElementById("sg-ratio-stage-results");
  var summary = document.getElementById("sg-ratio-stage-summary");

  var dataPromise = fetch(new URL("../../assets/data/planetary-ratio-stage-data.json", window.location.href))
    .then(function (response) {
      if (!response.ok) throw new Error("Unable to load published ratio-stage data.");
      return response.json();
    })
    .then(function (payload) {
      if (!payload || !Array.isArray(payload.models)) {
        throw new Error("Published ratio-stage data is invalid.");
      }
      return payload.models;
    });

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
  function selectionParams(item, motorSpeed, outputSpeed, continuous, peak) {
    var params = "&selection=ratio_stage_selector&candidate_stage=" +
      encodeURIComponent(item.stage) + "&candidate_ratio=" + encodeURIComponent(item.ratio);
    if (motorSpeed !== null) params += "&selector_motor_speed=" + encodeURIComponent(motorSpeed);
    if (outputSpeed !== null) params += "&selector_output_speed=" + encodeURIComponent(outputSpeed);
    if (continuous !== null) params += "&selector_continuous_nm=" + encodeURIComponent((continuous * KGF_CM_TO_NM).toFixed(5));
    if (peak !== null) params += "&selector_peak_nm=" + encodeURIComponent((peak * KGF_CM_TO_NM).toFixed(5));
    return params;
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

    if (motorSpeed > 8000) {
      summary.textContent = "Input speed exceeds the published 8,000 rpm continuous permissible speed for these standard gearboxes. Request engineering review.";
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
        "<p>No published configuration remains after the current filters. Relax a filter or send the mechanism / motor drawing for an engineering review.</p>" +
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
        selectionParams(item, motorSpeed, outputSpeed, requiredTorque, peakTorque) + "\">Project brief</a></td>" +
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
        selectionParams(item, motorSpeed, outputSpeed, requiredTorque, peakTorque) + "\">Project brief</a></td>" +
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
      "<th>Efficiency</th><th>First-check signal</th><th>Next</th>" +
      "</tr></thead><tbody>" + frameRows + "</tbody></table></div>" +
      excludedHtml +
      "<h3>Closest Published Configurations</h3>" +
      "<div class=\"siggear-selector-table-wrap\"><table>" +
      "<thead><tr>" +
      "<th>Model</th><th>Diameter</th><th>Stage</th><th>Published ratio</th>" +
      "<th>Estimated output</th><th>Ratio difference</th><th>Gearbox length</th>" +
      "<th>Rated torque</th><th>Efficiency</th><th>Next</th>" +
      "</tr></thead><tbody>" + configurationRows + "</tbody></table></div>" +
      "<p class=\"siggear-selector-note\">The continuous-torque filter uses published rated allowable torque only. " +
      "Maximum momentary torque is never used as a continuous rating. Smallest frame, shortest gearbox and closest ratio answer different questions; none proves final suitability. " +
      "Final selection still requires duty cycle, peak load, motor operating point, shaft loads, mechanical interface and configuration review.</p>";

    track(candidates.length, frameCandidates.length, closest, smallest, shortest);
  });
})();