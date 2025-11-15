import unittest

from backend.src.main import create_app
from backend.src.server import Request


class TransparencyRouteTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_transparency_logs_endpoint_returns_entries(self):
        request = Request(method="GET", path="/transparency/logs", headers={}, body=b"")
        response = self.app.handle(request)

        self.assertEqual(response.status_code, 200)
        payload = response.json_body()
        self.assertIn("items", payload)
        self.assertIn("meta", payload)
        self.assertGreaterEqual(len(payload["items"]), 1)
        self.assertEqual(payload["meta"]["total"], len(payload["items"]))


if __name__ == "__main__":
    unittest.main()
