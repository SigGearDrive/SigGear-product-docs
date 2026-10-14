# Template — SigGear five-channel qualified-acquisition weekly scorecard

**Week:** [Monday YYYY-MM-DD] to [Sunday YYYY-MM-DD]  
**Comparison:** [Previous Monday] to [Previous Sunday]  
**Data checked on:** [date/time with source data cutoff]  
**Owner:** SigGear overseas operations

## Scope and evidence rules

Five channels **only**: GitHub product docs, Google Search, TraceParts, YouTube, DirectIndustry. Treat `data/sales/weekly-attribution-review-sop.yml`, `data/sales/attribution-kpi-schema.yml` and `data/seo/utm-source-taxonomy.yml` as existing sources of truth. A click, video view, CAD link open and confirmed qualified RFQ are not equivalent. Manual internal QA downloads are not inbound customer leads.

## 1. Measured weekly comparison

| Metric | Previous week | This week | Evidence/source |
| --- | ---: | ---: | --- |
| Google Search impressions | pending | pending | GSC; whole site, plus planetary page breakout |
| Google Search clicks | pending | pending | GSC |
| Planetary model page impressions / clicks | pending | pending | GSC; sum **only returned canonical page rows**; document data lag |
| GitHub site sessions and engaged sessions | pending | pending | GA4 `googleanalytics4`; use site-wide and product-page metrics separately |
| YouTube views and minutes watched | pending | pending | YouTube connector; account `51467` |
| YouTube attributable visits to GitHub | pending | pending | GA4 `utm_source=youtube`; not automatically equal to video views |
| TraceParts CAD downloads (external engineers) | pending | pending | TraceParts native Analytics, exclude owner tests, permission-dependent |
| TraceParts attributable GitHub sessions | pending | pending | GA4 `utm_source=traceparts` / referrer |
| DirectIndustry listing views / RFQs | not launched | not launched | Platform exhibitor Analytics only when active |
| Confirmed inquiries / qualified opportunities | pending verification | pending verification | Sales pipeline with reliable acquisition evidence |

## 2. Platform statuses

| Channel | Work completed **during the week** | Exposure / intent signal | Confirmed leads | Next action / waiting party |
| --- | --- | --- | --- | --- |
| GitHub | [actual changes only] | [GA4 engagement / document use] | [evidence or unknown] | [owner] |
| Google Search | [actual changes only] | [GSC queries, model pages, impressions] | [evidence or unknown] | [owner] |
| TraceParts | [actual publishing and CAD changes] | [native download data if accessible] | [evidence or unknown] | [support/account] |
| YouTube | [videos actually published with URL] | [topic-relevant views, retention and traffic] | [evidence or unknown] | [filming/editing owner] |
| DirectIndustry | [actual platform progress] | [listing data only when launched] | [evidence or unknown] | [consultant/account] |

## 3. Source-labeled funnel

`Discovery → Website/Listing Visit → CAD/Specification Review → Engineering Request Received → Qualified Inquiry → Sample/Design-In → Order`

Use counts only for stages with distinct evidence; explicitly label unavailable, zero, pending, operator QA and test traffic. Do not assign last-click website traffic as the primary source when a customer has a more reliable earlier acquisition source.

## 4. Product and content test hypotheses

- Focus four editorial models: 10P, 20P, 32P, 42P; reassess only when search/inquiry data or engineering asset completeness supports changing them.
- Which diameter/model's page search impressions are rising?
- Which YouTube topic produces visits to its exact model/guide URL, not just views?
- Which technical question blocks RFQ (motor shaft, ratio, output speed, duty cycle, mounting)?

## 5. Next-week priority and blockers

1. [Priority one action; owner; asset; due date]
2. [Priority two action; owner; asset; due date]
3. [Platform dependency; response owner; next check]

## Source query recipe (do not confuse sources)

- **GSC:** `searchconsole` account `https://siggeardrive.github.io/SigGear-product-docs/`; query `date,clicks,impressions` for total and `page,clicks,impressions,position` for planetary model paths; account for privacy filtering and latest-data lag.
- **GA4:** `googleanalytics4` property `547548249`; `date,sessions,engaged_sessions`, `session_source_medium,sessions,landing_page`, `event_name,event_count` for actual site interactions; verify `utm_source` + `utm_medium` where present.
- **YouTube:** `youtube` account `51467`; `date,views,estimated_minutes_watched,subscribers_gained` and video-specific `video,video_title,views,estimated_minutes_watched` in same date range.
- **TraceParts:** operator test results are product QA; native CAD download lead totals require TraceParts Analytics permissions. GitHub → TraceParts outbound clicks are not proof TraceParts drove website visits.
- **DirectIndustry:** statuses may be 'submitted / waiting quote / contracted / listed / analytics accessible'. Do not report views or RFQs before native access.
- **Sales:** cross-reference verified new inquiries from actual customer records. Qualified stage must be explicitly confirmed, not inferred from video comments or `mailto:` button clicks.

**Next reference report:** `data/operations/five-channel-weekly-report-2026-10-14.md`.