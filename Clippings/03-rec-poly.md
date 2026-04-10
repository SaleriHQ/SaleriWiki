---
title: "03-rec-poly"
source: "https://www.seas.upenn.edu/~cis1940/spring13/lectures/03-rec-poly.html"
author:
published:
created: 2026-04-10
description: 递归模式、多态与 Prelude
tags:
  - "clippings"
  - haskell
  - recursion
  - polymorphism
---

# 递归模式、多态与 Prelude

在完成作业 2 的过程中，你可能花了大量时间编写显式的递归函数。到这里，你可能会认为这就是 Haskell 程序员大部分时间在做的事情。实际上，**有经验的 Haskell 程序员几乎从不写递归函数**！

这是怎么做到的呢？关键在于，虽然递归函数在理论上几乎可以做任何事情，但在实践中，某些常见的模式会反复出现。通过将这些模式抽象成库函数，程序员可以将递归的低层细节交给这些函数处理，从而在更高层次上思考问题——这就是**全粒度编程（wholemeal programming)** 的目标。

## 递归模式

回顾一下我们之前定义的 `Int` 值列表：

```haskell
data IntList = Empty | Cons Int IntList
  deriving Show
```

对于 `IntList`，我们可能想做哪些事情？以下是一些常见的可能性：

- 对列表中的每个元素执行某种操作
- 根据某个条件保留列表中的某些元素，丢弃其他元素
- 以某种方式"汇总"列表中的元素（求和、求积、找最大值……）
- 你可能还能想到其他！

### Map（映射）

让我们思考第一个（"对列表中的每个元素执行某种操作"）。例如，我们可以给列表中的每个元素加一：

```haskell
addOneToAll :: IntList -> IntList
addOneToAll Empty       = Empty
addOneToAll (Cons x xs) = Cons (x + 1) (addOneToAll xs)
```

或者我们可以取绝对值，确保列表中的每个元素都是非负的：

```haskell
absAll :: IntList -> IntList
absAll Empty       = Empty
absAll (Cons x xs) = Cons (abs x) (absAll xs)
```

或者，我们可以对每个元素求平方：

```haskell
squareAll :: IntList -> IntList
squareAll Empty       = Empty
squareAll (Cons x xs) = Cons (x*x) (squareAll xs)
```

此时，你脑海中应该警铃大作！这三个函数看起来太相似了。应该有一种方法能够抽象出它们的共同点，这样我们就不用重复自己！

确实有这种方法——你能想出来吗？在这三个例子中，哪些部分相同，哪些部分会变化？

会变化的部分，当然是我们想要对每个元素执行的操作。我们可以将这个操作指定为一个类型为 `Int -> Int` 的**函数**。这里我们开始看到，能够将函数作为输入传递给其他函数是多么有用！

```haskell
mapIntList :: (Int -> Int) -> IntList -> IntList
mapIntList _ Empty       = Empty
mapIntList f (Cons x xs) = Cons (f x) (mapIntList f xs)
```

现在我们可以用 `mapIntList` 来实现 `addOneToAll`、`absAll` 和 `squareAll`：

```haskell
exampleList = Cons (-1) (Cons 2 (Cons (-6) Empty))

addOne x = x + 1
square x = x * x

mapIntList addOne exampleList
mapIntList abs    exampleList
mapIntList square exampleList
```

### Filter（过滤）

另一种常见的模式是：我们只想根据某个测试保留列表中的某些元素，丢弃其他元素。例如，我们可能只想保留正数：

```haskell
keepOnlyPositive :: IntList -> IntList
keepOnlyPositive Empty           = Empty
keepOnlyPositive (Cons x xs)
  | x > 0      = Cons x (keepOnlyPositive xs)
  | otherwise  = keepOnlyPositive xs
```

或者只想保留偶数：

```haskell
keepOnlyEven :: IntList -> IntList
keepOnlyEven Empty = Empty
keepOnlyEven (Cons x xs)
  | even x    = Cons x (keepOnlyEven xs)
  | otherwise = keepOnlyEven xs
```

我们怎样才能推广这个模式？什么保持不变，我们需要抽象出什么？

```haskell
filterIntList :: (Int -> Bool) -> IntList -> IntList
filterIntList _ Empty = Empty
filterIntList p (Cons x xs)
  | p x       = Cons x (filterIntList p xs)
  | otherwise = filterIntList p xs
```

### Fold（折叠）

我们提到的最后一个模式是"汇总"列表中的元素；这也常被称为"折叠"或"归约"操作。我们下周会回来讨论这个。同时，你可能想思考一下如何抽象出这个模式！

