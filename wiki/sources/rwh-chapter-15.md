---
title: "RWH 第15章-使用单子编程"
source: "Clippings/RWH-Chapters-zh/第15章-使用单子编程.md"
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
  - "[[wiki/concepts/单子]]"
  - "[[wiki/concepts/IO Monad]]"
---

# RWH 第15章-使用单子编程

## 本章概述

本章介绍常用 Monad 实例：Writer Monad（日志）、Reader Monad（配置）、State Monad（可变状态）、MonadPlus 和列表 Monad。

## 关键概念

- **Writer Monad**: 日志累积、Monoid 组合
- **Reader Monad**: 共享配置、只读环境
- **State Monad**: 可变状态、状态传递
- **MonadPlus**: mzero、mplus、失败处理
- **列表 Monad**: 非确定性计算、backtracking
- **Monad Transformer**: MaybeT、EitherT

## 核心代码示例

```haskell
-- Writer Monad
import Control.Monad.Writer

type Log = [String]
log :: String -> Writer Log ()
log s = tell [s]

execLog :: Writer Log a -> (a, Log)
execLog = execWriter . fmap (\() -> id)

-- Reader Monad
import Control.Monad.Reader

ask :: Reader e e
asks :: (e -> a) -> Reader e a

local :: (e -> e) -> Reader e a -> Reader e a

-- State Monad
import Control.Monad.State

type Stack = [Int]
pop :: State Stack Int
pop = state $ (x:xs) -> (x, xs)

push :: Int -> State Stack ()
push x = state $ xs -> ((), x:xs)

-- 列表 Monad (非确定性)
choices :: [Int]
choices = do
  x <- [1,2,3]
  y <- [4,5]
  return (x,y)
-- 结果: [(1,4),(1,5),(2,4),(2,5),(3,4),(3,5)]
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/单子]]
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/高阶函数]]
