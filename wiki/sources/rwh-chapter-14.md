---
title: "RWH 第14章-单子"
source: "Clippings/RWH-Chapters-zh/第14章-单子.md"
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

# RWH 第14章-单子

## 本章概述

本章深入介绍 Monad 概念，通过 Maybe、Either、IO Monad 的实现展示 Monad 定律和 do 语法的本质。

## 关键概念

- **Monad 概念**: bind (>>=)、return、顺序组合
- **Maybe Monad**: Nothing 短路、Just 值传播
- **Either Monad**: Left 错误、Right 成功
- **IO Monad**: 副作用操作、状态封装
- **do 语法**: 隐式 bind、<- 绑定结果
- **Monad 定律**: 左单位元、右单位元、结合律

## 核心代码示例

```haskell
-- Monad 类型类
class Monad m where
  (>>=)  :: m a -> (a -> m b) -> m b
  return :: a -> m a
  (>>)   :: m a -> m b -> m b

-- Maybe Monad
instance Monad Maybe where
  return = Just
  Nothing >>= _ = Nothing
  Just x >>= f = f x

-- Either Monad
instance Monad (Either e) where
  return = Right
  Left e >>= _ = Left e
  Right x >>= f = f x

-- Monad 定律验证
-- 左单位元: return a >>= f  ===  f a
-- 右单位元: m >>= return     ===  m
-- 结合律: (m >>= f) >>= g    ===  m >>= (\x -> f x >>= g)

-- do 语法 desugar
do { x <- m; f x }  ===  m >>= \x -> f x
do { m; e }         ===  m >> e
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/单子]]
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/Maybe]]
- [[wiki/concepts/Either]]
- [[wiki/concepts/Applicative]]
- [[wiki/concepts/类型类]]
