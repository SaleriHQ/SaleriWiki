---
title: Chapter 6
source: Clippings/LADR4e.pdf
created: 2026-04-23
type: chapter
tags:
  - book
  - chapter
---

# Chapter 6
Inner Product Spaces
Inmakingthe definitionofa vectorspace, wegeneralizedthelinear structure
$$(additionandscalarmultiplication)of\mathbf{R}2 and\mathbf{R}3. Weignoredgeometricfeatures$$
suchasthenotionsoflengthandangle. Theseideasareembeddedintheconcept
ofinnerproducts,whichwewillinvestigateinthischapter.
Every inner product induces a norm, which you can think of as a length.
Thisnormsatisfieskeypropertiessuchasthe Pythagoreantheorem,thetriangle
inequality,theparallelogramequality,andthe Cauchy–Schwarzinequality.
orthogonal vectors in the context of an inner product space. We will see that
orthonormalbasesaretremendouslyusefulininnerproductspaces. The Gram–
Schmidtprocedureconstructssuchbases. Thischapterwillconcludebyputting
togetherthesetoolstosolveminimizationproblems.
standingassumptionsforthischapter
• \mathbf{F} denotes\mathbf{R} or\mathbf{C}.
• \mathcal{V} and\mathcal{W} denotevectorspacesover\mathbf{F}.
Matthew Petroff CCBY-SA
The George Peabody Library,nowpartof Johns Hopkins University,openedwhile
James Sylvester(1814–1897)wastheuniversity’sfirstmathematicsprofessor. Sylvester’s
publicationsincludethefirstuseofthewordmatrixinmathematics.

| --- | -------- | ------------------ | --- | --- | --- | --- | --- |
| 6A Inner | Products |     | and Norms |     |     |     |     |
| -------- | -------- | --- | --------- | --- | --- | --- | --- |
Tomotivatetheconceptofinnerproduct,
| think of                     | vectors in | \mathbf{R}2 and  | \mathbf{R}3 as     | arrows |     |     |     |
| ---------------------------- | ---------- | ------- | --------- | ------ | --- | --- | --- |
| withinitialpointattheorigin. |            |         | Thelength |        |     |     |     |
| of a vector                  | v in \mathbf{R}2    | or \mathbf{R}3   | is called | the    |     |     |     |
| norm of                      | v and is   | denoted | by ‖v‖.   | Thus   |     |     |     |
forv=(a,b)\in\mathbf{R}2,wehave
Thisvectorvhasnorm\sqrta2+b2.
‖v‖=\sqrta2+b2.
Similarly,ifv=(a,b,c)\in\mathbf{R}3,then‖v‖=\sqrta2+b2+c2.
Eventhoughwecannotdrawpicturesinhigherdimensions,thegeneralization
| to\mathbf{R}n iseasy: | wedefinethenormofx |     |     | =(x ,…,x | )\in\mathbf{R}n | by  |     |
| ------------ | ------------------ | --- | --- | -------- | ---- | --- | --- |
|              |                    |     |     | 1        | n    |     |     |
‖x‖=\sqrtx2+⋯+x2.
|     |     |     |     | 1   | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
\mathbf{R}n.
The norm is not linear on To inject linearity into the discussion, we
introducethedotproduct.
| 6.1 definition: | dotproduct        |       |                                  |        |     |     |     |
| --------------- | ----------------- | ----- | -------------------------------- | ------ | --- | --- | --- |
| Forx,y          | \in\mathbf{R}n,thedotproduct |       | ofxandy,denotedbyx\cdoty,isdefinedby |        |     |     |     |
|                 |                   |       | x\cdoty =x                           | y +⋯+x | y , |     |     |
|                 |                   |       |                                  | 1 1    | n n |     |     |
|                 | ,…,x              |       |                                  | ,…,y   |     |     |     |
| wherex          | =(x               | )andy | =(y                              | ).     |     |     |     |
|                 | 1                 | n     |                                  | 1 n    |     |     |     |
Thedotproductoftwovectorsin\mathbf{R}n
Ifwethinkofavectorasapointinstead
| is a number,      | not     | a vector.       | Notice       | that                             |           |                 |     |
| ----------------- | ------- | --------------- | ------------ | -------------------------------- | --------- | --------------- | --- |
|                   |         |                 |              | of as                            | an arrow, | then ‖x‖ should | be  |
| =‖x‖2             |         | \in\mathbf{R}n.            |              |                                  |           |                 |     |
| x\cdotx               | forallx |                 | Furthermore, | interpretedtomeanthedistancefrom |           |                 |     |
| thedotproducton\mathbf{R}n |         | hasthefollowing |              |                                  |           |                 |     |
theorigintothepointx.
properties.
\in\mathbf{R}n.
• x\cdotx \geq0forallx
| • x\cdotx  | =0ifandonlyifx         |      | =0. |                |     |                |     |
| ------ | ---------------------- | ---- | --- | -------------- | --- | -------------- | --- |
|        | \in\mathbf{R}n fixed,themapfrom\mathbf{R}n |      |     |                |     | \in\mathbf{R}n            |     |
| • Fory |                        |      |     | to\mathbf{R} thatsendsx |     | tox\cdotyislinear. |     |
| • x\cdoty  | =y\cdotxforallx,y          | \in\mathbf{R}n. |     |                |     |                |     |
Aninnerproductisageneralizationofthedotproduct. Atthispointyoumay
betemptedtoguessthataninnerproductisdefinedbyabstractingtheproperties
ofthedotproductdiscussedinthelastparagraph. Forrealvectorspaces,that
guessiscorrect. However,sothatwecanmakeadefinitionthatwillbeuseful
forbothrealandcomplexvectorspaces,weneedtoexaminethecomplexcase
beforemakingthedefinition.

