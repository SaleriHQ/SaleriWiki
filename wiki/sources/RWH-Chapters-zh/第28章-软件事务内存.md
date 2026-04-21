---
title: "RWH 第28章-软件事务内存"
source: "Clippings/RWH-Chapters-zh/第28章-软件事务内存.md"
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
  - "[[wiki/concepts/并发编程]]"
---

# RWH 第28章-软件事务内存

## 本章概述

本章深入介绍 Software Transactional Memory (STM)，包括 TVar、atomically、retry、orElse 和并发控制模式。

## 关键概念

- **STM**: Software Transactional Memory
- **TVar**: 事务性变量、原子读写
- **atomically**: 执行事务块
- **retry**: 事务重试、阻塞等待
- **orElse**: 备选事务、回退机制
- **always**: 不变量检查
- **并发控制**: 死锁避免、乐观锁

## 核心代码示例

```haskell
import Control.Concurrent.STM

-- TVar 操作
newTVar :: a -> STM (TVar a)
readTVar :: TVar a -> STM a
writeTVar :: TVar a -> a -> STM ()

-- 基本事务
atomically :: STM a -> IO a

withdraw :: TVar Int -> Int -> STM ()
withdraw account amount = do
  balance <- readTVar account
  if balance >= amount
    then writeTVar account (balance - amount)
    else retry

-- orElse 组合
transfer :: TVar Int -> TVar Int -> Int -> STM ()
transfer from to amount = do
  withdraw from amount `orElse` deposit to amount

-- deposit (不检查余额)
deposit :: TVar Int -> Int -> STM ()
deposit account amount = do
  balance <- readTVar account
  writeTVar account (balance + amount)

-- always 检查不变量
check :: Bool -> STM ()
check True = return ()
check False = retry

-- 银行转账 (完整示例)
transfer :: TVar Int -> TVar Int -> Int -> STM ()
transfer from to amount = atomically $ do
  balFrom <- readTVar from
  if balFrom >= amount
    then do
      writeTVar from (balFrom - amount)
      balTo <- readTVar to
      writeTVar to (balTo + amount)
    else retry
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/单子]]
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/类型系统]]
