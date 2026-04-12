---
title: fzf-lua
source: https://github.com/ibhagwan/fzf-lua
author: ibhagwan
created: 2026-04-12
type: source
tags:
  - source
  - neovim
  - fuzzy-search
  - lua
---

## 摘要

fzf-lua 是用 Lua 重写的现代化 fzf.vim，提供文件搜索、Git 操作、LSP 集成等丰富功能。基于 fzf 核心，支持异步运行，性能优异。

## 依赖

- Neovim >= 0.9
- fzf > 0.36 或 skim
- nvim-web-devicons（可选，图标支持）

## 快速开始

```bash
# 一键测试（沙盒模式）
sh -c "$(curl -s https://raw.githubusercontent.com/ibhagwan/fzf-lua/main/scripts/mini.sh)"
```

## 核心命令

### 文件和缓冲区

| 命令 | 功能 |
|------|------|
| `files` | 文件搜索 |
| `buffers` | 缓冲区列表 |
| `oldfiles` | 历史文件 |
| `global` | VSCode 风格全局搜索器 |

### 搜索

| 命令 | 功能 |
|------|------|
| `grep` | 正则搜索 |
| `live_grep` | 实时搜索 |
| `grep_cword` | 搜索光标下单词 |

### Git

| 命令 | 功能 |
|------|------|
| `git_files` | Git 文件 |
| `git_status` | Git 状态 |
| `git_hunks` | Git 变更块 |
| `git_commits` | Git 提交 |

### LSP

| 命令 | 功能 |
|------|------|
| `lsp_references` | 引用查找 |
| `lsp_definitions` | 定义跳转 |
| `lsp_code_actions` | 代码 Action |
| `lsp_finder` | LSP 综合视图 |

## 基础配置

```lua
require("fzf-lua").setup({
    winopts = { backdrop = 85 },
    keymap = {
        builtin = {
            ["<C-f>"] = "preview-page-down",
            ["<C-b>"] = "preview-page-up",
        },
    },
    actions = {
        files = {
            ["enter"] = require('fzf-lua.actions').file_edit_or_qf,
            ["ctrl-h"] = require('fzf-lua.actions').toggle_hidden,
        }
    }
})

-- 快捷键
vim.keymap.set('n', '<leader>ff', '<cmd>FzfLua files<CR>')
vim.keymap.set('n', '<leader>fg', '<cmd>FzfLua live_grep<CR>')
```

## 常用快捷键

| 快捷键 | 命令 |
|--------|------|
| `<C-p>` | 文件搜索 |
| `<C-g>` | grep |
| `<C-\>` | 缓冲区 |
| `<leader>gs` | Git 状态 |

## 相关概念

- [[wiki/concepts/Neovim-0.12-Configuration]]
