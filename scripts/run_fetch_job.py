"""Entry point for executing the article fetch job locally."""
from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path

# Ensure the repository root is importable when the script is executed directly.
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from backend.src.clients.news_api_client import (  # noqa: E402  # isort:skip
    NewsAPIClient,
    SampleNewsAPIClient,
)
from backend.src.jobs.fetch_articles import ArticleFetchJob  # noqa: E402  # isort:skip


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the NewsKoo fetch job")
    parser.add_argument("--api-key", dest="api_key", default=os.getenv("NEWS_API_KEY"))
    parser.add_argument(
        "--base-url",
        dest="base_url",
        default=os.getenv("NEWS_API_BASE_URL", "https://newsapi.org/v2"),
    )
    parser.add_argument("--query", dest="query", default="humor")
    parser.add_argument("--country", dest="country", default="us")
    parser.add_argument("--category", dest="category", default=None)
    parser.add_argument(
        "--interval",
        dest="interval",
        type=int,
        default=900,
        help="Interval between fetch cycles in seconds (default 15 minutes)",
    )
    parser.add_argument(
        "--run-once",
        dest="run_once",
        action="store_true",
        help="Fetch a single batch and print the processed results",
    )
    parser.add_argument(
        "--use-sample-data",
        dest="use_sample",
        action="store_true",
        help="Use bundled fixture data instead of hitting the remote API",
    )
    parser.add_argument(
        "--log-level",
        dest="log_level",
        default=os.getenv("LOG_LEVEL", "INFO"),
        help="Python logging level (e.g. INFO, DEBUG)",
    )
    return parser.parse_args()


def build_client(args: argparse.Namespace) -> NewsAPIClient:
    if args.use_sample:
        return SampleNewsAPIClient()
    if not args.api_key:
        raise SystemExit(
            "An API key is required unless --use-sample-data is supplied or NEWS_API_KEY is set"
        )
    return NewsAPIClient(base_url=args.base_url, api_key=args.api_key)


def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=getattr(logging, str(args.log_level).upper(), logging.INFO),
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
    client = build_client(args)
    job = ArticleFetchJob(
        client,
        query=args.query,
        country=args.country,
        category=args.category,
        interval_seconds=args.interval,
    )

    if args.run_once:
        processed = job.run_once()
        for article in processed:
            print(f"- {article['title']} ({article['source']}) -> {article['summary']}")
        return

    try:
        job.start()
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt received; shutting down job")
        job.stop()


if __name__ == "__main__":
    main()
