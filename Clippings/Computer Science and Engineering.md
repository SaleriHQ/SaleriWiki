---
title: "Computer Science and Engineering"
source: "https://4chan-science.fandom.com/wiki/Computer_Science_and_Engineering"
author:
  - "[[Contributors to /sci/ Wiki]]"
published:
created: 2026-04-21
description: "This page contains Computer Science and Engineering textbook recommendations. In order to have a solid CS&E foundation, you should touch upon each of the following fundamental topics. If your focus is on Computer Engineering (CpE), Electrical and Computer Engineering (ECE), or just have a strong..."
tags:
  - "clippings"
---

本页面包含计算机科学与工程教材推荐。

## 基础

为了打下扎实的 CS&E 基础，你应该涉猎以下每个基础主题。如果你的方向是计算机工程（CpE）、电气与计算机工程（ECE），或者对硬件有强烈兴趣，那么除了以下内容外，你还应该学习[EEE 基础](https://4chan-science.fandom.com/wiki/Electrical_and_Electronics_Engineering#Fundamentals "Electrical and Electronics Engineering")。

为了打下扎实的计算机科学与工程基础，你需要涉猎以下每个基础主题。如果你的重点是计算机工程（CpE）、电气与计算机工程（ECE），或者对硬件有强烈兴趣，那么除了以下内容外，你还应该学习电气与电子工程基础部分。

### 基础编程与数据结构

*先修知识：[初级代数](https://4chan-science.fandom.com/wiki/Mathematics#Elementary_Algebra "Mathematics")。有用的延伸知识：逻辑或证明。*

*先修知识：初级代数。有用的延伸知识：逻辑或证明。*

在考虑哪些是好教材来教授编程概念的同时，你还必须选择一门特定的语言作为起点。在没有扎实掌握一门语言（比如 C++）作为参考框架之前，不要同时学习太多语言。至于语言选择，你应该考虑像躲避瘟疫一样避开 Java 和 Basic，因为它们可能会养成糟糕的编程习惯，也不要听信那些声称 C++ 对初学者"太难"、"臃肿"、"慢"或其他不正确且严重误导的 C++ 语言批评者。你还应该知道，本列表中以及一般的教材都会假设你了解或熟悉 C++，至少是 C。

在考虑哪些是好教材来教授编程概念的同时，你还必须选择一门特定的语言作为起点。在没有扎实掌握一门语言（比如 C++）作为参考框架之前，不要同时学习太多语言。至于语言选择，你应该像躲避瘟疫一样避开 Java 和 Basic，因为它们可能会养成糟糕的编程习惯，也不要听信那些声称 C++ 对初学者"太难"、"臃肿"、"慢"或其他不正确且严重误导的 C++ 语言批评者。你还应该知道，本列表中以及一般的教材都会假设你了解或熟悉 C++，至少是 C。

如果你想从 C++ 开始（可以说是最通用的），可以考虑以下书籍：

- Programming: Principles and Practice Using C++ by Stroustrup（C++ 创始人所著。编程入门和 C++ 的优秀入门书籍）
- C++ Primer by Lippman, Lajoie, and Moo（可作为 Programming: Principles and Practice 的后续，或作为有编程经验的 C++ 第一本书）*不要与 C++ Primer Plus（Stephen Prata）混淆，后者评价不佳。*

无论如何强调都不为过：即使你只是想学习编码基础知识，一旦你掌握了编程语法（比如通过上述书籍），你也绝不能就此止步。相反，应该继续学习常见数据结构（以及与之相关的基本算法）的结构、实现和分析。这对于完全掌握编程和编写任何有一定复杂度的程序（即任何有用的程序）都是绝对必要的。不做到这一点，你的编程就不算入门。

无论如何强调都不为过：即使你只是想学习编码基础知识，一旦你掌握了编程语法（比如通过上述书籍），你也绝不能就此止步。相反，应该继续学习常见数据结构（以及与之相关的基本算法）的结构、实现和分析。这对于完全掌握编程和编写任何有一定复杂度的程序（即任何有用的程序）都是绝对必要的。不做到这一点，你的编程就不算真正入门。

C++ 最好的数据结构书籍是：

- Data Structures and Algorithms in C++ by Drozdek

另一本较老的、与语言无关的使用伪 Pascal 代码的书籍是：

- Data Structures and Algorithms by Aho, Ullman, and Hopcroft

尽管它是伪代码，但在这个学习阶段，你真的应该尝试用你所知道的任何语言实现所涵盖的主题。学习完上述书籍之一后，你就可以继续学习下面章节的算法教材了。

尽管它是伪代码，但在这个学习阶段，你真的应该尝试用你所知道的任何语言实现所涵盖的主题。学习完上述书籍之一后，你就可以继续学习下面章节中的算法教材了。

如果你想深入学习比 CS&E 专业学生在第二门编程课程中通常涉及的内容更深的数据结构，这第二本书（用 C 编写，但与 C++ 足够接近）是一个很好的后续选择：

- Advanced Data Structures by Peter Brass

关于 C++ 编程高级主题的其他参考资料：

- The C++ Standard Library: A Tutorial and Reference by Josuttis
- Effective C++: 55 Specific Ways to Improve Your Programs and Designs by Scott Meyers
- Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14 by Scott Meyers
- The C++ Programming Language by Stroustrup

其他语言资料可以在[编程教材推荐](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations "Programming Textbook Recommendations")页面找到

关于 C++ 编程高级主题的其他参考资料可以在编程教材推荐页面找到。

### 学会使用 Unix Shell、Make、系统编程和 C

假定你现在还不会这些。如果你已经掌握了 C++ 基础，学习 C 就简化为学习你不能再做什么以及 C 行为不同的几个怪癖：参见 [C for C++ Programmers](http://www.ccs.neu.edu/course/com3620/parent/C-for-Java-C++/c-for-c++-alt.html) 了解一些差异。

假定你现在还不会这些工具和语言。如果你已经掌握了 C++ 基础，学习 C 就简化为学习你不能再做什么以及 C 行为不同的几个怪癖。

- Advanced Programming in the UNIX Environment by Stevens and Rago（Windows 大致对应的书籍是 Windows System Programming by Hart 和/或 Windows Via C/C++ by Richter and Nasarre）
- [Make Manual](http://www.gnu.org/software/make/manual/)
- The C Programming Language by Kernighan and Ritchie（被称为 K&R，但要注意它出版于 1988 年，C 语言已随 C99 和 C11 标准发生了变化）
- C Programming: A Modern Approach by King
- [Modern C by Jens Gustedt](https://gustedt.gitlabpages.inria.fr/modern-c/)

你还应该开始学习如何使用版本控制系统，如 SVN 或 git，特别是如果你预见到自己将来会处理大型代码库或团队协作的话。与普遍看法相反，学习使用 1970 年代风格的终端文本编辑器如 vim/emacs 完全是没必要且无益的。

你还应该开始学习如何使用版本控制系统，如 SVN 或 git，特别是如果你预见到自己将来会处理大型代码库或团队协作的话。与普遍看法相反，学习使用 1970 年代风格的终端文本编辑器如 vim/emacs 完全是没必要且无益的。

### 计算机体系结构和数字逻辑

#### 数字逻辑

*先修知识：[预科数学](https://4chan-science.fandom.com/wiki/Mathematics#Precalculus "Mathematics")。有用的延伸知识：编程和电路。*

*先修知识：预科数学。有用的延伸知识：编程和电路。*

- Digital Design: Principles and Practices by Wakerly
- Fundamentals of Logic Design by Roth & Kinney（Wakerly 的替代选择）
- Digital Design and Computer Architecture by David Harris and Sarah Harris（连接数字逻辑和计算机体系结构的入门书籍）

#### 计算机组成与体系结构

*先修知识：编程。有用的延伸知识：Unix、电路和逻辑。*

*先修知识：编程。有用的延伸知识：Unix、电路和逻辑。*

- Computer Organization and Design: The Hardware/Software Interface by Patterson & Hennessy（旧版使用 MIPS 汇编语言，最新版使用 ARM）
- Computer Systems: A Programmer's Perspective by Bryant & O'Hallaron（基于 AMD64 的汇编）

高级现代和高性能体系结构的进阶第二本书：

- Computer Architecture: A Quantitative Approach by Hennessy & Patterson（他们名字的顺序区分了两本书，这本更高级）
- Parallel Computer Organization and Design by Dubois, Annavaram, and Stenström（涵盖内容超出并行主题）
- Modern Processor Design: Fundamentals of Superscalar Processors by John Paul Shen

其他参考资料：

- The Intel Microprocessors by Barry B. Brey
- Microprocessor Architecture: From Simple Pipelines to Chip Multiprocessors by Jean-Loup Baer

x86/AMD64 汇编语言的全面参考资料：[Intel <sup>®</sup> 64 and IA-32 Architectures Software Developer Manuals](http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html)（有 3463 页，所以不要试图全部读完）

x86/AMD64 汇编语言的全面参考资料是 Intel 的官方手册，但它有 3463 页，所以不要试图全部读完。

### 操作系统

*先修知识：体系结构和 C/C++ 编程。有用的延伸知识：Unix、系统编程。*

*先修知识：体系结构和 C/C++ 编程。有用的延伸知识：Unix、系统编程。*

- Operating System Concepts by Silberschatz, Galvin, and Gagne（恐龙书）
- Modern Operating Systems by Tanenbaum

更多内容参见 [OS 开发](#OS_Development) 部分

### 数学基础

学习算法、编译器、计算复杂性理论和高级主题，你需要熟悉抽象主题，如证明、集合、数论、组合学、图论和概率。但好消息（或坏消息）是，在学习初期你不需要在大多数这些领域有太深的*深度*，所以你不必担心一次完全掌握所有内容。最终，你会想要更深入地研究，[数学](#Mathematics) 部分提供了相关资源。现在也是学习 [LaTeX](https://4chan-science.fandom.com/wiki/Universal_Material#LaTeX "Universal Material") 和用 LaTeX 排版大部分作业的最佳时机。

学习算法、编译器、计算复杂性理论和高级主题，你需要熟悉证明、集合、数论、组合学、图论和概率等抽象主题。但好消息是，在学习初期你不需要在大多数这些领域有太深的深度，所以不必担心一次完全掌握所有内容。最终你会想要更深入地研究，数学部分提供了相关资源。现在也是学习 LaTeX 和用 LaTeX 排版大部分作业的最佳时机。

#### 证明与数学推理

*先修知识：[预科数学](https://4chan-science.fandom.com/wiki/Mathematics#Precalculus "Mathematics")。有用的延伸知识：数字逻辑或哲学逻辑。*

*先修知识：预科数学。有用的延伸知识：数字逻辑或哲学逻辑。*

这里你绝对想要完全掌握的最重要主题是阅读和书写证明、逻辑表达式和朴素集合论的技能。可悲的是，即使学过离散数学课程的学生仍然发现证明对他们来说完全是个难题。你可以尝试在离散数学书中学习证明，但你仍会发现自己缺乏大量必要的练习。因此强烈建议你学习面向数学的证明论著。你最不想做的事情就是在学习后续主题时还在为证明挣扎，那几乎保证你会失败或至少度过一段糟糕的时光。

这里你绝对想要完全掌握的最重要主题是阅读和书写证明、逻辑表达式和朴素集合论的技能。可悲的是，即使学过离散数学课程的学生仍然发现证明对他们来说完全难以理解。你可以尝试在离散数学书中学习证明，但你仍会发现自己缺乏大量必要的练习。因此强烈建议你学习面向数学的证明论著。你最不想做的事情就是在学习后续主题时还在为证明挣扎，那几乎保证你会失败或至少度过一段糟糕的时光。

- A Transition to Advanced Mathematics by Smith, Eggen, and St. Andre
- A Primer of Abstract Mathematics by Ash
- Conjecture and Proof by Laczkovich（上述书籍的优秀补充，展示了更多种类的数学证明）
- Proofs from THE BOOK by Aigner and Ziegler（不是证明教科书，而是一个优秀的高质量且优雅的证明集合，值得欣赏和从中汲取灵感）

如果你仍然发现自己在证明方面有困难，以下书籍采用更循序渐进的方法（但代价是排除了一些有价值的内容）

- How to Prove It: A Structured Approach by Velleman
- How to Read and Do Proofs: An Introduction to Mathematical Thought Processes by Solow
- [Book of Proof by Hammack](http://www.people.vcu.edu/~rhammack/BookOfProof/)

现在你终于能够灵活应对证明了，接下来要学的东西不多，很多都可以边学边积累。但为了提前熟悉这些主题，以下书籍作为速成课程（记住离散数学几乎只是触及了它们所涵盖的大部分主题的皮毛，如果你想要深度，可以直接跳到涵盖这些主题的书籍）：

现在你终于能够灵活应对证明了，接下来要学的东西不多，很多都可以边学边积累。但为了提前熟悉这些主题，以下书籍作为速成课程（记住离散数学几乎只是触及了它们所涵盖的大部分主题的皮毛，如果你想要深度，可以直接跳到相关主题的专业书籍）：

- Concrete Mathematics: A Foundation for Computer Science by Graham, Knuth, and Patashnik
- Discrete Mathematics and Its Applications by Rosen（难度略低于 Graham，覆盖了与证明书籍类似的内容）

#### 概率论

还有一个标准要求是了解[微积分](https://4chan-science.fandom.com/wiki/Mathematics#Calculus "Mathematics")和[线性代数](https://4chan-science.fandom.com/wiki/Mathematics#Linear_Algebra "Mathematics")，如果你还没有学过，去学习它们。在这个级别要研究的最后一件事是概率论，它在处理现实世界问题时不可或缺。

还有一个标准要求是了解微积分和线性代数，如果你还没有学过，去学习它们。在这个级别要研究的最后一件事是概率论，它在处理现实世界问题时不可或缺。

- The Art Of Probability by Hamming（其他概率教材的优秀入门或补充）
- Probability by Pitman
- A First Course in Probability by Ross
- [An Introduction to Probability and Random Processes by Rota and Baclawski](http://www.ellerman.org/gian-carlo-rota/)

另见 EEE 的[概率与随机过程](https://4chan-science.fandom.com/wiki/Electrical_and_Electronics_Engineering#Probability_and_Stochastic_Processes)推荐。

### 算法

*先修知识：编程和证明。有用的延伸知识：图论、组合学*

*先修知识：编程和证明。有用的延伸知识：图论、组合学*

算法及其分析的研究对于该领域任何认真工作都是必不可少的。

算法及其分析的研究对于该领域任何认真工作都是必不可少的。

- Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein <sup><a href="http://www.cs.dartmouth.edu/~thc/clrs-bugs/bugs-3e.php">[Errata]</a></sup>（被称为 CLRS，内容非常全面）
- Algorithms in C++ Parts 1-5: Fundamentals, Data Structures, Sorting, Searching, and Graph Algorithms by Sedgewick（也有 C 版本。涵盖理论和实现细节）
- Algorithm Design by Kleinberg and Tardos（更侧重于设计算法的过程，而非收集和分析最常见算法）
- The Design and Analysis of Algorithms by Kozen（上述书籍的补充，包含更多高级主题和复杂性理论的良好入门）
- An Introduction to the Analysis of Algorithms by Sedgewick and Flajolet（这本书关注算法的数学分析。作者的"解析组合"是其延续）

以及作为参考

- The Art of Computer Programming by Knuth

### 各种编程语言、范式和编译器

*先修知识：编程。有用的延伸知识：体系结构和算法。*

*先修知识：编程。有用的延伸知识：体系结构和算法。*

你应该学习几种与你熟悉的语言运作方式不同的"感觉"编程语言。人们通常学习的常见语言包括：Lisp/Scheme/Racket、Prolog、Haskell、Forth（或 Factor）、J、Matlab、Python、Lua、C# 和 C++。同样，你还应该深入研究这些语言所具有的结构以及将它们翻译成机器指令的编译器背后的理论

*先修知识：体系结构和算法。有用的延伸知识：自动机、计算复杂性理论和数理逻辑。*

*先修知识：体系结构和算法。有用的延伸知识：自动机、计算复杂性理论和数理逻辑。*

- Programming Language Pragmatics by Scott
- Engineering a Compiler by Cooper and Torczon <sup><a href="http://www.cs.rice.edu/~keith/Errata.html">[Errata]</a></sup>
- Compilers: Principles, Techniques, and Tools by Aho, Lam, Sethi, and Ullman（龙书）
- Advanced Compiler Design and Implementation by Muchnick（更高级，读完上述书籍后仍想要更多时阅读）

### 自动机、可计算性理论和计算复杂性理论

*先修知识：算法。有用的延伸知识：数字逻辑、体系结构和数理逻辑。*

*先修知识：算法。有用的延伸知识：数字逻辑、体系结构和数理逻辑。*

"你怎么知道在计算机上解决给定问题是可能的？即使可能，解决这个问题需要多少计算资源？" [计算理论](https://en.wikipedia.org/wiki/Theory_of_computation)正是基于回答这些基本问题。该主题自然分为三个不同的部分。首先，我们必须提出计算设备是什么的数学模型，以便开始证明关于它们的一般定理和结果。这是形式语言和[自动机](https://en.wikipedia.org/wiki/Automata_theory)的领域。接下来是[可计算性理论](https://en.wikipedia.org/wiki/Computability)，我们在其中确定在这些抽象机器上可以做什么。最后是[计算复杂性理论](https://en.wikipedia.org/wiki/Computational_complexity_theory)，它关注的是在有限计算资源下什么是可能的："一个问题能用[对数](https://en.wikipedia.org/wiki/L_\(complexity\))或[多项式](https://en.wikipedia.org/wiki/PSPACE) *空间*，或[多项式](https://en.wikipedia.org/wiki/P_\(complexity\))、[指数](https://en.wikipedia.org/wiki/EXPTIME)或[双指数](https://en.wikipedia.org/wiki/2-EXPTIME) *时间*来解决吗？[随机性](https://en.wikipedia.org/wiki/Nondeterministic_algorithm)能帮助你更快解决问题吗？找[负面答案](https://en.wikipedia.org/wiki/Complement_\(complexity\))和找正面答案一样容易吗？这个问题[可并行化](https://en.wikipedia.org/wiki/NC_\(complexity\))吗？"

"你怎么知道在计算机上解决给定问题是可能的？即使可能，解决这个问题需要多少计算资源？" 计算理论正是基于回答这些基本问题。该主题自然分为三个不同的部分。首先，我们必须提出计算设备是什么的数学模型，以便开始证明关于它们的一般定理和结果。这是形式语言和自动机的领域。接下来是可计算性理论，我们确定在这些抽象机器上可以做什么。最后是计算复杂性理论，它关注的是在有限计算资源下什么是可能的。

- Introduction to the Theory of Computation by Sipser <sup><a href="http://www-math.mit.edu/~sipser/book.html">[Errata]</a></sup>

Sipser 是一本非常易读（几乎达到初中水平）的书，涵盖所有三个领域，只需要读写简单证明的能力。对于想学习并理解这个主题的 CS 以外的人来说很棒，任何完成这本书的人都会比 99.95% 的 CS 专业学生更了解这个主题，并且在他们歪曲和严重错误描述它时能够轻易指出他们的错误（这种情况经常发生）。缺点是价格高得离谱，数学素养高的读者会因其不够深入而感到烦恼。

Sipser 是一本非常易读（几乎达到初中水平）的书，涵盖所有三个领域，只需要读写简单证明的能力。对于想学习并理解这个主题的非 CS 专业人士来说很棒，任何读完这本书的人都会比绝大多数 CS 专业学生更了解这个主题，并且在他们歪曲和严重错误描述它时能够轻易指出他们的错误。缺点是价格高得离谱，数学素养高的读者会因其不够深入而感到烦恼。

- Automata and Computability by Kozen（比 Sipser 更以数学细节涵盖该主题的前两个领域）
- Computational Complexity: A Modern Approach by Arora and Barak（可用作 Sipser 的后续或第一本深入复杂性理论的书）
- Theory of Computation by Kozen
- Computability, Complexity, and Languages: Fundamentals of Theoretical Computer Science by Martin Davis, Ron Sigal, and Elaine Weyuker

参考资料

- Computers and Intractability: A Guide to the Theory of NP-Completeness by Garey and Johnson

## 专题

### 并行编程

*先修知识：C/C++ 编程和体系结构。有用的延伸知识：*操作系统*。*

*先修知识：C/C++ 编程和体系结构。有用的延伸知识：操作系统。*

随着计算机变得越来越并行化，学习如何（以及何时）使用 OpenMP、MPI、pthreads/std::thread 和 OpenCL 进行编程，并了解并行算法与线性算法的独特方面，这很重要。很难找到好书，但大多数人会推荐这些作为通用介绍：

随着计算机变得越来越并行化，学习如何（以及何时）使用 OpenMP、MPI、pthreads/std::thread 和 OpenCL 进行编程，并了解并行算法与串行算法的独特方面，这很重要。很难找到好书，但大多数人会推荐这些作为通用介绍：

- An Introduction to Parallel Programming by Pacheco（涵盖 MPI、Pthreads 和 OpenMP）
- Introduction to Parallel Computing by Grama, Karypis, Kumar, and Gupta（涵盖 MPI、Pthreads 和 OpenMP）
- C++ Concurrency in Action: Practical Multithreading by Williams（只涵盖 std::thread）
- Heterogeneous Computing with OpenCL by Gaster, Howes, Kaeli, et al.（在继续 GPGPU 编码之前，你应该熟悉基本并行编程）
- OpenCL in Action: How to Accelerate Graphics and Computations by Scarpino
- OpenCL Programming Guide by Munshi, Gaster, et al.

### 网络

*先修知识：编程和概率。有用的延伸知识：操作系统、算法、并行编程或图论*

*先修知识：编程和概率。有用的延伸知识：操作系统、算法、并行编程或图论*

- Computer Networks: A Systems Approach by Peterson and Davie
- Computer Networks by Tanenbaum
- Unix Network Programming, Volume 1: The Sockets Networking API by Stevens, Fenner, and Rudoff
- Interconnections: Bridges, Routers, Switches, and Internetworking Protocols by Perlman
- [Data Networks](http://web.mit.edu/dimitrib/www/datanets.html) by Bertsekas and Gallager

### 计算机安全与密码学

*先修知识：证明、（基础）概率和（基础）算法/编程。有用的延伸知识：复杂性理论、抽象代数和数论*

*先修知识：证明、（基础）概率和（基础）算法/编程。有用的延伸知识：复杂性理论、抽象代数和数论*

- Introduction to Modern Cryptography by Katz and Lindell [<sup>[Errata]</sup>](https://www.cs.umd.edu/~jkatz/imc.html)（很好的起点，专注于回答"何时应该使用什么系统及为什么"的*可证明安全*）
- Cryptography Engineering: Design Principles and Practical Applications by Niels Ferguson, Bruce Schneier, Tadayoshi Kohno（专注于密码系统的实现细节）
- An Introduction to Mathematical Cryptography by Hoffstein, Pipher, and Silverman [<sup>[Website]</sup>](https://www.math.brown.edu/~jhs/MathCryptoHome.html)

另见[逆向工程与恶意软件分析](#Reverse_Engineering_and_Malware_Analysis)

### 信息论与编码理论

*先修知识：证明、概率和线性代数。有用知识：抽象代数、分析和测度论。有用的延伸知识：信号与系统分析、数字信号处理、通信系统和复杂性理论*

*先修知识：证明、概率和线性代数。有用知识：抽象代数、分析和测度论。有用的延伸知识：信号与系统分析、数字信号处理、通信系统和复杂性理论*

- Elements of Information Theory by Cover and Thomas
- The Mathematical Theory of Communication by Claude Shannon and Warren Weaver（开创这一切的论文，非常易读、优美且仍有价值）
- Principles of Digital Communication and Coding (Dover Books on Electrical Engineering) by Viterbi and Omura
- Introduction to Data Compression by Sayood
- Information Theory (Dover Books on Mathematics) by Ash
- Network Information Theory by El Gamal and Kim
- Coding and Information Theory by Roman
- Information Theory and Reliable Communication by Gallager

也请查看下一节中 MacKay 的书。

也请查看下一节中 MacKay 的书籍。

关于量子信息论，请参见

- Quantum Information Theory by Mark Wilde（可在线获取为"From Classical to Quantum Shannon Theory"）

### 人工智能、机器学习和计算机视觉

*先修知识：编程语言、概率、向量微积分和线性代数。有用知识：统计学（特别是贝叶斯）、图论、优化、逼近算法、信息论、傅里叶和泛函分析以及测度论。有用的延伸知识：信号与系统分析、数字信号处理、控制理论、理论神经科学*

*先修知识：编程语言、概率、向量微积分和线性代数。有用知识：统计学（特别是贝叶斯）、图论、优化、逼近算法、信息论、傅里叶和泛函分析以及测度论。有用的延伸知识：信号与系统分析、数字信号处理、控制理论、理论神经科学*

警告：大多数人们谈论的这些领域的内容都是不切实际的幻想，不要抱太大期望。在学习计算机视觉之前，先学习数字图像处理和一些计算机图形学会非常有帮助。

- Artificial Intelligence: A Modern Approach by Russell and Norvig
- Computer Vision by Shapiro and Stockman
- Multiple View Geometry in Computer Vision by Hartley and Zisserman <sup><a href="http://www.robots.ox.ac.uk/~vgg/hzbook/">[Errata]</a></sup>
- Computer Vision: Algorithms and Applications by Szeliski
- Pattern Recognition and Machine Learning by Bishop
- Information Theory, Inference & Learning Algorithms by MacKay（可[免费在线阅读](http://www.inference.phy.cam.ac.uk/mackay/itila/book.html)）
- The Elements of Statistical Learning: Data Mining, Inference, and Prediction by Hastie, Tibshirani, and Friedman（[可免费在线阅读](https://hastie.su.domains/Papers/ESLII.pdf)）

### 自然语言处理

- Natural Language Understanding by Allen（略有过时）
- Foundations of Statistical Natural Language Processing by Manning and Schütze
- Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition by Jurafsky and Martin

另见 EEE 的[语音处理](https://4chan-science.fandom.com/wiki/Electrical_and_Electronics_Engineering#Speech_Processing "Electrical and Electronics Engineering")推荐。

### 计算机图形学与图像处理

*先修知识：编程、向量微积分和线性代数。有用的延伸知识：现代几何、四元数、信号与系统分析、数值分析或并行编程*

*先修知识：编程、向量微积分和线性代数。有用的延伸知识：现代几何、四元数、信号与系统分析、数值分析或并行编程*

- Digital Image Processing by Gonzalez
- Fundamentals of Computer Graphics by Shirley and Marschner
- Computer Graphics: Principles and Practice by Hughes, van Dam, McGuire, Sklar, Foley, Feiner, Akeley（经典 CG 圣经 *Computer Graphics: Principles and Practice in C by Foley, van Dam, Feiner, and Hughes* 的更新/重写版）

### 离散与计算几何

- Computational Geometry: Algorithms and Applications by de Berg, Cheong, van Kreveld, and Overmars
- Discrete and Computational Geometry by Devadoss and O'Rourke
- Lectures on Discrete Geometry by Matousek <sup><a href="http://kam.mff.cuni.cz/~matousek/dg.html">[Errata]</a></sup>

### 高级算法与数学优化

*先修知识：算法、概率、证明和线性代数。有用的延伸知识：组合学（强烈建议）、图论（强烈建议）、复杂性理论*

*先修知识：算法、概率、证明和线性代数。有用的延伸知识：组合学（强烈建议）、图论（强烈建议）、复杂性理论*

#### 线性规划/优化

- Introduction to Linear Optimization by Bertsimas & Tsitsiklis
- Theory of Linear and Integer Programming by Schrijver

#### 组合优化与网络流

- Network Flows by Ahuja, Magnanti & Orlin <sup><a href="http://jorlin.scripts.mit.edu/Network_Flows:_Theory,_Algorithms,_and_Applications.html">[Errata]</a></sup>
- Combinatorial Optimization by Cook, Cunningham, Pulleyblank, and Schrijver
- Combinatorial Optimization - Theory and Algorithms by Korte & Vygen
- Combinatorial Optimization, Polyhedra and Efficiency by Schrijver <sup><a href="http://homepages.cwi.nl/~lex/co/">[Errata]</a></sup>

#### 凸优化

- [Convex Optimization](http://stanford.edu/~boyd/cvxbook/) by Boyd and Vandenberghe
- [Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications](http://www2.isye.gatech.edu/~nemirovs/Lect_ModConvOpt.pdf) by Ben-Tal and Nemirovski
- [Convex Optimization & Euclidean Distance Geometry](https://ccrma.stanford.edu/~dattorro/mybook.html) by Dattorro
- Convex Analysis by Rockafellar（理论部分，需要一些基础分析知识）

#### 近似算法

- [Approximation Algorithms](http://www.cc.gatech.edu/fac/Vijay.Vazirani/book.pdf) by Vazirani
- [The Design of Approximation Algorithms](http://www.designofapproxalgs.com/index.php) by Williamson and Shmoys
- Design and Analysis of Approximation Algorithms by Ding-Zhu Du, Ker-I Ko, Xiaodong Hu

#### 随机算法

- Randomized Algorithms by Motwani and Raghavan

### 数值分析与方法

*先修知识：基础编程、向量微积分、线性代数、基础微分方程。有用的延伸知识：算法、体系结构、分析。*

*先修知识：基础编程、向量微积分、线性代数、基础微分方程。有用的延伸知识：算法、体系结构、分析。*

#### 数值方法

- Numerical Methods for Engineers by Steven Chapra, Raymond Canale
- Scientific Computing: An Introductory Survey, Revised Second Edition by Michael T. Heath
- Scientific Computing with MATLAB and Octave by Alfio Quarteroni, Fausto Saleri, Paola Gervasio

#### 数值分析概述

- Numerical Methods for Scientists and Engineers (Dover Books) by Hamming
- Numerical Analysis by Burden and Faires
- An Introduction to Numerical Analysis by Atkinson
- An Introduction to Numerical Analysis by Süli and Mayers
- Numerical Analysis: A Mathematical Introduction by Schatzman

#### 数值线性代数

- Matrix Computations by Golub and Van Loan
- Numerical Linear Algebra by Trefethen and Bau III
- Matrix Analysis by Horn and Johnson

#### 逼近理论

- Introduction to Approximation Theory by Cheney
- Interpolation and Approximation (Dover Books) by Davis
- Approximation Theory and Methods by Powell
- Approximation Theory and Approximation Practice by Trefethen <sup>[<a href="https://people.maths.ox.ac.uk/trefethen/ATAP/">site</a>, <a href="http://www.chebfun.org/ATAP/">mirror</a>]</sup>

更高级的书籍：

- Theory of Approximation (Dover Books) by Achieser
- [Theory of Approximation of Functions of a Real Variable](https://archive.org/details/theoryofapproxim033501mbp) (Dover Books) by Timan（注意，亚马逊将这本书和 Achieser 的书关联在一起……）

#### 数值常微分方程

- Computer Methods for Ordinary Differential Equations and Differential-Algebraic Equations by Ascher and Petzold
- Numerical Methods for Ordinary Differential Equations by Butcher
- Solving Ordinary Differential Equations I: Nonstiff Problems by Hairer, Nørsett, and Wanner
- Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems by Hairer and Wanner
- Geometric Numerical Integration: Structure-Preserving Algorithms for Ordinary Differential Equations by Hairer, Lubich, and Wanner

#### 数值偏微分方程

- [Finite Difference and Spectral Methods for Ordinary and Partial Differential Equations by Trefethen](https://people.maths.ox.ac.uk/trefethen/pdetext.html)

##### 有限差分法

- Finite Difference Methods for Ordinary and Partial Differential Equations: Steady-State and Time-Dependent Problems by LeVeque <sup>[<a href="https://faculty.washington.edu/rjl/fdmbook/">Website</a>]</sup>
- Numerical Partial Differential Equations: Finite Difference Methods by Thomas
- Finite Difference Schemes and Partial Differential Equations by Strikwerda

##### 有限元法

- Finite Element Analysis: From Concepts to Applications by Burnett
- Applied Finite Element Analysis by Segerlind
- Programming the Finite Element Method by Smith, Griffiths, and Margetts
- Numerical Solution of Partial Differential Equations by the Finite Element Method (Dover Books on Mathematics) by Johnson
- The Mathematical Theory of Finite Element Methods by Brenner and Scott
- Theory and Practice of Finite Elements by Ern and Guermond

##### 谱方法

- [Chebyshev and Fourier Spectral Methods (Dover Books on Mathematics) by Boyd](http://www-personal.umich.edu/~jpboyd/BOOK_Spectral2000.html)
- Implementing Spectral Methods for Partial Differential Equations: Algorithms for Scientists and Engineers by Kopriva
- Spectral Methods: Fundamentals in Single Domains by Canuto, Hussaini, Quarteroni, and Zang
- Spectral Methods: Evolution to Complex Geometries and Applications to Fluid Dynamics Canuto, Hussaini, Quarteroni, and Zang

### 计算机代数系统与计算机算术

- Modern Computer Algebra von zur Gathen and Gerhard
- Modern Computer Arithmetic by Brent and Zimmermann
- Handbook of Floating-Point Arithmetic by Muller, Brisebarre, de Dinechin, et al.
- Elementary Functions: Algorithms and Implementation by Muller
- Computer Arithmetic: Algorithms and Hardware Designs by Behrooz Parhami
- Synthesis of Arithmetic Circuits: FPGA, ASIC and Embedded Systems by Deschamps, Bioul, and Sutter
- Hardware Implementation of Finite-Field Arithmetic by Deschamps, Imana, Sutter

### 有限域

- Finite Fields for Computer Scientists and Engineers by McEliece（简短且写得好的入门）
- Introduction to Finite Fields and Their Applications by Lidl and Niederreiter（更全面的介绍）
- Finite Fields (Encyclopedia of Mathematics and its Applications) by Lidl and Niederreiter（上述的扩展版本，通常被称为 FF 圣经，但日期是 1980 年代）
- Handbook of Finite Fields by Mullen and Panario（比 Lidl 更新、包含更多最新成果的广泛参考著作。Mullen 也有一本非常简短的入门书）
- Lectures on Finite Fields (Graduate Studies in Mathematics) by Xiang-Dong Hou（更偏数学的 FF 主题选集）

另见[应用抽象代数](https://4chan-science.fandom.com/wiki/Mathematics#Survey_of_Abstract_Algebra_Applications "Mathematics")数学页面

### 数学

尽量避免直接针对 CS 专业学生或标题类似"离散数学"的书籍，因为它们往往教的东西少得可怜。

- An Introduction to the Theory of Numbers by Hardy and Wright
- Combinatorics and Graph Theory by Harris, Hirst, and Mossinghoff
- Combinatorics: Topics, Techniques, Algorithms by Cameron
- All of Statistics: A Concise Course in Statistical Inference by Wasserman
- Probability Models by Sheldon Ross
- Signals and Systems by Oppenheim
- Discrete-Time Signal Processing by Oppenheim
- Analytic Combinatorics by Flajolet and Sedgewick（其算法书籍的后续）
- Quaternions and Rotation Sequences: A Primer with Applications to Orbits, Aerospace, and Virtual Reality by Kuipers
- Geometry by Brannan, Esplen, and Gray
- Geometric Methods and Applications: For Computer Science and Engineering by Gallier <sup><a href="http://www.cis.upenn.edu/~jean/gbooks/geom2.html">[Website]</a></sup>
- Logic for Computer Science: Foundations of Automatic Theorem Proving by Gallier

另见[数学教材推荐](https://4chan-science.fandom.com/wiki/Math_Textbook_Recommendations "Math Textbook Recommendations")、[数学](https://4chan-science.fandom.com/wiki/Mathematics "Mathematics")页面和[统计学推荐](https://4chan-science.fandom.com/wiki/Universal_Material#Statistics "Universal Material")

### 组合博弈论

不要与["经济"博弈论](https://4chan-science.fandom.com/wiki/Economics_Textbook_Recommendations#Game_Theory "Economics Textbook Recommendations")混淆，[组合博弈论](https://en.wikipedia.org/wiki/Combinatorial_game_theory)研究每个玩家都有完美信息的序贯博弈。

- On Numbers and Games by John H. Conway
- Winning Ways for Your Mathematical Plays: Volume 1-4 by Elwyn R. Berlekamp, John H. Conway, and Richard K. Guy
- Games, Puzzles, and Computation by Robert A. Hearn and Erik D. Demaine（博弈的复杂性）
- Combinatorial Game Theory (Graduate Studies in Mathematics) by Aaron N. Siegel
- Combinatorial Games: Tic-Tac-Toe Theory by József Beck
- [Games of No Chance](http://library.msri.org/books/Book29/contents.html)、[More Games of No Chance](http://library.msri.org/books/Book42/contents.html)、[Games of No Chance 3](http://library.msri.org/books/Book56/contents.html)、[Games of No Chance 4](http://library.msri.org/books/Book63/contents.html)；由 Richard Nowakowski 编辑

### 量子计算

不，量子计算机不会神奇地变得全能，能够解决世界上所有的问题，也不是解决 NP 中所有问题的万无一失的方法——但它仍然是一个非常有趣且快速发展的领域。你不需要彻底研究 Sakurai、Shankar 或 Griffiths 量子力学教材中的所有内容才能阅读量子计算，但你确实需要一些 QM 的理解。以下书籍将给你所有你想知道的关于量子力学*含义*的理解——如果你恰好是一名物理学生或自学者，可能从未在 Sakurai、Shankar 或 Griffiths 的书中或在所有过于常见的"闭嘴计算！"讲座中得到过，所以即使有 QM 背景也值得学习和欣赏。

- Quantum Processes, Systems, and Information by Schumacher and Westmoreland
- Quantum Theory: Concepts and Methods by Peres
- Quantum Theory by David Bohm（深入了解经典力学与量子理论的关系）

如果你有兴趣学习更多关于物理和 QM 的知识，请参见[物理教材推荐](https://4chan-science.fandom.com/wiki/Physics_Textbook_Recommendations "Physics Textbook Recommendations")

- An Introduction to Quantum Computing by Kaye, Laflamme, and Mosca
- Classical and Quantum Computation by Kitaev, Shen and Vyalyi
- Quantum Computation and Quantum Information by Michael Nielsen and Isaac Chuang（关于量子计算的书籍和参考）
- Quantum Computing: A Short Course From Theory To Experiment by Stolze and Suter（更偏向量子工程方面，需要扎实的物理背景）
- Introduction to Topological Quantum Computation by Jiannis K. Pachos（TQC 的基本概述）

### 类型理论与编程语言理论

*先修知识：编程语言概念、证明。有用的延伸知识：数理逻辑、抽象代数*

*先修知识：编程语言概念、证明。有用的延伸知识：数理逻辑、抽象代数*

- Types and Programming Languages by Pierce <sup><a href="http://www.cis.upenn.edu/~bcpierce/tapl/">[Errata]</a></sup>
- Advanced Topics in Types and Programming Languages by Pierce <sup><a href="http://www.cis.upenn.edu/~bcpierce/attapl/index.html">[Errata]</a></sup>
- Practical Foundations for Programming Languages by Harper <sup><a href="https://www.cs.cmu.edu/~rwh/plbook/2nded.pdf">[Draft]</a></sup>
- Foundations for Programming Languages by Mitchell
- Formal Semantics of Programming Languages by Winskel

### 操作系统开发

- Linux Kernel Development by Love
- Linkers and Loaders by Levine
- Linux Device Drivers by Corbet, Rubini, and Kroah-Hartman
- Understanding the Linux Kernel by Bovet and Cesati
- The Design of the UNIX Operating System by Bach
- The Design and Implementation of the FreeBSD Operating System by McKusick, Neville-Neil, and Watson
- Windows <sup>®</sup> Internals by Russinovich, Solomon, and Ionescu（当你被迫与 Windows 打交道时）
- Professional Linux Kernel Architecture by Wolfgang Mauerer

### 逆向工程与恶意软件分析

*先修知识：体系结构和操作系统。有用的延伸知识：计算机安全、操作系统开发、Unix/Windows、网络或编译器*

*先修知识：体系结构和操作系统。有用的延伸知识：计算机安全、操作系统开发、Unix/Windows、网络或编译器*

- Reversing: Secrets of Reverse Engineering by Eilam
- The Shellcoder's Handbook: Discovering and Exploiting Security Holes by Anley, Heasman, Lindner, and Richarte
- Practical Malware Analysis: The Hands-On Guide to Dissecting Malicious Software by Sikorski and Honig
- Practical Reverse Engineering: x86, x64, ARM, Windows Kernel, Reversing Tools, and Obfuscation by Dang, Gazet, and Bachaalany
- The Rootkit Arsenal: Escape and Evasion in the Dark Corners of the System by Blunden
- A Guide to Kernel Exploitation: Attacking the Core by Perma and Oldani

### 软件工程、开发与项目管理

*先修知识：编程。有用的延伸知识：大程序的经验。*

*先修知识：编程。有用的延伸知识：大程序的经验。*

- **The Mythical Man-Month: Essays on Software Engineering** by Brooks
- Code Complete: A Practical Handbook of Software Construction by McConnell
- Design Patterns: Elements of Reusable Object-Oriented Software by Gamma, Helm, Johnson, and Vlissides（四人帮的书）
- Software Requirements and Specifications: A Lexicon of Practice, Principles and Prejudices by Jackson
- Working Effectively with Legacy Code by Feathers
- The Pragmatic Programmer by Hunt and Thomas
- Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin
- Refactoring: Improving the Design of Existing Code by Fowler
- Peopleware: Productive Projects and Teams by DeMarco and Lister
- The psychology of computer programming by Gerald Weinberg

### 数据库

- An Introduction to Database Systems by Date
- Database Management Systems by Ramakrishnan and Gehrke
- Readings in Database Systems by Hellerstein and Stonebraker [<sup>[Red Book Website]</sup>](http://www.redbook.io/)
- Transaction Processing: Concepts and Techniques by Gray and Reuter
- Transactional Information Systems: Theory, Algorithms, and the Practice of Concurrency Control and Recovery by Weikum and Vossen

### 分布式系统与计算

- Distributed Systems: Principles and Paradigms by Tanenbaum and van Steen
- Distributed Systems by Mullender
- Distributed Algorithms by Lynch
- Introduction to Distributed Algorithms by Tel
- Distributed Computing: Fundamentals, Simulations, and Advanced Topics by Attiya and Welch

### 游戏开发

*先修知识：编程与数据结构、向量微积分、线性代数、基础物理。有用知识：算法、体系结构、四元数、计算机图形学、人工智能、数值分析与方法、网络或软件工程。*

*先修知识：编程与数据结构、向量微积分、线性代数、基础物理。有用知识：算法、体系结构、四元数、计算机图形学、人工智能、数值分析与方法、网络或软件工程。*

是啊是啊，我都能听到你在偷笑了。这些不是 API 指南，而是关于引擎盖下是什么的细节。

是啊是啊，我都能听到你在偷笑了。这些不是 API 指南，而是关于底层原理的细节。

#### 概述与引擎

- Game Engine Architecture by Gregory（全面概述构成游戏引擎的所有要素）
- Introduction to Game Development by Rabin（涵盖开发/引擎以及设计和制作/管理/营销细节）

#### 游戏图形

在继续之前，请参阅上面关于通用[计算机图形学](#Computer_Graphics_and_Image_Processing)和[数学](#Mathematics)文本的章节

- Mathematics for 3D Game Programming and Computer Graphics by Lengyel
- Real-Time Rendering by Akenine-Moller, Haines, and Hoffman
- Physically Based Rendering: From Theory To Implementation by Pharr and Humphreys

#### 游戏物理

- Real-Time Collision Detection by Ericson
- Game Physics by Eberly

#### 人工智能

- Artificial Intelligence for Games by Millington and Funge
- Game AI Pro: Collected Wisdom of Game AI Professionals by Steve Rabin
- Game AI Pro 2 by Steve Rabin（当前部署在最新游戏中的 AI 算法和技术）

更多人工智能理论，请参阅上面的学术人工智能文本部分。

### 其他参考资料

- Hacker's Delight by Warren
- Computer-Related Risks by Neumann
- Ethics for the Information Age by Quinn
- The Dawn of Software Engineering: from Turing to Dijkstra by Daylight
- Programming Pearls by Bentley
- Structure and Interpretation of Computer Programs by Abelson and Sussman（被称为 SICP）
- Feynman Lectures On Computation by Richard P. Feynman
- [Association of Computing Machinery (ACM) and IEEE Computer Society's joint undergraduate curricula guidelines and recommendations for Computer Science and Computer Engineering](http://www.acm.org/education/curricula-recommendations)（用于比较你所知道的和你应该知道的）
- CS Theory StackExchange 上关于[每个人都应该阅读的书籍](https://cstheory.stackexchange.com/questions/3253/what-books-should-everyone-read)的讨论
