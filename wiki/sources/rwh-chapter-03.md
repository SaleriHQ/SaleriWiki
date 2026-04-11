---
title: "RWH 第03章-定义类型、简化函数"
source: "Clippings/RWH-Chapters-zh/第03章-定义类型、简化函数.md"
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
  - "[[wiki/concepts/代数数据类型]]"
  - "[[wiki/concepts/模式匹配]]"
---

# RWH 第03章-定义类型、简化函数

## 本章概述

本章介绍如何定义自定义数据类型，包括 data 关键字、模式匹配、记录语法、Guards 条件语法，以及 where 和 let 局部声明的使用。

## 关键概念

- **data 关键字**: 定义自定义数据类型
- **代数数据类型**: Sum types、Product types、递归类型
- **模式匹配**: 按结构匹配、Wildcard、@ 模式
- **记录语法**: { field = value }、自动访问函数
- **Guards**: | 条件语法、otherwise、分支顺序
- **where 子句**: 局部函数定义、共享计算
- **let 表达式**: let...in 结构、词法绑定

## 核心代码示例

```haskell
-- 代数数据类型
data Bool = False | True
data Maybe a = Nothing | Just a
data Tree a = Leaf a | Node (Tree a) (Tree a)

-- 模式匹配
headMessage :: [Char] -> Char
headMessage [] = '0'
headMessage (x:_) = x

-- 记录语法
data Person = Person { name :: String, age :: Int }

-- Guards
classify :: Int -> String
classify n
  | n < 0     = "negative"
  | n == 0    = "zero"
  | otherwise = "positive"

-- where 子句
squareSum :: Int -> Int -> Int
squareSum x y = sx + sy
  where sx = x * x
        sy = y * y
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/代数数据类型]]
- [[wiki/concepts/模式匹配]]
- [[wiki/concepts/类型类]]
