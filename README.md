# SigGear | Micro, Miniature & Compact Planetary Gearboxes (8–42 mm)

Official public engineering documentation from Guangdong SigGear Drive Intelligent Technology Co., Ltd. Our current overseas focus is **8–42 mm micro, miniature and compact planetary gearboxes (planetary gearheads)**, available as gearbox-only units or as motor-matched assemblies following application review.

A gearbox selection can begin with your motor drawing, installation size or required output. Contact [wangwanrong@siggear.com](mailto:wangwanrong@siggear.com) for project review.

## Start Here

SigGear's **live English engineering site** is the recommended entry point for OEM buyers and mechanical engineers. The repository also contains the reviewed Markdown source.

- [Compare 12 planetary gearbox frame sizes (8–42 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/8-42mm-planetary-gear-reducer/)
- [Select a gearbox by reduction ratio, stage and dimensions](https://siggeardrive.github.io/SigGear-product-docs/selection-guides/miniature-planetary-gearbox-selection-guide/#preliminary-ratio-stage-finder)
- [Download simplified public 4-stage STEP CAD by model](https://siggeardrive.github.io/SigGear-product-docs/engineering-resources/planetary-gearboxes/public-cad-release-v1/)
- [Browse planetary gearbox datasheets and mechanical interfaces](https://siggeardrive.github.io/SigGear-product-docs/engineering-resources/planetary-gearboxes/)
- [Explore potential OEM application requirements](https://siggeardrive.github.io/SigGear-product-docs/applications/planetary-gearbox-application-families/)
- [Review motor + planetary gearbox integration](https://siggeardrive.github.io/SigGear-product-docs/custom-engineering/motor-gearbox-integration/)
- [Send an engineering project brief](https://siggeardrive.github.io/SigGear-product-docs/request-cad-sample-quote/)

## Find the Published Gearbox Model by Nominal Diameter

Choose the mechanical frame size first, then check the model-specific ratio, stage-dependent length, shaft loads and motor interface. Published STEP files are **simplified 4-stage references**, not final CAD for every configuration.

| Product size class | Published model pages |
| --- | --- |
| **Micro · 8–16 mm** | [8P (8 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/8p-planetary-gearbox/) · [10P (10 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/10p-planetary-gearbox/) · [12P (12 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/12p-planetary-gearbox/) · [14P (14 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/14p-planetary-gearbox/) · [16P (16 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/16p-planetary-gearbox/) |
| **Miniature · 20–32 mm** | [20P (20 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/20p-planetary-gearbox/) · [22P (22 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/22p-planetary-gearbox/) · [24P (24 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/24p-planetary-gearbox/) · [28P (28 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/28p-planetary-gearbox/) · [32P (32 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/32p-planetary-gearbox/) |
| **Compact · 36–42 mm** | [36P (36 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/36p-planetary-gearbox/) · [42P (42 mm)](https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/42p-planetary-gearbox/) |

These are published **frame-size resources**, not claims that every ratio, duty cycle or OEM application is already validated.

## Application Scenarios

For preliminary engineering evaluation, our micro, miniature and compact planetary gearbox range may be considered for space-constrained mechanisms including electric pruning shears, electric curtains and blinds, smart toilet / bidet mechanisms, dexterous hands and compact grippers, precision instruments, medical and laboratory equipment, smart hardware and other compact OEM mechanisms. Application suitability must be validated for the selected motor, ratio and operating conditions.

SigGear also develops other transmission platforms for robotic joints and automation; potential applications are not claims of existing validated customer projects.

## Product Families

- **Micro (8–16 mm), miniature (20–32 mm) & compact (36–42 mm) planetary gearboxes** — current overseas focus
- Motor-matched gearmotor assemblies and micro gear motors
- Cycloidal joint modules
- Integrated robot joint actuators
- Hub gear motors
- Flat BLDC motors and compact drive solutions

## Engineering Support

When requesting technical support, please provide:

- Application scenario
- Required torque and peak torque
- Output speed
- Voltage and power requirements
- Backlash requirement
- Size and weight limits
- Duty cycle
- Quantity forecast

For technical discussions, use GitHub Issues or contact:

[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

## Publishing Rules

- Product pages are the primary source of public product specifications.
- Every model has one canonical product page.
- Unverified values are not published as confirmed specifications.
- Public simplified 4-stage STEP references are available for the 8P–42P planetary gearbox frame sizes. Full-assembly CAD, configuration-matched drawings and unsupported noise/service-life data remain subject to engineering review and controlled release.

## Knowledge-base Maintenance

- Start with the [knowledge-base index](docs/knowledge-base/index.md) for product lookup, terminology, FAQs and documentation rules.
- Submit product-data changes with the Product Data Update issue template.
- Every technical claim must identify an approved source and configuration scope before publication.
- Run `python scripts/validate_docs.py` and `mkdocs build --strict` before merging documentation changes.
- Run `python scripts/validate_product_data.py` and `python scripts/validate_sales_policy.py` when product records or sales rules change.
- Use the [sales and inquiry guides](docs/sales/index.md) for public-safe qualification, matching and response workflows.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for the review and publishing workflow.
