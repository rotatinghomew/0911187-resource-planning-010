"""区分资源申请、可用容量和实际服务并回看计划。"""

from collections import defaultdict
from .demand import demand_counts
from .supply import slot_totals


def summarize(records):
    resources = defaultdict(list)
    for record in records:
        resources[(str(record.get("resource", "unknown")), str(record["period"]))].append(record)
    result = {}
    for (resource, period), events in sorted(resources.items()):
        served = {str(row.get("student_id")) for row in events if row["kind"] == "served" and row.get("student_id")}
        demand = demand_counts(events)
        supply = slot_totals(events)
        active_requests = demand["active_requesters"]
        active_student_ids = demand.pop("active_student_ids")
        result[f"{resource}:{period}"] = {
            **demand,
            "served_students": len(served),
            **supply,
            "waitlist_proxy": max(0, active_requests - supply["capacity_slots"]) if supply["capacity_slots"] is not None else None,
            "service_rate_among_requesters": len(served & active_student_ids) / len(active_student_ids) if active_student_ids else None,
        }
    return result
