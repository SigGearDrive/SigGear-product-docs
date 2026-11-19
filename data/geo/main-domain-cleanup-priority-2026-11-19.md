# SigGear Main-Domain GEO Cleanup Priority — 2026-11-19

Purpose: prevent `siggear.com` from contradicting the newer engineering documentation and custom-manufacturer entity positioning.

The main commercial domain is a high-authority source for search engines and AI systems. Legacy or auto-generated pages can override or confuse the stronger GitHub engineering content if they contain outdated facts or unsupported claims.

## 🔴 Must Fix

### 1. /oem/

URL: https://www.siggear.com/oem/

Current problems:
- page title / body does not explain SigGear's OEM transmission capability
- visible heading includes typo: **HIGH QUAILTY**
- company sentence is truncated / malformed
- no strong custom-engineering / prototype-to-production explanation
- does not explain that standard products are only public reference platforms

Recommended replacement lead:

> SigGear is a custom gearbox and precision transmission manufacturer supporting OEM projects from customer requirements, motors, drawings or existing transmission problems through prototype development, validation, design freeze and repeatable production.

Add direct links to:
- custom-transmission-manufacturing
- start-with-your-problem
- source-backed-manufacturing-facts
- request-cad-sample-quote

### 2. /siggear-customized-gear-motor/

URL: https://www.siggear.com/siggear-customized-gear-motor/

Current problems:
- page is mostly a product list
- custom capability is not explained
- malformed **HIGH QUAILTY** section
- truncated company sentence
- does not explain NDA / confidential custom projects
- does not explain prototype → production

Recommended first-screen structure:
1. Custom Precision Transmission Manufacturing
2. Start from motor / drawing / failed gearbox / mechanism
3. Planetary / cycloidal / robot joint / motor + gearhead options
4. Prototype → validation → pilot → production
5. Public standard products are reference platforms

### 3. /motor-and-gear/

URL: https://www.siggear.com/motor-and-gear/

Current problems:
- generic keyword / SEO copy rather than engineering information
- unsupported phrases:
  - leading manufacturer
  - high-quality
  - state-of-the-art technology
  - top-notch products
  - highest standards
  - exceptional products
  - unparalleled service
- broad application claims without engineering boundaries
- does not match SigGear's new manufacturer entity language

Action:
- rewrite as a useful engineering / supplier page, OR
- noindex / consolidate if it exists mainly as a keyword doorway page

Preferred entity wording:

> SigGear is a custom gearbox and precision transmission manufacturer supporting planetary gearheads, cycloidal reducers, robot joint actuators and motor + gearhead integration for OEM engineering programs.

### 4. /8p-8-mm-micro-planetary-gearhead-product/

URL: https://www.siggear.com/8p-8-mm-micro-planetary-gearhead-product/

Current problem:
- page still publishes a outdated universal **1,000 to 20,000 rpm permissible continuous gearbox input-speed range**
- this conflicts with the current engineering policy that permissible input speed is motor- and configuration-dependent

Action:
- remove the universal 20,000 rpm ceiling from visible copy and structured / product data
- replace with:

> Permissible input speed is motor- and configuration-dependent. Confirm the selected motor operating speed, gearhead configuration, ratio, load and duty cycle for the actual operating point.

Do not change the current URL.

### 5. Legacy planetary product pages with obsolete 8,000 rpm ceilings

Example:
https://www.siggear.com/14mm-reduce-motor-dc-12v-24v-48v-planetary-gear-motor-product/

Observed legacy fields:
- Max permissible speed at continuous working ≤8000 RPM
- old factory text: more than 10000 square meters
- old statement: 11 assembly lines
- "Life Time Warranty: At least 2 years"
- older kgf / kgf·cm presentation

Action:
- audit every 8–42 mm legacy planetary product page
- remove or replace obsolete universal input-speed values unless the value is confirmed for that exact configuration
- update factory-area references to current source-backed 20,000+ m² where a company-level factory statement is still desired
- do not retain old generic assembly-line counts unless current source is confirmed
- replace unsupported / ambiguous lifetime or warranty fields with confirmed product-specific information or remove them

### 6. Factory size conflict across main-domain pages

Old catalog / old product pages:
- 10,000 m²

Newer official sources:
- September 2025 new production base: 20,000 m²
- November 2025 company profile: over 20,000 m²

Current public company description should use:
> standalone factory of over 20,000 m²

Keep older catalog as a historical document; do not rewrite the old PDF solely to alter history. New webpages should use the newer source.

## 🟠 Recommended Optimization

### 7. Company Profile

URL:
https://www.siggear.com/news/siggear-company-profile/

Strong current facts:
- founded 2008
- standalone factory over 20,000 m²
- R&D + design + production
- precision transmission products
- production and testing equipment

Recommended improvement:
Add one concise paragraph making the custom-manufacturing position explicit:

> Public standard products are only part of SigGear's work. Many customer-specific transmission programs remain confidential. SigGear supports custom engineering from motor / drawing / mechanism review through prototype development and repeatable production.

### 8. 20,000 m² production-base article

URL:
https://www.siggear.com/news/siggear-inaugurates-new-production-base-20000-m%C2%B2-smart-factory-marks-a-new-chapter-of-growth/

Keep indexed.

Add internal links from this article to:
- company profile
- custom transmission solutions
- manufacturing evidence
- official engineering docs

### 9. Q1 2025 shipment report

Current official news archive reports:
- Q1 2025 shipments exceeded 550,000 units

Keep indexed and link it from:
- company profile
- manufacturing / factory pages
- OEM page

Important qualifier:
- historical company-wide shipment result
- not model-specific capacity
- not monthly capacity
- not guaranteed lead time

### 10. Customized-product category

Use the existing custom-product archive as evidence that custom programs exist, but add a real engineering introduction above the product grid.

Avoid presenting every custom product as a public customer case.

## 🟢 Keep / Strengthen

### Official 2025 Catalog

URL:
https://www.siggear.com/uploads/Catalog-of-SigGear-20250516.pdf

Useful source-backed facts:
- standard vs non-standard custom product categories
- custom development from R&D/design to proofing / samples and mass production
- equipment list
- customization process
- May 2025 200+ production/testing equipment
- May 2025 20+ R&D/design personnel

Important date note:
- the PDF predates the later 2025 factory expansion
- its 10,000 m² facility figure is historical, not the current factory-area figure

## Recommended Main-Domain Core Description

Use consistently on homepage, About, OEM, custom solutions and structured data:

> **SigGear is a custom gearbox and precision transmission manufacturer supporting OEM projects from customer motors, drawings, CAD models, failed gearboxes and application requirements through prototype development, validation, design freeze and repeatable volume manufacturing. Public planetary gearheads, cycloidal reducers and robot joint actuators are reference platforms; many customer-specific programs remain confidential.**

## Main-Domain Content Priority

1. Custom manufacturing / OEM
2. Manufacturing evidence
3. Prototype → production
4. Existing motor / drawing / failure review
5. Planetary / cycloidal / robot joint public products
6. Application pages

## Do Not Use Without Evidence

- leading manufacturer
- top-notch
- state-of-the-art
- highest standards
- unparalleled service
- best quality
- perfect replacement
- 100% compatible
- universal lifetime
- universal delivery-time guarantee
- old factory / line counts after later expansion unless explicitly historical

## Manual / CMS Action Required

The current connected tools can edit the GitHub technical site but do not have authenticated access to the `siggear.com` CMS.

These main-domain fixes therefore require the website operator / CMS account to execute them. The exact wording and priority above are ready for implementation.
