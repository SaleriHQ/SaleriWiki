---
name: pdfbook-to-markdown

description: 将 PDF 书籍转换为中文 Markdown 并按章节分割。适用于用户想要将一本 PDF 书籍转换为分章节的中文 Markdown 文件，并保存到 Clippings 目录中。

argument-hint: "<path-to-pdf> [target-folder]"
---

# PDF 书籍转中文 Markdown 并按章节分割

此技能将 PDF 书籍转换为 Markdown 格式，并按章节分割为独立的 Markdown 文件。

## 核心要求

1. **严格翻译** - 将英文内容准确翻译为中文，不遗漏、不删减
2. **完整保留** - 原文中的所有内容都必须保留，包括注释、脚注、参考文献
3. **格式规范** - 代码和数学公式使用 Obsidian 支持的格式

## 工作流程

1. **PDF 转 Markdown** - 使用 `markitdown[pdf]` 将 PDF 转为单一 Markdown 文件
2. **翻译内容** - 将英文内容翻译为中文，保持原意
3. **格式化代码** - 使用 Obsidian 代码块格式（```haskell 等）
4. **格式化数学** - 使用 `$...$`（行内）或 `$$...$$`（块级）格式
5. **按章节分割** - 将翻译后的内容按章节分割为独立文件
6. **保存到目标目录** - 将文件保存到 `Clippings/<folder>/` 目录下

## 命令格式

```
/pdfbook-to-markdown <path-to-pdf> [target-folder]
```

- `path-to-pdf`: PDF 文件的路径（必填）
- `target-folder`: 目标文件夹名（可选，默认使用 PDF 文件名）

## 使用示例

**基础用法**:
```
/pdfbook-to-markdown book.pdf
```

这会:
1. 将 `book.pdf` 转换为中文 Markdown
2. 在 `Clippings/book/` 目录下创建分割后的章节文件

**指定目标目录**:
```
/pdfbook-to-markdown book.pdf clippings
```

这会:
1. 将 `book.pdf` 转换为中文 Markdown
2. 在 `Clippings/clippings/` 目录下创建分割后的章节文件

## 章节识别规则

按以下顺序匹配章节标题：

1. `# 第X章` 或 `# Chapter X` 或 `# Part X`
2. `# X. ` (如 `# 1. Introduction` 或 `# 10. Advanced Topics` )
3. `## X. ` 或 `## Chapter X`
4. `# X ` (单个 `#` + 数字开头)

分割时：
- 以 `#` 开头的行作为新章节的起点
- 如果文件有多个 `#` 标题，保留最小级别的标题作为文件内的小标题

## 输出格式

每个章节文件包含:

```markdown
---
title: <章节标题>
source: <原始 PDF 路径>
created: <转换日期>
type: chapter
tags:
  - book
  - chapter
---

# <章节标题>

<章节内容（已翻译为中文）>
```

## 具体执行步骤

### 第一步：转换 PDF

使用 markitdown 将 PDF 转换为单一 Markdown：

```bash
uvx 'markitdown[pdf]' <path-to-pdf> -o /tmp/<book-name>.md
```

### 第二步：翻译内容

在分割前，先将整个 Markdown 内容翻译为中文：
- 保持原文的标题结构不变
- 翻译正文内容为中文
- 保留所有代码注释
- 不删减任何内容

### 第三步：格式化代码

代码块格式要求：

```markdown
```haskell
map :: (a -> b) -> [a] -> [b]
map f []     = []
map f (x:xs) = f x : map f xs
```
```

支持的代码语言标签：
- `haskell`, `python`, `javascript`, `java`, `c`, `cpp`, `rust`, `go`
- `bash`, `shell`, `sql`, `json`, `yaml`, `markdown`
- 其他标准语言标签

### 第四步：格式化数学公式

数学公式格式要求：

**行内公式**：
```markdown
欧拉公式 $e^{i\pi} + 1 = 0$ 是数学史上最重要的等式之一。
```

**块级公式**：
```markdown
$$
\int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$
```

### 第五步：解析并分割

1. 读取翻译后的 Markdown 文件
2. 使用标题级别识别章节结构
3. 按章节分割为独立文件

### 第六步：保存文件

1. 在 `Clippings/<target-folder>/` 目录下创建章节文件
2. 文件命名格式：使用中文章节标题
   - 例如：`第01章-简介.md`、`第02章-类型与函数.md`

### 第七步：清理与索引

1. 删除临时的合并文件

## 错误处理

- **PDF 读取失败**: 报告错误并建议检查文件路径或 PDF 是否损坏
- **章节识别失败**: 将整个文件保存为单个文件，命名为 `00-全文.md`
- **目标目录已存在**: 在目录名后追加数字（如 `book-2/`）

## 示例输出

对于一本包含以下结构的 PDF：

```
# Chapter 1: Introduction
Content...

# Chapter 2: Types and Functions
Content...
```

生成的目录结构：

```
Clippings/book/
├── 第01章-简介.md
└── 第02章-类型与函数.md
```

每个文件内容：

```markdown
---
title: 第1章 简介
source: book.pdf
created: 2026-04-21
type: chapter
tags:
  - book
  - chapter
---

# 第1章 简介

<翻译后的中文内容，代码和公式已格式化>
```