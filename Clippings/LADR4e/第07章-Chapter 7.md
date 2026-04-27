---
title: Chapter 7
source: Clippings/LADR4e.pdf
created: 2026-04-23
type: chapter
tags:
  - book
  - chapter
---

# Chapter 7
Operators on Inner Product Spaces
Thedeepestresultsrelatedtoinnerproductspacesdealwiththesubjecttowhich
wenowturn—linearmapsandoperatorsoninnerproductspaces. Aswewillsee,
goodtheoremscanbeprovedbyexploitingpropertiesoftheadjoint.
Thehugelyimportantspectraltheoremwillprovideacompletedescription
ofself-adjointoperatorsonrealinnerproductspacesandofnormaloperators
oncomplexinnerproductspaces. Wewillthenusethespectraltheoremtohelp
understandpositiveoperatorsandunitaryoperators,whichwillleadtounitary
matrices and matrix factorizations. The spectral theorem will also lead to the
popularsingularvaluedecomposition,whichwillleadtothepolardecomposition.
The most important results in the rest of this book are valid only in finite
dimensions. Thusfromnowonweassumethat\mathcal{V} and\mathcal{W} arefinite-dimensional.
standingassumptionsforthischapter
• \mathbf{F} denotes\mathbf{R} or\mathbf{C}.
• \mathcal{V} and\mathcal{W} arenonzerofinite-dimensionalinnerproductspacesover\mathbf{F}.
Petar MiloševićCCBY-SA
Marketsquarein Lviv,acitythathashadseveralnamesandhasbeeninseveral
countriesbecauseofchanginginternationalborders. From1772until1918,thecitywas
in Austriaandwascalled Lemberg. Between World War Iand World War II,thecitywas
in Polandandwascalled Lwów. Duringthistime,mathematiciansin Lwów,particularly
Stefan Banach(1892–1945)andhiscolleagues,developedthebasicresultsofmodern
functionalanalysis,usingtoolsofanalysistostudyinfinite-dimensionalvectorspaces.
Sincetheendof World War II,Lvivhasbeenin Ukraine,whichwaspartofthe
Soviet Unionuntil Ukrainebecameanindependentcountryin1991.

| --- | -------- | ----------------------------- | --- | --- | --- | --- | --- |
| 7A Self-Adjoint |     | and | Normal | Operators |     |     |     |
| --------------- | --- | --- | ------ | --------- | --- | --- | --- |
Adjoints
|     | adjoint,\mathcal{T} | ∗   |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- |
**7.1 定义：** ∗∶
| Suppose\mathcal{T} | \in ℒ(\mathcal{V},\mathcal{W}). | Theadjoint |     | of\mathcal{T} | isthefunction\mathcal{T} | \mathcal{W} \rightarrow \mathcal{V} | such |
| -------- | --------- | ---------- | --- | --- | -------------- | ----- | ---- |
that
∗
|             |     |                | \langle\mathcal{T}v,w\rangle=\langlev,\mathcal{T} |     | w\rangle  |     |     |
| ----------- | --- | -------------- | ----------- | --- | --- | --- | --- |
| foreveryv\in\mathcal{V} |     | andeveryw\in\mathcal{W}.   |             |     |     |     |     |
| To see      | why | the definition | above       |     |     |     |     |
Thewordadjointhasanothermeaning
| makessense,suppose\mathcal{T} |     | \inℒ(\mathcal{V},\mathcal{W}). |     | Fix |                 |         |         |
| ------------------- | --- | -------- | --- | --- | --------------- | ------- | ------- |
|                     |     |          |     | in  | linear algebra. | In case | you en- |
w\in\mathcal{W}. Considerthelinearfunctional counterthesecondmeaningelsewhere,
bewarnedthatthetwomeaningsfor
v↦\langle\mathcal{T}v,w\rangle
adjointareunrelatedtoeachother.
| on \mathcal{V} that | maps v | \in \mathcal{V} to \langle\mathcal{T}v,w\rangle; |     | this |     |     |     |
| --------- | ------ | -------------- | --- | ---- | --- | --- | --- |
linearfunctionaldependson\mathcal{T}andw. Bythe Rieszrepresentationtheorem(6.42),
thereexistsauniquevectorin\mathcal{V} suchthatthislinearfunctionalisgivenbytaking
|     |     |     |     |     | ∗   |     | ∗   |
| --- | --- | --- | --- | --- | --- | --- | --- |
theinnerproductwithit. Wecallthisuniquevector\mathcal{T} w. Inotherwords,\mathcal{T} wis
| theuniquevectorin\mathcal{V} |     | suchthat |             |     |      |     |     |
| ------------------ | --- | -------- | ----------- | --- | ---- | --- | --- |
|                    |     |          | \langle\mathcal{T}v,w\rangle=\langlev,\mathcal{T} |     | ∗ w\rangle |     |     |
foreveryv\in\mathcal{V}.
Intheequationabove,theinnerproductonthelefttakesplacein\mathcal{W} andthe
innerproductontherighttakesplacein\mathcal{V}. However,weusethesamenotation
\langle\cdot,\cdot\rangleforbothinnerproducts.
|     | adjointofalinearmapfrom\mathbf{R}3 |     |     |     | to\mathbf{R}2 |     |     |
| --- | ------------------------- | --- | --- | --- | ---- | --- | --- |
**7.2 例：** | Define\mathcal{T}∶   | \mathbf{R}3         | \rightarrow\mathbf{R}2 by     |           |          |              |            |     |
| ---------- | ---------- | ---------- | --------- | -------- | ------------ | ---------- | --- |
|            |            | \mathcal{T}(x        | ,x ,x     | )=(x +3x | ,2x ).       |            |     |
|            |            |            | 1 2       | 3 2      | 3 1          |            |     |
|            | ∗          | ,x         | ,x        | )\in\mathbf{R}3     | ,y )\in\mathbf{R}2.     |            |     |
| Tocompute\mathcal{T} | ,suppose(x |            |           | and(y    |              | Then       |     |
|            |            | 1          | 2 3       |          | 1 2          |            |     |
|            | \langle\mathcal{T}(x       | ,x ,x ),(y | ,y )\rangle=\langle(x |          | +3x ,2x ),(y | ,y )\rangle      |     |
|            |            | 1 2 3      | 1 2       | 2        | 3 1          | 1 2        |     |
|            |            |            |           |          | +3x +2x      |            |     |
|            |            |            |           | =x y     | y            | y          |     |
|            |            |            |           | 2 1      | 3 1          | 1 2        |     |
|            |            |            |           | =\langle(x ,x  | ,x ),(2y     | ,y ,3y )\rangle. |     |
|            |            |            |           | 1        | 2 3          | 2 1 1      |     |
Theequationaboveandthedefinitionoftheadjointimplythat
∗
|     |     | \mathcal{T}   | (y ,y | )=(2y | ,y ,3y ). |     |     |
| --- | --- | --- | ----- | ----- | --------- | --- | --- |
|     |     |     | 1     | 2 2   | 1 1       |     |     |

| --- | --- | --------- | --- | ------------------------------ | --- | --- | --- |
|     | adjointofalinearmapwithrangeofdimensionatmost |     |     |     |     |     | 1   |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
**7.3 例：** | Fixu\in\mathcal{V} | andx | \in\mathcal{W}. | Define\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W})by |     |     |     |
| ------ | ---- | --- | ------- | --------- | --- | --- | --- |
\mathcal{T}v=\langlev,u\ranglex
∗
| foreachv\in\mathcal{V}. |     | Tocompute\mathcal{T} | ,supposev\in\mathcal{V} |     | andw\in\mathcal{W}. |     | Then |
| ----------- | --- | ---------- | ----------- | --- | ------- | --- | ---- |
\langle\mathcal{T}v,w\rangle=\langle\langlev,u\ranglex,w\rangle
=\langlev,u\rangle\langlex,w\rangle
=\langlev,\langlew,x\rangleu\rangle.
Thus
∗
\mathcal{T} w=\langlew,x\rangleu.
∗
| Inthetwoexamplesabove,\mathcal{T} |     |     |     | turned |     |     |     |
| ----------------------- | --- | --- | --- | ------ | --- | --- | --- |
Thetwoexamplesaboveandtheproof
| outto be       | not justa | function | from | to      |           |          |                |
| -------------- | --------- | -------- | ---- | ------- | --------- | -------- | -------------- |
|                |           |          |      | \mathcal{W}       | below use | a common | technique for  |
| \mathcal{V} but a linear | map       | from     | \mathcal{W} to | \mathcal{V}. This |           | ∗:       |                |
|                |           |          |      |         | computing | \mathcal{T} start  | with a formula |
behavioristrueingeneral,asshownby for \langle\mathcal{T}v,w\rangle then manipulate it to get
| thenextresult. |     |     |     |     | justvinthefirstslot;theentryinthe |     |     |
| -------------- | --- | --- | --- | --- | --------------------------------- | --- | --- |
∗
|     |     |     |     |     | secondslotwillthenbe\mathcal{T} |     | w.  |
| --- | --- | --- | --- | --- | --------------------- | --- | --- |
7.4 adjointofalinearmapisalinearmap
| \inℒ(\mathcal{V},\mathcal{W}),then\mathcal{T} |     |     | ∗ \inℒ(\mathcal{W},\mathcal{V}). |     |     |     |     |
| ------------- | --- | --- | ---------- | --- | --- | --- | --- |
If\mathcal{T}
| Proof Suppose\mathcal{T} |     | \inℒ(\mathcal{V},\mathcal{W}). |     | Ifv\in\mathcal{V} andw | ,w  | \in\mathcal{W},then |     |
| -------------- | --- | -------- | --- | ---------- | --- | ------- | --- |
1 2
|     |     | \langle\mathcal{T}v,w | +w  | \rangle=\langle\mathcal{T}v,w | \rangle+\langle\mathcal{T}v,w  | \rangle    |     |
| --- | --- | ----- | --- | ------- | -------- | ---- | --- |
|     |     |       | 1   | 2       | 1        | 2    |     |
|     |     |       |     | ∗       |          | ∗    |     |
|     |     |       |     | =\langlev,\mathcal{T}   | w \rangle+\langlev,\mathcal{T} | w \rangle  |     |
|     |     |       |     | =\langlev,\mathcal{T} ∗ | w +\mathcal{T} ∗   | w \rangle. |     |
Theequationaboveshowsthat
|        |                 |     | ∗        | ∗       | ∗    |     |     |
| ------ | --------------- | --- | -------- | ------- | ---- | --- | --- |
|        |                 |     | \mathcal{T} (w +w  | )=\mathcal{T}     | w +\mathcal{T} | w . |     |
|        |                 |     | 1        | 2       | 1    | 2   |     |
| Ifv\in\mathcal{V}, | \lambda\in\mathbf{F},andw\in\mathcal{W},then |     |          |         |      |     |     |
|        |                 |     | \langle\mathcal{T}v,\lambdaw\rangle= | \lambda\langle\mathcal{T}v,w\rangle |      |     |     |
|        |                 |     |          | = \lambda\langlev,\mathcal{T} | ∗ w\rangle |     |     |
∗
|     |     |     |     | =\langlev,\lambda\mathcal{T} | w\rangle. |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- |
Theequationaboveshowsthat
|       |                           |     |     | ∗        | ∗   |     |     |
| ----- | ------------------------- | --- | --- | -------- | --- | --- | --- |
|       |                           |     | \mathcal{T}   | (\lambdaw)= \lambda\mathcal{T} | w.  |     |     |
| Thus\mathcal{T} | ∗ isalinearmap,asdesired. |     |     |          |     |     |     |

| -------- | ----------------------------- | --- | --- | --- | --- | --- |
propertiesoftheadjoint
7.5
| Suppose\mathcal{T}  | \inℒ(\mathcal{V},\mathcal{W}).    | Then            |     |     |     |     |
| --------- | ----------- | --------------- | --- | --- | --- | --- |
|           | ∗ ∗+\mathcal{T} ∗     |                 |     |     |     |     |
| (a) (\mathcal{S}+\mathcal{T}) | =\mathcal{S}          | forall\mathcal{S}\inℒ(\mathcal{V},\mathcal{W}); |     |     |     |     |
|           | ∗ ∗         |                 |     |     |     |     |
| (b) (\lambda\mathcal{T})  | = \lambda\mathcal{T} forall | \lambda\in\mathbf{F};            |     |     |     |     |
∗ ∗
$$(c) (\mathcal{T} ) =\mathcal{T};$$
|     | ∗ ∗ ∗ |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- |
$$(d) (\mathcal{S}\mathcal{T}) =\mathcal{T} \mathcal{S} forall\mathcal{S}\inℒ(\mathcal{W},\mathcal{U})(here\mathcal{U} isafinite-dimensionalinner$$
productspaceover\mathbf{F});
∗
| (e) \mathcal{I} =\mathcal{I},where\mathcal{I} | istheidentityoperatoron\mathcal{V}; |     |     |     |     |     |
| --------------- | ------------------------- | --- | --- | --- | --- | --- |
∗
$$(f) if\mathcal{T} isinvertible,then\mathcal{T} ∗ isinvertibleand(\mathcal{T} ∗ )-1 =(\mathcal{T}-1) .$$
| Proof Supposev\in\mathcal{V} | andw\in\mathcal{W}. |     |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- | --- |
$$(a) If\mathcal{S}\inℒ(\mathcal{V},\mathcal{W}),then$$
\langle(\mathcal{S}+\mathcal{T})v,w\rangle=\langle\mathcal{S}v,w\rangle+\langle\mathcal{T}v,w\rangle
|           |     |                  | ∗       | ∗     |     |     |
| --------- | --- | ---------------- | ------- | ----- | --- | --- |
|           |     | =\langlev,\mathcal{S}            | w\rangle+\langlev,\mathcal{T} | w\rangle    |     |     |
|           |     | =\langlev,\mathcal{S}            | ∗ w+\mathcal{T}   | ∗ w\rangle. |     |     |
|           | ∗ ∗ | ∗                |         |       |     |     |
| Thus(\mathcal{S}+\mathcal{T}) | w=\mathcal{S} | w+\mathcal{T} w,asdesired. |         |       |     |     |
$$(b) If \lambda\in\mathbf{F},then$$
|          |                        |          |       | ∗        | ∗   |     |
| -------- | ---------------------- | -------- | ----- | -------- | --- | --- |
|          | \langle(\lambda\mathcal{T})v,w\rangle=             | \lambda\langle\mathcal{T}v,w\rangle= | \lambda\langlev,\mathcal{T} | w\rangle=\langlev,\lambda\mathcal{T} | w\rangle. |     |
| Thus(\lambda\mathcal{T}) | ∗ w= \lambda\mathcal{T} ∗ w,asdesired. |          |       |          |     |     |
$$(c) Wehave$$
|     | ∗            | ∗   |                   |     |     |     |
| --- | ------------ | --- | ----------------- | --- | --- | --- |
|     | \langle\mathcal{T} w,v\rangle=\langlev,\mathcal{T} |     | w\rangle=\langle\mathcal{T}v,w\rangle=\langlew,\mathcal{T}v\rangle. |     |     |     |
∗
| Thus(\mathcal{T}                     | ∗ ) v=\mathcal{T}v,asdesired.       |               |      |         |             |     |
| -------------------------- | ------------------------- | ------------- | ---- | ------- | ----------- | --- |
| (d) Suppose\mathcal{S}\inℒ(\mathcal{W},\mathcal{U})andu\in\mathcal{U}. |                           |               | Then |         |             |     |
|                            | \langle(\mathcal{S}\mathcal{T})v,u\rangle=\langle\mathcal{S}(\mathcal{T}v),u\rangle=\langle\mathcal{T}v,\mathcal{S} |               | ∗    | u\rangle=\langlev,\mathcal{T} | ∗ (\mathcal{S} ∗ u)\rangle. |     |
|                            | ∗ ∗                       | ∗             |      |         |             |     |
| Thus(\mathcal{S}\mathcal{T})                   | u=\mathcal{T} (\mathcal{S}                    | u),asdesired. |      |         |             |     |
| (e) Supposeu\in\mathcal{V}.            | Then                      |               |      |         |             |     |
\langle\mathcal{I}u,v\rangle=\langleu,v\rangle.
∗
Thus\mathcal{I} v=v,asdesired.
$$(f) Suppose\mathcal{T}isinvertible. Takeadjointsofbothsidesoftheequation\mathcal{T}-1\mathcal{T} =\mathcal{I},$$
∗ (\mathcal{T}-1) ∗
then use (d) and (e) to show that \mathcal{T} = \mathcal{I}. Similarly, the equation
|     |     | ∗ ∗ |     | ∗   |     | ∗   |
| --- | --- | --- | --- | --- | --- | --- |
\mathcal{T}\mathcal{T}-1 = \mathcal{I} implies (\mathcal{T}-1) \mathcal{T} = \mathcal{I}. Thus (\mathcal{T}-1) is the inverse of \mathcal{T} , as
desired.
∗
| If\mathbf{F} = | \mathbf{R},thenthemap\mathcal{T} | ↦ \mathcal{T} isalinearmapfromℒ(\mathcal{V},\mathcal{W})toℒ(\mathcal{W},\mathcal{V}), |     |     |     |     |
| ----- | ------------- | ----------------------------------- | --- | --- | --- | --- |
asfollowsfrom(a)and(b)oftheresultabove. However,if\mathbf{F} =\mathbf{C},thenthismap
isnotlinearbecauseofthecomplexconjugatethatappearsin(b).

