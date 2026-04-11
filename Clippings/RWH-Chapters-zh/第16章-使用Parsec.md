---
title: "第16章-使用Parsec"
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

# 第16章-使用Parsec

解析文件或各种类型的数据是程序员的常见任务。我们已经在"Haskell 中的正则表达式"一文中学习了 Haskell 对正则表达式的支持。正则表达式对许多任务来说很好用，但在处理复杂数据格式时，它们会很快变得笨拙，或者根本无法使用。

例如，我们不能使用正则表达式来解析大多数编程语言的源代码。

Parsec 是一个有用的解析器组合库，我们将小的解析函数组合起来构建更复杂的解析器。Parsec 提供了一些简单的解析函数，以及将它们连接在一起的函数。对于 Haskell 来说，这个解析器库围绕函数的概念构建也就不足为奇了。

了解 Parsec 与其他语言中用于解析的工具相比处于什么位置是有帮助的。解析有时分为两个阶段：词法分析（工具如 flex 的领域）和解析本身（由诸如 bison 的程序执行）。Parsec 可以执行词法分析和解析。

## Parsec 初步：简单 CSV 解析

让我们直接跳进去编写一些解析 CSV 文件的代码。CSV 文件通常用作电子表格或数据库的纯文本表示。每一行是一条记录，每条记录中的字段由逗号分隔。与处理包含逗号的字段有关的方法，但现在我们不用担心。

第一个例子比实际需要的要长得多。我们很快就会介绍更多 Parsec 特性，它们会将解析器缩减到只有四行！

```haskell
-- file: ch16/csv1.hs
import Text.ParserCombinators.Parsec
{- A CSV file contains 0 or more lines, each of which is terminated
   by the end-of-line character (eol). -}
csvFile :: GenParser Char st [[String]]
csvFile =
    do result <- many line
       eof
       return result
-- Each line contains 1 or more cells, separated by a comma
line :: GenParser Char st [String]
line =
    do result <- cells
       eol                       -- end of line
       return result

-- Build up a list of cells.  Try to parse the first cell, then figure out
-- what ends the cell.
cells :: GenParser Char st [String]
cells =
    do first <- cellContent
       next <- remainingCells
       return (first : next)
-- The cell either ends with a comma, indicating that 1 or more cells follow,
-- or it doesn't, indicating that we're at the end of the cells for this line
remainingCells :: GenParser Char st [String]
remainingCells =
    (char ',' >> cells)            -- Found comma?  More cells coming
    <|> (return [])                -- No comma?  Return [], no more cells
-- Each cell contains 0 or more characters, which must not be a comma or
-- EOL
cellContent :: GenParser Char st String
cellContent =
    many (noneOf ",\n")

-- The end of line character is \n
eol :: GenParser Char st Char
eol = char '\n'
parseCSV :: String -> Either ParseError [[String]]
parseCSV input = parse csvFile "(unknown)" input
```

让我们看看这个例子的代码。我们这里没有使用太多快捷方式，所以请记住这会变得更短更简单！

我们从上到下构建它，所以我们的第一个函数是 csvFile。这个函数的类型是 `GenParser Char st [[String]]`。这意味着输入的类型是字符序列，这正是 Haskell 字符串，因为 String 与 [Char] 相同。它还意味着我们将返回类型为 `[[String]]` 的值：字符串列表的列表。st 目前可以忽略。

Parsec 程序员经常省略类型声明，因为我们编写了太多小函数。Haskell 的类型推断可以算出来。我们为首例列出了类型，这里是为了让你更好地了解发生了什么。你也可以随时在 ghci 中使用 :t 来检查类型。

csvFile 使用 do 块。正如这所暗示的，Parsec 是一个 monadic 库：它定义了自己的特殊解析 monad，GenParser。

我们首先运行 many line。many 是一个接受函数作为参数的函数。它尝试使用传递给它的函数重复解析输入。它收集所有重复解析的结果并返回它们的列表。所以，这里我们将解析所有行的结果存储在 result 中。然后我们寻找称为 eof 的文件结束指示器。最后，我们返回结果。所以，CSV 文件由许多行组成，然后是文件结束。我们经常可以像这样用普通英语阅读 Parsec 函数。

现在我们必须回答：什么是行？我们定义 line 函数就是这样做的。阅读函数，我们可以看到一行由单元格后跟换行符组成。

那么单元格是什么？我们在 cells 函数中定义了它们。一行的单元格以第一个单元格的内容开始，然后是剩余单元格的内容（如果有的话）。结果只是将第一个单元格和剩余单元格组装成列表。

让我们跳过 remainingCells 一会儿，看看 cellContent。一个单元格包含任意数量的字符，但每个字符不能是逗号或换行符。noneOf 函数匹配一项，只要它不在我们传递的项目列表中。所以，说 `many (noneOf ",\n")` 定义了我们想要的单元格。

回到 remainingCells，我们有 Parsec 中选择的第一个例子。选择运算符是 `<|>`。这个运算符的行为是这样的：它将尝试左侧的解析器，如果它没有消费输入，则尝试右侧的解析器。

