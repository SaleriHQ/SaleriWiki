---
title: Maybe 类型
created: 2026-04-10
updated: 2026-04-10
tags:
  - concept
  - haskell
  - type-system
sources: 1
related:
  - "[[wiki/sources/cis194-lecture3-rec-poly]]"
  - "[[wiki/concepts/全函数与偏函数]]"
  - "[[wiki/concepts/代数数据类型]]"
---

# Maybe 类型

## 定义

`Maybe` 是 Haskell 中表示"可能不存在值"的类型：

```haskell
data Maybe a = Nothing | Just a
  deriving (Eq, Show)
```

| 构造器 | 含义 |
|--------|------|
| `Nothing` | 表示"没有值"（失败、缺失、不适用） |
| `Just x`  | 表示"有一个值 x" |

## 常见用法

### 安全替代偏函数

```haskell
safeHead    :: [a] -> Maybe a    -- head 的安全版
safeDiv     :: Double -> Double -> Maybe Double
safeIndex   :: [a] -> Int -> Maybe a  -- (!!) 的安全版
lookup      :: Eq k => k -> [(k, v)] -> Maybe v
```

### 可选配置

```haskell
data Config = Config
  { port     :: Maybe Int
  , host     :: Maybe String
  , debug    :: Maybe Bool
  }

-- 使用默认值
getPort :: Config -> Int
getPort cfg = fromMaybe 8080 (port cfg)  -- 8080 作为默认值
```

## Maybe 的处理

### 模式匹配

```haskell
showMaybe :: Maybe Int -> String
showMaybe Nothing  = "没有值"
showMaybe (Just n) = "值为: " ++ show n
```

### do 语法（用于嵌套 Maybe）

```haskell
combineMaybe :: Maybe Int -> Maybe Int -> Maybe Int
combineMaybe mx my = do
  x <- mx
  y <- my
  return (x + y)
```

### 函数组合

```haskell
-- 用 (>>=) 链式处理
safeHead "hello" >>= safeTail >>= safeHead
-- Nothing 会在链中短路，最终返回 Nothing

-- 用 (<$>) 和 (<*>) 处理列表
(++) <$> safeHead "hello" <*> safeHead "world"
-- Just "hw"
```

## 与其他语言的类比

| 语言 | 对应概念 |
|------|---------|
| Java | `Optional<T>` |
| Rust | `Option<T>` |
| Swift | `Optional<T>` |
| Python | `None`（但无类型安全） |
| Kotlin | `T?`（空安全） |

## 来源

- [[wiki/sources/cis194-lecture3-rec-poly]] — Maybe 的引入，作为偏函数的安全替代方案

## 相关概念

- [[wiki/concepts/全函数与偏函数]] — Maybe 如何使偏函数变为全函数
- [[wiki/concepts/代数数据类型]] — Maybe 的定义方式
