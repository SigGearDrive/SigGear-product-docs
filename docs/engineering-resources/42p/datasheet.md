---
title: 42 mm Precision Planetary Gearhead Datasheet (42P) | 1–4 Stages | SigGear
description: Public 42P 42 mm precision planetary gearhead datasheet with 1–4 stage ratios, gearbox lengths, torque, efficiency, backlash, motor-matching data and links to mechanical-interface and CAD resources.
---


# 42 mm Precision Planetary Gearhead Datasheet (42P)

**Status:** Public engineering evaluation reference  
**Release date:** 2026-10-08

**Input-speed policy revised:** 2026-11-19. Permissible input speed is evaluated with the selected motor and gearhead configuration.  

The SigGear 42P is a 42 mm planetary gearhead platform with one- to four-stage configurations. Performance values below are consolidated from the current canonical product page. Mechanical-interface details are linked to the controlled 2D drawing reference released for this model.

## Key Specifications

| Parameter | Public value |
| --- | ---: |
| Nominal outer diameter | 42 mm |
| Number of stages | 1-4 |
| gearhead length range | 35.6–69.5 mm |
| Reduction ratio range | 3.8:1–660.7:1 |
| Rated allowable torque range | 7845.3–14710.0 mN·m |
| Maximum momentary torque range | 15690.6–29420.0 mN·m |
| Efficiency range | 66–90% |
| Backlash at no load | ≤ 1.2° |
| Continuous permissible input speed | Motor/configuration dependent; confirm selected operating point |
| Operating temperature range | −40 to 120 °C |
| Housing material | Steel |
| Gear material | Steel |
| Output bearing | Ball bearings |

Maximum momentary torque is not a continuous working rating.

## Stage, Ratio and Performance

| Stages | Gearbox body length L | Available ratios | Rated allowable torque | Maximum momentary torque | Efficiency |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | 35.6 mm | 3.8 / 4.3 / 5.1 | 7845.3 mN·m | 15690.6 mN·m | 90% |
| 2 | 46.9 mm | 14.4 / 16.3 / 18.6 / 19.2 / 21.8 / 25.7 | 9806.6 mN·m | 19613.3 mN·m | 80% |
| 3 | 58.2 mm | 54.4 / 61.9 / 70.4 / 72.8 / 80.1 / 82.8 / 94.2 / 97.4 / 110.8 / 130.3 | 11768.0 mN·m | 23536.0 mN·m | 73% |
| 4 | 69.5 mm | 206.4 / 234.6 / 266.8 / 276 / 303.5 / 313.9 / 345 / 357 / 369.2 / 406 / 419.9 / 477.5 / 493.93 / 561.70 / 660.7 | 14710.0 mN·m | 29420.0 mN·m | 66% |

## Published Load / Shaft Limits

| Parameter | Public value |
| --- | ---: |
| Radial load, 10 mm from flange | ≤ 16.0 kgf |
| Shaft axial load | ≤ 8.0 kgf |
| Radial play of shaft | ≤ 0.04 mm |
| Thrust play of shaft | ≤ 0.3 mm |

These values are taken from the current 42P specification sheet. Application suitability still depends on the actual load direction, duty cycle, stage / ratio, motor operating point and installation.

## Motor Matching Reference

- Adapted DC motor nominal voltage: **3–48 VDC**
- Adapted DC motor power: **below 200 W**

These are motor-matching conditions, not electrical ratings of the mechanical gearhead.

## Mechanical Interface and CAD

[View 42P Mechanical Interface v1.0](mechanical-interface.md){ .md-button .md-button--primary }

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

[View 42P Product Page](../../products/planetary-gearboxes/42p-planetary-gearbox.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