所以，在 remainingCells 中，我们的任务是提出第一个之后的所有单元格。回想一下 cellContent 使用 `noneOf ",\n"`。所以它不会从输入中消费逗号或换行符。如果我们解析一个单元格后看到逗号，意味着至少还有一个单元格跟随。否则，我们就完成了。所以，remainingCells 中的第一个选择是 `char ','`。这个解析器简单地匹配输入中传递的字符。如果我们找到逗号，我们希望这个函数返回该行上剩余的单元格。此时，"剩余单元格"看起来与行开头完全相同，所以我们递归调用 cells 来解析它们。如果我们没有找到逗号，我们返回空列表，表示该行上没有剩余的单元格。

最后，我们必须定义什么是行结束指示器。我们将其设置为 `char '\n'`，这目前很适合我们的目的。

在程序的最末尾，我们定义了一个函数 parseCSV，它接受一个 String 并将其解析为 CSV 文件。这个函数只是一个快捷方式，调用 Parsec 的 parse 函数，填充一些参数。parse 为 CSV 文件返回 `Either ParseError [[String]]`。如果出错，返回值将是带有错误的 Left；否则，将是带有结果的 Right。

* 有关 monads 的更多信息，请参阅第十四章。
† 有关处理在失败前可能消费一些输入的选择的信息，请参阅"Lookahead"。

现在我们理解了这个代码，让我们玩一玩看看它做什么：

```ghci
ghci> :l csv1.hs
[1 of 1] Compiling Main             ( csv1.hs, interpreted )
Ok, modules loaded: Main.
ghci> parseCSV ""
Loading package parsec-2.1.0.1 ... linking ... done.
Right []
```

这是有道理的——解析空字符串返回空列表。让我们尝试解析单个单元格：

```ghci
ghci> parseCSV "hi"
Left "(unknown)" (line 1, column 3):
unexpected end of input
expecting "," or "\n"
```

看那个。回想一下我们如何定义每行必须以换行符结束，而我们没有给它。Parsec 的错误消息很好地指出了问题的行号和列号，甚至还告诉了我们它期望什么！让我们给它一个换行符并继续实验：

```ghci
ghci> parseCSV "hi\n"
Right [["hi"]]
ghci> parseCSV "line1\nline2\nline3\n"
Right [["line1"],["line2"],["line3"]]
ghci> parseCSV "cell1,cell2,cell3\n"
Right [["cell1","cell2","cell3"]]
ghci> parseCSV "l1c1,l1c2\nl2c1,l2c2\n"
Right [["l1c1","l1c2"],["l2c1","l2c2"]]
ghci> parseCSV "Hi,\n\n,Hello\n"
Right [["Hi",""],[""],["","Hello"]]
```

你可以看到 parseCSV 正在做我们想要它做的事情。它甚至正确处理了空单元格和空行。

## sepBy 和 endBy 组合器

我们之前承诺通过使用一些 Parsec 辅助函数可以显著简化我们的 CSV 解析器。有两个可以大大简化这个代码。

第一个工具是 sepBy 函数。这个函数接受两个函数作为参数：第一个解析某种内容，而第二个解析分隔符。sepBy 首先尝试解析内容，然后是分隔符，轮流交替，直到无法解析分隔符。它返回所有能够解析的内容的列表。

第二个工具是 endBy。它类似于 sepBy，但期望最后一项后跟分隔符。也就是说，它继续解析直到无法解析更多内容。

所以，我们可以用 endBy 解析行，因为每一行必须以换行符结束。我们可以用 sepBy 解析单元格，因为最后一个单元格不会以逗号结尾。

看看我们的解析器现在有多简单：

```haskell
-- file: ch16/csv2.hs
import Text.ParserCombinators.Parsec
csvFile = endBy line eol
line = sepBy cell (char ',')
cell = many (noneOf ",\n")
eol = char '\n'
parseCSV :: String -> Either ParseError [[String]]
parseCSV input = parse csvFile "(unknown)" input
```

这个程序的行为与第一个完全相同。我们可以通过使用 ghci 重新运行 earlier example 中的示例来验证这一点。我们会从每一个得到相同的结果。然而程序更短更易读了。用不了多久你就可以将这样的 Parsec 代码翻译成普通英语的文件格式定义。

当你阅读这段代码时，你可以看到：

- CSV 文件包含零行或多行，每行以换行符终止。
- 一行包含一个或多个单元格，以逗号分隔。
- 一个单元格包含零个或多个字符，这些字符不能是逗号或换行符。
- 换行符是换行符，\n。

## 选择和错误

不同的操作系统使用不同的字符来标记行尾。Unix/Linux 系统和在文本模式下的 Windows 使用简单的 "\n"。DOS 和 Windows 系统使用 "\r\n"，Mac 传统上使用 "\r"。我们也可以添加对 "\n\r" 的支持，以防有人使用。

我们可以轻松地调整示例以能够处理单个文件中的所有这些类型的行尾。我们需要做两个修改：调整 eol 以识别不同的结尾，并调整 cell 中的 noneOf 模式以忽略 \r。

这必须小心完成。回想一下我们之前的 eol 定义只是 `char '\n'`。有一个称为 string 的解析器，我们可以用来匹配多字符模式。让我们首先考虑如何添加对 \n\r 的支持。

我们的第一个尝试可能看起来像这样：

```haskell
-- file: ch16/csv3.hs
-- This function is not correct!
eol = string "\n" <|> string "\n\r"
```

这不太正确。回想一下 `<|>` 运算符总是首先尝试左侧的选择。看着单个字符 \n 将匹配两种类型的行尾，所以它会看起来系统跟随的行以 \r 开头。不是我们想要的。在 ghci 中试试：

