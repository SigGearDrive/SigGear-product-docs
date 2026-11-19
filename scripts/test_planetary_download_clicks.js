#!/usr/bin/env node
"use strict";

// Test consent-gated click labels without sending analytics over the network.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const source = fs.readFileSync("docs/assets/javascripts/analytics-events.js", "utf8");
const events = [];
const handlers = {};
const base = "https://siggeardrive.github.io/SigGear-product-docs/selection-guides/planetary-gearhead-quick-selector/";
const window = {
  dataLayer: [],
  location: {
    href: base,
    hostname: "siggeardrive.github.io",
    pathname: "/SigGear-product-docs/selection-guides/planetary-gearhead-quick-selector/",
    search: ""
  },
  sessionStorage: {getItem: () => null, setItem: () => {}, removeItem: () => {}},
  gtag: (type, name, params) => events.push({type, name, params})
};
const document = {
  readyState: "loading",
  referrer: "",
  addEventListener: (type, cb) => { handlers[type] = cb; }
};
vm.runInNewContext(source, {window, document, URL, URLSearchParams}, {filename:"analytics-events.js"});
assert.equal(typeof handlers.click, "function");

function click(href) {
  events.length = 0;
  const link = {getAttribute: key => key === "href" ? href : null, textContent: "Download"};
  handlers.click({target: {closest: name => name === "a" ? link : null}});
  return events.slice();
}
function assertResource(href, type, model, expectCad) {
  const records = click(href);
  const files = records.filter(x => x.name === "planetary_engineering_file_click");
  assert.equal(files.length, 1, href);
  assert.equal(files[0].params.file_type, type);
  assert.equal(files[0].params.gearhead_model, model);
  assert.equal(records.filter(x => x.name === "cad_download_click").length, expectCad ? 1 : 0);
}

assertResource("../../assets/downloads/12p/12P_Planetary_Gearhead_Datasheet_Rev1.1.pdf", "datasheet_pdf", "12P", false);
assertResource("../../assets/downloads/22p/22P_2D_Drawing.pdf", "outline_2d_pdf", "22P", false);
assertResource("../../assets/downloads/32p/32P_Full_Assembly.step", "full_assembly_step", "32P", true);
assertResource("../../assets/downloads/8p/8P_Public_Simplified_STEP_v1.0_4-Stage.step", "simplified_4_stage_step", "8P", true);
assert.equal(click("../../assets/downloads/22p/not-a-released-file.pdf").filter(x=>x.name==="planetary_engineering_file_click").length, 0);
assert.equal(click("https://example.com/downloads/22p/22P_2D_Drawing.pdf").filter(x=>x.name==="planetary_engineering_file_click").length, 0);
// Application -> model -> file attribution is path-only and does not infer a sale.
function setPage(path, referrer) {
  window.location.pathname = path;
  window.location.href = "https://siggeardrive.github.io" + path;
  document.referrer = referrer || "";
}
const appPath = "/SigGear-product-docs/applications/electric-pruning-shears-planetary-gearbox/";
const modelPath = "/SigGear-product-docs/products/planetary-gearboxes/20p-planetary-gearbox/";
setPage(appPath, "");
let observed = click("../../assets/downloads/20p/20P_Planetary_Gearhead_Datasheet_Rev1.0.pdf");
let direct = observed.find(x => x.name === "planetary_engineering_file_click");
assert.equal(direct.params.source_page_type, "application");
assert.equal(direct.params.source_application, "electric-pruning-shears-planetary-gearbox");
assert.equal(direct.params.gearhead_model, "20P");
assert.equal(observed.filter(x => x.name === "application_product_click").length, 0);

observed = click("../../products/planetary-gearboxes/20p-planetary-gearbox/");
assert.equal(observed.filter(x => x.name === "application_product_click").length, 1);
assert.equal(observed.find(x => x.name === "application_product_click").params.gearhead_model, "20P");
assert.equal(observed.find(x => x.name === "application_product_click").params.source_application, "electric-pruning-shears-planetary-gearbox");

observed = click("../../engineering-resources/motors/");
assert.equal(observed.filter(x => x.name === "application_resource_click").length, 1);
assert.equal(observed.find(x => x.name === "application_resource_click").params.resource_type, "motor_datasheets");

observed = click("../../custom-engineering/motor-gearbox-integration/");
assert.equal(observed.find(x => x.name === "application_resource_click").params.resource_type, "motor_gearhead_assembly");

setPage(modelPath, "https://siggeardrive.github.io" + appPath);
observed = click("../../../assets/downloads/20p/20P_Full_Assembly.step");
direct = observed.find(x => x.name === "planetary_engineering_file_click");
assert.equal(direct.params.source_page_type, "product_model");
assert.equal(direct.params.source_application, "electric-pruning-shears-planetary-gearbox");
assert.equal(observed.find(x => x.name === "cad_download_click").params.source_application, "electric-pruning-shears-planetary-gearbox");

