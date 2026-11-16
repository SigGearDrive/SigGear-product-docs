---
title: 8 mm Precision Planetary Gearhead Datasheet (8P) | 1–4 Stages | SigGear
description: Public 8P 8 mm precision planetary gearhead datasheet with 1–4 stage ratios, gearbox lengths, torque, efficiency, backlash, motor-matching data and links to mechanical-interface and CAD resources.
---


# 8 mm Precision Planetary Gearhead Datasheet (8P)

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

**Continuous input-speed range revised:** 2026-10-15 (confirmed by SigGear engineering).  

The SigGear 8P is a 8 mm planetary gearhead platform with one- to four-stage configurations. Performance values below are consolidated from the current canonical product page. Mechanical-interface details are linked to the controlled 2D drawing reference released for this model.

## Key Specifications

| Parameter | Public value |
| --- | ---: |
| Nominal outer diameter | 8 mm |
| Number of stages | 1-4 |
| gearhead length range | 10.15–18.10 mm |
| Reduction ratio range | 3.8:1–731.16:1 |
| Rated allowable torque range | 19.6–39.2 mN·m |
| Maximum momentary torque range | 39.2–78.5 mN·m |
| Efficiency range | 66–90% |
| Backlash at no load | ≤ 1.5° |
| Continuous permissible input speed | 1,000–20,000 rpm |
| Operating temperature range | −40 to 120 °C |

Maximum momentary torque is not a continuous working rating.

## Stage, Ratio and Performance

| Stages | Gearbox body length L | Available ratios | Rated allowable torque | Maximum momentary torque | Efficiency |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | 10.15 mm | 3.8 / 4.5 / 5.2 | 19.6 mN·m | 39.2 mN·m | 90% |
| 2 | 12.80 mm | 14.4 / 17.1 / 19.8 / 20.3 / 23.4 / 27 | 24.5 mN·m | 49.0 mN·m | 80% |
| 3 | 15.45 mm | 54.9 / 65 / 75.1 / 76.95 / 88.9 / 91.1 / 102.75 / 105.3 / 121.7 / 140.6 | 29.4 mN·m | 58.8 mN·m | 73% |
| 4 | 18.10 mm | 208.5 / 246.9 / 285.3 / 292.4 / 337.9 / 346.3 / 390.46 / 400.14 / 410.1 / 462.4 / 473.85 / 534.3 / 547.56 / 632.74 / 731.16 | 39.2 mN·m | 78.5 mN·m | 66% |

## Published Load / Shaft Limits

| Parameter | Public value |
| --- | ---: |
| Radial load, 10 mm from flange | ≤ 0.4 kgf |
| Shaft axial load | ≤ 0.1 kgf |
| Radial shaft play | ≤ 0.04 mm |
| Thrust shaft play | ≤ 0.15 mm |

Only values currently published for 8P are shown. Do not transfer limits from another frame size.

## Motor Matching Reference

- Adapted DC motor nominal voltage: **3–36 VDC**
- Adapted DC motor power: **below 2.5 W**

These are motor-matching conditions, not electrical ratings of the mechanical gearhead.

## Mechanical Interface and CAD

[View 8P Mechanical Interface v1.0](mechanical-interface.md){ .md-button }

[Download 8P Simplified STEP - 4-Stage Reference](../../assets/downloads/8p/8P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

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

[View 8P Product Page](../../products/planetary-gearboxes/8p-planetary-gearbox.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