```ghci
ghci> :m Text.ParserCombinators.Parsec
ghci> let eol = string "\n" <|> string "\n\r"
Loading package parsec-2.1.0.1 ... linking ... done.
ghci> parse eol "" "\n"
Right "\n"
ghci> parse eol "" "\n\r"
Right "\n"
```

看起来解析器对两种结尾都起作用了，但实际上这样看，我们无法判断。如果它留下了一些未解析的东西，我们不知道，因为我们没有尝试从输入中消费任何其他东西。所以让我们在行尾之后寻找文件结尾：

```ghci
ghci> parse (eol >> eof) "" "\n\r"
Left (line 2, column 1):
unexpected "\r"
expecting end of input
ghci> parse (eol >> eof) "" "\n"
Right ()
```

正如所料，我们从 \n\r 结尾得到了错误。所以下一个诱惑可能是这样尝试：

```haskell
-- file: ch16/csv4.hs
-- This function is not correct!
eol = string "\n\r" <|> string "\n"
```

这也不对。回想一下 `<|>` 仅在左侧选项不消费输入时才尝试右侧的选项。但是当我们能够看到 \n 后面是否有 \r 时，我们已经消费了 \n。这次，我们在 ghci 的另一种情况下失败：

```ghci
ghci> :m Text.ParserCombinators.Parsec
ghci> let eol = string "\n\r" <|> string "\n"
Loading package parsec-2.1.0.1 ... linking ... done.
ghci> parse (eol >> eof) "" "\n\r"
Right ()
ghci> parse (eol >> eof) "" "\n"
Left (line 1, column 1):
unexpected end of input
expecting "\n\r"
```

我们遇到了 lookahead 问题。事实证明，在编写解析器时，能够" lookahead"即将到来的数据通常非常方便。Parsec 支持这一点，但在展示如何使用它之前，让我们看看你将如何编写它来凑合使用。你必须像这样手动展开 \n 后的所有选项：

```haskell
-- file: ch16/csv5.hs
eol =
    do char '\n'
       char '\r' <|> return '\n'
```

这个函数首先寻找 \n。如果找到，它会寻找 \r，如果可能就消费它。因为 char '\r' 的返回类型是 Char，替代 action 是简单返回一个 Char 而不尝试解析任何东西。Parsec 有一个函数 option 也可以表达这个习惯用法为 `option '\n' (char '\r')`。让我们用 ghci 测试一下：

```ghci
ghci> :l csv5.hs
[1 of 1] Compiling Main             ( csv5.hs, interpreted )
Ok, modules loaded: Main.
ghci> parse (eol >> eof) "" "\n\r"
Loading package parsec-2.1.0.1 ... linking ... done.
Right ()
ghci> parse (eol >> eof) "" "\n"
Right ()
```

这次，我们得到了正确的结果！但我们可以用 Parsec 的 lookahead 支持更简单地做到这一点。

### Lookahead

Parsec 有一个名为 try 的函数，用于表达 lookaheads。try 接受一个函数，一个解析器，然后应用它。如果解析器不成功，try 的行为就好像它根本没有消费任何输入。所以，当你在 `<|>` 的左侧使用 try 时，Parsec 将尝试右侧的选项，即使左侧在消费了一些输入后失败了。try 只在 `<|>` 左侧时有效果。不过，请记住，许多函数在内部使用 `<|>`。这里有一种使用 try 向 CSV 解析器添加扩展行尾支持的方法：

```haskell
-- file: ch16/csv6.hs
import Text.ParserCombinators.Parsec
csvFile = endBy line eol
line = sepBy cell (char ',')
cell = many (noneOf ",\n\r")
eol =   try (string "\n\r")
    <|> try (string "\r\n")
    <|> string "\n"
    <|> string "\r"
parseCSV :: String -> Either ParseError [[String]]
parseCSV input = parse csvFile "(unknown)" input
```

这里我们将两个字符的结尾放在前面，并对两个测试都运行 try。它们都出现在 `<|>` 的左侧，所以它们会做正确的事情。我们可以把 `string "\n"` 放在 try 中，但这不会改变任何行为，因为它们无论如何只查看一个字符。我们可以加载并在 ghci 中测试 eol 函数：

```ghci
ghci> :l csv6.hs
[1 of 1] Compiling Main             ( csv6.hs, interpreted )
Ok, modules loaded: Main.
ghci> parse (eol >> eof) "" "\n\r"
Loading package parsec-2.1.0.1 ... linking ... done.
Right ()
ghci> parse (eol >> eof) "" "\n"
Right ()
ghci> parse (eol >> eof) "" "\r\n"
Right ()
ghci> parse (eol >> eof) "" "\r"
Right ()
```

所有四种结尾都被正确处理了。你也可以像这样用一些不同的结尾测试完整的 CSV 解析器：

```ghci
ghci> parseCSV "line1\r\nline2\nline3\n\rline4\rline5\n"
Right [["line1"],["line2"],["line3"],["line4"],["line5"]]
```

正如你所看到的，这个程序甚至支持单个文件中的不同行尾。

## 错误处理

在本章开头，你看到了 Parsec 如何生成列出错误发生位置以及期望什么的错误消息。随着解析器变得更加复杂，期望的列表可能变得冗长。Parsec 提供了一种方法，让我们可以在解析失败时指定自定义错误消息。

让我们看看当我们当前的 CSV 解析器遇到错误时会发生什么：

