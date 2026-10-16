# SigGear Google organic acquisition: official commercial site -> technical documentation

Date: 2026-10-16  
Status: **ACTION NEEDED ON `www.siggear.com`; this GitHub task does not edit that website.**  
Priority: P0 — relevant brand-owned engineering links, not new SEO pages.

## Evidence and scope

- SigGear's English commercial domain **https://www.siggear.com/** already exposes an 8–42 mm planetary gearmotor product category and individually indexed product pages.
- The GitHub engineering property **https://siggeardrive.github.io/SigGear-product-docs/** already exposes the corresponding 8P–42P gearbox-only model records, ratio/stage selector, verified Datasheets and simplified public 4-stage STEP references.
- Search Console for the **GitHub site only**, read through 2026-10-13: **725 impressions and 18 clicks for 2026-09-16 to 2026-10-13** (date dimension). The query `22mm planetary gearbox` appeared with **2 impressions and 0 clicks**, not enough for reliable rank conclusions.
- Search Console for the **commercial siggear.com site is not connected** to the current analytics integration. Do not assert its organic clicks, country share or conversions.
- Page inspection on 2026-10-16 found https://www.siggear.com/12mm-micro-planetary-gear-motor-product/ describing 8,000 rpm as a motor maximum and describing up to 1.5° no-load backlash as `virtually no backlash`. These claims need editorial clarification, not a blind global replacement.

## P0 — Existing category page: add useful links (website manager)

Existing URL, **do not change the slug**:

https://www.siggear.com/8mm-42mm-micro-planetary-gear-motor/

Add a compact `Engineering Resources` block (suggested English copy):

> **Technical Data and Gearbox Selection — 8–42 mm**
>
> Developing a compact OEM mechanism with an existing motor? Explore SigGear's published 8P–42P planetary gearbox frames, compare available reduction ratios, stages and rated allowable torque, and review configuration-specific integration requirements. Our public STEP models are simplified **4-stage references** for initial mechanical packaging; final motor interfaces and stage-specific CAD require engineering review.
>
> **Compare published 8–42 mm planetary gearbox models:**  
> https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/8-42mm-planetary-gear-reducer/
>
> **Use the planetary gearbox selector:**  
> https://siggeardrive.github.io/SigGear-product-docs/selection-guides/miniature-planetary-gearbox-selection-guide/
>
> **View public Datasheets and 4-stage STEP CAD:**  
> https://siggeardrive.github.io/SigGear-product-docs/engineering-resources/planetary-gearboxes/public-cad-release-v1/

Ensure the *motor + gearbox* category remains differentiated from the *mechanical gearbox-only* specifications on GitHub.

## P0 — Existing 12 mm product page: repair parameter presentation (website manager + engineering)

Existing URL, **do not change or redirect**:

https://www.siggear.com/12mm-micro-planetary-gear-motor-product/

The site's legacy sentence refers to a whole **motor** being limited to 8,000 rpm, whereas engineering has confirmed **1,000–20,000 rpm continuous permissible input speed for the 8P–42P mechanical gearbox family**. Do **not** simply rewrite an assembled motor's rated speed as 20,000 rpm.

Suggested corrected English copy:

> **12 mm Planetary Gearbox and Gearmotor Integration**
>
> For the SigGear 12P **gearbox-only** frame, the engineering-confirmed preliminary permissible **continuous gearbox input-speed range is 1,000–20,000 rpm**. This is a gearbox input-speed specification, not a universal rated-speed claim for every motor or assembled gearmotor. The assembled drive operating point must be checked against its selected motor, ratio, load and duty cycle.
>
> Published 12P gearbox backlash at no load is **up to 1.5°**, according to the currently released configuration specifications. The gearbox should **not** be described as having “virtually no backlash.”
>
> **Check 12P ratios, torque and CAD references:**  
> https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/12p-planetary-gearbox/

Also verify the HTML page title displayed in Google: the existing search result has used a generic `China ... Manufacturer and Supplier | Yongkang` template. Replace inaccurate brand/template wording with **SigGear**, but preserve the original product URL and avoid unsupported ranking or absolute quality claims.

## P1 — Homepage company-to-engineering link

Existing homepage: https://www.siggear.com/

Add one natural link within the **Planetary Gear Motor** or technical-resources section:

> **Planetary Gearbox Datasheets, 3D CAD & Engineering Selection**  
> View published 8–42 mm gearbox technical data and design-in resources:
> https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/8-42mm-planetary-gear-reducer/

The homepage need not reproduce 12 full stage tables. This preserves its commercial overview and sends engineering researchers to the appropriate source.

## P1 — GitHub repository metadata

Current GitHub repository description mentions **6–42 mm** despite SigGear's current published and reviewed **8–42 mm** scope. A maintainer with repository settings access may correct the description through **GitHub > Repository > About > Edit > Description** to:

> SigGear 8–42 mm micro, miniature and compact planetary gearboxes: Datasheets, 4-stage STEP CAD, ratio/stage selector and OEM engineering documentation.

Keep existing repo topics, pages, and published history unchanged. GitHub connector currently does not expose the repository-settings write operation.

## Acceptance check

- [ ] Official site category page retains the existing URL and includes the three *working* product/selector/CAD technical links.
- [ ] Official site's 12 mm product page explains mechanical gearbox vs motor-matched gearmotor limits and removes `virtually no backlash` tied to 1.5°.
- [ ] Google-facing site title on that commercial page uses the correct brand and does not claim unverified quality or replacement compatibility.
- [ ] SigGear GitHub About and repository README explicitly link back to the existing official commercial domain; existing public model URL paths remain unchanged.
- [ ] Official site's web administrator confirms publishing and shares the URLs/screenshots of changed sections.
- [ ] If available, connect the **separate commercial site GSC property** for future side-by-side evaluation. Never conflate its data with the GitHub Pages GSC property.
- [ ] Reassess **28 full days after external links are live**, using the same date intervals for planetary impressions, nonbrand queries, model visits, selector visits and actually received engineering inquiries.

No paid link-building, duplicate doorway pages, sitewide forced redirects, artificial backlinks, cross-domain canonicals, or claims of guaranteed Google rankings. Links should be contextual and useful to an engineer.
