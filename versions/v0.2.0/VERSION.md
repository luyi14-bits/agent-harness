# 版本快照记录

## v0.2.0 (2026-07-13)
- **新增**：编排调度 + 状态管理 + 开发工作流 + 独立部署
- **功能**：
  - ParallelOrchestrator：并行子 Agent 执行，max_concurrency 控制
  - CheckpointManager：JSON 检查点保存/恢复/resume
  - 预定义开发工作流模板（brainstorm→plan→code→test→review）
  - FastAPI 独立部署服务（POST /execute + GET /status）
  - cache-guard CI 测试（TestReleaseCacheHitGuard）
- **测试覆盖**：36/36 全绿（迭代1: 22 + 迭代2: 14）
- **验收**：✅ PASS
- **回退命令**：将 `versions/v0.2.0/*` 覆盖回项目根目录即可
