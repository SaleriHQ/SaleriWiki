---
title: A Guide to vim.pack
source: https://echasnovski.com/blog/2026-03-13-a-guide-to-vim-pack.html
author: Evgeni Chasnovski
created: 2026-04-10
type: source
tags:
  - source
  - neovim
  - plugin-manager
---

## 摘要

Neovim 0.12 内置的 `vim.pack` 是官方原生插件管理器，完全使用 Lua 实现。这篇由 Evgeni Chasnovski（mini.nvim 作者）撰写的指南详细讲解了 `vim.pack` 的工作原理、最佳实践和使用方法。`vim.pack` 基于 Vim packages 机制，将所有插件统一安装到 `core` 包中作为 "opt" 插件，支持 lockfile 版本锁定、自动加载和 hooks 钩子机制。

## 关键概念

- **vim.pack**: Neovim 0.12 内置的原生插件管理器，通过 `vim.pack.add()` 安装/加载插件
- **Plugin Package**: Neovim/Vim 的插件包机制，`pack/` 子目录下组织 `start/` 和 `opt/` 插件
- **Runtime Files**: Neovim 运行时文件（Lua 模块、plugin 脚本、ftplugin 等），由 `'runtimepath'` 控制搜索路径
- **start/opt 插件**: start 插件启动时自动加载，opt 插件需 `:packadd` 按需加载
- **Lockfile**: `nvim-pack-lock.json` 记录所有插件状态，用于新机器引导和版本回滚
- **Hooks**: 通过 `PackChanged` / `PackChangedPre` autocmd 监听插件安装/更新/删除事件

## 核心 API

| API | 说明 |
|-----|------|
| `vim.pack.add()` | 安装并加载插件（主要接口） |
| `vim.pack.update()` | 更新已安装的插件 |
| `vim.pack.del()` | 从磁盘删除插件 |

## 配置组织方式

1. **单一 `vim.pack.add()`**: 最稳健的方式，在 `init.lua` 中一次性列出所有插件
2. **多个 `vim.pack.add()`**: 将插件分散到 `plugin/` 目录下的多个文件中，实现模块化配置
3. **Lazy Loading**: 通过 `vim.schedule()` 或 autocmd 延迟加载插件

## 与第三方插件管理器的迁移

- **mini.deps**: `MiniDeps.add()` → `vim.pack.add()`，hooks 改用 autocmd 形式
- **lazy.nvim**: 去掉 `cmd/event/ft/keys` 字段，`lua/plugins/` 目录 → `plugin/` 目录
- 注意：`lazy.nvim` 的 lazy loading 特性会导致启动时间优势，但结合 `vim.loader.enable()` 可弥补差距

## 与维基的关联

此来源涉及:
- [[wiki/concepts/Neovim-0.12-Configuration]] - Neovim 配置页面（已包含 vim.pack 基础用法）