| --- | --- | --------- | --------------------- | --- |
| Recallthatif            | \lambda=a+bi,wherea,b\in\mathbf{R},then |                                       |               |         |
| ----------------------- | ---------------------- | ------------------------------------- | ------------- | ------- |
| • theabsolutevalueof    |                        | \lambda,denotedby|\lambda|,isdefinedby|\lambda|=\sqrta2+b2; |               |         |
| • thecomplexconjugateof |                        | \lambda,denotedby                           | \lambda,isdefinedby | \lambda=a-bi; |
• |\lambda|2 = \lambda\lambda.
See Chapter 4forthedefinitionsandthebasicpropertiesoftheabsolutevalue
andcomplexconjugate.
$$)\in\mathbf{C}n,wedefinethenormofzby$$
| Forz=(z | ,…,z |     |     |     |
| ------- | ---- | --- | --- | --- |
1 n
|     |     | ‖z‖=\sqrt|z | |2+⋯+|z |2. |     |
| --- | --- | ------- | ----------- | --- |
|     |     |         | 1 n         |     |
Theabsolutevaluesareneededbecausewewant‖z‖tobeanonnegativenumber.
Notethat
|     |     | ‖z‖2 =z | z +⋯+z z . |     |
| --- | --- | ------- | ---------- | --- |
|     |     |         | 1 1 n n    |     |
‖z‖2
We want to think of as the inner product of z with itself, as we did
in \mathbf{R}n. The equation above thus suggests that the inner product of the vector
$$)\in\mathbf{C}n$$
| w=(w ,…,w | withzshouldequal |     |          |     |
| --------- | ---------------- | --- | -------- | --- |
| 1         | n                |     |          |     |
|           |                  | w z | +⋯+w z . |     |
|           |                  | 1 1 | n n      |     |
If the roles of the w and z were interchanged, the expression above would be
replacedwithitscomplexconjugate. Thusweshouldexpectthattheinnerproduct
ofwwithzequalsthecomplexconjugateoftheinnerproductofzwithw. With
thatmotivation,wearenowreadytodefineaninnerproducton\mathcal{V},whichmaybe
arealoracomplexvectorspace.
Onecommentaboutthenotationusedinthenextdefinition:
| • For \lambda\in\mathbf{C},thenotation |     | \lambda\geq0means | \lambdaisrealandnonnegative. |     |
| --------------------- | --- | -------- | ---------------------- | --- |
innerproduct
**6.2 定义：** An inner product on \mathcal{V} is a function that takes each ordered pair (u,v) of
| elementsof\mathcal{V} | toanumber\langleu,v\rangle\in\mathbf{F} |     | andhasthefollowingproperties. |     |
| ----------- | ---------------- | --- | ----------------------------- | --- |
positivity
\langlev,v\rangle\geq0forallv\in\mathcal{V}.
definiteness
\langlev,v\rangle=0ifandonlyifv=0.
additivityinfirstslot
\langleu+v,w\rangle=\langleu,w\rangle+\langlev,w\rangleforallu,v,w\in\mathcal{V}.
homogeneityinfirstslot
| \langle\lambdau,v\rangle= | \lambda\langleu,v\rangleforall | andallu,v\in\mathcal{V}. |     |     |
| ------- | ------------ | ------------ | --- | --- |
\lambda\in\mathbf{F}
conjugatesymmetry
\langleu,v\rangle=\langlev,u\rangleforallu,v\in\mathcal{V}.

| -------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Everyrealnumberequalsitscomplex
|            |      |           |         |      | Most | mathematicians | define | inner |
| ---------- | ---- | --------- | ------- | ---- | ---- | -------------- | ------ | ----- |
| conjugate. | Thus | if we are | dealing | with |      |                |        |       |
productsasabove,butmanyphysicists
arealvectorspace,theninthelastcon- use a definition that requires homo-
| dition above                       | we  | can dispense |     | with the |               |     |                         |     |
| ---------------------------------- | --- | ------------ | --- | -------- | ------------- | --- | ----------------------- | --- |
|                                    |     |              |     |          | geneity       | in  | the second slot instead | of  |
| complexconjugateandsimplystatethat |     |              |     |          | thefirstslot. |     |                         |     |
\langleu,v\rangle=\langlev,u\rangleforallu,v\in\mathcal{V}.
innerproducts
**6.3 例：** on\mathbf{F}n
| (a) The Euclideaninnerproduct |      |          |      |           | isdefinedby |     |        |     |
| ---------------------------- | ---- | -------- | ---- | --------- | ----------- | --- | ------ | --- |
|                              |      | \langle(w ,…,w |      | ),(z ,…,z | )\rangle=w        | z   | +⋯+w z |     |
|                              |      | 1        | n    | 1         | n           | 1 1 | n n    |     |
| forall(w                     | ,…,w | ),(z     | ,…,z | )\in\mathbf{F}n.     |             |     |        |     |
|                              | 1    | n        | 1    | n         |             |     |        |     |
arepositivenumbers,thenaninnerproductcanbedefinedon\mathbf{F}n
$$(b) Ifc ,…,c$$
| 1   | n   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
by
|          |      | \langle(w ,…,w | ),(z | ,…,z  | )\rangle=c | w z   | +⋯+c w z |     |
| -------- | ---- | -------- | ---- | ----- | ---- | ----- | -------- | --- |
|          |      | 1        | n    | 1     | n    | 1 1 1 | n n n    |     |
|          | ,…,w | ),(z     | ,…,z | )\in\mathbf{F}n. |      |       |          |     |
| forall(w | 1    | n        | 1    | n     |      |       |          |     |
$$(c) Aninnerproductcanbedefinedonthevectorspaceofcontinuousreal-valued$$
functionsontheinterval[-1,1]by
|     |     |     |     | \langlef,g\rangle=\int |     | fg  |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
-1
| forall | f,gcontinuousreal-valuedfunctionson[-1,1]. |     |     |     |     |     |     |     |
| ------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
$$(d) Aninnerproductcanbedefinedon𝒫(\mathbf{R})by$$
|     |     |     | \langlep,q\rangle=p(0)q(0)+\int |     |     | p′q′ |     |     |
| --- | --- | --- | ---------------- | --- | --- | ---- | --- | --- |
-1
forallp,q\in𝒫(\mathbf{R}).
$$(e) Aninnerproductcanbedefinedon𝒫(\mathbf{R})by$$
\infty
p(x)q(x)e-xdx
\langlep,q\rangle=\int
forallp,q\in𝒫(\mathbf{R}).
| 6.4 definition: |     | innerproductspace |     |     |     |     |     |     |
| --------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Aninnerproductspaceisavectorspace\mathcal{V} alongwithaninnerproducton\mathcal{V}.
Themostimportantexampleofaninnerproductspaceis\mathbf{F}nwiththe Euclidean
innerproductgivenby(a)intheexampleabove. When\mathbf{F}n isreferredtoasan
innerproductspace,youshouldassumethattheinnerproductisthe Euclidean
innerproductunlessexplicitlytoldotherwise.

Section6A Inner Productsand Norms 185
So that we do not have to keep repeating the hypothesis that \mathcal{V} and \mathcal{W} are
innerproductspaces,wemakethefollowingassumption.
**6.5 记号：** \mathcal{V},\mathcal{W}
Fortherestofthischapterandthenextchapter,\mathcal{V}and\mathcal{W}denoteinnerproduct
spacesover\mathbf{F}.
Notetheslightabuseoflanguagehere. Aninnerproductspaceisavector
spacealongwithaninnerproductonthatvectorspace. Whenwesaythatavector
space\mathcal{V} isaninnerproductspace,wearealsothinkingthataninnerproducton
\mathcal{V} islurkingnearbyorisclearfromthecontext(oristhe Euclideaninnerproduct
ifthevectorspaceis\mathbf{F}n).
6.6 basicpropertiesofaninnerproduct
$$(a) Foreachfixedv \in \mathcal{V},thefunctionthattakesu \in \mathcal{V} to\langleu,v\rangleisalinear$$
mapfrom\mathcal{V} to\mathbf{F}.
$$(b) \langle0,v\rangle=0foreveryv\in\mathcal{V}.$$
$$(c) \langlev,0\rangle=0foreveryv\in\mathcal{V}.$$
$$(d) \langleu,v+w\rangle=\langleu,v\rangle+\langleu,w\rangleforallu,v,w\in\mathcal{V}.$$
$$(e) \langleu,\lambdav\rangle= \lambda\langleu,v\rangleforall \lambda\in\mathbf{F} andallu,v\in\mathcal{V}.$$
Proof
$$(a) Forv\in\mathcal{V},thelinearityofu↦\langleu,v\ranglefollowsfromtheconditionsofadditivity$$
andhomogeneityinthefirstslotinthedefinitionofaninnerproduct.
$$(b) Everylinearmaptakes0to0. Thus(b)followsfrom(a).$$
$$(c) Ifv\in\mathcal{V},thentheconjugatesymmetrypropertyinthedefinitionofaninner$$
productand(b)showthat\langlev,0\rangle=\langle0,v\rangle=0=0.
$$(d) Supposeu,v,w\in\mathcal{V}. Then$$
\langleu,v+w\rangle=\langlev+w,u\rangle
=\langlev,u\rangle+\langlew,u\rangle
=\langlev,u\rangle+\langlew,u\rangle
=\langleu,v\rangle+\langleu,w\rangle.
$$(e) Suppose \lambda\in\mathbf{F} andu,v\in\mathcal{V}. Then$$
\langleu,\lambdav\rangle=\langle\lambdav,u\rangle
= \lambda\langlev,u\rangle
= \lambda \langlev,u\rangle
= \lambda\langleu,v\rangle.

186 Chapter 6 Inner Product Spaces
Norms
Our motivation for defining inner products came initially from the norms of
vectorson\mathbf{R}2 and\mathbf{R}3. Nowweseethateachinnerproductdeterminesanorm.
**6.7 定义：** norm,‖v‖
Forv\in\mathcal{V},thenormofv,denotedby‖v‖,isdefinedby
‖v‖=\sqrt\langlev,v\rangle.
**6.8 例：** norms
$$(a) If(z ,…,z )\in\mathbf{F}n (withthe Euclideaninnerproduct),then$$
1 n
‖(z ,…,z )‖=\sqrt|z |2+⋯+|z |2.
1 n 1 n
$$(b) For f inthevectorspaceofcontinuousreal-valuedfunctionson[-1,1]and$$
withinnerproductgivenasin6.3(c),wehave
‖f‖=\sqrt\int f2.
-1
6.9 basicpropertiesofthenorm
Supposev\in\mathcal{V}.
$$(a) ‖v‖=0ifandonlyifv=0.$$
$$(b) ‖\lambdav‖=|\lambda|‖v‖forall \lambda\in\mathbf{F}.$$
Proof
$$(a) Thedesiredresultholdsbecause\langlev,v\rangle=0ifandonlyifv=0.$$
$$(b) Suppose \lambda\in\mathbf{F}. Then$$
‖\lambdav‖2 =\langle\lambdav,\lambdav\rangle
= \lambda\langlev,\lambdav\rangle
= \lambda\lambda\langlev,v\rangle
=|\lambda|2‖v‖2.
Takingsquarerootsnowgivesthedesiredequality.
Theproofof(b)intheresultaboveillustratesageneralprinciple: working
withnormssquaredisusuallyeasierthanworkingdirectlywithnorms.

| --- | --- | --- | --------- | --------------------- |
Nowwecometoacrucialdefinition.
orthogonal
**6.10 定义：** | Twovectorsu,v\in\mathcal{V} |            | arecalledorthogonalif\langleu,v\rangle=0. |           |     |
| --------------- | ---------- | ----------------------------- | --------- | --- |
| In the          | definition | above,                        | the order | of  |
Thewordorthogonalcomesfromthe
thetwovectorsdoesnotmatter,because
Greekwordorthogonios,whichmeans
| \langleu,v\rangle =  | 0 if and | only if | \langlev,u\rangle =         | 0. In- right-angled. |
| -------- | -------- | ------- | --------------- | -------------------- |
| stead of | saying   | u and v | are orthogonal, |                      |
sometimeswesayuisorthogonaltov.
Exercise15asksyoutoprovethatifu,varenonzerovectorsin\mathbf{R}2,then
\langleu,v\rangle=‖u‖‖v‖cos\theta,
where\thetaistheanglebetweenuandv(thinkingofuandvasarrowswithinitial
Thustwononzerovectorsin\mathbf{R}2
pointattheorigin). areorthogonal(withrespect
to the Euclidean inner product) if and only if the cosine of the angle between
themis0,whichhappensifandonlyifthevectorsareperpendicularintheusual
senseofplanegeometry. Thusyoucanthinkofthewordorthogonalasafancy
wordmeaningperpendicular.
Webeginourstudyoforthogonalitywithaneasyresult.
6.11 orthogonalityand0
$$(a) 0isorthogonaltoeveryvectorin\mathcal{V}.$$
| (b) 0istheonlyvectorin\mathcal{V} |     |     | thatisorthogonaltoitself. |     |
| ----------------------- | --- | --- | ------------------------- | --- |
Proof
$$(a) Recallthat6.6(b)statesthat\langle0,v\rangle=0foreveryv\in\mathcal{V}.$$
| (b) Ifv\in\mathcal{V} | and\langlev,v\rangle=0,thenv=0(bydefinitionofinnerproduct). |     |     |     |
| --------- | ----------------------------------------------- | --- | --- | --- |
Forthespecialcase\mathcal{V} =\mathbf{R}2,thenexttheoremwasknownover3,500yearsago
in Babyloniaandthenrediscoveredandprovedover2,500yearsagoin Greece.
Ofcourse,theproofbelowisnottheoriginalproof.
6.12 Pythagoreantheorem
| Supposeu,v\in\mathcal{V}.         |     | Ifuandvareorthogonal,then |            |             |
| --------------------- | --- | ------------------------- | ---------- | ----------- |
|                       |     |                           | ‖u+v‖2     | =‖u‖2+‖v‖2. |
| Proof Suppose\langleu,v\rangle=0. |     |                           | Then       |             |
|                       |     | ‖u+v‖2                    | =\langleu+v,u+v\rangle |             |
=\langleu,u\rangle+\langleu,v\rangle+\langlev,u\rangle+\langlev,v\rangle
=‖u‖2+‖v‖2.

| -------- | ------------------ | --- | --- | --- |
| Supposeu,v\in\mathcal{V},withv\neq0. |     | Wewouldliketowriteuasascalarmultiple |     |     |
| --------------------- | --- | ------------------------------------ | --- | --- |
ofvplusavectorworthogonaltov,assuggestedinthepicturehere.
Anorthogonaldecomposition:
| uexpressedasascalarmultipleof |     | vplusavectororthogonaltov. |     |     |
| ----------------------------- | --- | -------------------------- | --- | --- |
Todiscoverhowtowriteuasascalarmultipleofvplusavectororthogonal
| tov,letc | \in\mathbf{F} denoteascalar. | Then |     |     |
| -------- | ----------------- | ---- | --- | --- |
$$u=cv+(u-cv).$$
| Thusweneedtochoosecsothatvisorthogonalto(u-cv). |     |     | Hencewewant |     |
| ----------------------------------------------- | --- | --- | ----------- | --- |
$$0=\langleu-cv,v\rangle=\langleu,v\rangle-c‖v‖2.$$
Theequationaboveshowsthatweshouldchoosectobe\langleu,v\rangle/‖v‖2. Makingthis
choiceofc,wecanwrite
|     |     | \langleu,v\rangle | \langleu,v\rangle |     |
| --- | --- | ----- | ----- | --- |
v+(u-
|     | u=  |      | v).  |     |
| --- | --- | ---- | ---- | --- |
|     |     | ‖v‖2 | ‖v‖2 |     |
Asyoushouldverify,theequationdisplayedaboveexplicitlywritesuasascalar
multipleofvplusavectororthogonaltov. Thuswehaveprovedthefollowing
keyresult.
anorthogonaldecomposition
6.13
|                       |        | \langleu,v\rangle  | \langleu,v\rangle    |         |
| --------------------- | ------ | ------ | -------- | ------- |
| Supposeu,v\in\mathcal{V},withv\neq0. |        | Setc = | andw=u-  | v. Then |
|                       |        | ‖v‖2   | ‖v‖2     |         |
|                       | u=cv+w | and    | \langlew,v\rangle=0. |         |
Theorthogonaldecomposition6.13willbeusedintheproofofthe Cauchy–
Schwarz inequality, which is our next result and is one of the most important
inequalitiesinmathematics.

| --- | --- | --------- | --------------------- | --- | --- | --- |
Cauchy–Schwarzinequality
6.14
| Supposeu,v\in\mathcal{V}. | Then |     |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- | --- |
|\langleu,v\rangle|\leq‖u‖‖v‖.
Thisinequalityisanequalityifandonlyifoneofu,visascalarmultipleof
theother.
Proof Ifv=0,thenbothsidesofthedesiredinequalityequal0. Thuswecan
| assumethatv\neq0. | Considertheorthogonaldecomposition |     |     |     |     |     |
| -------------- | ---------------------------------- | --- | --- | --- | --- | --- |
\langleu,v\rangle
|     |     | u=  | v+w |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
‖v‖2
| givenby6.13,wherewisorthogonaltov. |     |     | Bythe Pythagoreantheorem, |     |     |     |
| ---------------------------------- | --- | --- | ------------------------ | --- | --- | --- |
\langleu,v\rangle
|     |     | ‖u‖2 =∥ | v∥ +‖w‖2 |     |     |     |
| --- | --- | ------- | -------- | --- | --- | --- |
‖v‖2
∣\langleu,v\rangle∣2
|     |     | =   | +‖w‖2 |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
‖v‖2
∣\langleu,v\rangle∣2
| 6.15 |     | \geq   | .   |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- |
‖v‖2
Multiplying both sides of this inequality by ‖v‖2 and then taking square roots
givesthedesiredinequality.
| The proof | in the paragraph | above |     |     |     |     |
| --------- | ---------------- | ----- | --- | --- | --- | --- |
Augustin-Louis Cauchy(1789–1857)
showsthatthe Cauchy–Schwarzinequal-
|     |     |     | proved 6.16(a) | in  | 1821. | In 1859, |
| --- | --- | --- | -------------- | --- | ----- | -------- |
ity is an equality if and only if 6.15 is Cauchy’sstudent Viktor Bunyakovsky
| an equality. | This happens | if and only |     |     |     |     |
| ------------ | ------------ | ----------- | --- | --- | --- | --- |
$$(1804–1889)provedintegralinequalif w = 0. But w = 0 if and only if u ities like the one in 6.16(b). A few$$
| is a multiple | of v (see 6.13). | Thus the |                |         |             |     |
| ------------- | ---------------- | -------- | -------------- | ------- | ----------- | --- |
|               |                  |          | decades later, | similar | discoveries | by  |
Cauchy–Schwarzinequalityisanequal- Hermann Schwarz (1843–1921) atityifandonlyifuisascalarmultipleofv tractedmoreattentionandledtothe
| orvisascalarmultipleofu(orboth;the |     |     | nameofthisinequality. |     |     |     |
| ---------------------------------- | --- | --- | --------------------- | --- | --- | --- |
phrasinghasbeenchosentocovercases
inwhicheitheruorvequals0).
Cauchy–Schwarzinequality
**6.16 例：** | (a) Ifx ,…,x | ,y ,…,y   | \in\mathbf{R},then                   |     |     |     |     |
| ------------ | --------- | ------------------------- | --- | --- | --- | --- |
| 1            | n 1       | n                         |     |     |     |     |
|              | (x y +⋯+x | y )2 \leq(x2+⋯+x2)(y2+⋯+y2), |     |     |     |     |
|              | 1 1       | n n                       | 1 n | 1   | n   |     |
as follows from applying the Cauchy–Schwarz inequality to the vectors
$$)\in\mathbf{R}n,usingtheusual Euclideaninnerproduct.$$
| (x ,…,x | ),(y ,…,y |     |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- |
| 1       | n 1       | n   |     |     |     |     |

190 Chapter 6 Inner Product Spaces
$$(b) If f,garecontinuousreal-valuedfunctionson[-1,1],then$$
1 2 1 1
∣\int fg∣ \leq(\int f2)(\int g2),
-1 -1 -1
asfollowsfromapplyingthe Cauchy–Schwarzinequalityto Example6.3(c).
Thenextresult,calledthetriangleinequality,
hasthegeometricinterpretationthatthelength
ofeachsideofatriangleislessthanthesumof
thelengthsoftheothertwosides.
Notethatthetriangleinequalityimpliesthat
theshortestpolygonalpathbetweentwopointsis
Inthistriangle,thelengthof
asinglelinesegment(apolygonalpathconsists
u+vislessthanthelength
oflinesegments).
of uplusthelengthof v.
6.17 triangleinequality
Supposeu,v\in\mathcal{V}. Then
‖u+v‖\leq‖u‖+‖v‖.
Thisinequalityisanequalityifandonlyifoneofu,visanonnegativereal
multipleoftheother.
‖u+v‖2 =\langleu+v,u+v\rangle
=\langleu,u\rangle+\langlev,v\rangle+\langleu,v\rangle+\langlev,u\rangle
=\langleu,u\rangle+\langlev,v\rangle+\langleu,v\rangle+\langleu,v\rangle
=‖u‖2+‖v‖2+2Re\langleu,v\rangle
6.18 \leq‖u‖2+‖v‖2+2∣\langleu,v\rangle∣
6.19 \leq‖u‖2+‖v‖2+2‖u‖‖v‖
=(‖u‖+‖v‖)2,
where6.19followsfromthe Cauchy–Schwarzinequality(6.14). Takingsquare
rootsofbothsidesoftheinequalityabovegivesthedesiredinequality.
Theproofaboveshowsthatthetriangleinequalityisanequalityifandonlyif
wehaveequalityin6.18and6.19. Thuswehaveequalityinthetriangleinequality
ifandonlyif
6.20 \langleu,v\rangle=‖u‖‖v‖.
Ifoneofu,visanonnegativerealmultipleoftheother,then6.20holds. Conversely, suppose 6.20 holds. Then the condition for equality in the Cauchy–
Schwarzinequality(6.14)impliesthatoneofu,visascalarmultipleoftheother.
Thisscalarmustbeanonnegativerealnumber,by6.20,completingtheproof.
Forthereversetriangleinequality,see Exercise20.

| --- | --- | --- | --- | --------- | --------------------- | --- |
| The                  | next result              | is  | called      | the parallel- |        |     |
| -------------------- | ------------------------ | --- | ----------- | ------------- | ------ | --- |
| ogramequalitybecause |                          |     | of its      | geometric     |        |     |
| interpretation:      | ineveryparallelogram,the |     |             |               |        |     |
| sum                  | of the squares           | of  | the lengths |               | of the |     |
diagonalsequalsthesumofthesquaresof
| thelengthsofthefoursides. |     |     |     | Notethatthe |     |     |
| ------------------------- | --- | --- | --- | ----------- | --- | --- |
proof here is more straightforward than Thediagonalsofthisparallelogram
| theusualproofin Euclideangeometry. |     |     |     |     |     | areu+vandu-v. |
| --------------------------------- | --- | --- | --- | --- | --- | ------------- |
6.21 parallelogramequality
| Supposeu,v\in\mathcal{V}. |     | Then          |     |     |                |     |
| ------------- | --- | ------------- | --- | --- | -------------- | --- |
|               |     | ‖u+v‖2+‖u-v‖2 |     |     | =2(‖u‖2+‖v‖2). |     |
|     | ‖u+v‖2+‖u-v‖2 |     |     | =\langleu+v,u+v\rangle+\langleu-v,u-v\rangle |     |     |
| --- | ------------- | --- | --- | -------------------- | --- | --- |
=‖u‖2+‖v‖2+\langleu,v\rangle+\langlev,u\rangle
+‖u‖2+‖v‖2-\langleu,v\rangle-\langlev,u\rangle
=2(‖u‖2+‖v‖2),
asdesired.
| Exercises | 6A                          |     |     |     |          |         |
| --------- | --------------------------- | --- | --- | --- | -------- | ------- |
| 1         | Proveorgiveacounterexample: |     |     |     | Ifv ,…,v | \in\mathcal{V},then |
|           |                             |     |     |     | 1        | m       |
|           |                             |     |     | m   | m        |         |
|           |                             |     |     | \sum   | \sum\langlev,v    | \rangle\geq0.    |
|           |                             |     |     |     | j k      |         |
$$j=1k=1$$
| 2   | Suppose\mathcal{S}\inℒ(\mathcal{V}). |     | Define\langle\cdot,\cdot\rangle |     | by  |     |
| --- | -------------- | --- | ----------- | --- | --- | --- |
|     |     |     |     | \langleu,v\rangle | =\langle\mathcal{S}u,\mathcal{S}v\rangle |     |
| --- | --- | --- | --- | ----- | -------- | --- |
forallu,v\in\mathcal{V}. Showthat\langle\cdot,\cdot\rangle isaninnerproducton\mathcal{V} ifandonlyif\mathcal{S}is
injective.
3 (a) Show that the function taking an ordered pair ((x ,x ),(y ,y )) of
1 2 1 2
|     | elementsof\mathbf{R}2 |     |      | |+|x  | |isnotaninnerproducton\mathbf{R}2. |     |
| --- | ------------ | --- | ---- | ----- | ------------------------- | --- |
|     |              |     | to|x | 1 y 1 | 2 y 2                     |     |
$$(b) Showthatthefunctiontakinganorderedpair((x ,x ,x ),(y ,y ,y ))$$
1 2 3 1 2 3
|     | ofelementsof\mathbf{R}3 |     | tox | y   | +x y isnotaninnerproducton\mathbf{R}3. |     |
| --- | -------------- | --- | --- | --- | ----------------------------- | --- |
|     |                |     |     | 1 1 | 3 3                           |     |
4 Suppose \mathcal{T} \in ℒ(\mathcal{V}) is such that ‖\mathcal{T}v‖ \leq ‖v‖ for every v \in \mathcal{V}. Prove that
\mathcal{T}-\sqrt2\mathcal{I}
isinjective.

| -------- | ------------------ | --- | --- | --- |
| 5 Suppose\mathcal{V} isarealinnerproductspace. |                                       |     |                |     |
| ------------------------------------ | ------------------------------------- | --- | -------------- | --- |
| (a) Showthat\langleu+v,u-v\rangle=‖u‖2-‖v‖2      |                                       |     | foreveryu,v\in\mathcal{V}. |     |
| (b) Showthatifu,v\in\mathcal{V}                  | havethesamenorm,thenu+visorthogonalto |     |                |     |
u-v.
$$(c) Use(b)toshowthatthediagonalsofarhombusareperpendicularto$$
eachother.
| 6 Supposeu,v\in\mathcal{V}. | Provethat\langleu,v\rangle=0 | ⟺   | ‖u‖\leq‖u+av‖foralla\in\mathbf{F}. |     |
| --------------- | ---------------- | --- | -------------------- | --- |
7 Supposeu,v \in \mathcal{V}. Provethat‖au+bv‖ = ‖bu+av‖foralla,b \in \mathbf{R} ifand
onlyif‖u‖=‖v‖.
8 Suppose a,b,c,x,y \in \mathbf{R} and a2 + b2 + c2 + x2 + y2 \leq 1. Prove that
| a+b+c+4x+9y     | \leq10.                    |     |               |     |
| --------------- | ----------------------- | --- | ------------- | --- |
| Supposeu,v\in\mathcal{V}    | and‖u‖=‖v‖=1and\langleu,v\rangle=1. |     |               |     |
| 9               |                         |     | Provethatu=v. |     |
| 10 Supposeu,v\in\mathcal{V} | and‖u‖\leq1and‖v‖\leq1.       |     | Provethat     |     |
\sqrt1-‖u‖2\sqrt1-‖v‖2
\leq1-∣\langleu,v\rangle∣.
11 Findvectorsu,v\in\mathbf{R}2 suchthatuisascalarmultipleof(1,3),visorthogonalto(1,3),and(1,2)=u+v.
12 Supposea,b,c,darepositivenumbers.
|                         |     | 1 1 1 | 1       |     |
| ----------------------- | --- | ----- | ------- | --- |
| (a) Provethat(a+b+c+d)( |     | + +   | + )\geq16. |     |
|                         |     | a b c | d       |     |
Forwhichpositivenumbersa,b,c,distheinequalityaboveanequality?
$$(b)$$
13 Showthatthesquareofanaverageislessthanorequaltotheaverageofthe
,…,a
| squares. Moreprecisely,showthatifa |                                         | 1   | n \in\mathbf{R},thenthesquareofthe |     |
| ---------------------------------- | --------------------------------------- | --- | ----------------------- | --- |
| averageofa ,…,a                    | islessthanorequaltotheaverageofa2,…,a2. |     |                         |     |
| 1                                  | n                                       |     |                         | 1 n |
14 Supposev\in\mathcal{V} andv\neq0. Provethatv/‖v‖istheuniqueclosestelementon
| theunitsphereof\mathcal{V} | tov. Moreprecisely,provethatifu\in\mathcal{V} |     |     | and‖u‖=1, |
| ---------------- | --------------------------------- | --- | --- | --------- |
then
v
|     | ∥v- | ∥\leq‖v-u‖, |     |     |
| --- | --- | -------- | --- | --- |
‖v‖
withequalityonlyifu=v/‖v‖.
Supposeu,varenonzerovectorsin\mathbf{R}2.
| 15  |     | Provethat |     |     |
| --- | --- | --------- | --- | --- |
\langleu,v\rangle=‖u‖‖v‖cos\theta,
where\theta istheanglebetweenuandv(thinkingofuandvasarrowswith
initialpointattheorigin).
Hint:Usethelawofcosinesonthetriangleformedbyu,v,andu-v.

| --- | --- | --- | --- | --------- | --- | --------------------- | --- | --- | --- |
16 Theanglebetweentwovectors(thoughtofasarrowswithinitialpointat
theorigin)in\mathbf{R}2 or\mathbf{R}3 canbedefinedgeometrically. However,geometryis
notasclearin\mathbf{R}n
|     |         |               | forn>3. |     | Thustheanglebetweentwononzerovectors |     |     |     |     |
| --- | ------- | ------------- | ------- | --- | ------------------------------------ | --- | --- | --- | --- |
|     | x,y \in\mathbf{R}n | isdefinedtobe |         |     |                                      |     |     |     |     |
\langlex,y\rangle
|     |     |     |     |     | arccos | ,   |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
‖x‖‖y‖
wherethemotivationforthisdefinitioncomesfrom Exercise15. Explain
whythe Cauchy–Schwarzinequalityisneededtoshowthatthisdefinition
makessense.
17 Provethat
|     |                    |     |     | n     | 2         | n   | n b2 |     |     |
| --- | ------------------ | --- | --- | ----- | --------- | --- | ---- | --- | --- |
|     |                    |     |     |       | \leq(\sumka2)(\sum |     | k    |     |     |
|     |                    |     |     | (\suma b | )         |     |      | )   |     |
|     |                    |     |     | k k   |           | k   | k    |     |     |
|     |                    |     |     | k=1   |           | k=1 | k=1  |     |     |
|     |                    |     |     | ,…,a  | ,…,b      |     |      |     |     |
|     | forallrealnumbersa |     |     |       | andb      | .   |      |     |     |
|     |                    |     |     | 1 n   | 1         | n   |      |     |     |
f∶
| 18  | (a) Suppose |     | [1,\infty)\rightarrow[0,\infty)iscontinuous. |     |        |              | Showthat |     |     |
| --- | ----------- | --- | ------------------------ | --- | ------ | ------------ | -------- | --- | --- |
|     |             |     |                          | \infty   | 2      | \infty            |          |     |     |
|     |             |     |                          | (\int  | f ) \leq\int | x2(f(x))2dx. |          |     |     |
$$(b) Forwhichcontinuousfunctions f∶ [1,\infty) \rightarrow [0,\infty)istheinequality$$
in(a)anequalitywithbothsidesfinite?
19 Suppose v ,…,v is a basis of \mathcal{V} and \mathcal{T} \in ℒ(\mathcal{V}). Prove that if \lambda is an
|     |     | 1   | n   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eigenvalueof\mathcal{T},then
|     |     |     |     |      | n          | n   |     |     |     |
| --- | --- | --- | --- | ---- | ---------- | --- | --- | --- | --- |
|     |     |     |     | |\lambda|2 | \leq \sum \sum|ℳ(\mathcal{T}) |     | |2, |     |     |
j,k
$$j=1k=1$$
|     | whereℳ(\mathcal{T}) |     | denotestheentryinrowj,columnkofthematrixof\mathcal{T} |     |     |     |     |     | with |
| --- | --------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | ---- |
j,k
|     | respecttothebasisv |     |     | ,…,v | .   |     |     |     |     |
| --- | ------------------ | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |                    |     |     | 1 n  |     |     |     |     |     |
Provethatifu,v\in\mathcal{V},then∣‖u‖-‖v‖∣\leq‖u-v‖.
|     | The                            | inequality | above       | is called | the                        |         | inequality. |     | For the |
| --- | ------------------------------ | ---------- | ----------- | --------- | -------------------------- | ------- | ----------- | --- | ------- |
|     |                                |            |             |           |                            | reverse | triangle    |     |         |
|     | reversetriangleinequalitywhen\mathcal{V} |            |             |           | =\mathbf{C},see Exercise2in Chapter 4. |         |             |     |         |
| 21  | Supposeu,v\in\mathcal{V}                   |            | aresuchthat |           |                            |         |             |     |         |
|     |                                |            | ‖u‖=3,      |           | ‖u+v‖=4,                   |         | ‖u-v‖=6.    |     |         |
Whatnumberdoes‖v‖equal?
22 Showthatifu,v\in\mathcal{V},then
‖u+v‖‖u-v‖\leq‖u‖2+‖v‖2.
| 23  | Supposev | ,…,v | \in\mathcal{V}   | aresuchthat‖v   |     | ‖\leq1foreachk |     | =1,…,m. | Show |
| --- | -------- | ---- | ---- | --------------- | --- | ----------- | --- | ------- | ---- |
|     |          | 1    | m    |                 |     | k           |     |         |      |
|     |          |      | ,…,a | \in{1,-1}suchthat |     |             |     |         |      |
thatthereexista
|     |     |     | 1   | m   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
\sqrt
|     |     |     |     | ‖a v | +⋯+a | v ‖\leq | m.  |     |     |
| --- | --- | --- | --- | ---- | ---- | ---- | --- | --- | --- |
|     |     |     |     | 1    | 1    | m m  |     |     |     |

| --- | -------- | ------------------ | --- | --- | --- |
24 Proveorgiveacounterexample: If‖\cdot‖isthenormassociatedwithaninner
producton\mathbf{R}2,thenthereexists(x,y)\in\mathbf{R}2suchthat‖(x,y)‖\neqmax{|x|,|y|}.
25 Suppose p > 0. Prove that there is an inner product on \mathbf{R}2 such that the
associatednormisgivenby
‖(x,y)‖=(|x|p+|y|p)1/p
|     | forall(x,y)\in\mathbf{R}2 | ifandonlyifp=2.           |     |           |     |
| --- | -------------- | ------------------------- | --- | --------- | --- |
| 26  | Suppose\mathcal{V}       | isarealinnerproductspace. |     | Provethat |     |
‖u+v‖2-‖u-v‖2
\langleu,v\rangle=
forallu,v\in\mathcal{V}.
| 27  | Suppose\mathcal{V} | isacomplexinnerproductspace. |     | Provethat |     |
| --- | -------- | ---------------------------- | --- | --------- | --- |
‖u+v‖2-‖u-v‖2+‖u+iv‖2i-‖u-iv‖2i
\langleu,v\rangle=
forallu,v\in\mathcal{V}.
| 28  | Anormonavectorspace\mathcal{U} |     | isafunction |     |     |
| --- | -------------------- | --- | ----------- | --- | --- |
‖\cdot‖∶
|     |     |     |     | \mathcal{U} \rightarrow[0,\infty) |     |
| --- | --- | --- | --- | -------- | --- |
suchthat‖u‖ = 0ifandonlyifu = 0,‖\alphau‖ = |\alpha|‖u‖forall\alpha \in \mathbf{F} andall
u\in\mathcal{U},and‖u+v‖\leq‖u‖+‖v‖forallu,v\in\mathcal{U}.
Provethatanormsatisfying
theparallelogramequalitycomesfromaninnerproduct(inotherwords,
showthatif‖\cdot‖isanormon\mathcal{U} satisfyingtheparallelogramequality,then
thereisaninnerproduct\langle\cdot,\cdot\rangleon\mathcal{U} suchthat‖u‖=\langleu,u\rangle1/2 forallu\in\mathcal{U}).
| 29  | Suppose\mathcal{V}                 | ,…,\mathcal{V} areinnerproductspaces. |           | Showthattheequation |      |
| --- | ------------------------ | --------------------------- | --------- | ------------------- | ---- |
|     |                          | 1 m                         |           |                     |      |
|     |                          | \langle(u ,…,u                    | ),(v ,…,v | )\rangle=\langleu ,v \rangle+⋯+\langleu     | ,v \rangle |
|     |                          | 1 m                         | 1         | m 1 1               | m m  |
|     | definesaninnerproducton\mathcal{V} |                             | \times⋯\times\mathcal{V}      | .                   |      |
|     |                          |                             | 1         | m                   |      |
Intheexpressionaboveontheright,foreachk=1,…,m,theinnerproduct
|     | \langleu ,v | \rangledenotestheinnerproducton\mathcal{V} |     | . Eachofthespaces\mathcal{V} | ,…,\mathcal{V} may |
| --- | ----- | -------------------------- | --- | ------------------ | -------- |
|     | k k   |                            |     | k                  | 1 m      |
haveadifferentinnerproduct,eventhoughthesamenotationisusedhere.
| 30  | Suppose\mathcal{V} | isarealinnerproductspace. |                              | Foru,v,w,x | \in\mathcal{V},define |
| --- | -------- | ------------------------- | ---------------------------- | ---------- | --------- |
|     |          | \langleu+iv,w+ix\rangle               | =\langleu,w\rangle+\langlev,x\rangle+(\langlev,w\rangle-\langleu,x\rangle)i. |            |           |
\mathbf{C}
|     | (a) Showthat\langle\cdot,\cdot\rangle        | makes\mathcal{V} | intoacomplexinnerproductspace. |     |     |
| --- | ------------------------ | ------ | ------------------------------ | --- | --- |
|     |                          | \mathbf{C}      | \mathbf{C}                              |     |     |
|     | (b) Showthatifu,v\in\mathcal{V},then |        |                                |     |     |
$$2 =‖u‖2+‖v‖2.$$
|     |     | \langleu,v\rangle | =\langleu,v\rangle and | ‖u+iv‖ |     |
| --- | --- | ----- | ---------- | ------ | --- |
|     |     | \mathbf{C}     |            | \mathbf{C}      |     |
See Exercise8in Section1Bforthedefinitionofthecomplexification\mathcal{V} .
\mathbf{C}

| --- | --- | --------- | --------------------- | --- |
| 31 Supposeu,v,w\in\mathcal{V}. | Provethat |               |     |        |
| ------------------ | --------- | ------------- | --- | ------ |
|                    |           | ‖w-u‖2+‖w-v‖2 |     | ‖u-v‖2 |
1(u+v)∥2
|     | ∥w- | =   |     | - . |
| --- | --- | --- | --- | --- |
32 Suppose that \mathcal{E} is a subset of \mathcal{V} with the property that u,v \in \mathcal{E} implies
1(u+v)\in\mathcal{E}.
|     | Letw\in\mathcal{V}. | Showthatthereisatmostonepointin\mathcal{E}thatis |     |     |
| --- | ------- | -------------------------------------- | --- | --- |
| closesttow. | Inotherwords,showthatthereisatmostoneu\in\mathcal{E}suchthat |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- |
‖w-u‖\leq‖w-x‖
| forallx                                           | \in\mathcal{E}.                                |                               |     |          |
| ------------------------------------------------- | ---------------------------------- | ----------------------------- | --- | -------- |
| 33 Suppose                                        | f,garedifferentiablefunctionsfrom\mathbf{R} |                               |     | to\mathbf{R}n.    |
| (a) Showthat                                      |                                    |                               |     |          |
|                                                   | \langlef(t),g(t)\rangle                        | ′ =\langlef′(t),g(t)\rangle+\langlef(t),g′(t)\rangle. |     |          |
| (b) Supposecisapositivenumberand∥f(t)∥=cforeveryt |                                    |                               |     | \in\mathbf{R}. Show |
that\langlef′(t), f(t)\rangle=0foreveryt\in\mathbf{R}.
$$(c) Interprettheresultin(b)geometricallyintermsofthetangentvectorto$$
| acurvelyingonaspherein\mathbf{R}n |                                                        |     | centeredattheorigin. |     |
| ------------------------ | ------------------------------------------------------ | --- | -------------------- | --- |
|                          | f∶ \rightarrow\mathbf{R}niscalleddifferentiableifthereexistdifferentiable |     |                      |     |
| Afunction                | \mathbf{R}                                                      |     |                      |     |
functions f ,…, f from\mathbf{R}to\mathbf{R}suchthat f(t)=(f (t),…, f (t))foreach
|     | 1 n |     |     | 1 n |
| --- | --- | --- | --- | --- |
t\in\mathbf{R}. Furthermore,foreacht\in\mathbf{R},thederivative f′(t)\in\mathbf{R}nisdefinedby
| f′(t)=(f | ′(t),…, ′(t)). |     |     |     |
| -------- | -------------- | --- | --- | --- |
f
|     | 1 n |     |     |     |
| --- | --- | --- | --- | --- |
34 Useinnerproductstoprove Apollonius’sidentity: Inatrianglewithsidesof
lengtha,b,andc,letdbethelengthofthelinesegmentfromthemidpoint
| ofthesideoflengthctotheoppositevertex. |     |     | Then |     |
| -------------------------------------- | --- | --- | ---- | --- |
1c2+2d2.
a2+b2 =

| -------- | ------------------ | --- | --- |
35 Fix a positive integer n. The Laplacian \Deltap of a twice differentiable real-
| valuedfunctionpon\mathbf{R}n | isthefunctionon\mathbf{R}n | definedby |     |
| ------------------- | ----------------- | --------- | --- |
𝜕2p 𝜕2p
|     | \Deltap= | +⋯+ . |     |
| --- | --- | ----- | --- |
𝜕x2 𝜕x2
1 n
Thefunctionpiscalledharmonicif\Deltap=0.
| Apolynomialon\mathbf{R}n | isalinearcombination(withcoefficientsin\mathbf{R})of |     |     |
| --------------- | ------------------------------------------- | --- | --- |
functionsoftheformx m 1⋯x m n,wherem ,…,m arenonnegativeintegers.
|                            | 1 n                        | 1 n                           |                |
| -------------------------- | -------------------------- | ----------------------------- | -------------- |
| Supposeqisapolynomialon\mathbf{R}n. |                            | Provethatthereexistsaharmonic |                |
| polynomialpon\mathbf{R}n            | suchthatp(x)=q(x)foreveryx |                               | \in\mathbf{R}n with‖x‖=1. |
Theonlyfactaboutharmonicfunctionsthatyouneedforthisexerciseis
| thatifpisaharmonicfunctionon\mathbf{R}n |     | andp(x) = | 0forallx \in \mathbf{R}n with |
| ------------------------------ | --- | --------- | ------------------ |
‖x‖=1,thenp=0.
Hint:Areasonableguessisthatthedesiredharmonicpolynomialpisofthe
formq+(1-‖x‖2)rforsomepolynomialr. Provethatthereisapolynomial
ron\mathbf{R}nsuchthatq+(1-‖x‖2)risharmonicbydefininganoperator\mathcal{T}on
asuitablevectorspaceby
\mathcal{T}r=\Delta((1-‖x‖2)r)
andthenshowingthat\mathcal{T}isinjectiveandhencesurjective.
Inrealmsofnumbers,wherethesecretslie,
Anobletruthemergesfromthedeep,
Cauchyand Schwarz,theirwisdomtheyapply,
Aninequalityforalltokeep.
Twovectors,bythisbond,areintertwined,
Asinnerproductsweaveagildedthread,
Theirmagnitude,byprovidence,confined,
Aboundtowhichtheirdestinyiswed.
Thoughshadowsfall,andtwilightdimstheday,
Thisinequalitywillstandthetest,
Toguideusinourquest,tolighttheway,
Andinitstruth,ourunderstandingrest.
Sosing,yemuses,ofthisnoblefeat,
Cauchy–Schwarz,theboundthatnonecanbeat.
—writtenby Chat GPTwithinput Shakespeareansonneton Cauchy–Schwarzinequality

| --- | --- | --- | --- | --- | --------- | ---------------- | --- |
| 6B          | Orthonormal |       | Bases |     |              |           |     |
| ----------- | ----------- | ----- | ----- | --- | ------------ | --------- | --- |
| Orthonormal |             | Lists | and   | the | Gram–Schmidt | Procedure |     |
orthonormal
**6.22 定义：** • Alistofvectorsiscalledorthonormalifeachvectorinthelisthasnorm1
andisorthogonaltoalltheothervectorsinthelist.
| •   | Inotherwords,aliste |     |     | ,…,e | ofvectorsin\mathcal{V} | isorthonormalif |     |
| --- | ------------------- | --- | --- | ---- | ------------ | --------------- | --- |
|     |                     |     |     | 1    | m            |                 |     |
⎧
|     |     |     |     |      | {1  | ifj =k, |     |
| --- | --- | --- | --- | ---- | --- | ------- | --- |
|     |     |     |     | \langlee,e | \rangle=  |         |     |
j k ⎨
|     |     |     |     |     | {0  | ifj \neqk |     |
| --- | --- | --- | --- | --- | --- | ------ | --- |
⎩
|      | forallj,k            | \in{1,…,m}.        |     |                               |       |                           |     |
| ---- | -------------------- | ---------------- | --- | ----------------------------- | ----- | ------------------------- | --- |
| 6.23 | example:             | orthonormallists |     |                               |       |                           |     |
| (a)  | Thestandardbasisof\mathbf{F}n |                  |     | isanorthonormallist.          |       |                           |     |
|      | 1                    | 1 1              | 1   | 1 ,0)isanorthonormallistin\mathbf{F}3. |       |                           |     |
| (b)  | ( ,                  | , ),(-           | ,   |                               |       |                           |     |
|      | \sqrt3                   | \sqrt3 \sqrt3            | \sqrt2  | \sqrt2                            |       |                           |     |
|      | 1                    | 1 1              | 1   | 1                             | 1 1   | 2                         |     |
| (c)  | ( ,                  | , ),(-           | ,   | ,0),(                         | , ,-  | )isanorthonormallistin\mathbf{F}3. |     |
|      | \sqrt3                   | \sqrt3 \sqrt3            | \sqrt2  | \sqrt2                            | \sqrt6 \sqrt6 | \sqrt6                        |     |
$$(d) Supposenisapositiveinteger. Then,as Exercise4asksyoutoverify,$$
|     |     | 1   | cosx | cos2x | cosnx | sinx sin2x | sinnx |
| --- | --- | --- | ---- | ----- | ----- | ---------- | ----- |
|     |     |     | ,    | ,     | ,…,   | , , ,…,    |       |
|     |     |     | \sqrt    | \sqrt     | \sqrt     | \sqrt \sqrt        | \sqrt     |
$$|     |     | \sqrt2\pi | \pi    | \pi     | \pi     | \pi \pi        | \pi     |$$
isanorthonormallistofvectorsin\mathcal{C}[-\pi,\pi],thevectorspaceofcontinuous
real-valuedfunctionson[-\pi,\pi]withinnerproduct
\pi
|     |     |     |     |     | \langlef,g\rangle=\int | fg. |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |
-\pi
Theorthonormallistaboveisoftenusedformodelingperiodicphenomena,
suchastides.
$$(e) Supposewemake𝒫 (\mathbf{R})intoaninnerproductspaceusingtheinnerproduct$$
givenby
|     |     |     |     |     | \langlep,q\rangle=\int | pq  |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |
-1
forallp,q\in𝒫 (\mathbf{R}). Thestandardbasis1,x,x2 of𝒫 (\mathbf{R})isnotanorthonor-
| --- | --- | --- | --- | --- | --- | --- | --- |
mallistbecausethevectorsinthatlistdonothavenorm1. Dividingeach
vectorbyitsnormgivesthelist1/\sqrt2,\sqrt3/2x,\sqrt5/2x2,inwhicheachvector
hasnorm1,andthesecondvectorisorthogonaltothefirstandthirdvectors.
However,thefirstandthirdvectorsarenotorthogonal. Thusthisisnotan
orthonormallist. Soonwewillseehowtoconstructanorthonormallistfrom
|     | thestandardbasis1,x,x2 |     |     | (see Example6.34). |     |     |     |
| --- | ---------------------- | --- | --- | ----------------- | --- | --- | --- |

| --- | -------- | --- | ------------------ | --- | --- | --- | --- | --- |
Orthonormallistsareparticularlyeasytoworkwith,asillustratedbythenext
result.
6.24 normofanorthonormallinearcombination
| Supposee | ,…,e | isanorthonormallistofvectorsin\mathcal{V}. |     |     |     | Then |     |     |
| -------- | ---- | -------------------------------- | --- | --- | --- | ---- | --- | --- |
1 m
|         |      |     | +⋯+a | ‖2    | |2+⋯+|a | |2  |     |     |
| ------- | ---- | --- | ---- | ----- | ------- | --- | --- | --- |
|         |      | ‖a  | e    | e =|a |         |     |     |     |
|         |      |     | 1 1  | m m   | 1       | m   |     |     |
| foralla | ,…,a | \in\mathbf{F}. |      |       |         |     |     |     |
|         | 1    | m   |      |       |         |     |     |     |
Proof Becauseeache hasnorm1,thisfollowsfromrepeatedapplicationsof
k
the Pythagoreantheorem(6.12).
Theresultabovehasthefollowingimportantcorollary.
orthonormallistsarelinearlyindependent
6.25
Everyorthonormallistofvectorsislinearlyindependent.
|       |          | ,…,e |                                     |     |     |     | ,…,a |     |
| ----- | -------- | ---- | ----------------------------------- | --- | --- | --- | ---- | --- |
| Proof | Supposee |      | isanorthonormallistofvectorsin\mathcal{V}anda |     |     |     |      | \in\mathbf{F}  |
|       |          | 1    | m                                   |     |     |     | 1    | m   |
aresuchthat
+⋯+a
|        |                        |     |                                   | a e   | e =0. |     |         |      |
| ------ | ---------------------- | --- | --------------------------------- | ----- | ----- | --- | ------- | ---- |
|        |                        |     |                                   | 1 1 m | m     |     |         |      |
|        | |2+⋯+|a                | |2  |                                   |       |       |     |         |      |
| Then|a |                        |     | = 0(by6.24),whichmeansthatallthea |       |       |     | ’sare0. | Thus |
|        | 1                      | m   |                                   |       |       |     | k       |      |
| e ,…,e | islinearlyindependent. |     |                                   |       |       |     |         |      |
1 m
Nowwecometoanimportantinequality.
6.26 Bessel’sinequality
,…,e
| Supposee |     | isanorthonormallistofvectorsin\mathcal{V}. |     |     |     | Ifv\in\mathcal{V} | then |     |
| -------- | --- | -------------------------------- | --- | --- | --- | ----- | ---- | --- |
1 m
|     |     |     |     | \rangle∣2+⋯+∣\langlev,e | \rangle∣2 \leq‖v‖2. |     |     |     |
| --- | --- | --- | --- | ----------- | ---------- | --- | --- | --- |
∣\langlev,e
|       |                            |     |      | 1           | m                  |     |     |     |
| ----- | -------------------------- | --- | ---- | ----------- | ------------------ | --- | --- | --- |
| Proof | Supposev\in\mathcal{V}.                |     | Then |             |                    |     |     |     |
|       | v=\langle⏟v,⏟e⏟\ranglee⏟+⏟⋯+⏟\langlev⏟,e⏟\rangle⏟e |     |      | +⏟v-⏟\langle⏟v,⏟e | \rangle⏟e⏟-⋯⏟-⏟\langlev⏟,e⏟\rangle⏟e |     | .   |     |
|       |                            | 1 1 |      | m m         | 1                  | 1   | m m |     |
|       |                            |     | u    |             |                    | w   |     |     |
Let u and w be defined as in the equation above. If k \in {1,…,m}, then
| \langlew,e | \langlev,e |     | \langlev,e | ,e          |         |      | \langlew,u\rangle |        |
| ---- | ---- | --- | ---- | ----------- | ------- | ---- | ----- | ------ |
|      | \rangle =  | \rangle - | \rangle\langlee  | \rangle = 0. This | implies | that | =     | 0. The |
|      | k    | k   | k    | k k         |         |      |       |        |
Pythagoreantheoremnowimpliesthat
|     |     |     | ‖v‖2 | =‖u‖2+‖w‖2 |     |     |     |     |
| --- | --- | --- | ---- | ---------- | --- | --- | --- | --- |
\geq‖u‖2
|     |     |     |     | =∣\langlev,e \rangle∣2+⋯+∣\langlev,e |     | \rangle∣2, |     |     |
| --- | --- | --- | --- | ------------------ | --- | ---- | --- | --- |
|     |     |     |     | 1                  |     | m    |     |     |
wherethelastlinecomesfrom6.24.

| --- | --- | --- | --- | --------- | ---------------- | --- | --- |
Thenextdefinitionintroducesoneofthemostusefulconceptsinthestudyof
innerproductspaces.
| 6.27 | definition: | orthonormalbasis |     |     |     |     |     |
| ---- | ----------- | ---------------- | --- | --- | --- | --- | --- |
Anorthonormalbasisof\mathcal{V} isanorthonormallistofvectorsin\mathcal{V} thatisalsoa
basisof\mathcal{V}.
Forexample,thestandardbasisisanorthonormalbasisof\mathbf{F}n.
6.28 orthonormallistsoftherightlengthareorthonormalbases
Suppose\mathcal{V} isfinite-dimensional. Theneveryorthonormallistofvectorsin\mathcal{V}
| oflengthdim\mathcal{V} |     | isanorthonormalbasisof\mathcal{V}. |     |     |     |     |     |
| ------------ | --- | ------------------------ | --- | --- | --- | --- | --- |
By6.25,everyorthonormallistofvectorsin\mathcal{V} islinearlyindependent.
Proof
Thuseverysuchlistoftherightlengthisabasis—see2.38.
\mathbf{F}4
| 6.29 | example: | anorthonormalbasisof |     |     |     |     |     |
| ---- | -------- | -------------------- | --- | --- | --- | --- | --- |
Asmentionedabove,thestandardbasisisanorthonormalbasisof\mathbf{F}4. Wenow
showthat
$$(1,1,1,1),(1,1,-1,-1),(1,-1,-1,1),(-1,1,-1,1)$$
|     | 2   | 2 2 2 | 2 2 2 | 2 2 | 2 2 2 | 2 2 | 2 2 |
| --- | --- | ----- | ----- | --- | ----- | --- | --- |
isalsoanorthonormalbasisof\mathbf{F}4.
Wehave
|     |     | ∥(1,1,1,1)∥=\sqrt1 |       | 1     | 1   | 1   |     |
| --- | --- | -------------- | ----- | ----- | --- | --- | --- |
|     |     |                |       | +     | + + | =1. |     |
|     |     | 2              | 2 2 2 | 22 22 | 22  | 22  |     |
Similarly,theotherthreevectorsinthelistabovealsohavenorm1.
Notethat
| \langle(1,1,1,1),(1,1,-1,-1)\rangle= |       |     |     | 1 \cdot 1 + 1 | \cdot 1 + 1 \cdot(-1)+ | 1   | \cdot(-1)=0. |
| ------------------------ | ----- | --- | --- | --------- | -------------- | --- | -------- |
| 2                        | 2 2 2 | 2 2 | 2 2 | 2 2 2     | 2 2            | 2 2 | 2        |
Similarly, the inner product of any two distinct vectors in the list above also
equals0.
Thusthelistaboveisorthonormal. Becausewehaveanorthonormallistof
lengthfourinthefour-dimensionalvectorspace\mathbf{F}4, thislistisanorthonormal
| basisof\mathbf{F}4              | (by6.28). |     |      |                                  |     |     |     |
| ---------------------- | --------- | --- | ---- | -------------------------------- | --- | --- | --- |
| Ingeneral,givenabasise |           |     | ,…,e | of\mathcal{V}andavectorv\in\mathcal{V},weknowthatthere |     |     |     |
1 n
| issomechoiceofscalarsa |     |     | ,…,a | \in\mathbf{F} suchthat |     |     |     |
| ---------------------- | --- | --- | ---- | ----------- | --- | --- | --- |
|                        |     |     | 1    | n           |     |     |     |
|                        |     |     | v=a  | e +⋯+a      | e . |     |     |
|                        |     |     |      | 1 1         | n n |     |     |
Computingthenumbersa ,…,a thatsatisfytheequationabovecanbealong
|     |     |     | 1   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
computationforanarbitrarybasisof\mathcal{V}. Thenextresultshows,however,thatthis
| iseasyforanorthonormalbasis—justtakea |     |     |     |     | =\langlev,e | \rangle.  |     |
| ------------------------------------- | --- | --- | --- | --- | ----- | --- | --- |
|                                       |     |     |     |     | k k   |     |     |

200 Chapter 6 Inner Product Spaces
Notice how the next result makes
The formula below for ‖v‖ is called
each inner product space of dimension
Parseval’sidentity. Itwaspublishedin
n behave like \mathbf{F}n, with the role of the 1799inthecontextof Fourierseries.
coordinates of a vector in \mathbf{F}n played by
\langlev,e \rangle,…,\langlev,e \rangle.
1 n
6.30 writingavectorasalinearcombinationofanorthonormalbasis
Supposee ,…,e isanorthonormalbasisof\mathcal{V} andu,v\in\mathcal{V}. Then
1 n
$$(a) v=\langlev,e \ranglee +⋯+\langlev,e \ranglee ;$$
1 1 n n
$$(b) ‖v‖2 =∣\langlev,e \rangle∣2+⋯+∣\langlev,e \rangle∣2;$$
1 n
$$(c) \langleu,v\rangle=\langleu,e \rangle\langlev,e \rangle+⋯+\langleu,e \rangle\langlev,e \rangle.$$
1 1 n n
Proof Becausee ,…,e isabasisof\mathcal{V},thereexistscalarsa ,…,a suchthat
1 n 1 n
$$v=a e +⋯+a e .$$
1 1 n n
Becausee ,…,e isorthonormal,takingtheinnerproductofbothsidesofthis
1 n
equationwithe gives\langlev,e \rangle=a . Thus(a)holds.
k k k
Now(b)followsimmediatelyfrom(a)and6.24.
Take the inner product of u with eachside of (a) and then get(c) by using
conjugatelinearity[6.6(d)and6.6(e)]inthesecondslotoftheinnerproduct.
**6.31 例：** findingcoefficientsforalinearcombination
Supposewewanttowritethevector(1,2,4,7)\in\mathbf{F}4 asalinearcombination
oftheorthonormalbasis
$$(1,1,1,1),(1,1,-1,-1),(1,-1,-1,1),(-1,1,-1,1)$$
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
of\mathbf{F}4 from Example6.29. Insteadofsolvingasystemoffourlinearequations
in four unknowns, as typically would be required if we were working with a
nonorthonormalbasis,wesimplyevaluatefourinnerproductsanduse6.30(a),
gettingthat(1,2,4,7)equals
7(1,1,1,1)-4(1,1,-1,-1)+(1,-1,-1,1)+2(-1,1,-1,1).
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
Nowthatweunderstandtheusefulnessoforthonormalbases,howdowego
aboutfindingthem? Forexample,does𝒫 (\mathbf{R})withinnerproductasin6.3(c)
m
haveanorthonormalbasis? Thenextresultwillleadtoanswerstothesequestions.
Thealgorithmusedinthenextproof
Jørgen Gram(1850–1916)and Erhard
is called the Gram–Schmidt procedure.
Schmidt(1876–1959)popularizedthis
It gives a method for turning a linearly
algorithmthatconstructsorthonormal
independentlistintoanorthonormallist lists.
withthesamespanastheoriginallist.

Section6B Orthonormal Bases 201
6.32 Gram–Schmidtprocedure
Supposev ,…,v isalinearlyindependentlistofvectorsin\mathcal{V}. Let f =v .
1 m 1 1
Fork =2,…,m,define f inductivelyby
k
\langlev , f \rangle \langlev , f \rangle
$$f =v - k 1 f -⋯- k k-1 f .$$
k k ‖f ‖2 1 ‖f ‖2 k-1
1 k-1
f
Foreachk =1,…,m,lete = k . Thene ,…,e isanorthonormallistof
k ‖f ‖ 1 m
vectorsin\mathcal{V} suchthat k
span(v ,…,v )=span(e ,…,e )
1 k 1 k
foreachk =1,…,m.
Proof Wewillshowbyinductionon k thatthedesiredconclusion holds. To
getstartedwithk = 1, notethatbecausee = f /‖f ‖, wehave‖e ‖ = 1; also,
1 1 1 1
span(v )=span(e )becausee isanonzeromultipleofv .
1 1 1 1
Suppose1<k \leqmandtheliste ,…,e generatedby6.32isanorthonormal
1 k-1
listsuchthat
6.33 span(v ,…,v )=span(e ,…,e ).
1 k-1 1 k-1
Becausev ,…,v islinearlyindependent,wehavev \notinspan(v ,…,v ). Thus
1 m k 1 k-1
v \notin span(e ,…,e ) = span(f ,…, f ),whichimpliesthat f \neq 0. Hence
k 1 k-1 1 k-1 k
wearenotdividingby0inthedefinitionofe givenin6.32. Dividingavectorby
k
itsnormproducesanewvectorwithnorm1;thus‖e ‖=1.
k
Letj \in{1,…,k-1}. Then
\langlee ,e\rangle= \langlef , f\rangle
k j ‖f ‖‖f‖ k j
k j
1 \langlev , f \rangle \langlev , f \rangle
= \langlev - k 1 f -⋯- k k-1 f , f\rangle
‖f ‖‖f‖ k ‖f ‖2 1 ‖f ‖2 k-1 j
k j 1 k-1
= (\langlev , f\rangle-\langlev , f\rangle)
‖f ‖‖f‖ k j k j
k j
=0.
Thuse ,…,e isanorthonormallist.
1 k
From the definition of e given in 6.32, we see that v \in span(e ,…,e ).
k k 1 k
Combiningthisinformationwith6.33showsthat
span(v ,…,v )\subseteqspan(e ,…,e ).
1 k 1 k
Bothlistsabovearelinearlyindependent(thev’sbyhypothesis,andthee’sby
orthonormality and 6.25). Thus both subspaces above have dimension k, and
hence they are equal, completing the induction step and thus completing the
proof.

| --- | -------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
|               |     | anorthonormalbasisof |     |     | 𝒫 (\mathbf{R}) |     |     |     |     |
| ------------- | --- | -------------------- | --- | --- | ----- | --- | --- | --- | --- |
| 6.34 example: |     |                      |     |     | 2     |     |     |     |     |
Supposewemake𝒫 (\mathbf{R})intoaninnerproductspaceusingtheinnerproduct
givenby
|     |     |     |     | \langlep,q\rangle=\int |     | pq  |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
-1
| forallp,q | 𝒫   |      | Weknowthat1,x,x2 |     | isabasisof𝒫 |     |     |                  |     |
| --------- | --- | ---- | ---------------- | --- | ----------- | --- | --- | ---------------- | --- |
|           | \in   | (\mathbf{R}). |                  |     |             |     |     | (\mathbf{R}),butitisnotan |     |
orthonormalbasis. Wewillfindanorthonormalbasisof𝒫 (\mathbf{R})byapplyingthe
=x2.
| Gram–Schmidtprocedurewithv |     |     |     | =1,v | =x,andv |     |     |     |     |
| -------------------------- | --- | --- | --- | ---- | ------- | --- | --- | --- | --- |
Togetstarted,take f =v =1. Thus‖f ‖2 =\int 1 1=2. Hencetheformula
|     |     |     | 1   | 1   | 1   |     | -1  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in6.32tellsusthat
|     |     |     |     | \langlev , f \rangle |       | \langlex,1\rangle |     |     |     |
| --- | --- | --- | --- | -------- | ----- | ----- | --- | --- | --- |
|     |     | f   | =v  | - 2 1    | f =x- |       | =x, |     |     |
|     |     |     | 2 2 |          | 1     |       |     |     |     |
|     |     |     |     | ‖f ‖2    |       | ‖f    | ‖2  |     |     |
| wherethelastequalityholdsbecause\langlex,1\rangle=\int |     |     |     |     |     | tdt=0. |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
-1
|                    |     |     |     |               |     | 1   |       | 2.            |     |
| ------------------ | --- | --- | --- | ------------- | --- | --- | ----- | ------------- | --- |
| Theformulaabovefor |     |     | f   | impliesthat‖f | ‖2  | =\int  | t2dt= | Nowtheformula |     |
|                    |     |     | 2   |               | 2   | -1  |       | 3             |     |
in6.32tellsusthat
|                    |     | ,          |     | ,           |     |          |          |      |     |
| ------------------ | --- | ---------- | --- | ----------- | --- | -------- | -------- | ---- | --- |
|                    |     | \langlev 3 f 1 \rangle | \langlev  | 3 f 2 \rangle     |     | 1\langlex2,1\rangle- | 3\langlex2,x\ranglex |      | 1.  |
| f =v               | -   |            | f - | f =x2-      |     |          |          | =x2- |     |
| 3                  | 3   | ‖f ‖2      | 1   | ‖f ‖2 2     |     | 2        | 2        |      | 3   |
| Theformulaabovefor |     |            | f   | impliesthat |     |          |          |      |     |
| --- | --- | ----- | ---- | ------- | ---- | ---- | ----- | --- | --- |
|     | ‖f  | ‖2 =\int | (t2- | 1) dt=\int | (t4- | 2t2+ | 1)dt= | 8 . |     |
|     |     | 3     |      | 3       |      | 3    | 9     | 45  |     |
|     |     |       | -1   |         | -1   |      |       |     |     |
Nowdividingeachof f , f , f byitsnormgivesustheorthonormallist
|     |     |     | 1              | 2 3 |     |     |     |     |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | \sqrt1,\sqrt3x,\sqrt45(x2- |     |     | 1). |     |     |     |
|     |     |     |                | 2 2 | 8   | 3   |     |     |     |
Theorthonormallistabovehaslengththree,whichisthedimensionof𝒫 (\mathbf{R}).
| Hencethisorthonormallistisanorthonormalbasisof𝒫 |     |     |     |     |     |     | (\mathbf{R})[by6.28]. |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- |
Nowwecananswerthequestionabouttheexistenceoforthonormalbases.
6.35 existenceoforthonormalbasis
Everyfinite-dimensionalinnerproductspacehasanorthonormalbasis.
Suppose\mathcal{V} isfinite-dimensional. Chooseabasisof\mathcal{V}. Applythe Gram–
Proof
Schmidtprocedure(6.32)toit,producinganorthonormallistoflengthdim\mathcal{V}.
By6.28,thisorthonormallistisanorthonormalbasisof\mathcal{V}.
Sometimesweneedtoknownotonlythatanorthonormalbasisexists,butalso
thateveryorthonormallistcanbeextendedtoanorthonormalbasis. Inthenext
corollary,the Gram–Schmidtprocedureshowsthatsuchanextensionisalways
possible.

| --- | --- | --- | --------- | ---------------- | --- |
everyorthonormallistextendstoanorthonormalbasis
6.36
Suppose\mathcal{V} isfinite-dimensional. Theneveryorthonormallistofvectorsin\mathcal{V}
canbeextendedtoanorthonormalbasisof\mathcal{V}.
Proof Supposee ,…,e isanorthonormallistofvectorsin\mathcal{V}. Thene ,…,e
|     | 1   | m   |     |     | 1 m |
| --- | --- | --- | --- | --- | --- |
is linearly independent (by 6.25). Hence this list can be extended to a basis
e ,…,e ,v ,…,v of \mathcal{V} (see 2.32). Now apply the Gram–Schmidt procedure
| 1         | m 1 n   |                                  |              |     |     |
| --------- | ------- | -------------------------------- | ------------ | --- | --- |
| (6.32)toe | ,…,e ,v | ,…,v ,producinganorthonormallist |              |     |     |
|           | 1 m     | 1 n                              |              |     |     |
|           |         | e                                | ,…,e , f ,…, | f ; |     |
|           |         | 1                                | m 1          | n   |     |
heretheformulagivenbythe Gram–Schmidtprocedureleavesthefirstmvectors
unchangedbecausetheyarealreadyorthonormal. Thelistaboveisanorthonormal
basisof\mathcal{V} by6.28.
Recallthatamatrixiscalleduppertriangularifitlookslikethis:
∗ ∗
|     |     |     | ⎛ ⎜ | ⎞ ⎟ |     |
| --- | --- | --- | --- | --- | --- |
|     |     |     | ⎜ ⋱ | ⎟ , |     |
|     |     |     | ⎜   | ⎟   |     |
∗
|     |     |     | ⎝ 0 | ⎠   |     |
| --- | --- | --- | --- | --- | --- |
where the 0 in the matrix above indicates that all entries below the diagonal
equal0,andasterisksareusedtodenoteentriesonandabovethediagonal.
Inthelastchapter,wegaveanecessaryandsufficientconditionforanoperator
tohaveanupper-triangularmatrixwithrespecttosomebasis(see5.44). Nowthat
wearedealingwithinnerproductspaces,wewouldliketoknowwhetherthere
existsanorthonormalbasiswithrespecttowhichwehaveanupper-triangular
matrix. Thenextresultshowsthattheconditionforanoperatortohaveanuppertriangular matrix with respect to some orthonormal basis is the same as the
conditiontohaveanupper-triangularmatrixwithrespecttoanarbitrarybasis.
6.37 upper-triangularmatrixwithrespecttosomeorthonormalbasis
| Suppose | is finite-dimensional |     | and | ℒ(\mathcal{V}). Then | has an upper- |
| ------- | --------------------- | --- | --- | ---------- | ------------- |
|         | \mathcal{V}                     |     | \mathcal{T} \in |            | \mathcal{T}             |
triangularmatrixwithrespecttosomeorthonormalbasisof\mathcal{V}ifandonlyifthe
| minimalpolynomialof\mathcal{T}equals(z-\lambda |     |     |          | )forsome | ,…,\lambda \in\mathbf{F}. |
| ------------------------------ | --- | --- | -------- | -------- | -------- |
|                                |     |     | 1 )⋯(z-\lambda | m        | \lambda 1 m    |
Proof Suppose \mathcal{T} has an upper-triangular matrix with respect to some basis
v ,…,v of\mathcal{V}. Thusspan(v ,…,v )isinvariantunder\mathcal{T} foreachk = 1,…,n
| 1   | n   | 1   | k   |     |     |
| --- | --- | --- | --- | --- | --- |
$$(see5.39).$$
Applythe Gram–Schmidtproceduretov ,…,v ,producinganorthonormal
|        |           |             |          | 1 n    |     |
| ------ | --------- | ----------- | -------- | ------ | --- |
| basise | ,…,e of\mathcal{V}. | Because     |          |        |     |
|        | 1 n       |             |          |        |     |
|        |           | span(e ,…,e | )=span(v | ,…,v ) |     |
|        |           | 1           | k        | 1 k    |     |
foreachk (see6.32),weconcludethatspan(e ,…,e )isinvariantunder\mathcal{T} for
1 k
eachk =1,…,n. Thus,by5.39,\mathcal{T} hasanupper-triangularmatrixwithrespectto
| theorthonormalbasise |     | ,…,e . | Nowuse5.44tocompletetheproof. |     |     |
| -------------------- | --- | ------ | ----------------------------- | --- | --- |
1 n

| -------- | ------------------ | --- | --- | --- |
Forcomplexvectorspaces,thenext
Issai Schur(1875–1941)publisheda
resultisanimportantapplicationofthe
proofofthenextresultin1909.
| resultabove. | See Exercise20foraver- |     |     |     |
| ------------ | --------------------- | --- | --- | --- |
sionof Schur’stheoremthatappliessimultaneouslytomorethanoneoperator.
6.38 Schur’stheorem
Everyoperatoronafinite-dimensionalcomplexinnerproductspacehasan
upper-triangularmatrixwithrespecttosomeorthonormalbasis.
theoremofalgebra(4.13)and6.37.
| Linear Functionals | on  | Inner Product | Spaces |     |
| ------------------ | --- | ------------- | ------ | --- |
Becauselinearmapsintothescalarfield\mathbf{F}playaspecialrole,wedefinedaspecial
nameforthemandtheirvectorspacein Section3F.Thosedefinitionsarerepeated
belowincaseyouskipped Section3F.
| 6.39 definition:     | linearfunctional,dualspace,\mathcal{V}′ |                   |     |      |
| -------------------- | ----------------------------- | ----------------- | --- | ---- |
| Alinearfunctionalon\mathcal{V} |                               | isalinearmapfrom\mathcal{V} |     | to\mathbf{F}. |
•
• The dual space of \mathcal{V}, denoted by \mathcal{V}′, is the vector space of all linear
|     | Inotherwords,\mathcal{V}′ |     | =ℒ(\mathcal{V},\mathbf{F}). |     |
| --- | --------------- | --- | -------- | --- |
functionalson\mathcal{V}.
| 6.40 example: | linearfunctionalon\mathbf{F}3 |     |     |     |
| ------------- | -------------------- | --- | --- | --- |
Thefunction\phi∶
|     | \mathbf{F}3 \rightarrow\mathbf{F} | definedby |          |     |
| --- | ----- | --------- | -------- | --- |
|     |       | \phi(z ,z ,z | )=2z -5z | +z  |
|     |       | 1 2       | 3 1      | 2 3 |
isalinearfunctionalon\mathbf{F}3. Wecouldwritethislinearfunctionalintheform
\phi(z)=\langlez,w\rangle
foreveryz\in\mathbf{F}3,wherew=(2,-5,1).
| 6.41 example: | linearfunctionalon𝒫 |     | (\mathbf{R}) |     |
| ------------- | ------------------- | --- | --- | --- |
| Thefunction\phi∶ | 𝒫     |           |     |     |
| ------------- | ----- | --------- | --- | --- |
|               | (\mathbf{R})\rightarrow\mathbf{R} | definedby |     |     |
|     |     | \phi(p)=\int | p(t)(cos(\pit))dt |     |
| --- | --- | ------ | --------------- | --- |
-1
| isalinearfunctionalon𝒫 |     | (\mathbf{R}). |     |     |
| ---------------------- | --- | ---- | --- | --- |

| --- | --- | --- | --- | --- | --------- | ---------------- | --- | --- |
| If v \in                         | \mathcal{V}, then | the | map that | sends | u   |         |                    |          |
| ------------------------------ | ------- | --- | -------- | ----- | --- | ------- | ------------------ | -------- |
|                                |         |     |          |       | The | next    | result is named    | in honor |
| to\langleu,v\rangleisalinearfunctionalon\mathcal{V}. |         |     |          | The   |     |         |                    |          |
|                                |         |     |          |       | of  | Frigyes | Riesz (1880–1956), | who      |
nextresultstatesthateverylinearfunc- proved several theorems early in the
| tionalon\mathcal{V} | isofthisform. |     | Forexample, |     |     |     |     |     |
| --------- | ------------- | --- | ----------- | --- | --- | --- | --- | --- |
twentiethcenturythatlookverymuch
| we can take | v = | (2,-5,1) | in  | Example | liketheresultbelow. |     |     |     |
| ----------- | --- | -------- | --- | ------- | ------------------- | --- | --- | --- |
6.40.
Suppose we make the vector space 𝒫 (\mathbf{R}) into an inner product space by
defining\langlep,q\rangle=\int 1 pq. Let\phibeasin Example6.41. Itisnotobviousthatthere
-1
| existsq\in𝒫 | (\mathbf{R})suchthat |     |     |     |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
p(t)(cos(\pit))dt=\langlep,q\rangle
\int
-1
foreveryp\in𝒫 (\mathbf{R})[wecannottakeq(t)=cos(\pit)becausethatchoiceofqis
notanelementof𝒫
|     |     | (\mathbf{R})]. | Thenextresulttellsusthesomewhatsurprisingresult |     |     |     |     |     |
| --- | --- | ----- | ----------------------------------------------- | --- | --- | --- | --- | --- |
that there indeed exists a polynomial q \in 𝒫 (\mathbf{R}) such that the equation above
| holdsforallp\in𝒫 |     | (\mathbf{R}). |     |     |     |     |     |     |
| -------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
Rieszrepresentationtheorem
6.42
Suppose\mathcal{V} isfinite-dimensionaland\phiisalinearfunctionalon\mathcal{V}. Thenthere
| isauniquevectorv\in\mathcal{V} |     |     | suchthat |     |     |     |     |     |
| ------------------ | --- | --- | -------- | --- | --- | --- | --- | --- |
\phi(u)=\langleu,v\rangle
foreveryu\in\mathcal{V}.
suchthat\phi(u)=\langleu,v\ranglefor
Proof Firstweshowthatthereexistsavectorv\in\mathcal{V}
| everyu\in\mathcal{V}. | Lete | ,…,e        | beanorthonormalbasisof\mathcal{V}. |      |          |     | Then   |     |
| --------- | ---- | ----------- | ------------------------ | ---- | -------- | --- | ------ | --- |
|           |      | 1           | n                        |      |          |     |        |     |
|           |      | \phi(u)=\phi(\langleu,e |                          | \ranglee   | +⋯+\langleu,e  |     | \ranglee )   |     |
|           |      |             |                          | 1    | 1        | n   | n      |     |
|           |      |             | =\langleu,e                    |      | )+⋯+\langleu,e |     |        |     |
|           |      |             |                          | \rangle\phi(e |          |     | \rangle\phi(e ) |     |
|           |      |             |                          | 1    | 1        |     | n n    |     |
|           |      |             | =\langleu,\phi(e                  | )e   | +⋯+\phi(e   | )e  | \rangle      |     |
|           |      |             |                          | 1    | 1        | n   | n      |     |
foreveryu\in\mathcal{V},wherethefirstequalitycomesfrom6.30(a). Thussetting
|      |     |     | v=\phi(e | )e  | +⋯+\phi(e | )e  | ,   |     |
| ---- | --- | --- | ----- | --- | ------ | --- | --- | --- |
| 6.43 |     |     |       | 1 1 |        | n   | n   |     |
wehave\phi(u)=\langleu,v\rangleforeveryu\in\mathcal{V},asdesired.
Nowweprovethatonlyonevectorv\in\mathcal{V} hasthedesiredbehavior. Suppose
| v ,v \in\mathcal{V} | aresuchthat |     |     |     |     |     |     |     |
| ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
1 2
|              |     |      | \phi(u)=\langleu,v |        | \rangle=\langleu,v | \rangle   |      |     |
| ------------ | --- | ---- | --------- | ------ | ------ | --- | ---- | --- |
| foreveryu\in\mathcal{V}. |     | Then |           |        |        |     |      |     |
|              |     |      | 0=\langleu,v    | \rangle-\langleu,v | \rangle=\langleu,v |     | -v \rangle |     |
|              |     |      |           | 1      | 2      | 1   | 2    |     |
for every u \in \mathcal{V}. Taking u = v -v shows that v -v = 0. Thus v = v ,
|     |     |     |     | 1   | 2   |     | 1 2 | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
completingtheproofoftheuniquenesspartoftheresult.

| -------- | --- | ------------------ | --- | --- | --- |
computationillustrating Rieszrepresentationtheorem
**6.44 例：** | Supposewewanttofindapolynomialq\in𝒫 |     |     |     | (\mathbf{R})suchthat |     |
| --------------------------------- | --- | --- | --- | ----------- | --- |
| --------------------- | --- | ---- | ----------------- | --------------------- | --- |
| 6.45                  |     | \int    | p(t)(cos(\pit))dt=\int | pq                    |     |
|                       |     | -1   |                   | -1                    |     |
| foreverypolynomialp\in𝒫 |     |      | Todothis,wemake𝒫  |                       |     |
|                       |     | (\mathbf{R}). |                   | (\mathbf{R})intoaninnerproduct |     |
spacebydefining\langlep,q\rangletobetherightsideoftheequationaboveforp,q\in𝒫 (\mathbf{R}).
Note that the left side of the equation above does not equal the inner product
in𝒫 (\mathbf{R})ofpandthefunctiont ↦ cos(\pit)becausethislastfunctionisnota
polynomial.
| Definealinearfunctional\phion𝒫 |     |     | (\mathbf{R})byletting |     |     |
| --------------------------- | --- | --- | ------------ | --- | --- |
|     |     | \phi(p)=\int | p(t)(cos(\pit))dt |     |     |
| --- | --- | ------ | --------------- | --- | --- |
-1
𝒫
for each p \in (\mathbf{R}). Now use the orthonormal basis from Example 6.34 and
applyformula6.43fromtheproofofthe Rieszrepresentationtheoremtoseethat
ifp\in𝒫 (\mathbf{R}),then\phi(p)=\langlep,q\rangle,where
| ------- | --- | -------------- | --- | ---------------- | --- |
|         |     | \sqrt1cos(\pit)dt)\sqrt1 |     | \sqrt3tcos(\pit)dt)\sqrt3x |     |
| q(x)=(\int |     |                | +(\int |                  |     |
|         |     | 2              | 2   | 2                | 2   |
|         | -1  |                | -1  |                  |     |
|     | +(\int | \sqrt45(t2- | 1)cos(\pit)dt)\sqrt45(x2- |     | 1). |
| --- | --- | ------- | ------------------- | --- | --- |
|     |     | -1 8    | 3                   | 8   | 3   |
Abitofcalculusappliedtotheequationaboveshowsthat
|     |     |     | q(x)= (1-3x2). |     |     |
| --- | --- | --- | -------------- | --- | --- |
2\pi2
| Thesameprocedureshowsthatifwewanttofindq\in𝒫 |     |     |     |     | (\mathbf{R})suchthat6.45 |
| ------------------------------------------ | --- | --- | --- | --- | --------------- |
| holdsforallp\in𝒫 | (\mathbf{R}),thenweshouldtake |     |     |     |     |
| -------------- | -------------------- | --- | --- | --- | --- |
105((27-2\pi2)+(24\pi2-270)x2+(315-30\pi2)x4).
q(x)=
8\pi4
Suppose\mathcal{V} isfinite-dimensionaland\phialinearfunctionalon\mathcal{V}. Then6.43
givesaformulaforthevectorvthatsatisfies
\phi(u)=\langleu,v\rangle
| forallu\in\mathcal{V}. | Specifically,wehave |       |           |      |     |
| ---------- | ------------------- | ----- | --------- | ---- | --- |
|            |                     | v=\phi(e | )e +⋯+\phi(e | )e . |     |
|            |                     |       | 1 1       | n n  |     |
Therightsideoftheequationaboveseemstodependontheorthonormalbasis
e ,…,e aswellason\phi. However,6.42tellsusthatvisuniquelydetermined
1 n
by\phi. Thustherightsideoftheequationaboveisthesameregardlessofwhich
| orthonormalbasise |     | ,…,e of\mathcal{V} | ischosen. |     |     |
| ----------------- | --- | -------- | --------- | --- | --- |
|                   | 1   | n        |           |     |     |
Fortwoadditionaldifferentproofsofthe Rieszrepresentationtheorem,see
6.58andalso Exercise13in Section6C.

Section6B Orthonormal Bases 207
Exercises 6B
1 Supposee ,…,e isalistofvectorsin\mathcal{V} suchthat
1 m
‖a e +⋯+a e ‖2 =|a |2+⋯+|a |2
1 1 m m 1 m
foralla ,…,a \in\mathbf{F}. Showthate ,…,e isanorthonormallist.
1 m 1 m
Thisexerciseprovidesaconverseto6.24.
2 (a) Suppose\theta \in\mathbf{R}. Showthatboth
$$(cos\theta,sin\theta),(-sin\theta,cos\theta) and (cos\theta,sin\theta),(sin\theta,-cos\theta)$$
areorthonormalbasesof\mathbf{R}2.
$$(b) Showthateachorthonormalbasisof\mathbf{R}2 isoftheformgivenbyoneof$$
thetwopossibilitiesin(a).
3 Supposee ,…,e isanorthonormallistin\mathcal{V} andv\in\mathcal{V}. Provethat
1 m
‖v‖2 =∣\langlev,e \rangle∣2+⋯+∣\langlev,e \rangle∣2 ⟺ v\inspan(e ,…,e ).
1 m 1 m
4 Supposenisapositiveinteger. Provethat
1 cosx cos2x cosnx sinx sin2x sinnx
, \sqrt , \sqrt ,…, \sqrt , \sqrt , \sqrt ,…, \sqrt
$$\sqrt2\pi \pi \pi \pi \pi \pi \pi$$
isanorthonormallistofvectorsin\mathcal{C}[-\pi,\pi],thevectorspaceofcontinuous
real-valuedfunctionson[-\pi,\pi]withinnerproduct
\pi
\langlef,g\rangle=\int fg.
-\pi
Hint:Thefollowingformulasshouldhelp.
sin(x-y)+sin(x+y)
$$(sinx)(cosy)=$$
cos(x-y)-cos(x+y)
$$(sinx)(siny)=$$
cos(x-y)+cos(x+y)
$$(cosx)(cosy)=$$
5 Suppose f∶ [-\pi,\pi] \rightarrow \mathbf{R} iscontinuous. Foreachnonnegativeintegerk,
define
\pi \pi
a k = \sqrt 1 \pi \int -\pi f(x)cos(kx)dx and b k = \sqrt 1 \pi \int -\pi f(x)sin(kx)dx.
Provethat
$$a2 \infty \pi$$
0 + \sum(a2+b2)\leq\int f2.
2 k=1 k k -\pi
Theinequalityaboveisactuallyanequalityforallcontinuousfunctions
f∶ [-\pi,\pi] \rightarrow \mathbf{R}. However, proving that this inequality is an equality
involves Fourierseriestechniquesbeyondthescopeofthisbook.

| --- | -------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
| 6   | Supposee         | ,…,e isanorthonormalbasisof\mathcal{V}. |     |               |     |          |     |     |     |
| --- | ---------------- | ----------------------------- | --- | ------------- | --- | -------- | --- | --- | --- |
|     |                  | 1 n                           |     |               |     |          |     |     |     |
|     | (a) Provethatifv | ,…,v                          |     | arevectorsin\mathcal{V} |     | suchthat |     |     |     |
|     |                  | 1                             | n   |               |     |          |     |     |     |
|     |                         |     |      | ‖e           | -v  | ‖< \sqrt     |     |     |     |
| --- | ----------------------- | --- | ---- | ------------ | --- | -------- | --- | --- | --- |
|     |                         |     |      |              | k k |          | n   |     |     |
|     | foreachk,thenv          |     | ,…,v | isabasisof\mathcal{V}. |     |          |     |     |     |
|     |                         |     | 1    | n            |     |          |     |     |     |
|     | (b) Showthatthereexistv |     |      | ,…,v         | \in\mathcal{V}  | suchthat |     |     |     |
1 n
|     |               |     |      | ‖e                        | -v  | ‖\leq \sqrt |     |     |     |
| --- | ------------- | --- | ---- | ------------------------- | --- | ---- | --- | --- | --- |
|     |               |     |      |                           | k k |      | n   |     |     |
|     | foreachk,butv |     | ,…,v | isnotlinearlyindependent. |     |      |     |     |     |
|     |               |     | 1    | n                         |     |      |     |     |     |
Thisexercisestatesin(a)thatanappropriatelysmallperturbationofan
\sqrt
|     | orthonormalbasisisabasis. |     |     | Then(b)showsthatthenumber1/ |     |     |     | nonthe |     |
| --- | ------------------------- | --- | --- | --------------------------- | --- | --- | --- | ------ | --- |
rightsideoftheinequalityin(a)cannotbehigher.
7 Suppose\mathcal{T} \inℒ(\mathbf{R}3)hasanupper-triangularmatrixwithrespecttothebasis
$$(1,0,0),(1,1,1),(1,1,2). Findanorthonormalbasisof\mathbf{R}3 withrespectto$$
|     | which\mathcal{T} hasanupper-triangularmatrix. |     |     |     |     |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
1pqforall
| 8   | Make𝒫 (\mathbf{R})intoaninnerproductspacebydefining\langlep,q\rangle |     |     |     |     |     |     | = \int |     |
| --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | p,q\in𝒫 (\mathbf{R}).                                      |     |     |     |     |     |     |     |     |
$$(a) Applythe Gram–Schmidtproceduretothebasis1,x,x2 toproducean$$
|     | orthonormalbasisof𝒫 |     |     | (\mathbf{R}). |     |     |     |     |     |
| --- | ------------------- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     | (b) Thedifferentiationoperator(theoperatorthattakesptop′)on𝒫 |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
2 (\mathbf{R})
hasanupper-triangularmatrixwithrespecttothebasis1,x,x2,whichis
notanorthonormalbasis. Findthematrixofthedifferentiationoperator
on 𝒫 (\mathbf{R}) with respect to the orthonormal basis produced in (a) and
verifythatthismatrixisuppertriangular,asexpectedfromtheproofof
6.37.
9 Supposee ,…,e istheresultofapplyingthe Gram–Schmidtprocedureto
|     |                           | 1 m |     |      |      |             |     |              |     |
| --- | ------------------------- | --- | --- | ---- | ---- | ----------- | --- | ------------ | --- |
|     |                           |     |     | ,…,v |      |             |     | ,e           |     |
|     | alinearlyindependentlistv |     |     |      | in\mathcal{V}. | Provethat\langlev |     | \rangle > 0foreach |     |
|     |                           |     |     | 1    | m    |             |     | k k          |     |
$$k =1,…,m.$$
10 Suppose v ,…,v is a linearly independent list in \mathcal{V}. Explain why the
|     |     | 1 m |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
orthonormallistproducedbytheformulasofthe Gram–Schmidtprocedure
$$(6.32)istheonlyorthonormalliste ,…,e in\mathcal{V} suchthat\langlev ,e \rangle>0and$$
|     |        |          |     |      | 1         | m   |         | k k |     |
| --- | ------ | -------- | --- | ---- | --------- | --- | ------- | --- | --- |
|     | ,…,v   |          |     | ,…,e |           |     | =1,…,m. |     |     |
|     | span(v | )=span(e |     |      | )foreachk |     |         |     |     |
|     | 1      | k        | 1   | k    |           |     |         |     |     |
Theresultinthisexerciseisusedintheproofof7.58.
|     | Findapolynomialq\in𝒫 |      | (\mathbf{R})suchthatp(1)=\int |               |     |     | 1pqforeveryp\in𝒫 |     | (\mathbf{R}). |
| --- | ------------------ | ---- | ----------------- | ------------- | --- | --- | -------------- | --- | ---- |
|     | Findapolynomialq\in𝒫 |      | (\mathbf{R})suchthat       |               |     |     |                |     |      |
|     |                    |      | \int                 | p(x)cos(\pix)dx |     | =\int  | pq             |     |      |
|     | foreveryp\in𝒫        | (\mathbf{R}). |                   |               |     |     |                |     |      |

| --- | --- | --------- | ---------------- | --- |
13 Showthatalistv ,…,v ofvectorsin\mathcal{V} islinearlydependentifandonlyif
1 m
| the Gram–Schmidtformulain6.32produces |     |     | f =0forsomek | \in{1,…,m}. |
| ------------------------------------ | --- | --- | ------------ | --------- |
k
determiningwhetheralistofvectorsinaninnerproductspaceislinearly
dependent.
14 Suppose\mathcal{V} isarealinnerproductspaceandv ,…,v isalinearlyindepen1 m
dentlistofvectorsin\mathcal{V}. Provethatthereexistexactly2m orthonormallists
| e ,…,e ofvectorsin\mathcal{V} |        | suchthat      |        |     |
| ------------------- | ------ | ------------- | ------ | --- |
| 1 m                 |        |               |        |     |
|                     | span(v | ,…,v )=span(e | ,…,e ) |     |
|                     |        | 1 k           | 1 k    |     |
\in{1,…,m}.
forallk
| \langle\cdot,\cdot\rangle      | \langle\cdot,\cdot\rangle |                    |                | \langleu,v\rangle  |
| ---------- | ----- | ------------------ | -------------- | ------ |
| 15 Suppose | and   | are inner products | on \mathcal{V} such that | = 0 if |
|            | 1 2   |                    |                | 1      |
and only if \langleu,v\rangle = 0. Prove that there is a positive number c such that
| \langleu,v\rangle =c\langleu,v\rangle | foreveryu,v\in\mathcal{V}. |     |     |     |
| ------------- | -------------- | --- | --- | --- |
1 2
This exercise shows that if two inner products have the same pairs of
orthogonal vectors, then each of the inner products is a scalar multiple
oftheotherinnerproduct.
16 Suppose\mathcal{V}isfinite-dimensional. Suppose\langle\cdot,\cdot\rangle ,\langle\cdot,\cdot\rangle areinnerproductson
1 2
\mathcal{V} withcorrespondingnorms‖\cdot‖ and‖\cdot‖ . Provethatthereexistsapositive
| ------------------ | ----- | ------------ | --- | --- |
| numbercsuchthat‖v‖ | \leqc‖v‖ | foreveryv\in\mathcal{V}. |     |     |
17 Suppose\mathbf{F} =\mathbf{C} and\mathcal{V} isfinite-dimensional. Provethatif\mathcal{T} isanoperator
on\mathcal{V} suchthat1istheonlyeigenvalueof\mathcal{T} and‖\mathcal{T}v‖ \leq ‖v‖forallv \in \mathcal{V},
| then\mathcal{T} istheidentityoperator. |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- |
18 Supposeu ,…,u isalinearlyindependentlistin\mathcal{V}. Showthatthereexists
1 m
| v\in\mathcal{V} suchthat\langleu | ,v\rangle=1forallk | \in{1,…,m}. |     |     |
| -------------- | ------------ | --------- | --- | --- |
k
19 Supposev ,…,v isabasisof\mathcal{V}. Provethatthereexistsabasisu ,…,u
| 1   | n   |     |     | 1 n |
| --- | --- | --- | --- | --- |
of\mathcal{V} suchthat
⎧
|     |     | {0  | ifj \neqk, |     |
| --- | --- | --- | ------- | --- |
\langlev,u \rangle=
j k ⎨
|             |                                               | {1 ⎩ | ifj =k. |     |
| ----------- | --------------------------------------------- | ---- | ------- | --- |
| 20 Suppose\mathbf{F} | =\mathbf{C},\mathcal{V} isfinite-dimensional,andℰ\subseteqℒ(\mathcal{V})issuchthat |      |         |     |
\mathcal{S}\mathcal{T} =\mathcal{T}\mathcal{S}
forall\mathcal{S},\mathcal{T} \inℰ. Provethatthereisanorthonormalbasisof\mathcal{V} withrespect
towhicheveryelementofℰhasanupper-triangularmatrix.
Thisexercisestrengthens Exercise9(b)in Section5E(inthecontextofinner
productspaces)byassertingthatthebasisinthatexercisecanbechosento
beorthonormal.
21 Suppose\mathbf{F} = \mathbf{C}, \mathcal{V} isfinite-dimensional, \mathcal{T} \in ℒ(\mathcal{V}), andalleigenvalues
of\mathcal{T} haveabsolutevaluelessthan1. Let\epsilon > 0. Provethatthereexistsa
positiveintegermsuchthat∥\mathcal{T}mv∥\leq\epsilon‖v‖foreveryv\in\mathcal{V}.

| -------- | ------------------ | --- | --- | --- |
22 Suppose\mathcal{C}[-1,1]isthevectorspaceofcontinuousreal-valuedfunctions
ontheinterval[-1,1]withinnerproductgivenby
|     |     | \langlef,g\rangle=\int | fg  |     |
| --- | --- | ------- | --- | --- |
-1
forall f,g \in\mathcal{C}[-1,1]. Let\phibethelinearfunctionalon\mathcal{C}[-1,1]defined
| by\phi(f)= | f(0). Showthattheredoesnotexistg |     |     | \in\mathcal{C}[-1,1]suchthat |
| ------- | -------------------------------- | --- | --- | ---------------- |
\phi(f)=\langlef,g\rangle
| forevery | f \in\mathcal{C}[-1,1]. |     |     |     |
| -------- | ----------- | --- | --- | --- |
Thisexerciseshowsthatthe Rieszrepresentationtheorem(6.42)doesnot
holdoninfinite-dimensionalvectorspaceswithoutadditionalhypotheses
on\mathcal{V}and\phi.
23 Forallu,v\in\mathcal{V},defined(u,v)=‖u-v‖.
$$(a) Showthatdisametricon\mathcal{V}.$$
$$(b) Showthatif\mathcal{V} isfinite-dimensional,thendisacompletemetricon\mathcal{V}$$
$$(meaningthatevery Cauchysequenceconverges).$$
$$(c) Show that every finite-dimensional subspace of \mathcal{V} is a closed subset$$
| of\mathcal{V} | (withrespecttothemetricd). |     |     |     |
| --- | -------------------------- | --- | --- | --- |
Thisexerciserequiresfamiliaritywithmetricspaces.
orthogonalityatthe Supreme Court
Lawprofessor Richard Friedmanpresentingacasebeforethe U.S.Supreme
Courtin2010:
Mr.Friedman: Ithinkthatissueisentirelyorthogonaltotheissuehere
becausethe Commonwealthisacknowledging—
| Chief Justice Roberts: | I’msorry.             | Entirelywhat? |             |             |
| -------------------- | --------------------- | ------------- | ----------- | ----------- |
| Mr.Friedman:         | Orthogonal.           | Rightangle.   | Unrelated.  | Irrelevant. |
| Chief Justice Roberts: | Oh.                   |               |             |             |
| Justice Scalia:       | Whatwasthatadjective? |               | Ilikedthat. |             |
| Mr.Friedman:         | Orthogonal.           |               |             |             |
| Chief Justice Roberts: | Orthogonal.           |               |             |             |
| Mr.Friedman:         | Right,right.          |               |             |             |
| Justice Scalia:       | Orthogonal,ooh.       | (Laughter.)   |             |             |
Justice Kennedy: Iknewthiscasepresentedusaproblem. (Laughter.)

| --------- | -------------------------------------------- | --- | --- | --- | --- |
| 6C Orthogonal | Complements | and | Minimization | Problems |     |
| ------------- | ----------- | --- | ------------ | -------- | --- |
| Orthogonal    | Complements |     |              |          |     |
orthogonalcomplement,\mathcal{U}⟂
**6.46 定义：** If\mathcal{U} isasubsetof\mathcal{V},thentheorthogonalcomplement of\mathcal{U},denotedby\mathcal{U}⟂,
| isthesetofallvectorsin\mathcal{V} | thatareorthogonaltoeveryvectorin\mathcal{U}: |     |     |     |     |
| ----------------------- | ---------------------------------- | --- | --- | --- | --- |
∶\langleu,v\rangle=0foreveryu\in\mathcal{U}}.
\mathcal{U}⟂ ={v\in\mathcal{V}
Theorthogonalcomplement\mathcal{U}⟂
|     |     | dependson\mathcal{V} | aswellason\mathcal{U}. | However,the |     |
| --- | --- | ---------- | ------------ | ----------- | --- |
innerproductspace\mathcal{V} shouldalwaysbeclearfromthecontextandthusitcanbe
omittedfromthenotation.
| 6.47 example: | orthogonalcomplements |     |     |     |     |
| ------------- | --------------------- | --- | --- | --- | --- |
• If\mathcal{V} =\mathbf{R}3and\mathcal{U} isthesubsetof\mathcal{V} consistingofthesinglepoint(2,3,5),then
∶2x+3y+5z=0}.
\mathcal{U}⟂ istheplane{(x,y,z)\in\mathbf{R}3
| • If\mathcal{V} =\mathbf{R}3 | and\mathcal{U} istheplane{(x,y,z)\in\mathbf{R}3 |     | ∶2x+3y+5z=0},then\mathcal{U}⟂ |     | is  |
| --------- | -------------------------- | --- | ------------------- | --- | --- |
theline{(2t,3t,5t)∶t\in\mathbf{R}}.
• Moregenerally,if\mathcal{U} isaplanein\mathbf{R}3 containingtheorigin,then\mathcal{U}⟂ istheline
containingtheoriginthatisperpendicularto\mathcal{U}.
• If\mathcal{U} isalinein\mathbf{R}3 containingtheorigin,then\mathcal{U}⟂ istheplanecontainingthe
originthatisperpendicularto\mathcal{U}.
| • If\mathcal{V} =\mathbf{F}5  | and\mathcal{U} ={(a,b,0,0,0)\in\mathbf{F}5                  | ∶a,b\in\mathbf{F}},then |            |     |     |
| ---------- | -------------------------------------- | ------------ | ---------- | --- | --- |
|            | \mathcal{U}⟂ ={(0,0,x,y,z)\in\mathbf{F}5                    |              | ∶x,y,z\in\mathbf{F}}. |     |     |
| • Ife ,…,e | , f ,…, f isanorthonormalbasisof\mathcal{V},then |              |            |     |     |
| 1          | m 1 n                                  |              |            |     |     |
$$))⟂$$
|     | (span(e ,…,e | =span(f | ,…, f ). |     |     |
| --- | ------------ | ------- | -------- | --- | --- |
|     | 1            | m       | 1 n      |     |     |
Webeginwithsomestraightforwardconsequencesofthedefinition.
6.48 propertiesoforthogonalcomplement
| (a) If\mathcal{U}  | isasubsetof\mathcal{V},then\mathcal{U}⟂ | isasubspaceof\mathcal{V}. |     |     |     |
| -------- | ------------------- | --------------- | --- | --- | --- |
| (b) {0}⟂ | =\mathcal{V}.                 |                 |     |     |     |
\mathcal{V}⟂
| (c)         | ={0}.                 |               |      |     |     |
| ----------- | --------------------- | ------------- | ---- | --- | --- |
| (d) If\mathcal{U}     | isasubsetof\mathcal{V},then\mathcal{U}\cap\mathcal{U}⟂ | \subseteq{0}.         |      |     |     |
|             |                       | and\mathcal{G}\subseteq\mathcal{H},then\mathcal{H}⟂ | \subseteq\mathcal{G}⟂. |     |     |
| (e) If\mathcal{G}and\mathcal{H} | aresubsetsof\mathcal{V}         |               |      |     |     |

| -------- | ------------------ | --- | --- |
Proof
| (a) Suppose\mathcal{U}   | isasubsetof\mathcal{V}. | Then\langleu,0\rangle=0foreveryu\in\mathcal{U};thus0\in\mathcal{U}⟂. |     |
| -------------- | ------------- | -------------------------------- | --- |
| Supposev,w\in\mathcal{U}⟂. | Ifu\in\mathcal{U},then    |                                  |     |
\langleu,v+w\rangle=\langleu,v\rangle+\langleu,w\rangle=0+0=0.
Thusv+w\in\mathcal{U}⟂,whichshowsthat\mathcal{U}⟂
isclosedunderaddition.
| Similarly,suppose | \lambda\in\mathbf{F}     | andv\in\mathcal{U}⟂. | Ifu\in\mathcal{U},then |
| ----------------- | ------- | -------- | ---------- |
|                   | \langleu,\lambdav\rangle= | \lambda\langleu,v\rangle=  | \lambda\cdot0=0.     |
Thus \lambdav \in \mathcal{U}⟂,whichshowsthat\mathcal{U}⟂ isclosedunderscalarmultiplication.
| Thus\mathcal{U}⟂ | isasubspaceof\mathcal{V}. |     |     |
| ------ | --------------- | --- | --- |
$$(b) Suppose that v \in \mathcal{V}. Then \langle0,v\rangle = 0, which implies that v \in {0}⟂. Thus$$
{0}⟂ =\mathcal{V}.
|     | \mathcal{V}⟂. | \langlev,v\rangle |     |
| --- | --- | ----- | --- |
$$(c) Suppose that v \in Then = 0, which implies that v = 0. Thus$$
\mathcal{V}⟂ ={0}.
|     |     | andu\in\mathcal{U}\cap\mathcal{U}⟂. | Then\langleu,u\rangle=0,whichimplies |
| --- | --- | ---------- | ------------------------ |
$$(d) Suppose\mathcal{U}isasubsetof\mathcal{V}$$
| thatu=0. | Thus\mathcal{U}\cap\mathcal{U}⟂ | \subseteq{0}. |     |
| -------- | -------- | ----- | --- |
\mathcal{H}⟂.
$$(e) Suppose \mathcal{G} and \mathcal{H} are subsets of \mathcal{V} and \mathcal{G} \subseteq \mathcal{H}. Suppose v \in Then$$
\langleu,v\rangle = 0foreveryu \in \mathcal{H},whichimpliesthat\langleu,v\rangle = 0foreveryu \in \mathcal{G}.
| Hencev\in\mathcal{G}⟂. | Thus\mathcal{H}⟂ | \subseteq\mathcal{G}⟂. |     |
| ---------- | ------ | ---- | --- |
Recallthatif\mathcal{U} and\mathcal{W} aresubspacesof\mathcal{V},then\mathcal{V} isthedirectsumof\mathcal{U} and
\mathcal{W} (written\mathcal{V} =\mathcal{U}\oplus\mathcal{W})ifeachelementof\mathcal{V} canbewritteninexactlyoneway
asavectorin\mathcal{U} plusavectorin\mathcal{W} (see1.41). Furthermore,thishappensifand
| onlyif\mathcal{V} =\mathcal{U}+\mathcal{W} | and\mathcal{U}\cap\mathcal{W} | ={0}(see1.46). |     |
| ------------ | ------ | -------------- | --- |
Thenextresultshowsthateveryfinite-dimensionalsubspaceof\mathcal{V} leadstoa
naturaldirectsumdecompositionof\mathcal{V}. See Exercise16foranexampleshowing
thattheresultbelowcanfailwithoutthehypothesisthatthesubspace\mathcal{U} isfinitedimensional.
6.49 directsumofasubspaceanditsorthogonalcomplement
| Suppose\mathcal{U} | isafinite-dimensionalsubspaceof\mathcal{V}. |     | Then |
| -------- | --------------------------------- | --- | ---- |
=\mathcal{U}\oplus\mathcal{U}⟂.
\mathcal{V}
\mathcal{V} =\mathcal{U}+\mathcal{U}⟂.
Todothis,supposethatv\in\mathcal{V}. Lete ,…,e beanorthonormalbasisof\mathcal{U}. We
|                                  |     | 1   | m                        |
| -------------------------------- | --- | --- | ------------------------ |
| wanttowritevasthesumofavectorin\mathcal{U} |     |     | andavectororthogonalto\mathcal{U}. |

| --------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Wehave
|      | v=\langle⏟v,⏟e⏟\ranglee⏟+⏟⋯+⏟\langlev⏟,e⏟\rangle⏟e |     |     |     | +⏟v-⏟\langle⏟v,⏟e | \rangle⏟e⏟-⋯⏟-⏟\langlev⏟,e⏟\rangle⏟e |     |     | .   |
| ---- | -------------------------- | --- | --- | --- | ----------- | ------------------ | --- | --- | --- |
| 6.50 |                            | 1 1 |     | m   | m           | 1 1                |     | m   | m   |
|      |                            |     | u   |     |             |                    | w   |     |     |
Letuandwbedefinedasintheequationabove(aswasdoneintheproofof6.26).
| Becauseeache  |     | \in\mathcal{U},weseethatu\in\mathcal{U}. |      |        | Becausee |     | ,…,e | isanorthonormal |     |
| ------------- | --- | ---------------- | ---- | ------ | -------- | --- | ---- | --------------- | --- |
|               |     | k                |      |        |          |     | 1 m  |                 |     |
| list,foreachk |     | =1,…,mwehave     |      |        |          |     |      |                 |     |
|               |     |                  | \langlew,e | \rangle=\langlev,e | \rangle-\langlev,e   | \rangle   |      |                 |     |
|               |     |                  |      | k      | k        | k   |      |                 |     |
=0.
$$),whichshowsthatw\in\mathcal{U}⟂.$$
| Thuswisorthogonaltoeveryvectorinspan(e |     |     |     |            |     | ,…,e     |                    |     |     |
| -------------------------------------- | --- | --- | --- | ---------- | --- | -------- | ------------------ | --- | --- |
|                                        |     |     |     |            |     | 1 m      |                    |     |     |
| Hencewehavewrittenv                    |     |     | =   | u+w,whereu |     | \in \mathcal{U} andw | \in \mathcal{U}⟂,completingthe |     |     |
=\mathcal{U}+\mathcal{U}⟂.
proofthat\mathcal{V}
From 6.48(d), we know that \mathcal{U} \cap\mathcal{U}⟂ = {0}. Now equation \mathcal{V} = \mathcal{U} +\mathcal{U}⟂
=\mathcal{U}\oplus\mathcal{U}⟂
| impliesthat\mathcal{V}                 |     |     | (see1.46). |     |     |           |     |     |     |
| ---------------------------- | --- | --- | ---------- | --- | --- | --------- | --- | --- | --- |
| Nowwecanseehowtocomputedim\mathcal{U}⟂ |     |     |            |     |     | fromdim\mathcal{U}. |     |     |     |
6.51 dimensionoforthogonalcomplement
| Suppose\mathcal{V} |     | isfinite-dimensionaland\mathcal{U} |     |     | isasubspaceof\mathcal{V}. |     |     | Then |     |
| -------- | --- | ------------------------ | --- | --- | --------------- | --- | --- | ---- | --- |
dim\mathcal{U}⟂
=dim\mathcal{V}-dim\mathcal{U}.
| Proof | Theformulafordim\mathcal{U}⟂ |     |     | followsimmediatelyfrom6.49and3.94. |     |     |     |     |     |
| ----- | ------------------ | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
Thenextresultisanimportantconsequenceof6.49.
orthogonalcomplementoftheorthogonalcomplement
6.52
| Suppose\mathcal{U} |     | isafinite-dimensionalsubspaceof\mathcal{V}. |     |     |     | Then |     |     |     |
| -------- | --- | --------------------------------- | --- | --- | --- | ---- | --- | --- | --- |
=(\mathcal{U}⟂)⟂.
\mathcal{U}
\subseteq(\mathcal{U}⟂)⟂.
| 6.53 |     |     |     | \mathcal{U}   |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Todothis,supposeu\in\mathcal{U}. Then\langleu,w\rangle=0foreveryw\in\mathcal{U}⟂ (bythedefinition
| \mathcal{U}⟂). |         |      |            |     |              |     | \mathcal{U}⟂, |        | (\mathcal{U}⟂)⟂, |
| ---- | ------- | ---- | ---------- | --- | ------------ | --- | --- | ------ | ------ |
| of   | Because | u is | orthogonal | to  | every vector | in  | we  | have u | \in      |
completingtheproofof6.53.
$$(\mathcal{U}⟂)⟂.$$
| Toprovetheinclusionintheotherdirection,supposev |     |              |     |     |                             |       |           | \in   | By6.49,   |
| ----------------------------------------------- | --- | ------------ | --- | --- | --------------------------- | ----- | --------- | --- | --------- |
| wecanwritev                                     |     | = u+w,whereu |     | \in   | \mathcal{U} andw                      | \in \mathcal{U}⟂. | Wehavev-u |     | = w \in \mathcal{U}⟂. |
| Becausev\in(\mathcal{U}⟂)⟂                                  |     | andu\in(\mathcal{U}⟂)⟂   |     |     | (from6.53),wehavev-u\in(\mathcal{U}⟂)⟂. |       |           |     |           |
Thus
v-u\in\mathcal{U}⟂\cap(\mathcal{U}⟂)⟂,whichimpliesthatv-u=0[by6.48(d)],whichimplies
Thus(\mathcal{U}⟂)⟂
| thatv=u,whichimpliesthatv\in\mathcal{U}. |     |     |     |     |     | \subseteq\mathcal{U},whichalongwith6.53 |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
completestheproof.

| --- | -------- | --- | ------------------ | --- | --- | --- | --- |
|     | Suppose | \mathcal{U} is a    | subspace | of \mathcal{V} and   |                |            |            |
| --- | ------- | --------- | -------- | ---------- | -------------- | ---------- | ---------- |
|     |         |           |          |            | Exercise 16(a) | shows that | the result |
| we  | want to | show that | \mathcal{U} =      | \mathcal{V}. In some |                |            |            |
belowisnottruewithoutthehypothesis
situations,theeasiestwaytodothisisto that\mathcal{U}isfinite-dimensional.
showthattheonlyvectororthogonalto
\mathcal{U} is0,andthenusetheresultbelow. Forexample,theresultbelowisusefulfor
Exercise4.
|     | \mathcal{U}⟂  | ={0} ⟺ | \mathcal{U}   | =\mathcal{V} (for \mathcal{U} afinite-dimensionalsubspaceof |     |     | \mathcal{V})  |
| --- | --- | ------ | --- | --------------------------------------- | --- | --- | --- |
6.54
| Suppose\mathcal{U} |     | isafinite-dimensionalsubspaceof\mathcal{V}. |     |         | Then    |     |     |
| -------- | --- | --------------------------------- | --- | ------- | ------- | --- | --- |
|          |     |                                   |     | \mathcal{U}⟂ ={0} | ⟺ \mathcal{U} =\mathcal{V}. |     |     |
$$(\mathcal{U}⟂)⟂$$
Proof First suppose \mathcal{U}⟂ = {0}. Then by 6.52, \mathcal{U} = = {0}⟂ = \mathcal{V}, as
desired.
|     | Conversely,if\mathcal{U} |     | =\mathcal{V},then\mathcal{U}⟂ | =\mathcal{V}⟂ | ={0}by6.48(c). |     |     |
| --- | -------------- | --- | --------- | --- | -------------- | --- | --- |
Wenowdefineanoperator\mathcal{P} foreachfinite-dimensionalsubspace\mathcal{U} of\mathcal{V}.
\mathcal{U}
orthogonalprojection,\mathcal{P}
| 6.55 | definition: |     |     |     | \mathcal{U}   |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- | --- |
Suppose\mathcal{U} isafinite-dimensionalsubspaceof\mathcal{V}. Theorthogonalprojection
| of\mathcal{V} | onto\mathcal{U} | istheoperator\mathcal{P} |     | \inℒ(\mathcal{V})definedasfollows: |     | Foreachv\in\mathcal{V}, |     |
| --- | ----- | -------------- | --- | ---------------------- | --- | ----------- | --- |
\mathcal{U}
| writev=u+w,whereu\in\mathcal{U} |     |     |     | andw\in\mathcal{U}⟂. | Thenlet\mathcal{P} | v=u. |     |
| ------------------- | --- | --- | --- | -------- | -------- | ---- | --- |
\mathcal{U}
\mathcal{U}\oplus\mathcal{U}⟂
|     | Thedirectsumdecomposition\mathcal{V} |     |     | =   | givenby6.49showsthateach |     |     |
| --- | -------------------------- | --- | --- | --- | ------------------------ | --- | --- |
v \in \mathcal{V} canbeuniquelywrittenintheformv = u+wwithu \in \mathcal{U} andw \in \mathcal{U}⟂.
Thus\mathcal{P} viswelldefined. Seethefigurethataccompaniestheproofof6.61for
\mathcal{U}
| thepicturedescribing\mathcal{P} |     |     | vthatyoushouldkeepinmind. |     |     |     |     |
| --------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
\mathcal{U}
orthogonalprojectionontoone-dimensionalsubspace
**6.56 例：** Suppose u \in \mathcal{V} with u \neq 0 and \mathcal{U} is the one-dimensional subspace of \mathcal{V}
| definedby\mathcal{U} |     | =span(u). |     |     |     |     |     |
| ---------- | --- | --------- | --- | --- | --- | --- | --- |
Ifv\in\mathcal{V},then
|     |     |     |     | \langlev,u\rangle | \langlev,u\rangle |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | --- |
|     |     |     | v=  | u+(v- | u),   |     |     |
|     |     |     |     | ‖u‖2  | ‖u‖2  |     |     |
wherethefirsttermontherightisinspan(u)(andthusisin\mathcal{U})andthesecond
termontherightisorthogonaltou(andthusisin\mathcal{U}⟂). Thus\mathcal{P} vequalsthefirst
\mathcal{U}
| termontheright. |     | Inotherwords,wehavetheformula |     |     |     |     |     |
| --------------- | --- | ----------------------------- | --- | --- | --- | --- | --- |
\langlev,u\rangle
|     |     |     |     | \mathcal{P} v= | u   |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- |
\mathcal{U}
‖u‖2
foreveryv\in\mathcal{V}.
The formula above becomes \mathcal{P} u = u if v = u and becomes \mathcal{P} v = 0 if
|     |     |     |     | \mathcal{U}   |     |     | \mathcal{U}   |
| --- | --- | --- | --- | --- | --- | --- | --- |
v\in{u}⟂. Theseequationsarespecialcasesof(b)and(c)inthenextresult.

Section6C Orthogonal Complementsand Minimization Problems 215
6.57 propertiesoforthogonalprojection\mathcal{P}
\mathcal{U}
Suppose\mathcal{U} isafinite-dimensionalsubspaceof\mathcal{V}. Then
$$(a) \mathcal{P} \inℒ(\mathcal{V});$$
\mathcal{U}
$$(b) \mathcal{P} u=uforeveryu\in\mathcal{U};$$
\mathcal{U}
$$(c) \mathcal{P} w=0foreveryw\in\mathcal{U}⟂;$$
\mathcal{U}
$$(d) range\mathcal{P} =\mathcal{U};$$
\mathcal{U}
$$(e) null\mathcal{P} =\mathcal{U}⟂;$$
\mathcal{U}
$$(f) v-\mathcal{P} v\in\mathcal{U}⟂ foreveryv\in\mathcal{V};$$
\mathcal{U}
$$(g) \mathcal{P} 2 =\mathcal{P} ;$$
\mathcal{U} \mathcal{U}
$$(h) ‖\mathcal{P} v‖\leq‖v‖foreveryv\in\mathcal{V};$$
\mathcal{U}
$$(i) ife ,…,e isanorthonormalbasisof\mathcal{U} andv\in\mathcal{V},then$$
1 m
\mathcal{P} v=\langlev,e \ranglee +⋯+\langlev,e \ranglee .
\mathcal{U} 1 1 m m
Proof
$$(a) Toshowthat\mathcal{P} isalinearmapon\mathcal{V},supposev ,v \in\mathcal{V}. Write$$
\mathcal{U} 1 2
$$v =u +w and v =u +w$$
1 1 1 2 2 2
withu ,u \in\mathcal{U} andw ,w \in\mathcal{U}⟂. Thus\mathcal{P} v =u and\mathcal{P} v =u . Now
1 2 1 2 \mathcal{U} 1 1 \mathcal{U} 2 2
v +v =(u +u )+(w +w ),
1 2 1 2 1 2
whereu +u \in\mathcal{U} andw +w \in\mathcal{U}⟂. Thus
1 2 1 2
\mathcal{P} (v +v )=u +u =\mathcal{P} v +\mathcal{P} v .
\mathcal{U} 1 2 1 2 \mathcal{U} 1 \mathcal{U} 2
Similarly, suppose \lambda \in \mathbf{F} and v \in \mathcal{V}. Write v = u + w, where u \in \mathcal{U}
and w \in \mathcal{U}⟂. Then \lambdav = \lambdau + \lambdaw with \lambdau \in \mathcal{U} and \lambdaw \in \mathcal{U}⟂. Thus
\mathcal{P} (\lambdav)= \lambdau= \lambda\mathcal{P} v.
\mathcal{U} \mathcal{U}
Hence\mathcal{P} isalinearmapfrom\mathcal{V} to\mathcal{V}.
\mathcal{U}
$$(b) Supposeu \in \mathcal{U}. Wecanwriteu = u+0,whereu \in \mathcal{U} and0 \in \mathcal{U}⟂. Thus$$
\mathcal{P} u=u.
\mathcal{U}
$$(c) Supposew\in\mathcal{U}⟂. Wecanwritew=0+w,where0\in\mathcal{U}andw\in\mathcal{U}⟂. Thus$$
\mathcal{P} w=0.
\mathcal{U}
$$(d) Thedefinitionof\mathcal{P} impliesthatrange\mathcal{P} \subseteq \mathcal{U}. Furthermore,(b)implies$$
\mathcal{U} \mathcal{U}
that\mathcal{U} \subseteqrange\mathcal{P} . Thusrange\mathcal{P} =\mathcal{U}.
\mathcal{U} \mathcal{U}
$$(e) Theinclusion\mathcal{U}⟂ \subseteqnull\mathcal{P} followsfrom(c). Toprovetheinclusioninthe$$
\mathcal{U}
otherdirection,notethatifv\innull\mathcal{P} thenthedecompositiongivenby6.49
\mathcal{U}
mustbev=0+v,where0\in\mathcal{U} andv\in\mathcal{U}⟂. Thusnull\mathcal{P} \subseteq\mathcal{U}⟂.
\mathcal{U}

| -------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
andw\in\mathcal{U}⟂,then
| (f) Ifv\in\mathcal{V} | andv=u+wwithu\in\mathcal{U} |     |     |             |     |     |     |     |
| --------- | --------------- | --- | --- | ----------- | --- | --- | --- | --- |
|           |                 |     | v-\mathcal{P} | v=v-u=w\in\mathcal{U}⟂. |     |     |     |     |
\mathcal{U}
| (g) Ifv\in\mathcal{V} | andv=u+wwithu\in\mathcal{U} |     |     | andw\in\mathcal{U}⟂,then |     |     |     |     |
| --------- | --------------- | --- | --- | ------------ | --- | --- | --- | --- |
2)v=\mathcal{P}
|           |                 | (\mathcal{P}  |           | (\mathcal{P} v)=\mathcal{P}      | u=u=\mathcal{P} |        | v.  |     |
| --------- | --------------- | --- | --------- | ------------ | ----- | ------ | --- | --- |
|           |                 | \mathcal{U}   |           | \mathcal{U} \mathcal{U}          | \mathcal{U}     | \mathcal{U}      |     |     |
| (h) Ifv\in\mathcal{V} | andv=u+wwithu\in\mathcal{U} |     |           | andw\in\mathcal{U}⟂,then |       |        |     |     |
|           |                 |     | v‖2 =‖u‖2 | \leq‖u‖2+‖w‖2   |       | =‖v‖2, |     |     |
‖\mathcal{P}
\mathcal{U}
wherethelastequalitycomesfromthe Pythagoreantheorem.
| (i) Theformulafor\mathcal{P} |     | vfollowsfromequation6.50intheproofof6.49. |     |     |     |     |     |     |
| ------------------ | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
\mathcal{U}
Intheprevioussectionweprovedthe Rieszrepresentationtheorem(6.42),
whosekeypartstatesthateverylinearfunctionalonafinite-dimensionalinner
productspaceisgivenbytakingtheinnerproductwithsomefixedvector. Seeing
adifferentproofoftenprovidesnewinsight. Thuswenowgiveanewproofof
thekeypartofthe Rieszrepresentationtheoremusingorthogonalcomplements
insteadoforthonormalbasesasinourpreviousproof.
Therestatementbelowofthe Rieszrepresentationtheoremprovidesanidenwith\mathcal{V}′.
| tificationof\mathcal{V} |     | Wewillproveonlythe“onto”partoftheresultbelow |     |     |     |     |     |     |
| ------------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
becausethemoreroutine“one-to-one”partoftheresultcanbeprovedasin6.42.
|                              |     |     |     | \mathcal{V}′,v  |             |     |     | \langleu,v\rangleforall |
| ---------------------------- | --- | --- | --- | ----- | ----------- | --- | --- | ----------- |
| Intuitionbehindthisnewproof: |     |     |     | If\phi \in | \in \mathcal{V},and\phi(u) |     | =   |             |
u \in \mathcal{V},thenv \in (null\phi)⟂. However,(null\phi)⟂ isaone-dimensionalsubspace
of\mathcal{V} (exceptforthetrivialcaseinwhich\phi=0),asfollowsfrom6.51and3.21.
Thus we can obtain v by choosing any nonzero element of (null\phi)⟂ and then
multiplyingbyanappropriatescalar,asisdoneintheproofbelow.
Rieszrepresentationtheorem,revisited
6.58
| Suppose\mathcal{V} | isfinite-dimensional. |     |     | Foreachv\in\mathcal{V},define\phi |     |     | \in\mathcal{V}′ | by  |
| -------- | --------------------- | --- | --- | ------------------ | --- | --- | --- | --- |
v
\phi (u)=\langleu,v\rangle
v
| foreachu\in\mathcal{V}. |     | Thenv↦\phi | isaone-to-onefunctionfrom\mathcal{V} |     |     |     | onto\mathcal{V}′. |     |
| ----------- | --- | ------- | -------------------------- | --- | --- | --- | ------- | --- |
v
| Proof Toshowthatv↦\phi |     |               | issurjective, |                                |     |              |     |          |
| ------------------- | --- | ------------- | ------------- | ------------------------------ | --- | ------------ | --- | -------- |
|                     |     | v             |               | Caution:                       |     | The function | v   | ↦ \phi is a |
|                     | \mathcal{V}′. |               |               |                                |     |              |     | v        |
| suppose\phi            | \in   | If\phi = 0,then\phi |               | = \phi . linearmappingfrom\mathcal{V}to\mathcal{V}′if |     |              |     | =\mathbf{R}.      |
|                     |     |               |               | 0                              |     |              |     | \mathbf{F}        |
| Thusassume\phi         | \neq   | 0. Hencenull\phi |               | \neq \mathcal{V},                           |     |              |     |          |
However,thisfunctionisnotlinearif
which implies that (null\phi)⟂ \neq {0} (by \mathbf{F} =\mathbf{C}because\phi = \lambda\phi if \lambda\in\mathbf{C}.
|               |          |                |     |     |     |     | \lambdav  | v   |
| ------------- | -------- | -------------- | --- | --- | --- | --- | --- | --- |
| 6.49with\mathcal{U}     | =null\phi). |                |     |     |     |     |     |     |
| Letw\in(null\phi)⟂ |          | besuchthatw\neq0. |     | Let |     |     |     |     |
\phi(w)
| 6.59 |     |     |     | v= w. |     |     |     |     |
| ---- | --- | --- | --- | ----- | --- | --- | --- | --- |
‖w‖2
Thenv\in(null\phi)⟂.
Also,v\neq0(becausew\notinnull\phi).

| --------- | --- | -------------------------------------------- | --- | --- |
Takingthenormofbothsidesof6.59gives
|\phi(w)|
| 6.60 |     |     | ‖v‖= | .   |
| ---- | --- | --- | ---- | --- |
‖w‖
Applying\phitobothsidesof6.59andthenusing6.60,wehave
|\phi(w)|2
=‖v‖2.
\phi(v)=
‖w‖2
| Nowsupposeu\in\mathcal{V}. |     | Usingtheequationabove,wehave |      |        |
| -------------- | --- | ---------------------------- | ---- | ------ |
|                |     |                              | \phi(u) | \phi(u)   |
|                |     | u=(u-                        |      | v)+ v. |
|                |     |                              | \phi(v) | ‖v‖2   |
Thefirstterminparenthesesaboveisinnull\phiandhenceisorthogonaltov. Thus
takingtheinnerproductofbothsidesoftheequationabovewithvshowsthat
\phi(u)
|     |     | \langleu,v\rangle= |     | \langlev,v\rangle=\phi(u). |
| --- | --- | ------ | --- | ----------- |
‖v‖2
| Thus\phi=\phi | ,showingthatv↦\phi |     | issurjective,asdesired. |     |
| ------- | --------------- | --- | ----------------------- | --- |
|         | v               |     | v                       |     |
See Exercise13foryetanotherproofofthe Rieszrepresentationtheorem.
| Minimization  |     | Problems      |         |     |
| ------------- | --- | ------------- | ------- | --- |
| The following |     | problem often | arises: |     |
Theremarkablesimplicityofthesolu-
| Given a | subspace | \mathcal{U} of \mathcal{V} | and a point |     |
| ------- | -------- | ------ | ----------- | --- |
tiontothisminimizationproblemhas
v \in \mathcal{V}, find a point u \in \mathcal{U} such that ledtomanyimportantapplicationsof
| ‖v-u‖isassmallaspossible. |     |     | Thenext |     |
| ------------------------- | --- | --- | ------- | --- |
innerproductspacesoutsideofpure
| resultshowsthatu |     | = \mathcal{P} vistheunique |     | mathematics. |
| ---------------- | --- | ---------------- | --- | ------------ |
\mathcal{U}
solutionofthisminimizationproblem.
6.61 minimizingdistancetoasubspace
| Suppose\mathcal{U} | isafinite-dimensionalsubspaceof\mathcal{V},v\in\mathcal{V},andu\in\mathcal{U}. |     |     | Then |
| -------- | -------------------------------------------- | --- | --- | ---- |
‖v-\mathcal{P} v‖\leq‖v-u‖.
\mathcal{U}
Furthermore,theinequalityaboveisanequalityifandonlyifu=\mathcal{P} v.
\mathcal{U}
| 6.62 |     | ‖v-\mathcal{P} v‖2 | \leq‖v-\mathcal{P}  | v‖2+‖\mathcal{P} v-u‖2 |
| ---- | --- | -------- | ------ | ------------ |
|      |     | \mathcal{U}        |        | \mathcal{U} \mathcal{U}          |
|      |     |          | =∥(v-\mathcal{P} | v)+(\mathcal{P} v-u)∥2 |
|      |     |          |        | \mathcal{U} \mathcal{U}          |
=‖v-u‖2,

| -------- | ------------------ | --- | --- | --- |
v-u‖2,
wherethefirstlineaboveholdsbecause0\leq‖\mathcal{P}
\mathcal{U}
thesecondlineabovecomesfromthe Pythagoreanthev\in\mathcal{U}⟂
| orem[whichappliesbecausev-\mathcal{P} |     |     |     | by6.57(f), |
| --------------------------- | --- | --- | --- | ---------- |
\mathcal{U}
| and \mathcal{P} v-u | \in \mathcal{U}], and | the third | line above | holds by |
| --------- | --------- | --------- | ---------- | -------- |
\mathcal{U}
| simplealgebra. | Takingsquarerootsgivesthedesired |     |     |     |
| -------------- | -------------------------------- | --- | --- | --- |
inequality.
| The inequality | proved | above | is an equality | if and |
| -------------- | ------ | ----- | -------------- | ------ |
onlyif6.62isanequality,whichhappensifandonlyif
| ‖\mathcal{P} v-u‖=0,whichhappensifandonlyifu=\mathcal{P} |     |     |     | v.  |
| ------------------------------------ | --- | --- | --- | --- |
| \mathcal{U}                                    |     |     |     | \mathcal{U}   |
\mathcal{P} vistheclosest
Thelastresultisoftencombinedwiththeformula \mathcal{U}
pointin\mathcal{U}tov.
| 6.57(i) to | compute explicit | solutions | to minimization |     |
| ---------- | ---------------- | --------- | --------------- | --- |
problems,asinthefollowingexample.
| 6.63 example: | usinglinearalgebratoapproximatethesinefunction |     |     |     |
| ------------- | ---------------------------------------------- | --- | --- | --- |
Supposewewanttofindapolynomialuwithrealcoefficientsandofdegree
atmost5thatapproximatesthesinefunctionaswellaspossibleontheinterval
[-\pi,\pi],inthesensethat
\pi
∣sinx-u(x)∣2dx
\int
-\pi
isassmallaspossible.
Let\mathcal{C}[-\pi,\pi]denotetherealinnerproductspaceofcontinuousreal-valued
functionson[-\pi,\pi]withinnerproduct
\pi
| 6.64 |     | \langlef,g\rangle=\int |     | fg. |
| ---- | --- | ------- | --- | --- |
-\pi
$$\mathcal{C}[-\pi,\pi]$$
Let v \in be the function defined by v(x) = sinx. Let \mathcal{U} denote the
subspaceof\mathcal{C}[-\pi,\pi]consistingofthepolynomialswithrealcoefficientsandof
| degreeatmost5. | Ourproblemcannowbereformulatedasfollows: |                                   |     |     |
| -------------- | ---------------------------------------- | --------------------------------- | --- | --- |
|                | Findu\in\mathcal{U}                                  | suchthat‖v-u‖isassmallaspossible. |     |     |
| To compute     | the solution                             | to our                            | ap- |     |
Acomputerthatcanintegrateisuseful
| proximation | problem, | first apply | the |     |
| ----------- | -------- | ----------- | --- | --- |
here.
Gram–Schmidtprocedure(usingtheinnerproductgivenby6.64)tothebasis1,x,x2,x3,x4,x5 of\mathcal{U},producinganorthonormalbasise ,e ,e ,e ,e ,e of\mathcal{U}. Then,againusingtheinnerproductgiven
|     | 1 2 3 4 | 5 6 |     |     |
| --- | ------- | --- | --- | --- |
by6.64,compute\mathcal{P} vusing6.57(i)(withm=6). Doingthiscomputationshows
\mathcal{U}
that\mathcal{P} visthefunctionudefinedby
\mathcal{U}
u(x)=0.987862x-0.155271x3+0.00564312x5,
6.65
wherethe\pi’sthatappearintheexactanswerhavebeenreplacedwithagood
decimalapproximation. By6.61,thepolynomialuaboveisthebestapproximation
tothesinefunctionon[-\pi,\pi]usingpolynomialsofdegreeatmost5(here“best
\pi |sinx-u(x)|2dx).
approximation”meansinthesenseofminimizing\int
-\pi

Section6C Orthogonal Complementsand Minimization Problems 219
Toseehowgoodthisapproximationis,thenextfigureshowsthegraphsof
boththesinefunctionandourapproximationugivenby6.65overtheinterval
[-\pi,\pi].
Graphson[-\pi,\pi]ofthesinefunction(red)anditsbest
fifthdegreepolynomialapproximationu(blue)from6.65.
Ourapproximation6.65issoaccuratethatthetwographsarealmostidenticaloureyesmayseeonlyonegraph! Heretheredgraphisplacedalmostexactly
overthebluegraph. Ifyouareviewingthisonanelectronicdevice,enlargethe
pictureaboveby400%near\pi or-\pi toseeasmallgapbetweenthetwographs.
Anotherwell-knownapproximationtothesinefunctionbyapolynomialof
degree5isgivenbythe Taylorpolynomialpdefinedby
x3 x5
6.66 p(x)=x- + .
3! 5!
Toseehowgoodthisapproximationis,thenextpictureshowsthegraphsofboth
thesinefunctionandthe Taylorpolynomialpovertheinterval[-\pi,\pi].
Graphson[-\pi,\pi]ofthesinefunction(red)
andthe Taylorpolynomial(blue)from6.66.
The Taylorpolynomialofdegree5isanexcellentapproximationtosinxfor
xnear0. Butthepictureaboveshowsthatfor|x| > 2,the Taylorpolynomialis
not so accurate, especially compared to 6.65. For example, taking x = 3, our
approximation6.65estimatessin3withanerrorofapproximately0.001,butthe
Taylorpolynomial6.66estimatessin3withanerrorofapproximately0.4. Thus
atx =3,theerrorinthe Taylorpolynomialishundredsoftimeslargerthanthe
errorgivenby6.65. Linearalgebrahashelpedusdiscoveranapproximationto
thesinefunctionthatimprovesuponwhatwelearnedincalculus!

| -------- | ------------------ | --- | --- | --- | --- |
Pseudoinverse
| Suppose\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W})andw\in\mathcal{W}. | Considertheproblemoffindingv\in\mathcal{V} |     |     | such |
| -------- | -------------- | ------------------------------ | --- | --- | ---- |
that
\mathcal{T}v=w.
Forexample,if\mathcal{V} =\mathbf{F}n and\mathcal{W} =\mathbf{F}m,thentheequationabovecouldrepresenta
| systemofmlinearequationsinnunknownsv |     |     | ,…,v ,wherev=(v | ,…,v | ).  |
| ------------------------------------ | --- | --- | --------------- | ---- | --- |
|                                      |     |     | 1 n             | 1    | n   |
If\mathcal{T} isinvertible,thentheuniquesolutiontotheequationaboveisv=\mathcal{T}-1w.
However, if \mathcal{T} is not invertible, then for some w \in \mathcal{W} there may not exist any
solutionsoftheequationabove,andforsomew\in\mathcal{W} theremayexistinfinitely
manysolutionsoftheequationabove.
If\mathcal{T} isnotinvertible,thenwecanstilltrytodoaswellaspossiblewiththe
equationabove. Forexample,iftheequationabovehasnosolutions,theninstead
| ofsolvingtheequation\mathcal{T}v-w=0,wecantrytofindv\in\mathcal{V} |     |     |     | suchthat‖\mathcal{T}v-w‖ |     |
| -------------------------------------------- | --- | --- | --- | -------------- | --- |
isassmallaspossible. Asanotherexample,iftheequationabovehasinfinitely
manysolutionsv\in\mathcal{V},thenamongallthosesolutionswecantrytofindonesuch
that‖v‖isassmallaspossible.
Thepseudoinversewillprovidethetooltosolvetheequationaboveaswell
aspossible,evenwhen\mathcal{T} isnotinvertible. Weneedthenextresulttodefinethe
pseudoinverse.
Inthenexttwoproofs,wewillusewithoutfurthercommenttheresultthatif
\inℒ(\mathcal{V},\mathcal{W}),thennull\mathcal{T},(null\mathcal{T})⟂,andrange\mathcal{T}
| \mathcal{V} isfinite-dimensionaland\mathcal{T} |     |     |     |     | are |
| -------------------------- | --- | --- | --- | --- | --- |
allfinite-dimensional.
6.67 restrictionofalinearmaptoobtainaone-to-oneandontomap
Suppose \mathcal{V} is finite-dimensional and \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Then \mathcal{T}| is an
$$(null\mathcal{T})⟂$$
| injectivemapof(null\mathcal{T})⟂ | ontorange\mathcal{T}. |     |     |     |     |
| ---------------------- | ----------- | --- | --- | --- | --- |
$$(null\mathcal{T})⟂$$
Proof Suppose that v \in and \mathcal{T}| (null\mathcal{T})⟂ v = 0. Hence \mathcal{T}v = 0 and
thus v \in (null\mathcal{T})\cap(null\mathcal{T})⟂, which implies that v = 0 [by 6.48(d)]. Hence
null(\mathcal{T}| (null\mathcal{T})⟂ )={0},whichimpliesthat\mathcal{T}| (null\mathcal{T})⟂ isinjective,asdesired.
Clearlyrange(\mathcal{T}| )\subseteqrange\mathcal{T}. Toprovetheinclusionintheotherdirec-
$$(null\mathcal{T})⟂$$
tion,supposew \in range\mathcal{T}. Hencethereexistsv \in \mathcal{V} suchthatw = \mathcal{T}v. There
| existu\innull\mathcal{T} | andx \in(null\mathcal{T})⟂ | suchthatv=u+x(by6.49). |     | Now |     |
| ------------ | -------------- | ---------------------- | --- | --- | --- |
|              | \mathcal{T}| x =\mathcal{T}x       | =\mathcal{T}v-\mathcal{T}u=w-0=w,          |     |     |     |
$$(null\mathcal{T})⟂$$
| which shows                | that w \in range\mathcal{T}| | . Hence  | range\mathcal{T} \subseteq range\mathcal{T}| |          | , com- |
| -------------------------- | ---------------- | -------- | ---------------- | -------- | ------ |
|                            |                  | (null\mathcal{T})⟂ |                  | (null\mathcal{T})⟂ |        |
| pletingtheproofthatrange\mathcal{T}| |                  | =range\mathcal{T}. |                  |          |        |
$$(null\mathcal{T})⟂$$
Nowwecandefinethepseudoinverse
Toproducethepseudoinversenotation
| \mathcal{T}† (pronounced“\mathcal{T} | dagger”)ofalinear |     |                         |     |     |
| ---------------- | ----------------- | --- | ----------------------- | --- | --- |
|                  |                   |     | \mathcal{T}†in TEX,type T ̂\dagger. |     |     |
map\mathcal{T}. Inthenextdefinition(andfrom
nowon),thinkof\mathcal{T}| asaninvertiblelinearmapfrom(null\mathcal{T})⟂ontorange\mathcal{T},
$$(null\mathcal{T})⟂$$
asisjustifiedbytheresultabove.

| --------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| 6.68 definition: |     | pseudoinverse,\mathcal{T}† |     |     |     |     |     |     |     |
| ---------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Supposethat\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Thepseudoinverse
\mathcal{T}†
| \inℒ(\mathcal{W},\mathcal{V})of\mathcal{T} |     | isthelinearmapfrom\mathcal{W} |         |          | to\mathcal{V}    | definedby |     |     |     |
| ---------- | --- | ------------------- | ------- | -------- | ------ | --------- | --- | --- | --- |
|            |     |                     | \mathcal{T}†w=(\mathcal{T}| | )-1\mathcal{P}     |        | w         |     |     |     |
|            |     |                     |         | (null\mathcal{T})⟂ | range\mathcal{T} |           |     |     |     |
foreachw\in\mathcal{W}.
| Recallthat\mathcal{P}             |            | w=0ifw\in(range\mathcal{T})⟂and\mathcal{P} |                   |          |      |           | w=wifw\inrange\mathcal{T}. |     |        |
| ----------------------- | ---------- | -------------------- | ----------------- | -------- | ---- | --------- | -------------- | --- | ------ |
|                         | range\mathcal{T}     |                      |                   |          |      | range\mathcal{T}    |                |     |        |
|                         | (range\mathcal{T})⟂, |                      | \mathcal{T}†w               |          |      |           |                | \mathcal{T}†w |        |
| Thus if w               | \in          |                      | then              | = 0, and | if w | \in range\mathcal{T}, | then           |     | is the |
| uniqueelementof(null\mathcal{T})⟂ |            |                      | suchthat\mathcal{T}(\mathcal{T}†w)=w. |          |      |           |                |     |        |
Thepseudoinversebehavesmuchlikeaninverse,aswewillsee.
algebraicpropertiesofthepseudoinverse
6.69
| Suppose\mathcal{V} | isfinite-dimensionaland\mathcal{T} |     |       | \inℒ(\mathcal{V},\mathcal{W}). |     |     |     |     |     |
| -------- | ------------------------ | --- | ----- | -------- | --- | --- | --- | --- | --- |
| (a) If\mathcal{T}  | isinvertible,then\mathcal{T}†      |     | =\mathcal{T}-1. |          |     |     |     |     |     |
\mathcal{T}\mathcal{T}†
| (b) | =\mathcal{P}  | =theorthogonalprojectionof\mathcal{W} |     |     |     | ontorange\mathcal{T}. |     |     |     |
| --- | --- | --------------------------- | --- | --- | --- | ----------- | --- | --- | --- |
range\mathcal{T}
| \mathcal{T}†\mathcal{T} |             |                             |     |     |     | onto(null\mathcal{T})⟂. |     |     |     |
| --- | ----------- | --------------------------- | --- | --- | --- | ------------- | --- | --- | --- |
| (c) | =\mathcal{P} (null\mathcal{T})⟂ | =theorthogonalprojectionof\mathcal{V} |     |     |     |               |     |     |     |
Proof
$$(a) Suppose \mathcal{T} is invertible. Then (null\mathcal{T})⟂ = \mathcal{V} and range\mathcal{T} = \mathcal{W}. Thus$$
|             |     |      |                           |     |     |     | Hence\mathcal{T}† |     | =\mathcal{T}-1. |
| ----------- | --- | ---- | ------------------------- | --- | --- | --- | ------- | --- | ----- |
| \mathcal{T}| (null\mathcal{T})⟂ | =\mathcal{T}  | and\mathcal{P} | istheidentityoperatoron\mathcal{W}. |     |     |     |         |     |       |
range\mathcal{T}
| (b) Supposew\inrange\mathcal{T}.     |     |           | Thus |               |     |        |     |         |     |
| ------------------------ | --- | --------- | ---- | ------------- | --- | ------ | --- | ------- | --- |
|                          |     | \mathcal{T}\mathcal{T}†w=\mathcal{T}(\mathcal{T}| |      | )-1w=w=\mathcal{P}      |     |        |     |         |     |
|                          |     |           |      | (null\mathcal{T})⟂      |     | range\mathcal{T} | w.  |         |     |
| Ifw\in(range\mathcal{T})⟂,then\mathcal{T}†w=0. |     |           |      | Hence\mathcal{T}\mathcal{T}†w=0=\mathcal{P} |     |        |     | Thus\mathcal{T}\mathcal{T}† |     |
w.
range\mathcal{T}
| and\mathcal{P} | agreeonrange\mathcal{T}andon(range\mathcal{T})⟂. |     |     |     |     | Hencethesetwolinearmaps |     |     |     |
| ---- | ---------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
range\mathcal{T}
areequal(by6.49).
|              |     | (null\mathcal{T})⟂. |           |     | range\mathcal{T},thedefinitionof\mathcal{T}† |     |     |     |       |
| ------------ | --- | --------- | --------- | --- | ------------------------ | --- | --- | --- | ----- |
| (c) Supposev | \in   |           | Because\mathcal{T}v | \in   |                          |     |     |     | shows |
that
|       |                | \mathcal{T}†(\mathcal{T}v)=(\mathcal{T}| |          | )-1(\mathcal{T}v)=v=\mathcal{P} |            |          |          |     |         |
| ----- | -------------- | ---------- | -------- | ----------- | ---------- | -------- | -------- | --- | ------- |
|       |                |            | (null\mathcal{T})⟂ |             |            | (null\mathcal{T})⟂ | v.       |     |         |
| Ifv \in | null\mathcal{T},then\mathcal{T}†\mathcal{T}v |            | = 0      | = \mathcal{P}         | v. Thus\mathcal{T}†\mathcal{T} |          | and\mathcal{P}     |     | agreeon |
|       |                |            |          | (null\mathcal{T})⟂    |            |          | (null\mathcal{T})⟂ |     |         |
$$(null\mathcal{T})⟂$$
|         | andonnull\mathcal{T}. |             | Hencethesetwolinearmapsareequal(by6.49). |      |                   |     |     |             |     |
| ------- | ----------- | ----------- | ---------------------------------------- | ---- | ----------------- | --- | --- | ----------- | --- |
| Suppose | that        | \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). | If                                       | \mathcal{T} is |                   |     |     |             |     |
|         |             |             |                                          |      | The pseudoinverse |     | is  | also called | the |
surjective,then\mathcal{T}\mathcal{T}†istheidentityoperaMoore–Penroseinverse.
toron\mathcal{W},asfollowsfrom(b)intheresult
isinjective,then\mathcal{T}†\mathcal{T}
| above. If\mathcal{T} |     |     |     | istheidentityoperatoron\mathcal{V},asfollowsfrom |     |     |     |     |     |
| ---------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
$$(c)intheresultabove. Foradditionalalgebraicpropertiesofthepseudoinverse,$$
see Exercises19–23.

222 Chapter 6 Inner Product Spaces
For\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})andw\in\mathcal{W},wenowreturntotheproblemoffindingv\in\mathcal{V}
thatsolvestheequation
\mathcal{T}v=w.
Aswenotedearlier,if\mathcal{T} isinvertible,thenv=\mathcal{T}-1wistheuniquesolution,but
if\mathcal{T} isnotinvertible,then\mathcal{T}-1 isnotdefined. However,thepseudoinverse\mathcal{T}† is
defined. Takingv=\mathcal{T}†wmakes\mathcal{T}vasclosetowaspossible,asshownby(a)of
thenextresult. Thusthepseudoinverseprovideswhatiscalledabestfit tothe
equationabove.
Amongallvectorsv\in\mathcal{V} thatmake\mathcal{T}vascloseaspossibletow,thevector
\mathcal{T}†whasthesmallestnorm,asshownbycombining(b)inthenextresultwiththe
conditionforequalityin(a).
6.70 pseudoinverseprovidesbestapproximatesolutionorbestsolution
Suppose\mathcal{V} isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}),andw\in\mathcal{W}.
$$(a) Ifv\in\mathcal{V},then$$
∥\mathcal{T}(\mathcal{T}†w)-w∥\leq‖\mathcal{T}v-w‖,
withequalityifandonlyifv\in\mathcal{T}†w+null\mathcal{T}.
$$(b) Ifv\in\mathcal{T}†w+null\mathcal{T},then$$
∥\mathcal{T}†w∥\leq‖v‖,
withequalityifandonlyifv=\mathcal{T}†w.
Proof
$$(a) Supposev\in\mathcal{V}. Then$$
\mathcal{T}v-w=(\mathcal{T}v-\mathcal{T}\mathcal{T}†w)+(\mathcal{T}\mathcal{T}†w-w).
Thefirstterminparenthesesaboveisinrange\mathcal{T}. Becausetheoperator\mathcal{T}\mathcal{T}†
istheorthogonalprojectionof\mathcal{W} ontorange\mathcal{T} [by6.69(b)],thesecondterm
inparenthesesaboveisin(range\mathcal{T})⟂ [see6.57(f)].
thesecondterminparenthesesaboveislessthanorequalto‖\mathcal{T}v-w‖,with
equalityifandonlyifthefirstterminparenthesesaboveequals0. Hence
wehaveequalityifandonlyifv-\mathcal{T}†w\innull\mathcal{T},whichisequivalenttothe
statementthatv\in\mathcal{T}†w+null\mathcal{T},completingtheproofof(a).
$$(b) Supposev\in\mathcal{T}†w+null\mathcal{T}. Hencev-\mathcal{T}†w\innull\mathcal{T}. Now$$
$$v=(v-\mathcal{T}†w)+\mathcal{T}†w.$$
Thedefinitionof\mathcal{T}† impliesthat\mathcal{T}†w \in (null\mathcal{T})⟂. Thusthe Pythagorean
theoremimpliesthat∥\mathcal{T}†w∥\leq‖v‖,withequalityifandonlyifv=\mathcal{T}†w.
Aformulafor\mathcal{T}† willbegiveninthenextchapter(see7.78).

