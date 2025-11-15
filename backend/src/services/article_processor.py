"""Utilities for cleaning and summarising article payloads."""
from __future__ import annotations

import html
import logging
import re
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
_TAG_RE = re.compile(r"<[^>]+>")
_WHITESPACE_RE = re.compile(r"\s+")


def clean_text(text: Optional[str]) -> str:
    """Remove HTML fragments, condense whitespace and unescape entities."""

    if not text:
        return ""
    stripped = html.unescape(text)
    stripped = _TAG_RE.sub(" ", stripped)
    stripped = _WHITESPACE_RE.sub(" ", stripped)
    return stripped.strip()


def summarise_text(text: str, *, max_sentences: int = 2) -> str:
    """Build a lightweight extractive summary by selecting leading sentences."""

    if not text:
        return ""
    sentences = _SENTENCE_SPLIT_RE.split(text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return " ".join(sentences[:max_sentences])


def process_article(raw_article: Dict[str, Any]) -> Dict[str, Any]:
    """Normalise a raw article into NewsKoo's internal representation."""

    title = clean_text(raw_article.get("title"))
    description = clean_text(raw_article.get("description"))
    content = clean_text(
        raw_article.get("content") or raw_article.get("body") or description
    )
    summary = summarise_text(content or description, max_sentences=2)
    source_name = ""
    source = raw_article.get("source")
    if isinstance(source, dict):
        source_name = source.get("name", "")
    elif isinstance(source, str):
        source_name = source

    processed = {
        "title": title,
        "description": description,
        "content": content,
        "summary": summary,
        "source": source_name,
        "url": raw_article.get("url", ""),
        "published_at": raw_article.get("publishedAt") or raw_article.get("published_at"),
    }
    logger.debug("Processed article '%s' from source '%s'", title, source_name)
    return processed


__all__ = ["clean_text", "summarise_text", "process_article"]