```ghci
ghci> parseCSV "line1"
Left "(unknown)" (line 1, column 6):
unexpected end of input
expecting ",", "\n\r", "\r\n", "\n" or "\r"
```

这是一个相当长且技术性的错误消息。我们可以尝试使用 monad fail 函数来解决这个问题，像这样：

```haskell
-- file: ch16/csv7.hs
eol =   try (string "\n\r")
    <|> try (string "\r\n")
    <|> string "\n"
    <|> string "\r"
    <|> fail "Couldn't find EOL"
```

在 ghci 下，我们可以看到结果：

```ghci
ghci> :l csv7.hs
[1 of 1] Compiling Main             ( csv7.hs, interpreted )
Ok, modules loaded: Main.
ghci> parseCSV "line1"
Loading package parsec-2.1.0.1 ... linking ... done.
Left "(unknown)" (line 1, column 6):
unexpected end of input
expecting ",", "\n\r", "\r\n", "\n" or "\r"
  Couldn't find EOL
```

我们在错误结果中添加了一些，但没有真正帮助清理输出。Parsec 有一个 `<?>` 运算符，专为这些情况设计。它类似于 `<|>`，因为它首先尝试左侧的解析器。不是在失败时尝试另一个解析器，而是呈现错误消息。以下是我们将如何使用它：

```haskell
-- file: ch16/csv8.hs
eol =   try (string "\n\r")
    <|> try (string "\r\n")
    <|> string "\n"
    <|> string "\r"
    <?> "end of line"
```

现在，当你生成错误时，你会得到更有用的输出：

```ghci
ghci> :l csv8.hs
[1 of 1] Compiling Main             ( csv8.hs, interpreted )
Ok, modules loaded: Main.
ghci> parseCSV "line1"
Loading package parsec-2.1.0.1 ... linking ... done.
Left "(unknown)" (line 1, column 6):
unexpected end of input
expecting "," or end of line
```

这很有帮助！一般经验法则是你把你要找的东西的人类可读描述放在 `<?>` 的右边。

## 扩展示例：完整 CSV 解析器

我们之前的 CSV 示例有一个重要的缺陷——它们无法处理包含逗号的单元格。CSV 生成程序通常会将引号放在此类数据周围。但然后你又有另一个问题：如果单元格包含引号和逗号怎么办？在这些情况下，嵌入的引号会成对出现。

这是一个完整的 CSV 解析器。你可以从 ghci 使用它，或者如果你将其编译为独立程序，它将解析标准输入上的 CSV 文件并在输出上将其转换为不同格式：

```haskell
-- file: ch16/csv9.hs
import Text.ParserCombinators.Parsec
csvFile = endBy line eol
line = sepBy cell (char ',')
cell = quotedCell <|> many (noneOf ",\n\r")
quotedCell =
    do char '"'
       content <- many quotedChar
       char '"' <?> "quote at end of cell"
       return content
quotedChar =
        noneOf "\""
    <|> try (string "\"\"" >> return '"')
eol =   try (string "\n\r")
    <|> try (string "\r\n")
    <|> string "\n"
    <|> string "\r"
    <?> "end of line"
parseCSV :: String -> Either ParseError [[String]]
parseCSV input = parse csvFile "(unknown)" input
main =
    do c <- getContents
       case parse csvFile "(stdin)" c of
            Left e -> do putStrLn "Error parsing input:"
                         print e
            Right r -> mapM_ print r
```

这只是 21 行代码的完整功能 CSV 解析器，外加 10 行用于 parseCSV 和 main 实用函数。

让我们看看这个程序与之前版本的变化。首先，一个单元格现在可以是裸露单元格或带引号的单元格。我们首先给出 quotedCell 选项，因为如果单元格中的第一个字符是引号，我们希望遵循该路径。

quotedCell 以引号开始和结束，包含零个或多个字符。但是这些字符不能直接复制，因为它们可能包含嵌入的、成对出现的引号，所以我们定义了一个自定义 quotedChar 来处理它们。

当我们在引号单元格内处理字符时，我们首先说 `noneOf "\""`。这将匹配并返回任何单个字符，只要它不是引号。否则，如果是引号，我们查看是否有两个连续的引号。如果是，我们返回一个引号放到结果字符串中。

注意 quotedChar 中的 try 在 `<|>` 的右侧。回想一下我们说 try 只在 `<|>` 左侧时有效果。这个 try 确实出现在 `<|>` 的左侧，但必须在一个在 many 的实现内部。

这个 try 很重要。假设我们正在解析一个带引号的单元格，并且正在接近其结尾。后面会有另一个单元格。所以我们期望看到一个引号来结束当前单元格，后跟一个逗号。当我们点击 quotedChar 时，我们将失败 noneOf 测试并继续寻找两个连续的引号的测试。如果我们有引号，然后是逗号，我们也会失败。如果我们没有使用 try，我们会在此时崩溃并出现错误，说它期望第二个引号，因为第一个引号已经被消费了。由于我们使用 try，这被正确识别为单元格的一部分，所以它按预期终止了 many quotedChar 表达式。Lookahead 再次被证明非常有用，而且它如此容易添加的事实使其成为 Parsec 中一个了不起的工具。

我们可以用 ghci 在一些带引号的单元格上测试这个程序：

