# GSC sitemap investigation — 2026-10-15

## Reported issue
In the SigGear URL-prefix Search Console property `https://siggeardrive.github.io/SigGear-product-docs/`, the previously submitted `/sitemap.xml` was reported as **Couldn't fetch** / unknown type / 0 discovered pages, and the operator reports that this status has persisted for approximately five months. The screenshot shows a submission dated 2026-10-10 and no last-read date. Three priority pages are unknown to the GSC indexed-data report; all passed Google's live URL inspection, but the operator reports the indexing-request button was unresponsive.

## GitHub Pages and external HTTP verification
2026-10-15, GitHub Actions diagnostic CI:
- `https://siggeardrive.github.io/SigGear-product-docs/sitemap.xml`: HTTP **200**, content type **application/xml**, XML parsed, **148** URL entries, three requested URLs present.
- Same Sitemap with `User-Agent: Googlebot`: HTTP **200**, same bytes and 148 valid URL entries. **Caution:** a Googlebot User-Agent string on GitHub Actions is *not* a request from Google's verified crawler network.
- Online gearbox selection, public CAD and pruning shears URL: each HTTP **200**, no redirect.
- `https://siggeardrive.github.io/robots.txt`: HTTP **404** (standard missing-robots response, not a robots disallow).
- `https://siggeardrive.github.io/SigGear-product-docs/robots.txt`: HTTP **200**, allows project subpath, lists original sitemap. Robots rules are scoped to host root `/robots.txt`, so the project-subpath file is *not* the controlling robots location.

The public files and external HTTP responses **do not establish a technical crawl block**. The GSC "Couldn't fetch" status can mean the sitemap has not been processed yet, rather than a definitive failed server fetch. Actual Googlebot fetch logs are not available from GitHub Pages hosting.

## Safe optional test endpoint
The site **already has** a valid Sitemap index at `https://siggeardrive.github.io/SigGear-product-docs/sitemap-index.xml`, whose only child is the existing auto-generated `sitemap.xml`. A second external GitHub Actions HTTP probe verified the published index responds **HTTP 200**, `Content-Type: application/xml`, with no `X-Robots-Tag` or redirects. The original sitemap and each of the three priority pages also returned 200. **No new sitemap or website modification is required**; the alternative is ready for one controlled submission. Do not rename or replace the original sitemap, change canonical URLs, or duplicate and freeze the 148-page auto-generated listing.

Google documents XML Sitemap index files: https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps/

## Follow-up in the correct Search Console property
1. `sitemap-index.xml` was already deployed and returned HTTP 200 (`application/xml`) on 2026-10-15. Optionally inspect the published XML before submitting.
2. In Search Console > Sitemaps > Add a new sitemap, submit **`sitemap-index.xml`** once. Keep the original `sitemap.xml` submission intact.
3. Capture the exact status, discovered sitemaps/pages and latest read timestamp of both records, initially after submission and on subsequent days. Avoid repeated remove/re-submit attempts that erase useful status history.
4. A new index record also staying "Couldn't fetch" does not prove invalid XML; review whether the nested XML has been crawled, as well as the actual URL Inspection results and Google-side processing queue.
5. Continue normal internal links from indexed core pages to the three priority pages; keep sitemap and site redirects/canonicals stable.

No indexing is guaranteed by submitting a sitemap, and the absence of an immediate GSC response does not imply failure.

## Temporary diagnostic CI

- Probe PR: https://github.com/SigGearDrive/SigGear-product-docs/pull/205 (read-only, not for merge).
- First run HTTP evidence: `https://github.com/SigGearDrive/SigGear-product-docs/actions/runs/38705078547`.
- Second run including `sitemap-index.xml`: `https://github.com/SigGearDrive/SigGear-product-docs/actions/runs/38705619767`.
- The GitHub Actions runner's `User-Agent: Googlebot` check proves that request headers alone do not cause a block; it does **not** prove Google Search crawler infrastructure has fetched or processed the file.
