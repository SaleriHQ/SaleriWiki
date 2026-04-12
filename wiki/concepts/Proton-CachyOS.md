---
title: Proton-CachyOS
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - gaming
  - cachyos
  - proton
  - wine
sources: 1
---

## 定义

Proton-CachyOS 是基于 Valve 的 Proton `bleeding-edge` 分支构建的 Linux 游戏兼容层，由 CachyOS 团队维护和优化。它允许在 Linux 上运行 Windows 游戏，提供了比原生 Proton 更多的补丁和优化。

## 核心特性

### 包含的修改

| 特性 | 说明 |
|------|------|
| **Wine-staging 补丁** | 最新的 Wine 暂存版优化 |
| **Wine 全屏 FSR** | AMD FidelityFX 超分辨率支持 |
| **多媒体解码器** | 游戏过场动画的视频/音频支持 |
| **umu-launcher** | 统一游戏启动器支持 |
| **UMU-Protonfixes** | 游戏专用修复 |
| **热修复** | 游戏的早期工作区/修复 |

### 版本类型

| 版本 | 特点 |
|------|------|
| `proton-cachyos` | 基础版本，无 SLR 依赖 |
| `proton-cachyos-slr` | **推荐版本**，包含 Steam Linux Runtime 支持，适用于反作弊游戏 |

## 安装方法

### 自动安装（推荐）

```bash
# 标准版
sudo pacman -S cachyos/umu-launcher

# SLR 版本（支持反作弊）
sudo pacman -S proton-cachyos-slr
```

### Steam 手动安装

1. 下载最新版本：https://github.com/CachyOS/proton-cachyos/releases
2. 解压并移动到 `~/.steam/steam/compatibilitytools.d/`
3. 重启 Steam

## 环境变量

### 升频器

```bash
# AMD FSR4
PROTON_FSR4_UPGRADE=1
PROTON_FSR4_RDNA3_UPGRADE=1  # RDNA3 优化

# Nvidia DLSS
PROTON_DLSS_UPGRADE=1
PROTON_DLSS_INDICATOR=1

# Intel XeSS
PROTON_XESS_UPGRADE=1
```

### Nvidia 特性

```bash
PROTON_NVIDIA_NVCUDA=1      # CUDA 支持
PROTON_NVIDIA_NVENC=1        # NVENC 编码
PROTON_NVIDIA_NVML=1         # NVML 监控
PROTON_NVIDIA_NVOPTIX=1      # OptiX 光追
```

## 与其他 Proton 的比较

| Proton 版本 | 维护者 | 特点 |
|------------|--------|------|
| Proton (Valve) | Valve | 稳定，官方支持 |
| Proton Experimental | Valve | 最新功能 |
| **Proton-CachyOS** | CachyOS | 优化补丁多 |
| Proton-GE | GloriousEggroll | 自定义修复 |

## 来源

- [[wiki/sources/cachy-gaming]]

## 相关概念

- [[wiki/concepts/Linux游戏优化]]
- [[wiki/concepts/Lutris]]
