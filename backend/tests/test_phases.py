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
        self.assertEqual(payload["meta"]["count"], 6)
        self.assertEqual(payload["meta"]["implemented"], 5)

        statuses = {phase["identifier"]: phase["status"] for phase in payload["phases"]}
        self.assertEqual(sum(1 for status in statuses.values() if status == "documented"), 1)
        self.assertEqual(statuses.get("phase-011"), "documented")
        self.assertTrue(
            all(
                status == "implemented"
                for identifier, status in statuses.items()
                if identifier != "phase-011"
            )
        )

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
        self.assertIn("phase_011", snapshot)
        self.assertIn("risks", snapshot["phase_011"])
        self.assertIn("issues", snapshot["phase_011"])

    def test_phase_strategy_endpoint_exposes_phase_014_to_020(self):
        request = Request(method="GET", path="/phases/014-020", headers={}, body=b"")
        response = self.app.handle(request)

        self.assertEqual(response.status_code, 200)
        payload = response.json_body()
        self.assertEqual(payload["meta"]["count"], 7)
        self.assertEqual(payload["meta"]["phase_range"], [14, 20])
        self.assertEqual(len(payload["meta"]["storage_roots"]), 7)

        plans = payload["plans"]
        identifiers = [plan["identifier"] for plan in plans]
        self.assertIn("phase-014", identifiers)
        self.assertIn("phase-020", identifiers)

        phase_014 = plans[0]
        self.assertIn("tasks", phase_014)
        self.assertGreaterEqual(len(phase_014["tasks"]), 4)
        self.assertIn("notes", phase_014)
        self.assertIn("docs/records/phase-014/", phase_014["notes"][0])
        for plan in plans:
            self.assertIn("guardrails", plan)
            self.assertIn("reference_doc", plan["guardrails"])
            self.assertIn("notes", plan)
            self.assertGreaterEqual(len(plan["notes"]), 1)

    def test_architecture_strategy_endpoint_exposes_phase_021_to_027(self):
        request = Request(method="GET", path="/phases/021-027", headers={}, body=b"")
        response = self.app.handle(request)

        self.assertEqual(response.status_code, 200)
        payload = response.json_body()
        self.assertEqual(payload["meta"]["phase_range"], [21, 27])
        self.assertEqual(payload["meta"]["count"], 7)
        self.assertEqual(len(payload["plans"]), 7)

        identifiers = {plan["identifier"] for plan in payload["plans"]}
        self.assertIn("phase-021", identifiers)
        self.assertIn("phase-027", identifiers)

        first_plan = payload["plans"][0]
        self.assertIn("tasks", first_plan)
        self.assertGreaterEqual(len(first_plan["tasks"]), 4)
        self.assertTrue(all("guardrails" in plan for plan in payload["plans"]))
        self.assertTrue(all("notes" in plan for plan in payload["plans"]))
        self.assertTrue(all(len(plan["notes"]) >= 2 for plan in payload["plans"]))


if __name__ == "__main__":
    unittest.main()
