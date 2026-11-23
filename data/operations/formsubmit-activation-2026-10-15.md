# SigGear engineering inquiry — FormSubmit activation and operations

**Activation status:** SigGear owner confirmed on **2026-11-23** that a FormSubmit test message was received by the new address **luffy@siggear.com**, following the independent activation test flow. This is an owner-reported receipt, not a provider-dashboard audit. The previous address **wangwanrong@siggear.com** was separately activated and tested on **2026-10-15**.

**Live form:** https://siggeardrive.github.io/SigGear-product-docs/request-cad-sample-quote/

**Current published mode (2026-11-23):** Following owner-confirmed test receipt, native FormSubmit online submission to **luffy@siggear.com** is the default. **Prepare Email Instead** and **Copy Project Brief** remain available.

## Previous mailbox activation history (2026-10-15, preserved as audit record)

1. FormSubmit was configured for the SigGear external sales engineering mailbox.
2. The owner used a non-confidential internal test request and completed recipient activation.
3. The owner repeated the test and explicitly confirmed actual receipt in the mailbox on 2026-10-15.
4. The `ONLINE_DELIVERY_VERIFIED` gate in `docs/assets/javascripts/inquiry-form.js` was changed to `true` only after that **old-recipient** confirmation. Earlier on 2026-11-23 it was set to `false` during verification; after the new-recipient test receipt was confirmed it was set to `true`. The old recipient's activation was not used as evidence for the new one.

The previous `?form_setup=1` test URL does not bypass the new-address delivery hold and must not be used as evidence of activation. The standard URL is the one customers should use.

## Delivery architecture and privacy

- SigGear runs on GitHub Pages, and the public form performs a native HTTPS POST to FormSubmit. The provider handles the CAPTCHA and forwards the request to SigGear.
- The customer's **contact email** and **explicit data-processing acknowledgment** are mandatory for online sending. The contact name is optional; the application field is required.
- The online form includes a non-visible honeypot and FormSubmit's CAPTCHA; use neither unverified AJAX bypasses nor a `_captcha=false` setting.
- Do not solicit drawings, files controlled by an NDA, trade secrets or security-sensitive information through the public form. Ask for attachments by direct email or an agreed file transfer.
- The `_next` redirect contains no personal contact details. Contact information and project notes are not collected in GA4 event parameters.
- The legacy direct-email flow remains available in case the provider is blocked, unavailable, or the customer prefers to add engineering drawings.

## How to measure and verify leads

- `engineering_brief_online_submit_attempt` measures only intent and a browser-side POST attempt.
- `engineering_brief_provider_return` means the browser returned from provider processing, **not** that the request was delivered to the SigGear inbox.
- Treat a new request as **received** only when it actually appears at `luffy@siggear.com`. The historical test confirmation above refers exclusively to the previous mailbox.
- Mark it **qualified** only after a real application need, identifiable reply route, and next meaningful action are confirmed.
- Periodically submit non-confidential test data to verify the recipient mailbox and CAPTCHA workflow; investigate spam or provider delivery failure if results differ.

## Emergency fallback / rollback

If inbox delivery stops: use the existing **Prepare Email Instead** button; contact the provider. To temporarily disable online POST, change `ONLINE_DELIVERY_VERIFIED` to `false`, increment the `inquiry-form.js` cache-busting version in `mkdocs.yml`, and redeploy after validation. This restores the direct-email default without touching SEO pages or the selection-tool handoff.

## New public sales mailbox switch — 2026-11-23

- Published email, `mailto:` project briefs and organization JSON-LD use **luffy@siggear.com**.
- PR #296 changed public contacts and paused online sending pending new-recipient proof. PR #297 added an isolated non-confidential activation smoke-test page.
- SigGear owner subsequently confirmed test-email receipt at the new address ("收到", 2026-11-23). This confirmation is the release gate for enabling FormSubmit; it does not independently certify delivery of future customer inquiries.
- The public form uses native HTTPS POST to `https://formsubmit.co/luffy@siggear.com` with CAPTCHA, honeypot, contact email and explicit privacy consent. Direct email and Copy Project Brief stay available.
- The temporary activation page is removed when enabling live customer submission; validate the release with CI and live-site audit.
- After release, check the inbox regularly, periodically send a non-confidential production-page test, and roll back to `ONLINE_DELIVERY_VERIFIED = false` immediately if delivery stops.
