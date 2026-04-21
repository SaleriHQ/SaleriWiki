---
title: leap.nvim
source: https://codeberg.org/andyg/leap.nvim
author: andyg
created: 2026-04-12
type: source
tags:
  - source
  - neovim
  - motion
  - plugin
---

## 摘要

leap.nvim 是 Neovim 的运动和选择插件，基于 vim-sneak 构建。允许你以极少的按键次数跳转到屏幕上任何位置，几乎零认知负担。

## 核心特点

- **2-3 键到达屏幕任意位置**：输入 2 个字符即可跳转
- **零认知负担**：无需权衡、组合或暂停
- **Treesitter 集成**：语法树节点选择
- **远程操作**：跨窗口操作文本

## 快速使用

1. 触发命令，输入 2 字符搜索模式 `{char1}{char2}`
2. 输入 `{char1}` 后显示标签预览
3. 输入 `{char2}` 过滤匹配并自动跳转
4. 如需选择，输入标签字符

## 安装配置

```lua
-- 基础按键
vim.keymap.set({ 'n', 'x', 'o' }, 's', '<Plug>(leap)')
vim.keymap.set('n', 'S', '<Plug>(leap-from-window)')

-- 重复搜索（推荐）
vim.keymap.set({ 'n', 'x', 'o' }, '<cr>', function()
  require('leap').leap {
    ['repeat'] = true,
    opts = require('leap.user').with_traversal_keys('<cr>', '<bs>'),
  }
end)
```

## 进阶功能

### Treesitter 节点选择

```lua
vim.keymap.set({ 'x', 'o' }, 'R', function()
  require('leap.treesitter').select {
    opts = require('leap.user').with_traversal_keys('R', 'r')
  }
end)
```

### 远程操作

```lua
-- 跨窗口操作
vim.keymap.set({ 'n', 'o' }, 'gs', function()
  require('leap.remote').action()
end)

-- 示例：gs{leap}yap - 复制远程段落
```

### 增强版 f/t 动作

```lua
vim.keymap.set({ 'n', 'x', 'o' }, 'f', function()
  require('leap').leap({
    inputlen = 1,
    opts = require('leap.user').with_traversal_keys('f', 'F')
  })
end)
```

## 快捷键说明

| 键 | 功能 |
|----|------|
| `s` | 向前跳转（normal/visual/operator） |
| `S` | 从窗口跳转 |
| `<cr>` | 重复上次搜索 |
| `<bs>` | 反向重复搜索 |
| `<space>` | 移动到下一组标签 |
| `<enter>` | 跳转到最近/下一个匹配 |

## 设计理念

> 一个通用的运动方式可用于所有非平凡场景。
> 
> 不需要组合动作：一个命令实现一个逻辑移动。
> 
> 眼睛可以始终专注于目标。

## 相关概念

- [[wiki/concepts/Neovim-0.12-Configuration]]
