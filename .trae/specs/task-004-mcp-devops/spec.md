# TASK-004: MCP + DevOps Spec

## RQ-TOOL-001: PreToolUse 硬约束
- **WHEN** Agent 调用工具
- **THEN** 检查 whitelist/denylist → 拦截非法调用
- **Scenario**: Acceptance Agent 调用 Write → 拦截

## RQ-MCP-001: MCP 客户端
- **WHEN** Agent 需搜索网页
- **THEN** 调用 web-search MCP
- **Scenario**: `search_web("latest Python")` → 返回结果

## RQ-DEVOPS-001: DevOps Agent
- **WHEN** 验收通过
- **THEN** DevOps 构建 → 打包 → tag → release
- **Scenario**: `build()` → `pack()` → `git_tag()` → `release()`
