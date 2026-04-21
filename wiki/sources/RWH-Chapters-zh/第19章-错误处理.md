---
title: "RWH 第19章-错误处理"
source: "Clippings/RWH-Chapters-zh/第19章-错误处理.md"
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
  - "[[wiki/concepts/单子]]"
  - "[[wiki/concepts/代数数据类型]]"
---

# RWH 第19章-错误处理

## 本章概述

本章介绍 Haskell 中的错误处理策略，包括纯错误处理 (Maybe/Either)、IO 异常系统、Error Monad 和最佳实践。

## 关键概念

- **Maybe**: Nothing 表示失败、无信息
- **Either**: Left 错误、Right 成功
- **IO 异常**: throw、catch、try
- **Error Monad**: Error e、throwError、catchError
- **exceptT**: Transformer 版本
- **类型安全错误**: 显式 vs 隐式

## 核心代码示例

```haskell
-- Maybe 错误处理
lookup :: Eq k => k -> [(k, v)] -> Maybe v

findM :: Monad m => (a -> m Bool) -> [a] -> m (Maybe a)
findM _ [] = return Nothing
findM p (x:xs) = do
  flag <- p x
  if flag then return (Just x) else findM p xs

-- Either 错误处理
data ParseError = ParseError String SourcePos

firstSuccess :: [Either e a] -> Either e a
firstSuccess [] = error "No alternatives"
firstSuccess (x:xs) = case x of
  Right v -> Right v
  Left _ -> firstSuccess xs

-- IO 异常
import Control.Exception (try, catch, IOException)

readFileMayThrow :: FilePath -> IO String
readFileMayThrow path = readFile path

readFileSafe :: FilePath -> IO (Either IOException String)
readFileSafe path = try (readFile path)

-- Error Monad
class Monad m => MonadError e m | m -> e where
  throwError :: e -> m a
  catchError :: m a -> (e -> m a) -> m a
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/单子]]
- [[wiki/concepts/代数数据类型]]
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/Either]]
- [[wiki/concepts/Maybe]]
