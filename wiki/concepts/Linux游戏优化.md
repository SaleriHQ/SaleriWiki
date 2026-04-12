---
title: Linux 游戏优化
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - gaming
  - linux
  - performance
sources: 1
---

## 定义

在 Linux 系统上通过软件配置优化游戏性能的技术和方法。这些优化包括图形驱动设置、CPU 调度器调整、Shader 缓存、帧率限制等。

## 核心优化策略

### 1. 电源管理

使用 `game-performance` 脚本临时切换到性能模式：

```bash
game-performance %command%
```

- 提升系统电源级别
- 将 CPU 调度器设置为 performance
- 游戏退出后自动恢复

**注意**：不要同时使用 `gamemode` 和 `ananicy-cpp`，会冲突：
```bash
systemctl stop ananicy-cpp
```

### 2. Shader 缓存

#### AMD GPU

```bash
# 增加 Shader 缓存到 12GB
MESA_SHADER_CACHE_MAX_SIZE=12G
```

#### Nvidia GPU

```bash
# 增加 Shader 缓存
__GL_SHADER_DISK_CACHE_SIZE=12000000000
__GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1
```

配置文件：`~/.config/environment.d/gaming.conf`

### 3. 游戏启动器配置

#### Steam 启动选项格式

```bash
<环境变量> <包装器> %command% <应用参数>
```

**示例**：
```bash
# AMD FSR + 性能模式
PROTON_FSR4_UPGRADE=1 game-performance %command%

# Nvidia + DX11
__GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1 prime-run game-performance %command% -dx11
```

### 4. 常用游戏工具

| 工具 | 用途 |
|------|------|
| **mangohud** | 显示 FPS/硬件信息叠加层 |
| **gamescope** | Wayland 游戏合成器，支持 FSR |
| **gamemode** | 系统性能优化 |
| **dlss-swapper** | 升级游戏 DLSS 版本 |

## 游戏黑屏修复

Steam 游戏录制功能可能导致卡顿：

```bash
LD_PRELOAD="" %command%
```

## 常见问题

### Nvidia DirectX12 性能下降

Linux 下 Nvidia 驱动的 GPU 调度与 Windows 不同，目前无已知解决方案。

### Shader 重新编译

Shader 缓存超过限制会导致每次启动重新编译。增加缓存大小可解决。

## 关键原则

> **软件优化不能替代硬件升级**
>
> 双位数 FPS 提升并非总是可行，取决于游戏和硬件配置。

## 来源

- [[wiki/sources/cachy-gaming]]

## 相关概念

- [[wiki/concepts/Proton-CachyOS]]
- [[wiki/concepts/Lutris]]