setPage(modelPath, "https://www.google.com/search?q=20mm+planetary+gearhead");
observed = click("../../../assets/downloads/20p/20P_2D_Drawing.pdf");
direct = observed.find(x => x.name === "planetary_engineering_file_click");
assert.equal(direct.params.source_page_type, "product_model");
assert.equal(direct.params.source_application, "not_specified");

setPage("/SigGear-product-docs/engineering-resources/planetary-gearboxes/public-cad-release-v1/", "");
observed = click("../../../assets/downloads/12p/12P_Planetary_Gearhead_Datasheet_Rev1.1.pdf");
assert.equal(observed.find(x => x.name === "planetary_engineering_file_click").params.source_page_type, "gearhead_download_hub");

// Motor-only PDFs are a separate download-intent event, not gearhead files.
setPage("/SigGear-product-docs/engineering-resources/motors/", "");
observed = click("../../assets/downloads/motors/20mm/SigGear_20mm_BLDC_Motor_HR-BL2030-Q120260_Rev1.0.pdf");
let motorEvent = observed.find(x => x.name === "motor_datasheet_click");
assert.ok(motorEvent);
assert.equal(motorEvent.params.motor_diameter_mm, 20);
assert.equal(motorEvent.params.source_page_type, "motor_datasheet_hub");
assert.equal(motorEvent.params.source_application, "not_specified");
assert.equal(observed.filter(x => x.name === "planetary_engineering_file_click").length, 0);

setPage(appPath, "");
observed = click("../../assets/downloads/motors/8mm/SigGear_8mm_HS-816-Q_Winding_Set_A_D1.pdf");
motorEvent = observed.find(x => x.name === "motor_datasheet_click");
assert.equal(motorEvent.params.source_page_type, "application");
assert.equal(motorEvent.params.source_application, "electric-pruning-shears-planetary-gearbox");
assert.equal(motorEvent.params.motor_diameter_mm, 8);

observed = click("https://example.com/SigGear-product-docs/assets/downloads/motors/8mm/SigGear_test.pdf");
assert.equal(observed.filter(x => x.name === "motor_datasheet_click").length, 0);

// GEO click-origin regression: the source is the current engineering page,
// not the referrer that originally led the visitor to that engineering page.
for (const [pageSlug, expectedOrigin] of [
  ["custom-engineering/custom-planetary-gearbox", "geo_existing_motor"],
  ["custom-engineering/custom-gearbox-from-drawing-cad", "geo_drawing_step_sample"],
  ["custom-engineering/replacement-planetary-gearhead", "geo_replacement_redesign"],
  ["custom-engineering/gearbox-failure-analysis-durability-redesign", "geo_failure_durability"],
  ["custom-engineering/prototype-to-production", "geo_prototype_to_volume"],
  ["selection-guides/custom-gearbox-manufacturer-supplier-qualification", "geo_supplier_qualification"]
]) {
  setPage("/SigGear-product-docs/" + pageSlug + "/",
    "https://www.google.com/search?q=prior+referrer+not+origin");
  const opening = click("../../request-cad-sample-quote/?start=existing_motor");
  const opens = opening.filter(e => e.name === "engineering_brief_open_click");
  assert.equal(opens.length, 1, pageSlug);
  assert.equal(opens[0].params.inquiry_origin, expectedOrigin, pageSlug);
  assert.equal(opens[0].params.destination_path,
    "/SigGear-product-docs/request-cad-sample-quote/");
  assert.ok(!Object.values(opens[0].params).some(v =>
    typeof v === "string" && v.includes("prior+referrer")));
}
setPage("/SigGear-product-docs/engineering-center/", "");
const unspecifiedOrigin = click("../request-cad-sample-quote/");
assert.equal(unspecifiedOrigin.find(e => e.name === "engineering_brief_open_click")
  .params.inquiry_origin, "direct_or_external");
// Changing a project path while already on the inquiry form is not a new
// engineering-brief entry; only the actual page transition counts.
setPage("/SigGear-product-docs/request-cad-sample-quote/", "");
const selfContext = click("?start=existing_motor&path=gearbox_only");
assert.equal(selfContext.filter(e => e.name === "engineering_brief_open_click").length, 0,
  "same-form scenario selection must not be counted as another entry");

console.log("PASS six GEO source-page inquiry-click origins and unclassified fallback");

console.log("PASS application -> product -> engineering file journey events without adding cookie tracking");
console.log("PASS 33 motor PDF intent label and application-origin context");

console.log("PASS PDF, original 2D, full STEP, simplified STEP click classifications and legacy CAD events");
