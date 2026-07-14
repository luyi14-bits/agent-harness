# Tasks — TASK-002

- [ ] Task 1: ParallelOrchestrator
  - [ ] 实现并行执行（threading 或 asyncio）
  - [ ] 实现 max_concurrency 限制
  - [ ] 实现结果聚合
  - [ ] 编写测试

- [ ] Task 2: CheckpointManager
  - [ ] 实现 JSON 序列化保存/恢复
  - [ ] 实现 resume() 接口
  - [ ] 集成到 orchestrator 流程
  - [ ] 编写测试

- [ ] Task 3: 开发工作流模板
  - [ ] 预定义 dev_workflow SOP 结构
  - [ ] 编写测试

- [ ] Task 4: FastAPI 服务
  - [ ] FastAPI app 框架
  - [ ] POST /execute 端点
  - [ ] GET /status/{session_id} 端点
  - [ ] 启动脚本

- [ ] Task 5: cache-guard CI
  - [ ] 编写 TestReleaseCacheHitGuard
  - [ ] 输出测试

# Dependencies
- Task 1 无依赖
- Task 2 无依赖
- Task 1+2 可并行
- Task 3 depends on Task 1+2
- Task 4 无依赖（独立）
- Task 5 无依赖（独立）

# 工时估算
| Task | 子任务数 | 人天 |
|------|:-------:|:----:|
| Task 1 | 4 | 0.5 |
| Task 2 | 4 | 0.5 |
| Task 3 | 2 | 0.25 |
| Task 4 | 4 | 0.75 |
| Task 5 | 2 | 0.25 |
| **合计** | **16** | **2.25** |
