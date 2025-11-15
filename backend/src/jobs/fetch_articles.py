"""Background job that periodically fetches and processes articles."""
from __future__ import annotations

import logging
import threading
import time
from typing import Any, Callable, Dict, List, Optional

from backend.src.clients.news_api_client import NewsAPIClient
from backend.src.services.article_processor import process_article

logger = logging.getLogger(__name__)

ProcessedArticle = Dict[str, Any]
ArticleProcessor = Callable[[Dict[str, Any]], ProcessedArticle]


class ArticleFetchJob:
    """Encapsulates the periodic article ingestion workflow."""

    def __init__(
        self,
        client: NewsAPIClient,
        *,
        processor: ArticleProcessor = process_article,
        query: Optional[str] = None,
        country: Optional[str] = "us",
        category: Optional[str] = None,
        interval_seconds: int = 900,
    ) -> None:
        self.client = client
        self.processor = processor
        self.query = query
        self.country = country
        self.category = category
        self.interval_seconds = interval_seconds
        self._stop_event = threading.Event()

    # ------------------------------------------------------------------
    def run_once(self) -> List[ProcessedArticle]:
        """Fetch and process a batch of articles once."""

        logger.info(
            "Starting fetch cycle query=%s country=%s category=%s",
            self.query,
            self.country,
            self.category,
        )
        raw_articles = self.client.fetch_top_headlines(
            country=self.country, category=self.category, query=self.query
        )
        processed: List[ProcessedArticle] = []
        for raw_article in raw_articles:
            try:
                processed_article = self.processor(raw_article)
                processed.append(processed_article)
            except Exception:  # pragma: no cover - defensive guard
                logger.exception("Failed to process article: %s", raw_article)
        logger.info("Processed %s articles", len(processed))
        return processed

    # ------------------------------------------------------------------
    def start(self) -> None:
        """Start the scheduler loop. Blocks until :meth:`stop` is called."""

        logger.info(
            "Launching ArticleFetchJob interval=%ss query=%s country=%s category=%s",
            self.interval_seconds,
            self.query,
            self.country,
            self.category,
        )
        while not self._stop_event.is_set():
            cycle_started = time.monotonic()
            try:
                processed = self.run_once()
                logger.debug("Fetched batch summary: %s", processed[:2])
            except Exception:
                logger.exception("Fetch cycle failed")
            finally:
                elapsed = time.monotonic() - cycle_started
                wait_for = max(0, self.interval_seconds - elapsed)
                logger.debug("Waiting %.2fs before next cycle", wait_for)
                self._stop_event.wait(wait_for)

    def stop(self) -> None:
        """Signal the scheduler loop to stop."""

        logger.info("Stop signal received for ArticleFetchJob")
        self._stop_event.set()


__all__ = ["ArticleFetchJob"]
