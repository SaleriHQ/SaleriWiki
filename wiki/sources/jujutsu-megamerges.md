---
title: "Jujutsu megamerges for fun and profit"
source: https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit
author: Isaac Corbrey
published: 2026-04
created: 2026-04-21
type: source
tags:
  - source
  - jujutsu
  - git
  - vcs
  - workflow
related:
  - "[[wiki/concepts/函数式编程]]"
---

# Jujutsu megamerges for fun and profit

## 概述

Jujutsu (jj) 是一个 Git 替代品，本文介绍其**megamerge 工作流**：将多个分支合并为一个"巨型合并"提交，作为所有工作的基础。

## 核心概念

### 什么是 Megamerge

```ansi
@  megamerge (empty)
├─┬─╮  feat: Add feature X
│ ○ │  bugfix: Fix bug Y
│ ○ │  infra: Refactor something
├─╯
○  trunk/main
```

**关键点**：
- Megamerge 是带有**三个或更多父提交**的合并提交
- 你不需要推送 megamerge，只推送它包含的分支
- 始终工作在所有工作的总和之上

### 优势

| 优势 | 说明 |
|------|------|
| **无冲突开发** | 始终合并，提前发现冲突 |
| **上下文切换零摩擦** | 无需切换分支，直接编辑 |
| **小 PR 友好** | 更容易拆分重构和修复 |
| **分支自动同步** | 单命令 rebase 所有分支 |

## 核心命令

```sh
# 1. 创建 megamerge
jj new branch1 branch2 branch3
jj commit --message "megamerge"

# 2. 自动吸收变更到下游提交
jj absorb

# 3. 交互式 squash
jj squash --to target --from source --interactive

# 4. 将新变更加入 megamerge
jj stack new-feature-branch
```

## 推荐配置

```toml
[revset-aliases]
"closest_merge(to)" = "heads(::to & merges())"

[aliases]
# 将 revset 插入 megamerge
stack = ["rebase", "--after", "trunk()", "--before", "closest_merge(@)", "--revision"]

# 将整个栈加入 megamerge
stage = ["stack", "closest_merge(@).. ~ empty()"]

# 将你的变更 rebase 到 trunk
restack = ["rebase", "--onto", "trunk()", "--source", "roots(trunk()..) & mutable()"]
```

## Jujutsu vs Git

| 特性 | Git | Jujutsu |
|------|-----|---------|
| 合并冲突 | 事后解决 | 第一次-class 概念 |
| 变更历史 | 线性分支 | DAG 图结构 |
| 分支切换 | `git checkout` | `jj edit` |
| 智能 squash | 手动操作 | `jj absorb` 自动识别 |

## 与 Language Learn 的关联

**不直接相关**，但对于代码管理有潜在价值：

| 场景 | 说明 |
|------|------|
| 多分支管理 | 同时处理功能/修复/基础设施 |
| Code Review | 更清晰的变更边界 |
| 部署工作流 | 配合 Language Learn 的部署流程 |

## 来源

- [原文链接](https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit)
- [Jujutsu 官方文档](https://jj-vcs.github.io/jj/latest)
