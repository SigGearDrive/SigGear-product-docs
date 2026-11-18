(function () {
  "use strict";
  // Progressive enhancement; all 33 PDF links remain visible without JavaScript.
  function initializeMotorQuickDownloads() {
    var input = document.getElementById("siggear-motor-filter");
    var table = document.getElementById("siggear-motor-quick-table");
    var status = document.getElementById("siggear-motor-results");
    if (!input || !table || !status || table.dataset.motorFilterReady === "1") return;
    table.dataset.motorFilterReady = "1";

    function normalized(value) {
      return (value || "").normalize("NFKC")
        .toLowerCase().replace(/[øØ]/g, "").replace(/\s+/g, "").trim();
    }

    var rows = Array.prototype.slice.call(table.querySelectorAll("tbody tr"));
    var total = rows.reduce(function (sum, row) {
      return sum + row.querySelectorAll("a.siggear-motor-file").length;
    }, 0);

    function applyFilter() {
      var query = normalized(input.value);
      var visibleFiles = 0;
      var visibleGroups = 0;
      rows.forEach(function (row) {
        var cells = row.querySelectorAll("td");
        var family = [cells[0], cells[1], cells[3]]
          .map(function (cell) { return cell ? cell.textContent : ""; }).join(" ");
        var familyMatch = !query || normalized(family).indexOf(query) !== -1;
        var links = Array.prototype.slice.call(row.querySelectorAll("a.siggear-motor-file"));
        var matchedLinks = 0;
        links.forEach(function (link) {
          var searchable = link.textContent + " " + (link.getAttribute("title") || "");
          var matches = familyMatch || normalized(searchable).indexOf(query) !== -1;
          link.hidden = !matches;
          if (matches) matchedLinks += 1;
        });
        row.hidden = matchedLinks === 0;
        if (matchedLinks) visibleGroups += 1;
        visibleFiles += matchedLinks;
      });
      status.textContent = visibleFiles ?
        visibleGroups + " diameter group" + (visibleGroups === 1 ? "" : "s") +
        " · " + visibleFiles + " of " + total + " direct PDFs" :
        "No matching motor PDFs. Clear the search to see all " + total + " files.";
    }

    input.addEventListener("input", applyFilter);
    applyFilter();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeMotorQuickDownloads);
  } else {
    initializeMotorQuickDownloads();
  }
})();
