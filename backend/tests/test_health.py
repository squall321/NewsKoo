import unittest

from backend.src.main import create_app
from backend.src.server import Request


class HealthRouteTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_health_endpoint_returns_ok(self):
        request = Request(method="GET", path="/health", headers={}, body=b"")
        response = self.app.handle(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json_body(), {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
