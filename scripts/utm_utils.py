#!/usr/bin/env python3
"""Helpers for deterministic SigGear campaign tracking URLs."""

from __future__ import annotations

from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


def tracked_url(url: str, *, source: str, medium: str, campaign: str, content: str) -> str:
    """Return a URL with the canonical SigGear UTM fields added or replaced."""
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    query.update(
        {
            "utm_source": source,
            "utm_medium": medium,
            "utm_campaign": campaign,
            "utm_content": content,
        }
    )
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))
