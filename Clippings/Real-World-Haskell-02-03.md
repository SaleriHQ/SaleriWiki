# Real World Haskell

## 第二章：类型与函数

> 原文：Real World Haskell, Chapter 2 — Types and Functions
> 来源：http://book.realworldhaskell.org/read/types-and-functions.html

---

### 为什么关心类型？

Haskell 中每个表达式和函数都有一个类型。例如，值 `True` 的类型是 `Bool`，`"foo"` 的类型是 `String`。值的类型表明它与同一类型的其他值共享某些属性——比如我们可以相加数字、拼接列表，这些都是那些类型的属性。我们说一个表达式"具有类型 X"，或"属于类型 X"。

在深入讨论 Haskell 类型系统之前，先聊聊为什么要关心类型——类型究竟有什么用？在最底层，计算机只关心字节，几乎没有额外的结构。类型系统给我们的是**抽象**。类型为原始字节赋予了意义：它让我们可以说"这些字节是文本"、"那些字节是机票预订"等等。类型系统通常还会更进一步，防止我们意外混用不同类型。例如，类型系统通常不会允许我们把酒店预订当作租车收据来处理。

引入抽象的好处是，它让我们可以忽略或无视底层细节。如果我知道程序中的某个值是字符串，就不需要知道字符串的具体实现细节，可以直接假设它和其他字符串的行为一致。

不同类型系统关注的问题往往不同。一门编程语言的类型系统会深刻影响我们思考和编写代码的方式。Haskell 的类型系统让我们能够以非常抽象的层次思考，并写出简洁而强大的程序。

---

### Haskell 的类型系统

Haskell 的类型有三个有趣的特性：**强类型**、**静态类型**和**自动类型推断**。

#### 强类型

当说 Haskell 拥有强类型系统时，意思是类型系统保证程序不会包含某些类型的错误。这些错误来自于试图写无意义的表达式，比如把整数当作函数使用。例如，如果一个函数期望处理整数，而我们传入一个字符串，Haskell 编译器会拒绝编译。

我们把符合语言类型规则的表达式称为**类型良好**（well typed）的。违反类型规则的表达式是**类型错误**（ill typed）的，会导致类型错误。

Haskell 强类型的另一个方面是，它不会自动将值从一种类型转换为另一种类型（强制转换）。例如，C 编译器会在函数期望 `float` 类型参数时，自动静默地将 `int` 类型的值转换为 `float`；而 Haskell 编译器在类似情况下会报编译错误。我们必须通过显式应用转换函数来进行类型转换。

强类型确实偶尔会让写某些代码变得更困难。例如，在 C 语言中，一个经典做法是拿到字节数组后将其强制转换为看起来像是复杂数据结构的字节。这非常高效，因为不需要复制字节。但 Haskell 的类型系统不允许这种强制转换。要获得相同的结构化视图，需要进行一些复制，会有一点性能损耗。

强类型的巨大好处是，它能在 bug 引发问题之前就将其捕获。例如，在强类型语言中，我们不会意外地把字符串用在期望整数的地方。

**关于强与弱的补充说明**：在学术计算机科学中，强类型和弱类型有狭义的技术含义。类型系统的"强度"指的是它的宽松程度——较弱的类型系统会把更多表达式视为有效的。Perl 中 `"foo" + 2` 的结果是 `2`，而 `"13foo" + 2` 的结果是 `15`；Haskell 则会拒绝这两个表达式，因为 `(+)` 运算符要求两个操作数都是数值类型。由于 Perl 的类型系统比 Haskell 更宽松，按照这个狭义技术解释，我们说 Perl 更"弱"。

#### 静态类型

拥有静态类型系统意味着，编译器在代码执行之前就知道每个值和表达式的类型。Haskell 编译器或解释器会检测我们是否试图使用类型不匹配的值，并在运行前拒绝代码：

```haskell
ghci> True && "false"
<interactive>:1:8:
    Couldn't match expected type `Bool' against inferred type `[Char]'
    In the second argument of `(&&)', namely `"false"'
    In the expression: True && "false"
