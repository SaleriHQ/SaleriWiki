---
title: "第05章-编写库-处理JSON数据"
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

# 第五章：编写库：处理 JSON 数据

## JSON 快速导览

在本章中，我们将开发一个小型但完整的 Haskell 库。我们的库将操作和序列化一种称为 JSON（JavaScript 对象表示法）的流行形式的数据。

JSON 语言是一种用于存储和传输结构化数据的小巧简单表示——例如——通过网络连接。它最常用于将数据从 Web 服务传输到基于浏览器的 JavaScript 应用程序。JSON 格式在 http://www.json.org/ 描述，更详细的内容在 RFC 4627 (http://www.ietf.org/rfc/rfc4627.txt)。

JSON 支持四种基本类型的值——字符串、数字、布尔值和一个名为 null 的特殊值：

```
"a string" 12345 true null
```

该语言提供了两种复合类型：数组是值的有序序列，对象是名称/值对的无序集合。对象中的名称始终是字符串；对象或数组中的值可以是任何类型：

```
[-3.14, true, null, "a string"]
{"numbers": [1,2,3,4,5], "useful": false}
```

## 在 Haskell 中表示 JSON 数据

要在 Haskell 中处理 JSON 数据，我们使用代数数据类型来表示可能的 JSON 类型范围：

```haskell
-- file: ch05/SimpleJSON.hs
data JValue = JString String
            | JNumber Double
            | JBool Bool
            | JNull
            | JObject [(String, JValue)]
            | JArray [JValue]
              deriving (Eq, Ord, Show)
```

对于每个 JSON 类型，我们提供一个独特的值构造函数。其中一些构造函数有参数：如果我们想构造一个 JSON 字符串，我们必须提供一个 String 值作为 JString 构造函数的参数。

要开始尝试此代码，请在编辑器中保存文件 SimpleJSON.hs，切换到 ghci 窗口，并将文件加载到 ghci 中：

```ghci
ghci> :load SimpleJSON
[1 of 1] Compiling SimpleJSON       ( SimpleJSON.hs, interpreted )
Ok, modules loaded: SimpleJSON.
ghci> JString "foo"
JString "foo"
ghci> JNumber 2.7
JNumber 2.7
ghci> :type JBool True
JBool True :: JValue
```

我们可以看到如何使用构造函数来获取正常 Haskell 值并将其转换为 JValue。要做相反的事情，我们使用模式匹配。这里有一个我们可以添加到 SimpleJSON.hs 的函数，它将为我们从 JSON 值中提取字符串。如果 JSON 值实际上包含一个字符串，我们的函数将用 Just 构造函数包装该字符串；否则，它将返回 Nothing：

```haskell
-- file: ch05/SimpleJSON.hs
getString :: JValue -> Maybe String
getString (JString s) = Just s
getString _           = Nothing
```

当我们保存修改后的源文件时，我们可以在 ghci 中重新加载它并尝试新定义。（:reload 命令记住我们上次加载的源文件，因此我们不需要明确命名它。）

```ghci
ghci> :reload
Ok, modules loaded: SimpleJSON.
ghci> getString (JString "hello")
Just "hello"
ghci> getString (JNumber 3)
Nothing
```

再多一些访问器函数，我们就有了可以处理的一小段代码：

```haskell
-- file: ch05/SimpleJSON.hs
getInt (JNumber n) = Just (truncate n)
getInt _           = Nothing

getDouble (JNumber n) = Just n
getDouble _           = Nothing

getBool (JBool b) = Just b
getBool _         = Nothing

getObject (JObject o) = Just o
getObject _           = Nothing

getArray (JArray a) = Just a
getArray _          = Nothing

isNull v            = v == JNull
```

truncate 函数通过丢弃小数点后的数字将浮点数或有理数转换为整数：

```ghci
ghci> truncate 5.8
5
ghci> :module +Data.Ratio
ghci> truncate (22 % 7)
3
```

## Haskell 模块的解剖

Haskell 源文件包含单个模块的定义。模块让我们确定模块内部的哪些名称可以从其他模块访问。

源文件以模块声明开头。这必须先于源文件中的所有其他定义：