| --- | --- | ---------------------------------------- | --- | --- | --- |
Thenextresultshowstherelationshipbetweenthenullspaceandtherangeof
alinearmapanditsadjoint.
∗
| 7.6 | nullspaceandrangeof | \mathcal{T}   |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
\inℒ(\mathcal{V},\mathcal{W}).
| Suppose\mathcal{T} |     | Then |     |     |     |
| -------- | --- | ---- | --- | --- | --- |
∗ =(range\mathcal{T})⟂;
$$(a) null\mathcal{T}$$
| (b) | range\mathcal{T} ∗ =(null\mathcal{T})⟂; |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
∗ )⟂;
| (c)   | null\mathcal{T} =(range\mathcal{T}       |         |      |     |     |
| ----- | -------------------- | ------- | ---- | --- | --- |
| (d)   | range\mathcal{T} =(null\mathcal{T}       | ∗ )⟂.   |      |     |     |
| Proof | Webeginbyproving(a). | Letw\in\mathcal{W}. | Then |     |     |
|       |                      | ∗ ∗     |      |     |     |
|       | w\innull\mathcal{T}              | ⟺ \mathcal{T} w=0 |      |     |     |
∗
|     |     | ⟺ \langlev,\mathcal{T} | w\rangle=0forallv\in\mathcal{V} |     |     |
| --- | --- | ------ | ------------- | --- | --- |
⟺ \langle\mathcal{T}v,w\rangle=0forallv\in\mathcal{V}
w\in(range\mathcal{T})⟂.
⟺
| Thusnull\mathcal{T} | ∗ =(range\mathcal{T})⟂,proving(a). |     |     |     |     |
| --------- | ------------------------ | --- | --- | --- | --- |
Ifwetaketheorthogonalcomplementofbothsidesof(a),weget(d),where
we haveused 6.52. Replacing \mathcal{T} with \mathcal{T} ∗ in (a) gives(c), where wehave used
∗
| 7.5(c). | Finally,replacing\mathcal{T} | with\mathcal{T} in(d)gives(b). |     |     |     |
| ------- | ------------------ | -------------------- | --- | --- | --- |
Aswewillsoonsee,thenextdefinitionisintimatelyconnectedtothematrix
oftheadjointofalinearmap.
∗
| 7.7 | definition: conjugatetranspose,\mathcal{A} |     |     |     |     |
| --- | -------------------------------- | --- | --- | --- | --- |
The conjugate transpose of an m-by-n matrix \mathcal{A} is the n-by-m matrix \mathcal{A} ∗
obtainedbyinterchangingtherowsandcolumnsandthentakingthecomplex
conjugateofeachentry. Inotherwords,ifj \in {1,…,n}andk \in {1,…,m},
then
|     |     | (\mathcal{A} ∗ ) | =\mathcal{A} . |     |     |
| --- | --- | ------ | ---- | --- | --- |
j,k k,j
| 7.8 | example: conjugatetransposeofa2-by-3matrix |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- |
Theconjugatetransposeofthe2-by-3
|         |        |              | If a matrix | \mathcal{A} has only       | real entries, |
| ------- | ------ | ------------ | ----------- | ---------------- | ------------- |
|         | 2 3+4i | 7            |             |                  |               |
|         |        |              | then \mathcal{A} ∗    | = \mathcal{A}t, where \mathcal{A}t   | denotes the   |
| matrix( |        | )isthe3-by-2 |             |                  |               |
|         | 6 5    | 8i           |             |                  |               |
|         |        |              | transpose   | of \mathcal{A} (the matrix | obtained      |
matrix
|     |        |        | by interchanging | the rows | and the |
| --- | ------ | ------ | ---------------- | -------- | ------- |
|     | ⎛      | ⎞      | columns).        |          |         |
|     | ⎜      | ⎟      |                  |          |         |
|     | ⎜ 3-4i | 5 ⎟ ⎟. |                  |          |         |
⎜
|     | 7 -8i |     |     |     |     |
| --- | ----- | --- | --- | --- | --- |
|     | ⎝     | ⎠   |     |     |     |

232 Chapter 7 Operatorson Inner Product Spaces
Thenextresultshowshowtocompute
Theadjointofalinearmapdoesnot
∗
the matrix of \mathcal{T} from the matrix of \mathcal{T}.
depend on a choice of basis. Thus
Caution: Withrespecttononorthonor- we frequently emphasize adjoints of
∗
malbases,thematrixof\mathcal{T} doesnotnec- linearmapsinsteadoftransposesor
essarilyequaltheconjugatetransposeof conjugatetransposesofmatrices.
thematrixof\mathcal{T}.
∗
7.9 matrixof \mathcal{T} equalsconjugatetransposeofmatrixof \mathcal{T}
Let \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Suppose e ,…,e is an orthonormal basis of \mathcal{V} and
1 n
f ,…, f isanorthonormalbasisof\mathcal{W}. Thenℳ(\mathcal{T} ∗,(f ,…, f ),(e ,…,e ))
1 m 1 m 1 n
istheconjugatetransposeofℳ(\mathcal{T},(e ,…,e ),(f ,…, f )). Inotherwords,
1 n 1 m
ℳ(\mathcal{T} ∗ )=(ℳ(\mathcal{T})) ∗ .
Proof In this proof, we will write ℳ(\mathcal{T}) and ℳ(\mathcal{T} ∗ ) instead of the longer
expressionsℳ(\mathcal{T},(e ,…,e ),(f ,…, f ))andℳ(\mathcal{T} ∗,(f ,…, f ),(e ,…,e )).
1 n 1 m 1 m 1 n
Recall that we obtain the kth column of ℳ(\mathcal{T}) by writing \mathcal{T}e as a linear
k
combinationofthe f’s;thescalarsusedinthislinearcombinationthenbecome
j
thekth columnofℳ(\mathcal{T}). Because f ,…, f isanorthonormalbasisof\mathcal{W}, we
1 m
knowhowtowrite\mathcal{T}e asalinearcombinationofthe f’s[see6.30(a)]:
k j
\mathcal{T}e =\langle\mathcal{T}e , f \ranglef +⋯+\langle\mathcal{T}e , f \ranglef .
k k 1 1 k m m
Thus
theentryinrowj,columnk,ofℳ(\mathcal{T})is\langle\mathcal{T}e , f\rangle.
k j
In the statement above, replace \mathcal{T} with \mathcal{T} ∗ and interchange e ,…,e and
1 n
f ,…, f . Thisshowsthattheentryinrowj,columnk,ofℳ(\mathcal{T} ∗ )is\langle\mathcal{T} ∗ f ,e\rangle,
1 m k j
whichequals\langlef ,\mathcal{T}e\rangle,whichequals\langle\mathcal{T}e, f \rangle,whichequalsthecomplexconjugate
k j j k
oftheentryinrowk,columnj,ofℳ(\mathcal{T}). Thusℳ(\mathcal{T} ∗ )=(ℳ(\mathcal{T})) ∗ .
The Rieszrepresentationtheoremasstatedin6.58providesanidentificationof
\mathcal{V}withitsdualspace\mathcal{V}′definedin3.110. Underthisidentification,theorthogonal
complement\mathcal{U}⟂ ofasubset\mathcal{U} \subseteq\mathcal{V} correspondstotheannihilator\mathcal{U}0 of\mathcal{U}. If\mathcal{U}
isasubspaceof\mathcal{V},thentheformulasforthedimensionsof\mathcal{U}⟂ and\mathcal{U}0 become
identicalunderthisidentification—see3.125and6.51.
Suppose\mathcal{T}∶ \mathcal{V} \rightarrow \mathcal{W} isalinearmap.
Becauseorthogonalcomplementsand
Undertheidentificationof\mathcal{V}with\mathcal{V}′and
adjointsareeasiertodealwiththan
the identification of \mathcal{W} with \mathcal{W}′, the ad- annihilators and dual maps, there is
joint map \mathcal{T}
∗∶
\mathcal{W} \rightarrow \mathcal{V} corresponds to no need to work with annihilators
the dual map \mathcal{T}′∶ \mathcal{W}′ \rightarrow \mathcal{V}′ defined in anddualmapsinthecontextofinner
3.118,as Exercise32asksyoutoverify. productspaces.
Underthisidentification,theformulasfor
∗ ∗
null\mathcal{T} andrange\mathcal{T} [7.6(a)and(b)]thenbecomeidenticaltotheformulasfor
null\mathcal{T}′andrange\mathcal{T}′[3.128(a)and3.130(b)]. Furthermore,thetheoremaboutthe
matrixof\mathcal{T} ∗ (7.9)isanalogoustothetheoremaboutthematrixof\mathcal{T}′ (3.132).

| --- | --- | --- | --------- | ------------------------------ | --- |
| Self-Adjoint | Operators |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
Now we switch our attention to operators on inner product spaces. Instead of
consideringlinearmapsfrom\mathcal{V} to\mathcal{W},wewillfocusonlinearmapsfrom\mathcal{V} to\mathcal{V};
recallthatsuchlinearmapsarecalledoperators.
self-adjoint
**7.10 定义：** ∗
| Anoperator\mathcal{T} |     | \inℒ(\mathcal{V})iscalledself-adjoint |     |     | if\mathcal{T} =\mathcal{T} . |
| ----------- | --- | ------------------------- | --- | --- | -------- |
If\mathcal{T} \inℒ(\mathcal{V})ande ,…,e isanorthonormalbasisof\mathcal{V},then\mathcal{T} isself-adjoint
|                   |     |     | 1 n            |     | ∗                          |
| ----------------- | --- | --- | -------------- | --- | -------------------------- |
| ifandonlyifℳ(\mathcal{T},(e |     |     | ,…,e ))=ℳ(\mathcal{T},(e |     | ,…,e )) ,asfollowsfrom7.9. |
|                   |     |     | 1 n            |     | 1 n                        |
**7.11 例：** determiningwhether \mathcal{T} isself-adjointfromitsmatrix
Supposec \in\mathbf{F} and\mathcal{T} istheoperatoron\mathbf{F}2 whosematrix(withrespecttothe
standardbasis)is
|              |     |                                     |        |     | 2 c |
| ------------ | --- | ----------------------------------- | ------ | --- | --- |
|              |     |                                     | ℳ(\mathcal{T})=( |     | ).  |
|              |     |                                     |        |     | 3 7 |
| Thematrixof\mathcal{T} |     | ∗ (withrespecttothestandardbasis)is |        |     |     |
|              |     |                                     |        | ∗   | 2 3 |
|              |     |                                     | ℳ(\mathcal{T}    | )=( | ).  |
|              |     |                                     |        |     | c 7 |
∗
Thusℳ(\mathcal{T})=ℳ(\mathcal{T} )ifandonlyifc =3. Hencetheoperator\mathcal{T} isself-adjoint
| ifandonlyifc | =3. |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- |
Agoodanalogytokeepinmindisthattheadjointonℒ(\mathcal{V})playsarolesimilar
tothatofthecomplexconjugateon\mathbf{C}. Acomplexnumberzisrealifandonlyif
∗
$$z=z;thusaself-adjointoperator(\mathcal{T} =\mathcal{T} )isanalogoustoarealnumber.$$
Wewillseethattheanalogydiscussed
Anoperator\mathcal{T} \inℒ(\mathcal{V})isself-adjoint
aboveisreflectedinsomeimportantpropifandonlyif
ertiesofself-adjointoperators,beginning
\langle\mathcal{T}v,w\rangle=\langlev,\mathcal{T}w\rangle
witheigenvaluesinthenextresult.
| If \mathbf{F} =               | \mathbf{R}, then  | by  | definition | every     | forallv,w\in\mathcal{V}. |
| -------------------- | -------- | --- | ---------- | --------- | ------------ |
| eigenvalue           | is real, | so  | the next   | result is |              |
| interestingonlywhen\mathbf{F} |          |     | =\mathbf{C}.        |           |              |
7.12 eigenvaluesofself-adjointoperators
Everyeigenvalueofaself-adjointoperatorisreal.
| Suppose\mathcal{T} |     | isaself-adjointoperatoron\mathcal{V}. |     |     | Let \lambdabeaneigenvalueof\mathcal{T}, |
| -------- | --- | --------------------------- | --- | --- | ----------------------- |
Proof
| andletvbeanonzerovectorin\mathcal{V} |     |     |     | suchthat\mathcal{T}v= | \lambdav. Then |
| -------------------------- | --- | --- | --- | ----------- | -------- |
\lambda‖v‖2 =\langle\lambdav,v\rangle=\langle\mathcal{T}v,v\rangle=\langlev,\mathcal{T}v\rangle=\langlev,\lambdav\rangle= \lambda‖v‖2.
| Thus \lambda= | \lambda,whichmeansthat |     |     | \lambdaisreal,asdesired. |     |
| ------- | ---------------- | --- | --- | ------------------ | --- |

| --- | -------- | ----------------------------- | --- | --- | --- |
Thenextresultisfalseforrealinnerproductspaces. Asanexample,consider
the operator \mathcal{T} \in ℒ(\mathbf{R}2) that is a counterclockwise rotation of 90\circ around the
Noticethat\mathcal{T}visorthogonaltovforeveryv\in\mathbf{R}2,
origin;thus\mathcal{T}(x,y)=(-y,x).
| eventhough\mathcal{T} | \neq0.                             |     |     |              |      |
| ----------- | ------------------------------- | --- | --- | ------------ | ---- |
| 7.13        | \mathcal{T}visorthogonaltovforallv        |     | ⟺ \mathcal{T} | =0(assuming\mathbf{F} | =\mathbf{C})  |
| Suppose\mathcal{V}    | isacomplexinnerproductspaceand\mathcal{T} |     |     | \inℒ(\mathcal{V}).       | Then |
\langle\mathcal{T}v,v\rangle=0foreveryv\in\mathcal{V}
|     |     |     |     | ⟺ \mathcal{T} =0. |     |
| --- | --- | --- | --- | ------- | --- |
Ifu,w\in\mathcal{V},then
Proof
\langle\mathcal{T}(u+w),u+w\rangle-\langle\mathcal{T}(u-w),u-w\rangle
\langle\mathcal{T}u,w\rangle=
\langle\mathcal{T}(u+iw),u+iw\rangle-\langle\mathcal{T}(u-iw),u-iw\rangle
|     |     | +   |     |     | i,  |
| --- | --- | --- | --- | --- | --- |
ascanbeverifiedbycomputingtherightside. Notethateachtermontheright
sideisoftheform\langle\mathcal{T}v,v\rangleforappropriatev\in\mathcal{V}.
Nowsuppose\langle\mathcal{T}v,v\rangle=0foreveryv\in\mathcal{V}.
Thentheequationaboveimplies
that\langle\mathcal{T}u,w\rangle=0forallu,w\in\mathcal{V},whichthenimpliesthat\mathcal{T}u=0foreveryu\in\mathcal{V}
| (takew=\mathcal{T}u). | Hence\mathcal{T} | =0,asdesired. |     |     |     |
| ----------- | ------ | ------------- | --- | --- | --- |
Thenextresultisfalseforrealinner
Thenextresultprovidesanothergood
productspaces,asshownbyconsidering exampleofhowself-adjointoperators
anyoperatoronarealinnerproductspace
behavelikerealnumbers.
thatisnotself-adjoint.
|          | \langle\mathcal{T}v,v\rangleisrealforallv             |     | isself-adjoint | (assuming\mathbf{F}   | =\mathbf{C})  |
| -------- | ------------------------------- | --- | -------------- | ------------ | ---- |
| 7.14     |                                 | ⟺   | \mathcal{T}              |              |      |
| Suppose\mathcal{V} | isacomplexinnerproductspaceand\mathcal{T} |     |                | \inℒ(\mathcal{V}).       | Then |
|          | \mathcal{T} isself-adjoint                | ⟺   | \langle\mathcal{T}v,v\rangle\in\mathbf{R}       | foreveryv\in\mathcal{V}. |      |
Proof Ifv\in\mathcal{V},then
|      |     | ∗            | ∗          |     |     |
| ---- | --- | ------------ | ---------- | --- | --- |
| 7.15 |     | \langle\mathcal{T} v,v\rangle=\langlev,\mathcal{T} | v\rangle=\langle\mathcal{T}v,v\rangle. |     |     |
Now
|     | \mathcal{T} isself-adjoint | ⟺ \mathcal{T}-\mathcal{T} | ∗ =0 |     |     |
| --- | ---------------- | ----- | ---- | --- | --- |
∗
|     |     | ⟺ \langle(\mathcal{T}-\mathcal{T} | )v,v\rangle=0foreveryv\in\mathcal{V} |     |     |
| --- | --- | ------- | ------------------ | --- | --- |
⟺ \langle\mathcal{T}v,v\rangle-\langle\mathcal{T}v,v\rangle=0foreveryv\in\mathcal{V}
|     |     | ⟺ \langle\mathcal{T}v,v\rangle\in\mathbf{R} |     | foreveryv\in\mathcal{V}, |     |
| --- | --- | ---------- | --- | ------------ | --- |
wherethesecondequivalencefollowsfrom7.13asappliedto\mathcal{T} -\mathcal{T} ∗ andthe
thirdequivalencefollowsfrom7.15.

| --- | --- | ---------------------------------------- | --- |
Onarealinnerproductspace\mathcal{V},anonzerooperator\mathcal{T}mightsatisfy\langle\mathcal{T}v,v\rangle=0
forallv\in\mathcal{V}. However,thenextresultshowsthatthiscannothappenforaselfadjointoperator.
|          | self-adjointand             | \langle\mathcal{T}v,v\rangle=0forallv |         |
| -------- | --------------------------- | --------------- | ------- |
| 7.16 \mathcal{T}   |                             |                 | ⟺ \mathcal{T} =0  |
| Suppose\mathcal{T} | isaself-adjointoperatoron\mathcal{V}. |                 | Then    |
|          | \langle\mathcal{T}v,v\rangle=0foreveryv\in\mathcal{V}         |                 | ⟺ \mathcal{T} =0. |
Proof Wehavealreadyprovedthis(withoutthehypothesisthat\mathcal{T}isself-adjoint)
when\mathcal{V} isacomplexinnerproductspace(see7.13). Thuswecanassumethat\mathcal{V}
| isarealinnerproductspace. |     | Ifu,w\in\mathcal{V},then |     |
| ------------------------- | --- | ------------ | --- |
\langle\mathcal{T}(u+w),u+w\rangle-\langle\mathcal{T}(u-w),u-w\rangle
\langle\mathcal{T}u,w\rangle= ,
7.17
ascanbeprovedbycomputingtherightsideusingtheequation
\langle\mathcal{T}w,u\rangle=\langlew,\mathcal{T}u\rangle=\langle\mathcal{T}u,w\rangle,
wherethefirstequalityholdsbecause\mathcal{T} isself-adjointandthesecondequality
holdsbecauseweareworkinginarealinnerproductspace.
| Nowsuppose\langle\mathcal{T}v,v\rangle |     | = 0foreveryv | \in \mathcal{V}. Becauseeachtermontheright |
| ---------------- | --- | ------------ | ------------------------------ |
sideof7.17isoftheform\langle\mathcal{T}v,v\rangleforappropriatev,thisimpliesthat\langle\mathcal{T}u,w\rangle=0
forallu,w\in\mathcal{V}. Thisimpliesthat\mathcal{T}u=0foreveryu\in\mathcal{V} (takew=\mathcal{T}u). Hence
=0,asdesired.
\mathcal{T}
| Normal | Operators |     |     |
| ------ | --------- | --- | --- |
normal
**7.18 定义：** • Anoperatoronaninnerproductspaceiscallednormalifitcommuteswith
itsadjoint.
| • Inotherwords,\mathcal{T} |     | \inℒ(\mathcal{V})isnormalif\mathcal{T}\mathcal{T} | ∗ =\mathcal{T} ∗ \mathcal{T}. |
| ---------------- | --- | ----------------- | --------- |
∗
Everyself-adjointoperatorisnormal,becauseif\mathcal{T} isself-adjointthen\mathcal{T} =\mathcal{T}
∗
| andhence\mathcal{T}     | commuteswith\mathcal{T}                            | .   |     |
| ------------- | ---------------------------------------- | --- | --- |
| 7.19 example: | anoperatorthatisnormalbutnotself-adjoint |     |     |
Let\mathcal{T} betheoperatoron\mathbf{F}2 whosematrix(withrespecttothestandardbasis)
is
2 -3
|     |     | (   | ).  |
| --- | --- | --- | --- |
3 2
Thus\mathcal{T}(w,z)=(2w-3z,3w+2z).

| -------- | ----------------------------- | --- | --- | --- |
Thisoperator\mathcal{T}isnotself-adjointbecausetheentryinrow2,column1(which
equals3)doesnotequalthecomplexconjugateoftheentryinrow1,column2
$$(whichequals-3).$$
| Thematrixof\mathcal{T}\mathcal{T} | ∗ equals |     |     |      |
| ------------- | -------- | --- | --- | ---- |
| 2 -3          |          | 2 3 |     | 13 0 |
$$),$$
| (   | )(  |      | whichequals | ( ). |
| --- | --- | ---- | ----------- | ---- |
| 3   | 2   | -3 2 |             | 0 13 |
∗
Similarly,thematrixof\mathcal{T} \mathcal{T} equals
| 2   | 3   | 2 -3 |                | 13 0 |
| --- | --- | ---- | -------------- | ---- |
| (   | )(  |      | ), whichequals | ( ). |
| -3  | 2   | 3 2  |                | 0 13 |
| ∗   | ∗   |      |                | ∗ ∗  |
Because\mathcal{T}\mathcal{T} and\mathcal{T} \mathcal{T} havethesamematrix,weseethat\mathcal{T}\mathcal{T} =\mathcal{T} \mathcal{T}. Thus\mathcal{T} is
normal.
Inthenextsectionwewillseewhynormaloperatorsareworthyofspecial
attention. Thenextresultprovidesausefulcharacterizationofnormaloperators.
| 7.20 \mathcal{T} isnormalifandonlyif |      | \mathcal{T}vand | \mathcal{T} ∗ vhavethesamenorm |     |
| -------------------------- | ---- | ----- | -------------------- | --- |
| Suppose\mathcal{T} \inℒ(\mathcal{V}).            | Then |       |                      |     |
∗
| \mathcal{T} isnormal |     | ⟺ ‖\mathcal{T}v‖=‖\mathcal{T} | v‖foreveryv\in\mathcal{V}. |     |
| ---------- | --- | --------- | -------------- | --- |
|            |     | ∗            | ∗                  |               |
| ---------- | --- | ------------ | ------------------ | ------------- |
| \mathcal{T} isnormal | ⟺   | \mathcal{T} \mathcal{T}-\mathcal{T}\mathcal{T}       | =0                 |               |
|            |     | ∗            | ∗                  |               |
|            | ⟺   | \langle(\mathcal{T} \mathcal{T}-\mathcal{T}\mathcal{T}     | )v,v\rangle=0foreveryv\in\mathcal{V} |               |
|            |     | ∗            | ∗                  |               |
|            | ⟺   | \langle\mathcal{T} \mathcal{T}v,v\rangle=\langle\mathcal{T}\mathcal{T} | v,v\rangleforeveryv\in\mathcal{V}    |               |
|            |     | \langle\mathcal{T}v,\mathcal{T}v\rangle=\langle\mathcal{T}   | ∗ v,\mathcal{T} ∗            |               |
|            | ⟺   |              |                    | v\rangleforeveryv\in\mathcal{V} |
|            |     |              | ∗ v∥2              |               |
|            | ⟺   | ‖\mathcal{T}v‖2        | =∥\mathcal{T} foreveryv\in\mathcal{V}    |               |
∗
|     | ⟺   | ‖\mathcal{T}v‖=∥\mathcal{T} | v∥foreveryv\in\mathcal{V}, |     |
| --- | --- | ------- | -------------- | --- |
whereweused7.16toestablishthesecondequivalence(notethattheoperator
∗ ∗
\mathcal{T} \mathcal{T}-\mathcal{T}\mathcal{T} isself-adjoint).
Thenextresultpresentsseveralconsequencesoftheresultabove. Compare
$$(e)ofthenextresultto Exercise3. Thatexercisestatesthattheeigenvaluesof$$
the adjoint of each operator are equal (as a set) to the complex conjugates of
theeigenvaluesoftheoperator. Theexercisesaysnothingabouteigenvectors,
becauseanoperatoranditsadjointmayhavedifferenteigenvectors. However,
$$(e)ofthenextresultimpliesthatanormaloperatoranditsadjointhavethesame$$
eigenvectors.

| --- | --- | --------- | --- | --- | ------------------------------ | --- |
range,nullspace,andeigenvectorsofanormaloperator
7.21
| Suppose\mathcal{T} |     | \inℒ(\mathcal{V})isnormal. |     | Then |     |     |
| -------- | --- | -------------- | --- | ---- | --- | --- |
∗
| (a) | null\mathcal{T} | =null\mathcal{T} ; |     |     |     |     |
| --- | ----- | -------- | --- | --- | --- | --- |
∗
| (b) | range\mathcal{T} | =range\mathcal{T} | ;   |     |     |     |
| --- | ------ | ------- | --- | --- | --- | --- |
$$(c) \mathcal{V} =null\mathcal{T}\oplusrange\mathcal{T};$$
| (d) | \mathcal{T}-    | \lambda\mathcal{I} isnormalforevery |     | \lambda\in\mathbf{F}; |                |          |
| --- | ----- | ------------------- | --- | ---- | -------------- | -------- |
| (e) | ifv\in\mathcal{V} | and \lambda\in\mathbf{F},then\mathcal{T}v=     |     |      | \lambdavifandonlyif\mathcal{T} | ∗ v= \lambdav. |
Proof
| (a) | Supposev\in\mathcal{V}. | Then      |        |     |             |              |
| --- | ----------- | --------- | ------ | --- | ----------- | ------------ |
|     |             | v\innull\mathcal{T} ⟺ | ‖\mathcal{T}v‖=0 |     | ⟺ ∥\mathcal{T} ∗ v∥=0 | ⟺ v\innull\mathcal{T} ∗, |
∗
wherethemiddleequivalenceabovefollowsfrom7.20. Thusnull\mathcal{T} =null\mathcal{T} .
$$(b) Wehave$$
|     |     |        |         |     | ∗ )⟂ =(null\mathcal{T})⟂ | ∗,      |
| --- | --- | ------ | ------- | --- | -------------- | ------- |
|     |     | range\mathcal{T} | =(null\mathcal{T} |     |                | =range\mathcal{T} |
wherethefirstequalitycomesfrom7.6(d),thesecondequalitycomesfrom
$$(a)inthisresult,andthethirdequalitycomesfrom7.6(b).$$
$$(c) Wehave$$
|     |     | =(null\mathcal{T})\oplus(null\mathcal{T})⟂ |     |               |     | ∗              |
| --- | --- | ----------------- | --- | ------------- | --- | -------------- |
|     | \mathcal{V}   |                   |     | =null\mathcal{T}\oplusrange\mathcal{T} |     | =null\mathcal{T}\oplusrange\mathcal{T}, |
wherethefirstequalitycomesfrom6.49,thesecondequalitycomesfrom
7.6(b),andthethirdequalitycomesfrom(b)inthisresult.
| (d) | Suppose | \lambda\in\mathbf{F}. Then |        |     |             |            |
| --- | ------- | --------- | ------ | --- | ----------- | ---------- |
|     |         |           |        |     | ∗           | ∗          |
|     |         | (\mathcal{T}-       | \lambda\mathcal{I})(\mathcal{T}- | \lambda\mathcal{I}) | =(\mathcal{T}- \lambda\mathcal{I})(\mathcal{T}  | - \lambda\mathcal{I})      |
|     |         |           |        |     | ∗           | ∗+|\lambda|2\mathcal{I}    |
|     |         |           |        |     | =\mathcal{T}\mathcal{T} - \lambda\mathcal{T}-   | \lambda\mathcal{T}         |
|     |         |           |        |     | =\mathcal{T} ∗ \mathcal{T}- \lambda\mathcal{T}- | \lambda\mathcal{T} ∗+|\lambda|2\mathcal{I} |
∗
|     |     |     |     |     | =(\mathcal{T} - \lambda\mathcal{I})(\mathcal{T}- | \lambda\mathcal{I}) |
| --- | --- | --- | --- | --- | ------------ | --- |
∗
|     |            |                            |            |                         | =(\mathcal{T}- \lambda\mathcal{I})   | (\mathcal{T}- \lambda\mathcal{I}).     |
| --- | ---------- | -------------------------- | ---------- | ----------------------- | ---------- | ------------ |
|     | Thus\mathcal{T}-     | \lambda\mathcal{I} commuteswithitsadjoint. |            |                         | Hence\mathcal{T}-    | \lambda\mathcal{I} isnormal. |
| (e) | Supposev\in\mathcal{V} | and                        | \lambda\in\mathbf{F}.       | Then(d)and7.20implythat |            |              |
|     |            |                            |            |                         | ∗          | ∗            |
|     |            | ‖(\mathcal{T}-                       | \lambda\mathcal{I})v‖=∥(\mathcal{T}- |                         | \lambda\mathcal{I}) v∥=∥(\mathcal{T} | - \lambda\mathcal{I})v∥.     |
Thus‖(\mathcal{T} - \lambda\mathcal{I})v‖ = 0ifandonlyif∥(\mathcal{T} ∗ - \lambda\mathcal{I})v∥ = 0. Hence\mathcal{T}v = \lambdavif
∗
|     | andonlyif\mathcal{T} | v= \lambdav. |     |     |     |     |
| --- | ---------- | ------ | --- | --- | --- | --- |

| -------- | ----------------------------- | --- | --- | --- |
Becauseeveryself-adjointoperatorisnormal,thenextresultappliesinparticulartoself-adjointoperators.
7.22 orthogonaleigenvectorsfornormaloperators
Suppose \mathcal{T} \in ℒ(\mathcal{V}) is normal. Then eigenvectors of \mathcal{T} corresponding to
distincteigenvaluesareorthogonal.
Proof Suppose \alpha,\beta are distinct eigenvalues of \mathcal{T}, with corresponding eigenvectors u,v. Thus \mathcal{T}u = \alphau and \mathcal{T}v = \betav. From 7.21(e) we have \mathcal{T} ∗ v = \betav.
Thus
$$(\alpha-\beta)\langleu,v\rangle=\langle\alphau,v\rangle-\langleu,\betav\rangle$$
∗
|     |     | =\langle\mathcal{T}u,v\rangle-\langleu,\mathcal{T} | v\rangle  |     |
| --- | --- | ------------ | --- | --- |
=0.
Because \alpha \neq \beta, the equation above implies that \langleu,v\rangle = 0. Thus u and v are
orthogonal,asdesired.
Asstatedhere,thenextresultmakessenseonlywhen\mathbf{F} =\mathbf{C}. However,see
| Exercise12foraversionthatmakessensewhen\mathbf{F} |     |     | =\mathbf{C} andwhen\mathbf{F} | =\mathbf{R}. |
| ---------------------------------------- | --- | --- | ----------- | --- |
Suppose \mathbf{F} = \mathbf{C} and \mathcal{T} \in ℒ(\mathcal{V}). Under the analogy between ℒ(\mathcal{V}) and \mathbf{C},
withtheadjointonℒ(\mathcal{V})playingasimilarroletothatofthecomplexconjugateon
\mathbf{C},theoperators\mathcal{A}and\mathcal{B}asdefinedby7.24correspondtotherealandimaginary
partsof\mathcal{T}. Thustheinformaltitleoftheresultbelowshouldmakesense.
| 7.23 \mathcal{T} isnormal | ⟺ therealandimaginarypartsof |     | \mathcal{T} commute |     |
| --------------- | ---------------------------- | --- | --------- | --- |
Suppose\mathbf{F} = \mathbf{C} and\mathcal{T} \in ℒ(\mathcal{V}). Then\mathcal{T} isnormalifandonlyifthereexist
=\mathcal{A}+i\mathcal{B}.
commutingself-adjointoperators\mathcal{A}and\mathcal{B}suchthat\mathcal{T}
| Proof Firstsuppose\mathcal{T} | isnormal. | Let |     |     |
| ------------------- | --------- | --- | --- | --- |
|                     | \mathcal{T}+\mathcal{T}       | ∗   | ∗   |     |
\mathcal{T}-\mathcal{T}
| 7.24 | \mathcal{A}=  | and \mathcal{B}= | .   |     |
| ---- | --- | ------ | --- | --- |
|      | 2   |        | 2i  |     |
Then\mathcal{A}and\mathcal{B}areself-adjointand\mathcal{T} =\mathcal{A}+i\mathcal{B}. Aquickcomputationshowsthat
|     |     | ∗   | ∗   |     |
| --- | --- | --- | --- | --- |
\mathcal{T} \mathcal{T}-\mathcal{T}\mathcal{T}
| 7.25 | \mathcal{A}\mathcal{B}-\mathcal{B}\mathcal{A}= |     | .   |     |
| ---- | ------ | --- | --- | --- |
2i
Because \mathcal{T} is normal, the right side of the equation above equals 0. Thus the
operators\mathcal{A}and\mathcal{B}commute,asdesired.
Toprovetheimplicationintheotherdirection,nowsupposethereexistcom-
∗
mutingself-adjointoperators\mathcal{A}and\mathcal{B}suchthat\mathcal{T} =\mathcal{A}+i\mathcal{B}. Then\mathcal{T} =\mathcal{A}-i\mathcal{B}.
Addingthelasttwoequationsandthendividingby2producestheequationfor\mathcal{A}
in7.24. Subtractingthelasttwoequationsandthendividingby2iproducesthe
equationfor\mathcal{B}in7.24. Now7.24implies7.25. Because\mathcal{B}and\mathcal{A}commute,7.25
| impliesthat\mathcal{T} isnormal,asdesired. |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- |

| --- | --- | --------- | --- | ------------------------------ | --- | --- | --- | --- |
| Exercises                     | 7A       |     |           |         |     |          |          |     |
| ----------------------------- | -------- | --- | --------- | ------- | --- | -------- | -------- | --- |
| 1 Supposenisapositiveinteger. |          |     |           | Define\mathcal{T} |     | \inℒ(\mathbf{F}n)by |          |     |
|                               |          |     | \mathcal{T}(z ,…,z  | )=(0,z  |     | ,…,z     | ).       |     |
|                               |          |     | 1         | n       |     | 1 n-1    |          |     |
| Findaformulafor\mathcal{T}              |          |     | ∗ (z ,…,z | ).      |     |          |          |     |
|                               |          |     | 1         | n       |     |          |          |     |
| 2 Suppose\mathcal{T}                    | \inℒ(\mathcal{V},\mathcal{W}). |     | Provethat |         |     |          |          |     |
|                               | \mathcal{T}        | =0  | ⟺ \mathcal{T} ∗     | =0 ⟺    | \mathcal{T} ∗ | \mathcal{T} =0 ⟺   | \mathcal{T}\mathcal{T} ∗ =0. |     |
\inℒ(\mathcal{V})and
| 3 Suppose\mathcal{T} |     |     | \lambda\in\mathbf{F}. | Provethat |     |     |     |     |
| ---------- | --- | --- | ---- | --------- | --- | --- | --- | --- |
∗
|            | \lambdaisaneigenvalueof\mathcal{T} |                   |     |                 | ⟺ \lambdaisaneigenvalueof\mathcal{T} |                   |     | .   |
| ---------- | ------------------ | ----------------- | --- | --------------- | -------------------- | ----------------- | --- | --- |
| 4 Suppose\mathcal{T} | \inℒ(\mathcal{V})and\mathcal{U}          |                   |     | isasubspaceof\mathcal{V}. |                      | Provethat         |     |     |
|            |                    |                   |     |                 | \mathcal{U}⟂                   |                   |     | ∗   |
|            | \mathcal{U}                  | isinvariantunder\mathcal{T} |     |                 | ⟺                    | isinvariantunder\mathcal{T} |     | .   |
5 Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Supposee ,…,e isanorthonormalbasisof\mathcal{V} and
1 n
| f ,…,         | f isanorthonormalbasisof\mathcal{W}. |          |          |                                       | Provethat |         |       |     |
| ------------- | -------------------------- | -------- | -------- | ------------------------------------- | --------- | ------- | ----- | --- |
| 1             | m                          |          |          |                                       |           |         |       |     |
|               |                            | ‖2+⋯+‖\mathcal{T}e |          | ‖2                                    | ∗         | ∥2+⋯+∥\mathcal{T} | ∗ ∥2. |     |
|               |                            | ‖\mathcal{T}e      |          |                                       | =∥\mathcal{T}       | f       | f     |     |
|               |                            | 1        |          | n                                     |           | 1       | m     |     |
| Thenumbers‖\mathcal{T}e |                            |          | ‖2,…,‖\mathcal{T}e | ‖2intheequationabovedependontheortho- |           |         |       |     |
|               |                            | 1        |          | n                                     |           |         |       |     |
,…,e
| normalbasise |      | 1                                                  | n ,buttherightsideoftheequationdoesnotdepend |     |     |     |     |     |
| ------------ | ---- | -------------------------------------------------- | -------------------------------------------- | --- | --- | --- | --- | --- |
| one          | ,…,e | . Thustheequationaboveshowsthatthesumontheleftside |                                              |     |     |     |     |     |
1 n
| doesnotdependonwhichorthonormalbasise |          |     |           |     |     | ,…,e | isused. |     |
| ------------------------------------- | -------- | --- | --------- | --- | --- | ---- | ------- | --- |
|                                       |          |     |           |     |     | 1    | n       |     |
| 6 Suppose\mathcal{T}                            | \inℒ(\mathcal{V},\mathcal{W}). |     | Provethat |     |     |      |         |     |
∗
| (a) \mathcal{T}          | isinjective  | ⟺                      | \mathcal{T}     | issurjective; |     |     |     |     |
| -------------- | ------------ | ---------------------- | ----- | ------------- | --- | --- | --- | --- |
| (b) \mathcal{T}          | issurjective |                        | ⟺ \mathcal{T} ∗ | isinjective.  |     |     |     |     |
| 7 Provethatif\mathcal{T} |              | \inℒ(\mathcal{V},\mathcal{W}),then           |       |               |     |     |     |     |
| (a) dimnull\mathcal{T}   |              | ∗ =dimnull\mathcal{T}+dim\mathcal{W}-dim\mathcal{V}; |       |               |     |     |     |     |
∗
| (b) dimrange\mathcal{T} |     | =dimrange\mathcal{T}. |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
8 Suppose\mathcal{A}isanm-by-nmatrixwithentriesin\mathbf{F}. Use(b)in Exercise7to
provethattherowrankof\mathcal{A}equalsthecolumnrankof\mathcal{A}.
This exercise asks for yet another alternative proof of a result that was
previouslyprovedin3.57and3.133.
9 Provethattheproductoftwoself-adjointoperatorson\mathcal{V} isself-adjointif
andonlyifthetwooperatorscommute.
\inℒ(\mathcal{V}).
| 10 Suppose\mathbf{F} | =\mathbf{C}  | and\mathcal{T} |     | Provethat\mathcal{T} |     | isself-adjointifandonlyif |     |     |
| ----------- | --- | ---- | --- | ---------- | --- | ------------------------- | --- | --- |
∗
|     |     |     |     | \langle\mathcal{T}v,v\rangle=\langle\mathcal{T} |     | v,v\rangle |     |     |
| --- | --- | --- | --- | --------- | --- | ---- | --- | --- |
forallv\in\mathcal{V}.

| -------- | ----------------------------- | --- | --- | --- |
| Defineanoperator\mathcal{S}∶ |     | \mathbf{F}2 \rightarrow\mathbf{F}2           |     |     |
| ------------------ | --- | ---------------- | --- | --- |
| 11                 |     | by\mathcal{S}(w,z)=(-z,w). |     |     |
∗
| (a) Findaformulafor\mathcal{S}                     |                                                           | .   |     |     |
| ---------------------------------------- | --------------------------------------------------------- | --- | --- | --- |
| (b) Showthat\mathcal{S}isnormalbutnotself-adjoint. |                                                           |     |     |     |
| (c) Findalleigenvaluesof\mathcal{S}.               |                                                           |     |     |     |
| If                                       | =\mathbf{R},then\mathcal{S}istheoperatoron\mathbf{R}2ofcounterclockwiserotationby90\circ. |     |     |     |
\mathbf{F}
Anoperator\mathcal{B}\inℒ(\mathcal{V})iscalledskewif
∗
\mathcal{B} =-\mathcal{B}.
| Supposethat\mathcal{T} |     | \inℒ(\mathcal{V}). Provethat\mathcal{T} | isnormalifandonlyifthereexist |     |
| ------------ | --- | ----------------- | ----------------------------- | --- |
commutingoperators\mathcal{A}and\mathcal{B}suchthat\mathcal{A}isself-adjoint,\mathcal{B}isaskewoperator,
| and\mathcal{T} | =\mathcal{A}+\mathcal{B}. |     |     |     |
| ---- | ----- | --- | --- | --- |
∗
| 13 Suppose\mathbf{F} | =\mathbf{R}. | Define𝒜\inℒ(ℒ(\mathcal{V}))by𝒜\mathcal{T} | =\mathcal{T}  | forall\mathcal{T} \inℒ(\mathcal{V}). |
| ----------- | --- | ------------------- | --- | -------------- |
Findalleigenvaluesof𝒜.
$$(a)$$
| (b) Findtheminimalpolynomialof𝒜. |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- |
1pq.
14 Define an inner product on 𝒫 (\mathbf{R}) by \langlep,q\rangle = \int Define an operator
| ------ | ------ | --- | --- | --- |
| \mathcal{T} \inℒ(𝒫 | (\mathbf{R}))by |     |     |     |
\mathcal{T}(ax2+bx+c)=bx.
$$(a) Showthatwiththisinnerproduct,theoperator\mathcal{T} isnotself-adjoint.$$
| (b) Thematrixof\mathcal{T} |     | withrespecttothebasis1,x,x2 |     | is  |
| ---------------- | --- | --------------------------- | --- | --- |
0 0 0
⎛ ⎞
⎜ ⎟
⎜ 0 1 0 ⎟ ⎟.
⎜
0 0 0
⎝ ⎠
Thismatrixequalsitsconjugatetranspose,eventhough\mathcal{T} isnotselfadjoint. Explainwhythisisnotacontradiction.
| Suppose\mathcal{T} | \inℒ(\mathcal{V})isinvertible. | Provethat |     |     |
| -------- | ------------------ | --------- | --- | --- |
| (a) \mathcal{T}       | isself-adjoint | ⟺ \mathcal{T}-1 isself-adjoint; |     |     |
| ----------- | -------------- | --------------------- | --- | --- |
| (b) \mathcal{T}       | isnormal       | ⟺ \mathcal{T}-1 isnormal.       |     |     |
| 16 Suppose\mathbf{F} | =\mathbf{R}.            |                       |     |     |
isasubspaceofℒ(\mathcal{V}).
| (a) Showthatthesetofself-adjointoperatorson\mathcal{V} |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- |
$$(b) What is the dimension of the subspace of ℒ(\mathcal{V}) in (a) [in terms of$$
dim\mathcal{V}]?
17 Suppose\mathbf{F} = \mathbf{C}. Showthatthesetofself-adjointoperatorson\mathcal{V} isnota
subspaceofℒ(\mathcal{V}).
18 Supposedim\mathcal{V} \geq 2. Showthatthesetofnormaloperatorson\mathcal{V} isnota
subspaceofℒ(\mathcal{V}).

| --- | --- | --------- | --- | ------------------------------ | --- | --- |
∗
19 Suppose \mathcal{T} \in ℒ(\mathcal{V}) and ∥\mathcal{T} v∥ \leq ‖\mathcal{T}v‖ for every v \in \mathcal{V}. Prove that \mathcal{T} is
normal.
Thisexercisefailsoninfinite-dimensionalinnerproductspaces,leadingto
whatarecalledhyponormaloperators,whichhaveawell-developedtheory.
|     |     | ℒ(\mathcal{V}) |     | \mathcal{P}2  |     |     |
| --- | --- | ---- | --- | --- | --- | --- |
20 Suppose \mathcal{P} \in is such that = \mathcal{P}. Prove that the following are
equivalent.
| (a) \mathcal{P}isself-adjoint.  |     |     |     |           |     |     |
| --------------------- | --- | --- | --- | --------- | --- | --- |
| (b) \mathcal{P}isnormal.        |     |     |     |           |     |     |
| (c) Thereisasubspace\mathcal{U} |     |     | of\mathcal{V} | suchthat\mathcal{P} | =\mathcal{P}  | .   |
\mathcal{U}
21 Suppose \mathcal{D}∶ 𝒫 (\mathbf{R}) \rightarrow 𝒫 (\mathbf{R}) is the differentiation operator defined by
| --- | --- | --- | --- | --- | --- | --- |
p′. 𝒫
\mathcal{D}p = Prove that there does not exist an inner product on (\mathbf{R}) that
makes\mathcal{D}anormaloperator.
22 Giveanexampleofanoperator\mathcal{T} \in ℒ(\mathbf{R}3)suchthat\mathcal{T} isnormalbutnot
self-adjoint.
23 Suppose\mathcal{T}isanormaloperatoron\mathcal{V}. Supposealsothatv,w\in\mathcal{V}satisfythe
equations
|     |     | ‖v‖=‖w‖=2, |     | \mathcal{T}v=3v, |     | \mathcal{T}w=4w. |
| --- | --- | ---------- | --- | ------ | --- | ------ |
Showthat‖\mathcal{T}(v+w)‖=10.
| Suppose\mathcal{T} | \inℒ(\mathcal{V})and |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- |
|     |     | +a  | z+a | z2+⋯+a |     | zm-1+zm |
| --- | --- | --- | --- | ------ | --- | ------- |
|     |     | a 0 | 1   | 2      | m-1 |         |
istheminimalpolynomialof\mathcal{T}. Provethattheminimalpolynomialof\mathcal{T} ∗ is
|     |     | +a  | z+a | z2+⋯+a |     | zm-1+zm. |
| --- | --- | --- | --- | ------ | --- | -------- |
|     |     | a 0 | 1   | 2      | m-1 |          |
∗equalstheminimal
| Thisexerciseshowsthattheminimalpolynomialof |     |       |     |     |     | \mathcal{T}   |
| ------------------------------------------- | --- | ----- | --- | --- | --- | --- |
| polynomialof                                |     | \mathcal{T}if \mathbf{F} | =\mathbf{R}. |     |     |     |
∗
25 Suppose \mathcal{T} \in ℒ(\mathcal{V}). Prove that \mathcal{T} is diagonalizable if and only if \mathcal{T} is
diagonalizable.
| Fixu,x | \in\mathcal{V}. | Define\mathcal{T} | \inℒ(\mathcal{V})by\mathcal{T}v=\langlev,u\ranglexforeveryv\in\mathcal{V}. |     |     |     |
| ------ | --- | ------- | ---------------------------- | --- | --- | --- |
$$(a) Provethatif\mathcal{V} isarealvectorspace,then\mathcal{T} isself-adjointifandonlyif$$
thelistu,xislinearlydependent.
$$(b) Provethat\mathcal{T} isnormalifandonlyifthelistu,xislinearlydependent.$$
| 27 Suppose\mathcal{T} | \inℒ(\mathcal{V})isnormal. |        |        | Provethat |         |         |
| ----------- | -------------- | ------ | ------ | --------- | ------- | ------- |
|             |                | null\mathcal{T}k | =null\mathcal{T} | and       | range\mathcal{T}k | =range\mathcal{T} |
foreverypositiveintegerk.
28 Suppose \mathcal{T} \in ℒ(\mathcal{V}) is normal. Prove that if \lambda \in \mathbf{F}, then the minimal
\lambda)2.
| polynomialof\mathcal{T} |     | isnotapolynomialmultipleof(x- |     |     |     |     |
| ------------- | --- | ----------------------------- | --- | --- | --- | --- |

| -------- | ----------------------------- | --- | --- | --- |
29 Proveorgiveacounterexample: If\mathcal{T} \inℒ(\mathcal{V})andthereisanorthonormal
basise ,…,e of\mathcal{V} suchthat‖\mathcal{T}e ‖=∥\mathcal{T} ∗ e ∥foreachk =1,…,n,then\mathcal{T} is
| 1   | n   | k k |     |     |
| --- | --- | --- | --- | --- |
normal.
30 Suppose that \mathcal{T} \in ℒ(\mathbf{F}3) is normal and \mathcal{T}(1,1,1) = (2,2,2). Suppose
| (z ,z ,z | )\innull\mathcal{T}. Provethatz | +z +z | =0. |     |
| -------- | ------------------- | ----- | --- | --- |
| 1 2 3    |                     | 1 2 3 |     |     |
31 Fixapositiveintegern. Intheinnerproductspaceofcontinuousreal-valued
| functionson[-\pi,\pi]withinnerproduct\langlef,g\rangle=\int |     |     | \pi fg,let |     |
| ---------------------------------------- | --- | --- | -------- | --- |
-\pi
| \mathcal{V}   | =span(1,cosx,cos2x,…,cosnx,sinx,sin2x,…,sinnx). |     |     |     |
| --- | ----------------------------------------------- | --- | --- | --- |
∗
| (a) Define\mathcal{D}\inℒ(\mathcal{V})by\mathcal{D}f |     | = f′. Showthat\mathcal{D} | =-\mathcal{D}. Concludethat\mathcal{D} |     |
| -------------------- | --- | --------------- | ------------------ | --- |
isnormalbutnotself-adjoint.
| (b) Define\mathcal{T} | \inℒ(\mathcal{V})by\mathcal{T}f | = f″. Showthat\mathcal{T} | isself-adjoint. |     |
| ----------- | --------- | --------------- | --------------- | --- |
Suppose\mathcal{T}∶ \rightarrow\mathcal{W}isalinearmap. Showthatunderthestandardidentifica-
| 32  | \mathcal{V}   |     |     |     |
| --- | --- | --- | --- | --- |
tionof\mathcal{V} with\mathcal{V}′ (see6.58)andthecorrespondingidentificationof\mathcal{W} with
| \mathcal{W}′,theadjointmap\mathcal{T} | ∗∶  | correspondstothedualmap\mathcal{T}′∶ |     | \mathcal{W}′ \rightarrow\mathcal{V}′. |
| ----------------- | --- | -------------------------- | --- | ------- |
\mathcal{W} \rightarrow\mathcal{V}
Moreprecisely,showthat
\mathcal{T}′(\phi )=\phi
|                  |     | w \mathcal{T}∗w                    |     |     |
| ---------------- | --- | ------------------------ | --- | --- |
| forallw\in\mathcal{W},where\phi |     | and\phi aredefinedasin6.58. |     |     |
|                  | w   | \mathcal{T}∗w                      |     |     |

| --- | --- | --- | --------- | --- | --------------- | --- |
| 7B Spectral | Theorem |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- |
Recall that a diagonal matrix is a square matrix that is 0 everywhere except
possiblyonthediagonal. Recallthatanoperatoron\mathcal{V} iscalleddiagonalizableif
theoperatorhasadiagonalmatrixwithrespecttosomebasisof\mathcal{V}. Recallalso
thatthishappensifandonlyifthereisabasisof\mathcal{V} consistingofeigenvectorsof
theoperator(see5.55).
Thenicestoperatorson\mathcal{V} arethoseforwhichthereisanorthonormalbasis
of\mathcal{V}withrespecttowhichtheoperatorhasadiagonalmatrix. Theseareprecisely
theoperators\mathcal{T} \inℒ(\mathcal{V})suchthatthereisanorthonormalbasisof\mathcal{V} consisting
ofeigenvectorsof\mathcal{T}. Ourgoalinthissectionistoprovethespectraltheorem,
whichcharacterizestheseoperatorsastheself-adjointoperatorswhen\mathbf{F} =\mathbf{R} and
| asthenormaloperatorswhen\mathbf{F} |     | =\mathbf{C}. |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- |
Thespectraltheoremisprobablythemostusefultoolinthestudyofoperators
oninnerproductspaces. Itsextensiontocertaininfinite-dimensionalinnerproduct
spaces(see,forexample,Section10Doftheauthor’sbook Measure,Integration
&Real Analysis)playsakeyroleinfunctionalanalysis.
Becausetheconclusionofthespectraltheoremdependson\mathbf{F},wewillbreak
the spectral theorem into two pieces, called the real spectral theorem and the
complexspectraltheorem.
| Real Spectral | Theorem |     |     |     |     |     |
| ------------- | ------- | --- | --- | --- | --- | --- |
Toprovetherealspectraltheorem,wewillneedtwopreliminaryresults. These
preliminaryresultsholdonbothrealandcomplexinnerproductspaces,butthey
arenotneededfortheproofofthecomplexspectraltheorem.
Youcouldguessthatthenextresultis Thiscompleting-the-squaretechnique
trueandevendiscoveritsproofbythink-
|                    |                       |         | can      | be used | to derive | the quadratic |
| ------------------ | --------------------- | ------- | -------- | ------- | --------- | ------------- |
| ing about          | quadratic polynomials | with    | formula. |         |           |               |
| real coefficients. | Specifically,         | suppose |          |         |           |               |
b,c andb2
| \in\mathbf{R}  | <4c. Letxbearealnumber. |      |        | Then |      |     |
| --- | ----------------------- | ---- | ------ | ---- | ---- | --- |
|     |                         |      | b 2    |      | b2   |     |
|     | x2+bx+c                 | =(x+ | ) +(c- |      | )>0. |     |
Inparticular,x2+bx+cisaninvertiblerealnumber(aconvolutedwayofsaying
thatitisnot0). Replacingtherealnumberxwithaself-adjointoperator(recallthe
analogybetweenrealnumbersandself-adjointoperators)leadstothenextresult.
7.26 invertiblequadraticexpressions
| Suppose\mathcal{T} | \inℒ(\mathcal{V})isself-adjointandb,c |     |     | aresuchthatb2 |     | <4c. Then |
| -------- | ------------------------- | --- | --- | ------------- | --- | --------- |
\in\mathbf{R}
\mathcal{T}2+b\mathcal{T}+c\mathcal{I}
isaninvertibleoperator.

244 Chapter 7 Operatorson Inner Product Spaces
Proof Letvbeanonzerovectorin\mathcal{V}. Then
\langle(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})v,v\rangle=\langle\mathcal{T}2v,v\rangle+b\langle\mathcal{T}v,v\rangle+c\langlev,v\rangle
=\langle\mathcal{T}v,\mathcal{T}v\rangle+b\langle\mathcal{T}v,v\rangle+c‖v‖2
\geq‖\mathcal{T}v‖2-|b|‖\mathcal{T}v‖‖v‖+c‖v‖2
|b|‖v‖ 2 b2
=(‖\mathcal{T}v‖- ) +(c- )‖v‖2
2 4
>0,
wherethethirdlineaboveholdsbythe Cauchy–Schwarzinequality(6.14). The
lastinequalityimpliesthat(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})v\neq0. Thus\mathcal{T}2+b\mathcal{T}+c\mathcal{I} isinjective,
whichimpliesthatitisinvertible(see3.65).
Thenextresultwillbeakeytoolinourproofoftherealspectraltheorem.
7.27 minimalpolynomialofself-adjointoperator
Suppose\mathcal{T} \inℒ(\mathcal{V})isself-adjoint. Thentheminimalpolynomialof\mathcal{T} equals
$$(z- \lambda )⋯(z- \lambda )forsome \lambda ,…,\lambda \in\mathbf{R}.$$
1 m 1 m
Proof Firstsuppose\mathbf{F} =\mathbf{C}. Thezerosoftheminimalpolynomialof\mathcal{T} arethe
eigenvaluesof\mathcal{T} [by5.27(a)]. Alleigenvaluesof\mathcal{T} arereal(by7.12). Thusthe
secondversionofthefundamentaltheoremofalgebra(see4.13)tellsusthatthe
minimalpolynomialof\mathcal{T} hasthedesiredform.
Nowsuppose\mathbf{F} =\mathbf{R}. Bythefactorizationofapolynomialover\mathbf{R} (see4.16)
thereexist \lambda ,…,\lambda \in \mathbf{R} andb ,…,b ,c ,…,c \in \mathbf{R} withb2 < 4c foreach
1 m 1 \mathcal{N} 1 \mathcal{N} k k
ksuchthattheminimalpolynomialof\mathcal{T} equals
7.28 (z- \lambda )⋯(z- \lambda )(z2+b z+c )⋯(z2+b z+c );
1 m 1 1 \mathcal{N} \mathcal{N}
hereeithermor\mathcal{N} mightequal0,meaningthattherearenotermsofthecorrespondingform. Now
$$(\mathcal{T}- \lambda \mathcal{I})⋯(\mathcal{T}- \lambda \mathcal{I})(\mathcal{T}2+b \mathcal{T}+c \mathcal{I})⋯(\mathcal{T}2+b \mathcal{T}+c \mathcal{I})=0.$$
1 m 1 1 \mathcal{N} \mathcal{N}
If\mathcal{N} > 0,thenwecouldmultiplybothsidesoftheequationaboveontheright
by the inverse of \mathcal{T}2 +b \mathcal{T} +c \mathcal{I} (which is an invertible operator by 7.26) to
\mathcal{N} \mathcal{N}
obtainapolynomialexpressionof\mathcal{T}thatequals0. Thecorrespondingpolynomial
wouldhavedegreetwolessthanthedegreeof7.28,violatingtheminimalityof
thedegreeofthepolynomialwiththisproperty. Thuswemusthave\mathcal{N} =0,which
meansthattheminimalpolynomialin7.28hastheform(z- \lambda )⋯(z- \lambda ),as
1 m
desired.
Theresultabovealongwith5.27(a)impliesthateveryself-adjointoperator
hasaneigenvalue. Infact,aswewillseeinthenextresult,self-adjointoperators
haveenougheigenvectorstoformabasis.

