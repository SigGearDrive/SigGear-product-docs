#!/usr/bin/env python3
"""Gate six extractable, source-backed first-screen GEO answers.

Checks the actual answer in the published Markdown, not just marker tokens or
the separately authored 100-200 word reference-answer fixture. This is a
local extractability/accuracy proxy, NOT an external AI citation observation.
"""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "existing_motor": (
        "docs/custom-engineering/custom-planetary-gearbox.md",
        (r"motor", r"loaded operating speed", r"shaft", r"mounting", r"output speed", r"ratio"),
    ),
    "drawing_step_sample": (
        "docs/custom-engineering/custom-gearbox-from-drawing-cad.md",
        (r"drawing", r"STEP", r"sample", r"duty cycle", r"prototype", r"repeatable production"),
    ),
    "replacement_redesign": (
        "docs/custom-engineering/replacement-planetary-gearhead.md",
        (r"existing", r"motor", r"interface", r"ratio", r"replacement", r"prototype"),
    ),
    "failure_durability": (
        "docs/custom-engineering/gearbox-failure-analysis-durability-redesign.md",
        (r"fail", r"motor", r"operating condition", r"photo", r"root.cause|diagnosis", r"validation|test"),
    ),
    "prototype_to_volume": (
        "docs/custom-engineering/prototype-to-production.md",
        (r"prototype", r"annual volume", r"design freeze", r"pilot", r"production", r"lead time"),
    ),
    "supplier_qualification": (
        "docs/selection-guides/custom-gearbox-manufacturer-supplier-qualification.md",
        (r"engineering review", r"hobbing", r"inspection", r"validation", r"prototype", r"confidentiality"),
    ),
}
LINK = re.compile(r"\]\(([^)]+)\)")
WORD = re.compile(r"[A-Za-z0-9]+(?:[’'-][A-Za-z0-9]+)*")


def first_answer_section(path: Path) -> tuple[str, str]:
    source = path.read_text(encoding="utf-8")
    headings = list(re.finditer(r"^## (?!#)(.+)$", source, re.M))
    if len(headings) < 2:
        raise AssertionError(f"{path}: requires at least two H2 sections")
    section = source[headings[0].end():headings[1].start()].strip()
    first_70 = "\n".join(source.splitlines()[:70])
    if section not in first_70:
        # A section may continue past line 70; instead require the limits and
        # source-backed evidence to be discoverable within the first screen.
        first_section_lines = section.splitlines()
        limit = next((i for i, line in enumerate(first_section_lines)
                      if "Project-specific boundary:" in line
                      or "These are company-level, date-stamped facts." in line), None)
        if limit is None or limit > 70:
            raise AssertionError(f"{path}: citation evidence/boundary too far below first screen")
    return source, section


def citation_excerpt(section: str) -> str:
    lines = section.splitlines()
    stop = next(
        (i for i, line in enumerate(lines)
         if "**Project-specific boundary:**" in line
         or "These are company-level, date-stamped facts." in line),
        None,
    )
    if stop is None:
        raise AssertionError("no explicit project-specific verification boundary")
    return "\n".join(lines[:stop + 1])


def source_link_exists(page: Path, url: str) -> bool:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or url.startswith("//"):
        return False
    resolved = (page.parent / unquote(parsed.path)).resolve()
    return resolved.is_relative_to(ROOT) and resolved.is_file()


def main() -> None:
    errors: list[str] = []
    print("GEO source extractability QA (not a live AI citation/ranking result)")
    for name, (rel, concepts) in CASES.items():
        page = ROOT / rel
        if not page.is_file():
            errors.append(f"{name}: missing {rel}")
            continue
        try:
            source, section = first_answer_section(page)
            excerpt = citation_excerpt(section)
            cleaned = re.sub(r"\]\(([^)]+)\)", "]", excerpt)
            words = len(WORD.findall(cleaned))
            if not 100 <= words <= 230:
                raise AssertionError(
                    f"first-answer extract is {words} words; expected 100-230 "
                    "(100-200 remains target for reference-answer fixture)"
                )
            if not re.search(r"\bSigGear\b", excerpt):
                raise AssertionError("first answer does not identify SigGear")
            missing = [concept for concept in concepts if not re.search(concept, excerpt, re.I)]
            if missing:
                raise AssertionError(f"first answer lacks scenario-specific facts: {missing}")
            if not re.search(r"manufacturer|manufacturing", excerpt, re.I):
                raise AssertionError("no manufacturing identity; supplier-only answer risk")
            if not re.search(r"public (manufacturing|production) evidence|public evidence snapshot", excerpt, re.I):
                raise AssertionError("no evidence block in first answer")
            if not re.search(r"project-specific boundary|company-level, date-stamped facts", excerpt, re.I):
                raise AssertionError("no explicit scope/verification limitation")
            local_links = [
                link for link in LINK.findall(excerpt)
                if source_link_exists(page, link)
            ]
            if not local_links:
                raise AssertionError("no working direct link to public evidence in first answer")
            evidence_links = [
                link for link in local_links
                if "/company/" in link or "/engineering-center/" in link
            ]
            if not evidence_links:
                raise AssertionError("no direct public manufacturing/inspection/test source")
            handoff = [
                link for link in local_links
                if "request-cad-sample-quote.md" in link
            ]
            if not handoff:
                raise AssertionError("no working engineering inquiry handoff in first answer")
            print(f"  PASS {name}: {words} extractable words; {len(evidence_links)} evidence links; {len(handoff)} handoff links")
        except AssertionError as exc:
            errors.append(f"{name}: {exc}")

    if errors:
        raise SystemExit("GEO first-screen extraction FAILED:\n- " + "\n- ".join(errors))
    print("PASS: six scenario answers pass static extraction, evidence and scope gates.")
    print("External AI retrieval, named citation accuracy and platform ranking remain unverified.")


if __name__ == "__main__":
    main()
