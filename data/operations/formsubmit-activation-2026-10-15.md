# SigGear engineering inquiry — FormSubmit activation and operations

**Activation status:** FormSubmit recipient activation completed. SigGear owner confirmed on **2026-10-15** that the second test engineering inquiry was received by **wangwanrong@siggear.com**.

**Live form:** https://siggeardrive.github.io/SigGear-product-docs/request-cad-sample-quote/

**Published mode:** Online submission is the default; **Prepare Email Instead** and **Copy Project Brief** are preserved.

## Activation history (completed)

1. FormSubmit was configured for the SigGear external sales engineering mailbox.
2. The owner used a non-confidential internal test request and completed recipient activation.
3. The owner repeated the test and explicitly confirmed actual receipt in the mailbox on 2026-10-15.
4. The `ONLINE_DELIVERY_VERIFIED` gate in `docs/assets/javascripts/inquiry-form.js` was changed to `true` only after that confirmation; the live site deployment remains subject to the repository's build and validation checks.

The previous `?form_setup=1` owner-test URL remains harmless but is no longer necessary. The standard URL is the one customers should use.

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
- Treat a request as a **received** inquiry only after the actual email appears at `wangwanrong@siggear.com`.
- Mark it **qualified** only after a real application need, identifiable reply route, and next meaningful action are confirmed.
- Periodically submit non-confidential test data to verify the recipient mailbox and CAPTCHA workflow; investigate spam or provider delivery failure if results differ.

## Emergency fallback / rollback

If inbox delivery stops: use the existing **Prepare Email Instead** button; contact the provider. To temporarily disable online POST, change `ONLINE_DELIVERY_VERIFIED` to `false`, increment the `inquiry-form.js` cache-busting version in `mkdocs.yml`, and redeploy after validation. This restores the direct-email default without touching SEO pages or the selection-tool handoff.
