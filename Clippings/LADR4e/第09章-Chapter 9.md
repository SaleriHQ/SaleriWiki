---
title: Chapter 9
source: Clippings/LADR4e.pdf
created: 2026-04-23
type: chapter
tags:
  - book
  - chapter
---

# Chapter 9
Multilinear Algebra and Determinants
Webeginthischapterbyinvestigatingbilinearformsandquadraticformsona
vectorspace. Thenwewillmoveontomultilinearforms. Wewillshowthatthe
vectorspaceofalternatingn-linearformshasdimensiononeonavectorspaceof
dimensionn. Thisresultwillallowustogiveacleanbasis-freedefinitionofthe
determinantofanoperator.
Thisapproachtothedeterminantviaalternatingmultilinearformsleadsto
straightforwardproofsofkeypropertiesofdeterminants. Forexample,wewillsee
thatthedeterminantismultiplicative,meaningthatdet(\mathcal{S}\mathcal{T})=(det\mathcal{S})(det\mathcal{T})for
alloperators\mathcal{S}and\mathcal{T}onthesamevectorspace. Wewillalsoseethat\mathcal{T}isinvertible
ifandonlyifdet\mathcal{T} \neq0. Anotherimportantresultstatesthatthedeterminantof
anoperatoronacomplexvectorspaceequalstheproductoftheeigenvaluesof
theoperator,witheacheigenvalueincludedasmanytimesasitsmultiplicity.
Thechapterconcludeswithanintroductiontotensorproducts.
standingassumptionsforthischapter
• \mathbf{F} denotes\mathbf{R} or\mathbf{C}.
• \mathcal{V} and\mathcal{W} denotefinite-dimensionalnonzerovectorspacesover\mathbf{F}.
Daniel Schwen CCBY-SA
The Mathematical Instituteatthe Universityof Göttingen. Thisbuildingopenedin1930,
when Emmy Noether(1882–1935)hadalreadybeenaresearchmathematicianand
facultymemberattheuniversityfor15years(thefirsteightyearswithoutsalary).
Noetherwasfiredbythe Nazigovernmentin1933. Bythen Noetherandher
collaboratorshadcreatedmanyofthefoundationsofmodernalgebra,includingan
abstractalgebraviewpointthatcontributedtothedevelopmentoflinearalgebra.

| --- | --------- | --- | ------------------------------ | --- | --- | --- | --- |
| 9A Bilinear | Forms | and | Quadratic | Forms |     |     |     |
| ----------- | ----- | --- | --------- | ----- | --- | --- | --- |
| Bilinear    | Forms |     |           |       |     |     |     |
A bilinear form on \mathcal{V} is a function from \mathcal{V}\times\mathcal{V} to \mathbf{F} that is linear in each slot
separately,meaningthatifweholdeitherslotfixedthenwehavealinearfunction
| intheotherslot. | Hereistheformaldefinition. |     |     |     |     |     |     |
| --------------- | -------------------------- | --- | --- | --- | --- | --- | --- |
| 9.1 definition: | bilinearform               |     |     |     |     |     |     |
isafunction\beta∶
| Abilinearformon\mathcal{V}            |                   |          |              | \mathcal{V}\times\mathcal{V} \rightarrow\mathbf{F} suchthat |     |     |     |
| --------------------------- | ----------------- | -------- | ------------ | --------------- | --- | --- | --- |
|                             |                   | v↦\beta(v,u) | and          | v↦\beta(u,v)        |     |     |     |
| arebothlinearfunctionalson\mathcal{V} |                   |          | foreveryu\in\mathcal{V}. |                 |     |     |     |
| Forexample,if\mathcal{V}              | isarealinnerprod- |          |              |                 |     |     |     |
Recallthatthetermlinearfunctional,
uctspace,thenthefunctionthattakesan
|         |                  |     |          | used in the | definition | above,    | means    |
| ------- | ---------------- | --- | -------- | ----------- | ---------- | --------- | -------- |
| ordered | pair (u,v) \in \mathcal{V}\times\mathcal{V} | to  | \langleu,v\rangle is |             |            |           |          |
|         |                  |     |          | a linear    | function   | that maps | into the |
abilinearformon\mathcal{V}. If\mathcal{V} isanonzero scalarfield\mathbf{F}. Thusthetermbilinear
| complex | inner product | space, | then this |     |     |     |     |
| ------- | ------------- | ------ | --------- | --- | --- | --- | --- |
functionalwouldbemoreconsistent
function is not a bilinear form because terminologythanbilinearform,which
theinnerproductisnotlinearinthesec- unfortunatelyhasbecomestandard.
ondslot(complexscalarscomeoutofthe
secondslotastheircomplexconjugates).
If\mathbf{F} =\mathbf{R},thenabilinearformdiffersfromaninnerproductinthataninner
productrequiressymmetry[meaningthat\beta(v,w) = \beta(w,v)forallv,w \in \mathcal{V}]
andpositivedefiniteness[meaningthat\beta(v,v)>0forallv\in\mathcal{V}\{0}],butthese
propertiesarenotrequiredforabilinearform.
| 9.2 example:    | bilinearforms |         |           |            |       |     |     |
| --------------- | ------------- | ------- | --------- | ---------- | ----- | --- | --- |
| • Thefunction\beta∶ | \mathbf{F}3\times\mathbf{F}3         | \rightarrow\mathbf{F}      | definedby |            |       |     |     |
|                 | \beta((x ,x       | ,x ),(y | ,y ,y     | ))=x y -5x | y +2x | y   |     |
|                 | 1             | 2 3     | 1 2 3     | 1 2        | 2 3   | 3 1 |     |
isabilinearformon\mathbf{F}3.
• Suppose \mathcal{A} is an n-by-n matrix with \mathcal{A} \in \mathbf{F} in row j, column k. Define a
j,k
| bilinearform\beta | on\mathbf{F}n | by  |     |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- | --- | --- |
\mathcal{A}
|     |       |      |           | n     | n   |      |     |
| --- | ----- | ---- | --------- | ----- | --- | ---- | --- |
|     | \beta ((x | ,…,x | ),(y ,…,y | ))= \sum | \sum \mathcal{A} | xy . |     |
|     | \mathcal{A}     | 1 n  | 1         | n     | j,k | j k  |     |
$$k=1j=1$$
Thefirstbulletpointisaspecialcaseofthisbulletpointwithn=3and
|     |     |     | 0   | 1 0      |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
|     |     |     | ⎛   | ⎞        |     |     |     |
|     |     | \mathcal{A}=⎜ | ⎜ 0 | 0 -5 ⎟ ⎟ |     |     |     |
|     |     |     | ⎜   | ⎟.       |     |     |     |
|     |     |     | ⎝ 2 | 0 0 ⎠    |     |     |     |

| ------------------------------------------ | --- | --- | --- | --- |
• Suppose \mathcal{V} isa real innerproduct space and \mathcal{T} \in ℒ(\mathcal{V}). Then the function
| \beta∶ \mathcal{V}\times\mathcal{V} \rightarrow\mathbf{R} definedby |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
\beta(u,v)=\langleu,\mathcal{T}v\rangle
isabilinearformon\mathcal{V}.
Ifnisapositiveinteger,thenthefunction\beta∶
| •   |     | 𝒫 (\mathbf{R})\times𝒫 | (\mathbf{R})\rightarrow\mathbf{R} | definedby |
| --- | --- | ------- | ----- | --------- |
|     |     | n       | n     |           |
\beta(p,q)=p(2)\cdotq′(3)
| isabilinearformon𝒫 | (\mathbf{R}). |     |     |     |
| ------------------ | ---- | --- | --- | --- |
n
\in\mathcal{V}′. Thenthefunction\beta∶
| • Suppose\phi,\tau |     | \mathcal{V}\times\mathcal{V} \rightarrow\mathbf{F} | definedby |     |
| ------------ | --- | ------ | --------- | --- |
\beta(u,v)=\phi(u)\cdot\tau(v)
isabilinearformon\mathcal{V}.
• More generally, suppose that \phi ,…,\phi ,\tau ,…,\tau \in \mathcal{V}′. Then the function
|     | 1 n | 1 n |     |     |
| --- | --- | --- | --- | --- |
\beta∶
\mathcal{V}\times\mathcal{V} \rightarrow\mathbf{F} definedby
| \beta(u,v)=\phi | (v)+⋯+\phi |       |     |     |
| -------- | ------- | ----- | --- | --- |
|          | (u)\cdot\tau   | (u)\cdot\tau | (v) |     |
|          | 1 1     | n     | n   |     |
isabilinearformon\mathcal{V}.
Abilinearformon\mathcal{V} isafunctionfrom\mathcal{V}\times\mathcal{V} to\mathbf{F}. Because\mathcal{V}\times\mathcal{V} isavector
space,thisraisesthequestionofwhetherabilinearformcanalsobealinearmap
from\mathcal{V}\times\mathcal{V}to\mathbf{F}. Notethatnoneofthebilinearformsin9.2arelinearmapsexcept
insomespecialcasesinwhichthebilinearformisthezeromap. Exercise3shows
| thatabilinearform\betaon\mathcal{V} | isalinearmapon\mathcal{V}\times\mathcal{V} | onlyif\beta=0. |     |     |
| --------------------- | ----------------- | ---------- | --- | --- |
\mathcal{V}(2)
**9.3 定义：** isdenotedby\mathcal{V}(2).
Thesetofbilinearformson\mathcal{V}
Withtheusualoperationsofadditionandscalarmultiplicationoffunctions,
\mathcal{V}(2) isavectorspace.
,…,e
| For\mathcal{T} anoperatoronann-dimensionalvectorspace\mathcal{V} |     |     | andabasise | 1 n |
| -------------------------------------------- | --- | --- | ---------- | --- |
of\mathcal{V},weusedann-by-nmatrixtoprovideinformationabout\mathcal{T}. Wenowdothe
samethingforbilinearformson\mathcal{V}.
matrixofabilinearform,ℳ(\beta)
**9.4 定义：** Suppose\betaisabilinearformon\mathcal{V} ande ,…,e isabasisof\mathcal{V}. Thematrixof
1 n
\betawithrespecttothisbasisisthen-by-nmatrixℳ(\beta)whoseentryℳ(\beta)
j,k
inrowj,columnkisgivenby
|     | ℳ(\beta) =\beta(e,e | ).  |     |     |
| --- | ----------- | --- | --- | --- |
|     | j,k         | j k |     |     |
If the basis e ,…,e is not clear from the context, then the notation
1 n
ℳ(\beta,(e ,…,e ))isused.
1 n

| --- | --- | --------- | --- | ------------------------------ | --- | --- | --- | --- |
Recallthat\mathbf{F}n,n
denotesthevectorspaceofn-by-nmatriceswithentriesin\mathbf{F}
| andthatdim\mathbf{F}n,n |         | =n2 (see3.39and3.40). |     |     |     |     |     |     |
| -------------- | ------- | --------------------- | --- | --- | --- | --- | --- | --- |
|                | dim\mathcal{V}(2) | =(dim\mathcal{V})2              |     |     |     |     |     |     |
9.5
|          | ,…,e |              |     | Thenthemap\beta↦ℳ(\beta)isanisomorphism |     |     |     |     |
| -------- | ---- | ------------ | --- | ------------------------------- | --- | --- | --- | --- |
| Supposee |      | isabasisof\mathcal{V}. |     |                                 |     |     |     |     |
1 n
| of\mathcal{V}(2) | onto\mathbf{F}n,n.                                      | Furthermore,dim\mathcal{V}(2) |     |     | =(dim\mathcal{V})2. |     |     |            |
| ------ | ---------------------------------------------- | ------------------- | --- | --- | --------- | --- | --- | ---------- |
|        | Themap\beta↦ℳ(\beta)isclearlyalinearmapof\mathcal{V}(2)into\mathbf{F}n,n. |                     |     |     |           |     |     | For\mathcal{A}\in\mathbf{F}n,n, |
Proof
| defineabilinearform\beta |     |     | on\mathcal{V} by |     |     |     |     |     |
| -------------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
\mathcal{A}
|     |      |        |      |        |      | n   | n      |     |
| --- | ---- | ------ | ---- | ------ | ---- | --- | ------ | --- |
|     | \beta (x | e +⋯+x | e ,y | e +⋯+y | e )= | \sum   | \sum \mathcal{A} xy |     |
|     | \mathcal{A}    | 1 1    | n n  | 1 1    | n n  |     | j,k j  | k   |
$$k=1j=1$$
forx ,…,x ,y ,…,y \in \mathbf{F} (if\mathcal{V} = \mathbf{F}n ande ,…,e isthestandardbasisof\mathbf{F}n,
| 1   | n   | 1 n |     |     | 1   | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
this\beta isthesameasthebilinearform\beta inthesecondbulletpointof Example
| \mathcal{A}   |     |     |     |     | \mathcal{A}   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
9.2).
| Thelinearmap\beta↦ℳ(\beta)from\mathcal{V}(2)to\mathbf{F}n,nandthelinearmap\mathcal{A}↦\beta |     |     |     |     |     |     |     | from |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- |
\mathcal{A}
| \mathbf{F}n,n to\mathcal{V}(2) | areinversesofeachotherbecause\beta |     |     |     |     |        | \betaforall\beta | \mathcal{V}(2) and |
| ----------- | ------------------------------ | --- | --- | --- | --- | ------ | -------- | -------- |
|             |                                |     |     |     |     | ℳ(\beta) = |          | \in        |
ℳ(\beta )=\mathcal{A}forall\mathcal{A}\in\mathbf{F}n,n,asyoushouldverify.
\mathcal{A}
Thusbothmapsareisomorphismsandthetwospacesthattheyconnecthave
| thesamedimension. |     | Hencedim\mathcal{V}(2)                   |     | =dim\mathbf{F}n,n |     | =n2 =(dim\mathcal{V})2. |     |            |
| ----------------- | --- | ------------------------------ | --- | -------- | --- | ------------- | --- | ---------- |
| Recallthat\mathcal{C}t      |     |                                |     |          |     | Thematrix\mathcal{C}t   |     |            |
|                   |     | denotesthetransposeofamatrix\mathcal{C}. |     |          |     |               |     | isobtained |
byinterchangingtherowsandthecolumnsof\mathcal{C}.
9.6 compositionofabilinearformandanoperator
| Suppose\betaisabilinearformon\mathcal{V} |                     |                |        | and\mathcal{T} | \in ℒ(\mathcal{V}).         | Definebilinearforms\alpha |     |     |
| -------------------------- | ------------------- | -------------- | ------ | ---- | --------------- | -------------------- | --- | --- |
| and\rhoon\mathcal{V}                    | by                  |                |        |      |                 |                      |     |     |
|                            |                     | \alpha(u,v)=\beta(u,\mathcal{T}v) |        | and  | \rho(u,v)=\beta(\mathcal{T}u,v). |                      |     |     |
| Lete                       | ,…,e                | beabasisof\mathcal{V}.   | Then   |      |                 |                      |     |     |
| 1                          | n                   |                |        |      |                 |                      |     |     |
|                            | ℳ(\alpha)=ℳ(\beta)ℳ(\mathcal{T})       |                |        | and  | ℳ(\rho)=ℳ(\mathcal{T})tℳ(\beta). |                      |     |     |
| Proof                      | Ifj,k \in{1,…,n},then |                |        |      |                 |                      |     |     |
|                            |                     | ℳ(\alpha)           | =\alpha(e,e |      | )               |                      |     |     |
|                            |                     |                | j,k    | j k  |                 |                      |     |     |
=\beta(e,\mathcal{T}e
$$)$$
|     |     |     |     | j   | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
n
|     |     |     | =\beta(e, | \sum   | ℳ(\mathcal{T}) | e     | )   |     |
| --- | --- | --- | ----- | --- | ---- | ----- | --- | --- |
|     |     |     |       | j   |      | m,k m |     |     |
$$m=1$$
n
|     |     |     | =   | \sum \beta(e,e | )ℳ(\mathcal{T}) |     |     |     |
| --- | --- | --- | --- | ------- | ----- | --- | --- | --- |
|     |     |     |     |         | j m   | m,k |     |     |
$$m=1$$
|     |     |     | =(ℳ(\beta)ℳ(\mathcal{T})) |     |     | .   |     |     |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
j,k
Theproofthatℳ(\rho)=ℳ(\mathcal{T})tℳ(\beta)issimilar.
Thusℳ(\alpha)=ℳ(\beta)ℳ(\mathcal{T}).

336 Chapter 9 Multilinear Algebraand Determinants
Theresultbelowshowshowthematrixofabilinearformchangesifwechange
the basis. The formula in the result below should be compared to the changeof-basisformulaforthematrixofanoperator(see3.84). Thetwoformulasare
similar,exceptthatthetranspose\mathcal{C}t appearsintheformulabelowandtheinverse
\mathcal{C}-1 appearsinthechange-of-basisformulaforthematrixofanoperator.
9.7 change-of-basisformula
Suppose\beta\in\mathcal{V}(2). Supposee ,…,e and f ,…, f arebasesof\mathcal{V}. Let
1 n 1 n
\mathcal{A}=ℳ(\beta,(e ,…,e )) and \mathcal{B}=ℳ(\beta,(f ,…, f ))
1 n 1 n
and\mathcal{C} =ℳ(\mathcal{I},(e ,…,e ),(f ,…, f )). Then
1 n 1 n
\mathcal{A}=\mathcal{C}t\mathcal{B}\mathcal{C}.
Proof Thelinearmaplemma(3.4)tellsusthatthereexistsanoperator\mathcal{T} \inℒ(\mathcal{V})
suchthat\mathcal{T}f =e foreachk =1,…,n. Thedefinitionofthematrixofanoperator
k k
withrespecttoabasisimpliesthat
ℳ(\mathcal{T},(f ,…, f ))=\mathcal{C}.
1 n
Definebilinearforms\alpha,\rhoon\mathcal{V} by
\alpha(u,v)=\beta(u,\mathcal{T}v) and \rho(u,v)=\alpha(\mathcal{T}u,v)=\beta(\mathcal{T}u,\mathcal{T}v).
Then\beta(e,e )=\beta(\mathcal{T}f,\mathcal{T}f )=\rho(f, f )forallj,k \in{1,…,n}. Thus
j k j k j k
\mathcal{A}=ℳ(\rho,(f ,…, f ))
1 n
=\mathcal{C}tℳ(\alpha,(f ,…, f ))
1 n
=\mathcal{C}t\mathcal{B}\mathcal{C},
wherethesecondandthirdlineseachfollowfrom9.6.
**9.8 例：** thematrixofabilinearformon𝒫 (\mathbf{R})
Defineabilinearform\betaon𝒫 (\mathbf{R})by\beta(p,q)=p(2)\cdotq′(3). Let
\mathcal{A}=ℳ(\beta,(1,x-2,(x-3)2)) and \mathcal{B}=ℳ(\beta,(1,x,x2))
and\mathcal{C} =ℳ(\mathcal{I},(1,x-2,(x-3)2),(1,x,x2)). Then
0 1 0 0 1 6 1 -2 9
⎛ ⎞ ⎛ ⎞ ⎛ ⎞
⎜ ⎟ ⎜ ⎟ ⎜ ⎟
\mathcal{A}=⎜ ⎜ 0 0 0 ⎟ ⎟ and \mathcal{B}=⎜ ⎜ 0 2 12 ⎟ ⎟ and \mathcal{C} =⎜ ⎜ 0 1 -6 ⎟ ⎟.
⎝ 0 1 0 ⎠ ⎝ 0 4 24 ⎠ ⎝ 0 0 1 ⎠
Nowthechange-of-basisformula9.7assertsthat\mathcal{A}=\mathcal{C}t\mathcal{B}\mathcal{C},whichyoucanverify
withmatrixmultiplicationusingthematricesabove.

| --- | --------- | ------------------------------ | --- |
| Symmetric | Bilinear Forms |     |     |
| --------- | -------------- | --- | --- |
$$( 2 )$$
| 9.9 definition: | symmetricbilinearform,\mathcal{V} | s y m |     |
| --------------- | ----------------------- | ----- | --- |
Abilinearform\rho\in\mathcal{V}(2)
iscalledsymmetricif
\rho(u,w)=\rho(w,u)
forallu,w\in\mathcal{V}. Thesetofsymmetricbilinearformson\mathcal{V}isdenotedby\mathcal{V}(2).
sym
| 9.10 example: | symmetricbilinearforms |     |     |
| ------------- | ---------------------- | --- | --- |
• If\mathcal{V} isarealinnerproductspaceand\rho\in\mathcal{V}(2) isdefinedby
\rho(u,w)=\langleu,w\rangle,
then\rhoisasymmetricbilinearformon\mathcal{V}.
• Suppose\mathcal{V} isarealinnerproductspaceand\mathcal{T} \inℒ(\mathcal{V}). Define\rho\in\mathcal{V}(2) by
\rho(u,w)=\langleu,\mathcal{T}w\rangle.
Then \rho is a symmetric bilinear form on \mathcal{V} if and only if \mathcal{T} is a self-adjoint
| operator(thepreviousbulletpointisthespecialcase\mathcal{T} |     |     | =\mathcal{I}). |
| ------------------------------------------------ | --- | --- | ---- |
Suppose\rho∶
| •   | ℒ(\mathcal{V})\timesℒ(\mathcal{V})\rightarrow\mathbf{F} | isdefinedby |     |
| --- | ----------- | ----------- | --- |
\rho(\mathcal{S},\mathcal{T})=tr(\mathcal{S}\mathcal{T}).
Then\rhoisasymmetricbilinearformonℒ(\mathcal{V})becausetraceisalinearfunctional
onℒ(\mathcal{V})andtr(\mathcal{S}\mathcal{T})=tr(\mathcal{T}\mathcal{S})forall\mathcal{S},\mathcal{T} \inℒ(\mathcal{V});see8.56.
| 9.11 definition: | symmetricmatrix |     |     |
| ---------------- | --------------- | --- | --- |
Asquarematrix\mathcal{A}iscalledsymmetricifitequalsitstranspose.
Anoperatoron\mathcal{V}mayhaveasymmetricmatrixwithrespecttosomebutnotall
basesof\mathcal{V}. Incontrast,thenextresultshowsthatabilinearformon\mathcal{V} hasasymmetricmatrixwithrespecttoeitherallbasesof\mathcal{V}orwithrespecttonobasesof\mathcal{V}.
symmetricbilinearformsarediagonalizable
9.12
| Suppose\rho\in\mathcal{V}(2). | Thenthefollowingareequivalent. |     |     |
| -------------- | ------------------------------ | --- | --- |
$$(a) \rhoisasymmetricbilinearformon\mathcal{V}.$$
| ℳ(\rho,(e     | ,…,e                                   |     | ,…,e      |
| ---------- | -------------------------------------- | --- | --------- |
| (b)        | ))isasymmetricmatrixforeverybasise     |     | of\mathcal{V}.      |
|            | 1 n                                    |     | 1 n       |
| (c) ℳ(\rho,(e | ,…,e ))isasymmetricmatrixforsomebasise |     | ,…,e of\mathcal{V}. |
|            | 1 n                                    |     | 1 n       |
| (d) ℳ(\rho,(e | ,…,e ))isadiagonalmatrixforsomebasise  |     | ,…,e of\mathcal{V}. |
|            | 1 n                                    |     | 1 n       |

