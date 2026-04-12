---
title: "CachyOS 游戏指南"
source: "https://wiki.cachyos.org/configuration/gaming/"
author: "CachyOS 团队"
published: 2026-03-26
created: 2026-04-12
description: "本指南涵盖游戏包的安装、Steam Proton 游戏配置、各种 Proton 版本选择、Lutris 作为游戏统一管理平台，以及热门游戏的脚本安装器。"
tags:
  - "clippings"
  - "翻译"
---

欢迎来到 CachyOS 游戏指南。本指南将帮助你完成游戏环境的所有必要配置。

首先，请记住：

**请注意，获得两位数的 FPS 提升并非总是可行，甚至可能完全无法实现。有时候，优化只能带来微小的改善，甚至完全没有改善，这取决于游戏和硬件配置。**

**你不能指望软件优化能像免费的硬件升级一样工作。**

![](https://wiki.cachyos.org/_astro/gaming-meme.Dc0lFTAL.jpeg)

## 前置要求

### 必需的软件包

为了简化 CachyOS 的游戏环境配置，所有必要的游戏包都被整合到一个元包中，包含 Linux 游戏所需的所有依赖和库，还有一个单独的软件包用于工具和启动器/商店。

**如果你发现缺少任何软件包，请告知 CachyOS 团队。**

按照以下步骤开始游戏配置。

- 打开 CachyOS Hello。进入 **Apps/Tweaks**，点击 `Install Gaming packages`。

*CachyOS Hello 会同时安装 `cachyos-gaming-meta` 和 `cachyos-gaming-applications`。*

## Proton-CachyOS

Proton-CachyOS 基于 Proton 的 `bleeding-edge` 分支，并在其基础上应用了大量修改：

- **Wine-staging 补丁**
- **Wine 全屏 FSR**（AMD  FidelityFX 超分辨率）
- **包含游戏过场动画的视频和音频解码器**
- **支持 umu-launcher，包括 UMU-Protonfixes**
- **为游戏添加了早期的热修复/变通方案**

### 如何正确设置多个启动选项

Steam 中的启动选项使用以下格式构造：

```bash
<环境变量> <包装器> %command% <应用程序参数>
```

- **`<环境变量>`**：形式为 `变量名=值` 的选项
  ```bash
  PROTON_DXVK_D3D8=1
  # 或
  DXVK_HUD="fps,memory,version,api"
  ```
- **`<包装器>`**：修改实际应用程序运行方式的应用程序和脚本。包装器的参数通常放在包装器可执行文件之后。
  ```bash
  mangohud --dlsym
  # 或
  gamescope -W 1680 -H 1050 -w 1280 -h 720 -S fit -F fsr --mangoapp --
  ```
- **`%command%`**：这是实际的应用程序。必须原样指定，Steam 会在运行游戏时将其替换为正确的命令。
- **`<应用程序参数>`**：实际应用程序的各种参数，取决于具体应用程序。
  ```bash
  %command% -dx11
  ```

**组合所有元素的完整启动选项示例：**

```bash
__GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1 prime-run game-performance %command% -dx11
```

#### 环境变量

- DLSS 和 Nvidia 特性
  - `PROTON_DLSS_UPGRADE=1`：自动将 DLSS 升级到最新版本。
    - `PROTON_DLSS_INDICATOR=1`：在游戏中显示 DLSS 状态指示器。
    - `PROTON_NVIDIA_LIBS=1`：启用 Nvidia 库（PhysX、CUDA）——DLSS/光线追踪不需要此选项。
- 高级 Nvidia 控制
  - `PROTON_NVIDIA_NVCUDA=1`：仅启用 CUDA 支持。
  - `PROTON_NVIDIA_NVENC=1`：仅启用 NVENC 编码。
  - `PROTON_NVIDIA_NVML=1`：启用 NVML 监控。
  - `PROTON_NVIDIA_NVOPTIX=1`：启用 OptiX 光线追踪。
  - `PROTON_NVIDIA_LIBS_NO_32BIT=1`：限制库仅使用 64 位（修复 RTX 4000+ 性能问题）。
- AMD 和 Intel 超分辨率
  - `PROTON_FSR4_UPGRADE=1`：自动将 FSR 升级到最新版本。
    - `PROTON_FSR4_RDNA3_UPGRADE=1`：使用 RDNA3 优化的 FSR4 DLL。
    - `PROTON_XESS_UPGRADE=1`：自动将 XeSS 升级到最新版本。

### 在 Lutris 和 Heroic 中配置 Proton-CachyOS

确保系统中已安装 CachyOS 的 umu-launcher。使用以下命令安装：

```sh
sudo pacman -S cachyos/umu-launcher
```

1. 在 Lutris 主界面，点击 Wine 旁边的齿轮图标。
2. 进入 **Runner Options** 标签页，确认设置如下：
   - **Wine 版本** = `proton-cachyos`
   - **使用系统 winetricks** = *禁用*
   - **图形**
   - **启用 DXVK** = `启用`
     - 注意：使用 `umu-launcher` 时，用户自定义版本的 **DXVK**、**VKD3D** 和 **DXVK-NVAPI** 不会生效。
3. 进入 **System Options** 标签页。
   - **Lutris**
   - **禁用 Lutris Runtime** = `启用`
     - **优先使用系统库** = `启用`
4. 向下滚动到 **Game execution** 部分，找到 **Environment variables** 表格。
5. 添加以下环境变量：
   - **键**：`UMU_RUNTIME_UPDATE` *可选*
     - **值**：`0`
       - 这将跳过 proton-cachyos 的 Steam Linux Runtime 更新。请勿将此选项用于使用 Steam Linux Runtime 的任何 Proton，如 proton-cachyos-slr、-GE 或 -EM。
   - **键**：`PROTON_VERB` *可选*
     - **值**：`waitforexitandrun`
       - 这允许 protonfixes 与相应的 GAMEID 配合工作。
6. 点击 **Save** 保存更改。

### 反作弊支持

### 如何安装 proton-cachyos-slr

```sh
sudo pacman -S proton-cachyos-slr
```

手动安装（高级）：
1. 从[这里](https://github.com/CachyOS/proton-cachyos/releases)下载最新版本（向下滚动到 **Assets**）。
2. 解压文件并将文件夹移动到 `~/.steam/steam/compatibilitytools.d/`
3. 如果 Steam 正在运行，请重启 Steam。

## Wine-CachyOS

这是 `proton-cachyos` 核心的相同 `wine`，但作为独立软件包。可用于 Lutris、Heroic、Bottles 等。

- **包含 Proton-CachyOS 的所有 Wine 修改**
- **为游戏添加了早期的热修复/变通方案**

**附加配置选项**

- `WINE_WMCLASS="<名称>"`：设置所有 Wine 窗口的 `WM_CLASS`，允许窗口管理器通过规则控制 Wine 窗口。
- `WINEUSERSANDBOX=1`：禁用从 Wine 用户文件夹（如 Documents 和 Pictures）到用户 `HOME` 目录中相应文件夹的符号链接创建。
- `WINE_NO_WM_DECORATION=1`：禁用窗口装饰。这可以修复**无边框全屏**和鼠标穿透窗口的问题。
- `WINE_PREFER_SDL_INPUT=1`：解决手柄检测问题的变通方案。

### 如何使用 wine-cachyos-opt

通常，运行 `/opt/wine-cachyos/bin/wine` 而不是仅仅 `wine` 就足以让应用程序使用 `wine-cachyos-opt`。

如果需要更严格的配置，可以这样：

```shell
export PATH="/opt/wine-cachyos/bin/:$PATH"
export WINEDLLPATH="/opt/wine-cachyos/lib/wine:/opt/wine-cachyos/lib32/wine:$WINEDLLPATH"
export LD_LIBRARY_PATH="/opt/wine-cachyos/lib/:/opt/wine-cachyos/lib32/:$LD_LIBRARY_PATH"
```

如果想将 `winetricks` 与 `wine-cachyos-opt` 一起使用，可以这样调用：

```shell
WINE=/opt/wine-cachyos/bin/wine WINEPREFIX=<你的前缀> winetricks <动词>
```

## Steam 常见问题与技巧

### 应该在 Steam 中使用哪个 Proton 版本？

- `Proton 10.0` 是 Valve 的稳定版本。如果你想玩的游戏已知与它配合良好，请使用此版本。
- `Proton Experimental` 是 Valve 的前沿版本。如果你想玩的游戏相对较新、与当前 Proton 稳定版配合不佳，或者人们在 **[ProtonDB](https://www.protondb.com/)** 上推荐使用，请使用此版本。
- `proton-cachyos-slr` 是由 CachyOS 维护者构建和维护的版本。由于其各种 QoL 功能、修复和优化，强烈建议使用。对于使用反作弊的游戏（如 **BattlEye** 或 **Easy Anti-Cheat**）或自定义启动器，优先使用 `proton-cachyos-slr`。
- `proton-cachyos` 与 `proton-cachyos-slr` 是同一版本，但不依赖于 Steam Linux Runtime 构建。仅在你了解此差异意义的情况下使用，如果出现问题请回退到 `proton-cachyos-slr`。
- `Proton-GE` 是 [GloriousEggroll](https://github.com/GloriousEggroll/proton-ge-custom) 制作的自定义构建。它包含各种修复，在某些情况下可能会有用。
- `Proton 9.0.4 或更低版本` 是 Valve 的稳定版本。如果游戏仅适用于早期 Proton 版本，请使用这些版本。

### 修复 Steam 游戏录制功能导致的卡顿

将以下启动选项添加到游戏中：

```sh
LD_PRELOAD="" %command%
```

### 捕获和分享 Proton 日志

启用游戏 Proton 日志记录：

1. 在 Steam 中右键点击游戏，选择 **Properties**。
2. 在 **Launch Options** 下，设置 `PROTON_LOG` 环境变量：
  ```sh
  PROTON_LOG=1 %command%
  ```
  这会在你的主目录中创建一个名为 `steam-<AppID>.log` 的日志文件（例如，Counter Strike 2 使用 AppID **730**，所以文件名会是 `steam-730.log`）。

自定义日志目录：

要设置自定义日志目录，请使用 `PROTON_LOG_DIR`：

```bash
PROTON_LOG=1 PROTON_LOG_DIR=/home/cachyos/steam-logs %command%
```

### 使用 Proton-CachyOS、-GE 和 -EM 预缓存着色器

#### 在 Steam 中禁用此功能

在 Steam 中，点击 `Steam` -> `Settings`，进入 `Downloads`，取消勾选以下设置：

- **允许后台处理 Vulkan 着色器**
- **启用着色器预缓存**

### 重用 Windows NTFS 游戏分区

## Lutris

Lutris 是 CachyOS 上的游戏启动器。使用 Lutris，你可以轻松管理游戏运行器，包括 Wine、Proton 和模拟器。

- 只需点击 **Play** 按钮即可通过 Lutris 启动游戏。
- 点击左上角的 **+** 添加任何你想要的的游戏。
- 在左侧面板的 Sources 中设置商店，连接你的账户。它将安装该商店，然后你就可以像在 Windows 上一样在商店内运行游戏了。
- 还有更多功能！

*Lutris 支持的游戏商店：*

- [EA App](https://lutris.net/games/ea-app/)
- [Epic Games Store](https://lutris.net/games/epic-games-store/)
- [GOG Galaxy](https://lutris.net/games/gog-galaxy/)
- [Steam](https://lutris.net/games/steam/)
- [Ubisoft Connect](https://lutris.net/games/ubisoft-connect/)

### 如何在 Lutris 中正确设置多个启动选项和环境变量

- 启动选项（如 `-dx11` 或 `-fullscreen`）应使用空格分隔符添加到 **Game options** 标签下的 **Arguments** 字段中。
- 命令包装器（如 `mangohud --dlsym` 或 `game-performance`）应使用空格分隔符添加到 **System options** 标签下的 **Command prefix** 字段中。
- 环境变量（如 `PROTON_ENABLE_HDR=1`）应使用 `+` 按钮添加到 **System options** 标签下的 **Environment variables** 表格中。

## 性能与杂项技巧

### 不要同时使用 gamemode 和 ananicy-cpp

由于 `gamemode` 和 `ananicy-cpp` 同时尝试修改进程优先级，这可能导致冲突和意外行为。建议使用 gamemode 而不启用 ananicy-cpp。

停止 ananicy-cpp，执行以下命令：

```sh
systemctl stop ananicy-cpp
```

### 按需切换电源配置文件

CachyOS 包含一个包装脚本 [game-performance](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/bin/game-performance)，它使用 `power-profiles-daemon` 临时将电源配置文件切换到 `performance`。该配置文件会提升系统电源级别并将 CPU 调度器设置为 `performance`，同时还会将任何活动的 scx 调度器切换到其游戏配置文件（如果可用）。

当用于启动游戏时，系统保持在 **performance 模式**，直到游戏退出，此时会恢复之前的配置文件。

[Feral's GameMode](https://github.com/FeralInteractive/gamemode) 提供类似的功能。

### 如何将 game-performance 添加到 Steam、Lutris 和 Heroic Games Launcher

1. 打开你的 `Steam Library`。
2. 右键点击游戏标题，选择 `Properties`。
3. 在 `General` 标签中你会找到 `Launch Options` 部分。
4. 添加以下启动选项：
  ```sh
  game-performance %command%
  ```

### 增加最大着色器缓存大小

游戏着色器在游戏过程中会自动编译，这可能导致首次遇到时加载时间长和卡顿。这些着色器存储在系统中，以便在需要时重复使用。

然而，着色器缓存文件大小存在最大限制，当超过默认大小时，旧着色器会被遗忘。由于大型游戏的着色器可能超过 1GB，这可能导致每次启动都要重新编译着色器。

为避免长时间加载和卡顿，我们可以增加全局着色器缓存大小：

1. 打开终端。
2. 如果不存在，在配置文件夹中创建 `environment.d` 目录：
  ```sh
  mkdir -p ~/.config/environment.d
  ```
3. 创建一个新的配置文件：
  ```sh
  touch ~/.config/environment.d/gaming.conf
  ```
4. 用 **Micro**（文本编辑器）打开文件：
  ```sh
  micro ~/.config/environment.d/gaming.conf
  ```
  然后根据你的 GPU 厂商粘贴以下内容：

  AMD
  ```sh
  # 将 AMD 着色器缓存大小增加到 12GB
  MESA_SHADER_CACHE_MAX_SIZE=12G
  ```

  NVIDIA
  ```sh
  # 将 Nvidia 着色器缓存大小增加到 12GB
  __GL_SHADER_DISK_CACHE_SIZE=12000000000
  ```
5. 按 `CTRL+S` 保存文件，`CTRL+Q` 退出 Micro。重启系统。

重启后，最大着色器缓存大小应该会永久增加。感谢 [psygreg 的着色器增强器](https://github.com/psygreg/shader-booster/) 对本指南的帮助。

### 强制使用最新 DLSS 预设

#### 如何将 dlss-swapper 添加到 Steam、Lutris 和 Heroic Games Launcher

1. 打开你的 `Steam Library`。
2. 右键点击游戏标题，选择 `Properties`。
3. 在 `General` 标签中你会找到 `Launch Options` 部分。
4. 添加以下启动选项：
  ```sh
  dlss-swapper %command%
  ```

手动 DLL 替换方法

如果 `dlss-swapper` 不工作或出现问题，请尝试通过用最新版本替换 `nvngx_dlss.dll` 并使用 `dlss-swapper-dll` 包装脚本来手动更新游戏的 DLSS 实现。

### 光线追踪支持

Arch Wiki 已经提供了在各种硬件平台上启用[光线追踪](https://wiki.archlinux.org/title/Hardware_raytracing)的详细说明。

- [Nvidia 光线追踪](https://wiki.archlinux.org/title/Hardware_raytracing#NVIDIA)
- [AMD 光线追踪](https://wiki.archlinux.org/title/Hardware_raytracing#AMD)
- [Intel 光线追踪](https://wiki.archlinux.org/title/Hardware_raytracing#Intel)

### Nvidia 在 DirectX12 游戏中的性能下降

一些用户报告说问题与 Nvidia 的 Linux 驱动程序处理 GPU 调度的方式有关——与 Windows 不同，Windows 会强制执行正确的调度。Nvidia 尚未就此问题发表官方声明。目前没有已知的此问题解决方案。Nvidia 据称正在修复中，但尚不清楚何时发布。

**这与 CachyOS 无关。**

在某些游戏中，性能下降不如其他游戏明显。请查看此[基准对比视频](https://www.youtube.com/watch?v=SU2mFqCOh5A)作为参考。

关注 [Nvidia 线程](https://forums.developer.nvidia.com/t/directx12-performance-is-terrible-on-linux/303207/488)了解更多关于此问题的信息。
