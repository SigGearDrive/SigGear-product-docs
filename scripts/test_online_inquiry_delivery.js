#!/usr/bin/env node
"use strict";

// The customer now contacts SigGear through mailto; no form, POST or provider.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

const contact = fs.readFileSync("docs/contact.md", "utf8");
const inquiry = fs.readFileSync("docs/request-cad-sample-quote.md", "utf8");
const js = fs.readFileSync("docs/assets/javascripts/direct-contact.js", "utf8");
const css = fs.readFileSync("docs/assets/stylesheets/direct-contact.css", "utf8");
for (const [name, page] of [["contact", contact], ["inquiry", inquiry]]) {
  assert.match(page, /^# Contact SigGear$/m, name);
  assert.match(page, /Luffy Wang/, name);
  assert.match(page, /class="siggear-direct-email"/, name);
  assert.match(page, /href="mailto:luffy@siggear\.com\?subject=SigGear%20Engineering%20Inquiry"/, name);
  assert.doesNotMatch(page, /<(?:form|input|textarea|select|button)\b/i, name);
  assert.doesNotMatch(page, /(?:FormSubmit|formsubmit\.co|_captcha|privacy_ack|sg-contact-email)/i, name);
}
assert.match(inquiry, /id="engineering-project-brief"/);
assert.match(css, /\.siggear-direct-email/);
assert.match(css, /overflow-wrap:\s*anywhere/);
assert.match(css, /@media \(max-width: 44rem\)/);
assert.doesNotMatch(js, /(?:fetch\(|XMLHttpRequest|FormSubmit|formsubmit\.co)/i);

function subject(search) {
  const links = [0, 1].map(() => ({
    href: "mailto:luffy@siggear.com?subject=SigGear%20Engineering%20Inquiry",
    setAttribute(name, value) { assert.equal(name, "href"); this.href = value; }
  }));
  const context = {
    document: { querySelectorAll(name) {
      assert.equal(name, "[data-siggear-contact-link]");
      return links;
    } },
    window: { location: { search } },
    URLSearchParams
  };
  vm.runInNewContext(js, context);
  assert.equal(links[0].href, links[1].href);
  const url = new URL(links[0].href);
  assert.equal(url.protocol, "mailto:");
  assert.equal(url.pathname, "luffy@siggear.com");
  return url.searchParams.get("subject");
}

assert.equal(subject(""), "SigGear Engineering Inquiry");
assert.equal(subject("?model=12P&start=existing_motor"), "SigGear Engineering Inquiry - 12P - Existing Motor");
assert.equal(subject("?model=SG-8021&path=joint_actuator"), "SigGear Engineering Inquiry - SG-8021 - Joint Actuator");
assert.equal(subject("?model=12P&start=drawing_cad"), "SigGear Engineering Inquiry - 12P - Drawing / STEP");
assert.equal(subject("?model=%0Aevil%40example.com&path=joint_actuator"), "SigGear Engineering Inquiry - Joint Actuator");
console.log("PASS: no form, one-click mailto, visible email, model context preserved, no network POST");
