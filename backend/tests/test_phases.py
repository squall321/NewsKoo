import unittest

from backend.src.main import create_app
from backend.src.server import Request


class PhaseRoutesTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_phase_progress_lists_all_implemented_phases(self):
        request = Request(method="GET", path="/phases/progress", headers={}, body=b"")
        response = self.app.handle(request)

        self.assertEqual(response.status_code, 200)
        payload = response.json_body()
        self.assertEqual(payload["meta"]["count"], 5)
        self.assertEqual(payload["meta"]["implemented"], 5)
        self.assertTrue(all(phase["status"] == "implemented" for phase in payload["phases"]))

    def test_phase_readiness_snapshot_contains_segments_and_categories(self):
        request = Request(method="GET", path="/phases/readiness", headers={}, body=b"")
        response = self.app.handle(request)

        self.assertEqual(response.status_code, 200)
        payload = response.json_body()
        snapshot = payload["snapshot"]
        self.assertGreaterEqual(payload["meta"]["segments"], 5)
        self.assertIn("categories", snapshot)
        self.assertIn("metadata", snapshot["categories"])
        self.assertIn("performance", snapshot["categories"])


if __name__ == "__main__":
    unittest.main()
