#!/usr/bin/env node
"use strict";

// Isolated browser-free UI tests. Never sends a real HTTP request or email.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

const js = fs.readFileSync("docs/assets/javascripts/inquiry-form.js", "utf8");
const page = fs.readFileSync("docs/request-cad-sample-quote.md", "utf8");
const styles = fs.readFileSync("docs/assets/stylesheets/inquiry-form.css", "utf8");

assert.match(page, /name="_captcha" value="true"/);
assert.match(page, /name="_honey"/);
assert.match(page, /name="_next" value="https:\/\/siggeardrive.github.io\/SigGear-product-docs\/request-cad-sample-quote\/\?form_delivery=provider_return"/);
assert.match(page, /name="email"/);
assert.match(page, /name="message"/);
assert.match(page, /https:\/\/formsubmit.co\/privacy/);
assert.match(page, /id="sg-email-brief"[^>]+hidden style="display:none"/);
assert.match(styles, /\.siggear-honeypot\s*\{[\s\S]*?display:\s*none !important/);
assert.match(js, /var ONLINE_DELIVERY_VERIFIED = true;/);
assert.match(js, /form.action = "https:\/\/formsubmit.co\/luffy@siggear.com"/);
assert.doesNotMatch(js, /ownerSetupMode/);
assert.doesNotMatch(js, /engineering_brief_online_submit_success/);

function bootstrap(search, referrer = "", mode = "public") {
  const events = {};
  const elements = new Map();
  const gaEvents = [];
  function node(id) {
    if (!elements.has(id)) {
      elements.set(id, {
        id, value: "", required: false, checked: false, hidden: false,
        textContent: "", selectedIndex: 0, options: [{text:"Not specified"}],
        style: {},
        addEventListener(event, callback) {
          events[id + "." + event] = callback;
        },
        focus() {}, scrollIntoView() {}, setAttribute() {}, select() {}
      });
    }
    return elements.get(id);
  }
  const form = node("siggear-engineering-brief");
  form.action = "#";
  form.method = "POST";
  form.reportValidity = () => {
    return [...elements.values()].every(el =>
      (!el.required || (el.id === "sg-online-consent" ? el.checked : !!String(el.value).trim()))
    );
  };
  node("sg-application").value = "Example miniature motion design";
  node("sg-application").required = true;
  node("sg-path").value = "not_sure";
  node("sg-next-step").value = "Model recommendation";
  node("sg-brief-primary").textContent = "Prepare Email to SigGear";
  node("sg-online-consent-wrap").hidden = true;
  node("sg-online-delivery-note").hidden = true;
  node("sg-email-brief").hidden = true;
  node("sg-online-return").hidden = true;
  const location = {
    search, hash: "", hostname: "siggeardrive.github.io",
    origin: "https://siggeardrive.github.io",
    pathname: "/SigGear-product-docs/request-cad-sample-quote/",
    href: "https://siggeardrive.github.io/SigGear-product-docs/request-cad-sample-quote/" + search
  };
  const window = {location, gtag(event, name, params) {gaEvents.push({event,name,params});}};
  const document = {
    referrer,
    getElementById: node,
    createElement: () => node("temporary"),
    body: {appendChild(){},removeChild(){}},
    execCommand(){}
  };
  // Simulate a temporary delivery hold independently; production is now online.
  const script = mode === "safe_simulation" ? js.replace(
    "var ONLINE_DELIVERY_VERIFIED = true;",
    "var ONLINE_DELIVERY_VERIFIED = false;"
  ) : js;
  vm.runInNewContext(script, {document, window, URL, URLSearchParams, navigator:{clipboard:{}}, console}, {
    filename:"inquiry-form.js"
  });
  function submit() {
    let prevented = false;
    const event = {preventDefault(){prevented=true;}};
    assert.equal(typeof events["siggear-engineering-brief.submit"], "function");
    events["siggear-engineering-brief.submit"](event);
    return {prevented};
  }
  return {node, events, gaEvents, form, submit, window};
}

// Simulated emergency rollback must retain direct email if online delivery is held.
const safeFallback = bootstrap("", "", "safe_simulation");
assert.equal(safeFallback.form.action, "#");
assert.equal(safeFallback.node("sg-brief-primary").textContent, "Prepare Email to SigGear");
assert.equal(safeFallback.node("sg-email-brief").hidden, true);
assert.equal(safeFallback.node("sg-online-consent-wrap").hidden, true);
assert.equal(safeFallback.submit().prevented, true);
assert.match(safeFallback.window.location.href, /^mailto:luffy@siggear\.com/);
assert.ok(safeFallback.gaEvents.some(x => x.name === "engineering_brief_prepare_email"));
console.log("PASS simulated safe rollback: direct email to Luffy, no online POST");

// Test the actual public FormSubmit workflow after recipient confirmation.
const live = bootstrap("");
assert.equal(live.form.method, "POST");
assert.equal(live.form.action, "https://formsubmit.co/luffy@siggear.com");
assert.equal(live.node("sg-brief-primary").textContent, "Send Engineering Request Online");
assert.equal(live.node("sg-email-brief").hidden, false);
assert.equal(live.node("sg-email-brief").style.display, "inline-flex");
assert.equal(live.node("sg-online-consent-wrap").hidden, false);
assert.equal(live.node("sg-online-consent-wrap").style.display, "block");
assert.equal(live.node("sg-online-delivery-note").hidden, false);
assert.equal(live.node("sg-contact-email").required, true);
assert.equal(live.node("sg-online-consent").required, true);
assert.equal(live.form.reportValidity(), false, "missing email and privacy consent must block online submission");
live.node("sg-contact-email").value = "buyer@example.org";
live.node("sg-online-consent").checked = true;
live.node("sg-contact-name").value = "Example engineer";
assert.equal(live.form.reportValidity(), true);
assert.equal(live.submit().prevented, false, "browser must perform native POST after validation");
assert.match(live.node("sg-online-message").value, /Example miniature motion design/);
assert.match(live.node("sg-online-message").value, /Contact email: buyer@example.org/);
assert.match(live.node("sg-online-message").value, /Contact name: Example engineer/);
assert.match(live.node("sg-online-subject").value, /Custom Transmission Project Review/);
assert.equal(live.node("sg-online-url").value, "https://siggeardrive.github.io/SigGear-product-docs/request-cad-sample-quote/");
assert.ok(live.gaEvents.some(x => x.name === "engineering_brief_online_submit_attempt"));
assert.ok(!live.gaEvents.some(x => x.name === "engineering_brief_online_submit_success"));
console.log("PASS public FormSubmit default: native POST, consent, and no false receipt claim");

// Historical activation-test URL retains ordinary parameter handling in simulated future mode.
const oldSetupUrl = bootstrap("?form_setup=1");
assert.equal(oldSetupUrl.node("sg-brief-primary").textContent, "Send Engineering Request Online");
assert.equal(oldSetupUrl.node("sg-email-brief").hidden, false);
assert.equal(oldSetupUrl.node("sg-online-consent-wrap").hidden, false);
assert.match(oldSetupUrl.form.action, /^https:\/\/formsubmit.co\//);
console.log("PASS legacy activation URL does not alter online behavior");
const blockedSetup = bootstrap("?form_setup=1", "", "safe_simulation");
assert.equal(blockedSetup.node("sg-brief-primary").textContent, "Prepare Email to SigGear");
assert.equal(blockedSetup.submit().prevented, true);
assert.match(blockedSetup.window.location.href, /^mailto:luffy@siggear\.com/);

// Online requires reply email and privacy consent; direct email must not.
const fallback = bootstrap("");
fallback.node("sg-contact-email").value = "buyer@example.org";
assert.equal(fallback.form.reportValidity(), false, "privacy acknowledgment required");
fallback.node("sg-online-consent").checked = true;
assert.equal(fallback.form.reportValidity(), true);
fallback.node("sg-online-consent").checked = false;
assert.equal(typeof fallback.events["sg-email-brief.click"], "function");
fallback.events["sg-email-brief.click"]();
assert.match(fallback.window.location.href, /^mailto:luffy@siggear\.com/);
assert.ok(fallback.gaEvents.some(x => x.name === "engineering_brief_prepare_email"));
console.log("PASS Prepare Email Instead remains available without provider consent");

// Provider redirect is an event, but not proof of delivered or qualified inquiry.
const returned = bootstrap("?form_delivery=provider_return");
assert.equal(returned.node("sg-online-return").hidden, false);
const ev = returned.gaEvents.find(x => x.name === "engineering_brief_provider_return");
assert.ok(ev);
assert.equal(ev.params.delivery_confirmed, 0);
console.log("PASS provider return is not claimed as confirmed inbox delivery");


// Model-aware product-to-engineering inquiry paths; no external HTTP/email.
for (const [reference, kind] of [
  ["SG-6010C", "joint_actuator"],
  ["SG-6010D", "joint_actuator"],
  ["SG-6010HB", "joint_actuator"],
  ["SG-8021", "joint_actuator"],
  ["CPM-78-39", "joint_actuator"],
  ["CPM-80-25", "joint_actuator"],
  ["CPM-100-25", "joint_actuator"],
  ["SG-2877", "hub_gear_motor"],
  ["SG-2878", "hub_gear_motor"]
]) {
  assert.match(page, new RegExp('value="' + reference + '"'), "model must exist in form");
  assert.match(page, new RegExp('value="' + kind + '"'), "project path must exist in form");
  const inquiry = bootstrap("?model=" + encodeURIComponent(reference) +
    "&start=standard_product&path=" + kind);
  assert.equal(inquiry.node("sg-model").value, reference, "model prefill: " + reference);
  assert.equal(inquiry.node("sg-path").value, kind, "path prefill: " + reference);
  assert.equal(inquiry.node("sg-starting-point").value, "standard_product");
  assert.equal(inquiry.node("sg-existing-motor-fields").hidden, true,
    "joint/hub requests must not require a separate existing motor");
  inquiry.node("sg-contact-email").value = "engineer@example.org";
  inquiry.node("sg-online-consent").checked = true;
  assert.equal(inquiry.submit().prevented, false);
  assert.match(inquiry.node("sg-online-message").value, new RegExp("Model reference: " + reference));
  assert.match(inquiry.node("sg-online-subject").value, new RegExp(reference));
  assert.match(inquiry.node("sg-online-subject").value,
    kind === "joint_actuator" ? /Robot Joint \/ Cycloidal Module Engineering Review/ :
      /Hub Gear Motor Engineering Review/);
}
const legacyGearhead = bootstrap("?model=12P&start=existing_motor&path=gearbox_only");
assert.equal(legacyGearhead.node("sg-model").value, "12P");
assert.equal(legacyGearhead.node("sg-path").value, "gearbox_only");
assert.equal(legacyGearhead.node("sg-existing-motor-fields").hidden, false);
console.log("PASS 9 joint/hub product inquiry routes and unchanged 12P planetary gearbox route");

// Recognize six GEO engineering landing pages from the immediate same-site
// referrer only; both analytics and actual email brief must preserve context.
const geoCases = [
  ["custom-engineering/custom-planetary-gearbox", "geo_existing_motor", "Existing-motor gearbox engineering"],
  ["custom-engineering/custom-gearbox-from-drawing-cad", "geo_drawing_step_sample", "Customer drawing / STEP / sample"],
  ["custom-engineering/replacement-planetary-gearhead", "geo_replacement_redesign", "Existing gearbox replacement / redesign"],
  ["custom-engineering/gearbox-failure-analysis-durability-redesign", "geo_failure_durability", "Gearbox failure / durability"],
  ["custom-engineering/prototype-to-production", "geo_prototype_to_volume", "Prototype to volume production"],
  ["selection-guides/custom-gearbox-manufacturer-supplier-qualification", "geo_supplier_qualification", "Supplier qualification guide"]
];
const analyticsJs = fs.readFileSync("docs/assets/javascripts/analytics-events.js", "utf8");
const measureSchema = fs.readFileSync("data/sales/inquiry-measurement-schema.yml", "utf8");
for (const [slug, origin, label] of geoCases) {
  const fromPage = "https://siggeardrive.github.io/SigGear-product-docs/" + slug + "/";
  const review = bootstrap("", fromPage + "?private_hint=never-copy-this");
  review.node("sg-contact-email").value = "engineer@example.org";
  review.node("sg-online-consent").checked = true;
  assert.equal(review.submit().prevented, false);
  const attempt = review.gaEvents.find(e => e.name === "engineering_brief_online_submit_attempt");
  assert.equal(attempt.params.inquiry_origin, origin, "form origin: " + slug);
  assert.ok(review.node("sg-online-message").value.includes("Engineering entry page: " + label));
  assert.ok(!review.node("sg-online-message").value.includes("private_hint="));
  assert.ok(!review.node("sg-online-message").value.includes("never-copy-this"));
  assert.ok(analyticsJs.includes('if (pagePath === "/SigGear-product-docs/' + slug + '/") return "' + origin + '"'));
  assert.ok(measureSchema.includes("      - " + origin));
}
// External referrers and suppressed referrers must never be upgraded to a
// claimed GEO source or attributed to a particular AI assistant.
for (const referrer of ["", "https://example.com/SigGear-product-docs/custom-engineering/custom-planetary-gearbox/"]) {
  const unknown = bootstrap("", referrer);
  unknown.node("sg-contact-email").value = "engineer@example.org";
  unknown.node("sg-online-consent").checked = true;
  assert.equal(unknown.submit().prevented, false);
  const attempt = unknown.gaEvents.find(e => e.name === "engineering_brief_online_submit_attempt");
  assert.equal(attempt.params.inquiry_origin, "direct_or_external");
  assert.ok(!unknown.node("sg-online-message").value.includes("Engineering entry page:"));
}
console.log("PASS six GEO entry scenarios attributed without AI-source guesses or referrer-query leakage");


const catalogue = fs.readFileSync("docs/products/index.md", "utf8");
assert.match(catalogue, /Planetary Gearbox PDF \/ 2D \/ STEP/);
assert.match(catalogue, /Motor Datasheets/);
assert.match(catalogue, /Robot Joint Module Files/);
assert.match(catalogue, /SG-2877_Public_Reference_Datasheet_Rev0\.1\.pdf/);
assert.match(catalogue, /SG-2878_Public_Reference_Datasheet_Rev0\.1\.pdf/);
assert.match(catalogue, /Custom OEM \/ ODM/);
for(const [model, slug, folder] of [
  ["SG-6010C","sg6010c","robot-joint-actuators"],
  ["SG-6010D","sg6010d","robot-joint-actuators"],
  ["SG-8021","sg8021","robot-joint-actuators"],
  ["CPM-78-39","cpm78-39","cycloidal-joint-modules"],
  ["CPM-80-25","cpm80-25","cycloidal-joint-modules"],
  ["CPM-100-25","cpm100-25","cycloidal-joint-modules"],
  ["SG-6010HB","sg6010hb","robot-joint-actuators"],
  ["SG-2877","sg2877","hub-gear-motors"],
  ["SG-2878","sg2878","hub-gear-motors"]
]) {
  const productPage = fs.readFileSync("docs/products/" + folder + "/" + slug + ".md", "utf8");
  assert.match(productPage, new RegExp("model=" + model), model + " needs prefilled inquiry URL");
  if (folder === "hub-gear-motors") {
    assert.match(productPage, new RegExp(model + "_Public_Reference_Datasheet_Rev0\\.1\\.pdf"),
      model + " must retain its new published PDF link");
    assert.match(productPage, /not a verified STEP export/, "do not overstate Parasolid CAD");
    assert.match(productPage, /External controller required/, "do not imply a supplied controller");
  }
}
console.log("PASS product directory, 9 product-to-OEM paths and source-backed hub PDF safeguards");