```haskell
-- file: ch05/SimpleJSON.hs
module SimpleJSON
    (
      JValue(..)
    , getString
    , getInt
    , getDouble
    , getBool
    , getObject
    , getArray
    , isNull
    ) where
```

module 这个词是保留的。它后面是模块的名称，必须以大写字母开头。源文件必须与其包含的模块名称具有相同的基础名称（后缀前的组件）。这就是为什么我们的文件 SimpleJSON.hs 包含名为 SimpleJSON 的模块。

模块名称后面是导出列表，括在括号中。where 关键字表示模块体遵循。

导出列表指示此模块中的哪些名称对其他模块可见。这让我们保持私有代码对外部世界隐藏。JValue 后面跟着的 (..) 特殊表示法表示我们正在导出类型及其所有构造函数。

导出类型的名称（即其类型构造函数）但不导出其值构造函数似乎很奇怪。执行此操作的能力很重要：它让我们向用户隐藏类型的细节，使类型抽象。如果我们看不到类型的值构造函数，我们就不能对该类型的值进行模式匹配，也不能构造该类型的新值。在本章后面，我们将讨论一些可能想要使类型抽象的情况。

如果我们从模块声明中省略导出（及其周围的括号），模块中的每个名称都将被导出：

```haskell
-- file: ch05/Exporting.hs
module ExportEverything where
```

要完全不导出名称（很少有用），我们使用一对括号编写一个空导出列表：

```haskell
-- file: ch05/Exporting.hs
module ExportNothing () where
```

## 编译 Haskell 源

除了 ghci 解释器，GHC 发行版还包括一个编译器 ghc，它生成本机代码。如果您已经熟悉命令行编译器如 gcc 或 cl（Microsoft Visual Studio 的 C++ 编译器组件），您将立即对 ghc 感到熟悉。

要编译源文件，我们首先打开终端或命令提示符窗口，然后使用要编译的源文件的名称调用 ghc：

```bash
ghc -c SimpleJSON.hs
```

-c 选项告诉 ghc 仅生成目标代码。如果我们省略 -c 选项，编译器将尝试生成完整的可执行文件。那会失败，因为我们已经编写了 main 函数，而 GHC 调用它来启动独立程序的执行。

当 ghc 完成时，如果列出目录的内容，它应该包含两个新文件：SimpleJSON.hi 和 SimpleJSON.o。前者是接口文件，其中 ghc 以机器可读形式存储关于我们模块导出的名称的信息。后者是目标文件，包含生成的本机代码。

## 生成 Haskell 程序和导入模块

现在我们已经成功编译了我们的最小库，我们将编写一个 tiny 程序来使用它。在文本编辑器中创建以下文件并将其保存为 Main.hs：

```haskell
-- file: ch05/Main.hs
module Main () where

import SimpleJSON

main = print (JObject [("foo", JNumber 1), ("bar", JBool False)])
```

注意模块声明后面的 import 指令。这表示我们想要获取从 SimpleJSON 模块导出的所有名称，并在我们的模块中使它们可用。任何 import 指令必须出现在模块开头的组中，在模块声明之后，但在所有其他代码之前。例如，我们不能将它们分散在整个源文件中。

我们对源文件和函数的命名选择是刻意的。要创建可执行文件，ghc 期望一个名为 Main 的模块，其中包含一个名为 main 的函数（main 函数是当我们构建程序时将在运行程序时被调用的函数）。

```bash
ghc -o simple Main.hs SimpleJSON.o
```

这次，当我们调用 ghc 时省略 -c 选项，所以它将尝试生成可执行文件。生成可执行文件的过程称为链接。正如我们的命令行所示，ghc 完全能够在一调用中既编译源文件又链接可执行文件。

我们向 ghc 传递一个新选项 -o，它接受一个参数：ghc 应该创建的可执行文件的名称。* 这里，我们决定将程序命名为 simple。在 Windows 上，程序将具有 .exe 后缀，但在 Unix 变体上，将没有后缀。

最后，我们提供新源文件 Main.hs 的名称，以及我们已经编译的目标文件 SimpleJSON.o。我们必须明确列出每个包含应该进入可执行文件的代码的源文件或目标文件。如果我们忘记了一个源文件或目标文件，ghc 会抱怨未定义的符号，这表示它需要的一些定义在我们提供的文件中没有提供。

