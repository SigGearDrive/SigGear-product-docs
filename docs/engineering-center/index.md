---
title: SigGear Engineering Center | CAD, STEP, Datasheets and Design-In Resources
description: Use SigGear engineering resources to find a robot actuator or gearbox, evaluate CAD and interfaces, validate samples and prepare a configuration for design-in.
---

# SigGear Engineering Center

This Engineering Center is organized around the way an engineer normally evaluates a transmission product:

**find a relevant model -> check the published data -> evaluate the mechanical interface -> test a sample -> freeze the configuration for design-in.**

Use the public resources below for preliminary engineering evaluation. Robot actuator and gearbox engineering documents include public datasheets, STEP models, mechanical-interface references and measured test data where released. Configuration-specific production drawings, driver/firmware documentation and other controlled files are supplied according to the selected product and project stage.

## Start by What You Need to Do

| Engineering task | Start here |
| --- | --- |
| Need a custom transmission or feasibility review | [Custom Precision Transmission Engineering](../custom-engineering/index.md) |
| Need a custom planetary gearbox around an existing motor, size or interface | [Custom Planetary Gearbox Engineering](../custom-engineering/custom-planetary-gearbox.md) |
| Find a product family or model | [Browse Products](../products/index.md) |
| Find a solution by application | [Browse Applications](../applications/index.md) |
| Estimate robot-joint requirements | [Robot Joint Actuator Selection Guide](../selection-guides/robot-joint-actuator-selection-guide.md) |
| Download released CAD / STEP and interface data | [Public Engineering Packs](#public-engineering-packs) |
| Prepare and run a sample evaluation | [Sample Validation Workflow](sample-validation-workflow.md) |
| Prepare for a design freeze | [Design-In Checklist](design-in-checklist.md) |
| Request configuration-specific files or a sample | [Request CAD, Sample and Quote](../request-cad-sample-quote.md) |

## Public Engineering Packs

The currently released public Engineering Resources are listed below.

| Product | Public selection / design-in resources | Configuration-specific support |
| --- | --- | --- |
| [SG-6010C](../products/robot-joint-actuators/sg6010c.md) | [Datasheet](../engineering-resources/sg6010c/datasheet.md), [simplified STEP](../assets/downloads/sg6010c/SG-6010C_Public_Simplified_STEP_v1.0.step), [mechanical interface](../engineering-resources/sg6010c/mechanical-interface.md) | Quick Start, detailed CAN and firmware-specific integration documents after configuration review |
| [SG-6010HB](../products/robot-joint-actuators/sg6010hb.md) | [Datasheet](../engineering-resources/sg6010hb/datasheet.md), [mechanical interface](../engineering-resources/sg6010hb/mechanical-interface.md) | Controlled production drawing / detailed assembly CAD plus driver, encoder and communication configuration after project review |
| [SG-6010D](../products/robot-joint-actuators/sg6010d.md) | [Datasheet](../engineering-resources/sg6010d/datasheet.md), [mechanical interface](../engineering-resources/sg6010d/mechanical-interface.md) | Configuration-matched CAD, controlled drawing and integration documents after project review |
| [SG-8021](../products/robot-joint-actuators/sg8021.md) | [Datasheet](../engineering-resources/sg8021/datasheet.md), [mechanical interface](../engineering-resources/sg8021/mechanical-interface.md), real exploded product reference on the product page | Configuration-matched CAD, controlled drawing and integration documents after project review |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | [Datasheet](../engineering-resources/cpm80-25/datasheet.md), [STEP - no driver](../assets/downloads/cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step), [STEP - integrated driver](../assets/downloads/cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step), [mechanical interface](../engineering-resources/cpm80-25/mechanical-interface.md), [measured performance data](../engineering-resources/cpm80-25/performance-test-data.md) | Controlled drawing and configuration-specific electrical/control documents as applicable |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | [Datasheet](../engineering-resources/cpm100-25/datasheet.md), [mechanical interface](../engineering-resources/cpm100-25/mechanical-interface.md) | Configuration-matched CAD, controlled drawing and integration documents after project review |
| [8P-42P Planetary Series](../products/planetary-gearboxes/8-42mm-planetary-gear-reducer.md) | [Datasheet + Mechanical Interface Library](../engineering-resources/planetary-gearboxes/index.md) plus [public 4-stage STEP release](../engineering-resources/planetary-gearboxes/public-cad-release-v1.md) covering 8P, 10P, 12P, 14P, 16P, 20P, 22P, 24P, 28P, 32P, 36P and 42P | Controlled production drawing / configuration-specific CAD matched to selected model, stage, ratio and motor interface |
| [32P](../products/planetary-gearboxes/32p-planetary-gearbox.md) | [Datasheet](../engineering-resources/32p/datasheet.md), [4-stage simplified STEP](../assets/downloads/32p/32P_Public_Simplified_STEP_v1.0_4-Stage.step), [mechanical interface](../engineering-resources/32p/mechanical-interface.md), [motor integration guide](../engineering-resources/32p/motor-integration.md) | Controlled configuration-specific CAD/drawing for the selected stage, ratio and motor interface |

The CPM-80-25 performance page contains measured test data. Measured points should not be treated as guaranteed continuous operating ratings without an application-specific review.

## Public vs. Configuration-Specific Documentation

### Public

When a resource has been released publicly, it can be used for early evaluation without waiting for an inquiry response. Depending on the product, this may include:

- approved public specifications
- simplified external-interface STEP models
- mechanical-interface references
- stage / ratio tables
- measured test data where a reviewed public test source exists
- motor-integration guidance

### Configuration-Specific or Request-Only

The following may depend on the exact ordered version and therefore require configuration review:

- controlled production drawings
- exact connector and cable definition
- Quick Start instructions
- detailed CAN / RS485 documentation
- driver- and firmware-specific integration notes
- configuration-specific software examples
- noise, thermal or service-life information where available for the selected configuration

This separation is intentional: public files help an engineer evaluate fit quickly, while controlled files are matched to the actual configuration before final design release.

## Engineering Evaluation Path

### 1. Preliminary Fit

Check:

- torque and speed
- reduction ratio
- outer diameter, length and weight
- allowable external loads
- operating voltage where applicable
- driver / encoder / communication requirements

### 2. Mechanical Fit

Use the released STEP and interface information to check:

- installation envelope
- mounting pattern
- output interface
- motor-side or rear-side interface
- cable / connector clearance where applicable

### 3. Sample Evaluation

Use a defined test sequence instead of starting with a full application load.

[Open the Sample Validation Workflow](sample-validation-workflow.md){ .md-button .md-button--primary }

### 4. Design-In Review

Before freezing a design, confirm the exact product configuration, controlled drawing, interfaces and operating conditions.

[Open the Design-In Checklist](design-in-checklist.md){ .md-button }

## Need a Custom Transmission Rather Than a Catalog Model?

If the project starts from a motor, drawing, installation envelope or mechanism concept rather than a known SigGear model, begin with the Custom Engineering path.

[Open Custom Precision Transmission Engineering](../custom-engineering/index.md){ .md-button .md-button--primary }

## Need a Different Model or Configuration?

If the current public Engineering Packs do not cover the required size, ratio, driver or interface, send the application and the few parameters you already know. A complete specification is not required for the first review.

[Request CAD, Sample and Quote](../request-cad-sample-quote.md){ .md-button .md-button--primary }

**Wanrong Wang**  
International Sales / Sales Engineer, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)
