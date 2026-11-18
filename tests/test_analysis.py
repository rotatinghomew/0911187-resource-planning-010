import unittest

from resource_planning.analysis import summarize
from resource_planning.reports import build_report


class ResourcePlanningTests(unittest.TestCase):
    def setUp(self):
        self.records = [
            {"id": "r1", "kind": "request", "period": "2026-S1", "resource": "method-course", "student_id": "s1"},
            {"id": "r2", "kind": "request", "period": "2026-S1", "resource": "method-course", "student_id": "s2"},
            {"id": "c1", "kind": "cancel", "period": "2026-S1", "resource": "method-course", "student_id": "s2"},
            {"id": "cap1", "kind": "capacity", "period": "2026-S1", "resource": "method-course", "slots": 1},
            {"id": "serve1", "kind": "served", "period": "2026-S1", "resource": "method-course", "student_id": "s1"},
            {"id": "plan1", "kind": "plan", "period": "2026-S1", "resource": "method-course", "slots": 3},
        ]

    def test_cancellations_change_active_demand_not_historical_request_count(self):
        result = summarize(self.records)["method-course:2026-S1"]
        self.assertEqual(result["requesters"], 2)
        self.assertEqual(result["active_requesters"], 1)
        self.assertEqual(result["waitlist_proxy"], 0)

    def test_plan_and_realized_capacity_remain_distinct(self):
        report = build_report(self.records, "plan-r2")
        row = report["periods"]["method-course:2026-S1"]
        self.assertEqual(row["planned_slots"], 3)
        self.assertEqual(row["capacity_slots"], 1)
        self.assertEqual(row["service_rate_among_requesters"], 1)


if __name__ == "__main__":
    unittest.main()