在编译时，我们可以向 ghc 传递源文件和目标文件的任意混合。如果 ghc 注意它已经将源文件编译成目标文件，只有在我们修改了它的情况下才会重新编译源文件。

当 ghc 完成编译和链接我们的简单程序后，我们可以从命令行运行它。

## 打印 JSON 数据

现在我们有了 JSON 类型的 Haskell 表示，我们希望能够获取 Haskell 值并将其呈现为 JSON 数据。

有几种方法可以实现这一目标。最直接的可能是编写一个以 JSON 形式打印值的呈现函数。一旦完成，我们将探索一些更有趣的方法。

```haskell
-- file: ch05/PutJSON.hs
module PutJSON where

import Data.List (intercalate)
import SimpleJSON

renderJValue :: JValue -> String
renderJValue (JString s)   = show s
renderJValue (JNumber n)   = show n
renderJValue (JBool True)  = "true"
renderJValue (JBool False) = "false"
renderJValue JNull         = "null"
renderJValue (JObject o) = "{" ++ pairs o ++ "}"
  where pairs [] = ""
        pairs ps = intercalate ", " (map renderPair ps)
        renderPair (k,v)   = show k ++ ": " ++ renderJValue v
renderJValue (JArray a) = "[" ++ values a ++ "]"
  where values [] = ""
        values vs = intercalate ", " (map renderJValue vs)
```

良好的 Haskell 风格涉及将纯代码与执行 I/O 的代码分离。我们的 renderJValue 函数没有与外部世界的交互，但我们仍然需要能够打印 JValue：

```haskell
-- file: ch05/PutJSON.hs
putJValue :: JValue -> IO ()
putJValue v = putStrLn (renderJValue v)
```

打印 JSON 值现在很容易。

### 为什么要将呈现代码与实际打印值的代码分离？

这给了我们灵活性。例如，如果我们想在写出之前压缩数据并将呈现与打印混合，更改我们的代码以适应这种情况下会困难得多。

将纯代码与不纯代码分离的想法是强大的，它在 Haskell 代码中无处不在。存在几个 Haskell 压缩库，它们都有简单的接口：压缩函数接受未压缩的字符串并返回压缩的字符串。我们可以使用函数组合将 JSON 数据呈现为字符串，然后压缩成另一个字符串，推迟关于如何实际显示或传输数据的任何决定。

## 类型推断是一把双刃剑

Haskell 编译器推断类型的能力是强大而有价值的。早期，您很可能面临强烈的诱惑，通过省略尽可能多的类型声明来利用类型推断。让我们简单地让编译器找出全部吧！

在显式类型信息上偷工减料有一个缺点，一个不成比例地影响新 Haskell 程序员。作为这样的程序员，我们极有可能编写由于直接的类型错误而无法编译的代码。

当我们省略显式类型信息时，我们迫使编译器找出我们的意图。它将推断出合乎逻辑且一致的类型，但可能完全不是我们的意思。如果我们和编译器在发生了什么上不知不觉地不同意，我们自然需要更长时间才能找到问题的根源。

例如，假设我们编写一个我们认为返回 String 的函数，但没有为它写类型签名：

```haskell
-- file: ch05/Trouble.hs
upcaseFirst (c:cs) = toUpper c -- forgot ":cs" here
```

这里，我们想要大写一个单词的第一个字符，但我们忘记将单词的其余部分附加到结果上。我们认为函数的类型是 String -> String，但编译器将正确推断其类型为 String -> Char。假设我们然后尝试在其他地方使用此函数：

```haskell
-- file: ch05/Trouble.hs
camelCase :: String -> String
camelCase xs = concat (map upcaseFirst (words xs))
```

当我们尝试编译此代码或将其加载到 ghci 时，我们不一定会得到明显的错误消息：

```ghci
ghci> :load Trouble
[1 of 1] Compiling Main             ( Trouble.hs, interpreted )
Trouble.hs:9:27:
    Couldn't match expected type `[Char]' against inferred type `Char'
      Expected type: [Char] -> [Char]
      Inferred type: [Char] -> Char
    In the first argument of `map', namely `upcaseFirst'
    In the first argument of `concat', namely
        `(map upcaseFirst (words xs))'
