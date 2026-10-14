# SigGear → TraceParts Publisher: 12-model title and inbound-link update request

**Prepared:** 2026-10-14 · **Status:** ready for TraceParts Publisher/account manager review; NOT submitted or published on TraceParts

## What is already working

- **12/12 international English TraceParts model pages** have their user-copied full addresses and unique existing platform Product IDs recorded.
- The SigGear operator confirmed that all 12 models generated and downloaded STEP AP203 CAD on the international English site (2026-10-14).
- SigGear's GitHub product pages and public CAD table already link directly to each of those 12 English TraceParts product pages.
- **The changes requested below concern title/description, engineering-document website links, CAD lead access and RFQ availability. Do not re-upload or regenerate working CAD merely to change a title.**

## Requested platform-only corrections

1. **Product English display names:** align to the canonical SigGear diameter naming below. Where *Miniature* is currently used for 8–16 mm, change it to **Micro**; for 36–42 mm, change to **Compact**; leave 20–32 mm as **Miniature**. The supplied TraceParts URL slug contains *miniature* for every size, but URL slug alone is not proof of the exact current public product title. Confirm the product title in Publisher before editing.
2. **Link each TraceParts model listing to its own GitHub technical page**, not to the homepage. Use the tracked destination column below (including all UTM parameters) where the publisher supports a product website/document URL. Also keep the existing Datasheet and Mechanical Interface links if already published; update to tracked equivalents when appropriate.
3. **Keep existing unique identifiers, CAD, and published URL discoverability:** preserve manufacturer, PartNumber, Product ID, existing geometry, downloadable formats and verified specifications. If TraceParts changes the public URL slug after renaming, request a redirect or verify that the old URLs with Product ID remain functional, then coordinate replacement of GitHub direct links.
4. **RFQ / lead visibility:** ask whether this catalog's plan supports Request For Quotation and access to TraceParts Analytics (model-level downloads, leads, countries, time and contact permissions). Do not assume these features are included.
5. **Validation:** test one English product page for 8P, 24P, 32P and 42P following the publisher update; click the new website link, inspect `utm_source=traceparts`, and check GA4 referral attribution after reporting latency. Recheck 12/12 STEP downloads if the publication workflow unexpectedly alters CAD.

## 12 exact product records and required destination links

| Model | Existing TraceParts Product ID | Desired English Product Name | GitHub product page with TraceParts referral UTM |
| --- | --- | --- | --- |
| 8P | `27-05769189-121068` | SigGear 8P 8 mm Micro Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/8p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=8p_product_page |
| 10P | `27-05769189-121061` | SigGear 10P 10 mm Micro Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/10p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=10p_product_page |
| 12P | `27-05769189-121062` | SigGear 12P 12 mm Micro Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/12p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=12p_product_page |
| 14P | `27-05769189-121058` | SigGear 14P 14 mm Micro Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/14p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=14p_product_page |
| 16P | `27-05769189-121060` | SigGear 16P 16 mm Micro Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/16p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=16p_product_page |
| 20P | `27-05769189-121059` | SigGear 20P 20 mm Miniature Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/20p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=20p_product_page |
| 22P | `27-05769189-121064` | SigGear 22P 22 mm Miniature Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/22p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=22p_product_page |
| 24P | `27-05769189-121065` | SigGear 24P 24 mm Miniature Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/24p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=24p_product_page |
| 28P | `27-05769189-121063` | SigGear 28P 28 mm Miniature Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/28p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=28p_product_page |
| 32P | `27-05769189-121066` | SigGear 32P 32 mm Miniature Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/32p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=32p_product_page |
| 36P | `27-05769189-121067` | SigGear 36P 36 mm Compact Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/36p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=36p_product_page |
| 42P | `27-05769190-121069` | SigGear 42P 42 mm Compact Planetary Gearbox | https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/42p-planetary-gearbox/?utm_source=traceparts&utm_medium=referral&utm_campaign=cad_listing&utm_content=42p_product_page |

**Identifiers:** IDs and PartNumber values are copied from actual operator-supplied product URLs (see [`traceparts-model-urls-2026-10-14.yml`](traceparts-model-urls-2026-10-14.yml)). Do not invent new orderable SKUs; series references are not fully specified ratio/stage/motor configurations.

## Ready-to-send request to the existing TraceParts account manager / Smart-Publishing support

**Subject:** SigGear 12-Model Catalog — English Titles, Technical Links & Lead Access

Hello TraceParts Team,

Our SigGear catalog is already live on TraceParts International. We have confirmed STEP CAD downloads for all 12 planetary gearbox series (8P–42P).

We would like to improve the existing catalog without replacing the working CAD files. Please help us review the attached model-by-model update table.

1. Align the English product titles with our Micro (8–16 mm), Miniature (20–32 mm), and Compact (36–42 mm) product naming.
2. Ensure that every product record offers a link to the corresponding SigGear technical page, using the specified URL and UTM parameters.
3. Preserve the existing product IDs, part numbers, CAD download capability, and product discoverability. Please confirm whether renaming will affect existing public product URLs.
4. Confirm whether we can enable RFQ on these product listings, and how we can access TraceParts Analytics reports for CAD downloads and leads under our current plan.

Please advise whether we can apply these changes through Smart-Publishing or whether we should submit them to your publishing team.

Best regards,
Wanrong Wang
International Sales / Sales Engineer
Guangdong SigGear Drive Intelligent Technology Co., Ltd.
wangwanrong@siggear.com

**Official Smart-Publishing assistance:** https://info.traceparts.com/pcs/publishing-3d-catalogs/easy-straight-way-publish-cad-content/publish-your-cad-models/smart-publishing/traceparts-smart-publishing-help/

## Reporting status

- GA4 property: SigGear Product Documentation (`547548249`)
- Window checked: 2026-09-17 to 2026-10-14 inclusive, by GA4 connector dimensions `session_source_medium`, `session_manual_source`, `session_manual_campaign_name`, `sessions`, `engaged_sessions`, `landing_page`.
- Observed GA4 sessions: **6**, with **0 recorded as TraceParts source**. This is **not** proof the existing backlinks are missing, because visits may not have occurred, the external fields may not yet have been published, or analytics processing may be delayed.
- TraceParts publisher backlink/UTM QA remains **not verified**. No demo/test visit should be described as an organic lead.
- TraceParts Analytics download and named lead data have **not** been accessed; do not substitute GA4 sessions for native CAD-download counts.
