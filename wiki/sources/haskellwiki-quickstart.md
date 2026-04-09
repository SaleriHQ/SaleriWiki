---
title: 十分钟学会 Haskell
source: https://wiki.haskell.org/Cn/%E5%8D%81%E5%88%86%E9%92%9F%E5%AD%A6%E4%BC%9A_Haskell
author: Haskell Wiki
created: 2026-04-08
type: source
tags:
  - source
  - haskell
  - tutorial
---

## 摘要

Haskell Wiki 的快速入门教程，涵盖 Haskell 语言的基础知识：表达式、类型、列表、IO 操作等。适合作为入门参考。

## 关键内容

### 表达式
- 数学表达式直接求值
- 字符串用 `++` 连接
- 函数调用参数紧跟，无需括号

### 类型
- `Int` - 机器整数 (~30位)
- `Integer` - 任意精度整数
- `Double` - 双精度浮点
- `Bool` - 布尔值
- `Char` / `String` - 字符/字符串

### 列表
```haskell
[1..5]           -- [1,2,3,4,5]
x : xs           -- 头部 cons 尾部
[1,3..10]        -- [1,3,5,7,9]
```

### IO 操作
```haskell
putStrLn "Hello"
getLine >>= \name -> putStrLn ("Hi, " ++ name)
```

## 与 CIS194 的关联

与 [[wiki/sources/cis194-lecture1]] 互补，更侧重语法速查。
