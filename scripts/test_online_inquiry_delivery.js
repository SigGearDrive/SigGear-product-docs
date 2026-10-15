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
assert.match(page, /id="sg-online-activation-indicator"/);
assert.match(styles, /\.siggear-honeypot\s*\{[\s\S]*?display:\s*none !important/);
assert.match(js, /var ONLINE_DELIVERY_VERIFIED = false;/);
assert.doesNotMatch(js, /engineering_brief_online_submit_success/);

function bootstrap(search) {
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
  node("sg-online-activation-indicator").hidden = true;
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
    referrer: "",
    getElementById: node,
    createElement: () => node("temporary"),
    body: {appendChild(){},removeChild(){}},
    execCommand(){}
  };
  vm.runInNewContext(js, {document, window, URL, URLSearchParams, navigator:{clipboard:{}}, console}, {
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

// Public page remains email-only until inbox activation and actual receipt.
const normal = bootstrap("");
assert.equal(normal.node("sg-brief-primary").textContent,"Prepare Email to SigGear");
assert.equal(normal.node("sg-email-brief").hidden,true);
assert.equal(normal.node("sg-email-brief").style.display,"none");
assert.equal(normal.node("sg-online-activation-indicator").hidden,true);
assert.equal(normal.node("sg-online-consent-wrap").hidden,true);
assert.equal(normal.node("sg-contact-email").required,false);
assert.equal(normal.submit().prevented,true);
assert.match(normal.window.location.href, /^mailto:wangwanrong@siggear\.com/);
assert.ok(normal.gaEvents.some(x=>x.name==="engineering_brief_prepare_email"));
assert.ok(!normal.gaEvents.some(x=>x.name==="engineering_brief_online_submit_attempt"));
console.log("PASS public remains mailto-only until form activation and inbox test");

// Internal activation URL exercises exactly the future online submission path.
const setup = bootstrap("?form_setup=1");
assert.equal(setup.form.method,"POST");
assert.equal(setup.form.action,"https://formsubmit.co/wangwanrong@siggear.com");
assert.equal(setup.node("sg-brief-primary").textContent,"Send Engineering Request Online");
assert.equal(setup.node("sg-email-brief").hidden,false);
assert.equal(setup.node("sg-email-brief").style.display,"inline-flex");
assert.equal(setup.node("sg-online-activation-indicator").hidden,false);
assert.equal(setup.node("sg-online-activation-indicator").style.display,"block");
assert.equal(setup.node("sg-online-consent-wrap").hidden,false);
assert.equal(setup.node("sg-online-consent-wrap").style.display,"block");
assert.equal(setup.node("sg-contact-email").required,true);
assert.equal(setup.node("sg-online-consent").required,true);
setup.node("sg-contact-email").value="buyer@example.org";
setup.node("sg-online-consent").checked=true;
setup.node("sg-contact-name").value="Example engineer";
assert.equal(setup.submit().prevented,false,"native browser POST must not be prevented");
assert.match(setup.node("sg-online-message").value,/Example miniature motion design/);
assert.match(setup.node("sg-online-message").value,/Contact email: buyer@example.org/);
assert.match(setup.node("sg-online-message").value,/Contact name: Example engineer/);
assert.match(setup.node("sg-online-subject").value,/Planetary Gearbox Project Review/);
assert.equal(setup.node("sg-online-url").value,"https://siggeardrive.github.io/SigGear-product-docs/request-cad-sample-quote/");
assert.ok(setup.gaEvents.some(x=>x.name==="engineering_brief_online_submit_attempt"));
assert.ok(!setup.gaEvents.some(x=>x.name==="engineering_brief_online_submit_success"));
console.log("PASS activation mode prepares native POST, complete engineering brief, and intent-only analytics");

// The online button requires a real reply address and consent, while mailto fallback remains.
const missing = bootstrap("?form_setup=1");
assert.equal(missing.form.reportValidity(),false);
missing.node("sg-contact-email").value="buyer@example.org";
assert.equal(missing.form.reportValidity(),false);
missing.node("sg-online-consent").checked=true;
assert.equal(missing.form.reportValidity(),true);
missing.node("sg-online-consent").checked=false;
missing.events["sg-email-brief.click"]();
assert.match(missing.window.location.href,/^mailto:wangwanrong@siggear\.com/);
console.log("PASS consent and email required only online; email fallback works without either");

// Query-string return must not be interpreted as verified mailbox delivery.
const returned=bootstrap("?form_delivery=provider_return");
assert.equal(returned.node("sg-online-return").hidden,false);
const ev=returned.gaEvents.find(x=>x.name==="engineering_brief_provider_return");
assert.ok(ev);
assert.equal(ev.params.delivery_confirmed,0);
console.log("PASS third-party return explicitly does not mean inbox delivery");
