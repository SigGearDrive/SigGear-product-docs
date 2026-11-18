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
console.log("PASS PDF, original 2D, full STEP, simplified STEP click classifications and legacy CAD events");
