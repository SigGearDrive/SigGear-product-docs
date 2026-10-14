#!/usr/bin/env node
"use strict";

// Behavioral smoke tests for the public 8P-42P selection interface.
// These do not validate engineering operating limits beyond published data.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

const js = fs.readFileSync("docs/assets/javascripts/ratio-stage-selector.js", "utf8");
const data = JSON.parse(fs.readFileSync("docs/assets/data/planetary-ratio-stage-data.json", "utf8"));

async function run(input) {
  const ids = {
    "sg-selector-motor-speed": input.motorSpeed ?? "6000",
    "sg-selector-output-speed": input.outputSpeed ?? "140",
    "sg-selector-diameter": input.diameter ?? "12",
    "sg-selector-length": input.length ?? "18",
    "sg-selector-torque": input.torque ?? "0.2",
    "sg-selector-peak-torque": input.peak ?? "0.4",
    "sg-selector-torque-unit": input.unit ?? "nm",
    "sg-selector-ratio-tolerance": input.tolerance ?? "5"
  };
  const elements = Object.fromEntries(Object.entries(ids).map(([key, value]) =>
    [key, { value: String(value) }]
  ));
  let submit;
  const form = { addEventListener: (event, handler) => {
    assert.equal(event, "submit");
    submit = handler;
  } };
  const summary = { textContent: "", innerHTML: "" };
  const results = { innerHTML: "" };
  const special = {
    "siggear-ratio-stage-selector": form,
    "sg-ratio-stage-summary": summary,
    "sg-ratio-stage-results": results
  };
  const document = { getElementById: id => special[id] ?? elements[id] ?? null };
  const window = {
    location: {
      pathname: "/SigGear-product-docs/selection-guides/miniature-planetary-gearbox-selection-guide/",
      href: "https://siggeardrive.github.io/SigGear-product-docs/selection-guides/miniature-planetary-gearbox-selection-guide/"
    }
  };
  const fetch = async () => ({ok:true, json:async () => data});
  vm.runInNewContext(js, {document, window, URL, fetch, console}, {filename:"ratio-stage-selector.js"});
  assert.equal(typeof submit, "function", "Missing selector submit handler");
  await submit({preventDefault() {}});
  return {
    summary: summary.innerHTML || summary.textContent,
    results: results.innerHTML
  };
}

(async () => {
  const good = await run({});
  assert.match(good.results, /12P/);
  assert.match(good.results, /42\.9:1/);
  assert.match(good.results, /0\.353 N·m/);
  assert.match(good.results, /selector_continuous_nm=0\.20000/);
  assert.match(good.results, /selector_peak_nm=0\.40000/);
  assert.match(good.results, /candidate-design-in-pack/);
  console.log("PASS 12P 3-stage matching, published rating, and Design-In/inquiry links");

  const same = await run({
    unit: "kgfcm", torque: String(0.2/0.0980665), peak: String(0.4/0.0980665)
  });
  assert.match(same.results, /12P/);
  assert.match(same.results, /42\.9:1/);
  console.log("PASS equivalent torque inputs in N-m and kgf-cm");

  const highSpeed = await run({ motorSpeed: "9000" });
  assert.match(highSpeed.summary, /8,000 rpm/);
  assert.equal(highSpeed.results, "");
  console.log("PASS 9000 rpm continuous input speed rejection");

  const excessivePeak = await run({ peak:"1.0" });
  assert.match(excessivePeak.results, /No published configuration remains/);
  console.log("PASS peak torque exceeding published momentary limit excluded");

  const reversedTorque = await run({ peak:"0.1", torque:"0.2" });
  assert.match(reversedTorque.summary, /peak torque must not be lower than continuous torque/i);
  assert.equal(reversedTorque.results, "");
  console.log("PASS peak less than continuous torque rejection");

  const optionalPeak = await run({ peak:"" });
  assert.match(optionalPeak.results, /12P/);
  console.log("PASS optional peak input can remain blank");
})().catch(err => {
  console.error(err);
  process.exitCode = 1;
});
