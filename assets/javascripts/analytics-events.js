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
    if (path.indexOf("/applications/access-control-smart-lock-security-gear-motors/") !== -1) {
      return "smart_lock_access_control";
    }
    if (path.indexOf("/applications/pump-valve-fluid-control-gear-motors/") !== -1) {
      return "pump_valve_fluid";
    }
    if (path.indexOf("/applications/optical-imaging-camera-module-gear-motors/") !== -1) {
      return "optical_positioning";
    }
    if (path.indexOf("/applications/food-beverage-coffee-equipment-gear-motors/") !== -1) {
      return "coffee_equipment";
    }
    return "";
  }

  // Keep application attribution limited to public path slugs (no cookies or identifiers).
  function applicationSlugFromPath(pathname) {
    var match = (pathname || "").match(
      /\/SigGear-product-docs\/applications\/([a-z0-9-]+)\/$/i
    );
    return match ? match[1].toLowerCase() : "not_specified";
  }

  function engineeringFileSource() {
    var path = pagePath();
    var app = applicationSlugFromPath(path);
    var sourceType = "other";
    if (app !== "not_specified") {
      sourceType = "application";
    } else if (/\/products\/planetary-gearboxes\/\d{1,2}p-planetary-gearbox\/$/i.test(path)) {
      sourceType = "product_model";
    } else if (path.indexOf("/engineering-resources/planetary-gearboxes/public-cad-release-v1/") !== -1) {
      sourceType = "gearhead_download_hub";
    } else if (path.indexOf("/engineering-resources/motors/") !== -1) {
      sourceType = "motor_datasheet_hub";
    }

    // Only attribute a product download to an application when it is the
    // immediate same-site referrer. Do not invent a multi-page user journey.
    if (sourceType === "product_model" && document.referrer) {
      try {
        var referrer = new URL(document.referrer);
        if (referrer.hostname === window.location.hostname) {
          app = applicationSlugFromPath(referrer.pathname);
        }
      } catch (e) {
        // Invalid or private referrers remain unattributed.
      }
    }
    return {source_page_type: sourceType, source_application: app};
  }

  var JOINT_RELEASE_FILES = {
    "joint-actuators/SG-6010C_Public_Reference_Datasheet_Rev0.1.pdf": ["SG-6010C", "catalogue", "datasheet_pdf"],
    "joint-actuators/SG-6010D_Public_Reference_Datasheet_Rev0.1.pdf": ["SG-6010D", "catalogue", "datasheet_pdf"],
    "joint-actuators/SG-8021_Public_Reference_Datasheet_Rev0.1.pdf": ["SG-8021", "catalogue", "datasheet_pdf"],
    "joint-actuators/CPM-78-39_Public_Reference_Datasheet_Rev0.1.pdf": ["CPM-78-39", "catalogue", "datasheet_pdf"],
    "joint-actuators/CPM-80-25_Public_Reference_Datasheet_Rev0.1.pdf": ["CPM-80-25", "catalogue", "datasheet_pdf"],
    "joint-actuators/CPM-100-25_Public_Reference_Datasheet_Rev0.1.pdf": ["CPM-100-25", "catalogue", "datasheet_pdf"],
    "joint-actuators/SG-6010D_2D_Assembly_Drawing.pdf": ["SG-6010D", "published_assembly", "reference_2d_pdf"],
    "joint-actuators/CPM-80-25_2D_No_Driver_29p7mm.pdf": ["CPM-80-25", "no_driver_29_7mm", "reference_2d_pdf"],
    "joint-actuators/CPM-80-25_2D_Integrated_Driver_41p2mm.pdf": ["CPM-80-25", "integrated_driver_41_2mm", "reference_2d_pdf"],
    "joint-actuators/CPM-100-25D_2D_Dual_Encoder_Driver_48mm.pdf": ["CPM-100-25", "dual_encoder_driver_48mm", "reference_2d_pdf"],
    "joint-actuators/SG-6010C_Original_Full_Assembly_20261118.step": ["SG-6010C", "standard", "original_full_step"],
    "joint-actuators/SG-6010D_Original_Full_Assembly_20261118.step": ["SG-6010D", "published_assembly", "original_full_step"],
    "joint-actuators/SG-8021_Driver_Version_Original_Full_Assembly_20261118.step": ["SG-8021", "driver_version", "original_full_step"],
    "joint-actuators/CPM-78-39_Original_Full_Assembly_20261118.step": ["CPM-78-39", "standard", "original_full_step"],
    "joint-actuators/CPM-80-25_Original_Full_Assembly_No_Driver_20261118.step": ["CPM-80-25", "no_driver", "original_full_step"],
    "joint-actuators/CPM-80-25_Original_Full_Assembly_Integrated_Driver_20261118.step": ["CPM-80-25", "integrated_driver", "original_full_step"],
    "joint-actuators/CPM-100-25_Original_Full_Assembly_No_Driver_20261118.step": ["CPM-100-25", "standard_29_5mm", "original_full_step"],
    "joint-actuators/CPM-100-25D_Dual_Encoder_Driver_Original_Full_Assembly_20261118.step": ["CPM-100-25", "dual_encoder_driver_48mm", "original_full_step"],
    "sg6010c/SG-6010C_Public_Simplified_STEP_v1.0.step": ["SG-6010C", "simplified_standard", "simplified_step"],
    "cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_No_Driver.step": ["CPM-80-25", "simplified_no_driver", "simplified_step"],
    "cpm80-25/CPM-80-25_Public_Simplified_STEP_v1.0_Integrated_Driver.step": ["CPM-80-25", "simplified_integrated_driver", "simplified_step"]
  };

  function jointSourceType() {
    var currentPath = pagePath();
    if (currentPath.indexOf("/engineering-resources/robot-joint-actuators/quick-downloads/") !== -1) {
      return "joint_download_hub";
    }
    if (/\/products\/(?:robot-joint-actuators|cycloidal-joint-modules)\/(?:sg6010c|sg6010d|sg8021|cpm78-39|cpm80-25|cpm100-25)\//i.test(currentPath)) {
      return "joint_product_model";
    }
    if (currentPath.indexOf("/engineering-resources/") !== -1) return "engineering_reference";
    if (currentPath.indexOf("/applications/") !== -1) return "application";
    return "other";
  }

  function pagePath() {
    try {
      return new URL(window.location.href).pathname;
    } catch (e) {
      return window.location.pathname || "";
    }
  }

  function inquiryPageContext() {
    var context = {
      inquiry_model: "not_specified",
      inquiry_application: "not_specified",
      inquiry_type: "not_sure",
      selector_handoff: 0,
      selector_candidate_stage: "none"
    };

    try {
      var params = new URLSearchParams(window.location.search);
      var model = (params.get("model") || "").toUpperCase();
      if (/^(8P|10P|12P|14P|16P|20P|22P|24P|28P|32P|36P|42P)$/.test(model)) {
        context.inquiry_model = model;
      }

      var application = (params.get("app") || "").toLowerCase();
      if ([
        "electric_pruning_shears",
        "electric_curtain_blind",
        "smart_toilet_bidet",
        "dexterous_hand_gripper",
        "smart_lock_access_control",
        "pump_valve_fluid",
        "optical_positioning",
        "coffee_equipment"
      ].indexOf(application) !== -1) {
        context.inquiry_application = application;
      }

      var inquiryType = (params.get("path") || "not_sure").toLowerCase().replace(/-/g, "_");
      if (["gearbox_only", "motor_gearbox", "not_sure"].indexOf(inquiryType) !== -1) {
        context.inquiry_type = inquiryType;
      }

      if ((params.get("selection") || "") === "ratio_stage_selector") {
        context.selector_handoff = 1;
        var candidateStage = Number(params.get("candidate_stage"));
        if (Number.isInteger(candidateStage) && candidateStage >= 1 && candidateStage <= 4) {
          context.selector_candidate_stage = String(candidateStage);
        }
      }
    } catch (e) {
      // Keep normalized defaults.
    }

    return context;
  }

  function inquiryOriginGroup() {
    try {
      var currentParams = new URLSearchParams(window.location.search);
      if ((currentParams.get("selection") || "") === "ratio_stage_selector") return "selection_tool";

      var ref = document.referrer ? new URL(document.referrer) : null;
      if (!ref || ref.hostname !== window.location.hostname) return "direct_or_external";
      var refPath = ref.pathname || "";
      if (refPath.indexOf("/selection-guides/miniature-planetary-gearbox-selection-guide/") !== -1) return "selection_tool";
      if (refPath.indexOf("/engineering-resources/") !== -1) return "engineering_resource";
      if (/\/products\/planetary-gearboxes\/\d{1,2}p-planetary-gearbox\//i.test(refPath)) return "product_model";
      if (refPath.indexOf("/products/planetary-gearboxes/") !== -1) return "planetary_series";
      if (refPath.indexOf("/applications/") !== -1) return "application";
      if (refPath === "/" || /\/SigGear-product-docs\/$/.test(refPath)) return "homepage";
      return "internal_other";
    } catch (e) {
      return "unknown";
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
    var inquiryContext = inquiryPageContext();
    sendEvent("inquiry_page_view", {
      page_path: path,
      inquiry_model: inquiryContext.inquiry_model,
      inquiry_application: inquiryContext.inquiry_application,
      inquiry_type: inquiryContext.inquiry_type,
      inquiry_origin: inquiryOriginGroup(),
      selector_handoff: inquiryContext.selector_handoff,
      selector_candidate_stage: inquiryContext.selector_candidate_stage
    });
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

    // Count released robot-joint PDF/STEP intent by exact model and configuration.
    // Do not confuse a click with a successful download, sale or engineering approval.
    try {
      var jointFileUrl = new URL(href, window.location.href);
      var jointMatch = jointFileUrl.pathname.match(
        /\/SigGear-product-docs\/assets\/downloads\/(joint-actuators|sg6010c|cpm80-25)\/([^/]+)$/i
      );
      if (jointFileUrl.hostname === window.location.hostname && jointMatch) {
        var jointKey = jointMatch[1] + "/" + jointMatch[2];
        if (Object.prototype.hasOwnProperty.call(JOINT_RELEASE_FILES, jointKey)) {
          var jointInfo = JOINT_RELEASE_FILES[jointKey];
          sendEvent("joint_engineering_file_click", {
            page_path: pagePath(),
            joint_model: jointInfo[0],
            joint_variant: jointInfo[1],
            file_type: jointInfo[2],
            file_name: jointMatch[2],
            source_page_type: jointSourceType(),
            source_application: applicationSlugFromPath(pagePath()),
            link_text: label
          });
          // Retain the established generic cad_download_click for STEP files.
          if (jointInfo[2] === "datasheet_pdf" || jointInfo[2] === "reference_2d_pdf") return;
        }
      }
    } catch (e) {
      // Analytics must not block navigation or download.
    }

    // Track public motor-only PDF intent separately from planetary gearhead files.
    // This event is a click, not proof the PDF was read or a lead was created.
    try {
      var motorFileUrl = new URL(href, window.location.href);
      var motorFileMatch = motorFileUrl.pathname.match(
        /\/SigGear-product-docs\/assets\/downloads\/motors\/((?:8|10|12|14|16|20|22|24|28|32)mm)\/(SigGear_[^/]+\.pdf)$/i
      );
      if (motorFileUrl.hostname === window.location.hostname && motorFileMatch) {
        var motorSource = engineeringFileSource();
        sendEvent("motor_datasheet_click", {
          page_path: pagePath(),
          file_name: motorFileMatch[2],
          motor_diameter_mm: parseInt(motorFileMatch[1], 10),
          source_page_type: motorSource.source_page_type,
          source_application: motorSource.source_application,
          link_text: label
        });
        return;
      }
    } catch (e) {
      // Malformed links must never interrupt a genuine file download.
    }

    // Track direct engineering-file clicks (PDF datasheet, 2D drawing and STEP).
    // Preserve the existing CAD event so historical reporting remains comparable.
    try {
      var resourceUrl = new URL(href, window.location.href);
      var downloadMatch = resourceUrl.pathname.match(
        /\/SigGear-product-docs\/assets\/downloads\/((?:8|10|12|14|16|20|22|24|28|32|36|42)p)\/([^/]+)$/i
      );
      if (resourceUrl.hostname === window.location.hostname && downloadMatch) {
        var modelName = downloadMatch[1].toUpperCase();
        var fileName = downloadMatch[2];
        var kind = "";
        if (fileName.indexOf(modelName + "_Planetary_Gearhead_Datasheet_") === 0 &&
            /\.pdf$/i.test(fileName)) {
          kind = "datasheet_pdf";
        } else if (fileName === modelName + "_2D_Drawing.pdf") {
          kind = "outline_2d_pdf";
        } else if (fileName === modelName + "_Full_Assembly.step") {
          kind = "full_assembly_step";
        } else if (fileName === modelName + "_Public_Simplified_STEP_v1.0_4-Stage.step") {
          kind = "simplified_4_stage_step";
        }
        if (kind) {
          var fileSource = engineeringFileSource();
          sendEvent("planetary_engineering_file_click", {
            page_path: pagePath(),
            file_type: kind,
            gearhead_model: modelName,
            file_name: fileName,
            link_text: label,
            source_page_type: fileSource.source_page_type,
            source_application: fileSource.source_application
          });
          // The CAD block below still records its established STEP-only event.
          if (/\.pdf$/i.test(fileName)) return;
        }
      }
    } catch (e) {
      // Invalid destinations never block a real download.
    }

    // Record user intent to download released CAD without changing navigation
    // or sending analytics before the existing cookie-consent gated tag loads.
    try {
      var cadUrl = new URL(href, window.location.href);
      var cadPath = cadUrl.pathname;
      if (cadUrl.hostname === window.location.hostname && /\.(step|stp)$/i.test(cadPath)) {
        var cadMatch = cadPath.match(/\/(\d{1,2}p)\//i);
        var cadSource = engineeringFileSource();
        sendEvent("cad_download_click", {
          page_path: pagePath(),
          source_page_type: cadSource.source_page_type,
          source_application: cadSource.source_application,
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
        if (internalDestination.pathname.endsWith("/request-cad-sample-quote/")) {
          var briefModelRaw = (internalDestination.searchParams.get("model") || "").toUpperCase();
          var briefModel = /^(8P|10P|12P|14P|16P|20P|22P|24P|28P|32P|36P|42P)$/.test(briefModelRaw) ?
            briefModelRaw : "not_specified";
          var briefApplication = (internalDestination.searchParams.get("app") || "").toLowerCase();
          var validBriefApplications = [
            "electric_pruning_shears",
            "electric_curtain_blind",
            "smart_toilet_bidet",
            "dexterous_hand_gripper",
            "smart_lock_access_control",
            "pump_valve_fluid",
            "optical_positioning",
            "coffee_equipment"
          ];
          if (validBriefApplications.indexOf(briefApplication) === -1) {
            briefApplication = "not_specified";
          }
          var briefPath = (internalDestination.searchParams.get("path") || "not_sure").toLowerCase().replace(/-/g, "_");
          if (["gearbox_only", "motor_gearbox", "not_sure"].indexOf(briefPath) === -1) {
            briefPath = "not_sure";
          }

          var selectorHandoff = internalDestination.searchParams.get("selection") === "ratio_stage_selector" ? 1 : 0;
          var selectorStageValue = Number(internalDestination.searchParams.get("candidate_stage"));
          var selectorStage = Number.isInteger(selectorStageValue) &&
            selectorStageValue >= 1 && selectorStageValue <= 4 ?
            String(selectorStageValue) : "none";

          sendEvent("engineering_brief_open_click", {
            page_path: pagePath(),
            inquiry_model: briefModel,
            inquiry_application: briefApplication,
            inquiry_type: briefPath,
            inquiry_origin: selectorHandoff ? "selection_tool" : inquiryOriginGroup(),
            selector_handoff: selectorHandoff,
            selector_candidate_stage: selectorStage,
            destination_path: internalDestination.pathname,
            link_text: label
          });
          return;
        }

        // One click from a concise application page into a precise product or
        // download category is a useful intent signal, not a confirmed lead.
        var sourceApplication = applicationSlugFromPath(pagePath());
        if (sourceApplication !== "not_specified") {
          var linkedModel = internalDestination.pathname.match(
            /\/SigGear-product-docs\/products\/planetary-gearboxes\/((?:8|10|12|14|16|20|22|24|28|32|36|42)p)-planetary-gearbox\/$/i
          );
          if (linkedModel) {
            sendEvent("application_product_click", {
              page_path: pagePath(),
              source_application: sourceApplication,
              gearhead_model: linkedModel[1].toUpperCase(),
              destination_path: internalDestination.pathname,
              link_text: label
            });
            return;
          }

          var resourceType = "";
          if (internalDestination.pathname.endsWith("/engineering-resources/motors/")) {
            resourceType = "motor_datasheets";
          } else if (internalDestination.pathname.endsWith(
            "/engineering-resources/planetary-gearboxes/public-cad-release-v1/"
          )) {
            resourceType = "gearhead_downloads";
          } else if (internalDestination.pathname.endsWith(
            "/custom-engineering/motor-gearbox-integration/"
          )) {
            resourceType = "motor_gearhead_assembly";
          }
          if (resourceType) {
            sendEvent("application_resource_click", {
              page_path: pagePath(),
              source_application: sourceApplication,
              resource_type: resourceType,
              destination_path: internalDestination.pathname,
              link_text: label
            });
            return;
          }
        }

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
      // Track outbound engineering-CAD discovery; do not treat it as a
      // confirmed CAD download or completed inquiry.
      if (hostname === "traceparts.cn" || hostname.endsWith(".traceparts.cn") ||
          hostname === "traceparts.com" || hostname.endsWith(".traceparts.com")) {
        sendEvent("traceparts_catalog_click", {
          page_path: pagePath(),
          destination_url: destination.href,
          traceparts_portal: hostname.endsWith(".cn") ? "cn" : "international",
          link_text: label
        });
        return;
      }
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