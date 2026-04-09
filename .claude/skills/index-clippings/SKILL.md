---
name: index-clippings
description: 读取 Clippings 文件夹中的文件，在 index.md 中添加索引条目
argument-hint: [选项: add|remove|rebuild]
allowed-tools:
  - Read
  - Write
  - Glob
  - Bash
---

# Index Clippings Skill

## 用途
扫描 `Clippings/` 文件夹中的文件，并在 vault 根目录的 `index.md` 中创建/更新索引条目。

## 工作流程

### 1. 发现 Clippings 文件
使用 Glob 工具搜索 `Clippings/**/*.md` 获取所有文件列表。

### 2. 读取现有 index.md
尝试读取 `index.md`，如果不存在则创建新的。

### 3. 生成索引条目
为每个 Clippings 文件生成以下格式的索引条目：

```markdown
## 文件名

- **来源**: Clippings/子文件夹/
- **创建时间**: YYYY-MM-DD
- **标签**: #clippings #来源标签

> 简要描述（文件第一段或前100字）
```

### 4. 更新 index.md
将新生成的索引条目添加到 `index.md` 的 Clippings 部分。

## 索引格式

```markdown
# Index

## Clippings

<!-- INDEX:START -->

| 文件名 | 子文件夹 | 日期 | 标签 |
|--------|----------|------|------|
| [[Clippings/xxx/文件名]] | 子文件夹名 | YYYY-MM-DD | #clippings |

文件描述...

<!-- INDEX:END -->
```

## 选项说明
- `add`: 添加单个新文件的索引（需要提供文件名）
- `remove`: 从 index.md 中移除指定文件的索引
- `rebuild`: 重新扫描并重建所有 Clippings 的索引