Failed, modules loaded: none.
```

请注意，错误在我们使用 upcaseFirst 函数的地方报告。如果错误地确信我们的定义和 upcaseFirst 的类型是正确的，我们可能会在相当长一段时间内盯着错误的代码段，直到恍然大悟。

每次我们写一个类型签名，我们就从类型推断引擎中去除了一个自由度。这减少了我们对代码的理解与编译器之间的分歧可能性。类型声明也作为我们代码读者的速记，使我们更容易培养对必须发生的事情的感觉。

这并不是说我们需要在每个小代码片段中添加类型声明。但是，通常最好的做法是为代码中的每个顶层定义添加签名。最好在开始时相当积极地使用显式类型签名，然后随着你对类型检查如何工作的心智模型变得更准确，慢慢放松。

### 显式类型、undefined 值和 error

特殊值 undefined 无论在哪里使用都会愉快地通过类型检查，使用像 error "argh!" 这样的表达式也是如此。当我们使用这些时，编写类型签名尤为重要。假设我们在顶层定义的主体中使用 undefined 或 error "write me" 作为占位符。如果我们省略类型签名，我们可能能够在正确类型的版本会被编译器拒绝的地方使用我们定义的值。这很容易使我们误入歧途。

## 更通用的呈现观

我们的 JSON 呈现代码 narrowl 针对我们数据类型的确切需求和 JSON 格式约定。它产生的输出可能对人类眼睛不友好。我们现在将呈现视为更通用的任务：如何构建一个在各种情况下都有用的呈现数据的库？

我们希望产生适合人类消费（例如，用于调试）或机器处理的输出。执行此工作的库称为 pretty printers。有几个 Haskell pretty-printing 库已经存在。我们创建我们自己的不是为了替换它们，而是为了获得关于库设计和函数式编程技术的许多有用洞察。

我们将称我们通用 pretty-printing 模块为 Prettify，所以我们的代码将进入名为 Prettify.hs 的源文件。

### 命名

在我们的 Prettify 模块中，我们将基于几个已建立的 Haskell pretty-printing 库的名称，这将为我们提供与现有成熟库一定程度的兼容性。

为确保 Prettify 满足实际需求，我们编写了一个使用 Prettify API 的新 JSON 渲染器。完成后，我们将返回并填写 Prettify 模块的细节。

我们的 Prettify 模块不是直接呈现为字符串，而是使用一个我们称为 Doc 的抽象类型。通过在抽象类型之上构建我们的通用呈现库，我们可以选择灵活且高效的实现。如果我们决定更改底层代码，我们的用户将无法察觉。

我们将新的 JSON 呈现模块命名为 PrettyJSON.hs，并为呈现函数保留名称 renderJValue。呈现基本 JSON 值之一很简单：

```haskell
-- file: ch05/PrettyJSON.hs
renderJValue :: JValue -> Doc
renderJValue (JBool True)  = text "true"
renderJValue (JBool False) = text "false"
renderJValue JNull         = text "null"
renderJValue (JNumber num) = double num
renderJValue (JString str) = string str
```

我们的 Prettify 模块提供 text、double 和 string 函数。

## 开发 Haskell 代码而不发疯

早期，当我们掌握 Haskell 开发时，我们有如此多新的、不熟悉的概念需要一次跟踪，编写能够编译的代码可能是一个挑战。

当我们编写第一个实质性的代码体时，每隔几分钟暂停一下并尝试编译我们目前产生的东西是巨大的帮助。因为 Haskell 是如此强类型的，如果我们的代码干净地编译，我们确信我们没有走得太远进入编程杂草中。

快速开发程序骨架的一种有用技术是编写占位符或存根版本的类型和函数。例如，我们刚刚提到我们的 string、text 和 double 函数将由 Prettify 模块提供。如果我们不为这些函数或 Doc 类型提供定义，我们使用 JSON 渲染器的"早编译、频繁编译"的尝试将失败，因为编译器不会知道这些函数的任何信息。为避免此问题，我们编写不执行任何操作的存根代码：

```haskell
-- file: ch05/PrettyStub.hs
import SimpleJSON

data Doc = ToBeDefined
         deriving (Show)

string :: String -> Doc
string str = undefined

text :: String -> Doc
text str = undefined

