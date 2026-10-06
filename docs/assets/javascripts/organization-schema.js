(function () {
  if (document.querySelector('script[data-siggear-organization-schema]')) return;

  var organization = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Guangdong SigGear Drive Intelligent Technology Co., Ltd.",
    "alternateName": "SigGear",
    "url": "https://siggeardrive.github.io/SigGear-product-docs/",
    "email": "wangwanrong@siggear.com",
    "sameAs": [
      "https://www.youtube.com/@siggeardrive",
      "https://www.instagram.com/luffywan.robotics/",
      "https://www.tiktok.com/@robotactuator.engineer"
    ]
  };

  var script = document.createElement("script");
  script.type = "application/ld+json";
  script.setAttribute("data-siggear-organization-schema", "true");
  script.text = JSON.stringify(organization);
  document.head.appendChild(script);
})();