"""区分申请历史与取消后的当前需求人数。"""


def demand_counts(events):
    requested = {str(row["student_id"]) for row in events if row["kind"] in {"request", "booking"} and row.get("student_id")}
    cancelled = {str(row["student_id"]) for row in events if row["kind"] == "cancel" and row.get("student_id")}
    active = requested - cancelled
    return {"requesters": len(requested), "active_requesters": len(active), "active_student_ids": active}
