# TASK-004: MCP 工具集成 + DevOps Agent PRD

## 1. Executive Summary
为 Agent 引入三层工具硬约束（tools 白名单 / deny 黑名单 / PreToolUse hooks），集成 MCP 协议支持外部工具，新增 DevOps Agent 完成构建发布。

## 2. User Stories

### Story 1: 工具硬约束
- **WHEN** Acceptance Agent 尝试调用 Write 工具
- **THEN** PreToolUse 拦截 → 记录违规日志 → 拒绝执行

### Story 2: MCP web-search
- **WHEN** PM Agent 做竞品分析
- **THEN** 调用 web-search MCP 搜索同类产品

### Story 3: DevOps 构建发布
- **WHEN** 验收通过
- **THEN** DevOps Agent 构建 → 打包 → tag → release → 验证

## 3. FR
- FR-1: Tool硬约束（whitelist/denylist/PreToolUse hook）
- FR-2: MCP客户端模块（web-search内置）
- FR-3: DevOps Agent（SKILL.md + 构建/打包/发布/回滚）
- FR-4: SOP 管道更新（Acceptance → DevOps → Secretary）

## 4. Out of Scope
- Tauri桌面（下一迭代）
