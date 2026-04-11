---
title: "RWH 第09章-案例研究-文件系统搜索库"
source: "Clippings/RWH-Chapters-zh/第09章-案例研究-文件系统搜索库.md"
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
  - "[[wiki/concepts/递归]]"
  - "[[wiki/concepts/高阶函数]]"
---

# RWH 第09章-案例研究-文件系统搜索库

## 本章概述

本章通过构建一个类似 Unix find 的文件系统搜索库，介绍目录遍历、文件属性检查、Predicate 函数设计和递归搜索策略。

## 关键概念

- **目录遍历**: getDirectoryContents、递归下降
- **文件属性**: doesFileExist、doesDirectoryExist、getPermissions
- **Predicate 函数**: (a -> Bool) 过滤条件
- **递归搜索**: 深度优先、模式匹配路径
- **路径处理**: FilePath、</> 路径连接
- **过滤器组合**: and、or、not 组合谓词

## 核心代码示例

```haskell
import System.Directory (doesFileExist, doesDirectoryExist,
                         getPermissions, searchable)
import System.FilePath ((</>))

-- 递归搜索
find :: (FilePath -> Bool) -> FilePath -> IO [FilePath]
find p path = do
  isFile <- doesFileExist path
  if isFile
    then return [path | p path]
    else do
      isDir <- doesDirectoryExist path
      if isDir
        then searchdir path
        else return []

searchdir :: FilePath -> IO [FilePath]
searchdir dir = do
  names <- getDirectoryContents dir
  let properNames = filter (`notElem` [".", ".."]) names
  paths <- forM properNames $ \name -> do
    let path = dir </> name
    find (const True) path
  return (concat paths)

-- Predicate 组合
(.&&?) :: (a -> Bool) -> (a -> Bool) -> a -> Bool
f .&&? g = \x -> f x && g x

(.||?) :: (a -> Bool) -> (a -> Bool) -> a -> Bool
f .||? g = \x -> f x || g x
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/递归]]
- [[wiki/concepts/高阶函数]]
- [[wiki/concepts/IO Monad]]
