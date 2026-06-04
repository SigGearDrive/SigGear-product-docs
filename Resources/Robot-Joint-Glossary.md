# Robot Joint Glossary

## Introduction

This glossary explains common terms used in robotic actuators, robotic joints, reducers and motion control systems.

It is intended for:

- Robotics Engineers
- Robot Startups
- University Labs
- System Integrators
- Purchasing Teams

---

# A

## Absolute Encoder

An encoder that provides the exact shaft position immediately after power-up.

Advantages:

- No Homing Required
- Accurate Position Tracking
- Fast Startup

---

# B

## Backlash

The angular movement that occurs before torque is transmitted after reversing direction.

Typical Unit:

- Degree (°)
- Arc Minute (arcmin)

Lower backlash generally improves:

- Position Accuracy
- Motion Quality
- Force Control

---

# C

## CAN Bus

Controller Area Network.

A widely used communication protocol in robotics.

Applications:

- Robot Joint Modules
- Service Robots
- Exoskeletons
- Mobile Robots

---

## Cycloidal Reducer

A transmission mechanism using cycloidal discs and pins.

Advantages:

- Low Backlash
- High Torque Density
- Excellent Shock Resistance

Typical Applications:

- Humanoid Robots
- Quadruped Robots
- Industrial Robots

---

# D

## Duty Cycle

The percentage of time an actuator operates under load.

Example:

```text
60% Duty Cycle
```

means the actuator operates for 60% of the cycle and rests for 40%.

---

# E

## EtherCAT

Ethernet for Control Automation Technology.

A real-time communication protocol used in:

- Industrial Robots
- Humanoid Robots
- CNC Systems

Advantages:

- High Speed
- Precise Synchronization
- Multi-Axis Control

---

## Encoder

A sensor used to measure rotational position and speed.

Types:

- Incremental Encoder
- Absolute Encoder

---

# F

## FOC

Field Oriented Control.

A motor control technique used in modern servo and robotic actuator systems.

Advantages:

- Smooth Motion
- High Efficiency
- Precise Torque Control

---

# G

## Gear Ratio

The ratio between motor speed and output speed.

Example:

```text
10:1
```

means:

- Motor rotates 10 turns
- Output rotates 1 turn

Higher ratios increase torque and reduce speed.

---

# H

## Harmonic Drive

A precision transmission technology using:

- Circular Spline
- Flexspline
- Wave Generator

Advantages:

- Near-Zero Backlash
- High Position Accuracy

---

# I

## Integrated Joint Module

A robotic actuator that combines:

- Reducer
- Motor
- Encoder
- Driver Electronics

into a single package.

Examples:

- SG6010C
- SG8021
- CPM80-25
- CPM100-25

---

# M

## MIT Control

A robot motion control method combining:

- Position
- Velocity
- Torque Feedforward

within a single command structure.

Commonly used in:

- Humanoid Robots
- Quadruped Robots

---

# P

## Peak Torque

The maximum short-duration torque an actuator can provide.

Peak torque should not be used as the continuous operating torque.

---

## Planetary Gearbox

A transmission system consisting of:

- Sun Gear
- Planet Gears
- Ring Gear

Advantages:

- High Efficiency
- Compact Structure
- Lower Cost

---

# R

## Rated Torque

The continuous torque an actuator can provide during normal operation.

When selecting an actuator, rated torque is usually more important than peak torque.

---

## Reducer

A mechanical transmission device used to:

- Reduce Speed
- Increase Torque

Common Types:

- Planetary
- Cycloidal
- Harmonic

---

# S

## Servo Drive

An electronic controller used to regulate motor motion.

Functions:

- Position Control
- Velocity Control
- Torque Control

---

## Shock Load

A sudden force applied to the actuator.

Examples:

- Walking Impact
- Robot Falls
- Sudden Stops

Cycloidal reducers generally perform well under shock loads.

---

# T

## Torque

Rotational force produced by a motor or actuator.

Typical Unit:

```text
Nm
```

(Newton Meter)

---

## Torque Density

Torque output relative to actuator size and weight.

Higher torque density is generally desirable in robotics.

---

# U

## URDF

Unified Robot Description Format.

A standard XML format used in ROS and ROS2.

Applications:

- Robot Modeling
- Simulation
- Motion Planning

---

# W

## Wear

The gradual loss of material or performance caused by repeated operation.

Wear can increase:

- Backlash
- Noise
- Vibration

Proper reducer selection helps reduce wear.

---

# Common Robotics Acronyms

| Acronym | Meaning |
|----------|----------|
| AGV | Automated Guided Vehicle |
| AMR | Autonomous Mobile Robot |
| CAN | Controller Area Network |
| FOC | Field Oriented Control |
| ROS | Robot Operating System |
| ROS2 | Robot Operating System 2 |
| URDF | Unified Robot Description Format |
| MIT | MIT Motion Control Protocol |
| BLDC | Brushless DC Motor |
| SDK | Software Development Kit |

---

## Contact

Website:

https://www.siggear.com

Email:

wwang109@163.com
