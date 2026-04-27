---
title: Chapter 4
source: Clippings/LADR4e.pdf
created: 2026-04-23
type: chapter
tags:
  - book
  - chapter
---

# Chapter 4
Polynomials
This chapter contains material on polynomials that we will use to investigate
linearmapsfromavectorspacetoitself. Manyresultsinthischapterwillalready
befamiliartoyoufromothercourses;theyareincludedhereforcompleteness.
Becausethischapterisnotaboutlinearalgebra,yourinstructormaygothrough
itrapidly. Youmaynotbeaskedtoscrutinizealltheproofs. Makesure,however,
thatyouatleastreadandunderstandthestatementsofallresultsinthischaptertheywillbeusedinlaterchapters.
This chapter begins with a brief discussion of algebraic properties of the
complexnumbers. Thenweprovethatanonconstantpolynomialcannothave
more zeros than its degree. We also give a linear-algebra-based proof of the
divisionalgorithmforpolynomials,whichisworthreadingevenifyouarealready
familiarwithaproofthatdoesnotuselinearalgebra.
Aswewillsee,thefundamentaltheoremofalgebraleadstoafactorizationof
everypolynomialintodegree-onefactorsifthescalarfieldis\mathbf{C} ortofactorsof
degreeatmosttwoifthescalarfieldis\mathbf{R}.
standingassumptionforthischapter
• \mathbf{F} denotes\mathbf{R} or\mathbf{C}.
Alireza Javaheri CCBY
Statueofmathematicianandpoet Omar Khayyam(1048–1131),whosealgebra
bookwrittenin1070containedthefirstseriousstudyofcubicpolynomials.

| -------- | ----------- | --- |
Beforediscussingpolynomialswithcomplexorrealcoefficients,weneedto
learnabitmoreaboutthecomplexnumbers.
| 4.1 definition: | realpart,Rez,imaginarypart,Imz |     |
| --------------- | ------------------------------ | --- |
Supposez=a+bi,whereaandbarerealnumbers.
| • Therealpart      | ofz,denotedby Rez,isdefinedby Rez=a. |     |
| ------------------ | ---------------------------------- | --- |
| • Theimaginarypart | ofz,denotedby Imz,isdefinedby Imz=b. |     |
Thusforeverycomplexnumberz,wehave
$$z=Rez+(Imz)i.$$
| 4.2 definition: | complexconjugate,z,absolutevalue,|z| |     |
| --------------- | ------------------------------------ | --- |
Supposez\in\mathbf{C}.
• Thecomplexconjugateofz\in\mathbf{C},denotedbyz,isdefinedby
$$z=Rez-(Imz)i.$$
• Theabsolutevalueofacomplexnumberz,denotedby|z|,isdefinedby
|z|=\sqrt(Rez)2+(Imz)2.
**4.3 例：** realandimaginarypart,complexconjugate,absolutevalue
| Supposez=3+2i. | Then |     |
| -------------- | ---- | --- |
• Rez=3and Imz=2;
• z=3-2i;
| • |z|=\sqrt32+22 | =\sqrt13. |     |
| ------------ | ----- | --- |
withtheorderedpair(Rez,Imz)\in\mathbf{R}2
Identifyingacomplexnumberz\in\mathbf{C}
identifies \mathbf{C} with \mathbf{R}2. Note that \mathbf{C} is a one-dimensional complex vector space,
$$(identifiedwith\mathbf{R}2)asatwo-dimensionalrealvector$$
butwecanalsothinkof\mathbf{C}
space.
Theabsolutevalueofeachcomplexnumberisanonnegativenumber. Specifically, if z \in \mathbf{C}, then |z| equals the distance from the origin in \mathbf{R}2 to the point
$$(Rez,Imz)\in\mathbf{R}2.$$
| -------- | ------------- | ----------- |
Youshouldverifythatz=zifandonly
plexconjugate,andabsolutevaluehave if zisarealnumber.
| the properties | listed in | the following |
| -------------- | --------- | ------------- |
multipartresult.

Chapter 4 Polynomials 121
4.4 propertiesofcomplexnumbers
Supposew,z\in\mathbf{C}. Thenthefollowingequalitiesandinequalitieshold.
sumofzandz
z+z=2Rez.
differenceofzandz
z-z=2(Imz)i.
productofzandz
zz=|z|2.
additivityandmultiplicativityofcomplexconjugate
w+z=w+zandwz=wz.
doublecomplexconjugate
$$z=z.$$
realandimaginarypartsareboundedby|z|
|Rez|\leq|z|and|Imz|\leq|z|.
absolutevalueofthecomplexconjugate
∣z∣=|z|.
multiplicativityofabsolutevalue
|wz|=|w||z|.
triangleinequality
|w+z|\leq|w|+|z|.
Proof Except for the last item above,
Geometricinterpretationoftriangleintheroutineverificationsoftheassertions
equality: Thelengthofeachsideofa
abovearelefttothereader. Toverifythe
triangleislessthanorequaltothesum
triangleinequality,wehave ofthelengthsofthetwoothersides.
|w+z|2 =(w+z)(w+z)
=ww+zz+wz+zw
=|w|2+|z|2+wz+wz
=|w|2+|z|2+2Re(wz)
\leq|w|2+|z|2+2∣wz∣
=|w|2+|z|2+2|w||z|
=(|w|+|z|)2.
Takingsquarerootsnowgivesthedesired
See Exercise2forthereversetriangle
inequality|w+z|\leq|w|+|z|.
inequality.