Section7B Spectral Theorem 245
Thenextresult,whichgivesacompletedescriptionoftheself-adjointoperators
onarealinnerproductspace,isoneofthemajortheoremsinlinearalgebra.
7.29 realspectraltheorem
Suppose\mathbf{F} =\mathbf{R} and\mathcal{T} \inℒ(\mathcal{V}). Thenthefollowingareequivalent.
$$(a) \mathcal{T} isself-adjoint.$$
$$(b) \mathcal{T} hasadiagonalmatrixwithrespecttosomeorthonormalbasisof\mathcal{V}.$$
$$(c) \mathcal{V} hasanorthonormalbasisconsistingofeigenvectorsof\mathcal{T}.$$
Proof Firstsuppose(a)holds,so\mathcal{T} isself-adjoint. Ourresultsonminimalpolynomials,specifically6.37and7.27,implythat\mathcal{T} hasanupper-triangularmatrix
withrespecttosomeorthonormalbasisof\mathcal{V}. Withrespecttothisorthonormal
∗ ∗
basis, the matrix of \mathcal{T} is the transpose of the matrix of \mathcal{T}. However, \mathcal{T} = \mathcal{T}.
Thusthetransposeofthematrixof\mathcal{T} equalsthematrixof\mathcal{T}. Becausethematrix
of\mathcal{T} isupper-triangular,thismeansthatallentriesofthematrixaboveandbelow
thediagonalare0. Hencethematrixof\mathcal{T} isadiagonalmatrixwithrespecttothe
orthonormalbasis. Thus(a)implies(b).
Conversely,nowsuppose(b)holds,so\mathcal{T} hasadiagonalmatrixwithrespectto
someorthonormalbasisof\mathcal{V}. Thatdiagonalmatrixequalsitstranspose. Thus
∗ ∗
withrespecttothatbasis,thematrixof\mathcal{T} equalsthematrixof\mathcal{T}. Hence\mathcal{T} =\mathcal{T},
provingthat(b)implies(a).
Theequivalenceof(b)and(c)followsfromthedefinitions[orseetheproof
that(a)and(b)areequivalentin5.55].
**7.30 例：** anorthonormalbasisofeigenvectorsforanoperator
Consider the operator \mathcal{T} on \mathbf{R}3 whose matrix (with respect to the standard
basis)is
14 -13 8
⎛ ⎞
⎜ ⎟
⎜ ⎜ -13 14 8 ⎟ ⎟.
⎝ 8 8 -7 ⎠
Thismatrixwithrealentriesequalsitstranspose;thus\mathcal{T} isself-adjoint. Asyou
canverify,
$$(1,-1,0) (1,1,1) (1,1,-2)$$
, ,
\sqrt2 \sqrt3 \sqrt6
isanorthonormalbasisof\mathbf{R}3 consistingofeigenvectorsof\mathcal{T}. Withrespectto
thisbasis,thematrixof\mathcal{T} isthediagonalmatrix
27 0 0
⎛ ⎞
⎜ ⎟
⎜ ⎜ 0 9 0 ⎟ ⎟.
⎝ 0 0 -15 ⎠
See Exercise17foraversionoftherealspectraltheoremthatappliessimultaneouslytomorethanoneoperator.

| -------- | --- | ----------------------------- | --- | --- | --- | --- |
| Complex Spectral |     | Theorem |     |     |     |     |
| ---------------- | --- | ------- | --- | --- | --- | --- |
Thenextresultgivesacompletedescriptionofthenormaloperatorsonacomplex
innerproductspace.
7.31 complexspectraltheorem
| Suppose\mathbf{F} =\mathbf{C} | and\mathcal{T} | \inℒ(\mathcal{V}). | Thenthefollowingareequivalent. |     |     |     |
| ----------- | ---- | ------ | ------------------------------ | --- | --- | --- |
$$(a) \mathcal{T} isnormal.$$
$$(b) \mathcal{T} hasadiagonalmatrixwithrespecttosomeorthonormalbasisof\mathcal{V}.$$
$$(c) \mathcal{V} hasanorthonormalbasisconsistingofeigenvectorsof\mathcal{T}.$$
Proof Firstsuppose(a)holds,so\mathcal{T} isnormal. By Schur’stheorem(6.38),there
is an orthonormal basis e ,…,e of \mathcal{V} with respect to which \mathcal{T} has an upper-
|                   |                | 1    | n    |       |     |          |
| ----------------- | -------------- | ---- | ---- | ----- | --- | -------- |
| triangularmatrix. | Thuswecanwrite |      |      |       |     |          |
|                   |                |      |      | a     | ⋯   | a        |
|                   |                |      |      | ⎛ 1,1 |     | 1,n ⎞    |
|                   | ℳ(\mathcal{T},(e         | ,…,e | ))=⎜ | ⎜     | ⋱   | ⋮ ⎟ ⎟ ⎟. |
| 7.32              |                | 1    | n    | ⎜     |     |          |
|                   |                |      |      | ⎝ 0   |     | a ⎠      |
n,n
Wewillshowthatthismatrixisactuallyadiagonalmatrix.
Weseefromthematrixabovethat
|     |     | ‖2      |     | |2, |     |     |
| --- | --- | ------- | --- | --- | --- | --- |
|     |     | ‖\mathcal{T}e =|a | 1,1 |     |     |     |
|     |     | ∥\mathcal{T} ∗ e ∥2 =|a |     | |2+|a |2+⋯+|a |     | |2. |
| --- | --- | ------------- | --- | ------------- | --- | --- |
|     |     | 1             | 1,1 | 1,2           |     | 1,n |
∗
Because\mathcal{T}isnormal,‖\mathcal{T}e ‖=∥\mathcal{T} e ∥(see7.20). Thusthetwoequationsabove
| --- | --- | --- | --- | --- | --- | --- |
implythatallentriesinthefirstrowofthematrixin7.32,exceptpossiblythefirst
entrya ,equal0.
1,1
Now7.32implies
|     |     |     | ‖\mathcal{T}e | ‖2 =|a | |2  |     |
| --- | --- | --- | --- | ------ | --- | --- |
2 2,2
| (becausea | =0,asweshowedintheparagraphabove)and |     |     |     |     |     |
| --------- | ------------------------------------ | --- | --- | --- | --- | --- |
1,2
|     |     | ∥\mathcal{T} ∗ e ∥2 =|a |     | |2+|a |2+⋯+|a |     | |2. |
| --- | --- | ------------- | --- | ------------- | --- | --- |
|     |     | 2             | 2,2 | 2,3           |     | 2,n |
∗
Because\mathcal{T} isnormal,‖\mathcal{T}e ‖=∥\mathcal{T} e ∥. Thusthetwoequationsaboveimplythat
| --- | --- | --- | --- | --- | --- | --- |
allentriesinthesecondrowofthematrixin7.32,exceptpossiblythediagonal
entrya ,equal0.
2,2
Continuinginthisfashion,weseethatallnondiagonalentriesinthematrix
7.32equal0. Thus(b)holds,completingtheproofthat(a)implies(b).
Now suppose (b) holds, so \mathcal{T} has a diagonal matrix with respect to some
∗
orthonormal basis of \mathcal{V}. The matrix of \mathcal{T} (with respect to the same basis) is
∗
obtainedbytakingtheconjugatetransposeofthematrixof\mathcal{T};hence\mathcal{T} alsohasa
diagonalmatrix. Anytwodiagonalmatricescommute;thus\mathcal{T} commuteswith\mathcal{T} ∗ ,
whichmeansthat\mathcal{T} isnormal. Inotherwords,(a)holds,completingtheproof
that(b)implies(a).
Theequivalenceof(b)and(c)followsfromthedefinitions(alsosee5.55).

Section7B Spectral Theorem 247
See Exercises 13 and 20 for alternative proofs that (a) implies (b) in the
previousresult.
Exercises 14 and 15 interpret the real spectral theorem and the complex
spectraltheorembyexpressingthedomainspaceasanorthogonaldirectsumof
eigenspaces.
See Exercise16foraversionofthecomplexspectraltheoremthatapplies
simultaneouslytomorethanoneoperator.
Themainconclusionofthecomplexspectraltheoremisthateverynormal
operatoronacomplexfinite-dimensionalinnerproductspaceisdiagonalizable
byanorthonormalbasis,asillustratedbythenextexample.
**7.33 例：** anorthonormalbasisofeigenvectorsforanoperator
Considertheoperator\mathcal{T} \inℒ(\mathbf{C}2)definedby\mathcal{T}(w,z)=(2w-3z,3w+2z).
Thematrixof\mathcal{T} (withrespecttothestandardbasis)is
2 -3
$$( ).$$
3 2
Aswesawin Example7.19,\mathcal{T} isanormaloperator.
Asyoucanverify,
1 (i,1), 1 (-i,1)
\sqrt2 \sqrt2
isanorthonormalbasisof\mathbf{C}2 consistingofeigenvectorsof\mathcal{T},andwithrespectto
thisbasisthematrixof\mathcal{T} isthediagonalmatrix
2+3i 0
$$( ).$$
0 2-3i
Exercises 7B
1 Provethatanormaloperatoronacomplexinnerproductspaceisself-adjoint
ifandonlyifallitseigenvaluesarereal.
Thisexercisestrengthenstheanalogy(fornormaloperators)betweenselfadjointoperatorsandrealnumbers.
2 Suppose\mathbf{F} =\mathbf{C}. Suppose\mathcal{T} \inℒ(\mathcal{V})isnormalandhasonlyoneeigenvalue.
Provethat\mathcal{T} isascalarmultipleoftheidentityoperator.
3 Suppose\mathbf{F} =\mathbf{C} and\mathcal{T} \inℒ(\mathcal{V})isnormal. Provethatthesetofeigenvalues
of\mathcal{T} iscontainedin{0,1}ifandonlyifthereisasubspace\mathcal{U} of\mathcal{V} suchthat
\mathcal{T} =\mathcal{P} .
\mathcal{U}
4 Prove that a normal operator on a complex inner product space is skew
$$(meaningitequalsthenegativeofitsadjoint)ifandonlyifallitseigenvalues$$
arepurelyimaginary(meaningthattheyhaverealpartequalto0).

| -------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
\inℒ(\mathbf{C}3)isadiagonalizableoperator,
| 5 Proveorgiveacounterexample: |     |     | If\mathcal{T} |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
then\mathcal{T} isnormal(withrespecttotheusualinnerproduct).
6 Suppose \mathcal{V} is a complex inner product space and \mathcal{T} \in ℒ(\mathcal{V}) is a normal
| operatorsuchthat\mathcal{T}9 |     | =\mathcal{T}8. | Provethat\mathcal{T} | isself-adjointand\mathcal{T}2 |     |     | =\mathcal{T}. |     |
| ------------------ | --- | ---- | ---------- | ------------------- | --- | --- | --- | --- |
7 Give an example of an operator \mathcal{T} on a complex vector space such that
\mathcal{T}9 =\mathcal{T}8 but\mathcal{T}2
\neq\mathcal{T}.
8 Suppose\mathbf{F} =\mathbf{C} and\mathcal{T} \inℒ(\mathcal{V}). Provethat\mathcal{T} isnormalifandonlyifevery
| eigenvectorof\mathcal{T} | isalsoaneigenvectorof\mathcal{T} |        |            | ∗   | .                        |     |     |     |
| -------------- | ---------------------- | ------ | ---------- | --- | ------------------------ | --- | --- | --- |
| Suppose\mathbf{F}       | =\mathbf{C} and\mathcal{T}                | \inℒ(\mathcal{V}). | Provethat\mathcal{T} |     | isnormalifandonlyifthere |     |     |     |
∗
| existsapolynomialp\in𝒫(\mathbf{C})suchthat\mathcal{T} |     |     |     |     | =p(\mathcal{T}). |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- |
10 Suppose \mathcal{V} is a complex inner product space. Prove that every normal
| operatoron\mathcal{V} | hasasquareroot. |     |     |     |     |     |     |     |
| ----------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
\mathcal{S}2
| Anoperator\mathcal{S}\inℒ(\mathcal{V})iscalledasquarerootof |     |     |     |     | \mathcal{T} \inℒ(\mathcal{V})if |     | =\mathcal{T}. | We  |
| ------------------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- |
willdiscussmoreaboutsquarerootsofoperatorsin Sections7Cand8C.
| 11 Provethateveryself-adjointoperatoron\mathcal{V} |     |     |     | hasacuberoot. |           |     |        |     |
| ---------------------------------------- | --- | --- | --- | ------------- | --------- | --- | ------ | --- |
| Anoperator\mathcal{S}\inℒ(\mathcal{V})iscalledacuberootof      |     |     |     |               | \mathcal{T} \inℒ(\mathcal{V})if |     | \mathcal{S}3 =\mathcal{T}. |     |
12 Suppose\mathcal{V} isacomplexvectorspaceand\mathcal{T} \inℒ(\mathcal{V})isnormal. Provethat
∗
| if\mathcal{S}isanoperatoron\mathcal{V} |     | thatcommuteswith\mathcal{T},then\mathcal{S}commuteswith\mathcal{T} |     |     |     |     |     | .   |
| ------------------ | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
Theresultinthisexerciseiscalled Fuglede’stheorem.
13 Without using the complex spectral theorem, use the version of Schur’s
theorem that applies to two commuting operators (take ℰ = {\mathcal{T},\mathcal{T} ∗ } in
Exercise 20 in Section 6B) to give a different proof that if \mathbf{F} = \mathbf{C} and
\mathcal{T} \in ℒ(\mathcal{V}) isnormal, then \mathcal{T} hasa diagonalmatrix withrespect to some
orthonormalbasisof\mathcal{V}.
14 Suppose \mathbf{F} = \mathbf{R} and \mathcal{T} \in ℒ(\mathcal{V}). Prove that \mathcal{T} is self-adjoint if and only
ifallpairsofeigenvectorscorrespondingtodistincteigenvaluesof\mathcal{T} are
| orthogonaland\mathcal{V} |     | =\mathcal{E}(\lambda ,\mathcal{T})\oplus⋯\oplus\mathcal{E}(\lambda |     | ,\mathcal{T}),where |     | \lambda ,…,\lambda | denotethe |     |
| -------------- | --- | -------------- | --- | --------- | --- | ------ | --------- | --- |
|                |     | 1              |     | m         |     | 1      | m         |     |
distincteigenvaluesof\mathcal{T}.
15 Suppose\mathbf{F} =\mathbf{C}and\mathcal{T} \inℒ(\mathcal{V}). Provethat\mathcal{T}isnormalifandonlyifallpairs
ofeigenvectorscorrespondingtodistincteigenvaluesof\mathcal{T} areorthogonal
| and \mathcal{V} = | \mathcal{E}(\lambda ,\mathcal{T})\oplus⋯\oplus\mathcal{E}(\lambda |     | ,\mathcal{T}), | where | \lambda ,…,\lambda | denote | the distinct |     |
| ------- | ------------- | --- | ---- | ----- | ------ | ------ | ------------ | --- |
|         | 1             |     | m    |       | 1      | m      |              |     |
eigenvaluesof\mathcal{T}.
| Suppose\mathbf{F} | = \mathbf{C} andℰ | \subseteq ℒ(\mathcal{V}). | Provethatthereisanorthonormalbasis |     |     |     |     |     |
| -------- | -------- | ------- | ---------------------------------- | --- | --- | --- | --- | --- |
of\mathcal{V} withrespecttowhicheveryelementofℰhasadiagonalmatrixifand
| onlyif\mathcal{S}and\mathcal{T} | arecommutingnormaloperatorsforall\mathcal{S},\mathcal{T} |     |     |     |     |     | \inℰ. |     |
| ----------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
This exercise extends the complex spectral theorem to the context of a
collectionofcommutingnormaloperators.

| --- | --- | --------- | --------------- | --- |
17 Suppose\mathbf{F} = \mathbf{R} andℰ \subseteq ℒ(\mathcal{V}). Provethatthereisanorthonormalbasis
of\mathcal{V} withrespecttowhicheveryelementofℰhasadiagonalmatrixifand
| onlyif\mathcal{S}and\mathcal{T} | arecommutingself-adjointoperatorsforall\mathcal{S},\mathcal{T} |     |     | \inℰ. |
| ----------- | ------------------------------------------ | --- | --- | --- |
Thisexerciseextendstherealspectraltheoremtothecontextofacollection
ofcommutingself-adjointoperators.
18 Giveanexampleofarealinnerproductspace\mathcal{V},anoperator\mathcal{T} \in ℒ(\mathcal{V}),
andrealnumbersb,cwithb2
<4csuchthat
\mathcal{T}2+b\mathcal{T}+c\mathcal{I}
isnotinvertible.
This exercise shows that the hypothesis that \mathcal{T} is self-adjoint cannot be
deletedin7.26,evenforrealvectorspaces.
19 Suppose\mathcal{T} \inℒ(\mathcal{V})isself-adjointand\mathcal{U}isasubspaceof\mathcal{V} thatisinvariant
under\mathcal{T}.
| (a) Provethat\mathcal{U}⟂ | isinvariantunder\mathcal{T}.   |     |     |     |
| --------------- | -------------------- | --- | --- | --- |
| (b) Provethat\mathcal{T}| | \inℒ(\mathcal{U})isself-adjoint. |     |     |     |
\mathcal{U}
| (c) Provethat\mathcal{T}| | \inℒ(\mathcal{U}⟂)isself-adjoint. |     |     |     |
| --------------- | --------------------- | --- | --- | --- |
\mathcal{U}⟂
20 Suppose \mathcal{T} \in ℒ(\mathcal{V}) is normal and \mathcal{U} is a subspace of \mathcal{V} that is invariant
under\mathcal{T}.
Provethat\mathcal{U}⟂
| (a)              | isinvariantunder\mathcal{T}. |      |     |     |
| ---------------- | ------------------ | ---- | --- | --- |
| (b) Provethat\mathcal{U}   | isinvariantunder\mathcal{T}  | ∗ .  |     |     |
|                  | ∗                  | ∗    |     |     |
| (c) Provethat(\mathcal{T}| | ) =(\mathcal{T}              | )| . |     |     |
|                  | \mathcal{U}                  | \mathcal{U}    |     |     |
\inℒ(\mathcal{U}⟂)arenormaloperators.
| (d) Provethat\mathcal{T}| | \inℒ(\mathcal{U})and\mathcal{T}| | \mathcal{U}⟂  |     |     |
| --------------- | ---------- | --- | --- | --- |
\mathcal{U}
Thisexercisecanbeusedtogiveyetanotherproofofthecomplexspectral
theorem(useinductionondim\mathcal{V}andtheresultthat\mathcal{T}hasaneigenvector).
21 Supposethat\mathcal{T}isaself-adjointoperatoronafinite-dimensionalinnerproduct
| spaceandthat2and3aretheonlyeigenvaluesof\mathcal{T}. |     |     | Provethat |     |
| ------------------------------------------ | --- | --- | --------- | --- |
\mathcal{T}2-5\mathcal{T}+6\mathcal{I}
=0.
\inℒ(\mathbf{C}3)suchthat2and3aretheonly
22 Giveanexampleofanoperator\mathcal{T}
| eigenvaluesof\mathcal{T} | and\mathcal{T}2-5\mathcal{T}+6\mathcal{I} | \neq0. |     |     |
| -------------- | ----------- | --- | --- | --- |
23 Suppose\mathcal{T} \inℒ(\mathcal{V})isself-adjoint, \lambda\in\mathbf{F},and\epsilon >0. Supposethereexists
v\in\mathcal{V} suchthat‖v‖=1and
‖\mathcal{T}v- \lambdav‖<\epsilon.
| Provethat\mathcal{T} | hasaneigenvalue | \lambda′ suchthat∣\lambda- | \lambda′∣<\epsilon. |     |
| ---------- | --------------- | -------------- | ------ | --- |
Thisexerciseshowsthatforaself-adjointoperator,anumberthatisclose
tosatisfyinganequationthatwouldmakeitaneigenvalueisclosetoan
eigenvalue.