```ghci
ghci> :l csv9.hs
[1 of 1] Compiling Main             ( csv9.hs, interpreted )
Ok, modules loaded: Main.
ghci> parseCSV "\"This, is, one, big, cell\"\n"
Loading package parsec-2.1.0.1 ... linking ... done.
Right [["This, is, one, big, cell"]]
ghci> parseCSV "\"Cell without an end\n"
Left "(unknown)" (line 2, column 1):
unexpected end of input
expecting "\"\"" or quote at end of cell
```

让我们在一个真实的 CSV 文件上运行它。这是一个由电子表格程序生成的：

```
"Product","Price"
"O'Reilly Socks",10
"Shirt with ""Haskell"" text",20
"Shirt, ""O'Reilly"" version",20
"Haskell Caps",15
```

现在，我们可以在我们的测试程序下运行它并观察：

```sh
$ runhaskell csv9.hs < test.csv
["Product","Price"]
["O'Reilly Socks","10"]
["Shirt with \"Haskell\" text","20"]
["Shirt, \"O'Reilly\" version","20"]
["Haskell Caps","15"]
```

## Parsec 和 MonadPlus

Parsec 的 GenParser monad 是我们在"寻找替代方案"一文中介绍的 MonadPlus 类型类的实例。值 mzero 表示解析失败，而 mplus 使用 `(<|>)` 将两个替代解析组合为一个：

```haskell
-- file: ch16/ParsecPlus.hs
instance MonadPlus (GenParser tok st) where
    mzero = fail "mzero"
    mplus = (<|>)
```

## 解析 URL 编码的查询字符串

当我们在"高尔夫练习：关联列表"一文中介绍 application/x-www-form-urlencoded 文本时，我们提到我们将编写一个这些字符串的解析器。我们可以使用 Parsec 快速轻松地做到这一点。

每个键值对由 & 字符分隔：

```haskell
-- file: ch16/FormParse.hs
p_query :: CharParser () [(String, Maybe String)]
p_query = p_pair `sepBy` char '&'
```

注意在类型签名中，我们使用 Maybe 表示一个值：HTTP 规范不清楚键是否必须有关联的值，我们希望能够区分"无值"和"空值"：

```haskell
-- file: ch16/FormParse.hs
p_pair :: CharParser () (String, Maybe String)
p_pair = do
  name <- many1 p_char
  value <- optionMaybe (char '=' >> many p_char)
  return (name, value)
```

many1 函数类似于 many：它重复应用其解析器，返回结果列表。如果其解析器从不成功，many 将成功并返回空列表，而 many1 如果其解析器从不成功则将失败，否则返回至少一个元素的列表。

optionMaybe 函数修改解析器的行为。如果解析器失败，optionMaybe 不会：它返回 Nothing。否则，它用 Just 包装解析器的成功结果。这给了我们区分"无值"和"空值"的能力，正如我们之前提到的。

各个字符可以用几种方式编码：

```haskell
-- file: ch16/FormParse.hs
p_char :: CharParser () Char
p_char = oneOf urlBaseChars
     <|> (char '+' >> return ' ')
     <|> p_hex
urlBaseChars = ['a'..'z']++['A'..'Z']++['0'..'9']++"$-_.!*'(),"
p_hex :: CharParser () Char
p_hex = do
  char '%'
  a <- hexDigit
  b <- hexDigit
  let ((d, _):_) = readHex [a,b]
  return . toEnum $ d
```

某些字符可以按字面意思表示。空格特别处理，使用 + 字符。其他字符必须编码为 % 字符后跟两个十六进制数字。Numeric 模块的 readHex 将十六进制字符串解析为数字：

```ghci
ghci> parseTest p_query "foo=bar&a%21=b+c"
Loading package parsec-2.1.0.1 ... linking ... done.
[("foo",Just "bar"),("a!",Just "b c")]
```

尽管这个解析器很有吸引力且可读性强，但我们可以退后一步，重新审视一些构建模块，这会受益匪浅。

## 替代正则表达式进行随意解析

在许多流行语言中，人们倾向于使用正则表达式进行"随意"解析。众所周知，这非常棘手：难以编写，难以调试，几个月不关注后几乎无法理解，而且它们在失败时不提供错误消息。

如果我们能编写紧凑的 Parsec 解析器，我们将在可读性、表达力和错误报告方面有所收获。我们的解析器不会像正则表达式那样短，但它们足够接近，可以抵消正则表达式的大部分诱惑。

### 无变量解析

我们展示的一些解析器使用 do 记法并将中间解析的结果绑定到变量以供后续使用。这样的函数之一是 p_pair：

```haskell
-- file: ch16/FormParse.hs
p_pair :: CharParser () (String, Maybe String)
p_pair = do
  name <- many1 p_char
  value <- optionMaybe (char '=' >> many p_char)
  return (name, value)
```

我们可以使用 Control.Monad 中的 liftM2 组合器来摆脱对显式变量的需要：

```haskell
-- file: ch16/FormParse.hs
p_pair_app1 =
    liftM2 (,) (many1 p_char) (optionMaybe (char '=' >> many p_char))
```

这个解析器与 p_pair 具有完全相同的类型和行为，但它只有一行。与其使用"过程式"风格编写解析器，我们只是切换到强调我们正在应用解析器并组合其结果的编程风格。

我们可以将这种 applicative 风格编写解析器的方式走得更远。在大多数情况下，我们将获得的额外紧凑性不会以可读性为代价，超出初步理解的努力。

## 用于解析的 Applicative Functors

