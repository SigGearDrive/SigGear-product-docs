---
title: CPM-80-25 Datasheet | 10 Nm Rated, 50 Nm Peak Cycloidal Joint Module | SigGear
description: Approved public CPM-80-25 engineering datasheet with performance, dimensions, electrical parameters, configuration comparison and design-in resources.
---

# CPM-80-25 Technical Datasheet v1.0

**Status:** Approved for Public  
**Release date:** 2026-09-28

CPM-80-25 is an integrated cycloidal pinwheel robot joint module available as a motor-and-reducer assembly or with an integrated driver reference configuration.

## Key Performance

| Parameter | Value |
| --- | --- |
| Transmission | Cycloidal pinwheel |
| Reduction ratio | 25:1 |
| Backlash | 5-10 arcmin |
| Rated output torque | 10 Nm |
| Peak output torque | 50 Nm |
| Rated output speed | 120 rpm |
| No-load output speed | 168 rpm |
| Rated motor power | 500 W |
| Operating voltage range | 24-48 VDC |
| Allowable radial force | 500 N |
| Allowable axial force | 500 N |

!!! note
    Peak torque is not a continuous rating. Peak duration depends on current limit, voltage, duty cycle, installation and thermal conditions.

## Configuration Comparison

| Configuration | Max. outer diameter | Axial thickness | Weight |
| --- | ---: | ---: | ---: |
| No integrated driver | 80 mm | 29.7 mm | 430 g |
| Current integrated-driver reference | 80 mm | 41.2 mm | 512 g |

The integrated-driver values above describe the currently released reference outline. Future driver or encoder variants may use a different rear housing, cable routing or total thickness.

## Motor and Electrical Parameters

| Parameter | Value |
| --- | --- |
| Motor KV | 104 rpm/V |
| Thermistor | 10 kOhm B3435 +/-1% |
| Phase inductance | 235 uH |
| Phase current full scale | 33 A |
| Rated bus current | 12 A |
| Static working bus current | 0.08 A |
| Motor structure | 18 slots / 20 poles |
| Phase resistance | 224 uOhm |
| NTC B value | 3435 |
| Back EMF constant | 0.0727 Vs/rad |

## Driver and Control Configuration

The product can be supplied without an integrated driver or with a driver-equipped configuration.

Depending on the confirmed driver and project scope, available functions can include:

- CAN communication
- RS485 communication
- Position control
- Velocity control
- Torque control
- PID closed-loop control

Final protocol details, connector definitions, encoder configuration, current limits and firmware must match the quoted configuration.

## Public Engineering Resources

[Download STEP - No Driver](../../assets/downloads/cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step){ .md-button .md-button--primary }

[Download STEP - Integrated Driver](../../assets/downloads/cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step){ .md-button }

[View Mechanical Interface](mechanical-interface.md){ .md-button }

[View Measured Performance Data](performance-test-data.md){ .md-button }

## Design-In Note

The public STEP files are simplified and intended for packaging, mounting and early mechanical evaluation. Request the controlled drawing before final tooling, tolerance stack-up or production release.

## Engineering Contact

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
