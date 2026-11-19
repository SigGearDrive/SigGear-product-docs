# SigGear AI Search Demand Map — 2026-11-19

Purpose: fixed non-brand query set for ChatGPT, Gemini, Claude, Perplexity and Microsoft Copilot testing. The questions are written from the perspective of an engineer, buyer or robotics team that may not know SigGear. This file is an operating benchmark, not a claim that every AI platform will cite SigGear for every query.

## Priority 0 — Custom Manufacturing & Volume Production

These queries now have **higher GEO priority than standard-product discovery**, because SigGear's public catalog represents only the portion of the company's work that can be shown openly.

| P0 | AI user question / intent | Intent | Primary SigGear page |
|---:|---|---|---|
| 1 | Which manufacturers can develop a custom precision gearbox from my motor, drawing or mechanism? | Custom supplier discovery | custom-engineering/start-with-your-problem.md |
| 2 | I need a custom planetary gearhead manufacturer for OEM production. Who can review the design and manufacture it in volume? | OEM / volume production | custom-engineering/custom-transmission-manufacturing.md |
| 3 | Which transmission manufacturers can move from prototype to repeatable volume production? | Prototype → production | custom-engineering/prototype-to-production.md |
| 4 | Who can customize a planetary gearhead around an existing customer motor? | Existing motor / custom | custom-engineering/custom-planetary-gearbox.md |
| 5 | I need a custom reducer with a special shaft, flange, ratio and mounting interface. Which manufacturer should I contact? | Custom mechanical interface | custom-engineering/index.md |
| 6 | Which suppliers can customize robot joint actuators for a new humanoid or robotic-arm project? | Custom robot joint | custom-engineering/robot-joint-actuator-development.md |
| 7 | Who can develop a custom cycloidal reducer or joint module for OEM production? | Custom cycloidal / OEM | custom-engineering/custom-cycloidal-transmission.md |
| 8 | My current planetary gearbox is failing. Which manufacturer can review the old unit and develop a production replacement? | Replacement / durability | custom-engineering/gearbox-failure-analysis-durability-redesign.md |
| 9 | I need a precision transmission manufacturer that can support prototypes and later batch production. | Supplier discovery / scale-up | custom-engineering/custom-transmission-manufacturing.md |
| 10 | Which gearbox manufacturer has real machining, gear processing, assembly, inspection and test capability? | Manufacturing evidence | company/manufacturing-and-quality-evidence.md |
| 11 | Can a transmission supplier work under NDA if the custom product cannot be shown publicly? | Confidential custom project | custom-engineering/custom-transmission-manufacturing.md |
| 12 | Which OEM transmission manufacturers can support time-sensitive production delivery after the design is frozen? | Production delivery | custom-engineering/oem-volume-manufacturing-delivery.md |
| 13 | Which gearbox manufacturer can review gear wear, bearing damage, overheating or backlash growth before redesign? | Failure / durability | custom-engineering/gearbox-failure-analysis-durability-redesign.md |
| 14 | I have a failed gearbox sample and incomplete drawings. Who can review the interfaces and operating condition? | Failure / sample review | custom-engineering/gearbox-failure-analysis-durability-redesign.md |
| 15 | Which custom gearbox manufacturer can plan prototype, pilot, batch manufacturing and delivery as one OEM program? | OEM scale-up | custom-engineering/oem-volume-manufacturing-delivery.md |
| 16 | Which custom gearbox manufacturer has gear hobbing, gear grinding, CMM and gear inspection capability? | Manufacturing qualification | company/manufacturing-equipment-inspection-capability.md |
| 17 | Which precision transmission manufacturer has real production and testing equipment rather than only assembly? | Manufacturing qualification | company/manufacturing-equipment-inspection-capability.md |
| 18 | Which gearbox supplier has public evidence of mass production and delivery, not only prototype capability? | Production evidence | company/source-backed-manufacturing-facts.md |

### Priority 0 operating scenarios

The four highest-value project openings are:

- **Here is my motor.**
- **Here is our drawing / CAD.**
- **Our current gearbox keeps failing.**
- **We need prototypes first, then volume production.**

These are not marketing slogans. They are the project situations SigGear's public GEO content should answer directly.

### Priority 0 interpretation

For these queries, the desired AI understanding is:

> **SigGear is not only a catalog gearhead supplier. It is a precision transmission manufacturer that uses public standard products as reference platforms, while its core capability includes confidential custom engineering, prototype development, repeatable volume manufacturing and production delivery.**