## 多态（Polymorphism）

我们现在已经为 `Int` 列表编写了一些漂亮的、通用的映射和过滤函数。但我们还没有完成泛化！如果我们想要过滤 `Integer` 列表呢？或者 `Bool` 列表？或者列表的列表、树的栈的 `String` 列表？我们必须为每种情况创建新的数据类型和新的函数。更糟糕的是，**代码会完全相同**；唯一不同的是**类型签名**。Haskell 能帮助我们吗？

当然可以！Haskell 支持数据类型和函数的**多态**。"多态的"这个词来自希腊语（πολύμορφος），意思是"有多种形式"：多态的东西可以适用于多种类型。

### 多态数据类型

首先，让我们看看如何声明一个多态数据类型。

```haskell
data List t = E | C t (List t)
```

（我们不能重用 `Empty` 和 `Cons`，因为它们已经被用于 `IntList` 的构造器了，所以我们改用 `E` 和 `C`。）之前我们写的是 `data IntList = ...`，现在我们写 `data List t = ...`。`t` 是一个**类型变量**，可以代表任何类型。（类型变量必须以小写字母开头，而类型必须以大写字母开头。）`data List t = ...` 意味着 `List` 类型是由一个类型**参数化**的，这与函数可以被某些输入参数化的方式非常相似。

给定一个类型 `t`，`(List t)` 要么是构造器 `E`，要么是构造器 `C` 加上一个类型为 `t` 的值和另一个 `(List t)`。以下是一些例子：

```haskell
lst1 :: List Int
lst1 = C 3 (C 5 (C 2 E))

lst2 :: List Char
lst2 = C 'x' (C 'y' (C 'z' E))

lst3 :: List Bool
lst3 = C True (C False E)
```

### 多态函数

现在，让我们把 `filterIntList` 推广到我们新的多态 `List` 上。我们可以直接取 `filterIntList` 的代码，把 `Empty` 换成 `E`，把 `Cons` 换成 `C`：

```haskell
filterList :: (t -> Bool) -> List t -> List t
filterList _ E = E
filterList p (C x xs)
  | p x       = C x (filterList p xs)
  | otherwise = filterList p xs
```

现在，`filterList` 的类型是什么？让我们看看 ghci 推断出的类型：

```
*Main> :t filterList
filterList :: (t -> Bool) -> List t -> List t
```

我们可以这样理解："对于任何类型 `t`，`filterList` 接受一个从 `t` 到 `Bool` 的函数，以及一个 `t` 的列表，并返回一个 `t` 的列表。"

那么，如何推广 `mapIntList`？对于一个将函数应用于 `List t` 中每个元素的函数 `mapList`，应该给它什么类型？

我们的第一个想法可能是给它类型：

```haskell
mapList :: (t -> t) -> List t -> List t
```

这可以工作，但这意味着应用 `mapList` 时，我们总是得到一个与起始列表元素类型相同的列表。这过于限制了：我们希望能做一些事情，比如 `mapList show`，比如把一个 `Int` 列表转换成 `String` 列表。因此，这是 `mapList` 最通用的类型，以及它的实现：

```haskell
mapList :: (a -> b) -> List a -> List b
mapList _ E        = E
mapList f (C x xs) = C (f x) (mapList f xs)
```

关于多态函数，需要记住的一个重要一点是：**调用者选择类型**。当你写一个多态函数时，它必须适用于每一种可能的输入类型。这——连同 Haskell 无法直接根据类型做出决策这一事实——会产生一些有趣的影响，我们稍后会探讨。

## Prelude

