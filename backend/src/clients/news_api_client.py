"""HTTP client abstractions for communicating with external news APIs."""
from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

logger = logging.getLogger(__name__)


class NewsAPIError(RuntimeError):
    """Raised when the remote news API returns an error response."""


@dataclass(frozen=True)
class Article:
    """Representation of an article returned by the remote provider."""

    title: str
    description: str
    content: str
    url: str
    source: str
    published_at: Optional[datetime]


class NewsAPIClient:
    """Thin wrapper around a REST based news provider.

    Parameters
    ----------
    base_url:
        The base URL of the provider, for example ``https://newsapi.org/v2``.
    api_key:
        API key used for authenticating requests.
    opener:
        Optional callable compatible with :func:`urllib.request.urlopen` that
        can be injected for testing.
    max_retries:
        Number of times a failing HTTP request should be retried before the
        client gives up.
    backoff_factor:
        Determines how long the client waits between retries. The delay grows
        exponentially using ``backoff_factor * (2 ** attempt)``.
    timeout:
        Timeout in seconds for the underlying HTTP request.
    """

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        opener: Optional[Callable[..., Any]] = None,
        max_retries: int = 3,
        backoff_factor: float = 0.8,
        timeout: int = 15,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self._opener = opener or urlopen
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.timeout = timeout

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def fetch_top_headlines(
        self,
        *,
        country: Optional[str] = None,
        category: Optional[str] = None,
        query: Optional[str] = None,
        page_size: int = 20,
    ) -> List[Dict[str, Any]]:
        """Fetch the provider's top headlines.

        Returns a list of article dictionaries in the format provided by the
        upstream API. The caller can further process the entries using the
        :mod:`backend.src.services.article_processor` utilities.
        """

        params = {
            "apiKey": self.api_key,
            "country": country,
            "category": category,
            "q": query,
            "pageSize": page_size,
        }
        return self._request_with_retry("/top-headlines", params=params)

    def fetch_everything(
        self,
        *,
        query: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        language: Optional[str] = None,
        sort_by: Optional[str] = None,
        page_size: int = 20,
    ) -> List[Dict[str, Any]]:
        """Fetch articles that match the supplied query."""

        params = {
            "apiKey": self.api_key,
            "q": query,
            "from": from_date,
            "to": to_date,
            "language": language,
            "sortBy": sort_by,
            "pageSize": page_size,
        }
        return self._request_with_retry("/everything", params=params)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _request_with_retry(
        self, endpoint: str, *, params: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        params = {k: v for k, v in (params or {}).items() if v is not None}
        url = f"{self.base_url}{endpoint}"

        for attempt in range(1, self.max_retries + 1):
            try:
                full_url = f"{url}?{urlencode(params)}" if params else url
                logger.debug("News API request %s params=%s", full_url, params)
                with self._opener(full_url, timeout=self.timeout) as response:
                    payload = json.loads(response.read().decode("utf-8"))
                if payload.get("status") != "ok":
                    raise NewsAPIError(json.dumps(payload))
                articles = payload.get("articles", [])
                logger.info("Fetched %s articles from %s", len(articles), endpoint)
                return articles
            except (HTTPError, URLError, ValueError) as exc:
                logger.warning(
                    "Attempt %s/%s failed for %s: %s", attempt, self.max_retries, endpoint, exc
                )
                if attempt == self.max_retries:
                    logger.error("Giving up on endpoint %s after %s attempts", endpoint, attempt)
                    raise
                self._backoff(attempt)
        return []

    def _backoff(self, attempt: int) -> None:
        sleep_time = self.backoff_factor * (2 ** (attempt - 1))
        logger.debug("Backing off for %.2f seconds", sleep_time)
        time.sleep(sleep_time)


class SampleNewsAPIClient(NewsAPIClient):
    """Client that serves deterministic fixture data for local testing.

    The class inherits from :class:`NewsAPIClient` to make it a drop-in
    replacement while overriding the network calls. It is helpful for running
    the fetch job locally without providing real credentials.
    """

    def __init__(self) -> None:
        super().__init__(base_url="https://example.com", api_key="demo")
        self._sample_articles = [
            {
                "title": "Demo article about AI humor",
                "description": "A lightweight example showing how jokes are collected.",
                "content": "<p>Agents scour the web for lighthearted content.</p>",
                "url": "https://example.com/articles/ai-humor",
                "source": {"name": "Example Times"},
                "publishedAt": datetime.utcnow().isoformat(),
            },
            {
                "title": "Robots now appreciate puns",
                "description": "An upbeat exploration of robotic comedy clubs.",
                "content": "Puns are now their favorite form of entertainment.",
                "url": "https://example.com/articles/robot-puns",
                "source": {"name": "Robotics Daily"},
                "publishedAt": datetime.utcnow().isoformat(),
            },
        ]

    def _request_with_retry(
        self, endpoint: str, *, params: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        logger.info("Sample client returning %s fixture articles", len(self._sample_articles))
        return list(self._sample_articles)
