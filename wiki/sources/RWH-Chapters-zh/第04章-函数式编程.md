---
title: "RWH 第04章-函数式编程"
source: "Clippings/RWH-Chapters-zh/第04章-函数式编程.md"
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
  - "[[wiki/concepts/函数式编程]]"
  - "[[wiki/concepts/高阶函数]]"
---

# RWH 第04章-函数式编程

## 本章概述

本章培养函数式编程思维，介绍高阶函数、匿名函数(lambda)、闭包、Currying、部分应用，以及 Point-free 风格编程。

## 关键概念

- **函数式思维**: 表达式求值、组合优于命令
- **高阶函数**: 函数作为参数/返回值
- **匿名函数**: \x -> x + 1 lambda 表达式
- **闭包**: 捕获自由变量、状态封装
- **Currying**: 多参数函数转换为一元函数链
- **部分应用**: flip、($)、section 语法
- **Point-free 风格**: 组合子编程、避免显式参数

## 核心代码示例

```haskell
-- 高阶函数
map :: (a -> b) -> [a] -> [b]
filter :: (a -> Bool) -> [a] -> [a]

-- 匿名函数
ghci> map (\x -> x * 2) [1, 2, 3]
[2, 4, 6]

-- Currying
add :: Int -> Int -> Int
add x y = x + y
add 1 :: Int -> Int  -- 部分应用

-- Point-free
sum = foldr (+) 0
filter even = filter ((==) 0 . (`mod` 2))
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/函数式编程]]
- [[wiki/concepts/高阶函数]]
- [[wiki/concepts/纯函数]]
