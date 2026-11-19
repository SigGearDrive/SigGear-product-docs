---
title: 36 mm Precision Planetary Gearhead Datasheet (36P) | 1–4 Stages | SigGear
description: Public 36P 36 mm precision planetary gearhead datasheet with 1–4 stage ratios, gearbox lengths, torque, efficiency, backlash, motor-matching data and links to mechanical-interface and CAD resources.
---


# 36 mm Precision Planetary Gearhead Datasheet (36P)

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

**Input-speed policy revised:** 2026-11-19. Permissible input speed is evaluated with the selected motor and gearhead configuration.  

The SigGear 36P is a 36 mm planetary gearhead platform with one- to four-stage configurations. Performance values below are consolidated from the current canonical product page. Mechanical-interface details are linked to the controlled 2D drawing reference released for this model.

## Key Specifications

| Parameter | Public value |
| --- | ---: |
| Nominal outer diameter | 36 mm |
| Number of stages | 1-4 |
| gearhead length range | 30.6–61.5 mm |
| Reduction ratio range | 3.66:1–625:1 |
| Rated allowable torque range | 3922.7–9806.6 mN·m |
| Maximum momentary torque range | 7845.3–19613.3 mN·m |
| Efficiency range | 66–90% |
| Backlash at no load | ≤ 1.2° |
| Continuous permissible input speed | Motor/configuration dependent; confirm selected operating point |
| Operating temperature range | −40 to 120 °C |

Maximum momentary torque is not a continuous working rating.

## Stage, Ratio and Performance

| Stages | Gearbox body length L | Available ratios | Rated allowable torque | Maximum momentary torque | Efficiency |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | 30.6 mm | 3.66 / 4.2 / 5.0 | 3922.7 mN·m | 7845.3 mN·m | 90% |
| 2 | 40.9 mm | 13.4 / 15.4 / 17.6 / 18.3 / 21 / 25 | 5884.0 mN·m | 11768.0 mN·m | 80% |
| 3 | 51.2 mm | 49 / 56.3 / 64.6 / 67 / 74.1 / 76.9 / 88.2 / 91.5 / 105 / 125 | 7845.3 mN·m | 15690.6 mN·m | 73% |
| 4 | 61.5 mm | 179.4 / 205.9 / 236.3 / 245.1 / 271.2 / 281.3 / 311.2 / 322.8 / 334.9 / 370.5 / 384.3 / 441 / 457.5 / 525 / 625 | 9806.6 mN·m | 19613.3 mN·m | 66% |

## Published Load / Shaft Limits

| Parameter | Public value |
| --- | ---: |
| Radial load, 10 mm from flange | ≤ 10.0 kgf |
| Shaft axial load | ≤ 6.0 kgf |
| Radial shaft play | ≤ 0.04 mm |
| Thrust shaft play | ≤ 0.3 mm |

Only values currently published for 36P are shown. Do not transfer limits from another frame size.

## Motor Matching Reference

- Adapted DC motor nominal voltage: **3–48 VDC**
- Adapted DC motor power: **below 150 W**

These are motor-matching conditions, not electrical ratings of the mechanical gearhead.

## Mechanical Interface and CAD

[View 36P Mechanical Interface v1.0](mechanical-interface.md){ .md-button }

[Download 36P Simplified STEP - 4-Stage Reference](../../assets/downloads/36p/36P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

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

[View 36P Product Page](../../products/planetary-gearboxes/36p-planetary-gearbox.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