| -------- | ----------- | --- | --- |
| Zeros of | Polynomials |     |     |
| -------- | ----------- | --- | --- |
Recallthatafunctionp∶
\mathbf{F} \rightarrow\mathbf{F} iscalledapolynomialofdegreemifthereexist
| a ,…,a | \in\mathbf{F} witha \neq0suchthat |          |     |
| ------ | ------------------- | -------- | --- |
| 0 m    | m                   |          |     |
|        | p(z)=a              | +a z+⋯+a | zm  |
|        |                     | 0 1      | m   |
forallz\in\mathbf{F}. Apolynomialcouldhavemorethanonedegreeiftherepresentation
ofpintheformabovewerenotunique. Ourfirsttaskistoshowthatthiscannot
happen.
Thesolutionstotheequationp(z) = 0playacrucialroleinthestudyofa
| polynomialp\in𝒫(\mathbf{F}). | Thusthesesolutionshaveaspecialname.        |     |     |
| ----------------- | ------------------------------------------ | --- | --- |
| 4.5 definition:   | zeroofapolynomial                          |     |     |
| Anumber           | iscalledazero(orroot)ofapolynomialp\in𝒫(\mathbf{F})if |     |     |
\lambda\in\mathbf{F}
p(\lambda)=0.
Thenextresultisthekeytoolthatwewillusetoshowthatthedegreeofa
polynomialisunique.
4.6 eachzeroofapolynomialcorrespondstoadegree-onefactor
| Supposemisapositiveintegerandp |     | \in 𝒫(\mathbf{F})isapolynomialofdegreem. |     |
| ------------------------------ | --- | ----------------------------- | --- |
Suppose \lambda \in \mathbf{F}. Then p(\lambda) = 0 if and only if there exists a polynomial
q\in𝒫(\mathbf{F})ofdegreem-1suchthat
|     |     | p(z)=(z- \lambda)q(z) |     |
| --- | --- | --------------- | --- |
foreveryz\in\mathbf{F}.
,a ,…,a
| Proof Firstsupposep(\lambda)=0. |     | Leta     | \in\mathbf{F} besuchthat |
| ------------------------- | --- | -------- | ------------- |
|                           |     | 0 1      | m             |
|                           |     | +a z+⋯+a | zm            |
p(z)=a
|            |      | 0 1 | m   |
| ---------- | ---- | --- | --- |
| forallz\in\mathbf{F}. | Then |     |     |
\lambda)+⋯+a (zm- \lambdam)
| 4.7 | p(z)=p(z)-p(\lambda)=a | (z- |     |
| --- | ---------------- | --- | --- |
|     |                  | 1   | m   |
\in{1,…,m},theequation
| forallz\in\mathbf{F}. | Foreachk |     |     |
| ---------- | -------- | --- | --- |
k
zk- \lambdak =(z- \lambda)\sum\lambdaj-1zk-j
$$j=1$$
showsthatzk-\lambdak
equalsz-\lambdatimessomepolynomialofdegreek-1. Thus4.7
showsthatpequalsz- \lambdatimessomepolynomialofdegreem-1,asdesired.
To prove the implication in the other direction, now suppose that there is
a polynomial q \in 𝒫(\mathbf{F}) such that p(z) = (z- \lambda)q(z) for every z \in \mathbf{F}. Then
| p(\lambda)=(\lambda- | \lambda)q(\lambda)=0,asdesired. |     |     |
| -------- | ------------------- | --- | --- |

Chapter 4 Polynomials
Nowwecanprovethatpolynomialsdonothavetoomanyzeros.
| degreemimpliesatmost |     | mzeros |     |     |
| -------------------- | --- | ------ | --- | --- |
4.8
| Supposemisapositiveintegerandp |     | \in 𝒫(\mathbf{F})isapolynomialofdegreem. |     |     |
| ------------------------------ | --- | ----------------------------- | --- | --- |
Thenphasatmostmzerosin\mathbf{F}.
Proof Wewilluseinductiononm. Thedesiredresultholdsifm=1because
ifa \neq0thenthepolynomiala +a zhasonlyonezero(whichequals-a /a ).
| 1   |     | 0 1 |     | 0 1 |
| --- | --- | --- | --- | --- |
Thusassumethatm>1andthedesiredresultholdsform-1.
| Ifphasnozerosin\mathbf{F},thenthedesiredresultholdsandwearedone. |     |     |     | Thus |
| ------------------------------------------------------- | --- | --- | --- | ---- |
suppose p has a zero \lambda \in \mathbf{F}. By 4.6, there is polynomial q \in 𝒫(\mathbf{F}) of degree
m-1suchthat
|     |     | p(z)=(z- \lambda)q(z) |     |     |
| --- | --- | --------------- | --- | --- |
foreveryz\in\mathbf{F}. Ourinductionhypothesisimpliesthatqhasatmostm-1zeros
in\mathbf{F}. Theequationaboveshowsthatthezerosofpin\mathbf{F} areexactlythezerosofq
| in\mathbf{F} alongwith | \lambda. Thusphasatmostmzerosin\mathbf{F}. |     |     |     |
| ------------- | --------------------------- | --- | --- | --- |
Theresultaboveimpliesthatthecoefficientsofapolynomialareuniquely
determined(becauseifapolynomialhadtwodifferentsetsofcoefficients,then
subtractingthetworepresentationsofthepolynomialwouldgiveapolynomial
withsomenonzerocoefficientsbutinfinitelymanyzeros). Inparticular,thedegree
ofapolynomialisuniquelydefined.
Recall that the degree of the 0 poly- The0polynomialisdeclaredtohave
| nomial is | defined to be | -\infty. When |     |     |
| --------- | ------------- | -------- | --- | --- |
degree-\inftysothatexceptionsarenot
necessary, use the expected arithmetic neededforvariousreasonableresults
| with -\infty. | For example, | -\infty < m and | deg(pq)=degp+degq. |     |
| -------- | ------------ | ---------- | ------------------ | --- |
suchas
-\infty+m=-\inftyforeveryintegerm.
| Division | Algorithm for | Polynomials |     |     |
| -------- | ------------- | ----------- | --- | --- |
If p and s are nonnegative integers, with s \neq 0, then there exist nonnegative
integersqandrsuchthat
$$p=sq+r$$
andr <s. Thinkofdividingpbys,gettingquotientqwithremainderr. Ournext
result givesan analogous result forpolynomials. Thus the nextresult is often
calledthedivisionalgorithmforpolynomials,althoughasstatedhereitisnot
reallyanalgorithm,justausefulresult.
ThedivisionalgorithmforpolynomiThinkofthedivisionalgorithmforpoly-
| als could | be proved without | using any |     |     |
| --------- | ----------------- | --------- | --- | --- |
nomialsasgivingaremainderpolynolinearalgebra. However,asisappropri- mialrwhenthepolynomialpisdivided
ateforalinearalgebratextbook,theproof
bythepolynomials.
givenhereuseslinearalgebratechniques
andmakesniceuseofabasisof𝒫 (\mathbf{F}),whichisthe(n+1)-dimensionalvector
n
| spaceofpolynomialswithcoefficientsin\mathbf{F} |     | andofdegreeatmostn. |     |     |
| ------------------------------------- | --- | ------------------- | --- | --- |

| --- | -------- | ----------- | --- | --- | --- | --- |
divisionalgorithmforpolynomials
4.9
Supposethatp,s \in 𝒫(\mathbf{F}),withs \neq 0. Thenthereexistuniquepolynomials
q,r \in𝒫(\mathbf{F})suchthat
$$p=sq+r$$
| anddegr | <degs.                 |     |     |                       |     |      |
| ------- | ---------------------- | --- | --- | --------------------- | --- | ---- |
| Proof   | Letn=degpandletm=degs. |     |     | Ifn<m,thentakeq=0andr |     | =pto |
getthedesiredequationp=sq+rwithdegr <degs. Thuswenowassumethat
n\geqm.
Thelist
1,z,…,zm-1,s,zs,…,zn-ms
4.10
islinearlyindependentin𝒫 (\mathbf{F})becauseeachpolynomialinthislisthasadifferent
n
degree. Also,thelist4.10haslengthn+1,whichequalsdim𝒫 (\mathbf{F}). Hence4.10
n
| isabasisof𝒫 | (\mathbf{F})[by2.38]. |     |     |     |     |     |
| ----------- | ------------ | --- | --- | --- | --- | --- |
n
Becausep\in𝒫 (\mathbf{F})and4.10isabasisof𝒫 (\mathbf{F}),thereexistuniqueconstants
|         |                 | n        |         | n                 |           |     |
| ------- | --------------- | -------- | ------- | ----------------- | --------- | --- |
| ,a ,…,a |                 | andb     | ,b ,…,b | suchthat          |           |     |
| a 0 1   | m-1             | \in\mathbf{F}       | 0 1 n-m | \in\mathbf{F}                |           |     |
|         |                 |          | zm-1+b  |                   | zn-ms     |     |
| 4.11    | p=a             | +a z+⋯+a |         | s+b zs+⋯+b        |           |     |
|         | 0               | 1        | m-1     | 0 1               | n-m       |     |
|         | =a⏟⏟+a⏟z⏟+⏟⋯+⏟a |          | ⏟⏟zm⏟-1 | +s(b⏟⏟+b⏟z⏟+⏟⋯+⏟b | ⏟⏟zn-⏟m). |     |
|         | 0               | 1        | m-1     | 0 1               | n-m       |     |
|         |                 |          | r       |                   | q         |     |
Withr andqasdefinedabove,weseethatpcanbewrittenasp = sq+r with
degr <degs,asdesired.
Theuniquenessofq,r \in 𝒫(\mathbf{F})satisfyingtheseconditionsfollowsfromthe
uniquenessoftheconstantsa ,a ,…,a \in\mathbf{F} andb ,b ,…,b \in\mathbf{F} satisfy-
|     |     |     | 0 1 | m-1 0 | 1 n-m |     |
| --- | --- | --- | --- | ----- | ----- | --- |
ing4.11.
| Factorization |     | of Polynomials | over | \mathbf{C}   |     |     |
| ------------- | --- | -------------- | ---- | --- | --- | --- |
Wehavebeenhandlingpolynomialswith
Thefundamentaltheoremofalgebrais
| complex | coefficients | and | polynomials |                     |              |     |
| ------- | ------------ | --- | ----------- | ------------------- | ------------ | --- |
|         |              |     |             | anexistencetheorem. | Itsproofdoes |     |
withrealcoefficientssimultaneously,let- notleadtoamethodforfindingzeros.
| ting \mathbf{F} | denote | \mathbf{R} or \mathbf{C}. | Now we will |     |     |     |
| ------ | ------ | ------- | ----------- | --- | --- | --- |
Thequadraticformulagivesthezeros
seedifferencesbetweenthesetwocases. explicitlyforpolynomialsofdegree2.
coefficients. Thenwewillusethosere- existforpolynomialsofdegree3and4.
sultstoprovecorrespondingresultsfor Nosuchformulasexistforpolynomials
ofdegree5andabove.
polynomialswithrealcoefficients.
Ourproofofthefundamentaltheorem
ofalgebraimplicitlyusestheresultthatacontinuousreal-valuedfunctionona
closeddiskin\mathbf{R}2 attainsaminimumvalue. Awebsearchcanleadyoutoseveral

Chapter 4 Polynomials
otherproofsofthefundamentaltheoremofalgebra. Theproofusing Liouville’s
theoremisparticularlyniceifyouarecomfortablewithanalyticfunctions. All
proofsofthefundamentaltheoremofalgebraneedtousesomeanalysis,because
theresultisnottrueif\mathbf{C} isreplaced,forexample,withthesetofnumbersofthe
formc+diwherec,darerationalnumbers.
fundamentaltheoremofalgebra,firstversion
4.12
Everynonconstantpolynomialwithcomplexcoefficientshasazeroin\mathbf{C}.
Proof De Moivre’stheorem,whichyoucanproveusinginductiononkandthe
addition formulas for cosine and sine, states that if k is a positive integer and
\theta \in\mathbf{R},then
|     | (cos\theta+isin\theta)k | =cosk\theta+isink\theta. |     |
| --- | ------------- | -------------- | --- |
Supposew\in\mathbf{C} andkisapositiveinteger. Usingpolarcoordinates,weknow
| thatthereexistr | \geq0and\theta \in\mathbf{R} | suchthat |     |
| --------------- | --------- | -------- | --- |
r(cos\theta+isin\theta)=w.
De Moivre’stheoremimpliesthat
k
|     | (r1/k(cos\theta | +isin\theta)) |     |
| --- | ---------- | -------- | --- |
=w.
|                               |     | k k                          |     |
| ----------------------------- | --- | ---------------------------- | --- |
| Thuseverycomplexnumberhasakth |     | root,afactthatwewillsoonuse. |     |
Supposepisanonconstantpolynomialwithcomplexcoefficientsandhighestordernonzerotermc zm. Then|p(z)|\rightarrow\inftyas|z|\rightarrow\infty(because|p(z)|/∣zm∣\rightarrow|c |
m m
as|z| \rightarrow \infty). Thusthecontinuousfunctionz ↦ |p(z)|hasaglobalminimumat
| somepoint\zeta | \in\mathbf{C}. Toshowthatp(\zeta)=0,supposethatp(\zeta)\neq0. |     |     |
| ---------- | --------------------------------------- | --- | --- |
Defineanewpolynomialqby
p(z+\zeta)
|     |     | q(z)= | .   |
| --- | --- | ----- | --- |
p(\zeta)
Thefunctionz↦|q(z)|hasaglobalminimumvalueof1atz=0. Write
|     | q(z)=1+a | zk+⋯+a | zm, |
| --- | -------- | ------ | --- |
|     |          | k      | m   |
wherekisthesmallestpositiveintegersuchthatthecoefficientofzk isnonzero;
| inotherwords,a | \neq0. |     |     |
| -------------- | --- | --- | --- |
k
Let \beta \in \mathbf{C} be such that \betak = - . There is a constant c > 1 such that if
a
k
t\in(0,1),then
|     | |q(t\beta)|\leq∣1+a | tk\betak∣+tk+1c |     |
| --- | ------------ | ----------- | --- |
k
=1-tk(1-tc).
Thustakingt tobe1/(2c)intheinequalityabove, wehave|q(t\beta)| < 1, which
contradicts the assumption that the global minimum of z ↦ |q(z)| is 1. This
contradictionimpliesthatp(\zeta)=0,showingthatphasazero,asdesired.

| -------- | --- | ----------- | --- | --- | --- | --- |
Computerscanuseclevernumericalmethodstofindgoodapproximationsto
thezerosofanypolynomial,evenwhenexactzeroscannotbefound. Forexample,
noonewillevergiveanexactformulaforazeroofthepolynomialpdefinedby
p(x)=x5-5x4-6x3+17x2+4x-7.
However, a computer can find that the zeros of p are approximately the five
| numbers-1.87, | -0.74, | 0.62, | 1.47, 5.51. |     |     |     |
| ------------- | ------ | ----- | ----------- | --- | --- | --- |
Thefirstversionofthefundamentaltheoremofalgebraleadstothefollowing
factorizationresultforpolynomialswithcomplexcoefficients. Notethatinthis
factorization,thezerosofparethenumbers \lambda ,…,\lambda ,whicharetheonlyvalues
|     |     |     |     |     | 1 m |     |
| --- | --- | --- | --- | --- | --- | --- |
ofzforwhichtherightsideoftheequationinthenextresultequals0.
4.13 fundamentaltheoremofalgebra,secondversion
Ifp\in𝒫(\mathbf{C})isanonconstantpolynomial,thenphasauniquefactorization
$$(exceptfortheorderofthefactors)oftheform$$
|          |      | p(z)=c(z- |     | \lambda )⋯(z- | \lambda ), |     |
| -------- | ---- | --------- | --- | ------- | ---- | --- |
|          |      |           |     | 1       | m    |     |
| wherec,\lambda | ,…,\lambda | \in\mathbf{C}.       |     |         |      |     |
1 m
| Proof Letp\in𝒫(\mathbf{C})andletm=degp. |     |     |     | Wewilluseinductiononm. |     | Ifm=1, |
| ---------------------------- | --- | --- | --- | ---------------------- | --- | ------ |
thenthedesiredfactorizationexistsandisunique. Soassumethatm>1andthat
thedesiredfactorizationexistsandisuniqueforallpolynomialsofdegreem-1.
Firstwewillshowthatthedesiredfactorizationofpexists. Bythefirstversion
ofthefundamentaltheoremofalgebra(4.12),phasazero \lambda\in\mathbf{C}. By4.6,there
isapolynomialqofdegreem-1suchthat
|     |     |     | p(z)=(z- | \lambda)q(z) |     |     |
| --- | --- | --- | -------- | ------ | --- | --- |
forallz\in\mathbf{C}. Ourinductionhypothesisimpliesthatqhasthedesiredfactorization,
whichwhenpluggedintotheequationabovegivesthedesiredfactorizationofp.
Nowweturntothequestionofuniqueness. Thenumbercisuniquelydeterminedasthecoefficientofzm inp. Soweonlyneedtoshowthatexceptforthe
| order,thereisonlyonewaytochoose |     |         |     | \lambda ,…,\lambda | . If     |     |
| ------------------------------- | --- | ------- | --- | ------ | -------- | --- |
|                                 |     |         |     | 1      | m        |     |
|                                 | (z- | \lambda )⋯(z- | \lambda   | )=(z-\tau | )⋯(z-\tau ) |     |
|                                 |     | 1       | m   |        | 1 m      |     |
for all z \in \mathbf{C}, then because the left side of the equation above equals 0 when
$$z = \lambda ,oneofthe\tau’sontherightsideequals \lambda . Relabeling,wecanassume$$
| --- | --- | --- | --- | --- | --- | --- |
that\tau = \lambda . Nowifz\neq \lambda ,wecandividebothsidesoftheequationaboveby
| 1 1 |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
z- \lambda ,getting
|     | (z- | \lambda )⋯(z- | \lambda   | )=(z-\tau | )⋯(z-\tau ) |     |
| --- | --- | ------- | --- | ------ | -------- | --- |
|     |     | 2       | m   |        | 2 m      |     |
forallz \in \mathbf{C} exceptpossiblyz = \lambda . Actuallytheequationaboveholdsforall
z\in\mathbf{C},becauseotherwisebysubtractingtherightsidefromtheleftsidewewould
getanonzeropolynomialthathasinfinitelymanyzeros. Theequationaboveand
ourinductionhypothesisimplythatexceptfortheorder,the \lambda’sarethesameas
the\tau’s,completingtheproofofuniqueness.

| --- | --- | --- | --- | --- | -------- | --- | ----------- | --- | --- |
| Factorization |     | of Polynomials |     | over |     |     |     |     |     |
| ------------- | --- | -------------- | --- | ---- | --- | --- | --- | --- | --- |
\mathbf{R}
Apolynomialwithrealcoefficientsmay
Thefailureofthefundamentaltheorem
| havenorealzeros. |     | Forexample,thepoly- |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
ofalgebrafor\mathbf{R}accountsforthediffernomial1+x2
|     | hasnorealzeros. |     |     |     | encesbetweenlinearalgebraonreal |     |     |     |     |
| --- | --------------- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- |
Toobtainafactorizationtheoremover
andcomplexvectorspaces,aswewill
| \mathbf{R},wewilluseourfactorizationtheorem |     |     |     |     | seeinlaterchapters. |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
over\mathbf{C}. Webeginwiththenextresult.
4.14 polynomialswithrealcoefficientshavenonrealzerosinpairs
| Supposep\in𝒫(\mathbf{C})isapolynomialwithrealcoefficients. |     |     |     |     |     |     | If  | isazero |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
\lambda\in\mathbf{C}
| ofp,thensois |     | \lambda.  |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |                      |     | p(z)=a | +a      | z+⋯+a | zm,         |     |      |     |
| ------ | -------------------- | --- | ------ | ------- | ----- | ----------- | --- | ---- | --- |
|        |                      |     |        | 0       | 1     | m           |     |      |     |
| wherea | ,…,a arerealnumbers. |     |        | Suppose | \lambda\in\mathbf{C}   | isazeroofp. |     | Then |     |
| 0      | m                    |     |        |         |       |             |     |      |     |
|        |                      |     | a +a   | \lambda+⋯+a   | \lambdam    | =0.         |     |      |     |
|        |                      |     | 0      | 1       | m     |             |     |      |     |
Takethecomplexconjugateofbothsidesofthisequation,obtaining
|     |     |     | a +a | \lambda+⋯+a | \lambdam  | =0, |     |     |     |
| --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- |
|     |     |     | 0    | 1     | m   |     |     |     |     |
where we have used basic properties of the complex conjugate (see 4.4). The
| equationaboveshowsthat |     |     | \lambdaisazeroofp. |     |     |     |     |     |     |
| ---------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Wewantafactorizationtheoremfor
Thinkaboutthequadraticformulain
| polynomials | with | real coefficients. |     | We  |     |     |     |     |     |
| ----------- | ---- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
connectionwiththeresultbelow.
beginwiththefollowingresult.
4.15 factorizationofaquadraticpolynomial
Supposeb,c
\in\mathbf{R}. Thenthereisapolynomialfactorizationoftheform
|        |       |               | x2+bx+c | =(x- | \lambda )(x- | \lambda   | )   |     |     |
| ------ | ----- | ------------- | ------- | ---- | ------ | --- | --- | --- | --- |
| with \lambda | ,\lambda \in\mathbf{R} | ifandonlyifb2 |         | \geq4c. |        |     |     |     |     |
|        | 1 2   |               |         |      |        |     |     |     |     |
|     |     |         |     |      | b 2    |     | b2  |     |     |
| --- | --- | ------- | --- | ---- | ------ | --- | --- | --- | --- |
|     |     | x2+bx+c |     | =(x+ | ) +(c- |     | ).  |     |     |
Firstsupposeb2
|     |     | <4c. | Thentheright |     |     |          |       |              |     |
| --- | --- | ---- | ------------ | --- | --- | -------- | ----- | ------------ | --- |
|     |     |      |              |     | The | equation | above | is the basis | of  |
sideoftheequationaboveispositivefor
|                              |         |         |                |          | the     | technique | called | completing | the |
| ---------------------------- | ------- | ------- | -------------- | -------- | ------- | --------- | ------ | ---------- | --- |
| every x                      | \in \mathbf{R}.    | Hence   | the polynomial |          | square. |           |        |            |     |
| x2 + bx                      | + c has | no real | zeros          | and thus |         |           |        |            |     |
| cannotbefactoredintheform(x- |         |         |                | \lambda        | )(x- \lambda  | )with     | \lambda ,\lambda   | \in\mathbf{R}.        |     |
|                              |         |         |                | 1        | 2       |           | 1 2    |            |     |

| --- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
nowsupposeb2
|     | Conversely, |     |     | \geq 4c. | Thenthereisarealnumberd |     |     | suchthat |
| --- | ----------- | --- | --- | ----- | ----------------------- | --- | --- | -------- |
d2 b2
|     | = -c. | Fromthedisplayedequationabove,wehave |     |     |     |     |     |     |
| --- | ----- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
b 2
|     |     | x2+bx+c |     | =(x+ | ) -d2 |     |     |     |
| --- | --- | ------- | --- | ---- | ----- | --- | --- | --- |
|     |     |     |     |      | b      | b    |     |     |
| --- | --- | --- | --- | ---- | ------ | ---- | --- | --- |
|     |     |     |     | =(x+ | +d)(x+ | -d), |     |     |
whichgivesthedesiredfactorization.
The next result gives a factorization of a polynomial over \mathbf{R}. The idea of
the proof is to use the second version of the fundamental theorem of algebra
$$(4.13),whichgivesafactorizationofpasapolynomialwithcomplexcoefficients.$$
Complexbutnonrealzerosofpcomeinpairs;see4.14. Thusifthefactorization
ofpasanelementof𝒫(\mathbf{C})includestermsoftheform(x- \lambda)with \lambdaanonreal
complexnumber,then(x- \lambda)isalsoaterminthefactorization. Multiplying
togetherthesetwoterms,weget
x2-2(Re\lambda)x+|\lambda|2,
whichisaquadratictermoftherequiredform.
The idea sketched in the paragraph above almost provides a proof of the
existence of our desired factorization. However, we need to be careful about
onepoint. Suppose \lambdaisanonrealcomplexnumberand(x- \lambda)isaterminthe
factorizationofpasanelementof𝒫(\mathbf{C}). Weareguaranteedby4.14that(x-\lambda)
alsoappearsasaterminthefactorization,but4.14doesnotstatethatthesetwo
factorsappearthesamenumberoftimes,asneededtomaketheideaabovework.
However,theproofworksaroundthispoint.
In the nextresult, either m or \mathcal{M} may equal 0. The numbers \lambda ,…,\lambda are
|     |     |     |     |     |     |     |     | 1 m |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
preciselytherealzerosofp,forthesearetheonlyrealvaluesofxforwhichthe
rightsideoftheequationinthenextresultequals0.
4.16 factorizationofapolynomialover\mathbf{R}
Supposep\in𝒫(\mathbf{R})isanonconstantpolynomial. Thenphasauniquefactorization(exceptfortheorderofthefactors)oftheform
|          | p(x)=c(x- | \lambda )⋯(x-      |     | \lambda )(x2+b | x+c       | )⋯(x2+b | x+c       | ),  |
| -------- | --------- | ------------ | --- | -------- | --------- | ------- | --------- | --- |
|          |           | 1            |     | m        | 1         | 1       | \mathcal{M}         | \mathcal{M}   |
| wherec,\lambda |           | ,…,\lambda ,b ,…,b |     | ,c ,…,c  | \in\mathbf{R},withb2 | <4c     | foreachk. |     |
|          | 1         | m 1          | \mathcal{M}   | 1        | \mathcal{M}         | k       | k         |     |
Proof Firstwewillprovethatthedesiredfactorizationexists,andafterthatwe
willprovetheuniqueness.
Thinkofpasanelementof𝒫(\mathbf{C}). Ifall(complex)zerosofparereal,then
wehavethedesiredfactorizationby4.13. Thussupposephasazero with
\lambda\in\mathbf{C}
| \lambda\notin\mathbf{R}. | By4.14, | \lambdaisazeroofp. |     | Thuswecanwrite |     |     |     |     |
| ---- | ------- | ------------ | --- | -------------- | --- | --- | --- | --- |

Chapter 4 Polynomials 129
p(x)=(x- \lambda)(x- \lambda)q(x)
=(x2-2(Re\lambda)x+|\lambda|2)q(x)
forsomepolynomialq \in 𝒫(\mathbf{C})ofdegreetwolessthanthedegreeofp. Ifwe
can prove that q has real coefficients, then using induction on the degree of p
completestheproofoftheexistencepartofthisresult.
Toprovethatqhasrealcoefficients,wesolvetheequationaboveforq,getting
p(x)
q(x)=
x2-2(Re\lambda)x+|\lambda|2
forallx \in\mathbf{R}. Theequationaboveimpliesthatq(x)\in\mathbf{R} forallx \in\mathbf{R}. Writing
q(x)=a +a x+⋯+a xn-2,
0 1 n-2
wheren=degpanda ,…,a \in\mathbf{C},wethushave
0 n-2
$$0=Imq(x)=(Ima )+(Ima )x+⋯+(Ima )xn-2$$
0 1 n-2
forallx \in \mathbf{R}. Thisimpliesthat Ima ,…,Ima allequal0(by4.8). Thusall
0 n-2
coefficientsofqarereal,asdesired. Hencethedesiredfactorizationexists.
Nowweturntothequestionofuniquenessofourfactorization. Afactorofp
oftheformx2+b x+c withb2 <4c canbeuniquelywrittenas(x-\lambda )(x-\lambda )
k k k k k k
with \lambda \in\mathbf{C}. Amoment’sthoughtshowsthattwodifferentfactorizationsofpas
k
anelementof𝒫(\mathbf{R})wouldleadtotwodifferentfactorizationsofpasanelement
of𝒫(\mathbf{C}),contradicting4.13.
Exercises 4
1 Supposew,z\in\mathbf{C}. Verifythefollowingequalitiesandinequalities.
$$(a) z+z=2Rez$$
$$(b) z-z=2(Imz)i$$
$$(c) zz=|z|2$$
$$(d) w+z=w+zandwz=wz$$
$$(e) z=z$$
$$(f) |Rez|\leq|z|and|Imz|\leq|z|$$
$$(g) ∣z∣=|z|$$
$$(h) |wz|=|w||z|$$
Theresultsabovearethepartsof4.4thatwerelefttothereader.
2 Provethatifw,z\in\mathbf{C},then∣|w|-|z|∣\leq|w-z|.
Theinequalityaboveiscalledthereversetriangleinequality.

130 Chapter 4 Polynomials
3 Suppose \mathcal{V} isacomplexvectorspaceand \phi \in \mathcal{V}′. Define \sigma∶ \mathcal{V} \rightarrow \mathbf{R} by
\sigma(v)=Re\phi(v)foreachv\in\mathcal{V}. Showthat
\phi(v)=\sigma(v)-i\sigma(iv)
forallv\in\mathcal{V}.
4 Supposemisapositiveinteger. Istheset
{0}\cup{p\in𝒫(\mathbf{F})∶degp=m}
asubspaceof𝒫(\mathbf{F})?
5 Istheset
{0}\cup{p\in𝒫(\mathbf{F})∶degpiseven}
asubspaceof𝒫(\mathbf{F})?
6 Suppose that m and n are positive integers with m \leq n, and suppose
\lambda ,…,\lambda \in \mathbf{F}. Prove that there exists a polynomial p \in 𝒫(\mathbf{F}) with
1 m
degp = n such that 0 = p(\lambda ) = ⋯ = p(\lambda ) and such that p has no
1 m
otherzeros.
7 Supposethatmisanonnegativeinteger,z ,…,z aredistinctelements
1 m+1
of \mathbf{F}, and w ,…,w \in \mathbf{F}. Prove that there exists a unique polynomial
1 m+1
p\in𝒫 (\mathbf{F})suchthat
m
p(z )=w
k k
foreachk =1,…,m+1.
Thisresultcanbeprovedwithoutusinglinearalgebra. However,trytofind
theclearer,shorterproofthatusessomelinearalgebra.
8 Supposep \in 𝒫(\mathbf{C})hasdegreem. Provethatphasmdistinctzerosifand
onlyifpanditsderivativep′ havenozerosincommon.
9 Provethateverypolynomialofodddegreewithrealcoefficientshasareal
zero.
10 Forp\in𝒫(\mathbf{R}),define\mathcal{T}p∶ \mathbf{R} \rightarrow\mathbf{R} by
⎧p(x)-p(3)
{ { ifx \neq3,
$$(\mathcal{T}p)(x)= x-3$$
⎨
{
{ ⎩p′(3) ifx =3
foreachx \in\mathbf{R}. Showthat\mathcal{T}p\in𝒫(\mathbf{R})foreverypolynomialp\in𝒫(\mathbf{R})and
alsoshowthat\mathcal{T}∶ 𝒫(\mathbf{R})\rightarrow𝒫(\mathbf{R})isalinearmap.
11 Supposep\in𝒫(\mathbf{C}). Defineq∶ \mathbf{C} \rightarrow\mathbf{C} by
q(z)=p(z)p(z).
Provethatqisapolynomialwithrealcoefficients.

| --- | --- | --- | -------- | ----------- | --- |
12 Supposemisanonnegativeintegerandp \in 𝒫 (\mathbf{C})issuchthatthereare
m
| distinctrealnumbersx |     | ,x ,…,x withp(x | )\in\mathbf{R} | foreachk | =0,1,…,m. |
| -------------------- | --- | --------------- | --- | -------- | --------- |
|                      |     | 0 1 m           | k   |          |           |
Provethatallcoefficientsofparereal.
={pq∶q\in𝒫(\mathbf{F})}.
| 13 Supposep\in𝒫(\mathbf{F})withp\neq0. |     | Let\mathcal{U}   |     |     |     |
| ------------------------ | --- | ------ | --- | --- | --- |
| (a) Showthatdim𝒫(\mathbf{F})/\mathcal{U}    |     | =degp. |     |     |     |
$$(b) Findabasisof𝒫(\mathbf{F})/\mathcal{U}.$$
Supposep,q\in𝒫(\mathbf{C})arenonconstantpolynomialswithnozerosincommon.
| Letm=degpandn=degq.    |     | Uselinearalgebraasoutlinedbelowin(a)–(c) |     |             |     |
| ---------------------- | --- | ---------------------------------------- | --- | ----------- | --- |
| toprovethatthereexistr |     | \in𝒫 (\mathbf{C})ands\in𝒫                             |     | (\mathbf{C})suchthat |     |
|                        |     | n-1                                      |     | m-1         |     |
rp+sq=1.
Define\mathcal{T}∶
| (a) | 𝒫 (\mathbf{C})\times𝒫 | (\mathbf{C})\rightarrow𝒫 |       | (\mathbf{C})by |     |
| --- | ------- | ----- | ----- | ----- | --- |
|     | n-1     | m-1   | m+n-1 |       |     |
\mathcal{T}(r,s)=rp+sq.
| Showthatthelinearmap\mathcal{T}               |     | isinjective.       |     |           |         |
| ----------------------------------- | --- | ------------------ | --- | --------- | ------- |
| (b) Showthatthelinearmap\mathcal{T}           |     | in(a)issurjective. |     |           |         |
| (c) Use(b)toconcludethatthereexistr |     |                    | \in𝒫  | (\mathbf{C})ands\in𝒫 | (\mathbf{C})such |
|                                     |     |                    | n-1 |           | m-1     |
thatrp+sq=1.