| --------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | pseudoinverseofalinearmapfrom\mathbf{F}4 |     |     |     |     | to\mathbf{F}3 |     |
| --- | ------------------------------- | --- | --- | --- | --- | ---- | --- |
**6.71 例：** | Suppose\mathcal{T} | \inℒ(\mathbf{F}4,\mathbf{F}3)isdefinedby |     |     |     |     |     |     |
| -------- | -------------------- | --- | --- | --- | --- | --- | --- |
\mathcal{T}(a,b,c,d)=(a+b+c,2c+d,0).
Thislinearmapisneitherinjectivenorsurjective,butwecancomputeitspseudo-
={(x,y,0)∶x,y
| inverse. | Todothis,firstnotethatrange\mathcal{T} |     |                 |     |     |     | \in\mathbf{F}}. Thus |
| -------- | ---------------------------- | --- | --------------- | --- | --- | --- | --------- |
|          |                              | \mathcal{P}   | (x,y,z)=(x,y,0) |     |     |     |           |
range\mathcal{T}
| foreach(x,y,z)\in\mathbf{F}3. |     | Also, |     |     |     |     |     |
| ------------------ | --- | ----- | --- | --- | --- | --- | --- |
∶a+b+c
|     | null\mathcal{T} | ={(a,b,c,d)\in\mathbf{F}4 |     |     | =0and2c+d |     | =0}. |
| --- | ----- | -------------- | --- | --- | --------- | --- | ---- |
Thelist(-1,1,0,0),(-1,0,1,-2)oftwovectorsinnull\mathcal{T} spansnull\mathcal{T} because
| if(a,b,c,d)\innull\mathcal{T} |     | then |     |     |     |     |     |
| ----------------- | --- | ---- | --- | --- | --- | --- | --- |
$$(a,b,c,d)=b(-1,1,0,0)+c(-1,0,1,-2).$$
Becausethelist(-1,1,0,0),(-1,0,1,-2)islinearlyindependent,thislistisa
basisofnull\mathcal{T}.
| Nowsuppose(x,y,z)\in\mathbf{F}3. |               |          | Then |             |     |           |             |
| --------------------- | ------------- | -------- | ---- | ----------- | --- | --------- | ----------- |
|                       | \mathcal{T}†(x,y,z)=(\mathcal{T}| |          | )-1\mathcal{P} | (x,y,z)=(\mathcal{T}| |     |           | )-1(x,y,0). |
| 6.72                  |               | (null\mathcal{T})⟂ |      | range\mathcal{T}      |     | (null\mathcal{T})⟂  |             |
|                       |               |          |      |             |     | (a,b,c,d) | \mathbf{F}4          |
The right side of the equation above is the vector \in such that
\mathcal{T}(a,b,c,d)=(x,y,0)and(a,b,c,d)\in(null\mathcal{T})⟂. Inotherwords,a,b,c,dmust
satisfythefollowingequations:
a+b+c
=x
|     |     |     |     | 2c+d | =y  |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- |
-a+b=0
|     |     |     | -a+c-2d |     | =0, |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- |
wherethefirsttwoequationsareequivalenttotheequation\mathcal{T}(a,b,c,d)=(x,y,0)
andthelasttwoequationscomefromtheconditionfor(a,b,c,d)tobeorthogonal
to each of the basis vectors (-1,1,0,0),(-1,0,1,-2) in this basis of null\mathcal{T}.
Thinking of and as constants and a, b, c, as unknowns, we can solve the
|     | x   | y   |     |     | d   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
systemaboveoffourequationsinfourunknowns,getting
|     | 1           | 1   |          |     | 1       |     | 1           |
| --- | ----------- | --- | -------- | --- | ------- | --- | ----------- |
|     | a= (5x-2y), | b=  | (5x-2y), | c = | (x+4y), | d   | = (-2x+3y). |
|     | 11          | 11  |          |     | 11      |     | 11          |
Hence6.72tellsusthat
|     | \mathcal{T}†(x,y,z)= | 1   |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- |
$$(5x-2y,5x-2y,x+4y,-2x+3y).$$
Theformulaabovefor\mathcal{T}†showsthat\mathcal{T}\mathcal{T}†(x,y,z)=(x,y,0)forall(x,y,z)\in\mathbf{F}3,
whichillustratestheequation\mathcal{T}\mathcal{T}†
|     |     |     | =\mathcal{P}  |     | from6.69(b). |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- |
range\mathcal{T}

