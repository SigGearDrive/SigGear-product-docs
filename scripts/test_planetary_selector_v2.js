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
  const changeHandlers = {};
  const elements = Object.fromEntries(Object.entries(ids).map(([key, value]) =>
    [key, { value: String(value), addEventListener: (event, callback) => {
      changeHandlers[key + ":" + event] = callback;
    } }]
  ));
  let submit;
  const form = { addEventListener: (event, handler) => {
    assert.equal(event, "submit");
    submit = handler;
  } };
  const summary = { textContent: "", innerHTML: "" };
  const results = { innerHTML: "" };
  const applicationContext = { textContent: "", hidden: true };
  const special = {
    "siggear-ratio-stage-selector": form,
    "sg-ratio-stage-summary": summary,
    "sg-ratio-stage-results": results,
    "sg-selector-application-context": applicationContext
  };
  const document = { getElementById: id => special[id] ?? elements[id] ?? null };
  const gaEvents = [];
  const window = {
    location: {
      pathname: "/SigGear-product-docs/selection-guides/miniature-planetary-gearbox-selection-guide/",
      href: "https://siggeardrive.github.io/SigGear-product-docs/selection-guides/miniature-planetary-gearbox-selection-guide/" + (input.query || "")
    },
    gtag: (event, name, params) => gaEvents.push({event, name, params})
  };
  const fetch = async () => ({ok:true, json:async () => data});
  vm.runInNewContext(js, {document, window, URL, fetch, console}, {filename:"ratio-stage-selector.js"});
  assert.equal(typeof submit, "function", "Missing selector submit handler");
  if (input.switchTo) {
    elements["sg-selector-torque-unit"].value = input.switchTo;
    const onchange = changeHandlers["sg-selector-torque-unit:change"];
    assert.equal(typeof onchange, "function", "Unit conversion handler missing");
    onchange();
  }
  await submit({preventDefault() {}});
  return {
    summary: summary.innerHTML || summary.textContent,
    results: results.innerHTML,
    fields: elements,
    applicationContext,
    gaEvents
  };
}

