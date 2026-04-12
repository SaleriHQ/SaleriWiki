---
title: IO Monad
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - haskell
  - monad
  - io
  - side-effect
sources: 1
---

## 定义

IO Monad 是 Haskell 中处理**副作用**的机制。所有与外部世界的交互（读取文件、网络通信、打印输出）都必须通过 IO 类型进行。

```haskell
main :: IO ()
main = putStrLn "Hello, World!"
```

## IO 类型

```haskell
getLine :: IO String        -- 从 stdin 读取一行
putStrLn :: String -> IO () -- 输出字符串
readFile :: FilePath -> IO String
writeFile :: FilePath -> String -> IO ()
```

### IO 的本质

| 特性 | 说明 |
|------|------|
| `IO a` | 一个产生 `a` 值的 I/O 动作 |
| `IO ()` | 执行副作用但无返回值（类似 `void`） |
| 执行 | 动作只能从 `main` 或另一个 IO 动作内执行 |

## do 语法

```haskell
main :: IO ()
main = do
    putStrLn "What is your name?"
    name <- getLine           -- <- 从动作中提取结果
    let greeting = "Hello, " ++ name  -- let 用于纯代码
    putStrLn greeting
```

### `<-` vs `let`

| 语法 | 用途 | 示例 |
|------|------|------|
| `<-` | 从 IO 动作获取结果 | `name <- getLine` |
| `let` | 绑定纯表达式 | `let x = 1 + 2` |

## 纯代码与 IO 的对比

| 纯代码 | IO 动作 |
|--------|---------|
| 相同输入 → 相同输出 | 可能每次不同 |
| 无副作用 | 有副作用 |
| 可自由求值/重排序 | 必须按顺序执行 |
| 可缓存结果 | 不可缓存 |

## 为什么需要 IO Monad

### 1. 副作用隔离

```haskell
-- 纯函数：无副作用
process :: String -> String
process s = map toUpper s  -- 总是产生相同结果

-- IO 动作：可以读取文件
processFile :: IO String
processFile = readFile "input.txt"
```

### 2. 保持引用透明性

```haskell
-- 即使代码看起来"相同"，IO 结果也可能不同
result1 <- readFile "data.txt"  -- 第一次读取
result2 <- readFile "data.txt"  -- 第二次读取（文件可能已修改）
```

### 3. 允许编译器优化

- 纯代码可以被重排序、并行化
- IO 边界清晰，优化受限

## IO 作为 Monad

IO 是 Monad 接口的实现：

```haskell
instance Monad IO where
    (>>=)  :: IO a -> (a -> IO b) -> IO b
    (>>)   :: IO a -> IO b -> IO b
    return :: a -> IO a
```

## 常用 IO 函数

### 文件操作

```haskell
-- 读取
contents <- readFile "file.txt"

-- 写入
writeFile "out.txt" "content"

-- 追加
appendFile "log.txt" "new entry\n"
```

### 命令行参数

```haskell
import System.Environment (getArgs)

main :: IO ()
main = do
    args <- getArgs
    case args of
        [input, output] -> processFiles input output
        _              -> putStrLn "Usage: prog <input> <output>"
```

### 环境变量

```haskell
import System.Environment (getEnv)

main :: IO ()
main = do
    home <- getEnv "HOME"
    putStrLn $ "Home directory: " ++ home
```

## 来源

- [[wiki/sources/rwh-chapter-07]] — Haskell 中的经典 I/O

## 相关概念

- [[wiki/concepts/Maybe]] — 无值的情况
- [[wiki/concepts/单子]] — IO 是 Monad 的实例
- [[wiki/concepts/纯函数]] — 纯代码 vs IO
