---
title: "第17章-与C接口-FFI"
source: "http://book.realworldhaskell.org/"
author: "Bryan O'Sullivan, Don Stewart, John Goerzen"
translator: "Claude"
created: 2026-04-11
type: clipping
category: haskell
description: "Real World Haskell 中文翻译版"
tags:
  - clippings
  - haskell
  - book
  - rwh
  - translated
---

# 第17章-与C接口-FFI

编程语言不存在于完美的隔离中。它们栖身于数十年来构建的工具和库生态系统中，通常用各种编程语言编写。良好的工程实践表明我们应该重用这些努力。Haskell 外部函数接口（FFI）是 Haskell 代码可以使用其他语言编写代码并被其他语言使用的方式。在本章中，我们将看看 FFI 如何工作以及如何生成到 C 库的 Haskell 绑定，包括如何使用 FFI 预处理器自动化大部分工作。挑战：采用 PCRE（标准的 Perl 兼容正则表达式库），并使其以高效和功能性的方式从 Haskell 中可用。贯穿始终，我们将寻求抽象出 C 实现所需的手动工作，将该工作委托给 Haskell，使接口更健壮，产生一个干净的、高级的绑定。我们假设只对正则表达式有一些基本熟悉。

将一种语言绑定到另一种语言是一项 nontrivial 任务。绑定语言需要理解目标语言的调用约定、类型系统、数据结构、内存分配机制和链接策略，才能使事情正常工作。

任务是将两种语言的语义仔细对齐，以便两者都能理解它们之间传递的数据。

