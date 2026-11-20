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

**Image integrity QA:** additional current 'real-product-evidence' WebP assets for **8P, 10P, 12P, 14P and 20P** were found corrupt or incomplete (RIFF length mismatch; Pillow could not decode). These **five extra unusable files were also removed** rather than altered, fabricated or presented as valid. The existing **16P and 22P** photos successfully decoded in Pillow and remain published. Later 24P–42P assets and separate factory/test evidence remain unchanged. **Total removed image files: 40.**

### Public-page corrections

- **6 model pages (8P–20P):** removed all in-body old parameter diagrams, retired legacy cover-image references, removed invalid/unverifiable model photo references for 8P, 10P, 12P, 14P and 20P (16P retains an independently decodable genuine image), and replaced “drawing preview” links with the exact official **2D Drawing PDF**. Where motor voltage/power limits were being sourced from old promotion sheets, substituted a model-specific Datasheet + motor Datasheet review instruction. Preserved the verified top-of-page four-file set: Datasheet PDF, 2D Drawing, Original Full Assembly STEP, Simplified STEP.
- **22P:** already used real product evidence and direct engineering files; removed the five redundant legacy binary images from the repository, and kept its independently decodable real product photo; its model page only receives the global Datasheet-priority note.
- **Home and 8–42 mm series:** replaced non-decodable 10P and 20P thumbnails with **confirmed decodable real 16P (Micro)** and **22P (Miniature)** product photos, adjusting linked model labels and image aspect ratios. The 36P Compact real photo is unchanged.
- **Quality gate:** updated `scripts/validate_site_urls.py` representative photo checks and added `scripts/validate_legacy_image_and_page_freeze.py`, called in both PR verification and production deployment workflows.

**Unverified model-image metadata:** 8P, 10P, 12P, 14P and 20P no longer publish their unreadable WebP photos as OG, Twitter or ItemPage images. These model pages are still fully indexed-capable and keep the official files first. The Seo metadata hook emits per-model real evidence images only when an existing verified asset is available.

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

- [ ] 35 old parameter graphics plus 5 unreadable product WebPs absent from the branch and published `gh-pages`
- [ ] 16P and 22P retain validated real photos; other five early sizes have no broken product image and retain Datasheet/2D downloads
- [ ] No public source references deleted graphics
- [ ] 5 frozen page Git blob hashes match and are enforced by PR/deploy workflows
- [ ] `Validate Documentation`, `Deploy MkDocs` and final GitHub Pages build succeed

No older marketing image should be reintroduced merely to fill a blank image slot. The correct replacement is **a real product photo plus the current PDF Datasheet / 2D file link**, not an AI-generated specification graphic.