250 Chapter 7 Operatorson Inner Product Spaces
24 Suppose\mathcal{U} isafinite-dimensionalvectorspaceand\mathcal{T} \inℒ(\mathcal{U}).
$$(a) Suppose\mathbf{F} =\mathbf{R}. Provethat\mathcal{T} isdiagonalizableifandonlyifthereisa$$
basisof\mathcal{U} suchthatthematrixof\mathcal{T} withrespecttothisbasisequalsits
transpose.
$$(b) Suppose\mathbf{F} =\mathbf{C}. Provethat\mathcal{T} isdiagonalizableifandonlyifthereisa$$
basisof\mathcal{U}suchthatthematrixof\mathcal{T}withrespecttothisbasiscommutes
withitsconjugatetranspose.
Thisexerciseaddsanotherequivalencetothelistofconditionsequivalent
todiagonalizabilityin5.55.
25 Supposethat\mathcal{T} \in ℒ(\mathcal{V})andthereisanorthonormalbasise ,…,e of\mathcal{V}
1 n
consistingofeigenvectorsof\mathcal{T},withcorrespondingeigenvalues \lambda ,…,\lambda .
1 n
Showthatifk \in{1,…,n},thenthepseudoinverse\mathcal{T}† satisfiestheequation
\mathcal{T}†e = ⎧ { \lambda 1 k e k if \lambda k \neq0,
k ⎨
{ ⎩0 if \lambda
k
=0.

| --- | --- | --------- | ----------------- |
| 7C Positive | Operators |     |     |
| ----------- | --------- | --- | --- |
positiveoperator
**7.34 定义：** | Anoperator\mathcal{T} | \inℒ(\mathcal{V})iscalledpositiveif\mathcal{T} | isself-adjointand |     |
| ----------- | ------------------------ | ----------------- | --- |
\langle\mathcal{T}v,v\rangle\geq0
forallv\in\mathcal{V}.
If\mathcal{V} isacomplexvectorspace,thentherequirementthat\mathcal{T} beself-adjointcan
bedroppedfromthedefinitionabove(by7.14).
| 7.35 example: | positiveoperators |     |     |
| ------------- | ----------------- | --- | --- |
$$(a) Let\mathcal{T} \in ℒ(\mathbf{F}2)betheoperatorwhosematrix(usingthestandardbasis)is$$
Then\mathcal{T}isself-adjointand\langle\mathcal{T}(w,z),(w,z)\rangle=2|w|2-2Re(wz)+|z|2
$$( 2 -1).$$
-1 1
| =|w-z|2+|w|2 | \geq0forall(w,z)\in\mathbf{F}2. | Thus\mathcal{T} | isapositiveoperator. |
| ------------ | ----------------- | ----- | -------------------- |
$$(b) If \mathcal{U} is a subspace of \mathcal{V}, then the orthogonal projection \mathcal{P} is a positive$$
\mathcal{U}
operator,asyoushouldverify.
$$(c) If \mathcal{T} \in ℒ(\mathcal{V}) is self-adjoint and b,c \in \mathbf{R} are such that b2 < 4c, then$$
\mathcal{T}2+b\mathcal{T}+c\mathcal{I}
isapositiveoperator,asshownbytheproofof7.26.
| 7.36 definition:               | squareroot             |               |          |
| ------------------------------ | ---------------------- | ------------- | -------- |
| Anoperator\mathcal{R}iscalledasquareroot |                        | ofanoperator\mathcal{T} | if\mathcal{R}2 =\mathcal{T}. |
| 7.37 example:                  | squarerootofanoperator |               |          |
ℒ(\mathbf{F}3)
If \mathcal{T} \in is defined by \mathcal{T}(z ,z ,z ) = (z ,0,0), then the operator
|     |     | 1 2 3 | 3   |
| --- | --- | ----- | --- |
\mathcal{R}\inℒ(\mathbf{F}3) defined by \mathcal{R}(z ,z ,z ) = (z ,z ,0) is a square root of \mathcal{T} because
1 2 3 2 3
\mathcal{R}2
=\mathcal{T},asyoucanverify.
Thecharacterizationsofthepositive
Becausepositiveoperatorscorrespond
operators in the next result correspond tononnegativenumbers,bettertermi-
| to characterizations | of the nonnegative |     |     |
| -------------------- | ------------------ | --- | --- |
nologywouldusethetermnonnegative
numbersamong\mathbf{C}. Specifically,anum- operators.However,operatortheorists
ber z \in \mathbf{C} is nonnegative if and only consistentlycallthesepositiveoperaif it has a nonnegative square root, cor- tors,sowefollowthatcustom. Some
responding to condition (d). Also, z is mathematiciansusethetermpositive
nonnegative if and only if it has a real semidefinite operator, which means
squareroot,correspondingtocondition thesameaspositiveoperator.
$$(e). Finally,zisnonnegativeifandonly$$
if there exists w \in \mathbf{C} such that z = ww, corresponding to condition (f). See
Exercise20foranotherconditionthatisequivalenttobeingapositiveoperator.

| -------- | ----------------------------- | --- | --- |
characterizationsofpositiveoperators
7.38
| Let\mathcal{T} \inℒ(\mathcal{V}). | Thenthefollowingareequivalent. |     |     |
| ----------- | ------------------------------ | --- | --- |
$$(a) \mathcal{T} isapositiveoperator.$$
| (b) \mathcal{T} isself-adjointandalleigenvaluesof\mathcal{T} |     | arenonnegative. |     |
| ---------------------------------------- | --- | --------------- | --- |
$$(c) Withrespecttosomeorthonormalbasisof\mathcal{V},thematrixof\mathcal{T}isadiagonal$$
matrixwithonlynonnegativenumbersonthediagonal.
$$(d) \mathcal{T} hasapositivesquareroot.$$
$$(e) \mathcal{T} hasaself-adjointsquareroot.$$
| (f) \mathcal{T} =\mathcal{R} | ∗ \mathcal{R}forsome\mathcal{R}\inℒ(\mathcal{V}). |     |     |
| -------- | ----------------- | --- | --- |
Proof Wewillprovethat(a)\Rightarrow(b)\Rightarrow(c)\Rightarrow(d)\Rightarrow(e)\Rightarrow(f)\Rightarrow(a).
Firstsuppose(a)holds,sothat\mathcal{T}ispositive,whichimpliesthat\mathcal{T}isself-adjoint
$$(bydefinitionofpositiveoperator). Toprovetheotherconditionin(b),suppose$$
\lambdaisaneigenvalueof\mathcal{T}. Letvbeaneigenvectorof\mathcal{T} correspondingto \lambda. Then
|     | 0\leq\langle\mathcal{T}v,v\rangle=\langle\lambdav,v\rangle= | \lambda\langlev,v\rangle. |     |
| --- | ---------------- | ------- | --- |
Thus \lambdaisanonnegativenumber. Hence(b)holds,showingthat(a)implies(b).
Nowsuppose(b)holds,sothat\mathcal{T} isself-adjointandalleigenvaluesof\mathcal{T} are
nonnegative. Bythespectraltheorem(7.29and7.31),thereisanorthonormal
basise ,…,e of\mathcal{V} consistingofeigenvectorsof\mathcal{T}. Let \lambda ,…,\lambda betheeigen-
| 1   | n   |     | 1 n |
| --- | --- | --- | --- |
values of \mathcal{T} corresponding to e ,…,e ; thus each \lambda is a nonnegative number.
|     |     | 1 n | k   |
| --- | --- | --- | --- |
Thematrixof\mathcal{T} withrespecttoe ,…,e isthediagonalmatrixwith \lambda ,…,\lambda
1 n 1 n
onthediagonal,whichshowsthat(b)implies(c).
Nowsuppose(c)holds. Supposee ,…,e isanorthonormalbasisof\mathcal{V} such
1 n
thatthematrixof\mathcal{T}withrespecttothisbasisisadiagonalmatrixwithnonnegative
numbers \lambda ,…,\lambda on the diagonal. The linear map lemma (3.4) implies that
1 n
thereexists\mathcal{R}\inℒ(\mathcal{V})suchthat
|     |     | \mathcal{R}e =\sqrt\lambda e |     |
| --- | --- | -------- | --- |
|     |     | k k k    |     |
foreachk =1,…,n. Asyoushouldverify,\mathcal{R}isapositiveoperator. Furthermore,
| \mathcal{R}2e            | foreachk,whichimpliesthat\mathcal{R}2                |     | \mathcal{T}. Thus\mathcal{R}isapositive |
| -------------- | ------------------------------------------ | --- | ------------------- |
| k = \lambda k e      | k = \mathcal{T}e k                                   |     | =                   |
| squarerootof\mathcal{T}. | Hence(d)holds,whichshowsthat(c)implies(d). |     |                     |
Every positive operator is self-adjoint (by definition of positive operator).
Thus(d)implies(e).
Nowsuppose(e)holds,meaningthatthereexistsaself-adjointoperator\mathcal{R}on
|     |     | ∗ ∗ |     |
| --- | --- | --- | --- |
\mathcal{V} suchthat\mathcal{T} =\mathcal{R}2. Then\mathcal{T} =\mathcal{R} \mathcal{R}(because\mathcal{R} =\mathcal{R}). Hence(e)implies(f).
ℒ(\mathcal{V}) ∗
Finally, suppose (f) holds. Let \mathcal{R} \in be such that \mathcal{T} = \mathcal{R} \mathcal{R}. Then
| ∗ ∗ | ∗ ∗ ∗ ∗ | ∗   |     |
| --- | ------- | --- | --- |
\mathcal{T} =(\mathcal{R} \mathcal{R}) =\mathcal{R} (\mathcal{R} ) =\mathcal{R} \mathcal{R}=\mathcal{T}. Hence\mathcal{T} isself-adjoint. Tocompletethe
proofthat(a)holds,notethat
∗
|              | \langle\mathcal{T}v,v\rangle=\langle\mathcal{R}                                  | \mathcal{R}v,v\rangle=\langle\mathcal{R}v,\mathcal{R}v\rangle\geq0 |     |
| ------------ | ------------------------------------------ | --------------- | --- |
| foreveryv\in\mathcal{V}. | Thus\mathcal{T} ispositive,showingthat(f)implies(a). |                 |     |

| --- | --- | --- | --- | --------- | --- | ----------------- | --- |
Everynonnegativenumberhasauniquenonnegativesquareroot. Thenext
resultshowsthatpositiveoperatorsenjoyasimilarproperty.
7.39 eachpositiveoperatorhasonlyonepositivesquareroot
| Everypositiveoperatoron\mathcal{V} |     |        | hasauniquepositivesquareroot. |     |     |     |     |
| ------------------------ | --- | ------ | ----------------------------- | --- | --- | --- | --- |
| Proof Suppose            | \mathcal{T}   | \in ℒ(\mathcal{V}) | is positive.                  |     |     |     |     |
Apositiveoperatorcanhaveinfinitely
Suppose v \in \mathcal{V} is an eigenvector of \mathcal{T}. manysquareroots(althoughonlyone
| Hencethereexistsarealnumber |     |     | \lambda   | \geq 0 |                                     |     |             |
| --------------------------- | --- | --- | --- | --- | ----------------------------------- | --- | ----------- |
|                             |     |     |     |     | ofthemcanbepositive).               |     | Forexample, |
| suchthat\mathcal{T}v=                 | \lambdav. |     |     |     | theidentityoperatoron\mathcal{V}hasinfinitely |     |             |
Let\mathcal{R}beapositivesquarerootof\mathcal{T}.
|                        |     |     |          |     | manysquarerootsif |     | dim\mathcal{V} >1. |
| ---------------------- | --- | --- | -------- | --- | ----------------- | --- | -------- |
| Wewillprovethat\mathcal{R}v=\sqrt\lambdav. |     |     | Thiswill |     |                   |     |          |
imply that the behavior of \mathcal{R} on the eigenvectors of \mathcal{T} is uniquely determined.
Because there is a basis of \mathcal{V} consisting of eigenvectors of \mathcal{T} (by the spectral
theorem),thiswillimplythat\mathcal{R}isuniquelydetermined.
Toprovethat\mathcal{R}v=\sqrt\lambdav,notethatthespectraltheoremassertsthatthereisan
orthonormalbasise ,…,e of\mathcal{V} consistingofeigenvectorsof\mathcal{R}. Because\mathcal{R}isa
|     |     | 1 n |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
positiveoperator,allitseigenvaluesarenonnegative. Thusthereexistnonnegative
| numbers  | ,…,\lambda | suchthat\mathcal{R}e             | =\sqrt\lambda |       | foreachk | =1,…,n. |     |
| -------- | ---- | ---------------------- | --- | ----- | -------- | ------- | --- |
| \lambda 1      | n    |                        | k   | k e k |          |         |     |
| Becausee | ,…,e | isabasisof\mathcal{V},wecanwrite |     |       |          |         |     |
1 n
|     |     |     | v=a | e +⋯+a | e   |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     |     | 1   | 1      | n   | n   |     |
,…,a
| forsomenumbersa |     |      | \in\mathbf{F}. Thus |      |     |     |     |
| --------------- | --- | ---- | -------- | ---- | --- | --- | --- |
|                 |     | 1 n  |          |      |     |     |     |
|                 |     |      | \sqrt\lambda       | +⋯+a | \sqrt\lambda  |     |     |
|                 |     | \mathcal{R}v=a |          | e    |     | e . |     |
|                 |     |      | 1 1      | 1    | n   | n n |     |
Hence
|     |     | \lambdav=\mathcal{T}v=\mathcal{R}2v=a |     | \lambda   | e +⋯+a | \lambda   | e . |
| --- | --- | ----------- | --- | --- | ------ | --- | --- |
|     |     |             |     | 1 1 | 1      | n n | n   |
Theequationaboveimpliesthat
|       | a                 | \lambdae +⋯+a | \lambdae      | =a \lambda | e +⋯+a |     | \lambda e . |
| ----- | ----------------- | ------- | ------- | ---- | ------ | --- | ----- |
|       | 1                 | 1       | n n     | 1    | 1 1    | n   | n n   |
| Thusa | (\lambda- \lambda )=0foreachk |         | =1,…,n. |      | Hence  |     |       |
k k
|     |     |     | v=  | \sum   | a e . |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- |
k k
{k∶\lambda =\lambda}
k
Thus
|     |     | \mathcal{R}v= | \sum   | a \sqrt\lambdae | =\sqrt\lambdav, |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | --- |
|     |     |     |     | k     | k     |     |     |
{k∶\lambda
$$k =\lambda}$$
asdesired.
Thenotationdefinedbelowmakessensethankstotheresultabove.
| 7.40 notation: | \sqrt\mathcal{T}  |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- |
apositiveoperator,\sqrt\mathcal{T}
| For\mathcal{T} |     |     | denotestheuniquepositivesquarerootof\mathcal{T}. |     |     |     |     |
| ---- | --- | --- | -------------------------------------- | --- | --- | --- | --- |

| -------- | ----------------------------- | --- | --- | --- |
squarerootofpositiveoperators
**7.41 例：** Defineoperators\mathcal{S},\mathcal{T} on\mathbf{R}2 (withtheusual Euclideaninnerproduct)by
| \mathcal{S}(x,y)=(x,2y) |     | and \mathcal{T}(x,y)=(x+y,x+y). |     |     |
| ------------- | --- | --------------------- | --- | --- |
Thenwithrespecttothestandardbasisof\mathbf{R}2 wehave
|        | 1   | 0            | 1 1 |     |
| ------ | --- | ------------ | --- | --- |
| ℳ(\mathcal{S})=( |     | ) and ℳ(\mathcal{T})=( | ).  |     |
7.42
|     | 0   | 2   | 1 1 |     |
| --- | --- | --- | --- | --- |
Eachofthesematricesequalsitstranspose;thus\mathcal{S}and\mathcal{T} areself-adjoint.
If(x,y)\in\mathbf{R}2,then
|     | \langle\mathcal{S}(x,y),(x,y)\rangle=x2+2y2 |     | \geq0  |     |
| --- | --------------------- | --- | --- | --- |
and
| \langle\mathcal{T}(x,y),(x,y)\rangle=x2+2xy+y2 |     | =(x+y)2 | \geq0. |     |
| ------------------------ | --- | ------- | --- | --- |
Thus\mathcal{S}and\mathcal{T} arepositiveoperators.
Thestandardbasisof\mathbf{R}2isanorthonormalbasisconsistingofeigenvectorsof
\mathcal{S}. Notethat
|     |     | ( 1 , 1 ),( 1 ,- 1 ) |     |     |
| --- | --- | -------------------- | --- | --- |
|     |     | \sqrt2 \sqrt2 \sqrt2 \sqrt2          |     |     |
is an orthonormal basis of eigenvectors of \mathcal{T}, with eigenvalue 2 for the first
eigenvectorandeigenvalue0forthesecondeigenvector. Thus\sqrt\mathcal{T} hasthesame
eigenvectors,witheigenvalues\sqrt2and0.
Youcanverifythat
1 1
|          | 1   | 0             | ⎛ ⎜⎜⎜⎜ \sqrt | \sqrt ⎞ ⎟⎟⎟⎟ |
| -------- | --- | ------------- | -------- | -------- |
| ℳ(\sqrt\mathcal{S})=⎛⎜ |     | ⎞⎟ and ℳ(\sqrt\mathcal{T})= | 2        | 2        |
|          | ⎝ 0 | \sqrt 2 ⎠         | 1        | 1        |
|          |     |               | ⎝        | ⎠        |
\sqrt2 \sqrt2
with respect to the standard basis by showing that the squares of the matrices
abovearethematricesin7.42andthateachmatrixaboveisthematrixofapositive
operator.
Thestatementofthenextresultdoesnotinvolveasquareroot,buttheclean
proofmakesniceuseofthesquarerootofapositiveoperator.
| \mathcal{T} positiveand | \langle\mathcal{T}v,v\rangle=0 | ⟹ \mathcal{T}v=0 |     |     |
| ------------- | -------- | ------ | --- | --- |
7.43
Suppose \mathcal{T} is a positive operator on \mathcal{V} and v \in \mathcal{V} is such that \langle\mathcal{T}v,v\rangle = 0.
Then\mathcal{T}v=0.
| 0=\langle\mathcal{T}v,v\rangle=\langle\sqrt\mathcal{T}\sqrt\mathcal{T}v,v\rangle=\langle\sqrt\mathcal{T}v,\sqrt\mathcal{T}v\rangle=∥\sqrt\mathcal{T}v∥ |     |     |     | .   |
| ---------------------------------- | --- | --- | --- | --- |
Hence\sqrt\mathcal{T}v=0. Thus\mathcal{T}v=\sqrt\mathcal{T}(\sqrt\mathcal{T}v)=0,asdesired.

Section7C Positive Operators 255
Exercises 7C
1 Suppose \mathcal{T} \in ℒ(\mathcal{V}). Prove that if both \mathcal{T} and -\mathcal{T} are positive operators,
then\mathcal{T} =0.
2 Suppose \mathcal{T} \in ℒ(\mathbf{F}4) is the operator whose matrix (with respect to the
standardbasis)is
2 -1 0 0
⎛ ⎞
⎜ ⎟
⎜ -1 2 -1 0 ⎟
⎜ ⎜ ⎟ ⎟.
⎜ ⎜ 0 -1 2 -1 ⎟ ⎟
⎝ 0 0 -1 2 ⎠
Showthat\mathcal{T} isaninvertiblepositiveoperator.
3 Supposenisapositiveintegerand\mathcal{T} \inℒ(\mathbf{F}n)istheoperatorwhosematrix
$$(with respect to the standard basis) consists of all 1’s. Show that \mathcal{T} is a$$
positiveoperator.
4 Supposenisanintegerwithn>1. Showthatthereexistsann-by-nmatrix
∗
\mathcal{A}suchthatalloftheentriesof\mathcal{A}arepositivenumbersand\mathcal{A}=\mathcal{A} ,butthe
operatoron\mathbf{F}nwhosematrix(withrespecttothestandardbasis)equals\mathcal{A}is
notapositiveoperator.
5 Suppose\mathcal{T} \inℒ(\mathcal{V})isself-adjoint. Provethat\mathcal{T} isapositiveoperatorifand
onlyifforeveryorthonormalbasise ,…,e of\mathcal{V},allentriesonthediagonal
1 n
ofℳ(\mathcal{T},(e ,…,e ))arenonnegativenumbers.
1 n
6 Provethatthesumoftwopositiveoperatorson\mathcal{V} isapositiveoperator.
7 Suppose \mathcal{S} \in ℒ(\mathcal{V}) is an invertible positive operator and \mathcal{T} \in ℒ(\mathcal{V}) is a
positiveoperator. Provethat\mathcal{S}+\mathcal{T} isinvertible.
8 Suppose\mathcal{T} \in ℒ(\mathcal{V}). Provethat\mathcal{T} isapositiveoperatorifandonlyifthe
pseudoinverse\mathcal{T}† isapositiveoperator.
9 Suppose \mathcal{T} \in ℒ(\mathcal{V}) is a positive operator and \mathcal{S} \in ℒ(\mathcal{W},\mathcal{V}). Prove that
∗
\mathcal{S} \mathcal{T}\mathcal{S}isapositiveoperatoron\mathcal{W}.
10 Suppose\mathcal{T} isapositiveoperatoron\mathcal{V}. Supposev,w\in\mathcal{V} aresuchthat
\mathcal{T}v=w and \mathcal{T}w=v.
Provethatv=w.
11 Suppose\mathcal{T} isapositiveoperatoron\mathcal{V} and\mathcal{U} isasubspaceof\mathcal{V} invariant
under\mathcal{T}. Provethat\mathcal{T}| \inℒ(\mathcal{U})isapositiveoperatoron\mathcal{U}.
\mathcal{U}
12 Suppose\mathcal{T} \inℒ(\mathcal{V})isapositiveoperator. Provethat\mathcal{T}kisapositiveoperator
foreverypositiveintegerk.

| -------- | ----------------------------- | --- | --- | --- | --- |
| 13 Suppose\mathcal{T} | \inℒ(\mathcal{V})isself-adjointand\alpha\in\mathbf{R}. |     |     |     |     |
| ----------- | -------------------------- | --- | --- | --- | --- |
$$(a) Provethat\mathcal{T}-\alpha\mathcal{I} isapositiveoperatorifandonlyif\alphaislessthanor$$
equaltoeveryeigenvalueof\mathcal{T}.
$$(b) Provethat\alpha\mathcal{I}-\mathcal{T} isapositiveoperatorifandonlyif\alphaisgreaterthanor$$
equaltoeveryeigenvalueof\mathcal{T}.
| 14 Suppose\mathcal{T} | isapositiveoperatoron\mathcal{V} |     | andv ,…,v | \in\mathcal{V}. | Provethat |
| ----------- | ---------------------- | --- | --------- | --- | --------- |
1 m
|     |     | m   | m   |     |     |
| --- | --- | --- | --- | --- | --- |
,v\rangle\geq0.
|     |     | \sum   | \sum\langle\mathcal{T}v |     |     |
| --- | --- | --- | ---- | --- | --- |
k j
$$j=1k=1$$
15 Suppose\mathcal{T} \inℒ(\mathcal{V})isself-adjoint. Provethatthereexistpositiveoperators
\mathcal{A},\mathcal{B}\inℒ(\mathcal{V})suchthat
|             | \mathcal{T} =\mathcal{A}-\mathcal{B}                  | and \sqrt\mathcal{T}∗\mathcal{T} | =\mathcal{A}+\mathcal{B}        | and \mathcal{A}\mathcal{B}=\mathcal{B}\mathcal{A}=0. |     |
| ----------- | ----------------------- | -------- | ----------- | ------------ | --- |
| 16 Suppose\mathcal{T} | isapositiveoperatoron\mathcal{V}. |          | Provethat   |              |     |
|             | null\sqrt\mathcal{T}                  | =null\mathcal{T}   | and range\sqrt\mathcal{T} | =range\mathcal{T}.     |     |
Suppose that \mathcal{T} \in ℒ(\mathcal{V}) is a positive operator. Prove that there exists a
| polynomialpwithrealcoefficientssuchthat\sqrt\mathcal{T} |     |     |     | =p(\mathcal{T}). |     |
| ----------------------------------------- | --- | --- | --- | ------ | --- |
18 Suppose \mathcal{S} and \mathcal{T} arepositiveoperators on \mathcal{V}. Provethat \mathcal{S}\mathcal{T} isapositive
| operatorifandonlyif\mathcal{S}and\mathcal{T} |     |     | commute. |     |     |
| ------------------------ | --- | --- | -------- | --- | --- |
19 Showthattheidentityoperatoron\mathbf{F}2hasinfinitelymanyself-adjointsquare
roots.
20 Suppose\mathcal{T} \inℒ(\mathcal{V})ande ,…,e isanorthonormalbasisof\mathcal{V}. Provethat
|                                             |     | 1   | n   |      |             |
| ------------------------------------------- | --- | --- | --- | ---- | ----------- |
| \mathcal{T} isapositiveoperatorifandonlyifthereexistv |     |     |     | ,…,v | \in\mathcal{V} suchthat |
1 n
|           |         | \langle\mathcal{T}e | ,e\rangle=\langlev ,v\rangle |     |     |
| --------- | ------- | --- | ---------- | --- | --- |
|           |         |     | k j k j    |     |     |
| forallj,k | =1,…,n. |     |            |     |     |
The numbers {\langle\mathcal{T}e ,e\rangle} are the entries in the matrix of \mathcal{T} with
k j j,k=1,…,n
|     | respecttotheorthonormalbasise |     | ,…,e . |     |     |
| --- | ----------------------------- | --- | ------ | --- | --- |
1 n
21 Suppose n is a positive integer. The n-by-n Hilbert matrix is the n-by-n
|                                |     |     | 1   |            | ℒ(\mathcal{V})isan |
| ------------------------------ | --- | --- | --- | ---------- | -------- |
| matrixwhoseentryinrowj,columnk |     |     | is  | . Suppose\mathcal{T} | \in        |
j+k-1
operatorwhosematrixwithrespecttosomeorthonormalbasisof\mathcal{V} isthe
n-by-nHilbertmatrix. Provethat\mathcal{T} isapositiveinvertibleoperator.
|     | Example: The4-by-4Hilbertmatrixis |     |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- |
1 1 1
|     |     | ⎛ ⎜ | 2 3 4 ⎞ ⎟      |     |     |
| --- | --- | --- | -------------- | --- | --- |
|     |     | ⎜   | ⎟              |     |     |
|     |     | ⎜ ⎜ | 1 1 1 1 ⎟ ⎟    |     |     |
|     |     | ⎜   | ⎟              |     |     |
|     |     | ⎜ ⎜ | 2 3 4 5 ⎟ ⎟ ⎟. |     |     |
|     |     | ⎜ ⎜ | ⎟              |     |     |
|     |     | ⎜   | 1 1 1 1 ⎟      |     |     |
|     |     | ⎜ ⎜ | 3 4 5 6 ⎟ ⎟    |     |     |
|     |     | ⎜   | ⎟              |     |     |
|     |     |     | 1 1 1 1        |     |     |
|     |     | ⎝   | ⎠              |     |     |
|     |     |     | 4 5 6 7        |     |     |

| --- | --- | --------- | ----------------- |
22 Suppose\mathcal{T} \in ℒ(\mathcal{V})isapositiveoperatorandu \in \mathcal{V} issuchthat‖u‖ = 1
| and‖\mathcal{T}u‖\geq‖\mathcal{T}v‖forallv\in\mathcal{V} |     | with‖v‖=1. | Showthatuisaneigenvector |
| --------------------- | --- | ---------- | ------------------------ |
of\mathcal{T} correspondingtothelargesteigenvalueof\mathcal{T}.
| 23 For\mathcal{T} \inℒ(\mathcal{V})andu,v\in\mathcal{V},define\langleu,v\rangle |     |     | by\langleu,v\rangle =\langle\mathcal{T}u,v\rangle. |
| --------------------------------- | --- | --- | ---------------- |
\mathcal{T} \mathcal{T}
$$(a) Suppose\mathcal{T} \in ℒ(\mathcal{V}). Provethat\langle\cdot,\cdot\rangle isaninnerproducton\mathcal{V} ifand$$
\mathcal{T}
onlyif\mathcal{T} isaninvertiblepositiveoperator(withrespecttotheoriginal
innerproduct\langle\cdot,\cdot\rangle).
$$(b) Prove that every inner product on \mathcal{V} is of the form \langle\cdot,\cdot\rangle for some$$
\mathcal{T}
\inℒ(\mathcal{V}).
positiveinvertibleoperator\mathcal{T}
| 24 Suppose\mathcal{S}and\mathcal{T} | arepositiveoperatorson\mathcal{V}. |     | Provethat |
| --------------- | ------------------------ | --- | --------- |
null(\mathcal{S}+\mathcal{T})=null\mathcal{S}\capnull\mathcal{T}.
25 Let \mathcal{T} be the second derivative operator in Exercise 31(b) in Section 7A.
| Showthat-\mathcal{T} | isapositiveoperator. |     |     |
| ---------- | -------------------- | --- | --- |

258 Chapter 7 Operatorson Inner Product Spaces
### 7D Isometries, Unitary Operators, and Matrix Factorization
Isometries
Linearmapsthatpreservenormsaresufficientlyimportanttodeserveaname.
**7.44 定义：** isometry
Alinearmap\mathcal{S}\inℒ(\mathcal{V},\mathcal{W})iscalledanisometryif
‖\mathcal{S}v‖=‖v‖
foreveryv \in \mathcal{V}. Inotherwords,alinearmapisanisometryifitpreserves
norms.
If \mathcal{S} \in ℒ(\mathcal{V},\mathcal{W}) is an isometry and
The Greekwordisosmeansequal;the
v\in\mathcal{V} issuchthat\mathcal{S}v=0,then
Greek word metron means measure.
‖v‖=‖\mathcal{S}v‖=‖0‖=0, Thus isometry literally means equal
measure.
which implies that v = 0. Thus every
isometryisinjective.
**7.45 例：** orthonormalbasismapstoorthonormallist ⟹ isometry
Supposee ,…,e isanorthonormalbasisof\mathcal{V}andg ,…,g isanorthonormal
1 n 1 n
list in \mathcal{W}. Let \mathcal{S} \in ℒ(\mathcal{V},\mathcal{W}) be the linear map such that \mathcal{S}e = g for each
k k
$$k =1,…,n. Toshowthat\mathcal{S}isanisometry,supposev\in\mathcal{V}. Then$$
7.46 v=\langlev,e \ranglee +⋯+\langlev,e \ranglee
1 1 n n
and
7.47 ‖v‖2 =∣\langlev,e \rangle∣2+⋯+∣\langlev,e \rangle∣2,
1 n
wherewehaveused6.30(b). Applying\mathcal{S}tobothsidesof7.46gives
\mathcal{S}v=\langlev,e \rangle\mathcal{S}e +⋯+\langlev,e \rangle\mathcal{S}e =\langlev,e \rangleg +⋯+\langlev,e \rangleg .
1 1 n n 1 1 n n
Thus
7.48 ‖\mathcal{S}v‖2 =∣\langlev,e \rangle∣2+⋯+|\langlev,e \rangle|2.
1 n
Comparing7.47and7.48showsthat‖v‖=‖\mathcal{S}v‖. Thus\mathcal{S}isanisometry.
Thenextresultgivesconditionsequivalenttobeinganisometry. Theequivalence of (a) and (c) shows that a linear map is an isometry if and only if it
preservesinnerproducts. Theequivalenceof(a)and(d)showsthatalinearmap
isanisometryifandonlyifitmapssomeorthonormalbasistoanorthonormallist.
Thustheisometriesgivenby Example7.45includeallisometries. Furthermore,
alinearmapisanisometryifandonlyifitmapseveryorthonormalbasistoan
orthonormallist[becausewhetherornot(a)holdsdoesnotdependonthebasis
e ,…,e ].
1 n

| --------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Theequivalenceof(a)and(e)inthenextresultshowsthatalinearmapisan
isometryifandonlyifthecolumnsofitsmatrix(withrespecttoanyorthonormal
bases)formanorthonormallist. Hereweareidentifyingthecolumnsofanm-by-n
matrixwithelementsof\mathbf{F}m andthenusingthe Euclideaninnerproducton\mathbf{F}m.
7.49 characterizationsofisometries
| Suppose\mathcal{S}\inℒ(\mathcal{V},\mathcal{W}). |     |     | Supposee | ,…,e | isanorthonormalbasisof\mathcal{V} |     |     | and |
| ---------------- | --- | --- | -------- | ---- | ----------------------- | --- | --- | --- |
|                  |     |     |          | 1    | n                       |     |     |     |
f ,…, f isanorthonormalbasisof\mathcal{W}. Thenthefollowingareequivalent.
1 m
$$(a) \mathcal{S}isanisometry.$$
∗
$$(b) \mathcal{S} \mathcal{S}=\mathcal{I}.$$
$$(c) \langle\mathcal{S}u,\mathcal{S}v\rangle=\langleu,v\rangleforallu,v\in\mathcal{V}.$$
| (d) | \mathcal{S}e ,…,\mathcal{S}e | isanorthonormallistin\mathcal{W}. |     |     |     |     |     |     |
| --- | -------- | ----------------------- | --- | --- | --- | --- | --- | --- |
|     | 1        | n                       |     |     |     |     |     |     |
$$(e) Thecolumnsofℳ(\mathcal{S},(e ,…,e ),(f ,…, f ))formanorthonormallist$$
|       |                                             |     |     | 1 n                             | 1   | m     |      |     |
| ----- | ------------------------------------------- | --- | --- | ------------------------------- | --- | ----- | ---- | --- |
|       | in\mathbf{F}m withrespecttothe Euclideaninnerproduct. |     |     |                                 |     |       |      |     |
| Proof | Firstsuppose(a)holds,so\mathcal{S}isanisometry.       |     |     |                                 |     | Ifv\in\mathcal{V} | then |     |
| \langle(\mathcal{I}-\mathcal{S} | ∗ \mathcal{S})v,v\rangle=\langlev,v\rangle-\langle\mathcal{S}                           |     |     | ∗ \mathcal{S}v,v\rangle=‖v‖2-\langle\mathcal{S}v,\mathcal{S}v\rangle=‖v‖2-‖\mathcal{S}v‖2 |     |       |      | =0. |
|       |                                             |     |     | ∗                               |     |       | ∗    |     |
Hencetheself-adjointoperator\mathcal{I}-\mathcal{S} \mathcal{S}equals0(by7.16). Thus\mathcal{S} \mathcal{S}=\mathcal{I},proving
that(a)implies(b).
∗
| Nowsuppose(b)holds,so\mathcal{S} |     |     |     | \mathcal{S}=\mathcal{I}. | Ifu,v\in\mathcal{V} | then |     |     |
| ---------------------- | --- | --- | --- | ---- | ------- | ---- | --- | --- |
∗
|     |     | \langle\mathcal{S}u,\mathcal{S}v\rangle=\langle\mathcal{S} |     | \mathcal{S}u,v\rangle=\langle\mathcal{I}u,v\rangle=\langleu,v\rangle, |     |     |     |     |
| --- | --- | ---------- | --- | ------------------- | --- | --- | --- | --- |
provingthat(b)implies(c).
Now suppose that (c) holds, so \langle\mathcal{S}u,\mathcal{S}v\rangle = \langleu,v\rangle for all u,v \in \mathcal{V}. Thus if
j,k \in{1,…,n},then
|     |     |     |     | \langle\mathcal{S}e,\mathcal{S}e | \rangle=\langlee,e | \rangle.  |     |     |
| --- | --- | --- | --- | ------ | ------ | --- | --- | --- |
|     |     |     |     | j k    | j      | k   |     |     |
Hence\mathcal{S}e ,…,\mathcal{S}e isanorthonormallistin\mathcal{W},provingthat(c)implies(d).
|     | 1   | n   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Nowsupposethat(d)holds,so\mathcal{S}e ,…,\mathcal{S}e isanorthonormallistin\mathcal{W}. Let
|          |     |         |          | 1           | n             |     |      |         |
| -------- | --- | ------- | -------- | ----------- | ------------- | --- | ---- | ------- |
| \mathcal{A}=ℳ(\mathcal{S},(e |     | ,…,e    | ),(f ,…, | f )). Ifk,r | \in{1,…,n},then |     |      |         |
|          |     | 1 n     | 1        | m           |               |     |      |         |
|          | m   |         | m        | m           |               |     | ⎧ {1 | ifk =r, |
| 7.50     | \sum\mathcal{A}  | \mathcal{A}       | =\langle\sum\mathcal{A}     | f ,\sum\mathcal{A}       | f \rangle=\langle\mathcal{S}e       | ,\mathcal{S}e | \rangle=   |         |
|          |     | j,k j,r |          | j,k j       | j,r j         | k r | ⎨ {0 | ifk \neqr. |
|          | j=1 |         | j=1      | j=1         |               |     | ⎩    |         |
Theleftsideof7.50istheinnerproductin\mathbf{F}m ofcolumnskandrof\mathcal{A}. Thusthe
columnsof\mathcal{A}formanorthonormallistin\mathbf{F}m,provingthat(d)implies(e).
Nowsuppose(e)holds,sothecolumnsofthematrix\mathcal{A}definedintheparagraph
\mathbf{F}m.
above form an orthonormal list in Then 7.50 shows that \mathcal{S}e ,…,\mathcal{S}e is an
|     |     |     |     |     |     |     |     | 1 n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
orthonormallistin\mathcal{W}. Thus Example7.45,with\mathcal{S}e ,…,\mathcal{S}e playingtheroleof
|     |     |     |     |     |     | 1   | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
g ,…,g ,showsthat\mathcal{S}isanisometry,provingthat(e)implies(a).
1 n
See Exercises1and11foradditionalconditionsthatareequivalenttobeing
anisometry.

| -------- | ----------------------------- | --- | --- | --- |
Inthissubsection,weconfineourattentiontolinearmapsfromavectorspaceto
itself. Inotherwords,wewillbeworkingwithoperators.
| 7.51 definition: | unitaryoperator |     |     |     |
| ---------------- | --------------- | --- | --- | --- |
Anoperator\mathcal{S}\inℒ(\mathcal{V})iscalledunitaryif\mathcal{S}isaninvertibleisometry.
Aspreviouslynoted,everyisometry
|     |     | Although | the words “unitary” | and |
| --- | --- | -------- | ------------------- | --- |
isinjective. Everyinjectiveoperatoron “isometry” mean the same thing for
| a finite-dimensional | vector space | is in- |     |     |
| -------------------- | ------------ | ------ | --- | --- |
operatorsonfinite-dimensionalinner
vertible(see3.65). Astandingassump- productspaces,rememberthatauni-
| tionforthischapteristhat\mathcal{V} | isafinite- |     |     |     |
| ------------------------- | ---------- | --- | --- | --- |
taryoperatormapsavectorspaceto
dimensionalinnerproductspace. Thus itself,whileanisometrymapsavector
we could delete the word “invertible” space to another (possibly different)
| fromthedefinitionabovewithoutchang- |                    | vectorspace. |     |     |
| ----------------------------------- | ------------------ | ------------ | --- | --- |
| ingthemeaning.                      | Theunnecessaryword |              |     |     |
“invertible” has been retained in the definition above for consistency with the
definitionreadersmayencounterwhenlearningaboutinnerproductspacesthat
arenotnecessarilyfinite-dimensional.
| 7.52 example: rotationof | \mathbf{R}2  |     |     |     |
| ------------------------ | --- | --- | --- | --- |
Suppose\theta \in\mathbf{R} and\mathcal{S}istheoperatoron\mathbf{F}2 whosematrixwithrespecttothe
| standardbasisof\mathbf{F}2 | is  |     |     |     |
| ----------------- | --- | --- | --- | --- |
cos\theta -sin\theta
$$( ).$$
sin\theta cos\theta
The two columns of this matrix form an orthonormal list in \mathbf{F}2; hence \mathcal{S} is an
isometry[bytheequivalenceof(a)and(e)in7.49]. Thus\mathcal{S}isaunitaryoperator.
If \mathbf{F} = \mathbf{R}, then \mathcal{S} is the operator of counterclockwise rotation by \theta radians
aroundtheoriginof\mathbf{R}2. Thisobservationgivesusanotherwaytothinkaboutwhy
\mathcal{S}isanisometry,becauseeachrotationaroundtheoriginof\mathbf{R}2 preservesnorms.
Thenextresult(7.53)listsseveralconditionsthatareequivalenttobeinga
unitaryoperator. Alltheconditionsequivalenttobeinganisometryin7.49should
beaddedtothislist. Theextraconditionsin7.53arisebecauseoflimitingthe
contexttolinearmapsfromavectorspacetoitself. Forexample,7.49showsthat
alinearmap\mathcal{S}\inℒ(\mathcal{V},\mathcal{W})isanisometryifandonlyif\mathcal{S} ∗ \mathcal{S}=\mathcal{I},while7.53shows
|                                                    |     |     | ∗    | ∗   |
| -------------------------------------------------- | --- | --- | ---- | --- |
| thatanoperator\mathcal{S}\inℒ(\mathcal{V})isaunitaryoperatorifandonlyif\mathcal{S} |     |     | \mathcal{S}=\mathcal{S}\mathcal{S} | =\mathcal{I}. |
Anotherdifferenceisthat7.49(d)mentionsanorthonormallist,while7.53(d)
mentionsanorthonormalbasis. Also,7.49(e)mentionsthecolumnsofℳ(\mathcal{T}),
while7.53(e)mentionstherowsofℳ(\mathcal{T}). Furthermore,ℳ(\mathcal{T})in7.49(e)iswith
respecttoanorthonormalbasisof\mathcal{V}andanorthonormalbasisof\mathcal{W},whileℳ(\mathcal{T})
in7.53(e)iswithrespecttoasinglebasisof\mathcal{V} doingdoubleduty.

| --------- | -------------------------------------------------- | --- | --- | --- |
characterizationsofunitaryoperators
7.53
| Suppose\mathcal{S} | \in ℒ(\mathcal{V}). | Supposee ,…,e | isanorthonormalbasisof\mathcal{V}. | Then |
| -------- | ------- | ------------- | ------------------------ | ---- |
|          |         | 1 n           |                          |      |
thefollowingareequivalent.
$$(a) \mathcal{S}isaunitaryoperator.$$
| ∗                   | ∗                        |      |     |     |
| ------------------- | ------------------------ | ---- | --- | --- |
| (b) \mathcal{S} \mathcal{S}=\mathcal{S}\mathcal{S}          | =\mathcal{I}.                      |      |     |     |
| \mathcal{S}isinvertibleand\mathcal{S}-1 |                          | ∗    |     |     |
| (c)                 |                          | =\mathcal{S} . |     |     |
| (d) \mathcal{S}e ,…,\mathcal{S}e        | isanorthonormalbasisof\mathcal{V}. |      |     |     |
| 1                   | n                        |      |     |     |
$$(e) The rows of ℳ(\mathcal{S},(e ,…,e )) form an orthonormal basis of \mathbf{F}n with$$
1 n
respecttothe Euclideaninnerproduct.
∗
$$(f) \mathcal{S} isaunitaryoperator.$$
Proof Firstsuppose(a)holds,so\mathcal{S}isaunitaryoperator. Hence
∗
|     |     | \mathcal{S} \mathcal{S}=\mathcal{I} |     |     |
| --- | --- | ----- | --- | --- |
bytheequivalenceof(a)and(b)in7.49. Multiplybothsidesofthisequationby
| \mathcal{S}-1                 |     | ∗ \mathcal{S}-1.   | ∗ \mathcal{S}\mathcal{S}-1                  |     |
| ------------------- | --- | -------- | ----------------------- | --- |
| ontheright,getting\mathcal{S} |     | = Thus\mathcal{S}\mathcal{S} | = = \mathcal{I},asdesired,proving |     |
that(a)implies(b).
Thedefinitionsofinvertibleandinverseshowthat(b)implies(c).
Nowsuppose(c)holds,so\mathcal{S}isinvertibleand\mathcal{S}-1 =\mathcal{S} ∗ . Thus\mathcal{S} ∗ \mathcal{S}=\mathcal{I}. Hence
\mathcal{S}e ,…,\mathcal{S}e isanorthonormallistin\mathcal{V},bytheequivalenceof(b)and(d)in7.49.
| 1 n |     |     |     |     |
| --- | --- | --- | --- | --- |
The length of this list equals dim\mathcal{V}. Thus \mathcal{S}e ,…,\mathcal{S}e is an orthonormal basis
1 n
of\mathcal{V},provingthat(c)implies(d).
Now suppose (d) holds, so \mathcal{S}e ,…,\mathcal{S}e is an orthonormal basis of \mathcal{V}. The
|     |     | 1   | n   |     |
| --- | --- | --- | --- | --- |
equivalenceof(a)and(d)in7.49showsthat\mathcal{S}isaunitaryoperator. Thus
|     |     | ∗ ∗ ∗      | ∗   |     |
| --- | --- | ---------- | --- | --- |
|     |     | (\mathcal{S} ) \mathcal{S} =\mathcal{S}\mathcal{S} | =\mathcal{I}, |     |
wherethelastequationholdsbecausewealreadyshowedthat(a)implies(b)inthis
∗
result. Theequationaboveandtheequivalenceof(a)and(b)in7.49showthat\mathcal{S}
isanisometry. Thusthecolumnsofℳ(\mathcal{S} ∗,(e ,…,e ))formanorthonormalbasis
1 n
of\mathbf{F}n
| [bytheequivalenceof(a)and(e)of7.49]. |     |     | Therowsofℳ(\mathcal{S},(e | ,…,e )) |
| ------------------------------------ | --- | --- | --------------- | ------- |
1 n
arethecomplexconjugatesofthecolumnsofℳ(\mathcal{S} ∗,(e ,…,e )). Thustherows
1 n
$$))formanorthonormalbasisof\mathbf{F}n,provingthat(d)implies(e).$$
| ofℳ(\mathcal{S},(e | ,…,e |     |     |     |
| -------- | ---- | --- | --- | --- |
1 n
Now suppose (e) holds. Thus the columns of ℳ(\mathcal{S} ∗,(e ,…,e )) form an
1 n
| orthonormalbasisof\mathbf{F}n. |     |                                           |     | ∗   |
| --------------------- | --- | ----------------------------------------- | --- | --- |
|                       |     | Theequivalenceof(a)and(e)in7.49showsthat\mathcal{S} |     | is  |
anisometry,provingthat(e)implies(f).
∗
Nowsuppose(f)holds,so\mathcal{S} isaunitaryoperator. Thechainofimplications
wehavealreadyprovedinthisresultshowsthat(a)implies(f). Applyingthis
| ∗   |     | ∗ ∗ |     |     |
| --- | --- | --- | --- | --- |
resultto\mathcal{S} showsthat(\mathcal{S} ) isaunitaryoperator,provingthat(f)implies(a).
Wehaveshownthat(a)\Rightarrow(b)\Rightarrow(c)\Rightarrow(d)\Rightarrow(e)\Rightarrow(f)\Rightarrow(a),completingthe
proof.

262 Chapter 7 Operatorson Inner Product Spaces
Recall our analogy between \mathbf{C} and ℒ(\mathcal{V}). Under this analogy, a complex
numberzcorrespondstoanoperator\mathcal{S} \in ℒ(\mathcal{V}),andzcorrespondsto\mathcal{S} ∗ . The
∗
realnumbers(z=z)correspondtotheself-adjointoperators(\mathcal{S}=\mathcal{S} ),andthe
nonnegativenumberscorrespondtothe(badlynamed)positiveoperators.
Another distinguished subset of \mathbf{C} is the unit circle, which consists of the
complexnumberszsuchthat|z| = 1. Thecondition|z| = 1isequivalenttothe
∗
conditionzz=1. Underouranalogy,thiscorrespondstothecondition\mathcal{S} \mathcal{S}=\mathcal{I},
whichisequivalentto\mathcal{S}beingaunitaryoperator. Hencetheanalogyshowsthat
theunitcirclein\mathbf{C} correspondstothesetofunitaryoperators. Inthenexttwo
results, thisanalogyappearsintheeigenvaluesofunitaryoperators. Alsosee
Exercise15foranotherexampleofthisanalogy.
7.54 eigenvaluesofunitaryoperatorshaveabsolutevalue1
Suppose \lambdaisaneigenvalueofaunitaryoperator. Then|\lambda|=1.
Proof Suppose\mathcal{S}\inℒ(\mathcal{V})isaunitaryoperatorand \lambdaisaneigenvalueof\mathcal{S}. Let
v\in\mathcal{V} besuchthatv\neq0and\mathcal{S}v= \lambdav. Then
|\lambda|‖v‖=‖\lambdav‖=‖\mathcal{S}v‖=‖v‖.
Thus|\lambda|=1,asdesired.
Thenextresultcharacterizesunitaryoperatorsonfinite-dimensionalcomplex
innerproductspaces,usingthecomplexspectraltheoremasthemaintool.
7.55 descriptionofunitaryoperatorsoncomplexinnerproductspaces
Suppose\mathbf{F} =\mathbf{C} and\mathcal{S}\inℒ(\mathcal{V}). Thenthefollowingareequivalent.
$$(a) \mathcal{S}isaunitaryoperator.$$
$$(b) Thereisanorthonormalbasisof\mathcal{V} consistingofeigenvectorsof\mathcal{S}whose$$
correspondingeigenvaluesallhaveabsolutevalue1.
Proof Suppose(a)holds,so\mathcal{S}isaunitaryoperator. Theequivalenceof(a)and
$$(b) in 7.53 shows that \mathcal{S} is normal. Thus the complex spectral theorem (7.31)$$
showsthatthereisanorthonormalbasise ,…,e of\mathcal{V} consistingofeigenvectors
1 n
of\mathcal{S}. Everyeigenvalueof\mathcal{S}hasabsolutevalue1(by7.54),completingtheproof
that(a)implies(b).
Nowsuppose(b)holds. Lete ,…,e beanorthonormalbasisof\mathcal{V} consisting
1 n
ofeigenvectorsof\mathcal{S}whosecorrespondingeigenvalues \lambda ,…,\lambda allhaveabsolute
1 n
value1. Then\mathcal{S}e ,…,\mathcal{S}e isalsoanorthonormalbasisof\mathcal{V}because
1 n
⎧ {0 ifj \neqk,
\langle\mathcal{S}e,\mathcal{S}e \rangle=\langle\lambdae,\lambda e \rangle= \lambda \lambda \langlee,e \rangle=
j k j j k k j k j k ⎨ {1 ifj =k
⎩
forallj,k =1,…,n. Thustheequivalenceof(a)and(d)in7.53showsthat\mathcal{S}is
unitary,provingthat(b)implies(a).

Section7D Isometries,Unitary Operators,and Matrix Factorization 263
QR Factorization
Inthissubsection,weshiftourattentionfromoperatorstomatrices. Thisswitch
shouldgiveyougoodpracticeinidentifyinganoperatorwithasquarematrix
$$(afterpickingabasisofthevectorspaceonwhichtheoperatorisdefined). You$$
shouldalsobecomemorecomfortablewithtranslatingconceptsandresultsback
andforthbetweenthecontextofoperatorsandthecontextofsquarematrices.
When starting with n-by-n matrices instead of operators, unless otherwise
specifiedassumethattheassociatedoperatorsliveon\mathbf{F}n(withthe Euclideaninner
product)andthattheirmatricesarecomputedwithrespecttothestandardbasis
of\mathbf{F}n.
We begin by making the following definition, transferring the notion of a
unitaryoperatortoaunitarymatrix.
**7.56 定义：** unitarymatrix
An n-by-n matrix is called unitary if its columns form an orthonormal list
in\mathbf{F}n.
Inthedefinitionabove,wecouldhavereplaced“orthonormallistin\mathbf{F}n”with
“orthonormal basis of \mathbf{F}n” because every orthonormal list of length n in an ndimensional inner product space is an orthonormal basis. If \mathcal{S} \in ℒ(\mathcal{V}) and
e ,…,e and f ,…, f areorthonormalbasesof\mathcal{V},then\mathcal{S}isaunitaryoperator
1 n 1 n
ifandonlyifℳ(\mathcal{S},(e ,…,e ),(f ,…, f ))isaunitarymatrix,asshownbythe
1 n 1 n
equivalenceof(a)and(e)in7.49. Alsonotethatwecouldalsohavereplaced
“columns”inthedefinitionabovewith“rows”byusingtheequivalencebetween
conditions(a)and(e)in7.53.
Thenextresult,whoseproofwillbeleftasanexerciseforthereader,gives
someequivalentconditionsforasquarematrixtobeunitary. In(c),\mathcal{Q}vdenotes
thematrixproductof\mathcal{Q}andv,identifyingelementsof\mathbf{F}n withn-by-1matrices
$$(sometimescalledcolumnvectors). Thenormin(c)belowistheusual Euclidean$$
norm on \mathbf{F}n that comes from the Euclidean inner product. In (d), \mathcal{Q} ∗ denotes
theconjugatetransposeofthematrix\mathcal{Q},whichcorrespondstotheadjointofthe
associatedoperator.
7.57 characterizationsofunitarymatrices
Suppose\mathcal{Q}isann-by-nmatrix. Thenthefollowingareequivalent.
$$(a) \mathcal{Q}isaunitarymatrix.$$
$$(b) Therowsof\mathcal{Q}formanorthonormallistin\mathbf{F}n.$$
$$(c) ‖\mathcal{Q}v‖=‖v‖foreveryv\in\mathbf{F}n.$$
∗ ∗
$$(d) \mathcal{Q} \mathcal{Q} = \mathcal{Q}\mathcal{Q} = \mathcal{I}, the n-by-n matrix with 1’s on the diagonal and 0’s$$
elsewhere.

| --- | -------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
The QRfactorizationstatedandprovedbelowisthemaintoolinthewidely
used QR algorithm (not discussed here) for finding good approximations to
eigenvaluesandeigenvectorsofsquarematrices. Intheresultbelow,ifthematrix
\mathcal{A}isin\mathbf{F}n,n,thenthematrices\mathcal{Q}and\mathcal{R}arealsoin\mathbf{F}n,n.
7.58 QRfactorization
Suppose\mathcal{A}isasquarematrixwithlinearlyindependentcolumns. Thenthere
existuniquematrices\mathcal{Q}and\mathcal{R}suchthat\mathcal{Q}isunitary, \mathcal{R}isuppertriangular
withonlypositivenumbersonitsdiagonal,and
\mathcal{A}=\mathcal{Q}\mathcal{R}.
|       | Letv ,…,v | denotethecolumnsof\mathcal{A},thoughtofaselementsof\mathbf{F}n. |     |     |     |     | Apply |     |
| ----- | --------- | -------------------------------------------- | --- | --- | --- | --- | ----- | --- |
| Proof | 1         | n                                            |     |     |     |     |       |     |
the Gram–Schmidtprocedure(6.32)tothelistv ,…,v ,gettinganorthonormal
1 n
| basise   | ,…,e of\mathbf{F}n | suchthat                       |      |            |      |     |     |     |
| -------- | --------- | ------------------------------ | ---- | ---------- | ---- | --- | --- | --- |
|          | 1 n       |                                |      |            |      |     |     |     |
|          |           | span(v                         | ,…,v | )=span(e   | ,…,e | )   |     |     |
| 7.59     |           |                                | 1    | k          | 1    | k   |     |     |
| foreachk | =1,…,n.   | Let\mathcal{R}bethen-by-nmatrixdefinedby |      |            |      |     |     |     |
|          |           |                                |      | \mathcal{R} =\langlev ,e\rangle, |      |     |     |     |
|          |           |                                |      | j,k k      | j    |     |     |     |
where\mathcal{R} denotestheentryinrowj,columnkof\mathcal{R}. Ifj >k,thene isorthogonal
|     | j,k |     |     |     |     |     | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
tospan(e ,…,e )andhencee isorthogonaltov (by7.59). Inotherwords,if
|            | 1 k    |                                  | j   |     | k   |     |     |     |
| ---------- | ------ | -------------------------------- | --- | --- | --- | --- | --- | --- |
| j >kthen\langlev | ,e\rangle=0. | Thus\mathcal{R}isanupper-triangularmatrix. |     |     |     |     |     |     |
k j
|     | Let\mathcal{Q}betheunitarymatrixwhosecolumnsaree |     |     |     |     | ,…,e . | Ifk \in {1,…,n}, |     |
| --- | -------------------------------------- | --- | --- | --- | --- | ------ | -------------- | --- |
|     |                                        |     |     |     |     | 1 n    |                |     |
thenthekth columnof\mathcal{Q}\mathcal{R}equalsalinearcombinationofthecolumnsof\mathcal{Q},with
thecoefficientsforthelinearcombinationcomingfromthekth columnof\mathcal{R}—see
| 3.51(a). | Hencethekth | columnof\mathcal{Q}\mathcal{R}equals |       |          |       |     |     |     |
| -------- | ----------- | ---------------- | ----- | -------- | ----- | --- | --- | --- |
|          |             |                  | \langlev ,e | \ranglee +⋯+\langlev | ,e \ranglee | ,   |     |     |
|          |             |                  | k 1   | 1        | k k   | k   |     |     |
[by6.30(a)],thekth
| whichequalsv |     |     |     | columnof\mathcal{A}. |     | Thus\mathcal{A}=\mathcal{Q}\mathcal{R},asdesired. |     |     |
| ------------ | --- | --- | --- | ---------- | --- | ------------------- | --- | --- |
k
The equations defining the Gram–Schmidt procedure (see 6.32) show that
,…,e
| eachv | equalsapositivemultipleofe |     |     | plusalinearcombinationofe |     |     |     | .   |
| ----- | -------------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
|       | k                          |     |     | k                         |     |     | 1   | k-1 |
Thuseach\langlev ,e \rangleisapositivenumber. Henceallentriesonthediagonalof\mathcal{R}are
k k
positivenumbers,asdesired.
Finally,toshowthat\mathcal{Q}and\mathcal{R}areunique,supposewealsohave\mathcal{A}=\mathcal{Q}\mathcal{R},where ̂̂
| \mathcal{Q}isunitaryand\mathcal{R}isuppertriangularwithonlypositivenumbersonitsdiagonal. ̂ |     | ̂   |     |     |     |     |     |     |
| ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
̂
Letq ,…,q denotethecolumnsof\mathcal{Q} . Thinkingofmatrixmultiplicationasabove,
|     | 1 n |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
weseethateachv isalinearcombinationofq ,…,q ,withthecoefficientscom-
|     |     | k   |     |     | 1   | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ingfromthekthcolumnof\mathcal{R} ̂ . Thisimpliesthatspan(v ,…,v )=span(q ,…,q )
|     |     |     |     |     |     | 1 k | 1   | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
and\langlev ,q \rangle>0. Theuniquenessoftheorthonormallistssatisfyingthesecondik k
tions(see Exercise10in Section6B)nowshowsthatq =e foreachk =1,…,n.
|     |     |     |     |     |     | k k |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | ̂   |     |     | ̂   |     |     |     |     |
Hence\mathcal{Q}=\mathcal{Q},whichthenimpliesthat\mathcal{R}=\mathcal{R},completingtheproofofuniqueness.

Section7D Isometries,Unitary Operators,and Matrix Factorization 265
Theproofofthe QRfactorizationshowsthatthecolumnsoftheunitarymatrix
canbecomputedbyapplyingthe Gram–Schmidtproceduretothecolumnsofthe
matrixtobefactored. Thenextexampleillustratesthecomputationofthe QR
factorizationbasedontheproofthatwejustcompleted.
**7.60 例：** QRfactorizationofa3-by-3matrix
Tofindthe QRfactorizationofthematrix
1 2 1
⎛ ⎞
⎜ ⎟
\mathcal{A}=⎜ ⎜ 0 1 -4 ⎟ ⎟ ,
⎝ 0 3 2 ⎠
followtheproofof7.58. Thussetv ,v ,v equaltothecolumnsof\mathcal{A}:
1 2 3
$$v =(1,0,0), v =(2,1,3), v =(1,-4,2).$$
1 2 3
Applythe Gram–Schmidtproceduretov ,v ,v ,producingtheorthonormallist
1 2 3
$$e =(1,0,0), e =(0, 1 , 3 ), e =(0,- 3 , 1 ).$$
1 2 \sqrt10 \sqrt10 3 \sqrt10 \sqrt10
Stillfollowingtheproofof7.58,let\mathcal{Q}betheunitarymatrixwhosecolumnsare
e ,e ,e :
1 2 3
1 0 0
⎛ ⎞
⎜ ⎟
\mathcal{Q}= ⎜ ⎜ ⎜ ⎜ ⎜ 0 \sqrt 1 10 - \sqrt 3 10 ⎟ ⎟ ⎟ ⎟ ⎟ .
⎜ ⎟
⎜ ⎟
0 3 1
⎝ \sqrt10 \sqrt10 ⎠
Asintheproofof7.58,let\mathcal{R}bethe3-by-3matrixwhoseentryinrowj,columnk
is\langlev ,e\rangle,whichgives
k j
1 2 1
⎛ ⎞
⎜ ⎟
⎜ ⎟
\mathcal{R}= ⎜ ⎜ ⎜ ⎜ 0 \sqrt10 \sqrt 5 10 ⎟ ⎟ ⎟ ⎟ .
⎜ ⎟
⎜ ⎟
⎝ 0 0
7\sqrt10
⎠
Notethat\mathcal{R}isindeedanupper-triangularmatrixwithonlypositivenumberson
thediagonal,asrequiredbythe QRfactorization.
Nowmatrixmultiplicationcanverifythat\mathcal{A}=\mathcal{Q}\mathcal{R}isthedesiredfactorization
of\mathcal{A}:
1 0 0 1 2 1
⎛ ⎞⎛ ⎞
⎜ ⎟⎜ ⎟ 1 2 1
\mathcal{Q}\mathcal{R}= ⎜ ⎜ ⎜ ⎜ ⎜ 0 \sqrt 1 10 - \sqrt 3 10 ⎟ ⎟ ⎟ ⎟ ⎟ ⎜ ⎜ ⎜ ⎜ ⎜ 0 \sqrt10 \sqrt 5 10 ⎟ ⎟ ⎟ ⎟ ⎟ = ⎛ ⎜ ⎜ ⎜ 0 1 -4 ⎞ ⎟ ⎟ ⎟=\mathcal{A}.
⎜ ⎟⎜ ⎟
⎜ ⎝ 0 \sqrt 3 10 \sqrt 1 10 ⎟ ⎠ ⎜ ⎝ 0 0 7\sqrt 5 10 ⎟ ⎠ ⎝ 0 3 2 ⎠
Thus\mathcal{A}=\mathcal{Q}\mathcal{R},asexpected.
The QRfactorizationwillbethemajortoolusedintheproofofthe Cholesky
factorization(7.63)inthenextsubsection. Foranotherniceapplicationofthe QR
factorization,seetheproofof Hadamard’sinequality(9.66).

266 Chapter 7 Operatorson Inner Product Spaces
Ifa QRfactorizationisavailable,thenitcanbeusedtosolveacorresponding
system of linear equations without using Gaussian elimination. Specifically,
suppose\mathcal{A}isann-by-nsquarematrixwithlinearlyindependentcolumns. Suppose
thatb\in\mathbf{F}n andwewanttosolvetheequation\mathcal{A}x =bforx =(x ,…,x )\in\mathbf{F}n
1 n
$$(asusual,weareidentifyingelementsof\mathbf{F}n withn-by-1columnvectors).$$
Suppose \mathcal{A} = \mathcal{Q}\mathcal{R}, where \mathcal{Q} is unitary and \mathcal{R} is upper triangular with only
positivenumbersonitsdiagonal(\mathcal{Q}and\mathcal{R}arecomputablefrom\mathcal{A}usingjustthe
Gram–Schmidtprocedure,asshownintheproofof7.58). Theequation\mathcal{A}x =bis
equivalenttotheequation\mathcal{Q}\mathcal{R}x =b. Multiplyingbothsidesofthislastequation
∗
by\mathcal{Q} ontheleftandusing7.57(d)givestheequation
∗
\mathcal{R}x =\mathcal{Q} b.
∗
Thematrix\mathcal{Q} istheconjugatetransposeofthematrix\mathcal{Q}. Thuscomputing
∗
\mathcal{Q} b is straightforward. Because \mathcal{R} is an upper-triangular matrix with positive
numbersonitsdiagonal,thesystemoflinearequationsrepresentedbytheequation
abovecanquicklybesolvedbyfirstsolvingforx ,thenforx ,andsoon.
n n-1
Webeginthissubsectionwithacharacterizationofpositiveinvertibleoperators
intermsofinnerproducts.
7.61 positiveinvertibleoperator
Aself-adjointoperator\mathcal{T} \inℒ(\mathcal{V})isapositiveinvertibleoperatorifandonly
if\langle\mathcal{T}v,v\rangle>0foreverynonzerov\in\mathcal{V}.
Proof Firstsuppose\mathcal{T} isapositiveinvertibleoperator. Ifv\in\mathcal{V} andv\neq0,then
because\mathcal{T} isinvertiblewehave\mathcal{T}v\neq0. Thisimpliesthat\langle\mathcal{T}v,v\rangle\neq0(by7.43).
Hence\langle\mathcal{T}v,v\rangle>0.
Toprovetheimplicationintheotherdirection,supposenowthat\langle\mathcal{T}v,v\rangle>0
for every nonzero v \in \mathcal{V}. Thus \mathcal{T}v \neq 0 for every nonzero v \in \mathcal{V}. Hence \mathcal{T} is
injective. Thus\mathcal{T} isinvertible,asdesired.
Thenextdefinitiontransferstheresultabovetothelanguageofmatrices. Here
weareusingtheusual Euclideaninnerproducton\mathbf{F}n andidentifyingelementsof
\mathbf{F}n withn-by-1columnvectors.
**7.62 定义：** positivedefinite
Amatrix\mathcal{B}\in\mathbf{F}n,n iscalledpositivedefiniteif\mathcal{B} ∗ =\mathcal{B}and
\langle\mathcal{B}x,x\rangle>0
foreverynonzerox \in\mathbf{F}n.

| --------- | -------------------------------------------------- | --- | --- | --- | --- |
A matrix is upper triangular if and only if its conjugate transpose is lower
triangular(meaningthatallentriesabovethediagonalare0). Thefactorization
below,whichhasimportantconsequencesincomputationallinearalgebra,writes
a positive definite matrix as the product of a lower triangular matrix and its
conjugatetranspose.
Ournextresultissolelyaboutmatrices,althoughtheproofmakesuseofthe
identificationofresultsaboutoperatorswithresultsaboutsquarematrices. Inthe
resultbelow,ifthematrix\mathcal{B}isin\mathbf{F}n,n,thenthematrix\mathcal{R}isalsoin\mathbf{F}n,n.
7.63 Choleskyfactorization
Suppose is a positive definite matrix. Then there exists a unique upper\mathcal{B}
triangularmatrix\mathcal{R}withonlypositivenumbersonitsdiagonalsuchthat
|     |     | \mathcal{B}=\mathcal{R} | ∗ \mathcal{R}. |     |     |
| --- | --- | --- | ---- | --- | --- |
Proof Because\mathcal{B}ispositivedefinite,thereexistsaninvertiblesquarematrix\mathcal{A}
∗
of the same size as \mathcal{B} such that \mathcal{B} = \mathcal{A} \mathcal{A} [by the equivalence of (a) and (f) in
7.38].
Let\mathcal{A}=\mathcal{Q}\mathcal{R}bethe QRfactorizationof\mathcal{A}(see7.58),where\mathcal{Q}isunitaryand\mathcal{R}
∗ ∗ ∗
isuppertriangularwithonlypositivenumbersonitsdiagonal. Then\mathcal{A} =\mathcal{R} \mathcal{Q} .
Thus
|           |            |      | André-Louis | Cholesky (1875–1918) |       |
| --------- | ---------- | ---- | ----------- | -------------------- | ----- |
|           |            |      | discovered  | this factorization,  | which |
| \mathcal{B}=\mathcal{A} ∗ \mathcal{A}=\mathcal{R} | ∗ \mathcal{Q} ∗ \mathcal{Q}\mathcal{R}=\mathcal{R} | ∗ \mathcal{R}, |             |                      |       |
waspublishedposthumouslyin1924.
asdesired.
Toprovetheuniquenesspartofthisresult,suppose\mathcal{S}isanupper-triangular
∗
matrixwithonlypositivenumbersonitsdiagonaland\mathcal{B}=\mathcal{S} \mathcal{S}. Thematrix\mathcal{S}is
invertiblebecause\mathcal{B}isinvertible(see Exercise11in Section3D).Multiplyingboth
|                                                  |     | ∗ \mathcal{S}by\mathcal{S}-1 ontherightgivestheequation\mathcal{B}\mathcal{S}-1 |     |      | ∗    |
| ------------------------------------------------ | --- | --------------------------------------- | --- | ---- | ---- |
| sidesoftheequation\mathcal{B}=\mathcal{S}                            |     |                                         |     |      | =\mathcal{S} . |
| Let\mathcal{A}bethematrixfromthefirstparagraphofthisproof. |     |                                         |     | Then |      |
∗
|     | (\mathcal{A}\mathcal{S}-1) | (\mathcal{A}\mathcal{S}-1)=(\mathcal{S} | ∗ )-1\mathcal{A} ∗ \mathcal{A}\mathcal{S}-1 |     |     |
| --- | ------ | --------- | ------------- | --- | --- |
|     |        |           | =(\mathcal{S} ∗ )-1\mathcal{B}\mathcal{S}-1 |     |     |
∗ )-1\mathcal{S} ∗
=(\mathcal{S}
=\mathcal{I}.
Thus\mathcal{A}\mathcal{S}-1 isunitary.
Hence\mathcal{A}=(\mathcal{A}\mathcal{S}-1)\mathcal{S}isafactorizationof\mathcal{A}astheproductofaunitarymatrix
andanupper-triangularmatrixwithonlypositivenumbersonitsdiagonal. The
uniquenessofthe QRfactorization,asstatedin7.58,nowimpliesthat\mathcal{S}=\mathcal{R}.
Inthefirstparagraphoftheproofabove,wecouldhavechosen\mathcal{A}tobethe
unique positive definite matrix that is a square root of \mathcal{B} (see 7.39). However,
theproofwaspresentedwiththemoregeneralchoiceof\mathcal{A}becauseforspecific
positivedefinitematrices\mathcal{B},itmaybeeasiertofindadifferentchoiceof\mathcal{A}.

| --- | -------- | ----------------------------- | --- | --- | --- | --- |
| Exercises     | 7D  |         |     |                                     |     |     |
| ------------- | --- | ------- | --- | ----------------------------------- | --- | --- |
| 1 Supposedim\mathcal{V} |     | \geq 2and\mathcal{S} | \in   | ℒ(\mathcal{V},\mathcal{W}). Provethat\mathcal{S}isanisometryifand |     |     |
onlyif\mathcal{S}e ,\mathcal{S}e isanorthonormallistin\mathcal{W} foreveryorthonormalliste ,e
|     | 1   | 2   |     |     |     | 1 2 |
| --- | --- | --- | --- | --- | --- | --- |
oflengthtwoin\mathcal{V}.
ℒ(\mathcal{V},\mathcal{W})and\mathcal{T}
| 2 Suppose\mathcal{T}           |     | \in   |                         | \neq 0. Provethat\mathcal{T} | isascalarmultipleofan |     |
| -------------------- | --- | --- | ----------------------- | --------------- | --------------------- | --- |
| isometryifandonlyif\mathcal{T} |     |     | preservesorthogonality. |                 |                       |     |
Thephrase“\mathcal{T} preservesorthogonality”meansthat\langle\mathcal{T}u,\mathcal{T}v\rangle = 0forall
u,v\in\mathcal{V}suchthat\langleu,v\rangle=0.
3 (a) Showthattheproductoftwounitaryoperatorson\mathcal{V}isaunitaryoperator.
$$(b) Showthattheinverseofaunitaryoperatoron\mathcal{V} isaunitaryoperator.$$
Thisexerciseshowsthatthesetofunitaryoperatorson\mathcal{V}isagroup,where
thegroupoperationistheusualproductoftwooperators.
|                                 |     | \mathcal{A},\mathcal{B}                                 |     | ℒ(\mathcal{V})              | \mathcal{A}+i\mathcal{B}      |     |
| ------------------------------- | --- | ----------------------------------- | --- | ----------------- | --------- | --- |
| 4 Suppose                       | \mathbf{F}   | = \mathbf{C} and                             | \in   | are self-adjoint. | Show that | is  |
| unitaryifandonlyif\mathcal{A}\mathcal{B}=\mathcal{B}\mathcal{A}and\mathcal{A}2+\mathcal{B}2 |     |                                     |     | =\mathcal{I}.               |           |     |
| 5 Suppose\mathcal{S}\inℒ(\mathcal{V}).                |     | Provethatthefollowingareequivalent. |     |                   |           |     |
$$(a) \mathcal{S}isaself-adjointunitaryoperator.$$
| (b) | \mathcal{S}=2\mathcal{P}-\mathcal{I}                | forsomeorthogonalprojection\mathcal{P}on\mathcal{V}. |     |                             |     |     |
| --- | --------------------- | -------------------------------- | --- | --------------------------- | --- | --- |
| (c) | Thereexistsasubspace\mathcal{U} |                                  |     | of\mathcal{V} suchthat\mathcal{S}u=uforeveryu\in\mathcal{U} |     | and |
\mathcal{S}w=-wforeveryw\in\mathcal{U}⟂.
6 Suppose\mathcal{T} ,\mathcal{T} arebothnormaloperatorson\mathbf{F}3 with2,5,7aseigenvalues.
1 2
| Provethatthereexistsaunitaryoperator\mathcal{S}\inℒ(\mathbf{F}3)suchthat\mathcal{T} |     |     |     |     |     | ∗ \mathcal{S}. |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ---- |
$$1 =\mathcal{S} \mathcal{T} 2$$
7 Giveanexampleoftwoself-adjointoperators\mathcal{T} ,\mathcal{T} \inℒ(\mathbf{F}4)suchthatthe
1 2
eigenvaluesofbothoperatorsare2,5,7 buttheredoesnotexistaunitary
| operator\mathcal{S}\inℒ(\mathbf{F}4)suchthat\mathcal{T} |     |     |     | =\mathcal{S} ∗ \mathcal{T} \mathcal{S}. Besuretoexplainwhythereis |     |     |
| ------------------------ | --- | --- | --- | ----------------------------------- | --- | --- |
|                          |     |     |     | 1 2                                 |     |     |
nounitaryoperatorwiththerequiredproperty.
If\mathcal{S}\inℒ(\mathcal{V})andthereexistsanorthonormal
8 Proveorgiveacounterexample:
basis e ,…,e of \mathcal{V} such that ‖\mathcal{S}e ‖ = 1 for each e , then \mathcal{S} is a unitary
|     | 1   | n   |     | k   | k   |     |
| --- | --- | --- | --- | --- | --- | --- |
operator.
9 Suppose\mathbf{F} =\mathbf{C}and\mathcal{T} \inℒ(\mathcal{V}). Supposeeveryeigenvalueof\mathcal{T}hasabsolute
| value1and‖\mathcal{T}v‖\leq‖v‖foreveryv\in\mathcal{V}. |     |     |     | Provethat\mathcal{T} | isaunitaryoperator. |     |
| ----------------------------- | --- | --- | --- | ---------- | ------------------- | --- |
\inℒ(\mathcal{V})isaself-adjointoperatorsuchthat‖\mathcal{T}v‖\leq‖v‖
| 10 Suppose\mathbf{F} | =\mathbf{C}and\mathcal{T} |     |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- |
forallv\in\mathcal{V}.
| (a) | Showthat\mathcal{I}-\mathcal{T}2 | isapositiveoperator. |     |     |     |     |
| --- | ------------ | -------------------- | --- | --- | --- | --- |
Showthat\mathcal{T}+i\sqrt\mathcal{I}-\mathcal{T}2
| (b) |     |     | isaunitaryoperator. |     |     |     |
| --- | --- | --- | ------------------- | --- | --- | --- |
Suppose\mathcal{S}\inℒ(\mathcal{V}).
| 11  |     | Provethat\mathcal{S}isaunitaryoperatorifandonlyif |     |     |          |     |
| --- | --- | --------------------------------------- | --- | --- | -------- | --- |
|     |     | {\mathcal{S}v∶v\in\mathcal{V}                                 |     |     | ∶‖v‖\leq1}. |     |
and‖v‖\leq1}={v\in\mathcal{V}
12 Proveorgiveacounterexample: If\mathcal{S}\inℒ(\mathcal{V})isinvertibleand∥\mathcal{S}-1v∥=‖\mathcal{S}v‖
foreveryv\in\mathcal{V},then\mathcal{S}isunitary.

| --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
13 Explain why the columns of a square matrix of complex numbers form
an orthonormal list in \mathbf{C}n if and only if the rows of the matrix form an
orthonormallistin\mathbf{C}n.
14 Supposev \in \mathcal{V} with‖v‖ = 1andb \in \mathbf{F}. Alsosupposedim\mathcal{V} \geq 2. Prove
thatthereexistsaunitaryoperator\mathcal{S} \in ℒ(\mathcal{V})suchthat\langle\mathcal{S}v,v\rangle = bifand
onlyif|b|\leq1.
| Suppose\mathcal{T} | isaunitaryoperatoron\mathcal{V} |     |     | suchthat\mathcal{T}-\mathcal{I} | isinvertible. |     |     |
| -------- | --------------------- | --- | --- | ----------- | ------------- | --- | --- |
Provethat(\mathcal{T}+\mathcal{I})(\mathcal{T}-\mathcal{I})-1
| (a) |     |     | isaskewoperator(meaningthatitequals |     |     |     |     |
| --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
thenegativeofitsadjoint).
$$(b) Provethatif\mathbf{F} =\mathbf{C},theni(\mathcal{T}+\mathcal{I})(\mathcal{T}-\mathcal{I})-1 isaself-adjointoperator.$$
Thefunctionz↦i(z+1)(z-1)-1mapstheunitcirclein\mathbf{C}(exceptforthe
point1)to\mathbf{R}. Thus(b)illustratestheanalogybetweentheunitaryoperators
andtheunitcirclein\mathbf{C},alongwiththeanalogybetweentheself-adjoint
operatorsand\mathbf{R}.
16 Suppose\mathbf{F} =\mathbf{C}and\mathcal{T} \inℒ(\mathcal{V})isself-adjoint. Provethat(\mathcal{T}+i\mathcal{I})(\mathcal{T}-i\mathcal{I})-1
isaunitaryoperatorand1isnotaneigenvalueofthisoperator.
Explainwhythecharacterizationsofunitarymatricesgivenby7.57hold.
18 Asquarematrix\mathcal{A}iscalledsymmetricifitequalsitstranspose. Provethatif
\mathcal{A}isasymmetricmatrixwithrealentries,thenthereexistsaunitarymatrix
| \mathcal{Q}withrealentriessuchthat\mathcal{Q} |     |     | ∗ \mathcal{A}\mathcal{Q}isadiagonalmatrix. |     |     |     |     |
| ------------------------- | --- | --- | ---------------------- | --- | --- | --- | --- |
19 Supposenisapositiveinteger. Forthisexercise,weadoptthenotationthat
| atypicalelementzof\mathbf{C}n |         |                 |         |     | ,z ,…,z |     |              |
| -------------------- | ------- | --------------- | ------- | --- | ------- | --- | ------------ |
|                      |         | isdenotedbyz=(z |         |     |         | ).  | Definelinear |
|                      |         |                 |         |     | 0 1     | n-1 |              |
| functionals\omega         | ,\omega ,…,\omega |                 | on\mathbf{C}n by |     |         |     |              |
|                      | 0 1     | n-1             |         |     |         |     |              |
n-1
|     | \omega(z | ,z ,…,z | )=  | \sqrt \sum | z e-2\piijm/n. |     |     |
| --- | --- | ------- | --- | --- | ------------ | --- | --- |
|     | j   | 0 1     | n-1 |     | m            |     |     |
n m=0
| Thediscrete Fouriertransformistheoperatorℱ∶ |     |     |     |     | \mathbf{C}n  | \rightarrow\mathbf{C}n |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
definedby
|     |     | ℱz=(\omega | (z),\omega (z),…,\omega |     | (z)). |     |     |
| --- | --- | ----- | ------------- | --- | ----- | --- | --- |
|     |     |       | 0 1           |     | n-1   |     |     |
Showthatℱisaunitaryoperatoron\mathbf{C}n.
$$(a)$$
| (b) Showthatif(z |       | ,…,z    | )\in\mathbf{C}n andz | isdefinedtoequalz |         |     | ,then |
| ---------------- | ----- | ------- | --------- | ----------------- | ------- | --- | ----- |
|                  | 0     | n-1     |           | n                 |         |     | 0     |
|                  | ℱ-1(z | ,z ,…,z |           | )=ℱ(z             | ,z ,…,z |     |       |
$$).$$
|                |     | 0 1 | n-1 |     | n n-1 | 1   |     |
| -------------- | --- | --- | --- | --- | ----- | --- | --- |
| (c) Showthatℱ4 | =\mathcal{I}. |     |     |     |       |     |     |
analysis. The usual Fourier transform involves expressions of the form
\int\infty f(x)e-2\piitxdxforcomplex-valuedintegrablefunctions
f definedon\mathbf{R}.
-\infty
20 Suppose\mathcal{A}isasquarematrixwithlinearlyindependentcolumns. Provethat
thereexistuniquematrices\mathcal{R}and\mathcal{Q}suchthat\mathcal{R}islowertriangularwithonly
positivenumbersonitsdiagonal,\mathcal{Q}isunitary,and\mathcal{A}=\mathcal{R}\mathcal{Q}.

| --- | -------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
| 7E       | Singular | Value  | Decomposition |     |     |     |     |     |
| -------- | -------- | ------ | ------------- | --- | --- | --- | --- | --- |
| Singular |          | Values |               |     |     |     |     |     |
Wewillneedthefollowingresultinthissection.
∗
| 7.64     | propertiesof | \mathcal{T}                       | \mathcal{T}    |     |     |     |     |     |
| -------- | ------------ | ----------------------- | ---- | --- | --- | --- | --- | --- |
| Suppose\mathcal{T} |              | \inℒ(\mathcal{V},\mathcal{W}).                | Then |     |     |     |     |     |
| (a)      | \mathcal{T} ∗ \mathcal{T}        | isapositiveoperatoron\mathcal{V}; |      |     |     |     |     |     |
∗
| (b) | null\mathcal{T}     | \mathcal{T} =null\mathcal{T};   |     |            |     |     |     |     |
| --- | --------- | ----------- | --- | ---------- | --- | --- | --- | --- |
| (c) | range\mathcal{T}    | ∗ \mathcal{T} =range\mathcal{T} | ∗ ; |            |     |     |     |     |
|     |           |             |     | ∗          |     | ∗   |     |     |
| (d) | dimrange\mathcal{T} | =dimrange\mathcal{T}  |     | =dimrange\mathcal{T} |     | \mathcal{T}.  |     |     |
Proof
$$(a) Wehave$$
|     |     |     |     | ∗ ∗   | ∗ ∗ | ∗ ∗     |     |     |
| --- | --- | --- | --- | ----- | --- | ------- | --- | --- |
|     |     |     | (\mathcal{T}  | \mathcal{T}) =\mathcal{T} | (\mathcal{T}  | ) =\mathcal{T} \mathcal{T}. |     |     |
∗
|     | Thus\mathcal{T} | \mathcal{T} isself-adjoint. |     |     |     |     |     |     |
| --- | ----- | ----------------- | --- | --- | --- | --- | --- | --- |
Ifv\in\mathcal{V},then
|     |     | ∗             |     | ∗                     |     |     |     |     |
| --- | --- | ------------- | --- | --------------------- | --- | --- | --- | --- |
|     |     | \langle(\mathcal{T} \mathcal{T})v,v\rangle=\langle\mathcal{T} |     | (\mathcal{T}v),v\rangle=\langle\mathcal{T}v,\mathcal{T}v\rangle=‖\mathcal{T}v‖2 |     |     | \geq0. |     |
∗
|     | Thus\mathcal{T}               | \mathcal{T} isapositiveoperator. |             |      |                  |     |     |     |
| --- | ------------------- | ---------------------- | ----------- | ---- | ---------------- | --- | --- | --- |
| (b) | Firstsupposev\innull\mathcal{T} |                        | ∗ \mathcal{T}.        | Then |                  |     |     |     |
|     |                     | ‖\mathcal{T}v‖2                  | =\langle\mathcal{T}v,\mathcal{T}v\rangle=\langle\mathcal{T} |      | ∗ \mathcal{T}v,v\rangle=\langle0,v\rangle=0. |     |     |     |
∗
|     | Thus\mathcal{T}v=0,provingthatnull\mathcal{T} |     |     |     | \mathcal{T} \subseteqnull\mathcal{T}. |     |     |     |
| --- | ------------------------- | --- | --- | --- | --------- | --- | --- | --- |
Theinclusionintheotherdirectionisclear,becauseifv \in \mathcal{V} and\mathcal{T}v = 0,
∗
|     | then\mathcal{T} | \mathcal{T}v=0. |     |     |     |     |     |     |
| --- | ----- | ----- | --- | --- | --- | --- | --- | --- |
∗
|     | Thusnull\mathcal{T}                 | \mathcal{T} =null\mathcal{T},completingtheproofof(b). |             |     |                     |     |            |     |
| --- | ------------------------- | --------------------------------- | ----------- | --- | ------------------- | --- | ---------- | --- |
| (c) | Wealreadyknowfrom(a)that\mathcal{T} |                                   |             |     | ∗ \mathcal{T} isself-adjoint. |     | Thus       |     |
|     |                           | range\mathcal{T}                            | ∗ \mathcal{T} =(null\mathcal{T} |     | ∗ \mathcal{T})⟂ =(null\mathcal{T})⟂     |     | =range\mathcal{T} ∗, |     |
where the first and last equalities come from 7.6 and the second equality
comesfrom(b).
$$(d) Toverifythefirstequationin(d),notethat$$
|     |           |            |     | ∗ )⟂ |                |     | ∗          | ∗,  |
| --- | --------- | ---------- | --- | ---- | -------------- | --- | ---------- | --- |
|     | dimrange\mathcal{T} | =dim(null\mathcal{T} |     |      | =dim\mathcal{W}-dimnull\mathcal{T} |     | =dimrange\mathcal{T} |     |
wherethefirstequalitycomesfrom7.6(d),thesecondequalitycomesfrom
6.51, and the last equality comes from the fundamental theorem of linear
maps(3.21).
|     |                      |     | ∗   |            |     | ∗                 |     |     |
| --- | -------------------- | --- | --- | ---------- | --- | ----------------- | --- | --- |
|     | Theequalitydimrange\mathcal{T} |     |     | =dimrange\mathcal{T} |     | \mathcal{T} followsfrom(c). |     |     |

| --- | --- | --------- | -------------------------- | --- | --- |
Theeigenvaluesofanoperatortellussomethingaboutthebehaviorofthe
operator. Anothercollectionofnumbers,calledthesingularvalues,isalsouseful.
Eigenspacesandthenotation\mathcal{E}(usedintheexamples)weredefinedin5.52.
singularvalues
**7.65 定义：** Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Thesingularvaluesof\mathcal{T} arethenonnegativesquare
rootsoftheeigenvaluesof\mathcal{T} ∗ \mathcal{T},listedindecreasingorder,eachincludedas
∗
| manytimesasthedimensionofthecorrespondingeigenspaceof\mathcal{T} |     |     |     |     | \mathcal{T}.  |
| ------------------------------------------------------ | --- | --- | --- | --- | --- |
singularvaluesofanoperatoron\mathbf{F}4
**7.66 例：** Define \mathcal{T} \in ℒ(\mathbf{F}4) by \mathcal{T}(z ,z ,z ,z ) = (0,3z ,2z ,-3z ). A calculation
|     |     |     | 1 2 3 4 | 1 2 4 |     |
| --- | --- | --- | ------- | ----- | --- |
showsthat
|     |     | \mathcal{T} ∗ \mathcal{T}(z ,z | ,z ,z )=(9z | ,4z ,0,9z ), |     |
| --- | --- | ---------- | ----------- | ------------ | --- |
|     |     | 1          | 2 3 4 1     | 2 4          |     |
∗
asyoushouldverify. Thusthestandardbasisof \mathbf{F}4 diagonalizes \mathcal{T} \mathcal{T}, and we
see that the eigenvalues of \mathcal{T} ∗ \mathcal{T} are 9, 4, and 0. Also, the dimensions of the
eigenspacescorrespondingtotheeigenvaluesare
|          | ∗    |     | ∗             |              | ∗     |
| -------- | ---- | --- | ------------- | ------------ | ----- |
| dim\mathcal{E}(9,\mathcal{T} | \mathcal{T})=2 | and | dim\mathcal{E}(4,\mathcal{T} \mathcal{T})=1 | and dim\mathcal{E}(0,\mathcal{T} | \mathcal{T})=1. |
Takingnonnegativesquarerootsoftheseeigenvaluesof\mathcal{T} ∗ \mathcal{T}andusingdimension
informationfromabove,weconcludethatthesingularvaluesof\mathcal{T} are3,3,2,0.
Theonlyeigenvaluesof\mathcal{T} are-3and0. Thusinthiscase,thecollectionof
eigenvaluesdidnotpickupthenumber2thatappearsinthedefinition(andhence
thebehavior)of\mathcal{T},butthelistofsingularvaluesdoesinclude2.
| 7.67 example: | singularvaluesofalinearmapfrom\mathbf{F}4 |     |     | to\mathbf{F}3 |     |
| ------------- | -------------------------------- | --- | --- | ---- | --- |
\inℒ(\mathbf{F}4,\mathbf{F}3)hasmatrix(withrespecttothestandardbases)
Suppose\mathcal{T}
|     |     |     | 0 0 0 -5 |      |     |
| --- | --- | --- | -------- | ---- | --- |
|     |     | ⎛   |          | ⎞    |     |
|     |     | ⎜   |          | ⎟    |     |
|     |     | ⎜ ⎜ | 0 0 0 0  | ⎟ ⎟. |     |
|     |     |     | 1 1 0 0  |      |     |
|     |     | ⎝   |          | ⎠    |     |
∗
| Youcanverifythatthematrixof\mathcal{T} |     |     | \mathcal{T} is        |     |     |
| ---------------------------- | --- | --- | ----------- | --- | --- |
|                              |     |     | 1 1 0 0     |     |     |
|                              |     |     | ⎛           | ⎞   |     |
|                              |     |     | ⎜ ⎜ 1 1 0 0 | ⎟ ⎟ |     |
|                              |     |     | ⎜           | ⎟   |     |
|                              |     |     | ⎜ ⎜         | ⎟ ⎟ |     |
|                              |     |     | ⎜ 0 0 0 0   | ⎟   |     |
0 0 0 25
|     |     |     | ⎝   | ⎠   |     |
| --- | --- | --- | --- | --- | --- |
|     |     |     | ∗   |     | ∗   |
andthattheeigenvaluesoftheoperator\mathcal{T} \mathcal{T}are25,2,0,withdim\mathcal{E}(25,\mathcal{T} \mathcal{T})=1,
| dim\mathcal{E}(2,\mathcal{T} | ∗ 1,anddim\mathcal{E}(0,\mathcal{T} |     | ∗ 2. Thusthesingularvaluesof\mathcal{T} |     | are |
| -------- | --------------- | --- | ----------------------------- | --- | --- |
|          | \mathcal{T}) =            |     | \mathcal{T}) =                          |     |     |
5,\sqrt2,0,0.
See Exercise2foracharacterizationofthepositivesingularvalues.

\approx100e Chapter 7 Operatorson Inner Product Spaces
7.68 roleofpositivesingularvalues
Supposethat\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Then
$$(a) \mathcal{T} isinjective ⟺ 0isnotasingularvalueof\mathcal{T};$$
$$(b) thenumberofpositivesingularvaluesof\mathcal{T} equalsdimrange\mathcal{T};$$
$$(c) \mathcal{T}issurjective ⟺ numberofpositivesingularvaluesof\mathcal{T}equalsdim\mathcal{W}.$$
Proof Thelinearmap\mathcal{T} isinjectiveifandonlyifnull\mathcal{T} ={0},whichhappens
∗
ifandonlyifnull\mathcal{T} \mathcal{T} ={0}[by7.64(b)],whichhappensifandonlyif0isnot
∗
aneigenvalueof\mathcal{T} \mathcal{T},whichhappensifandonlyif0isnotasingularvalueof\mathcal{T},
completingtheproofof(a).
∗ ∗
Thespectraltheoremappliedto\mathcal{T} \mathcal{T}showsthatdimrange\mathcal{T} \mathcal{T}equalsthenum-
∗
berofpositiveeigenvaluesof\mathcal{T} \mathcal{T} (countingrepetitions). Thus7.64(d)implies
thatdimrange\mathcal{T} equalsthenumberofpositivesingularvaluesof\mathcal{T},proving(b).
Use(b)and2.39toshowthat(c)holds.
Thetablebelowcompareseigenvalueswithsingularvalues.
listofeigenvalues listofsingularvalues
context: vectorspaces context: innerproductspaces
definedonlyforlinearmapsfromavector defined for linear maps from an inner
spacetoitself productspacetoapossiblydifferentinner
productspace
canbearbitraryrealnumbers(if\mathbf{F} =\mathbf{R}) arenonnegativenumbers
orcomplexnumbers(if\mathbf{F} =\mathbf{C})
canbetheemptylistif\mathbf{F} =\mathbf{R} lengthoflistequalsdimensionofdomain
includes0 ⟺ operatorisnotinvertible includes0 ⟺ linearmapisnotinjective
nostandardorder,especiallyif\mathbf{F} =\mathbf{C} alwayslistedindecreasingorder
Thenextresultnicelycharacterizesisometriesintermsofsingularvalues.
7.69 isometriescharacterizedbyhavingallsingularvaluesequal1
Supposethat\mathcal{S}\inℒ(\mathcal{V},\mathcal{W}). Then
\mathcal{S}isanisometry ⟺ allsingularvaluesof\mathcal{S}equal1.
∗
\mathcal{S}isanisometry ⟺ \mathcal{S} \mathcal{S}=\mathcal{I}
∗
⟺ alleigenvaluesof\mathcal{S} \mathcal{S}equal1
⟺ allsingularvaluesof\mathcal{S}equal1,
wherethefirstequivalencecomesfrom7.49andthesecondequivalencecomes
∗
fromthespectraltheorem(7.29or7.31)appliedtotheself-adjointoperator\mathcal{S} \mathcal{S}.

Section7E Singular Value Decomposition 273
SVD for Linear Maps and for Matrices
The next result shows that every linear
The singular value decomposition is
mapfrom\mathcal{V}to\mathcal{W}hasaremarkablyclean
useful in computational linear algedescription in terms of its singular valbrabecausegoodtechniquesexistfor
ues and orthonormal lists in \mathcal{V} and \mathcal{W}. approximatingeigenvaluesandeigenIn the next section we will see several vectors of positive operators such as
important applications of the singular \mathcal{T} ∗ \mathcal{T},whoseeigenvaluesandeigenvecvalue decomposition (often called the torsleadtothesingularvaluedecomSVD). position.
7.70 singularvaluedecomposition
Suppose \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}) and the positive singular values of \mathcal{T} are s ,…,s .
1 m
Thenthereexistorthonormallistse ,…,e in\mathcal{V} and f ,…, f in\mathcal{W} suchthat
1 m 1 m
7.71 \mathcal{T}v=s \langlev,e \ranglef +⋯+s \langlev,e \ranglef
1 1 1 m m m
foreveryv\in\mathcal{V}.
Proof Lets ,…,s denotethesingularvaluesof\mathcal{T} (thusn=dim\mathcal{V}). Because
1 n
∗
\mathcal{T} \mathcal{T} isapositiveoperator[see7.64(a)],thespectraltheoremimpliesthatthere
existsanorthonormalbasise ,…,e of\mathcal{V} with
1 n
7.72 \mathcal{T} ∗ \mathcal{T}e =s2e
k k k
foreachk =1,…,n.
Foreachk =1,…,m,let
\mathcal{T}e
7.73 f = k.
k s
k
Ifj,k \in{1,…,m},then
\langlef, f \rangle=
\langle\mathcal{T}e,\mathcal{T}e \rangle=
\langlee,\mathcal{T} ∗ \mathcal{T}e \rangle=
s
k\langlee,e \rangle=
⎧ {0 ifj \neqk,
j k ss j k ss j k s j k ⎨ {1 ifj =k.
j k j k j ⎩
Thus f ,…, f isanorthonormallistin\mathcal{W}.
1 m
If k \in {1,…,n} and k > m, then s = 0 and hence \mathcal{T} ∗ \mathcal{T}e = 0 (by 7.72),
k k
whichimpliesthat\mathcal{T}e =0[by7.64(b)].
k
Supposev\in\mathcal{V}. Then
\mathcal{T}v=\mathcal{T}(\langlev,e \ranglee +⋯+\langlev,e \ranglee )
1 1 n n
=\langlev,e \rangle\mathcal{T}e +⋯+\langlev,e \rangle\mathcal{T}e
1 1 m m
=s \langlev,e \ranglef +⋯+s \langlev,e \ranglef ,
1 1 1 m m m
where the last index in the first line switched from n to m in the second line
because\mathcal{T}e = 0ifk > m(asnotedintheparagraphabove)andthethirdline
k
followsfrom7.73. Theequationaboveisourdesiredresult.

| -------- | ----------------------------- | --- | --- | --- | --- |
Suppose\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}),thepositivesingularvaluesof\mathcal{T} ares ,…,s ,and
1 m
e ,…,e and f ,…, f are as in the singular value decomposition 7.70. The
| 1 m | 1   | m   |     |     |     |
| --- | --- | --- | --- | --- | --- |
orthonormalliste ,…,e canbeextendedtoanorthonormalbasise ,…,e
|     | 1   | m   |     |     | 1 dim\mathcal{V} |
| --- | --- | --- | --- | --- | ------ |
of\mathcal{V} andtheorthonormallist f ,…, f canbeextendedtoanorthonormalbasis
|         |                              | 1   | m   |     |     |
| ------- | ---------------------------- | --- | --- | --- | --- |
| f ,…, f | of\mathcal{W}. Theformula7.71showsthat |     |     |     |     |
1 dim\mathcal{W}
⎧
|     |     | {s f     | if1\leqk \leqm, |     |     |
| --- | --- | -------- | --------- | --- | --- |
|     |     | \mathcal{T}e = k k |           |     |     |
k ⎨
|     |     | {0  | ifm<k \leqdim\mathcal{V}. |     |     |
| --- | --- | --- | ------------ | --- | --- |
⎩
,…,e
| Thusthematrixof\mathcal{T} |                   | withrespecttotheorthonormalbases(e |     |     | )and |
| ---------------- | ----------------- | ---------------------------------- | --- | --- | ---- |
|                  |                   |                                    |     | 1   | dim\mathcal{V} |
| (f ,…, f         | )hasthesimpleform |                                    |     |     |      |
1 dim\mathcal{W}
|     |     |     | ⎧ {s | if1\leqj =k \leqm, |     |
| --- | --- | --- | ---- | ------------ | --- |
k
| ℳ(\mathcal{T},(e | ,…,e | ),(f ,…, f | )) = ⎨      |            |     |
| ------ | ---- | ---------- | ----------- | ---------- | --- |
|        | 1    | dim\mathcal{V} 1     | dim\mathcal{W} j,k {0 | otherwise. |     |
⎩
If dim\mathcal{V} = dim\mathcal{W} (as happens, for example, if \mathcal{W} = \mathcal{V}), then the matrix
describedintheparagraphaboveisadiagonalmatrix. Ifweextendthedefinition
ofdiagonalmatrixasfollowstoapplytomatricesthatarenotnecessarilysquare,
thenwehaveprovedthewonderfulresultthateverylinearmapfrom\mathcal{V} to\mathcal{W} has
adiagonalmatrixwithrespecttoappropriateorthonormalbases.
| 7.74 definition: | diagonalmatrix |     |     |     |     |
| ---------------- | -------------- | --- | --- | --- | --- |
An\mathcal{M}-by-\mathcal{N} matrix\mathcal{A}iscalledadiagonalmatrixifallentriesofthematrix
| are0exceptpossibly\mathcal{A} |     | fork =1,…,min{\mathcal{M},\mathcal{N}}. |     |     |     |
| ------------------- | --- | ------------------- | --- | --- | --- |
k,k
The table below compares the spectral theorem (7.29 and 7.31) with the
singularvaluedecomposition(7.70).
|     | spectraltheorem |     | singularvaluedecomposition |     |     |
| --- | --------------- | --- | -------------------------- | --- | --- |
describes only self-adjoint operators describesarbitrarylinearmapsfroman
$$(when\mathbf{F} =\mathbf{R})ornormaloperators(when innerproductspacetoapossiblydifferent$$
| \mathbf{F} =\mathbf{C}) |     |     | innerproductspace |     |     |
| ----- | --- | --- | ----------------- | --- | --- |
producesasingleorthonormalbasis producestwoorthonormallists,onefor
|     |     |     | domain space | and one for range | space,    |
| --- | --- | --- | ------------ | ----------------- | --------- |
|     |     |     | that are not | necessarily the   | same even |
whenrangespaceequalsdomainspace
different proofs depending on whether sameproofworksregardlessofwhether
| \mathbf{F} =\mathbf{R}or\mathbf{F} | =\mathbf{C}  |     | \mathbf{F} =\mathbf{R}or\mathbf{F} | =\mathbf{C}  |     |
| ------- | --- | --- | ------- | --- | --- |
Thesingularvaluedecompositiongivesusanewwaytounderstandtheadjoint
andtheinverseofalinearmap. Specifically,thenextresultshowsthatgivena
singularvaluedecompositionofalinearmap\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}),wecanobtainthe
adjointof\mathcal{T} simplybyinterchangingtherolesofthee’sandthe f ’s(see7.77).
Similarly,wecanobtainthepseudoinverse\mathcal{T}†
|     |     |     | (see6.68)of\mathcal{T} | byinterchanging |     |
| --- | --- | --- | ------------ | --------------- | --- |
therolesofthee’sandthe f ’sandreplacingeachpositivesingularvalues of\mathcal{T}
k
| with1/s (see7.78). |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
k

| --- | --- | --- | --------- | -------------------------- | --- | --- |
| Recallthatthepseudoinverse\mathcal{T}† |     |     |     | in7.78belowequalstheinverse\mathcal{T}-1 |     |     |
| ---------------------------- | --- | --- | --- | ------------------------------ | --- | --- |
if\mathcal{T} is
invertible[see6.69(a)].
7.75 singularvaluedecompositionofadjointandpseudoinverse
Suppose \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}) and the positive singular values of \mathcal{T} are s ,…,s .
1 m
Supposee ,…,e and f ,…, f areorthonormallistsin\mathcal{V} and\mathcal{W} suchthat
|              | 1   | m     | 1    | m        |      |      |
| ------------ | --- | ----- | ---- | -------- | ---- | ---- |
| 7.76         |     | \mathcal{T}v=s  | \langlev,e | \ranglef +⋯+s  | \langlev,e | \ranglef   |
|              |     |       | 1    | 1 1      | m    | m m  |
| foreveryv\in\mathcal{V}. |     | Then  |      |          |      |      |
|              |     | ∗     |      | \langlew, +⋯+s |      | \langlew,  |
| 7.77         |     | \mathcal{T} w=s |      | f \ranglee     |      | f \ranglee |
|              |     |       | 1    | 1 1      | m    | m m  |
and
|      |     |      |     | \langlew, f \rangle | \langlew, | f \rangle |
| ---- | --- | ---- | --- | ------- | --- | --- |
|      |     | \mathcal{T}†w= |     | 1       |     | m   |
| 7.78 |     |      |     | e +⋯+   |     | e   |
|      |     |      |     | s 1     |     | s m |
|      |     |      |     | 1       |     | m   |
foreveryw\in\mathcal{W}.
| Proof Ifv\in\mathcal{V} |           | andw\in\mathcal{W} | then |               |      |             |
| ----------- | --------- | ------ | ---- | ------------- | ---- | ----------- |
|             | \langle\mathcal{T}v,w\rangle=\langles |        | \langlev,e | +⋯+s          | \langlev,e | ,w\rangle         |
|             |           |        | 1    | 1 \ranglef 1        | m    | m \ranglef m      |
|             |           |        | \langlev,e | ,w\rangle+⋯+s       |      | \langlev,e ,w\rangle    |
|             |           | =s     |      | \rangle\langlef           |      | \rangle\langlef         |
|             |           |        | 1    | 1 1           |      | m m m       |
|             |           | =\langlev,s  |      | \langlew, f \ranglee +⋯+s |      | \langlew, f \ranglee \rangle. |
|             |           |        | 1    | 1 1           | m    | m m         |
Thisimpliesthat
|     |     | \mathcal{T} ∗ w=s | \langlew, | f \ranglee +⋯+s |     | \langlew, f \ranglee , |
| --- | --- | ------- | --- | --------- | --- | ---------- |
|     |     |         | 1   | 1 1       | m   | m m        |
proving7.77.
| Toprove7.78,supposew\in\mathcal{W}. |     |     |     | Let   |     |     |
| ----------------------- | --- | --- | --- | ----- | --- | --- |
|                         |     |     | \langlew, | f \rangle   | \langlew, | f \rangle |
|                         |     |     |     | 1 +⋯+ |     | m   |
|                         |     | v=  |     | e     |     | e . |
|                         |     |     |     | s 1   | s   | m   |
|                         |     |     |     | 1     |     | m   |
Apply\mathcal{T} tobothsidesoftheequationabove,getting
|     |     |     | \langlew,  | f \rangle         | \langlew, | f \rangle  |
| --- | --- | --- | ---- | ----------- | --- | ---- |
|     |     | \mathcal{T}v= |      | 1 \mathcal{T}e +⋯+    |     | m \mathcal{T}e |
|     |     |     |      | 1           |     | m    |
|     |     |     |      | s           |     | s    |
|     |     |     |      | 1           |     | m    |
|     |     |     | =\langlew, | f \ranglef +⋯+\langlew, | f   | \ranglef   |
|     |     |     |      | 1 1         |     | m m  |
|     |     |     | =\mathcal{P}   | w,          |     |      |
range\mathcal{T}
wherethesecondlineholdsbecause7.76impliesthat\mathcal{T}e =s f ifk =1,…,m,
|     |     |     |     |     |     | k k k |
| --- | --- | --- | --- | --- | --- | ----- |
andthelastlineaboveholdsbecause7.76impliesthat f ,…, f spansrange\mathcal{T}
1 m
and thus is an orthonormal basis of range\mathcal{T} [and hence 6.57(i) applies]. The
equationabove,theobservationthatv\in(null\mathcal{T})⟂ [see Exercise8(b)],andthe
definitionof\mathcal{T}†w(see6.68)showthatv=\mathcal{T}†w,proving7.78.

| -------- | --- | ----------------------------- | --- | --- |
findingasingularvaluedecomposition
**7.79 例：** Define\mathcal{T} \in ℒ(\mathbf{F}4,\mathbf{F}3)by\mathcal{T}(x ,x ,x ,x ) = (-5x ,0,x +x ). Wewantto
|     |     |     | 1 2 3 4 | 4 1 2 |
| --- | --- | --- | ------- | ----- |
findasingularvaluedecompositionof\mathcal{T}. Thematrixof\mathcal{T} (withrespecttothe
standardbases)is
|     |     |     | 0 0 0 -5 |      |
| --- | --- | --- | -------- | ---- |
|     |     | ⎛ ⎜ |          | ⎞ ⎟  |
|     |     | ⎜   | 0 0 0 0  | ⎟ ⎟. |
⎜
|     |     | ⎝   | 1 1 0 0 | ⎠   |
| --- | --- | --- | ------- | --- |
∗
| Thus,asdiscussedin Example7.67,thematrixof\mathcal{T} |     |     |         | \mathcal{T} is |
| ------------------------------------------ | --- | --- | ------- | ---- |
|                                            |     |     | 1 1 0 0 |      |
|                                            |     | ⎛   |         | ⎞    |
|                                            |     | ⎜ ⎜ | 1 1 0 0 | ⎟ ⎟  |
|                                            |     | ⎜   |         | ⎟ ⎟, |
⎜
|     |     | ⎜ ⎜ | 0 0 0 0  | ⎟ ⎟ |
| --- | --- | --- | -------- | --- |
|     |     |     | 0 0 0 25 |     |
|     |     | ⎝   |          | ⎠   |
and the positive eigenvalues of \mathcal{T} ∗ \mathcal{T} are 25, 2, with dim\mathcal{E}(25,\mathcal{T} ∗ \mathcal{T}) = 1 and
∗
| dim\mathcal{E}(2,\mathcal{T} | \mathcal{T})=1. Hencethepositivesingularvaluesof\mathcal{T} |     |     | are5,\sqrt2. |
| -------- | --------------------------------------- | --- | --- | -------- |
Thustofindasingularvaluedecompositionof\mathcal{T},wemustfindanorthonormal
| liste ,e in\mathbf{F}4 | andanorthonormallist |          | f , f in\mathbf{F}3 | suchthat |
| ------------- | -------------------- | -------- | ---------- | -------- |
| 1 2           |                      |          | 1 2        |          |
|               |                      | \mathcal{T}v=5\langlev,e | \ranglef +\sqrt2\langlev,e | \ranglef       |
|               |                      |          | 1 1        | 2 2      |
forallv\in\mathbf{F}4.
∗
Anorthonormalbasisof\mathcal{E}(25,\mathcal{T} \mathcal{T})isthevector(0,0,0,1);anorthonormal
basisof\mathcal{E}(2,\mathcal{T} ∗ \mathcal{T})isthevector( 1 , 1 ,0,0). Thus,followingtheproofof7.70,
|     |     |     | \sqrt2 \sqrt2 |     |
| --- | --- | --- | ----- | --- |
wetake
1 1
|     | e =(0,0,0,1) |     | and e =( | , ,0,0) |
| --- | ------------ | --- | -------- | ------- |
\sqrt2 \sqrt2
and
|     | \mathcal{T}e  |             |       | \mathcal{T}e            |
| --- | --- | ----------- | ----- | ------------- |
|     | f = | 1 =(-1,0,0) | and f | = 2 =(0,0,1). |
|     |     | 5           |       | \sqrt2            |
Then,asexpected,weseethate ,e isanorthonormallistin\mathbf{F}4 and f , f isan
|                     |     |     | 1 2 | 1 2 |
| ------------------- | --- | --- | --- | --- |
| orthonormallistin\mathbf{F}3 |     | and |     |     |
+\sqrt2\langlev,e
|     |     | \mathcal{T}v=5\langlev,e | \ranglef  | \ranglef  |
| --- | --- | -------- | --- | --- |
|     |     |          | 1 1 | 2 2 |
forallv\in\mathbf{F}4.
Thuswehavefoundasingularvaluedecompositionof\mathcal{T}.
Thenextresulttranslatesthesingularvaluedecompositionfromthecontext
oflinearmapstothecontextofmatrices. Specifically,thefollowingresultgives
afactorizationofanarbitrarymatrixastheproductofthreenicematrices. The
proofgivesanexplicitconstructionofthesethreematricesintermsofthesingular
valuedecomposition.
Inthenextresult,thephrase“orthonormalcolumns”shouldbeinterpretedto
meanthatthecolumnsareorthonormalwithrespecttothestandard Euclidean
innerproduct.

| --- | --- | --- | --------- | --- | -------------------------- | --- | --- | --- | --- |
matrixversionof SVD
7.80
Suppose\mathcal{A}isap-by-nmatrixofrankm\geq1. Thenthereexistap-by-mmatrix
\mathcal{B} with orthonormal columns, an m-by-m diagonal matrix \mathcal{D} with positive
numbersonthediagonal,andann-by-mmatrix\mathcal{C}withorthonormalcolumns
suchthat
∗
|     |     |     |     | \mathcal{A}=\mathcal{B}\mathcal{D}\mathcal{C} |     | .   |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Proof Let \mathcal{T}∶ \mathbf{F}n \rightarrow \mathbf{F}p be the linear map whose matrix with respect to the
| standardbasesequals\mathcal{A}.                             |                                  |     | Thendimrange\mathcal{T} |         |      | =m(by3.78). | Let |      |     |
| ------------------------------------------------- | -------------------------------- | --- | ------------- | ------- | ---- | ----------- | --- | ---- | --- |
| 7.81                                              |                                  |     | \mathcal{T}v=s          | \langlev,e \ranglef | +⋯+s | \langlev,e        | \ranglef  |      |     |
|                                                   |                                  |     |               | 1 1     | 1    | m           | m m |      |     |
| beasingularvaluedecompositionof\mathcal{T}.                 |                                  |     |               |         | Let  |             |     |      |     |
|                                                   | \mathcal{B}=thep-by-mmatrixwhosecolumnsare |     |               |         |      | f ,…,       | f , |      |     |
|                                                   |                                  |     |               |         |      | 1           | m   |      |     |
| \mathcal{D}=them-by-mdiagonalmatrixwhosediagonalentriesares |                                  |     |               |         |      |             |     | ,…,s | ,   |
1 m
| \mathcal{C}      | =then-by-mmatrixwhosecolumnsaree |                             |     |          |     | ,…,e  | .            |     |     |
| ------ | -------------------------------- | --------------------------- | --- | -------- | --- | ----- | ------------ | --- | --- |
|        |                                  |                             |     |          |     | 1     | m            |     |     |
| Letu   | ,…,u                             | denotethestandardbasisof\mathbf{F}m. |     |          |     | Ifk   | \in{1,…,m}then |     |     |
|        | 1                                | m                           |     |          |     |       |              |     |     |
|        |                                  | (\mathcal{A}\mathcal{C}-\mathcal{B}\mathcal{D})u                    |     | =\mathcal{A}e -\mathcal{B}(s | u   | )=s f | -s f         | =0. |     |
|        |                                  |                             | k   | k        | k   | k k   | k k k        |     |     |
| Thus\mathcal{A}\mathcal{C} | =\mathcal{B}\mathcal{D}.                             |                             |     |          |     |       |              |     |     |
∗
Multiplybothsidesofthislastequationby\mathcal{C} (theconjugatetransposeof\mathcal{C})
ontherighttoget
|     |     |     |     |     | ∗    | ∗   |     |      |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- |
|     |     |     |     | \mathcal{A}\mathcal{C}\mathcal{C} | =\mathcal{B}\mathcal{D}\mathcal{C} | .   |     |      |     |
|     |     |     | ∗   |     |      |     |     | ,…,e |     |
Note that the rows of \mathcal{C} are the complex conjugates of e . Thus if
|     |     |     |     |     |     |     |     | 1   | m ∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k \in{1,…,m},thenthedefinitionofmatrixmultiplicationshowsthat\mathcal{C} e =u ;
|         |     |              |     |                    |     |     |      |     | k k |
| ------- | --- | ------------ | --- | ------------------ | --- | --- | ---- | --- | --- |
|         | ∗   |              |     | ∗                  |     |     | ,…,e |     |     |
| hence\mathcal{C}\mathcal{C} | e   | =e . Thus\mathcal{A}\mathcal{C}\mathcal{C} |     | v=\mathcal{A}vforallv\inspan(e |     |     |      | ).  |     |
|         | k   | k            |     |                    |     |     | 1    | m   | ∗   |
Ifv \in (span(e ,…,e ))⟂,then\mathcal{A}v = 0(asfollowsfrom7.81)and\mathcal{C} v = 0
|     |     | 1   | m   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∗
$$(asfollowsfromthedefinitionofmatrixmultiplication). Hence\mathcal{A}\mathcal{C}\mathcal{C} v=\mathcal{A}vfor$$
| allv\in(span(e      |     | ,…,e | ))⟂.    |                                      |     |      |        |         |           |
| ----------------- | --- | ---- | ------- | ------------------------------------ | --- | ---- | ------ | ------- | --------- |
|                   |     | 1    | m       |                                      |     |      |        |         |           |
|                   |     | ∗    |         |                                      |     | ,…,e |        |         | ,…,e ))⟂, |
| Because           | \mathcal{A}\mathcal{C}\mathcal{C} | and  | \mathcal{A} agree | on span(e                            |     | )    | and on | (span(e |           |
|                   |     |      | ∗       |                                      | 1   | m    |        | 1       | m         |
| weconcludethat\mathcal{A}\mathcal{C}\mathcal{C} |     |      | =\mathcal{A}.     | Thusthedisplayedequationabovebecomes |     |      |        |         |           |
|                   |     |      |         | \mathcal{A}=\mathcal{B}\mathcal{D}\mathcal{C}                                |     | ∗,   |        |         |           |
asdesired.
Notethatthematrix\mathcal{A}intheresultabovehaspnentries. Incomparison,the
matrices\mathcal{B},\mathcal{D},and\mathcal{C}abovehaveatotalof
m(p+m+n)
entries. Thusifpandnarelargenumbersandtherankmisconsiderablyless
thanpandn, thenthenumberofentriesthatmustbestoredonacomputerto
represent\mathcal{A}isconsiderablylessthanpn.

| -------- | ----------------------------- | --- | --- | --- | --- |
Exercises 7E
1 Suppose\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Showthat\mathcal{T} = 0ifandonlyifallsingularvalues
of\mathcal{T} are0.
2 Suppose\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W})ands > 0. Provethatsisasingularvalueof\mathcal{T} if
| andonlyifthereexistnonzerovectorsv\in\mathcal{V} |     |     | andw\in\mathcal{W} | suchthat |     |
| ------------------------------------ | --- | --- | ------ | -------- | --- |
∗
|     | \mathcal{T}v=sw | and \mathcal{T} | w=sv. |     |     |
| --- | ----- | ----- | ----- | --- | --- |
Thevectorsv,wsatisfyingbothequationsabovearecalleda Schmidtpair.
Erhard Schmidtintroducedtheconceptofsingularvaluesin1907.
| 3 Giveanexampleof\mathcal{T}   | \inℒ(\mathbf{C}2)suchthat0istheonlyeigenvalueof\mathcal{T} |     |     |     | and |
| -------------------- | ------------------------------------- | --- | --- | --- | --- |
| thesingularvaluesof\mathcal{T} | are5,0.                               |     |     |     |     |
4 Supposethat\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}),s isthelargestsingularvalueof\mathcal{T},ands is
|                              |           | 1            |     |     | n   |
| ---------------------------- | --------- | ------------ | --- | --- | --- |
| thesmallestsingularvalueof\mathcal{T}. |           | Provethat    |     |     |     |
|                              | {‖\mathcal{T}v‖∶v\in\mathcal{V} |              | ,s  |     |     |
|                              |           | and‖v‖=1}=[s |     | ].  |     |
n 1
5 Suppose \mathcal{T} \in ℒ(\mathbf{C}2) is defined by \mathcal{T}(x,y) = (-4y,x). Find the singular
valuesof\mathcal{T}.
ℒ(𝒫
6 Find the singular values of the differentiation operator \mathcal{D} \in (\mathbf{R}))
| definedby\mathcal{D}p=p′,wheretheinnerproducton𝒫 |     |     | (\mathbf{R})isasin Example6.34. |     |     |
| -------------------------------------- | --- | --- | --------------------- | --- | --- |
7 Suppose that \mathcal{T} \in ℒ(\mathcal{V}) is self-adjoint or that \mathbf{F} = \mathbf{C} and \mathcal{T} \in ℒ(\mathcal{V}) is
normal. Let \lambda ,…,\lambda be the eigenvalues of \mathcal{T}, each included in this list
1 n
as many times as the dimension of the corresponding eigenspace. Show
thatthesingularvaluesof\mathcal{T} are|\lambda |,…,|\lambda |,afterthesenumbershavebeen
1 n
sortedintodecreasingorder.
| Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). | Supposes |             | >0ande | ,…,e | isan |
| ----------------- | -------- | ----------- | ------ | ---- | ---- |
| 8                 |          | 1 \geqs 2 \geq⋯\geqs | m      | 1    | m    |
orthonormallistin\mathcal{V} and f ,…, f isanorthonormallistin\mathcal{W} suchthat
|     | 1         | m       |         |     |     |
| --- | --------- | ------- | ------- | --- | --- |
|     | \mathcal{T}v=s \langlev,e | \ranglef +⋯+s | \langlev,e \ranglef |     |     |
|     | 1         | 1 1     | m m     | m   |     |
foreveryv\in\mathcal{V}.
| (a) Provethat | f ,…, f isanorthonormalbasisofrange\mathcal{T}. |     |     |     |     |
| ------------- | ------------------------------------- | --- | --- | --- | --- |
1 m
| (b) Provethate | ,…,e isanorthonormalbasisof(null\mathcal{T})⟂. |     |     |     |     |
| -------------- | ------------------------------------ | --- | --- | --- | --- |
1 m
| (c) Provethats | ,…,s arethepositivesingularvaluesof\mathcal{T}. |     |     |     |     |
| -------------- | ------------------------------------- | --- | --- | --- | --- |
1 m
∗
$$(d) Prove that if k \in {1,…,m}, then e is an eigenvector of \mathcal{T} \mathcal{T} with$$
k
correspondingeigenvalues2.
k
$$(e) Provethat$$
|     | \mathcal{T}\mathcal{T} ∗ w=s2\langlew, | f \ranglef +⋯+s | 2\langlew, | f \ranglef |     |
| --- | ------------ | --------- | ---- | ---- | --- |
|     |              | 1 1 1     | m    | m m  |     |
forallw\in\mathcal{W}.

