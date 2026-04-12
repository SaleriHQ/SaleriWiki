---
title: "RWH 第18章-单子转换器"
source: "Clippings/RWH-Chapters-zh/第18章-单子转换器.md"
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
  - "[[wiki/concepts/类型类]]"
---

# RWH 第18章-单子转换器

## 本章概述

本章介绍 Monad Transformer (mtl 库)，包括 StateT、ReaderT、WriterT 等转换器的使用和 lifting 操作。

## 关键概念

- **Monad Transformer**: 叠加 Monad 能力
- **StateT**: 状态+其他 Monad 组合
- **ReaderT**: 配置+其他 Monad 组合
- **WriterT**: 日志+其他 Monad 组合
- **mtl 库**: 标准变换器集合
- **lifting**: lift :: m a -> t m a
- **run***: unStateT、runReaderT、runWriterT

## 核心代码示例

```haskell
import Control.Monad.State
import Control.Monad.Reader
import Control.Monad.Writer

-- StateT
type StateIO a = StateT Int IO a

evalStateT :: StateT s m a -> s -> m a
execStateT :: StateT s m a -> s -> m s

-- ReaderT
type ConfigIO a = ReaderT Config IO a

runReaderT :: ReaderT r m a -> r -> m a

-- 组合变换器
type MyMonad a = ReaderT Config (StateT Int (WriterT Log IO)) a

-- lifting
lift :: (MonadTrans t, Monad m) => m a -> t m a
liftIO :: MonadIO m => IO a -> m a

-- 运行组合
runMyMonad :: Config -> Int -> MyMonad a -> IO ((a, Int), Log)
runMyMonad cfg st m =
  runWriterT (runStateT (runReaderT m cfg) st)
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/单子]]
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/Monad变换器]]
- [[wiki/concepts/类型类]]