| -------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
| Exercises  | 6C   |     |           |     |     |     |     |     |
| ---------- | ---- | --- | --------- | --- | --- | --- | --- | --- |
| 1 Supposev | ,…,v | \in\mathcal{V}. | Provethat |     |     |     |     |     |
1 m
|            |                | {v  | ,…,v | }⟂ =(span(v |         | ,…,v | ))⟂. |     |
| ---------- | -------------- | --- | ---- | ----------- | ------- | ---- | ---- | --- |
|            |                |     | 1    | m           |         | 1    | m    |     |
| 2 Suppose\mathcal{U} | isasubspaceof\mathcal{V} |     |      | withbasisu  |         | ,…,u | and  |     |
|            |                |     |      |             |         | 1    | m    |     |
|            |                |     | u    | ,…,u        | ,v ,…,v |      |      |     |
|            |                |     |      | 1           | m 1     | n    |      |     |
isabasisof\mathcal{V}. Provethatifthe Gram–Schmidtprocedureisappliedtothe
| basisof\mathcal{V}                  | above,producingaliste |                     |                               |                            | ,…,e                        | , ,…,       | ,thene ,…,e | isan   |
| ------------------------- | --------------------- | ------------------- | ----------------------------- | -------------------------- | --------------------------- | ----------- | ----------- | ------ |
|                           |                       |                     |                               |                            | 1 m                         | f 1         | f n 1       | m      |
| orthonormalbasisof\mathcal{U}       |                       |                     | and                           | f ,…,                      | f isanorthonormalbasisof\mathcal{U}⟂. |             |             |        |
|                           |                       |                     |                               | 1                          | n                           |             |             |        |
| 3 Suppose\mathcal{U}                | isthesubspaceof\mathbf{R}4     |                     |                               | definedby                  |                             |             |             |        |
|                           |                       | \mathcal{U}                   | =span((1,2,3,-4),(-5,4,3,2)). |                            |                             |             |             |        |
| Findanorthonormalbasisof\mathcal{U} |                       |                     |                               | andanorthonormalbasisof\mathcal{U}⟂. |                             |             |             |        |
|                           | ,…,e                  |                     |                               |                            |                             |             |             | =1,…,n |
| 4 Supposee                |                       | isalistofvectorsin\mathcal{V} |                               |                            | with‖e                      | ‖=1foreachk |             |        |
|                           | 1                     | n                   |                               |                            |                             | k           |             |        |
and
|            |     |            | ‖v‖2 =∣\langlev,e |                          | \rangle∣2+⋯+∣\langlev,e |     | \rangle∣2 |     |
| ---------- | --- | ---------- | ----------- | ------------------------ | ----------- | --- | --- | --- |
|            |     |            |             | 1                        |             |     | n   |     |
| forallv\in\mathcal{V}. |     | Provethate | ,…,e        | isanorthonormalbasisof\mathcal{V}. |             |     |     |     |
|            |     |            | 1           | n                        |             |     |     |     |
Thisexerciseprovidesaconverseto6.30(b).
5 Supposethat\mathcal{V} isfinite-dimensionaland\mathcal{U} isasubspaceof\mathcal{V}. Showthat
| \mathcal{P} =\mathcal{I}-\mathcal{P}     |                          | ,where\mathcal{I} | istheidentityoperatoron\mathcal{V}. |          |          |        |          |     |
| ---------- | ------------------------ | ------- | ------------------------- | -------- | -------- | ------ | -------- | --- |
| \mathcal{U}⟂         | \mathcal{U}                        |         |                           |          |          |        |          |     |
| 6 Suppose\mathcal{V} | isfinite-dimensionaland\mathcal{T} |         |                           |          | \inℒ(\mathcal{V},\mathcal{W}). |        | Showthat |     |
|            |                          |         | \mathcal{T} =\mathcal{T}\mathcal{P}                     |          | =\mathcal{P}       | \mathcal{T}.     |          |     |
|            |                          |         |                           | (null\mathcal{T})⟂ |          | range\mathcal{T} |          |     |
Suppose that \mathcal{X} and \mathcal{Y} are finite-dimensional subspaces of \mathcal{V}. Prove that
| \mathcal{P} \mathcal{P} =0ifandonlyif\langlex,y\rangle=0forallx |     |     |     |     |     | \in\mathcal{X} andally | \in\mathcal{Y}. |     |
| ------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- |
\mathcal{X} \mathcal{Y}
8 Suppose\mathcal{U}isafinite-dimensionalsubspaceof\mathcal{V} andv\in\mathcal{V}. Definealinear
functional\phi∶
|     |     | \mathcal{U} \rightarrow\mathbf{F} | by  |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- |
\phi(u)=\langleu,v\rangle
forallu\in\mathcal{U}. Bythe Rieszrepresentationtheorem(6.42)asappliedtothe
| innerproductspace\mathcal{U},thereexistsauniquevectorw\in\mathcal{U} |     |     |     |     |     |     | suchthat |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- |
\phi(u)=\langleu,w\rangle
| forallu\in\mathcal{U}. |     | Showthatw=\mathcal{P} |     | v.  |     |     |     |     |
| ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
\mathcal{U}
ℒ(\mathcal{V})issuchthat\mathcal{P}2
| 9 Suppose\mathcal{V} | isfinite-dimensional. |     |     | Suppose\mathcal{P} |     | \in   |     | = \mathcal{P} |
| ---------- | --------------------- | --- | --- | -------- | --- | --- | --- | --- |
andeveryvectorinnull\mathcal{P} isorthogonaltoeveryvectorinrange\mathcal{P}. Prove
| thatthereexistsasubspace\mathcal{U} |     |     |     | of\mathcal{V} | suchthat\mathcal{P} | =\mathcal{P}  | .   |     |
| ------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- |
\mathcal{U}

