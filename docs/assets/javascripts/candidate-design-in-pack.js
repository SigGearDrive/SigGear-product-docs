(function () {
  var container = document.getElementById("sg-candidate-pack");
  if (!container) return;

  var status = document.getElementById("sg-candidate-pack-status");
  var content = document.getElementById("sg-candidate-pack-content");
  var name = document.getElementById("sg-pack-candidate-name");
  var detail = document.getElementById("sg-pack-candidate-detail");
  var row = document.getElementById("sg-pack-candidate-row");
  var boundary = document.getElementById("sg-pack-cad-boundary");
  var datasheet = document.getElementById("sg-pack-datasheet");
  var interfaceLink = document.getElementById("sg-pack-interface");
  var publicStep = document.getElementById("sg-pack-public-step");
  var brief = document.getElementById("sg-pack-project-brief");

  var validModels = ["8P","10P","12P","14P","16P","20P","22P","24P","28P","32P","36P","42P"];

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

  function fail(message) {
    status.textContent = message;
    content.hidden = true;
  }

  function track(model, stage) {
    if (typeof window.gtag !== "function") return;
    window.gtag("event", "candidate_design_in_pack_view", {
      page_path: window.location.pathname,
      inquiry_model: model,
      selector_candidate_stage: String(stage)
    });
  }

  async function init() {
    var params = new URLSearchParams(window.location.search);
    var model = (params.get("model") || "").toUpperCase();
    var stage = Number(params.get("stage"));
    var ratio = Number(params.get("ratio"));

    if (validModels.indexOf(model) === -1 ||
        !Number.isInteger(stage) || stage < 1 || stage > 4 ||
        !Number.isFinite(ratio) || ratio <= 0) {
      fail("Open this page from a validated Selection Tool result, or return to the Ratio & Stage Selection Guide.");
      return;
    }

    try {
      var response = await fetch(new URL("../../../assets/data/planetary-ratio-stage-data.json", window.location.href));
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
        fail("This model / stage / ratio combination does not match the current published SigGear ratio-stage data. Run the Selection Tool again before using the candidate pack.");
        return;
      }

      var slug = model.toLowerCase();
      var ratioText = fmt(matchedRatio, 4);
      var candidateLabel = model + " / " + stage + "-stage / " + ratioText + ":1";

      status.hidden = true;
      content.hidden = false;
      name.textContent = candidateLabel;
      detail.textContent = modelData.diameter + " mm frame · published gearbox body length " +
        fmt(stageData.length, 2) + " mm";

      row.innerHTML =
        "<tr>" +
        "<td>" + esc(model) + "</td>" +
        "<td>" + fmt(modelData.diameter, 0) + " mm</td>" +
        "<td>" + stage + "</td>" +
        "<td>" + ratioText + ":1</td>" +
        "<td>" + fmt(stageData.length, 2) + " mm</td>" +
        "<td>" + fmt(stageData.rated, 2) + " kgf·cm</td>" +
        "<td>" + fmt(stageData.momentary, 2) + " kgf·cm</td>" +
        "<td>" + fmt(stageData.efficiency, 0) + "%</td>" +
        "</tr>";

      if (stage === 4) {
        boundary.innerHTML =
          "<strong>Selected candidate: 4-stage.</strong> " +
          "The released public STEP uses the same published stage count and can be used for preliminary external packaging and interface review. " +
          "It is still a simplified public reference and is not ratio-specific production CAD. Request the controlled configuration CAD / drawing before design freeze.";
      } else {
        boundary.innerHTML =
          "<strong>Selected candidate: " + stage + "-stage.</strong> " +
          "The released public STEP is a 4-stage reference, so its gearbox body length does not match this selected stage. " +
          "Do not use the public STEP as the exact axial envelope for this candidate. Use the published " +
          fmt(stageData.length, 2) + " mm gearbox body length for preliminary sizing and request stage-matched controlled CAD / drawing before final placement.";
      }

      datasheet.href = "../../" + slug + "/datasheet/";
      interfaceLink.href = "../../" + slug + "/mechanical-interface/";
      publicStep.href = "../../../assets/downloads/" + slug + "/" + model +
        "_Public_Simplified_STEP_v1.0_4-Stage.step";
      brief.href = "../../../request-cad-sample-quote/?model=" + encodeURIComponent(model) +
        "&selection=ratio_stage_selector&candidate_stage=" + encodeURIComponent(stage) +
        "&candidate_ratio=" + encodeURIComponent(matchedRatio);

      track(model, stage);
    } catch (error) {
      fail("The current published candidate data could not be loaded. Use the Datasheet / Mechanical Interface directly or send the project for engineering review.");
    }
  }

  init();
})();