```

编译器推导出了表达式 `"false"` 的类型是 `[Char]`。`(&&)` 运算符要求每个操作数都是 `Bool` 类型，左操作数确实符合。由于 `"false"` 的实际类型与要求的类型不匹配，编译器拒绝了这个表达式。

静态类型有时确实会让编写某些有用的代码变得困难。在 Python 等语言中，**鸭子类型**（duck typing）很常见——一个对象只要表现得足够像另一个对象，就可以作为替代品。好在 Haskell 的**类型类**（typeclass）系统（将在第6章介绍）以安全、便捷的形式提供了动态类型几乎所有的好处。

Haskell 静态类型和强类型的结合，使得类型错误不可能在运行时发生。虽然这意味着需要多做一点前期思考，但也消除了许多本来可能极难发现的简单错误。Haskell 社区有句格言：**代码一旦编译通过，就更可能正确运行**。（更现实的说法可能是：Haskell 代码的 trivial bug 往往更少。）

用动态类型语言编写的程序需要大量的测试用例来确保不会发生简单的类型错误。测试套件无法提供完整的覆盖率——一些常见任务（如重构程序使其更加模块化）可能会引入测试套件可能无法发现的新类型错误。在 Haskell 中，编译器为我们证明了类型错误的不存在：一旦 Haskell 程序编译通过，运行时就绝不会出现类型错误。重构通常只是移动代码、重新编译、稍作整理，直到编译器给出"全部通过"。

一个帮助理解静态类型价值的比喻：把它想象成拼图。在 Haskell 中，如果一块拼图的形状不对，就根本塞不进去。在动态类型语言中，所有拼块都是 1×1 的小方块，永远能塞进去，所以你必须不断检查结果图片（通过测试）来判断是否正确。

#### 类型推断

最后，Haskell 编译器可以自动推断程序中**几乎所有**表达式的类型。这个过程称为**类型推断**（type inference）。Haskell 允许我们显式声明任何值的类型，但有了类型推断，这几乎总是可选的，而非必须。

**对类型系统的期望**：我们探索 Haskell 类型系统主要能力和好处的旅程将跨越多个章节。早期可能会觉得 Haskell 的类型有点麻烦——不像 Python 或 Ruby 那样写完代码就能跑去看结果，而是必须先让程序通过类型检查器的审查。为什么要忍受这个学习曲线？

虽然强静态类型让 Haskell 安全，类型推断让 Haskell 简洁。最终结果是：我们得到了一门比流行静态类型语言更安全、比动态类型语言表现力更强的语言。这是一个大胆的主张，我们会在整本书中用证据来支撑它。

修复类型错误一开始可能感觉比使用动态语言更费劲。不妨把这看作是把大量调试工作提前了——编译器会指出代码中的许多逻辑缺陷，而不是让我们在运行时跌跌撞撞地发现问题。

而且，由于 Haskell 能推断表达式和函数的类型，我们无需像较弱静态类型语言那样大量"打字"，就能享受静态类型的好处。在其他语言中，类型系统服务于编译器的需求。在 Haskell 中，类型系统为你服务。

---

### 常见基本类型

以下是一些最常见的基础类型：

| 类型 | 说明 |
|------|------|
| `Char` | 表示一个 Unicode 字符 |
| `Bool` | 布尔逻辑值，值为 `True` 或 `False` |
| `Int` | 有符号定宽整数。32 位机器上通常是 32 位，64 位机器上是 64 位。Haskell 标准只保证 `Int` 宽于 28 位 |
| `Integer` | 无界有符号整数。性能开销比 `Int` 大，但不会静默溢出，答案更可靠 |
| `Double` | 浮点数，通常是 64 位，使用系统的原生浮点表示 |

类型注解（type annotation）的写法：`expression :: MyType`。`::` 和后面类型的组合称为**类型签名**（type signature）。

---

### 函数应用

在 Haskell 中应用函数，直接写函数名，后跟参数，不需要括号或逗号：

```haskell
ghci> odd 3
True
ghci> compare 2 3
LT
ghci> compare 3 3
EQ
```

函数应用的优先级高于运算符，所以以下两表达式含义相同：

```haskell
ghci> (compare 2 3) == LT
True
ghci> compare 2 3 == LT
True
```

有时必须用括号来明确解析复杂表达式：

```haskell
ghci> compare (sqrt 3) (sqrt 6)
LT
```

---

### 有用的复合数据类型：列表与元组

复合数据类型由其他类型构造而来。Haskell 中最常见的复合类型是**列表**和**元组**。

列表类型是**多态**的——列表中的值可以是任意类型。用类型变量（必须以小写字母开头）来表示多态类型：

```haskell
ghci> :type last
last :: [a] -> a
```

类型 `[a]` 表示"类型 a 的列表"。类型变量 `a` 是一个占位符，之后会替换为具体类型。

**元组**是固定大小的值集合，每个值可以是不同类型。这与列表不同——列表可以任意长度，但所有元素必须类型相同：

```haskell
ghci> (1964, "Labyrinths")
(1964,"Labyrinths")
ghci> :type (True, "hello")
(True, "hello") :: (Bool, [Char])
```

元组类型表示其中元素的**数量、位置和类型**。元素数量或类型不同的元组具有不同类型；即使类型相同但顺序不同，也是不同的类型：

```haskell
ghci> (False, 'a') :: (Bool, Char)
ghci> ('a', False) :: (Char, Bool)  -- 不同类型！
```

元组中零元素有一种特殊类型 `()`，读作"单元"（unit），类似于 C 中的 `void`。

**元组不是可变列表**：与 Python 不同，Haskell 中的元组和列表**不是**可互换的。

---

### 函数类型与纯度

看看一个函数的类型：

```haskell
ghci> :type lines
lines :: String -> [String]
```

`->` 读作"返回"。这个签名可以解读为：lines 接收一个 String，返回一个 String 列表。

**副作用**（side effect）是指函数行为与系统全局状态之间的依赖关系。在 Haskell 中，**默认情况下函数没有副作用**：函数的结果只取决于我们显式提供的输入。我们称这类函数为**纯函数**（pure function），有副作用的函数是**非纯的**（impure）。

如果函数有副作用，通过阅读类型签名就能看出来——返回类型以 `IO` 开头：

```haskell
ghci> :type readFile
readFile :: FilePath -> IO String
```

Haskell 的类型系统防止我们意外混用纯代码和非纯代码。

---

### Haskell 源文件与简单函数

在 `.hs` 文件中定义函数：

```haskell
-- file: ch03/add.hs
add a b = a + b
```

等号左边是函数名和参数，右边是函数体。Haskell 没有 `return` 关键字——函数是一个表达式，其值就是结果。

**变量是什么？** 在 Haskell 中，变量给表达式提供了一个名称。一旦变量绑定到某个表达式，它的值就不会改变。`x = 10` 后再写 `x = 11` 会导致编译错误——**不能对同一变量赋值两次**。

---

### 条件求值

Haskell 的 `if` 表达式：

```haskell
-- file: ch02/myDrop.hs
myDrop n xs = if n <= 0 || null xs
              then xs
              else myDrop (n - 1) (tail xs)
