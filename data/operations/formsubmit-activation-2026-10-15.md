# SigGear engineering inquiry online delivery — activation checklist

Status: **implementation prepared; public online submit disabled until inbox test is verified.**
Owner: SigGear overseas sales engineering.
Live canonical inquiry page: https://siggeardrive.github.io/SigGear-product-docs/request-cad-sample-quote/
Owner activation test URL: https://siggeardrive.github.io/SigGear-product-docs/request-cad-sample-quote/?form_setup=1

## Purpose

SigGear's site is deployed as static GitHub Pages. A native HTML POST to FormSubmit provides form forwarding, spam protection and a CAPTCHA flow without a new SigGear server. The original Prepare Email to SigGear remains the public default until verified delivery. **Neither opening an email draft nor a FormSubmit redirect proves receipt.**

## Required activation steps (human action)

1. Open the owner activation URL above in the published site. The online button and privacy consent should appear only with `form_setup=1`.
2. Enter `SigGear internal activation test — do not quote` in the Application field. Enter the owner-controlled reply address under Contact email. Do not enter a real customer name, proprietary drawing or confidential design data.
3. Tick the service-processing consent, click **Send Engineering Request Online**, and complete the provider CAPTCHA if shown.
4. Check `wangwanrong@siggear.com` for a FormSubmit activation request, including spam/junk folders. Check the sender and that the confirmation link is on the official `formsubmit.co` domain before confirming.
5. After activation, repeat a test submission from the same SigGear owner activation URL. **Verify actual message arrival in the SigGear mailbox**, with the project brief, reply-to address and sender details.
6. Check that the failure and spam paths are understandable; confirm that **Prepare Email Instead** and **Copy Project Brief** still work.
7. Only after this second test succeeds: set `ONLINE_DELIVERY_VERIFIED = true` in `docs/assets/javascripts/inquiry-form.js`, rerun CI and deploy via reviewed Pull Request.
8. Track live requests as sales leads only **after actual receipt and qualification**. `engineering_brief_online_submit_attempt` is just a pre-delivery attempt.

## Guardrails

- Never send an external test request on a customer's behalf or put customer data in a test.
- Do not upload NDA-restricted drawings to the public form; use direct email and agreed engineering file channels.
- No permanent secrets or API keys in the public GitHub repository.
- Keep FormSubmit's native CAPTCHA enabled and the honeypot field; do not switch to AJAX and silently bypass the provider challenge.
- Third-party service availability and delivery remain separate from the website deployment status.
- FormSubmit's service retains submissions for a limited period; investigate provider privacy and company policy before requesting sensitive personal or project data.
- The online form's `_next` redirect, and all Google Analytics events, are **not evidence of inbox receipt**.