`Prelude` 是一个包含大量标准定义的模块，它会被隐式导入到每个 Haskell 程序中。值得花些时间[浏览其文档](http://haskell.org/ghc/docs/latest/html/libraries/base/Prelude.html)，熟悉可用的工具。

当然，多态列表在 `Prelude` 中有定义，还有[许多用于处理它们的有用的多态函数](http://haskell.org/ghc/docs/latest/html/libraries/base/Prelude.html#11)。例如，`filter` 和 `map` 就是我们 `filterList` 和 `mapList` 的对应物。事实上，[`Data.List` 模块包含更多列表函数](http://www.haskell.org/ghc/docs/latest/html/libraries/base/Data-List.html)。

另一个有用的多态类型是 `Maybe`，定义如下：

```haskell
data Maybe a = Nothing | Just a
```

类型为 `Maybe a` 的值要么包含一个类型为 `a` 的值（包装在 `Just` 构造器中），要么是 `Nothing`（表示某种失败或错误）。[`Data.Maybe` 模块有处理 `Maybe` 值的函数](http://www.haskell.org/ghc/docs/latest/html/libraries/base/Data-Maybe.html)。

## 全函数与偏函数

考虑这个多态类型：

```haskell
[a] -> a
```

什么函数可以有这种类型？类型说的是：给定一个类型为 `a` 的元素的列表，函数必须产生某个类型为 `a` 的值。例如，Prelude 函数 `head` 就有这个类型。

……但如果给 `head` 一个空列表作为输入会发生什么？让我们看看 `head` 的[源代码](http://www.haskell.org/ghc/docs/latest/html/libraries/base/src/GHC-List.html#head)……

它崩溃了！它不可能做其他事情，因为它必须适用于**所有**类型。没有办法凭空制造出一个任意类型的元素。

`head` 被称为**偏函数（partial function）**：对于某些输入，`head` 会崩溃。如果函数在某些输入下会无限递归，也被称为偏函数。在所有可能的输入上都有良好定义的函数被称为**全函数（total functions）**。

尽可能避免偏函数是好的 Haskell 实践。实际上，在任何编程语言中避免偏函数都是好的实践——但在大多数语言中，这会非常麻烦。Haskell 倾向于让它变得相当容易和合理。

**`head` 是一个错误！** 它不应该在 `Prelude` 中。你几乎永远不应该使用的其他偏函数包括 `tail`、`init`、`last` 和 `(!!)`。从现在开始，在作业中使用这些函数之一会扣风格分！

该怎么办？

### 替换偏函数

像 `head`、`tail` 等偏函数通常可以用模式匹配来替代。考虑以下两个定义：

```haskell
doStuff1 :: [Int] -> Int
doStuff1 []  = 0
doStuff1 [_] = 0
doStuff1 xs  = head xs + (head (tail xs))
```

```haskell
doStuff2 :: [Int] -> Int
doStuff2 []        = 0
doStuff2 [_]       = 0
doStuff2 (x1:x2:_) = x1 + x2
```

这些函数计算出完全相同的结果，而且都是全函数。但只有第二个是**明显全函数的**，而且它本来就更容易阅读。

### 编写偏函数

如果你发现自己**正在编写**一个偏函数该怎么办？有两种方法。第一种是改变函数的输出类型来表明可能的失败。回顾 `Maybe` 的定义：

```haskell
data Maybe a = Nothing | Just a
```

现在，假设我们正在编写 `head`。我们可以这样安全地重写它：

```haskell
safeHead :: [a] -> Maybe a
safeHead []    = Nothing
safeHead (x:_) = Just x
```

实际上，在 [`safe` 包](http://hackage.haskell.org/package/safe)中确实定义了这样的函数。

为什么这是一个好主意？

1. `safeHead` 永远不会崩溃。
2. `safeHead` 的类型明确表示它可能会对某些输入失败。
3. 类型系统确保 `safeHead` 的用户必须适当检查 `safeHead` 的返回值，以确定他们得到的是值还是 `Nothing`。

从某种意义上说，`safeHead` 仍然是"偏的"；但我们已经在类型系统中反映了这种偏性，所以现在是安全的。目标是让类型尽可能多地告诉我们关于函数行为的信息。

好吧，但如果我们知道我们只会在**保证**有非空列表的情况下使用 `head` 呢？在这种情况下，返回 `Maybe a` 真的很烦人，因为我们必须付出努力来处理一个我们"知道"实际上不会发生的情况。

答案是：如果某个条件真的是**保证的**，那么类型应该反映这种保证！这样编译器就可以为你执行保证。例如：

```haskell
data NonEmptyList a = NEL a [a]

nelToList :: NonEmptyList a -> [a]
nelToList (NEL x xs) = x:xs

listToNel :: [a] -> Maybe (NonEmptyList a)
listToNel []     = Nothing
listToNel (x:xs) = Just $ NEL x xs

headNEL :: NonEmptyList a -> a
headNEL (NEL a _) = a

tailNEL :: NonEmptyList a -> [a]
tailNEL (NEL _ as) = as
```

你可能认为这样做只是给不是超级天才的笨蛋准备的。当然，*你*永远不会犯把空列表传递给只期望非空列表的函数这种错误，对吧？好吧，确实有个笨蛋参与了，但不是你想象的那个。

---

*翻译于 2013-03-14 14:39:58*
