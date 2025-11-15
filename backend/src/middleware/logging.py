"""Logging and error handling middleware utilities."""
from __future__ import annotations

import logging
import time
from typing import Callable

from backend.src.server import Middleware, Request, Response


def configure_logging(log_level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )


def request_logging_middleware() -> Middleware:
    logger = logging.getLogger("app.requests")

    def middleware(request: Request, call_next: Callable[[Request], Response]) -> Response:
        start = time.perf_counter()
        response = call_next(request)
        duration = (time.perf_counter() - start) * 1000
        logger.info("%s %s -> %s (%.2fms)", request.method, request.path, response.status_code, duration)
        response.headers.setdefault("X-Process-Time", f"{duration:.2f}ms")
        return response

    return middleware


def error_handling_middleware() -> Middleware:
    logger = logging.getLogger("app.errors")

    def middleware(request: Request, call_next: Callable[[Request], Response]) -> Response:
        try:
            return call_next(request)
        except Exception:  # pragma: no cover - defensive guard
            logger.exception("Unhandled error while processing %s", request.path)
            return Response.json({"detail": "Internal server error"}, status_code=500)

    return middleware