| --------- | -------------------------------------------- | --- | --- | --- |
\inℒ(\mathcal{V})issuchthat\mathcal{P}2
| 10 Suppose\mathcal{V} | isfinite-dimensionaland\mathcal{P} |     |     | =\mathcal{P}and |
| ----------- | ------------------------ | --- | --- | ----- |
‖\mathcal{P}v‖\leq‖v‖
foreveryv\in\mathcal{V}. Provethatthereexistsasubspace\mathcal{U}of\mathcal{V} suchthat\mathcal{P} =\mathcal{P} .
\mathcal{U}
11 Suppose\mathcal{T} \inℒ(\mathcal{V})and\mathcal{U} isafinite-dimensionalsubspaceof\mathcal{V}. Provethat
|     | \mathcal{U} isinvariantunder\mathcal{T} | ⟺ \mathcal{P} \mathcal{T}\mathcal{P} | =\mathcal{T}\mathcal{P} . |     |
| --- | ------------------- | ------ | ----- | --- |
|     |                     | \mathcal{U}      | \mathcal{U} \mathcal{U}   |     |
ℒ(\mathcal{V}),
12 Suppose \mathcal{V} is finite-dimensional, \mathcal{T} \in and \mathcal{U} is a subspace of \mathcal{V}.
Provethat
|     | \mathcal{U} and\mathcal{U}⟂ arebothinvariantunder\mathcal{T} |     | ⟺ \mathcal{P} \mathcal{T} =\mathcal{T}\mathcal{P} | .   |
| --- | ------------------------------ | --- | --------- | --- |
|     |                                |     | \mathcal{U}         | \mathcal{U}   |
13 Suppose\mathbf{F} =\mathbf{R} and\mathcal{V} isfinite-dimensional. Foreachv\in\mathcal{V},let\phi v denote
thelinearfunctionalon\mathcal{V} definedby
\phi (u)=\langleu,v\rangle
v
forallu\in\mathcal{V}.
to\mathcal{V}′.
| (a) Showthatv↦\phi | isaninjectivelinearmapfrom\mathcal{V} |     |     |     |
| --------------- | --------------------------- | --- | --- | --- |
v
| (b) Use(a)andadimension-countingargumenttoshowthatv↦\phi |     |     |     | isan |
| ----------------------------------------------------- | --- | --- | --- | ---- |
v
isomorphismfrom\mathcal{V} onto\mathcal{V}′.
The purpose of this exercise is to give an alternative proof of the Riesz
| representationtheorem(6.42and6.58)when\mathbf{F} |     |     | =\mathbf{R}. Thusyoushouldnot |     |
| --------------------------------------- | --- | --- | -------------------- | --- |
usethe Rieszrepresentationtheoremasatoolinyoursolution.
,…,e
14 Supposethate 1 n isanorthonormalbasisof\mathcal{V}. Explainwhythedual
basis(see3.112)ofe ,…,e ise ,…,e undertheidentificationof\mathcal{V}′ with
1 n 1 n
\mathcal{V} providedbythe Rieszrepresentationtheorem(6.58).
In\mathbf{R}4,let
\mathcal{U} =span((1,1,0,0),(1,1,1,2)).
| Findu\in\mathcal{U} | suchthat‖u-(1,2,3,4)‖isassmallaspossible. |     |     |     |
| ------- | ----------------------------------------- | --- | --- | --- |
16 Suppose\mathcal{C}[-1,1]isthevectorspaceofcontinuousreal-valuedfunctions
ontheinterval[-1,1]withinnerproductgivenby
\langlef,g\rangle=\int fg
-1
| forall | f,g \in\mathcal{C}[-1,1]. Let\mathcal{U} bethesubspaceof\mathcal{C}[-1,1]definedby |     |     |     |
| ------ | -------------------------------------------------- | --- | --- | --- |
\in\mathcal{C}[-1,1]∶
\mathcal{U} ={f f(0)=0}.
| (a) Showthat\mathcal{U}⟂ | ={0}. |     |     |     |
| -------------- | ----- | --- | --- | --- |
$$(b) Show that 6.49 and 6.52 do not hold without the finite-dimensional$$
hypothesis.

