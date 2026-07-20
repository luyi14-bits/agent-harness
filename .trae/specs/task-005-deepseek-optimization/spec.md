# TASK-005: DeepSeek 深度优化 Spec

## Why
DeepSeek 集成当前无成本感知、FC 错误不自愈、reasoning 不可控。不解决这三个问题，AgentHarness 无法进入 awesome-deepseek-agent 官方列表。

## Requirements

### RQ-COST-001: CostAwareRouter
- **GIVEN** 一个短查询（<100 字）
- **WHEN** 调用 ModelRouter
- **THEN** 默认路由到 Flash
- **AND** Token 预算超限时熔断

### RQ-REPAIR-001: Tool-Call Repair
- **GIVEN** FC 返回 `\`\`\`json\n{"name":"t"}\n\`\`\``
- **WHEN** repair_function_call 执行
- **THEN** 去除代码块标记并返回有效 JSON

### RQ-EFFORT-001: reasoning_effort
- **GIVEN** Agent config 设置 reasoning_effort="low"
- **WHEN** 组装 API 请求
- **THEN** 请求中包含 reasoning_effort="low"