| --- | --- | --------- | --- | -------------------------- | --- | --- | --- |
∗
9 Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Showthat\mathcal{T}and\mathcal{T} havethesamepositivesingular
values.
| Suppose\mathcal{T}                    | \in   | ℒ(\mathcal{V},\mathcal{W})hassingularvaluess |                   |     | ,…,s . | Provethatif\mathcal{T} | isan |
| --------------------------- | --- | ------------------------ | ----------------- | --- | ------ | ------------ | ---- |
| 10                          |     |                          |                   |     | 1 n    |              |      |
| invertiblelinearmap,then\mathcal{T}-1 |     |                          | hassingularvalues |     |        |              |      |
1 1
,…, .
s s
n 1
|                 |     | \inℒ(\mathcal{V},\mathcal{W})andv | ,…,v |     |                          |     |     |
| --------------- | --- | ----------- | ---- | --- | ------------------------ | --- | --- |
| 11 Supposethat\mathcal{T} |     |             |      |     | isanorthonormalbasisof\mathcal{V}. |     | Let |
1 n
| s ,…,s           | denotethesingularvaluesof\mathcal{T}. |                |                          |           |          |     |     |
| ---------------- | --------------------------- | -------------- | ------------------------ | --------- | -------- | --- | --- |
| 1                | n                           |                |                          |           |          |     |     |
| (a) Provethat‖\mathcal{T}v |                             | ‖2+⋯+‖\mathcal{T}v       | ‖2                       | =s2+⋯+s2. |          |     |     |
|                  |                             | 1              | n                        | 1         | n        |     |     |
| (b) Provethatif\mathcal{W} |                             | =\mathcal{V} and\mathcal{T}        | isapositiveoperator,then |           |          |     |     |
|                  |                             | \langle\mathcal{T}v ,v \rangle+⋯+\langle\mathcal{T}v |                          | ,v        | \rangle=s +⋯+s | .   |     |
|                  |                             | 1 1            |                          | n         | n 1      | n   |     |
Seethecommentafter Exercise5in Section7A.
12 (a) Giveanexampleofafinite-dimensionalvectorspaceandanoperator\mathcal{T}
| onitsuchthatthesingularvaluesof\mathcal{T}2 |     |     |     |     | donotequalthesquaresofthe |     |     |
| --------------------------------- | --- | --- | --- | --- | ------------------------- | --- | --- |
singularvaluesof\mathcal{T}.
$$(b) Suppose \mathcal{T} \in ℒ(\mathcal{V}) is normal. Prove that the singular values of \mathcal{T}2$$
equalthesquaresofthesingularvaluesof\mathcal{T}.
13 Suppose \mathcal{T} ,\mathcal{T} \in ℒ(\mathcal{V}). Prove that \mathcal{T} and \mathcal{T} have the same singular
|                                              | 1     | 2   |     | 1   | 2   |               |     |
| -------------------------------------------- | ----- | --- | --- | --- | --- | ------------- | --- |
|                                              |       |     |     |     | ,\mathcal{S}  | \inℒ(\mathcal{V})suchthat |     |
| valuesifandonlyifthereexistunitaryoperators\mathcal{S} |       |     |     |     | 1   | 2             |     |
| \mathcal{T} =\mathcal{S}                                         | \mathcal{T} \mathcal{S} . |     |     |     |     |               |     |
| 1                                            | 1 2 2 |     |     |     |     |               |     |
14 Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Lets denotethesmallestsingularvalueof\mathcal{T}. Prove
n
| thats | ‖v‖\leq‖\mathcal{T}v‖foreveryv\in\mathcal{V}. |     |     |     |     |     |     |
| ----- | -------------------- | --- | --- | --- | --- | --- | --- |
n
15 Suppose\mathcal{T} \in ℒ(\mathcal{V})ands \geq ⋯ \geq s arethesingularvaluesof\mathcal{T}. Prove
|             |                          | 1           |     | n      |         |     |     |
| ----------- | ------------------------ | ----------- | --- | ------ | ------- | --- | --- |
| thatif      | \lambdaisaneigenvalueof\mathcal{T},thens |             |     | \geq|\lambda|\geqs | .       |     |     |
|             |                          |             |     | 1      | n       |     |     |
|             |                          |             |     | ∗ †    | ∗       |     |     |
| 16 Suppose\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}).                 | Provethat(\mathcal{T} |     | )      | =(\mathcal{T}†) . |     |     |
Comparetheresultinthisexercisetotheanalogousresultforinvertible
linearmaps[see7.5(f)].
Suppose ℒ(\mathcal{V}). Provethat is self-adjoint if and only if \mathcal{T}† is self-
| 17  | \mathcal{T} \in |     | \mathcal{T}   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
adjoint.
Matricesunfold
Singularvaluesgleamlikestars
Orderinchaosshines
—writtenby Chat GPTwithinputhaikuabout SVD

