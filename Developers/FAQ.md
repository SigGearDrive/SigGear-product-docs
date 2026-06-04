# FAQ

## Frequently Asked Questions

This document answers common questions from robotics developers, system integrators and startup teams evaluating SigGear robotic joint modules.

---

# General Questions

## What products does SigGear provide?

SigGear specializes in:

- Planetary Gearboxes
- Cycloidal Reducers
- Robotic Joint Modules
- Precision Motion Transmission Systems

Featured products:

- SG6010C
- SG8021
- CPM80-25
- CPM100-25

---

## Are SigGear products suitable for humanoid robots?

Yes.

Recommended products:

| Joint Location | Recommended Product |
|---------------|---------------------|
| Neck | SG6010C |
| Wrist | SG6010C |
| Elbow | CPM80-25 |
| Shoulder | CPM80-25 |
| Hip | CPM100-25 |
| Knee | CPM100-25 |

---

## Are SigGear products suitable for quadruped robots?

Yes.

Recommended products:

- CPM80-25
- SG8021

Applications:

- Hip Joints
- Knee Joints
- Dynamic Leg Systems

---

## Are SigGear products suitable for exoskeletons?

Yes.

Recommended products:

- SG6010C
- CPM80-25

Applications:

- Rehabilitation Systems
- Industrial Assistance Systems
- Wearable Robotics

---

# Communication Questions

## What communication interfaces are supported?

Current support:

- CAN Bus
- USB Type-C
- MIT Motion Control
- ODrive-Compatible Communication

Future support:

- EtherCAT
- TwinCAT
- Codesys

---

## What CAN baud rates are supported?

Typical configurations:

```text
500 kbps
1 Mbps
```

---

## Does SigGear support EtherCAT?

EtherCAT support is currently under development.

Please contact SigGear for roadmap updates.

---

## Does SigGear support ROS2?

ROS2 support is planned.

Future resources include:

- URDF Models
- Gazebo Simulation
- Native ROS2 Drivers

---

# Technical Questions

## What is the difference between rated torque and peak torque?

### Rated Torque

Continuous torque available during normal operation.

### Peak Torque

Maximum short-duration torque.

Always size a robot actuator based on rated torque.

---

## What backlash can be expected?

Typical values:

| Product | Typical Backlash |
|----------|----------|
| SG6010C | 15-20 arcmin |
| SG8021 | 15-20 arcmin |
| CPM80-25 | Low Backlash |
| CPM100-25 | 0.05° |

---

## Which reducer is better for humanoid robots?

For:

- Hip Joints
- Knee Joints
- Dynamic Motion

Cycloidal reducers are generally recommended.

Recommended:

- CPM80-25
- CPM100-25

---

## Which reducer is better for service robots?

Planetary reducers are often preferred.

Recommended:

- SG6010C
- SG8021

---

# Development Questions

## Is SDK documentation available?

Yes.

Available documentation includes:

- CAN Protocol
- MIT Control
- Error Codes
- Python Examples

---

## Is source code available?

The repository currently provides:

- Documentation
- Protocol Information
- Examples

Source code availability depends on project requirements.

---

## Are CAD files available?

Current resources include:

- Product Images
- Dimension Drawings
- Mechanical Drawings

Future releases may include:

- STEP Models
- URDF Models
- Gazebo Resources

---

## Can I customize the product?

Yes.

Available customization options include:

- Gear Ratio
- Mechanical Interface
- Communication Interface
- Product Configuration

---

# Business Questions

## Do you support prototype orders?

Yes.

Prototype and low-volume orders are supported.

---

## Do you support OEM projects?

Yes.

OEM and ODM services are available.

---

## Do you support mass production?

Yes.

SigGear supports:

- Prototype Production
- Pilot Production
- Mass Production

---

## What industries do you serve?

Typical industries include:

- Humanoid Robotics
- Quadruped Robotics
- Exoskeleton Systems
- Service Robotics
- Industrial Automation
- Medical Robotics

---

## How can I contact SigGear?

Website:

https://www.siggear.com

Email:

wwang109@163.com

Location:

Dongguan, Guangdong, China

---

# Need More Help?

If your application requires:

- Product Selection
- Joint Design
- Communication Integration
- Custom Development

please contact SigGear engineering support.

Website:

https://www.siggear.com

Email:

wwang109@163.com
