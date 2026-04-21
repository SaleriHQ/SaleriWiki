---
title: "RWH 第01章-入门"
source: "Clippings/RWH-Chapters-zh/第01章-入门.md"
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
  - "[[wiki/concepts/类型系统]]"
---

# RWH 第01章-入门

## 本章概述

本章介绍 GHC (Glasgow Haskell Compiler) 环境的安装和使用，包括 ghci 交互式解释器的基本操作。通过简单的算术和布尔运算示例，帮助读者建立对 Haskell 的初步认识。

## 关键概念

- **GHC 组件**: ghc 编译器、ghci 交互式解释器、runghc 脚本运行器
- **ghci 基础**: 表达式求值、:set prompt 命令、基本命令 (:?, :load, :edit)
- **算术运算**: Haskell 中的加(+)、减(-)、乘(*)、除(/)运算
- **布尔运算**: True/False、(&&)、(||)、not
- **列表操作**: 列表字面量 [1,2,3]、字符串即字符列表
- **简单程序**: runghc 运行脚本程序

## 核心代码示例

```haskell
-- ghci 中的基本运算
ghci> 2 + 2
4
ghci> (6 * 100) - 200
400
ghci> not True && False
False

-- 列表操作
ghci> [1, 2, 3] ++ [4, 5]
[1,2,3,4,5]
ghci> head "Hello"
'H'
ghci> length "Haskell"
7
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/函数式编程]]
- [[wiki/concepts/类型系统]]
- [[wiki/concepts/纯函数]]
