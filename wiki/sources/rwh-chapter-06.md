---
title: "RWH 第06章-使用类型类"
source: "Clippings/RWH-Chapters-zh/第06章-使用类型类.md"
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
  - "[[wiki/concepts/类型类]]"
  - "[[wiki/concepts/类型系统]]"
---

# RWH 第06章-使用类型类

## 本章概述

本章深入讲解 Haskell 类型类系统，包括 Eq、Ord、Num、Show 等标准类型类，实例声明语法，newtype 声明和类型同义词。

## 关键概念

- **类型类**: 类似接口的共享行为抽象
- **Eq 类型类**: (==)、(/=) 相等性比较
- **Ord 类型类**: (<)、(<=)、(>)、(>=)、compare
- **Num 类型类**: (+)、(-)、(*)、abs、signum
- **Show 类型类**: show、prints 转换为字符串
- **Read 类型类**: read、解析字符串为值
- **实例声明**: instance 关键字、自动派生
- **newtype**: 单构造函数包装器、无运行时开销
- **type 同义词**: type String = [Char]

## 核心代码示例

```haskell
-- 类型类约束
Eq a => [a] -> [a] -> Bool
Ord a => a -> a -> Ordering

-- 实例声明
instance Eq Color where
  Red == Red = True
  Green == Green = True
  _ == _ = False

-- newtype
newtype Username = Username String
newtype Password = Password String

-- 类型同义词
type Point = (Double, Double)
type Matrix = [[Double]]
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/类型类]]
- [[wiki/concepts/类型系统]]
- [[wiki/concepts/代数数据类型]]
