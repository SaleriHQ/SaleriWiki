---
title: "LYAH 第二章: 准备好了吗？"
source: "https://haskell.swizzer.cc/ch02/ready-go/"
author: "Miran Lipovača"
course: "Learn You A Haskell"
created: 2026-04-09
updated: 2026-04-09
type: source
tags:
  - source
  - haskell
  - tutorial
  - beginner
related:
  - "[[wiki/concepts/函数式编程]]"
  - "[[Clippings/01-intro]]"
---

# LYAH 第二章: 准备好了吗？

## 来源信息

- **教材**: Learn You A Haskell for Great Good!
- **作者**: Miran Lipovača
- **章节**: 第二章 - 入门基础

---

## 核心内容

### ghci 交互式环境

```haskell
-- 启动
ghci

-- 简单运算
ghci> 2 + 15
17
ghci> 49 * 100
4900
ghci> 5 / 2
2.5
```

### 运算符优先级

```haskell
ghci> 50 * 100 - 4999   -- 等于 (50 * 100) - 4999
1
ghci> 50 * (100 - 4999)
-244950
```

### 布尔运算

```haskell
ghci> True && False
False
ghci> True && True
True
ghci> False || True
True
ghci> not False
True
```

### 相等性

```haskell
ghci> 5 == 5
True
ghci> 5 /= 4
True
ghci> "hello" == "hello"
True
```

### 类型错误

```haskell
-- 类型不匹配会报错
ghci> 5 + "llama"
-- No instance for (Num [Char])

ghci> True == 5
-- 类型不匹配
```

---

## 关键概念

- **ghci**: GHC 交互式解释器
- **运算符**: `+`, `-`, `*`, `/`, `&&`, `||`, `not`, `==`, `/=`
- **类型检查**: Haskell 在编译时拒绝类型不匹配

---

## 相关来源

- [[Clippings/01-intro]] - UPenn CIS194 Haskell 入门
- [[Clippings/02. Ready Go - Learn You A Haskell for Great Good!]]
