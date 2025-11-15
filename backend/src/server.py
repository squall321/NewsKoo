"""Lightweight HTTP application framework for the NewsKoo backend."""
from __future__ import annotations

import json
from dataclasses import dataclass
from http import HTTPStatus
from typing import Callable, Dict, List, Tuple


@dataclass
class Request:
    method: str
    path: str
    headers: Dict[str, str]
    body: bytes

    @classmethod
    def from_environ(cls, environ: Dict[str, str]) -> "Request":
        method = environ.get("REQUEST_METHOD", "GET").upper()
        path = environ.get("PATH_INFO", "/")
        length = int(environ.get("CONTENT_LENGTH") or 0)
        body = environ["wsgi.input"].read(length) if length else b""
        headers = {
            key[5:].replace("_", "-").title(): value
            for key, value in environ.items()
            if key.startswith("HTTP_")
        }
        return cls(method=method, path=path, headers=headers, body=body)


@dataclass
class Response:
    status_code: int
    headers: Dict[str, str]
    body: bytes

    @classmethod
    def json(cls, payload: Dict[str, str], status_code: int = 200) -> "Response":
        return cls(
            status_code=status_code,
            headers={"Content-Type": "application/json"},
            body=json.dumps(payload).encode("utf-8"),
        )

    def json_body(self) -> Dict[str, str]:
        return json.loads(self.body.decode("utf-8"))


Handler = Callable[[Request], Response]
Middleware = Callable[[Request, Handler], Response]


class Application:
    def __init__(self) -> None:
        self._routes: Dict[Tuple[str, str], Handler] = {}
        self._middleware: List[Middleware] = []

    def add_route(self, method: str, path: str, handler: Handler) -> None:
        self._routes[(method.upper(), path)] = handler

    def add_middleware(self, middleware: Middleware) -> None:
        self._middleware.append(middleware)

    def _dispatch(self, request: Request) -> Response:
        handler = self._routes.get((request.method.upper(), request.path))
        if handler is None:
            return Response(
                status_code=HTTPStatus.NOT_FOUND,
                headers={"Content-Type": "application/json"},
                body=json.dumps({"detail": "Not Found"}).encode("utf-8"),
            )
        return handler(request)

    def handle(self, request: Request) -> Response:
        handler: Handler = self._dispatch
        for middleware in reversed(self._middleware):
            next_handler = handler

            def handler(req: Request, middleware=middleware, next_handler=next_handler):
                return middleware(req, next_handler)

        return handler(request)

    def wsgi_app(self, environ, start_response):
        request = Request.from_environ(environ)
        response = self.handle(request)
        status_text = f"{response.status_code} {HTTPStatus(response.status_code).phrase}"
        headers = list(response.headers.items())
        start_response(status_text, headers)
        return [response.body]

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)
