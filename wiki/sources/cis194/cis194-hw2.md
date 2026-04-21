---
title: CIS 194 Homework 2 — 代数数据类型
source: UPenn CIS194
author: CIS 194 Course Staff
created: 2026-04-09
type: source
tags:
  - source
  - homework
  - haskell
  - cis194
---

## 摘要

CIS 194 第二次作业通过**日志文件解析系统**这一实战项目，深入练习代数数据类型（ADT）、**递归数据结构的构建与遍历**、以及**函数复合**。作业包含 6 个练习，从解析到排序再到查询，完整覆盖了 ADT 在实际问题中的应用。

## 关键概念

### 代数数据类型的实际应用

作业定义了一组 ADT 来建模日志消息：

```haskell
-- 消息类型：枚举 + 带参数构造器
data MessageType
    = Info
    | Warning
    | Error Int          -- 带参数的构造器（错误级别）
    deriving (Show, Eq)

-- 日志消息：递归使用自定义类型
data LogMessage
    = LogMessage MessageType TimeStamp String
    | Unknown String     -- 处理格式错误的数据
    deriving (Show, Eq)

type TimeStamp = Int
```

### 递归数据类型：二叉搜索树

`MessageTree` 是递归数据结构的经典范例：

```haskell
data MessageTree = Leaf
    | Node MessageTree LogMessage MessageTree
```

通过 `insert`、`build`、`inOrder` 三个函数，学生练习递归数据结构的三大操作：**插入**、**构建**、**遍历**。

## 关键要点

1. **多构造器 ADT**：`MessageType` 用三种构造器（`Info`、`Warning`、`Error Int`）表示日志级别，`Error` 带参数表示严重程度
2. **`Unknown` 构造器**：`LogMessage` 中的 `Unknown String` 优雅地处理格式错误，体现了"将无效状态表示为类型"的思想
3. **二叉搜索树的递归操作**：
   - `insert`：将新消息递归插入左/右子树
   - `build`：通过折叠（fold）依次插入构建整棵树
   - `inOrder`：中序遍历（左→根→右）得到时间戳有序的列表
4. **不要重复造轮子**：使用 `read`、`lines`、`words` 等标准库函数，而非手写解析逻辑

## 与维基的关联

此来源涉及：
- [[wiki/concepts/代数数据类型]] — ADT 定义、多构造器、递归类型
- [[wiki/concepts/递归]] — 递归数据结构的插入、构建、遍历
- [[wiki/concepts/模式匹配]] — `insert`、`whatWentWrong` 等函数的实现
