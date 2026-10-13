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

  function track(resultCount, top) {
    if (typeof window.gtag !== "function") return;
    window.gtag("event", "ratio_stage_selector_run", {
      page_path: window.location.pathname,
      used_diameter_filter: numberValue("sg-selector-diameter") !== null ? 1 : 0,
      used_length_filter: numberValue("sg-selector-length") !== null ? 1 : 0,
      used_torque_filter: numberValue("sg-selector-torque") !== null ? 1 : 0,
      result_count: resultCount,
      top_candidate_model: top ? top.model : "none",
      top_candidate_stage: top ? String(top.stage) : "none"
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
    var requiredTorque = numberValue("sg-selector-torque");

    if (!motorSpeed || motorSpeed <= 0 || !outputSpeed || outputSpeed <= 0) {
      summary.textContent = "Enter a motor operating speed and a target output speed greater than zero.";
      results.innerHTML = "";
      return;
    }

    var targetRatio = motorSpeed / outputSpeed;
    var candidates = [];

    gearboxes.forEach(function (gearbox) {
      if (maxDiameter !== null && maxDiameter > 0 && gearbox.diameter > maxDiameter) return;

      gearbox.stages.forEach(function (stage) {
        if (maxLength !== null && maxLength > 0 && stage.length > maxLength) return;
        if (requiredTorque !== null && requiredTorque > 0 && stage.rated < requiredTorque) return;

        stage.ratios.forEach(function (ratio) {
          var predictedOutput = motorSpeed / ratio;
          var errorPct = Math.abs(ratio - targetRatio) / targetRatio * 100;
          candidates.push({
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
    });

    candidates.sort(function (a, b) {
      if (a.errorPct !== b.errorPct) return a.errorPct - b.errorPct;
      if (a.diameter !== b.diameter) return a.diameter - b.diameter;
      return a.stage - b.stage;
    });

    var visible = candidates.slice(0, 12);

    summary.innerHTML =
      "<strong>Preliminary target ratio: " + fmt(targetRatio, 2) + ":1.</strong> " +
      "Results are sorted by the closest published ratio after the filters you entered. " +
      "No ratio tolerance, safety factor or final motor compatibility has been assumed.";

    if (!visible.length) {
      results.innerHTML =
        "<p>No published configuration remains after the current diameter, gearbox-length and rated-torque filters. " +
        "Relax a filter or send the mechanism / motor drawing for an engineering review.</p>";
      track(0, null);
      return;
    }

    var rows = visible.map(function (item) {
      var slug = item.model.toLowerCase();
      return "<tr>" +
        "<td><a href=\"../products/planetary-gearboxes/" + slug + "-planetary-gearbox/\">" + esc(item.model) + "</a></td>" +
        "<td>" + fmt(item.diameter, 0) + " mm</td>" +
        "<td>" + item.stage + "</td>" +
        "<td>" + fmt(item.ratio, 2) + ":1</td>" +
        "<td>" + fmt(item.predictedOutput, 2) + " rpm</td>" +
        "<td>" + fmt(item.errorPct, 2) + "%</td>" +
        "<td>" + fmt(item.length, 2) + " mm</td>" +
        "<td>" + fmt(item.rated, 2) + " kgf·cm</td>" +
        "<td>" + fmt(item.efficiency, 0) + "%</td>" +
        "<td><a href=\"../engineering-resources/" + slug + "/datasheet/\">Datasheet</a><br>" +
        "<a href=\"../request-cad-sample-quote/?model=" + encodeURIComponent(item.model) + "\">Project brief</a></td>" +
        "</tr>";
    }).join("");

    results.innerHTML =
      "<div class=\"siggear-selector-table-wrap\"><table>" +
      "<thead><tr>" +
      "<th>Model</th><th>Diameter</th><th>Stage</th><th>Published ratio</th>" +
      "<th>Estimated output</th><th>Ratio difference</th><th>Gearbox length</th>" +
      "<th>Rated torque</th><th>Efficiency</th><th>Next</th>" +
      "</tr></thead><tbody>" + rows + "</tbody></table></div>" +
      "<p class=\"siggear-selector-note\">Rated-torque filtering uses the published rated allowable torque for the stage only. " +
      "Maximum momentary torque is not used as a continuous rating. Final selection still requires duty cycle, motor operating point, shaft loads, mechanical interface and configuration review.</p>";

    track(visible.length, visible[0]);
  });
})();