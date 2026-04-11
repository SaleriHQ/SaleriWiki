---
title: "十分钟学会 Haskell"
source: "https://wiki.haskell.org/Cn/%E5%8D%81%E5%88%86%E9%92%9F%E5%AD%A6%E4%BC%9A_Haskell"
author: "Haskell Wiki"
created: 2026-04-07
type: clipping
category: haskell
description: "Haskell 语言快速入门教程"
tags:
  - clippings
  - haskell
  - tutorial
  - quickstart
---
## 概要

Haskell 是函数式（一切通过函数调用来完成）、静态、隐式类型（ [类型](https://wiki.haskell.org/index.php?title=Type "Type") 由编译器检测，类型声明不是必需的）、惰性（除非必要，否则什么也不做）的语言。其最大众化的近亲大概是 ML 族语言（不过不是惰性的）。

最流行(common)的 Haskell 编译器是 [GHC](https://wiki.haskell.org/index.php?title=GHC "GHC") ， [下载地址](http://www.haskell.org/ghc/download_ghc_661.html) 。GHC 在 [GNU/Linux](https://wiki.haskell.org/index.php?title=GNU/Linux "GNU/Linux"), [FreeBSD](https://wiki.haskell.org/index.php?title=BSD "BSD"), [MacOS](https://wiki.haskell.org/index.php?title=Mac_OS_X "Mac OS X"), [Windows](https://wiki.haskell.org/index.php?title=Windows "Windows") 以及 [Solaris](https://wiki.haskell.org/index.php?title=Solaris&action=edit&redlink=1 "Solaris (page does not exist)") 平台上都有可供使用的二进制包。安装 GHC，即获得 ghc 和 。前者用于将 Haskell 程序库或应用程序编译成二进制码。后者为解释器，可在编写 Haskell 代码后立即得到反馈.

## 表达式

大部份数学表达式都可以输入 ghci 直接解答。 Prelude> 是 GHCi 默认提示符。

```
Prelude> 3 * 5
 15
 Prelude> 4 ^ 2 - 1
 15
 Prelude> (1 - 5)^(3 * 2 - 4)
 16
```

字符串需要双引号引用，以 `++` 连接。

```
Prelude> "Hello"
 "Hello"
 Prelude> "Hello" ++ ", Haskell"
 "Hello, Haskell"
```

调用函数时，参数紧接 [函数](https://wiki.haskell.org/index.php?title=Function "Function") 即可，其间无须添加括号。

```
Prelude> succ 5
 6
 Prelude> truncate 6.59
 6
 Prelude> round 6.59
 7
 Prelude> sqrt 2
 1.4142135623730951
 Prelude> not (5 < 3)
 True
 Prelude> gcd 21 14
 7
```

## 控制台

调用 [I/O actions](https://wiki.haskell.org/index.php?title=Introduction_to_IO "Introduction to IO") 进行控制台输入和输出。如：

```
Prelude> putStrLn "Hello, Haskell"
 Hello, Haskell
 Prelude> putStr "No newline"
 No newlinePrelude> print (5 + 4)
 9
 Prelude> print (1 < 2)
 True
```

`putStr` 和 `putStrLn` 输出字符串到终端。 `print` 输出任意类型的值。（如果 `print` 作用于字符串，输出将用引号引用。)

复杂的 I/O acttions 需要 `do` 语句块，以分号间隔。

```
Prelude> do { putStr "2 + 2 = " ; print (2 + 2) }
 2 + 2 = 4
 Prelude> do { putStrLn "ABCDE" ; putStrLn "12345" }
 ABCDE
 12345
```

通过 `getLine` （返回字符串）或 `readLn` （返回任意你需要的类型）获得输入。用 `<-` 符号给 I/O action 的结果命名。

```
Prelude> do { n <- readLn ; print (n^2) }
 4
 16
```

（4 是输入。16 是结果。）

`do` 语句块的另一种方式，以缩进取代花括号和分号。虽然在 ghci 中未能获得完美支持，但是可以把它们塞进源文件（如 Test.hs ）里然后编译：

```
main = do putStrLn "What is 2 + 2?"
          x <- readLn
          if x == 4
              then putStrLn "You're right!"
              else putStrLn "You're wrong!"
```

运行 ghc --make Test.hs，得到 Test（ [Windows](https://wiki.haskell.org/index.php?title=Windows "Windows") 上是 Test.exe）。顺便接触了 if 语句。

do 之后首个非空白字符，如上例 `putStrLn` 的 p，是特别的。每新起一行，行首与之对齐，即视为同一 do 块之新句；缩进较之多则继续前句；较之少则结束此 do 块。是为页面布局（layout），Haskell 以之回避语句结束标记和花括号。（故then 和 else 子句务必缩进，否则将脱离 if 语句，导致错误。）

（注意：切勿使用制表符。从技术上讲，八格制表符可以正常工作，但不是个好主意。也不要使用非等宽字体——显然，有些人在编程的时候会犯此糊涂！）

## 类型

到目前为止，我们一直没有提到过类型声明。那是因为 Haskell 暗中推断，不必声明之。如果非要声明类型，可用 `::` 符号明确指出，如：

```
Prelude> 5 :: Int
 5
 Prelude> 5 :: Double
 5.0
```

类型 [types](https://wiki.haskell.org/index.php?title=Type "Type") （以及类型类 type [classes](https://wiki.haskell.org/index.php?title=Class&action=edit&redlink=1 "Class (page does not exist)") ，稍后提及）总是以大写开头。变量（variables）总是以小写开头。这是语言规则，而不只是 [命名习惯](https://wiki.haskell.org/index.php?title=Study_captials&action=edit&redlink=1 "Study captials (page does not exist)") 。

你也可以让 ghci 告诉你选择的内容的类型，这种方法很有用，因为类型声明并不是必需的。

```
Prelude> :t True
 True :: Bool
 Prelude> :t 'X'
 'X' :: Char
 Prelude> :t "Hello, Haskell"
 "Hello, Haskell" :: [Char]
```

(在这个例子中， `[Char]` 是 `String` 的另外一种表达方式。参见后面的 [section on lists](#Structured_data) 。)

有关数字的例子则更加有趣：

```
Prelude> :t 42
 42 :: (Num t) => t
 Prelude> :t 42.0
 42.0 :: (Fractional t) => t
 Prelude> :t gcd 15 20
 gcd 15 20 :: (Integral t) => t
```

这些类型用到了 "类型类（type classes）" 含义如下：

- `42` 可作为任意数字(numeric)类型。(这就是为什么我既可以把 `5` 声明为 `Int` 类型，也可以声明为 `Double` 类型的原因。)
- `42.0` 可作为任意分数(fractional)类型，但不能是整数(integral)类型。
- `gcd 15 20` (此为函数调用) 可作为任意整数(integral)类型，但不能是分数类型。

在Haskell "Prelude"(你不需要import任何东西就能使用的那部分库)中有五种数字(numeric)类型:

- `Int` 是一个至少30位(bit)精度的整数。
- `Integer` 是一个无限精度的整数。
- `Float` 是一个单精度浮点数。
- `Double` 是一个双精度浮点数。
- `Rational` 是一个没有舍入误差的分数/小数类型。

上面5个都是 `Num` 类型的 **实例（instances）** 。其中前两个是 `Integral` 类型的 **实例** ，后面三种是 `Fractional` 类型的 **实例** 。

总的一块来看一下，

```
Prelude> gcd 42 35 :: Int
 7
 Prelude> gcd 42 35 :: Double
 
 <interactive>:1:0:
     No instance for (Integral Double)
```

最后值得一提的类型是 `()` ，念做"unit"。 它只有一个取值，也写作 `()` 并念做"unit"。

```
Prelude> ()
 ()
 Prelude> :t ()
 () :: ()
```

你可以把它看作类似C语言中的 void 关键字。在一个I/O动作中，如果你不想返回任何东西，你可以返回 `()` 。

## 有结构的数据

基本数据类型可以很容易的通过两种方式组合在一起：通过 \[方括号\] 组合的 **列表（lists）** ，和通过 (圆括号) 组合的 **元组（tuples）** 。

列表可以用来储存多个相同类型的值：

```haskell
Prelude> [1, 2, 3]
 [1,2,3]
 Prelude> [1 .. 5]
 [1,2,3,4,5]
 Prelude> [1, 3 .. 10]
 [1,3,5,7,9]
 Prelude> [True, False, True]
 [True,False,True]
```

Haskell 中的字符串（String）其实只不过是字符（Character）类型的 List：

```
Prelude> ['H', 'e', 'l', 'l', 'o']
 "Hello"
```

冒号 `:` 运算符用来把一个项（item）添加到列表的开始处。(相当于LISP语言中的 cons 函数)

```
Prelude> 'C' : ['H', 'e', 'l', 'l', 'o']
 "CHello"
```

元组则和列表不同，它用来储存固定个数，但类型不同的值。【译者注：列表是类型相同，但个数不固定，甚至还可以是无限个数】

```
Prelude> (1, True)
 (1,True)
 Prelude> zip [1 .. 5] ['a' .. 'e']
 [(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]
```

上面这个例子用到了 `zip` 函数，它可以把两个列表组合成一个元组的列表。

类型一般都符合你的期望：

```
Prelude> :t ['a' .. 'c']
 ['a' .. 'c'] :: [Char]
 Prelude> :t [('x', True), ('y', False)]
 [('x', True), ('y', False)] :: [(Char, Bool)]
```

列表在Haskell中被大量使用。有些函数能够很好地对列表进行运算：

```
Prelude> [1 .. 5]
 [1,2,3,4,5]
 Prelude> map (+ 2) [1 .. 5]
 [3,4,5,6,7]
 Prelude> filter (> 2) [1 .. 5]
 [3,4,5]
```

有两个作用于双元素元组的优美函数：

```
Prelude> fst (1, 2)
 1
 Prelude> snd (1, 2)
 2
 Prelude> map fst [(1, 2), (3, 4), (5, 6)]
 [1,3,5]
```

我们已经定义了一个名为 `main` 的 [IO动作](https://wiki.haskell.org/index.php?title=Introduction_to_Haskell_IO/Actions "Introduction to Haskell IO/Actions") 函数:

```
main = do putStrLn "What is 2 + 2?"
          x <- readLn
          if x == 4
              then putStrLn "You're right!"
              else putStrLn "You're wrong!"
```

现在，我们定义一个名为 `factorial` (阶乘)的对上面的函数做一点补充。我添加了一个模块头部，这是一种良好的风格。

```
module Main where

factorial n = if n == 0 then 1 else n * factorial (n - 1)

main = do putStrLn "What is 5! ?"
          x <- readLn
          if x == factorial 5
              then putStrLn "You're right!"
              else putStrLn "You're wrong!"
```

使用命令 ghc --make Test.hs 重新编译。并用下面的命令执行

```
$ ./Test
 What is 5! ?
 120
 You're right!
```

这是一个函数。表现得就和内建函数一样，可以通过 `factorial 5` 来调用。

现在向 ghci 询问函数 `factorial` 的 [类型](https://wiki.haskell.org/index.php?title=%E7%B1%BB%E5%9E%8B&action=edit&redlink=1 "类型 (page does not exist)").

```
$ ghci Test.hs
 << GHCi banner >>
 Ok, modules loaded: Main.
 Prelude Main> :t factorial
 factorial :: (Num a) => a -> a
```

Function types are written with the argument type, then `->`, then the result type. (This also has the type class `Num`.)

`factorial` 函数可以通过case得以简化：

```
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

## 语法规则

查看 [语法](https://wiki.haskell.org/index.php?title=Category:Syntax "Category:Syntax") 以了解更多有用的语法。

```
secsToWeeks secs = let perMinute = 60
                       perHour   = 60 * perMinute
                       perDay    = 24 * perHour
                       perWeek   =  7 * perday
                   in  secs / perWeek
```

`let` 表达式定义了临时名称。(This is using layout again. You could use {braces}, and separate the names with semicolons, if you prefer.)

```
classify age = case age of 0 -> "newborn"
                           1 -> "infant"
                           2 -> "toddler"
                           _ -> "senior citizen"
```

`case` 表达式实现了多路分支。符号 `_` 表示"任何东西"。

## Using libraries

Everything used so far in this tutorial is part of the [Prelude](https://wiki.haskell.org/index.php?title=Prelude "Prelude"), which is the set of Haskell functions that are always there in any program.

The best road from here to becoming a very productive Haskell programmer (aside from practice!) is becoming familiar with other [libraries](https://wiki.haskell.org/index.php?title=Applications_and_libraries "Applications and libraries") that do the things you need. Documentation on the standard libraries is at [http://haskell.org/ghc/docs/latest/html/libraries/](http://haskell.org/ghc/docs/latest/html/libraries/). There are modules there with:

- Two test frameworks, QuickCheck and HUnit
- Regular expressions and predictive parsers
- More...

```
module Main where

import qualified Data.Map as M

errorsPerLine = M.fromList
    [ ("Chris", 472), ("Don", 100), ("Simon", -5) ]

main = do putStrLn "Who are you?"
          name <- getLine
          case M.lookup name errorsPerLine of
              Nothing -> putStrLn "I don't know you"
              Just n  -> do putStr "Errors per line: "
                            print n
```

The `import` says to use code from `Data.Map` and that it will be prefixed by `M`. (That's necessary because some of the functions have the same names as functions from the prelude. Most libraries don't need the `as` part.)

If you want something that's not in the standard library, try looking at [http://hackage.haskell.org/packages/hackage.html](http://hackage.haskell.org/packages/hackage.html) or this wiki's [applications and libraries](https://wiki.haskell.org/index.php?title=Applications_and_libraries "Applications and libraries") page. This is a collection of many different libraries written by a lot of people for Haskell. Once you've got a library, extract it and switch into that directory and do this:

```
runhaskell Setup configure
 runhaskell Setup build
 runhaskell Setup install
```

On a UNIX system, you may need to be root for that last part.

## Topics that don't fit in 10 minute limit

- Advanced functions