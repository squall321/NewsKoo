"""Routes that expose the Phase 003-007 readiness payload."""
from __future__ import annotations

from collections import Counter

from backend.src.server import Application, Request, Response
from backend.src.services.phase_readiness import phase_readiness_service


def register_routes(app: Application) -> None:
    app.add_route("GET", "/phases/progress", list_phase_progress)
    app.add_route("GET", "/phases/readiness", readiness_snapshot)


def list_phase_progress(_: Request) -> Response:
    phases = phase_readiness_service.list_phase_progress()
    status_counts = Counter(phase["status"] for phase in phases)
    payload = {
        "phases": phases,
        "meta": {
            "count": len(phases),
            "statuses": dict(status_counts),
            "implemented": status_counts.get("implemented", 0),
        },
    }
    return Response.json(payload)


def readiness_snapshot(_: Request) -> Response:
    snapshot = phase_readiness_service.readiness_snapshot
    payload = {
        "snapshot": snapshot,
        "meta": {
            "segments": len(snapshot.get("segments", [])),
            "categories": len(snapshot.get("categories", {}).get("metadata", [])),
        },
    }
    return Response.json(payload)
