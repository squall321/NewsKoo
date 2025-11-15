"""Route registration helpers."""
from __future__ import annotations

from backend.src.server import Application

from . import health, transparency


def register_routes(app: Application) -> None:
    """Register all route groups for the application."""
    health.register_routes(app)
    transparency.register_routes(app)
