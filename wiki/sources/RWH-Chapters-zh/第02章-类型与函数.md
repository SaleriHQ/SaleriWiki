---
title: "RWH 第02章-类型与函数"
source: "Clippings/RWH-Chapters-zh/第02章-类型与函数.md"
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
  - "[[wiki/concepts/类型推断]]"
---

# RWH 第02章-类型与函数

## 本章概述

本章深入介绍 Haskell 的类型系统，包括静态类型、类型推断、函数定义、列表和元组的使用。通过丰富的示例展示纯函数和递归编程的基础。

## 关键概念

- **静态类型**: 编译时检查类型、类型安全保证
- **类型推断**: 编译器自动推断类型、minNumOps = 3 + 4
- **函数应用**: 中缀函数、函数组合、优先级规则
- **列表**: 同构元素集合、[Int]、head/tail/length
- **元组**: 固定长度异构类型、(Bool, Char, Int)
- **纯函数**: 无副作用、引用透明性
- **递归**: 递归定义、基线条件、归纳推理
- **惰性求值**: 按需计算、无穷数据结构

## 核心代码示例

```haskell
-- 类型签名
ghci> :t head
head :: [a] -> a

-- 函数定义
first :: (a, b) -> a
first (x, _) = x

-- 递归求阶乘
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- 列表递归
sumList :: [Integer] -> Integer
sumList [] = 0
sumList (x:xs) = x + sumList xs
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/类型系统]]
- [[wiki/concepts/类型推断]]
- [[wiki/concepts/递归]]
- [[wiki/concepts/纯函数]]
