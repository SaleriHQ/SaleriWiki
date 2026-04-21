---
title: "CIS194: Homework 1 - 信用卡验证与汉诺塔"
source: "Clippings/01-intro.pdf"
course: "UPenn CIS194"
lecture: 1
author: "Brent Yorgey"
created: 2026-04-08
updated: 2026-04-08
type: source
tags:
  - source
  - haskell
  - homework
  - exercise
related:
  - "[[wiki/concepts/函数式编程]]"
  - "[[Clippings/01-intro]]"
---

# CIS194: Homework 1 - 信用卡验证与汉诺塔

## 来源信息

- **课程**: UPenn CIS194 - Introduction to Haskell
- **讲师**: Brent Yorgey
- **作业编号**: Homework 1
- **截止日期**: January 14

---

## 练习 1: 信用卡数字提取

### 函数签名

```haskell
toDigits :: Integer -> [Integer]
toDigitsRev :: Integer -> [Integer]
```

### 要求

- `toDigits`: 将正整数转换为数字列表
- `toDigitsRev`: 同样，但数字顺序反转
- 0 或负数返回空列表

### 示例

```
toDigits 1234 == [1,2,3,4]
toDigitsRev 1234 == [4,3,2,1]
toDigits 0 == []
toDigits (-17) == []
```

---

## 练习 2: 交替翻倍

### 函数签名

```haskell
doubleEveryOther :: [Integer] -> [Integer]
```

### 规则

从右数起，每隔一个数字翻倍（第二位、第四位...）

### 示例

```
doubleEveryOther [8,7,6,5] == [16,7,12,5]
doubleEveryOther [1,2,3] == [1,4,3]
```

---

## 练习 3: 求和

### 函数签名

```haskell
sumDigits :: [Integer] -> Integer
```

### 规则

将所有数字的每一位相加（处理两位数）

### 示例

```
sumDigits [16,7,12,5] = 1+6+7+1+2+5 = 22
```

---

## 练习 4: 验证信用卡

### 函数签名

```haskell
validate :: Integer -> Bool
```

### 完整算法

1. 使用 `toDigits` 获取数字列表
2. 使用 `doubleEveryOther` 翻倍交替位
3. 使用 `sumDigits` 求和
4. 检查 `sum mod 10 == 0`

### 示例

```
validate 4012888888881881 = True
validate 4012888888881882 = False
```

---

## 练习 5: 汉诺塔

### 函数签名

```haskell
type Peg = String
type Move = (Peg, Peg)
hanoi :: Integer -> Peg -> Peg -> Peg -> [Move]
```

### 递归策略

移动 n 个盘子从 a 到 b（使用 c 作为临时存储）：

1. 将 n-1 个盘子从 a 移动到 c（使用 b）
2. 将最上面的盘子从 a 移动到 b
3. 将 n-1 个盘子从 c 移动到 b（使用 a）

### 示例

```
hanoi 2 "a" "b" "c" == [("a","c"), ("a","b"), ("c","b")]
```

---

## 练习 6 (可选): 四柱汉诺塔

挑战：使用 4 根柱子代替 3 根，用尽可能少的步数移动。

---

## 涉及的概念

- [[wiki/concepts/函数式编程]] - 纯函数式、递归、模式匹配
- 列表操作 - `map`、`head`、`tail`
- 类型声明 - 类型同义词 `type Peg = String`

---

## 作业要求

> 努力写出不仅能运行，而且风格优雅、简洁的代码。
> 
> 编写执行单一任务的小函数，然后组合这些小函数来创建更复杂的函数。
> 
> 不要重复自己：为一个逻辑任务编写一个函数，并在需要时重用函数。

---

## 相关来源

- [[Clippings/01-intro]] - CIS194 Lecture 1 讲义
- [[Clippings/01-intro.pdf]] - 原始 PDF 文件