double :: Double -> Doc
double num = undefined
```

### 点自由风格

这种完全作为其他函数组合编写定义的风格称为点自由风格。使用"点"这个词与用于函数组合的"."字符无关。在 Haskell 中，point 大致与 value 同义，所以点自由表达式不提及它操作的值。

将此点自由定义与"点"版本对比，后者使用变量 s 来引用其操作的值：

```haskell
-- file: ch05/PrettyJSON.hs
pointyString :: String -> Doc
pointyString s = enclose '"' '"' (hcat (map oneChar s))
```

enclose 函数简单地将开头和结尾字符包装在 Doc 值周围：

```haskell
-- file: ch05/PrettyJSON.hs
enclose :: Char -> Char -> Doc -> Doc
enclose left right x = char left <> x <> char right
```

我们在 pretty-printing 库中提供 (<>) 函数。它连接两个 Doc 值，所以它是 (++) 的 Doc 等价物：

```haskell
-- file: ch05/PrettyStub.hs
(<>) :: Doc -> Doc -> Doc
a <> b = undefined
```

char 函数：

```haskell
-- file: ch05/PrettyStub.hs
char :: Char -> Doc
char c = undefined
```

我们的 pretty-printing 库还提供 hcat，它将多个 Doc 值连接成一个——它是列表的 concat 类似物：

```haskell
-- file: ch05/PrettyStub.hs
hcat :: [Doc] -> Doc
hcat xs = undefined
```

我们的 string 函数将 oneChar 函数应用于字符串中的每个字符，连接全部结果，并用引号将其包围。oneChar 函数转义或呈现单个字符：

```haskell
-- file: ch05/PrettyJSON.hs
oneChar :: Char -> Doc
oneChar c = case lookup c simpleEscapes of
              Just r -> text r
              Nothing | mustEscape c -> hexEscape c
                      | otherwise    -> char c
    where mustEscape c = c < ' ' || c == '\x7f' || c > '\xff'

simpleEscapes :: [(Char, String)]
simpleEscapes = zipWith ch "\b\n\f\r\t\\\"/" "bnfrt\\\""
    where ch a b = (a, ['\\',b])
```

simpleEscapes 值是对列表。我们将对列表的对称为关联列表或简称 alist。我们 alist 的每个元素将字符与其转义表示相关联：

```ghci
ghci> take 4 simpleEscapes
[('\b',"\\b"),('\n',"\\n"),('\f',"\\f"),('\r',"\\r")]
```

我们的 case 表达式尝试查看我们的字符是否在此 alist 中有匹配。如果我们找到匹配，我们发出它；否则，我们可能需要以更复杂的方式转义字符。如果是这样，我们执行此转义。只有当不需要任何种类的转义时，我们才发出纯字符。为保守起见，我们发出的唯一未转义字符是可打印的 ASCII 字符。

更复杂的转义涉及将字符转换为 "\u" 后跟一个由表示 Unicode 字符数值价值的四位字符序列的十六进制数字：

```haskell
-- file: ch05/PrettyJSON.hs
smallHex :: Int -> Doc
smallHex x  = text "\\u"
           <> text (replicate (4 - length h) '0')
           <> text h
    where h = showHex x ""
```

showHex 函数来自 Numeric 库（您需要在 Prettify.hs 开头导入它），并返回数字的十六进制表示：

```ghci
ghci> showHex 114111 ""
"1bdbf"
```

replicate 函数由 Prelude 提供，并构建其参数的固定长度重复列表：

```ghci
ghci> replicate 5 "foo"
["foo","foo","foo","foo","foo"]
```

有一个问题：smallHex 提供的四位编码只能表示直到 0xffff 的 Unicode 字符。有效的 Unicode 字符可以高达 0x10ffff。要在 JSON 字符串中正确表示高于 0xffff 的字符，我们遵循一些复杂的规则将其拆分为两个，这为我们提供了一些 Haskell 数字的位级操作机会：

```haskell
-- file: ch05/PrettyJSON.hs
astral :: Int -> Doc
astral n = smallHex (a + 0xd800) <> smallHex (b + 0xdc00)
    where a = (n - 0x10000) `div` 0x400
          b = (n - 0x10000) `mod` 0x400
