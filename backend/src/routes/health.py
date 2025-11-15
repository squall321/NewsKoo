"""Health check route."""
from backend.src.server import Application, Request, Response


def register_routes(app: Application) -> None:
    app.add_route("GET", "/health", health_check)


def health_check(_: Request) -> Response:
    return Response.json({"status": "ok"})