```

`if` 后跟三个部分：
- **谓词**（predicate）：类型为 `Bool` 的表达式
- **then 分支**：谓词为 `True` 时的值
- **else 分支**：谓词为 `False` 时的值

> 注意：Haskell 是表达式导向的语言，`if` 必须有 `else`——因为 `if` 表达式必须有个结果。

---

### 通过示例理解求值

#### 惰性求值

在严格求值（strict evaluation）的语言中，会先求子表达式 `1 + 2` 的值，然后再应用函数。Haskell 选择了**非严格求值**（nonstrict evaluation）。

在 Haskell 中，子表达式 `1 + 2` 不会被立刻求值为 `3`。相反，我们创建了一个"承诺"（promise）——当需要 `isOdd (1 + 2)` 的值时再去计算它。用于跟踪未求值表达式的记录称为**thunk**。如果这个表达式的结果从未被使用，就根本不会计算它。

非严格求值通常称为**惰性求值**（lazy evaluation）。

#### `myDrop` 的完整求值过程

以 `myDrop 2 "abcd"` 为例：

1. 应用 `myDrop`：将 `n` 绑定到 `2`，`xs` 绑定到 `"abcd"`
2. 求值谓词 `2 <= 0 || null "abcd"`，结果为 `False`
3. 进入 else 分支：`myDrop (2-1) (tail "abcd")`
4. 重复递归，每次移除一个字符
5. 最终返回 `"cd"`

**短路求值是"免费"的**：`(||)` 运算符在 Haskell 中是普通函数，惰性求值天然支持短路特性：

```haskell
newOr a b = if a then a else b
```

如果 `a` 为 `True`，永远不会求值 `b`。如果 `b` 是 `length [1..] > 0` 这样的无限列表，就不会陷入无限循环。

---

### Haskell 中的多态性

列表类型是多态的。类型签名中的类型变量表示泛型：

```haskell
ghci> :type last
last :: [a] -> a
```

`a` 是类型变量，读作："接收一个类型为 [a] 的列表，返回一个类型为 a 的值"。

当函数签名中包含类型变量时，我们称该函数是**多态的**（polymorphic）。这种多态性称为**参数多态**（parametric polymorphism）。

> **为什么重要**：参数多态使得代码"对类型不关心"——无法创建、无法检查该类型的值，只能将其当作完全抽象的"黑盒"。

Haskell 不支持以下多态形式：
- **子类型多态**（如面向对象语言的继承）
- **强制转换多态**（如整数自动转浮点数）

---

### 推理多态函数

通过类型签名可以推理函数行为。例如 `fst :: (a, b) -> a`：

- `fst` 没有足够信息来构造一个 `a` 类型的值
- 也不能把 `a` 转成 `b`
- 因此唯一可能的有效行为（忽略无限循环或崩溃）是**返回元组的第一个元素**

> 学术成果：任何非病态的 `(a,b) -> a` 类型的函数都必然与 `fst` 的行为完全一致。Philip Wadler 的论文 "Theorems for free" 深入探讨了这一推理过程。

---

### 多参数函数的类型

```haskell
ghci> :type take
take :: Int -> [a] -> [a]
```

`->` 是右结合的。这个类型等价于：

```haskell
take :: Int -> ([a] -> [a])
```

即：`take` 接收一个 `Int`，返回一个**函数**，该函数接收一个列表并返回一个列表。这就是**柯里化**（currying）的核心，将在后续章节详细讨论。

---

### 纯度的价值

纯函数的结果只能依赖其参数。仅通过函数名和类型签名就能推断出纯函数的行为：

```haskell
ghci> :type not
not :: Bool -> Bool
```

仅凭此签名，`not` 可能的有效行为只有三种：
- 忽略参数，总是返回 `True` 或 `False`
- 原样返回参数
- 对参数取反

纯函数**不能**访问文件、网络或获取当前时间。纯代码本质上是模块化的——每个函数都是自包含的。纯度带来的一个不那么显而易见的好处是，处理非纯代码反而更容易了——Haskell 鼓励我们将必须有副作用的代码与不需要副作用的代码分离，非纯代码往往简洁而"重活"都在纯代码中完成。

---

## 第三章：定义类型、简化函数

> 原文：Real World Haskell, Chapter 3 — Defining Types, Streamlining Functions
> 来源：http://book.realworldhaskell.org/read/defining-types-streamlining-functions.html

---

### 定义新数据类型

虽然列表和元组很有用，但通常需要构造自己的数据类型。这让我们可以为程序中的值添加结构，给一组相关值起个名字并赋予其独立类型。定义自己的类型还能提高代码的类型安全性——Haskell 不会允许我们意外混用两个结构相似但名称不同的类型。

用 `data` 关键字定义新数据类型：

```haskell
-- file: ch03/BookStore.hs
data BookInfo = Book Int String [String]
                deriving (Show)