```

### 数组

现在我们已经涵盖了字符串，是时候呈现数组了。JSON 数组是一个值的有序列表，用方括号括起来，用逗号分隔：

```haskell
-- file: ch05/PrettyJSON.hs
renderJValue (JArray a) = text "[" <> value a <> text "]"
    where value [] = text ""
          value vs = text (foldr1 (<>) (map (renderJValue) vs))
```

我们使用 text 函数生成字面条形，并使用 (<>) 连接它们。foldr1 函数类似于 foldr，但适用于具有至少一个元素的列表，并且不存在空列表的情况：

```ghci
ghci> :type foldr1
foldr1 :: (a -> a -> a) -> [a] -> a
ghci> foldr1 (+) [1,2,3,4]
10
```

### 对象

JSON 对象是名称/值对的无序集合。在 JSON 中，对象以花括号包裹，名称和值用冒号分隔，对之间用逗号分隔：

```haskell
-- file: ch05/PrettyJSON.hs
renderJValue (JObject o) = text "{" <> members o <> text "}"
    where members [] = text ""
          members vs = text (foldr1 (<>) (map renderMember vs) <> ",")
          renderMember (k, v) = text (show k) <> text ": " <> renderJValue v
```

## Prettify 模块的实现

现在我们已经编写了使用 Prettify API 的代码，是时候实现实际的模块了。我们将把 Prettify 代码放在 Prettify.hs 中。

```haskell
-- file: ch05/Prettify.hs
module Prettify
    (
      Doc(..)
    , char
    , text
    , double
    , line
    ) where

data Doc = Empty
         | Char Char
         | Text String
         | Line
         | Concat Doc Doc
         | Union Doc Doc
           deriving (Show)

char :: Char -> Doc
char c = Char c

text :: String -> Doc
text "" = Empty
text s  = Text s

double :: Double -> Doc
double d = text (show d)

line :: Doc
line = Line

(<>) :: Doc -> Doc -> Doc
Empty <> y = y
x <> Empty = x
x <> y = Concat x y

hcat :: [Doc] -> Doc
hcat = fold (<>)

fold :: (Doc -> Doc -> Doc) -> [Doc] -> Doc
fold f [] = Empty
fold f (x:xs) = x `f` fold f xs

hsep :: [Doc] -> Doc
hsep = fold (<+>)

(<+>) :: Doc -> Doc -> Doc
x <+> y = x <> text " " <> y
```

## 更好的 API

我们已经实现了一个简单的 Prettify 模块，但我们可以通过提供更多有用的函数使其更易用。

```haskell
-- file: ch05/Prettify.hs
pretty :: Int -> Doc -> String
pretty w x = best 0 [x]
    where best col (d:ds) = case d of
                              Empty -> best col ds
                              Char c -> c : best (col + 1) ds
                              Text s -> s ++ best (col + length s) ds
                              Line -> '\n' : best 0 ds
                              Concat x y -> best col (x:y:ds)
                              Union x y -> best col (choose col x y:ds)
          best _ _ = ""
```

## 练习

1. JSON 数组不能包含 null 值吗？修改 SimpleJSON.hs 数据类型以允许 JNull 存在于 JArray 中。

2. 在 JSON 中，对象的键必须是字符串，但值可以是任何 JSON 类型。修改我们的 JObject 类型以反映此约束。

3. 编写一个函数，从 JValue 返回所有可能的路径到字符串值。例如，给定值 `JObject [("name", JString "John"), ("age", JNumber 30)]`，返回列表 `["name"]`。

4. 编写一个函数，展平 JArray 中的所有字符串。例如，`JArray [JString "a", JArray [JString "b", JString "c"]]` 变成 `["a", "b", "c"]`。

5. 使用模式匹配实现 JValue 的 Eq 实例。

## 总结

在本章中，我们构建了一个处理 JSON 数据的小型 Haskell 库。我们涵盖了：

- 如何使用代数数据类型表示 JSON 值的类型
- 如何编写访问器函数以从 JSON 值中提取数据
- Haskell 模块的工作原理以及如何导出和导入函数
- 如何使用 GHC 编译和链接程序
- 如何使用类型推断和类型签名的良好实践
- 如何使用抽象类型（如 Doc）构建灵活的库
- 如何使用点自由风格编写简洁的代码

在下一章中，我们将探索 Haskell 类型系统更强大的特性之一：类型类。
