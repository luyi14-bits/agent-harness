# TASK-002: 编排调度 + 状态管理 + 工作流 + 部署 Spec

## Why

迭代 1 交付了核心映射引擎，但缺少企业级能力：子 Agent 只能串行执行、流程中断无法恢复、没有端到端工作流模板、无法独立部署为后端服务、缓存命中率退化无自动检测。

## Meta

- **优先级**: P1/P2
- **估算工时**: 3 人天
- **PRD 来源**: `docs/prd/task-002-orch-checkpoint-workflow-deploy-prd.md`

## Requirements

### Requirement: PAR-ORCH-001
The system SHALL support parallel orchestration of multiple sub-Agents.

#### Scenario: Execute agents in parallel
- **GIVEN** an SOP node with `mode: parallel`
- **WHEN** the orchestrator executes it
- **THEN** all sub-Agents start concurrently
- **AND** results are aggregated after all complete

#### Scenario: Max concurrency limit
- **GIVEN** a parallel SOP node with `max_concurrency: 2`
- **WHEN** 5 sub-Agents are queued
- **THEN** at most 2 run simultaneously

### Requirement: CHECKPOINT-001
The system SHALL support checkpoint save/resume for Agent execution.

#### Scenario: Save checkpoint
- **GIVEN** a running SOP execution
- **WHEN** a checkpoint is triggered
- **THEN** Agent state + current step are saved to disk

#### Scenario: Resume from checkpoint
- **GIVEN** a saved checkpoint file
- **WHEN** resume() is called
- **THEN** execution continues from the saved step

### Requirement: WORKFLOW-001
The system SHALL provide a predefined developer workflow chain.

#### Scenario: Full dev workflow
- **GIVEN** a defined workflow chain
- **WHEN** orchestrated
- **THEN** steps run in order: brainstorm → plan → code → test → review

### Requirement: DEPLOY-001
The system SHALL support serving as a FastAPI backend.

#### Scenario: REST API execution
- **GIVEN** the FastAPI server is running
- **WHEN** POST /execute with SOP definition
- **THEN** returns a session_id and executes asynchronously

### Requirement: CACHE-GUARD-001
The system SHALL provide a CI guard for cache hit rate regression.

#### Scenario: Cache hit rate guard
- **GIVEN** a CI pipeline
- **WHEN** TestReleaseCacheHitGuard runs
- **THEN** fails if hit rate drops below threshold
