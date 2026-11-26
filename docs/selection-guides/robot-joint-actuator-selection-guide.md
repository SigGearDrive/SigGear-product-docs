---
title: Robot Joint Actuator and Gearbox Selection Guide | Torque and Sizing
description: Compare six SigGear planetary and cycloidal joint modules, then download real model-specific PDF datasheets, available 2D drawings and exact STEP variants. Review torque, speed, duty and control before design-in.
---

# Robot Joint Actuator and Gearbox Selection Guide

**Choose a published SigGear joint module, download the actual engineering files, then verify the complete joint requirement.** These public models are reference platforms for feasibility reviews; they are not automatic matches to any particular humanoid, robotic-arm or exoskeleton joint.

[**All Joint Module Datasheets / 2D / STEP**](../engineering-resources/robot-joint-actuators/quick-downloads.md){ .md-button .md-button--primary }
[**Custom Joint Review — Drawing / STEP**](../request-cad-sample-quote.md?start=drawing_cad&path=joint_actuator){ .md-button }
[**Separate 8–42 mm Gearhead Files**](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md){ .md-button }

## Published Starting Points — Direct PDF / 2D / STEP

<div class="siggear-joint-downloads" markdown="1">

| Model · dimensions · ratio · rated / peak torque · rated speed | Datasheet PDF | 2D engineering reference | Original Full Assembly STEP |
| --- | --- | --- | --- |
| [**SG-6010C**](../products/robot-joint-actuators/sg6010c.md) · Planetary<br>Ø80 × 34.07 mm · 9.67:1<br>6 / 18 N·m · 310 rpm | [**PDF**](../assets/downloads/joint-actuators/SG-6010C_Public_Reference_Datasheet_Rev0.1.pdf) | / | [**STEP**](../assets/downloads/joint-actuators/SG-6010C_Original_Full_Assembly_20261118.step) |
| [**SG-6010D**](../products/robot-joint-actuators/sg6010d.md) · Planetary<br>Ø80 × 58.77 mm · 28.13:1<br>16 / 50 N·m · 100 rpm | [**PDF**](../assets/downloads/joint-actuators/SG-6010D_Public_Reference_Datasheet_Rev0.1.pdf) | [**2D PDF**](../assets/downloads/joint-actuators/SG-6010D_2D_Assembly_Drawing.pdf) | [**STEP**](../assets/downloads/joint-actuators/SG-6010D_Original_Full_Assembly_20261118.step) |
| [**SG-8021**](../products/robot-joint-actuators/sg8021.md) · Planetary<br>Ø100 × 42.6 mm · 9.25:1<br>10 / 30 N·m · 160 rpm | [**PDF**](../assets/downloads/joint-actuators/SG-8021_Public_Reference_Datasheet_Rev0.1.pdf) | / | [**Driver STEP**](../assets/downloads/joint-actuators/SG-8021_Driver_Version_Original_Full_Assembly_20261118.step) |
| [**CPM-78-39**](../products/cycloidal-joint-modules/cpm78-39.md) · Cycloidal<br>Ø78.7 × 35.8 mm · 39:1<br>20 / 52 N·m · 48 rpm | [**PDF**](../assets/downloads/joint-actuators/CPM-78-39_Public_Reference_Datasheet_Rev0.1.pdf) | / | [**STEP**](../assets/downloads/joint-actuators/CPM-78-39_Original_Full_Assembly_20261118.step) |
| [**CPM-80-25**](../products/cycloidal-joint-modules/cpm80-25.md) · Cycloidal<br>Ø80 · 25:1<br>10 / 50 N·m · 120 rpm | [**PDF**](../assets/downloads/joint-actuators/CPM-80-25_Public_Reference_Datasheet_Rev0.1.pdf) | [**No driver · 29.7 mm**](../assets/downloads/joint-actuators/CPM-80-25_2D_No_Driver_29p7mm.pdf) · [**With driver · 41.2 mm**](../assets/downloads/joint-actuators/CPM-80-25_2D_Integrated_Driver_41p2mm.pdf) | [**No driver**](../assets/downloads/joint-actuators/CPM-80-25_Original_Full_Assembly_No_Driver_20261118.step) · [**With driver**](../assets/downloads/joint-actuators/CPM-80-25_Original_Full_Assembly_Integrated_Driver_20261118.step) |
| [**CPM-100-25**](../products/cycloidal-joint-modules/cpm100-25.md) · Cycloidal<br>Ø100 · 25:1<br>25 / 75 N·m · 60 rpm | [**PDF**](../assets/downloads/joint-actuators/CPM-100-25_Public_Reference_Datasheet_Rev0.1.pdf) | [**SG2556D · 48 mm only**](../assets/downloads/joint-actuators/CPM-100-25D_2D_Dual_Encoder_Driver_48mm.pdf) | [**Standard · 29.5 mm**](../assets/downloads/joint-actuators/CPM-100-25_Original_Full_Assembly_No_Driver_20261118.step) · [**Dual encoder + driver · 48 mm**](../assets/downloads/joint-actuators/CPM-100-25D_Dual_Encoder_Driver_Original_Full_Assembly_20261118.step) |

