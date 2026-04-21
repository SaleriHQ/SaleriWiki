---
title: "RWH 第11章-测试与质量保证"
source: "Clippings/RWH-Chapters-zh/第11章-测试与质量保证.md"
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
  - "[[wiki/concepts/代数数据类型]]"
---

# RWH 第11章-测试与质量保证

## 本章概述

本章介绍 Haskell 测试框架，包括 HUnit 单元测试、QuickCheck 属性测试、测试组织结构和最佳实践。

## 关键概念

- **HUnit**: 单元测试框架、Assertion、TestCase
- **QuickCheck**: 属性测试、自动生成测试用例
- **Arbitrary**: 类型类、随机数据生成
- **属性测试**: forall、==>, 量化条件
- **测试组织**: Test.HUnit、Test.QuickCheck
- **断言**: assertEqual、assertBool、assertFailure

## 核心代码示例

```haskell
-- HUnit 示例
import Test.HUnit

test1 :: Test
test1 = TestCase $ assertEqual "head" 1 (head [1,2,3])

test2 :: Test
test2 = TestCase $ assertBool "length >= 0" (length [] >= 0)

tests :: Test
tests = TestList [TestLabel "test1" test1,
                  TestLabel "test2" test2]

-- QuickCheck 示例
import Test.QuickCheck

prop_reverse :: [Int] -> Bool
prop_reverse xs = reverse (reverse xs) == xs

prop_sort :: [Int] -> Bool
prop_sort xs = all (\(x,y) -> x <= y) (zip sorted (tail sorted))
  where sorted = sort xs

-- 带条件的属性
prop_insert :: Int -> [Int] -> Property
prop_insert x xs = x >= 0 ==> insert x (sort xs) == sort (x:xs)
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/类型系统]]
- [[wiki/concepts/代数数据类型]]
- [[wiki/concepts/类型类]]
