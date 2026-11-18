# 支持资源规划

课程、平台时段和导师支持按学期记录申请和实际服务。

## 数据约定

应用使用本地合成记录，输入为 UTF-8 JSON。每条记录都应有稳定的业务标识；日期采用 ISO 8601 格式。缺失值表示未观察到，不解释为数值零。输入校验、领域整理和结果汇总彼此分离，调用方可通过 Python API 使用。

## 运行与测试

需要 Python 3.11 或更新版本，不依赖外部服务。执行 `python -m unittest discover -s tests -v` 运行测试。将 `src` 加入 `PYTHONPATH` 后可导入 `resource_planning`；核心示例见 `examples/sample.json`。

## 目录

- `src/resource_planning/`：记录读取、领域计算及结果汇总。
- `examples/`：本地合成数据。
- `tests/`：输入边界与当前业务口径测试。
