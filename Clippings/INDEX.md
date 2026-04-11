---
title: Clippings 索引
created: 2026-04-11
tags:
  - index
  - clippings
description: 所有 Clippings 文章的统一索引，支持多维度筛选
---

# 📚 Clippings 索引

> 本页面使用 Dataview 动态查询，所有记录随文件变更自动更新。
>
> **标准 front matter 格式**：
> ```yaml
> type: clipping
> category: haskell|neovim|ai|video|other
> ```

---

## 📊 统计概览

```dataview
TABLE WITHOUT ID
  "总计" AS "指标",
  length(list) AS "数量"
FROM "Clippings"
WHERE type = "clipping"
FLATTEN {
  "Haskell": length(filter(list, (t) => t.category = "haskell")),
  "Neovim": length(filter(list, (t) => t.category = "neovim")),
  "AI": length(filter(list, (t) => t.category = "ai")),
  "Video": length(filter(list, (t) => t.category = "video")),
  "其他": length(filter(list, (t) => !contains(["haskell", "neovim", "ai", "video"], t.category)))
} AS "分类统计"
```

---

## 🏷️ 按分类筛选

### Haskell

```dataview
TABLE
  file.link AS "文章",
  author AS "作者",
  created AS "导入日期"
FROM "Clippings"
WHERE type = "clipping" AND category = "haskell"
SORT created DESC
```

### Neovim / Vim

```dataview
TABLE
  file.link AS "文章",
  author AS "作者",
  created AS "导入日期"
FROM "Clippings"
WHERE type = "clipping" AND category = "neovim"
SORT created DESC
```

### AI / 安全

```dataview
TABLE
  file.link AS "文章",
  author AS "作者",
  created AS "导入日期"
FROM "Clippings"
WHERE type = "clipping" AND category = "ai"
SORT created DESC
```

### 视频 / 访谈

```dataview
TABLE
  file.link AS "文章",
  author AS "作者",
  created AS "导入日期"
FROM "Clippings"
WHERE type = "clipping" AND category = "video"
SORT created DESC
```

---

## 📅 按时间筛选

### 最近一周

```dataview
TABLE
  file.link AS "文章",
  category AS "分类",
  author AS "作者"
FROM "Clippings"
WHERE type = "clipping" AND created >= date(today) - dur(7 days)
SORT created DESC
```

### 最近一月

```dataview
TABLE
  file.link AS "文章",
  category AS "分类",
  author AS "作者"
FROM "Clippings"
WHERE type = "clipping" AND created >= date(today) - dur(30 days)
SORT created DESC
```

---

## 🗂️ 按标签筛选

### 教程类

```dataview
TABLE
  file.link AS "教程",
  category AS "分类",
  author AS "作者"
FROM "Clippings"
WHERE type = "clipping" AND contains(file.tags, "tutorial")
SORT category
```

### 作业类

```dataview
TABLE
  file.link AS "作业",
  category AS "分类",
  created AS "日期"
FROM "Clippings"
WHERE type = "clipping" AND contains(file.tags, "homework")
SORT created DESC
```

### 讲义类

```dataview
TABLE
  file.link AS "讲义",
  category AS "分类",
  created AS "日期"
FROM "Clippings"
WHERE type = "clipping" AND contains(file.tags, "lecture")
SORT created DESC
```

---

## 📋 完整列表

```dataview
TABLE
  file.link AS "文章",
  category AS "分类",
  author AS "作者",
  created AS "导入日期",
  source AS "原始来源"
FROM "Clippings"
WHERE type = "clipping"
SORT category, created DESC
```

---

## ⚡ 快速搜索

> 使用 Obsidian 内置搜索（`Ctrl + Shift + F`）配合标签：
> - `#haskell` - 所有 Haskell 相关
> - `#neovim` - 所有 Neovim 相关
> - `#video` - 所有视频教程

---

## 📝 添加新 Clippings

新增文件时请使用以下 front matter 模板：

```yaml
---
title: "文章标题"
source: "原始来源URL"
author: "作者"
created: YYYY-MM-DD
type: clipping
category: haskell|neovim|ai|video|other
description: "简短描述"
tags:
  - clippings
  - 主题标签
---
```

**category 可选值**：
| 值 | 说明 |
|----|------|
| `haskell` | Haskell 语言学习资料 |
| `neovim` | Neovim/Vim 配置教程 |
| `ai` | AI、安全相关 |
| `video` | 视频字幕转换文章 |
| `other` | 其他类别 |

---

*本索引由 `/video-subtitle-to-article` skill 维护*