</div>

**Document boundary:** Joint Datasheets are **Public Reference Rev0.1**; released 2D files are engineering references, not controlled production drawings. **SG-8021 STEP is driver-equipped**, CPM-80-25 driver/no-driver models have different thicknesses, and the 48 mm CPM-100-25D drawing must **not** be assigned to the standard 29.5 mm CPM-100-25. CPM-78-39 2D model correspondence is pending. For production, confirm exact configuration, encoder, control, load and drawing revision.

## Robot Joint Reducer Specifications to Compare

| Check | What matters |
| --- | --- |
| **Torque and duty** | Continuous/rated torque vs peak torque, peak duration and repetitions |
| **Output motion** | Speed, acceleration, joint angle, direction reversals and holding |
| **Complete size** | Diameter, thickness, weight, cable / driver / brake space |
| **Loads and precision** | Radial, axial and overturning loads; backlash, stiffness and feedback |
| **Electronics** | Bus voltage, current limit, encoder, driver and verified communication protocol |

A model's listed peak torque must never be treated as a continuous rating. Do not transfer the specifications of one module or driver variant to another.

## Quick Robot Joint Actuator Sizing Workflow

1. Determine the **joint position, mass, link geometry, motion cycle and external loads**.
2. Calculate approximate **gravity + inertia + external-force torque**; separate continuous and short-duration peaks.
3. Shortlist a published **planetary or cycloidal module** using the datasheet and correct STEP variant.
4. Check speed, voltage/current, output bearings, encoder, driver, control, brake, duty and thermal limits.
5. Run a representative **prototype test**; approve the exact configuration before a production commitment.

## Step 1: Define the Joint and Mechanism

Send the joint type (shoulder, elbow, wrist, hip, knee, ankle or other axis), moving mass, payload, link lengths, center-of-gravity distance, angular range and external force directions. The same actuator may face very different conditions at different robot axes.

## Step 2: Estimate Robot Joint Output Torque

### Gravity Torque

For a simplified one-axis screening estimate:

`T_gravity = m × g × r × sin(theta)`

Here `m` is supported mass, `g` gravitational acceleration, `r` the center-of-gravity distance from the joint, and `theta` the mechanism's orientation relative to gravity. Check worst-case posture, not only the neutral position.

### Acceleration Torque

`T_acceleration = J × alpha`

`J` is inertia referred to the joint output; `alpha` is angular acceleration. Include moving links and payload, not just the actuator rotor.

### External-Force Torque

`T_external = F × r`

Use the perpendicular lever arm for external forces.

### Preliminary Total

Include gravity, acceleration, applied forces, friction, and mechanical losses. These are first-pass equations, **not validated torque ratings**; impact, flexibility, multi-axis dynamics and control behavior may require more complete modeling.

## Step 3: Separate Continuous and Peak Torque

**Continuous torque** covers the defined repeated cycle or holding requirement under thermal limits. **Peak torque** is a short-duration event: specify the peak magnitude, duration, recurrence, cooling, supply voltage and driver current limit. Never infer allowable peak duration from the headline number alone.

