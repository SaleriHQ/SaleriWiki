---
title: Either
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - haskell
  - error-handling
  - monad
sources: 1
---

## 定义

Either 是 Haskell 中表示**可能失败的操作**的数据类型。与 Maybe 不同，它可以携带**错误信息**。

```haskell
data Either a b = Left a | Right b
  deriving (Eq, Ord, Show)
```

| 构造器 | 用途 |
|--------|------|
| `Left a` | 表示错误（通常是 String 或自定义错误类型） |
| `Right b` | 表示成功，携带结果值 |

## 与 Maybe 的对比

| Maybe | Either |
|-------|--------|
| `Nothing` - 失败无信息 | `Left err` - 失败带错误信息 |
| `Just a` - 成功 | `Right a` - 成功 |

```haskell
-- Maybe：只知失败，不知原因
lookup :: Eq k => k -> [(k, v)] -> Maybe v

-- Either：失败时携带错误信息
lookup :: Eq k => k -> [(k, v)] -> Either String v
lookup _ [] = Left "Key not found"
lookup k ((k', v):kvs)
    | k == k'   = Right v
    | otherwise = lookup k kvs
```

## 基本用法

### 模式匹配

```haskell
case lookup "foo" dict of
    Right value -> putStrLn $ "Found: " ++ value
    Left err    -> putStrLn $ "Error: " ++ err
```

### 标准库函数

```haskell
-- 提取 Right 值
either :: (a -> c) -> (b -> c) -> Either a b -> c
either f _ (Left a)  = f a
either _ g (Right b) = g b

-- 将 Maybe 转为 Either
maybeToEither :: e -> Maybe a -> Either e a
maybeToEither _ (Just a) = Right a
maybeToEither e Nothing   = Left e
```

## Either 作为 Monad

```haskell
instance Monad (Either e) where
    return = Right
    (Left e)  >>= _ = Left e    -- 失败时短路
    (Right x) >>= f  = f x       -- 成功时继续

instance Functor (Either e) where
    fmap _ (Left e)  = Left e
    fmap f (Right x) = Right (f x)

instance Applicative (Either e) where
    pure = Right
    Left e  <*> _ = Left e
    Right f <*> r  = fmap f r
```

### Monad 实例的实用示例

```haskell
-- 链式错误处理
validateAge :: Int -> Either String Int
validateAge age
    | age < 0    = Left "Age cannot be negative"
    | age > 150  = Left "Age is unrealistic"
    | otherwise  = Right age

validateName :: String -> Either String String
validateName "" = Left "Name cannot be empty"
validateName n  = Right n

-- 使用 Monaddo
register :: String -> Int -> Either String (String, Int)
register name age = do
    validName <- validateName name
    validAge  <- validateAge age
    return (validName, validAge)
```

## 常用模式

### either 组合

```haskell
-- 优雅处理错误
handleResult :: Either String Int -> String
handleResult = either ("Error: " ++) show

handleResult (Right 42)  -- "42"
handleResult (Left "oops") -- "Error: oops"
```

### fromEither

```haskell
fromEither :: a -> Either e a -> a
fromEither _ (Right a) = a
fromEither def (Left _) = def
```

### partitionEithers

```haskell
-- 将 [Either a b] 分为成功和失败两组
partitionEithers :: [Either a b] -> ([a], [b])
partitionEithers = partitionEithers

-- 示例
inputs = [Right 1, Left "err1", Right 2, Left "err2"]
(successes, errors) = partitionEithers inputs
-- successes = [1, 2]
-- errors = ["err1", "err2"]
```

### 收集所有错误

```haskell
-- 使用 Validation 单子的库（如 Ehaskell）
-- 可以收集所有错误而不是短路
```

## 错误处理策略对比

| 策略 | 优点 | 缺点 |
|------|------|------|
| `Maybe` | 简单 | 无错误信息 |
| `Either e` | 带错误信息 | 只返回第一个错误 |
| `IO (Either e a)` | 可抛异常 | 混合副作用 |
| `Validation` | 收集所有错误 | 不是 Monad |

## 来源

- [[wiki/sources/rwh-chapter-19]] — 错误处理的完整讨论

## 相关概念

- [[wiki/concepts/Maybe]] — 无错误信息的失败
- [[wiki/concepts/单子]] — Either 是 Monad 实例
- [[wiki/concepts/纯函数]] — Either 保持纯度