```

- `BookInfo` 是**类型构造器**（type constructor），必须以大写字母开头
- `Book` 是**值构造器**（value constructor / data constructor），也必须以大写字母开头
- `Int`、`String`、`[String]` 是**组件**（component），即字段（field）

类型构造器和值构造器在不同的命名空间，可以同名：

```haskell
data BookReview = BookReview BookInfo CustomerID String
```

这是常见且完全合法的习惯用法。

---

### 类型别名

`type` 关键字用于创建类型别名，仅为提高可读性，不创建新类型：

```haskell
type CustomerID = Int
type ReviewBody = String
type BookRecord = (BookInfo, BookReview)
```

---

### 代数数据类型

**代数数据类型**（Algebraic Data Type，ADT）可以拥有多个值构造器，用 `|` 分隔（读作"或"）：

```haskell
data Bool = False | True
data BillingInfo = CreditCard CardNumber CardHolder Address
                 | CashOnDelivery
                 | Invoice CustomerID
                   deriving (Show)
```

每个值构造器可以有零个或多个参数：
- `CreditCard`：接收三个参数（卡号、持卡人、地址）
- `CashOnDelivery`：无参数，表示"货到付款"
- `Invoice`：接收一个参数（客户 ID）

#### 枚举类型

ADT 也用作枚举：

```haskell
data Roygbiv = Red | Orange | Yellow | Green | Blue | Indigo | Violet
               deriving (Eq, Show)
```

与 C 的 `enum` 不同，Haskell 的枚举值**不能**隐式转换为整数——类型安全！

#### 代数数据类型与其他语言的类比

| Haskell ADT | C/C++ 对应 |
|-------------|-----------|
| 单构造器 + 多字段 | `struct`（结构体） |
| 无参构造器枚举 | `enum`（枚举） |
| 多构造器 |  discriminated union（带标记的联合体） |

以 C discriminated union 为例，需要额外字段来手动追踪当前使用的是哪个分支；而 Haskell 中哪个构造器被使用是**内置于值本身**的：

```haskell
-- C 需要手动追踪类型标签
enum shape_type { shape_circle, shape_poly };
struct shape { enum shape_type type; union { ... } shape; };

