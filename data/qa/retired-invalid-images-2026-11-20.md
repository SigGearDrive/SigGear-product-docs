# SigGear image asset retirement register — 2026-11-20

This register records **eight source files confirmed undecodable by the repository's complete image decoder**. They were retained in the repository before this cleanup, but the last live audit showed no published page depending on them. Deletion is safer than publishing broken pictures or inventing replacements. Historical filenames are recorded for provenance only; they are **not approved images**.

| Retired historical file | Safe disposition |
| --- | --- |
| `docs/assets/brand/siggear-logo-white.webp` | Retired. Official approved white-background logo original **still needed** for TraceParts / 3Dfindit; external-catalog readiness corrected. |
| `docs/assets/images/evidence/manufacturing/siggear-manufacturing-quality-evidence.webp` | Retired. No authentic usable replacement in this release; do not claim this photo as manufacturing evidence. |
| `docs/assets/images/evidence/planetary/8-42mm-planetary-gearbox-family-real.webp` | Replaced on the 8–42 mm series site by the owner-supplied original `docs/assets/images/products/planetary-gearboxes/siggear-8-42mm-planetary-gearheads-real-lineup.jpg`. |
| `docs/assets/images/evidence/planetary/compact-gearmotor-measurement-caliper.webp` | Retired. New verified caliper/motor-assembly original still needed if this specific evidence is reused. |
| `docs/assets/images/evidence/planetary/compact-gearmotor-size-reference.webp` | Retired. The old YouTube production pack now refers to genuine published lineup imagery rather than this invalid source. |
| `docs/assets/images/evidence/planetary/micro-gearmotor-size-reference.webp` | Retired. The frozen motor-integration page already withholds the photo; historical exception register is retained as a trace, not an active asset. |
| `docs/assets/images/products/planetary-gearboxes/32p/32p-real-product-evidence.webp` | Retired. Real approved model image is `docs/assets/images/products/planetary-gearboxes/32p/32p-real-product-evidence.png`. |
| `docs/assets/images/products/robot-joint-actuators/sg8021/sg8021-robot-joint-actuator-front-angle.webp` | Retired. The SG-8021 page retains its independently decoded *exploded-view* illustration; **do not** mislabel it as a front-angle photograph. A true front-angle original may be supplied later. |

## Rules

1. No file in the list above may reappear in the public docs tree without an explicitly authorized, correctly sourced recovery.
2. All retained `docs/` images must pass **file signature/format, full frame/pixel decoding**, and relevant source link checks.
3. Once GitHub Pages publishes a source revision, a separate **live-site** scan must inspect canonical pages, image references, HTTP responses and full image decoding. A successful source test is not proof of live deployment.
4. Do not substitute a fabricated company logo, machine photo, robot actuator perspective or motor/gearmotor measurement image for an unavailable original.
5. GitHub history preserves the earlier objects for audit; this change removes them from current published assets only.

## Authentic owner-supplied assets — 20 November 2026

The readable, owner-supplied transparent logo and eight standalone original equipment photographs are registered under **new** filenames in `data/qa/owner-supplied-company-media-2026-11-20.json`. The white-background version is an alpha composite of the same unaltered official wordmark. The original eight corrupt historical WebP files remain deleted. Three renders supplied as `80-21` are held in `data/media-review/80-21/` pending exact-model confirmation and are not called SG-8021 photographs.
