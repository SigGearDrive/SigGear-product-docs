# Google Search Console — SigGear GitHub Pages indexing handoff

## Verified project property and public sitemap

- Search Console URL-prefix property: `https://siggeardrive.github.io/SigGear-product-docs/`
- Public XML sitemap: `https://siggeardrive.github.io/SigGear-product-docs/sitemap.xml`
- Sitemap index (alternative, not required when submitting the XML directly): `https://siggeardrive.github.io/SigGear-product-docs/sitemap-index.xml`
- GitHub Pages project root: `https://siggeardrive.github.io/SigGear-product-docs/`

## One-time owner action: confirm sitemap submission

1. Open [Google Search Console](https://search.google.com/search-console/) and select the exact URL-prefix property above (not `siggear.com`).
2. Open **Indexing → Sitemaps**.
3. Check the submitted sitemap list. If `sitemap.xml` is already listed with **Success**, do not resubmit it just for a new deployment. Otherwise enter **`sitemap.xml`** and select Submit.
4. Inspect the submission status, last read time, discovered URLs and any errors. Save the observed figures separately from GitHub sitemap counts.
5. Open **Indexing → Pages** to see Google's **indexed / not indexed** totals and exclusion reasons. A sitemap URL count is never an indexed-URL count.
6. Use URL Inspection on a small set of priority URLs, especially the engineering download hub, the 8–42 mm product comparison, and one model page. Request recrawling only when a changed page needs it; repeated requests don't speed it up.

### Priority URL inspection list

- `https://siggeardrive.github.io/SigGear-product-docs/engineering-resources/planetary-gearboxes/public-cad-release-v1/`
- `https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/8-42mm-planetary-gear-reducer/`
- `https://siggeardrive.github.io/SigGear-product-docs/products/planetary-gearboxes/22p-planetary-gearbox/`
- `https://siggeardrive.github.io/SigGear-product-docs/applications/electric-pruning-shears-planetary-gearbox/`
- `https://siggeardrive.github.io/SigGear-product-docs/applications/humanoid-robot-joint-actuators/`

## GitHub Pages project path caveat

A file at `https://siggeardrive.github.io/SigGear-product-docs/robots.txt` is inside a project subdirectory, **not the domain-host robots file**. Google normally looks at `https://siggeardrive.github.io/robots.txt`. Do not assume that the subdirectory robots file advertises the sitemap to Google.

Sitemap submission in Search Console is the reliable owner-controlled next action. The connected Windsor.ai Google Search Console integration is read-only; it reports Search Analytics and limited Sitemap data but cannot submit sitemaps or retrieve the full Pages indexing report.

The CI workflow `.github/workflows/check-live-pages-http.yml` checks whether the public sitemap responds successfully, whether key canonical URLs are listed, and reports what is available at the host-root robots URL. It **cannot prove Google has indexed a URL**.

Reference: [Google sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) · [robots.txt location rules](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt) · [URL recrawl guidance](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl).

## Monitoring without false claims

- Compare Search Analytics clicks, impressions, CTR and average position using the **same property and date windows**; allow approximately 2–3 days for finalized data.
- Search Analytics URLs with impressions are evidence of search visibility, not a complete list of indexed pages.
- Review Pages indexed/excluded totals and Sitemap status inside Search Console after major releases. Keep these private operational figures out of public repository pages.
- Do not change all 32 application pages again without a page-specific reason, a verified technical issue, or sufficient post-recrawl search data.
