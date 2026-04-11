---
title: "Obsidian Dataview 插件完全指南"
source: "https://www.youtube.com/watch?v=6p5Eb1sqgIY"
author: "Paul Dickson"
created: 2026-04-11
type: clipping
category: video
description: "Dataview 插件入门与进阶：四种查询类型、六个查询组件、YAML 最佳实践"
tags:
  - clippings
  - video
  - obsidian
  - dataview
  - plugin
  - tutorial
---

# Obsidian Dataview 插件完全指南：从入门到进阶

> **视频来源**: YouTube - Paul Dickson
> **时长**: 21:51
> **主题**: 全面介绍 Obsidian 最强大的插件之一 Dataview，涵盖基础查询语法到进阶工作流

---

## 一、Dataview 核心概念

### 1.1 什么是 Dataview

Dataview 是 Obsidian 的核心插件之一，它将你的笔记库（Vault）转化为可查询的数据库。你可以用类似 SQL 的语法，从海量的 Markdown 文件中筛选、排序、汇总信息。

**核心能力**：
- 用简单查询语言检索笔记
- 自动从 YAML front matter 提取元数据
- 支持多种视图格式（表格、列表、任务、日历）
- 查询结果动态更新

### 1.2 数据来源

Dataview 支持两类数据来源：

| 类型 | 说明 | 示例 |
|------|------|------|
| **内置数据** | 自动从文件属性提取 | `file.name`, `file.path`, `file.mtime` |
| **YAML front matter** | 用户自定义元数据 | `tags`, `author`, `created` |

**常用内置字段**：

```
file.name      - 文件名
file.path      - 文件路径
file.folder    - 文件夹路径
file.mtime     - 修改时间
file.ctime     - 创建时间
file.size      - 文件大小
```

### 1.3 四种查询类型

| 类型 | 用途 | 典型场景 |
|------|------|----------|
| `LIST` | 简单列表 | 列出所有书籍、项目 |
| `TABLE` | 表格展示 | 展示笔记的多维属性 |
| `TASK` | 任务聚合 | 汇总分散在各笔记中的任务 |
| `CALENDAR` | 日历视图 | 可视化任务/笔记的时间分布 |

---

## 二、查询语法详解

### 2.1 核心查询组件

Dataview 的查询由以下组件构成：

```dataview
TABLE file.name AS "标题", author, tags
FROM "文件夹路径"
WHERE author = "Paul"
SORT file.mtime DESC
LIMIT 10
```

| 组件 | 作用 | 必填 |
|------|------|------|
| `FROM` | 指定数据来源（标签/路径/文件夹） | 是 |
| `WHERE` | 过滤条件 | 否 |
| `GROUP BY` | 按字段分组汇总 | 否 |
| `FLATTEN` | 展平嵌套数据结构 | 否 |
| `SORT` | 排序（ASC/DESC） | 否 |
| `LIMIT` | 限制返回数量 | 否 |

### 2.2 LIST 查询示例

```dataview
LIST
FROM #book
SORT file.mtime DESC
LIMIT 5
```

展示按最近修改排序的 5 本书。

### 2.3 TABLE 查询示例

```dataview
TABLE file.name AS "标题", category, topics, author
FROM ""
WHERE author
LIMIT 5
```

创建包含多列的表格视图。

### 2.4 TASK 查询示例

```dataview
TASK
FROM ""
WHERE file.name = "my-tasks"
GROUP BY file.link
```

聚合指定笔记中的所有任务，支持在 Dataview 中直接勾选完成。

### 2.5 CALENDAR 查询示例

```dataview
CALENDAR file.mtime
FROM "note-lab"
WHERE file.tasks
```

在日历上可视化显示包含任务的笔记。

---

## 三、YAML Front Matter 最佳实践

### 3.1 基础结构

```yaml
---
title: "笔记标题"
author: "作者名"
category: "分类"
tags:
  - tag1
  - tag2
created: 2026-04-11
status: "in-progress"
---

# 笔记正文
```

### 3.2 字段命名规范

- 使用小写字母和短横线（如 `created-date`）
- 保持字段命名一致性
- 为常用字段建立模板

### 3.3 动态列重命名

