---
title: Monad 变换器
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - haskell
  - monad
  - transformer
  - mtl
sources: 1
---

## 动机

Monad 提供了一种构建带效果计算的强大方式。但在实际代码中，我们经常需要**同时使用多种效果**。

例如：
- 解析器：需要 State（跟踪位置）+ Either（可能失败）
- 文件扫描器：需要 IO（访问文件系统）+ Writer（记录结果）

## 什么是 Monad 变换器

Monad 变换器类似于常规 Monad，但它是**修改底层 Monad 行为**的包装器。

```
┌─────────────────────────────┐
│    WriterT w m a            │  ← 添加"记录"能力
├─────────────────────────────┤
│    StateT s m a            │  ← 添加"可变状态"能力
├─────────────────────────────┤
│    ReaderT r m a           │  ← 添加"只读环境"能力
├─────────────────────────────┤
│    IO a                    │  ← 底层 Monad（通常是 IO）
└─────────────────────────────┘
```

## 常用变换器

| 变换器 | 添加的效果 | 底层 Monad |
|--------|-----------|-----------|
| `StateT s m a` | 可变状态 | `m` |
| `ReaderT r m a` | 只读环境 | `m` |
| `WriterT w m a` | 记录日志 | `m` |
| `MaybeT m a` | 可能失败 | `m` |
| `ExceptT e m a` | 错误处理 | `m` |

## 命名约定

- Monad: `State s a`
- 变换器: `StateT s m a`（多一个类型参数 `m`）
- `T` = Transformer

```haskell
-- State Monad
get :: State s s
put :: s -> State s ()

-- StateT Transformer
get :: Monad m => StateT s m s
put :: Monad m => s -> StateT s m ()
```

## 基本示例：WriterT on IO

```haskell
import Control.Monad.Writer
import Control.Monad.Trans

-- 记录日志的 IO 动作
type LogIO = WriterT [String] IO ()

logMsg :: String -> LogIO
logMsg msg = tell [msg]

program :: LogIO
program = do
    logMsg "Starting..."
    liftIO $ putStrLn "Enter your name:"
    name <- liftIO getLine
    logMsg $ "User entered: " ++ name
    logMsg "Done!"

main :: IO ()
main = do
    ((), logs) <- runWriterT program
    mapM_ putStrLn logs
```

## lift 操作

`lift` 将底层 Monad 的动作提升到变换器层：

```haskell
import Control.Monad.Trans (liftIO)

program :: ReaderT Config (StateT State IO) ()
program = do
    config <- ask                    -- ReaderT 操作
    modify (\s -> s { count = 1 })  -- StateT 操作
    liftIO $ putStrLn "Hello"       -- IO 操作
    -- liftIO = lift . lift (两层变换器)
```

## Monad 类型类

mtl 库为每个变换器提供类型类：

```haskell
-- MonadReader: ask, local
class Monad m => MonadReader r m | m -> r where
    ask   :: m r
    local :: (r -> r) -> m a -> m a

-- MonadState: get, put
class Monad m => MonadState s m | m -> s where
    get :: m s
    put :: s -> m ()

-- MonadWriter: tell, listen
class (Monoid w, Monad m) => MonadWriter w m | m -> w where
    tell :: w -> m ()
    listen :: m a -> m (a, w)
```

## 堆叠多个变换器

```haskell
type AppM = ReaderT Config        -- 只读配置
              (StateT AppState    -- 可变状态
                (WriterT [String] -- 日志
                  IO))            -- IO

-- 运行堆叠
runApp :: Config -> AppState -> AppM a -> IO (a, AppState, [String])
runApp config state action =
    runWriterT $ runStateT (runReaderT action config) state
```

## 常用函数

### 执行函数

```haskell
runStateT  :: StateT s m a -> s -> m (a, s)
runReaderT :: ReaderT r m a -> r -> m a
runWriterT :: WriterT w m a -> m (a, w)
evalStateT :: StateT s m a -> s -> m a      -- 只返回结果
execWriterT :: WriterT w m a -> m w         -- 只返回日志
```

### 升降 Monad

```haskell
-- lift: 将内层 Monad 动作提升到外层
lift :: (MonadTrans t, Monad m) => m a -> t m a

-- liftIO: 将 IO 动作提升（需要 MonadIO）
liftIO :: MonadIO m => IO a -> m a
```

## MonadIO

对于任意 Monad 变换器堆叠，可以使用 `MonadIO` 统一提升 IO：

```haskell
class MonadIO m where
    liftIO :: IO a -> m a

-- 自动实例
instance MonadIO IO where liftIO = id
instance MonadIO (ReaderT r m) where liftIO = lift . liftIO
instance MonadIO (StateT s m) where liftIO = lift . liftIO
```

## 来源

- [[wiki/sources/rwh-chapter-18]] — Monad 变换器的完整介绍

## 相关概念

- [[wiki/concepts/单子]] — Monad 基础
- [[wiki/concepts/IO Monad]] — IO 是基础
- [[wiki/concepts/Writer]] — Writer Monad
- [[wiki/concepts/Reader]] — Reader Monad
- [[wiki/concepts/State]] — State Monad