## Step 4: Define Speed and the Complete Motion Cycle

Provide rated/max output speed, acceleration, travel angle, reversing frequency, holding time and rest intervals.

`P = T × omega` links mechanical power, torque and angular speed **at the same operating point**. Maximum torque and maximum speed are not necessarily available simultaneously.

## Step 5: Establish the Installation Envelope

Confirm full installed diameter/thickness/length, weight, mounting and bearing interfaces, cable bend space, driver board and optional brake—not only the transmission shell.

## Step 6: Review Radial, Axial and Overturning Loads

Define load direction, distance to the output bearing, cantilevered moment and shocks. Output torque alone does not qualify the joint's bearing and housing. External support may be necessary for the completed mechanism.

## Step 7: Define Positioning and Mechanical Behavior

Check backlash, repeatability, stiffness/compliance, backdrivability, resolution and power-off holding. Encoders, bearing clearances, assembly tolerance and controller tuning all affect the completed axis.

## Step 8: Choose a Transmission and Product Architecture

SigGear publishes **planetary joint actuators** (SG-6010C, SG-6010D, SG-8021) and **cycloidal joint modules** (CPM-78-39, CPM-80-25, CPM-100-25). Evaluate the actual configuration; architecture alone is not a performance guarantee.

[**Planetary vs Cycloidal Comparison**](planetary-vs-cycloidal-robot-joint.md){ .md-button }
[**Integrated Joint vs Motor + Gearhead**](integrated-robot-joint-vs-motor-gearhead.md){ .md-button }

## Step 9: Define Encoder, Driver and Communication Requirements

Confirm whether the exact version includes commutation feedback, output position sensing, integrated/external driver, supported control mode and **CAN / RS485 / EtherCAT or other explicitly documented protocol**. **CPM-78-39 standard catalog configuration uses Hall sensors**; an integrated driver or absolute encoder must not be assumed.

[**CAN / Encoder / Driver Selection Guide**](robot-joint-can-encoder-driver-selection.md){ .md-button }

## Step 10: Review Voltage, Current and Power Architecture

Check nominal/min/max bus voltage, continuous/peak current, power supply, wiring/connector limits, regenerative energy and stop behavior. Electrical current limits influence available operating torque.

## Step 11: Evaluate Thermal Conditions and Duty Cycle

Describe enclosure, cooling, ambient temperature, motion/holding cycle and mounting conduction. A sealed joint may perform differently from an open-air bench test; verify with representative loading.

## Step 12: Define Brake, Safety and Power-Off Behavior

For gravity-loaded or safety-relevant joints, review brake/holding need, unintended motion, emergency stop, manual release and overload response. A brake is **not included by assumption**.

## Step 13: Plan Prototype Validation

Validate representative payload, continuous cycles, peaks, joint temperature, external bearing loads, direction changes, encoder and driver behavior, communications, and power-off conditions before design freeze.

## Requirement Checklist

The **shortest useful first message** is: your joint mechanism/drawing, required speed and load (or torque if known), available space, preferred control/voltage and prototype quantity. More detailed information can be confirmed after initial engineering review.

## Smaller Gearboxes for Hands and Auxiliary Mechanisms

For **separate** precision reduction rather than complete integrated joint actuation, compare [SigGear's 12 planetary Gearheads, Ø8–42 mm](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md). These are **not automatically qualified** as primary load-bearing humanoid joints.

## Related Application Guides

[Humanoid](../applications/humanoid-robot-joint-actuators.md) · [Robotic Arm](../applications/robotic-arm-joint-actuators.md) · [Quadruped](../applications/quadruped-robot-joint-gearboxes.md) · [Exoskeleton](../applications/exoskeleton-joint-actuators.md) · [Manufacturing Evidence](../company/manufacturing-and-quality-evidence.md)

## Request a Joint-Actuator Selection Review

**Luffy · Sales Engineer, SigGear** — [luffy@siggear.com](mailto:luffy@siggear.com)

[**Send Joint Requirements / STEP**](../request-cad-sample-quote.md?start=drawing_cad&path=joint_actuator){ .md-button .md-button--primary }
