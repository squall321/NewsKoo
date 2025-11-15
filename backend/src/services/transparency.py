"""Transparency log domain objects used by the public API."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import List


@dataclass(slots=True)
class TranslationLogEntry:
    """Represents a single translation/curation audit log."""

    log_id: str
    source_url: str
    language_pair: str
    model_name: str
    inference_time_ms: int
    reviewer: str
    status: str
    last_synced_at: str
    guardrail_notes: str

    def to_dict(self) -> dict:
        return asdict(self)


class TransparencyLogService:
    """Simple in-memory service to expose recent transparency logs."""

    def __init__(self, entries: List[TranslationLogEntry] | None = None) -> None:
        if entries is None:
            entries = self._seed_entries()
        self._entries = entries

    @staticmethod
    def _seed_entries() -> List[TranslationLogEntry]:
        now = datetime.now(timezone.utc)
        return [
            TranslationLogEntry(
                log_id="LOG-20240512-001",
                source_url="https://reddit.com/r/techhumor/comments/abcd12",
                language_pair="en->ko",
                model_name="LLM-Llama3-8B-Q4",
                inference_time_ms=820,
                reviewer="curation.ops+hana",
                status="approved",
                last_synced_at=now.isoformat(),
                guardrail_notes="translation-guardrails.md#style-conversion",
            ),
            TranslationLogEntry(
                log_id="LOG-20240512-002",
                source_url="https://twitter.com/funnyproduct/status/987654321",
                language_pair="en->ko",
                model_name="LLM-Llama3-8B-Q4",
                inference_time_ms=910,
                reviewer="curation.ops+min",
                status="needs_review",
                last_synced_at=now.isoformat(),
                guardrail_notes="flagged for tone polishing",
            ),
            TranslationLogEntry(
                log_id="LOG-20240512-003",
                source_url="https://producthunt.com/posts/meme-trends",
                language_pair="en->ko",
                model_name="LLM-NanoTranslate-13B-Q8",
                inference_time_ms=1010,
                reviewer="legal.review+partner",
                status="shared_with_partner",
                last_synced_at=now.isoformat(),
                guardrail_notes="partner export redacted user handles",
            ),
        ]

    def list_entries(self, limit: int | None = None) -> list[dict]:
        data = self._entries[:limit] if limit else self._entries
        return [entry.to_dict() for entry in data]

    @property
    def total_entries(self) -> int:
        return len(self._entries)
