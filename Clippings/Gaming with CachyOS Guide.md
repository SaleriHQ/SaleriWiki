---
title: "Gaming with CachyOS Guide"
source: "https://wiki.cachyos.org/configuration/gaming/"
author:
published: 2026-03-26
created: 2026-04-12
description: "It covers essential package installation, Steam gaming with Proton, various Proton version options, Lutris as a central hub for all games, and script installers for popular games."
tags:
  - "clippings"
---
Welcome to the guide for Gaming on CachyOS. This will guide you through the essential aspects on how to set everything up for gaming.

First of all.

*Remember. getting a double digit improvement in FPS is not always possible or possible at all. Sometimes, optimizations can lead to minor improvements or even none at all, depending on the game and hardware configuration.*

*You can’t expect software optimizations acting like a free hardware upgrade.*

![](https://wiki.cachyos.org/_astro/gaming-meme.Dc0lFTAL.jpeg)

## Prerequisites

### Essential Packages

To make it easier to set CachyOS up for gaming, all the necessary gaming packages are grouped into one meta-package that includes all the necessary dependencies and libraries for gaming in Linux, with and a separate meta-package for tools and launchers/stores.

*If you find that any packages are missing, feel free to let the CachyOS team know.*

Follow the steps below to start with the gaming setup.

- [CachyOS Hello](#tab-panel-122)
- [Meta Package](#tab-panel-123)
- [Tools & Stores](#tab-panel-124)

- Open CachyOS Hello. Go to **Apps/Tweaks** and click on `Install Gaming packages`. ![](https://wiki.cachyos.org/_astro/cachyos_hello-gaming.BFhnUF0h.png)

*CachyOS Hello installs both `cachyos-gaming-meta` and `cachyos-gaming-applications`.*

## Proton-CachyOS

Proton-CachyOS is based on Proton’s `bleeding-edge` branch and applies a number of modifications on top of it.

- **Wine-staging patches**
- **Wine Fullscreen FSR**
- **Includes video and audio codecs for game cutscenes**
- **Support for umu-launcher including UMU-Protonfixes**
- **Adds early hotfixes/workarounds for games**

### How to Properly Set Multiple Launch Options

The launch options in Steam are constructed using the following pattern.

```bash
<env variables> <wrappers> %command% <application arguments>
```

- **`<env variables>`**: These are options in the form `VARIABLE=value`
	```bash
	PROTON_DXVK_D3D8=1
	# Or
	DXVK_HUD="fps,memory,version,api"
	```
- **`<wrappers>`**: These are applications and scripts that modify how the real application is run. Arguments to the wrapper usually go after the wrapper’s executable.
	```bash
	mangohud --dlsym
	# Or
	gamescope -W 1680 -H 1050 -w 1280 -h 720 -S fit -F fsr --mangoapp --
	```
- **`%command%`**: This is the real application. This should be specified exactly as is and Steam will replace it with the proper command when the application is run.
- **`<application arguments>`**: These are various arguments to the real application, and they depend on the application.
	```bash
	%command% -dx11
	```

**Example of a complete launch option combining all the elements:**

```bash
__GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1 prime-run game-performance %command% -dx11
```

#### Environment Variables

- [Graphics & Upscaling](#tab-panel-106)
- [Display & HDR](#tab-panel-107)
- [Performance & Caching](#tab-panel-108)
- [Input & Compatibility](#tab-panel-109)

- DLSS & Nvidia Features
	- `PROTON_DLSS_UPGRADE=1`: Automatically upgrade DLSS to the latest version.
		- `PROTON_DLSS_INDICATOR=1`: Show DLSS status indicator in-game.
		- `PROTON_NVIDIA_LIBS=1`: Enable Nvidia libraries (PhysX, CUDA) - not needed for DLSS/ray tracing.
Advanced Nvidia Controls
- `PROTON_NVIDIA_NVCUDA=1`: Enable only CUDA support.
- `PROTON_NVIDIA_NVENC=1`: Enable only NVENC encoding.
- `PROTON_NVIDIA_NVML=1`: Enable NVML monitoring.
- `PROTON_NVIDIA_NVOPTIX=1`: Enable OptiX ray tracing.
- `PROTON_NVIDIA_LIBS_NO_32BIT=1`: Restrict libraries to only 64-bit (fixes RTX 4000+ performance issues).
- AMD & Intel Upscaling
	- `PROTON_FSR4_UPGRADE=1`: Automatically upgrade FSR to the latest version.
		- `PROTON_FSR4_RDNA3_UPGRADE=1`: Use a RDNA3-optimized FSR4 DLL.
		- `PROTON_XESS_UPGRADE=1`: Automatically upgrade XeSS to the latest version.

### Setting Up Proton-CachyOS with Lutris and Heroic

Make sure you have umu-launcher from CachyOS installed in your system. Install it with the following command.

```sh
sudo pacman -S cachyos/umu-launcher
```

- [Lutris Global](#tab-panel-110)
- [Lutris Per Game](#tab-panel-111)
- [Heroic Games Launcher](#tab-panel-112)

1. In the main Lutris screen, click the cogwheel icon next to Wine.
2. Go to the **Runner Options** tab and confirm that your settings match the following:
	- **Wine version** = `proton-cachyos`
		- **Use System winetricks** = *Disabled*
		- **Graphics**
		- **Enable DXVK** = `Enabled`
			- Note: User-defined versions of **DXVK**, **VKD3D**, and **DXVK-NVAPI** are not applied when using `umu-launcher`.
3. Navigate to the **System Options** tab.
	- **Lutris**
		- **Disable Lutris Runtime** = `Enabled`
				- **Prefer system libraries** = `Enabled`
4. Continue scrolling down to the **Game execution** section and locate the **Environment variables** table.
5. Add the following environment variables:
	- **Key**: `UMU_RUNTIME_UPDATE` *optional*
		- **Value**: `0`
				- *This will skip Steam Linux Runtime updates for proton-cachyos. Do not use this with any Proton that utilizes the Steam Linux Runtime, such as proton-cachyos-slr, -GE, or -EM.*
		- **Key**: `PROTON_VERB` *optional*
		- **Value**: `waitforexitandrun`
				- *This allows protonfixes to work with a corresponding GAMEID.*
6. Click **Save** to apply the changes.

### Anti-Cheat Support

### How To Install proton-cachyos-slr

- [pacman](#tab-panel-125)
- [protonup](#tab-panel-126)

```sh
sudo pacman -S proton-cachyos-slr
```

Manual Installation (Advanced)
1. Download the latest version [here](https://github.com/CachyOS/proton-cachyos/releases) (scroll down to **Assets**).
2. Decompress the file and move the folder to `~/.steam/steam/compatibilitytools.d/`
3. Restart Steam if you had it open.

## Wine-CachyOS

This is the same `wine` that is at the core of `proton-cachyos`, but as a standalone package. It can be used in Lutris, Heroic, Bottles, and others.

- **All the Wine modifications included with Proton-CachyOS**
- **Adds early hotfixes/workarounds for games**

**Additional configuration options**

- `WINE_WMCLASS="<name>"`: Set the `WM_CLASS` of all Wine windows, allowing the window manager to control the Wine windows through rules.
- `WINEUSERSANDBOX=1`: Disable the creation of symlinks from Wine user folders (such as Documents and Pictures) to the equivalent folders in the user’s `HOME` directory.
- `WINE_NO_WM_DECORATION=1`: Disable window decorations. It can fix issues with **borderless fullscreen** and the mouse clicking through the window.
- `WINE_PREFER_SDL_INPUT=1`: Workaround for controller detection issues

### How To Use wine-cachyos-opt

- [Standalone](#tab-panel-119)
- [Lutris](#tab-panel-120)
- [Heroic Games Launcher](#tab-panel-121)

Normally, running `/opt/wine-cachyos/bin/wine` instead of just `wine` should be enough for an application to run using `wine-cachyos-opt`.

If a more strict configuration is required, it could look like this:

```shell
export PATH="/opt/wine-cachyos/bin/:$PATH"
export WINEDLLPATH="/opt/wine-cachyos/lib/wine:/opt/wine-cachyos/lib32/wine:$WINEDLLPATH"
export LD_LIBRARY_PATH="/opt/wine-cachyos/lib/:/opt/wine-cachyos/lib32/:$LD_LIBRARY_PATH"
```

If you want to use `winetricks` with `wine-cachyos-opt`, you can invoke it like this:

```shell
WINE=/opt/wine-cachyos/bin/wine WINEPREFIX=<your prefix> winetricks <verb>
```

## Steam FAQ & Tips

### Which Proton Version Should Be Used in Steam?

- `Proton 10.0` is the stable release from `Valve`. Use this if the game you want to play is known to work well with it.
- `Proton Experimental` is the bleeding edge release from `Valve`. Use this if the game you want to play is relatively new, doesn’t work well with the current Proton stable release, or if people recommend it on **[ProtonDB](https://www.protondb.com/)**.
- `proton-cachyos-slr` is the one built and maintained by CachyOS maintainers. Using it is highly recommended due to its various QoL features, fixes, and optimizations. For games using anti-cheat, such as **BattlEye** or **Easy Anti-Cheat**, or custom launchers, `proton-cachyos-slr` is preferred.
- `proton-cachyos` is the same version as `proton-cachyos-slr` but built without depending on the Steam Linux Runtime. Use it only if you understand the significance of this difference, and fall back to `proton-cachyos-slr` if issues occur.
- `Proton-GE` is a custom build made by [GloriousEggroll](https://github.com/GloriousEggroll/proton-ge-custom). It includes various fixes, and can be useful to have in certain situations.
- `Proton 9.0.4 or lower` are the stable releases from `Valve`. Use this if the game you want to play only works with a previous Proton release.

### Fix Stuttering Caused by the Steam Game Recorder Feature

Add the following launch option to your game.

```sh
LD_PRELOAD="" %command%
```

### Capturing and Sharing Proton Logs

To enable Proton logging for a game:

1. Right-click your game in Steam and select **Properties**.
2. Under **Launch Options**, set the `PROTON_LOG` environment variable:
	```sh
	PROTON_LOG=1 %command%
	```
	This will create a log file in your home directory named `steam-<AppID>.log` (for example, Counter Strike 2 uses AppID **730**, so the file would be `steam-730.log`).
Custom Log Directory

To set a custom log directory, use `PROTON_LOG_DIR`:

```bash
PROTON_LOG=1 PROTON_LOG_DIR=/home/cachyos/steam-logs %command%
```

### Pre-caching Shaders with Proton-CachyOS, -GE, and -EM

#### To disable this feature in Steam

In Steam, click on `Steam` -> `Settings`, go to `Downloads`, and uncheck these settings:

- **Allow background processing of Vulkan shaders**
- **Enable Shader Pre-caching**

### Repurposing a Windows NTFS Game Partition

## Lutris

Lutris is a game launcher on CachyOS. With Lutris, you can easily manage your game runners, including Wine, Proton, and emulators.

- Launch games through Lutris simply by clicking the **Play** button.
- Add any game you want by clicking the **+** at the top-left corner.
- Set up a store in the Sources at the left panel and connecting your account. It will then proceed to install said store, and then you’ll be able to run games from within the store, just like you do on Windows.
- And more!

*Game stores supported in Lutris:*

- [EA App](https://lutris.net/games/ea-app/)
- [Epic Games Store](https://lutris.net/games/epic-games-store/)
- [GOG Galaxy](https://lutris.net/games/gog-galaxy/)
- [Steam](https://lutris.net/games/steam/)
- [Ubisoft Connect](https://lutris.net/games/ubisoft-connect/)

### How to Properly Set Multiple Launch Options and Environment Variables in Lutris

- Launch options such as `-dx11` or `-fullscreen` should be added in the **Arguments** field under the **Game options** tab using a space as a separator.
- Command wrappers, for example `mangohud --dlsym` or `game-performance`, should be added in the **Command prefix** field under the **System options** tab using a space as a separator.
- Environment variables such as `PROTON_ENABLE_HDR=1` should be added in the **Environment variables** table under the **System options** tab using the `+` button to add a new entry.

## Performance & Misc Tips

### Do Not Combine gamemode and ananicy-cpp

Due to `gamemode` and `ananicy-cpp` both trying to modify a process niceness at the same time, it can lead to conflicts and unexpected behavior. It’s recommended to use gamemode without ananicy-cpp.

To stop ananicy-cpp, execute the following command:

```sh
systemctl stop ananicy-cpp
```

### Power Profile Switching On-Demand

CachyOS includes a wrapper script [game-performance](https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/bin/game-performance) which uses `power-profiles-daemon` to temporarily switch the power profile to `performance`. The profile raises system power levels and sets the CPU governor to `performance`, and also switches any active scx scheduler to its gaming profile (if available).

When used to launch a game, the system remains in **performance mode** until the game exits, at which point the previous profile is restored.

[Feral’s GameMode](https://github.com/FeralInteractive/gamemode) offers similar functionality.

### How To Add game-performance to Steam, Lutris, and Heroic Games Launcher

- [Steam](#tab-panel-113)
- [Heroic Games Launcher](#tab-panel-114)
- [Lutris](#tab-panel-115)

1. Open your `Steam Library`.
2. Right-click the game’s title and select `Properties`.
3. On the `General` tab you’ll the find `Launch Options` section.
4. Add the following launch option:
	```sh
	game-performance %command%
	```

### Increase maximum shader cache size

Game shaders are compiled automatically while playing, which may cause long loading times and stuttering the first time you encounter them. These shaders are stored on your system to be reused when needed.

However, there is a maximum limit to the shader cache’s file size, causing old shaders to be forgotten when exceeding the default size. This can be an issue since large games can have shaders over 1GB in size, causing them to re-compile shaders every launch.

To avoid long loading times and stuttering, we can increase the global shader cache size:

1. Open a terminal.
2. Create a `environment.d` directory in your config folder if it doesn’t exist:
	```sh
	mkdir -p ~/.config/environment.d
	```
3. Create a new configuration file:
	```sh
	touch ~/.config/environment.d/gaming.conf
	```
4. Open the file with **Micro** (a text editor).
	```sh
	micro ~/.config/environment.d/gaming.conf
	```
	And paste the following depending on your GPU vendor: AMD
	```sh
	# Increase AMD's shader cache size to 12GB
	MESA_SHADER_CACHE_MAX_SIZE=12G
	```
	NVIDIA
	```sh
	# Increase Nvidia's shader cache size to 12GB
	__GL_SHADER_DISK_CACHE_SIZE=12000000000
	```
5. Save the file by pressing `CTRL+S` and `CTRL+Q` to exit Micro. Restart your system.

After restarting, the maximum shader cache size should be permanently increased. Thanks to [psygreg’s shader booster](https://github.com/psygreg/shader-booster/) for helping this guide.

### Forcing the Latest DLSS Preset

#### How to add dlss-swapper to Steam, Lutris, and Heroic Games Launcher

- [Steam](#tab-panel-116)
- [Heroic Games Launcher](#tab-panel-117)
- [Lutris](#tab-panel-118)

1. Open your `Steam Library`.
2. Right click the game’s title and select `Properties`.
3. On the `General` tab you’ll find `Launch Options` section.
4. Add the following Launch Option:
	```sh
	dlss-swapper %command%
	```

Manual DLL Replacement Method

If `dlss-swapper` is not working or causing issues, try updating game’s DLSS implementation manually by replacing `nvngx_dlss.dll` with an up-to-date version and using the `dlss-swapper-dll` wrapper script instead.

### Ray Tracing Support

The Arch Wiki has already provides comprehensive instructions on how to enable [ray tracing](https://wiki.archlinux.org/title/Hardware_raytracing) for various hardware platforms.

- [Ray tracing on Nvidia](https://wiki.archlinux.org/title/Hardware_raytracing#NVIDIA)
- [Ray tracing on AMD](https://wiki.archlinux.org/title/Hardware_raytracing#AMD)
- [Ray tracing on Intel](https://wiki.archlinux.org/title/Hardware_raytracing#Intel)

### Performance Drop on Nvidia in DirectX12 Games

Some users report that the issue is related to how Nvidia’s Linux drivers handle GPU scheduling—unlike on Windows, where proper scheduling is enforced. There’s been no official Nvidia statement on this matter yet. There is Currently no known workaround for this issue. Nvidia is supposedly working on a fix, but it’s not clear when it will be released.

**It has nothing to do with CachyOS.**

In some titles, the performance drop is less noticeable than in others. Check out this [benchmark comparison video](https://www.youtube.com/watch?v=SU2mFqCOh5A) for reference.

Follow the [Nvidia thread](https://forums.developer.nvidia.com/t/directx12-performance-is-terrible-on-linux/303207/488) to learn more about this issue.