| --- | -------- | ----------------------------- | --- | --- | --- | --- | --- |
| 7F Consequences |           |      | of Singular |     | Value Decomposition |     |     |
| --------------- | --------- | ---- | ----------- | --- | ------------------- | --- | --- |
| Norms           | of Linear | Maps |             |     |                     |     |     |
Thesingularvaluedecompositionleadstothefollowingupperboundfor‖\mathcal{T}v‖.
| 7.82     | upperboundfor | ‖\mathcal{T}v‖ |                                    |     |     |     |      |
| -------- | ------------- | ---- | ---------------------------------- | --- | --- | --- | ---- |
| Suppose\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}).      |      | Lets bethelargestsingularvalueof\mathcal{T}. |     |     |     | Then |
|     |     |     |     | ‖\mathcal{T}v‖\leqs | ‖v‖ |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- |
forallv\in\mathcal{V}.
| Proof Lets                | ,…,s | denotethepositive |       |      |                        |       |                  |
| ------------------------- | ---- | ----------------- | ----- | ---- | ---------------------- | ----- | ---------------- |
|                           | 1    | m                 |       |      | For a lower            | bound | on ‖\mathcal{T}v‖, look at |
| singularvaluesof\mathcal{T},andlete |      |                   | ,…,e  | be   |                        |       |                  |
|                           |      |                   | 1     | m    | Exercise14in Section7E. |       |                  |
| anorthonormallistin\mathcal{V}and   |      |                   | f ,…, | f be |                        |       |                  |
|                           |      |                   | 1     | m    |                        |       |                  |
anorthonormallistin\mathcal{W} thatprovideasingularvaluedecompositionof\mathcal{T}. Thus
| 7.83       |            | \mathcal{T}v=s  | \langlev,e      | \ranglef          | +⋯+s \langlev,e | \ranglef   |     |
| ---------- | ---------- | ----- | --------- | ----------- | --------- | ---- | --- |
|            |            |       | 1         | 1 1         | m         | m m  |     |
| forallv\in\mathcal{V}. | Henceifv\in\mathcal{V} |       | then      |             |           |      |     |
|            |            | ‖\mathcal{T}v‖2 | =s2∣\langlev,e  | \rangle∣2+⋯+s     | 2∣\langlev,e    | \rangle∣2  |     |
|            |            |       | 1         | 1           | m         | m    |     |
|            |            |       | \leqs2(∣\langlev,e | \rangle∣2+⋯+∣\langlev,e |           | \rangle∣2) |     |
|            |            |       | 1         | 1           |           | m    |     |
\leqs2‖v‖2,
wherethelastinequalityfollowsfrom Bessel’sinequality(6.26). Takingsquare
rootsofbothsidesoftheinequalityaboveshowsthat‖\mathcal{T}v‖\leqs ‖v‖,asdesired.
Suppose\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W})ands isthelargestsingularvalueof\mathcal{T}. Theresult
aboveshowsthat
|      |     |        | forallv\in\mathcal{V} |     | with‖v‖\leq1. |     |     |
| ---- | --- | ------ | --------- | --- | ---------- | --- | --- |
| 7.84 |     | ‖\mathcal{T}v‖\leqs | 1         |     |            |     |     |
Takingv=e in7.83showsthat\mathcal{T}e =s f . Because‖f ‖=1,thisimpliesthat
|     | 1   |     |     | 1   | 1 1 | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
‖\mathcal{T}e ‖=s . Thusbecause‖e ‖=1,theinequalityin7.84leadstotheequation
| ---- | --- | ------------ | --- | --- | ----------- | --- | --- |
|      |     | max{‖\mathcal{T}v‖∶v\in\mathcal{V} |     |     | and‖v‖\leq1}=s |     |     |
| 7.85 |     |              |     |     |             | 1 . |     |
Theequationaboveisthemotivationforthefollowingdefinition,whichdefines
thenormof\mathcal{T} tobetheleftsideoftheequationabovewithoutneedingtoreferto
singularvaluesorthesingularvaluedecomposition.
| 7.86 definition: |          | normofalinearmap,‖\cdot‖ |                                         |     |     |     |     |
| ---------------- | -------- | -------------------- | --------------------------------------- | --- | --- | --- | --- |
| Suppose\mathcal{T}         | \inℒ(\mathcal{V},\mathcal{W}). |                      | Thenthenormof\mathcal{T},denotedby‖\mathcal{T}‖,isdefinedby |     |     |     |     |
‖\mathcal{T}‖=max{‖\mathcal{T}v‖∶v\in\mathcal{V}
and‖v‖\leq1}.

