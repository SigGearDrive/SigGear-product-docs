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

  function emailIntent(href) {
    var intent = {
      inquiry_type: "general_email",
      inquiry_model: "not_specified",
      inquiry_application: "not_specified",
      email_subject: ""
    };

    try {
      var emailUrl = new URL(href, window.location.href);
      var subject = (emailUrl.searchParams.get("subject") || "").trim();
      var lower = subject.toLowerCase();
      intent.email_subject = subject.slice(0, 120);

      var modelMatch = subject.match(/\b(8P|10P|12P|14P|16P|20P|22P|24P|28P|32P|36P|42P)\b/i);
      if (modelMatch) {
        intent.inquiry_model = modelMatch[1].toUpperCase();
      }

      if (lower.indexOf("gearbox only") !== -1) {
        intent.inquiry_type = "gearbox_only";
      } else if (lower.indexOf("motor + gearbox") !== -1 ||
                 lower.indexOf("motor and gearbox") !== -1) {
        intent.inquiry_type = "motor_gearbox";
      } else if (lower.indexOf("planetary gearbox") !== -1) {
        intent.inquiry_type = "planetary_general";
      }

      if (lower.indexOf("pruning") !== -1) {
        intent.inquiry_type = "application_review";
        intent.inquiry_application = "electric_pruning_shears";
      } else if (lower.indexOf("curtain") !== -1 || lower.indexOf("blind") !== -1) {
        intent.inquiry_type = "application_review";
        intent.inquiry_application = "electric_curtain_blind";
      } else if (lower.indexOf("smart toilet") !== -1 || lower.indexOf("bidet") !== -1) {
        intent.inquiry_type = "application_review";
        intent.inquiry_application = "smart_toilet_bidet";
      } else if (lower.indexOf("dexterous hand") !== -1 || lower.indexOf("robot gripper") !== -1) {
        intent.inquiry_type = "application_review";
        intent.inquiry_application = "dexterous_hand_gripper";
      }
    } catch (e) {
      // Keep generic values for malformed mailto links.
    }

    return intent;
  }

  function priorityApplicationFromPath(pathname) {
    var path = pathname || "";
    if (path.indexOf("/applications/electric-pruning-shears-planetary-gearbox/") !== -1) {
      return "electric_pruning_shears";
    }
    if (path.indexOf("/applications/electric-curtain-blind-window-opener-gear-motors/") !== -1) {
      return "electric_curtain_blind";
    }
    if (path.indexOf("/applications/smart-toilet-bidet-planetary-gear-motors/") !== -1) {
      return "smart_toilet_bidet";
    }
    if (path.indexOf("/applications/robot-gripper-gear-motors/") !== -1) {
      return "dexterous_hand_gripper";
    }
    return "";
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

  function trackCampaignLanding() {
    try {
      var params = new URLSearchParams(window.location.search);
      var source = (params.get("utm_source") || "").toLowerCase();
      var medium = (params.get("utm_medium") || "").toLowerCase();
      var campaign = params.get("utm_campaign") || "";
      var content = params.get("utm_content") || "";

      if (!source) return;

      sendEvent("campaign_landing", {
        page_path: pagePath(),
        utm_source: source,
        utm_medium: medium,
        utm_campaign: campaign,
        utm_content: content,
        referrer: document.referrer || ""
      });

      if (source === "youtube" || source === "instagram" || source === "tiktok") {
        sendEvent("social_landing", {
          page_path: pagePath(),
          social_platform: source,
          utm_medium: medium,
          utm_campaign: campaign,
          utm_content: content
        });
      }
    } catch (e) {
      // Ignore malformed campaign parameters.
    }
  }

  var path = pagePath();

  trackCampaignLanding();

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
      var intent = emailIntent(href);
      var emailParams = {
        page_path: pagePath(),
        contact_method: "email",
        link_text: label,
        inquiry_type: intent.inquiry_type,
        inquiry_model: intent.inquiry_model,
        inquiry_application: intent.inquiry_application,
        email_subject: intent.email_subject
      };

      // Preserve the existing event for historical continuity.
      sendEvent("email_click", emailParams);

      // Add a dedicated conversion event when the mailto link represents a
      // structured planetary inquiry rather than a generic contact email.
      if (intent.inquiry_type !== "general_email") {
        sendEvent("planetary_inquiry_click", emailParams);
      }
      return;
    }

    // Record user intent to download released CAD without changing navigation
    // or sending analytics before the existing cookie-consent gated tag loads.
    try {
      var cadUrl = new URL(href, window.location.href);
      var cadPath = cadUrl.pathname;
      if (cadUrl.hostname === window.location.hostname && /\.(step|stp)$/i.test(cadPath)) {
        var cadMatch = cadPath.match(/\/(\d{1,2}p)\//i);
        sendEvent("cad_download_click", {
          page_path: pagePath(),
          cad_model: cadMatch ? cadMatch[1].toUpperCase() : "not_specified",
          cad_format: "STEP",
          file_name: cadPath.split("/").pop() || "",
          cad_reference: /Public_Simplified_STEP.*4-Stage\.(step|stp)$/i.test(cadPath) ?
            "public_simplified_4_stage" : "other_step",
          link_text: label
        });
        return;
      }
    } catch (e) {
      // Malformed links are ignored; normal click navigation continues.
    }

    try {
      var internalDestination = new URL(href, window.location.href);
      if (internalDestination.hostname === window.location.hostname) {
        var priorityApplication = priorityApplicationFromPath(internalDestination.pathname);
        if (priorityApplication) {
          sendEvent("priority_application_click", {
            page_path: pagePath(),
            application: priorityApplication,
            destination_path: internalDestination.pathname,
            link_text: label
          });
          return;
        }
      }
    } catch (e) {
      // Ignore malformed internal links and continue normal navigation.
    }

    try {
      var destination = new URL(href, window.location.href);
      var hostname = destination.hostname.replace(/^www\./, "");
      var socialPlatform = "";

      if (hostname === "youtube.com" || hostname === "youtu.be") {
        socialPlatform = "youtube";
      } else if (hostname === "instagram.com") {
        socialPlatform = "instagram";
      } else if (hostname === "tiktok.com") {
        socialPlatform = "tiktok";
      }

      if (socialPlatform) {
        sendEvent("social_click", {
          page_path: pagePath(),
          social_platform: socialPlatform,
          destination_url: destination.href,
          link_text: label
        });
        return;
      }
    } catch (e) {
      // Ignore invalid or non-URL href values and continue with internal-link tracking.
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