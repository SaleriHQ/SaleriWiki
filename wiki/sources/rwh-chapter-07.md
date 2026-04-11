---
title: "RWH 第07章-输入输出"
source: "Clippings/RWH-Chapters-zh/第07章-输入输出.md"
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
  - "[[wiki/concepts/单子]]"
---

# RWH 第07章-输入输出

## 本章概述

本章介绍 Haskell 中的 IO 操作，包括 IO Monad、do 语法、getLine/putStrLn 等基本 IO 函数、文件读写、命令行参数处理和环境变量访问。

## 关键概念

- **IO Monad**: IO a 类型、副作用操作包装
- **do 语法**: 顺序组合 IO 操作、<- 绑定
- **getLine/putStrLn**: 标准输入输出
- **文件读写**: readFile、writeFile、appendFile
- **命令行参数**: getArgs、getProgName
- **环境变量**: getEnvironment
- **字符串处理**: String、效率考虑

## 核心代码示例

```haskell
-- 基本 IO
main :: IO ()
main = do
  putStrLn "Enter your name:"
  name <- getLine
  putStrLn ("Hello, " ++ name ++ "!")

-- 文件操作
main :: IO ()
main = do
  content <- readFile "input.txt"
  writeFile "output.txt" (map toUpper content)

-- 命令行参数
import System.Environment (getArgs, getProgName)
main :: IO ()
main = do
  args <- getArgs
  progName <- getProgName
  case args of
    [input] -> processFile input
    _ -> putStrLn "Usage: prog <input>"
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/单子]]
- [[wiki/concepts/纯函数]]
