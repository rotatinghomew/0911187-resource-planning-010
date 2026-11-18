"""汇总实际开放容量和决策时计划名额。"""


def slot_totals(events):
    capacity = [row["slots"] for row in events if row["kind"] == "capacity" and isinstance(row.get("slots"), (int, float))]
    planned = [row["slots"] for row in events if row["kind"] == "plan" and isinstance(row.get("slots"), (int, float))]
    return {
        "capacity_slots": sum(float(value) for value in capacity) if capacity else None,
        "planned_slots": sum(float(value) for value in planned) if planned else None,
    }
