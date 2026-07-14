# 版本快照记录

## v0.3.0 (2026-07-14)
- **Agent 核心重构**：body保留 + 双层prompt + 全局约束 + 自动留痕
- **新增功能**：
  - SkillParser 保留 SKILL.md body 全文（PM Agent: 60字→4692字）
  - AgentFactory 双层 prompt：全局约束（共享）+ 角色 body（专属）+ N×skill 挂载
  - `--attach skill1,skill2` 用户导入多 Skill，无需改代码
  - `--chat` 群聊模式（Dispatcher 入口 → 路由 PM Agent）
  - Code-Review Agent（skills/Luyi14-code-review/SKILL.md）
  - Agent 自动 `write_log()` 写 LOG.md 留痕
  - frontmatter `agent_name` 字段自定义显示名
- **测试覆盖**：36/36 全绿（无回归）
- **验收**：✅ PASS
