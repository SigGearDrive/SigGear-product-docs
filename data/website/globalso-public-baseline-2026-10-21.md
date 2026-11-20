# SigGear commercial website — public pre-change audit (2026-10-21)

**Evidence: live public pages opened 2026-10-21. This is NOT a CMS backup.** The authenticated Globalso product count, admin permissions, database records, image library and import fields remain unverified. No live site change was made.

## Public URLs and observed content

| Page | Observed | Required draft-only change |
| --- | --- | --- |
| [Homepage](https://www.siggear.com/) | Main featured planetary entry says gear **motor** and navigation prioritizes gearmotor/joint products. | Add a discrete `Precision Planetary Gearboxes — 8–42 mm` gateway without displacing original catalog. |
| [8MM–42MM Micro Planetary Gear Motor category](https://www.siggear.com/8mm-42mm-micro-planetary-gear-motor/) | Public list shows nominal 8/10/12/14/16/20/22/24/28/32/36/42 mm **gear motor** titles; pagination exists, and the introduction has visible copy errors (`HIGH QUAILTY`, truncated text). | Preserve motor+gearbox products and URLs. Add user-friendly link to new gearbox-only category and technical selector/CAD. Do not auto-rename existing category. |
| [12MM Micro Planetary Gear Motor](https://www.siggear.com/12mm-micro-planetary-gear-motor-product/) | HTML title still uses **Yongkang** manufacturer template. Paragraph equates 1.5° backlash with `virtually no backlash`, and mentions an **assembled motor** maximum of 8,000 rpm. | Replace incorrect brand template; describe published gearbox backlash as **≤1.5° at no load** and avoid `virtually no backlash`. Do NOT apply the standalone mechanical gearbox 1,000–20,000 rpm limit to a finished motor + gearbox. Preserve URL, approved assembled-motor limits and other unverified facts until product review. |
| [Contact](https://www.siggear.com/contact-us/) | Public phone and contact email route to company's existing general sales contact; may not represent Luffy's preferred DirectIndustry callback route. | In the future check website RFQ ownership/privacy routing before creating new site forms. Do not change team contact identity without approval. |

## Before any Globalso edits

1. Authenticated CMS count and role audit; screenshots of category tree and exact draft/publish controls.
2. Actual account export: products (reported 76), categories, media, SEO and permalinks, plus restore plan. **None obtained in this session**.
3. Genuine Globalso CSV import template download and a test mapping for 8P / 22P / 42P as draft only.
4. Correct category split: **gearbox-only** vs **motor + gearbox**. Product fields with stage-specific torque, ratios and sizes; no invented SKUs.
5. Review public image and downloaded CAD permissions, and validate RFQ-to-email functionality on live approved pages only.
6. No deletion, domain change, or major publication without SigGear explicit sign-off.

**Staging:** [Draft PR #217](https://github.com/SigGearDrive/SigGear-product-docs/pull/217), including the 12-model CSV and first three editorial product page samples.
