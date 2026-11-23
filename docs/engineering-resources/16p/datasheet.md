---
title: 16 mm Precision Planetary Gearhead Datasheet (16P) | 1–4 Stages | SigGear
description: Public 16P 16 mm precision planetary gearhead datasheet with 1–4 stage ratios, gearbox lengths, torque, efficiency, backlash, motor-matching data and links to mechanical-interface and CAD resources.
---


# 16 mm Precision Planetary Gearhead Datasheet (16P)

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-06

**Input-speed policy revised:** 2026-11-19. Permissible input speed is evaluated with the selected motor and gearhead configuration.  

The SigGear 16P is a 16 mm planetary gearhead platform with one- to four-stage configurations. Performance values below are consolidated from the current canonical product page. Mechanical-interface details are linked to the controlled 2D drawing reference released for this model.

## Key Specifications

| Parameter | Public value |
| --- | ---: |
| Nominal outer diameter | 16 mm |
| Number of stages | 1-4 |
| gearhead length range | 17.55–30.45 mm |
| Reduction ratio range | 3.85:1–459.5:1 |
| Rated allowable torque range | 392.3–882.6 mN·m |
| Maximum momentary torque range | 784.5–2549.7 mN·m |
| Efficiency range | 66–90% |
| Backlash at no load | ≤ 1.5° |
| Continuous permissible input speed | Motor/configuration dependent; confirm selected operating point |
| Operating temperature range | −40 to 120 °C |

Maximum momentary torque is not a continuous working rating.

## Stage, Ratio and Performance

| Stages | Gearbox body length L | Available ratios | Rated allowable torque | Maximum momentary torque | Efficiency |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | 17.55 mm | 3.85 / 4.33 / 4.63 | 392.3 mN·m | 784.5 mN·m | 90% |
| 2 | 21.85 mm | 14.8 / 16.7 / 17.8 / 18.7 / 20 / 21.4 | 490.3 mN·m | 980.7 mN·m | 80% |
| 3 | 26.15 mm | 57.1 / 64.2 / 68.6 / 72.2 / 77.2 / 81.2 / 82.5 / 86.8 / 92.8 / 99.25 | 686.5 mN·m | 1961.3 mN·m | 73% |
| 4 | 30.45 mm | 219.7 / 247 / 264.2 / 277.9 / 297.2 / 312.55 / 317.75 / 334.2 / 351.5 / 357.4 / 375.9 / 382.1 / 401.9 / 429.8 / 459.5 | 882.6 mN·m | 2549.7 mN·m | 66% |

## Published Load / Shaft Limits

| Parameter | Public value |
| --- | ---: |
| Radial load, 10 mm from flange | ≤ 1.6 kgf |
| Shaft axial load | ≤ 0.5 kgf |
| Radial shaft play | ≤ 0.04 mm |
| Thrust shaft play | ≤ 0.2 mm |

Only values currently published for 16P are shown. Do not transfer limits from another frame size.

## Motor Matching Reference

- Adapted DC motor nominal voltage: **3–36 VDC**
- Adapted DC motor power: **below 10 W**

These are motor-matching conditions, not electrical ratings of the mechanical gearhead.

## Mechanical Interface and CAD

[View 16P Mechanical Interface v1.0](mechanical-interface.md){ .md-button }

[Download 16P Simplified STEP - 4-Stage Reference](../../assets/downloads/16p/16P_Public_Simplified_STEP_v1.0_4-Stage.step){ .md-button .md-button--primary }

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

[View 16P Product Page](../../products/planetary-gearboxes/16p-planetary-gearbox.md){ .md-button }

## Engineering Contact

**Luffy Wang**  
International Sales / Sales Engineer, SigGear  
[luffy@siggear.com](mailto:luffy@siggear.com)
