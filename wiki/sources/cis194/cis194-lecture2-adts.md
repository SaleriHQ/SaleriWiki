---
title: CIS 194 Lecture 2 — 代数数据类型
source: https://www.seas.upenn.edu/~cis1940/spring13/lectures/02-ADTs.html
author: CIS 194 Course Staff
created: 2026-04-09
type: source
tags:
  - source
  - lecture
  - haskell
  - cis194
  - adts
---

## 摘要

CIS 194 第二次课程讲义，通过 **FailableDouble**（可失败双精度数）和 **Person**（人员）等具体例子，系统讲解代数数据类型（ADT）的核心概念：多构造器、模式匹配、递归类型。与作业版（HW2）不同，课程版更注重概念讲解，作业版更注重实战练习。

## 关键概念

### 枚举类型

枚举是 ADT 的特例——只有零参数构造器：

```haskell
data Thing = Shoe | Ship | SealingWax | Cabbage | King
  deriving Show

isSmall :: Thing -> Bool
isSmall Shoe       = True
isSmall Ship       = False
isSmall SealingWax = True
isSmall Cabbage    = True
isSmall King       = False
```

### 超越枚举

带参数的构造器：

```haskell
data FailableDouble = Failure
                    | OK Double
  deriving Show

safeDiv :: Double -> Double -> FailableDouble
safeDiv _ 0 = Failure
safeDiv x y = OK (x / y)
```

### 多参数构造器

```haskell
data Person = Person String Int Thing
  deriving Show

brent :: Person
brent = Person "Brent" 31 SealingWax

getAge :: Person -> Int
getAge (Person _ a _) = a
```

### @-patterns（as-模式）

匹配模式的同时保留整体：

```haskell
baz :: Person -> String
baz p@(Person n _ _) = "The name field of (" ++ show p ++ ") is " ++ n
```

### 嵌套模式

```haskell
checkFav :: Person -> String
checkFav (Person n _ SealingWax) = n ++ ", you're my kind of person!"
checkFav (Person n _ _)          = n ++ ", your favorite thing is lame."
```

### 递归数据类型

```haskell
-- 自定义整数列表
data IntList = Empty | Cons Int IntList

intListProd :: IntList -> Int
intListProd Empty      = 1
intListProd (Cons x l) = x * intListProd l

-- 二叉树
data Tree = Leaf Char
          | Node Tree Int Tree
  deriving Show
```

## 关键要点

1. **构造器即模式**：模式匹配是构造的反操作——提取构造时填入的值
2. **`@` 模式**：既绑定整体变量，又绑定内部各字段
3. **嵌套模式**：可以在一个模式中深入多层结构
4. **递归 ADT + 递归函数**：天然配对，基准情况（`Empty`）+ 递归情况（`Cons`）
5. **类型构造器与值构造器同名**：常见惯用手法，两者存在于不同命名空间

## 与维基的关联

此来源涉及：
- [[wiki/concepts/代数数据类型]] — 枚举、超越枚举、ADT 的一般形式
- [[wiki/concepts/模式匹配]] — 模式匹配完整语法（@ 模式、嵌套模式、case 表达式）
- [[wiki/concepts/递归]] — 递归数据类型 IntList 和 Tree
- [[wiki/sources/cis194-hw2]] — 作业版：MessageTree 递归数据结构的实战练习
