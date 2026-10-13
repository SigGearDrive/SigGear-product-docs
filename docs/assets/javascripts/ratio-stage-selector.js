(function () {
  var form = document.getElementById("siggear-ratio-stage-selector");
  if (!form) return;

  var results = document.getElementById("sg-ratio-stage-results");
  var summary = document.getElementById("sg-ratio-stage-summary");

  var gearboxes = [
    { model:"8P", diameter:8, stages:[
      {stage:1,length:10.15,ratios:[3.8,4.5,5.2],rated:0.2,momentary:0.4,efficiency:90},
      {stage:2,length:12.80,ratios:[14.4,17.1,19.8,20.3,23.4,27],rated:0.25,momentary:0.5,efficiency:80},
      {stage:3,length:15.45,ratios:[54.9,65,75.1,76.95,88.9,91.1,102.75,105.3,121.7,140.6],rated:0.3,momentary:0.6,efficiency:73},
      {stage:4,length:18.10,ratios:[208.5,246.9,285.3,292.4,337.9,346.3,390.46,400.14,410.1,462.4,473.85,534.3,547.56,632.74,731.16],rated:0.4,momentary:0.8,efficiency:66}
    ]},
    { model:"10P", diameter:10, stages:[
      {stage:1,length:10.25,ratios:[3.5,4,4.75],rated:1.3,momentary:2.6,efficiency:90},
      {stage:2,length:13.00,ratios:[12.25,14,16,16.6,19,22.6],rated:1.5,momentary:3.0,efficiency:80},
      {stage:3,length:15.75,ratios:[42.9,49,56,58.2,64,66.5,76,79,90.25,107.2],rated:1.8,momentary:3.6,efficiency:73},
      {stage:4,length:18.50,ratios:[150.1,171.5,196,203.7,224,232.7,256,266,276.4,304,315.9,361,375.1,428.7],rated:2.0,momentary:4.0,efficiency:66}
    ]},
    { model:"12P", diameter:12, stages:[
      {stage:1,length:11.35,ratios:[3.5,4,4.75],rated:2.0,momentary:4.0,efficiency:90},
      {stage:2,length:14.10,ratios:[12.25,14,16,16.6,19,22.6],rated:3.0,momentary:6.0,efficiency:80},
      {stage:3,length:16.85,ratios:[42.9,49,56,58.2,64,66.5,76,79,90.25,107.2],rated:3.6,momentary:7.2,efficiency:73},
      {stage:4,length:19.60,ratios:[150.1,171.5,196,203.7,224,232.7,256,266,276.4,304,315.9,361,375.1,428.7,509.1],rated:4.2,momentary:8.4,efficiency:66}
    ]},
    { model:"14P", diameter:14, stages:[
      {stage:1,length:15.2,ratios:[3.75,4.38,4.66],rated:3.5,momentary:7.0,efficiency:90},
      {stage:2,length:19.0,ratios:[14,16.4,17.5,19.2,20.4,21.7],rated:4.0,momentary:8.0,efficiency:80},
      {stage:3,length:22.8,ratios:[52.7,61.6,65.5,71.9,76.5,81.4,84,89.4,95.1,101.2],rated:5.0,momentary:10.0,efficiency:73},
      {stage:4,length:26.6,ratios:[197.75,231,245.74,269.8,287,305.4,315.1,335.25,356.7,368,379.5,391.6,416.6,443.3],rated:6.0,momentary:12.0,efficiency:66}
    ]},
    { model:"16P", diameter:16, stages:[
      {stage:1,length:17.55,ratios:[3.85,4.33,4.63],rated:4.0,momentary:8.0,efficiency:90},
      {stage:2,length:21.85,ratios:[14.8,16.7,17.8,18.7,20,21.4],rated:5.0,momentary:10.0,efficiency:80},
      {stage:3,length:26.15,ratios:[57.1,64.2,68.6,72.2,77.2,81.2,82.5,86.8,92.8,99.25],rated:7.0,momentary:20.0,efficiency:73},
      {stage:4,length:30.45,ratios:[219.7,247,264.2,277.9,297.2,312.55,317.75,334.2,351.5,357.4,375.9,382.1,401.9,429.8,459.5],rated:9.0,momentary:26.0,efficiency:66}
    ]},
    { model:"20P", diameter:20, stages:[
      {stage:1,length:20.1,ratios:[4,4.75,6],rated:6.0,momentary:12.0,efficiency:90},
      {stage:2,length:24.9,ratios:[16,19,22.6,24,28.5,36],rated:7.0,momentary:14.0,efficiency:80},
      {stage:3,length:29.7,ratios:[64,76,90.2,96,107.2,114,135.4,144,171,216],rated:10.0,momentary:20.0,efficiency:73},
      {stage:4,length:34.5,ratios:[256,304,361,384,428.7,456,509.1,541.5,576,643,684,812.2,864,1026,1296],rated:13.0,momentary:26.0,efficiency:66}
    ]},
    { model:"22P", diameter:22, stages:[
      {stage:1,length:22.6,ratios:[3.5,4,4.75],rated:8.0,momentary:16.0,efficiency:90},
      {stage:2,length:27.9,ratios:[12.25,14,16,16.6,19,22.6],rated:10.0,momentary:20.0,efficiency:80},
      {stage:3,length:33.2,ratios:[42.9,49,56,58.2,64,66.5,76,79,90.25,107.2],rated:15.0,momentary:30.0,efficiency:73},
      {stage:4,length:38.5,ratios:[150.1,171.5,196,203.7,224,232.7,256,266,276.4,304,315.9,361,375.1,428.7,509.1],rated:25.0,momentary:50.0,efficiency:66}
    ]},
    { model:"24P", diameter:24, stages:[
      {stage:1,length:24.6,ratios:[3.83,4.4,5.25],rated:10.0,momentary:20.0,efficiency:90},
      {stage:2,length:30.4,ratios:[14.7,16.8,19.4,20.1,23,27.7],rated:15.0,momentary:30.0,efficiency:80},
      {stage:3,length:36.2,ratios:[56.2,64.5,74.1,77,85.2,88.5,101.6,105.6,121.3,144.7],rated:20.0,momentary:40.0,efficiency:73},
      {stage:4,length:42.0,ratios:[215.2,247.2,284,294.9,326.2,338.6,374.8,389.3,404.3,447.2,464.5,533.6,554.2,636.7,759.7],rated:30.0,momentary:60.0,efficiency:66}
    ]},
    { model:"28P", diameter:28, stages:[
      {stage:1,length:25.6,ratios:[3.83,4.4,5.25],rated:20.0,momentary:40.0,efficiency:90},
      {stage:2,length:31.9,ratios:[14.7,16.8,19.4,20.1,23,27.7],rated:25.0,momentary:50.0,efficiency:80},
      {stage:3,length:38.2,ratios:[56.2,64.5,74.1,77,85.2,88.5,101.6,105.6,121.3,144.7],rated:35.0,momentary:70.0,efficiency:73},
      {stage:4,length:44.5,ratios:[215.2,247.2,284,294.9,326.2,338.8,374.8,389.3,404.3,447.2,464.5,533.6,554.2,636.7,759.7],rated:50.0,momentary:100.0,efficiency:66}
    ]},
    { model:"32P", diameter:32, stages:[
      {stage:1,length:28.05,ratios:[3.5,4,4.75],rated:35.0,momentary:70.0,efficiency:90},
      {stage:2,length:36.35,ratios:[12.2,14,16,16.6,19,22.6],rated:50.0,momentary:100.0,efficiency:80},
      {stage:3,length:44.65,ratios:[42.9,49,56,58.2,64,66.5,76,79,90.2,107.2],rated:65.0,momentary:130.0,efficiency:73},
      {stage:4,length:52.95,ratios:[150.1,171.5,196,203.7,224,232.7,256,266,276.4,304,315.9,361,375.1,428.7,509.1],rated:80.0,momentary:160.0,efficiency:66}
    ]},
    { model:"36P", diameter:36, stages:[
      {stage:1,length:30.6,ratios:[3.66,4.2,5.0],rated:40.0,momentary:80.0,efficiency:90},
      {stage:2,length:40.9,ratios:[13.4,15.4,17.6,18.3,21,25],rated:60.0,momentary:120.0,efficiency:80},
      {stage:3,length:51.2,ratios:[49,56.3,64.6,67,74.1,76.9,88.2,91.5,105,125],rated:80.0,momentary:160.0,efficiency:73},
      {stage:4,length:61.5,ratios:[179.4,205.9,236.3,245.1,271.2,281.3,311.2,322.8,334.9,370.5,384.3,441,457.5,525,625],rated:100.0,momentary:200.0,efficiency:66}
    ]},
    { model:"42P", diameter:42, stages:[
      {stage:1,length:35.6,ratios:[3.8,4.3,5.1],rated:80.0,momentary:160.0,efficiency:90},
      {stage:2,length:46.9,ratios:[14.4,16.3,18.6,19.2,21.8,25.7],rated:100.0,momentary:200.0,efficiency:80},
      {stage:3,length:58.2,ratios:[54.4,61.9,70.4,72.8,80.1,82.8,94.2,97.4,110.8,130.3],rated:120.0,momentary:240.0,efficiency:73},
      {stage:4,length:69.5,ratios:[206.4,234.6,266.8,276,303.5,313.9,345,357,369.2,406,419.9,477.5,493.93,561.70,660.7],rated:150.0,momentary:300.0,efficiency:66}
    ]}
  ];

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

  form.addEventListener("submit", function (event) {
    event.preventDefault();

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