| -------- | --------------------------------- | --- | --- | --- | --- |
Proof First suppose (a) holds, so \rho is a symmetric bilinear form. Suppose
e ,…,e isabasisof\mathcal{V}andj,k \in {1,…,n}. Then\rho(e,e ) = \rho(e ,e)because
| 1 n |     |     |     | j k | k j |
| --- | --- | --- | --- | --- | --- |
\rhoissymmetric. Thusℳ(\rho,(e ,…,e ))isasymmetricmatrix,showingthat(a)
1 n
implies(b).
Clearly(b)implies(c).
Nowsuppose(c)holdsande ,…,e isabasisof\mathcal{V}suchthatℳ(\rho,(e ,…,e ))
|     |     | 1   | n   |     | 1 n |
| --- | --- | --- | --- | --- | --- |
isasymmetricmatrix. Supposeu,w \in \mathcal{V}. Thereexista ,…,a ,b ,…,b \in \mathbf{F}
|             |        |          |        | 1 n     | 1 n |
| ----------- | ------ | -------- | ------ | ------- | --- |
| suchthatu=a | e +⋯+a | e andw=b | e +⋯+b | e . Now |     |
|             | 1 1    | n n      | 1 1    | n n     |     |
n n
|     |     | \rho(u,w)=\rho(\sum | ae,\sumb     | e ) |     |
| --- | --- | ---------- | --------- | --- | --- |
|     |     |            | j j       | k k |     |
|     |     |            | j=1 k=1   |     |     |
|     |     |            | n n       |     |     |
|     |     | = \sum        | \sumab \rho(e,e | )   |     |
|     |     |            | j k       | j k |     |
$$j=1k=1$$
|     |     |     | n n |     |     |
| --- | --- | --- | --- | --- | --- |
,e)
|     |     | = \sum | \sumab \rho(e |     |     |
| --- | --- | --- | ------- | --- | --- |
|     |     |     | j k     | k j |     |
$$j=1k=1$$
n n
|     |     | =\rho(\sumb | e , \sum   | ae) |     |
| --- | --- | ----- | ------- | --- | --- |
|     |     |       | k k     | j j |     |
|     |     |       | k=1 j=1 |     |     |
=\rho(w,u),
wherethethirdlineholdsbecauseℳ(\rho)isasymmetricmatrix.
Theequation
aboveshowsthat\rhoisasymmetricbilinearform,provingthat(c)implies(a).
Atthispoint,wehaveprovedthat(a),(b),(c)areequivalent. Becauseevery
diagonalmatrixissymmetric, (d)implies(c). Tocompletetheproof, wewill
showthat(a)implies(d)byinductiononn=dim\mathcal{V}.
Ifn=1,then(a)implies(d)becauseevery1-by-1matrixisdiagonal. Now
suppose n > 1 and the implication (a) ⟹ (d) holds for one less dimension.
Suppose(a)holds,so\rhoisasymmetricbilinearform. If\rho=0,thenthematrixof
\rhowithrespecttoeverybasisof\mathcal{V} isthezeromatrix,whichisadiagonalmatrix.
Hencewecanassumethat\rho \neq 0,whichmeansthereexistu,w \in \mathcal{V} suchthat
| \rho(u,w)\neq0. | Now |     |     |     |     |
| --------- | --- | --- | --- | --- | --- |
2\rho(u,w)=\rho(u+w,u+w)-\rho(u,u)-\rho(w,w).
Becausetheleftsideoftheequationaboveisnonzero,thethreetermsontheright
| cannotallequal0. | Hencethereexistsv\in\mathcal{V} |        | suchthat\rho(v,v)\neq0. |                |               |
| ---------------- | ------------------- | ------ | ----------------- | -------------- | ------------- |
|                  | ∶                   | \rho(u,v) |                   |                |               |
| Let \mathcal{U}            | = {u \in \mathcal{V}            | =      | 0}. Thus \mathcal{U} is     | the null space | of the linear |
functionalu↦\rho(u,v)on\mathcal{V}. Thislinearfunctionalisnotthezerolinearfunctional
becausev \notin \mathcal{U}. Thusdim\mathcal{U} = n-1. Byourinductionhypothesis,thereisa
basise ,…,e of\mathcal{U}suchthatthesymmetricbilinearform\rho| hasadiagonal
| 1   | n-1 |     |     | \mathcal{U}\times\mathcal{U} |     |
| --- | --- | --- | --- | --- | --- |
matrixwithrespecttothisbasis.
| Becausev\notin\mathcal{U},theliste |     | ,…,e | ,visabasisof\mathcal{V}. | Supposek | \in{1,…,n-1}. |
| ------------------- | --- | ---- | -------------- | -------- | ----------- |
1 n-1
Then \rho(e ,v) = 0 by the construction of \mathcal{U}. Because \rho is symmetric, we also
k
have\rho(v,e )=0. Thusthematrixof\rhowithrespecttoe ,…,e ,visadiagonal
|     | k   |     |     | 1 n-1 |     |
| --- | --- | --- | --- | ----- | --- |
matrix,completingtheproofthat(a)implies(d).

| --- | --- | --------- | ------------------------------ | --- | --- | --- |
Thepreviousresultstatesthateverysymmetricbilinearformhasadiagonal
matrixwithrespecttosomebasis. Ifourvectorspacehappenstobearealinner
productspace,thenthenextresultshowsthateverysymmetricbilinearformhas
adiagonalmatrixwithrespecttosomeorthonormalbasis. Notethattheinner
producthereisunrelatedtothebilinearform.
diagonalizationofasymmetricbilinearformbyanorthonormalbasis
9.13
Suppose\mathcal{V} isarealinnerproductspaceand\rhoisasymmetricbilinearformon
\mathcal{V}. Then\rhohasadiagonalmatrixwithrespecttosomeorthonormalbasisof\mathcal{V}.
Proof Let f ,…, f beanorthonormalbasisof\mathcal{V}. Let\mathcal{B}=ℳ(\rho,(f ,…, f )).
|     | 1 n |     |     |     | 1   | n   |
| --- | --- | --- | --- | --- | --- | --- |
Then\mathcal{B}isasymmetricmatrix(by9.12). Let\mathcal{T} \inℒ(\mathcal{V})betheoperatorsuchthat
| ℳ(\mathcal{T},(f | ,…, f ))=\mathcal{B}. | Thus\mathcal{T} isself-adjoint. |     |     |     |     |
| ------ | ----------- | --------------------- | --- | --- | --- | --- |
|        | 1 n         |                       |     |     |     |     |
Therealspectraltheorem(7.29)statesthat\mathcal{T}hasadiagonalmatrixwithrespect
tosomeorthonormalbasise ,…,e of\mathcal{V}. Let\mathcal{C} =ℳ(\mathcal{I},(e ,…,e ),(f ,…, f )).
|     |     | 1   | n   | 1   | n 1 | n   |
| --- | --- | --- | --- | --- | --- | --- |
Thus\mathcal{C}-1\mathcal{B}\mathcal{C}isthematrixof\mathcal{T}withrespecttothebasise ,…,e (by3.84). Hence
1 n
| \mathcal{C}-1\mathcal{B}\mathcal{C}isadiagonalmatrix. |     | Now         |         |         |     |     |
| ----------------------- | --- | ----------- | ------- | ------- | --- | --- |
|                         |     | \mathcal{M}(\rho,(e ,…,e | ))=\mathcal{C}t\mathcal{B}\mathcal{C} | =\mathcal{C}-1\mathcal{B}\mathcal{C}, |     |     |
|                         |     | 1           | n       |         |     |     |
wherethefirstequalityholdsby9.7andthesecondequalityholdsbecause\mathcal{C}isa
unitarymatrixwithrealentries(whichimpliesthat\mathcal{C}-1 =\mathcal{C}t;see7.57).
Nowweturnourattentiontoalternatingbilinearforms. Alternatingmultilinear
formswillplayamajorroleinourapproachtodeterminantslaterinthischapter.
| 9.14 definition: | alternatingbilinearform,\mathcal{V}(2) |     |     |     |     |     |
| ---------------- | ---------------------------- | --- | --- | --- | --- | --- |
alt
| Abilinearform\alpha\in\mathcal{V}(2) |     | iscalledalternatingif |     |     |     |     |
| ------------------- | --- | --------------------- | --- | --- | --- | --- |
\alpha(v,v)=0
forallv\in\mathcal{V}. Thesetofalternatingbilinearformson\mathcal{V} isdenotedby\mathcal{V}(2).
alt
| 9.15 example:     | alternatingbilinearforms |           |                |           |        |     |
| ----------------- | ------------------------ | --------- | -------------- | --------- | ------ | --- |
| • Supposen\geq3and\alpha∶ |                          | \mathbf{F}n\times\mathbf{F}n     | \rightarrow\mathbf{F} isdefinedby |           |        |     |
|                   | \alpha((x ,…,x                | ),(y ,…,y | ))=x y         | -x y +x y | -x y . |     |
|                   | 1                        | n 1       | n 1 2          | 2 1 1 3   | 3 1    |     |
Then\alphaisanalternatingbilinearformon\mathbf{F}n.
| • Suppose\phi,\tau | \in\mathcal{V}′. | Thenthebilinearform\alphaon\mathcal{V} |     | definedby |     |     |
| ------------ | ---- | ----------------------- | --- | --------- | --- | --- |
\alpha(u,w)=\phi(u)\tau(w)-\phi(w)\tau(u)
isalternating.

| -------- | --------------------------------- | --- | --- | --- |
Thenextresultshowsthatabilinearformisalternatingifandonlyifswitching
theorderofthetwoinputsmultipliestheoutputby-1.
9.16 characterizationofalternatingbilinearforms
Abilinearform\alphaon\mathcal{V} isalternatingifandonlyif
\alpha(u,w)=-\alpha(w,u)
forallu,w\in\mathcal{V}.
| Firstsupposethat\alphaisalternating. |     | Ifu,w\in\mathcal{V},then |     |     |
| ------------------------------- | --- | ------------ | --- | --- |
Proof
$$0=\alpha(u+w,u+w)$$
=\alpha(u,u)+\alpha(u,w)+\alpha(w,u)+\alpha(w,w)
=\alpha(u,w)+\alpha(w,u).
Thus\alpha(u,w)=-\alpha(w,u),asdesired.
Toprovetheimplicationintheotherdirection,suppose\alpha(u,w)=-\alpha(w,u)
for all u,w \in \mathcal{V}. Then \alpha(v,v) = -\alpha(v,v) for all v \in \mathcal{V}, which implies that
\alpha(v,v)=0forallv\in\mathcal{V}. Thus\alphaisalternating.
Nowweshowthatthevectorspaceofbilinearformson\mathcal{V} isthedirectsumof
thesymmetricbilinearformson\mathcal{V} andthealternatingbilinearformson\mathcal{V}.
| 9.17 \mathcal{V}(2) | =\mathcal{V} ( 2 ) \oplus\mathcal{V} ( 2 ) |     |     |     |
| --------- | ----------------- | --- | --- | --- |
s y m a l t
| Thesets\mathcal{V}(2) | and\mathcal{V}(2) aresubspacesof\mathcal{V}(2). |     | Furthermore, |     |
| ----------- | --------------------------- | --- | ------------ | --- |
sym alt
\mathcal{V}(2) =\mathcal{V}(2) \oplus\mathcal{V}(2).
sym
alt
twosymmetricbilinearformson\mathcal{V} isasymmetricbilinearformon\mathcal{V},andevery
scalarmultipleofanysymmetricbilinearformon\mathcal{V} isasymmetricbilinearform
on\mathcal{V}. Also, thezerobilinearformisin\mathcal{V}(2). Thus\mathcal{V}(2) isasubspaceof\mathcal{V}(2).
|     |     | sym | sym |     |
| --- | --- | --- | --- | --- |
Similarly,theverificationthat\mathcal{V}(2)
|     |     | isasubspaceof\mathcal{V}(2) | isstraightforward. |     |
| --- | --- | ----------------- | ------------------ | --- |
alt
Next,wewanttoshowthat\mathcal{V}(2) =\mathcal{V}(2) +\mathcal{V}(2). Todothis,suppose\beta\in\mathcal{V}(2).
sym
alt
| Define\rho,\alpha\in\mathcal{V}(2) | by            |     |               |     |
| -------------- | ------------- | --- | ------------- | --- |
|                | \beta(u,w)+\beta(w,u) |     | \beta(u,w)-\beta(w,u) |     |
| \rho(u,w)=        |               | and | \alpha(u,w)=       | .   |
2 2
| Then\rho\in\mathcal{V}(2) | and\alpha\in\mathcal{V}(2),and\beta=\rho+\alpha. |     | Thus\mathcal{V}(2) =\mathcal{V}(2) | +\mathcal{V}(2). |
| ---------- | ------------------- | --- | -------------- | ------ |
|            | sym                 |     |                | sym    |
alt alt
Finally,toshowthattheintersectionofthetwosubspacesunderconsideration
| equals{0},suppose\beta\in\mathcal{V}(2) | \cap\mathcal{V}(2). | Ifu,w\in\mathcal{V},then9.16impliesthat |     |     |
| ----------------------- | ------ | --------------------------- | --- | --- |
sym
alt
\beta(u,w)=-\beta(w,u)=-\beta(u,w)
|                   |          | Hence\mathcal{V}(2) | =\mathcal{V}(2) \oplus\mathcal{V}(2) |           |
| ----------------- | -------- | --------- | ----------- | --------- |
| andhence\beta(u,w)=0. | Thus\beta=0. |           | sym         | (by1.46). |
alt

Section9A Bilinear Formsand Quadratic Forms 341
**9.18 定义：** quadraticformassociatedwithabilinearform,q
\beta
For\betaabilinearformon\mathcal{V},defineafunctionq ∶ \mathcal{V} \rightarrow\mathbf{F} byq (v)=\beta(v,v).
\beta \beta
Afunctionq∶ \mathcal{V} \rightarrow\mathbf{F} iscalledaquadraticformon\mathcal{V} ifthereexistsabilinear
form\betaon\mathcal{V} suchthatq=q .
\beta
Notethatif\betaisabilinearform,thenq =0ifandonlyif\betaisalternating.
\beta
**9.19 例：** quadraticform
Suppose\betaisthebilinearformon\mathbf{R}3 definedby
\beta((x ,x ,x ),(y ,y ,y ))=x y -4x y +8x y -3x y .
1 2 3 1 2 3 1 1 1 2 1 3 3 3
Thenq isthequadraticformon\mathbf{R}3 givenbytheformula
\beta
q (x ,x ,x )=x2-4x x +8x x -3x2.
\beta 1 2 3 1 1 2 1 3 3
Thequadraticformintheexampleaboveistypicalofquadraticformson\mathbf{F}n,
asshowninthenextresult.
9.20 quadraticformson\mathbf{F}n
Suppose n is a positive integer and q is a function from \mathbf{F}n to \mathbf{F}. Then q
is a quadratic form on \mathbf{F}n if and only if there exist numbers \mathcal{A} \in \mathbf{F} for
j,k
j,k \in{1,…,n}suchthat
n n
q(x ,…,x )= \sum \sum \mathcal{A} xx
1 n j,k j k
$$k=1j=1$$
forall(x ,…,x )\in\mathbf{F}n.
1 n
Proof Firstsupposeqisaquadraticformon\mathbf{F}n. Thusthereexistsabilinearform
\betaon\mathbf{F}n suchthatq = q . Let\mathcal{A}bethematrixof\betawithrespecttothestandard
\beta
basisof\mathbf{F}n. Thenforall(x ,…,x )\in\mathbf{F}n,wehavethedesiredequation
1 n
n n
q(x ,…,x )=\beta((x ,…,x ),(x ,…,x ))= \sum \sum \mathcal{A} xx .
1 n 1 n 1 n j,k j k
$$k=1j=1$$
Conversely,supposethereexistnumbers\mathcal{A} \in\mathbf{F}forj,k \in{1,…,n}suchthat
j,k
n n
q(x ,…,x )= \sum \sum \mathcal{A} xx
1 n j,k j k
$$k=1j=1$$
forall(x ,…,x )\in\mathbf{F}n. Defineabilinearform\betaon\mathbf{F}n by
1 n
n n
\beta((x ,…,x ),(y ,…,y ))= \sum \sum \mathcal{A} xy .
1 n 1 n j,k j k
$$k=1j=1$$
Thenq=q ,asdesired.
\beta

| --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Althoughquadraticformsaredefinedintermsofanarbitrarybilinearform,
theequivalenceof(a)and(b)intheresultbelowshowsthatasymmetricbilinear
formcanalwaysbeused.
characterizationsofquadraticforms
9.21
Supposeq∶
|     | \mathcal{V} \rightarrow\mathbf{F} isafunction. |     | Thefollowingareequivalent. |     |     |     |     |     |
| --- | ----------------- | --- | -------------------------- | --- | --- | --- | --- | --- |
$$(a) qisaquadraticform.$$
$$(b) Thereexistsauniquesymmetricbilinearform\rhoon\mathcal{V} suchthatq=q .$$
\rho
| (c) q(\lambdav)= | \lambda2q(v)forall | \lambda\in\mathbf{F} | andallv\in\mathcal{V},andthefunction |     |     |     |     |     |
| ---------- | ------------ | --- | ------------------------ | --- | --- | --- | --- | --- |
$$(u,w)↦q(u+w)-q(u)-q(w)$$
isasymmetricbilinearformon\mathcal{V}.
$$(d) q(2v)=4q(v)forallv\in\mathcal{V},andthefunction$$
$$(u,w)↦q(u+w)-q(u)-q(w)$$
isasymmetricbilinearformon\mathcal{V}.
Proof First suppose (a) holds, so q is a quadratic form. Hence there exists a
bilinearform\betasuchthatq=q . By9.17,thereexistasymmetricbilinearform\rho
\beta
| on\mathcal{V} andanalternatingbilinearform\alphaon\mathcal{V} |                    |     |           |      | suchthat\beta=\rho+\alpha. |     | Now   |        |
| ------------------------------------ | ------------------ | --- | --------- | ---- | -------------- | --- | ----- | ------ |
|                                      |                    | q=q | =q        | +q   | =q .           |     |       |        |
|                                      |                    |     | \beta         | \rho    | \alpha \rho            |     |       |        |
| \rho′                                   | \mathcal{V}(2)               |     |           |      |                | \rho′  | \mathcal{V}(2)  | \cap\mathcal{V}(2), |
| If \in                                 | sym also satisfies | q   | = q, then | q    | = 0; thus      | -\rho  | \in sym |        |
|                                      |                    | \rho′  |           | \rho′-\rho |                |     |       | alt    |
whichimpliesthat\rho′ =\rho(by9.17). Thiscompletestheproofthat(a)implies(b).
Nowsuppose(b)holds,sothereexistsasymmetricbilinearform\rhoon\mathcal{V} such
| thatq=q | . If \lambda\in\mathbf{F} andv\in\mathcal{V} |     | then |     |     |     |     |     |
| ------- | --------------- | --- | ---- | --- | --- | --- | --- | --- |
\rho
|     | q(\lambdav)=\rho(\lambdav,\lambdav)= |     | \lambda\rho(v,\lambdav)= |     | \lambda2\rho(v,v)= | \lambda2q(v), |     |     |
| --- | --------------- | --- | --------- | --- | --------- | ------- | --- | --- |
showingthatthefirstpartof(c)holds.
Ifu,w\in\mathcal{V},then
q(u+w)-q(u)-q(w)=\rho(u+w,u+w)-\rho(u,u)-\rho(w,w)=2\rho(u,w).
Thusthefunction(u,w)↦q(u+w)-q(u)-q(w)equals2\rho,whichisasymmetric
bilinearformon\mathcal{V},completingtheproofthat(b)implies(c).
Clearly(c)implies(d).
Nowsuppose(d)holds. Let\rhobethesymmetricbilinearformon\mathcal{V} definedby
q(u+w)-q(u)-q(w)
|     | \rho(u,w)= |     |     |     |     | .   |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Ifv\in\mathcal{V},then
|     | q(2v)-q(v)-q(v) |     |     |     | 4q(v)-2q(v) |     |     |     |
| --- | --------------- | --- | --- | --- | ----------- | --- | --- | --- |
\rho(v,v)=
|         |                                       |     |     |     | =   | =q(v). |     |     |
| ------- | ------------------------------------- | --- | --- | --- | --- | ------ | --- | --- |
| Thusq=q | ,completingtheproofthat(d)implies(a). |     |     |     |     |        |     |     |
\rho

Section9A Bilinear Formsand Quadratic Forms 343
**9.22 例：** symmetricbilinearformassociatedwithaquadraticform
Supposeqisthequadraticformon\mathbf{R}3 givenbytheformula
q(x ,x ,x )=x2-4x x +8x x -3x2.
1 2 3 1 1 2 1 3 3
A bilinear form \beta on \mathbf{R}3 such that q = q is given by Example 9.19, but this
\beta
bilinearformisnotsymmetric,aspromisedby9.21(b). However,thebilinear
form\rhoon\mathbf{R}3 definedby
\rho((x ,x ,x ),(y ,y ,y ))=x y -2x y -2x y +4x y +4x y -3x y
1 2 3 1 2 3 1 1 1 2 2 1 1 3 3 1 3 3
issymmetricandsatisfiesq=q .
\rho
Thenextresultstatesthatforeachquadraticformwecanchooseabasissuch
thatthequadraticformlookslikeaweightedsumofsquaresofthecoordinates,
meaningthattherearenocrosstermsoftheformxx withj \neqk.
j k
9.23 diagonalizationofquadraticform
Supposeqisaquadraticformon\mathcal{V}.
$$(a) Thereexistabasise ,…,e of\mathcal{V} and \lambda ,…,\lambda \in\mathbf{F} suchthat$$
1 n 1 n
q(x e +⋯+x e )= \lambda x2+⋯+ \lambda x2
1 1 n n 1 1 n n
forallx ,…,x \in\mathbf{F}.
1 n
$$(b) If\mathbf{F} = \mathbf{R} and\mathcal{V} isaninnerproductspace, thenthebasisin(a)canbe$$
chosentobeanorthonormalbasisof\mathcal{V}.
Proof
$$(a) Thereexistsasymmetricbilinearform\rhoon\mathcal{V}suchthatq=q (by9.21). Now$$
\rho
thereexistsabasise ,…,e of\mathcal{V} suchthatℳ(\rho,(e ,…,e ))isadiagonal
1 n 1 n
matrix (by 9.12). Let \lambda ,…,\lambda denote the entries on the diagonal of this
1 n
matrix. Thus
⎧ {\lambda ifj =k,
\rho(e,e )= j
j k ⎨ {0 ifj \neqk
⎩
forallj,k \in{1,…,n}. Ifx ,…,x \in\mathbf{F},then
1 n
q(x e +⋯+x e )=\rho(x e +⋯+x e ,x e +⋯+x e )
1 1 n n 1 1 n n 1 1 n n
n n
= \sum \sum xx \rho(e,e )
j k j k
$$k=1j=1$$
= \lambda x2+⋯+ \lambda x2,
1 1 n n
asdesired.
$$(b) Suppose\mathbf{F} =\mathbf{R} and\mathcal{V} isaninnerproductspace. Then9.13tellsusthatthe$$
basisin(a)canbechosentobeanorthonormalbasisof\mathcal{V}.

| -------- | --------------------------------- | --- | --- |
| Exercises 9A |     |     |     |
| ------------ | --- | --- | --- |
1 Provethatif\betaisabilinearformon\mathbf{F},thenthereexistsc \in\mathbf{F} suchthat
\beta(x,y)=cxy
| forallx,y | \in\mathbf{F}. |     |     |
| --------- | --- | --- | --- |
2 Letn = dim\mathcal{V}. Suppose\betaisabilinearformon\mathcal{V}. Provethatthereexist
| \phi ,…,\phi | ,\tau ,…,\tau \in\mathcal{V}′ | suchthat      |           |
| ------ | ----------- | ------------- | --------- |
| 1      | n 1 n       |               |           |
|        | \beta(u,v)=\phi    | (u)\cdot\tau (v)+⋯+\phi | (u)\cdot\tau (v) |
|        |             | 1 1           | n n       |
forallu,v\in\mathcal{V}.
| Thisexerciseshowsthatif |     | n=dim\mathcal{V},theneverybilinearformon\mathcal{V}isof |     |
| ----------------------- | --- | ----------------------------------- | --- |
theformgivenbythelastbulletpointof Example9.2.
Suppose\beta∶
| 3      | \mathcal{V}\times\mathcal{V} \rightarrow\mathbf{F}isabilinearformon\mathcal{V}andalsoisalinearfunctional |     |     |
| ------ | -------------------------------------------------- | --- | --- |
| on\mathcal{V}\times\mathcal{V}. | Provethat\beta=0.                                      |     |     |
4 Suppose\mathcal{V} isarealinnerproductspaceand\betaisabilinearformon\mathcal{V}. Show
| thatthereexistsauniqueoperator\mathcal{T} |     |     | \inℒ(\mathcal{V})suchthat |
| ------------------------------- | --- | --- | ------------- |
\beta(u,v)=\langleu,\mathcal{T}v\rangle
forallu,v\in\mathcal{V}.
This exercise states that if \mathcal{V} is a real inner product space, then every
bilinearformon\mathcal{V}isoftheformgivenbythethirdbulletpointin9.2.
5 Suppose\betaisabilinearformonarealinnerproductspace\mathcal{V}and\mathcal{T} isthe
unique operator on \mathcal{V} such that \beta(u,v) = \langleu,\mathcal{T}v\rangle for all u,v \in \mathcal{V} (see
Exercise 4). Show that \beta is an inner product on \mathcal{V} if and only if \mathcal{T} is an
invertiblepositiveoperatoron\mathcal{V}.
Proveorgiveacounterexample: If\rhoisasymmetricbilinearformon\mathcal{V},then
{v\in\mathcal{V} ∶\rho(v,v)=0}
isasubspaceof\mathcal{V}.
7 Explainwhytheproofof9.13(diagonalizationofasymmetricbilinearform
byanorthonormalbasisonarealinnerproductspace)failsifthehypothesis
| that\mathbf{F} =\mathbf{R}                 | isdropped. |            |                |
| ------------------------ | ---------- | ---------- | -------------- |
| 8 Findformulasfordim\mathcal{V}(2) |            | anddim\mathcal{V}(2) | intermsofdim\mathcal{V}. |
|                          |            | sym        | alt            |
∶
9 Supposethatnisapositiveintegerand\mathcal{V} = {p \in 𝒫 (\mathbf{R}) p(0) = p(1)}.
n
| Define\alpha∶ |     | by  |     |
| -------- | --- | --- | --- |
\mathcal{V}\times\mathcal{V} \rightarrow\mathbf{R}
|     |     | \alpha(p,q)=\int | pq′. |
| --- | --- | -------- | ---- |
Showthat\alphaisanalternatingbilinearformon\mathcal{V}.

Section9A Bilinear Formsand Quadratic Forms 345
10 Supposethatnisapositiveintegerand
\mathcal{V} ={p\in𝒫 (\mathbf{R})∶p(0)=p(1)andp′(0)=p′(1)}.
n
Define\rho∶ \mathcal{V}\times\mathcal{V} \rightarrow\mathbf{R} by
\rho(p,q)=\int pq″.
Showthat\rhoisasymmetricbilinearformon\mathcal{V}.

| -------- | --- | --------------------------------- | --- | --- | --- | --- |
| 9B Alternating |       | Multilinear | Forms |     |     |     |
| -------------- | ----- | ----------- | ----- | --- | --- | --- |
| Multilinear    | Forms |             |       |     |     |     |
\mathcal{V}m
**9.24 定义：** | Formapositiveinteger,define\mathcal{V}m |     |     | by       |     |     |     |
| ----------------------------- | --- | --- | -------- | --- | --- | --- |
|                               |     | \mathcal{V}m  | =\mathcal{V}⏟\times⋯\times\mathcal{V}. |     |     |     |
mtimes
Nowwecandefinem-linearformsasageneralizationofthebilinearforms
thatwediscussedintheprevioussection.
m-linearform,\mathcal{V}(m),multilinearform
**9.25 定义：** isafunction\beta∶
| • Formapositiveinteger,anm-linearformon\mathcal{V} |     |     |     |     |     | \mathcal{V}m\rightarrow\mathbf{F} |
| ---------------------------------------- | --- | --- | --- | --- | --- | ---- |
thatislinearineachslotwhentheotherslotsareheldfixed. Thismeans
| thatforeachk               |     | \in{1,…,m}andallu |                  | ,…,u | \in\mathcal{V},thefunction |     |
| -------------------------- | --- | --------------- | ---------------- | ---- | -------------- | --- |
|                            |     |                 |                  | 1 m  |                |     |
|                            |     | v↦\beta(u           | ,…,u             | ,v,u | ,…,u )         |     |
|                            |     | 1               | k-1              | k+1  | m              |     |
| isalinearmapfrom\mathcal{V}          |     | to\mathbf{F}.            |                  |      |                |     |
| • Thesetofm-linearformson\mathcal{V} |     |                 | isdenotedby\mathcal{V}(m). |      |                |     |
• Afunction\betaiscalledamultilinearformon\mathcal{V} ifitisanm-linearformon
\mathcal{V} forsomepositiveintegerm.
| Inthedefinitionabove,theexpression\beta(u |      |               |     | ,…,u | ,v,u       | ,…,u )means |
| ------------------------------------- | ---- | ------------- | --- | ---- | ---------- | ----------- |
|                                       |      |               |     | 1    | k-1        | k+1 m       |
| \beta(v,u ,…,u                            | )ifk | =1andmeans\beta(u |     | ,…,u | ,v)ifk =m. |             |
| 2                                     | m    |               | 1   | m-1  |            |             |
A 1-linear form on \mathcal{V} is a linear functional on \mathcal{V}. A 2-linear form on \mathcal{V} is
a bilinear form on \mathcal{V}. You can verify that with the usual addition and scalar
| multiplicationoffunctions,\mathcal{V}(m) |               |     | isavectorspace. |     |     |     |
| ------------------------------ | ------------- | --- | --------------- | --- | --- | --- |
| 9.26 example:                  | m-linearforms |     |                 |     |     |     |
Defineafunction\beta∶
| • Suppose\alpha,\rho\in\mathcal{V}(2). |     |           |          | \mathcal{V}4 \rightarrow\mathbf{F}   | by    |     |
| ------------------ | --- | --------- | -------- | ------- | ----- | --- |
|                    |     | \beta(v ,v ,v | ,v )=\alpha(v | ,v )\rho(v | ,v ). |     |
|                    |     | 1 2       | 3 4      | 1 2     | 3 4   |     |
Then\beta\in\mathcal{V}(4).
| Define\beta∶ | (ℒ(\mathcal{V}))m |          |        |     |     |     |
| -------- | ------- | -------- | ------ | --- | --- | --- |
| •        |         | \rightarrow\mathbf{F} by    |        |     |     |     |
|          |         | \beta(\mathcal{T} ,…,\mathcal{T} | )=tr(\mathcal{T} | ⋯\mathcal{T}  | ).  |     |
|          |         | 1        | m      | 1   | m   |     |
Then\betaisanm-linearformonℒ(\mathcal{V}).

| --- | --- | --- | --------- | --- | --------------------------- | --- | --- | --- |
Alternatingmultilinearforms,whichwenowdefine,playanimportantroleas
weheadtowarddefiningdeterminants.
alternatingforms,\mathcal{V}(m)
|     | 9.27 definition: |     |     |     | alt |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Supposemisapositiveinteger.
• Anm-linearform\alphaon\mathcal{V}iscalledalternatingif\alpha(v ,…,v )=0whenever
|     |        |                     |     |     |       |                             | 1 m |     |
| --- | ------ | ------------------- | --- | --- | ----- | --------------------------- | --- | --- |
|     | v ,…,v | isalistofvectorsin\mathcal{V} |     |     | withv | =v forsometwodistinctvalues |     |     |
|     | 1      | m                   |     |     |       | j k                         |     |     |
ofjandkin{1,…,m}.
|     | \mathcal{V}(m) |          | ∶\alphaisanalternatingm-linearformon\mathcal{V}}. |     |     |     |     |     |
| --- | ---- | -------- | ---------------------------------- | --- | --- | --- | --- | --- |
|     | •    | ={\alpha\in\mathcal{V}(m) |                                    |     |     |     |     |     |
alt
You should verify that \mathcal{V}(m) is a subspace of \mathcal{V}(m). See Example 9.15 for
alt
examples of alternating 2-linear forms. See Exercise 2 for an example of an
alternating3-linearform.
Thenextresulttellsusthatifalinearlydependentlistisinputtoanalternating
multilinearform,thentheoutputequals0.
9.28 alternatingmultilinearformsandlineardependence
Supposemisapositiveintegerand\alphaisanalternatingm-linearformon\mathcal{V}. If
|     | v ,…,v | isalinearlydependentlistin\mathcal{V},then |     |     |           |     |     |     |
| --- | ------ | -------------------------------- | --- | --- | --------- | --- | --- | --- |
|     | 1      | m                                |     |     |           |     |     |     |
|     |        |                                  |     | \alpha(v | ,…,v )=0. |     |     |     |
|     |        |                                  |     | 1   | m         |     |     |     |
Proof Supposev ,…,v isalinearlydependentlistin\mathcal{V}. Bythelineardepen-
|     |     | 1   | m   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
dencelemma(2.19),somev isalinearcombinationofv ,…,v . Thusthere
|        |      |           | k   |      |      |         | 1 k-1 |     |
| ------ | ---- | --------- | --- | ---- | ---- | ------- | ----- | --- |
| existb | ,…,b | suchthatv |     | =b v | +⋯+b | v       | . Now |     |
|        | 1    | k-1       | k   | 1 1  |      | k-1 k-1 |       |     |
k-1
|     |     | \alpha(v ,…,v | )=\alpha(v | ,…,v |     | ,\sumbv,v | ,…,v ) |     |
| --- | --- | -------- | ----- | ---- | --- | ------ | ------ | --- |
|     |     | 1        | m     | 1    | k-1 | j j    | k+1 m  |     |
$$j=1$$
k-1
|     |     |     | =   | \sumb  | \alpha(v ,…,v | ,v,v  | ,…,v ) |     |
| --- | --- | --- | --- | --- | -------- | ----- | ------ | --- |
|     |     |     |     | j   | 1        | k-1 j | k+1 m  |     |
$$j=1$$
=0.
Thenextresultstatesthatifm>dim\mathcal{V},thentherearenoalternatingm-linear
otherthanthefunctionon\mathcal{V}m
| formson\mathcal{V} |                                      |     |     |     | thatisidentically0. |        |     |     |
| -------- | ------------------------------------ | --- | --- | --- | ------------------- | ------ | --- | --- |
|          | nononzeroalternatingm-linearformsfor |     |     |     |                     | m>dim\mathcal{V} |     |     |
9.29
|     | Supposem>dim\mathcal{V}. |     | Then0istheonlyalternatingm-linearformon\mathcal{V}. |     |     |     |     |     |
| --- | -------------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
Proof Supposethat\alphaisanalternatingm-linearformon\mathcal{V} andv ,…,v \in\mathcal{V}.
|     |     |     |     |     |     |     |     | 1 m |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Because m > dim\mathcal{V}, this list is not linearly independent (by 2.22). Thus 9.28
Hence\alphaisthezerofunctionfrom\mathcal{V}m
| impliesthat\alpha(v |     | ,…,v | )=0. |     |     |     |     | to\mathbf{F}. |
| -------------- | --- | ---- | ---- | --- | --- | --- | --- | ---- |
|                |     | 1    | m    |     |     |     |     |      |

| -------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
| Alternating | Multilinear |     | Forms | and | Permutations |     |     |     |
| ----------- | ----------- | --- | ----- | --- | ------------ | --- | --- | --- |
swappinginputvectorsinanalternatingmultilinearform
9.30
Supposemisapositiveinteger,\alphaisanalternatingm-linearformon\mathcal{V},and
v ,…,v isalistofvectorsin\mathcal{V}. Thenswappingthevectorsinanytwoslots
| 1 m        |     |                                   |     |     |     |     |     |     |
| ---------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
| of\alpha(v ,…,v |     | )changesthevalueof\alphabyafactorof-1. |     |     |     |     |     |     |
| 1          | m   |                                   |     |     |     |     |     |     |
+v
| Proof Putv |     | inboththefirsttwoslots,getting |     |     |     |     |     |     |
| ---------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
1 2
|     |     | 0=\alpha(v |     | +v ,v | +v  | ,v ,…,v | ).  |     |
| --- | --- | ----- | --- | ----- | --- | ------- | --- | --- |
|     |     |       | 1   | 2     | 1 2 | 3       | m   |     |
Usethemultilinearpropertiesof\alphatoexpandtherightsideoftheequationabove
$$(asintheproofof9.16)toget$$
|     |     | ,v  | ,v ,…,v |        |     | ,v ,v | ,…,v |     |
| --- | --- | --- | ------- | ------ | --- | ----- | ---- | --- |
|     |     | \alpha(v |         | )=-\alpha(v |     |       | ).   |     |
|     |     | 2   | 1 3     | m      |     | 1 2   | 3 m  |     |
Similarly,swappingthevectorsinanytwoslotsof\alpha(v ,…,v )changesthe
|     |     |     |     |     |     |     | 1   | m   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
valueof\alphabyafactorof-1.
To see what can happen with multiple swaps, suppose \alpha is an alternating
|               |     |       | ,v  | ,v  |       |          | ,v ,v |               |
| ------------- | --- | ----- | --- | --- | ----- | -------- | ----- | ------------- |
| 3-linear form | on  | \mathcal{V} and | v   | \in   | \mathcal{V}. To | evaluate | \alpha(v   | ) in terms of |
|               |     |       | 1 2 | 3   |       |          | 3 1   | 2             |
\alpha(v ,v ,v ), start with \alpha(v ,v ,v ) and swap the entries in the first and third
| 1 2              | 3   |       | 3      | 1 2 |                                   |     |     |     |
| ---------------- | --- | ----- | ------ | --- | --------------------------------- | --- | --- | --- |
|                  |     | ,v ,v |        | ,v  | ,v                                |     |     |     |
| slots,getting\alpha(v |     |       | )=-\alpha(v |     | ). Nowinthelastexpression,swapthe |     |     |     |
|                  |     | 3 1 2 |        | 2 1 | 3                                 |     |     |     |
entriesinthefirstandsecondslots,getting
|     |     | \alpha(v ,v | ,v )=-\alpha(v |     | ,v ,v | )=\alpha(v | ,v ,v ). |     |
| --- | --- | ------ | --------- | --- | ----- | ----- | -------- | --- |
|     |     | 3      | 1 2       |     | 2 1   | 3     | 1 2 3    |     |
Moregenerally,weseethatifwedoanoddnumberofswaps,thenthevalueof\alpha
changesbyafactorof-1,andifwedoanevennumberofswaps,thenthevalue
of\alphadoesnotchange.
To deal with arbitrary multiple swaps, we need a bit of information about
permutations.
| 9.31 definition: |     | permutation,permm |     |     |     |     |     |     |
| ---------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Supposemisapositiveinteger.
• A permutation of (1,…,m) is a list (j ,…,j ) that contains each of the
|     |     |     |     |     | 1   | m   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
numbers1,…,mexactlyonce.
• Thesetofallpermutationsof(1,…,m)isdenotedbypermm.
For example, (2,3,4,5,1) \in perm5. You should think of an element of
permmasarearrangementofthefirstmpositiveintegers.
The number of swaps used to change a permutation (j ,…,j ) to the stan-
|     |     |     |     |     |     |     | 1   | m   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
dardorder(1,…,m)candependonthespecificswapsselected. Thefollowing
definitionhastheadvantageofassigningawell-definedsigntoeverypermutation.

Section9B Alternating Multilinear Forms 349
**9.32 定义：** signofapermutation
Thesignofapermutation(j ,…,j )isdefinedby
1 m
sign(j ,…,j )=(-1)\mathcal{N},
1 m
where\mathcal{N} isthenumberofpairsofintegers(k,ℓ)with1 \leq k < ℓ \leq msuch
thatkappearsafterℓinthelist(j ,…,j ).
1 m
Hencethesignofapermutationequals1ifthenaturalorderhasbeenchanged
anevennumberoftimesandequals-1ifthenaturalorderhasbeenchangedan
oddnumberoftimes.
**9.33 例：** signs
• Thepermutation(1,…,m)[nochangesinthenaturalorder]hassign1.
• Theonlypairofintegers(k,ℓ)withk <ℓsuchthatkappearsafterℓinthelist
$$(2,1,3,4)is(1,2). Thusthepermutation(2,1,3,4)hassign-1.$$
• Inthepermutation(2,3,…,m,1),theonlypairs(k,ℓ)withk <ℓthatappear
withchangedorderare(1,2),(1,3),…,(1,m). Becausewehavem-1such
pairs,thesignofthispermutationequals(-1)m-1.
9.34 swappingtwoentriesinapermutation
Swappingtwoentriesinapermutationmultipliesthesignofthepermutation
by-1.
Proof Suppose we have two permutations, where the second permutation is
obtainedfromthefirstbyswappingtwoentries. Thetwoswappedentrieswere
intheirnaturalorderinthefirstpermutationifandonlyiftheyarenotintheir
naturalorderinthesecondpermutation. Thuswehaveanetchange(sofar)of1
or-1(bothoddnumbers)inthenumberofpairsnotintheirnaturalorder.
Considereachentrybetweenthetwoswappedentries. Ifanintermediateentry
wasoriginallyinthenaturalorderwithrespecttobothswappedentries,thenit
isnowinthenaturalorderwithrespecttoneitherswappedentry. Similarly,if
anintermediateentrywasoriginallyinthenaturalorderwithrespecttoneither
oftheswappedentries,thenitisnowinthenaturalorderwithrespecttoboth
swappedentries. Ifanintermediateentrywasoriginallyinthenaturalorderwith
respecttoexactlyoneoftheswappedentries,thenthatisstilltrue. Thusthenet
change(foreachpaircontaininganentrybetweenthetwoswappedentries)inthe
numberofpairsnotintheirnaturalorderis2,-2,or0(allevennumbers).
Forallotherpairsofentries,thereisnochangeinwhetherornottheyarein
theirnaturalorder. Thusthetotalnetchangeinthenumberofpairsnotintheir
naturalorderisanoddnumber. Hencethesignofthesecondpermutationequals
-1timesthesignofthefirstpermutation.

350 Chapter 9 Multilinear Algebraand Determinants
9.35 permutationsandalternatingmultilinearforms
Supposemisapositiveintegerand\alpha\in\mathcal{V}(m). Then
alt
\alpha(v ,…,v )=(sign(j ,…,j ))\alpha(v ,…,v )
j j 1 m 1 m
1 m
foreverylistv ,…,v ofvectorsin\mathcal{V} andall(j ,…,j )\inpermm.
1 m 1 m
Proof Suppose v ,…,v \in \mathcal{V} and (j ,…,j ) \in permm. We can get from
1 m 1 m
$$(j ,…,j ) to (1,…,m) by a series of swaps of entries in different slots. Each$$
1 m
suchswapchangesthevalueof\alphabyafactorof-1(by9.30)andalsochangesthe
signoftheremainingpermutationbyafactorof-1(by9.34). Afteranappropriate
numberofswaps,wereachthepermutation1,…,m,whichhassign1. Thusthe
valueof\alphachangedsignsanevennumberoftimesifsign(j ,…,j )=1andan
1 m
oddnumberoftimesifsign(j ,…,j )=-1,whichgivesthedesiredresult.
1 m
Ouruseofpermutationsnowleadsinanaturalwaytothefollowingbeautiful
formulaforalternatingn-linearformsonann-dimensionalvectorspace.
9.36 formulafor(dim\mathcal{V})-linearalternatingformson\mathcal{V}
Letn=dim\mathcal{V}. Supposee ,…,e isabasisof\mathcal{V} andv ,…,v \in\mathcal{V}. Foreach
1 n 1 n
k \in{1,…,n},letb ,…,b \in\mathbf{F} besuchthat
1,k n,k
n
$$v = \sumb e.$$
k j,k j
$$j=1$$
Then
\alpha(v ,…,v )=\alpha(e ,…,e ) \sum (sign(j ,…,j ))b ⋯b
1 n 1 n 1 n j ,1 j ,n
1 n
$$(j ,…,j )\inpermn$$
1 n
foreveryalternatingn-linearform\alphaon\mathcal{V}.
Proof Suppose\alphaisanalternatingn-linearformon\mathcal{V}. Then
n n
\alpha(v ,…,v )=\alpha(\sum b e ,…, \sum b e )
1 n j ,1 j j ,n j
1 1 n n
$$j =1 j =1$$
1 n
n n
= \sum ⋯ \sum b ⋯b \alpha(e ,…,e )
j ,1 j ,n j j
1 n 1 n
$$j =1 j =1$$
1 n
= \sum b ⋯b \alpha(e ,…,e )
j ,1 j ,n j j
1 n 1 n
$$(j ,…,j )\inpermn$$
1 n
=\alpha(e ,…,e ) \sum (sign(j ,…,j ))b ⋯b ,
1 n 1 n j ,1 j ,n
1 n
$$(j ,…,j )\inpermn$$
1 n
wherethethirdlineholdsbecause\alpha(e ,…,e ) = 0ifj ,…,j arenotdistinct
j j 1 n
1 n
integers,andthelastlineholdsby9.35.

| --- | --- | --- | --- | --------- | --------------------------- | --- | --- | --- |
Thefollowingresultwillbethekeytoourdefinitionofthedeterminantinthe
nextsection.
dim\mathcal{V}(dim\mathcal{V})
| 9.37 |     |     | =1  |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
alt
Thevectorspace\mathcal{V}(dim\mathcal{V})
hasdimensionone.
alt
Suppose\alphaand\alpha′arealternatingn-linearformson\mathcal{V}with
Proof Letn=dim\mathcal{V}.
\alpha\neq0. Lete ,…,e besuchthat\alpha(e ,…,e )\neq0. Thereexistsc \in\mathbf{F} suchthat
|     | 1   | n   |      | 1      | n   |      |     |     |
| --- | --- | --- | ---- | ------ | --- | ---- | --- | --- |
|     |     |     | \alpha′(e | ,…,e   |     | ,…,e |     |     |
|     |     |     |      | )=c\alpha(e |     | ).   |     |     |
|     |     |     |      | 1 n    | 1   | n    |     |     |
Furthermore,9.28impliesthate ,…,e islinearlyindependentandthusisabasis
|     |     |     |     | 1   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
of\mathcal{V}.
| Supposev |           | ,…,v   | \in\mathcal{V}.  | Letb beasin9.36forj,k |         |         | =1,…,n.  | Then |
| -------- | --------- | ------ | ---- | --------------------- | ------- | ------- | -------- | ---- |
|          |           | 1      | n    | j,k                   |         |         |          |      |
|          | \alpha′(v ,…,v | )=\alpha′(e | ,…,e | )                     | \sum       | (sign(j | ,…,j ))b | ⋯b   |
|          | 1         | n      | 1    | n                     |         |         | 1 n j ,1 | j ,n |
|          |           |        |      | (j ,…,j               | )\inpermn |         | 1        | n    |
1 n
|     |     | =c\alpha(e | ,…,e | )    | \sum         | (sign(j | ,…,j ))b | ⋯b   |
| --- | --- | ----- | ---- | ---- | --------- | ------- | -------- | ---- |
|     |     |       | 1    | n    |           |         | 1 n j ,1 | j ,n |
|     |     |       |      | ,…,j |           |         | 1        | n    |
|     |     |       |      | (j 1 | n )\inpermn |         |          |      |
|     |     | =c\alpha(v | ,…,v | ),   |           |         |          |      |
|     |     |       | 1    | n    |           |         |          |      |
wherethefirstandlastlinesabovecomefrom9.36. Theequationaboveimplies
that \alpha′ = c\alpha. Thus \alpha′,\alpha is not a linearly independent list, which implies that
dim\mathcal{V}(n)
\leq1.
alt
To complete the proof, we only need to show that there exists a nonzero
$$(thuseliminatingthepossibilitythatdim\mathcal{V}(n)$$
alternatingn-linearform\alphaon\mathcal{V}
alt
equals0). Todothis,lete ,…,e beanybasisof\mathcal{V},andlet\phi ,…,\phi \in \mathcal{V}′ be
|     |     |     | 1   | n   |     |     | 1   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
thelinearfunctionalson\mathcal{V} thatallowustoexpresseachelementof\mathcal{V} asalinear
| combinationofe |     | ,…,e | . Inotherwords, |     |     |     |     |     |
| -------------- | --- | ---- | --------------- | --- | --- | --- | --- | --- |
|                |     | 1    | n               |     |     |     |     |     |
n
|     |     |     |     | v= \sum\phi(v)e |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- |
|     |     |     |     |           | j   | j   |     |     |
$$j=1$$
| foreveryv\in\mathcal{V}(see3.114).                  |     |         |      | Nowforv   | ,…,v | \in\mathcal{V},define          |           |     |
| --------------------------------------- | --- | ------- | ---- | --------- | ---- | ------------------ | --------- | --- |
|                                         |     |         |      |           | 1 n  |                    |           |     |
| 9.38                                    | \alpha(v | ,…,v )= |      | \sum (sign(j | ,…,j | ))\phi                | (v )⋯\phi (v | ).  |
|                                         | 1   | n       |      |           | 1    | n                  | j 1 j     | n   |
|                                         |     |         | ,…,j |           |      |                    | 1 n       |     |
|                                         |     |         | (j 1 | n )\inpermn |      |                    |           |     |
| Theverificationthat\alphaisann-linearformon\mathcal{V} |     |         |      |           |      | isstraightforward. |           |     |
,…,v
| Toseethat\alphaisalternating,supposev |     |     |     |     |     | \in \mathcal{V} | withv = | v . Foreach |
| -------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ----------- |
|                                  |     |     |     |     | 1   | n   | 1       | 2           |
$$(j ,…,j )\inpermn,thepermutation(j ,j ,j ,…,j )hastheoppositesign. Be-$$
| 1   | n   |     |     |     | 2 1 3 | n   |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- |
causev =v ,thecontributionsfromthesetwopermutationstothesumin9.38
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
canceleachother. Hence\alpha(v ,v ,v ,…,v )=0. Similarly,\alpha(v ,…,v )=0if
|                         |     |     |     | 1 1 3          | n   |                     | 1   | n   |
| ----------------------- | --- | --- | --- | -------------- | --- | ------------------- | --- | --- |
| anytwovectorsinthelistv |     |     |     | ,…,v areequal. |     | Thus\alphaisalternating. |     |     |
1 n
Finally,consider9.38witheachv =e . Because\phi(e )equals0ifj \neqkand
|     |     |     |     | k   | k   |     | j k |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
equals1ifj =k,onlythepermutation(1,…,n)makesanonzerocontributionto
therightsideof9.38inthiscase,givingtheequation\alpha(e ,…,e )=1. Thuswe
|     |     |     |     |     |     |     | 1 n |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
haveproducedanonzeroalternatingn-linearform\alphaon\mathcal{V},asdesired.

| --- | -------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
| Earlier |     | we showed | that | the value | of  |     |     |     |     |
| ------- | --- | --------- | ---- | --------- | --- | --- | --- | --- | --- |
Theformula9.38usedinthelastproof
| an alternating |     | multilinear |     | form | applied |     |     |     |     |
| -------------- | --- | ----------- | --- | ---- | ------- | --- | --- | --- | --- |
toconstructanonzeroalternatingntoalinearlydependentlistis0;see9.28. linearformcamefromtheformulain
| The | next result | provides |     | a converse | of  |     |     |     |     |
| --- | ----------- | -------- | --- | ---------- | --- | --- | --- | --- | --- |
9.36,andthatformulaarosenaturally
9.28forn-linearmultilinearformswhen fromthepropertiesofanalternating
| n =       | dim\mathcal{V}. | In the    | following | result, | the | multilinearform. |     |     |     |
| --------- | ----- | --------- | --------- | ------- | --- | ---------------- | --- | --- | --- |
| statement |       | that \alpha is | nonzero   | means   | (as |                  |     |     |     |
usualforafunction)that\alphaisnotthefunctionon\mathcal{V}n thatisidentically0.
9.39 alternating(dim\mathcal{V})-linearformsandlinearindependence
| Letn |     | dim\mathcal{V}. Suppose\alphaisanonzeroalternatingn-linearformon\mathcal{V} |     |     |     |     |     |     | and |
| ---- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
=
| e ,…,e |     | isalistofvectorsin\mathcal{V}. |     |     | Then |     |     |     |     |
| ------ | --- | -------------------- | --- | --- | ---- | --- | --- | --- | --- |
1 n
|              |     |      |                        | \alpha(e | ,…,e | )\neq0 |     |     |     |
| ------------ | --- | ---- | ---------------------- | --- | ---- | --- | --- | --- | --- |
|              |     |      |                        |     | 1    | n   |     |     |     |
| ifandonlyife |     | ,…,e | islinearlyindependent. |     |      |     |     |     |     |
|              |     | 1    | n                      |     |      |     |     |     |     |
Proof Firstsuppose\alpha(e ,…,e )\neq0. Then9.28impliesthate ,…,e islinearly
|     |     |     | 1   | n   |     |     |     | 1   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
independent.
Toprovetheimplicationintheotherdirection,nowsupposee ,…,e islinearly
|     |     |     |     |     |     |     |     | 1   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
independent. Becausen=dim\mathcal{V},thisimpliesthate ,…,e isabasisof\mathcal{V}(see
|     |     |     |     |     |     | 1   | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.38).
Because\alphaisnotthezeron-linearform,thereexistv ,…,v \in \mathcal{V} suchthat
1 n
| \alpha(v       | ,…,v                        | )\neq0. Now9.36impliesthat\alpha(e |     |     |                 | ,…,e )\neq0. |           |     |     |
| --------- | --------------------------- | -------------------------- | --- | --- | --------------- | --------- | --------- | --- | --- |
| 1         |                             | n                          |     |     |                 | 1 n       |           |     |     |
| Exercises |                             | 9B                         |     |     |                 |           |           |     |     |
| 1         | Supposemisapositiveinteger. |                            |     |     | Showthatdim\mathcal{V}(m) |           | =(dim\mathcal{V})m. |     |     |
Supposen\geq3and\alpha∶
| 2   |     |           |       | \mathbf{F}n\times\mathbf{F}n\times\mathbf{F}n |      | \rightarrow\mathbf{F} isdefinedby |        |     |       |
| --- | --- | --------- | ----- | -------- | ---- | -------------- | ------ | --- | ----- |
|     |     | \alpha((x ,…,x | ),(y  | ,…,y     | ),(z | ,…,z ))        |        |     |       |
|     |     | 1         | n     | 1        | n    | 1 n            |        |     |       |
|     |     | =x        | y z   | -x y     | z -x | y z -x y z     | +x y z | +x  | y z . |
|     |     |           | 1 2 3 | 2 1      | 3 3  | 2 1 1 3 2      | 3 1    | 2 2 | 3 1   |
Showthat\alphaisanalternating3-linearformon\mathbf{F}n.
| 3   | Supposemisapositiveintegerand\alphaisanm-linearformon\mathcal{V} |              |     |     |      |                     |     |       | suchthat |
| --- | ------------------------------------------------- | ------------ | --- | --- | ---- | ------------------- | --- | ----- | -------- |
|     | \alpha(v ,…,v                                          | )=0wheneverv |     |     | ,…,v | isalistofvectorsin\mathcal{V} |     | withv | =v j+1   |
|     | 1                                                 | m            |     |     | 1    | m                   |     |       | j        |
for some j \in {1,…,m-1}. Prove that \alpha is an alternating m-linear form
on\mathcal{V}.
If\alpha\in\mathcal{V}(4),then
4 Proveorgiveacounterexample:
alt
|     |     |     |        |       | )\in\mathcal{V}4 | ∶\alpha(v  |         |     |     |
| --- | --- | --- | ------ | ----- | ---- | ----- | ------- | --- | --- |
|     |     |     | {(v ,v | ,v ,v |      | ,v ,v | ,v )=0} |     |     |
|     |     |     | 1      | 2 3   | 4    | 1 2   | 3 4     |     |     |
isasubspaceof\mathcal{V}4.

Section9B Alternating Multilinear Forms 353
5 Supposemisapositiveintegerand\betaisanm-linearformon\mathcal{V}. Definean
m-linearform\alphaon\mathcal{V} by
\alpha(v ,…,v )= \sum (sign(j ,…,j ))\beta(v ,…,v )
1 m 1 m j j
1 m
$$(j ,…,j )\inpermm$$
1 m
forv ,…,v \in\mathcal{V}. Explainwhy\alpha\in\mathcal{V}(m).
1 m alt
6 Supposemisapositiveintegerand\betaisanm-linearformon\mathcal{V}. Definean
m-linearform\alphaon\mathcal{V} by
\alpha(v ,…,v )= \sum \beta(v ,…,v )
1 m j j
1 m
$$(j ,…,j )\inpermm$$
1 m
forv ,…,v \in\mathcal{V}. Explainwhy
1 m
\alpha(v ,…,v )=\alpha(v ,…,v )
k k 1 m
1 m
forallv ,…,v \in\mathcal{V} andall(k ,…,k )\inpermm.
1 m 1 m
7 Giveanexampleofanonzeroalternating2-linearform\alphaon\mathbf{R}3andalinearly
independentlistv ,v in\mathbf{R}3 suchthat\alpha(v ,v )=0.
1 2 1 2
Thisexerciseshowsthat9.39canfailifthehypothesisthatn=dim\mathcal{V} is
deleted.

| --- | -------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
### 9C Determinants
| Defining | the Determinant |     |     |     |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Thenextdefinitionwillleadustoaclean,beautiful,basis-freedefinitionofthe
determinantofanoperator.
| 9.40 | definition: \alpha |     |     |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
\mathcal{T}
\mathcal{V}(m),
Suppose that m is a positive integer and \mathcal{T} \in ℒ(\mathcal{V}). For \alpha \in define
alt
| \alpha \in\mathcal{V}(m) | by  |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- |
\mathcal{T} alt
|     |     | \alpha (v | ,…,v )=\alpha(\mathcal{T}v |     | ,…,\mathcal{T}v | )   |     |     |
| --- | --- | ---- | ----------- | --- | ----- | --- | --- | --- |
|     |     | \mathcal{T}    | 1 m         |     | 1     | m   |     |     |
,…,v
| foreachlistv |     | ofvectorsin\mathcal{V}. |     |     |     |     |     |     |
| ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- |
|              | 1   | m             |     |     |     |     |     |     |
If\alpha\in\mathcal{V}(m)
| Suppose\mathcal{T} | \inℒ(\mathcal{V}). |     | andv | ,…,v |     | isalistofvectorsin\mathcal{V} |     | with |
| -------- | ------ | --- | ---- | ---- | --- | ------------------- | --- | ---- |
|          |        |     | alt  | 1    | m   |                     |     |      |
$$v = v for some j \neq k, then \mathcal{T}v = \mathcal{T}v , which implies that \alpha (v ,…,v ) =$$
| j   | k   |     | j   | k   |     |     | \mathcal{T} 1 | m   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
\alpha(\mathcal{T}v ,…,\mathcal{T}v )=0. Thusthefunction\alpha↦\alpha isalinearmapof\mathcal{V}(m) toitself.
| 1   | m   |     |     |     | \mathcal{T}   |     | alt |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
dim\mathcal{V}(dim\mathcal{V})
| We  | know that |     | = 1 (see | 9.37). | Every | linear | map from | a one- |
| --- | --------- | --- | -------- | ------ | ----- | ------ | -------- | ------ |
alt
dimensionalvectorspacetoitselfismultiplicationbysomeuniquescalar. For
| thelinearmap\alpha↦\alpha |     | ,wenowdefinedet\mathcal{T} |     |     | tobethatscalar. |     |     |     |
| --------------- | --- | ---------------- | --- | --- | --------------- | --- | --- | --- |
\mathcal{T}
| 9.41 | definition: determinantofanoperator,det\mathcal{T} |     |     |     |     |     |     |     |
| ---- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Suppose\mathcal{T} \inℒ(\mathcal{V}). Thedeterminant of\mathcal{T},denotedbydet\mathcal{T},isdefinedtobe
| theuniquenumberin\mathbf{F} |     | suchthat |     |     |     |     |     |     |
| ------------------ | --- | -------- | --- | --- | --- | --- | --- | --- |
\alpha =(det\mathcal{T})\alpha
\mathcal{T}
forall\alpha\in\mathcal{V}(dim\mathcal{V}).
alt
| 9.42 | example: determinantsofoperators |     |     |     |     |     |     |     |
| ---- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Letn=dim\mathcal{V}.
=\alphaforall\alpha\in\mathcal{V}(n).
| • If\mathcal{I} istheidentityoperatoron\mathcal{V},then\alpha |     |     |     |     |     |     | Thusdet\mathcal{I} | =1. |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- |
|                                      |     |     |     | \mathcal{I}   |     |     | alt      |     |
• Moregenerally,if \lambda\in\mathbf{F},then\alpha = \lambdan\alphaforall\alpha\in\mathcal{V}(n). Thusdet(\lambda\mathcal{I})= \lambdan.
|     |     |     | \lambda\mathcal{I}  |     |     | alt |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
• Stillmoregenerally,if\mathcal{T} \inℒ(\mathcal{V})and \lambda\in\mathbf{F},then\alpha = \lambdan\alpha = \lambdan(det\mathcal{T})\alpha
|     |     |     |     |     |     | \lambda\mathcal{T}  | \mathcal{T}   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
forall\alpha\in\mathcal{V}(n).
|     |     | Thusdet(\lambda\mathcal{T})= | \lambdandet\mathcal{T}. |     |     |     |     |     |
| --- | --- | ------------ | ------- | --- | --- | --- | --- | --- |
alt
• Suppose\mathcal{T} \inℒ(\mathcal{V})andthereisabasise ,…,e of\mathcal{V}consistingofeigenvectors
1 n
|                                  |     |     |     | ,…,\lambda |     | If\alpha\in\mathcal{V}(n),then |     |     |
| -------------------------------- | --- | --- | --- | ---- | --- | ------------- | --- | --- |
| of\mathcal{T},withcorrespondingeigenvalues |     |     |     | \lambda 1  | n . |               |     |     |
alt
|     | \alpha (e ,…,e | )=\alpha(\lambda | e ,…,\lambda | e )=(\lambda |     | ⋯\lambda )\alpha(e | ,…,e ). |     |
| --- | --------- | ----- | ------ | ------ | --- | ------- | ------- | --- |
|     | \mathcal{T} 1       | n     | 1 1    | n n    |     | 1 n     | 1 n     |     |
If\alpha\neq0,then9.39implies\alpha(e ,…,e )\neq0. Thustheequationaboveimplies
1 n
|     |     |     | det\mathcal{T} | = \lambda ⋯\lambda | .   |     |     |     |
| --- | --- | --- | ---- | ------ | --- | --- | --- | --- |
1 n

| --- | --- | --------- | ------------ | --- |
Ournexttaskistodefineandgiveaformulaforthedeterminantofasquare
matrix. Todothis,weassociatewitheachsquarematrixanoperatorandthen
define the determinant of the matrix to be the determinant of the associated
operator.
| 9.43 definition: determinantofamatrix,det\mathcal{A} |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- |
Suppose that n is a positive integer and \mathcal{A} is an n-by-n square matrix with
entries in \mathbf{F}. Let \mathcal{T} \in ℒ(\mathbf{F}n) be the operator whose matrix with respect to
thestandardbasisof\mathbf{F}n equals\mathcal{A}. Thedeterminant of\mathcal{A},denotedbydet\mathcal{A},is
definedbydet\mathcal{A}=det\mathcal{T}.
determinantsofmatrices
**9.44 例：** isthen-by-nidentitymatrix,thenthecorrespondingoperatoron\mathbf{F}n
| • If\mathcal{I} |     |     |     | isthe |
| ----- | --- | --- | --- | ----- |
identityoperator\mathcal{I} on\mathbf{F}n. Thusthefirstbulletpointof9.42impliesthatthe
determinantoftheidentitymatrixis1.
• Suppose \mathcal{A} is a diagonal matrix with \lambda ,…,\lambda on the diagonal. Then the
1 n
|     | \mathbf{F}n  |     | \mathbf{F}n  |     |
| --- | --- | --- | --- | --- |
corresponding operator on has the standard basis of as eigenvectors,
with eigenvalues \lambda ,…,\lambda . Thus the last bullet point of 9.42 implies that
1 n
| det\mathcal{A}= \lambda ⋯\lambda . |     |     |     |     |
| ------------ | --- | --- | --- | --- |
1 n
Forthenextresult,thinkofeachlistv ,…,v ofnvectorsin\mathbf{F}n asalistof
1 n
n-by-1 column vectors. The notation ( v ⋯ v ) then denotes the n-by-n
|                      |           | 1 n              |     |     |
| -------------------- | --------- | ---------------- | --- | --- |
| squarematrixwhosekth | columnisv | foreachk =1,…,n. |     |     |
k
9.45 determinantisanalternatingmultilinearform
Suppose that n is a positive integer. The map that takes a list v ,…,v of
|             |     |                                   | 1   | n   |
| ----------- | --- | --------------------------------- | --- | --- |
| vectorsin\mathbf{F}n |     | )isanalternatingn-linearformon\mathbf{F}n. |     |     |
todet( v 1 ⋯ v n
| ,…,e       | bethestandardbasisof\mathbf{F}nandsupposev |     | ,…,v |           |
| ---------- | --------------------------------- | --- | ---- | --------- |
| Proof Lete |                                   |     |      | isalistof |
| 1 n        |                                   |     | 1 n  |           |
vectorsin\mathbf{F}n. Let\mathcal{T} \inℒ(\mathbf{F}n)betheoperatorsuchthat\mathcal{T}e =v fork =1,…,n.
k k
Thus\mathcal{T} istheoperatorwhosematrixwithrespecttoe ,…,e is( v ⋯ v ).
|     |     | 1   | n 1 | n   |
| --- | --- | --- | --- | --- |
Hencedet( v ⋯ v )=det\mathcal{T},bydefinitionofthedeterminantofamatrix.
1 n
Let\alphabeanalternatingn-linearformon\mathbf{F}n
|     |     | suchthat\alpha(e | ,…,e )=1. | Then |
| --- | --- | ----------- | --------- | ---- |
1 n
| det( | v 1 ⋯ | v n )=det\mathcal{T} |     |     |
| ---- | ----- | ---------- | --- | --- |
,…,e
|     |     | =(det\mathcal{T})\alpha(e | )   |     |
| --- | --- | ---------- | --- | --- |
1 n
|     |     | =\alpha(\mathcal{T}e ,…,\mathcal{T}e ) |     |     |
| --- | --- | ------------- | --- | --- |
|     |     | 1 n           |     |     |
|     |     | =\alpha(v ,…,v ),  |     |     |
|     |     | 1 n           |     |     |
wherethethirdlinefollowsfromthedefinitionofthedeterminantofanoperator.
Theequationaboveshowsthatthemapthattakesalistofvectorsv ,…,v in\mathbf{F}n
|     |     |     | 1   | n   |
| --- | --- | --- | --- | --- |
$$)isthealternatingn-linearform\alphaon\mathbf{F}n.$$
| todet( v ⋯ v |     |     |     |     |
| ------------ | --- | --- | --- | --- |
1 n

| --- | -------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
The previous result has several important consequences. For example, it
immediatelyimpliesthatamatrixwithtwoidenticalcolumnshasdeterminant0.
Wewillcomebacktootherconsequenceslater,butfornowwewanttogivea
formulaforthedeterminantofasquarematrix. Recallthatif\mathcal{A}isamatrix,then
\mathcal{A} denotestheentryinrowj,columnkof\mathcal{A}.
j,k
9.46 formulafordeterminantofamatrix
Supposethatnisapositiveintegerand\mathcal{A}isann-by-nsquarematrix. Then
|     | det\mathcal{A}= |     | \sum   | (sign(j | ,…,j | ))\mathcal{A} | ⋯\mathcal{A}   | .    |
| --- | ----- | --- | --- | ------- | ---- | --- | ---- | ---- |
|     |       |     |     |         | 1    | n   | j ,1 | j ,n |
|     |       |     |     |         |      |     | 1    | n    |
$$(j 1 ,…,j n )\inpermn$$
Proof Apply9.36with\mathcal{V} =\mathbf{F}n ande ,…,e thestandardbasisof\mathbf{F}n and\alphathe
|     |     |     |     | 1   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
alternatingn-linearformon\mathbf{F}n thattakesv ,…,v todet( v ⋯ v )[see
|     |     |     |     |     | 1   | n   |     | 1 n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
9.45]. Ifeachv isthekth columnof\mathcal{A},theneachb in9.36equals\mathcal{A} . Finally,
|     | k   |      |        |     |     | j,k      |     | j,k |
| --- | --- | ---- | ------ | --- | --- | -------- | --- | --- |
|     | \alpha(e | ,…,e | )=det( | e   | ⋯   | e )=det\mathcal{I} | =1. |     |
|     |     | 1    | n      | 1   |     | n        |     |     |
Thustheformulain9.36becomestheformulastatedinthisresult.
| 9.47 | example: explicitformulafordeterminant |     |     |     |     |     |     |     |
| ---- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
• If\mathcal{A}isa2-by-2matrix,thentheformulain9.46becomes
|     |     |     | det\mathcal{A}=\mathcal{A} |     | \mathcal{A} -\mathcal{A} | \mathcal{A}   | .   |     |
| --- | --- | --- | ------ | --- | ---- | --- | --- | --- |
|     |     |     |        | 1,1 | 2,2  | 2,1 | 1,2 |     |
• If\mathcal{A}isa3-by-3matrix,thentheformulain9.46becomes
|     | det\mathcal{A}=\mathcal{A} |     | \mathcal{A} \mathcal{A}       | -\mathcal{A}    | \mathcal{A} \mathcal{A}   | -\mathcal{A}        | \mathcal{A}       | \mathcal{A}           |
| --- | ------ | --- | --------- | ----- | ----- | --------- | ------- | ----------- |
|     |        | 1,1 | 2,2 3,3   | 2,1   | 1,2   | 3,3       | 3,1 2,2 | 1,3         |
|     |        |     |           | +\mathcal{A}    |       |           | +\mathcal{A}      |             |
|     |        | -\mathcal{A}  | 1,1 \mathcal{A} 3,2 | \mathcal{A} 2,3 | 3,1 \mathcal{A} | 1,2 \mathcal{A} 2,3 | 2,1 \mathcal{A}   | 3,2 \mathcal{A} 1,3 . |
Thesumintheformulain9.46containsn!terms. Becausen!growsrapidlyas
nincreases,theformulain9.46isnotaviablemethodtoevaluatedeterminants
evenformoderatelysizedn. Forexample,10!isoverthreemillion,and100!is
approximately10158,leadingtoasumthatthefastestcomputercannotevaluate.
Wewillsoonseesomeresultsthatleadtofasterevaluationsofdeterminantsthan
directuseofthesumin9.46.
determinantofupper-triangularmatrix
9.48
Supposethat\mathcal{A}isanupper-triangularmatrixwith \lambda ,…,\lambda onthediagonal.
|           |           |               |     |      |                 |     | 1   | n         |
| --------- | --------- | ------------- | --- | ---- | --------------- | --- | --- | --------- |
| Thendet\mathcal{A}= | \lambda         | ⋯\lambda .          |     |      |                 |     |     |           |
|           | 1         | n             |     |      |                 |     |     |           |
| Proof     | If(j ,…,j | )\inpermnwith(j |     | ,…,j | )\neq(1,…,n),thenj |     |     | >kforsome |
|           | 1         | n             |     | 1    | n               |     |     | k         |
k \in {1,…,n}, which implies that \mathcal{A} = 0. Thus the only permutation that
j k ,k
canmakeanonzerocontributiontothesumin9.46isthepermutation(1,…,n).
| Because\mathcal{A} | = \lambda | foreachk | =1,…,n,thisimpliesthatdet\mathcal{A}= |     |     |     |     | \lambda ⋯\lambda . |
| -------- | --- | -------- | --------------------------- | --- | --- | --- | --- | ------ |
|          | k,k | k        |                             |     |     |     |     | 1 n    |

Section9C Determinants
| Properties |     | of Determinants |     |     |     |     |
| ---------- | --- | --------------- | --- | --- | --- | --- |
Ourdefinitionofthedeterminantleadstothefollowingmagicalproofthatthe
determinantismultiplicative.
9.49 determinantismultiplicative
|     | Suppose\mathcal{S},\mathcal{T} |     | \inℒ(\mathcal{V}). |                           |     |     |
| --- | ---------- | --- | ------ | ------------------------- | --- | --- |
| (a) |            |     |        | Thendet(\mathcal{S}\mathcal{T})=(det\mathcal{S})(det\mathcal{T}). |     |     |
$$(b) Suppose\mathcal{A}and\mathcal{B}aresquarematricesofthesamesize. Then$$
det(\mathcal{A}\mathcal{B})=(det\mathcal{A})(det\mathcal{B})
Proof
| (a) | Letn=dim\mathcal{V}. |     | Suppose\alpha\in\mathcal{V}(n) | andv ,…,v   | \in\mathcal{V}. Then |     |
| --- | ---------- | --- | ------------- | ----------- | -------- | --- |
|     |            |     |               | alt 1       | n        |     |
|     |            |     | ,…,v          | ,…,\mathcal{S}\mathcal{T}v      |          |     |
|     |            |     | \alpha (v          | )=\alpha(\mathcal{S}\mathcal{T}v     | )        |     |
|     |            |     | \mathcal{S}\mathcal{T} 1          | n 1         | n        |     |
|     |            |     |               | =(det\mathcal{S})\alpha(\mathcal{T}v | ,…,\mathcal{T}v )  |     |
1 n
|     |     |     |     | =(det\mathcal{S})(det\mathcal{T})\alpha(v | ,…,v ), |     |
| --- | --- | --- | --- | ---------------- | ------- | --- |
1 n
wherethefirstequationfollowsfromthedefinitionof\alpha ,thesecondequation
\mathcal{S}\mathcal{T}
followsfromthedefinitionofdet\mathcal{S},andthethirdequationfollowsfromthe
definitionofdet\mathcal{T}. Theequationaboveimpliesthatdet(\mathcal{S}\mathcal{T})=(det\mathcal{S})(det\mathcal{T}).
\inℒ(\mathbf{F}n)besuchthatℳ(\mathcal{S})=\mathcal{A}andℳ(\mathcal{T})=\mathcal{B},whereallmatrices
$$(b) Let\mathcal{S},\mathcal{T}$$
ofoperatorsinthisproofarewithrespecttothestandardbasisof\mathbf{F}n. Then
|     | ℳ(\mathcal{S}\mathcal{T})=ℳ(\mathcal{S})ℳ(\mathcal{T})=\mathcal{A}\mathcal{B}(see3.43). |     |     | Thus |     |     |
| --- | --------------------------- | --- | --- | ---- | --- | --- |
det(\mathcal{A}\mathcal{B})=det(\mathcal{S}\mathcal{T})=(det\mathcal{S})(det\mathcal{T})=(det\mathcal{A})(det\mathcal{B}),
wherethesecondequalitycomesfromtheresultin(a).
Thedeterminantofanoperatordetermineswhethertheoperatorisinvertible.
| 9.50 | invertible | ⟺   | nonzerodeterminant |     |     |     |
| ---- | ---------- | --- | ------------------ | --- | --- | --- |
Anoperator\mathcal{T} \inℒ(\mathcal{V})isinvertibleifandonlyifdet\mathcal{T} \neq0. Furthermore,if
| \mathcal{T}   | isinvertible,thendet(\mathcal{T}-1)= |     |     | 1 . |     |     |
| --- | -------------------------- | --- | --- | --- | --- | --- |
det\mathcal{T}
|     | Firstsuppose\mathcal{T} |     | isinvertible. | Thus\mathcal{T}\mathcal{T}-1 | =\mathcal{I}. Now9.49impliesthat |     |
| --- | ------------- | --- | ------------- | -------- | ---------------------- | --- |
Proof
|           |     | 1=det\mathcal{I}                                         | =det(\mathcal{T}\mathcal{T}-1)=(det\mathcal{T})(det(\mathcal{T}-1)). |     |     |     |
| --------- | --- | ---------------------------------------------- | ---------------------------- | --- | --- | --- |
| Hencedet\mathcal{T} |     | \neq0anddet(\mathcal{T}-1)isthemultiplicativeinverseofdet\mathcal{T}. |                              |     |     |     |
To prove the other direction, now suppose det\mathcal{T} \neq 0. Suppose v \in \mathcal{V} and
andlet\alpha\in\mathcal{V}(n)
| v\neq0.      | Letv,e | ,…,e         | beabasisof\mathcal{V}   |               | besuchthat\alpha\neq0. | Then |
| --------- | ------ | ------------ | ------------- | ------------- | -------------- | ---- |
|           |        | 2            | n             |               | alt            |      |
| \alpha(v,e     | ,…,e   | )\neq0(by9.39). |               | Now           |                |      |
|           | 2      | n            |               |               |                |      |
|           |        | \alpha(\mathcal{T}v,\mathcal{T}e      | ,…,\mathcal{T}e         | )=(det\mathcal{T})\alpha(v,e | ,…,e )\neq0.      |      |
|           |        |              | 2             | n             | 2 n            |      |
| Thus\mathcal{T}v\neq0. |        | Hence\mathcal{T}       | isinvertible. |               |                |      |

| -------- | --- | --------------------------------- | --- | --- | --- | --- |
Ann-by-nmatrix\mathcal{A}isinvertible(see3.80forthedefinitionofaninvertible
matrix)ifandonlyiftheoperatoron\mathbf{F}nassociatedwith\mathcal{A}(viathestandardbasis
\mathbf{F}n)
of is invertible. Thus the previous result shows that a square matrix \mathcal{A} is
invertibleifandonlyifdet\mathcal{A}\neq0.
9.51 eigenvaluesanddeterminants
Suppose\mathcal{T} \in ℒ(\mathcal{V})and \lambda \in \mathbf{F}. Then \lambdaisaneigenvalueof\mathcal{T} ifandonlyif
det(\lambda\mathcal{I}-\mathcal{T})=0.
Proof Thenumber \lambdaisaneigenvalueof\mathcal{T} ifandonlyif\mathcal{T}-\lambda\mathcal{I} isnotinvertible
$$(see5.7),whichhappensifandonlyif \lambda\mathcal{I}-\mathcal{T} isnotinvertible,whichhappensif$$
andonlyifdet(\lambda\mathcal{I}-\mathcal{T})=0(by9.50).
\inℒ(\mathcal{V})and\mathcal{S}∶
| Suppose\mathcal{T} |     |     | \mathcal{W} \rightarrow\mathcal{V} isaninvertiblelinearmap. |     |     | Toprovethat |
| -------- | --- | --- | ----------------------------- | --- | --- | ----------- |
det(\mathcal{S}-1\mathcal{T}\mathcal{S})=det\mathcal{T},wecouldtrytouse9.49and9.50,writing
det(\mathcal{S}-1\mathcal{T}\mathcal{S})=(det\mathcal{S}-1)(det\mathcal{T})(det\mathcal{S})
=det\mathcal{T}.
Thatproofworksif\mathcal{W} = \mathcal{V},butif\mathcal{W} \neq \mathcal{V} thenitmakesnosensebecausethe
determinantisdefinedonlyforlinearmapsfromavectorspacetoitself,and\mathcal{S}
maps\mathcal{W} to\mathcal{V},makingdet\mathcal{S}undefined. Theproofgivenbelowworksaroundthis
| issueandisvalidwhen\mathcal{W} |     |     | \neq\mathcal{V}. |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- |
9.52 determinantisasimilarityinvariant
| Suppose\mathcal{T} | \inℒ(\mathcal{V})and\mathcal{S}∶ |     | \mathcal{W} \rightarrow\mathcal{V} isaninvertiblelinearmap. |     | Then |     |
| -------- | ---------- | --- | ----------------------------- | --- | ---- | --- |
det(\mathcal{S}-1\mathcal{T}\mathcal{S})=det\mathcal{T}.
\in\mathcal{W}(n). Define\alpha\in\mathcal{V}(n)
| Proof Letn=dim\mathcal{W} |              | =dim\mathcal{V}.  | Suppose\tau      |           |     | by  |
| --------------- | ------------ | ------- | ------------- | --------- | --- | --- |
|                 |              |         |               | alt       |     | alt |
|                 |              | \alpha(v     | ,…,v )=\tau(\mathcal{S}-1v | ,…,\mathcal{S}-1v ) |     |     |
|                 |              | 1       | n             | 1 n       |     |     |
| forv ,…,v       | \in\mathcal{V}. Supposew |         | ,…,w \in\mathcal{W}.      | Then      |     |     |
| 1               | n            |         | 1 n           |           |     |     |
|                 | \tau            | (w ,…,w | )=\tau(\mathcal{S}-1\mathcal{T}\mathcal{S}w    | ,…,\mathcal{S}-1\mathcal{T}\mathcal{S}w | )   |     |
|                 | \mathcal{S}-1\mathcal{T}\mathcal{S}        | 1       | n             | 1         | n   |     |
|                 |              |         | =\alpha(\mathcal{T}\mathcal{S}w        | ,…,\mathcal{T}\mathcal{S}w )  |     |     |
1 n
,…,\mathcal{S}w
|     |     |     | =\alpha \mathcal{T} (\mathcal{S}w | 1 n ) |     |     |
| --- | --- | --- | -------- | ----- | --- | --- |
,…,\mathcal{S}w
|     |     |     | =(det\mathcal{T})\alpha(\mathcal{S}w |         | )   |     |
| --- | --- | --- | ----------- | ------- | --- | --- |
|     |     |     |             | 1       | n   |     |
|     |     |     | =(det\mathcal{T})\tau(w  | ,…,w ). |     |     |
|     |     |     |             | 1 n     |     |     |
Theequationaboveandthedefinitionofthedeterminantoftheoperator\mathcal{S}-1\mathcal{T}\mathcal{S}
implythatdet(\mathcal{S}-1\mathcal{T}\mathcal{S})=det\mathcal{T}.

| --- | --- | --- | --- | --- | --------- | ------------ | --- |
|     |                           |     |     | =\mathbf{F}n  |      | isthestandardbasisof\mathbf{F}n, |     |
| --- | ------------------------- | --- | --- | ---- | ---- | ----------------------- | --- |
|     | Forthespecialcaseinwhich\mathcal{V} |     |     | ande | ,…,e |                         |     |
1 n
thenextresultistruebythedefinitionofthedeterminantofamatrix. Theleft
sideoftheequationinthenextresultdoesnotdependonachoiceofbasis,which
meansthattherightsideisindependentofthechoiceofbasis.
9.53 determinantofoperatorequalsdeterminantofitsmatrix
| Suppose\mathcal{T} | \inℒ(\mathcal{V})ande |     | ,…,e | isabasisof\mathcal{V}. |      | Then |     |
| -------- | --------- | --- | ---- | ------------ | ---- | ---- | --- |
|          |           |     | 1    | n            |      |      |     |
|          |           |     |      | =detℳ(\mathcal{T},(e   | ,…,e |      |     |
|          |           |     | det\mathcal{T} |              |      | )).  |     |
1 n
|       | Let | ,…, bethestandardbasisof\mathbf{F}n. |     |     | Let\mathcal{S}∶ | \mathbf{F}n \rightarrow\mathcal{V}bethelinearmap |     |
| ----- | --- | --------------------------- | --- | --- | ----- | ------------------- | --- |
| Proof | f 1 | f n                         |     |     |       |                     |     |
suchthat\mathcal{S}f =e foreachk =1,…,n. Thusℳ(\mathcal{S},(f ,…, f ),(e ,…,e ))and
|          | k    | k        |     |                                     |     | 1 n 1 | n     |
| -------- | ---- | -------- | --- | ----------------------------------- | --- | ----- | ----- |
| ℳ(\mathcal{S}-1,(e | ,…,e | ),(f ,…, |     |                                     |     |       |       |
|          | 1    | n 1      | f n | ))bothequalthen-by-nidentitymatrix. |     |       | Hence |
ℳ(\mathcal{S}-1\mathcal{T}\mathcal{S},(f
| 9.54                                |     |      |                | ,…, f ))=ℳ(\mathcal{T},(e |     | ,…,e )), |     |
| ----------------------------------- | --- | ---- | -------------- | --------------- | --- | -------- | --- |
|                                     |     |      |                | 1 n             |     | 1 n      |     |
| asfollowsfromtwoapplicationsof3.43. |     |      |                | Thus            |     |          |     |
|                                     |     | det\mathcal{T} | =det(\mathcal{S}-1\mathcal{T}\mathcal{S})    |                 |     |          |     |
|                                     |     |      | =detℳ(\mathcal{S}-1\mathcal{T}\mathcal{S},(f |                 | ,…, | f ))     |     |
1 n
|     |     |     | =detℳ(\mathcal{T},(e |     | ,…,e | )), |     |
| --- | --- | --- | ---------- | --- | ---- | --- | --- |
|     |     |     |            | 1   | n    |     |     |
wherethefirstlinecomesfrom9.52,thesecondlinecomesfromthedefinitionof
thedeterminantofamatrix,andthethirdlinefollowsfrom9.54.
Thenextresultgivesamoreintuitivewaytothinkaboutdeterminantsthanthe
definitionortheformulain9.46. Wecouldmakethecharacterizationintheresult
belowthedefinitionofthedeterminantofanoperatoronafinite-dimensional
complexvectorspace,withthecurrentdefinitionthenbecomingaconsequence
ofthatdefinition.
| 9.55     | if \mathbf{F} =\mathbf{C},thendeterminantequalsproductofeigenvalues |      |        |          |                             |     |     |
| -------- | ------------------------------------------------- | ---- | ------ | -------- | --------------------------- | --- | --- |
| Suppose\mathbf{F} | =\mathbf{C}                                                | and\mathcal{T} | \inℒ(\mathcal{V}). | Thendet\mathcal{T} | equalstheproductoftheeigen- |     |     |
valuesof\mathcal{T},witheacheigenvalueincludedasmanytimesasitsmultiplicity.
Proof There is a basis of \mathcal{V} with respect to which \mathcal{T} has an upper-triangular
matrixwiththediagonalentriesofthematrixconsistingoftheeigenvaluesof\mathcal{T},
witheacheigenvalueincludedasmanytimesasitsmultiplicity—see8.37. Thus
9.53and9.48implythatdet\mathcal{T} equalstheproductoftheeigenvaluesof\mathcal{T},with
eacheigenvalueincludedasmanytimesasitsmultiplicity.
Asthenextresultshows,thedeterminantinteractsnicelywiththetransposeof
asquarematrix,withthedualofanoperator,andwiththeadjointofanoperator
onaninnerproductspace.

| -------- | --------------------------------- | --- | --- | --- | --- |
determinantoftranspose,dual,oradjoint
9.56
| (a) Suppose\mathcal{A}isasquarematrix. |                           | Thendet\mathcal{A}t |        | =det\mathcal{A}. |      |
| ---------------------------- | ------------------------- | --------- | ------ | ------ | ---- |
| (b) Suppose\mathcal{T}                 | \inℒ(\mathcal{V}). Thendet\mathcal{T}′          |           | =det\mathcal{T}. |        |      |
| (c) Suppose\mathcal{V}                 | isaninnerproductspaceand\mathcal{T} |           |        | \inℒ(\mathcal{V}). | Then |
∗
det(\mathcal{T} )=det\mathcal{T}.
Proof
Define\alpha∶ (\mathbf{F}n)n
| (a) Letnbeapositiveinteger. |     |     |     | \rightarrow\mathbf{F}  | by  |
| --------------------------- | --- | --- | --- | --- | --- |
t
|     | \alpha(v ,…,v | )=det(( |     | v ⋯ | v )) |
| --- | -------- | ------- | --- | --- | ---- |
|     | 1        | n       |     | 1   | n    |
forallv ,…,v \in \mathbf{F}n. Theformulain9.46forthedeterminantofamatrix
1 n
showsthat\alphaisann-linearformon\mathbf{F}n.
| Supposev | ,…,v \in\mathbf{F}nandv | =v  | forsomej | \neqk. | If\mathcal{B}isann-by-nmatrix, |
| -------- | ------------ | --- | -------- | --- | -------------------- |
|          | 1 n          | j   | k        |     |                      |
t
| then( v | ⋯ v ) \mathcal{B}cannotequaltheidentitymatrixbecauserowjand |     |     |     |     |
| ------- | ------------------------------------------------- | --- | --- | --- | --- |
1 n
|         | t                  |     |       |     | t                      |
| ------- | ------------------ | --- | ----- | --- | ---------------------- |
| rowkof( | v ⋯ v ) \mathcal{B}areequal. |     | Thus( | v   | ⋯ v ) isnotinvertible, |
|         | 1 n                |     |       | 1   | n                      |
whichimpliesthat\alpha(v ,…,v )=0. Hence\alphaisanalternatingn-linearform
|     | 1   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- |
on\mathbf{F}n.
Notethat\alphaappliedtothestandardbasisof\mathbf{F}n
|     |     |     |     | equals1. | Becausethevector |
| --- | --- | --- | --- | -------- | ---------------- |
spaceofalternatingn-linearformson\mathbf{F}n hasdimensionone(by9.37),this
| impliesthat\alphaisthedeterminantfunction. |                                     |     |     | Thus(a)holds. |     |
| ------------------------------------- | ----------------------------------- | --- | --- | ------------- | --- |
| (b) Theequationdet\mathcal{T}′                  | =det\mathcal{T}followsfrom(a)and9.53and3.132. |     |     |               |     |
∗
$$(c) Pickanorthonormalbasisof\mathcal{V}. Thematrixof\mathcal{T} withrespecttothatbasis$$
istheconjugatetransposeofthematrixof\mathcal{T} withrespecttothatbasis(by
∗
| 7.9). Thus9.53,9.46,and(a)implythatdet(\mathcal{T} |     |     |     | )=det\mathcal{T}. |     |
| ---------------------------------------- | --- | --- | --- | ------- | --- |
helpfulresultsinevaluatingdeterminants
9.57
$$(a) Ifeithertwocolumnsortworowsofasquarematrixareequal,thenthe$$
determinantofthematrixequals0.
$$(b) Suppose \mathcal{A} is a square matrix and \mathcal{B} is the matrix obtained from \mathcal{A} by$$
| swappingeithertwocolumnsortworows. |     |     |     | Thendet\mathcal{A}=-det\mathcal{B}. |     |
| ---------------------------------- | --- | --- | --- | --------------- | --- |
$$(c) Ifonecolumnoronerowofasquarematrixismultipliedbyascalar,then$$
thevalueofthedeterminantismultipliedbythesamescalar.
$$(d) Ifascalarmultipleofonecolumnofasquarematrixisaddedtoanother$$
column,thenthevalueofthedeterminantisunchanged.
$$(e) Ifascalarmultipleofonerowofasquarematrixisaddedtoanotherrow,$$
thenthevalueofthedeterminantisunchanged.

| --- | --- | --- | --- | --- | --------- | --- | ------------ | --- |
Proof All the assertions in this result follow from the result that the maps
| ,…,v | det( |     |     | )andv | ,…,v | det( |     | t areboth |
| ---- | ---- | --- | --- | ----- | ---- | ---- | --- | --------- |
| v 1  | n ↦  | v 1 | ⋯   | v n   | 1    | n ↦  | v 1 | ⋯ v n )   |
alternatingn-linearformson\mathbf{F}n[see9.45and9.56(a)].
|     |                               |     |     |     | ,…,v | \in\mathbf{F}n |          |      |
| --- | ----------------------------- | --- | --- | --- | ---- | --- | -------- | ---- |
|     | Forexample,toprove(d)supposev |     |     |     | 1    | n   | andc \in\mathbf{F}. | Then |
+cv
|     | det( v | 1   | 2 v 2 | ⋯   | v n )     |     |     |       |
| --- | ------ | --- | ----- | --- | --------- | --- | --- | ----- |
|     | =det(  |     | v v   | ⋯   | v )+cdet( | v   | v v | ⋯ v ) |
|     |        |     | 1 2   |     | n         | 2   | 2 3 | n     |
$$),$$
|     | =det( |     | v v | ⋯   | v   |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     |       |     | 1 2 |     | n   |     |     |     |
wherethefirstequationfollowsfromthemultilinearitypropertyandthesecond
equationfollowsfromthealternatingproperty. Theequationaboveshowsthat
addingamultipleofthesecondcolumntothefirstcolumndoesnotchangethe
valueofthedeterminant. Thesameconclusionholdsforanytwocolumns. Thus
$$(d)holds.$$
Theproofof(e)followsfrom(d)andfrom9.56(a). Theproofsof(a),(b),and
$$(c)usesimilartoolsandarelefttothereader.$$
Formatriceswhoseentriesareconcretenumbers,theresultaboveleadstoa
muchfasterwaytoevaluatethedeterminantthandirectapplicationoftheformula
in 9.46. Specifically, apply the Gaussian elimination procedure of swapping
rows[by9.57(b),thischangesthedeterminantbyafactorof-1],multiplying
a row by a nonzero constant [by 9.57(c), this changes the determinant by the
sameconstant],andaddingamultipleofonerowtoanotherrow[by9.57(e),this
doesnotchangethedeterminant]toproduceanupper-triangularmatrix,whose
determinantistheproductofthediagonalentries(by9.48). Ifyoursoftwarekeeps
trackofthenumberofrowswapsandoftheconstantsusedwhenmultiplyinga
rowbyaconstant,thenthedeterminantoftheoriginalmatrixcanbecomputed.
ℒ(\mathcal{V})ifand
|     | Becauseanumber |     | \lambda \in | \mathbf{F} isaneigenvalueofanoperator\mathcal{T} |     |     |     | \in   |
| --- | -------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |
only if det(\lambda\mathcal{I} -\mathcal{T}) = 0 (by 9.51), you may be tempted to think that one way
ℳ(\mathcal{T}),
to find eigenvalues quickly is to choose a basis of \mathcal{V}, let \mathcal{A} = evaluate
det(\lambda\mathcal{I}-\mathcal{A}),andthensolvetheequationdet(\lambda\mathcal{I}-\mathcal{A}) = 0for \lambda. However,that
procedureisrarelyefficient,exceptwhendim\mathcal{V} =2(orwhendim\mathcal{V} equals3or
4ifyouarewillingtousethecubicorquarticformulas). Oneproblemisthatthe
proceduredescribedintheparagraphaboveforevaluatingadeterminantdoesnot
workwhenthematrixincludesasymbol(suchasthe \lambdain \lambda\mathcal{I}-\mathcal{A}). Thisproblem
arisesbecausedecisionsneedtobemadeinthe Gaussianeliminationprocedure
aboutwhethercertainquantitiesequal0,andthosedecisionsbecomecomplicated
| inexpressionsinvolvingasymbol |     |     |     |     | \lambda.  |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Recallthatanoperatoronafinite-dimensionalinnerproductspaceisunitary
ifitpreservesnorms(see7.51andtheparagraphfollowingit). Everyeigenvalue
of a unitary operator has absolute value 1 (by 7.54). Thus the product of the
eigenvaluesofaunitaryoperatorhasabsolutevalue1. Hence(atleastinthecase
\mathbf{F} =\mathbf{C})thedeterminantofaunitaryoperatorhasabsolutevalue1(by9.55). The
| nextresultgivesaproofthatworkswithouttheassumptionthat\mathbf{F} |     |     |     |     |     |     |     | =\mathbf{C}. |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

362 Chapter 9 Multilinear Algebraand Determinants
9.58 everyunitaryoperatorhasdeterminantwithabsolutevalue1
Suppose \mathcal{V} is an inner product space and \mathcal{S} \in ℒ(\mathcal{V}) is a unitary operator.
Then|det\mathcal{S}|=1.
∗
Proof Because\mathcal{S}isunitary,\mathcal{I} =\mathcal{S} \mathcal{S}(see7.53). Thus
$$1=det(\mathcal{S} ∗ \mathcal{S})=(det\mathcal{S} ∗ )(det\mathcal{S})=(det\mathcal{S})(det\mathcal{S})=|det\mathcal{S}|2,$$
wherethesecondequalitycomesfrom9.49(a)andthethirdequalitycomesfrom
9.56(c). Theequationaboveimpliesthat|det\mathcal{S}|=1.
Thedeterminantofapositiveoperatoronaninnerproductspacemesheswell
withtheanalogythatsuchoperatorscorrespondtothenonnegativerealnumbers.
9.59 everypositiveoperatorhasnonnegativedeterminant
Suppose \mathcal{V} is an inner product space and \mathcal{T} \in ℒ(\mathcal{V}) is a positive operator.
Thendet\mathcal{T} \geq0.
Proof By the spectral theorem (7.29 or 7.31), \mathcal{V} has an orthonormal basis
consistingofeigenvectorsof\mathcal{T}. Thusbythelastbulletpointof9.42,det\mathcal{T} equals
aproductoftheeigenvaluesof\mathcal{T},possiblywithrepetitions. Eacheigenvalueof\mathcal{T}
isanonnegativenumber(by7.38). Thusweconcludethatdet\mathcal{T} \geq0.
Suppose\mathcal{V} isaninnerproductspaceand\mathcal{T} \in ℒ(\mathcal{V}). Recallthatthelistof
∗
nonnegativesquarerootsoftheeigenvaluesof\mathcal{T} \mathcal{T} (eachincludedasmanytimes
asitsmultiplicity)iscalledthelistofsingularvaluesof\mathcal{T} (see Section7E).
9.60 |det\mathcal{T}|=productofsingularvaluesof \mathcal{T}
Suppose\mathcal{V} isaninnerproductspaceand\mathcal{T} \inℒ(\mathcal{V}). Then
|det\mathcal{T}|=\sqrtdet(\mathcal{T}∗\mathcal{T})=productofsingularvaluesof\mathcal{T}.
|det\mathcal{T}|2 =(det\mathcal{T})(det\mathcal{T})=(det(\mathcal{T} ∗ ))(det\mathcal{T})=det(\mathcal{T} ∗ \mathcal{T}),
wherethemiddleequalitycomesfrom9.56(c)andthelastequalitycomesfrom
9.49(a). Taking square roots of both sides of the equation above shows that
|det\mathcal{T}|=\sqrtdet(\mathcal{T}∗\mathcal{T}).
Let s ,…,s denote the list of singular values of \mathcal{T}. Thus s2,…,s2 is the
1 n 1 n
∗
list of eigenvalues of \mathcal{T} \mathcal{T} (with appropriate repetitions), corresponding to an
∗
orthonormalbasisof\mathcal{V} consistingofeigenvectorsof\mathcal{T} \mathcal{T}. Hencethelastbullet
pointof9.42impliesthat
det(\mathcal{T} ∗ \mathcal{T})=s2⋯s2.
1 n
Thus|det\mathcal{T}|=s ⋯s ,asdesired.
1 n

| --- | --- | --------- | ------------ |
Anoperator\mathcal{T} onarealinnerproductspacechangesvolumebyafactorofthe
productofthesingularvalues(by7.111). Thusthenextresultfollowsimmediately
from7.111and9.60. Thisresultexplainswhytheabsolutevalueofadeterminant
appearsinthechangeofvariablesformulainmultivariablecalculus.
| 9.61 \mathcal{T} changesvolumebyfactorof |     | |det\mathcal{T}| |     |
| ------------------------------ | --- | ------ | --- |
\inℒ(\mathbf{R}n)and\Omega\subseteq\mathbf{R}n.
| Suppose\mathcal{T} |     | Then |     |
| -------- | --- | ---- | --- |
volume\mathcal{T}(\Omega)=|det\mathcal{T}|(volume\Omega).
Foroperatorsonfinite-dimensionalcomplexvectorspaces,wenowconnect
thedeterminanttoapolynomialthatwehavepreviouslyseen.
9.62 if \mathbf{F} =\mathbf{C},thencharacteristicpolynomialof \mathcal{T} equalsdet(z\mathcal{I}-\mathcal{T})
Suppose\mathbf{F} =\mathbf{C}and\mathcal{T} \inℒ(\mathcal{V}). Let \lambda ,…,\lambda denotethedistincteigenvalues
1 m
,…,d
| of\mathcal{T},andletd | denotetheirmultiplicities. |     | Then |
| ----------- | -------------------------- | --- | ---- |
1 m
|     | det(z\mathcal{I}-\mathcal{T})=(z- | \lambda )d 1⋯(z- | \lambda )d m. |
| --- | ------------- | ---------- | ------- |
|     |               | 1          | m       |
Proof Thereexistsabasisof\mathcal{V} withrespecttowhich\mathcal{T} hasanupper-triangular
matrixwitheach \lambda appearingonthediagonalexactlyd times(by8.37). With
|     | k   |     | k   |
| --- | --- | --- | --- |
respecttothisbasis,z\mathcal{I}-\mathcal{T} hasanupper-triangularmatrixwithz- \lambda appearing
k
onthediagonalexactlyd timesforeachk. Thus9.48givesthedesiredequation.
k
Suppose \mathbf{F} = \mathbf{C} and \mathcal{T} \in ℒ(\mathcal{V}). The characteristic polynomial of \mathcal{T} was
definedin8.26asthepolynomialontherightsideoftheequationin9.62. We
didnotpreviouslydefinethecharacteristicpolynomialofanoperatoronafinitedimensionalrealvectorspacebecausesuchoperatorsmayhavenoeigenvalues,
makingadefinitionusingtherightsideoftheequationin9.62inappropriate.
Wenowpresentanewdefinitionofthecharacteristicpolynomial,motivated
by 9.62. This new definition is valid for both real and complex vector spaces.
Theequationin9.62showsthatthisnewdefinitionisequivalenttoourprevious
| definitionwhen\mathbf{F}  | =\mathbf{C} (8.26).               |     |     |
| ---------------- | ------------------------ | --- | --- |
| 9.63 definition: | characteristicpolynomial |     |     |
| Suppose\mathcal{T} \inℒ(\mathcal{V}).  | Thepolynomialdefinedby   |     |     |
z↦det(z\mathcal{I}-\mathcal{T})
iscalledthecharacteristicpolynomialof\mathcal{T}.
The formula in 9.46 shows that the characteristic polynomial of an operator \mathcal{T} \inℒ(\mathcal{V}) is a monic polynomial of degree dim\mathcal{V}. The zeros in \mathbf{F} of the
characteristicpolynomialof\mathcal{T} areexactlytheeigenvaluesof\mathcal{T} (by9.51).

364 Chapter 9 Multilinear Algebraand Determinants
Previouslyweprovedthe Cayley–Hamiltontheorem(8.29)inthecomplex
case. Nowwecanextendthatresulttooperatorsonrealvectorspaces.
9.64 Cayley–Hamiltontheorem
Suppose\mathcal{T} \inℒ(\mathcal{V})andqisthecharacteristicpolynomialof\mathcal{T}. Thenq(\mathcal{T})=0.
Proof If\mathbf{F} =\mathbf{C},thentheequationq(\mathcal{T})=0followsfrom9.62and8.29.
Now suppose \mathbf{F} = \mathbf{R}. Fix a basis of \mathcal{V}, and let \mathcal{A} be the matrix of \mathcal{T} with
respecttothisbasis. Let\mathcal{S}betheoperatoron\mathbf{C}dim\mathcal{V} suchthatthematrixof\mathcal{S}
$$(withrespecttothestandardbasisof\mathbf{C}dim\mathcal{V})is\mathcal{A}. Forallz\in\mathbf{R} wehave$$
q(z)=det(z\mathcal{I}-\mathcal{T})=det(z\mathcal{I}-\mathcal{A})=det(z\mathcal{I}-\mathcal{S}).
Thusqisthecharacteristicpolynomialof\mathcal{S}. Thecase\mathbf{F} = \mathbf{C} (firstsentenceof
thisproof)nowimpliesthat0=q(\mathcal{S})=q(\mathcal{A})=q(\mathcal{T}).
The Cayley–Hamiltontheorem(9.64)impliesthatthecharacteristicpolynomialofanoperator\mathcal{T} \inℒ(\mathcal{V})isapolynomialmultipleoftheminimalpolynomial
of\mathcal{T} (by5.29). Thusifthedegreeoftheminimalpolynomialof\mathcal{T} equalsdim\mathcal{V},
thenthecharacteristicpolynomialof\mathcal{T} equalstheminimalpolynomialof\mathcal{T}. This
happens for a very large percentage of operators, including over 99.999% of
4-by-4matriceswithintegerentriesin[-100,100](seetheparagraphfollowing
5.25).
Thelastsentenceinournextresultwaspreviouslyprovedinthecomplexcase
$$(see8.54). Nowwecangiveaproofthatworksonbothrealandcomplexvector$$
spaces.
9.65 characteristicpolynomial,trace,anddeterminant
Suppose\mathcal{T} \inℒ(\mathcal{V}). Letn=dim\mathcal{V}. Thenthecharacteristicpolynomialof\mathcal{T}
canbewrittenas
zn-(tr\mathcal{T})zn-1+⋯+(-1)n(det\mathcal{T}).
Proof Theconstanttermofapolynomialfunctionofzisthevalueofthepolynomialwhenz=0. Thustheconstanttermofthecharacteristicpolynomialof\mathcal{T}
equalsdet(-\mathcal{T}),whichequals(-1)ndet\mathcal{T} (bythethirdbulletpointof9.42).
Fixabasisof\mathcal{V},andlet\mathcal{A}bethematrixof\mathcal{T} withrespecttothisbasis. The
matrixofz\mathcal{I}-\mathcal{T} withrespecttothisbasisisz\mathcal{I}-\mathcal{A}. Thetermcomingfromthe
identitypermutation{1,…,n}intheformula9.46fordet(z\mathcal{I}-\mathcal{A})is
$$(z-\mathcal{A} )⋯(z-\mathcal{A} ).$$
1,1 n,n
Thecoefficientofzn-1intheexpressionaboveis-(\mathcal{A} +⋯+\mathcal{A} ),whichequals
1,1 n,n
-tr\mathcal{T}. Thetermsintheformulafordet(z\mathcal{I}-\mathcal{A})comingfromotherelementsof
permncontainatmostn-2factorsoftheformz-\mathcal{A} andthusdonotcontribute
k,k
tothecoefficientofzn-1 inthecharacteristicpolynomialof\mathcal{T}.

Section9C Determinants 365
In the result below, think of the
columns of the n-by-n matrix \mathcal{A} as eleHadamard(1865–1963)in1893.
mentsof\mathbf{F}n. Thenormsappearingbelow
thenarisefromthestandardinnerproducton\mathbf{F}n. Recallthatthenotation\mathcal{R} in
\cdot,k
theproofbelowmeansthekth columnofthematrix\mathcal{R}(aswasdefinedin3.44).
9.66 Hadamard’sinequality
Suppose\mathcal{A}isann-by-nmatrix. Letv ,…,v denotethecolumnsof\mathcal{A}. Then
1 n
n
|det\mathcal{A}|\leq\prod‖v ‖.
k
$$k=1$$
Proof If \mathcal{A} is not invertible, then det\mathcal{A} = 0 and hence the desired inequality
holdsinthiscase.
Thus assume that \mathcal{A} is invertible. The QR factorization (7.58) tells us that
thereexistaunitarymatrix\mathcal{Q}andanupper-triangularmatrix\mathcal{R}whosediagonal
containsonlypositivenumberssuchthat\mathcal{A}=\mathcal{Q}\mathcal{R}. Wehave
|det\mathcal{A}|=|det\mathcal{Q}||det\mathcal{R}|
=|det\mathcal{R}|
n
=\prod \mathcal{R}
k,k
$$k=1$$
n
\leq\prod‖\mathcal{R} ‖
\cdot,k
$$k=1$$
n
=\prod‖\mathcal{Q}\mathcal{R} ‖
\cdot,k
$$k=1$$
n
=\prod‖v ‖,
k
$$k=1$$
wherethefirstlinecomesfrom9.49(b), thesecondlinecomesfrom9.58, the
thirdlinecomesfrom9.48,andthefifthlineholdsbecause\mathcal{Q}isanisometry.
Togiveageometricinterpretationto Hadamard’sinequality,suppose\mathbf{F} =\mathbf{R}.
Let\mathcal{T} \in ℒ(\mathbf{R}n)betheoperatorsuchthat\mathcal{T}e = v foreachk = 1,…,n,where
k k
e ,…,e isthestandardbasisof\mathbf{R}n. Then\mathcal{T} mapsthebox\mathcal{P}(e ,…,e )ontothe
1 n 1 n
parallelepiped \mathcal{P}(v ,…,v ) [see 7.102 and 7.105 for a review of this notation
1 n
andterminology]. Becausethebox\mathcal{P}(e ,…,e )hasvolume1,thisimplies(by
1 n
9.61)thattheparallelepiped\mathcal{P}(v ,…,v )hasvolume|det\mathcal{T}|,whichequals|det\mathcal{A}|.
1 n
Thus Hadamard’sinequalityabovecanbeinterpretedtosaythatamongallparallelepipedswhoseedgeshavelengths‖v ‖,…,‖v ‖,theoneswithlargestvolume
1 n
haveorthogonaledges(andthushavevolume\prodn ‖v ‖).
$$k=1 k$$
Foranecessaryandsufficientconditionfor Hadamard’sinequalitytobean
equality,see Exercise18.

| --- | -------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Thematrixinthenextresultiscalledthe Vandermondematrix. Vandermonde
matriceshaveimportantapplicationsinpolynomialinterpolation, thediscrete
Fouriertransform,andotherareasofmathematics. Theproofofthenextresultis
aniceillustrationofthepowerofswitchingbetweenmatricesandlinearmaps.
9.67 determinantof Vandermondematrix
| Supposen>1and\beta |     |        | ,…,\beta | \in\mathbf{F}. | Then   |       |          |          |     |     |
| -------------- | --- | ------ | ---- | --- | ------ | ----- | -------- | -------- | --- | --- |
|                |     |        | 1    | n   |        |       |          |          |     |     |
|                |     |        |      | \beta2  | \betan-1   |       |          |          |     |     |
|                |     |        | 1 \beta  |     | ⋯      |       |          |          |     |     |
|                |     | ⎛      | 1    | 1   |        | 1 ⎞   |          |          |     |     |
|                |     | ⎜ ⎜    |      |     |        | ⎟ ⎟   |          |          |     |     |
|                |     | ⎜      | 1 \beta  | \beta2  | ⋯ \betan-1 | ⎟     |          |          |     |     |
|                |     | ⎜ ⎜    | 2    | 2   |        | 2 ⎟ ⎟ |          |          |     |     |
|                |     | ⎜      |      |     |        | ⎟     |          |          |     |     |
|                |     | ⎜      |      |     |        | ⎟     |          |          |     |     |
|                |     | det⎜ ⎜ |      |     |        | ⎟ ⎟ = | \prod        | (\beta -\beta ). |     |     |
|                |     | ⎜      |      | ⋱   |        | ⎟     |          | k j      |     |     |
|                |     | ⎜ ⎜    |      |     |        | ⎟ ⎟   | 1\leq j<k\leqn |          |     |     |
|                |     | ⎜      |      |     |        | ⎟     |          |          |     |     |
|                |     | ⎜      |      |     |        | ⎟     |          |          |     |     |
|                |     | ⎜      |      |     |        | ⎟     |          |          |     |     |
|                |     |        |      | \beta2  | \betan-1   |       |          |          |     |     |
|                |     | ⎝      | 1 \beta  |     | ⋯      | ⎠     |          |          |     |     |
|                |     |        | n    | n   |        | n     |          |          |     |     |
Let1,z,…,zn-1bethestandardbasisof𝒫
| Proof                 |     |     |                    |     |     |     | (\mathbf{F})andlete |     | ,…,e denote |     |
| --------------------- | --- | --- | ------------------ | --- | --- | --- | ---------- | --- | ----------- | --- |
|                       |     |     |                    |     |     |     | n-1        | 1   | n           |     |
| thestandardbasisof\mathbf{F}n. |     |     | Definealinearmap\mathcal{S}∶ |     |     |     | 𝒫 (\mathbf{F})\rightarrow\mathbf{F}n   | by  |             |     |
n-1
|     |     |     |     | \mathcal{S}p=(p(\beta |     | ),…,p(\beta | )). |     |     |     |
| --- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- |
|     |     |     |     |         | 1   |         | n   |     |     |     |
Let\mathcal{A}denotethe Vandermondematrixshowninthestatementofthisresult.
Notethat
|     |         |       | \mathcal{A}=ℳ(\mathcal{S},(1,z,…,zn-1),(e |                     |     |     | ,…,e | )). |     |     |
| --- | ------- | ----- | --------------------- | ------------------- | --- | --- | ---- | --- | --- | --- |
|     |         |       |                       |                     |     |     | 1    | n   |     |     |
|     | Let\mathcal{T}∶ 𝒫 | (\mathbf{F})\rightarrow𝒫 |                       | (\mathbf{F})betheoperatoron𝒫 |     |     |      |     |     |     |
$$(\mathbf{F})suchthat\mathcal{T}1=1and$$
|      |           | n-1 | n-1                                  |       |       |        | n-1 |     |           |     |
| ---- | --------- | --- | ------------------------------------ | ----- | ----- | ------ | --- | --- | --------- | --- |
|      |           |     | \mathcal{T}zk                                  | =(z-\beta | )(z-\beta | )⋯(z-\beta |     | )   |           |     |
|      |           |     |                                      |       | 1     | 2      |     | k   |           |     |
|      | =1,…,n-1. |     | Let\mathcal{B}=ℳ(\mathcal{T},(1,z,…,zn-1),(1,z,…,zn-1)). |       |       |        |     |     |           |     |
| fork |           |     |                                      |       |       |        |     |     | Then\mathcal{B}isan |     |
upper-triangularmatrixallofwhosediagonalentriesequal1. Thusdet\mathcal{B}=1(by
9.48).
|     | Let\mathcal{C} =ℳ(\mathcal{S}\mathcal{T},(1,z,…,zn-1),(e |     |     |     | ,…,e | )). | Thus\mathcal{C} | =\mathcal{A}\mathcal{B}(by3.81),which |     |     |
| --- | -------------------------- | --- | --- | --- | ---- | --- | ----- | ----------------- | --- | --- |
|     |                            |     |     |     | 1    | n   |       |                   |     |     |
impliesthat
det\mathcal{A}=(det\mathcal{A})(det\mathcal{B})=det\mathcal{C}.
| Thedefinitionsof\mathcal{C},\mathcal{S},and\mathcal{T} |      |     |        | showthat\mathcal{C}equals |                                    |         |     |         |       |      |
| ------------------------ | ---- | --- | ------ | --------------- | ---------------------------------- | ------- | --- | ------- | ----- | ---- |
| 1                        | 0    |     |        | 0               |                                    | ⋯       |     | 0       |       |      |
| ⎛                        |      |     |        |                 |                                    |         |     |         |       | ⎞    |
| ⎜ ⎜                      |      |     |        |                 |                                    |         |     |         |       | ⎟ ⎟  |
| ⎜ 1                      | \beta -\beta |     |        | 0               |                                    | ⋯       |     | 0       |       | ⎟    |
| ⎜                        | 2    | 1   |        |                 |                                    |         |     |         |       | ⎟    |
| ⎜ ⎜                      |      |     |        |                 |                                    |         |     |         |       | ⎟ ⎟  |
| ⎜                        |      |     |        |                 |                                    |         |     |         |       | ⎟    |
| ⎜ ⎜ 1                    | \beta -\beta | (\beta  | -\beta )(\beta | -\beta              | )                                  | ⋯       |     | 0       |       | ⎟ ⎟  |
| ⎜                        | 3    | 1   | 3 1    | 3               | 2                                  |         |     |         |       | ⎟ ⎟. |
| ⎜ ⎜                      |      |     |        |                 |                                    |         |     |         |       | ⎟    |
| ⎜                        |      |     |        |                 |                                    |         |     |         |       | ⎟    |
| ⎜ ⎜                      |      |     |        |                 |                                    |         |     |         |       | ⎟ ⎟  |
| ⎜                        |      |     |        |                 |                                    | ⋱       |     |         |       | ⎟    |
| ⎜                        |      |     |        |                 |                                    |         |     |         |       | ⎟    |
| ⎜ ⎜                      |      |     |        |                 |                                    |         |     |         |       | ⎟ ⎟  |
| ⎜                        |      |     |        |                 |                                    |         |     |         |       | ⎟    |
| ⎝ 1                      | \beta -\beta | (\beta  | -\beta )(\beta | -\beta              | )                                  | ⋯ (\beta -\beta | )(\beta | -\beta )⋯(\beta | -\beta    | ) ⎠  |
|                          | n    | 1   | n 1    | n               | 2                                  | n       | 1   | n 2     | n n-1 |      |
| Nowdet\mathcal{A}=det\mathcal{C}             |      |     | = \prod    | (\beta              | -\beta),wherewehaveused9.56(a)and9.48. |         |     |         |       |      |
|                          |      |     |        | k               | j                                  |         |     |         |       |      |
1\leqj<k\leqn

| --- | --- | --- | --------- | ------------ |
| Exercises | 9C  |     |     |     |
| --------- | --- | --- | --- | --- |
1 Proveorgiveacounterexample: \mathcal{S},\mathcal{T} \inℒ(\mathcal{V}) ⟹ det(\mathcal{S}+\mathcal{T})=det\mathcal{S}+det\mathcal{T}.
2 Supposethefirstcolumnofasquarematrix\mathcal{A}consistsofallzerosexcept
possiblythefirstentry\mathcal{A} . Let\mathcal{B}bethematrixobtainedfrom\mathcal{A}bydeleting
1,1
| thefirstrowandthefirstcolumnof\mathcal{A}. |                                             |                      | Showthatdet\mathcal{A}=\mathcal{A} | 1,1 det\mathcal{B}. |
| -------------------------------- | ------------------------------------------- | -------------------- | -------------- | --------- |
| 3 Suppose\mathcal{T}                       | \inℒ(\mathcal{V})isnilpotent.                           | Provethatdet(\mathcal{I}+\mathcal{T})=1. |                |           |
| 4 Suppose\mathcal{S}\inℒ(\mathcal{V}).                 | Provethat\mathcal{S}isunitaryifandonlyif|det\mathcal{S}|=‖\mathcal{S}‖=1. |                      |                |           |
5 Suppose\mathcal{A}isablockupper-triangularmatrix
|            |                                  | \mathcal{A}     | ∗       |           |
| ---------- | -------------------------------- | ----- | ------- | --------- |
|            |                                  | ⎛     | 1 ⎞     |           |
|            |                                  | ⎜     | ⎟       |           |
|            |                                  | \mathcal{A}=⎜ ⎜ | ⋱ ⎟ ⎟ , |           |
|            |                                  | 0     | \mathcal{A}       |           |
|            |                                  | ⎝     | m ⎠     |           |
| whereeach\mathcal{A} | alongthediagonalisasquarematrix. |       |         | Provethat |
k
|              | det\mathcal{A}=(det\mathcal{A}   |                           | )⋯(det\mathcal{A}      | ).             |
| ------------ | ------------ | ------------------------- | ------------ | -------------- |
|              |              |                           | 1 m          |                |
| 6 Suppose\mathcal{A}=( | v ⋯          | v )isann-by-nmatrix,withv |              | denotingthekth |
|              | 1            | n                         |              | k              |
| columnof\mathcal{A}.   | Showthatif(m | ,…,m                      | )\inpermn,then |                |
1 n
|     | det( v | ⋯ v )=(sign(m | ,…,m | ))det\mathcal{A}. |
| --- | ------ | ------------- | ---- | ------- |
|     | m 1    | m n           | 1    | n       |
7 Suppose\mathcal{T} \inℒ(\mathcal{V})isinvertible. Letpdenotethecharacteristicpolynomial
andletqdenotethecharacteristicpolynomialof\mathcal{T}-1.
| of\mathcal{T} |     |       |           | Provethat |
| --- | --- | ----- | --------- | --------- |
|     |     | q(z)= | zdim\mathcal{V}p( ) |           |
|     |     | p(0)  | z         |           |
forallnonzeroz\in\mathbf{F}.
8 Suppose\mathcal{T} \inℒ(\mathcal{V})isanoperatorwithnoeigenvalues(whichimpliesthat
| \mathbf{F} =\mathbf{R}). | Provethatdet\mathcal{T} | >0. |     |     |
| ------ | ------------- | --- | --- | --- |
9 Supposethat\mathcal{V} isarealvectorspaceofevendimension,\mathcal{T} \in ℒ(\mathcal{V}),and
| det\mathcal{T} <0. | Provethat\mathcal{T} | hasatleasttwodistincteigenvalues. |     |     |
| -------- | ---------- | --------------------------------- | --- | --- |
10 Suppose\mathcal{V} isarealvectorspaceofodddimensionand\mathcal{T} \inℒ(\mathcal{V}). Without
| usingtheminimalpolynomial,provethat\mathcal{T} |     |     | hasaneigenvalue. |     |
| ------------------------------------ | --- | --- | ---------------- | --- |
Thisresultwaspreviouslyprovedwithoutusingdeterminantsorthecharacteristicpolynomial—see5.34.
11 Proveorgiveacounterexample: If\mathbf{F} =\mathbf{R},\mathcal{T} \inℒ(\mathcal{V}),anddet\mathcal{T} >0,then
\mathcal{T} hasasquareroot.
| If \mathbf{F} | =\mathbf{C},\mathcal{T} \inℒ(\mathcal{V}),anddet\mathcal{T} | \neq0,then\mathcal{T}hasasquareroot(see8.41). |     |     |
| ---- | ------------------ | -------------------------------- | --- | --- |

| --- | -------- | --- | --------------------------------- | --- | --- | --- | --- | --- |
Definep∶
| 12  | Suppose\mathcal{S},\mathcal{T} |     | \inℒ(\mathcal{V})and\mathcal{S}isinvertible. |     |     |     | \mathbf{F} \rightarrow\mathbf{F} | by  |
| --- | ---------- | --- | ---------------------- | --- | --- | --- | ---- | --- |
p(z)=det(z\mathcal{S}-\mathcal{T}).
Provethatpisapolynomialofdegreedim\mathcal{V}andthatthecoefficientofzdim\mathcal{V}
inthispolynomialisdet\mathcal{S}.
13 Suppose \mathbf{F} = \mathbf{C}, \mathcal{T} \in ℒ(\mathcal{V}), and n = dim\mathcal{V} > 2. Let \lambda ,…,\lambda denote
1 n
theeigenvaluesof\mathcal{T}, witheacheigenvalueincludedasmanytimesasits
multiplicity.
$$(a) Findaformulaforthecoefficientofzn-2inthecharacteristicpolynomial$$
,…,\lambda
|     | of\mathcal{T} | intermsof |     | \lambda   | .   |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- |
|     |     |           |     | 1   | n   |     |     |     |
$$(b) Findaformulaforthecoefficientofzinthecharacteristicpolynomial$$
|     | of\mathcal{T} | intermsof |     | \lambda ,…,\lambda | .   |     |     |     |
| --- | --- | --------- | --- | ------ | --- | --- | --- | --- |
|     |     |           |     | 1      | n   |     |     |     |
14 Suppose\mathcal{V}isaninnerproductspaceand\mathcal{T}isapositiveoperatoron\mathcal{V}. Prove
that
|     |     |     |     |     | det\sqrt\mathcal{T} | =\sqrtdet\mathcal{T}. |     |     |
| --- | --- | --- | --- | --- | ----- | ------- | --- | --- |
15 Suppose\mathcal{V} isaninnerproductspaceand\mathcal{T} \inℒ(\mathcal{V}). Usethepolardecompositiontogiveaproofthat
|det\mathcal{T}|=\sqrtdet(\mathcal{T}∗\mathcal{T})
thatisdifferentfromtheproofgivenearlier(see9.60).
|     |          |     | ℒ(\mathcal{V}). | Defineg∶ |     |          | +x\mathcal{T}).   |          |
| --- | -------- | --- | ----- | -------- | --- | -------- | ------- | -------- |
| 16  | Suppose\mathcal{T} | \in   |       |          | \mathbf{F} \rightarrow | \mathbf{F} byg(x) | = det(\mathcal{I} | Showthat |
g’(0)=tr\mathcal{T}.
Lookforacleansolutiontothisexercise, withoutusingtheexplicitbut
complicatedformulaforthedeterminantofamatrix.
Supposea,b,carepositivenumbers.
| 17  |                   |     |             |                                  |     | Findthevolumeoftheellipsoid |       |      |
| --- | ----------------- | --- | ----------- | -------------------------------- | --- | --------------------------- | ----- | ---- |
|     |                   |     |             |                                  |     | x2 y2                       | z2    |      |
|     |                   |     | {(x,y,z)\in\mathbf{R}3 |                                  | ∶   | +                           | + <1} |      |
|     |                   |     |             |                                  |     | a2 b2                       | c2    |      |
|     | byfindingaset\Omega\subseteq\mathbf{R}3 |     |             | whosevolumeyouknowandanoperator\mathcal{T} |     |                             |       | on\mathbf{R}3 |
suchthat\mathcal{T}(\Omega)equalstheellipsoidabove.
18 Suppose that \mathcal{A} is an invertible square matrix. Prove that Hadamard’s
inequality(9.66)isanequalityifandonlyifeachcolumnof\mathcal{A}isorthogonal
totheothercolumns.
19 Suppose\mathcal{V} isaninnerproductspace,e ,…,e isanorthonormalbasisof\mathcal{V},
|     |                                |     |     |     |     | 1   | n   |     |
| --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | and\mathcal{T} \inℒ(\mathcal{V})isapositiveoperator. |     |     |     |     |     |     |     |
\leq\prodn
|     | (a) Provethatdet\mathcal{T} |     |     |     | \langle\mathcal{T}e ,e | \rangle.  |     |     |
| --- | ----------------- | --- | --- | --- | ------ | --- | --- | --- |
|     |                   |     |     | k=1 | k k    |     |     |     |
$$(b) Provethatif\mathcal{T} isinvertible,thentheinequalityin(a)isanequalityif$$
|     | andonlyife |     | isaneigenvectorof\mathcal{T} |     |     | foreachk | =1,…,n. |     |
| --- | ---------- | --- | ------------------ | --- | --- | -------- | ------- | --- |
k

Section9C Determinants 369
20 Suppose\mathcal{A}isann-by-nmatrix,andsupposecissuchthat|\mathcal{A} |\leqcforall
j,k
j,k \in{1,…,n}. Provethat
|det\mathcal{A}|\leqcnnn/2.
Theformulaforthedeterminantofamatrix(9.46)showsthat|det\mathcal{A}|\leqcnn!.
However,theestimategivenbythisexerciseismuchbetter. Forexample,if
$$c=1andn=100,thencnn!\approx10158,buttheestimategivenbythisexercise$$
isthemuchsmallernumber10100. If nisanintegerpowerof 2,thenthe
inequalityaboveissharpandcannotbeimproved.
21 Supposenisapositiveintegerand\delta∶ \mathbf{C}n,n \rightarrow\mathbf{C} isafunctionsuchthat
\delta(\mathcal{A}\mathcal{B})=\delta(\mathcal{A})\cdot\delta(\mathcal{B})
forall\mathcal{A},\mathcal{B}\in\mathbf{C}n,n and\delta(\mathcal{A})equalstheproductofthediagonalentriesof\mathcal{A}
foreachdiagonalmatrix\mathcal{A}\in\mathbf{C}n,n. Provethat
\delta(\mathcal{A})=det\mathcal{A}
forall\mathcal{A}\in\mathbf{C}n,n.
Recallthat\mathbf{C}n,ndenotesthesetof n-by-nmatriceswithentriesin\mathbf{C}. This
exerciseshowsthatthedeterminantistheuniquefunctiondefinedonsquare
matricesthatismultiplicativeandhasthedesiredbehaviorondiagonal
matrices. This result is analogous to Exercise 10 in Section 8D, which
showsthatthetraceisuniquelydeterminedbyitsalgebraicproperties.
Ifindthatinmyownelementarylectures,Ihave,forpedagogicalreasons,pushed
determinantsmoreandmoreintothebackground. Toooften Ihavehadtheexperiencethat,whilethestudentsacquiredfacilitywiththeformulas,whichareso
usefulinabbreviatinglongexpressions,theyoftenfailedtogainfamiliaritywith
theirmeaning,andskillinmanipulationpreventedthestudentfromgoingintoall
thedetailsofthesubjectandsogainingamastery.
—Elementary Mathematicsfroman Advanced Standpoint: Geometry,Felix Klein

| -------- | --------------------------------- | --- | --- | --- |
| 9D Tensor      | Products      |        |     |     |
| -------------- | ------------- | ------ | --- | --- |
| Tensor Product | of Two Vector | Spaces |     |     |
The motivation for our next topic comes from wanting to form the product of
a vector v \in \mathcal{V} and a vector w \in \mathcal{W}. This product will be denoted by v\otimesw,
pronounced“vtensorw”,andwillbeanelementofsomenewvectorspacecalled
| \mathcal{V}\otimes\mathcal{W}(alsopronounced“\mathcal{V} | tensor\mathcal{W}”). |     |     |     |
| -------------------- | ---------- | --- | --- | --- |
Wealreadyhaveavectorspace\mathcal{V}\times\mathcal{W} (see Section3E),calledtheproductof
\mathcal{V} and\mathcal{W}. However,\mathcal{V}\times\mathcal{W} willnotserveourpurposesherebecauseitdoesnot
provideanaturalwaytomultiplyanelementof\mathcal{V} byanelementof\mathcal{W}. Wewould
likeourtensorproducttosatisfysomeoftheusualpropertiesofmultiplication.
Forexample,wewouldlikethedistributivepropertytobesatisfied,meaningthat
| ifv ,v ,v\in\mathcal{V} | andw ,w ,w\in\mathcal{W},then |          |     |              |
| ----------- | ----------------- | -------- | --- | ------------ |
| 1 2         | 1 2               |          |     |              |
| (v +v )\otimesw=v | \otimesw+v \otimesw           | and v\otimes(w | +w  | )=v\otimesw +v\otimesw . |
| 1 2         | 1 2               |          | 1 2 | 1 2          |
WewouldalsolikescalarmultiplicaToproduce\otimesin TEX,type\otimes.
tiontointeractwellwiththisnewmultiplication,meaningthat
\lambda(v\otimesw)=(\lambdav)\otimesw=v\otimes(\lambdaw)
forall \lambda\in\mathbf{F},v\in\mathcal{V},andw\in\mathcal{W}.
| Furthermore,itwouldbeniceifeachbasisof\mathcal{V} |     |     | whencombinedwitheach |     |
| --------------------------------------- | --- | --- | -------------------- | --- |
basisof\mathcal{W} producedabasisof\mathcal{V}\otimes\mathcal{W}. Specifically,ife ,…,e isabasisof\mathcal{V}
|     |     |     |     | 1 m |
| --- | --- | --- | --- | --- |
and f ,…, f isabasisof\mathcal{W},thenwewouldlikealist(inanyorder)consisting
| 1 n |     |     |     |     |
| --- | --- | --- | --- | --- |
of e \otimes f , as j ranges from 1 to m and k ranges from 1 to n, to be a basis of
j k
\mathcal{V}\otimes\mathcal{W}. Thisimpliesthatdim(\mathcal{V}\otimes\mathcal{W})shouldequal(dim\mathcal{V})(dim\mathcal{W}). Recallthat
| dim(\mathcal{V}\times\mathcal{W})=dim\mathcal{V}+dim\mathcal{W} |     | (see3.92),whichshowsthattheproduct\mathcal{V}\times\mathcal{W} |     |     |
| ------------------ | --- | ------------------------------------- | --- | --- |
willnotserveourpurposeshere.
Toproduceavectorspacewhosedimensionis(dim\mathcal{V})(dim\mathcal{W})inanatural
fashion from \mathcal{V} and \mathcal{W}, we look at the vector space of bilinear functionals, as
definedbelow.
**9.68 定义：** bilinearfunctionalon\mathcal{V}\times\mathcal{W},thevectorspaceℬ(\mathcal{V},\mathcal{W})
• A bilinear functional on \mathcal{V}\times\mathcal{W} is a function \beta∶ \mathcal{V}\times\mathcal{W} \rightarrow \mathbf{F} such that
| v↦\beta(v,w)isalinearfunctionalon\mathcal{V} |             | foreachw\in\mathcal{W} |     | andw↦\beta(v,w) |
| ------------------------------ | ----------- | ---------- | --- | ----------- |
| isalinearfunctionalon\mathcal{W}         | foreachv\in\mathcal{V}. |            |     |             |
• Thevectorspaceofbilinearfunctionalson\mathcal{V}\times\mathcal{W} isdenotedbyℬ(\mathcal{V},\mathcal{W}).
| If\mathcal{W} =\mathcal{V},thenabilinearfunctionalon\mathcal{V}\times\mathcal{W} |     |     | isabilinearform;see9.1. |     |
| ----------------------------------- | --- | --- | ----------------------- | --- |
Theoperationsofadditionandscalarmultiplicationonℬ(\mathcal{V},\mathcal{W})aredefined
tobetheusualoperationsofadditionandscalarmultiplicationoffunctions. As
youcanverify,theseoperationsmakeℬ(\mathcal{V},\mathcal{W})intoavectorspacewhoseadditive
| identityisthezerofunctionfrom\mathcal{V}\times\mathcal{W} |     | to\mathbf{F}. |     |     |
| -------------------------------- | --- | ---- | --- | --- |

| --- | --- | --- | --- | --------- | --- | -------------- | --- |
bilinearfunctionals
**9.69 例：** Define\beta∶
| • Suppose\phi\in\mathcal{V}′ |     | and\tau | \in\mathcal{W}′. |     | \mathcal{V}\times\mathcal{W} \rightarrow\mathbf{F} | by\beta(v,w)=\phi(v)\tau(w). |     |
| ------------- | --- | ---- | ---- | --- | ------ | ------------------ | --- |
Then\betaisabilinearfunctionalon\mathcal{V}\times\mathcal{W}.
Define\beta∶
| • Supposev\in\mathcal{V} |     | andw\in\mathcal{W}. |     |     | \mathcal{V}′\times\mathcal{W}′ \rightarrow\mathbf{F} | by\beta(\phi,\tau)=\phi(v)\tau(w). |     |
| ------------ | --- | ------- | --- | --- | -------- | ------------------ | --- |
Then\betaisabilinearfunctionalon\mathcal{V}′\times\mathcal{W}′.
Define\beta∶
| •   | \mathcal{V}\times\mathcal{V}′ | \rightarrow   | \mathbf{F} by\beta(v,\phi) | = \phi(v). | Then\betaisabilinearfunctionalon |     |     |
| --- | ---- | --- | ---------- | ------- | ---------------------------- | --- | --- |
\mathcal{V}\times\mathcal{V}′.
Define\beta∶
| • Suppose\phi |     | \in \mathcal{V}′. | \mathcal{V}\timesℒ(\mathcal{V}) |     | \rightarrow \mathbf{F} by\beta(v,\mathcal{T}) |     | = \phi(\mathcal{T}v). Then\betaisa |
| ---------- | --- | ----- | ------ | --- | ------------ | --- | ----------------- |
bilinearfunctionalon\mathcal{V}\timesℒ(\mathcal{V}).
Define\beta∶
| • Supposemandnarepositiveintegers. |                                        |     |     |     | \mathbf{F}m,n\times\mathbf{F}n,m |     | \rightarrow\mathbf{F}by\beta(\mathcal{A},\mathcal{B})= |
| ---------------------------------- | -------------------------------------- | --- | --- | --- | --------- | --- | ----------- |
| tr(\mathcal{A}\mathcal{B}).                            | Then\betaisabilinearfunctionalon\mathbf{F}m,n\times\mathbf{F}n,m. |     |     |     |           |     |             |
9.70 dimensionofthevectorspaceofbilinearfunctionals
dimℬ(\mathcal{V},\mathcal{W})=(dim\mathcal{V})(dim\mathcal{W}).
Proof Lete ,…,e beabasisof\mathcal{V} and f ,…, f beabasisof\mathcal{W}. Forabilinear
|     | 1   | m   |     |     | 1 n |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
functional\beta \in ℬ(\mathcal{V},\mathcal{W}),letℳ(\beta)bethem-by-nmatrixwhoseentryinrowj,
| columnkis\beta(e, |     | f ). | Themap\beta↦ℳ(\beta)isalinearmapofℬ(\mathcal{V},\mathcal{W})into\mathbf{F}m,n. |     |     |     |     |
| ------------- | --- | ---- | ----------------------------------------- | --- | --- | --- | --- |
j k
\in\mathbf{F}m,n,defineabilinearfunctional\beta
| Foramatrix\mathcal{C} |     |     |     |     |     | on\mathcal{V}\times\mathcal{W} | by  |
| ----------- | --- | --- | --- | --- | --- | ----- | --- |
\mathcal{C}
|     |     |           |       |        |      | n   | m       |
| --- | --- | --------- | ----- | ------ | ---- | --- | ------- |
|     | \beta   | (a e +⋯+a | e ,b  | f +⋯+b | f )= | \sum \sum | \mathcal{C} ab    |
|     | \mathcal{C}   | 1 1       | m m 1 | 1      | n n  |     | j,k j k |
$$k=1j=1$$
| fora ,…,a | ,b  | ,…,b | \in\mathbf{F}. |     |     |     |     |
| --------- | --- | ---- | --- | --- | --- | --- | --- |
| 1         | m   | 1    | n   |     |     |     |     |
Thelinearmap\beta↦ℳ(\beta)fromℬ(\mathcal{V},\mathcal{W})to\mathbf{F}m,nandthelinearmap\mathcal{C}
↦\beta
\mathcal{C}
from \mathbf{F}m,n to ℬ(\mathcal{V},\mathcal{W}) are inverses of each other because \beta = \beta for all
ℳ(\beta)
\in\mathbf{F}m,n,asyoushouldverify.
| \beta\inℬ(\mathcal{V},\mathcal{W})andℳ(\beta |     |     | )=\mathcal{C}forall\mathcal{C} |     |     |     |     |
| -------------- | --- | --- | ---------- | --- | --- | --- | --- |
\mathcal{C}
Thusbothmapsareisomorphismsandthetwospacesthattheyconnecthavethe
Hencedimℬ(\mathcal{V},\mathcal{W})=dim\mathbf{F}m,n
| samedimension. |     |     |     |     | =mn=(dim\mathcal{V})(dim\mathcal{W}). |     |     |
| -------------- | --- | --- | --- | --- | ----------------- | --- | --- |
Severaldifferentdefinitionsof\mathcal{V}\otimes\mathcal{W} appearinthemathematicalliterature.
Thesedefinitionsareequivalenttoeachother,atleastinthefinite-dimensional
context,becauseanytwovectorspacesofthesamedimensionareisomorphic.
Theresultabovestatesthatℬ(\mathcal{V},\mathcal{W})hasthedimensionthatweseek,asdo
ℒ(\mathcal{V},\mathcal{W})and\mathbf{F}dim\mathcal{V},dim\mathcal{W}.
Thusitmaybetemptingtodefine\mathcal{V}\otimes\mathcal{W}tobeℬ(\mathcal{V},\mathcal{W})
orℒ(\mathcal{V},\mathcal{W})or\mathbf{F}dim\mathcal{V},dim\mathcal{W}. However,noneofthosedefinitionswouldleadtoa
| basis-freedefinitionofv\otimeswforv\in\mathcal{V} |     |     |     | andw\in\mathcal{W}. |     |     |     |
| ------------------------------- | --- | --- | --- | ------- | --- | --- | --- |
Thefollowingdefinition,whileitmayseemabitstrangeandabstractatfirst,
hasthehugeadvantagethatitdefinesv\otimeswinabasis-freefashion. Wedefine
\mathcal{V}\otimes\mathcal{W} tobethevectorspaceofbilinearfunctionalson\mathcal{V}′\times\mathcal{W}′ insteadofthe
moretemptingchoiceofthevectorspaceofbilinearfunctionalson\mathcal{V}\times\mathcal{W}.

| -------- | --- | --------------------------------- | --- | --- | --- |
tensorproduct,\mathcal{V}\otimes\mathcal{W},v\otimesw
**9.71 定义：** | Thetensorproduct |     |                         | isdefinedtobeℬ(\mathcal{V}′,\mathcal{W}′). |                      |     |
| ---------------- | --- | ----------------------- | ---------------------- | -------------------- | --- |
| •                |     | \mathcal{V}\otimes\mathcal{W}                     |                        |                      |     |
| • Forv\in\mathcal{V}         |     | andw\in\mathcal{W},thetensorproduct |                        | v\otimeswistheelementof\mathcal{V}\otimes\mathcal{W} |     |
definedby
$$(v\otimesw)(\phi,\tau)=\phi(v)\tau(w)$$
forall(\phi,\tau)\in\mathcal{V}′\times\mathcal{W}′.
Wecanquicklyprovethatthedefinitionof\mathcal{V}\otimes\mathcal{W}givesitthedesireddimension.
dimensionofthetensorproductoftwovectorspaces
9.72
dim(\mathcal{V}\otimes\mathcal{W})=(dim\mathcal{V})(dim\mathcal{W}).
Proof Becauseavectorspaceanditsdualhavethesamedimension(by3.111),
we have dim\mathcal{V}′ = dim\mathcal{V} and dim\mathcal{W}′ = dim\mathcal{W}. Thus 9.70 tells us that the
dimensionofℬ(\mathcal{V}′,\mathcal{W}′)equals(dim\mathcal{V})(dim\mathcal{W}).
Tounderstandthedefinitionofthetensorproductv\otimeswoftwovectorsv\in\mathcal{V}
andw\in\mathcal{W},focusonthekindofobjectitis. Anelementof\mathcal{V}\otimes\mathcal{W} isabilinear
functionalon\mathcal{V}′\times\mathcal{W}′,andinparticularitisafunctionfrom\mathcal{V}′\times\mathcal{W}′to\mathbf{F}. Thusfor
eachelementof\mathcal{V}′\times\mathcal{W}′,itshouldproduceanelementof\mathbf{F}.
Thedefinitionabove
hasthisbehavior,becausev\otimeswappliedtoatypicalelement(\phi,\tau)of\mathcal{V}′\times\mathcal{W}′
producesthenumber\phi(v)\tau(w).
Thesomewhatabstractnatureofv\otimeswshouldnotmatter. Theimportantpoint
isthebehavioroftheseobjects. Thenextresultshowsthattensorproductsof
vectorshavethedesiredbilinearityproperties.
9.73 bilinearityoftensorproduct
| Supposev,v |       | ,v andw,w | ,w     | and \lambda\in\mathbf{F}. Then |      |
| ---------- | ----- | --------- | ------ | ------------- | ---- |
|            | 1     | 2 \in\mathcal{V}      | 1 2 \in\mathcal{W} |               |      |
| (v +v      | )\otimesw=v | \otimesw+v      | \otimesw and | v\otimes(w +w )=v\otimesw | +v\otimesw |
| 1 2        |       | 1         | 2      | 1 2           | 1 2  |
and
\lambda(v\otimesw)=(\lambdav)\otimesw=v\otimes(\lambdaw).
| Proof Suppose(\phi,\tau)\in\mathcal{V}′\times\mathcal{W}′. |          |                  | Then            |           |     |
| ------------------------- | -------- | ---------------- | --------------- | --------- | --- |
|                           | ((v      | +v )\otimesw)(\phi,\tau)=\phi(v | +v              | )\tau(w)     |     |
|                           | 1        | 2                | 1               | 2         |     |
|                           |          |                  | =\phi(v )\tau(w)+\phi(v  | )\tau(w)     |     |
|                           |          |                  | =(v \otimesw)(\phi,\tau)+(v | \otimesw)(\phi,\tau)  |     |
|                           |          |                  | =(v \otimesw+v        | \otimesw)(\phi,\tau). |     |
| Thus(v                    | +v )\otimesw=v | \otimesw+v             | \otimesw.             |           |     |
| 1                         | 2        | 1                | 2               |           |     |
Theothertwoequalitiesareprovedsimilarly.

| --- | --- | --- | --------- | -------------- | --- |
Listsare, bydefinition, ordered. Theordermatterswhen, forexample, we
formthematrixofanoperatorwithrespecttoabasis. Forlistsinthissection
| withtwoindices,suchas{e |     | \otimes f } | inthenextresult,theordering |     |     |
| ----------------------- | --- | ----- | --------------------------- | --- | --- |
j k j=1,…,m;k=1,…,n
doesnotmatterandwedonotspecifyit—justchooseanyconvenientordering.
The linear independence of elements of \mathcal{V}\otimes \mathcal{W} in (a) of the result below
capturestheideathattherearenorelationshipsamongvectorsin\mathcal{V}\otimes\mathcal{W} other
thantherelationshipsthatcomefrombilinearityofthetensorproduct(see9.73)
andtherelationshipsthatmaybepresentduetolineardependenceofalistof
| vectorsin\mathcal{V}   | oralistofvectorsin\mathcal{W}. |     |     |     |     |
| ------------ | -------------------- | --- | --- | --- | --- |
| 9.74 basisof | \mathcal{V}\otimes\mathcal{W}                  |     |     |     |     |
Suppose e ,…,e is a list of vectors in \mathcal{V} and f ,…, f is a list of vectors
|     | 1 m |     | 1   | n   |     |
| --- | --- | --- | --- | --- | --- |
in\mathcal{W}.
$$(a) Ife ,…,e and f ,…, f arebothlinearlyindependentlists,then$$
| 1   | m 1 | n      |                   |     |     |
| --- | --- | ------ | ----------------- | --- | --- |
|     |     | {e \otimes f | } j=1,…,m;k=1,…,n |     |     |
j k
isalinearlyindependentlistin\mathcal{V}\otimes\mathcal{W}.
$$(b) If e ,…,e is a basis of \mathcal{V} and f ,…, f is a basis of \mathcal{W}, then the list$$
| 1    | m                 |                | 1 n |     |     |
| ---- | ----------------- | -------------- | --- | --- | --- |
| {e \otimes | f }               | isabasisof\mathcal{V}\otimes\mathcal{W}. |     |     |     |
| j    | k j=1,…,m;k=1,…,n |                |     |     |     |
Proof Toprove(a),supposee ,…,e and f ,…, f arebothlinearlyindependent
|     |     | 1 m | 1 n |     |     |
| --- | --- | --- | --- | --- | --- |
lists. Thislinearindependenceandthelinearmaplemma(3.4)implythatthere
| exist\phi ,…,\phi | \in\mathcal{V}′ and\tau | ,…,\tau \in\mathcal{W}′ | suchthat   |              |     |
| ----------- | -------- | -------- | ---------- | ------------ | --- |
| 1           | m        | 1 n      |            |              |     |
|             | ⎧        |          |            | ⎧            |     |
|             | {1       | ifj =k,  |            | {1 ifj =k,   |     |
|             | \phi(e )=   |          | and \tau(f )= |              |     |
|             | j k ⎨    |          | j k        | ⎨            |     |
|             | {0 ⎩     | ifj \neqk   |            | {0 ⎩ ifj \neqk, |     |
where j,k \in {1,…,m} in the first equation and j,k \in {1,…,n} in the second
equation.
| Suppose{a | }   | isalistofscalarssuchthat |     |     |     |
| --------- | --- | ------------------------ | --- | --- | --- |
j,k j=1,…,m;k=1,…,n
n m
| 9.75 |     | \sum \sum a | (e \otimes f )=0. |     |     |
| ---- | --- | ----- | ----------- | --- | --- |
|      |     | j,k   | j k         |     |     |
$$k=1j=1$$
Notethat(e \otimes f )(\phi ,\tau )equals1ifj =\mathcal{M}andk =\mathcal{N},andequals0otherwise.
j k \mathcal{M} \mathcal{N}
Thusapplyingbothsidesof9.75to(\phi ,\tau )showsthata =0,provingthat
|          |                        |     | \mathcal{M} \mathcal{N} | \mathcal{M},\mathcal{N} |     |
| -------- | ---------------------- | --- | --- | --- | --- |
| {e \otimes f } | islinearlyindependent. |     |     |     |     |
j k j=1,…,m;k=1,…,n
| Now(b)followsfrom(a),theequationdim\mathcal{V}\otimes\mathcal{W} |     |     |     | = (dim\mathcal{V})(dim\mathcal{W})[see |     |
| -------------------------------------- | --- | --- | --- | ------------------ | --- |
9.72],andtheresultthatalinearlyindependentlistoftherightlengthisabasis
$$(see2.38).$$
| Everyelementof\mathcal{V}\otimes\mathcal{W}                          |                           | isafinitesumofelementsoftheformv\otimesw,where |     |                |     |
| ------------------------------------------ | ------------------------- | ---------------------------------------- | --- | -------------- | --- |
| v\in\mathcal{V} andw\in\mathcal{W},asimpliedby(b)intheresultabove. |                           |                                          |     | However,ifdim\mathcal{V} | >1  |
| anddim\mathcal{W}                                    | >1,then Exercise4showsthat |                                          |     |                |     |
{v\otimesw∶(v,w)\in\mathcal{V}\times\mathcal{W}}\neq\mathcal{V}\otimes\mathcal{W}.

374 Chapter 9 Multilinear Algebraand Determinants
**9.76 例：** tensorproductofelementof \mathbf{F}m withelementof \mathbf{F}n
Supposemandnarepositiveintegers. Lete ,…,e denotethestandardbasis
1 m
of\mathbf{F}m andlet f ,…, f denotethestandardbasisof\mathbf{F}n. Suppose
1 n
$$v=(v ,…,v )\in\mathbf{F}m and w=(w ,…,w )\in\mathbf{F}n.$$
1 m 1 n
Then
m n
v\otimesw=(\sum ve)\otimes(\sumw f )
j j k k
$$j=1 k=1$$
n m
= \sum \sum(vw )(e \otimes f ).
j k j k
$$k=1j=1$$
Thus with respect to the basis {e \otimes f } of \mathbf{F}m \otimes\mathbf{F}n provided by
j k j=1,…,m;k=1,…,n
9.74(b),thecoefficientsofv\otimeswarethenumbers{vw } . Ifinstead
j k j=1,…,m;k=1,…,n
ofwritingthesenumbersinalist,wewritetheminanm-by-nmatrixwithvw
j k
inrowj,columnk,thenwecanidentifyv\otimeswwiththem-by-nmatrix
v w ⋯ v w
⎛ 1 1 1 n ⎞
⎜ ⎟
⎜ ⎟
⎜ ⎜ ⋱ ⎟ ⎟.
⎜ ⎟
⎜ ⎟
⎝ v w ⋯ v w ⎠
m 1 m n
See Exercises5and6forpracticeinusingtheidentificationfromtheexample
above.
Wenowdefinebilinearmaps,whichdifferfrombilinearfunctionalsinthat
thetargetspacecanbeanarbitraryvectorspaceratherthanjustthescalarfield.
**9.77 定义：** bilinearmap
Abilinearmapfrom\mathcal{V}\times\mathcal{W} toavectorspace\mathcal{U} isafunctionΓ∶ \mathcal{V}\times\mathcal{W} \rightarrow\mathcal{U}
such that v ↦ Γ(v,w) is a linear map from \mathcal{V} to \mathcal{U} for each w \in \mathcal{W} and
w↦Γ(v,w)isalinearmapfrom\mathcal{W} to\mathcal{U} foreachv\in\mathcal{V}.
**9.78 例：** bilinearmaps
• Everybilinearfunctionalon\mathcal{V}\times\mathcal{W} isabilinearmapfrom\mathcal{V}\times\mathcal{W} to\mathbf{F}.
• ThefunctionΓ∶ \mathcal{V}\times\mathcal{W} \rightarrow\mathcal{V}\otimes\mathcal{W} definedbyΓ(v,w)=v\otimeswisabilinearmap
from\mathcal{V}\times\mathcal{W} to\mathcal{V}\otimes\mathcal{W} (by9.73).
• ThefunctionΓ∶ ℒ(\mathcal{V})\timesℒ(\mathcal{V})\rightarrowℒ(\mathcal{V})definedbyΓ(\mathcal{S},\mathcal{T})=\mathcal{S}\mathcal{T} isabilinear
mapfromℒ(\mathcal{V})\timesℒ(\mathcal{V})toℒ(\mathcal{V}).
• ThefunctionΓ∶ \mathcal{V}\timesℒ(\mathcal{V},\mathcal{W})\rightarrow\mathcal{W} definedbyΓ(v,\mathcal{T})=\mathcal{T}visabilinearmap
from\mathcal{V}\timesℒ(\mathcal{V},\mathcal{W})to\mathcal{W}.

| --- | --- | --- | --- | --------- | -------------- | --- |
Tensorproductsallowustoconvertbilinearmapson\mathcal{V}\times\mathcal{W}intolinearmapson
\mathcal{V}\otimes\mathcal{W}(andviceversa),asshownbythenextresult. Inthemathematicalliterature,
$$(a)oftheresultbelowiscalledthe“universalproperty”oftensorproducts.$$
convertingbilinearmapstolinearmaps
9.79
| Suppose\mathcal{U} | isavectorspace. |     |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- | --- |
SupposeΓ∶
| (a)        |     | \mathcal{V}\times\mathcal{W}    | \rightarrow \mathcal{U} | isabilinearmap. | Thenthereexistsaunique |     |
| ---------- | --- | ------ | --- | --------------- | ---------------------- | --- |
| linearmapΓ |     | ̂∶ \mathcal{V}\otimes\mathcal{W} | \rightarrow\mathcal{U}  | suchthat        |                        |     |
̂ (v\otimesw)=Γ(v,w)
Γ
forall(v,w)\in\mathcal{V}\times\mathcal{W}.
$$(b) Conversely,suppose\mathcal{T}∶ \mathcal{V}\otimes\mathcal{W} \rightarrow\mathcal{U} isalinearmap. Thenthereexistsa$$
uniquebilinearmap\mathcal{T}#∶
|     |     |     |     | \mathcal{V}\times\mathcal{W} \rightarrow\mathcal{U} | suchthat |     |
| --- | --- | --- | --- | ------ | -------- | --- |
\mathcal{T}#(v,w)=\mathcal{T}(v\otimesw)
forall(v,w)\in\mathcal{V}\times\mathcal{W}.
Proof Lete ,…,e beabasisof\mathcal{V}andlet f ,…, f beabasisof\mathcal{W}. Bythelinear
|     | 1   | m   |     |     | 1 n |     |
| --- | --- | --- | --- | --- | --- | --- |
̂∶
| maplemma(3.4)and9.74(b),thereexistsauniquelinearmapΓ |     |     |     |     |     | \mathcal{V}\otimes\mathcal{W} \rightarrow\mathcal{U} |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ------ |
suchthat
̂
|                      |     |           | Γ         | (e \otimes f )=Γ(e, | f )          |          |
| -------------------- | --- | --------- | --------- | ------------- | ------------ | -------- |
|                      |     |           |           | j k           | j k          |          |
| forallj \in{1,…,m}andk |     |           | \in{1,…,n}. |               |              |          |
| Nowsuppose(v,w)\in\mathcal{V}\times\mathcal{W}. |     |           |           | Thereexista   | ,…,a ,b ,…,b | suchthat |
|                      |     |           |           |               | 1 m 1 n      | \in\mathbf{F}       |
| v=a e +⋯+a           |     | e andw=b  |           | f +⋯+b        | f . Thus     |          |
| 1 1                  |     | m m       |           | 1 1           | n n          |          |
|                      |     |           |           | n m           |              |          |
|                      |     | ̂         |           | ̂(\sum           |              |          |
|                      |     | Γ (v\otimesw)=Γ |           | \sum(ab          | )(e \otimes f ))   |          |
j k j k
$$k=1j=1$$
|     |     |     |     | n m |     |     |
| --- | --- | --- | --- | --- | --- | --- |
̂
|     |     |     |     | = \sum \sum ab | Γ(e \otimes f ) |     |
| --- | --- | --- | --- | -------- | --------- | --- |
|     |     |     |     |          | j k j k   |     |
$$k=1j=1$$
|     |     |     |     | n m      |          |     |
| --- | --- | --- | --- | -------- | -------- | --- |
|     |     |     |     | = \sum \sum ab | Γ(e, f ) |     |
|     |     |     |     |          | j k j k  |     |
$$k=1j=1$$
=Γ(v,w),
asdesired,wherethesecondlineholdsbecauseΓ ̂islinear,thethirdlineholdsby
̂,andthefourthlineholdsbecauseΓisbilinear.
thedefinitionofΓ
TheuniquenessofthelinearmapΓ ̂ satisfyingΓ ̂ (v\otimesw) = Γ(v,w)follows
from9.74(b),completingtheproofof(a).
To prove (b), define a function \mathcal{T}#∶ \mathcal{V}\times\mathcal{W} \rightarrow \mathcal{U} by \mathcal{T}#(v,w) = \mathcal{T}(v\otimesw)
forall(v,w)\in\mathcal{V}\times\mathcal{W}. Thebilinearityofthetensorproduct(see9.73)andthe
| linearityof\mathcal{T} | implythat\mathcal{T}# |     | isbilinear. |     |     |     |
| ------------ | ----------- | --- | ----------- | --- | --- | --- |
Clearlythechoiceof\mathcal{T}#
thatsatisfiestheconditionsisunique.

376 Chapter 9 Multilinear Algebraand Determinants
Toprove9.79(a),wecouldnotjustdefineΓ ̂ (v\otimesw)=Γ(v,w)forallv\in\mathcal{V}
andw \in \mathcal{W} (andthenextendΓ ̂ linearlytoallof\mathcal{V}\otimes\mathcal{W})becauseelementsof
\mathcal{V}\otimes\mathcal{W} donothaveuniquerepresentationsasfinitesumsofelementsoftheform
v\otimesw. Ourproofusedabasisof\mathcal{V} andabasisof\mathcal{W} togetaroundthisproblem.
AlthoughourconstructionofΓ ̂ intheproofof9.79(a)dependedonabasis
of\mathcal{V} andabasisof\mathcal{W},theequationΓ ̂ (v\otimesw)=Γ(v,w)thatholdsforallv\in\mathcal{V}
andw\in\mathcal{W}showsthatΓ ̂doesnotdependonthechoiceofbasesfor\mathcal{V} and\mathcal{W}.
Tensor Product of Inner Product Spaces
Theresultbelowfeaturesthreeinnerproducts—oneon\mathcal{V}\otimes\mathcal{W},oneon\mathcal{V},andone
on\mathcal{W},althoughweusethesamesymbol\langle\cdot,\cdot\rangleforallthreeinnerproducts.
9.80 innerproductontensorproductoftwoinnerproductspaces
Suppose \mathcal{V} and \mathcal{W} are inner product spaces. Then there is a unique inner
producton\mathcal{V}\otimes\mathcal{W} suchthat
\langlev\otimesw,u\otimesx\rangle=\langlev,u\rangle\langlew,x\rangle
forallv,u\in\mathcal{V} andw,x \in\mathcal{W}.
Proof Supposee ,…,e isanorthonormalbasisof\mathcal{V} and f ,…, f isanortho1 m 1 n
normalbasisof\mathcal{W}. Defineaninnerproducton\mathcal{V}\otimes\mathcal{W} by
n m n m n m
9.81 \langle\sum \sum b j,k e j \otimes f k ,\sum \sum c j,k e j \otimes f k \rangle= \sum \sum b j,k c j,k .
$$k=1j=1 k=1j=1 k=1j=1$$
Thestraightforwardverificationthat9.81definesaninnerproducton\mathcal{V}\otimes\mathcal{W}
islefttothereader[use9.74(b)].
Suppose that v,u \in \mathcal{V} and w,x \in \mathcal{W}. Let v ,…,v \in \mathbf{F} be such that
1 m
$$v=v e +⋯+v e ,withsimilarexpressionsforu,w,andx. Then$$
1 1 m m
m n m n
\langlev\otimesw,u\otimesx\rangle=\langle\sum ve \otimes \sumw f , \sum ue \otimes \sumx f \rangle
j j k k j j k k
$$j=1 k=1 j=1 k=1$$
n m n m
=\langle\sum \sum vw e \otimes f ,\sum \sum ux e \otimes f \rangle
j k j k j k j k
$$k=1j=1 k=1j=1$$
n m
= \sum \sum vuw x
j j k k
$$k=1j=1$$
m n
=(\sum vu)(\sumw x )
j j k k
$$j=1 k=1$$
=\langlev,u\rangle\langlew,x\rangle.
Thereisonlyoneinnerproducton\mathcal{V}\otimes\mathcal{W}suchthat\langlev\otimesw,u\otimesx\rangle=\langlev,u\rangle\langlew,x\rangle
forallv,u\in\mathcal{V} andw,x \in\mathcal{W} becauseeveryelementof\mathcal{V}\otimes\mathcal{W} canbewrittenas
alinearcombinationofelementsoftheformv\otimesw[by9.74(b)].

| --- | --- | --- | --------- | --- | -------------- | --- | --- |
Thedefinitionbelowofanaturalinnerproducton\mathcal{V}\otimes\mathcal{W} isnowjustifiedby
9.80. Wecouldnothavesimplydefined\langlev\otimesw,u\otimesx\rangletobe\langlev,u\rangle\langlew,x\rangle(andthen
usedadditivityineachslotseparatelytoextendthedefinitionto\mathcal{V}\otimes\mathcal{W})without
someproofbecauseelementsof\mathcal{V}\otimes\mathcal{W} donothaveuniquerepresentationsas
finitesumsofelementsoftheformv\otimesw.
innerproductontensorproductoftwoinnerproductspaces
**9.82 定义：** | Suppose\mathcal{V}                                 | and\mathcal{W} | areinnerproductspaces. |     | Theinnerproducton\mathcal{V}\otimes\mathcal{W} |          |     | is  |
| ---------------------------------------- | ---- | ---------------------- | --- | -------------------- | -------- | --- | --- |
| theuniquefunction\langle\cdot,\cdot\ranglefrom(\mathcal{V}\otimes\mathcal{W})\times(\mathcal{V}\otimes\mathcal{W})to\mathbf{F} |      |                        |     |                      | suchthat |     |     |
\langlev\otimesw,u\otimesx\rangle=\langlev,u\rangle\langlew,x\rangle
| forallv,u\in\mathcal{V} |     | andw,x \in\mathcal{W}. |     |     |     |     |     |
| ----------- | --- | ---------- | --- | --- | --- | --- | --- |
Takeu = v andx = w intheequationaboveandthentakesquarerootsto
showthat
‖v\otimesw‖=‖v‖‖w‖
| forallv\in\mathcal{V} | andallw\in\mathcal{W}. |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- |
Theconstruction of the inner product in the proof of 9.80 depended onan
orthonormalbasise ,…,e of\mathcal{V} andanorthonormalbasis f ,…, f of\mathcal{W}. For-
|                       |     | 1 m |                   |                             | 1   | n   |     |
| --------------------- | --- | --- | ----------------- | --------------------------- | --- | --- | --- |
| mula9.81impliesthat{e |     | \otimes   | f }               | isadoublyindexedorthonormal |     |     |     |
|                       |     | j   | k j=1,…,m;k=1,…,n |                             |     |     |     |
list in \mathcal{V}\otimes\mathcal{W} and hence is an orthonormal basis of \mathcal{V}\otimes\mathcal{W} [by 9.74(b)]. The
importanceofthenextresultarisesbecausetheorthonormalbasesusedtherecan
bedifferentfromtheorthonormalbasesusedtodefinetheinnerproductin9.80.
Althoughthenotationforthebasesisthesameintheproofof9.80andinthe
resultbelow,thinkofthemastwodifferentsetsoforthonormalbases.
| 9.83 | orthonormalbasisof |     | \mathcal{V}\otimes\mathcal{W} |     |     |     |     |
| ---- | ------------------ | --- | --- | --- | --- | --- | --- |
Suppose\mathcal{V} and\mathcal{W} areinnerproductspaces,ande ,…,e isanorthonormal
|          |     |                              |     | 1   | m    |     |     |
| -------- | --- | ---------------------------- | --- | --- | ---- | --- | --- |
| basisof\mathcal{V} | and | ,…, isanorthonormalbasisof\mathcal{W}. |     |     | Then |     |     |
|          |     | f 1 f n                      |     |     |      |     |     |
{e \otimes f }
j k j=1,…,m;k=1,…,n
isanorthonormalbasisof\mathcal{V}\otimes\mathcal{W}.
|       | Weknowthat{e | \otimes f | }                 | isabasisof\mathcal{V}\otimes\mathcal{W} |     | [by9.74(b)]. |     |
| ----- | ------------ | --- | ----------------- | ------------- | --- | ------------ | --- |
| Proof |              | j   | k j=1,…,m;k=1,…,n |               |     |              |     |
Thusweonlyneedtoverifyorthonormality. Todothis,supposej,\mathcal{M} \in{1,…,m}
| andk,\mathcal{N} | \in{1,…,n}. | Then |     |     |     |     |     |
| ------ | --------- | ---- | --- | --- | --- | --- | --- |
|        |           |      |     | ⎧   |     | =\mathcal{N}, |     |
{1 ifj =\mathcal{M}andk
|     | \langlee \otimes f | ,e \otimes f \rangle=\langlee,e | \rangle\langlef , f | \rangle=   |     |     |     |
| --- | ------ | ------------- | ------- | ---- | --- | --- | --- |
|     | j k    | \mathcal{M} \mathcal{N}           | j \mathcal{M} k \mathcal{N} | ⎨ {0 |     |     |     |
⎩ otherwise.
| Hencethedoublyindexedlist{e |     |     | \otimes f } |     | isindeedanorthonormal |     |     |
| --------------------------- | --- | --- | ----- | --- | --------------------- | --- | --- |
j k j=1,…,m;k=1,…,n
basisof\mathcal{V}\otimes\mathcal{W}.
See Exercise11foranexampleofhowtheinnerproductstructureon\mathcal{V}\otimes\mathcal{W}
| interactswithoperatorson\mathcal{V} |     |     | and\mathcal{W}. |     |     |     |     |
| ------------------------- | --- | --- | ----- | --- | --- | --- | --- |

378 Chapter 9 Multilinear Algebraand Determinants
Tensor Product of Multiple Vector Spaces
Wehavebeendiscussingpropertiesofthetensorproductoftwofinite-dimensional
vectorspaces. Nowweturnourattentiontothetensorproductofmultiplefinitedimensionalvectorspaces. Thisgeneralizationrequiresnonewideas,onlysome
slightlymorecomplicatednotation. Readerswithagoodunderstandingofthe
tensorproductoftwovectorspacesshouldbeabletomaketheextensiontothe
tensorproductofmorethantwovectorspaces.
Thusinthissubsection,noproofswillbeprovided. Thedefinitionsandthe
statementsofresultsthatwillbeprovidedshouldbeenoughinformationtoenable
readerstofillinthedetails,usingwhathasalreadybeenlearnedaboutthetensor
productoftwovectorspaces.
Webeginwiththefollowingnotationalassumption.
**9.84 记号：** \mathcal{V} ,…,\mathcal{V}
1 m
For the rest of this subsection, m denotes an integer greater than 1 and
\mathcal{V} ,…,\mathcal{V} denotefinite-dimensionalvectorspaces.
1 m
Thenotionofanm-linearfunctional,whichweareabouttodefine,generalizes
the notion of a bilinear functional (see 9.68). Recall that the use of the word
“functional”indicatesthatwearemappingintothescalarfield\mathbf{F}. Recallalsothat
theterminology“m-linearform”isusedinthespecialcase\mathcal{V} =⋯=\mathcal{V} (see
1 m
9.25). Thenotationℬ(\mathcal{V} ,…,\mathcal{V} )generalizesourpreviousnotationℬ(\mathcal{V},\mathcal{W}).
1 m
**9.85 定义：** m-linearfunctional,thevectorspaceℬ(\mathcal{V} ,…,\mathcal{V} )
1 m
• Anm-linearfunctionalon\mathcal{V} \times⋯\times\mathcal{V} isafunction\beta∶ \mathcal{V} \times⋯\times\mathcal{V} \rightarrow\mathbf{F}
1 m 1 m
thatisalinearfunctionalineachslotwhentheotherslotsareheldfixed.
• The vector space of m-linear functionals on \mathcal{V} \times⋯\times\mathcal{V} is denoted by
1 m
ℬ(\mathcal{V} ,…,\mathcal{V} ).
1 m
**9.86 例：** m-linearfunctional
Suppose\phi \in\mathcal{V} ′ foreachk \in{1,…,m}. Define\beta∶ \mathcal{V} \times⋯\times\mathcal{V} \rightarrow\mathbf{F} by
k k 1 m
\beta(v ,…,v )=\phi (v )\times⋯\times\phi (v ).
1 m 1 1 m m
Then\betaisanm-linearfunctionalon\mathcal{V} \times⋯\times\mathcal{V} .
1 m
Thenextresultcanbeprovedbyimitatingtheproofof9.70.
9.87 dimensionofthevectorspaceofm-linearfunctionals
dimℬ(\mathcal{V} ,…,\mathcal{V} )=(dim\mathcal{V} )\times⋯\times(dim\mathcal{V} ).
1 m 1 m

Section9D Tensor Products 379
Nowwecandefinethetensorproductofmultiplevectorspacesandthetensor
productofelementsofthosevectorspaces. Thefollowingdefinitioniscompletely
analogoustoourpreviousdefinition(9.71)inthecasem=2.
**9.88 定义：** tensorproduct,\mathcal{V} \otimes⋯\otimes\mathcal{V} ,v \otimes⋯\otimesv
1 m 1 m
• Thetensorproduct \mathcal{V} \otimes⋯\otimes\mathcal{V} isdefinedtobeℬ(\mathcal{V}′,…,\mathcal{V} ′).
1 m 1 m
• Forv \in\mathcal{V} ,…,v \in\mathcal{V} ,thetensorproduct v \otimes⋯\otimesv istheelement
1 1 m m 1 m
of\mathcal{V} \otimes⋯\otimes\mathcal{V} definedby
1 m
$$(v \otimes⋯\otimesv )(\phi ,…,\phi )=\phi (v )⋯\phi (v )$$
1 m 1 m 1 1 m m
forall(\phi ,…,\phi )\in\mathcal{V}′\times⋯\times\mathcal{V} ′.
1 m 1 m
The next result can be proved by following the pattern of the proof of the
analogousresultwhenm=2(see9.72).
9.89 dimensionofthetensorproduct
dim(\mathcal{V} \otimes⋯\otimes\mathcal{V} )=(dim\mathcal{V} )⋯(dim\mathcal{V} ).
1 m 1 m
Ournextresultgeneralizes9.74.
9.90 basisof \mathcal{V} \otimes⋯\otimes\mathcal{V}
1 m
Supposedim\mathcal{V} =n andek,…,ek isabasisof\mathcal{V} fork =1,…,m. Then
k k 1 n k k
{e1 \otimes⋯\otimesem}
j 1 j m j 1 =1,…,n 1 ;⋯;j m =1,…,n m
isabasisof\mathcal{V} \otimes⋯\otimes\mathcal{V} .
1 m
Supposem=2ande1,…,e1 isabasisof\mathcal{V} ande2,…,e2 isabasisof\mathcal{V} .
1 n 1 1 1 n 2 2
Thenwithrespecttothebasis{e1 \otimese2} intheresultabove,the
j 1 j 2 j 1 =1,…,n 1 ;j 2 =1,…,n 2
coefficientsofanelementof\mathcal{V} \otimes\mathcal{V} canberepresentedbyann -by-n matrix
1 2 1 2
thatcontainsthecoefficientofe1\otimese2 inrowj ,columnj . Thusweneedamatrix,
j j 1 2
1 2
whichisanarrayspecifiedbytwoindices,torepresentanelementof\mathcal{V} \otimes\mathcal{V} .
1 2
Ifm > 2,thentheresultaboveshowsthatweneedanarrayspecifiedbym
indicestorepresentanarbitraryelementof\mathcal{V} \otimes⋯\otimes\mathcal{V} . Thustensorproducts
1 m
mayappearwhenwedealwithobjectsspecifiedbyarrayswithmultipleindices.
Thenextdefinitiongeneralizesthenotionofabilinearmap(see9.77). As
withbilinearmaps,thetargetspacecanbeanarbitraryvectorspace.
**9.91 定义：** m-linearmap
An m-linear map from \mathcal{V} \times ⋯ \times \mathcal{V} to a vector space \mathcal{U} is a function
1 m
Γ∶ \mathcal{V} \times⋯\times\mathcal{V} \rightarrow \mathcal{U} thatisalinearmapineachslotwhentheotherslots
1 m
areheldfixed.

| --- | -------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
Thenextresultcanbeprovedbyfollowingthepatternoftheproofof9.79.
convertingm-linearmapstolinearmaps
9.92
| Suppose\mathcal{U} |     | isavectorspace. |     |     |     |     |     |     |     |
| -------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
SupposethatΓ∶
| (a) |                      |      | \mathcal{V} \times⋯\times\mathcal{V} |           | \rightarrow\mathcal{U}   | isanm-linearmap. |               | Thenthereexists |     |
| --- | -------------------- | ---- | ------ | --------- | ---- | ---------------- | ------------- | --------------- | --- |
|     |                      |      | 1      |           | m    |                  |               |                 |     |
|     | auniquelinearmapΓ    |      |        | ̂∶ \mathcal{V}      | \otimes⋯\otimes\mathcal{V} | \rightarrow\mathcal{U}               | suchthat      |                 |     |
|     |                      |      |        | 1         |      | m                |               |                 |     |
|     |                      |      |        | ̂         |      |                  | ,…,v          |                 |     |
|     |                      |      | Γ      | (v 1 \otimes⋯\otimesv |      | m )=Γ(v          | 1 m           | )               |     |
|     | forall(v             | ,…,v | )\in\mathcal{V}    | \times⋯\times\mathcal{V}      |      | .                |               |                 |     |
|     |                      | 1    | m      | 1         | m    |                  |               |                 |     |
| (b) | Conversely,suppose\mathcal{T}∶ |      |        | \mathcal{V}         | \otimes⋯\otimes\mathcal{V} | \rightarrow\mathcal{U}               | isalinearmap. | Thenthere       |     |
|     |                      |      |        | 1         |      | m                |               |                 |     |
existsauniquem-linearmap\mathcal{T}#∶
|     |          |      |      |      |       | \mathcal{V} \times⋯\times\mathcal{V} | \rightarrow\mathcal{U}  | suchthat |     |
| --- | -------- | ---- | ---- | ---- | ----- | ------ | --- | -------- | --- |
|     |          |      |      |      |       | 1      | m   |          |     |
|     |          |      | \mathcal{T}#(v | ,…,v | )=\mathcal{T}(v | \otimes⋯\otimesv   |     | )        |     |
|     |          |      |      | 1    | m     | 1      | m   |          |     |
|     | forall(v | ,…,v | )\in\mathcal{V}  | \times⋯\times\mathcal{V} |       | .      |     |          |     |
|     |          | 1    | m    | 1    | m     |        |     |          |     |
See Exercises12and13fortensorproductsofmultipleinnerproductspaces.
| Exercises |          | 9D  |        |      |              |     |                 |     |       |
| --------- | -------- | --- | ------ | ---- | ------------ | --- | --------------- | --- | ----- |
| 1         | Supposev | \in   | \mathcal{V} andw | \in \mathcal{W}. | Provethatv\otimesw |     | = 0ifandonlyifv |     | = 0or |
$$w=0.$$
2 Giveanexampleofsixdistinctvectorsv ,v ,v ,w ,w ,w in\mathbf{R}3 suchthat
|     |            |     |       |     |       | 1                                 | 2 3 1 | 2 3 |     |
| --- | ---------- | --- | ----- | --- | ----- | --------------------------------- | ----- | --- | --- |
|     |            |     |       |     | +v    | +v                                |       |     |     |
|     |            |     | v     | \otimesw  | \otimesw    |                                   | \otimesw =0 |     |     |
|     |            |     |       | 1   | 1 2   | 2                                 | 3 3   |     |     |
|     | butnoneofv |     | \otimesw ,v | \otimesw  | ,v \otimesw | isascalarmultipleofanotherelement |       |     |     |
|     |            | 1   | 1     | 2 2 | 3     | 3                                 |       |     |     |
ofthislist.
Supposethatv ,…,v isalinearlyindependentlistin\mathcal{V}. Supposealsothat
| 3   |             |            | 1         | m        |      |           |     |     |     |
| --- | ----------- | ---------- | --------- | -------- | ---- | --------- | --- | --- | --- |
|     | w ,…,w      | isalistin\mathcal{W} |           | suchthat |      |           |     |     |     |
|     | 1           | m          |           |          |      |           |     |     |     |
|     |             |            |           | v \otimesw     | +⋯+v | \otimesw        | =0. |     |     |
|     |             |            |           | 1        | 1    | m         | m   |     |     |
|     | Provethatw  |            | =⋯=w      | =0.      |      |           |     |     |     |
|     |             | 1          |           | m        |      |           |     |     |     |
| 4   | Supposedim\mathcal{V} |            | >1anddim\mathcal{W} |          | >1.  | Provethat |     |     |     |
{v\otimesw∶(v,w)\in\mathcal{V}\times\mathcal{W}}
isnotasubspaceof\mathcal{V}\otimes\mathcal{W}.
|     | Thisexerciseimpliesthatif |     |     |     | dim\mathcal{V} | >1anddim\mathcal{W} | >1,then |     |     |
| --- | ------------------------- | --- | --- | --- | ---- | --------- | ------- | --- | --- |
{v\otimesw∶(v,w)\in\mathcal{V}\times\mathcal{W}}\neq\mathcal{V}\otimes\mathcal{W}.

Section9D Tensor Products 381
5 Supposemandnarepositiveintegers. Forv \in \mathbf{F}m andw \in \mathbf{F}n, identify
v\otimeswwithanm-by-nmatrixasin Example9.76. Withthatidentification,
showthattheset
{v\otimesw∶v\in\mathbf{F}m andw\in\mathbf{F}n}
isthesetofm-by-nmatrices(withentriesin\mathbf{F})thathaverankatmostone.
6 Suppose m and n are positive integers. Give a description, analogous to
Exercise5,ofthesetofm-by-nmatrices(withentriesin\mathbf{F})thathaverank
atmosttwo.
7 Supposedim\mathcal{V} >2anddim\mathcal{W} >2. Provethat
{v \otimesw +v \otimesw ∶v ,v \in\mathcal{V} andw ,w \in\mathcal{W}}\neq\mathcal{V}\otimes\mathcal{W}.
1 1 2 2 1 2 1 2
8 Supposev ,…,v \in\mathcal{V} andw ,…,w \in\mathcal{W} aresuchthat
1 m 1 m
v \otimesw +⋯+v \otimesw =0.
1 1 m m
Supposethat\mathcal{U}isavectorspaceandΓ∶ \mathcal{V}\times\mathcal{W} \rightarrow\mathcal{U}isabilinearmap. Show
that
Γ(v ,w )+⋯+Γ(v ,w )=0.
1 1 m m
9 Suppose\mathcal{S}\inℒ(\mathcal{V})and\mathcal{T} \inℒ(\mathcal{W}). Provethatthereexistsauniqueoperator
on\mathcal{V}\otimes\mathcal{W} thattakesv\otimeswto\mathcal{S}v\otimes\mathcal{T}wforallv\in\mathcal{V} andw\in\mathcal{W}.
Inanabuseofnotation,theoperatoron\mathcal{V}\otimes\mathcal{W} givenbythisexerciseis
oftencalled\mathcal{S}\otimes\mathcal{T}.
10 Suppose\mathcal{S}\inℒ(\mathcal{V})and\mathcal{T} \inℒ(\mathcal{W}). Provethat\mathcal{S}\otimes\mathcal{T}isaninvertibleoperator
on\mathcal{V}\otimes\mathcal{W} ifandonlyifboth\mathcal{S}and\mathcal{T} areinvertibleoperators. Also,prove
thatifboth\mathcal{S}and\mathcal{T} areinvertibleoperators,then(\mathcal{S}\otimes\mathcal{T})-1 =\mathcal{S}-1\otimes\mathcal{T}-1,
whereweareusingthenotationfromthecommentafter Exercise9.
11 Suppose\mathcal{V} and\mathcal{W} areinnerproductspaces. Provethatif\mathcal{S} \in ℒ(\mathcal{V})and
\mathcal{T} \inℒ(\mathcal{W}),then(\mathcal{S}\otimes\mathcal{T}) ∗ =\mathcal{S} ∗ \otimes\mathcal{T} ∗ ,whereweareusingthenotationfrom
thecommentafter Exercise9.
12 Supposethat\mathcal{V} ,…,\mathcal{V} arefinite-dimensionalinnerproductspaces. Prove
1 m
thatthereisauniqueinnerproducton\mathcal{V} \otimes⋯\otimes\mathcal{V} suchthat
1 m
\langlev \otimes⋯\otimesv ,u \otimes⋯\otimesu \rangle=\langlev ,u \rangle⋯\langlev ,u \rangle
1 m 1 m 1 1 m m
forall(v ,…,v )and(u ,…,u )in\mathcal{V} \times⋯\times\mathcal{V} .
1 m 1 m 1 m
Notethattheequationaboveimpliesthat
‖v \otimes⋯\otimesv ‖=‖v ‖\times⋯\times‖v ‖
1 m 1 m
forall(v ,…,v )\in\mathcal{V} \times⋯\times\mathcal{V} .
1 m 1 m

| ------------------------------------------ | --- | --- | --- | --- |
13 Suppose that \mathcal{V} ,…,\mathcal{V} are finite-dimensional inner product spaces and
1 m
| \mathcal{V} \otimes⋯\otimes\mathcal{V} ismadeintoaninnerproductspaceusingtheinnerproduct |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- |
1 m
Supposeek,…,ek
| from Exercise12.           |     | isanorthonormalbasisof\mathcal{V} |     | foreach |
| ------------------------- | --- | ----------------------- | --- | ------- |
|                           | 1   | n k                     |     | k       |
| k =1,…,m. Showthatthelist |     |                         |     |         |
{e1 \otimes⋯\otimesem}
|                         | j    | j j =1,…,n | ;⋯;j =1,…,n |     |
| ----------------------- | ---- | ---------- | ----------- | --- |
|                         | 1    | m 1 1      | m m         |     |
| isanorthonormalbasisof\mathcal{V} | \otimes⋯\otimes\mathcal{V} | .          |             |     |
|                         | 1    | m          |             |     |

• pagev: Photosby Carrie Heeterand Bishnu Sarangi. Publicdomainimage.
• page1: Originalpaintingby Pierre Louis Dumesnil;1884copyby Nils
| Forsberg. | Publicdomainimagedownloadedon29March2022from |     |
| --------- | -------------------------------------------- | --- |
https://commons.wikimedia.org/wiki/File:René_Descartes_i_samtal_med_Sveriges_drottning,_Kristina.jpg.
| • page27: | Publicdomainimagedownloadedon4February2022from |     |
| --------- | ---------------------------------------------- | --- |
https://commons.wikimedia.org/wiki/File:IAS_Princeton.jpg.
• page51: Photoby Stefan Schäfer;Creative Commons Attribution Share Alike
| license. | Downloadedon28March2022from |     |
| -------- | --------------------------- | --- |
https://commons.wikimedia.org/wiki/File:Burg Dankwarderode2016.jpg.
• page119: Photoby Alireza Javaheri. Creative Commons Attributionlicense.
Downloadedon12March2023from
https://commons.wikimedia.org/wiki/File:Hakim_Omar_Khayam_-_panoramio.jpg.
| • page132: | Statuecompletedby Giovanni Paganucciin1863. | Photoby |
| ---------- | ----------------------------------------- | ------- |
Hans-Peter Postel;Creative Commons Attributionlicense. Downloadedon14
March2022from
https://commons.wikimedia.org/wiki/File:Leonardo_da_Pisa.jpg.
• page181: Photoby Matthew Petroff;Creative Commons Attribution Share
| Alikelicense. | Downloadedon31March2022from |     |
| ------------- | --------------------------- | --- |
https://commons.wikimedia.org/wiki/File:George-peabody-library.jpg.
• page227: Photoby Petar Milošević;Creative Commons Attribution Share
| Alikelicense. | Downloadedon30March2022from |     |
| ------------- | --------------------------- | --- |
https://en.wikipedia.org/wiki/Lviv.
• page297: Photoby David Iliff;Creative Commons Attribution Share Alike
| license. | Downloadedon30March2022from |     |
| -------- | --------------------------- | --- |
https://en.wikipedia.org/wiki/File:Long_Room_Interior,_Trinity_College_Dublin,_Ireland_-_Diliff.jpg.
• page332: Photoby Daniel Schwen;Creative Commons Attribution Share
| Alikelicense. | Downloadedon9July2019from |     |
| ------------- | ------------------------- | --- |
https://commons.wikimedia.org/wiki/File:Mathematik_Göttingen.jpg.

| \mathcal{A}-1,91 |     | ⟺,23   | \mathcal{T}†,221 |     |
| ------ | --- | ------ | ------ | --- |
| \mathcal{A} ,74  |     | Im,120 | \mathcal{T}m,137 |     |
j,\cdot
| \mathcal{A} ,69 |     | -\infty,31 | ‖\mathcal{T}‖,280 |     |
| ----- | --- | ----- | ------- | --- |
j,k
| \mathcal{A} ,74 |     |     | \mathcal{T}#,375,380 |     |
| ----- | --- | --- | ---------- | --- |
\cdot,k
ℒ(\mathcal{V}),52
| \alpha ,354 |     |     | tr\mathcal{A},326 |     |
| ------ | --- | --- | ------- | --- |
\mathcal{T}
| ∗      |     | ℒ(\mathcal{V},\mathcal{W}),52 |         |     |
| ------ | --- | --------- | ------- | --- |
| \mathcal{A} ,231 |     |           | tr\mathcal{T},327 |     |
| \mathcal{A}t,77  |     |           | \mathcal{T}| ,133 |     |
|        |     | ℳ(\beta),334  | \mathcal{U}       |     |
\mathcal{T}/\mathcal{U},142
| ̂,375,380 |     | ℳ(\mathcal{T}),69,154 |     |     |
| --------- | --- | ----------- | --- | --- |
Γ
|     |     | ℳ(v),88 | \mathcal{U}⟂,211 |     |
| --- | --- | ------- | ------ | --- |
\mathcal{B},287
\mathcal{U}0,109
| ℬ(\mathcal{V} ,…,\mathcal{V}   | ),378 |          |           |     |
| ---------- | ----- | -------- | --------- | --- |
| 1          | m     |          |           |     |
| ℬ(\mathcal{V},\mathcal{W}),370 |       | perm,348 | \langleu,v\rangle,184 |     |
𝒫(\mathbf{F}),30
| \mathbf{C},2  |     | \pi,101    | \mathcal{V},15       |     |
| ---- | --- | -------- | ---------- | --- |
| \circ,55 |     | 𝒫 (\mathbf{F}),31 | \mathcal{V}′,105,204 |     |
m
|     |     | p(\mathcal{T}),137 | \mathcal{V}/\mathcal{U},99 |     |
| --- | --- | -------- | ------ | --- |
deg,31
|     |     | \mathcal{P} ,214 | -v,15 |     |
| --- | --- | ------ | ----- | --- |
\mathcal{U}
\Delta,196
|     |     |     | \mathcal{V} \otimes⋯\otimes\mathcal{V} | ,379 |
| --- | --- | --- | ------ | ---- |
|     |     |     | 1      | m    |
det\mathcal{A},355
|          |     | q ,341 | v \otimes⋯\otimesv   | ,379 |
| -------- | --- | ------ | -------- | ---- |
|          |     | \beta      | 1        | m    |
| det\mathcal{T},354 |     |        | \mathcal{V}(2),334 |      |
,7
| dim,44 |     |     | \mathcal{V}(2),339 |     |
| ------ | --- | --- | -------- | --- |
alt
| \oplus,21 |     | \mathbf{R},2 | \mathcal{V}(2),337 |     |
| ---- | --- | --- | -------- | --- |
sym
Re,120
| ,…,s  |         |     | \mathcal{V} ,17      |     |
| ----- | ------- | --- | ---------- | --- |
| \mathcal{E}(s f | f ),287 |     | \mathbf{C}          |     |
| 1 1   | n n     |     | \mathcal{V}m,103,346 |     |
\mathcal{E}(\lambda,\mathcal{T}),164
\mathcal{S}\otimes\mathcal{T},381
\mathcal{V}(m),346
⊊,299
| \mathbf{F},4 |     |     | \mathcal{V}(m),347 |     |
| --- | --- | --- | -------- | --- |
alt
| \mathbf{F}\infty,13 |     |     | \mathcal{V}\otimes\mathcal{W},372 |     |
| ----- | --- | --- | ------- | --- |
\sqrt\mathcal{T},253
| \mathbf{F}m,n,72 |     | ̃   | v\otimesw,372 |     |
| ------- | --- | --- | ------- | --- |
\mathcal{T} ,102
| \mathbf{F}n,6 |     |     | v+\mathcal{U},98 |     |
| ---- | --- | --- | ------ | --- |
\mathcal{T}′,107
| \mathbf{F}\mathcal{S},13 |     | ∗   |     |     |
| ----- | --- | --- | --- | --- |
\mathcal{T} ,228
||v||,186
\mathcal{T}-1,82
\mathcal{G}(\lambda,\mathcal{T}),308
z,120
\mathcal{T}(\Omega),288
|z|,120
| \mathcal{I},52,90 |     | \mathcal{T} ,68 |     |     |
| ------- | --- | ----- | --- | --- |
\mathbf{C}

Index
Abbott,Edwin A.,6 bilinearform,333
absolutevalue,120 bilinearfunctional,370
addition bilinearmap,374
inquotientspace,100 blockdiagonalmatrix,314
ofcomplexnumbers,2 Bunyakovsky,Viktor,189
offunctions,13
∗
oflinearmaps,55 \mathcal{C} -algebras,295
ofmatrices,71 Carroll,Lewis,11
ofsubspaces,19 Cauchy,Augustin-Louis,189
ofvectors,12 Cauchy–Schwarzinequality,189
ofvectorsin\mathbf{F}n,6 Cayley,Arthur,312
additiveinverse Cayley–Hamiltontheorem,364
in\mathbf{C},3,4 oncomplexvectorspace,312
in\mathbf{F}n,9 change-of-basisformula
invectorspace,12,15 forbilinearforms,336
additivity,52 foroperators,93
adjointofalinearmap,228 characteristicpolynomial,363
algebraicmultiplicity,311 oncomplexvectorspace,311
alternatingbilinearform,339 Chat GPT,196,279
alternatingm-linearform,347 Choleskyfactorization,267
annihilator,109 Cholesky,André-Louis,267
Apollonius’sidentity,195 Christina,Queenof Sweden,1
Artin,Emil,80 closedunderaddition,18
associativity,3,12,56 closedunderscalarmultiplication,18
columnrankofamatrix,77,114,239
backwardshift,53,59,84,140 column–rowfactorization,78
ball,287 commutativity,3,7,12,25,56,73,80
Banach,Stefan,227 commutingoperators,138,175–180,
basis,39 209,235,248–249,256
ofeigenvectors,165,245,246, companionmatrix,152
250 complexconjugate,120
ofgeneralizedeigenvectors,301 complexnumber,2
Bernsteinpolynomials,49 complexspectraltheorem,246
Bessel’sinequality,198 complexvectorspace,13

386 Index
complexification doubledualspace,118
eigenvaluesof,140 dual
generalizedeigenvectorsof,318 ofabasis,106
minimalpolynomialof,153 ofalinearmap,107,153,162,
multiplicityofeigenvalues,318 174
ofalinearmap,68 ofavectorspace,105,204
ofavectorspace,17,43 ofanoperator,140
ofaninnerproductspace,194
conjugatesymmetry,183 eigenspace,164
conjugatetransposeofamatrix,231 eigenvalue
coordinate,6 ofadjoint,239
cuberootofanoperator,248 ofdualofanoperator,140
ofoperator,134
De Moivre’stheorem,125
ofpositiveoperator,252
degreeofapolynomial,31
ofself-adjointoperator,233
Descartes,René,1
ofunitaryoperator,262
determinant
onodd-dimensionalspace,150,
ofmatrix,355
318,367
ofoperator,354
eigenvector,135
ofpositiveoperator,362
ellipsoid,287
ofunitaryoperator,362
Euclideaninnerproduct,184
diagonalmatrix,163,274
diagonalofasquarematrix,155 Fibonacci,132
diagonalizable,163,172,176,245, Fibonaccisequence,174
246,294,307,316 field,10
differentiationlinearmap,53,56,59, finite-dimensionalvectorspace,30
61,62,67,70,79,138,208, Flatland,6
304 forwardshift,140
dimension,44 Frankenstein,50
ofasumofsubspaces,47 Frobeniusnorm,331
directsum,21,42,98 Fuglede’stheorem,248
ofasubspaceanditsorthogonal fundamentaltheoremofalgebra,125
complement,212 fundamentaltheoremoflinearmaps,
ofnull\mathcal{T}dim\mathcal{V} andrange\mathcal{T}dim\mathcal{V},
discrete Fouriertransform,269 Gauss,Carl Friedrich,51
distributiveproperty,3,12,15,56,80 Gaussianelimination,51,65,361
divisionalgorithmforpolynomials, generalizedeigenspace,308
124 generalizedeigenvector,300
divisionofcomplexnumbers,4 geometricmultiplicity,311
dotproduct,182 Gershgorindisk,170

Index 387
Gershgorindisktheorem,171 Laplacian,196
Gershgorin,Semyon Aronovich,171 lengthoflist,5
Gram,Jørgen,200 Leonardoof Pisa,132
Gram–Schmidtprocedure,200 linearcombination,28
graphofalinearmap,103 lineardependencelemma,33
linearequations,64–65,95
Hadamard’sinequality,365 linearfunctional,105,204
Halmos,Paul,27 linearmap,52
Hamilton,William,297 linearmaplemma,54
harmonicfunction,196 linearspan,29
Hilbertmatrix,256 linearsubspace,18
Hilbert–Schmidtnorm,331 lineartransformation,52
homogeneity,52 linearlydependent,33
homogeneoussystemoflinear linearlyindependent,32
equations,65,95 list,5
hyponormaloperator,241 ofvectors,28
lower-triangularmatrix,162,267
identitymatrix,90
Lviv,227
identityoperator,52,56 Lwów,227
imaginarypart,120
infinite-dimensionalvectorspace,31 matrix,69
injective,60 multiplication,73
innerproduct,183 ofbilinearform,334
innerproductspace,184 oflinearmap,69
ofnilpotentoperator,305
Institutefor Advanced Study,27
ofoperator,154
invariantsubspace,133
ofproductoflinearmaps,74,91
inverse
of\mathcal{T}′,113
ofalinearmap,82
∗
of\mathcal{T} ,232
ofamatrix,91
ofvector,88
invertiblelinearmap,82
minimalpolynomial
invertiblematrix,91
andbasisofgeneralized
isometry,258
eigenvectors,306
isomorphicvectorspaces,86
andcharacteristicpolynomial,312
isomorphism,86
anddiagonalizability,169
Jordanbasis,322 andgeneralizedeigenspace
Jordanform,324 decomposition,316
Jordan,Camille,324 andgeneralizedeigenspaces,317
andinvertibility,149
kernel,59 andupper-triangularmatrices,
Khayyam,Omar,119 159,203

388 Index
computing,145 complement,211
definitionof,145 projection,214
gcdwithitsderivative,173 vectors,187
nodirectsumdecomposition,325 orthonormal
ofadjoint,241 basis,199
ofcompanionmatrix,152 list,197
ofcomplexification,153
ofdualmap,153 parallelogramequality,191
ofnilpotentoperator,305,324 Parseval’sidentity,200
ofnormaloperator,241 partialdifferentiationoperator,175
ofquotientoperator,153 Peabody Library,181
ofrestrictionoperator,148 permutation,348
ofself-adjointoperator,244 photocredits,383
polynomialmultipleof,148 point,12
zerosof,146 polardecomposition,286
minimizingdistance,217 polynomial,30
m-linearform,346 positivedefinite,266
m-linearfunctional,378 positiveoperator,251
m-linearmap,379 positivesemidefiniteoperator,251
monicpolynomial,144 principalaxes,287
Moon,v,xvii product
Moore–Penroseinverse,221 ofcomplexnumbers,2
multilinearform,346 oflinearmaps,55
multiplication,seeproduct ofmatrices,73
multiplicityofaneigenvalue,310 ofpolynomials,138
ofscalarandlinearmap,55
nilpotentoperator,303,322 ofscalarandvector,12
Noether,Emmy,332 ofscalarandvectorin\mathbf{F}n,9
nonsingularmatrix,91 ofvectorspaces,96
normofalinearmap,280 pseudoinverse,221,250,255,275,279
normofavector,182,186 Pythagoreantheorem,187
normaloperator,235
nullspace,59 QRfactorization,264,365
ofpowersofanoperator,298 quadraticform,341
of\mathcal{T}′,111 quotient
of\mathcal{T} ∗ ,231 map,101
operator,142,153,162,173
one-to-one,60
space,99
onto,62
operator,133 range,61
orthogonal ofpowersofanoperator,306

Index 389
of\mathcal{T}′,112 squarerootofanoperator,248,251,
of\mathcal{T} ∗ ,231 253,320
rankofamatrix,79,114,239 standardbasis
realpart,120 of\mathbf{F}n,39
realspectraltheorem,245 of𝒫 (\mathbf{F}),39
m
realvectorspace,13 subspace,18
reversetriangleinequality,129,193, subtractionofcomplexnumbers,4
294 sum,seeaddition
Rieszrepresentationtheorem,205,210, sumofsubspaces,19
216,224,225 Supreme Court,210
Riesz,Frigyes,205 surjective,62
rowrankofamatrix,77,114,239
SVD,seesingularvaluedecomposition
Sylvester,James,181
scalar,4 symmetricbilinearform,337
scalarmultiplication,9,12 symmetricmatrix,269,337
inquotientspace,100
tensorproduct,372,379
oflinearmaps,55
Throughthe Looking Glass,11
ofmatrices,71
trace
Schmidtpair,278
ofamatrix,326
Schmidt,Erhard,200,278
ofanoperator,327
Schur’stheorem,204
translate,99
Schur,Issai,204
transposeofamatrix,77,231
Schwarz,Hermann,189
triangleinequality,121,190,281
self-adjointoperator,233
tuple,5
Shelley,Mary Wollstonecraft,50
two-sidedideal,58
signofapermutation,349
simultaneousdiagonalization,176 unitcirclein\mathbf{C},262,269
simultaneouslyuppertriangularizable, unitarymatrix,263
178 unitaryoperator,260
singularmatrix,91 Universityof Dublin,297
singularvaluedecomposition Universityof Göttingen,332
upper-triangularmatrix,155–160,264,
ofadjoint,275
267,314
oflinearmap,273
ofpseudoinverse,275
Vandermondematrix,366
singularvalues,271,362
vector,8,12
skewoperator,240,247,269
vectorspace,12
span,29
volume,292,363
spans,29
ofabox,291
spectraltheorem,245,246
squarematrix,91 zeroofapolynomial,122

Colophon: Notes on Typesetting
• Thisbookwastypesetin Lua LATEXbytheauthor,whowrotethe LATEXcodeto
implementthebook’sdesign.
• The LATEXsoftwareusedforthisbookwaswrittenby Leslie Lamport. The TEX
software,whichformsthebasefor LATEX,waswrittenby Donald Knuth.
• Themaintextfontinthisbookisthe Open Type Formatversionof TEXGyre
Termes,afontbasedon Times,whichwasdesignedby Stanley Morisonand
Victor Lardentforthe Britishnewspaper The Timesin1931.
• Themainmathfontinthisbookisthe Open Type Formatversionof TEXGyre
Pagella Math,afontbasedon Palatino,whichwasdesignedby Hermann Zapf.
• Thesansseriffontusedforpageheadingsandsomeotherdesignelementsis
the Open Type Formatversionof TEXGyre Heros,afontbasedon Helvetica,
whichwasdesignedby Max Miedingerand Eduard Hoffmann.
• The Lua LATEXpackagesfontspecandunicode-math,bothwrittenby Will
Robertson,wereusedtomanagefonts.
• The LATEXpackagefontsize,writtenby Ivan Valbusa,wasusedtogracefully
changethemainfontsto10.5pointsize.
• Thefiguresinthebookwereproducedby Mathematica,using Mathematica
code written by the author. Mathematica was created by Stephen Wolfram.
The Mathematicapackage Ma Te X,writtenby Szabolcs Horvát,wasusedto
place LATEX-generatedlabelsinthe Mathematicafigures.
• The LATEXpackagegraphicx,writtenby David Carlisleand Sebastian Rahtz,
wasusedtoincludephotosandfigures.
• The LATEX package multicol, written by Frank Mittelbach, was used to get
around LATEX’slimitationthattwo-columnformatmuststartonanewpage
$$(neededforthe Symbol Indexandthe Index).$$
• The LATEXpackages Tik Z,writtenby Till Tantau,andtcolorbox,writtenby
Thomas Sturm,wereusedtoproducethedefinitionboxesandresultboxes.
• The LATEXpackagecolor,writtenby David Carlisle,wasusedtoaddappropriate
colortovariousdesignelements.
• The LATEXpackagewrapfig,writtenby Donald Arseneau,wasusedtowrap
textaroundthecommentboxes.
• The LATEXpackagemicrotype,writtenby Robert Schlicht,wasusedtoreduce
hyphenationandproducemorepleasingrightjustification.