import unittest

from backend.src.main import create_app
from backend.src.server import Request


class RevenueRoutesTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_phase_eight_revenue_endpoint_exposes_hypotheses(self):
        request = Request(method="GET", path="/revenue/phase-008", headers={}, body=b"")
        response = self.app.handle(request)

        self.assertEqual(response.status_code, 200)
        payload = response.json_body()
        plan = payload["plan"]
        self.assertEqual(plan["phase"], "008")
        self.assertEqual(len(plan["hypotheses"]), 3)
        self.assertEqual(len(plan["experiments"]), 3)
        self.assertIn("translation-guardrails.md", plan["guardrails"]["reference_doc"])
        self.assertEqual(payload["meta"]["hypotheses"], 3)
        self.assertEqual(payload["meta"]["experiments"], 3)


if __name__ == "__main__":
    unittest.main()
