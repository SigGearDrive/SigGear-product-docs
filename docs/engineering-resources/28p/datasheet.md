---
title: 28 mm Precision Planetary Gearhead Datasheet (28P) | 1–4 Stages | SigGear
description: Public 28P 28 mm precision planetary gearhead datasheet with 1–4 stage ratios, gearbox lengths, torque, efficiency, backlash, motor-matching data and links to mechanical-interface and CAD resources.
---


# 28 mm Precision Planetary Gearhead Datasheet (28P)

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

**Continuous input-speed range revised:** 2026-10-15 (confirmed by SigGear engineering).  

The SigGear 28P is a 28 mm planetary gearhead platform with one- to four-stage configurations. Performance values below are consolidated from the current canonical product page. Mechanical-interface details are linked to the controlled 2D drawing reference released for this model.

## Key Specifications

| Parameter | Public value |
| --- | ---: |
| Nominal outer diameter | 28 mm |
| Number of stages | 1-4 |
| gearhead length range | 25.6–44.5 mm |
| Reduction ratio range | 3.83:1–759.7:1 |
| Rated allowable torque range | 1961.3–4903.3 mN·m |
| Maximum momentary torque range | 3922.7–9806.6 mN·m |
| Efficiency range | 66–90% |
| Backlash at no load | ≤ 1.2° |
| Continuous permissible input speed | 1,000–20,000 rpm |

Maximum momentary torque is not a continuous working rating.

The current public source does not state operating temperature for 28P; no value is inferred here.

## Stage, Ratio and Performance

| Stages | Gearbox body length L | Available ratios | Rated allowable torque | Maximum momentary torque | Efficiency |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | 25.6 mm | 3.83 / 4.4 / 5.25 | 1961.3 mN·m | 3922.7 mN·m | 90% |
| 2 | 31.9 mm | 14.7 / 16.8 / 19.4 / 20.1 / 23 / 27.7 | 2451.7 mN·m | 4903.3 mN·m | 80% |
| 3 | 38.2 mm | 56.2 / 64.5 / 74.1 / 77 / 85.2 / 88.5 / 101.6 / 105.6 / 121.3 / 144.7 | 3432.3 mN·m | 6864.7 mN·m | 73% |
| 4 | 44.5 mm | 215.2 / 247.2 / 284 / 294.9 / 326.2 / 338.8 / 374.8 / 389.3 / 404.3 / 447.2 / 464.5 / 533.6 / 554.2 / 636.7 / 759.7 | 4903.3 mN·m | 9806.6 mN·m | 66% |

## Load / Shaft Data Boundary

Radial load, axial load and shaft-play limits are not currently published for 28P in the canonical public specification. They are therefore not inferred from another frame size and must be confirmed for the selected configuration if required.

## Motor Matching Reference

- Adapted DC motor nominal voltage: **3–36 VDC**
- Adapted DC motor power: **below 30 W**

These are motor-matching conditions, not electrical ratings of the mechanical gearhead.

## Mechanical Interface and CAD

[View 28P Mechanical Interface v1.0](mechanical-interface.md){ .md-button }

[Download 28P Simplified STEP - 4-Stage Reference](../../assets/downloads/28p/28P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

A simplified public **4-stage STEP reference** is released for early packaging and mechanical Design-In. The full assembly STEP is included in SigGear's public release scope. The original assembly source has been identified; its public download will be activated after binary upload and revision verification.

For final CAD, provide the selected ratio, stage count and motor interface.

[View 2D Drawing & Full Assembly Release Status](../planetary-gearboxes/public-cad-release-v1.md){ .md-button }

## Selection Information Required

Please provide:

- Required output speed or reduction ratio
- Continuous and momentary output torque
- Motor voltage, power and speed
- Motor shaft diameter and length
- Motor mounting-hole pattern and locating pilot
- Output-shaft requirements
- Radial and axial loads
- Duty cycle and ambient temperature
- Backlash, noise and service-life targets
- Prototype and annual quantity

## Related Product

[View 28P Product Page](../../products/planetary-gearboxes/28p-planetary-gearbox.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
