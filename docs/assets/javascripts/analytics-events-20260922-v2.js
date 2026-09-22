(function () {
  var MEASUREMENT_ID = "G-Q14K9BLGK4";
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

  function analyticsReady() {
    return Array.isArray(window.dataLayer);
  }

  function ensureGtag() {
    if (!analyticsReady()) return false;
    if (typeof window.gtag !== "function") {
      window.gtag = function () {
        window.dataLayer.push(arguments);
      };
    }
    return true;
  }

  function configureDebugMode() {
    if (!debugEnabled() || !ensureGtag()) return false;
    window.gtag("config", MEASUREMENT_ID, {
      debug_mode: true,
      send_page_view: false
    });
    return true;
  }

  function sendEvent(name, params) {
    if (!ensureGtag()) return false;
    var eventParams = Object.assign({}, params || {}, {
      send_to: MEASUREMENT_ID
    });
    if (debugEnabled()) {
      eventParams.debug_mode = true;
    }
    window.gtag("event", name, eventParams);
    return true;
  }

  function pagePath() {
    try {
      return new URL(window.location.href).pathname;
    } catch (e) {
      return window.location.pathname || "";
    }
  }

  function debugStatus(message) {
    if (!debugEnabled()) return;
    var box = document.getElementById("siggear-ga4-debug-status");
    if (!box) {
      box = document.createElement("div");
      box.id = "siggear-ga4-debug-status";
      box.style.cssText =
        "position:fixed;left:12px;bottom:12px;z-index:99999;background:#fff;" +
        "border:1px solid #777;padding:8px 10px;font:12px/1.35 monospace;" +
        "max-width:360px;color:#111;box-shadow:0 2px 8px rgba(0,0,0,.2)";
      document.body.appendChild(box);
    }
    box.textContent = message;
  }

  function startDebugDiagnostics() {
    if (!debugEnabled()) return;

    var attempts = 0;
    var timer = window.setInterval(function () {
      attempts += 1;
      var ready = analyticsReady();
      debugStatus(
        "SigGear GA4 debug | dataLayer=" + (ready ? "ready" : "waiting") +
        " | attempt=" + attempts
      );

      if (ready) {
        window.clearInterval(timer);
        configureDebugMode();
        var sent = sendEvent("siggear_debug_ping", {
          page_path: pagePath()
        });
        debugStatus(
          "SigGear GA4 debug | dataLayer=ready | debug=configured | ping=" +
          (sent ? "queued" : "failed")
        );
      } else if (attempts >= 10) {
        window.clearInterval(timer);
        debugStatus("SigGear GA4 debug | dataLayer not available after 5s");
      }
    }, 500);
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

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", startDebugDiagnostics);
  } else {
    startDebugDiagnostics();
  }
})();