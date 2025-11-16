"""Routes exposing the phase-014~020 strategic payloads."""
from __future__ import annotations

from backend.src.server import Application, Request, Response
from backend.src.services.phase_strategy import phase_strategy_service


def register_routes(app: Application) -> None:
    app.add_route("GET", "/phases/014-020", list_phase_strategy_014_020)
    app.add_route("GET", "/phases/021-027", list_phase_strategy_021_027)


def list_phase_strategy_014_020(_: Request) -> Response:
    return _build_response_for_range(14, 20)


def list_phase_strategy_021_027(_: Request) -> Response:
    return _build_response_for_range(21, 27)


def _build_response_for_range(start: int, end: int) -> Response:
    plans = phase_strategy_service.list_plans(start, end)
    payload = {
        "plans": plans,
        "meta": {
            "count": len(plans),
            "phase_range": [start, end],
            "storage_roots": sorted({plan["storage_path"] for plan in plans}),
        },
    }
    return Response.json(payload)

