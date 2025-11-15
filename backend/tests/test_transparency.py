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

        guardrail_budget = payload["meta"].get("guardrail_budget")
        self.assertIsNotNone(guardrail_budget)
        self.assertEqual(guardrail_budget["window"], "rolling-7d")
        self.assertEqual(guardrail_budget["status"], "within_budget")
        self.assertIn("gpu_seconds", guardrail_budget)
        self.assertIn("api_calls", guardrail_budget)


if __name__ == "__main__":
    unittest.main()
