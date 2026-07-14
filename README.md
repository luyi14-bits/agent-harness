# Tree-SOP Agent

> **版本**：Alpha 0.1 | 群聊式多 Agent 软件开发体系 — 预置完整公司级 SOP 管道，每个 Skill 自动变为 Agent 知识外挂

## 项目概述

Tree-SOP Agent 是一个**群聊式多 Agent 软件开发框架**。预置 11 个 Agent 角色（PM、Spec、Coding、Code-Review、TDD、Acceptance、Security、DevOps、Secretary、Trinity + Dispatcher），按标准公司开发流程编排协作。用户向群聊输入需求，系统自动路由、自动执行、自动留痕。底层使用 DeepSeek V4 Pro/Flash 混用策略和三层缓存优化。

### 最终 SOP 管道

```
用户: "帮我做一个登录功能"
         │
         ▼
    Dispatcher（理解意图，启动管道）
         │
         ▼
    PM ───→ Trinity（架构评审）
         │
         ▼
    Spec-Pipeline（拆任务）
         │
         ▼
    Coding ───→ Code-Review（代码审查）
         │              │
         ▼              ▼
    TDD ←── CR Report
         │
         ▼
    Acceptance ──→ Security（并行）
         │
         ▼
    DevOps（构建发布）
         │
         ▼
    Secretary（留痕看板 + 版本快照）
```

每个节点产出 HandoverPackage 传递到下一节点，自动写 LOG.md 留痕。LOOP SOP 全程监控门禁。

## 关键技术选型

| 维度 | 选型 | 状态 |
|------|------|------|
| 底层模型 | DeepSeek V4 Pro（规划/调研/审查）+ Flash（编程/测试） | ✅ 已集成 |
| 参考框架 | Superpowers（skill→agent 理念）+ CrewAI（per-agent 模型分配） | ✅ 调研完成 |
| Skill 体系 | tree-SOP 结构化定义（YAML frontmatter + Markdown body） | ✅ v0.1.0 |
| 编排模式 | 顺序/并行/层级 + 检查点恢复 | ✅ v0.2.0 |
| 缓存策略 | 三层 Context 分区 + 前缀 hash 不变性检测 | ✅ v0.1.0 |
| FC 适配 | reasoning_content + tool_choice 显式函数名 | ✅ v0.1.0 |
| 预置 Agent | 11 个角色，用户可导入多 Skill 挂载 | 💡 待实现 |
| 桌面 UI | Tauri + Monaco + xterm.js | 💡 待实现 |

## 项目结构

```
tree-sop-agent/
├── README.md                  # 项目首页
├── PIPELINE_KANBAN.md         # 管线看板（6 列流转 + 想法池）
├── CHANGELOG.md               # 发布历史
├── ITERATION_LOG.md           # LOOP 迭代追踪表
├── .gitignore                 # Git 忽略规则
├── auto_test.py               # CLI 自测脚本
├── docs/                      # 技术文档
│   ├── prd/                   # PRD 文档
│   ├── acceptance-report-task-001.md
│   └── agent-framework-research.html
├── .trae/specs/               # Spec 任务目录
├── src/tree_sop_agent/        # 核心代码
│   ├── core/                  # SkillDef / Parser / Registry / AgentFactory
│   ├── adapters/              # ModelRouter / DeepSeekAdapter / CacheEngine / Context
│   ├── orchestrator/          # Sequential / Hierarchical / Parallel + Checkpoint
│   ├── cli/                   # CLI 入口
│   └── server/                # FastAPI 独立部署
├── tests/                     # pytest 测试套件（36 个）
├── versions/                  # 版本快照
│   ├── v0.1.0/
│   └── v0.2.0/
└── skills/                    # LOOP SOP 留痕日志
```

## 路线图

| 阶段 | 目标 | 状态 |
|------|------|:----:|
| Phase 0 | 调研开源 Agent 框架 | ✅ 完成 |
| Phase 1 | 确定 skill → agent 映射架构 | ✅ v0.1.0 已发布 |
| Phase 2 | 搭建项目骨架 + DeepSeek 接入 | ✅ v0.1.0 已发布 |
| Phase 3 | 实现 skill 定义层 + 映射引擎 | ✅ v0.1.0 已发布 |
| Phase 4 | 实现编排调度器 + 状态管理 | ✅ v0.1.0 已发布 |
| Phase 5 | 完整开发工作流（brainstorm→plan→code→test→review） | ✅ v0.2.0 已发布 |
| Phase 6 | 预置 Agent 角色体系 + 多 Skill 挂载 | 💡 待评估 |
| Phase 7 | Tauri 桌面应用（Monaco + xterm.js） | 💡 待评估 |
