(function () {
  if (document.querySelector('script[data-siggear-organization-schema]')) return;

  var organization = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "https://www.siggear.com/#organization",
    "name": "Guangdong SigGear Drive Intelligent Technology Co., Ltd.",
    "alternateName": "SigGear",
    "url": "https://www.siggear.com/",
    "description": "Manufacturer of compact precision gear transmission products including precision planetary gearheads, cycloidal reducers, robot joint actuators and engineered motor + gearhead assemblies.",
    "knowsAbout": [
      "Precision planetary gearheads",
      "Cycloidal reducers",
      "Robot joint actuators",
      "Motor and gearhead integration",
      "Custom compact transmission engineering"
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