| --------- | ---------------------------------------- | --- |
In general, the maximum of an infinite set of nonnegative numbers need
notexist. However,thediscussionbefore7.86showsthatthemaximuminthe
definition of the norm of a linear map \mathcal{T} from \mathcal{V} to \mathcal{W} does indeed exist (and
equalsthelargestsingularvalueof\mathcal{T}).
Wenowhavetwodifferentusesofthewordnormandthenotation‖\cdot‖. Our
firstuseofthisnotationwasinconnectionwithaninnerproducton\mathcal{V},whenwe
defined‖v‖=\sqrt\langlev,v\rangleforeachv\in\mathcal{V}. Ourseconduseofthenormnotationand
terminologyiswiththedefinitionwejustmadeof‖\mathcal{T}‖for\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). The
norm‖\mathcal{T}‖for\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})doesnotusuallycomefromtakinganinnerproduct
of\mathcal{T} withitself(see Exercise21). Youshouldbeabletotellfromthecontextand
fromthesymbolsusedwhichmeaningofthenormisintended.
Thepropertiesofthenormonℒ(\mathcal{V},\mathcal{W})listedbelowlookidenticaltoproperties
ofthenormonaninnerproductspace(see6.9and6.17). Theinequalityin(d)is
calledthetriangleinequality,thususingthesameterminologythatweusedfor
| thenormon\mathcal{V}. Forthereversetriangleinequality,see Exercise1. |     |     |
| --------------------------------------------------------- | --- | --- |
7.87 basicpropertiesofnormsoflinearmaps
| Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). | Then |     |
| ----------------- | ---- | --- |
$$(a) ‖\mathcal{T}‖\geq0;$$
| (b) ‖\mathcal{T}‖=0 ⟺           | \mathcal{T} =0; |     |
| --------------------- | ----- | --- |
| (c) ‖\lambda\mathcal{T}‖=|\lambda|‖\mathcal{T}‖forall | \lambda\in\mathbf{F};  |     |
$$(d) ‖\mathcal{S}+\mathcal{T}‖\leq‖\mathcal{S}‖+‖\mathcal{T}‖forall\mathcal{S}\inℒ(\mathcal{V},\mathcal{W}).$$
Proof
$$(a) Because‖\mathcal{T}v‖\geq0foreveryv\in\mathcal{V},thedefinitionof‖\mathcal{T}‖impliesthat‖\mathcal{T}‖\geq0.$$
$$(b) Suppose‖\mathcal{T}‖ = 0. Thus\mathcal{T}v = 0forallv \in \mathcal{V} with‖v‖ \leq 1. Ifu \in \mathcal{V} with$$
u\neq0,then
u
|     | \mathcal{T}u=‖u‖\mathcal{T}( | )=0, |
| --- | -------- | ---- |
‖u‖
wherethelastequalityholdsbecauseu/‖u‖hasnorm1. Because\mathcal{T}u=0for
| allu\in\mathcal{V},wehave\mathcal{T}   | =0.                 |                |
| ---------------- | ------------------- | -------------- |
| Conversely,if\mathcal{T}   | =0then\mathcal{T}v=0forallv\in\mathcal{V} | andhence‖\mathcal{T}‖=0. |
| (c) Suppose \lambda\in\mathbf{F}. | Then                |                |
‖\lambda\mathcal{T}‖=max{‖\lambda\mathcal{T}v‖∶v\in\mathcal{V}
and‖v‖\leq1}
=|\lambda|max{‖\mathcal{T}v‖∶v\in\mathcal{V}
and‖v‖\leq1}
=|\lambda|‖\mathcal{T}‖.
$$(d) Suppose\mathcal{S} \in ℒ(\mathcal{V},\mathcal{W}). Thedefinitionof‖\mathcal{S}+\mathcal{T}‖impliesthatthereexists$$
suchthat‖v‖\leq1and‖\mathcal{S}+\mathcal{T}‖=∥(\mathcal{S}+\mathcal{T})v∥.
| v\in\mathcal{V} |     | Now |
| --- | --- | --- |
‖\mathcal{S}+\mathcal{T}‖=∥(\mathcal{S}+\mathcal{T})v∥=‖\mathcal{S}v+\mathcal{T}v‖\leq‖\mathcal{S}v‖+‖\mathcal{T}v‖\leq‖\mathcal{S}‖+‖\mathcal{T}‖,
completingtheproofof(d).

| --- | -------------------------------------- | --- | --- | --- | --- |
For\mathcal{S},\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}),thequantity‖\mathcal{S}-\mathcal{T}‖isoftencalledthedistancebetween
\mathcal{S} and \mathcal{T}. Informally, think of the condition that ‖\mathcal{S}-\mathcal{T}‖ is a small number as
meaningthat\mathcal{S}and\mathcal{T} areclosetogether. Forexample,Exercise9assertsthatfor
| every\mathcal{T}   | \inℒ(\mathcal{V}),thereisaninvertibleoperatorascloseto\mathcal{T} |     |     | aswewish. |     |
| -------- | ------------------------------------------- | --- | --- | --------- | --- |
| 7.88     | alternativeformulasfor                      | ‖\mathcal{T}‖ |     |           |     |
| Suppose\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}). Then                               |     |     |           |     |
$$(a) ‖\mathcal{T}‖=thelargestsingularvalueof\mathcal{T};$$
| (b) ‖\mathcal{T}‖=max{‖\mathcal{T}v‖∶v\in\mathcal{V} |     | and‖v‖=1}; |     |     |     |
| -------------------- | --- | ---------- | --- | --- | --- |
$$(c) ‖\mathcal{T}‖=thesmallestnumbercsuchthat‖\mathcal{T}v‖\leqc‖v‖forallv\in\mathcal{V}.$$
Proof
$$(a) See7.85.$$
| (b) Letv\in\mathcal{V} | besuchthat0<‖v‖\leq1. |     | Letu=v/‖v‖. | Then    |        |
| ---------- | ------------------ | --- | ----------- | ------- | ------ |
|            | v                  |     |             | v ‖\mathcal{T}v‖  |        |
|            | ‖u‖=∥ ∥=1          | and | ‖\mathcal{T}u‖=∥\mathcal{T}(    | )∥=     | \geq‖\mathcal{T}v‖. |
|            | ‖v‖                |     |             | ‖v‖ ‖v‖ |        |
Thus when finding the maximum of ‖\mathcal{T}v‖ with ‖v‖ \leq 1, we can restrict
| attentiontovectorsin\mathcal{V} |         | withnorm1,proving(b).             |     |     |     |
| --------------------- | ------- | --------------------------------- | --- | --- | --- |
| (c) Supposev\in\mathcal{V}        | andv\neq0. | Thenthedefinitionof‖\mathcal{T}‖impliesthat |     |     |     |
v
|     |     | ∥\mathcal{T}( | )∥\leq‖\mathcal{T}‖, |     |     |
| --- | --- | --- | ------- | --- | --- |
‖v‖
whichimpliesthat
| 7.89        |                          | ‖\mathcal{T}v‖\leq‖\mathcal{T}‖‖v‖. |     |                 |     |
| ----------- | ------------------------ | ------------ | --- | --------------- | --- |
| Nowsupposec | \geq0and‖\mathcal{T}v‖\leqc‖v‖forallv\in\mathcal{V}. |              |     | Thisimpliesthat |     |
‖\mathcal{T}v‖\leqc
for all v \in \mathcal{V} with ‖v‖ \leq 1. Taking the maximum of the left side of the
| inequalityaboveoverallv\in\mathcal{V} |     | with‖v‖\leq1showsthat‖\mathcal{T}‖\leqc. |     |     | Thus‖\mathcal{T}‖is |
| ------------------------- | --- | ------------------------ | --- | --- | --------- |
thesmallestnumbercsuchthat‖\mathcal{T}v‖\leqc‖v‖forallv\in\mathcal{V}.
Whenworkingwithnormsoflinearmaps,youwillprobablyfrequentlyuse
theinequality7.89.
For computing an approximation of the norm of a linear map \mathcal{T} given the
matrixof\mathcal{T} withrespecttosomeorthonormalbases,7.88(a)islikelytobemost
∗
useful. The matrix of \mathcal{T} \mathcal{T} is quickly computable from matrix multiplication.
Thenacomputercanbeaskedtofindanapproximationforthelargesteigenvalue
∗
of\mathcal{T} \mathcal{T} (excellentnumericalalgorithmsexistforthispurpose). Thentakingthe
squarerootandusing7.88(a)givesanapproximationforthenormof\mathcal{T} (which
usuallycannotbecomputedexactly).

| --------- | ---------------------------------------- | --- | --- | --- |
Youshouldverifyallassertionsintheexamplebelow.
| 7.90 example: | norms |     |     |     |
| ------------- | ----- | --- | --- | --- |
• If\mathcal{I} denotestheusualidentityoperatoron\mathcal{V},then‖\mathcal{I}‖=1.
ℒ(\mathbf{F}n) \mathbf{F}n
• If \mathcal{T} \in and the matrix of \mathcal{T} with respect to the standard basis of
consistsofall1’s,then‖\mathcal{T}‖=n.
ℒ(\mathcal{V})
• If \mathcal{T} \in and \mathcal{V} has an orthonormal basis consisting of eigenvectors of
\mathcal{T} withcorrespondingeigenvalues \lambda ,…,\lambda ,then‖\mathcal{T}‖isthemaximumofthe
|     |     | 1   | n   |     |
| --- | --- | --- | --- | --- |
|,…,|\lambda
| numbers|\lambda | |.  |     |     |     |
| --------- | --- | --- | --- | --- |
1 n
• Suppose\mathcal{T} \in ℒ(\mathbf{R}5)istheoperatorwhosematrix(withrespecttothestandardbasis)isthe5-by-5matrixwhoseentryinrowj,columnkis1/(j2+k).
Standardmathematicalsoftwareshowsthatthelargestsingularvalueof\mathcal{T} is
isapproximately10-6.
approximately0.8andthesmallestsingularvalueof\mathcal{T}
Thus‖\mathcal{T}‖ \approx 0.8and(using Exercise10in Section7E)∥\mathcal{T}-1∥ \approx 106. Itisnot
possibletofindexactformulasforthesenorms.
Alinearmapanditsadjointhavethesamenorm,asshownbythenextresult.
7.91 normoftheadjoint
∗
| Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). | Then∥\mathcal{T}     | ∥=‖\mathcal{T}‖.   |             |        |
| ----------------- | ---------- | -------- | ----------- | ------ |
| Proof Supposew\in\mathcal{W}. | Then       |          |             |        |
| ∗                 | ∗ ∗        | ∗        | ∗           | ∗      |
| ∥\mathcal{T} w∥2 =\langle\mathcal{T}        | w,\mathcal{T} w\rangle=\langle\mathcal{T}\mathcal{T} | w,w\rangle\leq∥\mathcal{T}\mathcal{T} | w∥‖w‖\leq‖\mathcal{T}‖∥\mathcal{T} | w∥‖w‖. |
Theinequalityaboveimpliesthat
∗
∥\mathcal{T} w∥\leq‖\mathcal{T}‖‖w‖,
∗
| whichalongwith7.88(c)impliesthat∥\mathcal{T} |     |     | ∥\leq‖\mathcal{T}‖. |     |
| ---------------------------------- | --- | --- | ------ | --- |
Replacing\mathcal{T} with\mathcal{T} ∗ intheinequality∥\mathcal{T} ∗ ∥\leq‖\mathcal{T}‖andthenusingtheequation
| ∗ ∗                     |     | ∗         | ∗                |     |
| ----------------------- | --- | --------- | ---------------- | --- |
| (\mathcal{T} ) =\mathcal{T} showsthat‖\mathcal{T}‖\leq∥\mathcal{T} |     | ∥. Thus∥\mathcal{T} | ∥=‖\mathcal{T}‖,asdesired. |     |
You may want to construct an alternative proof of the result above using
Exercise9in Section7E,whichassertsthatalinearmapanditsadjointhavethe
samepositivesingularvalues.
| Approximation | by Linear | Maps with | Lower-Dimensional | Range |
| ------------- | --------- | --------- | ----------------- | ----- |
Thenextresultisaspectacularapplicationofthesingularvaluedecomposition.
Itsaysthattobestapproximatealinearmapbyalinearmapwhoserangehas
dimension at most k, chop off the singular value decomposition after the first
k terms. Specifically,thelinearmap\mathcal{T} inthenextresulthasthepropertythat
k
dimrange\mathcal{T} =kand\mathcal{T} minimizesthedistanceto\mathcal{T} amongalllinearmapswith
k k
rangeofdimensionatmostk. Thisresultleadstoalgorithmsforcompressing
hugematriceswhilepreservingtheirmostimportantinformation.

284 Chapter 7 Operatorson Inner Product Spaces
7.92 bestapproximationbylinearmapwhoserangehasdimension\leqk
Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})ands \geq⋯\geqs arethepositivesingularvaluesof\mathcal{T}.
1 m
Suppose1\leqk <m. Then
min{‖\mathcal{T}-\mathcal{S}‖∶\mathcal{S}\inℒ(\mathcal{V},\mathcal{W})and dimrange\mathcal{S}\leqk}=s .
k+1
Furthermore,if
\mathcal{T}v=s \langlev,e \ranglef +⋯+s \langlev,e \ranglef
1 1 1 m m m
isasingularvaluedecompositionof\mathcal{T} and\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})isdefinedby
k
\mathcal{T} v=s \langlev,e \ranglef +⋯+s \langlev,e \ranglef
k 1 1 1 k k k
foreachv\in\mathcal{V},thendimrange\mathcal{T} =kand‖\mathcal{T}-\mathcal{T} ‖=s .
k k k+1
Proof Ifv\in\mathcal{V} then
∥(\mathcal{T}-\mathcal{T} )v∥2 =∥s \langlev,e \ranglef +⋯+s \langlev,e \ranglef ∥2
k k+1 k+1 k+1 m m m
=s 2∣\langlev,e \rangle∣2+⋯+s 2∣\langlev,e \rangle∣2
k+1 k+1 m m
\leqs 2(∣\langlev,e \rangle∣2+⋯+∣\langlev,e \rangle∣2)
k+1 k+1 m
\leqs 2‖v‖2.
k+1
Thus ‖\mathcal{T} -\mathcal{T} ‖ \leq s . The equation (\mathcal{T} -\mathcal{T} )e = s f now shows that
k k+1 k k+1 k+1 k+1
‖\mathcal{T}-\mathcal{T} ‖=s .
k k+1
Suppose\mathcal{S} \in ℒ(\mathcal{V},\mathcal{W})anddimrange\mathcal{S} \leq k. Thus\mathcal{S}e ,…,\mathcal{S}e ,whichisa
1 k+1
listoflengthk+1,islinearlydependent. Hencethereexista ,…,a \in\mathbf{F},not
1 k+1
all0,suchthat
a \mathcal{S}e +⋯+a \mathcal{S}e =0.
1 1 k+1 k+1
Nowa e +⋯+a e \neq0becausea ,…,a arenotall0. Wehave
1 1 k+1 k+1 1 k+1
∥(\mathcal{T}-\mathcal{S})(a e +⋯+a e )∥2 =∥\mathcal{T}(a e +⋯+a e )∥2
1 1 k+1 k+1 1 1 k+1 k+1
=‖s a f +⋯+s a f ‖2
1 1 1 k+1 k+1 k+1
=s2|a |2+⋯+s 2|a |2
1 1 k+1 k+1
\geqs 2(|a |2+⋯+|a |2)
k+1 1 k+1
=s 2‖a e +⋯+a e ‖2.
k+1 1 1 k+1 k+1
Becausea e +⋯+a e \neq0,theinequalityaboveimpliesthat
1 1 k+1 k+1
‖\mathcal{T}-\mathcal{S}‖\geqs .
k+1
Thus\mathcal{S}=\mathcal{T} minimizes‖\mathcal{T}-\mathcal{S}‖among\mathcal{S}\inℒ(\mathcal{V},\mathcal{W})withdimrange\mathcal{S}\leqk.
k
For other examples of the use of the singular value decomposition in best
approximation,see Exercise22,whichfindsasubspaceofgivendimensionon
which the restriction of a linear map is as small as possible, and Exercise 27,
whichfindsaunitaryoperatorthatisascloseaspossibletoagivenoperator.

Section7F Consequencesof Singular Value Decomposition 285
Recall our discussion before 7.54 of the analogy between complex numbers z
with|z|=1andunitaryoperators. Continuingwiththisanalogy,notethatevery
complexnumberzexcept0canbewrittenintheform
z
$$z=( )|z|$$
|z|
z
=( )\sqrtzz,
|z|
wherethefirstfactor,namely,z/|z|,hasabsolutevalue1.
Ouranalogyleadsustoguessthateveryoperator\mathcal{T} \inℒ(\mathcal{V})canbewrittenas
aunitaryoperatortimes\sqrt\mathcal{T}∗\mathcal{T}. Thatguessisindeedcorrect. Thecorresponding
resultiscalledthepolardecomposition,whichgivesabeautifuldescriptionofan
arbitraryoperatoron\mathcal{V}.
Note that if \mathcal{T} \in ℒ(\mathcal{V}), then \mathcal{T} ∗ \mathcal{T} is a positive operator [as was shown in
7.64(a)]. Thustheoperator\sqrt\mathcal{T}∗\mathcal{T} makessenseandiswelldefinedasapositive
operatoron\mathcal{V}.
Thepolardecompositionthatweareabouttostateandprovesaysthatevery
operatoron\mathcal{V} istheproductofaunitaryoperatorandapositiveoperator. Thus
we can write an arbitrary operator on \mathcal{V} as the product of two nice operators,
eachofwhichcomesfromaclassthatwecancompletelydescribeandthatwe
understandreasonablywell. Theunitaryoperatorsaredescribedby7.55if\mathbf{F} =\mathbf{C};
thepositiveoperatorsaredescribedbytherealandcomplexspectraltheorems
$$(7.29and7.31).$$
Specifically,considerthecase\mathbf{F} =\mathbf{C},andsuppose
\mathcal{T} =\mathcal{S}\sqrt\mathcal{T}∗\mathcal{T}
isapolardecompositionofanoperator\mathcal{T} \inℒ(\mathcal{V}),where\mathcal{S}isaunitaryoperator.
Thenthereisanorthonormalbasisof\mathcal{V} withrespecttowhich\mathcal{S}hasadiagonal
matrix,andthereisanorthonormalbasisof\mathcal{V} withrespecttowhich\sqrt\mathcal{T}∗\mathcal{T} has
a diagonal matrix. Warning: There may not exist an orthonormal basis that
simultaneouslyputsthematricesofboth\mathcal{S}and\sqrt\mathcal{T}∗\mathcal{T} intothesenicediagonal
forms—\mathcal{S}mayrequireoneorthonormalbasisand\sqrt\mathcal{T}∗\mathcal{T} mayrequireadifferent
orthonormalbasis.
However (still assuming that \mathbf{F} = \mathbf{C}), if \mathcal{T} is normal, then an orthonormal
basisof\mathcal{V} canbechosensuchthatboth\mathcal{S}and\sqrt\mathcal{T}∗\mathcal{T} havediagonalmatriceswith
respecttothisbasis—see Exercise31. Theconverseisalsotrue: If\mathcal{T} \in ℒ(\mathcal{V})
and\mathcal{T} =\mathcal{S}\sqrt\mathcal{T}∗\mathcal{T}forsomeunitaryoperator\mathcal{S}\inℒ(\mathcal{V})suchthat\mathcal{S}and\sqrt\mathcal{T}∗\mathcal{T}both
havediagonalmatriceswithrespecttothesameorthonormalbasisof\mathcal{V},then\mathcal{T}
isnormal. Thisholdsbecause\mathcal{T} thenhasadiagonalmatrixwithrespecttothis
sameorthonormalbasis,whichimpliesthat\mathcal{T} isnormal[bytheequivalenceof
$$(c)and(a)in7.31].$$

| --- | -------- | --- | ----------------------------- | --- | --- | --- | --- | --- |
Thepolardecompositionbelowisvalidonbothrealandcomplexinnerproduct
spacesandforalloperatorsonthosespaces.
7.93 polardecomposition
Suppose\mathcal{T} \inℒ(\mathcal{V}). Thenthereexistsaunitaryoperator\mathcal{S}\inℒ(\mathcal{V})suchthat
=\mathcal{S}\sqrt\mathcal{T}∗\mathcal{T}.
\mathcal{T}
|       | Lets ,…,s               |     | bethepositivesingularvaluesof\mathcal{T},andlete |          |     |     |     | ,…,e and |
| ----- | ----------------------- | --- | -------------------------------------- | -------- | --- | --- | --- | -------- |
| Proof | 1                       | m   |                                        |          |     |     |     | 1 m      |
| f ,…, | f beorthonormallistsin\mathcal{V} |     |                                        | suchthat |     |     |     |          |
1 m
|      |     |     |      | \langlev,e   | +⋯+s | \langlev,e |        |     |
| ---- | --- | --- | ---- | ------ | ---- | ---- | ------ | --- |
| 7.94 |     |     | \mathcal{T}v=s | 1 1 \ranglef | 1    | m    | m \ranglef m |     |
foreveryv \in\mathcal{V}. Extende ,…,e and f ,…, f toorthonormalbasese ,…,e
|     |     |     | 1   | m   | 1   | m   |     | 1 n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
,…,
| and | f f of\mathcal{V}. |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- |
|     | 1 n      |     |     |     |     |     |     |     |
Define\mathcal{S}\inℒ(\mathcal{V})by
|             |     |      | \mathcal{S}v=\langlev,e |     | +⋯+\langlev,e |     |     |     |
| ----------- | --- | ---- | ------- | --- | ------- | --- | --- | --- |
|             |     |      |         |     | \ranglef      |     | \ranglef  |     |
|             |     |      |         | 1   | 1       | n   | n   |     |
| foreachv\in\mathcal{V}. |     | Then |         |     |         |     |     |     |
∥2
|     |     |     | ‖\mathcal{S}v‖2 | =∥\langlev,e | \ranglef +⋯+\langlev,e  |     | \ranglef  |     |
| --- | --- | --- | ----- | ------ | ----------- | --- | --- | --- |
|     |     |     |       |        | 1 1         |     | n n |     |
|     |     |     |       | =∣\langlev,e | \rangle∣2+⋯+∣\langlev,e |     | \rangle∣2 |     |
|     |     |     |       | 1      |             |     | n   |     |
=‖v‖2.
Thus\mathcal{S}isaunitaryoperator.
|     | ∗   |     |     |     |     |     |     | ∗   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Applying\mathcal{T} tobothsidesof7.94andthenusingtheformulafor\mathcal{T} givenby
7.77showsthat
∗
|              |     | \mathcal{T}              | \mathcal{T}v=s2\langlev,e |      | \ranglee +⋯+s | 2\langlev,e | \ranglee      |     |
| ------------ | --- | -------------- | --------- | ---- | ------- | ----- | ------- | --- |
|              |     |                |           | 1    | 1 1     | m     | m m     |     |
| foreveryv\in\mathcal{V}. |     | Thusifv\in\mathcal{V},then |           |      |         |       |         |     |
|              |     | \sqrt\mathcal{T}∗\mathcal{T}v=s        |           | \langlev,e | \ranglee +⋯+s |       | \langlev,e \ranglee |     |
|              |     |                |           | 1    | 1 1     | m     | m m     |     |
because the operator that sends v to the right side of the equation above is a
| positiveoperatorwhosesquareequals\mathcal{T} |     |     |     |     | ∗ \mathcal{T}. | Now |     |     |
| ---------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- |
\mathcal{S}\sqrt\mathcal{T}∗\mathcal{T}v=\mathcal{S}(s
|     |     |     |     | \langlev,e | \ranglee      | +⋯+s | \langlev,e \ranglee ) |     |
| --- | --- | --- | --- | ---- | ------- | ---- | --------- | --- |
|     |     |     |     | 1    | 1 1     | m    | m m       |     |
|     |     |     | =s  | \langlev,e | \ranglef +⋯+s | \langlev,e | \ranglef        |     |
|     |     |     |     | 1    | 1 1     | m    | m m       |     |
=\mathcal{T}v,
wherethelastequationfollowsfrom7.94.
Exercise27showsthattheunitaryoperator\mathcal{S}producedintheproofaboveis
ascloseasaunitaryoperatorcanbeto\mathcal{T}.
Alternativeproofsofthepolardecompositiondirectlyusethespectraltheorem,
avoiding the singular value decomposition. However, the proof above seems
cleanerthanthosealternativeproofs.

