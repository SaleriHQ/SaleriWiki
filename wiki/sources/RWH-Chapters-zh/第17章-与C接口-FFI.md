---
title: "RWH 第17章-与C接口-FFI"
source: "Clippings/RWH-Chapters-zh/第17章-与C接口-FFI.md"
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
  - "[[wiki/concepts/类型系统]]"
  - "[[wiki/concepts/IO Monad]]"
---

# RWH 第17章-与C接口-FFI

## 本章概述

本章介绍 Haskell 的 Foreign Function Interface (FFI)，包括 C 绑定声明、hsc2hs 和 c2hs 工具使用、类型映射和调用 C 库。

## 关键概念

- **FFI**: Foreign Function Interface、外部语言调用
- **C 绑定**: foreign import、dynamic import
- **hsc2hs**: Haskell 到 C 预处理器
- **c2hs**: C 到 Haskell 接口生成器
- **类型映射**: CInt、CUInt、CString、Ptr
- **marshalling**: Haskell/C 数据转换
- **安全调用**: unsafe、safe 调用约定

## 核心代码示例

```haskell
-- 基本 FFI 导入
{-# LANGUAGE ForeignFunctionInterface #-}

import Foreign.C.String (CString, peekCString)
import Foreign.C.Types (CInt, CDouble)
import Foreign.Ptr (Ptr)

-- 导入 C 函数
foreign import ccall "math.h sqrt"
  c_sqrt :: CDouble -> CDouble

-- 调用 C 函数
haskell_sqrt :: Double -> Double
haskell_sqrt = realToFrac . c_sqrt . realToFrac

-- marshalling
withCString :: String -> (CString -> IO a) -> IO a
peekCString :: CString -> IO String

-- 回调 C 函数
foreign import ccall "wrapper"
  createFun :: (CInt -> IO CInt) -> IO (FunPtr (CInt -> IO CInt))
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/类型系统]]
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/代数数据类型]]
