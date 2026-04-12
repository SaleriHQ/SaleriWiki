---
title: Applicative
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - haskell
  - functor
  - functor
  - typeclass
sources: 0
---

## 定义

Applicative 是位于 **Functor** 和 **Monad** 之间的类型类。它允许在上下文中应用函数。

```haskell
class Functor f => Applicative f where
    pure  :: a -> f a              -- 将值放入上下文
    (<*>) :: f (a -> b) -> f a -> f b  -- 应用上下文中的函数
```

## 类型类层次

```
Functor      (<$>)    -- 映射
    ↓
Applicative  (<*>)   -- 应用包装的函数
    ↓
Monad        (>>=)   -- 链式计算
```

## Applicative 的核心操作

### pure

将普通值放入 Applicative 上下文：

```haskell
pure 3 :: Maybe Int       -- Just 3
pure 3 :: [Int]           -- [3]
pure (+1) :: IO (Int -> Int)  -- IO 动作（惰性）
```

### <*>

应用包装在上下文中的函数：

```haskell
Just (+1) <*> Just 3      -- Just 4
Nothing   <*> Just 3      -- Nothing
Just (+1) <*> Nothing    -- Nothing

[(*2), (+3)] <*> [1, 2]  -- [2, 4, 3, 5]
```

## 与 Functor 的对比

```haskell
-- Functor: 只能映射单个值
fmap (+1) (Just 3)      -- Just 4
(+1) <$> (Just 3)       -- Just 4

-- Applicative: 可以应用多个参数
pure (+1) <*> Just 3    -- Just 4

-- 更实际的例子：应用两个参数的函数
pure (+) <*> Just 3 <*> Just 5  -- Just 8
pure (+) <*> Nothing  <*> Just 5  -- Nothing
```

## 与 Monad 的对比

```haskell
-- Monad: 可以根据前一个结果决定下一个动作
getLine >>= \name -> putStrLn ("Hello, " ++ name)

-- Applicative: 不能根据值决定
-- （适合并行/确定性场景）
validate name = Name <$> checkLength name <*> checkChars name
```

## 常用 Applicative 实例

### Maybe

```haskell
instance Applicative Maybe where
    pure = Just
    Just f  <*> Just x = Just (f x)
    _       <*> _       = Nothing
```

### IO

```haskell
instance Applicative IO where
    pure = return
    iof <*> ix = do
        f <- iof
        x <- ix
        return (f x)
```

### 列表

```haskell
instance Applicative [] where
    pure x = [x]
    fs <*> xs = [f x | f <- fs, x <- xs]
```

## 实用模式

### liftA2 / liftA3

```haskell
-- 提升二元函数
liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
liftA2 f x y = f <$> x <*> y

-- 示例
liftA2 (+) (Just 3) (Just 5)  -- Just 8
liftA2 (:) (Just 'a') (Just "bc")  -- Just "abc"
```

### 条件 Applicative

```haskell
-- (<|>) 来自 Alternative
instance Alternative Maybe where
    empty = Nothing
    Nothing <|> y = y
    x       <|> _ = x
```

### 解析器

```haskell
--Applicative 风格的解析器
data Parser a = Parser { runParser :: String -> [(a, String)] }

instance Applicative Parser where
    pure x = Parser $ \s -> [(x, s)]
    Parser f <*> Parser p = Parser $ \s ->
        [(x, s2) | (g, s1) <- f s, (x, s2) <- p s1]
```

## Applicative 定律

| 定律 | 说明 |
|------|------|
| `pure id <*> v = v` | 身份 |
| `pure (.) <*> u <*> v <*> w = u <*> (v <*> w)` | 组合 |
| `pure f <*> pure x = pure (f x)` | 同态 |
| `u <*> pure y = pure ($ y) <*> u` | 交换 |

## 使用场景

| 场景 | 推荐 |
|------|------|
| 验证（可选参数） | Applicative ✓ |
| 并行计算 | Applicative ✓ |
| 依赖结果的计算 | Monad ✗ |
| 错误处理 | Either Monad |

## 来源

- [[wiki/sources/rwh-chapter-14]] — Monad 的介绍

## 相关概念

- [[wiki/concepts/Functor]] — Applicative 的基础
- [[wiki/concepts/单子]] — Applicative 的超集
- [[wiki/concepts/Maybe]] — Maybe 是 Applicative 实例