| --- | --------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
| Operators |     | Applied | to Ellipsoids |     | and Parallelepipeds |     |     |     |
| --------- | --- | ------- | ------------- | --- | ------------------- | --- | --- | --- |
ball,\mathcal{B}
**7.95 定义：** Theballin\mathcal{V}
ofradius1centeredat0,denotedby\mathcal{B},isdefinedby
∶‖v‖<1}.
\mathcal{B}={v\in\mathcal{V}
| Ifdim\mathcal{V} | =2,theworddiskissometimesusedinsteadof |     |     |     |     |     |     |     |
| ------ | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ball. However,usingballinalldimensionsislessconfusing.
| Similarly,ifdim\mathcal{V} |     | =2,thenthewordellipseissometimes |     |     |     |     |     |     |
| ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
usedinsteadofthewordellipsoidthatweareabouttodefine.
| Again,usingellipsoid |     |     | inalldimensionsislessconfusing. |     |     |     |     |     |
| -------------------- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
Youcanthinkoftheellipsoiddefinedbelowasobtained
bystartingwiththeball\mathcal{B}andthenstretchingbyafactorof
| s alongeach |             | f -axis.      |     |        |                   |     | Theball\mathcal{B}in\mathbf{R}2. |     |
| ----------- | ----------- | ------------- | --- | ------ | ----------------- | --- | ------------- | --- |
| k           |             | k             |     |        |                   |     |               |     |
| 7.96        | definition: | ellipsoid,\mathcal{E}(s |     | f ,…,s | f ),principalaxes |     |               |     |
|             |             |               |     | 1 1    | n n               |     |               |     |
|             |             | ,…,           |     |        |                   |     | ,…,s          |     |
Supposethat f 1 f n isanorthonormalbasisof\mathcal{V} ands 1 n arepositive
numbers. Theellipsoid \mathcal{E}(s f ,…,s f )withprincipalaxess f ,…,s f is
|     |     |     |     | 1 1 | n n |     | 1   | 1 n n |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
definedby
|     |     |        |          |     | |\langlev, \rangle|2 |     | |\langlev, \rangle|2 |     |
| --- | --- | ------ | -------- | --- | -------- | --- | -------- | --- |
|     |     |        |          |     | f        |     | f        |     |
|     | \mathcal{E}(s | f ,…,s | f )={v\in\mathcal{V} |     | ∶ 1      | +⋯+ | n <1}.   |     |
|     | 1   | 1 n    | n        |     | s2       |     | s2       |     |
|     |     |        |          |     | 1        |     | n        |     |
Theellipsoidnotation\mathcal{E}(s f ,…,s f )doesnotexplicitlyincludetheinner
|     |     |     |     | 1 1 | n n |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
product space \mathcal{V}, even though the definition above depends on \mathcal{V}. However,
the inner product space \mathcal{V} should be clear from the context and also from the
| requirementthat |          | f ,…,      | f beanorthonormalbasisof\mathcal{V}. |     |     |     |     |     |
| --------------- | -------- | ---------- | -------------------------- | --- | --- | --- | --- | --- |
|                 |          | 1          | n                          |     |     |     |     |     |
| 7.97            | example: | ellipsoids |                            |     |     |     |     |     |
Theellipsoid\mathcal{E}(2f , f )in\mathbf{R}2,where Theellipsoid\mathcal{E}(2f , f )in\mathbf{R}2,where
|     |                          | 1   | 2   |     |     |       | 1 2        |         |
| --- | ------------------------ | --- | --- | --- | --- | ----- | ---------- | ------- |
| f   | , f isthestandardbasisof |     |     | \mathbf{R}2. |     | 1 1   |            | 1 1     |
|     | 1 2                      |     |     |     | f   | =( ,  | )and f =(- | , ).    |
|     |                          |     |     |     | 1   | \sqrt 2 \sqrt | 2 2        | \sqrt 2 \sqrt 2 |

| -------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
Theellipsoid
|     |     |     |     |     |     | \mathcal{E}(4f ,3f        | ,2f )in\mathbf{R}3,      |     |
| --- | --- | --- | --- | --- | --- | --------------- | --------------- | --- |
|     |     |     |     |     |     | 1               | 2 3             |     |
|     |     |     |     |     |     | where           | f , f , f isthe |     |
|     |     |     |     |     |     |                 | 1 2 3           |     |
|     |     |     |     |     |     | standardbasisof |                 | \mathbf{R}3. |
Theellipsoid\mathcal{E}(f ,…, f )equalstheball\mathcal{B}in\mathcal{V} foreveryorthonormalbasis
|         |                                    | 1   | n   |     |     |     |     |     |
| ------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| f ,…, f | of\mathcal{V} [by Parseval’sidentity6.30(b)]. |     |     |     |     |     |     |     |
1 n
| 7.98 notation:           |     | \mathcal{T}(\Omega) |     |                     |     |     |     |     |
| ------------------------ | --- | ---- | --- | ------------------- | --- | --- | --- | --- |
| For\mathcal{T} afunctiondefinedon\mathcal{V} |     |      |     | and\Omega\subseteq\mathcal{V},define\mathcal{T}(\Omega)by |     |     |     |     |
\mathcal{T}(\Omega)={\mathcal{T}v∶v\in\Omega}.
| Thusif\mathcal{T} | isafunctiondefinedon\mathcal{V},then\mathcal{T}(\mathcal{V})=range\mathcal{T}. |     |     |     |     |     |     |     |
| ------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Thenextresultstatesthateveryinvertibleoperator\mathcal{T} \inℒ(\mathcal{V})mapstheball
\mathcal{B} in \mathcal{V} onto an ellipsoid in \mathcal{V}. The proof shows that the principal axes of this
ellipsoidcomefromthesingularvaluedecompositionof\mathcal{T}.
7.99 invertibleoperatortakesballtoellipsoid
Suppose\mathcal{T} \inℒ(\mathcal{V})isinvertible. Then\mathcal{T}mapstheball\mathcal{B}in\mathcal{V}ontoanellipsoid
in\mathcal{V}.
| Suppose\mathcal{T} |     | hassingularvaluedecomposition |     |     |     |     |     |     |
| -------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
Proof
| 7.100 |     | \mathcal{T}v=s | \langlev,e | \ranglef +⋯+s |     | \langlev,e \ranglef |     |     |
| ----- | --- | ---- | ---- | ------- | --- | ------- | --- | --- |
|       |     |      | 1    | 1 1     | n   | n n     |     |     |
forallv\in\mathcal{V};heres ,…,s arethesingularvaluesof\mathcal{T}ande ,…,e and ,…,
|     |     | 1   | n   |     |     |     | 1 n | f 1 f n |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- |
arebothorthonormalbasesof\mathcal{V}. Wewillshowthat\mathcal{T}(\mathcal{B})=\mathcal{E}(s f ,…,s f ).
|     |     |     |     |     |     |     | 1 1 | n n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
First suppose v \in \mathcal{B}. Because \mathcal{T} is invertible, none of the singular values
| s ,…,s | equals0(see7.68). |     | Thus7.100impliesthat |     |     |     |     |     |
| ------ | ----------------- | --- | -------------------- | --- | --- | --- | --- | --- |
1 n
|            | ∣\langle\mathcal{T}v, f | \rangle∣2    | ∣\langle\mathcal{T}v,              | f \rangle∣2  |             |        |         |     |
| ---------- | ------- | ------ | ------------------ | ------ | ----------- | ------ | ------- | --- |
|            |         | 1      |                    | n      |             |        |         |     |
|            |         | +⋯+    |                    | =|\langlev,e | \rangle|2+⋯+|\langlev,e |        | \rangle|2 <1. |     |
|            | s2      |        |                    | s2     | 1           |        | n       |     |
|            | 1       |        |                    | n      |             |        |         |     |
| Thus\mathcal{T}v\in\mathcal{E}(s |         | f ,…,s | f ). Hence\mathcal{T}(\mathcal{B})\subseteq\mathcal{E}(s |        |             | f ,…,s | f ).    |     |
|            | 1       | 1 n    | n                  |        |             | 1 1 n  | n       |     |
Toproveinclusionintheotherdirection,nowsupposew\in\mathcal{E}(s f ,…,s f ).
|     |     |     |     |     |     |     |     | 1 1 n n |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- |
Let
|                                    |        |      | \langlew, | f \rangle   | \langlew, | f \rangle       |      |          |
| ---------------------------------- | ------ | ---- | --- | ----- | --- | --------- | ---- | -------- |
|                                    |        |      |     | 1     |     | n         |      |          |
|                                    |        | v=   |     | e +⋯+ |     | e .       |      |          |
|                                    |        |      |     | s 1   |     | s n       |      |          |
|                                    |        |      |     | 1     |     | n         |      |          |
| Then‖v‖<1and7.100impliesthat\mathcal{T}v=\langlew, |        |      |     |       | f   | \ranglef +⋯+\langlew, | f \ranglef | =w. Thus |
|                                    |        |      |     |       | 1   | 1         | n    | n        |
| \mathcal{T}(\mathcal{B})\supseteq\mathcal{E}(s                           | f ,…,s | f ). |     |       |     |           |      |          |
1 1 n n

| --- | --------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
We now use the previous result to show that invertible operators take all
ellipsoids,notjusttheballofradius1,toellipsoids.
7.101 invertibleoperatortakesellipsoidstoellipsoids
| Suppose\mathcal{T} | \inℒ(\mathcal{V})isinvertibleand\mathcal{E}isanellipsoidin\mathcal{V}. |     |     |     |     |     |     | Then\mathcal{T}(\mathcal{E})isan |     |
| -------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- |
ellipsoidin\mathcal{V}.
Proof There exist an orthonormal basis f ,…, f of \mathcal{V} and positive numbers
|                      |               |       |                       |     |                     | 1        | n    |       |     |
| -------------------- | ------------- | ----- | --------------------- | --- | ------------------- | -------- | ---- | ----- | --- |
| s ,…,s               | suchthat\mathcal{E}=\mathcal{E}(s |       | f ,…,s                |     | f ). Define\mathcal{S}\inℒ(\mathcal{V})by |          |      |       |     |
| 1 n                  |               |       | 1 1                   | n   | n                   |          |      |       |     |
|                      |               | \mathcal{S}(a f | +⋯+a                  | f   | )=a                 | s f +⋯+a |      | s f . |     |
|                      |               | 1     | 1                     | n n | 1                   | 1 1      | n    | n n   |     |
| Then\mathcal{S}mapstheball\mathcal{B}of\mathcal{V} |               |       | onto\mathcal{E},asyoucanverify. |     |                     |          | Thus |       |     |
\mathcal{T}(\mathcal{E})=\mathcal{T}(\mathcal{S}(\mathcal{B}))=(\mathcal{T}\mathcal{S})(\mathcal{B}).
Theequationaboveand7.99,appliedto\mathcal{T}\mathcal{S},showthat\mathcal{T}(\mathcal{E})isanellipsoidin\mathcal{V}.
| Recall(see3.95)thatifu\in\mathcal{V} |     |     |     | and\Omega\subseteq\mathcal{V} |     | thenu+\Omegaisdefinedby |     |     |     |
| ------------------------ | --- | --- | --- | ------ | --- | ------------------ | --- | --- | --- |
u+\Omega={u+w∶w\in\Omega}.
+
Geometrically, the sets \Omega and u \Omega look the same, but they are in different
locations.
Inthefollowingdefinition,ifdim\mathcal{V} =2thenthewordparallelogramisoften
usedinsteadofparallelepiped.
| 7.102 | definition: | \mathcal{P}(v ,…,v |     | ),parallelepiped |     |     |     |     |     |
| ----- | ----------- | -------- | --- | ---------------- | --- | --- | --- | --- | --- |
1 n
| Supposev | ,…,v | isabasisof\mathcal{V}. |     | Let |     |     |     |     |     |
| -------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
1 n
|                 |      | ,…,v                                   |      | +⋯+a |     | ∶a ,…,a |              | \in(0,1)}. |     |
| --------------- | ---- | -------------------------------------- | ---- | ---- | --- | ------- | ------------ | -------- | --- |
|                 | \mathcal{P}(v  |                                        | )={a | v    |     | v       |              |          |     |
|                 |      | 1 n                                    |      | 1 1  | n   | n 1     | n            |          |     |
| Aparallelepiped |      | isasetoftheformu+\mathcal{P}(v                   |      |      |     | ,…,v    | )forsomeu\in\mathcal{V}. |          | The |
|                 |      |                                        |      |      |     | 1       | n            |          |     |
| vectorsv        | ,…,v | arecalledtheedgesofthisparallelepiped. |      |      |     |         |              |          |     |
1 n
| 7.103 | example:          | parallelepipeds |     |     |     |                      |     |     |     |
| ----- | ----------------- | --------------- | --- | --- | --- | -------------------- | --- | --- | --- |
|       | Theparallelepiped |                 |     |     |     | Aparallelepipedin\mathbf{R}3. |     |     |     |
$$(0.3,0.5)+\mathcal{P}((1,0),(1,1))in\mathbf{R}2.$$

290 Chapter 7 Operatorson Inner Product Spaces
7.104 invertibleoperatortakesparallelepipedstoparallelepipeds
Supposeu\in\mathcal{V},v ,…,v isabasisof\mathcal{V},and\mathcal{T} \inℒ(\mathcal{V})isinvertible. Then
1 n
\mathcal{T}(u+\mathcal{P}(v ,…,v ))=\mathcal{T}u+\mathcal{P}(\mathcal{T}v ,…,\mathcal{T}v ).
1 n 1 n
Proof Because\mathcal{T} isinvertible,thelist\mathcal{T}v ,…,\mathcal{T}v isabasisof\mathcal{V}. Thelinearity
1 n
of\mathcal{T} impliesthat
\mathcal{T}(u+a v +⋯+a v )=\mathcal{T}u+a \mathcal{T}v +⋯+a \mathcal{T}v
1 1 n n 1 1 n n
foralla ,…,a \in(0,1). Thus\mathcal{T}(u+\mathcal{P}(v ,…,v ))=\mathcal{T}u+\mathcal{P}(\mathcal{T}v ,…,\mathcal{T}v ).
1 n 1 n 1 n
Justastherectanglesaredistinguishedamongtheparallelogramsin\mathbf{R}2,we
giveaspecialnametotheparallelepipedsin\mathcal{V} whosedefiningedgesareorthogonaltoeachother.
**7.105 定义：** box
Aboxin\mathcal{V} isasetoftheform
u+\mathcal{P}(r e ,…,r e ),
1 1 n n
where u \in \mathcal{V} and r ,…,r are positive numbers and e ,…,e is an ortho1 n 1 n
normalbasisof\mathcal{V}.
Notethatinthespecialcaseof\mathbf{R}2eachboxisarectangle,buttheterminology
boxcanbeusedinalldimensions.
**7.106 例：** boxes
Thebox(1,0)+\mathcal{P}(\sqrt2e ,\sqrt2e ),where Thebox\mathcal{P}(e ,2e ,e ),wheree ,e ,e
1 2 1 2 3 1 2 3
$$e =( 1 , 1 )ande =(- 1 , 1 ). isthestandardbasisof \mathbf{R}3.$$
1 \sqrt2 \sqrt2 2 \sqrt2 \sqrt2
Suppose \mathcal{T} \in ℒ(\mathcal{V}) is invertible. Then \mathcal{T} maps every parallelepiped in \mathcal{V}
to a parallelepiped in \mathcal{V} (by 7.104). In particular, \mathcal{T} maps every boxin \mathcal{V} to a
parallelepipedin\mathcal{V}. Thisraisesthequestionofwhether\mathcal{T} mapssomeboxesin
\mathcal{V} toboxesin\mathcal{V}. Thefollowingresultanswersthisquestion,withthehelpofthe
singularvaluedecomposition.

Section7F Consequencesof Singular Value Decomposition 291
7.107 everyinvertibleoperatortakessomeboxestoboxes
Suppose\mathcal{T} \inℒ(\mathcal{V})isinvertible. Suppose\mathcal{T}hassingularvaluedecomposition
\mathcal{T}v=s \langlev,e \ranglef +⋯+s \langlev,e \ranglef ,
1 1 1 n n n
where s ,…,s are the singular values of \mathcal{T} and e ,…,e and f ,…, f are
1 n 1 n 1 n
orthonormalbasesof\mathcal{V} andtheequationaboveholdsforallv\in\mathcal{V}. Then\mathcal{T}
mapstheboxu+\mathcal{P}(r e ,…,r e )ontothebox\mathcal{T}u+\mathcal{P}(r s f ,…,r s f )for
1 1 n n 1 1 1 n n n
allpositivenumbersr ,…,r andallu\in\mathcal{V}.
1 n
Proof Ifa ,…,a \in(0,1)andr ,…,r arepositivenumbersandu\in\mathcal{V},then
1 n 1 n
\mathcal{T}(u+a r e +⋯+a r e )=\mathcal{T}u+a r s f +⋯+a r s f .
1 1 1 n n n 1 1 1 1 n n n n
Thus\mathcal{T}(u+\mathcal{P}(r e ,…,r e ))=\mathcal{T}u+\mathcal{P}(r s f ,…,r s f ).
1 1 n n 1 1 1 n n n
Volume via Singular Values
Ourgoalinthissubsectionistounderstandhowanoperatorchangesthevolume
ofsubsetsofitsdomain. Becausenotionsofvolumebelongtoanalysisrather
thantolinearalgebra,wewillworkonlywithanintuitivenotionofvolume. Our
intuitiveapproachtovolumecanbeconvertedintoappropriatecorrectdefinitions,
correctstatements,andcorrectproofsusingthemachineryofanalysis.
Ourintuitionaboutvolumeworksbestinrealinnerproductspaces. Thusthe
assumptionthat\mathbf{F} =\mathbf{R} willappearfrequentlyintherestofthissubsection.
If dim\mathcal{V} = n, then by volume we will mean n-dimensional volume. You
shouldbefamiliarwiththisconceptin\mathbf{R}3. Whenn=2,thisisusuallycalledarea
insteadofvolume,butforconsistencyweusethewordvolumeinalldimensions.
Themostfundamentalintuitionaboutvolumeisthatthevolumeofabox(whose
definingedgesarebydefinitionorthogonaltoeachother)istheproductofthe
lengthsofthedefiningedges. Thuswemakethefollowingdefinition.
**7.108 定义：** volumeofabox
Suppose\mathbf{F} =\mathbf{R}. Ifu\in\mathcal{V} andr ,…,r arepositivenumbersande ,…,e is
1 n 1 n
anorthonormalbasisof\mathcal{V},then
volume(u+\mathcal{P}(r e ,…,r e ))=r \times⋯\timesr .
1 1 n n 1 n
Thedefinitionaboveagreeswiththefamiliarformulasforthearea(whichwe
arecallingthevolume)ofarectanglein\mathbf{R}2andforthevolumeofaboxin\mathbf{R}3. For
example,thefirstboxin Example7.106hastwo-dimensionalvolume(orarea)2
becausethedefiningedgesofthatboxhavelength\sqrt2and\sqrt2. Thesecondbox
in Example7.106hasthree-dimensionalvolume2becausethedefiningedgesof
thatboxhavelength1,2,and1.

| --- | -------- | --- | ----------------------------- | --- | --- | --- | --- |
| To  | define | the volume | of  | a subset | of  | \mathcal{V}, approximate | the |
| --- | ------ | ---------- | --- | -------- | --- | -------------- | --- |
subsetbyafinitecollectionofdisjointboxes,andthenaddup
| thevolumesoftheapproximatingcollectionofboxes. |     |     |     |                                |     |     | Aswe |
| ---------------------------------------------- | --- | --- | --- | ------------------------------ | --- | --- | ---- |
| approximateasubsetof\mathcal{V}                          |     |     |     | moreaccuratelybydisjointunions |     |     |      |
ofmoreboxes,wegetabetterapproximationtothevolume.
Volumeofthis
isdefinedbyapproximatingtheareaunderacurvebyadisjoint ball\approxsumofthe
collectionofrectangles. Thisdiscussionleadstothefollowing volumesofthe
| nonrigorousbutintuitivedefinition. |             |         |     |                                      |     |     | fiveboxes. |
| ---------------------------------- | ----------- | ------- | --- | ------------------------------------ | --- | --- | ---------- |
| 7.109                              | definition: | volume  |     |                                      |     |     |            |
| Suppose\mathbf{F}                           | =\mathbf{R}          | and\Omega\subseteq\mathcal{V}. |     | Thenthevolumeof\Omega,denotedbyvolume\Omega,is |     |     |            |
approximatelythesumofthevolumesofacollectionofdisjointboxesthat
approximate\Omega.
Weareignoringmanyreasonablequestionsbytakinganintuitiveapproachto
volume. Forexample,ifweapproximate\Omegabyboxeswithrespecttoonebasis,
do we get the same volume if we approximate \Omega by boxes with respect to a
differentbasis? If\Omega and\Omega aredisjointsubsetsof\mathcal{V},isvolume(\Omega \cup\Omega ) =
|     |     |     | 1   | 2   |     |     | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
volume\Omega +volume\Omega ? Providedthatweconsideronlyreasonablynicesubsets
| --- | --- | --- | --- | --- | --- | --- | --- |
of \mathcal{V}, techniques of analysis show that both these questions have affirmative
answersthatagreewithourintuitionaboutvolume.
| 7.110              | example: | volumechangebyalinearmap |                        |     |          |     |     |
| ------------------ | -------- | ------------------------ | ---------------------- | --- | -------- | --- | --- |
| Suppose            |          | that \mathcal{T}                   | \in ℒ(\mathbf{R}2)                | is  | defined  | by  |     |
| \mathcal{T}v =2\langlev,e          | \ranglee       | +\langlev,e                    | \ranglee ,wheree             |     | ,e isthe |     |     |
|                    | 1        | 1                        | 2 2                    |     | 1 2      |     |     |
| standardbasisof\mathbf{R}2. |          |                          | Thislinearmapstretches |     |          |     |     |
| vectorsalongthee   |          | -axisbyafactorof2and     |                        |     |          |     |     |
| leaves | vectors | along | the e | -axis | unchanged. |     |     |
| ------ | ------- | ----- | ----- | ----- | ---------- | --- | --- |
The ball approximated by five boxes above Eachboxherehastwicethewidth
getsmappedby\mathcal{T} totheellipsoidshownhere. andthesameheightastheboxesin
Each of the five boxes in the original figure thepreviousfigure.
getsmappedtoaboxoftwicethewidthandthesameheightasintheoriginal
figure. Henceeachboxgetsmappedtoaboxoftwicethevolume(area)asinthe
originalfigure. Thesumofthevolumesofthefivenewboxesapproximatesthe
volumeoftheellipsoid. Thus\mathcal{T} changesthevolumeoftheballbyafactorof2.
Intheexampleabove,\mathcal{T} mapsboxeswithrespecttothebasise ,e toboxes
1 2
withrespecttothesamebasis;thuswecanseehow\mathcal{T}changesvolume. Ingeneral,
an operator maps boxes to parallelepipeds that are not boxes. However, if we
choose the right basis (coming from the singular value decomposition!), then
boxeswithrespecttothatbasisgetmappedtoboxeswithrespecttoapossibly
differentbasis,asshownin7.107. Thisobservationleadstoanaturalproofof
thefollowingresult.

| --- | --------- | ---------------------------------------- | --- | --- | --- | --- |
volumechangesbyafactoroftheproductofthesingularvalues
7.111
| Suppose\mathbf{F} | =\mathbf{R},\mathcal{T} | \inℒ(\mathcal{V})isinvertible,and\Omega\subseteq\mathcal{V}. |     |     | Then |     |
| -------- | ---- | ------------------------- | --- | --- | ---- | --- |
volume\mathcal{T}(\Omega)=(productofsingularvaluesof\mathcal{T})(volume\Omega).
| Proof                             | Suppose\mathcal{T} | hassingularvaluedecomposition |              |                         |     |                   |
| --------------------------------- | -------- | ----------------------------- | ------------ | ----------------------- | --- | ----------------- |
|                                   |          | \mathcal{T}v=s                          | \langlev,e \ranglef +⋯+s | \langlev,e                    | \ranglef  |                   |
|                                   |          |                               | 1 1 1        | n                       | n n |                   |
| forallv\in\mathcal{V},wheree                  |          | ,…,e                          | and f ,…, f  | areorthonormalbasesof\mathcal{V}. |     |                   |
|                                   |          | 1                             | n 1 n        |                         |     |                   |
| Approximate\Omegabyboxesoftheformu+\mathcal{P}(r |          |                               |              | e ,…,r                  | e   | ),whichhavevolume |
1 1 n n
r \times⋯\timesr . The operator \mathcal{T} maps each box u+\mathcal{P}(r e ,…,r e ) onto the box
| 1      | n        |                        |     |      | 1 1 | n n         |
| ------ | -------- | ---------------------- | --- | ---- | --- | ----------- |
| \mathcal{T}u+\mathcal{P}(r | s f ,…,r | s f ),whichhasvolume(s |     | \times⋯\timess |     | )(r \times⋯\timesr ). |
|        | 1 1 1    | n n n                  |     | 1    | n   | 1 n         |
Theoperator\mathcal{T}mapsacollectionofboxesthatapproximate\Omegaontoacollection
ofboxesthatapproximate\mathcal{T}(\Omega). Because\mathcal{T} changesthevolumeofeachboxina
collectionthatapproximates\Omegabyafactorofs ,thelinearmap\mathcal{T}changes
1 \times⋯\timess n
thevolumeof\Omegabythesamefactor.
\inℒ(\mathcal{V}).
| Suppose\mathcal{T}               |     | Aswewillseewhenwegettodeterminants,theproduct |               |     |                 |     |
| ---------------------- | --- | --------------------------------------------- | ------------- | --- | --------------- | --- |
| ofthesingularvaluesof\mathcal{T} |     | equals|det\mathcal{T}|;see9.60and9.61.                  |               |     |                 |     |
| Properties             | of  | an Operator                                   | as Determined | by  | Its Eigenvalues |     |
We conclude this chapter by presenting the table below. The context of this
tableisafinite-dimensionalcomplexinnerproductspace. Thefirstcolumnof
thetableshowsapropertythatanormaloperatoronsuchaspacemighthave.
Thesecondcolumnofthetableshowsasubsetof\mathbf{C} suchthattheoperatorhas
thecorrespondingpropertyifandonlyifalleigenvaluesoftheoperatorliein
thespecifiedsubset. Forexample,thefirstrowofthetablestatesthatanormal
operatorisinvertibleifandonlyifallitseigenvaluesarenonzero(thisfirstrow
istheonlyoneinthetablethatdoesnotneedthehypothesisthattheoperatoris
normal).
Make sure you can explain why all results in the table hold. For example,
thelastrowofthetableholdsbecausethenormofanoperatorequalsitslargest
singularvalue(by7.85)andthesingularvaluesofanormaloperator,assuming
\mathbf{F} =\mathbf{C},equaltheabsolutevaluesoftheeigenvalues(by Exercise7in Section7E).
|     | propertiesofanormaloperator |     |       | eigenvaluesarecontainedin |         |     |
| --- | --------------------------- | --- | ----- | ------------------------- | ------- | --- |
|     | invertible                  |     | \mathbf{C}\{0} |                           |         |     |
|     | self-adjoint                |     | \mathbf{R}     |                           |         |     |
|     | skew                        |     |       |                           | ∶Re\lambda=0} |     |
{\lambda\in\mathbf{C}
|     | orthogonalprojection |     | {0,1} |     |         |     |
| --- | -------------------- | --- | ----- | --- | ------- | --- |
|     | positive             |     | [0,\infty) |     |         |     |
|     | unitary              |     | {\lambda\in\mathbf{C}  |     | ∶|\lambda|=1} |     |
∶|\lambda|<1}
|     | normislessthan1 |     | {\lambda\in\mathbf{C} |     |     |     |
| --- | --------------- | --- | ---- | --- | --- | --- |

| -------- | ----------------------------- | --- | --- | --- | --- |
| Exercises        | 7F                           |     |     |     |     |
| ---------------- | ---------------------------- | --- | --- | --- | --- |
| 1 Provethatif\mathcal{S},\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}),then∣‖\mathcal{S}‖-‖\mathcal{T}‖∣\leq‖\mathcal{S}-\mathcal{T}‖. |     |     |     |     |
Theinequalityaboveiscalledthereversetriangleinequality.
2 Suppose that \mathcal{T} \in ℒ(\mathcal{V}) is self-adjoint or that \mathbf{F} = \mathbf{C} and \mathcal{T} \in ℒ(\mathcal{V}) is
| normal.    | Provethat      |                      |     |     |     |
| ---------- | -------------- | -------------------- | --- | --- | --- |
|            | ‖\mathcal{T}‖=max{|\lambda|∶   | \lambdaisaneigenvalueof\mathcal{T}}. |     |     |     |
| 3 Suppose\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W})andv\in\mathcal{V}. | Provethat            |     |     |     |
∗ \mathcal{T}v=‖\mathcal{T}‖2v.
|            | ‖\mathcal{T}v‖=‖\mathcal{T}‖‖v‖                 | ⟺   | \mathcal{T}              |     |     |
| ---------- | --------------------------- | --- | -------------- | --- | --- |
| 4 Suppose\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}),v\in\mathcal{V},and‖\mathcal{T}v‖=‖\mathcal{T}‖‖v‖. |     | Provethatifu\in\mathcal{V} |     | and |
\langleu,v\rangle=0,then\langle\mathcal{T}u,\mathcal{T}v\rangle=0.
5 Suppose\mathcal{U} isafinite-dimensionalinnerproductspace,\mathcal{T} \inℒ(\mathcal{V},\mathcal{U}),and
| \mathcal{S}\inℒ(\mathcal{U},\mathcal{W}). | Provethat |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- |
‖\mathcal{S}\mathcal{T}‖\leq‖\mathcal{S}‖‖\mathcal{T}‖.
| 6 Proveorgiveacounterexample:        |     | If\mathcal{S},\mathcal{T} \inℒ(\mathcal{V}),then‖\mathcal{S}\mathcal{T}‖=‖\mathcal{T}\mathcal{S}‖. |                      |     |     |
| ------------------------------------ | --- | -------------------------- | -------------------- | --- | --- |
| 7 Showthatdefiningd(\mathcal{S},\mathcal{T})=‖\mathcal{S}-\mathcal{T}‖for\mathcal{S},\mathcal{T} |     |                            | \inℒ(\mathcal{V},\mathcal{W})makesdametric |     |     |
onℒ(\mathcal{V},\mathcal{W}).
Thisexerciseisintendedforreaderswhoarefamiliarwithmetricspaces.
| 8 (a) Provethatif\mathcal{T}  | \inℒ(\mathcal{V})and‖\mathcal{I}-\mathcal{T}‖<1,then\mathcal{T} |                | isinvertible. |        |     |
| ------------------- | --------------------- | -------------- | ------------- | ------ | --- |
|                     | ℒ(\mathcal{V})                  |                |               | ℒ(\mathcal{V})   |     |
| (b) Suppose         | that \mathcal{S} \in              | is invertible. | Prove that    | if \mathcal{T} \in | and |
| ‖\mathcal{S}-\mathcal{T}‖<1/∥\mathcal{S}-1∥,then\mathcal{T} |                       | isinvertible.  |               |        |     |
Thisexerciseshowsthatthesetofinvertibleoperatorsinℒ(\mathcal{V})isanopen
subsetofℒ(\mathcal{V}),usingthemetricdefinedin Exercise7.
9 Suppose\mathcal{T} \in ℒ(\mathcal{V}). Provethatforevery\epsilon > 0,thereexistsaninvertible
operator\mathcal{S}\inℒ(\mathcal{V})suchthat0<‖\mathcal{T}-\mathcal{S}‖<\epsilon.
10 Supposedim\mathcal{V} > 1and\mathcal{T} \in ℒ(\mathcal{V})isnotinvertible. Provethatforevery
\epsilon > 0, there exists \mathcal{S} \in ℒ(\mathcal{V}) such that 0 < ‖\mathcal{T} - \mathcal{S}‖ < \epsilon and \mathcal{S} is not
invertible.
11 Suppose\mathbf{F} = \mathbf{C} and\mathcal{T} \in ℒ(\mathcal{V}). Provethatforevery\epsilon > 0thereexistsa
diagonalizableoperator\mathcal{S}\inℒ(\mathcal{V})suchthat0<‖\mathcal{T}-\mathcal{S}‖<\epsilon.
Showthat∥\sqrt\mathcal{T}∥=\sqrt‖\mathcal{T}‖.
| 12 Suppose\mathcal{T}   | \inℒ(\mathcal{V})isapositiveoperator.  |     |          |     |     |
| ------------- | -------------------------- | --- | -------- | --- | --- |
| 13 Suppose\mathcal{S},\mathcal{T} | \inℒ(\mathcal{V})arepositiveoperators. |     | Showthat |     |     |
‖\mathcal{S}-\mathcal{T}‖\leqmax{‖\mathcal{S}‖,‖\mathcal{T}‖}\leq‖\mathcal{S}+\mathcal{T}‖.
14 Suppose\mathcal{U} and\mathcal{W} aresubspacesof\mathcal{V} suchthat‖\mathcal{P} -\mathcal{P} ‖<1. Provethat
|      |        |     | \mathcal{U}   | \mathcal{W}   |     |
| ---- | ------ | --- | --- | --- | --- |
| dim\mathcal{U} | =dim\mathcal{W}. |     |     |     |     |

| --- | --------- | --- | ---------------------------------------- | --- | --- | --- | --- |
\inℒ(\mathbf{F}3)by
15 Define\mathcal{T}
|                                                  |     |     |       | ,z ,z    | ,2z | ,3z     |     |
| ------------------------------------------------ | --- | --- | ----- | -------- | --- | ------- | --- |
|                                                  |     |     | \mathcal{T}(z 1 | 2 3 )=(z | 3   | 1 2 ).  |     |
| Find(explicitly)aunitaryoperator\mathcal{S}\inℒ(\mathbf{F}3)suchthat\mathcal{T} |     |     |       |          |     | =\mathcal{S}\sqrt\mathcal{T}∗\mathcal{T}. |     |
Suppose\mathcal{S}\inℒ(\mathcal{V})isapositiveinvertibleoperator.
| 16  |     |     |     |     |     | Provethatthereexists |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- |
\delta > 0 such that \mathcal{T} is a positive operator for every self-adjoint operator
\mathcal{T} \inℒ(\mathcal{V})with‖\mathcal{S}-\mathcal{T}‖<\delta.
17 Prove that if u \in \mathcal{V} and \phi is the linear functional on \mathcal{V} defined by the
u
| equation\phi |     | (v)=\langlev,u\rangle,then‖\phi |     | ‖=‖u‖. |     |     |     |
| --------- | --- | ---------------- | --- | ------ | --- | --- | --- |
|           |     | u                |     | u      |     |     |     |
Herewearethinkingofthescalarfield\mathbf{F}asaninnerproductspacewith
\langle\alpha,\beta\rangle=\alpha\betaforall\alpha,\beta\in\mathbf{F}.
|     |     |     |     | Thus‖\phi | u ‖meansthenormof | \phi u | asalinear |
| --- | --- | --- | --- | ------ | ----------------- | --- | --------- |
mapfrom\mathcal{V}to\mathbf{F}.
| 18 Supposee |     | ,…,e | isanorthonormalbasisof\mathcal{V} |     |     | and\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). |     |
| ----------- | --- | ---- | ----------------------- | --- | --- | ------------- | --- |
|             | 1   |      | n                       |     |     |               |     |
‖2)1/2.
| (a) | Provethatmax{‖\mathcal{T}e |     | ‖,…,‖\mathcal{T}e | ‖}\leq‖\mathcal{T}‖\leq(‖\mathcal{T}e |     | ‖2+⋯+‖\mathcal{T}e |     |
| --- | ---------------- | --- | ------- | ----------- | --- | -------- | --- |
|     |                  |     | 1       | n           |     | 1        | n   |
$$(b) Provethat‖\mathcal{T}‖=(‖\mathcal{T}e ‖2+⋯+‖\mathcal{T}e ‖2)1/2ifandonlyifdimrange\mathcal{T} \leq1.$$
|     |     |     | 1   |     | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Here e ,…,e is an arbitrary orthonormal basis of \mathcal{V}, not necessarily
1 n
connectedwithasingularvaluedecompositionof \mathcal{T}. If s ,…,s isthelist
|     |     |     |     |     |     | 1   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- |
ofsingularvaluesof \mathcal{T},thentherightsideoftheinequalityaboveequals
$$(s2+⋯+s2)1/2,aswasshownin Exercise11(a)in Section7E.$$
1 n
| 19 Provethatif\mathcal{T} |     | \inℒ(\mathcal{V},\mathcal{W}),then∥\mathcal{T} |     | ∗   | \mathcal{T}∥=‖\mathcal{T}‖2. |     |     |
| --------------- | --- | -------------- | --- | --- | -------- | --- | --- |
Thisformulafor∥\mathcal{T} ∗ \mathcal{T}∥leadstotheimportantsubjectof \mathcal{C} ∗-algebras.
20 Suppose\mathcal{T} \in ℒ(\mathcal{V})isnormal. Provethat∥\mathcal{T}k∥ = ‖\mathcal{T}‖k foreverypositive
integerk.
Provethatthenormonℒ(\mathcal{V},\mathcal{W})does
| 21 Supposedim\mathcal{V} |     | >1anddim\mathcal{W} |     | >1. |     |     |     |
| -------------- | --- | --------- | --- | --- | --- | --- | --- |
notcomefromaninnerproduct. Inotherwords,provethattheredoesnot
existaninnerproductonℒ(\mathcal{V},\mathcal{W})suchthat
|         |          | max{‖\mathcal{T}v‖∶v\in\mathcal{V} |     | and‖v‖\leq1}=\sqrt\langle\mathcal{T},\mathcal{T}\rangle |     |     |     |
| ------- | -------- | ------------ | --- | ---------------- | --- | --- | --- |
| forall\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}). |              |     |                  |     |     |     |
22 Suppose \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Let n = dim\mathcal{V} and let s \geq ⋯ \geq s denote the
|                    |         |     |                |     |         | 1          | n     |
| ------------------ | ------- | --- | -------------- | --- | ------- | ---------- | ----- |
| singularvaluesof\mathcal{T}. |         |     | Provethatif1\leqk |     | \leqn,then |            |       |
|                    | min{‖\mathcal{T}| | ‖∶\mathcal{U} | isasubspaceof\mathcal{V} |     | with    | dim\mathcal{U} =k}=s | .     |
|                    |         | \mathcal{U}   |                |     |         |            | n-k+1 |
23 Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Showthat\mathcal{T} isuniformlycontinuouswithrespect
| tothemetricson\mathcal{V} |     |     | and\mathcal{W} | thatarisefromthenormsonthosespaces(see |     |     |     |
| --------------- | --- | --- | ---- | -------------------------------------- | --- | --- | --- |
Exercise23in Section6B).
| 24 Suppose\mathcal{T} |     | \inℒ(\mathcal{V})isinvertible. |     | Provethat |     |     |     |
| ----------- | --- | ------------------ | --- | --------- | --- | --- | --- |
\mathcal{T}
|     |     | ∥\mathcal{T}-1∥=‖\mathcal{T}‖-1 |     | ⟺   | isaunitaryoperator. |     |     |
| --- | --- | ----------- | --- | --- | ------------------- | --- | --- |
‖\mathcal{T}‖

| -------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
25 Fix u,x \in \mathcal{V} with u \neq 0. Define \mathcal{T} \in ℒ(\mathcal{V}) by \mathcal{T}v = \langlev,u\ranglex for every
| v\in\mathcal{V}. | Provethat |     |     |     |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
‖x‖
|     |     |     | \sqrt\mathcal{T}∗\mathcal{T}v= |     | \langlev,u\rangleu |     |     |     |     |
| --- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- |
‖u‖
foreveryv\in\mathcal{V}.
26 Suppose\mathcal{T} \in ℒ(\mathcal{V}). Provethat\mathcal{T} isinvertibleifandonlyifthereexistsa
| uniqueunitaryoperator\mathcal{S}\inℒ(\mathcal{V})suchthat\mathcal{T} |                         |     |      |                            |          | =\mathcal{S}\sqrt\mathcal{T}∗\mathcal{T}. |     |      |      |
| ------------------------------------ | ----------------------- | --- | ---- | -------------------------- | -------- | ------- | --- | ---- | ---- |
|                                      | \inℒ(\mathcal{V})ands               |     | ,…,s |                            |          |         |     |      | ,…,e |
| 27 Suppose\mathcal{T}                          |                         |     | 1    | n arethesingularvaluesof\mathcal{T}. |          |         |     | Lete | 1 n  |
| and f ,…,                            | f beorthonormalbasesof\mathcal{V} |     |      |                            | suchthat |         |     |      |      |
1 n
|            |                | \mathcal{T}v=s | \langlev,e    | \ranglef  | +⋯+s    | \langlev,e | \ranglef  |     |     |
| ---------- | -------------- | ---- | ------- | --- | ------- | ---- | --- | --- | --- |
|            |                |      | 1       | 1 1 |         | n n  | n   |     |     |
| forallv\in\mathcal{V}. | Define\mathcal{S}\inℒ(\mathcal{V})by |      |         |     |         |      |     |     |     |
|            |                |      | \mathcal{S}v=\langlev,e | \ranglef  | +⋯+\langlev,e | \ranglef   | .   |     |     |
|            |                |      |         | 1 1 |         | n    | n   |     |     |
-1|,…,|s
| (a) Showthat\mathcal{S}isunitaryand‖\mathcal{T}-\mathcal{S}‖=max{|s          |     |     |     |     |     |     |     | -1|}. |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
|                                                |     |     |     |     |     | 1   |     | n     |     |
| (b) Showthatif\mathcal{E}\inℒ(\mathcal{V})isunitary,then‖\mathcal{T}-\mathcal{E}‖\geq‖\mathcal{T}-\mathcal{S}‖. |     |     |     |     |     |     |     |       |     |
Thisexercisefindsaunitaryoperator\mathcal{S}thatisascloseaspossible(among
theunitaryoperators)toagivenoperator\mathcal{T}.
28 Suppose\mathcal{T} \in ℒ(\mathcal{V}). Provethatthereexistsaunitaryoperator\mathcal{S} \in ℒ(\mathcal{V})
| suchthat\mathcal{T}   | =\sqrt\mathcal{T}\mathcal{T}∗\mathcal{S}. |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 29 Suppose\mathcal{T} | \inℒ(\mathcal{V}).  |     |     |     |     |     |     |     |     |
$$(a) Usethepolardecompositiontoshowthatthereexistsaunitaryoperator$$
|                            |     |        | ∗                           | ∗                     | ∗                            |     |     |     |         |
| -------------------------- | --- | ------ | --------------------------- | --------------------- | ---------------------------- | --- | --- | --- | ------- |
| \mathcal{S}\inℒ(\mathcal{V})suchthat\mathcal{T}\mathcal{T}           |     |        |                             | =\mathcal{S}\mathcal{T}                   | \mathcal{T}\mathcal{S} .                         |     |     |     |         |
| (b) Showhow(a)impliesthat\mathcal{T} |     |        |                             | and\mathcal{T}                  | ∗ havethesamesingularvalues. |     |     |     |         |
|                            |     | ℒ(\mathcal{V}),\mathcal{S} | ℒ(\mathcal{V})isaunitaryoperator,and\mathcal{R} |                       |                              |     |     |     | ℒ(\mathcal{V})isa |
| 30 Suppose\mathcal{T}                | \in   |        | \in                           |                       |                              |     |     | \in   |         |
| positiveoperatorsuchthat\mathcal{T}  |     |        |                             | =\mathcal{S}\mathcal{R}. Provethat\mathcal{R}=\sqrt\mathcal{T}∗\mathcal{T}. |                              |     |     |     |         |
Thisexerciseshowsthatifwewrite\mathcal{T}astheproductofaunitaryoperator
and a positive operator (as in the polar decomposition 7.93), then the
positiveoperatorequals\sqrt\mathcal{T}∗\mathcal{T}.
31 Suppose\mathbf{F} =\mathbf{C} and\mathcal{T} \inℒ(\mathcal{V})isnormal. Provethatthereexistsaunitary
|                         |     |     |     | =\mathcal{S}\sqrt\mathcal{T}∗\mathcal{T} | andsuchthat\mathcal{S}and\sqrt\mathcal{T}∗\mathcal{T} |     |     |     |      |
| ----------------------- | --- | --- | --- | ------ | ------------------- | --- | --- | --- | ---- |
| operator\mathcal{S}\inℒ(\mathcal{V})suchthat\mathcal{T} |     |     |     |        |                     |     |     |     | both |
havediagonalmatriceswithrespecttothesameorthonormalbasisof\mathcal{V}.
| Supposethat\mathcal{T} |     | ℒ(\mathcal{V},\mathcal{W})and\mathcal{T} |     |     | 0. Lets | ,…,s | denotethepositive |     |     |
| ------------ | --- | ---------- | --- | --- | ------- | ---- | ----------------- | --- | --- |
| 32           |     | \in          |     | \neq   |         | 1    | m                 |     |     |
singularvaluesof\mathcal{T}. Showthatthereexistsanorthonormalbasise ,…,e
|            |          |     |     |      |     |     |     |     | 1 m |
| ---------- | -------- | --- | --- | ---- | --- | --- | --- | --- | --- |
| of(null\mathcal{T})⟂ | suchthat |     |     |      |     |     |     |     |     |
|            |          |     |     | e    | e   |     |     |     |     |
|            |          |     |     | 1,…, | m)) |     |     |     |     |
\mathcal{T}(\mathcal{E}(
|                       |     |     |                       | s   | s   |     |     |     |     |
| --------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
|                       |     |     |                       | 1   | m   |     |     |     |     |
| equalstheballinrange\mathcal{T} |     |     | ofradius1centeredat0. |     |     |     |     |     |     |
