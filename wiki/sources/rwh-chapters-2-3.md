---
title: Real World Haskell 第 2、3 章
source: http://book.realworldhaskell.org/read/types-and-functions.html
author: Bryan O'Sullivan, Don Stewart, John Goerzen
created: 2026-04-09
type: source
tags:
  - source
  - book
  - haskell
  - real-world-haskell
---

## 摘要

Real World Haskell 第 2、3 章的完整中文翻译。第 2 章深入类型系统（强类型/静态类型/类型推断/多态/纯度/惰性求值），第 3 章讲解自定义类型、代数数据类型、模式匹配、记录语法、参数化类型、递归类型、卫述语等核心概念。

> 注：此为 `Clippings/Real-World-Haskell-02-03.md` 的来源摘要，原文为英文，此处为中文翻译版本。

## 关键概念

### 第 2 章：类型与函数

- **强类型**：拒绝类型不匹配的表达式，不会隐式转换
- **静态类型**：编译时检查所有类型错误
- **类型推断**：编译器自动推导类型，无需处处注解
- **多态**：类型变量 `a`，同一函数处理多种类型
- **纯度**：无副作用，函数结果只依赖输入
- **惰性求值**：按需求值，thunk 延迟计算

### 第 3 章：定义类型

- **代数数据类型**：多构造器，枚举 + 带参数
- **模式匹配**：通过构造器分解值，构造的反操作
- **记录语法**：命名字段，自动生成访问函数
- **参数化类型**：`Maybe a`、`Either a b`
- **递归类型**：类型定义中引用自身
- **卫述语（Guards）**：模式 + 布尔条件组合

## 关键要点

1. **`read`**：字符串 → 值（需显式类型注解）
2. **`words`/`unwords`**：单词分割与合并
3. **`lines`/`take`/`drop`**：列表操作三剑客
4. **函数复合 `.`**：`map f . filter g` 组合数据流
5. **`Maybe`**：`Nothing`/`Just a` 优雅处理缺失值
6. **`let` vs `where`**：局部变量绑定，两种风格可互换

## 与维基的关联

此来源涉及：
- [[wiki/concepts/类型系统]] — 强类型、静态类型、类型推断
- [[wiki/concepts/标准库函数]] — `read`、`words`、`unwords`、`take`、`drop`、`.` 的完整详解
- [[wiki/concepts/代数数据类型]] — 代数数据类型、参数化类型、递归类型
- [[wiki/concepts/模式匹配]] — 模式匹配、@ 模式、case 表达式、卫述语
- [[wiki/concepts/函数式编程]] — 纯度、函数复合、高阶函数
