(function () {
  // Legacy links may contain model or application context from a product
  // page. Use it to prefill only the subject of a direct email; no form, POST
  // or customer data collection is performed.
  var links = document.querySelectorAll("[data-siggear-contact-link]");
  if (!links.length) return;
  var validModels = /^(8P|10P|12P|14P|16P|20P|22P|24P|28P|32P|36P|42P|SG-6010C|SG-6010D|SG-6010HB|SG-8021|SG-2877|SG-2878|CPM-78-39|CPM-80-25|CPM-100-25)$/;
  var startingPoints = {
    existing_motor: "Existing Motor",
    drawing_cad: "Drawing / STEP",
    failing_gearbox: "Gearbox Replacement",
    prototype_to_volume: "Prototype to Production",
    standard_product: "Product Inquiry"
  };
  var projectTypes = {
    gearbox_only: "Gearhead Only",
    motor_gearbox: "Motor + Gearhead",
    joint_actuator: "Joint Actuator",
    hub_gear_motor: "Hub Gear Motor"
  };
  var params;
  try { params = new URLSearchParams(window.location.search); }
  catch (error) { return; }
  var requestedModel = (params.get("model") || "").trim().toUpperCase();
  var model = validModels.test(requestedModel) ? requestedModel : "";
  var start = (params.get("start") || "").trim().toLowerCase().replace(/-/g, "_");
  var path = (params.get("path") || "").trim().toLowerCase().replace(/-/g, "_");
  var subject = "SigGear Engineering Inquiry";
  if (model) subject += " - " + model;
  if (Object.prototype.hasOwnProperty.call(startingPoints, start)) {
    subject += " - " + startingPoints[start];
  } else if (Object.prototype.hasOwnProperty.call(projectTypes, path)) {
    subject += " - " + projectTypes[path];
  }
  var href = "mailto:luffy@siggear.com?subject=" + encodeURIComponent(subject);
  links.forEach(function (link) { link.setAttribute("href", href); });
})();
