---
title: CIS194 Lecture 1 - Haskell 基础
source: https://www.seas.upenn.edu/~cis1940/spring13/lectures/01-intro.html
author: Brent Yorgey (UPenn)
created: 2026-04-08
type: source
tags:
  - source
  - haskell
  - course
---

## 摘要

CIS194 是宾夕法尼亚大学的 Haskell 编程课程。Lecture 1 介绍了函数式编程的核心概念：函数式思维、纯性、惰性求值和静态类型系统。

## 关键概念

- **函数式**: 函数是一等公民，程序 = 表达式求值
- **纯性**: 无副作用，引用透明，不可变数据
- **惰性**: 表达式按需求值，支持无限数据结构
- **静态类型**: 编译时检查，类型推断

## Haskell 三大主题

1. **Types** - 表达力强的类型系统
2. **Abstraction** - DRY 原则，参数多态、高阶函数
3. **Wholemeal Programming** - 整体思维编程

## 基础语法

```haskell
-- 模式匹配
sumtorial 0 = 0
sumtorial n = n + sumtorial (n-1)

-- 守卫
hailstone n
  | even n    = n `div` 2
  | otherwise = 3*n + 1

-- 列表
[1..5]         -- [1,2,3,4,5]
map (+2) [1,2]  -- [3,4]
```
