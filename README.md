# 科研支持资源规划

项目整理研究生对方法课程、实验平台等资源的申请、预约取消、实际服务、开放容量和计划名额。每条本地合成 JSON 记录包含稳定 `id`、`period` 和事件 `kind`；申请人数、供给容量与服务人数分别核算。

容量缺失时不会推断等待人数为零，已取消申请保留在历史申请数中但退出当前需求代理。当前实现比较单期申请和计划名额，不提供按学生阶段与项目类型校正的需求预测，也不保存发布时的预测依据。

需要 Python 3.11 或更新版本，不依赖外部服务。执行 `PYTHONPATH=src python -m unittest discover -s tests -v` 运行测试。`resource_planning.facts` 校验事件，`resource_planning.demand.demand_counts` 计算当前需求，`resource_planning.supply.slot_totals` 汇总容量与计划，`resource_planning.analysis.summarize` 对照供需与服务，`resource_planning.reports.build_report` 生成带修订号的阶段报告。样例见 `examples/sample.json`。
