---
title: MiniMax — Modular Independent Neovim Improvements
source: https://nvim-mini.org/MiniMax/configs/nvim-0.12/
author: Evgeni Chasnovski
created: 2026-04-10
type: source
tags:
  - source
  - neovim
  - configuration
  - mini.nvim
---

## 摘要

MiniMax 是一个模块化的 Neovim 0.12 配置示例，由 mini.nvim 作者维护。它展示如何用 `vim.pack` 内置插件管理器搭配 `mini.nvim` 打造一个稳定、功能丰富、开箱即用的 Neovim 配置。配置设计为可读、可自定义，适合作为个人配置的起点。

## 目录结构

```
nvim-0.12/
├── init.lua          启动时执行的入口文件
├── plugin/           启动时自动 sourced 的文件
│   ├── 10_options.lua  基础选项
│   ├── 20_keymaps.lua  自定义映射
│   ├── 30_mini.lua     MINI 配置
│   └── 40_plugins.lua  MINI 以外的插件
├── snippets/         用户代码片段
└── after/            覆盖插件行为的文件
    ├── ftplugin/       文件类型行为
    ├── lsp/            语言服务器配置
    └── snippets/       高优先级代码片段
```

## 核心设计理念

### 1. vim.pack 作为插件管理器

```lua
-- 所有插件通过 vim.pack.add() 安装和加载
vim.pack.add({ 'https://github.com/nvim-mini/mini.nvim' })
```

`mini.nvim` 在 init.lua 中立即加载，以使 `mini.misc` 可用于辅助函数。

### 2. 加载辅助函数

通过 `mini.misc.safely()` 包装，实现 fail-safe 的模块化配置：

| 辅助函数 | 触发时机 | 用途 |
|---------|---------|------|
| `Config.now(f)` | 立即执行 | 启动时必须执行（colorscheme、statusline 等） |
| `Config.later(f)` | 首屏绘制后执行 | 启动后非必要功能 |
| `Config.now_if_args(f)` | 根据启动参数决定 | 启动时带文件则立即执行，否则延迟 |
| `Config.on_event(ev, f)` | 事件触发时执行一次 | 如 `InsertEnter` 首次进入插入模式 |
| `Config.on_filetype(ft, f)` | 文件类型确定时执行一次 | 如首个 Lua 文件打开时 |

### 3. mini.nvim 模块

`mini.nvim` 是全功能插件库，提供 30+ 模块。MiniMax 配置启用了其中大部分：

**核心模块**（立即加载）:
- `mini.basics` — 通用配置预设（快捷键、选项、autocmd）
- `mini.icons` — 图标提供器
- `mini.notify` — 通知系统
- `mini.sessions` — 会话管理
- `mini.starter` — 启动屏幕
- `mini.statusline` — 状态栏
- `mini.tabline` — 标签页行
- `mini.completion` — 异步两阶段补全（LSP + 内置回退）
- `mini.files` — 文件系统导航（Miller columns 视图）
- `mini.misc` — 杂项工具函数

**延迟加载模块**:
- `mini.ai` — 扩展 textobject（`ci(`, `va'`, `daF` 等）
- `mini.align` — 文本对齐
- `mini.bracketed` — 方括号导航（`]b`, `[j` 等）
- `mini.bufremove` — 缓冲区管理
- `mini.clue` — 快捷键提示
- `mini.cmdline` — 命令行增强
- `mini.comment` — 注释操作
- `mini.diff` — Git diff
- `mini.git` — Git 集成
- `mini.hipatterns` — 高亮模式（TODO/FIXME/颜色值）
- `mini.indentscope` — 缩进可视化
- `mini.jump` / `mini.jump2d` — 跳转
- `mini.keymap` — 多步骤/组合键映射
- `mini.map` — 窗口地图
- `mini.move` — 选择移动
- `mini.operators` — 文本操作符
- `mini.pairs` — 自动配对
- `mini.pick` — 万能拾取器（文件/grep/LSP/等）
- `mini.snippets` — 代码片段管理
- `mini.splitjoin` — 参数分割/合并
- `mini.surround` — 环绕操作
- `mini.trailspace` — 尾部空白管理
- `mini.visits` — 文件访问记录

### 4. 外部插件

`plugin/40_plugins.lua` 管理的非 MINI 插件：

- **nvim-treesitter** + **nvim-treesitter-textobjects** — 语法解析和增量选择
- **nvim-lspconfig** — 语言服务器配置
- **conform.nvim** — 代码格式化
- **friendly-snippets** — 代码片段集合

### 5. Leader 映射设计

采用"双键 Leader 映射"方式：

```
<Leader><group><action>
```

| 前缀 | 含义 |
|------|------|
| `<Leader>b` | Buffer 操作 |
| `<Leader>e` | 探索/编辑配置 |
| `<Leader>f` | 模糊查找 |
| `<Leader>g` | Git 操作 |
| `<Leader>l` | 语言/LSP |
| `<Leader>m` | Map |
| `<Leader>o` | 其他 |
| `<Leader>s` | 会话 |
| `<Leader>t` | 终端 |
| `<Leader>v` | Visits 访问记录 |

## Lockfile 管理的插件

MiniMax 通过 `nvim-pack-lock.json` 记录以下插件的精确版本：

- `mini.nvim`
- `nvim-lspconfig`
- `nvim-treesitter`
- `nvim-treesitter-textobjects`
- `conform.nvim`
- `friendly-snippets`

## 与维基的关联

此来源涉及:
- [[wiki/concepts/Neovim-0.12-Configuration]] - Neovim 0.12 配置页面
- [[wiki/sources/vim-pack-guide]] - vim.pack 深度指南（同一作者）