-- Haskell 优雅得多
data Shape = Circle Vector Double
           | Poly [Vector]
```

---

### 模式匹配

模式匹配让我们得以**查看值内部**并绑定变量：

```haskell
myNot True  = False
myNot False = True

sumList (x:xs) = x + sumList xs
sumList []     = 0
```

**构造（construction）和解构（deconstruction）** 是互逆的：用值构造器创建值，用模式匹配反向提取值：

```haskell
bookID (Book id title authors) = id
bookTitle (Book id title authors) = title
bookAuthors (Book id title authors) = authors
```

**通配符模式** `_` 匹配任何内容，但不绑定变量：

```haskell
nicerID (Book id _ _) = id
```

**注意**：
- 模式按从上到下顺序检查，匹配成功即停止
- 列表字面量 `[1,2]` 等价于 `(1:(2:[]))`
- 字面量模式（如 `3`）要求完全匹配
- 变量名在模式中只能出现一次——不能在多处绑定同一变量来表示"这两个值应该相同"

#### 穷尽匹配与警告

GHC 提供编译选项 `-fwarn-incomplete-patterns`，会在模式不穷举时给出警告。**必须覆盖所有构造器**，否则会导致运行时错误：

```haskell
-- 缺少 [] 分支，运行时崩溃！
badExample (x:xs) = x + badExample xs
ghci> badExample []
*** Exception: BadPattern.hs:4:0-36: Non-exhaustive patterns in function badExample
```

---

### 记录语法

手动写访问函数是重复劳动。Haskell 提供了**记录语法**，同时定义类型和访问函数：

```haskell
data Customer = Customer {
      customerID      :: CustomerID
    , customerName    :: String
    , customerAddress :: Address
    } deriving (Show)
```

Haskell 自动生成 `customerID`、`customerName`、`customerAddress` 访问函数。

记录语法还支持**命名参数**创建值（字段顺序可调换）：

```haskell
customer2 = Customer {
              customerID = 271828
            , customerAddress = ["1048576 Disk Drive", "Milpitas, CA 95134", "USA"]
            , customerName = "Jane Q. Citizen"
            }
```

---

### 参数化类型

类型可以接受**类型参数**（类型变量）：

```haskell
data Maybe a = Just a
             | Nothing
```

`Maybe` 用于表示"值可能存在也可能不存在"（类似于其他语言中的 null）：

```haskell
ghci> Just 1.5
Just 1.5
ghci> Nothing
Nothing
ghci> :type Just "invisible bike"
Just "invisible bike" :: Maybe [Char]
```

---

### 递归类型

类型可以递归定义——即在自身中出现：

```haskell
-- 自定义列表
data List a = Cons a (List a)
            | Nil
              deriving (Show)

-- 自定义二叉树
data Tree a = Node a (Tree a) (Tree a)
            | Empty
              deriving (Show)
```

`List a` 和内置列表 `[a]` 是**同构**的（形状相同），可以互相转换：

```haskell
fromList (x:xs) = Cons x (fromList xs)
fromList []     = Nil
```

与 Java 的对比：Java 用 `null` 表示缺失子树，Haskell 用无参构造器 `Empty`：

```haskell
simpleTree = Node "parent" (Node "left child" Empty Empty)
                           (Node "right child" Empty Empty)
```

---

### 错误处理

`error :: String -> a` 在出错时打印消息并终止程序：

```haskell
mySecond :: [a] -> a
mySecond xs = if null (tail xs)
              then error "list too short"
              else head (tail xs)
```

缺点：`error` 无法让调用者区分可恢复错误和严重错误。

**更好的方式：使用 `Maybe`**

```haskell
safeSecond :: [a] -> Maybe a
safeSecond [] = Nothing
safeSecond xs = if null (tail xs)
                then Nothing
                else Just (head (tail xs))

-- 用模式匹配简化
tidySecond :: [a] -> Maybe a
tidySecond (_:x:_) = Just x
tidySecond _        = Nothing
```

---

### 引入局部变量

#### `let` 表达式

```haskell
lend amount balance = let reserve    = 100
                          newBalance = balance - amount
                      in if balance < reserve
                         then Nothing
                         else Just newBalance