```dataview
TABLE file.name AS "标题", tags AS "标签", status AS "状态"
FROM ""
```

用 `AS` 关键字自定义表格列标题。

---

## 四、进阶工作流

### 4.1 建立 Dataview 查询目录

**推荐做法**：在 Vault 中创建专门目录存储查询模板

```
workspaces/
└── dataview/
    ├── basic-list-queries.md
    ├── basic-table-queries.md
    ├── basic-task-queries.md
    ├── calendar-queries.md
    └── advanced-queries/
        ├── search-field.md
        ├── list-folder-with-tags.md
        └── get-missing-notes.md
```

每个查询笔记的结构：

```markdown
---
title: "查询名称"
notes: "简短说明这个查询的用途"
---

## 用途说明

这个查询用于...

## 查询代码

```dataview
YOUR QUERY HERE
```

## 示例

[实际效果截图或说明]
```

### 4.2 使用 Canvas 可视化管理查询

将查询目录放在 Canvas 中，可以：
- 直观看到所有查询
- 按功能分组
- 快速复制需要的查询
- 适合初学者参考学习

### 4.3 常用进阶查询

**获取断链笔记**：
```dataview
LIST
FROM ""
WHERE contains(file.outlinks, this.file)
```

**列出空笔记**：
```dataview
TABLE file.name, file.size
FROM ""
WHERE file.size < 100
```

**按创建天数筛选**：
```dataview
LIST file.link, (date(today) - file.ctime).day AS "Days Since Created"
FROM "cards"
SORT file.ctime DESC
LIMIT 40
```

---

## 五、优缺点分析

### 5.1 优势

| 优势 | 说明 |
|------|------|
| **强大查询能力** | 支持复杂条件筛选、汇总、可视化 |
| **高度灵活** | 支持 YAML 和行内字段 |
| **多视图输出** | 表格、列表、任务、日历 |
| **动态更新** | 添加/修改笔记自动刷新 |
| **社区支持** | 丰富的教程和示例 |

### 5.2 局限

| 局限 | 说明 |
|------|------|
| **学习曲线** | 查询语法需要时间掌握 |
| **性能问题** | 大型 Vault 可能变慢 |
| **依赖结构** | 需要规范的 YAML 和标签 |
| **插件依赖** | 第三方插件存在兼容性风险 |

### 5.3 性能优化建议

- 避免在大型笔记库中使用过于宽泛的 `FROM ""`
- 使用 `LIMIT` 限制结果数量
- 定期清理空笔记和断链
- 考虑使用 DataviewJS 优化复杂查询

---

## 六、调试技巧

### 6.1 使用示例 Vault

Dataview 官方提供了[示例 Vault](https://github.com/blacksmithgu/obsidian-dataview)，包含完整查询示例。建议：
1. 下载示例 Vault
2. 逐个研究 `dataview-queries/` 目录
3. 在源码模式查看查询写法
4. 尝试修改并观察效果

### 6.2 AI 辅助调试

可以使用 ChatGPT、Claude 等 AI 工具辅助：
- 解释查询语法
- 建议修改方案
- 生成新查询模板
- 排查错误原因

> 注意：AI 建议不一定完全正确，但仍可作为调试起点。

---

## 七、总结

Dataview 是 Obsidian 知识管理的重要工具，特别适合：

- **知识库管理**：用标签和分类组织大量笔记
- **项目管理**：跟踪分散在各笔记中的任务
- **文献管理**：管理书籍、论文等阅读笔记
- **习惯追踪**：用日历视图可视化习惯养成

**核心学习路径**：
1. 理解四种查询类型（LIST/TABLE/TASK/CALENDAR）
2. 掌握六个查询组件（FROM/WHERE/SORT/LIMIT/GROUP BY/FLATTEN）
3. 建立个人查询模板库
4. 在 Canvas 中可视化组织

---

## 相关资源

- [Dataview 官方文档](https://blacksmithgu.github.io/obsidian-dataview/)
- [Dataview 示例 Vault (GitHub)](https://github.com/blacksmithgu/obsidian-dataview)
- [[wiki/concepts/Neovim-0.12-Configuration]] - Obsidian 配置可参考此笔记的管理方式
