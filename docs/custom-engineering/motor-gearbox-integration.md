---
title: Motor + Gearbox Integration Engineering | Custom Gear Motor Matching | SigGear
description: SigGear helps engineers evaluate compact motor + gearbox combinations, including existing customer motors, planetary gearbox matching, output-speed targets, shaft and mounting interfaces, prototypes and production preparation.
---

# Motor + Gearbox Integration Engineering

## Start With the Motor, the Mechanism or the Required Output

A compact drive project does not need to start with a complete motor and gearbox specification.

You may already have a motor that must be kept. You may instead know only the available space, required output speed, load and operating voltage.

SigGear can review the motor and gearbox as one transmission system and identify the mechanical and operating inputs that still need to be confirmed.

Depending on the selected product family and project requirements, the supply scope may be:

- gearbox only
- motor only
- matched motor + gearbox assembly
- an integrated drive or actuator where motor, reducer, sensing and control are reviewed together

[Send Your Motor or Mechanism](mailto:wangwanrong@siggear.com?subject=Motor%20and%20Gearbox%20Integration%20Review){ .md-button .md-button--primary }
[Request Engineering Review](../request-cad-sample-quote.md){ .md-button }

## Path A — I Already Have a Motor

If the motor is already fixed, the first task is to determine whether the gearbox can be matched mechanically and whether the motor operating point is suitable for the required output.

Useful information includes:

- motor drawing or exact motor model
- motor type
- nominal voltage
- rated and peak power, if available
- rated and no-load speed
- shaft diameter and usable shaft length
- shaft flat, key, pinion or other input feature
- motor mounting-hole pattern
- locating pilot diameter
- maximum total assembly length
- required output speed
- required continuous and peak torque, or the load if torque is not yet known
- duty cycle
- expected prototype and production quantity

A motor drawing is often more useful than a long text description because it makes the shaft, pilot and mounting constraints visible immediately.

## Path B — I Need a Complete Motor + Gearbox Solution

If the motor has not yet been selected, start from the output requirement and installation envelope.

Useful starting inputs are:

- application and what needs to move
- required output speed
- continuous and peak torque, load or force if known
- available diameter and total length
- operating voltage or available power supply
- duty cycle and motion pattern
- noise, backlash or positioning requirement where relevant
- shaft and mounting requirements
- encoder, brake, cable or connector requirements where relevant
- prototype quantity and expected production volume

The motor and gearbox should be evaluated together. A high motor speed may reduce required motor torque but can increase reduction-ratio and gearbox input-speed requirements. A different ratio can change output speed, available torque, efficiency and gearbox length.

Final selection therefore requires review of the complete operating point rather than only one parameter.

## If the Gear Ratio Is Unknown

The customer does not need to calculate the final ratio before contacting SigGear.

When motor speed and desired output speed are known, a preliminary ratio can be estimated from:

**preliminary reduction ratio ≈ motor speed / desired output speed**

The final ratio still needs to be checked against:

- available gearbox ratios and stage count
- gearbox input-speed limit
- required output torque
- motor operating point
- gearbox efficiency
- duty cycle
- assembly length
- thermal condition

If the motor speed is also unknown, send the application and output motion requirement first.

## If the Required Torque Is Unknown

A project can start from the mechanism.

Useful information can include:

- load or payload
- arm length or linkage geometry
- wheel diameter
- pulley, belt, screw or rack information
- friction or resistance
- acceleration requirement
- gravity direction
- motion cycle
- a sketch, CAD screenshot or marked-up drawing

From this information, the engineering review can identify what must be calculated, measured or tested before final motor and gearbox selection.

## Mechanical Matching Between Motor and Gearbox

The motor-to-gearbox interface normally needs review of:

- motor shaft diameter
- usable shaft length
- shaft geometry
- gearbox input interface
- mounting-hole pattern
- locating pilot
- concentricity and assembly arrangement
- total axial length
- torque-transfer method
- available housing space

A motor that is suitable electrically may still require a different mechanical interface before it can be used with a gearbox platform.

## Motor Types and Product Families

SigGear's current public micro gear-motor information states that, depending on the selected gearbox and project requirements, engineering review can include:

- brushed DC motors
- brushless DC motors
- stepper motors
- servo motors
- customer-specified motors

Compatibility is not assumed from motor type alone. Input speed, power, shaft interface, duty cycle, thermal conditions and required output performance must be reviewed for the selected gearbox.

[Browse Micro Gear Motors](../products/micro-gear-motors/index.md){ .md-button }
[Browse Planetary Gearboxes](../products/planetary-gearboxes/index.md){ .md-button }

## Existing SigGear Planetary Platforms

For miniature and compact motor + gearbox projects, SigGear publishes planetary gearbox platforms from **8 mm to 42 mm nominal outer diameter**.

The current public series includes:

