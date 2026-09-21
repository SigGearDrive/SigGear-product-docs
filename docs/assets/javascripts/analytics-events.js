(function () {
  function sendEvent(name, params) {
    if (typeof window.gtag !== "function") return;
    window.gtag("event", name, params || {});
  }

  function pagePath() {
    try {
      return new URL(window.location.href).pathname;
    } catch (e) {
      return window.location.pathname || "";
    }
  }

  var path = pagePath();

  if (path.endsWith("/request-cad-sample-quote/")) {
    sendEvent("inquiry_page_view", { page_path: path });
  }

  if (path.endsWith("/contact/")) {
    sendEvent("contact_page_view", { page_path: path });
  }

  document.addEventListener("click", function (event) {
    var link = event.target && event.target.closest ? event.target.closest("a") : null;
    if (!link) return;

    var href = link.getAttribute("href") || "";
    var label = (link.textContent || "").trim().slice(0, 80);

    if (href.indexOf("mailto:") === 0) {
      sendEvent("email_click", {
        page_path: pagePath(),
        link_text: label
      });
      return;
    }

    if (href.indexOf("request-cad-sample-quote") !== -1) {
      sendEvent("cad_quote_click", {
        page_path: pagePath(),
        link_text: label
      });
      return;
    }

    if (href === "../contact.md" || href === "../../contact.md" || href === "contact.md" ||
        href.endsWith("/contact/") || href.indexOf("/contact/") !== -1) {
      sendEvent("contact_click", {
        page_path: pagePath(),
        link_text: label
      });
    }
  }, true);
})();