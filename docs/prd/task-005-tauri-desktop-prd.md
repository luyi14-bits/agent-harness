# TASK-005: Tauri 桌面应用 PRD

## 1. Executive Summary
构建独立桌面应用壳（Tauri v2），组件全用开源：Monaco Editor + xterm.js + React。不写 exe，Rust 壳包裹前端，通过 HTTP/WS 对接 Python Agent 引擎。

## 2. Architecture
```
Tauri (Rust shell)
  ├─ Frontend: React + Monaco Editor + xterm.js + CopilotKit
  └─ Backend via HTTP/WS → Python (agent engine)
```

## 3. User Stories
- 用户打开桌面程序 → 看到项目文件树
- 左侧：群聊输入面板
- 右侧：Agent 调度面板（谁在干活）
- 底部：终端（xterm.js）
- 中间：Monaco Editor 代码编辑 + diff

## 4. FR
- FR-1: Tauri v2 项目脚手架
- FR-2: React 前端框架
- FR-3: Monaco Editor 集成
- FR-4: xterm.js 终端集成
- FR-5: CopilotKit Agent 面板
- FR-6: HTTP 对接 Python agent 引擎
