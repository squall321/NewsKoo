"""Application entrypoint."""
from __future__ import annotations

from wsgiref.simple_server import make_server

from backend.src.config.settings import settings
from backend.src.middleware.logging import (
    configure_logging,
    error_handling_middleware,
    request_logging_middleware,
)
from backend.src.routes import register_routes
from backend.src.server import Application, Request, Response


def create_app() -> Application:
    configure_logging(settings.log_level)

    app = Application()

    def root_handler(_: Request) -> Response:
        return Response.json({"app": settings.app_name, "environment": settings.app_env})

    app.add_route("GET", "/", root_handler)
    register_routes(app)

    app.add_middleware(error_handling_middleware())
    app.add_middleware(request_logging_middleware())
    return app


app = create_app()


def run_server() -> None:
    with make_server(settings.app_host, settings.app_port, app) as server:
        print(f"Server running at http://{settings.app_host}:{settings.app_port}")
        server.serve_forever()


if __name__ == "__main__":
    run_server()
