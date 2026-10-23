---
title: Electric Pruning Shears Planetary Gearhead | SigGear OEM Guide
description: "SigGear 8–42 mm planetary gearheads for electric pruning shears. Review cutting torque, 32P/42P options, motor matching, STEP CAD and OEM selection."
---

# Planetary Gearheads for Electric Pruning Shears — OEM Selection

**Electric pruning shears, cordless garden pruners and powered secateurs** need compact transmissions that move a blade against changing cutting resistance. A **precision planetary gearhead (planetary gearbox)** reduces motor speed and transmits torque, but the correct frame size depends on blade geometry, gearbox loading, motor speed and duty cycle—not only branch diameter.

This is a preliminary engineering guide for a **potential OEM application**. It is not a claim that SigGear has delivered, tested or mass-produced a specific pruning-shear project.

[Find a Gearhead for Pruning Shears](../selection-guides/miniature-planetary-gearbox-selection-guide.md?app=electric_pruning_shears#preliminary-ratio-stage-finder){ .md-button .md-button--primary }
[Compare 8–42 mm Planetary Gearheads](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button .md-button--primary }
[Gearhead Ratio and Stage Selection](../selection-guides/miniature-planetary-gearbox-selection-guide.md?app=electric_pruning_shears#preliminary-ratio-stage-finder){ .md-button }
[Start Pruning-Shear Project Brief](../request-cad-sample-quote.md?app=electric_pruning_shears){ .md-button }

## How to Choose a Planetary Gearhead for Electric Pruning Shears

Engineers searching for a **planetary gearbox for electric pruning shears** should distinguish the blade's cutting force from torque required at the gearhead output.

| Decision | What to establish before choosing a SigGear model |
| --- | --- |
| **Blade mechanism** | Pivot-to-cutting-point distance, crank or gear-segment geometry, angle through the cutting stroke and any changing mechanical advantage |
| **Motor operating point** | Loaded motor speed, supply voltage/current limit, start-up behavior and target blade closing time |
| **Torque profile** | No-load movement, typical cuts, short cutting peaks, jam/blocked-blade case and peak duration |
| **Packaging and life** | Maximum diameter, total motor + gearhead length, external bearing support, repeated-cut duty and exposure to debris/moisture |

**First-pass torque calculation.** For a simplified pivoting blade, the cutting-edge moment is approximately `T_blade = F_cut × r_effective`, with force in newtons and effective perpendicular moment arm in metres. **This is blade torque, not necessarily gearhead output torque.** A crank, gear segment, screw or linkage changes the transmission ratio and efficiency throughout the stroke. Calculate or measure the gearhead-shaft load at multiple positions before choosing the gearhead ratio or rating.

**First-pass ratio calculation.** For loaded motor speed `n_motor` and gearhead reduction ratio `i`, the nominal gearhead output speed is `n_output ≈ n_motor / i`. The actual blade closing time must also account for the transmission geometry, acceleration and current limits. Always check the exact stage-specific rated torque and speed rather than inferring them from diameter alone.

### Published Models to Compare for Cordless Pruning Tools

- **[20P 20 mm](../products/planetary-gearboxes/20p-planetary-gearbox.md) / [22P 22 mm](../products/planetary-gearboxes/22p-planetary-gearbox.md)** — compact packaging comparisons where the real mechanism load permits a smaller frame.
- **[32P 32 mm](../products/planetary-gearboxes/32p-planetary-gearbox.md)** — a Miniature-class starting point for more demanding compact tool envelopes.
- **[36P 36 mm](../products/planetary-gearboxes/36p-planetary-gearbox.md) / [42P 42 mm](../products/planetary-gearboxes/42p-planetary-gearbox.md)** — Compact-class comparisons when a larger frame and higher output loads are under evaluation.

These are **preliminary mechanical comparison paths**, not certified or validated pruning-shear product matches. The finished cordless tool needs its own cutting-cycle, jam, thermal, user-safety and service-life validation.

[Download 8P–42P Simplified STEP CAD](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button }
[Find a Gearhead by Loaded Motor Speed](../selection-guides/miniature-planetary-gearbox-selection-guide.md?app=electric_pruning_shears#preliminary-ratio-stage-finder){ .md-button .md-button--primary }

## Begin With Cutting Mechanism Geometry

Blade force at the cutting edge is not automatically the same as gearbox shaft torque. A shear may use a cam, crank, gear segment, linkage or screw between the gearbox and blade pivot.

To estimate gearbox output torque, determine the actual blade and pivot geometry, force application point, transmission efficiency and target motion. Cutting resistance changes through the stroke and by material, so review both a normal cycle and the most demanding expected cutting event.

## Gearhead Only or Motor + Gearhead Assembly?

**Already selected a motor?** SigGear can review a **Gearhead Only** option. Send motor model, loaded operating speed, shaft drawing, mounting-hole pattern, locating pilot, output speed requirement and allowable assembly length.

**Need a complete drive?** SigGear can evaluate a **Motor + Gearhead Assembly** using the voltage/current limits, expected output load and speed, duty cycle and installation envelope.

[Motor + Gearbox Matching Engineering](../custom-engineering/motor-gearbox-integration.md){ .md-button }

## Six Checks for Pruning-Shear Design

| Check | Engineering question |
| --- | --- |
| Load | What is normal movement torque versus the short cutting peak and a stalled blade? |
| Speed | What blade close/return time is needed, and what does that mean at the gearbox output? |
| Dimensions | What gearbox diameter and full gearmotor length fit the housing? |
| Shaft interface | Does the crank or transmission add radial load requiring external support? |
| Electrical and thermal | Can the chosen motor and battery support repeated cutting cycles? |
| Outdoor and user safety | How will the full tool handle debris, moisture, end stops and obstruction? |

A momentary gearbox torque rating must never be treated as a continuous rating, and a planetary reducer should not automatically be treated as a power-off brake.

## Which SigGear Planetary Gearhead Should Be Reviewed?

SigGear publishes 12 nominal gearbox outer diameters from **8 to 42 mm**. Useful frame-size reference pages include [20P](../products/planetary-gearboxes/20p-planetary-gearbox.md), [22P](../products/planetary-gearboxes/22p-planetary-gearbox.md), [32P](../products/planetary-gearboxes/32p-planetary-gearbox.md), [36P](../products/planetary-gearboxes/36p-planetary-gearbox.md) and [42P](../products/planetary-gearboxes/42p-planetary-gearbox.md).

These are **catalog comparisons, not validated pruning-shear recommendations**. The selected model and stage must match the real ratio, continuous and peak torque, length and mechanical interface requirements.

[Compare Published Stage, Ratio and Torque Data](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button .md-button--primary }
[Open Datasheets and Simplified Public CAD](../engineering-resources/planetary-gearboxes/index.md){ .md-button }

The public simplified STEP files represent 4-stage reference geometry for preliminary mechanical packaging. A different stage count or final production design needs configuration-specific controlled CAD.

## Frequently Asked Questions: Electric Pruning-Shear Gearheads

### How much torque does an electric pruning shear gearhead need?

There is no universal output torque for all pruning shears. It depends on the cutting-edge force, blade pivot and linkage geometry, motor speed, expected wood resistance and cut-cycle peaks. Use measured or calculated **gearhead-output torque**, then compare the chosen stage's rated and momentary limits.

### Is a bigger planetary gearhead always better for an electric pruner?

No. A larger diameter may offer a different torque and bearing-load envelope but also changes weight, available housing space and motor matching. Compare [32P](../products/planetary-gearboxes/32p-planetary-gearbox.md), [36P](../products/planetary-gearboxes/36p-planetary-gearbox.md) and [42P](../products/planetary-gearboxes/42p-planetary-gearbox.md) only after the load and installation limits are defined.

### Can I use my existing DC or BLDC motor?

Yes, SigGear can **evaluate** a Gearhead Only option for a customer-selected motor. Provide the shaft drawing, mounting pattern, locating pilot, loaded input rpm and required output torque. Compatibility is confirmed after interface and operating-point review, not from nominal motor diameter alone.

### Is a planetary gearhead self-locking when the blade stops?

Not by default. Blade holding, overload response and user safety may require additional brake, control or mechanical provisions in the finished power tool.

### Is the public STEP file production-ready CAD?

No. Public downloads are **simplified 4-stage reference geometry** for early packaging. A different stage, ratio or motor interface requires configuration-specific drawing and CAD confirmation before production release.

## Request an OEM Engineering Review

For the first review, please send a mechanism drawing or sketch, expected cutting force or output torque, desired blade speed, housing dimensions, motor drawing if selected, power supply and estimated prototype or annual quantity.

Unknown specifications can be discussed after a first mechanical review. Application suitability, environmental performance and safety of the finished tool require customer validation.

**Wanrong Wang — SigGear**  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com?subject=Electric%20Pruning%20Shears%20Gearbox%20Inquiry)

[Email Pruning-Shear Requirements](mailto:wangwanrong@siggear.com?subject=Electric%20Pruning%20Shears%20Planetary%20Gearbox%20Review&body=Application%3A%20Electric%20pruning%20shears%0AExisting%20motor%20or%20complete%20drive%3A%20%0ARequired%20output%20speed%20or%20cycle%20time%3A%20%0ALoad%20or%20torque%20if%20known%3A%20%0AMaximum%20diameter%20and%20length%3A%20%0APrototype%20quantity%20%2F%20annual%20volume%3A%20%0A%0APlease%20attach%20a%20motor%20drawing%20or%20mechanism%20sketch%20if%20available.){ .md-button .md-button--primary }
[Start Pruning-Shear Project Brief](../request-cad-sample-quote.md?app=electric_pruning_shears){ .md-button }

For other outdoor mechanisms, see the [Agriculture and Outdoor Equipment Gear Motor Guide](agriculture-outdoor-equipment-gear-motors.md).