| -------- | ------------------ | --- | --- | --- |
| Findp\in𝒫 | (\mathbf{R})suchthatp(0)=0,p′(0)=0,and\int |     |     | ∣2+3x-p(x)∣2dxis |
| ------- | ------------------------------ | --- | --- | ---------------- |
assmallaspossible.
\pi
| Findp\in𝒫 |               |     | ∣sinx-p(x)∣2dxassmallaspossible. |     |
| ------- | ------------- | --- | -------------------------------- | --- |
| 18      | (\mathbf{R})thatmakes\int |     |                                  |     |
-\pi
Thepolynomial6.65isanexcellentapproximationtotheanswertothis
exercise,buthereyouareaskedtofindtheexactsolution,whichinvolves
| powersof | \pi.  | Acomputerthatcanperformsymbolicintegrationshould |     |     |
| -------- | --- | ------------------------------------------------ | --- | --- |
help.
Suppose\mathcal{V} isfinite-dimensionaland\mathcal{P} \inℒ(\mathcal{V})isanorthogonalprojection
Provethat\mathcal{P}†
| of\mathcal{V} ontosomesubspaceof\mathcal{V}. |                          |            |             | =\mathcal{P}.        |
| ------------------------ | ------------------------ | ---------- | ----------- | ---------- |
| 20 Suppose\mathcal{V}              | isfinite-dimensionaland\mathcal{T} |            | \inℒ(\mathcal{V},\mathcal{W}).    | Showthat   |
|                          | null\mathcal{T}†                   | =(range\mathcal{T})⟂ | and range\mathcal{T}† | =(null\mathcal{T})⟂. |
\inℒ(\mathbf{F}3,\mathbf{F}2)isdefinedby
21 Suppose\mathcal{T}
\mathcal{T}(a,b,c)=(a+b+c,2b+3c).
| (a) For(x,y)\in\mathbf{F}2,findaformulafor\mathcal{T}†(x,y). |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- |
$$(b) Verify that the equation \mathcal{T}\mathcal{T}† = \mathcal{P} from 6.69(b) holds with the$$
range\mathcal{T}
formulafor\mathcal{T}†
obtainedin(a).
\mathcal{T}†\mathcal{T}
$$(c) Verify that the equation = \mathcal{P} (null\mathcal{T})⟂ from 6.69(c) holds with the$$
formulafor\mathcal{T}† obtainedin(a).
| 22 Suppose\mathcal{V} | isfinite-dimensionaland\mathcal{T} |         | \inℒ(\mathcal{V},\mathcal{W}).  | Provethat |
| ----------- | ------------------------ | ------- | --------- | --------- |
|             |                          | \mathcal{T}\mathcal{T}†\mathcal{T} =\mathcal{T} | and \mathcal{T}†\mathcal{T}\mathcal{T}† | =\mathcal{T}†.      |
Bothformulasaboveclearlyholdif \mathcal{T}isinvertiblebecauseinthatcasewe
canreplace\mathcal{T}†with\mathcal{T}-1.
23 Suppose\mathcal{V} and\mathcal{W} arefinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Provethat
$$(\mathcal{T}†) † =\mathcal{T}.$$
Theequationaboveisanalogoustotheequation(\mathcal{T}-1)-1
=\mathcal{T}thatholdsif
\mathcal{T}isinvertible.