标准 Haskell 库包含一个名为 Control.Applicative 的模块，我们之前在"fmap 的中缀使用"一文中遇到过。该模块定义了一个名为 Applicative 的类型类，它代表一个 applicative functor。这比 functor 结构稍微多一些，但比 monad 少一些。它还定义了 Alternative，类似于 MonadPlus。

通常，我们认为介绍 applicative functors 的最好方式是让它们工作。理论上，每个 monad 都是一个 applicative functor，但不是每个 applicative functor 都是 monad。因为 applicative functors 在 monads 很久之后才被添加到标准 Haskell 库中，我们通常不能免费获得 Applicative 实例；经常，我们必须声明我们使用的 monad 是 Applicative 或 Alternative。

要为 Parsec 执行此操作，我们将编写一个小模块，我们可以导入而不是普通的 Parsec 模块：

```haskell
-- file: ch16/ApplicativeParsec.hs
module ApplicativeParsec
    (
      module Control.Applicative
    , module Text.ParserCombinators.Parsec
    ) where
import Control.Applicative
import Control.Monad (MonadPlus(..), ap)
-- Hide a few names that are provided by Applicative.
import Text.ParserCombinators.Parsec hiding (many, optional, (<|>))
-- The Applicative instance for every Monad looks like this.
instance Applicative (GenParser s a) where
    pure  = return
    (<*>) = ap
-- The Alternative instance for every MonadPlus looks like this.
instance Alternative (GenParser s a) where
    empty = mzero
    (<|>) = mplus
```

为方便起见，我们模块的导出部分导出我们从 Applicative 和 Parsec 模块导入的所有名称。因为我们在导入时隐藏了 Parsec 版本的 `<|>`，将要导出的是来自 Control.Applicative 的——正如我们所愿。

### 通过示例进行 Applicative 解析

我们将从头开始重写我们现有的表单解析器，从 p_hex 开始，它解析一个十六进制转义序列。以下是普通 do 记法风格的代码：

```haskell
-- file: ch16/FormApp.hs
p_hex :: CharParser () Char
p_hex = do
  char '%'
  a <- hexDigit
  b <- hexDigit
  let ((d, _):_) = readHex [a,b]
  return . toEnum $ d
```

这是我们的 applicative 版本：

```haskell
-- file: ch16/FormApp.hs
a_hex = hexify <$> (char '%' *> hexDigit) <*> hexDigit
    where hexify a b = toEnum . fst . head . readHex $ [a,b]
```

虽然各个解析器基本未动，但我们用来粘合它们的组合器发生了变化。唯一熟悉的是 `(<$>)`，我们已经知道它是 fmap 的同义词。

从我们的 Applicative 定义，我们知道 `(<*>)` 是 ap。

另一个不熟悉的组合器是 `(*>)`，它应用其第一个参数，丢弃其结果，然后应用第二个参数并返回其结果。换句话说，它类似于 `(>>)`。

### 关于角括号的有用提示

在我们继续之前，这里有一个有用的辅助工具，用于记住 Control.Applicative 中的组合器中所有角括号的用途：如果有一个角括号指向一侧，则应使用该侧的结果。

例如，`(*>)` 返回其右侧的结果；`(<*>)` 返回两侧的结果；而 `(<*)`——我们还没有见过——返回其左侧的结果。

虽然这里的概念应该主要从我们对 functors 和 monads 的 earlier 覆盖中熟悉，但我们将逐步讲解这个函数来解释发生了什么。

首先，为了掌握我们的类型，我们将 hexify 提升到顶层并赋予它一个签名：

```haskell
-- file: ch16/FormApp.hs
hexify :: Char -> Char -> Char
hexify a b = toEnum . fst . head . readHex $ [a,b]
```

Parsec 的 hexDigit 解析器解析单个十六进制数字：

```ghci
ghci> :type hexDigit
hexDigit :: CharParser st Char
```

因此，`char '%' *> hexDigit` 具有相同的类型，因为 `(*>)` 返回其右侧的结果。（CharParser 类型不过是 GenParser Char 的同义词。）

```ghci
ghci> :type char '%' *> hexDigit
char '%' *> hexDigit :: GenParser Char st Char
```

表达式 `hexify <$> (char '%' *> hexDigit)` 是一个解析器，它匹配 % 字符后跟 hexDigit，其结果是一个函数：

```ghci
ghci> :type hexify <$> (char '%' *> hexDigit)
hexify <$> (char '%' *> hexDigit) :: GenParser Char st (Char -> Char)
```

最后，`(<*>)` 应用其左侧的解析器，然后是右侧的解析器，然后将左侧解析结果的函数应用于右侧解析结果的值。

如果你能理解这个，你就已经理解了 `(<*>)` 和 ap 组合器——`(<*>)` 是提升到 applicative functors 的普通旧 `($)`，而 ap 是提升到 monads 的相同东西：

```ghci
ghci> :type ($)
($) :: (a -> b) -> a -> b
ghci> :type (<*>)
(<*>) :: (Applicative f) => f (a -> b) -> f a -> f b
ghci> :type ap
ap :: (Monad m) => m (a -> b) -> m a -> m b
```

接下来，我们将考虑 p_char 解析器：

```haskell
-- file: ch16/FormApp.hs
p_char :: CharParser () Char
p_char = oneOf urlBaseChars
     <|> (char '+' >> return ' ')
     <|> p_hex
urlBaseChars = ['a'..'z']++['A'..'Z']++['0'..'9']++"$-_.!*'(),"
```

