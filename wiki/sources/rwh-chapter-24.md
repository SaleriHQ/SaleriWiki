---
title: "RWH 第24章-并发与多核编程"
source: "Clippings/RWH-Chapters-zh/第24章-并发与多核编程.md"
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

# RWH 第24章-并发与多核编程

## 本章概述

本章深入介绍 Haskell 并发编程，包括 forkIO 线程创建、MVar 同步、STM (Software Transactional Memory) 和并行策略。

## 关键概念

- **并发**: 同时执行多个任务
- **forkIO**: 创建轻量级线程
- **MVar**: 同步变量、阻塞读写
- **STM**: Software Transactional Memory
- **TVar**: 事务性变量
- **并行策略**: Strategies、par、pseq
- **线程安全**: 原子操作、无数据竞争

## 核心代码示例

```haskell
import Control.Concurrent
import Control.Concurrent.MVar
import Control.Monad.STM

-- 创建线程
forkIO :: IO () -> IO ThreadId

-- MVar 同步
newMVar :: a -> IO (MVar a)
takeMVar :: MVar a -> IO a
putMVar :: MVar a -> a -> IO ()

-- 生产者-消费者
producer :: MVar Int -> IO ()
producer mv = do
  putMVar mv 42
  putMVar mv 99

consumer :: MVar Int -> IO ()
consumer mv = do
  x <- takeMVar mv
  print x

-- STM
atomically :: STM a -> IO a
retry :: STM a
orElse :: STM a -> STM a -> STM a

data TVar a = TVar a
newTVar :: a -> STM (TVar a)
readTVar :: TVar a -> STM a
writeTVar :: TVar a -> a -> STM ()

-- 并行策略
import Control.Parallel (par, pseq)
parMap :: Strategy a -> (a -> b) -> [a] -> [b]
using :: a -> Strategy a -> a
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/单子]]
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/类型系统]]
