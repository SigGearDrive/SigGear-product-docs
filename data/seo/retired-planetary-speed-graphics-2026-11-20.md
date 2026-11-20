# Retired Legacy Planetary Speed Graphics and Five-Page Freeze — 2026-11-20

## Owner decision

Remove product images that might repeat obsolete or misleading **≤8,000 rpm** speed limits. Do **not** use older promotional specification images as evidence of current motor/gearhead input speed or performance. Refer customers to the **currently downloadable SigGear Datasheet PDFs** and appropriate model-specific engineering drawings. The permitted continuous input speed is **motor- and configuration-dependent**; 12P's independently confirmed value remains in its current official Datasheet. Do not introduce a universal input-speed rating.

After completing this cleanup, **freeze the five existing pages rebuilt in PRs #283–#285**. The freeze is operational and can be lifted only on an explicit owner instruction.

## Cleanup scope: SigGear GitHub product documentation

**Affected sizes:** 8P, 10P, 12P, 14P, 16P, 20P and 22P.

The GitHub repository held a consistent older **five-image promotional / screenshot bundle** per size:

- `-planetary-gearbox-main.webp` (old cover)
- `-planetary-gearbox-structure-and-ratios.webp`
- `-planetary-gearbox-mechanical-details.webp`
- `-planetary-gearbox-motor-compatibility.webp`
- `-planetary-gearbox-dimensions.webp`

**35 legacy images were removed from the current repository branch and publication output.** The cleanup removes the *whole older parameter-artwork family* so it cannot be cited again, including some unused graphics. Not every binary was independently transcribed or proven to contain the exact “≤8,000 rpm” phrase. The safer removal scope was chosen because the user explicitly wants the current Datasheet—not these images—to be the speed/specification reference.

**Authentic photos preserved:** the individual `8p-real-product-evidence.webp` through `22p-real-product-evidence.webp` assets. Newer 24P/28P/32P/36P/42P real product photos and real factory/test evidence remain unchanged.

### Public-page corrections

- **6 model pages (8P–20P):** removed all in-body old parameter diagrams, retired legacy cover-image references, switched main visible photo to real product evidence, and replaced “drawing preview” links with the exact official **2D Drawing PDF**. Where motor voltage/power limits were being sourced from old promotion sheets, substituted a model-specific Datasheet + motor Datasheet review instruction. Preserved the verified top-of-page four-file set: Datasheet PDF, 2D Drawing, Original Full Assembly STEP, Simplified STEP.
- **22P:** already used real product evidence and direct engineering files; removed the five redundant legacy binary images from the repository, with no change to its model page.
- **Home and 8–42 mm series:** switched 10P and 20P thumbnail URLs from old promotional image covers to their existing real product evidence photos.
- **Quality gate:** updated `scripts/validate_site_urls.py` representative photo checks and added `scripts/validate_legacy_image_and_page_freeze.py`, called in both PR verification and production deployment workflows.

**No Datasheet PDF, STEP, controlled drawing, model-specific verified torque data or URL was deleted or modified.** The technical drawing and ratio/torque detail remain available as official source files for each size.

## Five completed pages now frozen

The authoritative list of five GitHub blob hashes is `data/seo/frozen-legacy-pages-2026-11-20.json`. Future PRs are blocked in CI if any frozen file changes without an intentional, explicitly owner-approved manifest update.

| Frozen existing page | Existing published URL |
| --- | --- |
| Motor + Gearbox Integration | `/custom-engineering/motor-gearbox-integration/` |
| Application-to-Gearhead Size Guide | `/applications/planetary-gearbox-application-families/` |
| Robot Joint Selection Guide | `/selection-guides/robot-joint-actuator-selection-guide/` |
| Planetary Engineering Resource Index | `/engineering-resources/planetary-gearboxes/` |
| Miniature Planetary Gearbox Selector | `/selection-guides/miniature-planetary-gearbox-selection-guide/` |

**They are frozen, not unpublished.** Their public URLs, existing canonicals, PDFs, 2D, STEP, and query/anchor links remain live. No post-launch GSC performance claim can be made yet.

## Remaining boundary

This operation covers **GitHub Pages / SigGear-product-docs** only. The commercial `siggear.com` site is hosted separately and may still contain legacy ≤8,000 rpm artwork/text; it was not modified by this GitHub cleanup. A separate CMS-side review is required to claim cross-domain removal.

## Acceptance

- [ ] 35 old binary graphics absent from the branch and published `gh-pages`
- [ ] 7 sizes retain real photo and model-specific Datasheet/2D reference
- [ ] No public source references deleted graphics
- [ ] 5 frozen page Git blob hashes match and are enforced by PR/deploy workflows
- [ ] `Validate Documentation`, `Deploy MkDocs` and final GitHub Pages build succeed

No older marketing image should be reintroduced merely to fill a blank image slot. The correct replacement is **a real product photo plus the current PDF Datasheet / 2D file link**, not an AI-generated specification graphic.