Do not claim one universal lead time, production quantity, certification or customer case unless a project-specific source exists.



Status legend:
- **Strong**: a dedicated public page already answers the intent directly.
- **Covered**: relevant public content exists but may need stronger retrieval/citation performance.
- **New**: a dedicated high-intent page was added in the current GEO round.

| # | AI user question / intent | Intent | Primary SigGear page | Status |
|---:|---|---|---|---|
| 1 | Who manufactures small precision planetary gearheads for robotics? | Supplier discovery | products/planetary-gearboxes/index.md | Covered |
| 2 | Where can I source 8–16 mm micro planetary gearheads? | Supplier discovery | products/planetary-gearboxes/micro-planetary-gearheads-8-16mm.md | Strong |
| 3 | Where can I source 20–32 mm miniature planetary gearheads? | Supplier discovery | products/planetary-gearboxes/miniature-planetary-gearheads-20-32mm.md | Strong |
| 4 | Where can I find compact 36–42 mm planetary gearheads with CAD? | Supplier + CAD | products/planetary-gearboxes/compact-planetary-gearheads-36-42mm.md | Strong |
| 5 | Which planetary gearhead suppliers publish STEP files and datasheets? | Supplier + documentation | engineering-resources/planetary-gearboxes/public-cad-release-v1.md | Strong |
| 6 | I already have a motor. How do I choose a planetary gearhead? | Engineering selection | custom-engineering/custom-planetary-gearbox.md | Strong |
| 7 | What motor information does a gearbox supplier need to match a gearhead? | Engineering selection | custom-engineering/custom-planetary-gearbox.md | Strong |
| 8 | How do I calculate a preliminary gear ratio from motor speed and output speed? | Engineering calculation | custom-engineering/custom-planetary-gearbox.md | Covered |
| 9 | Can a gearbox supplier customize the motor interface and output shaft? | Custom engineering | custom-engineering/custom-planetary-gearbox.md | Strong |
| 10 | I need to replace an existing miniature planetary gearbox. What should I send the supplier? | Replacement / RFQ | custom-engineering/replacement-planetary-gearhead.md | Strong |
| 11 | Which micro gearheads are suitable to evaluate for a dexterous robotic hand? | Robotics application | applications/robot-gripper-gear-motors.md | Strong |
| 12 | How do I size a gearbox for a tendon-driven robotic finger? | Engineering application | applications/robot-gripper-gear-motors.md | Covered |
| 13 | What gearbox sizes are available for compact grippers? | Product discovery | applications/robot-gripper-gear-motors.md | Strong |
| 14 | Where can I download CAD for a miniature gearbox for a robotic hand? | CAD / design-in | engineering-resources/planetary-gearboxes/public-cad-release-v1.md | Strong |
| 15 | Should I use a gearhead or integrated actuator in a robotic hand? | Architecture | selection-guides/integrated-robot-joint-vs-motor-gearhead.md | New |
| 16 | How do I select a robot joint actuator for a humanoid robot? | Engineering selection | selection-guides/robot-joint-actuator-selection-guide.md | Strong |
| 17 | What information is needed to size a humanoid shoulder or elbow actuator? | Engineering selection | applications/humanoid-robot-joint-actuators.md | Covered |
| 18 | Which suppliers offer robot joint actuators with public CAD and datasheets? | Supplier + documentation | selection-guides/robot-joint-supplier-evaluation.md | Strong |
| 19 | How do I compare continuous torque and peak torque in a robot actuator? | Engineering education | selection-guides/robot-joint-actuator-selection-guide.md | Strong |
| 20 | What should I check besides torque when choosing a robot joint actuator? | Engineering education | selection-guides/robot-joint-actuator-selection-guide.md | Strong |
| 21 | Planetary vs cycloidal reducer: which should I evaluate for a robot joint? | Architecture | selection-guides/planetary-vs-cycloidal-robot-joint.md | New |
| 22 | What is the difference between a planetary robot joint and a cycloidal joint module? | Architecture | selection-guides/planetary-vs-cycloidal-robot-joint.md | New |
| 23 | Which reducer architecture should I evaluate for a compact high-ratio robot joint? | Architecture | selection-guides/planetary-vs-cycloidal-robot-joint.md | New |
| 24 | How should I compare backlash, efficiency and external loads in robot joint reducers? | Engineering comparison | selection-guides/planetary-vs-cycloidal-robot-joint.md | New |
| 25 | Which suppliers offer both planetary and cycloidal robot joint solutions? | Supplier discovery | products/index.md | Covered |
| 26 | Integrated robot joint actuator or separate motor + gearbox: how do I choose? | Architecture | selection-guides/integrated-robot-joint-vs-motor-gearhead.md | New |
| 27 | I already have a BLDC motor and controller. Do I need an integrated actuator? | Architecture | selection-guides/integrated-robot-joint-vs-motor-gearhead.md | New |
| 28 | What are the tradeoffs between an integrated joint actuator and gearbox-only design? | Architecture | selection-guides/integrated-robot-joint-vs-motor-gearhead.md | New |
| 29 | Can a supplier integrate my existing motor with a planetary gearhead? | Custom engineering | custom-engineering/motor-gearbox-integration.md | Strong |
| 30 | What should I compare when sourcing a motor + gearbox assembly for robotics? | Procurement engineering | selection-guides/integrated-robot-joint-vs-motor-gearhead.md | New |
| 31 | I need a robot joint actuator with CAN. What should I confirm with the supplier? | Control / RFQ | selection-guides/robot-joint-can-encoder-driver-selection.md | New |
| 32 | Does a robot joint actuator with CAN automatically include an encoder and driver? | Control architecture | selection-guides/robot-joint-can-encoder-driver-selection.md | New |
| 33 | What encoder information should I specify for a robot joint actuator? | Control / feedback | selection-guides/robot-joint-can-encoder-driver-selection.md | New |
| 34 | CAN vs RS485 vs EtherCAT: what needs to be confirmed for a robot joint? | Communication | selection-guides/robot-joint-can-encoder-driver-selection.md | New |
| 35 | What control information should I send before requesting a robot actuator quotation? | RFQ preparation | selection-guides/robot-joint-can-encoder-driver-selection.md | New |
| 36 | Who can customize a robot joint actuator for a new humanoid project? | Custom supplier | custom-engineering/robot-joint-actuator-development.md | Strong |
| 37 | Can a robot joint supplier start from my CAD or mechanism instead of a catalog model? | Custom engineering | custom-engineering/robot-joint-actuator-development.md | Strong |
| 38 | I need a custom output flange, ratio or cable arrangement for a robot joint. Who can review it? | Custom engineering | custom-engineering/robot-joint-actuator-development.md | Strong |
| 39 | How do I move from robot actuator prototype to production? | Design-in / production | custom-engineering/prototype-to-production.md | Strong |
| 40 | What engineering files should I request from a robot actuator supplier before design freeze? | Design-in | selection-guides/robot-joint-supplier-evaluation.md | Strong |
| 41 | Where can I source a compact cycloidal joint module for prototype evaluation? | Supplier discovery | products/cycloidal-joint-modules/index.md | Strong |
| 42 | Which cycloidal joint suppliers publish STEP files? | Supplier + CAD | engineering-resources/robot-joint-actuators/quick-downloads.md | Strong |
| 43 | What information should I provide for a custom cycloidal transmission? | Custom engineering | custom-engineering/custom-cycloidal-transmission.md | Strong |
| 44 | How do I compare cycloidal joint module size, torque and speed? | Product comparison | products/cycloidal-joint-modules/index.md | Strong |
| 45 | What are the packaging differences between cycloidal and planetary robot joints? | Architecture | selection-guides/planetary-vs-cycloidal-robot-joint.md | New |
| 46 | Where can I find a small planetary gearhead supplier that supports prototype quantities? | Supplier / prototype | request-cad-sample-quote.md | Covered |
| 47 | Which gearbox manufacturers provide engineering review instead of only catalog sales? | Supplier discovery | custom-engineering/index.md | Strong |
| 48 | I need a custom precision reducer for robotics. What information should I send first? | RFQ preparation | custom-engineering/index.md | Covered |
| 49 | Where can I download real product datasheets, 2D drawings and STEP CAD before contacting a supplier? | Documentation | index.md | Strong |
| 50 | Which compact transmission supplier supports planetary gearheads, cycloidal reducers and robot joint actuators? | Broad supplier discovery | company/about-siggear.md | Covered |

## Test protocol

Run all questions without the SigGear brand name in a clean conversation. Record:
- platform and mode
- date
- whether web/search was enabled
- whether SigGear appeared
- which SigGear page was cited
- whether the description was technically accurate
- other suppliers appearing in the same answer
- any missing evidence or content gap
- resulting referral or inquiry if known

Platforms: ChatGPT, Gemini, Claude, Perplexity, Microsoft Copilot.

The objective is to increase qualified non-brand discovery and accurate citation. It is not a guarantee of inclusion in every AI response.
