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
This page contains Computer Science and Engineering textbook recommendations.

## Fundamentals

In order to have a solid CS&E foundation, you should touch upon each of the following fundamental topics. If your focus is on Computer Engineering (CpE), Electrical and Computer Engineering (ECE), or just have a strong interest in hardware then you should also study the [EEE Fundamentals](https://4chan-science.fandom.com/wiki/Electrical_and_Electronics_Engineering#Fundamentals "Electrical and Electronics Engineering") in addition to what is below.

### Basic Programming & Data Structures

*Prerequisites: [Grade School Algebra](https://4chan-science.fandom.com/wiki/Mathematics#Elementary_Algebra "Mathematics"). Useful tangential knowledge: Logic or Proofs.*

Besides considering what are good books for teaching programming concepts, you also must pick a particular language to start with. Don't start learning too many languages at once before you have a solid grasp of one, say C++, to act as a frame of reference. As for language choice, you should consider avoiding Java and Basic like the plague as they can instill terrible habits and don't listen to rabid C fanboys that claim C++ is "too hard for beginners", "bloated", "slow", or any other incorrect and greatly misinformed claims on the C++ language. You should also be aware that most material in this list and in general will assume that you know or are familiar with C++ or at least C.

Possible books to look into if you want to start with C++ (which is arguably the most versatile) would be:

- Programming: Principles and Practice Using C++ by Stroustrup (Written by the creator of C++. An excellent introduction to programming and to C++)
- C++ Primer by Lippman, Lajoie, and Moo (Works as a follow up to Programming: Principles and Practice or as a first book on C++ with some prior programming experience) \*Not to be confused with C++ Primer Plus (Stephen Prata), which has a less than favorable [reception](http://accu.org/index.php?module=bookreviews&func=search&rid=1744).

This cannot be stressed enough: Even if all you were looking for is to learn the basics of how to code, once you've mastered the syntax of programming (such as with the books above) you mustn't stop there. Rather, continue on to studying the structure, implementation, and analysis of common data structures (and the basic algorithms that go with them). This is utterly essential for fully grasping programming and for coding any program with even an ounce of complexity behind it (i.e. any useful program whatsoever). You do not know any programming until you've done so.

The best data structures book for C++ is:

- Data Structures and Algorithms in C++ by Drozdek

Another older and language agnostic book with Pseudo-pascal code is:

- Data Structures and Algorithms by Aho, Ullman, and Hopcroft

Even though it's in pseudo-code, at this stage of your education you really should try implementing the topics covered in whatever language you know. After studying one of the above, you will be able to move on to the algorithms textbooks in the section below.

To go further into data structures than what CS&E majors typically do in their 2nd programming course, this 2nd book (it's in C but it's close enough to C++) makes a good follow up:

- Advanced Data Structures by Peter Brass

For additional references on advanced topics in C++ programming:

- The C++ Standard Library: A Tutorial and Reference by Josuttis
- Effective C++: 55 Specific Ways to Improve Your Programs and Designs by Scott Meyers
- Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14 by Scott Meyers
- The C++ Programming Language by Stroustrup

Other language materials can be found on the [Programming Textbook Recommendations](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations "Programming Textbook Recommendations") page

### Learn your way around a Unix shell, Make, System Programming and C

Assuming you don't know them already that is. If you know the basics of C++, learning C distills down to learning what you can't do anymore and the few quirks where C behaves differently: see [C for C++ Programmers](http://www.ccs.neu.edu/course/com3620/parent/C-for-Java-C++/c-for-c++-alt.html) for some of the differences.

- Advanced Programming in the UNIX Environment by Stevens and Rago (The rough Windows equivalent would be Windows System Programming by Hart and/or Windows Via C/C++ by Richter and Nasarre)
- [Make Manual](http://www.gnu.org/software/make/manual/)
- The C Programming Language by Kernighan and Ritchie (known as K&R, but beware it was published in 1988 and the C language has changed with C99 and C11 standards)
- C Programming: A Modern Approach by King
- [Modern C by Jens Gustedt](https://gustedt.gitlabpages.inria.fr/modern-c/)

You should also start learning how to use revision control systems like SVN or git especially if you see yourself working on large code bases or on a team in the future. Contrary to the popular belief, learning to use a 1970s style terminal text editor like vim/emacs is completely unnecessary and unhelpful.

### Computer Architecture and Digital Logic

#### Digital Logic

*Prerequisites: [Precalculus](https://4chan-science.fandom.com/wiki/Mathematics#Precalculus "Mathematics"). Useful tangential knowledge: Programming and Circuits.*

- Digital Design: Principles and Practices by Wakerly
- Fundamentals of Logic Design by Roth & Kinney (Alternative to Wakerly)
- Digital Design and Computer Architecture by David Harris and Sarah Harris (Introductory book bridging digital logic and computer architecture)

#### Computer Organization and Architecture

*Prerequisites: Programming. Useful tangential knowledge: Unix, Circuits, and Logic.*

- Computer Organization and Design: The Hardware/Software Interface by Patterson & Hennessy (The assembly language used in old editions was MIPS, the newest edition uses ARM)
- Computer Systems: A Programmer's Perspective by Bryant & O'Hallaron (AMD64 based assembly)

Follow up 2nd book on advanced modern and high performance architecture:

- Computer Architecture: A Quantitative Approach by Hennessy & Patterson (The order of their names differentiates between their 2 books, this one is more advanced)
- Parallel Computer Organization and Design by Dubois, Annavaram, and Stenström (Covers more than just parallel topics)
- Modern Processor Design: Fundamentals of Superscalar Processors by John Paul Shen

Other references:

- The Intel Microprocessors by Barry B. Brey
- Microprocessor Architecture: From Simple Pipelines to Chip Multiprocessors by Jean-Loup Baer

For a comprehensive reference of x86/AMD64 assembly language: [Intel <sup>®</sup> 64 and IA-32 Architectures Software Developer Manuals](http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html) (It's 3463 pages long so do not try to read it all)

### Operating Systems

*Prerequisites: Architecture and C/C++ Programming. Useful tangential knowledge: Unix, System Programming.*

- Operating System Concepts by Silberschatz, Galvin, and Gagne (The Dinosaur book)
- Modern Operating Systems by Tanenbaum

For more see the [OS Development](#OS_Development) section

### Mathematics Primer

To study algorithms, compilers, complexity theory, and advanced topics you'll need some familiarity with abstract topics such as proofs, sets, number theory, combinatorics, graph theory, and probability. But the good *(or bad)* news is that you don't need that much in terms of *depth* in most of these areas at the beginning of your studies so you don't have to worry about fully mastering them all at once. Eventually, you will want to dive deeper and resources for that are provided in the [Mathematics](#Mathematics) section. Now is also the best time for you to consider learning [LaTeX](https://4chan-science.fandom.com/wiki/Universal_Material#LaTeX "Universal Material") and practicing typesetting most of your work in it.

#### Proofs and Mathematical Reasoning

*Prerequisites: [Precalculus](https://4chan-science.fandom.com/wiki/Mathematics#Precalculus "Mathematics"). Useful tangential knowledge: Digital Logic or Philosophical Logic.*

The most important topics you absolutely want to fully grasp here is the skill of reading and writing proofs, logical expressions, and naive set theory. Sadly, even majors who take courses on discrete mathematics still find that proofs totally elude them. You could try to pick up proofs in a discrete math book but you will find yourself lacking in much needed practice. Therefore it's strongly recommend that you study a mathematics oriented exposition on proofs instead. The last thing you want is to do is to be struggling with proofs when you move on to later topics and that will almost guarantee you failure or at least a terrible time.

- A Transition to Advanced Mathematics by Smith, Eggen, and St. Andre
- A Primer of Abstract Mathematics by Ash
- Conjecture and Proof by Laczkovich (An excellent supplement to the above books and shows a larger variety of proofs in mathematics)
- Proofs from THE BOOK by Aigner and Ziegler (Not a textbook on proofs but it is an excellent collection of well done and elegant proofs to appreciate and draw inspiration from)

If you still find yourself struggling with proofs, then the following books take a far more hand holding approach through them (but at the cost of excluding some valuable material)

- How to Prove It: A Structured Approach by Velleman
- How to Read and Do Proofs: An Introduction to Mathematical Thought Processes by Solow
- [Book of Proof by Hammack](http://www.people.vcu.edu/~rhammack/BookOfProof/)

Now that you can finally reason your way out of a paper bag, there's not much to learn that you couldn't pick up as you go. But to be familiar with the topics ahead of time, these books serve as a crash course (remember that discrete mathematics barely scratches the surface of most topics they cover, feel free to skip to books covering these topics if you want depth):

- Concrete Mathematics: A Foundation for Computer Science by Graham, Knuth, and Patashnik
- Discrete Mathematics and Its Applications by Rosen (The level is a bit lower than Graham and covers similar material to the proof books)

#### Probability

There's also the standard requirements that you know [Calculus](https://4chan-science.fandom.com/wiki/Mathematics#Calculus "Mathematics") and [Linear Algebra](https://4chan-science.fandom.com/wiki/Mathematics#Linear_Algebra "Mathematics") so if you haven't already done so, go learn about them. One last thing to study at this level is introductory probability which is indispensable for dealing with the real world.

- The Art Of Probability by Hamming (Great introduction or supplement to the other probability texts)
- Probability by Pitman
- A First Course in Probability by Ross
- [An Introduction to Probability and Random Processes by Rota and Baclawski](http://www.ellerman.org/gian-carlo-rota/)

See also the EEE's [Probability and Stochastic Processes](https://4chan-science.fandom.com/wiki/Electrical_and_Electronics_Engineering#Probability_and_Stochastic_Processes) recommendations.

### Algorithms

*Prerequisites: Programming and Proofs. Useful tangential knowledge: Graph theory, Combinatorics*

The study of algorithms and their analysis is essential for any serious work in the field.

- Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein <sup><a href="http://www.cs.dartmouth.edu/~thc/clrs-bugs/bugs-3e.php">[Errata]</a></sup> (Known as CLRS and is very encyclopedic)
- Algorithms in C++ Parts 1-5: Fundamentals, Data Structures, Sorting, Searching, and Graph Algorithms by Sedgewick (Also available in a C version. Covers theory and implementation details)
- Algorithm Design by Kleinberg and Tardos (Greater focus on the process of designing algorithms rather than collecting and analyzing the most common algorithms)
- The Design and Analysis of Algorithms by Kozen (Supplement to the above books with more advanced topics and good introduction to complexity theory)
- An Introduction to the Analysis of Algorithms by Sedgewick and Flajolet (The book concerns itself with the mathematical analysis of algorithms. The authors' "Analytic Combinatorics" book is a continuation)

and as a reference

- The Art of Computer Programming by Knuth

### Various Programming Languages, Paradigms, and Compilers

*Prerequisites: Programming. Useful tangential knowledge: Architecture and Algorithms.*

You should study a few different "feeling" programming languages that operate differently from what you're comfortable with. Common languages people tend to study are: [Lisp/Scheme/Racket](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations#Lisp.2FScheme.2FRacket "Programming Textbook Recommendations"), [Prolog](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations#Prolog "Programming Textbook Recommendations"), [Haskell](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations#Haskell "Programming Textbook Recommendations"), [Forth](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations#Forth "Programming Textbook Recommendations") (or Factor), [J](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations#J "Programming Textbook Recommendations"), [Matlab](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations#Matlab "Programming Textbook Recommendations"), [Python](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations#Python "Programming Textbook Recommendations"), [Lua](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations#Lua "Programming Textbook Recommendations"), C#, and [C++](https://4chan-science.fandom.com/wiki/Programming_Textbook_Recommendations#C++ "Programming Textbook Recommendations"). Similarly you should also delve into the study of the structures that these languages have and into the theory of compilers behind their translation into machine instructions

*Prerequisites: Architecture and Algorithms. Useful tangential knowledge: Automata, Complexity Theory, and Mathematical Logic.*

- Programming Language Pragmatics by Scot
- Engineering a Compiler by Cooper and Torczon <sup><a href="http://www.cs.rice.edu/~keith/Errata.html">[Errata]</a></sup>
- Compilers: Principles, Techniques, and Tools by Aho, Lam, Sethi, and Ullman (The Dragon book)
- Advanced Compiler Design and Implementation by Muchnick (More advanced, read it when you finish the above and still want more)

### Automata, Computability Theory, and Complexity Theory

*Prerequisites: Algorithms. Useful tangential knowledge: Digital Logic, Architecture, and Mathematical Logic.*

"How do you know that it's even possible to solve a given problem on a computer? And even if it is possible, how difficult in terms of computational resources will it be to solve that problem?" [The Theory of Computation](https://en.wikipedia.org/wiki/Theory_of_computation) is based on answering these fundamental questions. The subject naturally breaks down into 3 distinct parts. First, we must come up with mathematical models of what computation devices are so we can start proving general theorems and results about them. This is the domain of Formal Languages and [Automata](https://en.wikipedia.org/wiki/Automata_theory). Next comes [Computability Theory](https://en.wikipedia.org/wiki/Computability) where we determine what's possible to do on these abstract machines. Finally, we reach [Complexity Theory](https://en.wikipedia.org/wiki/Computational_complexity_theory) which concerns itself with what is possible given limited computational resources: "Can a problem be solve in [logarithmic](https://en.wikipedia.org/wiki/L_\(complexity\)) or [polynomial](https://en.wikipedia.org/wiki/PSPACE) *space* or in [polynomial](https://en.wikipedia.org/wiki/P_\(complexity\)) or [exponential](https://en.wikipedia.org/wiki/EXPTIME) or [double exponential](https://en.wikipedia.org/wiki/2-EXPTIME) *time*? Does [randomness](https://en.wikipedia.org/wiki/Nondeterministic_algorithm) help you solve problems faster? Is finding the [negative answer](https://en.wikipedia.org/wiki/Complement_\(complexity\)) as easy as finding the positive? Is the problem [parallelizable](https://en.wikipedia.org/wiki/NC_\(complexity\))?"

- Introduction to the Theory of Computation by Sipser <sup><a href="http://www-math.mit.edu/~sipser/book.html">[Errata]</a></sup>

Sipser is a very easy to read (almost middle school level) book covering all three areas while requiring no more than the ability to read and write simple proofs. Great for people outside of CS who want to learn and understand the subject with the added benefit that anyone who completes the book will know the subject better than 99.95% of CS majors and will be able to easily call them out when they butcher and grossly misrepresent it (which they do quite often). Downside is that it's horribly overpriced and math savvy readers will be annoyed that it doesn't go much deeper.

- Automata and Computability by Kozen (Covers the first 2 areas of the subject in more mathematical detail than Sipser)
- Computational Complexity: A Modern Approach by Arora and Barak (Can be used as a follow up to Sipser or 1st book on Complexity that goes deep)
- Theory of Computation by Kozen
- Computability, Complexity, and Languages: Fundamentals of Theoretical Computer Science by Martin Davis, Ron Sigal, and Elaine Weyuker

References

- Computers and Intractability: A Guide to the Theory of NP-Completeness by Garey and Johnson

## Special Topics

### Parallel Programming

*Prerequisites: Programming in C/C++ and Architecture. Useful tangential knowledge:* Operating Systems*.*

As computers grow increasingly parallel, it's important to learn how to (and when to) program with [OpenMP](http://openmp.org/wp/openmp-specifications/), MPI, pthreads/std::thread, and OpenCl and be aware of the unique aspects of parallel algorithms from their linear brothers. Good books are hard to find but most recommend these as a general introduction:

- An Introduction to Parallel Programming by Pacheco (covers MPI, Pthreads, and OpenMP)
- Introduction to Parallel Computing by Grama, Karypis, Kumar, and Gupta (covers MPI, Pthreads, and OpenMP)
- C++ Concurrency in Action: Practical Multithreading by Williams (just covers std::thread)
- Heterogeneous Computing with OpenCL by Gaster, Howes, Kaeli, et al. (you should be familiar with basic parallel programming before moving on to GPGPU coding)
- OpenCL in Action: How to Accelerate Graphics and Computations by Scarpino
- OpenCL Programming Guide by Munshi, Gaster, et al.

### Networks

*Prerequisites: Programming and Probability. Useful tangential knowledge: Operating Systems, Algorithm, Parallel Programming, or Graph Theory*

- Computer Networks: A Systems Approach by Peterson and Davie
- Computer Networks by Tanenbaum
- Unix Network Programming, Volume 1: The Sockets Networking API by Stevens, Fenner, and Rudoff
- Interconnections: Bridges, Routers, Switches, and Internetworking Protocols by Perlman
- [Data Networks](http://web.mit.edu/dimitrib/www/datanets.html) by Bertsekas and Gallager

### Computer Security and Cryptography

*Prerequisites: Proofs, (lite) Probability, and (lite) Algorithms/Programming. Useful tangential knowledge: Complexity Theory, Abstract Algebra, and Number Theory*

- Introduction to Modern Cryptography by Katz and Lindell [<sup>[Errata]</sup>](https://www.cs.umd.edu/~jkatz/imc.html) (Great starting point, focuses on *provable security* that answers the question of "when you should use what system and why")
- Cryptography Engineering: Design Principles and Practical Applications by Niels Ferguson, Bruce Schneier, Tadayoshi Kohno (Focuses on implementation details of cryptographic systems)
- An Introduction to Mathematical Cryptography by Hoffstein, Pipher, and Silverman [<sup>[Website]</sup>](https://www.math.brown.edu/~jhs/MathCryptoHome.html)

Also see [Reverse Engineering and Malware Analysis](#Reverse_Engineering_and_Malware_Analysis)

### Information Theory and Coding Theory

*Prerequisites: Proofs, Probability, and Linear Algebra. Useful knowledge: Abstract Algebra, Analysis, and Measure Theory. Useful tangential knowledge: Signal and Systems Analysis, Digital Signal Processing, Communication Systems, and Complexity Theory*

- Elements of Information Theory by Cover and Thomas
- The Mathematical Theory of Communication by Claude Shannon and Warren Weaver (The paper that started it all and is very readable, beautiful, and still useful to read)
- Principles of Digital Communication and Coding (Dover Books on Electrical Engineering) by Viterbi and Omura
- Introduction to Data Compression by Sayood
- Information Theory (Dover Books on Mathematics) by Ash
- Network Information Theory by El Gamal and Kim
- Coding and Information Theory by Roman
- Information Theory and Reliable Communication by Gallager

Also take a look at MacKay's book in the next section below.

For Quantum Information Theory see

- Quantum Information Theory by Mark Wilde (Available online as " [From Classical to Quantum Shannon Theory](https://arxiv.org/abs/1106.1445) ")

### AI, Machine Learning, and Computer Vision

*Prerequisites: Programming Languages, Probability, Vector Calculus, and Linear Algebra. Useful knowledge: Statistics (especially Bayesian), Graph Theory, Optimization, Approximation Algorithms, Information Theory, Fourier and Functional Analysis, and Measure Theory. Useful tangential knowledge: Signal and System Analysis, Digital Signal Processing, Control Theory, Theoretical Neuroscience*

Warning: most everything people say about these areas are wild pipe dreams, don't get your hopes up. Studying digital image processing and a bit of computer graphics beforehand would be very helpful for computer vision.

- Artificial Intelligence: A Modern Approach by Russell and Norvig
- Computer Vision by Shapiro and Stockman
- Multiple View Geometry in Computer Vision by Hartley and Zisserman <sup><a href="http://www.robots.ox.ac.uk/~vgg/hzbook/">[Errata]</a></sup>
- Computer Vision: Algorithms and Applications by Szeliski
- Pattern Recognition and Machine Learning by Bishop
- Information Theory, Inference & Learning Algorithms by MacKay ([Available for free online](http://www.inference.phy.cam.ac.uk/mackay/itila/book.html))
- The Elements of Statistical Learning: Data Mining, Inference, and Prediction by Hastie, Tibshirani, and Friedman ([Available for free online](https://hastie.su.domains/Papers/ESLII.pdf))

### Natural Language Processing

- Natural Language Understanding by Allen (a bit dated)
- Foundations of Statistical Natural Language Processing by Manning and Schütze
- Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition by Jurafsky and Martin

See also EEE's [Speech Processing](https://4chan-science.fandom.com/wiki/Electrical_and_Electronics_Engineering#Speech_Processing "Electrical and Electronics Engineering") recommendations.

### Computer Graphics and Image Processing

*Prerequisites: Programming, Vector Calculus, and Linear Algebra. Useful tangential knowledge: Modern Geometry, Quaternions, Signal and System Analysis, Numerical Analysis, or Parallel Programming*

- Digital Image Processing by Gonzalez
- Fundamentals of Computer Graphics by Shirley and Marschner
- Computer Graphics: Principles and Practice by Hughes, van Dam, McGuire, Sklar, Foley, Feiner, Akeley (updated/rewritten version of the classic CG bible *Computer Graphics: Principles and Practice in C by Foley, van Dam, Feiner, and Hughes*)

### Discrete and Computational Geometry

- Computational Geometry: Algorithms and Applications by de Berg, Cheong, van Kreveld, and Overmars
- Discrete and Computational Geometry by Devadoss and O'Rourke
- Lectures on Discrete Geometry by Matousek <sup><a href="http://kam.mff.cuni.cz/~matousek/dg.html">[Errata]</a></sup>

### Advanced Algorithms and Mathematical Optimization

*Prerequisites: Algorithms, Probability, Proofs, and Linear Algebra. Useful tangential knowledge: Combinatorics (strongly advised), Graph Theory (strongly advised), Complexity Theory*

#### Linear Programming/Optimization

- Introduction to Linear Optimization by Bertsimas & Tsitsiklis
- Theory of Linear and Integer Programming by Schrijver

#### Combinatorial Optimization and Network Flows

- Network Flows by Ahuja, Magnanti & Orlin <sup><a href="http://jorlin.scripts.mit.edu/Network_Flows:_Theory,_Algorithms,_and_Applications.html">[Errata]</a></sup>
- Combinatorial Optimization by Cook, Cunningham, Pulleyblank, and Schrijver
- Combinatorial Optimization - Theory and Algorithms by Korte & Vygen
- Combinatorial Optimization, Polyhedra and Efficiency by Schrijver <sup><a href="http://homepages.cwi.nl/~lex/co/">[Errata]</a></sup>

#### Convex Optimization

- [Convex Optimization](http://stanford.edu/~boyd/cvxbook/) by Boyd and Vandenberghe
- [Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications](http://www2.isye.gatech.edu/~nemirovs/Lect_ModConvOpt.pdf) by Ben-Tal and Nemirovski
- [Convex Optimization & Euclidean Distance Geometry](https://ccrma.stanford.edu/~dattorro/mybook.html) by Dattorro
- Convex Analysis by Rockafellar (for the theory, requires some baby analysis)

#### Approximation Algorithms

- [Approximation Algorithms](http://www.cc.gatech.edu/fac/Vijay.Vazirani/book.pdf) by Vazirani
- [The Design of Approximation Algorithms](http://www.designofapproxalgs.com/index.php) by Williamson and Shmoys
- Design and Analysis of Approximation Algorithms by Ding-Zhu Du, Ker-I Ko, Xiaodong Hu

#### Randomized Algorithms

- Randomized Algorithms by Motwani and Raghavan

### Numerical Analysis and Methods

*Prerequisites: Basic Programming, Vector Calculus, Linear Algebra, basic DEs. Useful tangential knowledge: Algorithms, Architecture, Analysis.*

#### Numerical Recipes

- Numerical Methods for Engineers by Steven Chapra, Raymond Canale
- Scientific Computing: An Introductory Survey, Revised Second Edition by Michael T. Heath
- Scientific Computing with MATLAB and Octave by Alfio Quarteroni, Fausto Saleri, Paola Gervasio

#### Overviews of Numerical Analysis

- Numerical Methods for Scientists and Engineers (Dover Books) by Hamming
- Numerical Analysis by Burden and Faires
- An Introduction to Numerical Analysis by Atkinson
- An Introduction to Numerical Analysis by Süli and Mayers
- Numerical Analysis: A Mathematical Introduction by Schatzman

#### Numerical Linear Algebra

- Matrix Computations by Golub and Van Loan
- Numerical Linear Algebra by Trefethen and Bau III
- Matrix Analysis by Horn and Johnson

#### Approximation Theory

- Introduction to Approximation Theory by Cheney
- Interpolation and Approximation (Dover Books) by Davis
- Approximation Theory and Methods by Powell
- Approximation Theory and Approximation Practice by Trefethen <sup>[<a href="https://people.maths.ox.ac.uk/trefethen/ATAP/">site</a>, <a href="http://www.chebfun.org/ATAP/">mirror</a>]</sup>

More advanced books:

- Theory of Approximation (Dover Books) by Achieser
- [Theory of Approximation of Functions of a Real Variable](https://archive.org/details/theoryofapproxim033501mbp) (Dover Books) by Timan (Careful, Amazon links this and Achieser's book together...)

#### Numerical Ordinary Differential Equations

- Computer Methods for Ordinary Differential Equations and Differential-Algebraic Equations by Ascher and Petzold
- Numerical Methods for Ordinary Differential Equations by Butcher
- Solving Ordinary Differential Equations I: Nonstiff Problems by Hairer, Nørsett, and Wanner
- Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems by Hairer and Wanner
- Geometric Numerical Integration: Structure-Preserving Algorithms for Ordinary Differential Equations by Hairer, Lubich, and Wanner

#### Numerical Partial Differential Equations

- [Finite Difference and Spectral Methods for Ordinary and Partial Differential Equations by Trefethen](https://people.maths.ox.ac.uk/trefethen/pdetext.html)

##### Finite Difference Methods

- Finite Difference Methods for Ordinary and Partial Differential Equations: Steady-State and Time-Dependent Problems by LeVeque <sup>[<a href="https://faculty.washington.edu/rjl/fdmbook/">Website</a>]</sup>
- Numerical Partial Differential Equations: Finite Difference Methods by Thomas
- Finite Difference Schemes and Partial Differential Equations by Strikwerda

##### Finite Element Methods

- Finite Element Analysis: From Concepts to Applications by Burnett
- Applied Finite Element Analysis by Segerlind
- Programming the Finite Element Method by Smith, Griffiths, and Margetts
- Numerical Solution of Partial Differential Equations by the Finite Element Method (Dover Books on Mathematics) by Johnson
- The Mathematical Theory of Finite Element Methods by Brenner and Scott
- Theory and Practice of Finite Elements by Ern and Guermond

##### Spectral Methods

- [Chebyshev and Fourier Spectral Methods (Dover Books on Mathematics) by Boyd](http://www-personal.umich.edu/~jpboyd/BOOK_Spectral2000.html)
- Implementing Spectral Methods for Partial Differential Equations: Algorithms for Scientists and Engineers by Kopriva
- Spectral Methods: Fundamentals in Single Domains by Canuto, Hussaini, Quarteroni, and Zang
- Spectral Methods: Evolution to Complex Geometries and Applications to Fluid Dynamics Canuto, Hussaini, Quarteroni, and Zang

### Computer Algebra Systems and Computer Arithmetic

- Modern Computer Algebra von zur Gathen and Gerhard
- Modern Computer Arithmetic by Brent and Zimmermann
- Handbook of Floating-Point Arithmetic by Muller, Brisebarre, de Dinechin, et al.
- Elementary Functions: Algorithms and Implementation by Muller
- Computer Arithmetic: Algorithms and Hardware Designs by Behrooz Parhami
- Synthesis of Arithmetic Circuits: FPGA, ASIC and Embedded Systems by Deschamps, Bioul, and Sutter
- Hardware Implementation of Finite-Field Arithmetic by Deschamps, Imana, Sutter

### Finite Fields

- Finite Fields for Computer Scientists and Engineers by McEliece (Short and well written intro)
- Introduction to Finite Fields and Their Applications by Lidl and Niederreiter (A more comprehensive intro)
- Finite Fields (Encyclopedia of Mathematics and its Applications) by Lidl and Niederreiter (An expanded version of the above, often called the bible of FF but dated to 1980s)
- Handbook of Finite Fields by Mullen and Panario (Extensive reference work that has more recent results than Lidl. Mullen also has a very breif intro text as well)
- Lectures on Finite Fields (Graduate Studies in Mathematics) by Xiang-Dong Hou (A more mathematical selection of topics on FF)

See also [Applied Abstract Algebra](https://4chan-science.fandom.com/wiki/Mathematics#Survey_of_Abstract_Algebra_Applications "Mathematics") math page

### Mathematics

Try to avoid books directly targeting CS majors and/or with titles like "Discrete Math" as they tend to teach next to nothing.

- An Introduction to the Theory of Numbers by Hardy and Wright
- Combinatorics and Graph Theory by Harris, Hirst, and Mossinghoff
- Combinatorics: Topics, Techniques, Algorithms by Cameron
- All of Statistics: A Concise Course in Statistical Inference by Wasserman
- Probability Models by Sheldon Ross
- Signals and Systems by Oppenheim
- Discrete-Time Signal Processing by Oppenheim
- Analytic Combinatorics by Flajolet and Sedgewick (follow up to their algorithm book)
- Quaternions and Rotation Sequences: A Primer with Applications to Orbits, Aerospace, and Virtual Reality by Kuipers
- Geometry by Brannan, Esplen, and Gray
- Geometric Methods and Applications: For Computer Science and Engineering by Gallier <sup><a href="http://www.cis.upenn.edu/~jean/gbooks/geom2.html">[Website]</a></sup>
- Logic for Computer Science: Foundations of Automatic Theorem Proving by Gallier

see also [Math Textbook Recommendations](https://4chan-science.fandom.com/wiki/Math_Textbook_Recommendations "Math Textbook Recommendations"), [Mathematics](https://4chan-science.fandom.com/wiki/Mathematics "Mathematics") page, and [Statistics Recommendations](https://4chan-science.fandom.com/wiki/Universal_Material#Statistics "Universal Material")

### Combinatorial Game Theory

Not to be confused with ["Economic" Game Theory](https://4chan-science.fandom.com/wiki/Economics_Textbook_Recommendations#Game_Theory "Economics Textbook Recommendations"), [Combinatorial Game Theory](https://en.wikipedia.org/wiki/Combinatorial_game_theory) studies sequential games where each player has perfect knowledge.

- On Numbers and Games by John H. Conway
- Winning Ways for Your Mathematical Plays: Volume 1-4 by Elwyn R. Berlekamp, John H. Conway, and Richard K. Guy
- Games, Puzzles, and Computation by Robert A. Hearn and Erik D. Demaine (complexity of games)
- Combinatorial Game Theory (Graduate Studies in Mathematics) by Aaron N. Siegel
- Combinatorial Games: Tic-Tac-Toe Theory by József Beck
- [Games of No Chance](http://library.msri.org/books/Book29/contents.html), [More Games of No Chance](http://library.msri.org/books/Book42/contents.html), [Games of No Chance 3](http://library.msri.org/books/Book56/contents.html), [Games of No Chance 4](http://library.msri.org/books/Book63/contents.html); Edited by Richard Nowakowski

### Quantum Computing

No, quantum computers won't magically be all powerful and able to solve all the world's problems nor is it a sure fire way of solving all the problems in NP but it's still a very interesting and rapidly developing field. You don't need thoroughly study all of the material in Sakurai, Shankar, or Griffiths' Quantum Mechanics texts to read about Quantum Computing but you do obviously need some understanding of QM. The following books will give you all the understanding of what Quantum Mechanics *means* that you always wanted to know - and if you happen to be a physics student or autodidact, probably never got in Sakurai, Shankar, or Griffiths' books or in the all too common "shut up and calculate!" lectures making them more than worthwhile to study and appreciate even with a QM background as well.

- Quantum Processes, Systems, and Information by Schumacher and Westmoreland
- Quantum Theory: Concepts and Methods by Peres
- Quantum Theory by David Bohm (Insight into the relationship between classical mechanics and quantum theory)

If you're interested in learning more about physics and QM see the [Physics Textbook Recommendations](https://4chan-science.fandom.com/wiki/Physics_Textbook_Recommendations "Physics Textbook Recommendations")

- An Introduction to Quantum Computing by Kaye, Laflamme, and Mosca
- Classical and Quantum Computation by Kitaev, Shen and Vyalyi
- Quantum Computation and Quantum Information by Michael Nielsen and Isaac Chuang (The book and reference on QC)
- Quantum Computing: A Short Course From Theory To Experiment by Stolze and Suter (More on the Quantum Engineering side and requires a strong physics background)
- Introduction to Topological Quantum Computation by Jiannis K. Pachos (Basic Overview of TQC)

### Type Theory and Programming Language Theory

*Prerequisites: Programming Language Concepts, Proofs. Useful tangential knowledge: Mathematical Logic, Abstract Algebra*

- Types and Programming Languages by Pierce <sup><a href="http://www.cis.upenn.edu/~bcpierce/tapl/">[Errata]</a></sup>
- Advanced Topics in Types and Programming Languages by Pierce <sup><a href="http://www.cis.upenn.edu/~bcpierce/attapl/index.html">[Errata]</a></sup>
- Practical Foundations for Programming Languages by Harper <sup><a href="https://www.cs.cmu.edu/~rwh/plbook/2nded.pdf">[Draft]</a></sup>
- Foundations for Programming Languages by Mitchell
- Formal Semantics of Programming Languages by Winskel

### OS Development

- Linux Kernel Development by Love
- Linkers and Loaders by Levine
- Linux Device Drivers by Corbet, Rubini, and Kroah-Hartman
- Understanding the Linux Kernel by Bovet and Cesati
- The Design of the UNIX Operating System by Bach
- The Design and Implementation of the FreeBSD Operating System by McKusick, Neville-Neil, and Watson
- Windows <sup>®</sup> Internals by Russinovich, Solomon, and Ionescu (For when fate forces you to deal with Windows)
- Professional Linux Kernel Architecture by Wolfgang Mauerer

### Reverse Engineering and Malware Analysis

*Prerequisites: Architecture and Operating Systems. Useful tangential knowledge: Computer Security, OS Development, Unix/Windows, Networks, or Compilers*

- Reversing: Secrets of Reverse Engineering by Eilam
- The Shellcoder's Handbook: Discovering and Exploiting Security Holes by Anley, Heasman, Lindner, and Richarte
- Practical Malware Analysis: The Hands-On Guide to Dissecting Malicious Software by Sikorski and Honig
- Practical Reverse Engineering: x86, x64, ARM, Windows Kernel, Reversing Tools, and Obfuscation by Dang, Gazet, and Bachaalany
- The Rootkit Arsenal: Escape and Evasion in the Dark Corners of the System by Blunden
- A Guide to Kernel Exploitation: Attacking the Core by Perla and Oldani

### Software Engineering, Development, and Project Management

*Prerequisites: Programming. Useful tangential knowledge: Experience with large programs.*

- **The Mythical Man-Month: Essays on Software Engineering** by Brooks
- Code Complete: A Practical Handbook of Software Construction by McConnell
- Design Patterns: Elements of Reusable Object-Oriented Software by Gamma, Helm, Johnson, and Vlissides (Gang of Four book)
- Software Requirements and Specifications: A Lexicon of Practice, Principles and Prejudices by Jackson
- Working Effectively with Legacy Code by Feathers
- The Pragmatic Programmer by Hunt and Thomas
- Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin
- Refactoring: Improving the Design of Existing Code by Fowler
- Peopleware: Productive Projects and Teams by DeMarco and Lister
- The psychology of computer programming by Gerald Weinberg

### Databases

- An Introduction to Database Systems by Date
- Database Management Systems by Ramakrishnan and Gehrke
- Readings in Database Systems by Hellerstein and Stonebraker [<sup>[Red Book Website]</sup>](http://www.redbook.io/)
- Transaction Processing: Concepts and Techniques by Gray and Reuter
- Transactional Information Systems: Theory, Algorithms, and the Practice of Concurrency Control and Recovery by Weikum and Vossen

### Distributed Systems and Computing

- Distributed Systems: Principles and Paradigms by Tanenbaum and van Steen
- Distributed Systems by Mullender
- Distributed Algorithms by Lynch
- Introduction to Distributed Algorithms by Tel
- Distributed Computing: Fundamentals, Simulations, and Advanced Topics by Attiya and Welch

### Game Development

*Prerequisites: Programming & Data Structures, Vector Calculus, Linear Algebra, Intro Physics. Useful knowledge: Algorithms, Architecture, Quaternions, Computer Graphics, AI, Numerical Analysis and Methods, Networks, or Software Engineering.*

Yeah, yeah, I can hear you snickering already. These aren't API guides but details on what's under the hood.

#### Overviews and Engines

- Game Engine Architecture by Gregory (Broad overview of everything that makes a game engine tick)
- Introduction to Game Development by Rabin (Covers development/engines as well as design and production/management/marketing details)

#### Game Graphics

See the above sections on general [computer graphics](#Computer_Graphics_and_Image_Processing) and [mathematics](#Mathematics) texts before moving on

- Mathematics for 3D Game Programming and Computer Graphics by Lengyel
- Real-Time Rendering by Akenine-Moller, Haines, and Hoffman
- Physically Based Rendering: From Theory To Implementation by Pharr and Humphreys

#### Game Physics

- Real-Time Collision Detection by Ericson
- Game Physics by Eberly

#### Artificial Intelligence

- Artificial Intelligence for Games by Millington and Funge
- Game AI Pro: Collected Wisdom of Game AI Professionals by Steve Rabin
- Game AI Pro 2 by Steve Rabin (AI algorithms and techniques currently being deployed in recent games)

For more AI theory, see the above section on academic AI texts.

### Miscellaneous References

- Hacker's Delight by Warren
- Computer-Related Risks by Neumann
- Ethics for the Information Age by Quinn
- The Dawn of Software Engineering: from Turing to Dijkstra by Daylight
- Programming Pearls by Bentley
- Structure and Interpretation of Computer Programs by Abelson and Sussman (Known as SICP)
- Feynman Lectures On Computation by Richard P. Feynman
- [Association of Computing Machinery (ACM) and IEEE Computer Society's joint undergraduate curricula guidelines and recommendations for Computer Science and Computer Engineering](http://www.acm.org/education/curricula-recommendations) (For comparing what you know with what you should know)
- This [thread](https://cstheory.stackexchange.com/questions/3253/what-books-should-everyone-read) on CS Theory StackExchange