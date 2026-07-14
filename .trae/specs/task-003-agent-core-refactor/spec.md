# TASK-003: Agent 核心重构 Spec

## Why
Agent 当前只有一句话 prompt（ROLE_PRESETS），SKILL.md 的 body 正文被丢弃。用户不能自定义 Agent 名、不能挂载多个 skill、无群聊入口、无代码审查环节。

## Meta
- **优先级**: P0
- **估算工时**: 3 人天
- **PRD 来源**: `docs/prd/task-003-agent-core-refactor-prd.md`

## Requirements

### RQ-BODY-001: SkillParser 保留 body
- **WHEN** 解析 SKILL.md
- **THEN** body 存入 SkillDef.body，frontmatter 支持 agent_name
- **Scenario**: 解析后 skill.body 包含 frontmatter 之后的正文全文

### RQ-PROMPT-001: 双层 prompt 组装
- **WHEN** AgentFactory 创建 Agent
- **THEN** prompt 顺序：全局约束 → 角色 body → N×skill body
- **Scenario**: `--attach` 后 CLI 显示完整组装 prompt

### RQ-DISPATCH-001: Dispatcher 群聊入口
- **WHEN** `--chat` 模式启动
- **THEN** 接收自然语言 → 路由 PM Agent
- **Scenario**: 输入"做一个登录功能" → 启动 SOP 管道

### RQ-CR-001: Code-Review Agent
- **WHEN** Coding 完成 → CR Agent 收到交接
- **THEN** 审查代码 → 产出 CR Report
- **Scenario**: CR Report 包含 style/bug/security/performance 四维度评价

### RQ-LOG-001: Agent 自动留痕
- **WHEN** Agent 完成任务
- **THEN** 自动追加 LOG.md
- **Scenario**: 执行后 skill 目录下 LOG.md 有新增条目

### RQ-NAME-001: 自定义显示名
- **WHEN** frontmatter 含 agent_name
- **THEN** CLI 和日志显示此名称
- **Scenario**: frontmatter name="pm-agent" agent_name="PM 经理" → 显示"PM 经理"
