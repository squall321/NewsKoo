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
    gpu_seconds: int
    api_calls: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(slots=True)
class GuardrailBudgetSnapshot:
    """Represents weekly GPU/API consumption against guardrail budgets."""

    window: str
    gpu_seconds_budget: int
    gpu_seconds_used: int
    api_calls_budget: int
    api_calls_used: int

    @property
    def gpu_seconds_remaining(self) -> int:
        return max(self.gpu_seconds_budget - self.gpu_seconds_used, 0)

    @property
    def api_calls_remaining(self) -> int:
        return max(self.api_calls_budget - self.api_calls_used, 0)

    @property
    def is_within_budget(self) -> bool:
        return (
            self.gpu_seconds_used <= self.gpu_seconds_budget
            and self.api_calls_used <= self.api_calls_budget
        )

    def to_dict(self) -> dict:
        return {
            "window": self.window,
            "gpu_seconds": {
                "budget": self.gpu_seconds_budget,
                "used": self.gpu_seconds_used,
                "remaining": self.gpu_seconds_remaining,
            },
            "api_calls": {
                "budget": self.api_calls_budget,
                "used": self.api_calls_used,
                "remaining": self.api_calls_remaining,
            },
            "status": "within_budget" if self.is_within_budget else "over_budget",
        }


class TransparencyLogService:
    """Simple in-memory service to expose recent transparency logs."""

    GPU_SECONDS_WEEKLY_BUDGET = 6 * 60 * 60  # 6 GPU hours/week per guardrail plan
    API_CALLS_WEEKLY_BUDGET = 10  # guardrail doc: keep paid API usage exceptional

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
                gpu_seconds=340,
                api_calls=0,
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
                gpu_seconds=415,
                api_calls=0,
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
                gpu_seconds=520,
                api_calls=1,
            ),
        ]

    def list_entries(self, limit: int | None = None) -> list[dict]:
        data = self._entries[:limit] if limit else self._entries
        return [entry.to_dict() for entry in data]

    @property
    def total_entries(self) -> int:
        return len(self._entries)

    def guardrail_snapshot(self) -> GuardrailBudgetSnapshot:
        gpu_used = sum(entry.gpu_seconds for entry in self._entries)
        api_used = sum(entry.api_calls for entry in self._entries)
        return GuardrailBudgetSnapshot(
            window="rolling-7d",
            gpu_seconds_budget=self.GPU_SECONDS_WEEKLY_BUDGET,
            gpu_seconds_used=gpu_used,
            api_calls_budget=self.API_CALLS_WEEKLY_BUDGET,
            api_calls_used=api_used,
        )
