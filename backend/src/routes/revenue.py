"""Routes for Phase 008 revenue hypotheses."""
from __future__ import annotations

from backend.src.server import Application, Request, Response
from backend.src.services.revenue import phase_eight_revenue_service


def register_routes(app: Application) -> None:
    app.add_route("GET", "/revenue/phase-008", get_phase_eight_revenue)


def get_phase_eight_revenue(_: Request) -> Response:
    plan = phase_eight_revenue_service.plan
    payload = {
        "plan": plan,
        "meta": {
            "phase": plan["phase"],
            "hypotheses": len(plan["hypotheses"]),
            "experiments": len(plan["experiments"]),
            "guardrail_ref": plan["guardrails"]["reference_doc"],
        },
    }
    return Response.json(payload)