(async () => {
  const knownContexts = [
    ["electric_pruning_shears", "Electric pruning shears"],
    ["electric_curtain_blind", "Electric curtain / blind / window opener"],
    ["smart_toilet_bidet", "Smart toilet / bidet mechanism"],
    ["dexterous_hand_gripper", "Dexterous hand / robot gripper"]
  ];
  for (const [app, label] of knownContexts) {
    const fromApp = await run({query: "?app=" + app});
    assert.equal(fromApp.applicationContext.hidden, false);
    assert.ok(fromApp.applicationContext.textContent.includes(label), "Matching app context label must be visible");
    assert.match(fromApp.results, new RegExp("&app=" + app));
    assert.ok(fromApp.gaEvents.some(x =>
      x.name === "ratio_stage_selector_run" && x.params.inquiry_application === app
    ));
  }
  console.log("PASS 4 supported OEM application paths reach published candidates and GA4");

  const appNoMatch = await run({query: "?app=electric_curtain_blind", torque:"1.0", peak:"1.2"});
  assert.match(appNoMatch.results, /Request Custom Engineering Review/);
  assert.match(appNoMatch.results, /&amp;app=electric_curtain_blind/);
  console.log("PASS no-match custom feasibility request retains safe application slug");

  const appOutsideSpeed = await run({query: "?app=smart_toilet_bidet",motorSpeed:"21000"});
  assert.match(appOutsideSpeed.results, /speed_above_engineering/);
  assert.match(appOutsideSpeed.results, /&amp;app=smart_toilet_bidet/);
  console.log("PASS out-of-range speed review retains application context");

  const injected = await run({query: "?app=%3Cscript%3Eevil%3C%2Fscript%3E"});
  assert.equal(injected.applicationContext.hidden,true);
  assert.doesNotMatch(injected.results, /&app=|<script>evil/);
  assert.ok(injected.gaEvents.some(x=>x.name==="ratio_stage_selector_run" && x.params.inquiry_application==="not_specified"));
  console.log("PASS unknown or unsafe app values are ignored and never propagated");

  const from12p = await run({ diameter: "", query: "?max_diameter=12" });
  assert.equal(from12p.fields["sg-selector-diameter"].value, "12");
  assert.match(from12p.results, /12P/);
  assert.match(from12p.results, /selector_max_diameter=12/);
  console.log("PASS 12P model-page link prefills editable maximum diameter");

  const ignoreInvalid = await run({ diameter: "", query: "?max_diameter=19" });
  assert.equal(ignoreInvalid.fields["sg-selector-diameter"].value, "");
  assert.match(ignoreInvalid.results, /12P/);
  console.log("PASS unsupported diameter prefill safely ignored");

  const preserveUserFilter = await run({ diameter: "20", query: "?max_diameter=12" });
  assert.equal(preserveUserFilter.fields["sg-selector-diameter"].value, "20");
  console.log("PASS explicit user diameter is not overwritten");

  const good = await run({});
  assert.match(good.results, /12P/);
  assert.match(good.results, /42\.9:1/);
  assert.match(good.results, /0\.353 N·m/);
  assert.match(good.results, /selector_continuous_nm=0\.20000/);
  assert.match(good.results, /selector_peak_nm=0\.40000/);
  assert.match(good.results, /candidate-design-in-pack/);
  assert.match(good.results, /selector_max_diameter=12/);
  assert.match(good.results, /selector_max_gearbox_length=18/);
  assert.match(good.results, /ratio-dependent efficiency has not been separately verified/);
  console.log("PASS 12P 3-stage matching, published rating, and Design-In/inquiry links");

  const same = await run({
    unit: "kgfcm", torque: String(0.2/0.0980665), peak: String(0.4/0.0980665)
  });
  assert.match(same.results, /12P/);
  assert.match(same.results, /42\.9:1/);
  console.log("PASS equivalent torque inputs in N-m and kgf-cm");

  const switched = await run({switchTo: "kgfcm"});
  assert.match(switched.results, /12P/);
  assert.ok(Math.abs(Number(switched.fields["sg-selector-torque"].value) * 0.0980665 - 0.2) < 1e-6);
  assert.ok(Math.abs(Number(switched.fields["sg-selector-peak-torque"].value) * 0.0980665 - 0.4) < 1e-6);
  console.log("PASS unit switch converts existing torque values without silently changing load");

  const highSpeed = await run({ motorSpeed: "9000" });
  assert.match(highSpeed.results, /Candidate Frame Comparison/);
  assert.match(highSpeed.results, /12P/);
  assert.doesNotMatch(highSpeed.summary, /custom feasibility/i);
  console.log("PASS 9,000 rpm treated as standard input speed");

  const upperBoundary = await run({motorSpeed: "20000", outputSpeed: String(20000 / 42.9)});
  assert.match(upperBoundary.results, /Candidate Frame Comparison/);
  assert.match(upperBoundary.results, /12P/);
  console.log("PASS 20,000 rpm continuous standard upper boundary");

  const lowerBoundary = await run({motorSpeed: "1000", outputSpeed: String(1000 / 42.9)});
  assert.match(lowerBoundary.results, /Candidate Frame Comparison/);
  assert.match(lowerBoundary.results, /12P/);
  console.log("PASS 1,000 rpm continuous standard lower boundary");

  const higherSpeed = await run({motorSpeed: "20001"});
  assert.match(higherSpeed.summary, /exceeds the standard continuous input-speed range/);
  assert.match(higherSpeed.results, /speed_above_engineering/);
  assert.match(higherSpeed.results, /selector_motor_speed=20001/);
  console.log("PASS >20,000 rpm routed to custom feasibility review");

  const lowSpeed = await run({motorSpeed: "999"});
  assert.match(lowSpeed.summary, /below the standard continuous input-speed range/);
  assert.match(lowSpeed.results, /speed_below_engineering/);
  assert.match(lowSpeed.results, /selector_motor_speed=999/);
  console.log("PASS <1,000 rpm routed to custom feasibility review");

  const excessivePeak = await run({ peak:"1.0" });
  assert.match(excessivePeak.results, /No published standard configuration remains/);
  assert.match(excessivePeak.results, /Request Custom Engineering Review/);
  assert.match(excessivePeak.results, /selector_peak_nm=1.00000/);
  console.log("PASS excessive peak load excluded from catalog and referred for customization");

  const excessiveContinuous = await run({torque: "1.0", peak: "1.2"});
  assert.match(excessiveContinuous.results, /No published standard configuration remains/);
  assert.match(excessiveContinuous.results, /selector_continuous_nm=1.00000/);
  assert.match(excessiveContinuous.results, /Request Custom Engineering Review/);
  console.log("PASS excessive continuous load passed to custom engineering rather than rejected");

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
