# Checklist — TASK-001 Skill → Agent 映射引擎

> 每条可回答"是/否"。验收时逐项对照代码证据。

## Skill 定义格式 (SKILL-FMT-001)

- [ ] SKILL-FMT-001.1: YAML frontmatter 解析器能正确提取 name/description/tools/model
- [ ] SKILL-FMT-001.2: 缺失必填字段时抛出明确的 ValidationError
- [ ] SKILL-FMT-001.3: 支持树形 SOP 嵌套定义（sub_skills 递归结构）
- [ ] SKILL-FMT-001.4: 支持 MCP server / shell / API 三种工具声明

## Agent 映射引擎 (MAP-ENG-001)

- [ ] MAP-ENG-001.1: `SkillRegistry.load()` 加载 skill 后成功创建 Agent 实例
- [ ] MAP-ENG-001.2: Agent 实例化时注入正确的 role preset（system prompt）
- [ ] MAP-ENG-001.3: Agent 拥有 skill 声明中的工具集
- [ ] MAP-ENG-001.4: 两个并发 Agent 的上下文完全隔离（无变量污染）

## 模型策略 (MODEL-STRAT-001)

- [ ] MODEL-STRAT-001.1: model=pro 的技能路由到 DeepSeek V4 Pro
- [ ] MODEL-STRAT-001.2: model=flash 的技能路由到 DeepSeek V4 Flash
- [ ] MODEL-STRAT-001.3: Pro 和 Flash session 完全独立（各自缓存前缀独立）
- [ ] MODEL-STRAT-001.4: 用户可通过配置覆盖默认模型分配

## 缓存前缀 (CACHE-PREFIX-001)

- [ ] CACHE-PREFIX-001.1: 前缀组装顺序固定为 base → output style → language → memory → skill index
- [ ] CACHE-PREFIX-001.2: skill 正文内容不进缓存前缀
- [ ] CACHE-PREFIX-001.3: 前缀变更检测（PrefixSnapshot hash 对比）
- [ ] CACHE-PREFIX-001.4: 记忆更新走 `<memory-update>` XML 块，前缀不变

## Function Calling 适配 (FC-ADAPT-001)

- [ ] FC-ADAPT-001.1: 带 tool_calls 的消息原样保留 reasoning_content
- [ ] FC-ADAPT-001.2: 不带 tool_calls 的消息省略 reasoning_content
- [ ] FC-ADAPT-001.3: tool_choice 使用显式函数名称，不使用 `"required"`
- [ ] FC-ADAPT-001.4: 多轮对话保留完整 tool_calls 历史
- [ ] FC-ADAPT-001.5: deepseek-reasoner 自动降级到 deepseek-chat 并记录日志

## 三层 Context 分区 (CTX-PART-001)

- [ ] CTX-PART-001.1: 消息序列正确分为 immutable/append-only/volatile 三区
- [ ] CTX-PART-001.2: immutable 区整 session 字节级不变（缓存命中）
- [ ] CTX-PART-001.3: volatile 区内容不发给 API
- [ ] CTX-PART-001.4: 分区边界有 guards 防止数据跨界

## SOP 编排 (SOP-ORCH-001)

- [ ] SOP-ORCH-001.1: SequentialOrchestrator 正确串行执行子 Agent
- [ ] SOP-ORCH-001.2: 子 Agent 间的结果正确传递（HandoverPackage）
- [ ] SOP-ORCH-001.3: HierarchicalOrchestrator 递归展开树形 SOP
- [ ] SOP-ORCH-001.4: 每层 SOP 维护独立上下文作用域

## CLI 自测 (CLI-SELF-001)

- [ ] CLI-SELF-001.1: `auto_test.py` 从命令行独立运行（不依赖 IDE）
- [ ] CLI-SELF-001.2: 成功时 exit(0) + 输出 OK
- [ ] CLI-SELF-001.3: 失败时 exit(1) + 错误信息
- [ ] CLI-SELF-001.4: 依赖缺失时输出安装提示

## 代码质量

- [ ] CQ-001: 所有公开类/函数在 `__init__.py` 中导出
- [ ] CQ-002: 全部 `except` 有日志，无 `except: pass`
- [ ] CQ-003: API Key 通过环境变量注入，不硬编码
- [ ] CQ-004: JSON 日志格式含模块名（可路由到 ELK）
- [ ] CQ-005: Pydantic Field 均有 `description`
- [ ] CQ-006: 数据库操作（如有）有 rollback + close
- [ ] CQ-007: 文件路径使用 os.path 动态拼接
- [ ] CQ-008: 类型声明完整（TypedDict 或 dataclass）