```

`let` 引入绑定，`in` 结束作用域。Haskell 是惰性语言，`let` 中的表达式在被需要之前不会求值。

**遮蔽**（Shadowing）：内层 `let` 可以重新绑定同名变量：

```haskell
bar = let x = 1
      in ((let x = "foo" in x), x)
-- 结果：("foo", 1)
```

GHC 选项 `-fwarn-name-shadowing` 可检测遮蔽。

#### `where` 子句

另一种引入局部变量的方式，定义跟在表达式之后：

```haskell
lend2 amount balance = if amount < reserve * 0.5
                       then Just newBalance
                       else Nothing
    where reserve    = 100
          newBalance = balance - amount
```

`let` 和 `where` 的选择是风格偏好：`where` 把"辅助信息"放在后面，让主表达式更突出。

---

### 缩进规则（Offside Rule）

Haskell 用**缩进**作为代码结构的提示（称为 offside rule）：

- 顶层声明后，缩进必须保持一致
- `let` 和 `where` 块中，后续行的缩进决定是新条目还是续行

```haskell
foo = let firstDefinition = blah blah
          -- 注释行视为空
                          continuation blah
          -- 减少缩进 → 新定义
          secondDefinition = yada yada
      in whatever
```

**建议**：始终使用空格而非 Tab——不同系统对 Tab 宽度的约定不同，可能导致编译问题。

**显式结构化**：`let` 和 `where` 的布局规则可以用显式大括号和分号替代：

```haskell
foo = let { a = 1; b = 2; c = 3 } in a + b + c
```

---

### `case` 表达式

`case` 在表达式中进行模式匹配：

```haskell
fromMaybe defval wrapped =
    case wrapped of
      Nothing     -> defval
      Just value  -> value
```

匹配按从上到下顺序进行，第一个匹配的模式决定结果。

---

### 常见模式匹配错误

#### 错误：把变量当作字面量匹配

```haskell
-- 错误！apple 是局部变量，不是匹配 "apple"
whichFruit f = case f of
                 apple  -> Apple
                 orange -> Orange
```

`apple` 是新绑定的变量，始终匹配成功——这个函数总是返回 `Apple`。

正确做法是用**字面量字符串**：

```haskell
betterFruit f = case f of
                  "apple"  -> Apple
                  "orange" -> Orange
```

#### 错误：在模式中用同一变量绑定多个位置

```haskell
-- 错误！a 出现了两次
bad_nodesAreSame (Node a _ _) (Node a _ _) = Just a
```

同一个名字不能绑定多次来表示"两个值应该相等"。需要用**卫述语**（guard）来比较。

---

### 卫述语（Guards）

模式匹配只能做"形状"的固定检查。卫述语让我们能做更灵活的条件判断：

```haskell
nodesAreSame (Node a _ _) (Node b _ _)
    | a == b    = Just a
nodesAreSame _ _ = Nothing
```

卫述语用 `|` 引入，后跟 `Bool` 表达式。如果卫述语求值为 `True`，使用对应函数体；如果都不成功，尝试下一个模式。

```haskell
lend3 amount balance
     | amount <= 0            = Nothing
     | amount > reserve * 0.5  = Nothing
     | otherwise               = Just newBalance
    where reserve    = 100
          newBalance = balance - amount
```

`otherwise` 只是绑定到 `True` 的变量，用于提高可读性。

用卫述语重写 `myDrop`：

```haskell
niceDrop n xs | n <= 0 = xs
niceDrop _ []          = []
niceDrop n (_:xs)      = niceDrop (n - 1) xs
```

相比 `if` 表达式，卫述语让各种情况一目了然。

---

### 练习

1. 实现一个计算列表元素个数的函数，与标准 `length` 比较
2. 计算列表平均值（注意用 `fromIntegral` 将整数转为浮点）
3. 将列表转为回文：`[1,2,3]` → `[1,2,3,3,2,1]`
4. 判断列表是否为回文
5. 按子列表长度排序（参考 `Data.List.sortBy`）
6. 实现 `intersperse :: a -> [[a]] -> [a]`（在元素间插入分隔符）
7. 计算二叉树高度（到最远 `Empty` 的 hops 数）
8. 定义二维点方向的 `Direction` 类型（向左/向右/直线）
9. 计算三个点的转向（返回 `Direction`）
10. 对点列表计算每相邻三点的转向
11. 用 Graham scan 算法计算凸包

---

*原文来源：Real World Haskell, Chapters 2 & 3*
*http://book.realworldhaskell.org/*
