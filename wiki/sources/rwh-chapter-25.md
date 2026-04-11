---
title: "RWH 第25章-性能分析与优化"
source: "Clippings/RWH-Chapters-zh/第25章-性能分析与优化.md"
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
  - "[[wiki/concepts/高阶函数]]"
---

# RWH 第25章-性能分析与优化

## 本章概述

本章介绍 Haskell 性能分析和优化技术，包括 Profiling工具、空间分析、GC 调优、严格求值和 INLINE/SPECIALIZE  pragmas。

## 关键概念

- **Profiling**: +RTS -p/-h/-xc、成本中心
- **空间分析**: 堆大小、保留、 thunk 积聚
- **GC 调优**: +RTS -G1/-A/-H
- **严格求值**: seq、$!、BangPatterns
- **INLINE**: 内联展开、减少函数调用开销
- **SPECIALIZE**: 具体类型实例化、多态优化
- **空间泄漏**: thunk 避免、seq 引入

## 核心代码示例

```haskell
-- 编译时启用 profiling
-- ghc -O2 -rtsopts -prof -fprof-auto MyProgram.hs

-- 运行 profiling
-- ./MyProgram +RTS -p -hc

-- 严格求值
foldl' :: (a -> b -> a) -> a -> [b] -> a
foldl' f acc [] = acc
foldl' f acc (x:xs) = let acc' = f acc x in acc' `seq` foldl' f acc' xs

-- $! 运算符
f $! x = x `seq` f x

-- BangPatterns
{-# LANGUAGE BangPatterns #-}
strictMap :: (a -> b) -> [a] -> [b]
strictMap f [] = []
strictMap f (!x:xs) = f x : strictMap f xs

-- INLINE
{-# INLINE myFunc #-}
myFunc :: Int -> Int
myFunc x = x + 1

-- SPECIALIZE
{-# SPECIALIZE myFunc :: Int -> Int #-}
{-# SPECIALIZE myFunc :: Double -> Double #-}

-- RTS 选项
-- +RTS -s -G1 -A10m -H50m -RTS
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/类型系统]]
- [[wiki/concepts/高阶函数]]
- [[wiki/concepts/纯函数]]
