---
title: "RWH 第20章-系统编程"
source: "Clippings/RWH-Chapters-zh/第20章-系统编程.md"
author: "Bryan O'Sullivan, Don Stewart, John Goerzen"
translator: "Claude"
created: 2026-04-11
updated: 2026-04-11
type: source
tags:
  - source
  - haskell
  - book
  - rwh
related:
  - "[[wiki/concepts/IO Monad]]"
  - "[[wiki/concepts/单子]]"
---

# RWH 第20章-系统编程

## 本章概述

本章介绍 Haskell 系统编程，包括进程控制 (System.Process)、目录操作 (System.Directory)、时间处理 (Data.Time) 和信号处理 (System.Posix.Signals)。

## 关键概念

- **进程控制**: createProcess、waitForProcess
- **目录操作**: createDirectory、removeDirectory
- **时间处理**: UTCTime、NominalDiffTime、formatTime
- **信号处理**: signal, killProcess、keyboard 事件
- **环境信息**: getEnv、setEnv、unsetEnv
- **临时文件**: openTempFile、getTemporaryDirectory

## 核心代码示例

```haskell
import System.Process (createProcess, shell, waitForProcess)
import System.Directory (createDirectory, doesFileExist, getPermissions)
import Data.Time (UTCTime, getCurrentTime, formatTime)
import System.Locale (defaultTimeLocale)

-- 进程控制
runCommand :: String -> IO ()
runCommand cmd = do
  (_, _, _, ph) <- createProcess (shell cmd)
  waitForProcess ph >>= print

-- 目录操作
createDirectoryIfMissing :: Bool -> FilePath -> IO ()
removePathForcibly :: FilePath -> IO ()

-- 时间处理
formatTime' :: UTCTime -> String
formatTime' = formatTime defaultTimeLocale "%Y-%m-%d %H:%M:%S"

getCurrentTime :: IO UTCTime
diffUTCTime :: UTCTime -> UTCTime -> NominalDiffTime

-- 信号处理
import System.Posix.Signals

installHandler :: Signal -> Handler -> Maybe Signal -> IO Handler
sigINT :: Signal
sigTERM :: Signal
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/单子]]
- [[wiki/concepts/类型系统]]