在 applicative 风格中，这几乎保持不变，只是一种方便的表示法：

```haskell
-- file: ch16/FormApp.hs
a_char = oneOf urlBaseChars
     <|> (' ' <$ char '+')
     <|> a_hex
```

这里，`(<$)` 组合器如果右侧的解析器成功，则使用左侧的值。

最后，p_pair_app1 的等价物几乎相同：

```haskell
-- file: ch16/FormParse.hs
p_pair_app1 =
    liftM2 (,) (many1 p_char) (optionMaybe (char '=' >> many p_char))
```

我们所有改变的是用于提升的组合器——liftA 函数的行为与其 liftM 兄弟相同：

```haskell
-- file: ch16/FormApp.hs
a_pair :: CharParser () (String, Maybe String)
a_pair = liftA2 (,) (many1 a_char) (optionMaybe (char '=' *> many a_char))
```

## 解析 JSON 数据

为了更好地感受使用 applicative functors 进行解析，并探索 Parsec 的更多角落，我们将编写一个遵循 RFC 4627 定义的 JSON 解析器。

在顶层，JSON 值必须是对象或数组：

```haskell
-- file: ch16/JSONParsec.hs
p_text :: CharParser () JValue
p_text = spaces *> text
     <?> "JSON text"

    where text = JObject <$> p_object
             <|> JArray <$> p_array
```

这些在结构上相似，有一个开始字符，后跟一个或多个以逗号分隔的项目，后跟一个结束字符。我们通过编写一个小辅助函数来捕获这种相似性：

```haskell
-- file: ch16/JSONParsec.hs
p_series :: Char -> CharParser () a -> Char -> CharParser () [a]
p_series left parser right =
    between (char left <* spaces) (char right) $
            (parser <* spaces) `sepBy` (char ',' <* spaces)
```

这里，我们终于有了我们之前介绍的 `(<*)` 组合器的用武之地。我们使用它来跳过某些标记后可能存在的任何空白。有了这个 p_series 函数，解析数组很简单：

```haskell
-- file: ch16/JSONParsec.hs
p_array :: CharParser () (JAry JValue)
p_array = JAry <$> p_series '[' p_value ']'
```

处理 JSON 对象几乎不更复杂，只需要一点点额外努力来为对象的每个字段生成名称/值对：

```haskell
-- file: ch16/JSONParsec.hs
p_object :: CharParser () (JObj JValue)
p_object = JObj <$> p_series '{' p_field '}'
    where p_field = (,) <$> (p_string <* char ':' <* spaces) <*> p_value
```

解析单个值是调用现有解析器，然后使用适当的 JValue 构造函数包装其结果：

```haskell
-- file: ch16/JSONParsec.hs
p_value :: CharParser () JValue
p_value = value <* spaces
  where value = JString <$> p_string
            <|> JNumber <$> p_number
            <|> JObject <$> p_object
            <|> JArray <$> p_array
            <|> JBool <$> p_bool
            <|> JNull <$ string "null"
            <?> "JSON value"
p_bool :: CharParser () Bool
p_bool = True <$ string "true"
     <|> False <$ string "false"
```

choice 组合器允许我们将这种梯形替代表示为一个列表。它返回第一个成功解析器的结果：

```haskell
-- file: ch16/JSONParsec.hs
p_value_choice = value <* spaces
  where value = choice [ JString <$> p_string
                       , JNumber <$> p_number
                       , JObject <$> p_object
                       , JArray <$> p_array
                       , JBool <$> p_bool
                       , JNull <$ string "null"
                       ]
                <?> "JSON value"
```

这引导我们到两个最有趣的解析器，用于数字和字符串。我们先处理数字，因为它们更简单：

```haskell
-- file: ch16/JSONParsec.hs
p_number :: CharParser () Double
p_number = do s <- getInput
              case readSigned readFloat s of
                [(n, s')] -> n <$ setInput s'
                _         -> empty
```

我们的技巧是利用 Haskell 的标准数字解析库函数，它们在 Numeric 模块中定义。readFloat 函数读取一个无符号浮点数；readSigned 获取一个无符号数的解析器，并将其转换为一个可能带符号的数字解析器。

因为这些函数对 Parsec 一无所知，我们必须特别处理它们。Parsec 的 getInput 函数让我们直接访问 Parsec 的未消费输入流。如果 readSigned readFloat 成功，它返回解析后的数字和未解析输入的 rest。然后我们使用 setInput 将其作为 Parsec 的新未消费输入流返回。

解析字符串并不困难，只是详细：

```haskell
-- file: ch16/JSONParsec.hs
p_string :: CharParser () String
p_string = between (char '\"') (char '\"') (many jchar)
    where jchar = char '\\' *> (p_escape <|> p_unicode)
              <|> satisfy (`notElem` "\"\\")
```

我们可以在我们刚遇到的 choice 组合器的帮助下解析和解码转义序列：

```haskell
-- file: ch16/JSONParsec.hs
p_escape = choice (zipWith decode "bnfrt\\\"/" "\b\n\f\r\t\\\"/")
    where decode c r = r <$ char c
```

最后，JSON 允许我们将字符串中的 Unicode 字符编码为 \u 后跟四个十六进制数字：

