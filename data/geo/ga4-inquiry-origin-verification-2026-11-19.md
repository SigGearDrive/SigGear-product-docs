# GA4 GEO Inquiry-Origin Reporting & Verification — 2026-11-19

## Goal

Measure which **real SigGear engineering page** leads to a structured inquiry action. Do not confuse an internal page entry with a visit originating from ChatGPT, Gemini, Claude, Perplexity or Microsoft Copilot.

This is a reporting / QA procedure, **not observed GA4 event data**.

## Observed integration status on 2026-11-19

- The public MkDocs configuration sets Google Analytics measurement ID `G-Q14K9BLGK4` and **optional consent, unchecked by default**.
- The website code emits normalized `inquiry_origin` as a parameter on `engineering_brief_open_click`, `inquiry_page_view`, `engineering_brief_prepare_email` and `engineering_brief_online_submit_attempt` when Google Analytics is available after consent.
- A same-site source-page **click** is categorized from its **current URL**. An inquiry-form **page view / submit attempt** is categorized from an **exact, immediate same-site referring URL**, when provided by the browser.
- On this date, Windsor.ai can access SigGear's **Search Console** property, but its `googleanalytics4` connector has **no selected GA4 property**. No live GA4 event count or registered custom dimension can be verified through this connection yet.
- This file is an operator checklist; it does not assert that external AI tools have recommended SigGear.

## One GA4 custom dimension, six GEO values

Check the correct GA4 property and whether this custom dimension already exists. **Do not create a duplicate.** If it is absent, someone with the required GA4 Editor/Admin access should register exactly one **event-scoped custom dimension**:

| GA4 field | Value |
| --- | --- |
| Dimension name | SigGear Inquiry Origin |
| Scope | Event |
| Event parameter | `inquiry_origin` |
| Description | Normalized immediate first-party engineering entry page or fallback; not an AI referral claim |

The six new values of this **one** parameter:

| Value | First-party page where a client started the inquiry click |
| --- | --- |
| `geo_existing_motor` | Existing Motor / Custom Planetary Gearbox |
| `geo_drawing_step_sample` | Customer Drawing / STEP / Sample |
| `geo_replacement_redesign` | Replacement / Redesign |
| `geo_failure_durability` | Failure / Durability |
| `geo_prototype_to_volume` | Prototype → Volume |
| `geo_supplier_qualification` | Supplier Qualification |

Existing non-GEO codes, including `product_model`, `application`, `selection_tool`, `internal_other`, `direct_or_external` and `unknown`, remain valid. **No cookies, free text, filenames, customer names, drawing details or external-referrer URL are needed** for this dimension.

Official GA4 guidance:
- [About GA4 custom dimensions and metrics](https://support.google.com/analytics/answer/14240153)
- [Monitor events in DebugView](https://support.google.com/analytics/answer/7201382)
- [GA4 data freshness](https://support.google.com/analytics/answer/11198161)

## Live QA: one consented browser session, no actual inquiry submission

1. In the correct GA4 property, verify its web-stream measurement ID is the same **`G-Q14K9BLGK4`** in `mkdocs.yml`. This is a **measurement ID**, not the property numeric ID.
2. In a clean browser session, visit one real SigGear engineering page and **accept analytics cookies**. Do not infer missing GA4 data from a session that rejected analytics.
3. Open that page with `?debug_mode=1` if needed, then click its **existing** Engineering Review / inquiry link. Open GA4 **Admin → Data display → DebugView** or Realtime to inspect actual events. This is an operator test; no website visit or inbox message is represented as having occurred by the existence of this checklist.
4. Look for `engineering_brief_open_click` at the source page, followed by `inquiry_page_view` on the request form. Check the `inquiry_origin` value is the same corresponding `geo_...` code on both. **Do not submit an online form solely to make the analytics graph move.**
5. Check the event shows no customer drawing, free-text mechanism description, email address, company or motor parameters. The source URL should not include a private query string in the event parameter.
6. Use `?debug_mode=0` to clear the site's session-level debugging preference after verification. GA4 DebugView is a troubleshooting tool, not production traffic reporting.
7. After the custom dimension becomes reportable (Google advises allowing **24–48 hours**), create a GA4 **Exploration**: Rows = `Event name` and `SigGear Inquiry Origin`; Value = `Event count`; filter event name to the events below. Track date and cookie-consent caveats.

## Event meanings — do not convert clicks into sales

| Event | Correct interpretation |
| --- | --- |
| `engineering_brief_open_click` | Link click to the inquiry form, from the page on which the visitor clicked |
| `inquiry_page_view` | Form opened; same-site immediate referrer available or unknown |
| `engineering_brief_prepare_email` | Visitor attempted to open their own email composer; not proof of sending |
| `engineering_brief_online_submit_attempt` | Browser attempted a FormSubmit POST; not proof of mailbox delivery |
| `engineering_brief_provider_return` | Provider redirect back to the site; not proof of SigGear mailbox receipt |
| Actual qualified inquiry | Only a real received message and manual qualification in the sales pipeline |

GA4 may contain **different event counts** from Search Console clicks due to cookie consent, attribution windows, time zones, and other factors. Never divide unrelated GSC impressions by GA4 inquiry counts and call the result an AI conversion rate.

## Account connection prerequisite

The existing Windsor.ai account still needs a **GA4 property selection**. Authorize the correct Google account, grant the Google Analytics permission, and select the GA4 property on Windsor.ai before finishing. This action requires the account owner's own sign-in and authorization. No token or password should be placed in GitHub.

Once connected, query **event name + event count** for the six scenarios and only use `SigGear Inquiry Origin` as a reporting dimension **after GA4 actually exposes it**. If events or custom dimension data are missing, record **not verified**, not zero.

## Completion criteria

- [ ] Correct GA4 property connected to Windsor.ai and verified
- [ ] `inquiry_origin` event-scoped custom dimension exists exactly once in the right property
- [ ] One consented, real browser QA session yields the expected source-page click event and form page-view origin
- [ ] A GA4 report groups engineering inquiry events by the correct six `geo_...` values
- [ ] Pipeline only counts inbox-confirmed contacts as received inquiries; GA4 never claims confirmation

The GitHub build and Node regression tests validate **website code**, not the above external GA4 and inbox conditions.
