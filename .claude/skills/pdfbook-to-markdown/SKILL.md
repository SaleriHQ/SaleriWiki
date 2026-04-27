---
name: pdfbook-to-markdown

description: 将 PDF 书籍（数学教材或计算机书籍）转换为中文 Markdown 并按章节分割。当用户想要将 PDF 书籍转换为分章节的中文 Markdown 文件、保存到 Clippings 目录、或处理包含大量数学公式/代码的教材时使用此技能。

argument-hint: "<path-to-pdf> [target-folder]"
---

# PDF 书籍转中文 Markdown

此技能将 PDF 教材（数学类或计算机类）转换为中文 Markdown，保留公式和代码格式。

## 书籍类型识别

处理前先判断书籍类型：

| 特征 | 数学教材 | 计算机书籍 |
|------|---------|-----------|
| 公式密度 | 高（大量 LaTeX） | 低 |
| 代码块 | 少 | 多 |
| 标题结构 | 1A/1B/1.1 节 | Chapter/Section |
| 示例 | LADR、高等数学 | 算法导论、TCP/IP |

## 数学教材格式

### 标题层级

```markdown
## 第1章 向量空间        ← 章

### 1A $\mathbb{R}^n$    ← 节

#### 复数                ← 小节
```

### 定义/定理/例 → **粗体**

```markdown
**1.1 定义：** 复数，$\mathbb{C}$

**1.2 例：** 复数算术
```

### 公式格式

```markdown
行内: 设 $x \in \mathbb{R}^n$

块级:
$$
\sum_{k=1}^n x_k = x_1 + \cdots + x_n
$$
```

### 证明

```markdown
**证明。** ... $\blacksquare$
```

### 练习

```markdown
#### 练习 1A
```

## 计算机书籍格式

### 标题层级

```markdown
## 第1章 引言          ← 章

### 1.1 背景           ← 节

### 1.1.1 历史         ← 小节
```

### 代码块

````markdown
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```
````

支持的语法高亮：`python`, `javascript`, `java`, `c`, `cpp`, `rust`, `go`, `haskell`, `bash`, `sql`, `json`, `yaml`

### 术语表/备注

```markdown
**术语：时间复杂度**

指算法执行时间与输入规模的关系。
```

## 工作流程

```
1. markitdown[pdf] → raw.md
2. fix_markitdown.py → fixed.md
3. split_chapters.py → 章节文件
4. AI 翻译每个章节
5. 清理临时文件
```

## 执行步骤

### 第一步：转换 PDF

```bash
mkdir -p Clippings/<target-folder>
uvx 'markitdown[pdf]' <path-to-pdf> -o Clippings/<target-folder>/raw.md
```

### 第二步：修复碎片化

```bash
python scripts/fix_markitdown.py Clippings/<target-folder>/raw.md \
    Clippings/<target-folder>/fixed.md
```

修复内容：
- 表格碎裂
- Unicode 数学符号 → LaTeX
- CamelCase 连写
- 无意义表格（目录页等）

### 第三步：分割章节

```bash
python scripts/split_chapters.py Clippings/<target-folder>/fixed.md \
    Clippings/<target-folder>/
```

### 第四步：翻译

**翻译原则（通用）**：
- LaTeX 公式 `$...$` 和 `$$...$$` 保持不变
- 代码块内容保持不变
- markdown 标题结构保持不变
- 只翻译文字描述

**数学书籍额外原则**：
- 变量名不翻译：`$x$` 保持 `$x$`
- 符号系统不翻译：`$\mathbb{R}$` 保持原样
- 证明结构保持：`**证明。** ... $\blacksquare$`

**计算机书籍额外原则**：
- 变量名、函数名不翻译
- 保留英文技术术语（可选译注）

**翻译示例**：

```markdown
原文: Let $f: \mathbb{R}^n \to \mathbb{R}$ be a function.
翻译: 设 $f: \mathbb{R}^n \to \mathbb{R}$ 为一个函数。

原文: ```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
翻译: ```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
```

### 第五步：保存

```markdown
---
title: <章节标题>
source: <PDF 路径>
created: <日期>
type: chapter
tags:
  - book
  - chapter
---

<内容>
```

### 第六步：清理

```bash
rm Clippings/<target-folder>/raw.md
rm Clippings/<target-folder>/fixed.md
```

## 数学符号速查

| Unicode | LaTeX |
|---------|-------|
| ℝ | `\mathbb{R}` |
| ℂ | `\mathbb{C}` |
| 𝛼 | `\alpha` |
| 𝛽 | `\beta` |
| ∈ | `\in` |
| → | `\rightarrow` |
| ≤ ≥ | `\leq` `\geq` |
| ≠ | `\neq` |
| ∞ | `\infty` |

## 常见错误

| 错误 | 正确做法 |
|------|---------|
| 翻译公式内文字 `$x 轴$` | 保持 `$x$` |
| 翻译变量名 `$n$` | 保持 `$n$` |
| 用 callout `> [!note]` | 用 `**粗体**` |
| 翻译代码注释 `// i++` | 保持 `// i++` |
| 删除 $\blacksquare$ | 保留证明结束标记 |

## 输出结构

```
Clippings/<target-folder>/
├── 第01章-向量空间.md      # 数学书
├── 第01章-引言.md          # 计算机书
├── 第02章-算法基础.md
└── ...
```

## 错误处理

- **PDF 读取失败**：检查文件路径，尝试其他 PDF
- **章节识别失败**：保存为 `00-全文.md`
- **目标目录已存在**：追加数字如 `book-2/`
