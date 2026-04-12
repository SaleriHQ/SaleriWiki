---
title: CachyOS 游戏指南
source: https://wiki.cachyos.org/configuration/gaming/
author: CachyOS Team
created: 2026-04-12
type: source
tags:
  - source
  - cachyos
  - gaming
  - linux
---

## 摘要

CachyOS 游戏设置指南涵盖了在 CachyOS 上进行游戏所需的一切配置。内容包括游戏包的安装、Steam Proton 游戏设置、各种 Proton 版本的选择、Lutris 游戏管理器的使用，以及热门游戏的脚本安装器。

**重要提醒**：软件优化不能替代硬件升级，获得双位数 FPS 提升并非总是可行，取决于游戏和硬件配置。

## 核心组件

### Proton-CachyOS

基于 Proton `bleeding-edge` 分支，包含：
- **Wine-staging 补丁** - 最新 Wine 优化
- **Wine 全屏 FSR** - AMD FSR 超分辨率支持
- **视频/音频解码器** - 游戏过场动画支持
- **umu-launcher 支持** - 包含 UMU-Protonfixes
- **热修复** - 游戏的早期修复/变通方案

### Wine-CachyOS

Proton-CachyOS 的独立版本，可用于 Lutris、Heroic、Bottles 等。

### 游戏元包

```bash
# CachyOS Hello -> Apps/Tweaks -> Install Gaming packages
# 安装：cachyos-gaming-meta + cachyos-gaming-applications
```

## 启动选项格式

```bash
<环境变量> <包装器> %command% <应用参数>
```

**示例**：
```bash
__GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1 prime-run game-performance %command% -dx11
```

## 关键环境变量

| 变量 | 说明 |
|------|------|
| `PROTON_DLSS_UPGRADE=1` | 自动升级 DLSS |
| `PROTON_FSR4_UPGRADE=1` | 自动升级 FSR4 |
| `PROTON_XESS_UPGRADE=1` | 自动升级 XeSS |
| `MESA_SHADER_CACHE_MAX_SIZE=12G` | AMD Shader 缓存大小 |
| `__GL_SHADER_DISK_CACHE_SIZE=12000000000` | Nvidia Shader 缓存大小 |

## Proton 版本选择

| 版本 | 用途 |
|------|------|
| Proton 10.0 | 稳定版，通用游戏 |
| Proton Experimental | 新游戏/实验性功能 |
| proton-cachyos-slr | **推荐**，含反作弊支持 |
| proton-cachyos | 无 SLR 依赖版本 |
| Proton-GE | GloriousEggroll 自定义构建 |

## 性能优化

### game-performance 脚本

临时切换到性能模式，游戏退出后自动恢复：
```bash
game-performance %command%
```

### 防止 gamemode 与 ananicy-cpp 冲突

```bash
systemctl stop ananicy-cpp
```

## 相关概念

- [[wiki/concepts/Proton-CachyOS]]
- [[wiki/concepts/Linux游戏优化]]
- [[wiki/concepts/Lutris]]
