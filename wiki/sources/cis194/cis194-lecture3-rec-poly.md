---
title: CIS 194 Lecture 3 — 递归模式、多态与 Prelude
source: https://www.seas.upenn.edu/~cis1940/spring13/lectures/03-rec-poly.html
author: CIS 194 Course Staff
created: 2026-04-10
type: source
tags:
  - source
  - lecture
  - haskell
  - cis194
  - recursion
  - polymorphism
---

## 摘要

CIS 194 第三次课程讲义，核心观点：**经验丰富的 Haskell 程序员几乎不手写递归函数**，而是借助标准库中的高阶函数（Map、Filter、Fold）来抽象递归模式。此讲义进一步深化了多态（Polymorphism）概念，并介绍了全函数（Total Function）与偏函数（Partial Function）的区别。

## 关键概念

### 三大递归模式

Haskell 标准库将常见的递归操作抽象为三个高阶函数：

**Map（映射）** — 对每个元素执行操作：

```haskell
-- 具体版
absAll :: IntList -> IntList
absAll Empty       = Empty
absAll (Cons x xs) = Cons (abs x) (absAll xs)

squareAll :: IntList -> IntList
squareAll Empty       = Empty
squareAll (Cons x xs) = Cons (x*x) (squareAll xs)

-- 抽象版（泛化到任意类型）
mapIntList :: (Int -> Int) -> IntList -> IntList
mapIntList _ Empty       = Empty
mapIntList f (Cons x xs) = Cons (f x) (mapIntList f xs)
```

**Filter（过滤）** — 按条件保留元素：

```haskell
keepOnlyEven :: IntList -> IntList
keepOnlyEven Empty = Empty
keepOnlyEven (Cons x xs)
  | even x    = Cons x (keepOnlyEven xs)
  | otherwise = keepOnlyEven xs
```

**Fold（折叠）** — 将列表"总结"为单个值（如 sum、product、maximum）。下节课详细讲解。

### 多态数据类型

将 `IntList` 参数化，解放类型约束：

```haskell
-- 多态列表：参数 t 可以是任意类型
data List t = E | C t (List t)

lst1 :: List Int
lst1 = C 3 (C 5 (C 2 E))

lst2 :: List Char
lst2 = C 'x' (C 'y' (C 'z' E))
```

### 多态函数

**类型变量**（必须小写开头）表示"任意类型"：

```haskell
-- 最泛化的 mapList：输入类型 a，输出类型 b
mapList :: (a -> b) -> List a -> List b
mapList _ E        = E
mapList f (C x xs) = C (f x) (mapList f xs)

-- 关键洞察：调用者选择类型，函数必须对所有类型都成立
filterList :: (t -> Bool) -> List t -> List t
```

### Prelude 标准函数

- `map :: (a -> b) -> [a] -> [b]` — List t 的 Prelude 版
- `filter :: (a -> Bool) -> [a] -> [a]` — Filter 的 Prelude 版
- `Maybe a` — 表示可能失败的值：`Nothing | Just a`

### 全函数 vs 偏函数

| 术语 | 定义 | 例子 |
|------|------|------|
| **全函数 (Total)** | 对所有合法输入都有定义的函数 | `safeHead :: [a] -> Maybe a` |
| **偏函数 (Partial)** | 存在导致崩溃或无限循环的输入 | `head :: [a] -> a`（空列表崩溃） |

**核心原则：避免偏函数。用 `Maybe` 或 `NonEmptyList` 让类型反映可能的失败。**

```haskell
-- 偏函数（会崩溃）
head :: [a] -> a

-- 全函数（用类型编码失败可能性）
safeHead :: [a] -> Maybe a
safeHead []    = Nothing
safeHead (x:_) = Just x
```

## 关键要点

1. **Wholemeal Programming**：用高阶函数思考，而不是逐个写递归函数
2. **多态 = 类型参数化**：类型变量 `a`、`b` 让函数和数据结构适用于任意类型
3. **调用者决定类型**：多态函数必须对所有类型都成立，不能依赖类型做决策
4. **偏函数是错误**：`head`、`tail`、`init`、`last`、`!!` 应避免使用
5. **`Maybe` 是安全的替代方案**：用类型系统反映可能的失败，而非依赖运行时崩溃
6. **`NonEmptyList`**：当语义上保证非空时，用新类型让编译器强制执行

## 与维基的关联

此来源涉及：
- [[wiki/concepts/递归]] — Map/Filter/Fold 三大递归抽象模式
- [[wiki/concepts/代数数据类型]] — 多态数据类型 List t 的定义
- [[wiki/concepts/模式匹配]] — Filter、Map 中的模式匹配
- [[wiki/sources/cis194-hw2]] — 递归数据结构的实战基础
- [[wiki/sources/cis194-lecture2-adts]] — 递归 ADT（IntList、Tree）的概念基础
