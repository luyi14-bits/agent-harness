# Tasks — TASK-003

- [ ] Task 1: SkillDef + SkillParser body 保留
  - [ ] SkillDef 新增 body/agent_name 字段
  - [ ] SkillParser 提取 body 全文
  - [ ] 测试：解析后 body 正确

- [ ] Task 2: 全局约束层
  - [ ] 新建 `core/global_constraints.py`
  - [ ] 包含：越权禁止/交接协议/留痕规则/安全红线

- [ ] Task 3: AgentFactory 双层 prompt 组装
  - [ ] 修改 `_build_role_preset()`：优先用 body
  - [ ] 支持多 skill 拼接（attached_skills）
  - [ ] CLI `--attach` 参数

- [ ] Task 4: Agent 自动留痕
  - [ ] Agent 新增 `write_log()` 方法
  - [ ] 自动调用时机：prepare_handover 后

- [ ] Task 5: Dispatcher 群聊入口
  - [ ] 新建 `orchestrator/dispatcher.py`
  - [ ] CLI `--chat` 模式

- [ ] Task 6: Code-Review Agent
  - [ ] 创建 `skills/Luyi14-code-review/SKILL.md`
  - [ ] CR 四维度审查：style/bug/security/performance

# Dependencies
- Task 1 无依赖
- Task 2 无依赖
- Task 3 depends on Task 1+2
- Task 4 depends on Task 3
- Task 5 无依赖
- Task 6 无依赖
- Task 1 和 Task 2 可并行

# 工时估算
| Task | 子任务 | 人天 |
|------|:-----:|:----:|
| Task 1 | 3 | 0.5 |
| Task 2 | 1 | 0.25 |
| Task 3 | 3 | 0.75 |
| Task 4 | 2 | 0.25 |
| Task 5 | 2 | 0.5 |
| Task 6 | 2 | 0.5 |
| **合计** | **13** | **2.75** |