对于 Haskell，这个技术栈由 FFI (http://www.cse.unsw.edu.au/~chak/haskell/ffi/) 指定到 Haskell 报告。FFI 报告描述了如何正确绑定 Haskell 和 C 以及如何将绑定扩展到其他语言。该标准设计为可移植的，以便 FFI 绑定可以在 Haskell 实现、操作系统和 C 编译器之间可靠地工作。

所有 Haskell 的实现都支持 FFI，当在新领域使用 Haskell 时它是一项关键技术。我们只需绑定到用 Haskell 以外的语言编写的现有库，而不是在领域中重新实现标准库。

FFI 为语言增加了新的灵活性维度：如果我们需要出于某种原因访问原始硬件（例如我们正在编程新硬件或实现操作系统），FFI 让我们获得该硬件的访问权。它也给了我们一个性能逃生舱：如果我们无法足够快地让代码热点运行，总是可以选择用 C 尝试。所以让我们看看 FFI 对编写代码实际意味着什么。

## 外部语言绑定：基础知识

最常见的操作（不出所料）是从 Haskell 调用 C 函数。所以让我们这样做，从标准 C 数学库中绑定一些函数。我们将把绑定放在源文件中，然后将其编译成使用 C 代码的 Haskell 二进制文件。

首先，我们需要启用 FFI 扩展，因为 FFI 附录支持默认不启用。我们像往常一样通过源文件顶部的 LANGUAGE pragma 来执行此操作：

```haskell
-- file: ch17/SimpleFFI.hs
{-# LANGUAGE ForeignFunctionInterface #-}
```

LANGUAGE pragmas 指示模块使用的 Haskell 98 扩展。这次我们只引入 FFI 扩展。跟踪你需要的语言扩展很重要。更少的扩展通常意味着更可移植、更健壮的代码。事实上，十多年前编写的 Haskell 程序由于标准化而能够完美编译运行，尽管语言语法、类型系统和核心库发生了变化。

下一步是导入 Foreign 模块，它提供有用的类型（如指针、数值类型和数组）和实用函数（如 malloc 和 alloca）用于编写到其他语言的绑定：

```haskell
-- file: ch17/SimpleFFI.hs
import Foreign
import Foreign.C.Types
```

对于外部库的广泛工作，对 Foreign 模块的良好了解是必不可少的。其他有用的模块包括 Foreign.C.String、Foreign.Ptr 和 Foreign.Marshal.Array。

现在我们可以开始调用 C 函数的工作了。为此，我们需要知道三件事：C 函数的名称、其类型及其相关的头文件。另外，对于不是由标准 C 库提供的代码，我们需要知道 C 库的链接名称。实际的绑定工作使用 foreign import 声明完成，像这样：

```haskell
-- file: ch17/SimpleFFI.hs
foreign import ccall "math.h sin"
     c_sin :: CDouble -> CDouble
```

这定义了一个新的 Haskell 函数 c_sin，其具体实现是 C 通过 sin 函数。当调用 c_sin 时，将调用实际的 sin（使用标准 C 调用约定，由 ccall 指示）。Haskell 运行时将控制传递给 C，C 将其结果返回给 Haskell。结果然后被包装为类型 CDouble 的 Haskell 值。

编写 FFI 绑定时，一个常见的习惯用法是用前缀 c_ 暴露 C 函数，使其与更用户友好、高级函数区分开来。原始 C 函数由 math.h 头文件指定，其中声明它的类型为：

```c
double sin(double x);
```

编写绑定时，程序员必须将这样的 C 类型签名转换为它们等效的 Haskell FFI，确保数据表示匹配。例如，C 中的 double 对应于 Haskell 中的 CDouble。我们需要在这里小心，因为如果出错，Haskell 编译器会愉快地生成错误的代码来调用 C！可怜的 Haskell 编译器不知道 C 函数实际需要什么类型，所以如果被指示，它将用错误的参数调用 C 函数。最好这将导致 C 编译器警告，更可能的是将以运行时崩溃结束。最糟糕的是错误会静默地不被注意，直到发生一些关键故障。所以确保你使用正确的 FFI 类型，不要害怕使用 QuickCheck 通过绑定测试你的 C 代码。

最重要的原始 C 类型在 Haskell 中用相当直观的名字表示（有符号和无符号类型）CChar、CUChar、CInt、CUInt、CLong、CULong、CSize、CFloat 和 CDouble。更多在 FFI 标准中定义，可以在 Haskell base 库的 Foreign.C.Types 下找到。也可以为你自己的 C 表示类型定义 Haskell 端表示类型，我们稍后会看到。

### 小心副作用

一点需要注意的是，我们将 sin 绑定为 Haskell 中的纯函数，一个没有副作用的函数。在这种情况下这没问题，因为 C 中的 sin 函数是引用透明的。

通过将纯 C 函数绑定到纯 Haskell 函数，Haskell 编译器了解到了一些关于 C 代码的知识——即它没有副作用，使优化更容易。纯代码对 Haskell 程序员也更灵活，因为它产生自然持久的数据结构和线程安全函数。然而，虽然纯 Haskell 代码始终是线程安全的，但这对 C 来说更难保证。即使文档表明函数可能没有副作用，也很少能确保它也是线程安全的，除非明确记录为"可重入"。纯的、线程安全的 C 代码虽然罕见，但却是宝贵的商品。这是从 Haskell 使用 C 的最简单的风格。

当然，带副作用的代码在命令式语言中更常见，其中语句的显式排序鼓励使用效果。由于全局或局部状态的变化，或具有其他副作用，C 中的函数给定相同参数返回不同值更为常见。通常，这在 C 中通过函数只返回状态值或一些 void 类型而不是有用的结果值来发出信号。这表明函数的工作在其副作用中。对于这样的函数，我们需要将这些副作用捕获到 IO monad 中（例如通过将返回类型更改为 IO CDouble）。我们还需要非常小心非同时也是可重入的纯 C 函数，因为与 C 相比，Haskell 代码中多个线程非常常见。我们可能需要用事务锁来调节 FFI 绑定的访问，或者通过复制底层 C 状态使非可重入代码安全使用。

### 高级包装器

有了 foreign imports，下一步是将我们传递给外部语言调用和从外部语言调用接收的 C 类型转换为原生 Haskell 类型，包装绑定使其看起来像一个普通的 Haskell 函数：

```haskell
-- file: ch17/SimpleFFI.hs
fastsin :: Double -> Double
fastsin x = realToFrac (c_sin (realToFrac x))
```

编写像这样的绑定便捷包装器时，需要记住的主要事情是正确地将输入和输出转换回正常 Haskell 类型。要在浮点值之间转换，我们可以使用 realToFrac，它让我们转换不同的浮点值（并且这些转换（如从 CDouble 到 Double）通常是无代价的，因为底层表示不变）。对于整数值，可以使用 fromIntegral。对于其他常见 C 数据类型（如数组），我们可能需要将数据解包为更易处理的 Haskell 类型（如列表），或者可能将 C 数据保持为不透明且仅间接操作（可能通过 ByteString）。选择取决于转换的成本以及源类型和目标类型上可用的函数。

现在我们可以继续在程序中使用绑定的函数。例如，我们可以将 C sin 函数应用于 Haskell 的十分之一列表：

```haskell
-- file: ch17/SimpleFFI.hs
main = mapM_ (print . fastsin) [0/10, 1/10 .. 10/10]
```

这个简单的程序在计算时打印每个结果。将完整绑定放在 SimpleFFI.hs 文件中允许我们在 ghci 中运行它：

```sh
$ ghci SimpleFFI.hs
*Main> main
0.0
9.983341664682815e-2
0.19866933079506122
0.2955202066613396
0.3894183423086505
0.479425538604203
0.5646424733950354
0.644217687237691
0.7173560908995227
0.7833269096274833
0.8414709848078964
```

或者，我们可以将代码编译为可执行文件，动态链接到相应的 C 库：

```sh
$ ghc -O --make SimpleFFI.hs
[1 of 1] Compiling Main             ( SimpleFFI.hs, SimpleFFI.o )
Linking SimpleFFI ...
```

然后运行它：

```sh
$ ./SimpleFFI
0.0
9.983341664682815e-2
0.19866933079506122
0.2955202066613396
0.3894183423086505
0.479425538604203
0.5646424733950354
0.644217687237691
0.7173560908995227
0.7833269096274833
0.8414709848078964
```

我们现在做得很好，有了一个完整程序，静态链接到 C，交织着 C 和 Haskell 代码并跨语言边界传递数据。像刚才所示的简单绑定几乎是微不足道的，因为标准 Foreign 库为常见类型（如 CDouble）提供了方便的别名。在下一节中，我们将看到一个更大的工程任务：绑定到 PCRE 库，这带来了内存管理和类型安全的问题。

## Haskell 的正则表达式：PCRE 绑定

正如我们在前几节中看到的，Haskell 程序作为一种基础数据结构对列表有相当的偏见。列表函数是核心库的一部分，构造和分解列表结构的便捷语法内置于语言中。字符串当然是简单的字符列表（而不是例如平坦的字符数组）。这种灵活性一切都很好，但导致标准库倾向于多态列表操作而不是字符串特定操作。

事实上，许多常见任务可以通过基于正则表达式的字符串处理解决，但正则表达式支持不是 Haskell Prelude 的一部分。所以让我们看看如何采用一个现成的正则表达式库 PCRE，并为其提供自然、便捷的 Haskell 绑定，为 Haskell 提供有用的正则表达式。

PCRE 本身是一个实现 Perl 风格正则表达式的通用 C 库。它广泛可用并预装在许多系统上。你可以在 http://www.pcre.org/ 找到它。在以下部分中，我们假设 PCRE 库和头文件在机器上可用。

## 简单任务：使用 C 预处理器

从 Haskell 到 C 编写新 FFI 绑定的最简单任务是将 C 头文件中定义的常量绑定到等效的 Haskell 值。例如，PCRE 提供了一组标志，用于修改核心模式匹配系统的工作方式（如忽略大小写或允许匹配换行符）。这些标志在 PCRE 头文件中显示为数字常量：

```c
/* Options */
#define PCRE_CASELESS           0x00000001
#define PCRE_MULTILINE          0x00000002
#define PCRE_DOTALL             0x00000004
#define PCRE_EXTENDED           0x00000008
```

要将这些值导出到 Haskell，我们需要以某种方式将它们插入 Haskell 源文件。一个明显的方法是使用 C 预处理器将定义从 C 替换到 Haskell 源，然后我们将正常的 Haskell 源文件编译它。使用预处理器，我们甚至可以声明简单的常量，通过 Haskell 源文件上的文本替换：

```haskell
-- file: ch17/Enum1.hs
{-# LANGUAGE CPP #-}
#define N 16
main = print [ 1 .. N ]
```

该文件以类似于 C 源的方式使用预处理器处理（当编译器发现 LANGUAGE pragma 时，为我们运行 CPP），产生程序输出：

```sh
$ runhaskell Enum.hs
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
```

然而，依赖 CPP 是一个相当脆弱的方法。C 预处理器不知道它正在处理 Haskell 源文件，会愉快地包含文本或转换源，以使我们的 Haskell 代码无效。我们需要小心不要混淆 CPP。如果我们包含 C 头文件，我们冒着替换不需要的符号或向 Haskell 源插入 C 类型信息和原型的风险，导致一个混乱的灾难。

为了解决这些问题，binding 预处理器 hsc2hs 与 GHC 一起分发。它提供了一种方便的语法用于在 Haskell 中包含 C 绑定信息，以及让我们安全地操作头文件。它是大多数 Haskell FFI 绑定的选择工具。

### 使用 hsc2hs 将 Haskell 绑定到 C

要将 hsc2hs 用作 Haskell 的智能绑定工具，我们需要创建一个 .hsc 文件 Regex.hsc，它将包含我们绑定的 Haskell 源以及 hsc2hs 处理规则、C 头文件和 C 类型信息。首先，我们需要一些 pragma 和导入：

```haskell
-- file: ch17/Regex-hsc.hs
{-# LANGUAGE CPP, ForeignFunctionInterface #-}
module Regex where
import Foreign
import Foreign.C.Types
#include <pcre.h>
```

该模块以 FFI 绑定的典型前言开始：启用 CPP，启用 FFI 语法，声明模块名称，然后从 base 库导入一些东西。异常的项目是最后一行，我们包含了 PCRE 的 C 头文件。这在 .hs 源文件中无效，但在 .hsc 代码中没问题。

### 为 PCRE 添加类型安全

接下来，我们需要一个类型来表示 PCRE 编译时选项。在 C 中，这些是编译函数的整数标志，所以我们可以用 CInt 来表示它们。我们对标志的唯一了解是它们是 C 数字常量，所以 CInt 是合适的表示。

作为 Haskell 库作者，这感觉邋遢。可以用作 regex 标志的值类型包含的值比 CInt 允许的要少。没有什么可以阻止最终用户传递非法的整数值作为参数，或者混淆只应在 regex 编译时传递的标志与运行时标志。也可能对标志进行任意数学运算或其他整数和标志混淆的错误。

我们真的需要更精确地指定标志的类型与其作为数值运行时的表示不同。如果我们能做到这一点，我们可以静态地防止一类与标志误用相关的 bug。

添加这样一层类型安全相对容易，是 newtype（类型引入声明）的一个很好的用例。newtype 让我们创建一个与另一个类型具有相同运行时表示的类型，但在编译时被类型检查器当作不同类型处理。我们可以将标志表示为 CInt 值，但在编译时它们将被明显地标记。这使得使用无效标志值成为类型错误（因为我们只指定那些有效标志并阻止访问数据构造函数），或者将标志传递给期望整数的函数成为类型错误。我们使用 Haskell 类型系统为 C PCRE API 引入一层类型安全。

为此，我们为 PCRE 编译时选项定义一个 newtype，其表示实际上是一个 CInt 值，像这样：

```haskell
-- file: ch17/Regex-hsc.hs
-- | A type for PCRE compile-time options. These are newtyped CInts,
-- which can be bitwise-or'd together, using '(Data.Bits..|.)'
--
newtype PCREOption = PCREOption { unPCREOption :: CInt }
    deriving (Eq,Show)
```

类型名是 PCREOption，它有一个同名的单一构造函数，也叫 PCREOption，通过用构造函数包装它将 CInt 值提升为新类型。我们也可以愉快地使用 Haskell 记录语法定义一个访问器 unPCREOption 来访问底层 CInt。这在一行中提供了很多便利。当我们在这里时，我们还可以为标志派生一些有用的类型类操作（相等性和打印）。我们需要记住从源模块抽象地导出数据构造函数，确保用户不能构造自己的 PCREOption 值。

### 绑定到常量

现在我们已经引入了所需的模块，打开了我们需要的语言功能，并定义了表示 PCRE 选项的类型，我们需要实际定义一些对应于这些 PCRE 常量的 Haskell 值。

我们可以通过两种方式使用 hsc2hs。第一种是使用 hsc2hs 提供的 #const 关键字。这让我们命名要由 C 预处理器提供的常量。我们可以使用 #const 关键字通过列出 CPP 符号来手动绑定常量：

```haskell
-- file: ch17/Regex-hsc-const.hs
caseless       :: PCREOption
caseless       = PCREOption #const PCRE_CASELESS
dollar_endonly :: PCREOption
dollar_endonly = PCREOption #const PCRE_DOLLAR_ENDONLY
dotall         :: PCREOption
dotall         = PCREOption #const PCRE_DOTALL
```

这在 Haskell 端引入了三个新常量，caseless、dollar_endonly 和 dotall，对应于同名的 C 定义。我们立即用 newtype 构造函数包装常量，所以它们只作为抽象 PCREOption 类型向程序员公开。

创建 .hsc 文件是第一步。我们现在需要实际创建一个 Haskell 源文件，完成 C 预处理。是时候在 .hsc 文件上运行 hsc2hs 了：

```sh
$ hsc2hs Regex.hsc
```

这会创建一个新的输出文件 Regex.hs，其中 CPP 变量已被展开，产生有效的 Haskell 代码：

```haskell
-- file: ch17/Regex-hsc-const-generated.hs
caseless       :: PCREOption
caseless       = PCREOption 1
{-# Line 21 "Regex.hsc" #-}
dollar_endonly :: PCREOption
dollar_endonly = PCREOption 32
{-# Line 24 "Regex.hsc" #-}
dotall         :: PCREOption
dotall         = PCREOption 4
{-# Line 27 "Regex.hsc" #-}
```

注意原始 .hsc 文件中的行通过 LINE pragma 列出在每个展开的定义旁边。编译器使用此信息来报告相对于源文件的错误（原始文件中的错误），而不是生成的文件中的错误。我们可以加载这个生成的 .hs 文件到解释器并使用结果：

```sh
$ ghci Regex.hs
*Regex> caseless
PCREOption {unPCREOption = 1}
*Regex> unPCREOption caseless
1
*Regex> unPCREOption caseless + unPCREOption caseless
2
*Regex> caseless + caseless
interactive>:1:0:
    No instance for (Num PCREOption)
```

事情按预期工作。这些值是不透明的，如果我们尝试破坏抽象，我们会收到类型错误，并且如果需要我们可以解包并操作它们。unPCREOption 访问器用于解包盒子。这是一个好的开始，但让我们看看如何进一步简化这个任务。

### 自动化绑定

显然，手动列出所有 C defines 并包装它们是乏味且容易出错的。将所有字面值包装在 newtype 构造函数中也是令人厌烦的。这种绑定是如此常见的任务，hsc2hs 提供了方便的语法来自动化它：#enum 结构。

我们可以用等价的替换顶层绑定的列表：

```haskell
-- file: ch17/Regex-hsc.hs
-- PCRE compile options
#{enum PCREOption, PCREOption
  , caseless             = PCRE_CASELESS
  , dollar_endonly       = PCRE_DOLLAR_ENDONLY
  , dotall               = PCRE_DOTALL
  }
```

这更简洁！#enum 结构给了我们三个字段来处理。第一个是我们希望 C defines 被当作的类型。这让我们为绑定选择其他东西而不仅仅是 CInt。我们选择构造 PCREOption's。

第二个字段是一个可选构造函数，放在符号前面。这专门用于我们想要构造 newtype 值的情况，这里节省了大量繁琐工作。#enum 语法的最后部分是自解释的：它只是定义要通过 CPP 填充的常量 Haskell 名称。

像之前一样通过 hsc2hs 运行此代码，生成一个 Haskell 文件，其中包含以下绑定代码（为简洁起见，LINE pragmas 已移除）：

```haskell
-- file: ch17/Regex.hs
caseless              :: PCREOption
caseless              = PCREOption 1
dollar_endonly        :: PCREOption
dollar_endonly        = PCREOption 32
dotall                :: PCREOption
dotall                = PCREOption 4
```

完美。现在我们可以用 Haskell 处理这些值。我们的目标是让标志被视为抽象类型，而不是 C 中的位字段。在 C 中传递多个标志是通过按位或将多个标志组合在一起。对于抽象类型，这会暴露太多信息。为了保持抽象并赋予它 Haskell 风格，我们更希望用户传入一个列表，让库自己组合标志。这可以通过一个简单的 fold 实现：

```haskell
-- file: ch17/Regex.hs
-- | Combine a list of options into a single option, using bitwise (.|.)
combineOptions :: [PCREOption] -> PCREOption
combineOptions = PCREOption . foldr ((.|.) . unPCREOption) 0
```

这个简单的循环从 0 的初始值开始，解包每个标志，并使用按位或——(.|.)——在底层 CInt 上，将每个值与循环累加器组合。然后最终累积的状态用 PCREOption 构造函数包装。

现在让我们转向实际编译一些正则表达式。

## 在 Haskell 和 C 之间传递字符串数据

下一个任务是编写到 PCRE 正则表达式编译函数的绑定。让我们看看它的类型，直接来自 pcre.h 头文件：

```c
pcre *pcre_compile(const char *pattern,
                   int options,
                   const char **errptr,
                   int *erroffset,
                   const unsigned char *tableptr);
```

此函数将正则表达式模式编译成某种内部格式，接受模式作为参数以及一些标志和一些用于返回状态信息的变量。

我们需要弄清楚用哪些 Haskell 类型来表示每个参数。大多数这些类型由 FFI 标准为我们定义的等效类型覆盖，可在 Foreign.C.Types 中找到。第一个参数，即正则表达式本身，作为空终止的 char 指针传递给 C，等效于 Haskell CString 类型。我们已经选择用抽象 PCREOption newtype 表示 PCRE 编译时选项，其运行时表示是 CInt。因为表示被保证是相同的，我们可以安全地传递 newtype。其他参数更复杂，需要一些工作来构造和分解。

第三个参数是指向 C 字符串的指针，当编译表达式时将生成任何错误消息时使用。指针的值将被 C 函数修改以指向自定义错误字符串。我们可以用 Ptr CString 类型表示。在 Haskell 中，指针是堆分配的原始地址容器，可以使用 FFI 库中的一些分配原语创建和操作。例如，我们可以将指向 C int 的指针表示为 Ptr CInt，将指向无符号 char 的指针表示为 Ptr Word8。

### 关于指针的说明

一旦我们有了方便的 Haskell Ptr 值，我们可以用它做各种指针操作。我们可以比较它是否等于空指针，用特殊的 nullPtr 常量表示。我们可以将指针从一种类型强制转换为另一种类型，或者用 plusPtr 按字节偏移推进指针。我们甚至可以使用 poke 修改指针指向的值，当然也可以使用 peek 解引用指针得到它指向的东西。在大多数情况下，Haskell 程序员不需要直接操作指针，但当需要时，这些工具会派上用场。

那么问题是如何表示当我们编译正则表达式时返回的抽象 pcre 指针。我们需要一个与 C 类型一样抽象的 Haskell 类型。因为 C 类型被抽象处理，我们可以为数据分配任何堆分配的 Haskell 类型，只要它很少或没有操作。这是一个用于任意类型的外部数据的常见技巧。用于表示未知外部数据的习惯简单类型是指向 () 类型的指针。我们可以使用类型同义词来记住绑定：

```haskell
-- file: ch17/PCRE-compile.hs
type PCRE = ()
```

也就是说，外部数据是一些未知的、不透明的对象，我们将只当作指向 () 的指针，充分知道我们永远不会实际解引用那个指针。这给了我们以下 pcre_compile 的 foreign import 绑定，它必须在 IO 中，因为返回的指针在每次调用时都会不同，即使返回的对象在功能上等效：

```haskell
-- file: ch17/PCRE-compile.hs
foreign import ccall unsafe "pcre.h pcre_compile"
    c_pcre_compile  :: CString
                    -> PCREOption
                    -> Ptr CString
                    -> Ptr CInt
                    -> Ptr Word8
                    -> IO (Ptr PCRE)
```

### 类型化指针

我们可以通过使用类型化指针而不是使用 () 类型来进一步提高绑定的安全性。也就是说，一个独特的类型，区别于单元类型，没有有意义的运行时表示。一个无法构造数据的类型，使得解引用成为类型错误。构建这样可证明不可检查的数据类型的一种好方法是使用零元数据类型：

```haskell
-- file: ch17/PCRE-nullary.hs
data PCRE
```

### 关于安全性的说明

制作 foreign import 声明时，我们可以选择使用安全关键字指定调用时使用的安全级别。安全调用效率较低但保证 Haskell 系统可以从 C 安全调用。不安全调用开销小得多，但被调用的 C 代码必须不回调 Haskell。

默认情况下，foreign imports 是安全的，但实际上 C 代码回调 Haskell 的情况很少，所以我们大多使用不安全调用以提高效率。

这需要 EmptyDataDecls 语言扩展。这个类型显然不包含任何值！我们只能构造指向这样的值的指针，因为没有可以具有此类型的具体值（除了 bottom）。

我们也可以使用递归 newtype 实现相同的事情，不需要语言扩展：

```haskell
-- file: ch17/PCRE-recursive.hs
newtype PCRE = PCRE (Ptr PCRE)
```

同样，我们不能真正用这种类型的值做任何事情，因为它没有运行时表示。以这些方式使用类型化指针只是在我们提供的 C 基础上添加 Haskell 层安全性的另一种方式。什么需要在 C 程序员方面要求纪律（记住永远不要解引用 PCRE 指针）可以在 Haskell 绑定的类型系统中静态强制执行。如果这段代码编译成功，类型检查器已经给了我们一个证明： C 返回的 PCRE 对象在 Haskell 端永远不会被解引用。

### 内存管理：让垃圾收集器工作

一个尚未解决的问题是如何管理与 C 库返回的抽象 PCRE 结构相关的内存。调用者不需要分配它——库通过在 C 端分配内存来处理。但有时，我们需要释放它。这又是通过将使用 C 库的繁琐抽象到 Haskell 绑定内部来隐藏复杂性的机会。

我们将使用 Haskell 垃圾收集器在不再使用它时自动释放 C 结构。为此，我们将利用 Haskell 垃圾收集器终结器和 ForeignPtr 类型。

我们不希望用户必须手动释放 foreign 调用返回的 Ptr PCRE 值。PCRE 库特别指出结构在 C 端用 malloc 分配，需要在不再使用时释放，否则我们有泄漏内存的风险。

Haskell 垃圾收集器已经大大自动化了为 Haskell 值管理内存的任务。我们可以巧妙地将我们辛勤工作的垃圾收集器分配给任务来照顾 C 的内存。技巧是将一块 Haskell 数据与外部分配器数据关联，并给 Haskell 垃圾收集器一个任意函数，一旦它注意到 Haskell 数据完成，就去释放 C 资源。

我们有两个工具可用——不透明的 ForeignPtr 数据类型和 newForeignPtr 函数，其类型为：

```haskell
-- file: ch17/ForeignPtr.hs
newForeignPtr :: FinalizerPtr a -> Ptr a -> IO (ForeignPtr a)
```

该函数接受两个参数：一个当数据超出范围时运行的终结器和一个指向关联 C 数据的指针。它返回一个新的托管指针，一旦垃圾收集器决定数据不再使用，将运行其终结器。

多么美好的抽象！

每当 C 库要求用户在不再使用时显式释放或以其他方式清理资源时，这些可终结指针是合适的。这是一个简单的设备，可以大大有助于使 C 库绑定更自然、更实用、更符合风格。

因此，想到这里，我们可以将手动管理的 Ptr PCRE 类型隐藏在自动管理的数据结构中。这产生了用于表示用户将看到的正则表达式的数据类型：

```haskell
-- file: ch17/PCRE-compile.hs
data Regex = Regex !(ForeignPtr PCRE)
                   !ByteString
        deriving (Eq, Ord, Show)
```

这个新的 Regex 数据类型由两部分组成。第一个是一个抽象的 ForeignPtr，我们将用它来管理在 C 中分配的底层 PCRE 数据。第二个组件是一个严格的 ByteString，即我们编译的正则表达式的字符串表示。通过在 Regex 类型内部保留正则表达式的用户级表示，我们可以更容易地打印友好的错误消息并以有意义的方式显示 Regex 本身。

### 高级接口： marshaling 数据

编写 FFI 绑定时的挑战（一旦决定了 Haskell 类型）是转换为 Haskell 程序员熟悉的低级指针数组和其他 C 类型的常规数据类型。理想的 Haskell 正则表达式编译接口会是什么样子？我们有一些设计直觉可以指导我们。

首先，编译行为应该是引用透明的操作：传递相同的 regex 字符串每次都会产生功能上相同的编译模式，尽管 C 库会给我们功能上相同的表达式在可观察上不同的指针。如果我们能隐藏这些内存管理细节，我们应该能够将绑定表示为纯函数。将 C 函数在 Haskell 中表示为纯操作的能力是迈向灵活性的关键一步，也是接口易于使用的指标（因为在可以使用之前不需要复杂的状态初始化）。

尽管是纯的，函数仍然可能失败。如果用户提供的正则表达式格式不正确，则返回错误字符串。表示可选失败和错误值的好数据类型是 Either。也就是说，要么我们返回一个有效的编译正则表达式，要么我们返回一个错误字符串。将 C 函数的结果编码为熟悉的、基础的 Haskell 类型（如 Either）这是使绑定更符合习惯的另一个有用步骤。

对于用户提供的参数，我们已经决定将编译标志作为列表传入。我们可以选择将输入正则表达式作为高效的 ByteString 或常规 String 传递。那么适当的类型签名，用于引用透明编译成功与值或失败与错误字符串，将是：

```haskell
-- file: ch17/PCRE-compile.hs
compile :: ByteString -> [PCREOption] -> Either String Regex
```

输入是一个 ByteString，可从 Data.ByteString.Char8 模块获得（我们将限定导入以避免名称冲突），包含正则表达式和标志列表（如果没有标志要传递，则为空列表）。结果则是一个错误字符串，或者一个新的、编译的正则表达式。

### Marshaling ByteStrings

给定这个类型，我们可以勾勒出 compile 函数：原始 C 绑定的高级接口。在其核心，它将调用 c_pcre_compile。在此之前，它必须将输入 ByteString marshaling 为 CString。这是使用 ByteString 库的 useAsCString 函数完成的，它将输入 ByteString 复制为空终止的 C 数组（也有一个不安全的、零拷贝变体，假设 ByteString 已经空终止）：

```haskell
-- file: ch17/ForeignPtr.hs
useAsCString :: ByteString -> (CString -> IO a) -> IO a
```

此函数将 ByteString 作为输入。第二个参数是一个用户定义的函数，它将使用结果的 CString 运行。我们在这里看到另一个有用的习惯用法：通过闭包自然作用域的数据 marshaling 函数。我们的 useAsCString 函数将输入数据转换为 C 字符串，然后我们可以作为指针传递给 C。然后我们的负担是向它提供一个调用 C 的代码块。

这种风格的代码通常以悬空的 do 块表示法编写。以下伪代码说明了这个结构：

```haskell
-- file: ch17/DoBlock.hs
useAsCString str $ \cstr -> do
   ... operate on the C string
   ... return a result
```

这里的第二个参数是一个匿名函数，一个 lambda，以 monadic do 块为主体。使用简单的 ($) 应用运算符来避免括号来界定代码块参数是常见的。这是在处理这样的代码块参数时记住的一个有用习惯用法。

### 分配本地 C 数据：Storable 类

我们可以愉快地将 ByteString 数据 marshal 为 C 兼容类型，但 pcre_compile 函数还需要一些指针和数组来放置其他返回值。这些应该只是短期存在，所以我们不需要复杂的分配策略。这种短期生存期的 C 数据可以用 alloca 函数创建：

```haskell
-- file: ch17/ForeignPtr.hs
alloca :: Storable a => (Ptr a -> IO b) -> IO b
```

此函数接受一个接受指向某种 C 类型作为参数的代码块，并安排用正确形状的未初始化数据 fresh 地调用该函数。分配机制镜像其他语言中的局部堆栈变量。分配的内存在参数函数退出时释放。这样，我们获得词法作用域的低级数据类型分配，它们在作用域退出后保证被释放。我们可以使用它来分配任何具有 Storable 类型类实例的数据类型。这种重载分配操作符的含义是，所分配的数据类型可以根据使用推断！Haskell 会根据我们对数据使用的函数知道要分配什么。

要分配一个指向 CString 的指针，例如，它将被调用函数修改为指向特定的 CString，我们会调用 alloca，在伪代码中：

```haskell
-- file: ch17/DoBlock.hs
alloca $ \stringptr -> do
   ... call some Ptr CString function
   peek stringptr
```

这本地分配一个 Ptr CString 并将代码块应用于该指针，然后调用 C 函数来修改指针内容。最后，我们使用 Storable 类 peek 函数解引用指针，产生一个 CString。

### 整合一切

我们已经决定了用什么 Haskell 类型表示 C 函数，用什么结果数据表示，以及它的内存如何管理。我们已经为 pcre_compile 函数的标志选择了表示，并想出了如何获取来往于检查它的 C 字符串。所以让我们编写从 Haskell 编译 PCRE 正则表达式的完整函数：

```haskell
-- file: ch17/PCRE-compile.hs
compile :: ByteString -> [PCREOption] -> Either String Regex
compile str flags = unsafePerformIO $
  useAsCString str $ \pattern -> do
    alloca $ \errptr       -> do
    alloca $ \erroffset    -> do
        pcre_ptr <- c_pcre_compile pattern (combineOptions flags) errptr
        erroffset nullPtr
        if pcre_ptr == nullPtr
            then do
                err <- peekCString =<< peek errptr
                return (Left err)
            else do
                reg <- newForeignPtr finalizerFree pcre_ptr -- release with free()
                return (Right (Regex reg str))
```

就这样！让我们仔细走一遍这里的细节，因为它相当密集。第一个引人注目的是使用 unsafePerformIO，这是一个相当著名的函数，具有非常不寻常的类型，从不祥的 System.IO.Unsafe 导入：

```haskell
-- file: ch17/ForeignPtr.hs
unsafePerformIO :: IO a -> a
```

这个函数做了一些奇怪的事情。它接受一个 IO 值并将其转换为纯值！在警告了这么久的关于效果的危险之后，这里有危险效果的一行启用者。如果不明智地使用，这个函数让我们绕过 Haskell 类型系统提供的所有安全保证，在 Haskell 程序中的任何地方插入任意副作用。我们可以破坏优化，修改内存中的任意位置，删除用户机器上的文件，或者从我们的斐波那契数列中发射核导弹。那么为什么这个函数存在呢？

它的存在正是为了启用 Haskell 绑定到我们知道是引用透明的 C 代码，但无法向 Haskell 类型系统证明这一点。它让我们对编译器说："我知道我在做什么——这段代码真的是纯的。"对于正则表达式编译，我们知道情况就是这样：给定相同的模式，我们每次都应该得到相同的正则表达式匹配器。然而，向编译器证明这一点超出了 Haskell 类型系统的能力范围，所以我们被迫断言这段代码是纯的。使用 unsafePerformIO 允许我们做到这一点。

然而，如果我们知道 C 代码是纯的，为什么我们不直接在 import 声明中给它一个纯类型呢？我们不这样做，是因为我们必须为 C 函数工作的局部内存分配，这必须在 IO monad 中完成，因为这是一个局部副作用。那些副作用不会逃离围绕 foreign 调用的代码，所以当包装时，我们使用 unsafePerformIO 重新引入纯粹性。

unsafePerformIO 的参数是我们编译函数的实际主体，由四部分组成：将 Haskell 数据 marshal 为 C 形式；调用 C 库；检查返回值；最后，从结果构造一个 Haskell 值。我们用 useAsCString 和 alloca 进行 marshal，设置我们需要传递给 C 的数据，并使用之前开发的 combineOptions 将标志列表折叠为单个 CInt。一旦一切就绪，我们终于可以用模式、标志和结果指针调用 c_pcre_compile。我们为字符编码表使用 nullPtr，在这种情况下未使用。

从 C 调用返回的结果是指向抽象 PCRE 结构的指针。然后我们对照 nullPtr 测试它。如果正则表达式有问题，我们必须解引用错误指针，产生一个 CString。然后我们用库函数 peekCString 将其解包为正常的 Haskell 字符串。错误路径的最终结果是 Left err 值，向调用者指示失败。

但是如果调用成功，我们分配一个新的存储托管指针，使用 ForeignPtr 的 C 函数。特殊值 finalizerFree 被绑定为该数据的终结器，它使用标准 C free 来释放数据。然后将其包装为不透明的 Regex 值。成功结果用 Right 标记，然后返回给用户。就这样完成了！

我们需要用 hsc2hs 处理源文件，然后在 ghci 中加载函数。然而，第一次尝试这样做会导致错误：

```sh
$ hsc2hs Regex.hsc
$ ghci Regex.hs
During interactive linking, GHCi couldn't find the following symbol:
  pcre_compile
```

这可能是因为你没有让 GHCi 加载当前会话所需的额外目标文件、归档或 DLL。重新启动 GHCi，使用 -L/path/to/object/dir 和 -lmissinglibname 标志指定缺失的库，或者简单地在 GHCi 命令行上命名相关文件。

有点可怕。然而，这只是因为我们没有将我们想要调用的 C 库链接到 Haskell 代码。假设 PCRE 库已安装在系统默认库位置，我们可以通过在 ghci 命令行添加 -lpcre 让 ghci 知道它。现在我们可以尝试在一些正则表达式上运行代码，看看成功和错误的情况：

```sh
$ ghci Regex.hs -lpcre
*Regex> :m + Data.ByteString.Char8
*Regex Data.ByteString.Char8> compile (pack "a.*b") []
Right (Regex 0x00000000028882a0 "a.*b")
*Regex Data.ByteString.Char8> compile (pack "a.*b[xy]+(foo?)") []
Right (Regex 0x0000000002888860 "a.*b[xy]+(foo?)")
*Regex Data.ByteString.Char8> compile (pack "*") []
Left "nothing to repeat"
```

正则表达式被打包到字节字符串并 marshal 到 C，在那里由 PCRE 库编译。然后结果被返回给 Haskell，我们使用默认 Show 实例显示结构。下一步是用这些编译的正则表达式模式匹配一些字符串。

## 匹配字符串

好的正则表达式库的第二部分是匹配函数。给定一个编译的正则表达式，此函数执行编译后的 regex 对某些输入的匹配，指示它是否匹配，如果匹配，字符串的哪些部分匹配。在 PCRE 中，此函数的类型为：

```c
int pcre_exec(const pcre *code,
              const pcre_extra *extra,
              const char *subject,
              int length,
              int startoffset,
              int options,
              int *ovector,
              int ovecsize);
```

最重要的参数是输入 pcre 指针结构（我们从 pcre_compile 获得的）和主体字符串。其他标志让我们提供簿记结构和返回值的空间。我们可以直接将此类型转换为 Haskell import 声明：

```haskell
-- file: ch17/RegexExec.hs
foreign import ccall "pcre.h pcre_exec"
    c_pcre_exec     :: Ptr PCRE
                    -> Ptr PCREExtra
                    -> Ptr Word8
                    -> CInt
                    -> CInt
                    -> PCREExecOption
                    -> Ptr CInt
                    -> CInt
                    -> IO CInt
```

我们使用与之前相同的方法为 PCREExtra 结构创建类型化指针，以及用一个 newtype 表示在 regex 执行时传递的标志。这让我们确保用户不会在 regex 运行时错误地传递编译时标志。

### 提取有关模式的信息

调用 pcre_exec 涉及的主要复杂之处是用于保存模式匹配器找到的匹配子串偏移量的 int 指针数组。这些偏移量保存在偏移向量中，其所需大小通过分析输入正则表达式以确定它包含的捕获模式数量来确定。PCRE 提供了一个函数 pcre_fullinfo，用于确定有关正则表达式的许多信息，包括模式数量。我们需要调用这个，现在我们可以直接写下绑定到 pcre_fullinfo 的 Haskell 类型：

```haskell
-- file: ch17/RegexExec.hs
foreign import ccall "pcre.h pcre_fullinfo"
    c_pcre_fullinfo :: Ptr PCRE
                    -> Ptr PCREExtra
                    -> PCREInfo
                    -> Ptr a
                    -> IO CInt
```

此函数最重要的参数是编译后的正则表达式和 PCREInfo 标志，它指示我们感兴趣的信息。在这种情况下，我们关心捕获模式计数。标志被编码为数字常量，我们需要使用特定的 PCRE_INFO_CAPTURECOUNT 值。还有其他决定函数结果类型的常量范围，我们可以像之前一样使用 #enum 结构绑定。最后一个参数是指向将存储有关该模式信息的位置的指针（其大小取决于传入的标志参数！）。

调用 pcre_fullinfo 确定捕获模式计数非常容易：

```haskell
-- file: ch17/RegexExec.hs
capturedCount :: Ptr PCRE -> IO Int
capturedCount regex_ptr =
    alloca $ \n_ptr -> do
         c_pcre_fullinfo regex_ptr nullPtr info_capturecount n_ptr
         return . fromIntegral =<< peek (n_ptr :: Ptr CInt)
```

这需要一个原始 PCRE 指针并为匹配模式的 CInt 计数分配空间。然后我们调用信息函数并 peek 结果结构，找到一个 CInt。最后，我们将其转换为正常的 Haskell Int 并返回给用户。

### 使用子串进行模式匹配

现在让我们编写 regex 匹配函数。匹配函数的 Haskell 类型类似于编译正则表达式的类型：

```haskell
-- file: ch17/RegexExec.hs
match :: Regex -> ByteString -> [PCREExecOption] -> Maybe [ByteString]
```

这个函数是用户将编译后的正则表达式匹配字符串的方式。同样，主要的设计点是它是一个纯函数。匹配是一个纯函数：给定相同的输入正则表达式和主体字符串，它将始终返回相同的匹配子串。我们通过类型签名向用户传达此信息，指示当你调用此函数时不会发生副作用。

参数是编译后的 Regex、一个严格的 ByteString（包含输入数据）和一个在运行时修改正则表达式引擎行为的标志列表。结果要么是完全没有匹配（用 Nothing 值指示），要么只是匹配子串的列表。我们使用 Maybe 类型在类型中清楚地表明匹配可能失败。

使用严格的 ByteString 作为输入数据，我们可以提取恒定时间的匹配子串，不进行拷贝，这使接口相当高效。如果在输入中匹配了子串，偏移向量将填充主体字符串中整数偏移的对。我们需要循环遍历这个结果向量，读取偏移量，并逐步构建 ByteString 切片。

match 包装器的实现可以分为三个部分。在顶层，我们的函数分解编译后的 Regex 结构，产生底层 PCRE 指针：

```haskell
-- file: ch17/RegexExec.hs
match :: Regex -> ByteString -> [PCREExecOption] -> Maybe [ByteString]
match (Regex pcre_fp _) subject os = unsafePerformIO $ do
  withForeignPtr pcre_fp $ \pcre_ptr -> do
    n_capt <- capturedCount pcre_ptr
    let ovec_size = (n_capt + 1) * 3
        ovec_bytes = ovec_size * sizeOf (undefined :: CInt)
```

因为它是纯的，我们可以使用 unsafePerformIO 来隐藏任何内部分配效果。在模式匹配 PCRE 类型后，我们需要分解隐藏我们 C 分配的原始 PCRE 数据的 ForeignPtr。我们可以使用 withForeignPtr。这在调用期间保留与 PCRE 值关联的 Haskell 数据，防止它至少在此调用被使用时被收集。然后我们调用信息函数并使用该值计算偏移向量的大小（其公式在 PCRE 文档中给出）。我们需要的字节数是元素数乘以 CInt 的大小。要便携地计算 C 类型大小，Storable 类提供了一个 sizeOf 函数，它接受所需类型的任意值（我们可以在那里使用 undefined 值进行类型分派）。

下一步是分配我们计算大小的偏移向量，以便将输入 ByteString 转换为指向 C char 数组的指针。最后，我们用所有必需的参数调用 pcre_exec：

```haskell
-- file: ch17/RegexExec.hs
    allocaBytes ovec_bytes $ \ovec -> do
        let (str_fp, off, len) = toForeignPtr subject
        withForeignPtr str_fp $ \cstr -> do
            r <- c_pcre_exec
                         pcre_ptr
                         nullPtr
                         (cstr `plusPtr` off)
                         (fromIntegral len)
                         0
                         (combineExecOptions os)
                         ovec
                         (fromIntegral ovec_size)
```

对于偏移向量，我们使用 allocaBytes 来精确控制所分配数组的大小。它像 alloca，但不是使用 Storable 类来确定所需大小，而是采用要分配的字节数的显式大小。分解 ByteString，产生 ByteStrings 包含的底层内存指针，使用 toForeignPtr 完成，它将我们好的 ByteString 类型转换为托管指针。对结果使用 withForeignPtr 给出一个原始的 Ptr CChar，这正是我们需要传递给 C 的输入字符串。编程在 Haskell 通常只是解决类型谜题！

然后我们用原始 PCRE 指针、正确偏移量的输入字符串指针、其长度和结果向量指针调用 c_pcre_exec。返回一个状态代码，最后我们分析结果：

```haskell
-- file: ch17/RegexExec.hs
            if r < 0
                then return Nothing
                else let loop n o acc =
                            if n == r
                              then return (Just (reverse acc))
                              else do
                                    i <- peekElemOff ovec o
                                    j <- peekElemOff ovec (o+1)
                                    let s = substring i j subject
                                    loop (n+1) (o+2) (s : acc)
                     in loop 0 0 []
  where
    substring :: CInt -> CInt -> ByteString -> ByteString
    substring x y _ | x == y = empty
    substring a b s = end
        where
            start = unsafeDrop (fromIntegral a) s
            end   = unsafeTake (fromIntegral (b-a)) start
```

如果结果值小于零，则有错误或没有匹配，所以我们向用户返回 Nothing。否则，我们需要一个循环从偏移向量中 peek 偏移对（通过 peekElemOff）。这些偏移量用于查找匹配的子串。为了构建子串，我们使用一个辅助函数，给定起始和结束偏移量，删除主体字符串的周围部分，只留下匹配的部分。循环运行直到它提取了匹配器告诉我们找到的子串数。子串在尾递归循环中累积，构建每个字符串的反向列表。在将子串返回给用户之前，我们需要翻转该列表并将其包装在成功的 Just 标签中。让我们试试吧！

## 真实交易：编译和匹配正则表达式

如果我们取出这个函数及其周围的 hsc2hs 定义和数据包装，用 hsc2hs 处理它，我们可以在 GHCi 中加载生成的 Haskell 文件并尝试我们的代码（我们需要导入 Data.ByteString.Char8 以便我们可以从字符串字面值构建 ByteStrings）：

```sh
$ hsc2hs Regex.hsc
$ ghci Regex.hs -lpcre
*Regex> :t compile
compile :: ByteString -> [PCREOption] -> Either String Regex
*Regex> :t match
match :: Regex -> ByteString -> Maybe [ByteString]
```

事情似乎井然有序。现在让我们尝试一些编译和匹配。首先，一些简单的：

```ghci
*Regex> :m + Data.ByteString.Char8
*Regex Data.ByteString.Char8> let Right r = compile (pack "the quick brown fox") []
*Regex Data.ByteString.Char8> match r (pack "the quick brown fox") []
Just ["the quick brown fox"]
*Regex Data.ByteString.Char8> match r (pack "The Quick Brown Fox") []
Nothing
*Regex Data.ByteString.Char8> match r (pack "What
  do you know about the quick brown fox?") []
Just ["the quick brown fox"]
```

（我们也可以通过使用 OverloadedStrings 扩展避免 pack 调用）。或者我们可以更大胆：

```ghci
*Regex Data.ByteString.Char8> let Right r = compile
(pack "a*abc?xyz+pqr{3}ab{2,}xy{4,5}pq{0,6}AB{0,}zz") []
*Regex Data.ByteString.Char8> match r (pack "abxyzpqrrrabbxyyyypqAzz") []
Just ["abxyzpqrrrabbxyyyypqAzz"]
*Regex Data.ByteString.Char8> let Right r = compile
(pack "^([^!]+)!(.+)=apquxz\\.ixr\\.zzz\\.ac\\.uk$") []
*Regex Data.ByteString.Char8> match r (pack "abc!pqr=apquxz.ixr.zzz.ac.uk") []
Just ["abc!pqr=apquxz.ixr.zzz.ac.uk","abc","pqr"]
```

这相当棒。Perl 正则表达式的全部力量在 Haskell，就在你的指尖。

## 总结

在本章中，我们研究了如何声明允许 Haskell 代码调用 C 函数的绑定，如何在两种语言之间 marshal 不同数据类型，如何在低级分配内存（通过本地分配或通过 C 的内存管理），以及如何利用 Haskell 类型系统和垃圾收集器来自动化处理 C 的大部分艰苦工作。最后，我们看了 FFI 预处理器如何能减轻构建新绑定的大量劳动。结果是一个自然的 Haskell API，实际上主要在 C 中实现。

大多数 FFI 任务属于这些类别。我们无法涵盖的其他高级技术包括将 Haskell 链接到 C 程序、在一种语言和另一种语言之间注册回调，以及 c2hs 预处理工具。你可以在网上找到有关这些主题的更多信息。
