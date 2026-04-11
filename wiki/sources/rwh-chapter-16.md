---
title: "RWH 第16章-使用Parsec"
source: "Clippings/RWH-Chapters-zh/第16章-使用Parsec.md"
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
  - "[[wiki/concepts/类型类]]"
---

# RWH 第16章-使用Parsec

## 本章概述

本章介绍 Parsec 解析组合子库，包括组合子解析基础、token 解析、表达式解析器构建和错误报告。

## 关键概念

- **Parsec**: 工业级解析库、组合子解析
- **Parser**: 消耗输入、返回结果
- **组合子**: try、(<|>)、many、many1、optional
- **Token 解析**: string、oneOf、noneOf、spaces
- **Expr 解析器**: precedence climbing、操作符表
- **错误报告**: unexpected、expected、<?>
- **SourcePos**: 位置追踪、友好错误消息

## 核心代码示例

```haskell
import Text.Parsec
import Text.Parsec.String (Parser)

-- 基本解析器
char :: Char -> Parser Char
string :: String -> Parser String
oneOf :: [Char] -> Parser Char

-- 组合子
try :: Parser a -> Parser a
(<|>) :: Parser a -> Parser a -> Parser a
many :: Parser a -> Parser [a]
many1 :: Parser a -> Parser [a]
optional :: Parser a -> Parser ()

-- 表达式解析器
expr :: Parser Int
expr = term `chainl1` addop

term :: Parser Int
term = factor `chainl1` mulop

factor :: Parser Int
factor = parens expr <|> number

addop :: Parser (Int -> Int -> Int)
addop = (char '+' >> return (+)) <|> (char '-' >> return (-))
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/单子]]
- [[wiki/concepts/类型类]]
- [[wiki/concepts/代数数据类型]]
