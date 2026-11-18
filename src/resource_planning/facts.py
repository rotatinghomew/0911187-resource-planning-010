"""读取资源需求、供给容量、实际服务与计划记录。"""

import json
from pathlib import Path


def load_records(path):
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("记录文件必须包含数组")
    records = []
    seen = set()
    for position, record in enumerate(payload):
        if not isinstance(record, dict) or not record.get("id") or not record.get("period"):
            raise ValueError(f"第 {position + 1} 条资源记录缺少 id 或 period")
        if record["id"] in seen:
            raise ValueError(f"重复记录标识：{record['id']}")
        seen.add(record["id"])
        if record.get("kind") not in {"request", "booking", "cancel", "served", "capacity", "plan"}:
            raise ValueError(f"记录 {record['id']} 的 kind 无效")
        records.append(dict(record))
    return records
