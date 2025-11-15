"""Routes exposing the transparency log prototype required by Phase 002."""
from __future__ import annotations

from backend.src.server import Application, Request, Response
from backend.src.services.transparency import TransparencyLogService

_service = TransparencyLogService()


def register_routes(app: Application) -> None:
    app.add_route("GET", "/transparency/logs", list_logs)


def list_logs(_: Request) -> Response:
    payload = {
        "items": _service.list_entries(limit=10),
        "meta": {
            "total": _service.total_entries,
            "limit": 10,
            "guardrails": "docs/strategy/translation-guardrails.md",
            "guardrail_budget": _service.guardrail_snapshot().to_dict(),
        },
    }
    return Response.json(payload)
