# CIS 194：第二次作业 — 代数数据类型

> **截止日期：** 1 月 28 日，星期一
> **提交文件：** `LogAnalysis.hs`

---

## 日志文件解析

日志文件 `error.log` 每行包含一条日志消息。每行开头有一个字符表示日志类型：

- `'I'` — 信息消息
- `'W'` — 警告消息
- `'E'` — 错误消息

错误消息行还有一个整数表示错误级别（1–100），1 表示"也许明年夏天会处理"的无关紧要错误，100 表示"灾难性重大故障"。所有类型的日志消息都有一个整数时间戳，后跟至行尾的文本内容。

### 数据类型

```haskell
data MessageType
    = Info
    | Warning
    | Error Int
    deriving (Show, Eq)

type TimeStamp = Int

data LogMessage
    = LogMessage MessageType TimeStamp String
    | Unknown String
    deriving (Show, Eq)
```

注意 `LogMessage` 有两个构造器：一个用于表示格式正常的日志消息，另一个（`Unknown`）用于表示任何不符合格式的内容。

### 练习 1 — `parseMessage`

定义一个函数，解析日志文件中的单行内容：

```haskell
parseMessage :: String -> LogMessage
```

**示例：**

```haskell
parseMessage "E 2 562 help help"
    == LogMessage (Error 2) 562 "help help"

parseMessage "I 29 la la la"
    == LogMessage Info 29 "la la la"

parseMessage "This is not in the right format"
    == Unknown "This is not in the right format"
```

再定义一个函数，解析整个日志文件：

```haskell
parse :: String -> [LogMessage]
```

使用 `read`、`lines`、`words`、`unwords`、`take`、`drop` 和函数复合（`.`）—— 不要重复造轮子！

---

## 将日志排序

由于多台服务器、闪电风暴、磁盘故障和一个无聊又不称职的程序员的共同作用，日志消息的顺序完全乱了。在整理之前，根本无法理清发生了什么。我们设计了一个数据结构来帮助处理——日志消息的二叉搜索树：

```haskell
data MessageTree = Leaf
    | Node MessageTree LogMessage MessageTree
```

`MessageTree` 是递归数据类型：`Node` 构造器本身接受两个子节点（左、右子树）和一个 `LogMessage`。`Leaf` 表示空树。

`MessageTree` 按时间戳排序：任何 `Node` 中的 `LogMessage` 的时间戳应大于左子树中所有消息的时间戳，并小于右子树中所有消息的时间戳。`Unknown` 消息**不应**存储在 `MessageTree` 中，因为它们没有时间戳。

### 练习 2 — `insert`

```haskell
insert :: LogMessage -> MessageTree -> MessageTree
```

将一个新的 `LogMessage` 插入现有的有序 `MessageTree`，返回一个新的有序 `MessageTree`。如果消息是 `Unknown`，则返回树本身不变。

### 练习 3 — `build`

```haskell
build :: [LogMessage] -> MessageTree
```

通过依次插入（从 `Leaf` 开始），从消息列表构建完整的 `MessageTree`。

### 练习 4 — `inOrder`

```haskell
inOrder :: MessageTree -> [LogMessage]
```

接收一个有序的 `MessageTree`，返回其中所有 `LogMessage` 按时间戳从小到大排列的列表。（这就是二叉树的中序遍历。）

用以下表达式排序并过滤掉未知消息：

```haskell
inOrder (build tree)
```

> 注意：排序列表有更好的方法；这里只是练习递归数据结构的题目！

---

## 事后分析

### 练习 5 — `whatWentWrong`

"相关"定义为"严重级别至少为 50 的错误"。

```haskell
whatWentWrong :: [LogMessage] -> [String]
```

接收一个**未排序**的 `LogMessage` 列表，返回所有严重级别 ≥ 50 的错误消息文本，按时间戳排序。

**示例：**

给定以下日志文件：

```
I 6 Completed armadillo processing
I 1 Nothing to report
E 99 10 Flange failed!
I 4 Everything normal
I 11 Initiating self-destruct sequence
E 70 3 Way too many pickles
E 65 8 Bad pickle-flange interaction detected
W 5 Flange is due for a check-up
I 7 Out for lunch, back in two time steps
E 20 2 Too many pickles
I 9 Back from lunch
```

`whatWentWrong` 的输出应为：

```haskell
[ "Way too many pickles"
, "Bad pickle-flange interaction detected"
, "Flange failed!"
]
```

---

## 注意事项

- 我们会用你们没有见过的日志文件测试你的解决方案，所以**不要硬编码！**
- 我们鼓励（事实上非常鼓励）你和同学讨论作业，但必须自己动手写代码。

---

## 尾声

### 练习 6（选做）

由于种种原因，我们开始怀疑这场混乱是由一个自大的黑客引起的。你能找到是谁干的吗？
