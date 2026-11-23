---
title: 14 mm Precision Planetary Gearhead Datasheet (14P) | 1–4 Stages | SigGear
description: Public 14P 14 mm precision planetary gearhead datasheet with 1–4 stage ratios, gearbox lengths, torque, efficiency, backlash, motor-matching data and links to mechanical-interface and CAD resources.
---


# 14 mm Precision Planetary Gearhead Datasheet (14P)

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

**Input-speed policy revised:** 2026-11-19. Permissible input speed is evaluated with the selected motor and gearhead configuration.  

The SigGear 14P is a 14 mm planetary gearhead platform with one- to four-stage configurations. Performance values below are consolidated from the current canonical product page. Mechanical-interface details are linked to the controlled 2D drawing reference released for this model.

## Key Specifications

| Parameter | Public value |
| --- | ---: |
| Nominal outer diameter | 14 mm |
| Number of stages | 1-4 |
| gearhead length range | 15.2–26.6 mm |
| Reduction ratio range | 3.75:1–443.3:1 |
| Rated allowable torque range | 343.2–588.4 mN·m |
| Maximum momentary torque range | 686.5–1176.8 mN·m |
| Efficiency range | 66–90% |
| Backlash at no load | ≤ 1.5° |
| Continuous permissible input speed | Motor/configuration dependent; confirm selected operating point |
| Operating temperature range | −40 to 120 °C |

Maximum momentary torque is not a continuous working rating.

## Stage, Ratio and Performance

| Stages | Gearbox body length L | Available ratios | Rated allowable torque | Maximum momentary torque | Efficiency |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | 15.2 mm | 3.75 / 4.38 / 4.66 | 343.2 mN·m | 686.5 mN·m | 90% |
| 2 | 19.0 mm | 14 / 16.4 / 17.5 / 19.2 / 20.4 / 21.7 | 392.3 mN·m | 784.5 mN·m | 80% |
| 3 | 22.8 mm | 52.7 / 61.6 / 65.5 / 71.9 / 76.5 / 81.4 / 84 / 89.4 / 95.1 / 101.2 | 490.3 mN·m | 980.7 mN·m | 73% |
| 4 | 26.6 mm | 197.75 / 231 / 245.74 / 269.8 / 287 / 305.4 / 315.1 / 335.25 / 356.7 / 368 / 379.5 / 391.6 / 416.6 / 443.3 | 588.4 mN·m | 1176.8 mN·m | 66% |

## Published Load / Shaft Limits

| Parameter | Public value |
| --- | ---: |
| Radial load, 10 mm from flange | ≤ 0.8 kgf |
| Shaft axial load | ≤ 0.25 kgf |
| Radial shaft play | ≤ 0.04 mm |
| Thrust shaft play | ≤ 0.2 mm |

Only values currently published for 14P are shown. Do not transfer limits from another frame size.

## Motor Matching Reference

- Adapted DC motor nominal voltage: **3–36 VDC**
- Adapted DC motor power: **below 5 W**

These are motor-matching conditions, not electrical ratings of the mechanical gearhead.

## Mechanical Interface and CAD

[View 14P Mechanical Interface v1.0](mechanical-interface.md){ .md-button }

[Download 14P Simplified STEP - 4-Stage Reference](../../assets/downloads/14p/14P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

[Download 14P Full Assembly STEP](../../assets/downloads/14p/14P_Full_Assembly.step){ .md-button }

A simplified public **4-stage STEP reference** is released for early packaging and mechanical Design-In. The full assembly STEP for 14P is now publicly available. It is the original Creo assembly export supplied for this release. The simplified STEP remains a separate 4-stage reference model for preliminary packaging.

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

[View 14P Product Page](../../products/planetary-gearboxes/14p-planetary-gearbox.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[luffy@siggear.com](mailto:luffy@siggear.com)
