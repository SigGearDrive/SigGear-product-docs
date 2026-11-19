#!/usr/bin/env node
"use strict";

// Run the actual GA4 click handler without external requests or cookies.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

const source = fs.readFileSync("docs/assets/javascripts/analytics-events.js", "utf8");
const events = [];
const handlers = {};
const base = "https://siggeardrive.github.io/SigGear-product-docs/engineering-resources/robot-joint-actuators/quick-downloads/";
const window = {
  dataLayer: [],
  location: {
    href: base,
    hostname: "siggeardrive.github.io",
    pathname: "/SigGear-product-docs/engineering-resources/robot-joint-actuators/quick-downloads/",
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

function click(url) {
  events.length = 0;
  const link = {getAttribute: key => key === "href" ? url : null, textContent: "Download"};
  handlers.click({target: {closest: name => name === "a" ? link : null}});
  return events.slice();
}

function testFile(folder, filename, model, variant, type) {
  const url = "../../../assets/downloads/" + folder + "/" + filename;
  const observed = click(url);
  const joint = observed.filter(x => x.name === "joint_engineering_file_click");
  assert.equal(joint.length, 1, "one joint event: " + filename);
  assert.equal(joint[0].params.joint_model, model, filename);
  assert.equal(joint[0].params.joint_variant, variant, filename);
  assert.equal(joint[0].params.file_type, type, filename);
  assert.equal(joint[0].params.source_page_type, "joint_download_hub", filename);
  assert.equal(joint[0].params.source_application, "not_specified", filename);
  assert.equal(observed.filter(x => x.name === "cad_download_click").length,
    type === "datasheet_pdf" ? 0 : 1, filename);
  assert.equal(observed.filter(x => x.name === "planetary_engineering_file_click").length, 0);
}

for (const model of ["SG-6010C","SG-6010D","SG-8021","CPM-78-39","CPM-80-25","CPM-100-25"]) {
  testFile("joint-actuators", model + "_Public_Reference_Datasheet_Rev0.1.pdf",
    model, "catalogue", "datasheet_pdf");
}
const full = [
  ["SG-6010C_Original_Full_Assembly_20261118.step","SG-6010C","standard"],
  ["SG-6010D_Original_Full_Assembly_20261118.step","SG-6010D","published_assembly"],
  ["SG-8021_Driver_Version_Original_Full_Assembly_20261118.step","SG-8021","driver_version"],
  ["CPM-78-39_Original_Full_Assembly_20261118.step","CPM-78-39","standard"],
  ["CPM-80-25_Original_Full_Assembly_No_Driver_20261118.step","CPM-80-25","no_driver"],
  ["CPM-80-25_Original_Full_Assembly_Integrated_Driver_20261118.step","CPM-80-25","integrated_driver"],
  ["CPM-100-25_Original_Full_Assembly_No_Driver_20261118.step","CPM-100-25","standard_29_5mm"],
  ["CPM-100-25D_Dual_Encoder_Driver_Original_Full_Assembly_20261118.step","CPM-100-25","dual_encoder_driver_48mm"]
];
for (const [file,model,variant] of full) {
  testFile("joint-actuators",file,model,variant,"original_full_step");
}
testFile("sg6010c","SG-6010C_Public_Simplified_STEP_v1.0.step","SG-6010C","simplified_standard","simplified_step");
testFile("cpm80-25","CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step","CPM-80-25","simplified_no_driver","simplified_step");
testFile("cpm80-25","CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step","CPM-80-25","simplified_integrated_driver","simplified_step");

assert.equal(click("../../../assets/downloads/joint-actuators/random-v2.step")
  .filter(x => x.name === "joint_engineering_file_click").length, 0);
assert.equal(click("https://example.com/SigGear-product-docs/assets/downloads/joint-actuators/SG-6010D_Original_Full_Assembly_20261118.step")
  .filter(x => x.name === "joint_engineering_file_click").length, 0);

const product = "/SigGear-product-docs/products/cycloidal-joint-modules/cpm100-25/";
window.location.pathname = product;
window.location.href = "https://siggeardrive.github.io" + product;
const observed = click("../../../assets/downloads/joint-actuators/CPM-100-25D_Dual_Encoder_Driver_Original_Full_Assembly_20261118.step");
assert.equal(observed.find(x => x.name === "joint_engineering_file_click").params.source_page_type,
             "joint_product_model");

console.log("PASS six reference PDFs, eight full STEP assemblies, three simplified STEP configurations");
console.log("PASS 17 joint engineering click classifications, correct variants, legacy CAD event continuity and same-site controls");
