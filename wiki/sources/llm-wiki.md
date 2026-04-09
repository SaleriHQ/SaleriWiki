---
title: LLM Wiki 模式
source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
author: Andrej Karpathy
created: 2026-04-08
type: source
tags:
  - source
  - llm
  - knowledge-base
---

## 摘要

LLM-Wiki 是一种利用大型语言模型构建个人知识库的模式。与传统 RAG 不同，LLM **增量构建和维护持久化维基**，知识编译一次后持续更新，而非每次查询重新检索。

## 核心观点

1. **持久化累积** - 交叉引用自动生成，矛盾会被标记
2. **人机协作** - 人类负责来源和提问，AI 负责所有维护工作
3. **三层架构** - 原始资料层 → 维基层 → 模式层

## 适用场景

- 个人知识管理
- 长期研究项目
- 书籍阅读笔记
- 团队知识库

## 关键工具

- Obsidian - 笔记和可视化
- qmd - 本地搜索
- Dataview - 动态查询
