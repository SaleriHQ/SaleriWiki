---
title: Minimal Neovim v0.12 配置指南
source: https://vieitesss.github.io/posts/Neovim-new-config/#lsp
author: Daniel Vieites Torres
created: 2026-04-12
type: source
tags:
  - source
  - neovim
  - configuration
  - lua
---

## 摘要

Neovim v0.12 带来了新的 LSP API 和内置包管理器。本文展示了如何用 **少于 10 个插件** 构建完整的 Neovim 配置，将配置从近 2000 行减少到 500 行以下。

## 目录结构

```
~/.config/nvim/
├── init.lua
├── lua/
│   ├── autocmds.lua
│   ├── configs.lua
│   ├── keymaps.lua
│   ├── lsp.lua
│   ├── plugins.lua
│   └── statusline.lua
└── lsp/
    ├── rust-analyzer.lua
    ├── gopls.lua
    ├── lua_ls.lua
    └── ...
```

## 核心插件

| 插件 | 用途 |
|------|------|
| **gitsigns.nvim** | Git 状态显示 |
| **mason.nvim** | LSP 服务器管理 |
| **blink.cmp** | 代码补全（支持模糊匹配） |
| **fzf-lua** | 模糊搜索 |
| **vim-fugitive** | Git 集成 |
| **techbase.nvim** | 配色方案 |

## 关键配置

### vim.pack（内置包管理器）

```lua
vim.pack.add({
    { src = "https://github.com/lewis6991/gitsigns.nvim" },
})
```

### LSP 配置（原生 vim.lsp）

```lua
vim.lsp.enable({
  "bashls",
  "gopls",
  "lua_ls",
  "texlab",
  "ts_ls",
  "rust-analyzer",
})

vim.diagnostic.config({ virtual_text = true })
```

### blink.cmp 配置

```lua
require('blink.cmp').setup({
    fuzzy = { implementation = 'prefer_rust_with_warning' },
    signature = { enabled = true },
    keymap = { preset = "default" },
    sources = { default = { "lsp" } }
})
```

## 核心观点

> 使用内置功能和最小化插件配置，保持配置简洁。

## 相关概念

- [[wiki/concepts/Neovim-0.12-Configuration]]
