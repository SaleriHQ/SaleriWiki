---
title: Lutris
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - gaming
  - linux
  - launcher
sources: 1
---

## 定义

Lutris 是一个开源的 Linux 游戏启动器，支持管理 Wine、Proton、各种模拟器和原生游戏。它提供了一个统一的界面来配置游戏运行环境、启动参数和第三方商店。

## 核心功能

| 功能 | 说明 |
|------|------|
| **统一管理** | 一个界面管理所有游戏来源 |
| **多运行时** | 支持 Wine、Proton、Steam、模拟器 |
| **脚本安装器** | 社区维护的游戏安装脚本 |
| **商店集成** | Epic、GOG、EA、Ubisoft 等 |

## 支持的平台/商店

- [EA App](https://lutris.net/games/ea-app/)
- [Epic Games Store](https://lutris.net/games/epic-games-store/)
- [GOG Galaxy](https://lutris.net/games/gog-galaxy/)
- [Steam](https://lutris.net/games/steam/)
- [Ubisoft Connect](https://lutris.net/games/ubisoft-connect/)

## 配置 Proton-CachyOS

### 全局配置

1. 点击 Lutris 主界面 Wine 旁边的齿轮图标
2. 进入 **Runner Options** 标签页
3. 设置：
   - **Wine version** = `proton-cachyos`
   - **Use System winetricks** = 禁用

4. 进入 **System Options** 标签页
   - **Disable Lutris Runtime** = 启用
   - **Prefer system libraries** = 启用

5. 在 **Environment variables** 添加：
   - `UMU_RUNTIME_UPDATE` = `0`（可选，跳过 SLR 更新）
   - `PROTON_VERB` = `waitforexitandrun`（可选，配合 protonfixes）

### 启动选项格式

| 选项类型 | 放置位置 |
|----------|----------|
| 应用参数 (`-dx11`) | **Game options** → **Arguments** |
| 包装器 (`mangohud --dlsym`) | **System options** → **Command prefix** |
| 环境变量 (`PROTON_ENABLE_HDR=1`) | **System options** → **Environment variables** |

## 与 Steam 的比较

| 特性 | Steam | Lutris |
|------|-------|--------|
| 原生游戏 | 支持 | 支持 |
| Windows 游戏 | Proton | Wine/Proton |
| 第三方商店 | 仅 Epic | Epic、GOG、EA、Ubisoft |
| 模拟器 | 不支持 | 支持 |
| 配置复杂度 | 简单 | 复杂但灵活 |

## 安装

```bash
# CachyOS
sudo pacman -S lutris

# 其他发行版
# 见 https://lutris.net/downloads/
```

## 来源

- [[wiki/sources/cachy-gaming]]

## 相关概念

- [[wiki/concepts/Proton-CachyOS]]
- [[wiki/concepts/Linux游戏优化]]
