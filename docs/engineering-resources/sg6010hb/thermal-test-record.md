---
title: SG-6010HB Thermal Test Record | Stall and 110 rpm Load Conditions | SigGear
description: Source-backed SG-6010HB temperature-rise test record showing measured time from 30°C to 100°C under stall and 110 rpm load conditions at several torque levels.
---

# SG-6010HB Thermal Test Record v1.0

**Status:** Public engineering test record  
**Release date:** 2026-10-09  
**Source:** Internal SG-6010HB temperature-rise test worksheet supplied for engineering documentation

This page publishes only the test values that are clearly identifiable in the source worksheet.

It is **not** a continuous-duty rating, thermal certification, lifetime statement or replacement for application-specific validation.

## What the Source Records

The worksheet contains two test sections:

1. **Stall condition — time from 30°C to 100°C**
2. **110 rpm load condition — time from 30°C to 100°C**

The source does not identify the exact temperature sensor location in the table heading, so this page does not label the 100°C threshold as winding temperature, housing temperature, PCB temperature or another specific measurement point.

## Stall Condition — 30°C to 100°C

| Applied torque | Recorded time to 100°C |
| ---: | ---: |
| 6.0 Nm | 929.68 s |
| 10 Nm | 113.61 s |
| 15 Nm | 10.72 s |
| 20 Nm | 5 s |
| 25 Nm | No time value recorded |
| 30 Nm | No time value recorded |

The source worksheet also contains the note **“Peak 21 Nm”** in this section.

This note is **not used as a published SG-6010HB peak-torque specification** because the worksheet does not define the note sufficiently and the current public product specification remains **18 Nm peak torque**.

## 110 rpm Load Condition — 30°C to 100°C

| Applied torque | Recorded time to 100°C |
| ---: | ---: |
| 6.0 Nm | 578 s |
| 10 Nm | 42 s |
| 15 Nm | 12 s |
| 20 Nm | 5 s |
| 25 Nm | No time value recorded |
| 30 Nm | No time value recorded |

The source labels this section as a **110 rpm load temperature-rise test**.

The **110 rpm** value is a test condition only. It does not replace the currently published SG-6010HB rated output speed of **310 rpm**.

## Source Fields Not Interpreted Publicly

The worksheet contains additional fields that are not sufficiently defined for safe public engineering use:

- A repeated multi-value **temperature** text field without sensor names or point mapping.
- A **dynamometer voltage** column with values 0.25, 0.35, 0.45, 0.55 and 0.65 for several rows, but no unit or calibration definition.

These values are therefore not converted into product specifications, efficiency values, electrical voltage claims or thermal-channel labels.

## Engineering Interpretation Boundary

The test record supports a limited statement:

> Under the recorded test setup, the time for the monitored temperature channel to rise from 30°C to 100°C became much shorter as applied torque increased.

It does **not** by itself establish:

- continuous allowable torque
- continuous duty cycle
- allowable peak duration
- winding temperature limit
- housing temperature limit
- thermal resistance
- thermal time constant
- safe operating area
- lifetime at temperature
- exoskeleton duty-cycle suitability

Those items require a defined test setup, sensor location, cooling condition, ambient condition, mounting condition and acceptance criteria.

## Use for Project Evaluation

For an exoskeleton or compact joint project, use this record as supporting thermal evidence only.

Final selection should still define:

- continuous joint torque
- peak torque and peak duration
- speed profile
- duty cycle
- ambient temperature
- mounting heat path
- enclosure / airflow condition
- driver current limits
- motor and driver temperature protection
- required thermal margin

## Related Resources

[SG-6010HB Product Page](../../products/robot-joint-actuators/sg6010hb.md){ .md-button }
[SG-6010HB Technical Datasheet](datasheet.md){ .md-button }
[SG-6010HB Mechanical Interface](mechanical-interface.md){ .md-button }
[Exoskeleton Joint Selection Guide](../../applications/exoskeleton-joint-actuators.md){ .md-button }

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