```haskell
-- file: ch16/JSONParsec.hs
p_unicode :: CharParser () Char
p_unicode = char 'u' *> (decode <$> count 4 hexDigit)
    where decode x = toEnum code
              where ((code,_):_) = readHex x
```

与 monads 相比，applicative functors 缺少的唯一功能是能够将值绑定到变量，这里我们需要它以便能够验证我们正在尝试解码的值。

这是我们的解析器中我们需要使用 monadic 函数的地方。这种模式扩展到更复杂的解析器——我们只是偶尔需要 monads 提供的额外一点能力。

在撰写本文时，applicative functors 对 Haskell 来说仍然是相当新的，人们才开始探索除解析领域之外的可能用途。

## 解析 HTTP 请求

作为 applicative 解析的另一个例子，我们将开发一个基本的 HTTP 请求解析器：

```haskell
-- file: ch16/HttpRequestParser.hs
module HttpRequestParser
    (
      HttpRequest(..)
    , Method(..)
    , p_request
    , p_query
    ) where
import ApplicativeParsec
import Numeric (readHex)
import Control.Monad (liftM4)
import System.IO (Handle)
```

HTTP 请求由一个方法、一个标识符、一系列头部和一个可选主体组成。为简单起见，我们将专注于 HTTP 1.1 标准指定的六种方法类型中的两种。POST 方法有一个主体；GET 没有：

```haskell
-- file: ch16/HttpRequestParser.hs
data Method = Get | Post
          deriving (Eq, Ord, Show)
data HttpRequest = HttpRequest {
      reqMethod :: Method
    , reqURL :: String
    , reqHeaders :: [(String, String)]
    , reqBody :: Maybe String
    } deriving (Eq, Show)
```

因为我们以 applicative 风格编写，我们的解析器可以既简短又可读。也就是说，如果你已经习惯于 applicative 解析表示法：

```haskell
-- file: ch16/HttpRequestParser.hs
p_request :: CharParser () HttpRequest
p_request = q "GET" Get (pure Nothing)
        <|> q "POST" Post (Just <$> many anyChar)
  where q name ctor body = liftM4 HttpRequest req url p_headers body
            where req = ctor <$ string name <* char ' '
        url = optional (char '/') *>
              manyTill notEOL (try $ string " HTTP/1." <* oneOf "01")
              <* crlf
```

简而言之，q 辅助函数接受一个方法名称、要应用的类型构造函数和一个用于请求可选主体的解析器。url 辅助函数不尝试验证 URL，因为 HTTP 规范没有说明 URL 包含哪些字符。该函数只是消费输入，直到行结束或到达 HTTP 版本标识符。

## 回溯及其不满

try 组合器必须保留输入，以防它需要恢复它以便可以使用替代解析器。这种做法称为回溯。因为 try 必须保存输入，所以使用它很昂贵。在解析器中散布不必要的 try 使用是一种非常有效的减速方式，有时甚至达到不可接受的性能。

避免回溯需求的标准方法是整理解析器，以便我们可以仅使用单个输入标记决定它是否会成功或失败。在这种情况下，两个解析器消费相同的初始标记，所以我们将它们变成一个解析器：

```ghci
ghci> let parser = (++) <$> string "HT" <*> (string "TP" <|> string "ML")
ghci> parseTest parser "HTTP"
"HTTP"
ghci> parseTest parser "HTML"
"HTML"
```

更好的是，如果我们将不匹配的输入提供给它，Parsec 会给我们一个改进的错误消息：

```ghci
ghci> parseTest parser "HTXY"
parse error at (line 1, column 3):
unexpected "X"
expecting "TP" or "ML"
```

## 解析头部

跟随 HTTP 请求第一行的是零个或多个头部。头部以字段名开始，后跟冒号，后跟内容。如果跟随的行以空格开头，它们被视为当前内容的延续：

```haskell
-- file: ch16/HttpRequestParser.hs
p_headers :: CharParser st [(String, String)]
p_headers = header `manyTill` crlf
  where header = liftA2 (,) fieldName (char ':' *> spaces *> contents)
        contents = liftA2 (++) (many1 notEOL <* crlf)
                               (continuation <|> pure [])
        continuation = liftA2 (:) (' ' <$ many1 (oneOf " \t")) contents
        fieldName = (:) <$> letter <*> many fieldChar
        fieldChar = letter <|> digit <|> oneOf "-_"
crlf :: CharParser st ()
crlf = (() <$ string "\r\n") <|> (() <$ newline)
notEOL :: CharParser st Char
notEOL = noneOf "\r\n"
```

## 练习

1. 我们的 HTTP 请求解析器太简单了，在实际部署中无用。它缺少重要功能，甚至不能抵抗最基本的拒绝服务攻击。
   正确处理 Content-Length 字段（如果存在）。

2. 针对 naive Web 服务器的流行拒绝服务攻击只是发送不合理的长头部。单个头部可能包含数十或数百兆字节的垃圾文本，导致服务器耗尽内存。
   重组头部解析器，以便在任何行超过 4,096 个字符时失败。它必须在此发生时立即失败；它不能等到一行的结尾最终出现。

3. 添加处理 Transfer-Encoding: chunked 头部的能力（如果存在）。
   详见 RFC 2616 第 3.6.1 节（http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.6.1）。

4. 另一种流行的攻击是打开连接并使其空闲或极慢地发送数据。
   在 IO monad 中编写一个包装器，调用解析器。使用 System.Timeout 模块在解析器在 30 秒内未完成时关闭连接。
