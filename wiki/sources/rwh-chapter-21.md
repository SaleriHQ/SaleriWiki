---
title: "RWH 第21章-使用数据库"
source: "Clippings/RWH-Chapters-zh/第21章-使用数据库.md"
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
  - "[[wiki/concepts/IO Monad]]"
  - "[[wiki/concepts/类型类]]"
---

# RWH 第21章-使用数据库

## 本章概述

本章介绍 Haskell 数据库编程，使用 HDBC (Haskell Database Connectivity) 接口操作 SQLite 和 PostgreSQL，包括查询、事务和参数化查询。

## 关键概念

- **HDBC**: Haskell Database Connectivity
- **连接管理**: connect、disconnect、commit
- **查询执行**: quickQuery、execute、fetchAllRows
- **事务**: transaction、自动提交控制
- **参数化查询**: toSql、fromSql、SqlValue
- **SQLite**: 文件数据库、轻量级
- **PostgreSQL**: 高级特性、网络连接

## 核心代码示例

```haskell
import Database.HDBC
import Database.HDBC.Sqlite3 (connectSqlite3)

-- 连接数据库
main :: IO ()
main = do
  conn <- connectSqlite3 "test.db"
  -- 执行查询
  results <- quickQuery conn "SELECT * FROM users WHERE age > ?" [toSql 18]
  mapM_ (putStrLn . show) results
  commit conn
  disconnect conn

-- 参数化查询
insertUser :: IConnection conn => conn -> String -> Int -> IO ()
insertUser conn name age = do
  execute conn "INSERT INTO users (name, age) VALUES (?, ?)"
    [toSql name, toSql age]
  commit conn

-- 事务处理
withTransaction :: IConnection conn => conn -> IO a -> IO a
withTransaction conn action = do
  beginTransaction conn
  result <- action
  commit conn
  return result
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/类型类]]
- [[wiki/concepts/代数数据类型]]
