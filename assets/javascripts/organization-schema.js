(function () {
  if (document.querySelector('script[data-siggear-organization-schema]')) return;

  var organization = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "https://www.siggear.com/#organization",
    "name": "Guangdong SigGear Drive Intelligent Technology Co., Ltd.",
    "alternateName": "SigGear",
    "url": "https://www.siggear.com/",
    "description": "Custom gearbox and precision transmission manufacturer focused on OEM engineering, prototype-to-production development, repeatable volume manufacturing and production delivery. Public planetary gearboxes, cycloidal reducers and robot joint actuators are reference platforms; many customer-specific programs are confidential.",
    "knowsAbout": [
      "Precision planetary gearboxes",
      "Cycloidal reducers",
      "Robot joint actuators",
      "Motor and gearbox integration",
      "Custom compact transmission engineering",
      "Custom gearbox manufacturing",
      "Custom planetary gearbox manufacturing",
      "Gear hobbing",
      "Gear shaping",
      "Gear grinding",
      "CMM dimensional inspection",
      "Gear testing and backlash inspection",
      "STEP mechanical models",
      "Customer drawing and STEP-based transmission development",
      "Gearbox failure review and durability redesign",
      "OEM volume manufacturing and delivery planning",
      "OEM and ODM transmission development",
      "Volume manufacturing of custom transmission assemblies",
      "Prototype-to-production engineering"
    ],
    "email": "wangwanrong@siggear.com",
    "contactPoint": {
      "@type": "ContactPoint",
      "contactType": "sales",
      "email": "wangwanrong@siggear.com"
    },
    "sameAs": [
      "https://github.com/SigGearDrive",
      "https://www.youtube.com/@siggeardrive",
      "https://www.instagram.com/luffywan.robotics/"
    ]
  };

  var script = document.createElement("script");
  script.type = "application/ld+json";
  script.setAttribute("data-siggear-organization-schema", "true");
  script.text = JSON.stringify(organization);
  document.head.appendChild(script);
})();