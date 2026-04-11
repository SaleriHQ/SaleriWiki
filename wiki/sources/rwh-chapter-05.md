---
title: "RWH 第05章-编写库-处理JSON数据"
source: "Clippings/RWH-Chapters-zh/第05章-编写库-处理JSON数据.md"
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
  - "[[wiki/concepts/代数数据类型]]"
  - "[[wiki/concepts/类型类]]"
---

# RWH 第05章-编写库-处理JSON数据

## 本章概述

本章通过构建一个小型 Haskell 库来处理 JSON 数据，介绍 JSON 格式、数据类型设计、序列化/反序列化、模块组织和泛型编程基础。

## 关键概念

- **JSON 格式**: null、boolean、number、string、array、object
- **库设计**: 模块导出、类型抽象、信息隐藏
- **数据序列化**: ToJson、FromJson 类型类
- **泛型编程**: DeriveGeneric、toJSON、fromJSON
- **错误处理**: Maybe、Either、显式错误消息

## 核心代码示例

```haskell
-- JSON 数据类型
data JsonValue = JsonNull
               | JsonBool Bool
               | JsonNumber Double
               | JsonString String
               | JsonArray [JsonValue]
               | JsonObject [(String, JsonValue)]

-- 类型类实例
instance ToJson Bool where
  toJson True = JsonBool True
  toJson False = JsonBool False

-- 泛型派生
{-# LANGUAGE DeriveGeneric #-}
data Config = Config { port :: Int } deriving (Generic)
instance ToJson Config)
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/代数数据类型]]
- [[wiki/concepts/类型类]]
- [[wiki/concepts/模式匹配]]
