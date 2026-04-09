# Salieri Wiki - LLM-Optimized Knowledge Base

## 概述

这是一个基于 [LLM-Wiki](Clippings/llm-wiki.md) 模式构建的个人知识库。AI 增量构建和维护持久化维基，而非每次查询重新检索。

**核心理念**: 知识编译一次，持续更新。交叉引用自动生成，矛盾会被标记。

---

## 目录结构

```
SalieriWiki/
├── index.md              # 总索引 - 所有页面的目录
├── CLAUDE.md             # 本文件 - 维基规范
├── Clippings/            # 原始资料库（不可变）
│   ├── 01-intro.md
│   └── ...
│
└── wiki/                  # AI 生成和维护的维基
    ├── concepts/         # 概念页
    ├── entities/         # 实体页
    ├── sources/          # 来源摘要
    └── notes/            # 笔记和探索
```

---

## 页面格式规范

### 通用 Frontmatter

```yaml
---
title: 页面标题
created: 2026-04-08
updated: 2026-04-08
tags:
  - concept
  - haskell
related:
  - "[[wiki/concepts/函数式编程]]"
  - "[[Clippings/01-intro]]"
---
```

### 来源摘要页 (Sources)

```yaml
---
title: 来源标题
source: 原始链接
author: 作者
created: 2026-04-08
type: source
tags:
  - source
  - paper
---

## 摘要

关键要点的一两段总结...

## 关键概念

- **概念1**: 说明
- **概念2**: 说明

## 与维基的关联

此来源涉及:
- [[wiki/concepts/函数式编程]]
- [[wiki/concepts/类型系统]]
```

### 概念页 (Concepts)

```yaml
---
title: 概念名称
created: 2026-04-08
updated: 2026-04-08
tags:
  - concept
sources: 3
---

## 定义

概念的清晰定义...

## 关键要点

1. 要点1
2. 要点2

## 来源

- [[Clippings/01-intro]] - 来源说明
- [[wiki/sources/某来源]] - 来源说明

## 相关概念

- [[wiki/concepts/相关概念]]
```

---

## 工作流程

### Ingest（导入新来源）

当用户添加新来源时:

1. **阅读来源** - 读取原始文件
2. **讨论要点** - 与用户讨论关键收获
3. **创建摘要页** - 在 `wiki/sources/` 创建摘要
4. **更新相关页面** - 更新相关概念和实体页
5. **更新索引** - 运行 `$index-clippings` 更新 index.md
6. **Git 提交** - 使用 `ingest` 类型提交，commit message 格式见下方

### Query（查询）

1. **读取索引** - 先读 index.md 找到相关页面
2. **深入阅读** - 读取相关 wiki 页面
3. **综合回答** - 生成带引用的答案
4. **归档优质答案** - 有价值的分析可归档为新页面

### Lint（健康检查）

定期执行:
1. 检查页面间矛盾
2. 标记过时的内容
3. 找出孤立页面（无入站链接）
4. 发现缺失的交叉引用
5. 建议新的探索方向
6. **Git 提交** - 使用 `lint` 类型提交，格式: `lint: <本次发现和修复的摘要>`

### Git 版本管理

所有对 vault 的修改都通过 Git 进行版本管理。提交信息遵循特定格式，使 CLAUDE 能够通过 `git log` 理解操作历史。

#### 提交信息格式

```
<type>(<scope>): <标题>

<详细说明>
```

**type 类型**:
- `ingest` - 导入新来源
- `lint` - 健康检查
- `refactor` - 重构页面结构
- `fix` - 修复断链或错误
- `docs` - 更新文档

#### 提交信息示例

**ingest 类型**:
```
ingest: Add Real World Haskell source

- Clipping: Clippings/Real-World-Haskell.md
- Created: wiki/sources/real-world-haskell.md
- Created: wiki/concepts/类型推断.md
- Updated: index.md
```

**lint 类型**:
```
lint: Fix broken links and orphan pages

- Found: 4 broken links, 3 orphan source pages
- Created: wiki/concepts/代数数据类型.md
- Created: wiki/concepts/类型类.md
- Fixed: wiki/concepts/模式匹配.md
- Updated: index.md
```

#### CLAUDE 如何使用 Git 历史

当用户询问"上次 ingest 做了什么"时，CLAUDE 会:
1. 执行 `git log --grep="ingest" --oneline -10` 查找最近的 ingest 操作
2. 执行 `git show <commit>` 查看详细变更
3. 从 commit message 中提取关键信息回答

#### Git 命令速查

| 操作 | 命令 |
|------|------|
| 查看最近操作 | `git log --oneline -10` |
| 查看 ingest 历史 | `git log --grep="ingest" --oneline` |
| 查看 lint 历史 | `git log --grep="lint" --oneline` |
| 查看某次变更 | `git show <commit>` |
| 查看当前状态 | `git status` |
| 查看变更统计 | `git diff --stat` |

---

## 索引格式

### index.md

```markdown
# Vault Index

## 📁 Clippings

<!-- INDEX:START -->
| 文件 | 来源 | 日期 | 标签 |
|------|------|------|------|
| [[Clippings/xxx]] | 来源 | 日期 | #tag |

描述...
<!-- INDEX:END -->

## 📚 Wiki

### 概念
| 页面 | 标签 | 相关来源 |
|------|------|----------|
| [[wiki/concepts/xxx]] | #tag | 3 |

### 来源摘要
| 页面 | 原始来源 | 日期 |
|------|----------|------|
| [[wiki/sources/xxx]] | URL | 日期 |
```

---

## 工具

### Git

| 命令 | 说明 |
|------|------|
| `git status` | 查看当前修改状态 |
| `git log --oneline -10` | 查看最近 10 条操作记录 |
| `git log --grep="ingest"` | 查看所有 ingest 操作 |
| `git diff` | 查看未提交的修改 |
| `git show <commit>` | 查看某次提交的详情 |

### Skills

- `$index-clippings` - 扫描 Clippings/ 并更新 index.md

---

## 原则

1. **原始资料不可变** - 永远不修改 Clippings/ 中的文件
2. **AI 负责维护** - 用户只需提供来源和提问
3. **索引保持最新** - 每次 ingest 后更新 index.md
4. **Git 版本管理** - 所有修改通过 Git 提交，操作历史由 Git 管理
5. **链接优先** - 使用 [[wikilinks]] 而非纯文本

---

## 扩展

随着维基增长，可以添加:
- [qmd](https://github.com/tobi/qmd) - 本地搜索工具
- Dataview - 动态查询
- Obsidian Graph View - 可视化连接
