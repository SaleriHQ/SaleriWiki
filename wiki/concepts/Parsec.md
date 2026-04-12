---
title: Parsec
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - haskell
  - parsing
  - combinator
sources: 1
---

## 定义

Parsec 是一个**函数式解析器组合库**，允许将小的解析函数组合成复杂的解析器。

```
Parsec = 解析 + Combinator（组合子）
```

## 核心概念

| 概念 | 说明 |
|------|------|
| `Parser` | 解析器类型 |
| `GenParser a st` | 泛型解析器（处理 `a` 类型输入） |
| `parse` | 运行解析器 |

## 基础类型

```haskell
-- 解析器：输入 → [(结果, 剩余输入)]
type Parser a = GenParser Char () a

-- 运行解析器
parse :: Parser a -> String -> Either ParseError a
parse csvFile "(unknown)" input
```

## 基础解析器

### 单字符解析

```haskell
char :: Char -> Parser Char      -- 匹配单个字符
oneOf :: [Char] -> Parser Char  -- 匹配列表中的字符
noneOf :: [Char] -> Parser Char -- 匹配不在列表中的字符

-- 示例
letter = oneOf ['a'..'z']
digit  = oneOf ['0'..'9']
```

### 字符串解析

```haskell
string :: String -> Parser String  -- 匹配特定字符串

-- 示例
keyword = string "if"
```

## 组合子

### 选择 `<|>`

```haskell
-- 尝试左侧，失败则尝试右侧
choice :: [Parser a] -> Parser a
choice = fold (<|>) empty

-- 示例
reserved = string "if" <|> string "else"
```

### 重复

```haskell
many :: Parser a -> Parser [a]     -- 零次或多次
many1 :: Parser a -> Parser [a]    -- 一次或多次
skipMany :: Parser a -> Parser ()   -- 零次或多次，跳过结果
skipMany1 :: Parser a -> Parser ()   -- 一次或多次
```

### 分隔列表

```haskell
sepBy :: Parser a -> Parser sep -> Parser [a]
-- 解析: a sep a sep a ... (最后一个后无分隔符)
-- 示例: "a,b,c" -> [a, b, c]

endBy :: Parser a -> Parser sep -> Parser [a]
-- 解析: a sep a sep a sep
-- 示例: "a,b,c," -> [a, b, c] (用于每项后必须有分隔符的情况)
```

## 实际示例：CSV 解析

```haskell
import Text.ParserCombinators.Parsec

-- CSV: 0或多行，每行以换行结束
csvFile :: Parser [[String]]
csvFile = many line <* eof

-- 一行：1或多单元格，以换行结束
line :: Parser [String]
line = cells <* eol

-- 单元格：逗号分隔
cells :: Parser [String]
cells = cell `sepBy` char ','

-- 单元格内容：除逗号和换行外的字符
cell :: Parser String
cell = many (noneOf ",\n")

-- 换行符
eol :: Parser Char
eol = char '\n'

-- 解析入口
parseCSV :: String -> Either ParseError [[String]]
parseCSV = parse csvFile "(CSV)"
```

## Applicative 风格

```haskell
import Text.Parsec
import Text.Parsec.String

-- Applicative 风格
data Person = Person String Int deriving (Show)

person :: Parser Person
person = Person <$> name <*> (char ' ' *> age)

name :: Parser String
name = many letter

age :: Parser Int
age = read <$> many digit
```

## 错误处理

### 期望与意外

```haskell
-- 尝试匹配但不消费输入
try :: Parser a -> Parser a

-- 示例：区分 + 和 -
expr = try (string "+-" >> return "plus minus")
       <|> (string "+" >> return "plus")
       <|> (string "-" >> return "minus")
```

### Lookahead

```haskell
lookAhead :: Parser a -> Parser a      -- 查看但不消费
lookAhead' :: Parser a -> Parser a     -- 严格版本
```

### 自定义错误

```haskell
unexpected :: String -> Parser a
unexpected "keyword" = unexpected "unexpected keyword"

<?> :: Parser a -> String -> Parser a  -- 期望标签
string "if" <?> "if keyword"
```

## Token 解析

使用 `Text.Parsec.Token` 简化词法分析：

```haskell
import Text.Parsec.Token
import Text.Parsec.Language (haskellDef)

-- 创建词法分析器
TokenParser { ident, reserved, symbol, ... } = makeTokenParser haskellDef

-- 使用
variable = do
    name <- ident
    if name `elem` reservedWords
        then unexpected "variable name"
        else return name
```

## Monad vs Applicative 解析

```haskell
-- Monad: 可以根据结果决定下一步
monadParser = do
    x <- token
    if condition x
        then parseA
        else parseB

-- Applicative: 确定性，不需要根据结果决定
applicativeParser = Person
    <$> name
    <*> (spaces *> int)
```

## 来源

- [[wiki/sources/rwh-chapter-16]] — 使用 Parsec 的完整指南

## 相关概念

- [[wiki/concepts/Monad变换器]] — Parsec 基于 State Monad
- [[wiki/concepts/Applicative]] — Parsec 也实现 Applicative
- [[wiki/concepts/错误处理]] — 解析错误处理