**8P / 10P / 12P / 14P / 16P / 20P / 22P / 24P / 28P / 32P / 36P / 42P**

Each frame size has its own stage count, ratio, torque, efficiency, length and operating limits. Data from one frame size must not be transferred to another without confirmation.

[Browse the 8-42 mm Planetary Gearbox Series](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md){ .md-button .md-button--primary }

## 32P Motor Integration as a Public Reference

The 32P Engineering Pack currently provides the clearest public example of SigGear's motor-to-gearbox integration workflow.

For the published 32P reference:

| Item | Published reference |
| --- | --- |
| Motor type | DC motor |
| Nominal voltage | 3-36 VDC |
| Motor power | Below 100 W |
| Continuous gearbox input speed | <= 8,000 rpm |

These values belong to the published 32P adapted-motor reference only. They are not universal limits for all SigGear gearboxes or motors.

The public 32P Motor Integration Guide also includes the current motor-side mounting reference and the information required to evaluate a customer's existing motor.

[View the 32P Motor Integration Guide](../engineering-resources/32p/motor-integration.md){ .md-button .md-button--primary }
[View the 32P Gearbox](../products/planetary-gearboxes/32p-planetary-gearbox.md){ .md-button }

## Other Compact Drive Architectures

Not every motorized project should use a miniature planetary gearbox.

Depending on torque, space, joint architecture, load condition and control requirements, SigGear may also review:

- cycloidal transmission
- integrated robot joint actuators
- flat BLDC motor and joint-drive configurations
- other compact transmission arrangements supported by the available engineering platforms

[Custom Cycloidal Transmission Engineering](custom-cycloidal-transmission.md){ .md-button }
[Browse Robot Joint Actuators](../products/robot-joint-actuators/index.md){ .md-button }
[Browse Flat BLDC Motors and Joint Drives](../products/flat-bldc-motors/index.md){ .md-button }

## Typical Project Situations

Motor + gearbox integration may be relevant when:

### A customer motor must be retained

The gearbox must be designed or selected around the existing shaft, pilot, mounting pattern, speed and assembly envelope.

### A standard gear motor is too large

The project needs a shorter, smaller-diameter or differently arranged assembly.

### The output shaft or mounting is application-specific

The customer needs a different shaft, flange, mounting pattern or housing interface.

### The team knows the final motion but not the motor

The output speed, load and space are known, but the motor and reduction ratio are still open.

### Prototype performance needs refinement

The first sample moves, but output speed, torque, noise, temperature, current or mechanical fit needs to be adjusted before design freeze.

## Engineering Development Path

A motor + gearbox project may move through:

**Application / Motor / Drawing**  
→ **Feasibility Review**  
→ **Motor and Gearbox Operating-Point Review**  
→ **Ratio and Frame-Size Evaluation**  
→ **Mechanical Interface Review**  
→ **Configuration Drawing**  
→ **Prototype / Sample**  
→ **Application Test**  
→ **Motor / Ratio / Interface Refinement**  
→ **Design Confirmation**  
→ **Pilot Preparation**  
→ **Production**

The exact path depends on whether the motor, gearbox, mechanism and electrical architecture are already fixed.

## What to Send First

For a first review, send what you already have.

If you already have a motor:

1. motor drawing or model
2. motor speed
3. required output speed
4. load or torque requirement
5. maximum assembly size
6. shaft / mounting constraints

If you need a complete motor + gearbox:

1. application
2. output speed
3. load / torque if known
4. available diameter and length
5. operating voltage
6. duty cycle
7. prototype and expected production quantity

A complete specification is not required before the first discussion.

## Applications

Compact motor + gearbox integration can be relevant in:

- humanoid and service robots
- quadruped robots
- robotic arms
- dexterous hands and grippers
- exoskeletons
- UAV and drone mechanisms
- AGV / AMR
- robotic lawn and outdoor equipment
- electric curtains and smart-home mechanisms
- smart sanitary and household mechanisms
- medical and laboratory equipment
- precision instruments
- compact industrial automation
- other products that require a small motor and reduction transmission

These are application areas where a compact drive may be relevant. They are not statements that SigGear has a public production case in every listed application.

## Confidential Development Projects

Custom motor + gearbox development often involves customer drawings, unreleased products and application-specific interfaces.

Those projects may not be publicly shown.

SigGear therefore uses public gearbox platforms, motor-integration references, CAD, interface data and test resources to help new engineering teams evaluate its capabilities without exposing confidential customer designs.

## Discuss Your Motor + Gearbox Project

Send the motor drawing, mechanism, installation space or output requirement you already have.

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Request Engineering Review](../request-cad-sample-quote.md){ .md-button .md-button--primary }
[Send Your Motor or Mechanism](mailto:wangwanrong@siggear.com?subject=Motor%20and%20Gearbox%20Integration%20Review){ .md-button }
