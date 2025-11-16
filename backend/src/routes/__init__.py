"""Route registration helpers."""
from __future__ import annotations

from backend.src.server import Application

from . import health, phase_strategy, phases, revenue, transparency


def register_routes(app: Application) -> None:
    """Register all route groups for the application."""
    health.register_routes(app)
    transparency.register_routes(app)
    phases.register_routes(app)
    phase_strategy.register_routes(app)
    revenue.register_routes(app)
