# GEO / GA4 Traffic Quality Baseline — 2026-11-20

**Purpose:** Distinguish real measured website activity from verified overseas engineering demand and qualified received inquiries. This is an internal operating record, **not** a claim of AI citations, external customer traffic or lead generation.

**Read-only source:** Windsor.ai `googleanalytics4` connector → SigGear Product Documentation, property `547548249`. Read date **2026-11-20**. Observed GA4 reporting window **2026-11-01 through 2026-11-19**, inclusive. The connector is read-only and cannot change GA4 custom definitions or Explorations.

## 1. Headline GA4 readout

| Metric | Observed value | Interpretation |
| --- | ---: | --- |
| Sessions, summed by date | **15** | GA4 recorded sessions, not 15 overseas buyers |
| Page views (`screen_page_views`), summed by date | **57** | Repeated views can belong to a single person |
| Active users, country report | **1** | Reported aggregate unique active user; do not sum per-day users |
| Country, country report | **China** | The only country in this GA4 report; not reliable proof that all site traffic globally came from China |
| Event: `engineering_brief_open_click` | **4** | 3 historical clicks from Nov 16 + 1 Existing Motor test on Nov 19; one historical click was on the form page itself |
| Event: `inquiry_page_view` | **6** | 2 on Nov 5 + 3 on Nov 16 + 1 Existing Motor test on Nov 19 |
| Event: `engineering_brief_online_submit_attempt` | **No row returned** | Do not infer a confirmed submission, zero commercial inquiries or email delivery |
| `customevent_inquiry_origin = geo_existing_motor` | **1 click + 1 form page view on Nov 19** | User-verified internal test, **not** external buyer activity |

### Daily observed activity

| Date | Sessions | Page views |
| --- | ---: | ---: |
| 2026-11-05 | 1 | 6 |
| 2026-11-09 | 2 | 6 |
| 2026-11-16 | 1 | 8 |
| 2026-11-17 | 1 | 1 |
| 2026-11-18 | 5 | 28 |
| 2026-11-19 | 5 | 8 |
| **Sum** | **15** | **57** |

No other date row was returned in the selected window; this does **not** prove there were no consent-denied visitors.

## 2. Acquisition and visitor-quality caution

- Session source/medium breakdown returned `chatgpt.com / ai-assistant` (11 sessions), `siggear.com / referral` (4), and `(not set)` (1). Channel-group output likewise returned `AI Assistant`, `Referral` and `Unassigned` respectively.
- **Data-quality note:** The source/medium breakdown numerically sums to **16**, while summing the daily sessions returns **15**. The tool responses do **not** establish why. Preserve both raw observations, do not silently force reconciliation, and do not use their sum as a market-share denominator.
- The country report returned **China (15 sessions, 1 active user)**. The evidence is **consistent with testing or concentrated internal usage**, especially given the confirmed Nov 19 Existing Motor test. It does **not** verify the identity of every visitor or justify declaring all sessions internal.
- Neither an AI Assistant channel label nor a visit from `chatgpt.com` proves that ChatGPT organically suggested SigGear to a new buyer. A user's own clicks or diagnostic work can also generate such traffic.
- No **independently verified overseas prospect visit, inbox-confirmed inquiry, qualified opportunity, or model-specific AI citation** is established by these GA4 rows alone. This is **not a claim of zero prospects**; it is a claim that current evidence is insufficient.

## 3. Most-viewed paths in current sample (not verified foreign demand)

| Public page path | Page views |
| --- | ---: |
| `/engineering-resources/planetary-gearboxes/public-cad-release-v1/` | 7 |
| `/request-cad-sample-quote/` | 6 |
| `/products/planetary-gearboxes/8p-planetary-gearbox/` | 4 |
| `/engineering-resources/8p/datasheet/` | 3 |
| `/engineering-resources/8p/mechanical-interface/` | 3 |
| `/engineering-resources/motors/` | 3 |
| `/selection-guides/miniature-planetary-gearbox-selection-guide/` | 3 |
| `/custom-engineering/custom-planetary-gearbox/` | 2 |

All paths above are under `/SigGear-product-docs` on the existing GitHub Pages host. **Page views do not prove an independent client's technical evaluation.**

## 4. Data-source availability on 2026-11-20

| Source | Status | Next action |
| --- | --- | --- |
| GA4 through Windsor.ai | **Connected** to property `547548249` | Use read-only `date`, `event_name`, `event_count`, `customevent_inquiry_origin`, `page_path` and source/country fields for recurring comparison |
| GA4 custom event dimension | **Readable** as `customevent_inquiry_origin` | Preserve one event-scoped custom dimension with six known `geo_...` codes |
| GA4 Free Form exploration | Configured by user in GA4 with origin rows, event-name columns, event-count values and inquiry-event filter | Retain the report; avoid reconfiguring for every round. The user still controls its date range and naming |
| Search Console via Windsor.ai | **No selected Search Console account** at time of check | Do not replace the one working GA4 account just to obtain a GSC snapshot. A dated manual export from the verified GitHub Pages Search Console property is an alternative |
| Google indexing / ranking | **Not checked with URL Inspection in this read** | Never infer indexing state from GA4 traffic |
| Inbox / sales pipeline | **Not checked in this read** | Count a qualified inquiry only after a real received request and an identifiable engineering need have been confirmed |

## 5. Weekly operating rule — make this repeatable

**Measure:** Every completed weekly review should separate:
1. **Discovery:** GSC impressions/clicks for exact product, custom-engineering and qualification URLs (only with a verified source and comparable date range).
2. **Engagement:** GA4 sessions and page views for priority engineering pages; channel and country as context, not proof of buyer quality.
3. **Inquiry intent:** `engineering_brief_open_click` → `inquiry_page_view`, segmented by `customevent_inquiry_origin`. Record counts, not false funnel conversion percentages on tiny and non-user-matched samples.
4. **Actual lead:** separate inbox-confirmed engineering inquiries, manually assessed project relevance, and customer follow-up outcome.

**Evidence labels** for every reported observation:
- `observed_analytics`: raw connector data, may include tests.
- `confirmed_internal_test`: user-operated diagnostics (Existing Motor Nov 19).
- `candidate_external`: a distinct, unverified visit that may merit cross-checking; do not call it a prospect.
- `verified_inquiry`: actual message received and confirmed in the sales process.
- `unavailable`: source disconnected or data absent, **not zero**.

**Do not** remove the six public GEO pages, change canonical paths, fabricate robot/customer cases, infer conversions from clicks, or draw an overseas demand conclusion from this current low-volume/test-dominated sample.

## 6. Next operational checkpoint

- Keep the GA4 code and six-page funnel stable; no new content edit follows from these numbers.
- Once real, independently distinguishable visits accumulate, compare source/country/landing pages with inquiry-origin events and **manually confirmed correspondence**.
- Recover Search Console discovery metrics without unnecessarily disconnecting GA4; if the Windsor.ai free limit prevents both, a manual GSC export is sufficient for the next dated review.
- Exclude explicitly confirmed debugging events from **marketing conclusions** without rewriting the original GA4 records or guessing at unknown users' identities.

**Related verification:** [GA4 Inquiry Origin Verification](ga4-inquiry-origin-verification-2026-11-19.md).  
**Related public-search observation:** [P0 Public Retrieval Observation](p0-public-retrieval-observation-2026-11-19.md).  
**GEO five-platform strategy:** [Five-Platform Operating Board](five-platform-operating-board-2026-11-19.md).
