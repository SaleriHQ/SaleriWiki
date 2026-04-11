---
title: "RWH 第08章-高效文件处理"
source: "Clippings/RWH-Chapters-zh/第08章-高效文件处理.md"
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
  - "[[wiki/concepts/类型系统]]"
---

# RWH 第08章-高效文件处理

## 本章概述

本章介绍 Haskell 中的高效文件处理技术，包括 ByteString、Text 类型、正则表达式处理、文件名匹配 (Glob) 和缓冲区管理。

## 关键概念

- **ByteString**: 高效字节处理、lazy vs strict
- **Text**: Unicode 文本处理、locale 感知
- **正则表达式**: Text.Regex、(=~)、模式匹配
- **Glob 模式**: 文件名匹配、**、?
- **缓冲区**: 块读取、流式处理
- **I/O 效率**: 避免字符串复制、减少 GC 压力

## 核心代码示例

```haskell
-- ByteString
import qualified Data.ByteString as B
import qualified Data.ByteString.Lazy as L

-- 高效读取
processFile :: FilePath -> IO ()
processFile path = B.readFile path >>= return . B.length

-- Text 处理
import qualified Data.Text as T
import qualified Data.Text.IO as TIO

countLines :: T.Text -> Int
countLines = length . T.lines

-- 正则表达式
import Text.Regex.Posix
getUrls :: String -> [String]
getUrls s = s =~ "https?://[a-zA-Z0-9._-]+"
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/类型系统]]
- [[wiki/concepts/高阶函数]]
