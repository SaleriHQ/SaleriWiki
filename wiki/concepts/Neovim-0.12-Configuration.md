---
title: Neovim 0.12 配置指南
created: 2026-04-10
updated: 2026-04-10
tags:
  - concept
  - neovim
  - editor
  - configuration
sources: 5
related:
  - "[[Clippings/Neovim-0.12-Minimal-Config]]"
  - "[[wiki/sources/vim-pack-guide]]"
---

# Neovim 0.12 配置指南

> **版本**: Neovim 0.12.1
> **来源**: [Neovim 官方文档](https://neovim.io/doc/)

## 概述

Neovim 0.12 是一个重要的里程碑版本，带来了**内置插件管理器** `vim.pack` 等众多新特性。本指南基于官方文档，帮助你从零开始配置一个现代、高效的 Neovim 编辑器。

---

## Neovim 0.12 新特性

### 内置插件管理器 `vim.pack`

```ad-important
title: 重要更新
Neovim 0.12 内置了 `vim.pack` 插件管理器，无需再使用第三方插件管理器（如 packer、lazy 等）！
```

### 其他关键新特性

| 类别 | 新特性 |
|------|--------|
| **内置插件管理器** | `vim.pack` - 原生插件管理，支持安装、更新、删除 |
| **LSP 增强** | 内置 `vim.lsp.config()` 和 `vim.lsp.enable()` |
| **Treesitter** | 改进的语法高亮和增量选择 |
| **UI/UX** | 新 TUI 进度条、改进的错误提示 |
| **性能** | 大幅减少启动时间和渲染延迟 |
| **编辑体验** | 改进的补全菜单、snippet 支持 |

---

## 目录结构

### 配置文件位置

```bash
# 查看配置目录
nvim --headless -c 'echo stdpath("config")' -c 'quit'
# Linux/macOS: ~/.config/nvim
# Windows: ~/AppData/Local/nvim
```

### 推荐目录结构

```
~/.config/nvim/
├── init.lua              # 主配置文件
├── lua/                  # Lua 模块目录
│   └── mymodules/        # 自定义模块
│       └── utils.lua
├── lsp/                  # LSP 配置目录
│   └── *.lua             # 每个语言服务器的配置文件
├── plugin/               # 插件配置（可选）
│   └── *.lua
└── after/                # after 目录（可选）
    └── plugin/
```

---

## 基础配置 (`init.lua`)

### 基础选项设置

```lua
-- ~/.config/nvim/init.lua

-- ===========================
-- 1. 基础设置
-- ===========================

-- 启用更多内置功能
vim.g.loaded_netrw = 1      -- 禁用内置文件浏览器
vim.g.loaded_netrwPlugin = 1

-- 设置 Leader 键
vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

-- ===========================
-- 2. 选项设置 (vim.opt)
-- ===========================

local opt = vim.opt

-- 通用设置
opt.number = true                    -- 显示行号
opt.relativenumber = true            -- 显示相对行号
opt.cursorline = true                -- 高亮当前行
opt.mouse = 'a'                      -- 启用鼠标支持
opt.clipboard = 'unnamedplus'        -- 使用系统剪贴板
opt.termguicolors = true              -- 启用真彩色

-- 缩进设置
opt.expandtab = true                  -- 使用空格代替 Tab
opt.shiftwidth = 2                    -- 缩进宽度
opt.tabstop = 2                       -- Tab 字符宽度
opt.softtabstop = 2                   -- 软 Tab 宽度
opt.smartindent = true                -- 智能缩进

-- 搜索设置
opt.ignorecase = true                 -- 忽略大小写
opt.smartcase = true                  -- 智能大小写
opt.hlsearch = true                   -- 高亮搜索结果
opt.incsearch = true                  -- 增量搜索

-- UI 设置
opt.signcolumn = 'yes'               -- 显示符号列
opt.splitright = true                -- 右侧分割窗口
opt.splitbelow = true                 -- 下方分割窗口
opt.encoding = 'utf-8'                -- 编码设置
opt.scrolloff = 8                     -- 滚动时保留上下文
opt.sidescrolloff = 8

-- 文件设置
opt.backup = false                    -- 禁用备份
opt.writebackup = false
opt.swapfile = false                 -- 禁用交换文件
opt.undofile = true                  -- 持久化撤销历史

-- 命令行设置
opt.cmdheight = 1                     -- 命令行高度
opt.showmode = false                  -- 隐藏模式显示
opt.showcmd = true                    -- 显示命令

-- 状态栏设置
opt.laststatus = 3                   -- 全局状态栏
opt.ruler = false                     -- 关闭标尺
```

### 常用映射

```lua
-- ===========================
-- 3. 常用键映射 (vim.keymap.set)
-- ===========================

local keymap = vim.keymap.set

-- 空格键作为 Leader 的映射
keymap('n', '<leader>w', ':write<CR>', { desc = '保存文件' })
keymap('n', '<leader>q', ':quit<CR>', { desc = '退出' })
keymap('n', '<leader>Q', ':quit!<CR>', { desc = '强制退出' })

-- 窗口导航
keymap('n', '<C-h>', '<C-w>h', { desc = '移动到左侧窗口' })
keymap('n', '<C-j>', '<C-w>j', { desc = '移动到下方窗口' })
keymap('n', '<C-k>', '<C-w>k', { desc = '移动到上方窗口' })
keymap('n', '<C-l>', '<C-w>l', { desc = '移动到右侧窗口' })

-- 窗口调整
keymap('n', '<leader>h', ':vertical resize -3<CR>', { desc = '减小宽度' })
keymap('n', '<leader>l', ':vertical resize +3<CR>', { desc = '增加宽度' })
keymap('n', '<leader>j', ':resize -3<CR>', { desc = '减小高度' })
keymap('n', '<leader>k', ':resize +3<CR>', { desc = '增加高度' })

-- 标签页操作
keymap('n', '<leader>t', ':tabnew<CR>', { desc = '新建标签页' })
keymap('n', '<leader>x', ':tabclose<CR>', { desc = '关闭标签页' })
keymap('n', '<leader>1', '1gt', { desc = '切换到标签页 1' })
keymap('n', '<leader>2', '2gt', { desc = '切换到标签页 2' })

-- 文本操作
keymap('n', '<leader>y', '"+y', { desc = '复制到系统剪贴板' })
keymap('v', '<leader>y', '"+y', { desc = '复制到系统剪贴板' })
keymap('n', '<leader>p', '"+p', { desc = '从系统剪贴板粘贴' })
keymap('n', '<leader>d', '"_d', { desc = '删除到黑洞寄存器' })
keymap('v', '<leader>d', '"_d', { desc = '删除到黑洞寄存器' })

-- LSP 相关映射（使用 Neovim 0.11+ 内置映射）
-- grn - 重命名
-- gra - 代码操作
-- gri - 查找实现
-- grr - 查找引用
-- gO - 文档符号
```

---

## 内置插件管理器 (`vim.pack`)

### 基本用法

`vim.pack` 是 Neovim 0.12 新增的内置插件管理器，无需安装任何第三方插件即可管理插件。

### 安装插件

```lua
-- ~/.config/nvim/init.lua

-- ===========================
-- 4. 使用 vim.pack 安装插件
-- ===========================

vim.pack.add({
  -- 直接使用 URL
  'https://github.com/nvim-tree/nvim-tree.lua',

  -- 指定插件名称
  { src = 'https://github.com/nvim-tree/nvim-tree.lua', name = 'nvim-tree' },

  -- 指定版本/分支
  {
    src = 'https://github.com/nvim-tree/nvim-tree.lua',
    version = vim.version.range('1.0'),  -- 使用 semver 范围
  },

  -- 使用分支
  {
    src = 'https://github.com/nvim-tree/nvim-tree.lua',
    version = 'main',  -- 或 'master' 或 commit hash
  },
})
```

### 使用简写来源

```lua
-- 方法 1: 创建辅助函数
local gh = function(x) return 'https://github.com/' .. x end
vim.pack.add({
  gh('nvim-tree/nvim-tree.lua'),
  gh('nvim-lualine/lualine.nvim'),
  gh('nvim-treesitter/nvim-treesitter'),
})

-- 方法 2: 配置 Git 的 insteadOf
-- git config --global url."https://github.com/".insteadOf "gh:"
-- 然后在 init.lua 中:
vim.pack.add({
  'gh:nvim-tree/nvim-tree.lua',
  'gh:nvim-lualine/lualine.nvim',
})
```

### 更新插件

```vim
" 在 Neovim 中执行
:vim.pack.update()

" 或者强制更新所有插件
:lua vim.pack.update(nil, { force = true })

" 更新指定插件
:lua vim.pack.update({ 'nvim-tree' })

" 查看已安装的插件（离线模式）
:lua vim.pack.update(nil, { offline = true })
```

### 删除插件

```lua
-- 从 init.lua 中移除插件配置后重启

-- 删除不再需要的插件
vim.pack.del({ '过时插件名称' })
```

### 插件钩子 (Hooks)

```lua
-- 监听插件状态变化
vim.api.nvim_create_autocmd('PackChanged', {
  callback = function(ev)
    local name = ev.data.spec.name
    local kind = ev.data.kind  -- 'install', 'update', 'delete'

    -- 插件安装或更新后执行构建
    if kind == 'install' or kind == 'update' then
      if name == 'some-plugin-needing-build' then
        vim.system({ 'make' }, { cwd = ev.data.path })
      end
    end
  end,
})
```

### 推荐的 10 个核心插件

```lua
-- ~/.config/nvim/init.lua 中的插件部分

-- ===========================
-- 精选插件列表
-- ===========================

vim.pack.add({
  -- 文件树
  'https://github.com/nvim-tree/nvim-tree.lua',

  -- 状态栏
  'https://github.com/nvim-lualine/lualine.nvim',

  -- 语法高亮
  'https://github.com/nvim-treesitter/nvim-treesitter',

  -- LSP 配置（如果需要更高级的 LSP 功能）
  -- 'https://github.com/neovim/nvim-lspconfig',

  -- 模糊查找
  'https://github.com/nvim-telescope/telescope.nvim',

  -- Git 集成
  'https://github.com/lewis6991/gitsigns.nvim',

  -- 缩进线
  'https://github.com/lukas-reineke/indent-blankline.nvim',

  -- 括号匹配
  'https://github.com/windwp/nvim-autopairs',

  -- 注释
  'https://github.com/numToStr/Comment.nvim',

  -- 颜色高亮（预览颜色值）
  'https://github.com/NvChad/nvim-colorizer.lua',
})
```

---

## LSP 配置 (内置)

Neovim 0.11+ 内置了 LSP 客户端，可以直接使用，无需第三方插件。

### 基本 LSP 配置

```lua
-- ~/.config/nvim/init.lua

-- ===========================
-- 5. LSP 配置
-- ===========================

-- 配置 TypeScript/JavaScript LSP
vim.lsp.config['ts_ls'] = {
  cmd = { 'typescript-language-server', '--stdio' },
  filetypes = { 'javascript', 'javascriptreact', 'typescript', 'typescriptreact' },
  root_markers = { 'package.json', 'tsconfig.json', '.git' },
}

-- 配置 Lua LSP (需要安装 lua-language-server)
vim.lsp.config['lua_ls'] = {
  cmd = { 'lua-language-server' },
  filetypes = { 'lua' },
  root_markers = { '.luarc.json', '.luarc.jsonc', '.git' },
  settings = {
    Lua = {
      runtime = {
        version = 'LuaJIT',
      },
      diagnostics = {
        globals = { 'vim' },
      },
      workspace = {
        library = vim.api.nvim_get_runtime_file('', true),
      },
    },
  },
}

-- 配置 Python LSP (需要安装 pyright)
vim.lsp.config['pyright'] = {
  cmd = { 'pyright-langserver', '--stdio' },
  filetypes = { 'python' },
  root_markers = { 'pyproject.toml', 'setup.py', '.git' },
}

-- 启用所有配置的 LSP
vim.lsp.enable('ts_ls')
vim.lsp.enable('lua_ls')
vim.lsp.enable('pyright')
```

### LSP 配置目录方式

```
~/.config/nvim/
└── lsp/
    ├── ts_ls.lua
    ├── lua_ls.lua
    └── pyright.lua
```

```lua
-- ~/.config/nvim/lsp/lua_ls.lua
return {
  cmd = { 'lua-language-server' },
  filetypes = { 'lua' },
  root_markers = { '.luarc.json', '.git' },
  settings = {
    Lua = {
      runtime = { version = 'LuaJIT' },
      diagnostics = { globals = { 'vim' } },
      workspace = {
        library = vim.api.nvim_get_runtime_file('', true),
      },
    },
  },
}
```

```vim
" 启用方式：创建文件后执行
:lua vim.lsp.enable('lua_ls')
```

### 自定义 LSP 键映射

```lua
-- LSP 附加事件处理
vim.api.nvim_create_autocmd('LspAttach', {
  callback = function(ev)
    local client = vim.lsp.get_client_by_id(ev.data.client_id)

    -- 自定义键映射
    vim.keymap.set('n', 'gd', vim.lsp.buf.definition, {
      buffer = ev.buf,
      desc = '跳转到定义',
    })
    vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, {
      buffer = ev.buf,
      desc = '跳转到声明',
    })
    vim.keymap.set('n', 'K', vim.lsp.buf.hover, {
      buffer = ev.buf,
      desc = '显示 Hover 信息',
    })
    vim.keymap.set('n', '<leader>ca', vim.lsp.buf.code_action, {
      buffer = ev.buf,
      desc = '代码操作',
    })
    vim.keymap.set('n', '<leader>rn', vim.lsp.buf.rename, {
      buffer = ev.buf,
      desc = '重命名',
    })
  end,
})
```

### LSP 默认快捷键

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `grn` | 重命名 | `vim.lsp.buf.rename()` |
| `gra` | 代码操作 | `vim.lsp.buf.code_action()` |
| `gri` | 查找实现 | `vim.lsp.buf.implementation()` |
| `grr` | 查找引用 | `vim.lsp.buf.references()` |
| `grt` | 类型定义 | `vim.lsp.buf.type_definition()` |
| `gO` | 文档符号 | `vim.lsp.buf.document_symbol()` |
| `grx` | CodeLens | `vim.lsp.codelens.run()` |
| `Ctrl-S` | 签名帮助 | Insert 模式下 |
| `K` | Hover | Normal 模式 |

---

## Treesitter 配置

### 安装语言解析器

```lua
-- ~/.config/nvim/init.lua

-- ===========================
-- 6. Treesitter 配置
-- ===========================

-- 确保在插件加载后执行
vim.api.nvim_create_autocmd('BufReadPost', {
  pattern = '*',
  callback = function()
    local ts = require('nvim-treesitter.configs')

    ts.setup({
      ensure_installed = {
        'lua',
        'vim',
        'vimdoc',
        'javascript',
        'typescript',
        'python',
        'rust',
        'go',
        'markdown',
        'markdown_inline',
        'html',
        'css',
        'json',
        'yaml',
        'toml',
        'bash',
        'dockerfile',
      },
      sync_install = false,
      auto_install = true,

      highlight = {
        enable = true,
        additional_vim_regex_highlighting = false,
      },

      indent = {
        enable = true,
      },

      incremental_selection = {
        enable = true,
        keymaps = {
          init_selection = '<CR>',
          node_incremental = '<CR>',
          scope_incremental = '<S-CR>',
          node_decremental = '<BS>',
        },
      },
    })
  end,
})
```

---

## 自动命令 (Autocmd)

```lua
-- ~/.config/nvim/init.lua

-- ===========================
-- 7. 自动命令
-- ===========================

-- 高亮复制内容
vim.api.nvim_create_autocmd('TextYankPost', {
  callback = function()
    vim.highlight.on_yank({ higroup = 'IncSearch', timeout = 200 })
  end,
  desc = '复制时高亮',
})

-- 自动去除尾随空格
vim.api.nvim_create_autocmd('BufWritePre', {
  pattern = '*',
  callback = function()
    vim.cmd([[%s/\s\+$//e]])
  end,
  desc = '保存前去除尾随空格',
})

-- 自动设置换行格式
vim.api.nvim_create_autocmd('FileType', {
  pattern = { 'python', 'lua', 'javascript', 'typescript' },
  callback = function()
    vim.opt_local.formatoptions:remove({ 't' })
  end,
  desc = '代码文件禁用自动换行',
})

-- 文件类型检测后设置
vim.api.nvim_create_autocmd('FileType', {
  pattern = 'qf',
  callback = function()
    vim.opt_local.number = false
    vim.opt_local.relativenumber = false
  end,
  desc = 'Quickfix 窗口禁用行号',
})
```

---

## 完整示例配置

```lua
-- ~/.config/nvim/init.lua
-- Neovim 0.12 完整配置示例

-- ============================================================
-- 1. 基础设置
-- ============================================================

vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

-- ============================================================
-- 2. 选项设置
-- ============================================================

local opt = vim.opt

opt.number = true
opt.relativenumber = true
opt.cursorline = true
opt.mouse = 'a'
opt.clipboard = 'unnamedplus'
opt.termguicolors = true

opt.expandtab = true
opt.shiftwidth = 2
opt.tabstop = 2
opt.softtabstop = 2
opt.smartindent = true

opt.ignorecase = true
opt.smartcase = true
opt.hlsearch = true
opt.incsearch = true

opt.signcolumn = 'yes'
opt.splitright = true
opt.splitbelow = true
opt.encoding = 'utf-8'
opt.scrolloff = 8
opt.sidescrolloff = 8

opt.backup = false
opt.writebackup = false
opt.swapfile = false
opt.undofile = true

opt.cmdheight = 1
opt.showmode = false
opt.showcmd = true
opt.laststatus = 3

-- ============================================================
-- 3. 键映射
-- ============================================================

local keymap = vim.keymap.set

-- 保存退出
keymap('n', '<leader>w', ':write<CR>', { desc = '保存' })
keymap('n', '<leader>q', ':quit<CR>', { desc = '退出' })
keymap('n', '<leader>Q', ':quit!<CR>', { desc = '强制退出' })

-- 窗口导航
keymap('n', '<C-h>', '<C-w>h', { desc = '左窗口' })
keymap('n', '<C-j>', '<C-w>j', { desc = '下窗口' })
keymap('n', '<C-k>', '<C-w>k', { desc = '上窗口' })
keymap('n', '<C-l>', '<C-w>l', { desc = '右窗口' })

-- 复制到剪贴板
keymap('n', '<leader>y', '"+y', { desc = '复制' })
keymap('v', '<leader>y', '"+y', { desc = '复制' })
keymap('n', '<leader>p', '"+p', { desc = '粘贴' })

-- ============================================================
-- 4. 插件管理 (vim.pack)
-- ============================================================

vim.pack.add({
  'https://github.com/nvim-tree/nvim-tree.lua',
  'https://github.com/nvchad/nvim-colorizer.lua',
  'https://github.com/nvim-lualine/lualine.nvim',
})

-- ============================================================
-- 5. LSP 配置
-- ============================================================

vim.lsp.config['lua_ls'] = {
  cmd = { 'lua-language-server' },
  filetypes = { 'lua' },
  root_markers = { '.luarc.json', '.git' },
  settings = {
    Lua = {
      runtime = { version = 'LuaJIT' },
      diagnostics = { globals = { 'vim' } },
    },
  },
}

vim.lsp.enable('lua_ls')

-- ============================================================
-- 6. 自动命令
-- ============================================================

vim.api.nvim_create_autocmd('TextYankPost', {
  callback = function()
    vim.highlight.on_yank({ higroup = 'IncSearch', timeout = 200 })
  end,
  desc = '复制高亮',
})

-- ============================================================
-- 7. 配色方案
-- ============================================================

vim.cmd.colorscheme('habamax')
```

---

## 常见问题

### Q: 如何查看配置目录？

```vim
:echo stdpath('config')  " 配置目录
:echo stdpath('data')    " 数据目录
:echo stdpath('state')   " 状态目录
:echo stdpath('cache')   " 缓存目录
```

### Q: 如何诊断问题？

```vim
:checkhealth          " 运行健康检查
:checkhealth vim.lsp  " 检查 LSP
:checkhealth provider " 检查 Provider
```

### Q: 如何调试启动时间？

```bash
nvim --startuptime /tmp/startup.log
cat /tmp/startup.log
```

### Q: 如何禁用插件进行调试？

```bash
nvim --noplugin        " 不加载插件
nvim --clean           " 干净启动
```

### Q: 如何安装语言服务器？

```bash
# TypeScript
npm install -g typescript typescript-language-server

# Lua
brew install lua-language-server  # macOS
# 或从 https://github.com/LuaLS/lua-language-server/releases 下载

# Python
pip install pyright

# Go
go install golang.org/x/tools/gopls@latest

# Rust
rustup component add rust-analyzer
```

---

## 相关资源

- **官方文档**: https://neovim.io/doc/
- **GitHub**: https://github.com/neovim/neovim
- **社区插件**: https://neovimcraft.com/
- **LSP 服务器列表**: https://microsoft.github.io/language-server-protocol/implementors/servers/

---

## 来源

- [[Clippings/Neovim-0.12-Minimal-Config]] - YouTube 教程摘要
- Neovim 官方文档 (内置): `news.txt`, `lsp.txt`, `pack.txt`, `lua-guide.txt`, `starting.txt`
