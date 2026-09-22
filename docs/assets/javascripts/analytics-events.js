(function () {
  var DEBUG_KEY = "siggear_ga4_debug";

  function debugEnabled() {
    try {
      var query = new URLSearchParams(window.location.search);
      if (query.get("debug_mode") === "1") {
        window.sessionStorage.setItem(DEBUG_KEY, "1");
      } else if (query.get("debug_mode") === "0") {
        window.sessionStorage.removeItem(DEBUG_KEY);
      }
      return window.sessionStorage.getItem(DEBUG_KEY) === "1";
    } catch (e) {
      return false;
    }
  }

  function sendEvent(name, params) {
    // MkDocs Material keeps its gtag helper private, but creates dataLayer
    // only after analytics consent has been granted. Reuse that same queue
    // without creating it ourselves, so no event is queued before consent.
    if (!Array.isArray(window.dataLayer)) return;
    function gtag() {
      window.dataLayer.push(arguments);
    }
    var eventParams = params || {};
    if (debugEnabled()) {
      eventParams.debug_mode = true;
    }
    gtag("event", name, eventParams);
  }

  function pagePath() {
    try {
      return new URL(window.location.href).pathname;
    } catch (e) {
      return window.location.pathname || "";
    }
  }

  var path = pagePath();

  if (debugEnabled()) {
    sendEvent("siggear_debug_ping", {
      page_path: path
    });
  }

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
        contact_method: "email"
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