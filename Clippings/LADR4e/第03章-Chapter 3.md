---
title: Chapter 3
source: Clippings/LADR4e.pdf
created: 2026-04-23
type: chapter
tags:
  - book
  - chapter
---

# Chapter 3
So far our attention has focused on vector spaces. No one gets excited about
vectorspaces. Theinterestingpartoflinearalgebraisthesubjecttowhichwe
nowturn—linearmaps.
We will frequently use the powerful fundamental theorem of linear maps,
whichstatesthatthedimensionofthedomainofalinearmapequalsthedimension
ofthesubspacethatgetssentto0plusthedimensionoftherange. Thiswillimply
thestrikingresultthatalinearmapfromafinite-dimensionalvectorspacetoitself
isone-to-oneifandonlyifitsrangeisthewholespace.
Amajorconceptthatwewillintroduceinthischapteristhematrixassociated
withalinearmapandwithabasisofthedomainspaceandabasisofthetarget
space. Thiscorrespondencebetweenlinearmapsandmatricesprovidesmuch
insightintokeyaspectsoflinearalgebra.
Thischapterconcludesbyintroducingproduct,quotient,anddualspaces.
Inthischapterwewillneedadditionalvectorspaces,whichwecall\mathcal{U} and\mathcal{W},
inadditionto\mathcal{V}. Thusourstandingassumptionsarenowasfollows.
standingassumptionsforthischapter
• \mathbf{F} denotes\mathbf{R} or\mathbf{C}.
• \mathcal{U},\mathcal{V},and\mathcal{W} denotevectorspacesover\mathbf{F}.
Stefan Schäfer CCBY-SA
Thetwelfth-century Dankwarderode Castlein Brunswick(Braunschweig),where Carl
Friedrich Gauss(1777–1855)wasbornandgrewup. In1809Gausspublishedamethod
forsolvingsystemsoflinearequations. Thismethod,nowcalled Gaussianelimination,
wasusedina Chinesebookwrittenover1600yearsearlier.

| -------- | ---------- | --- | --- | --- |
| 3A Vector  | Space        | of Linear Maps |      |     |
| ---------- | ------------ | -------------- | ---- | --- |
| Definition | and Examples | of Linear      | Maps |     |
Nowwearereadyforoneofthekeydefinitionsinlinearalgebra.
| 3.1 definition: | linearmap |     |     |     |
| --------------- | --------- | --- | --- | --- |
\mathcal{T}∶
A linear map from \mathcal{V} to \mathcal{W} is a function \mathcal{V} \rightarrow \mathcal{W} with the following
properties.
additivity
\mathcal{T}(u+v)=\mathcal{T}u+\mathcal{T}vforallu,v\in\mathcal{V}.
homogeneity
| \mathcal{T}(\lambdav)= | \lambda(\mathcal{T}v)forall | \lambda\in\mathbf{F} andallv\in\mathcal{V}. |     |     |
| ------ | ----------- | -------------- | --- | --- |
Note that for linear maps we often Somemathematiciansusethephrase
usethenotation\mathcal{T}vaswellastheusual
|                           |             |     | linear transformation, | which means   |
| ------------------------- | ----------- | --- | ---------------------- | ------------- |
| functionnotation\mathcal{T}(v).     |             |     | thesameaslinearmap.    |               |
| 3.2 notation:             | ℒ(\mathcal{V},\mathcal{W}),ℒ(\mathcal{V}) |     |                        |               |
| • Thesetoflinearmapsfrom\mathcal{V} |             | to\mathcal{W} | isdenotedbyℒ(\mathcal{V},\mathcal{W}).     |               |
| • Thesetoflinearmapsfrom\mathcal{V} |             | to\mathcal{V} | isdenotedbyℒ(\mathcal{V}).       | Inotherwords, |
ℒ(\mathcal{V})=ℒ(\mathcal{V},\mathcal{V}).
Let’slookatsomeexamplesoflinearmaps. Makesureyouverifythateach
ofthefunctionsdefinedinthenextexampleisindeedalinearmap:
| 3.3 example: | linearmaps |     |     |     |
| ------------ | ---------- | --- | --- | --- |
zero
Inadditiontoitsotheruses,weletthesymbol0denotethelinearmapthattakes
everyelementofsomevectorspacetotheadditiveidentityofanother(orpossibly
| thesame)vectorspace. |     | Tobespecific,0\inℒ(\mathcal{V},\mathcal{W})isdefinedby |     |     |
| -------------------- | --- | -------------------------------- | --- | --- |
0v=0.
The0ontheleftsideoftheequationaboveisafunctionfrom\mathcal{V} to\mathcal{W},whereas
the0ontherightsideistheadditiveidentityin\mathcal{W}. Asusual,thecontextshould
allowyoutodistinguishbetweenthemanyusesofthesymbol0.
identityoperator
Theidentityoperator,denotedby\mathcal{I},isthelinearmaponsomevectorspacethat
| takeseachelementtoitself. |     | Tobespecific,\mathcal{I} | \inℒ(\mathcal{V})isdefinedby |     |
| ------------------------- | --- | -------------- | ---------------- | --- |
\mathcal{I}v=v.

| --- | --- | --------- | ----------------------- | --- | --- |
differentiation
Define\mathcal{D}\inℒ(𝒫(\mathbf{R}))by
\mathcal{D}p=p′.
Theassertionthatthisfunctionisalinearmapisanotherwayofstatingabasic
resultaboutdifferentiation: (f +g)′ = f′+g′ and(\lambdaf)′ = \lambdaf′ whenever f,g
| aredifferentiableand |     | \lambdaisaconstant. |     |     |     |
| -------------------- | --- | ------------- | --- | --- | --- |
integration
Define\mathcal{T} \inℒ(𝒫(\mathbf{R}),\mathbf{R})by
|     |     | \mathcal{T}p=\int | p.  |     |     |
| --- | --- | ---- | --- | --- | --- |
Theassertionthatthisfunctionislinearisanotherwayofstatingabasicresult
aboutintegration: theintegralofthesumoftwofunctionsequalsthesumofthe
integrals,andtheintegralofaconstanttimesafunctionequalstheconstanttimes
theintegralofthefunction.
multiplicationbyx2
| Definealinearmap\mathcal{T} |     | \inℒ(𝒫(\mathbf{R}))by |     |     |     |
| ----------------- | --- | ---------- | --- | --- | --- |
$$(\mathcal{T}p)(x)=x2p(x)$$
| foreachx | \in\mathbf{R}. |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
backwardshift
Recallthat\mathbf{F}\infty
|             | denotesthevectorspaceofallsequencesofelementsof\mathbf{F}. |       |           |      | Define |
| ----------- | ------------------------------------------------- | ----- | --------- | ---- | ------ |
| alinearmap\mathcal{T} | \inℒ(\mathbf{F}\infty)by                                          |       |           |      |        |
|             |                                                   | ,x ,x | ,…)=(x ,x | ,…). |        |
\mathcal{T}(x
|     |     | 1 2 | 3 2 | 3   |     |
| --- | --- | --- | --- | --- | --- |
from\mathbf{R}3 to\mathbf{R}2
| Definealinearmap\mathcal{T} |     | \inℒ(\mathbf{R}3,\mathbf{R}2)by |     |     |     |
| ----------------- | --- | ----------- | --- | --- | --- |
\mathcal{T}(x,y,z)=(2x-y+3z,7x+5y-6z).
from\mathbf{F}n to\mathbf{F}m
Togeneralizethepreviousexample,letmandnbepositiveintegers,let\mathcal{A} \in\mathbf{F}
j,k
foreachj =1,…,mandeachk =1,…,n,anddefinealinearmap\mathcal{T} \inℒ(\mathbf{F}n,\mathbf{F}m)
by
|                              | \mathcal{T}(x ,…,x )=(\mathcal{A} | x +⋯+\mathcal{A} | x ,…,\mathcal{A}             | x +⋯+\mathcal{A} | x ).  |
| ---------------------------- | ------------- | ------ | ------------------ | ------ | ----- |
|                              | 1 n           | 1,1 1  | 1,n n              | m,1 1  | m,n n |
| Actuallyeverylinearmapfrom\mathbf{F}n |               |        | to\mathbf{F}m isofthisform. |        |       |
composition
| Fixapolynomialq\in𝒫(\mathbf{R}). |     | Definealinearmap\mathcal{T} |     | \inℒ(𝒫(\mathbf{R}))by |     |
| --------------------- | --- | ----------------- | --- | ---------- | --- |
$$(\mathcal{T}p)(x)=p(q(x)).$$
Theexistencepartofthenextresultmeansthatwecanfindalinearmapthat
takesonwhatevervalueswewishonthevectorsinabasis. Theuniquenesspart
ofthenextresultmeansthatalinearmapiscompletelydeterminedbyitsvalues
onabasis.

54 Chapter 3 Linear Maps
3.4 linearmaplemma
Supposev ,…,v isabasisof\mathcal{V} andw ,…,w \in \mathcal{W}. Thenthereexistsa
1 n 1 n
uniquelinearmap\mathcal{T}∶ \mathcal{V} \rightarrow\mathcal{W} suchthat
\mathcal{T}v =w
k k
foreachk =1,…,n.
Proof Firstweshowtheexistenceofalinearmap\mathcal{T} withthedesiredproperty.
Define\mathcal{T}∶ \mathcal{V} \rightarrow\mathcal{W} by
\mathcal{T}(c v +⋯+c v )=c w +⋯+c w ,
1 1 n n 1 1 n n
wherec ,…,c arearbitraryelementsof\mathbf{F}. Thelistv ,…,v isabasisof\mathcal{V}. Thus
1 n 1 n
theequationabovedoesindeeddefineafunction\mathcal{T} from\mathcal{V} to\mathcal{W} (becauseeach
elementof\mathcal{V} canbeuniquelywrittenintheformc v +⋯+c v ).
1 1 n n
Foreachk,takingc = 1andtheotherc’sequalto0intheequationabove
k
showsthat\mathcal{T}v =w .
k k
Ifu,v\in\mathcal{V} withu=a v +⋯+a v andv=c v +⋯+c v ,then
1 1 n n 1 1 n n
\mathcal{T}(u+v)=\mathcal{T}((a +c )v +⋯+(a +c )v )
1 1 1 n n n
=(a +c )w +⋯+(a +c )w
1 1 1 n n n
=(a w +⋯+a w )+(c w +⋯+c w )
1 1 n n 1 1 n n
=\mathcal{T}u+\mathcal{T}v.
Similarly,if \lambda\in\mathbf{F} andv=c v +⋯+c v ,then
1 1 n n
\mathcal{T}(\lambdav)=\mathcal{T}(\lambdac v +⋯+ \lambdac v )
1 1 n n
= \lambdac w +⋯+ \lambdac w
1 1 n n
= \lambda(c w +⋯+c w )
1 1 n n
= \lambda\mathcal{T}v.
Thus\mathcal{T} isalinearmapfrom\mathcal{V} to\mathcal{W}.
Toproveuniqueness,nowsupposethat\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})andthat\mathcal{T}v =w for
k k
each k = 1,…,n. Let c ,…,c \in \mathbf{F}. Then the homogeneity of \mathcal{T} implies that
1 n
\mathcal{T}(c v )=c w foreachk =1,…,n. Theadditivityof\mathcal{T} nowimpliesthat
k k k k
\mathcal{T}(c v +⋯+c v )=c w +⋯+c w .
1 1 n n 1 1 n n
Thus\mathcal{T}isuniquelydeterminedonspan(v ,…,v )bytheequationabove. Because
1 n
v ,…,v is a basis of \mathcal{V}, this implies that \mathcal{T} is uniquely determined on \mathcal{V}, as
1 n
desired.

| --- | --- | --- | --------- | ----------------------- | --- | --- | --- |
| Algebraic |     | Operations | on  | ℒ(\mathcal{V},\mathcal{W}) |     |     |     |
| --------- | --- | ---------- | --- | ------ | --- | --- | --- |
Webeginbydefiningadditionandscalarmultiplicationonℒ(\mathcal{V},\mathcal{W}).
additionandscalarmultiplicationonℒ(\mathcal{V},\mathcal{W})
**3.5 定义：** | Suppose\mathcal{S},\mathcal{T}         |     | \inℒ(\mathcal{V},\mathcal{W})and |     | \lambda\in\mathbf{F}. Thesum\mathcal{S}+\mathcal{T} | andtheproduct | \lambda\mathcal{T}  | are |
| ------------------ | --- | ---------- | --- | -------------- | ------------- | --- | --- |
| thelinearmapsfrom\mathcal{V} |     |            | to\mathcal{W} | definedby      |               |     |     |
$$(\mathcal{S}+\mathcal{T})(v)=\mathcal{S}v+\mathcal{T}v$$
|     |     |     |     | and (\lambda\mathcal{T})(v)= | \lambda(\mathcal{T}v) |     |     |
| --- | --- | --- | --- | ------------ | ----- | --- | --- |
forallv\in\mathcal{V}.
| Youshouldverifythat\mathcal{S}+\mathcal{T} |     |     |     | and \lambda\mathcal{T} |     |     |     |
| ---------------------- | --- | --- | --- | ------ | --- | --- | --- |
Linearmapsarepervasivethroughout
asdefinedaboveareindeedlinearmaps.
|          |        |        |          | mathematics. | However,theyarenotas |     |     |
| -------- | ------ | ------ | -------- | ------------ | -------------------- | --- | --- |
| In other | words, | if \mathcal{S},\mathcal{T} | \in ℒ(\mathcal{V},\mathcal{W}) | and          |                      |     |     |
ubiquitousasimaginedbypeoplewho
| \lambda\in\mathbf{F},then\mathcal{S}+\mathcal{T} |     | \inℒ(\mathcal{V},\mathcal{W})and |     | \lambda\mathcal{T} \in seemtothinkcosisalinearmapfrom |     |     |     |
| ----------- | --- | ---------- | --- | ----------------------------------- | --- | --- | --- |
ℒ(\mathcal{V},\mathcal{W}).
\mathbf{R}to\mathbf{R}whentheyincorrectlywritethat
Because we took the trouble to de- cos(x+y)equalscosx+cosyandthat
| fineadditionandscalarmultiplicationon |     |     |     | cos2xequals2cosx. |     |     |     |
| ------------------------------------- | --- | --- | --- | ----------------- | --- | --- | --- |
ℒ(\mathcal{V},\mathcal{W}),thenextresultshouldnotbea
surprise.
3.6 ℒ(\mathcal{V},\mathcal{W})isavectorspace
Withtheoperationsofadditionandscalarmultiplicationasdefinedabove,
ℒ(\mathcal{V},\mathcal{W})isavectorspace.
Theroutineproofoftheresultaboveislefttothereader. Notethattheadditive
identityofℒ(\mathcal{V},\mathcal{W})isthezerolinearmapdefinedin Example3.3.
Usuallyitmakesnosensetomultiplytogethertwoelementsofavectorspace,
butforsomepairsoflinearmapsausefulproductexists,asinthenextdefinition.
| 3.7  | definition: | productoflinearmaps |     |                  |     |        |     |
| ---- | ----------- | ------------------- | --- | ---------------- | --- | ------ | --- |
|      | ℒ(\mathcal{U},\mathcal{V})      |                     |     | ℒ(\mathcal{V},\mathcal{W}),          |     | ℒ(\mathcal{U},\mathcal{W}) |     |
| If \mathcal{T} | \in           | and                 | \mathcal{S} \in | then the product | \mathcal{S}\mathcal{T}  | \in      | is  |
definedby
$$(\mathcal{S}\mathcal{T})(u)=\mathcal{S}(\mathcal{T}u)$$
forallu\in\mathcal{U}.
Thus\mathcal{S}\mathcal{T} isjusttheusualcomposition\mathcal{S}\circ\mathcal{T} oftwofunctions,butwhenboth
functionsarelinear,weusuallywrite\mathcal{S}\mathcal{T} insteadof\mathcal{S}\circ\mathcal{T}. Theproductnotation
\mathcal{S}\mathcal{T} helpsmakethedistributiveproperties(seenextresult)seemnatural.
Notethat\mathcal{S}\mathcal{T} isdefinedonlywhen\mathcal{T} mapsintothedomainof\mathcal{S}. Youshould
verifythat\mathcal{S}\mathcal{T} isindeedalinearmapfrom\mathcal{U} to\mathcal{W} whenever\mathcal{T} \inℒ(\mathcal{U},\mathcal{V})and
\mathcal{S}\inℒ(\mathcal{V},\mathcal{W}).

| -------- | ---------- | --- | --- | --- | --- | --- | --- |
algebraicpropertiesofproductsoflinearmaps
3.8
associativity
| (\mathcal{T} \mathcal{T} )\mathcal{T}                       | = \mathcal{T} (\mathcal{T} \mathcal{T} | )whenever\mathcal{T} |     | ,\mathcal{T} ,and\mathcal{T}             | arelinearmapssuchthat |     |       |
| ----------------------------- | -------- | ---------- | --- | -------------------- | --------------------- | --- | ----- |
| 1 2                           | 3 1 2 3  |            | 1   | 2                    | 3                     |     |       |
| theproductsmakesense(meaning\mathcal{T} |          |            |     | mapsintothedomainof\mathcal{T} |                       |     | ,and\mathcal{T} |
|                               |          |            |     | 3                    |                       |     | 2 2   |
| mapsintothedomainof\mathcal{T}          |          | ).         |     |                      |                       |     |       |
identity
\mathcal{T}\mathcal{I} = \mathcal{I}\mathcal{T} = \mathcal{T} whenever \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}); here the first \mathcal{I} is the identity
| operatoron\mathcal{V},andthesecond\mathcal{I} |     |     | istheidentityoperatoron\mathcal{W}. |     |     |     |     |
| ------------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
distributiveproperties
| (\mathcal{S} + \mathcal{S} | )\mathcal{T} = \mathcal{S} \mathcal{T} +    | \mathcal{S} \mathcal{T} | and         | \mathcal{S}(\mathcal{T} + | \mathcal{T} ) = | \mathcal{S}\mathcal{T} + \mathcal{S}\mathcal{T} | whenever |
| ------ | ------------- | --- | ----------- | ----- | ----- | ------- | -------- |
| 1      | 2 1           | 2   |             | 1     | 2     | 1       | 2        |
| \mathcal{T},\mathcal{T} ,\mathcal{T} | \inℒ(\mathcal{U},\mathcal{V})and\mathcal{S},\mathcal{S} |     | ,\mathcal{S} \inℒ(\mathcal{V},\mathcal{W}). |       |       |         |          |
| 1 2    |               |     | 1 2         |       |       |         |          |
Theroutineproofoftheresultaboveislefttothereader.
Multiplicationoflinearmapsisnotcommutative. Inotherwords, itisnot
necessarilytruethat\mathcal{S}\mathcal{T} =\mathcal{T}\mathcal{S},evenifbothsidesoftheequationmakesense.
| 3.9 example: | twononcommutinglinearmapsfrom𝒫(\mathbf{R})to𝒫(\mathbf{R}) |     |     |     |     |     |     |
| ------------ | --------------------------------------- | --- | --- | --- | --- | --- | --- |
ℒ(𝒫(\mathbf{R}))
Suppose \mathcal{D} \in is the differentiation map defined in Example 3.3
and\mathcal{T} \inℒ(𝒫(\mathbf{R}))isthemultiplicationbyx2 mapdefinedearlierinthissection.
Then
| ((\mathcal{T}\mathcal{D})p)(x)=x2p′(x) |     |     | but ((\mathcal{D}\mathcal{T})p)(x)=x2p′(x)+2xp(x). |     |     |     |     |
| ------------------ | --- | --- | ------------------------------ | --- | --- | --- | --- |
Thus\mathcal{T}\mathcal{D} \neq \mathcal{D}\mathcal{T}—differentiatingandthenmultiplyingbyx2 isnotthesameas
multiplyingbyx2
andthendifferentiating.
linearmapstake0to0
3.10
| Suppose\mathcal{T} | isalinearmapfrom\mathcal{V} |     | to\mathcal{W}. | Then\mathcal{T}(0)=0. |     |     |     |
| -------- | ----------------- | --- | ---- | ----------- | --- | --- | --- |
Byadditivity,wehave
Proof
\mathcal{T}(0)=\mathcal{T}(0+0)=\mathcal{T}(0)+\mathcal{T}(0).
Addtheadditiveinverseof\mathcal{T}(0)toeachsideoftheequationabovetoconclude
that\mathcal{T}(0)=0.
| Supposem,b\in\mathbf{R}. | Thefunction |     | f∶  | \mathbf{R} \rightarrow\mathbf{R} | definedby |     |     |
| ------------- | ----------- | --- | --- | ---- | --------- | --- | --- |
f(x)=mx+b
isalinearmapifandonlyifb=0(use3.10). Thusthelinearfunctionsofhigh
schoolalgebraarenotthesameaslinearmapsinthecontextoflinearalgebra.

| --- | --- | --- | --------- | --- | ----------------------- | --- | --- |
| Exercises | 3A  |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- |
Define\mathcal{T}∶
| 1   | Supposeb,c | \in\mathbf{R}. |     | \mathbf{R}3  | \rightarrow\mathbf{R}2 by |     |     |
| --- | ---------- | --- | --- | --- | ------ | --- | --- |
\mathcal{T}(x,y,z)=(2x-4y+3z+b,6x+cxyz).
|     | Showthat\mathcal{T}  | islinearifandonlyifb=c |          |         | =0. |     |     |
| --- | ---------- | ---------------------- | -------- | ------- | --- | --- | --- |
| 2   | Supposeb,c | \in\mathbf{R}.                    | Define\mathcal{T}∶ | 𝒫(\mathbf{R})\rightarrow\mathbf{R}2 | by  |     |     |
|     | \mathcal{T}p=(3p(4)+5p′(6)+bp(1)p(2),\int |     |     |     | x3p(x)dx+csinp(0)). |     |     |
| --- | ---------------------------- | --- | --- | --- | ------------------- | --- | --- |
-1
|     | Showthat\mathcal{T} | islinearifandonlyifb=c |     |     | =0. |     |     |
| --- | --------- | ---------------------- | --- | --- | --- | --- | --- |
3 Suppose that \mathcal{T} \in ℒ(\mathbf{F}n,\mathbf{F}m). Show that there exist scalars \mathcal{A} \in \mathbf{F} for
j,k
|     | j =1,…,mandk | =1,…,nsuchthat |       |        |        |        |       |
| --- | ------------ | -------------- | ----- | ------ | ------ | ------ | ----- |
|     | \mathcal{T}(x          | ,…,x )=(\mathcal{A}      |       | x +⋯+\mathcal{A} | x ,…,\mathcal{A} | x +⋯+\mathcal{A} | x )   |
|     |              | 1 n            | 1,1   | 1      | 1,n n  | m,1 1  | m,n n |
|     |              | ,…,x           | )\in\mathbf{F}n. |        |        |        |       |
forevery(x
|     |                                    | 1   | n   |     |                         |     |     |
| --- | ---------------------------------- | --- | --- | --- | ----------------------- | --- | --- |
|     | Thisexerciseshowsthatthelinearmap\mathcal{T} |     |     |     | hastheformpromisedinthe |     |     |
secondtolastitemof Example3.3.
4 Suppose \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}) and v ,…,v is a list of vectors in \mathcal{V} such that
|     |     |     |     | 1   | m   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
\mathcal{T}v ,…,\mathcal{T}v is a linearly independent list in \mathcal{W}. Prove that v ,…,v is
|     | 1   | m   |     |     |     |     | 1 m |
| --- | --- | --- | --- | --- | --- | --- | --- |
linearlyindependent.
5 Provethatℒ(\mathcal{V},\mathcal{W})isavectorspace,aswasassertedin3.6.
6 Provethatmultiplicationoflinearmapshastheassociative,identity,and
distributivepropertiesassertedin3.8.
7 Showthateverylinearmapfromaone-dimensionalvectorspacetoitselfis
multiplicationbysomescalar. Moreprecisely,provethatifdim\mathcal{V} =1and
|     | \mathcal{T} \inℒ(\mathcal{V}),thenthereexists |     |     | \lambda\in\mathbf{F} | suchthat\mathcal{T}v= | \lambdavforallv\in\mathcal{V}. |     |
| --- | ----------------------- | --- | --- | --- | ----------- | ------------ | --- |
Giveanexampleofafunction\phi∶
| 8   |     |     |     |     | \mathbf{R}2 \rightarrow\mathbf{R} suchthat |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- |
\phi(av)=a\phi(v)
|     | foralla\in\mathbf{R} | andallv\in\mathbf{R}2 |     | but\phiisnotlinear. |     |     |     |
| --- | --------- | ---------- | --- | ---------------- | --- | --- | --- |
This exercise and the next exercise show that neither homogeneity nor
additivityaloneisenoughtoimplythatafunctionisalinearmap.
| 9   | Giveanexampleofafunction\phi∶ |     |     |     | \mathbf{C} \rightarrow\mathbf{C} suchthat |     |     |
| --- | -------------------------- | --- | --- | --- | ------------- | --- | --- |
\phi(w+z)=\phi(w)+\phi(z)
forallw,z\in\mathbf{C}but\phiisnotlinear.
$$(Here\mathbf{C}isthoughtofasacomplexvector$$
space.)
Therealsoexistsafunction\phi∶ \mathbf{R} \rightarrow\mathbf{R}suchthat\phisatisfiestheadditivity
conditionabovebut\phiisnotlinear. However,showingtheexistenceofsuch
afunctioninvolvesconsiderablymoreadvancedtools.

| -------- | ---------- | --- | --- | --- | --- |
\mathcal{T}∶
10 Prove or give a counterexample: If q \in 𝒫(\mathbf{R}) and 𝒫(\mathbf{R}) \rightarrow 𝒫(\mathbf{R}) is
| definedby\mathcal{T}p=q\circp,then\mathcal{T} |     | isalinearmap. |     |     |     |
| --------------------- | --- | ------------- | --- | --- | --- |
Thefunction\mathcal{T}definedherediffersfromthefunction\mathcal{T}definedinthelast
bulletpointof3.3bytheorderofthefunctionsinthecompositions.
11 Suppose \mathcal{V} is finite-dimensional and \mathcal{T} \in ℒ(\mathcal{V}). Prove that \mathcal{T} is a scalar
| multipleoftheidentityifandonlyif\mathcal{S}\mathcal{T} |     |     | =\mathcal{T}\mathcal{S}forevery\mathcal{S}\inℒ(\mathcal{V}). |     |     |
| ---------------------------------- | --- | --- | ------------------ | --- | --- |
Suppose \mathcal{U} is a subspace of \mathcal{V} with \mathcal{U} \neq \mathcal{V}. Suppose \mathcal{S} \in ℒ(\mathcal{U},\mathcal{W}) and
Define\mathcal{T}∶
| \mathcal{S}\neq0(whichmeansthat\mathcal{S}u\neq0forsomeu\in\mathcal{U}). |     |     |     | \mathcal{V} \rightarrow\mathcal{W} | by  |
| ---------------------------------- | --- | --- | --- | ---- | --- |
⎧ {\mathcal{S}v ifv\in\mathcal{U},
\mathcal{T}v=
|     |     | ⎨ {0 ifv\in\mathcal{V} | and v\notin\mathcal{U}. |     |     |
| --- | --- | ---------- | -------- | --- | --- |
⎩
| Provethat\mathcal{T} | isnotalinearmapon\mathcal{V}. |     |     |     |     |
| ---------- | ------------------- | --- | --- | --- | --- |
13 Suppose\mathcal{V} isfinite-dimensional. Provethateverylinearmaponasubspace
| of\mathcal{V} canbeextendedtoalinearmapon\mathcal{V}. |                              |     | Inotherwords,showthatif\mathcal{U} |             |     |
| --------------------------------- | ---------------------------- | --- | ------------------------ | ----------- | --- |
| isasubspaceof\mathcal{V}                    | and\mathcal{S}\inℒ(\mathcal{U},\mathcal{W}),thenthereexists\mathcal{T} |     |                          | \inℒ(\mathcal{V},\mathcal{W})such |     |
that\mathcal{T}u=\mathcal{S}uforallu\in\mathcal{U}.
Theresultinthisexerciseisusedintheproofof3.125.
Suppose\mathcal{V} isfinite-dimensionalwithdim\mathcal{V} >0,andsuppose\mathcal{W} isinfinite-
| dimensional. | Provethatℒ(\mathcal{V},\mathcal{W})isinfinite-dimensional. |     |     |     |     |
| ------------ | -------------------------------------- | --- | --- | --- | --- |
15 Suppose v ,…,v is a linearly dependent list of vectors in \mathcal{V}. Suppose
1 m
,…,w
| also that | \mathcal{W} \neq {0}. Prove | that there exist | w   | \in \mathcal{W} such | that no |
| --------- | -------------- | ---------------- | --- | -------- | ------- |
1 m
| \mathcal{T} \inℒ(\mathcal{V},\mathcal{W})satisfies\mathcal{T}v |     | =w foreachk | =1,…,m. |     |     |
| -------------------- | --- | ----------- | ------- | --- | --- |
k k
16 Suppose \mathcal{V} is finite-dimensional with dim\mathcal{V} > 1. Prove that there exist
| \mathcal{S},\mathcal{T} \inℒ(\mathcal{V})suchthat\mathcal{S}\mathcal{T} |     | \neq\mathcal{T}\mathcal{S}. |     |     |     |
| ------------------- | --- | ---- | --- | --- | --- |
17 Suppose \mathcal{V} is finite-dimensional. Show that the only two-sided ideals of
ℒ(\mathcal{V})are{0}andℒ(\mathcal{V}).
| Asubspaceℰof          | ℒ(\mathcal{V})iscalledatwo-sidedidealof |        | ℒ(\mathcal{V})if | \mathcal{T}\mathcal{E}\inℰand |     |
| --------------------- | ----------------------------- | ------ | ------ | ------- | --- |
| \mathcal{E}\mathcal{T} \inℰforall\mathcal{E}\inℰandall\mathcal{T} |                               | \inℒ(\mathcal{V}). |        |         |     |

| --- | --- | --- | --- | --------- | ------------------- | --- | --- |
| 3B Null    | Spaces | and         | Ranges |     |     |     |     |
| ---------- | ------ | ----------- | ------ | --- | --- | --- | --- |
| Null Space | and    | Injectivity |        |     |     |     |     |
Inthissectionwewilllearnabouttwosubspacesthatareintimatelyconnected
witheachlinearmap. Webeginwiththesetofvectorsthatgetmappedto0.
| 3.11 | definition: | nullspace,null\mathcal{T} |     |     |     |     |     |
| ---- | ----------- | --------------- | --- | --- | --- | --- | --- |
For\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}),thenullspaceof\mathcal{T},denotedbynull\mathcal{T},isthesubsetof\mathcal{V}
| consistingofthosevectorsthat\mathcal{T} |     |           |       | mapsto0:                            |         |     |     |
| ----------------------------- | --- | --------- | ----- | ----------------------------------- | ------- | --- | --- |
|                               |     |           | null\mathcal{T} | ={v\in\mathcal{V}                               | ∶\mathcal{T}v=0}. |     |     |
| 3.12 example:                 |     | nullspace |       |                                     |         |     |     |
| • If\mathcal{T} isthezeromapfrom\mathcal{V}       |     |           |       | to\mathcal{W},meaningthat\mathcal{T}v=0foreveryv\in\mathcal{V},then |         |     |     |
null\mathcal{T} =\mathcal{V}.
• Suppose \phi \in ℒ(\mathbf{C}3,\mathbf{C}) is defined by \phi(z ,z ,z ) = z +2z +3z . Then
|                |     |     |      |     | 1 2 3                      | 1 2 | 3   |
| -------------- | --- | --- | ---- | --- | -------------------------- | --- | --- |
|                |     |     | )\in\mathbf{C}3 | ∶z  |                            |     |     |
| null\phiequals{(z |     | ,z  | ,z   | +2z | +3z =0},whichisasubspaceof |     |     |
|                |     | 1 2 | 3    | 1   | 2 3                        |     |     |
thedomainof\phi. Wewillsoonseethatthenullspaceofeachlinearmapisa
subspaceofitsdomain.
| • Suppose                  | \mathcal{D}   | \in ℒ(𝒫(\mathbf{R})) | is  | the dif- |                         |     |         |
| -------------------------- | --- | --------- | --- | -------- | ----------------------- | --- | ------- |
|                            |     |           |     |          | Theword“null”meanszero. |     | Thusthe |
| ferentiationmapdefinedby\mathcal{D}p |     |           |     | = p′.    |                         |     |         |
term“nullspace”shouldremindyou
Theonlyfunctionswhosederivative
|     |     |     |     |     | of the connection | to 0. Some | mathe- |
| --- | --- | --- | --- | --- | ----------------- | ---------- | ------ |
equalsthezerofunctionarethecon- maticiansusethetermkernelinstead
| stantfunctions. |     | Thusthenullspaceof |     |     |     |     |     |
| --------------- | --- | ------------------ | --- | --- | --- | --- | --- |
ofnullspace.
\mathcal{D}equalsthesetofconstantfunctions.
• Suppose that \mathcal{T} \in ℒ(𝒫(\mathbf{R})) is the multiplication by x2 map defined by
| (\mathcal{T}p)(x)=x2p(x).   |                                   | Theonlypolynomialpsuchthatx2p(x)=0forallx |        |           |         |     | \in\mathbf{R}  |
| ----------------- | --------------------------------- | ----------------------------------------- | ------ | --------- | ------- | --- | --- |
| isthe0polynomial. |                                   | Thusnull\mathcal{T}                                 |        | ={0}.     |         |     |     |
| • Suppose\mathcal{T}        | \inℒ(\mathbf{F}\infty)isthebackwardshiftdefinedby |                                           |        |           |         |     |     |
|                   |                                   |                                           | \mathcal{T}(x ,x | ,x ,…)=(x | ,x ,…). |     |     |
|                   |                                   |                                           | 1      | 2 3       | 2 3     |     |     |
Then\mathcal{T}(x ,x ,x ,…)equals0ifandonlyifthenumbersx ,x ,… areall0.
|     | 1   | 2 3 |     |     |     | 2 3 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
={(a,0,0,…)∶a\in\mathbf{F}}.
Thusnull\mathcal{T}
Thenextresultshowsthatthenullspaceofeachlinearmapisasubspaceof
| thedomain. | Inparticular,0isinthenullspaceofeverylinearmap. |     |     |     |     |     |     |
| ---------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
thenullspaceisasubspace
3.13
| Suppose\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}). |     | Thennull\mathcal{T} | isasubspaceof\mathcal{V}. |     |     |     |
| -------- | -------- | --- | --------- | --------------- | --- | --- | --- |

| -------- | --- | ---------- | --- | --- | --- | --- |
| Proof Because\mathcal{T}    |     | isalinearmap,\mathcal{T}(0)=0(by3.10). |      |     | Thus0\innull\mathcal{T}. |     |
| ----------------- | --- | ---------------------------- | ---- | --- | ------------ | --- |
| Supposeu,v\innull\mathcal{T}. |     |                              | Then |     |              |     |
\mathcal{T}(u+v)=\mathcal{T}u+\mathcal{T}v=0+0=0.
| Henceu+v\innull\mathcal{T}. |     | Thusnull\mathcal{T} | isclosedunderaddition.             |       |     |     |
| --------------- | --- | --------- | ---------------------------------- | ----- | --- | --- |
| Supposeu\innull\mathcal{T}  |     | and       | \lambda\in\mathbf{F}. Then                          |       |     |     |
|                 |     |           | \mathcal{T}(\lambdau)= \lambda\mathcal{T}u=                        | \lambda0=0. |     |     |
| Hence \lambdau\innull\mathcal{T}. |     | Thusnull\mathcal{T} | isclosedunderscalarmultiplication. |       |     |     |
Wehaveshownthatnull\mathcal{T} contains0andisclosedunderadditionandscalar
| multiplication. | Thusnull\mathcal{T} |     | isasubspaceof\mathcal{V} | (by1.34). |     |     |
| --------------- | --------- | --- | -------------- | --------- | --- | --- |
Aswewillsoonsee,foralinearmapthenextdefinitioniscloselyconnected
tothenullspace.
| 3.14 definition: | injective |     |     |     |     |     |
| ---------------- | --------- | --- | --- | --- | --- | --- |
Afunction\mathcal{T}∶
\mathcal{V} \rightarrow\mathcal{W} iscalledinjectiveif\mathcal{T}u=\mathcal{T}vimpliesu=v.
| We could | rephrase |     | the definition |     |     |     |
| -------- | -------- | --- | -------------- | --- | --- | --- |
Thetermone-to-onemeansthesame
| abovetosaythat\mathcal{T} |     | isinjectiveifu | \neq v |     |     |     |
| --------------- | --- | -------------- | --- | --- | --- | --- |
asinjective.
| impliesthat\mathcal{T}u\neq\mathcal{T}v. |     | Thus\mathcal{T}isinjective |     |     |     |     |
| ----------------- | --- | ---------------- | --- | --- | --- | --- |
ifandonlyifitmapsdistinctinputstodistinctoutputs.
The next result says that we can check whether a linear map is injective
by checking whether 0 is the only vector that gets mapped to 0. As a simple
applicationofthisresult,weseethatofthelinearmapswhosenullspaceswe
computedin3.12,onlymultiplicationbyx2 isinjective(exceptthatthezeromap
| isinjectiveinthespecialcase\mathcal{V} |     |                      | ={0}). |     |     |     |
| ---------------------------- | --- | -------------------- | ------ | --- | --- | --- |
| injectivity                  |     | ⟺ nullspaceequals{0} |        |     |     |     |
3.15
| Let\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). |     | Then\mathcal{T} | isinjectiveifandonlyifnull\mathcal{T} |     | ={0}. |     |
| ------------- | --- | ----- | --------------------------- | --- | ----- | --- |
First suppose is injective. We want to prove that null\mathcal{T} {0}. We
| Proof |     | \mathcal{T}   |     |     |     | =   |
| ----- | --- | --- | --- | --- | --- | --- |
already know that {0} \subseteq null\mathcal{T} (by 3.10). To prove the inclusion in the other
| direction,supposev\innull\mathcal{T}. |     |     | Then |     |     |     |
| ------------------------- | --- | --- | ---- | --- | --- | --- |
\mathcal{T}(v)=0=\mathcal{T}(0).
Because \mathcal{T} is injective, the equation above implies that v = 0. Thus we can
| concludethatnull\mathcal{T} |     | ={0},asdesired. |     |     |     |     |
| ----------------- | --- | --------------- | --- | --- | --- | --- |
Toprovetheimplicationintheotherdirection,nowsupposenull\mathcal{T} ={0}. We
wanttoprovethat\mathcal{T}isinjective. Todothis,supposeu,v\in\mathcal{V}and\mathcal{T}u=\mathcal{T}v. Then
$$0=\mathcal{T}u-\mathcal{T}v=\mathcal{T}(u-v).$$
Thusu-visinnull\mathcal{T},whichequals{0}. Henceu-v = 0,whichimpliesthat
| u=v. Hence\mathcal{T} | isinjective,asdesired. |     |     |     |     |     |
| ----------- | ---------------------- | --- | --- | --- | --- | --- |

| --- | --- | --- | --- | --------- | --- | ------------------- | --- | --- |
| Range | and | Surjectivity |     |     |     |     |     |     |
| ----- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Nowwegiveanametothesetofoutputsofalinearmap.
range
**3.16 定义：** For\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}),therangeof\mathcal{T}isthesubsetof\mathcal{W}consistingofthosevectors
thatareequalto\mathcal{T}vforsomev\in\mathcal{V}:
|            |                   |                                         |        | range\mathcal{T}                              | ={\mathcal{T}v∶v\in\mathcal{V}}. |      |      |     |
| ---------- | ----------------- | --------------------------------------- | ------ | ----------------------------------- | ---------- | ---- | ---- | --- |
| 3.17       | example:          | range                                   |        |                                     |            |      |      |     |
| • If\mathcal{T}      | isthezeromapfrom\mathcal{V} |                                         |        | to\mathcal{W},meaningthat\mathcal{T}v=0foreveryv\in\mathcal{V},then |            |      |      |     |
| range\mathcal{T}     |                   | ={0}.                                   |        |                                     |            |      |      |     |
| • Suppose\mathcal{T} |                   | \inℒ(\mathbf{R}2,\mathbf{R}3)isdefinedby\mathcal{T}(x,y)=(2x,5y,x+y). |        |                                     |            |      | Then |     |
|            |                   |                                         | range\mathcal{T} | ={(2x,5y,x+y)∶x,y                   |            | \in\mathbf{R}}. |      |     |
Notethatrange\mathcal{T} isasubspaceof\mathbf{R}3. Wewillsoonseethattherangeofeach
elementofℒ(\mathcal{V},\mathcal{W})isasubspaceof\mathcal{W}.
Suppose\mathcal{D}\inℒ(𝒫(\mathbf{R}))isthedifferentiationmapdefinedby\mathcal{D}p=p′.
| •   |     |     |     |     |     |     |     | Because |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- |
foreverypolynomialq\in𝒫(\mathbf{R})thereexistsapolynomialp\in𝒫(\mathbf{R})suchthat
p′ =q,therangeof\mathcal{D}is𝒫(\mathbf{R}).
Thenextresultshowsthattherangeofeachlinearmapisasubspaceofthe
vectorspaceintowhichitisbeingmapped.
therangeisasubspace
3.18
| If\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}),thenrange\mathcal{T} |     |     | isasubspaceof\mathcal{W}. |     |     |     |     |
| --- | ------------------ | --- | --- | --------------- | --- | --- | --- | --- |
Proof Suppose \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Then \mathcal{T}(0) = 0 (by 3.10), which implies that
0\inrange\mathcal{T}.
If w ,w \in range\mathcal{T}, then there exist v ,v \in \mathcal{V} such that \mathcal{T}v = w and
|     | 1   | 2      |     |     | 1   | 2   | 1   | 1   |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- |
| \mathcal{T}v  | =w  | . Thus |     |     |     |     |     |     |
2 2
|        |            |             | \mathcal{T}(v                        | +v )=\mathcal{T}v    | +\mathcal{T}v                    | =w +w .       |     |      |
| ------ | ---------- | ----------- | -------------------------- | ---------- | ---------------------- | ------------- | --- | ---- |
|        |            |             |                            | 1 2        | 1                      | 2 1 2         |     |      |
| Hencew |            | +w \inrange\mathcal{T}. |                            | Thusrange\mathcal{T} | isclosedunderaddition. |               |     |      |
|        | Ifw\inrange\mathcal{T} |             | and \lambda\in\mathbf{F},thenthereexistsv\in\mathcal{V} |            |                        | suchthat\mathcal{T}v=w. |     | Thus |
|        |            |             |                            | \mathcal{T}(\lambdav)=     | \lambda\mathcal{T}v=                   | \lambdaw.           |     |      |
Hence \lambdaw\inrange\mathcal{T}. Thusrange\mathcal{T} isclosedunderscalarmultiplication.
Wehaveshownthatrange\mathcal{T}contains0andisclosedunderadditionandscalar
| multiplication. |     | Thusrange\mathcal{T} |     | isasubspaceof\mathcal{W} |     | (by1.34). |     |     |
| --------------- | --- | ---------- | --- | -------------- | --- | --------- | --- | --- |

| -------- | --- | ---------- | --- | --- | --- | --- | --- |
surjective
**3.19 定义：** Afunction\mathcal{T}∶
\mathcal{V} \rightarrow\mathcal{W} iscalledsurjectiveifitsrangeequals\mathcal{W}.
Toillustratethedefinitionabove,notethatoftherangeswecomputedin3.17,
onlythedifferentiationmapissurjective(exceptthatthezeromapissurjectivein
| thespecialcase\mathcal{W} | ={0}). |     |     |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- | --- | --- |
WhetheralinearmapissurjectivedeSomepeopleusethetermonto,which
| pendsonwhatwearethinkingofasthe |     |     |     |     | meansthesameassurjective. |     |     |
| ------------------------------- | --- | --- | --- | --- | ------------------------- | --- | --- |
vectorspaceintowhichitmaps.
surjectivitydependsonthetargetspace
**3.20 例：** Thedifferentiationmap\mathcal{D}\inℒ(𝒫 (\mathbf{R}))definedby\mathcal{D}p=p′ isnotsurjective,
becausethepolynomialx5
|     |     |     | isnotintherangeof\mathcal{D}. |     |     | However,thedifferentiation |     |
| --- | --- | --- | ------------------- | --- | --- | -------------------------- | --- |
map\mathcal{S} \in ℒ(𝒫 (\mathbf{R}),𝒫 (\mathbf{R}))definedby\mathcal{S}p = p′ issurjective,becauseitsrange
5 4
equals𝒫
$$(\mathbf{R}),whichisthevectorspaceintowhich\mathcal{S}maps.$$
| Fundamental | Theorem |     | of Linear |     | Maps |     |     |
| ----------- | ------- | --- | --------- | --- | ---- | --- | --- |
Thenextresultissoimportantthatitgetsadramaticname.
3.21 fundamentaltheoremoflinearmaps
ℒ(\mathcal{V},\mathcal{W}).
| Suppose\mathcal{V} | isfinite-dimensionaland\mathcal{T} |     |     |     | \in   | Thenrange\mathcal{T} | isfinite- |
| -------- | ------------------------ | --- | --- | --- | --- | ---------- | --------- |
dimensionaland
|     |     | dim\mathcal{V} | =dimnull\mathcal{T}+dimrange\mathcal{T}. |     |     |     |     |
| --- | --- | ---- | -------------------- | --- | --- | --- | --- |
Proof Let u ,…,u be a basis of null\mathcal{T}; thus dimnull\mathcal{T} =m. The linearly
1 m
| independentlistu | ,…,u |     | canbeextendedtoabasis |     |     |     |     |
| ---------------- | ---- | --- | --------------------- | --- | --- | --- | --- |
1 m
|     |     |     | ,…,u |     | ,v ,…,v |     |     |
| --- | --- | --- | ---- | --- | ------- | --- | --- |
u
|     |     |     | 1   | m   | 1   | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
of\mathcal{V}(by2.32). Thusdim\mathcal{V} =m+n. Tocompletetheproof,weneedtoshowthat
range\mathcal{T} isfinite-dimensionalanddimrange\mathcal{T} = n. Wewilldothisbyproving
,…,\mathcal{T}v
| that\mathcal{T}v 1 | n isabasisofrange\mathcal{T}. |      |      |         |                   |          |     |
| -------- | ------------------- | ---- | ---- | ------- | ----------------- | -------- | --- |
| Letv\in\mathcal{V}.  | Becauseu            | ,…,u |      | ,v ,…,v | spans\mathcal{V},wecanwrite |          |     |
|          |                     | 1    | m    | 1       | n                 |          |     |
|          | v=a                 | u    | +⋯+a | u       | +b v              | +⋯+b v , |     |
|          |                     | 1    | 1    | m m     | 1 1               | n n      |     |
wherethea’sandb’sarein\mathbf{F}. Applying\mathcal{T} tobothsidesofthisequation,weget
|     |     |     | \mathcal{T}v=b | \mathcal{T}v +⋯+b |     | \mathcal{T}v , |     |
| --- | --- | --- | ---- | ------- | --- | ---- | --- |
|     |     |     |      | 1 1     | n   | n    |     |
wherethetermsoftheform\mathcal{T}u disappearedbecauseeachu isinnull\mathcal{T}. Thelast
|     |     |     | k   |     |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
equationimpliesthatthelist\mathcal{T}v ,…,\mathcal{T}v spansrange\mathcal{T}. Inparticular,range\mathcal{T} is
|     |     |     | 1   |     | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
finite-dimensional.

| --- | --- | --- | --- | --------- | --- | ------------------- | --- | --- |
|     | Toshow\mathcal{T}v | ,…,\mathcal{T}v | islinearlyindependent,supposec |      |     |     | ,…,c | \in\mathbf{F} and |
| --- | -------- | ----- | ------------------------------ | ---- | --- | --- | ---- | ------ |
|     |          | 1     | n                              |      |     |     | 1    | n      |
|     |          |       | c \mathcal{T}v                           | +⋯+c | \mathcal{T}v  | =0. |      |        |
|     |          |       | 1                              | 1    | n n |     |      |        |
Then
+⋯+c
|     |     |     | \mathcal{T}(c | v   | v )=0. |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     |     |     | 1 1 | n n    |     |     |     |
Hence
|          |      |                       | c v      | +⋯+c | v \innull\mathcal{T}. |     |     |     |
| -------- | ---- | --------------------- | -------- | ---- | --------- | --- | --- | --- |
|          |      |                       | 1        | 1 n  | n         |     |     |     |
| Becauseu | ,…,u | spansnull\mathcal{T},wecanwrite |          |      |           |     |     |     |
|          | 1    | m                     |          |      |           |     |     |     |
|          |      |                       | c v +⋯+c | v =d | u +⋯+d    |     | u , |     |
|          |      |                       | 1 1      | n n  | 1 1       | m   | m   |     |
wherethed’sarein\mathbf{F}. Thisequationimpliesthatallthec’s(andd’s)are0(be-
|        | ,…,u | ,v ,…,v |                         |     |     |        | ,…,\mathcal{T}v |            |
| ------ | ---- | ------- | ----------------------- | --- | --- | ------ | ----- | ---------- |
| causeu |      |         | islinearlyindependent). |     |     | Thus\mathcal{T}v |       | islinearly |
|        | 1    | m 1     | n                       |     |     |        | 1     | n          |
independentandhenceisabasisofrange\mathcal{T},asdesired.
Nowwecanshowthatnolinearmapfromafinite-dimensionalvectorspace
to a “smaller” vector space can be injective, where “smaller” is measured by
dimension.
3.22 linearmaptoalower-dimensionalspaceisnotinjective
Suppose \mathcal{V} and \mathcal{W} are finite-dimensional vector spaces such that
| dim\mathcal{V} | >dim\mathcal{W}.Thennolinearmapfrom\mathcal{V} |     |     |     |     | to\mathcal{W} isinjective. |     |     |
| ---- | -------------------------- | --- | --- | --- | --- | ---------------- | --- | --- |
\inℒ(\mathcal{V},\mathcal{W}).
| Proof | Let\mathcal{T} |     | Then     |                 |     |     |     |     |
| ----- | ---- | --- | -------- | --------------- | --- | --- | --- | --- |
|       |      |     | dimnull\mathcal{T} | =dim\mathcal{V}-dimrange\mathcal{T} |     |     |     |     |
\geqdim\mathcal{V}-dim\mathcal{W}
>0,
wherethefirstlineabovecomesfromthefundamentaltheoremoflinearmaps
$$(3.21)andthesecondlinefollowsfrom2.37. Theinequalityabovestatesthat$$
dimnull\mathcal{T} >0. Thismeansthatnull\mathcal{T} containsvectorsotherthan0. Thus\mathcal{T} is
notinjective(by3.15).
| 3.23 | example: | linearmapfrom\mathbf{F}4 |     | to\mathbf{F}3 | isnotinjective |     |     |     |
| ---- | -------- | --------------- | --- | ---- | -------------- | --- | --- | --- |
Definealinearmap\mathcal{T}∶
|     |        |              | \mathbf{F}4  | \rightarrow\mathbf{F}3 by |      |         |        |        |
| --- | ------ | ------------ | --- | ------ | ---- | ------- | ------ | ------ |
|     | \mathcal{T}(z ,z | ,z ,z )=(\sqrt7z | +\piz | +z     | ,97z | +3z +2z | ,z +6z | +7z ). |
|     | 1 2    | 3 4          | 1   | 2 4    | 1    | 2       | 3 2    | 3 4    |
Becausedim\mathbf{F}4 >dim\mathbf{F}3,wecanuse3.22toassertthat\mathcal{T}isnotinjective,without
doinganycalculations.

| -------- | ---------- | --- | --- | --- |
The next result shows that no linear map from a finite-dimensional vector
spacetoa“bigger”vectorspacecanbesurjective,where“bigger”ismeasuredby
dimension.
linearmaptoahigher-dimensionalspaceisnotsurjective
3.24
Suppose \mathcal{V} and \mathcal{W} are finite-dimensional vector spaces such that
| dim\mathcal{V} <dim\mathcal{W}.Thennolinearmapfrom\mathcal{V} |          |           | to\mathcal{W}            | issurjective. |
| ------------------------------- | -------- | --------- | -------------- | ------------- |
| Proof Let\mathcal{T}                      | \inℒ(\mathcal{V},\mathcal{W}). | Then      |                |               |
|                                 |          | dimrange\mathcal{T} | =dim\mathcal{V}-dimnull\mathcal{T} |               |
\leqdim\mathcal{V}
<dim\mathcal{W},
wheretheequalityabovecomesfromthefundamentaltheoremoflinearmaps
$$(3.21). Theinequalityabovestatesthatdimrange\mathcal{T} <dim\mathcal{W}.Thismeansthat$$
| range\mathcal{T} cannotequal\mathcal{W}. |     | Thus\mathcal{T} isnotsurjective. |     |     |
| -------------------- | --- | ---------------------- | --- | --- |
Aswewillsoonsee,3.22and3.24haveimportantconsequencesinthetheory
of linear equations. The idea is to express questions about systems of linear
equationsintermsoflinearmaps. Let’sbeginbyrephrasingintermsoflinear
mapsthequestionofwhetherahomogeneoussystemoflinearequationshasa
nonzerosolution.
Fixpositiveintegersmandn,andlet
Homogeneous,inthiscontext,means
| \mathcal{A} \in\mathbf{F}forj                           | =1,…,mandk | =1,…,n. |                                   |     |
| ---------------------------------- | ---------- | ------- | --------------------------------- | --- |
| j,k                                |            |         | thattheconstanttermontherightside |     |
| Considerthehomogeneoussystemoflin- |            |         | ofeachequationbelowis0.           |     |
earequations
n
|     |     | \sum\mathcal{A}  | x =0 |     |
| --- | --- | --- | ---- | --- |
1,k k
$$k=1$$
⋮
n
|     |     | \sum\mathcal{A}  | m,k x =0. |     |
| --- | --- | --- | --------- | --- |
k
$$k=1$$
Clearly x = ⋯ = x = 0 is a solution of the system of equations above; the
|     | 1 n |     |     |     |
| --- | --- | --- | --- | --- |
questionhereiswhetheranyothersolutionsexist.
| Define\mathcal{T}∶ | \mathbf{F}n \rightarrow\mathbf{F}m | by    |       |          |
| -------- | ------ | ----- | ----- | -------- |
|          |        |       | n     | n        |
|          | ,…,x   |       | ,…,\sum\mathcal{A} |          |
| 3.25     | \mathcal{T}(x    | )=(\sum\mathcal{A} | 1,k x | m,k x ). |
|          | 1      | n     | k     | k        |
|          |        | k=1   | k=1   |          |
Theequation\mathcal{T}(x ,…,x )=0(the0hereistheadditiveidentityin\mathbf{F}m,namely,
|     | 1   | n   |     |     |
| --- | --- | --- | --- | --- |
thelistoflengthmofall0’s)isthesameasthehomogeneoussystemoflinear
equationsabove.
Thuswewanttoknowifnull\mathcal{T} isstrictlybiggerthan{0},whichisequivalent
to\mathcal{T} notbeinginjective(by3.15). Thenextresultgivesanimportantcondition
| forensuringthat\mathcal{T} | isnotinjective. |     |     |     |
| ---------------- | --------------- | --- | --- | --- |

| --- | --- | --------- | ------------------- | --- | --- |
homogeneoussystemoflinearequations
3.26
Ahomogeneoussystemoflinearequationswithmorevariablesthanequations
hasnonzerosolutions.
Proof Usethenotationandresultfromthediscussionabove. Thus\mathcal{T} isalinear
| mapfrom\mathbf{F}n | to\mathbf{F}m,andwehaveahomogeneoussystemofmlinearequations |     |     |     |     |
| --------- | -------------------------------------------------- | --- | --- | --- | --- |
withnvariablesx ,…,x . From3.22weseethat\mathcal{T} isnotinjectiveifn>m.
|     | 1   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- |
Exampleoftheresultabove: ahomogeneoussystemoffourlinearequations
withfivevariableshasnonzerosolutions.
Nowweconsiderthequestionofwhetherasystemoflinearequationshasno
solutionsforsomechoiceoftheconstantterms. Torephrasethisquestioninterms
ofalinearmap,fixpositiveintegersmandn,andlet\mathcal{A} \in\mathbf{F} forallj =1,…,m
j,k
andallk =1,…,n. Forc ,…,c \in\mathbf{F},considerthesystemoflinearequations
1 m
n
|     |     | \sum\mathcal{A}  | x =c |     |     |
| --- | --- | --- | ---- | --- | --- |
|     |     | 1,k | k 1  |     |     |
$$k=1$$
| 3.27 |     |     | ⋮   |     |     |
| ---- | --- | --- | --- | --- | --- |
n
|     |     | \sum\mathcal{A}  | x =c . |     |     |
| --- | --- | --- | ------ | --- | --- |
|     |     | m,k | k m    |     |     |
$$k=1$$
Withthisnotation,thequestionhereiswhetherthereissomechoiceoftheconstant
| termsc ,…,c | \in\mathbf{F} suchthatnosolutionexiststothesystemabove. |               |                                 |              |     |
| ----------- | -------------------------------------------- | ------------- | ------------------------------- | ------------ | --- |
| 1           | m                                            |               |                                 |              |     |
| Define\mathcal{T}∶    | \mathbf{F}n \mathbf{F}m                                        |               |                                 |              |     |
|             | \rightarrow                                            | asin3.25. The | Theresults3.26and3.28,whichcom- |              |     |
| equation    | \mathcal{T}(x ,…,x ) =                                 | (c ,…,c ) is  |                                 |              |     |
|             | 1 n                                          | 1 m           | pare the number                 | of variables | and |
thesameasthesystemofequations3.27. the number of equations, can also
| Thuswewanttoknowifrange\mathcal{T} |     | \neq \mathbf{F}m. |                 |          |          |
| ------------------------ | --- | ----- | --------------- | -------- | -------- |
|                          |     |       | be proved using | Gaussian | elimina- |
Hence we can rephrase our question tion. Theabstractapproachtakenhere
about not having a solution for some seemstoprovidecleanerproofs.
| choiceofc | ,…,c \in\mathbf{F}asfollows: | What |     |     |     |
| --------- | ----------------- | ---- | --- | --- | --- |
1 m
conditionensuresthat\mathcal{T}isnotsurjective? Thenextresultgivesonesuchcondition.
3.28 systemoflinearequationswithmoreequationsthanvariables
Asystemoflinearequationswithmoreequationsthanvariableshasnosolution
forsomechoiceoftheconstantterms.
Proof Usethenotationfromthediscussionabove. Thus\mathcal{T} isalinearmapfrom
\mathbf{F}n to \mathbf{F}m, andwehaveasystemof m equationswith n variables x ,…,x ; see
|     |     |     |     | 1   | n   |
| --- | --- | --- | --- | --- | --- |
3.27. Ifn < m,then3.24impliesthat\mathcal{T} isnotsurjective. Asdiscussedabove,
this shows that if we have more equations than variables in a system of linear
equations,thenthereisnosolutionforsomechoiceoftheconstantterms.
Example of the result above: a system of five linear equations with four
variableshasnosolutionforsomechoiceoftheconstantterms.

| -------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| Exercises                                | 3B                            |     |     |     |     |                |                |     |
| ---------------------------------------- | ----------------------------- | --- | --- | --- | --- | -------------- | -------------- | --- |
| 1 Giveanexampleofalinearmap\mathcal{T}withdimnull\mathcal{T} |                               |     |     |     |     | =3anddimrange\mathcal{T} |                | =2. |
| Suppose\mathcal{S},\mathcal{T}                               | \inℒ(\mathcal{V})aresuchthatrange\mathcal{S}\subseteqnull\mathcal{T}. |     |     |     |     |                | Provethat(\mathcal{S}\mathcal{T})2 | =0. |
|            | ,…,v |                      |     |     |         | \inℒ(\mathbf{F}m,\mathcal{V})by |     |     |
| ---------- | ---- | -------------------- | --- | --- | ------- | ---------- | --- | --- |
| 3 Supposev |      | isalistofvectorsin\mathcal{V}. |     |     | Define\mathcal{T} |            |     |     |
1 m
|                     |     | \mathcal{T}(z ,…,z       | )=z | v   | +⋯+z | v          | .   |     |
| ------------------- | --- | -------------- | --- | --- | ---- | ---------- | --- | --- |
|                     |     | 1              | m   | 1   | 1    | m m        |     |     |
| (a) Whatpropertyof\mathcal{T} |     | correspondstov |     |     | ,…,v | spanning\mathcal{V}? |     |     |
|                     |     |                |     |     | 1    | m          |     |     |
$$(b) What property of \mathcal{T} corresponds to the list v ,…,v being linearly$$
|     |     |     |     |     |     | 1   | m   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
independent?
|     | \inℒ(\mathbf{R}5,\mathbf{R}4)∶dimnull\mathcal{T} |     |     |     | >2}isnotasubspaceofℒ(\mathbf{R}5,\mathbf{R}4). |     |     |     |
| --- | ------------------ | --- | --- | --- | ---------------------------- | --- | --- | --- |
4 Showthat{\mathcal{T}
\inℒ(\mathbf{R}4)suchthatrange\mathcal{T}
| 5 Giveanexampleof\mathcal{T}            |           |                                        |     |                      |     | =null\mathcal{T}. |         |      |
| ----------------------------- | --------- | -------------------------------------- | --- | -------------------- | --- | ------- | ------- | ---- |
| 6 Provethattheredoesnotexist\mathcal{T} |           |                                        |     | \inℒ(\mathbf{R}5)suchthatrange\mathcal{T} |     |         | =null\mathcal{T}. |      |
| 7 Suppose\mathcal{V}                    | and\mathcal{W}      | arefinite-dimensionalwith2\leqdim\mathcal{V}        |     |                      |     |         | \leqdim\mathcal{W}.  | Show |
|                               | \inℒ(\mathcal{V},\mathcal{W})∶\mathcal{T} | isnotinjective}isnotasubspaceofℒ(\mathcal{V},\mathcal{W}). |     |                      |     |         |         |      |
that{\mathcal{T}
| 8 Suppose\mathcal{V} | and\mathcal{W}      | arefinite-dimensionalwithdim\mathcal{V}           |     |     |     |     | \geqdim\mathcal{W} \geq2. | Show |
| ---------- | --------- | --------------------------------------- | --- | --- | --- | --- | --------- | ---- |
| that{\mathcal{T}     | \inℒ(\mathcal{V},\mathcal{W})∶\mathcal{T} | isnotsurjective}isnotasubspaceofℒ(\mathcal{V},\mathcal{W}). |     |     |     |     |           |      |
9 Suppose \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}) is injective and v ,…,v is linearly independent
|      |             |       |                           |     | 1   | n   |     |     |
| ---- | ----------- | ----- | ------------------------- | --- | --- | --- | --- | --- |
| in\mathcal{V}. | Provethat\mathcal{T}v | ,…,\mathcal{T}v | islinearlyindependentin\mathcal{W}. |     |     |     |     |     |
1 n
| 10 Supposev | ,…,v | spans\mathcal{V}and\mathcal{T} |     | \inℒ(\mathcal{V},\mathcal{W}). | Showthat\mathcal{T}v |     | ,…,\mathcal{T}v | spans |
| ----------- | ---- | ---------- | --- | -------- | ---------- | --- | ----- | ----- |
|             | 1    | n          |     |          |            |     | 1     | n     |
range\mathcal{T}.
ℒ(\mathcal{V},\mathcal{W}).
11 Suppose that \mathcal{V} is finite-dimensional and that \mathcal{T} \in Prove that
| thereexistsasubspace\mathcal{U} |                    | of\mathcal{V}   | suchthat |        |            |      |        |     |
| --------------------- | ------------------ | ----- | -------- | ------ | ---------- | ---- | ------ | --- |
|                       | \mathcal{U}\capnull\mathcal{T}            | ={0}  | and      | range\mathcal{T} | ={\mathcal{T}u∶u\in\mathcal{U}}. |      |        |     |
|                       | isalinearmapfrom\mathbf{F}4 |       |          | to\mathbf{F}2   |            |      |        |     |
| 12 Suppose\mathcal{T}           |                    |       |          |        | suchthat   |      |        |     |
|                       |                    | ,x ,x | ,x )\in\mathbf{F}4  |        | ∶x         |      |        |     |
|                       | null\mathcal{T}              | ={(x  |          |        | =5x        | andx | =7x }. |     |
|                       |                    | 1 2   | 3 4      |        | 1          | 2    | 3 4    |     |
| Provethat\mathcal{T}            | issurjective.      |       |          |        |            |      |        |     |
13 Suppose\mathcal{U} isathree-dimensionalsubspaceof\mathbf{R}8 andthat\mathcal{T} isalinearmap
| from\mathbf{R}8                                     | to\mathbf{R}5 | suchthatnull\mathcal{T} | =\mathcal{U}. | Provethat\mathcal{T} |      | issurjective. |                |     |
| ------------------------------------------ | ---- | ------------- | --- | ---------- | ---- | ------------- | -------------- | --- |
| Provethattheredoesnotexistalinearmapfrom\mathbf{F}5 |      |               |     |            |      | to\mathbf{F}2          |                |     |
| 14                                         |      |               |     |            |      |               | whosenullspace |     |
| equals{(x                                  | ,x   | ,x ,x ,x )\in\mathbf{F}5 | ∶x  | =3x        | andx | =x            | =x }.          |     |
|                                            | 1 2  | 3 4 5         |     | 1          | 2    | 3             | 4 5            |     |
15 Supposethereexistsalinearmapon\mathcal{V} whosenullspaceandrangeareboth
| finite-dimensional. |     | Provethat\mathcal{V} |     | isfinite-dimensional. |     |     |     |     |
| ------------------- | --- | ---------- | --- | --------------------- | --- | --- | --- | --- |

| --- | --- | --- | --------- | --- | ------------------- | --- | --- |
16 Suppose\mathcal{V} and\mathcal{W} arebothfinite-dimensional. Provethatthereexistsan
| injectivelinearmapfrom\mathcal{V} |     |     | to\mathcal{W} | ifandonlyifdim\mathcal{V} |     | \leqdim\mathcal{W}. |     |
| ----------------------- | --- | --- | --- | --------------- | --- | ------ | --- |
Suppose \mathcal{V} and \mathcal{W} are both finite-dimensional. Prove that there exists a
| surjectivelinearmapfrom\mathcal{V} |     |     | onto\mathcal{W} | ifandonlyifdim\mathcal{V} |     | \geqdim\mathcal{W}. |     |
| ------------------------ | --- | --- | ----- | --------------- | --- | ------ | --- |
18 Suppose \mathcal{V} and \mathcal{W} are finite-dimensional and that \mathcal{U} is a subspace of \mathcal{V}.
ℒ(\mathcal{V},\mathcal{W})
Prove that there exists \mathcal{T} \in such that null\mathcal{T} = \mathcal{U} if and only if
| dim\mathcal{U} | \geqdim\mathcal{V}-dim\mathcal{W}. |     |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- | --- |
19 Suppose\mathcal{W}isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Provethat\mathcal{T}isinjective
ifandonlyifthereexists\mathcal{S}\inℒ(\mathcal{W},\mathcal{V})suchthat\mathcal{S}\mathcal{T} istheidentityoperator
on\mathcal{V}.
| Suppose | is  | finite-dimensional |     | and | ℒ(\mathcal{V},\mathcal{W}). | Prove | that is sur- |
| ------- | --- | ------------------ | --- | --- | ------- | ----- | ------------ |
| 20      | \mathcal{W}   |                    |     | \mathcal{T}   | \in       |       | \mathcal{T}            |
jectiveifandonlyifthereexists\mathcal{S}\inℒ(\mathcal{W},\mathcal{V})suchthat\mathcal{T}\mathcal{S}istheidentity
operatoron\mathcal{W}.
21 Suppose\mathcal{V} isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}),and\mathcal{U} isasubspaceof\mathcal{W}.
| Provethat{v\in\mathcal{V} |         | ∶\mathcal{T}v\in\mathcal{U}}isasubspaceof\mathcal{V}           |     |     | and |     |     |
| ------------- | ------- | ------------------------------ | --- | --- | --- | --- | --- |
|               | dim{v\in\mathcal{V} | ∶\mathcal{T}v\in\mathcal{U}}=dimnull\mathcal{T}+dim(\mathcal{U}\caprange\mathcal{T}). |     |     |     |     |     |
22 Suppose \mathcal{U} and \mathcal{V} are finite-dimensional vector spaces and \mathcal{S}\inℒ(\mathcal{V},\mathcal{W})
| and\mathcal{T} | \inℒ(\mathcal{U},\mathcal{V}). | Provethat |     |     |     |     |     |
| ---- | -------- | --------- | --- | --- | --- | --- | --- |
\leqdimnull\mathcal{S}+dimnull\mathcal{T}.
dimnull\mathcal{S}\mathcal{T}
23 Suppose \mathcal{U} and \mathcal{V} are finite-dimensional vector spaces and \mathcal{S}\inℒ(\mathcal{V},\mathcal{W})
| and\mathcal{T}               | \inℒ(\mathcal{U},\mathcal{V}).   | Provethat |                            |                    |     |     |           |
| ------------------ | ---------- | --------- | -------------------------- | ------------------ | --- | --- | --------- |
|                    | dimrange\mathcal{S}\mathcal{T} |           | \leqmin{dimrange\mathcal{S},dimrange\mathcal{T}}. |                    |     |     |           |
| 24 (a) Supposedim\mathcal{V} |            | =5and\mathcal{S},\mathcal{T}  |                            | \inℒ(\mathcal{V})aresuchthat\mathcal{S}\mathcal{T} |     | =0. | Provethat |
dimrange\mathcal{T}\mathcal{S}\leq2.
| (b) Giveanexampleof\mathcal{S},\mathcal{T} |     |     | \inℒ(\mathbf{F}5)with\mathcal{S}\mathcal{T} |     | =0anddimrange\mathcal{T}\mathcal{S}=2. |     |     |
| ---------------------- | --- | --- | ------------ | --- | ------------------ | --- | --- |
Suppose that is finite-dimensional and \mathcal{S},\mathcal{T} ℒ(\mathcal{V},\mathcal{W}). Prove that
| 25          |     | \mathcal{W}                                     |     |     | \in   |     |      |
| ----------- | --- | ------------------------------------- | --- | --- | --- | --- | ---- |
| null\mathcal{S}\subseteqnull\mathcal{T} |     | ifandonlyifthereexists\mathcal{E}\inℒ(\mathcal{W})suchthat\mathcal{T} |     |     |     |     | =\mathcal{E}\mathcal{S}. |
26 Suppose that \mathcal{V} is finite-dimensional and \mathcal{S},\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Prove that
| range\mathcal{S}\subseteqrange\mathcal{T} |            | ifandonlyifthereexists\mathcal{E}\inℒ(\mathcal{V})suchthat\mathcal{S}=\mathcal{T}\mathcal{E}. |     |            |                        |     |     |
| ------------- | ---------- | ----------------------------------------- | --- | ---------- | ---------------------- | --- | --- |
| 27 Suppose\mathcal{P}   | \inℒ(\mathcal{V})and\mathcal{P}2 |                                           | =\mathcal{P}. | Provethat\mathcal{V} | =null\mathcal{P}\oplusrange\mathcal{P}.         |     |     |
| 28 Suppose\mathcal{D}   | \in          | ℒ(𝒫(\mathbf{R}))issuchthatdeg\mathcal{D}p                    |     |            | = (degp)-1foreverynon- |     |     |
constantpolynomialp\in𝒫(\mathbf{R}).
Provethat\mathcal{D}issurjective.
Thenotation\mathcal{D}isusedabovetoremindyouofthedifferentiationmapthat
sendsapolynomialptop′.

| -------- | ---------- | --- | --- |
29 Supposep \in 𝒫(\mathbf{R}). Provethatthereexistsapolynomialq \in 𝒫(\mathbf{R})such
| that5q″+3q′ | =p. |     |     |
| ----------- | --- | --- | --- |
Thisexercisecanbedonewithoutlinearalgebra,butit’smorefuntodoit
usinglinearalgebra.
30 Suppose\phi \in ℒ(\mathcal{V},\mathbf{F})and\phi \neq 0. Supposeu \in \mathcal{V} isnotinnull\phi. Prove
that
=null\phi\oplus{au∶a\in\mathbf{F}}.
\mathcal{V}
31 Suppose \mathcal{V} is finite-dimensional, \mathcal{X} is a subspace of \mathcal{V}, and \mathcal{Y} is a finitedimensionalsubspaceof\mathcal{W}. Provethatthereexists\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})suchthat
| null\mathcal{T} =\mathcal{X} andrange\mathcal{T} | =\mathcal{Y}ifandonlyifdim\mathcal{X}+dim\mathcal{Y} |     | =dim\mathcal{V}. |
| ------------------ | ---------------------- | --- | ------ |
Showthatif\phi∶ℒ(\mathcal{V})\rightarrow\mathbf{F}
| 32 Suppose\mathcal{V}isfinite-dimensionalwithdim\mathcal{V} |     | >1. |     |
| --------------------------------------- | --- | --- | --- |
is a linear map such that \phi(\mathcal{S}\mathcal{T}) = \phi(\mathcal{S})\phi(\mathcal{T}) for all \mathcal{S},\mathcal{T} \in ℒ(\mathcal{V}), then
\phi=0.
Hint:Thedescriptionofthetwo-sidedidealsofℒ(\mathcal{V})givenby Exercise17
in Section3Amightbeuseful.
33 Suppose that \mathcal{V} and \mathcal{W} are real vector spaces and \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Define
∶
| \mathcal{T} \mathcal{V} \rightarrow\mathcal{W} | by  |     |     |
| ------ | --- | --- | --- |
| \mathbf{C} \mathbf{C} \mathbf{C}  |     |     |     |
\mathcal{T} (u+iv)=\mathcal{T}u+i\mathcal{T}v
\mathbf{C}
forallu,v\in\mathcal{V}.
| (a) Showthat\mathcal{T} | isa(complex)linearmapfrom\mathcal{V} |              | to\mathcal{W} . |
| ------------- | -------------------------- | ------------ | ----- |
|               | \mathbf{C}                          | \mathbf{C}            | \mathbf{C}     |
| (b) Showthat\mathcal{T} | isinjectiveifandonlyif\mathcal{T}    | isinjective. |       |
\mathbf{C}
| (c) Showthatrange\mathcal{T} | =\mathcal{W} ifandonlyifrange\mathcal{T} | =\mathcal{W}. |     |
| ------------------ | -------------------- | --- | --- |
\mathbf{C} \mathbf{C}
See Exercise8in Section1Bforthedefinitionofthecomplexification\mathcal{V} .
\mathbf{C}
| Thelinearmap\mathcal{T} | iscalledthecomplexificationofthelinearmap\mathcal{T}. |     |     |
| ------------- | ------------------------------------------- | --- | --- |
\mathbf{C}

| --- | --- | --- | --- | --- | --------- | -------- | --- |
### 3C Matrices
| Representing | a   | Linear | Map | by a Matrix |     |     |     |
| ------------ | --- | ------ | --- | ----------- | --- | --- | --- |
and\mathcal{T}∶
| Weknowthatifv | ,…,v | isabasisof\mathcal{V} |     |     | \mathcal{V} \rightarrow\mathcal{W} | islinear,thenthevalues |     |
| ------------- | ---- | ----------- | --- | --- | ---- | ---------------------- | --- |
1 n
of\mathcal{T}v ,…,\mathcal{T}v determinethevaluesof\mathcal{T}onarbitraryvectorsin\mathcal{V}—seethelinear
| 1   | n   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
maplemma(3.4). Aswewillsoonsee,matricesprovideanefficientmethodof
| recordingthevaluesofthe\mathcal{T}v |     |     | ’sintermsofabasisof\mathcal{W}. |     |     |     |     |
| ------------------------- | --- | --- | --------------------- | --- | --- | --- | --- |
k
| 3.29 definition: | matrix,\mathcal{A} |     |     |     |     |     |     |
| ---------------- | -------- | --- | --- | --- | --- | --- | --- |
j,k
Supposemandnarenonnegativeintegers. Anm-by-nmatrix\mathcal{A}isarectangular
| arrayofelementsof\mathbf{F} |     | withmrowsandncolumns: |     |         |       |      |     |
| ------------------ | --- | --------------------- | --- | ------- | ----- | ---- | --- |
|                    |     |                       |     | \mathcal{A} 1,1 ⋯ | \mathcal{A} 1,n |      |     |
|                    |     |                       | ⎛ ⎜ |         |       | ⎞ ⎟  |     |
|                    |     | \mathcal{A}=⎜                   |     | ⋮       | ⋮     | ⎟ ⎟. |     |
⎜
|              |     |                                   | ⎝ \mathcal{A} | m,1 ⋯ | \mathcal{A} m,n | ⎠   |     |
| ------------ | --- | --------------------------------- | --- | ----- | ----- | --- | --- |
| Thenotation\mathcal{A} |     | denotestheentryinrowj,columnkof\mathcal{A}. |     |       |       |     |     |
j,k
| 3.30 example: | \mathcal{A} j,k | equalsentryinrowj,columnkof |        |     |                                  | \mathcal{A}   |     |
| ------------- | ----- | --------------------------- | ------ | --- | -------------------------------- | --- | --- |
|               |       | 8                           | 4 5-3i |     |                                  |     |     |
| Suppose       | \mathcal{A} =   | (                           |        | ).  |                                  |     |     |
|               |       | 1                           | 9 7    |     | Whendealingwithmatrices,thefirst |     |     |
indexreferstotherownumber;thesec-
| Thus\mathcal{A} 2,3 referstotheentryinthesecond |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
row,thirdcolumnof\mathcal{A},whichmeansthat ondindexreferstothecolumnnumber.
\mathcal{A} 2,3 =7.
Nowwecometothekeydefinitioninthissection.
| 3.31 definition: | matrixofalinearmap,ℳ(\mathcal{T}) |     |      |             |     |           |          |
| ---------------- | ----------------------- | --- | ---- | ----------- | --- | --------- | -------- |
| Suppose\mathcal{T}         | \inℒ(\mathcal{V},\mathcal{W})andv             |     | ,…,v | isabasisof\mathcal{V} |     | andw ,…,w | isabasis |
|                  |                         |     | 1    | n           |     | 1         | m        |
of\mathcal{W}. Thematrixof \mathcal{T}withrespecttothesebasesisthem-by-nmatrixℳ(\mathcal{T})
| whoseentries\mathcal{A} |     | aredefinedby |     |     |     |     |     |
| ------------- | --- | ------------ | --- | --- | --- | --- | --- |
j,k
|                            |      | \mathcal{T}v   | =\mathcal{A}        | w +⋯+\mathcal{A}                            | w   | .   |      |
| -------------------------- | ---- | ---- | --------- | --------------------------------- | --- | --- | ---- |
|                            |      |      | k 1,k     | 1                                 | m,k | m   |      |
|                            | ,…,v |      | ,…,w      |                                   |     |     |      |
| Ifthebasesv                |      | andw |           | arenotclearfromthecontext,thenthe |     |     |      |
|                            | 1    | n    | 1         | m                                 |     |     |      |
| notationℳ(\mathcal{T},(v             |      | ,…,v | ),(w ,…,w | ))isused.                         |     |     |      |
|                            |      | 1 n  | 1         | m                                 |     |     |      |
| Thematrixℳ(\mathcal{T})ofalinearmap\mathcal{T} |      |      |           | \inℒ(\mathcal{V},\mathcal{W})dependsonthebasisv         |     |     | ,…,v |
1 n
of\mathcal{V} andthebasisw ,…,w of\mathcal{W},aswellason\mathcal{T}. However,thebasesshould
|     |     | 1   | m   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
beclearfromthecontext,andthustheyareoftennotincludedinthenotation.
Torememberhowℳ(\mathcal{T})isconstructedfrom\mathcal{T},youmightwriteacrossthe
topofthematrixthebasisvectorsv ,…,v forthedomainandalongtheleftthe
|     |     |     |     | 1 n |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
,…,w
| basisvectorsw |     | forthevectorspaceintowhich\mathcal{T} |     |     |     | maps,asfollows: |     |
| ------------- | --- | --------------------------- | --- | --- | --- | --------------- | --- |
1 m

| --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|                                    |       |                      |     | v ⋯  | v ⋯                 | v          |        |          |             |
| ---------------------------------- | ----- | -------------------- | --- | ---- | ------------------- | ---------- | ------ | -------- | ----------- |
|                                    |       |                      |     | 1    | k                   | n          |        |          |             |
|                                    |       |                      | w   |      | \mathcal{A}                   |            |        |          |             |
|                                    |       |                      | 1 ⎛ |      | 1,k                 |            | ⎞      |          |             |
|                                    | ℳ(\mathcal{T})= |                      | ⎜ ⎜ |      |                     |            | ⎟ ⎟    |          |             |
|                                    |       |                      | ⋮ ⎜ |      | ⋮                   |            | ⎟.     |          |             |
|                                    |       | w                    | ⎝   |      | \mathcal{A}                   |            | ⎠      |          |             |
|                                    |       |                      | m   |      | m,k                 |            |        |          |             |
| Inthematrixaboveonlythekth         |       |                      |     | col- |                     |            |        |          |             |
|                                    |       |                      |     |      | The                 | kth column | of     | ℳ(\mathcal{T})     | consists of |
| umnisshown.                        |       | Thusthesecondindexof |     |      |                     |            |        |          |             |
|                                    |       |                      |     |      | the                 | scalars    | needed | to write | \mathcal{T}v as a     |
| eachdisplayedentryofthematrixabove |       |                      |     |      |                     |            |        |          | k           |
|                                    |       |                      |     |      | linearcombinationof |            |        | w ,…,w   | :           |
|                                    |       |                      |     |      |                     |            |        | 1        | m           |
isk. Thepictureaboveshouldremindyou
m
| that\mathcal{T}v                       | canbecomputedfromℳ(\mathcal{T})by |     |     |     |     |     | \mathcal{T}v =\sum\mathcal{A} | w     | .   |
| ---------------------------- | ----------------------- | --- | --- | --- | --- | --- | ------ | ----- | --- |
|                              | k                       |     |     |     |     |     | k      | j,k j |     |
| multiplyingeachentryinthekth |                         |     |     |     |     |     | j=1    |       |     |
column
| bythecorrespondingw |     |     | fromtheleftcol- |     |     |     |     |     |     |
| ------------------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
j
| umn, and | then | adding | up the | resulting |     |     |     |     |     |
| -------- | ---- | ------ | ------ | --------- | --- | --- | --- | --- | --- |
vectors.
| If \mathcal{T} | is a linear | map | from | \mathbf{F}n to | \mathbf{F}m, |      |          |     |         |
| ---- | ----------- | --- | ---- | ----- | --- | ---- | -------- | --- | ------- |
|      |             |     |      |       | If  | \mathcal{T} is | a linear | map | from an |
thenunlessstatedotherwise,assumethe
|     |     |     |     |     | n-dimensional |     | vector | space | to an |
| --- | --- | --- | --- | --- | ------------- | --- | ------ | ----- | ----- |
bases in question are the standard ones m-dimensional vector space, then
| (wherethekth | basisvectoris1inthekth |     |     |     |     |     |     |     |     |
| ------------ | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ℳ(\mathcal{T})isanm-by-nmatrix.
| slotand0inallotherslots). |     |     | Ifyouthink |     |     |     |     |     |     |
| ------------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
ofelementsof\mathbf{F}mascolumnsofmnumbers,thenyoucanthinkofthekthcolumn
| ofℳ(\mathcal{T})as\mathcal{T} | appliedtothekth |                             |     | standardbasisvector. |     |      |     |     |     |
| --------- | --------------- | --------------------------- | --- | -------------------- | --- | ---- | --- | --- | --- |
|           |                 | thematrixofalinearmapfrom\mathbf{F}2 |     |                      |     | to\mathbf{F}3 |     |     |     |
**3.32 例：** | Suppose\mathcal{T} | \inℒ(\mathbf{F}2,\mathbf{F}3)isdefinedby |     |     |     |     |     |     |     |     |
| -------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
\mathcal{T}(x,y)=(x+3y,2x+5y,7x+9y).
Because\mathcal{T}(1,0)=(1,2,7)and\mathcal{T}(0,1)=(3,5,9),thematrixof\mathcal{T} withrespect
tothestandardbasesisthe3-by-2matrixbelow:
|     |     |     |        |     | 1 3 |      |     |     |     |
| --- | --- | --- | ------ | --- | --- | ---- | --- | --- | --- |
|     |     |     |        |     | ⎛ ⎜ | ⎞ ⎟  |     |     |     |
|     |     |     | ℳ(\mathcal{T})=⎜ |     | 2 5 | ⎟ ⎟. |     |     |     |
⎜
|     |     |     |     |     | ⎝ 7 9 | ⎠   |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
Whenworkingwith𝒫 (\mathbf{F}),usethestandardbasis1,x,x2,…,xm unlessthe
m
contextindicatesotherwise.
| 3.33 | example: | matrixofthedifferentiationmapfrom𝒫 |     |     |     |     | (\mathbf{R})to𝒫 | (\mathbf{R}) |     |
| ---- | -------- | ---------------------------------- | --- | --- | --- | --- | ------ | --- | --- |
$$(\mathbf{R}))isthedifferentiationmapdefinedby\mathcal{D}p=p′.$$
| Suppose\mathcal{D}\inℒ(𝒫 |     |     | (\mathbf{R}),𝒫 |     |     |     |     |     |     |
| ------------ | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Because(xn)′ =nxn-1,thematrixof\mathcal{D}withrespecttothestandardbasesisthe
3-by-4matrixbelow:
|     |     |     |        |     | 0 1 0 | 0      |     |     |     |
| --- | --- | --- | ------ | --- | ----- | ------ | --- | --- | --- |
|     |     |     |        | ⎛ ⎜ |       | ⎞ ⎟    |     |     |     |
|     |     |     | ℳ(\mathcal{D})=⎜ |     | 0 0 2 | 0 ⎟ ⎟. |     |     |     |
⎜
|     |     |     |     | ⎝   | 0 0 0 | 3 ⎠ |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |

| --- | --- | --- | --- | --- | --------- | -------- | --- |
| Addition | and | Scalar | Multiplication |     | of Matrices |     |     |
| -------- | --- | ------ | -------------- | --- | ----------- | --- | --- |
Fortherestofthissection,assumethat\mathcal{U},\mathcal{V},and\mathcal{W} arefinite-dimensionaland
thatabasishasbeenchosenforeachofthesevectorspaces. Thusforeachlinear
mapfrom\mathcal{V} to\mathcal{W},wecantalkaboutitsmatrix(withrespecttothechosenbases).
Isthematrixofthesumoftwolinearmapsequaltothesumofthematricesof
thetwomaps? Rightnowthisquestiondoesnotyetmakesensebecausealthough
wehavedefinedthesumoftwolinearmaps,wehavenotdefinedthesumoftwo
matrices. Fortunately,thenaturaldefinitionofthesumoftwomatriceshasthe
| rightproperties. |     | Specifically,wemakethefollowingdefinition. |     |     |     |     |     |
| ---------------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
| 3.34 definition: |     | matrixaddition                             |     |     |     |     |     |
Thesumoftwomatricesofthesamesizeisthematrixobtainedbyadding
correspondingentriesinthematrices:
| \mathcal{A}   | ⋯   | \mathcal{A}   | \mathcal{C}        | ⋯    | \mathcal{C}       |        |        |
| --- | --- | --- | -------- | ---- | ------- | ------ | ------ |
| ⎛   | 1,1 | 1,n | ⎞ ⎛      | 1,1  | 1,n ⎞   |        |        |
| ⎜   |     |     | ⎟ ⎜      |      | ⎟       |        |        |
| ⎜ ⎜ | ⋮   | ⋮   | ⎟ ⎟ +⎜ ⎜ | ⋮    | ⋮ ⎟ ⎟   |        |        |
| \mathcal{A}   | ⋯   | \mathcal{A}   | \mathcal{C}        | ⋯    | \mathcal{C}       |        |        |
| ⎝   | m,1 | m,n | ⎠ ⎝      | m,1  | m,n ⎠   |        |        |
|     |     |     |          | \mathcal{A}    | +\mathcal{C}      | ⋯ \mathcal{A} +\mathcal{C} |        |
|     |     |     |          | ⎛    | 1,1 1,1 | 1,n    | 1,n ⎞  |
|     |     |     |          | =⎜ ⎜ | ⋮       | ⋮      | ⎟ ⎟ ⎟. |
⎜
|     |     |     |     | ⎝ \mathcal{A} | +\mathcal{C}      | ⋯ \mathcal{A} +\mathcal{C} | ⎠   |
| --- | --- | --- | --- | --- | ------- | ------ | --- |
|     |     |     |     |     | m,1 m,1 | m,n    | m,n |
Inthenextresult,theassumptionisthatthesamebasesareusedforallthree
linearmaps\mathcal{S}+\mathcal{T},\mathcal{S},and\mathcal{T}.
matrixofthesumoflinearmaps
3.35
| Suppose\mathcal{S},\mathcal{T} |     | \inℒ(\mathcal{V},\mathcal{W}). | Thenℳ(\mathcal{S}+\mathcal{T})=ℳ(\mathcal{S})+ℳ(\mathcal{T}). |     |     |     |     |
| ---------- | --- | -------- | --------------------- | --- | --- | --- | --- |
Theverificationoftheresultabovefollowsfromthedefinitionsandisleftto
thereader.
Stillassumingthatwehavesomebasesinmind,isthematrixofascalartimes
alinearmapequaltothescalartimesthematrixofthelinearmap? Again,the
questiondoesnotyetmakesensebecausewehavenotdefinedscalarmultiplication
onmatrices. Fortunately,thenaturaldefinitionagainhastherightproperties.
| 3.36 definition: |     | scalarmultiplicationofamatrix |     |     |     |     |     |
| ---------------- | --- | ----------------------------- | --- | --- | --- | --- | --- |
Theproductofascalarandamatrixisthematrixobtainedbymultiplying
eachentryinthematrixbythescalar:
|     |     | \mathcal{A}     | ⋯ \mathcal{A} |           | \lambda\mathcal{A}  | ⋯ \lambda\mathcal{A}     |     |
| --- | --- | ----- | --- | --------- | --- | -------- | --- |
|     |     | ⎛ 1,1 | 1,n | ⎞ ⎛       | 1,1 | 1,n ⎞    |     |
|     | \lambda⎜  | ⎜ ⋮   | ⋮   | ⎟ ⎟ ⎟=⎜ ⎜ | ⋮   | ⋮ ⎟ ⎟ ⎟. |     |
|     |     | ⎜     |     | ⎜         |     |          |     |
|     |     | ⎝ \mathcal{A}   | ⋯ \mathcal{A} | ⎠ ⎝       | \lambda\mathcal{A}  | ⋯ \lambda\mathcal{A} ⎠   |     |
|     |     | m,1   | m,n |           | m,1 | m,n      |     |

72 Chapter 3 Linear Maps
**3.37 例：** additionandscalarmultiplicationofmatrices
3 1 4 2 6 2 4 2 10 4
2( )+( )=( )+( )=( )
-1 5 1 6 -2 10 1 6 -1 16
Inthenextresult,theassumptionisthatthesamebasesareusedforboththe
linearmaps \lambda\mathcal{T} and\mathcal{T}.
3.38 thematrixofascalartimesalinearmap
Suppose \lambda\in\mathbf{F} and\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Thenℳ(\lambda\mathcal{T})= \lambdaℳ(\mathcal{T}).
Theverificationoftheresultaboveisalsolefttothereader.
Becauseadditionandscalarmultiplicationhavenowbeendefinedformatrices,
you should not be surprised that a vector space is about to appear. First we
introduceabitofnotationsothatthisnewvectorspacehasaname,andthenwe
findthedimensionofthisnewvectorspace.
**3.39 记号：** \mathbf{F}m,n
Formandnpositiveintegers,thesetofallm-by-nmatriceswithentriesin\mathbf{F}
isdenotedby\mathbf{F}m,n.
3.40 dim\mathbf{F}m,n =mn
Supposemandnarepositiveintegers. Withadditionandscalarmultiplication
definedasabove,\mathbf{F}m,n isavectorspaceofdimensionmn.
Proof Theverificationthat\mathbf{F}m,n isavectorspaceislefttothereader. Notethat
theadditiveidentityof\mathbf{F}m,n isthem-by-nmatrixallofwhoseentriesequal0.
Thereadershouldalsoverifythatthelistofdistinctm-by-nmatricesthathave
0inallentriesexceptfora1inoneentryisabasisof\mathbf{F}m,n. Therearemnsuch
matrices,sothedimensionof\mathbf{F}m,n equalsmn.
Suppose, aspreviously, that v ,…,v isabasisof\mathcal{V} andw ,…,w isabasis
1 n 1 m
of\mathcal{W}. Supposealsothatu ,…,u isabasisof\mathcal{U}.
1 p
Considerlinearmaps\mathcal{T}∶ \mathcal{U} \rightarrow \mathcal{V} and\mathcal{S}∶ \mathcal{V} \rightarrow \mathcal{W}. Thecomposition\mathcal{S}\mathcal{T} isa
linearmapfrom\mathcal{U} to\mathcal{W}. Doesℳ(\mathcal{S}\mathcal{T})equalℳ(\mathcal{S})ℳ(\mathcal{T})? Thisquestiondoes
notyetmakesensebecausewehavenotdefinedtheproductoftwomatrices. We
willchooseadefinitionofmatrixmultiplicationthatforcesthisquestiontohave
apositiveanswer. Let’sseehowtodothis.

| --- | --- | --- | --- | --- | --------- | -------- | --- |
| Supposeℳ(\mathcal{S})=\mathcal{A}andℳ(\mathcal{T})=\mathcal{B}. |     |     |     | For1\leqk | \leqp,wehave |     |     |
| ----------------------- | --- | --- | --- | ------ | --------- | --- | --- |
n
|     |     | (\mathcal{S}\mathcal{T})u k =\mathcal{S}(\sum\mathcal{B} |     | r,k v r ) |     |     |     |
| --- | --- | ------------- | --- | --------- | --- | --- | --- |
$$r=1$$
n
|     |     | =   | \sum\mathcal{B}  | \mathcal{S}v  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
r,k r
$$r=1$$
n m
|     |     | =   | \sum\mathcal{B}  | \sum\mathcal{A}  | w   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | r,k | j,r | j   |     |     |
$$r=1 j=1$$
m n
|     |     | =   | \sum(\sum\mathcal{A} | \mathcal{B}       | )w. |     |     |
| --- | --- | --- | ---- | ------- | --- | --- | --- |
|     |     |     |      | j,r r,k | j   |     |     |
$$j=1 r=1$$
Thusℳ(\mathcal{S}\mathcal{T})isthem-by-pmatrixwhoseentryinrowj,columnk,equals
n
|     |     |     | \sum\mathcal{A}  | \mathcal{B} . |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
j,r r,k
$$r=1$$
Nowweseehowtodefinematrixmultiplicationsothatthedesiredequation
ℳ(\mathcal{S}\mathcal{T})=ℳ(\mathcal{S})ℳ(\mathcal{T})holds.
| 3.41 | definition: matrixmultiplication |     |     |     |     |     |     |
| ---- | -------------------------------- | --- | --- | --- | --- | --- | --- |
Suppose\mathcal{A}isanm-by-nmatrixand\mathcal{B}isann-by-pmatrix. Then\mathcal{A}\mathcal{B}isdefined
to be the m-by-p matrix whose entry in row j, column k, is given by the
equation
n
|     |     | (\mathcal{A}\mathcal{B}) | = \sum\mathcal{A} | \mathcal{B}       | .   |     |     |
| --- | --- | ---- | ---- | ------- | --- | --- | --- |
|     |     |      | j,k  | j,r r,k |     |     |     |
$$r=1$$
Thustheentryinrowj,columnk,of\mathcal{A}\mathcal{B}iscomputedbytakingrowjof\mathcal{A}and
columnkof\mathcal{B},multiplyingtogethercorrespondingentries,andthensumming.
| Note | that we define | the product | of  |     |     |     |     |
| ---- | -------------- | ----------- | --- | --- | --- | --- | --- |
Youmayhavelearnedthisdefinition
| two matrices | only when | the number | of  |     |     |     |     |
| ------------ | --------- | ---------- | --- | --- | --- | --- | --- |
ofmatrixmultiplicationinanearlier
| columns                        | of the first         | matrix equals | the |                          |          |         |          |
| ------------------------------ | -------------------- | ------------- | --- | ------------------------ | -------- | ------- | -------- |
|                                |                      |               |     | course,                  | although | you may | not have |
| numberofrowsofthesecondmatrix. |                      |               |     | seenthismotivationforit. |          |         |          |
| 3.42 example:                  | matrixmultiplication |               |     |                          |          |         |          |
Herewemultiplytogethera3-by-2matrixanda2-by-4matrix,obtaininga
3-by-4matrix:
|     | 1 2            |       |     |     | 10 7  | 4 1         |     |
| --- | -------------- | ----- | --- | --- | ----- | ----------- | --- |
|     | ⎛ ⎞            | 6 5 4 | 3   | ⎛   |       | ⎞           |     |
|     | ⎜ ⎜ 3 4 ⎟ ⎟ ⎟( |       | )=⎜ | ⎜   | 26 19 | 12 5 ⎟ ⎟ ⎟. |     |
|     | ⎜              |       |     | ⎜   |       |             |     |
|     |                | 2 1 0 | -1  |     |       |             |     |
|     | ⎝ 5 6 ⎠        |       |     | ⎝   | 42 31 | 20 9 ⎠      |     |
Matrix multiplication is not commutative—\mathcal{A}\mathcal{B} is not necessarily equal to
\mathcal{B}\mathcal{A}evenifbothproductsaredefined(see Exercise10). Matrixmultiplicationis
distributiveandassociative(see Exercises11and12).

| -------- | ---------- | --- | --- | --- | --- |
Inthenextresult,weassumethatthesamebasisof\mathcal{V} isusedinconsidering
\mathcal{T} \in ℒ(\mathcal{U},\mathcal{V}) and \mathcal{S} \in ℒ(\mathcal{V},\mathcal{W}), the same basis of \mathcal{W} is used in considering
| \mathcal{S}\inℒ(\mathcal{V},\mathcal{W})and\mathcal{S}\mathcal{T}  | \inℒ(\mathcal{U},\mathcal{W}),andthesamebasisof\mathcal{U}isusedinconsidering |     |     |     |     |
| -------------- | --------------------------------------------- | --- | --- | --- | --- |
| \mathcal{T} \inℒ(\mathcal{U},\mathcal{V})and\mathcal{S}\mathcal{T} | \inℒ(\mathcal{U},\mathcal{W}).                                      |     |     |     |     |
3.43 matrixofproductoflinearmaps
If\mathcal{T} \inℒ(\mathcal{U},\mathcal{V})and\mathcal{S}\inℒ(\mathcal{V},\mathcal{W}),thenℳ(\mathcal{S}\mathcal{T})=ℳ(\mathcal{S})ℳ(\mathcal{T}).
Theproofoftheresultaboveisthecalculationthatwasdoneasmotivation
beforethedefinitionofmatrixmultiplication.
Inthenextpieceofnotation,notethatasusualthefirstindexreferstoarow
andthesecondindexreferstoacolumn,withaverticallycentereddotusedasa
placeholder.
| 3.44 notation: | \mathcal{A} ,\mathcal{A}    |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- |
|                | j,\cdot \cdot,k |     |     |     |     |
Suppose\mathcal{A}isanm-by-nmatrix.
| • If1\leqj | \leqm,then\mathcal{A} | denotesthe1-by-nmatrixconsistingofrowjof\mathcal{A}. |     |     |     |
| ------- | -------- | ------------------------------------------ | --- | --- | --- |
j,\cdot
• If1\leq k \leq n,then\mathcal{A} \cdot,k denotesthem-by-1matrixconsistingofcolumnk
of\mathcal{A}.
|               | \mathcal{A} equalsjth                | rowof \mathcal{A}and\mathcal{A} | equalskth | columnof         | \mathcal{A}   |
| ------------- | -------------------------- | ----------- | --------- | ---------------- | --- |
| 3.45 example: | j,\cdot                        |             | \cdot,k       |                  |     |
| Thenotation\mathcal{A}  | denotesthesecondrowof\mathcal{A}and\mathcal{A} |             |           | denotesthesecond |     |
|               | 2,\cdot                        |             |           | \cdot,2              |     |
8 4 5
| columnof\mathcal{A}. | Thusif\mathcal{A}=( | ),then |     |     |     |
| ---------- | --------- | ------ | --- | --- | --- |
1 9 7
|     | \mathcal{A} =( | 1 9 7 ) and | \mathcal{A} =( | ).  |     |
| --- | ---- | ----------- | ---- | --- | --- |
|     | 2,\cdot  |             | \cdot,2  | 9   |     |
Theproductofa1-by-nmatrixandann-by-1matrixisa1-by-1matrix. However,wewillfrequentlyidentifya1-by-1matrixwithitsentry. Forexample,
|     |     | ( 3 4 )( )=( | 26 ) |     |     |
| --- | --- | ------------ | ---- | --- | --- |
because 3\cdot6+4\cdot2 = 26. However, we can identify ( 26 ) with 26, writing
| ( 3 4 )( | )=26. |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
Thenextresultusestheconventiondiscussedintheparagraphabovetogive
anotherwaytothinkofmatrixmultiplication. Forexample,thenextresultand
thecalculationintheparagraphaboveexplainwhytheentryinrow2,column1,
oftheproductin Example3.42equals26.

| --- | --- | --- | --- | --- | --------- | -------- |
entryofmatrixproductequalsrowtimescolumn
3.46
| Suppose\mathcal{A}isanm-by-nmatrixand\mathcal{B}isann-by-pmatrix. |          |     |                                            |     |         | Then |
| --------------------------------------------- | -------- | --- | ------------------------------------------ | --- | ------- | ---- |
|                                               |          |     | (\mathcal{A}\mathcal{B})                                       | =\mathcal{A}  | \mathcal{B}       |      |
|                                               |          |     |                                            | j,k | j,\cdot \cdot,k |      |
| if1\leqj                                         | \leqmand1\leqk |     | \leqp. Inotherwords,theentryinrowj,columnk,of |     |         |      |
\mathcal{A}\mathcal{B}equals(rowjof\mathcal{A})times(columnkof\mathcal{B}).
Proof Suppose1\leqj \leqmand1\leqk \leqp. Thedefinitionofmatrixmultiplication
statesthat
| 3.47 |     | (\mathcal{A}\mathcal{B}) | =\mathcal{A}  | \mathcal{B} +⋯+\mathcal{A}  | \mathcal{B}   | .   |
| ---- | --- | ---- | --- | ------- | --- | --- |
|      |     |      | j,k | j,1 1,k | j,n | n,k |
Thedefinitionofmatrixmultiplicationalsoimpliesthattheproductofthe1-by-n
matrix \mathcal{A} and the n-by-1 matrix \mathcal{B} is the 1-by-1 matrix whose entry is the
|     | j,\cdot |     |     | \cdot,k |     |     |
| --- | --- | --- | --- | --- | --- | --- |
numberontherightsideoftheequationabove. Thustheentryinrowj,columnk,
of\mathcal{A}\mathcal{B}equals(rowjof\mathcal{A})times(columnkof\mathcal{B}).
Thenextresultgivesyetanotherwaytothinkofmatrix multiplication. In
theresultbelow,(\mathcal{A}\mathcal{B}) iscolumnk ofthem-by-pmatrix\mathcal{A}\mathcal{B}. Thus(\mathcal{A}\mathcal{B}) is
\cdot,k \cdot,k
anm-by-1matrix. Also,\mathcal{A}\mathcal{B} isanm-by-1matrixbecauseitistheproductofan
\cdot,k
m-by-nmatrixandann-by-1matrix. Thusthetwosidesoftheequationinthe
resultbelowhavethesamesize,makingitreasonablethattheymightbeequal.
3.48 columnofmatrixproductequalsmatrixtimescolumn
| Suppose\mathcal{A}isanm-by-nmatrixand\mathcal{B}isann-by-pmatrix. |                                                     |     |      |     |     | Then |
| --------------------------------------------- | --------------------------------------------------- | --- | ---- | --- | --- | ---- |
|                                               |                                                     |     | (\mathcal{A}\mathcal{B}) | =\mathcal{A}\mathcal{B} |     |      |
|                                               |                                                     |     |      | \cdot,k | \cdot,k |      |
| if1\leqk                                         | \leqp. Inotherwords,columnkof\mathcal{A}\mathcal{B}equals\mathcal{A}timescolumnkof\mathcal{B}. |     |      |     |     |      |
Proof Asdiscussedabove,(\mathcal{A}\mathcal{B}) and\mathcal{A}\mathcal{B} arebothm-by-1matrices. If1\leq
|     |     |     |     | \cdot,k | \cdot,k |     |
| --- | --- | --- | --- | --- | --- | --- |
j \leq m,thentheentryinrowjof(\mathcal{A}\mathcal{B}) istheleftsideof3.47andtheentryin
\cdot,k
| rowjof\mathcal{A}\mathcal{B} | istherightsideof3.47. |     |     | Thus(\mathcal{A}\mathcal{B}) | =\mathcal{A}\mathcal{B} | .   |
| -------- | --------------------- | --- | --- | -------- | --- | --- |
|          | \cdot,k                   |     |     |          | \cdot,k | \cdot,k |
Our next result will give another way of thinking about the product of an
m-by-nmatrixandann-by-1matrix,motivatedbythenextexample.
| 3.49 example: | productofa3-by-2matrixanda2-by-1matrix |     |     |     |     |     |
| ------------- | -------------------------------------- | --- | --- | --- | --- | --- |
Useourdefinitionsandbasicarithmetictoverifythat
|     | 1     | 2        |     | 7             | 1       | 2              |
| --- | ----- | -------- | --- | ------------- | ------- | -------------- |
|     | ⎛     | ⎞        | 5   | ⎛ ⎞           | ⎛ ⎞     | ⎛ ⎞            |
|     | ⎜ ⎜ 3 | 4 ⎟ ⎟ ⎟( | )=⎜ | ⎜ 19 ⎟ ⎟ ⎟=5⎜ | ⎜ 3 ⎟ ⎟ | +1⎜ ⎜ 4 ⎟ ⎟ ⎟. |
|     | ⎜     |          |     | ⎜             | ⎜ ⎟     | ⎜              |
|     | ⎝ 5 | 6 ⎠ |     | ⎝ 31 ⎠ | ⎝ 5 ⎠ | ⎝ 6 ⎠ |
| --- | --- | --- | --- | ------ | ----- | ----- |
Thus in this example, the product of a 3-by-2 matrix and a 2-by-1 matrix is a
linearcombinationofthecolumnsofthe3-by-2matrix,withthescalars(5and1)
thatmultiplythecolumnscomingfromthe2-by-1matrix.

| -------- | ---------- | --- | --- | --- |
Thenextresultgeneralizestheexampleabove.
linearcombinationofcolumns
3.50
b
|     |     | ⎛ 1 | ⎞   |     |
| --- | --- | --- | --- | --- |
|     |     | ⎜   | ⎟   |     |
Suppose\mathcal{A}isanm-by-nmatrixandb=⎜ ⎜ ⋮ ⎟ ⎟ isann-by-1matrix. Then
b
|     |      | ⎝ n     | ⎠   |     |
| --- | ---- | ------- | --- | --- |
|     | \mathcal{A}b=b | \mathcal{A} +⋯+b  | \mathcal{A} . |     |
|     |      | 1 \cdot,1 n | \cdot,n |     |
In other words, \mathcal{A}b is a linear combination of the columns of \mathcal{A}, with the
scalarsthatmultiplythecolumnscomingfromb.
Proof Ifk \in{1,…,m},thenthedefinitionofmatrixmultiplicationimpliesthat
theentryinrowkofthem-by-1matrix\mathcal{A}bis
|     | \mathcal{A}   | b +⋯+\mathcal{A} b | .   |     |
| --- | --- | -------- | --- | --- |
|     | k,1 | 1 k,n    | n   |     |
+⋯+b
Theentryinrowkofb \mathcal{A} \cdot,1 \mathcal{A} \cdot,n alsoequalsthenumberdisplayedabove.
|                             | 1      | n                        |         |         |
| --------------------------- | ------ | ------------------------ | ------- | ------- |
| Because\mathcal{A}bandb               | \mathcal{A} +⋯+b | \mathcal{A} havethesameentryinrowk |         | foreach |
|                             | 1 \cdot,1  | n \cdot,n                    |         |         |
| \in{1,…,m},weconcludethat\mathcal{A}b=b |        | +⋯+b                     |         |         |
| k                           |        | \mathcal{A} \cdot,1                    | \mathcal{A} \cdot,n . |         |
|                             |        | 1                        | n       |         |
Ourtwopreviousresultsfocusonthecolumnsofamatrix. Analogousresults
holdfortherowsofamatrix. Specifically,see Exercises8and9,whichcanbe
provedusingappropriatemodificationsoftheproofsof3.48and3.50.
The next result is the main tool used in the next subsection to prove the
column–rowfactorization(3.56)andtoprovethatthecolumnrankofamatrix
equalstherowrank(3.57). Tobeconsistentwiththenotationoftenusedwiththe
column–rowfactorization,includinginthenextsubsection,thematricesinthe
nextresultarecalled\mathcal{C}and\mathcal{R}insteadof\mathcal{A}and\mathcal{B}.
matrixmultiplicationaslinearcombinationsofcolumnsorrows
3.51
Suppose\mathcal{C}isanm-by-cmatrixand\mathcal{R}isac-by-nmatrix.
$$(a) If k \in {1,…,n}, then column k of \mathcal{C}\mathcal{R} is a linear combination of the$$
columns of \mathcal{C}, with the coefficients of this linear combination coming
fromcolumnkof\mathcal{R}.
$$(b) Ifj \in{1,…,m},thenrowjof\mathcal{C}\mathcal{R}isalinearcombinationoftherowsof$$
\mathcal{R},withthecoefficientsofthislinearcombinationcomingfromrowjof
\mathcal{C}.
Proof Suppose k \in {1,…,n}. Then column k of \mathcal{C}\mathcal{R} equals \mathcal{C}\mathcal{R} (by 3.48),
\cdot,k
whichequalsthelinearcombinationofthecolumnsof\mathcal{C}withcoefficientscoming
| from\mathcal{R} (by3.50). | Thus(a)holds. |     |     |     |
| --------------- | ------------- | --- | --- | --- |
\cdot,k
To prove (b), follow the pattern of the proof of (a) but use rows instead of
columnsanduse Exercises8and9insteadof3.48and3.50.

| --- | --- | --- | --- | --------- | -------- |
| Column–Row | Factorization |     | and Rank | of a | Matrix |
| ---------- | ------------- | --- | -------- | ---- | ------ |
Webeginbydefiningtwononnegativeintegersassociatedwitheachmatrix.
columnrank,rowrank
**3.52 定义：** Suppose\mathcal{A}isanm-by-nmatrixwithentriesin\mathbf{F}.
| • Thecolumnrank |     | of\mathcal{A}isthedimensionofthespanofthecolumnsof\mathcal{A} |     |     |     |
| --------------- | --- | ----------------------------------------- | --- | --- | --- |
in\mathbf{F}m,1.
| • Therowrank | of\mathcal{A}isthedimensionofthespanoftherowsof\mathcal{A}in\mathbf{F}1,n. |     |     |     |     |
| ------------ | --------------------------------------------- | --- | --- | --- | --- |
If\mathcal{A}isanm-by-nmatrix,thenthecolumnrankof\mathcal{A}isatmostn(because\mathcal{A}has
ncolumns)andthecolumnrankof\mathcal{A}isalsoatmostm(becausedim\mathbf{F}m,1 =m).
Similarly,therowrankof\mathcal{A}isalsoatmostmin{m,n}.
| 3.53 example: | columnrankandrowrankofa2-by-4matrix |     |     |     |     |
| ------------- | ----------------------------------- | --- | --- | --- | --- |
Suppose
|     |     |     | 4 7 | 1 8 |     |
| --- | --- | --- | --- | --- | --- |
|     |     | \mathcal{A}=( |     | ).  |     |
|     |     |     | 3 5 | 2 9 |     |
Thecolumnrankof\mathcal{A}isthedimensionof
|     |         | ⎛   | 4 7     | 1   | 8 ⎞ |
| --- | ------- | --- | ------- | --- | --- |
|     | span⎜⎜( |     | ),( ),( | ),( | )⎟⎟ |
|     |         |     | 3 5     | 2   | 9   |
|     |         | ⎝   |         |     | ⎠   |
in\mathbf{F}2,1. Neitherofthefirsttwovectorslistedabovein\mathbf{F}2,1 isascalarmultipleof
theother. Thusthespanofthislistoflengthfourhasdimensionatleasttwo. The
spanofthislistofvectorsin\mathbf{F}2,1 cannothavedimensionlargerthantwobecause
dim\mathbf{F}2,1=2.
Thusthespanofthislisthasdimensiontwo,whichmeansthatthe
columnrankof\mathcal{A}istwo.
Therowrankof\mathcal{A}isthedimensionof
|     | span(( | 4   | 7 1 8 ),( | 3 5 | 2 9 )) |
| --- | ------ | --- | --------- | --- | ------ |
in\mathbf{F}1,4. Neitherofthetwovectorslistedabovein\mathbf{F}1,4 isascalarmultipleofthe
other. Thusthespanofthislistoflengthtwohasdimensiontwo,whichmeans
thattherowrankof\mathcal{A}istwo.
Wenowdefinethetransposeofamatrix.
transpose,\mathcal{A}t
**3.54 定义：** Thetransposeofamatrix\mathcal{A},denotedby\mathcal{A}t,isthematrixobtainedfrom\mathcal{A}by
interchangingrowsandcolumns. Specifically,if\mathcal{A}isanm-by-nmatrix,then
\mathcal{A}t isthen-by-mmatrixwhoseentriesaregivenbytheequation
|     |     |     | (\mathcal{A}t) =\mathcal{A} | .   |     |
| --- | --- | --- | ------- | --- | --- |
|     |     |     | k,j     | j,k |     |

| --- | -------- | ---------- | --- | --- | --- | --- | --- |
transposeofamatrix
**3.55 例：** 5 -7
|      | ⎛     | ⎞     |         | 5   | 3 -4 |     |     |
| ---- | ----- | ----- | ------- | --- | ---- | --- | --- |
|      | ⎜     | ⎟     | ,then\mathcal{A}t |     |      |     |     |
| If\mathcal{A}= | ⎜ ⎜ 3 | 8 ⎟ ⎟ | =(      |     |      | ).  |     |
-7 8 2
-4 2
|     | ⎝   | ⎠   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Notethathere\mathcal{A}isa3-by-2matrixand\mathcal{A}t
isa2-by-3matrix.
Thetransposehasnicealgebraicproperties: (\mathcal{A}+\mathcal{B})t =\mathcal{A}t+\mathcal{B}t,(\lambda\mathcal{A})t = \lambda\mathcal{A}t,
| and(\mathcal{A}\mathcal{C})t | =\mathcal{C}t\mathcal{A}tforallm-by-nmatrices\mathcal{A},\mathcal{B},all |     |     |     |     |     |     |
| -------- | -------------------------------- | --- | --- | --- | --- | --- | --- |
\lambda\in\mathbf{F},andalln-by-pmatrices
\mathcal{C}(see Exercises14and15).
Thenextresultwillbethemaintoolusedtoprovethatthecolumnrankequals
therowrank(see3.57).
3.56 column–rowfactorization
Suppose\mathcal{A}isanm-by-nmatrixwithentriesin\mathbf{F}andcolumnrankc \geq1. Then
thereexistanm-by-cmatrix\mathcal{C}andac-by-nmatrix\mathcal{R},bothwithentriesin\mathbf{F},
suchthat\mathcal{A}=\mathcal{C}\mathcal{R}.
| Proof | Eachcolumnof\mathcal{A}isanm-by-1matrix. |     |     |     | Thelist\mathcal{A} | ,…,\mathcal{A} | ofcolumns |
| ----- | ------------------------------ | --- | --- | --- | -------- | ---- | --------- |
|       |                                |     |     |     |          | \cdot,1  | \cdot,n       |
of\mathcal{A}canbereducedtoabasisofthespanofthecolumnsof\mathcal{A}(by2.30). This
basishaslengthc,bythedefinitionofthecolumnrank. Theccolumnsinthis
basiscanbeputtogethertoformanm-by-cmatrix\mathcal{C}.
Ifk \in{1,…,n},thencolumnkof\mathcal{A}isalinearcombinationofthecolumns
of\mathcal{C}. Makethecoefficientsofthislinearcombinationintocolumnkofac-by-n
| matrixthatwecall\mathcal{R}. |     | Then\mathcal{A}=\mathcal{C}\mathcal{R},asfollowsfrom3.51(a). |     |     |     |     |     |
| ------------------ | --- | ------------------------------ | --- | --- | --- | --- | --- |
In Example3.53,thecolumnrankandrowrankturnedouttoequaleachother.
Thenextresultstatesthatthishappensforallmatrices.
3.57 columnrankequalsrowrank
| Suppose\mathcal{A}\in\mathbf{F}m,n. |     | Thenthecolumnrankof\mathcal{A}equalstherowrankof\mathcal{A}. |     |     |     |     |     |
| -------------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
Proof Letcdenotethecolumnrankof\mathcal{A}. Ifc = 0,then\mathcal{A} = 0andhencethe
| rowrankof\mathcal{A}alsoequals0. |     |     | Thuswecanassumethatc |     |     | \geq1. |     |
| ---------------------- | --- | --- | -------------------- | --- | --- | --- | --- |
Let\mathcal{A}=\mathcal{C}\mathcal{R}bethecolumn–rowfactorizationof\mathcal{A}givenby3.56,where\mathcal{C}is
anm-by-cmatrixand\mathcal{R}isac-by-nmatrix. Then3.51(b)tellsusthateveryrow
of\mathcal{A}isalinearcombinationoftherowsof\mathcal{R}. Because\mathcal{R}hascrows,thisimplies
thattherowrankof\mathcal{A}islessthanorequaltothecolumnrankcof\mathcal{A}.
Toprovetheinequalityintheotherdirection,applythepreviousparagraph
resultto\mathcal{A}t,getting
columnrankof\mathcal{A}=rowrankof\mathcal{A}t
\leqcolumnrankof\mathcal{A}t
=rowrankof\mathcal{A}.
Thusthecolumnrankof\mathcal{A}equalstherowrankof\mathcal{A}.

| --- | --- | --- | --- | --------- | -------- |
Because the column rank equals the row rank, the last result allows us to
dispensewiththeterms“columnrank”and“rowrank”andjustusethesimpler
term“rank”.
rank
**3.58 定义：** | Therank ofamatrix\mathcal{A}\in\mathbf{F}m,n |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- |
isthecolumnrankof\mathcal{A}.
See3.133and Exercise8in Section7Aforalternativeproofsthatthecolumn
rankequalstherowrank.
| Exercises           | 3C       |                                          |     |                 |     |
| ------------------- | -------- | ---------------------------------------- | --- | --------------- | --- |
| 1 Suppose\mathcal{T}          | \inℒ(\mathcal{V},\mathcal{W}). | Showthatwithrespecttoeachchoiceofbasesof |     |                 |     |
| \mathcal{V} and\mathcal{W},thematrixof\mathcal{T} |          | hasatleastdimrange\mathcal{T}                      |     | nonzeroentries. |     |
2 Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}),where\mathcal{V} and\mathcal{W} arefinite-dimensionalandnonzero.
Provethatdimrange\mathcal{T} =1ifandonlyifthereexistabasisof\mathcal{V} andabasis
| of\mathcal{W} suchthatwithrespecttothesebases,allentriesofℳ(\mathcal{T})equal1. |                  |                               |                    |              |        |
| ----------------------------------------------------------- | ---------------- | ----------------------------- | ------------------ | ------------ | ------ |
| 3 Supposev                                                  | ,…,v isabasisof\mathcal{V} |                               | andw ,…,w          | isabasisof\mathcal{W}. |        |
|                                                             | 1 n              |                               | 1                  | m            |        |
| (a) Showthatif\mathcal{S},\mathcal{T}                                           |                  | \inℒ(\mathcal{V},\mathcal{W}),thenℳ(\mathcal{S}+\mathcal{T})=ℳ(\mathcal{S})+ℳ(\mathcal{T}). |                    |              |        |
| (b) Showthatif                                              | \lambda\in\mathbf{F}              | and\mathcal{T}                          | \inℒ(\mathcal{V},\mathcal{W}),thenℳ(\lambda\mathcal{T})= |              | \lambdaℳ(\mathcal{T}). |
Thisexerciseasksyoutoverify3.35and3.38.
4 Supposethat\mathcal{D} \in ℒ(𝒫 (\mathbf{R}),𝒫 (\mathbf{R}))isthedifferentiationmapdefinedby
3 2
| \mathcal{D}p=p′. | Findabasisof𝒫 | (\mathbf{R})andabasisof𝒫 |     |     |     |
| ------ | ------------- | --------------- | --- | --- | --- |
$$(\mathbf{R})suchthatthematrixof$$
| --- | --- | --- | --- | --- | --- |
\mathcal{D}withrespecttothesebasesis
|     |     |     | 1 0 0 0 |      |     |
| --- | --- | --- | ------- | ---- | --- |
|     |     | ⎛   |         | ⎞    |     |
|     |     | ⎜   |         | ⎟    |     |
|     |     | ⎜ ⎜ | 0 1 0 0 | ⎟ ⎟. |     |
|     |     |     | 0 0 1 0 |      |     |
|     |     | ⎝   |         | ⎠    |     |
Comparewith Example3.33. Thenextexercisegeneralizesthisexercise.
5 Suppose\mathcal{V}and\mathcal{W}arefinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Provethatthere
existabasisof\mathcal{V} andabasisof\mathcal{W} suchthatwithrespecttothesebases,all
entriesofℳ(\mathcal{T})are0exceptthattheentriesinrowk,columnk,equal1if
| 1\leqk \leqdimrange\mathcal{T}. |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
,…,v
6 Suppose v is a basis of \mathcal{V} and \mathcal{W} is finite-dimensional. Suppose
1 m
| \mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). | Provethatthereexistsabasisw |     |     | ,…,w | of\mathcal{W} suchthatall |
| ---------- | --------------------------- | --- | --- | ---- | --------------- |
1 n
| entriesinthefirstcolumnofℳ(\mathcal{T})[withrespecttothebasesv |     |     |     |     | ,…,v |
| ---------------------------------------------------- | --- | --- | --- | --- | ---- |
and
1 m
| w ,…,w | ]are0exceptforpossiblya1inthefirstrow,firstcolumn. |     |     |     |     |
| ------ | -------------------------------------------------- | --- | --- | --- | --- |
| 1      | n                                                  |     |     |     |     |
Inthisexercise,unlike Exercise5,youaregiventhebasisof\mathcal{V}insteadof
beingabletochooseabasisof\mathcal{V}.

| -------- | ---------- | --- | --- | --- |
7 Supposew ,…,w isabasisof\mathcal{W} and\mathcal{V} isfinite-dimensional. Suppose
1 n
| \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). | Provethatthereexistsabasisv |     | ,…,v of\mathcal{V} | suchthatall |
| ----------- | --------------------------- | --- | -------- | ----------- |
1 m
entries in the first row of ℳ(\mathcal{T}) [with respect to the bases v ,…,v and
1 m
| w ,…,w ]are0exceptforpossiblya1inthefirstrow,firstcolumn. |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- |
| 1 n                                                       |     |     |     |     |
Inthisexercise,unlike Exercise5,youaregiventhebasisof\mathcal{W}insteadof
beingabletochooseabasisof\mathcal{W}.
| 8 Suppose\mathcal{A}isanm-by-nmatrixand\mathcal{B}isann-by-pmatrix. |                                                  |                   |     | Provethat |
| ----------------------------------------------- | ------------------------------------------------ | ----------------- | --- | --------- |
|                                                 |                                                  | (\mathcal{A}\mathcal{B}) j,\cdot =\mathcal{A} j,\cdot \mathcal{B} |     |           |
| foreach1\leqj                                      | \leqm. Inotherwords,showthatrowjof\mathcal{A}\mathcal{B}equals(rowjof\mathcal{A}) |                   |     |           |
times\mathcal{B}.
Thisexercisegivestherowversionof3.48.
| 9 Supposea=( | a ⋯ | a )isa1-by-nmatrixand\mathcal{B}isann-by-pmatrix. |     |     |
| ------------ | --- | --------------------------------------- | --- | --- |
|              | 1   | n                                       |     |     |
Provethat
|     |     | a\mathcal{B}=a \mathcal{B} +⋯+a | \mathcal{B} .   |     |
| --- | --- | ----------- | ----- | --- |
|     |     | 1 1,\cdot       | n n,\cdot |     |
Inotherwords,showthata\mathcal{B}isalinearcombinationoftherowsof\mathcal{B},with
thescalarsthatmultiplytherowscomingfroma.
Thisexercisegivestherowversionof3.50.
10 Giveanexampleof2-by-2matrices\mathcal{A}and\mathcal{B}suchthat\mathcal{A}\mathcal{B}\neq\mathcal{B}\mathcal{A}.
11 Prove that the distributive property holds for matrix addition and matrix
multiplication. Inotherwords,suppose\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{D},\mathcal{E},and\mathcal{F}arematrices
| whosesizesaresuchthat\mathcal{A}(\mathcal{B}+\mathcal{C})and(\mathcal{D}+\mathcal{E})\mathcal{F}makesense. |     |     |     | Explainwhy |
| ---------------------------------------------- | --- | --- | --- | ---------- |
\mathcal{A}\mathcal{B}+\mathcal{A}\mathcal{C}and\mathcal{D}\mathcal{F}+\mathcal{E}\mathcal{F}bothmakesenseandprovethat
| \mathcal{A}(\mathcal{B}+\mathcal{C})=\mathcal{A}\mathcal{B}+\mathcal{A}\mathcal{C} |     | (\mathcal{D}+\mathcal{E})\mathcal{F} | =\mathcal{D}\mathcal{F}+\mathcal{E}\mathcal{F}. |     |
| ------------ | --- | ------ | ------- | --- |
and
12 Provethatmatrixmultiplicationisassociative. Inotherwords,suppose\mathcal{A},\mathcal{B},
| and\mathcal{C}arematriceswhosesizesaresuchthat(\mathcal{A}\mathcal{B})\mathcal{C}makessense. |     |     |     | Explain |
| ---------------------------------------------------- | --- | --- | --- | ------- |
why\mathcal{A}(\mathcal{B}\mathcal{C})makessenseandprovethat
$$(\mathcal{A}\mathcal{B})\mathcal{C} =\mathcal{A}(\mathcal{B}\mathcal{C}).$$
Trytofindacleanproofthatillustratesthefollowingquotefrom Emil Artin:
“Itismyexperiencethatproofsinvolvingmatricescanbeshortenedby50%
ifonethrowsthematricesout.”
13 Suppose \mathcal{A} is an n-by-n matrix and 1 \leq j,k \leq n. Show that the entry in
| rowj,columnk,of\mathcal{A}3 | (whichisdefinedtomean\mathcal{A}\mathcal{A}\mathcal{A})is |     |     |     |
| ----------------- | --------------------------- | --- | --- | --- |
n n
|     |     | \sum \sum\mathcal{A} \mathcal{A} \mathcal{A} | .   |     |
| --- | --- | -------- | --- | --- |
|     |     | j,p p,r  | r,k |     |
$$p=1r=1$$
14 Supposemandnarepositiveintegers. Provethatthefunction\mathcal{A}↦\mathcal{A}t isa
| linearmapfrom\mathbf{F}m,n | to\mathbf{F}n,m. |     |     |     |
| ----------------- | ------- | --- | --- | --- |

| --- | --- | --- | ------------------ | --- |
15 Provethatif\mathcal{A}isanm-by-nmatrixand\mathcal{C}isann-by-pmatrix,then
$$(\mathcal{A}\mathcal{C})t =\mathcal{C}t\mathcal{A}t.$$
Thisexerciseshowsthatthetransposeoftheproductoftwomatricesisthe
productofthetransposesintheoppositeorder.
| 16 Suppose\mathcal{A}isanm-by-nmatrixwith\mathcal{A} |     |     | \neq 0. Provethattherankof\mathcal{A}is1 |     |
| -------------------------------- | --- | --- | --------------------------- | --- |
ifandonlyifthereexist(c ,…,c ) \in \mathbf{F}m and(d ,…,d ) \in \mathbf{F}n suchthat
|           |                 | 1 m | 1 n     |     |
| --------- | --------------- | --- | ------- | --- |
|           | =1,…,mandeveryk |     | =1,…,n. |     |
| \mathcal{A} j,k =cd | foreveryj       |     |         |     |
j k
| 17 Suppose\mathcal{T} | \inℒ(\mathcal{V}),andu | ,…,u andv | ,…,v arebasesof\mathcal{V}. | Provethat |
| ----------- | ---------- | --------- | ----------------- | --------- |
|             |            | 1 n       | 1 n               |           |
thefollowingareequivalent.
| (a) \mathcal{T} isinjective. |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
Thecolumnsofℳ(\mathcal{T})arelinearlyindependentin\mathbf{F}n,1.
$$(b)$$
| (c) Thecolumnsofℳ(\mathcal{T})span\mathbf{F}n,1.                  |     |           |          |     |
| ---------------------------------------------- | --- | --------- | -------- | --- |
| (d) Therowsofℳ(\mathcal{T})span\mathbf{F}1,n.                     |     |           |          |     |
| (e) Therowsofℳ(\mathcal{T})arelinearlyindependentin\mathbf{F}1,n. |     |           |          |     |
| Hereℳ(\mathcal{T})meansℳ(\mathcal{T},(u                            |     | ,…,u ),(v | ,…,v )). |     |
|                                                |     | 1 n       | 1 n      |     |

82 Chapter 3 Linear Maps
### 3D Invertibility and Isomorphisms
Invertible Linear Maps
We begin this section by defining the notions of invertible and inverse in the
contextoflinearmaps.
**3.59 定义：** invertible,inverse
• Alinearmap\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})iscalledinvertibleifthereexistsalinearmap
\mathcal{S}\inℒ(\mathcal{W},\mathcal{V})suchthat\mathcal{S}\mathcal{T}equalstheidentityoperatoron\mathcal{V} and\mathcal{T}\mathcal{S}equals
theidentityoperatoron\mathcal{W}.
• A linear map \mathcal{S} \in ℒ(\mathcal{W},\mathcal{V}) satisfying \mathcal{S}\mathcal{T} = \mathcal{I} and \mathcal{T}\mathcal{S} = \mathcal{I} is called an
inverseof\mathcal{T}(notethatthefirst\mathcal{I}istheidentityoperatoron\mathcal{V}andthesecond
\mathcal{I} istheidentityoperatoron\mathcal{W}).
Thedefinitionabovementions“aninverse”. However,thenextresultshows
thatwecanchangethisterminologyto“theinverse”.
3.60 inverseisunique
Aninvertiblelinearmaphasauniqueinverse.
Proof Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})isinvertibleand\mathcal{S} and\mathcal{S} areinversesof\mathcal{T}. Then
1 2
\mathcal{S} =\mathcal{S} \mathcal{I} =\mathcal{S} (\mathcal{T}\mathcal{S} )=(\mathcal{S} \mathcal{T})\mathcal{S} =\mathcal{I}\mathcal{S} =\mathcal{S} .
1 1 1 2 1 2 2 2
Thus\mathcal{S} =\mathcal{S} .
1 2
Nowthatweknowthattheinverseisunique,wecangiveitanotation.
**3.61 记号：** \mathcal{T}-1
If \mathcal{T} is invertible, then its inverse is denoted by \mathcal{T}-1. In other words, if
\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})isinvertible,then\mathcal{T}-1 istheuniqueelementofℒ(\mathcal{W},\mathcal{V})such
that\mathcal{T}-1\mathcal{T} =\mathcal{I} and\mathcal{T}\mathcal{T}-1 =\mathcal{I}.
**3.62 例：** inverseofalinearmapfrom\mathbf{R}3 to\mathbf{R}3
Suppose \mathcal{T} \in ℒ(\mathbf{R}3) is defined by \mathcal{T}(x,y,z) = (-y,x,4z). Thus \mathcal{T} is a
counterclockwiserotationby90\circ inthexy-planeandastretchbyafactorof4in
thedirectionofthez-axis.
Hencetheinversemap\mathcal{T}-1 \inℒ(\mathbf{R}3)istheclockwiserotationby90\circ inthe
xy-planeandastretchbyafactorof 1 inthedirectionofthez-axis:
\mathcal{T}-1(x,y,z)=(y,-x,1z).

| --- | --- | --------- | ---------------------------- | --- | --- | --- |
Thenextresultshowsthatalinearmapisinvertibleifandonlyifitisone-tooneandonto.
| 3.63 | invertibility | ⟺ injectivityandsurjectivity |     |     |     |     |
| ---- | ------------- | ---------------------------- | --- | --- | --- | --- |
Alinearmapisinvertibleifandonlyifitisinjectiveandsurjective.
Proof Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Weneedtoshowthat\mathcal{T} isinvertibleifandonly
ifitisinjectiveandsurjective.
Firstsuppose\mathcal{T} isinvertible. Toshowthat\mathcal{T} isinjective,supposeu,v \in \mathcal{V}
| and\mathcal{T}u=\mathcal{T}v. | Then |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
$$u=\mathcal{T}-1(\mathcal{T}u)=\mathcal{T}-1(\mathcal{T}v)=v,$$
| sou=v. | Hence\mathcal{T} | isinjective. |     |     |     |     |
| ------ | ------ | ------------ | --- | --- | --- | --- |
We are still assuming that is invertible. Now we want to prove that is
|     |     | \mathcal{T}   |     |     |     | \mathcal{T}   |
| --- | --- | --- | --- | --- | --- | --- |
surjective. Todothis,letw \in \mathcal{W}. Thenw = \mathcal{T}(\mathcal{T}-1w),whichshowsthatwis
in the range of \mathcal{T}. Thus range\mathcal{T} \mathcal{W}. Hence is surjective, completing this
= \mathcal{T}
directionoftheproof.
Nowsuppose\mathcal{T}isinjectiveandsurjective. Wewanttoprovethat\mathcal{T}isinvertible.
Foreachw\in\mathcal{W},define\mathcal{S}(w)tobetheuniqueelementof\mathcal{V}suchthat\mathcal{T}(\mathcal{S}(w))=
w(theexistenceanduniquenessofsuchanelementfollowfromthesurjectivity
andinjectivityof\mathcal{T}). Thedefinitionof\mathcal{S}impliesthat\mathcal{T} \circ\mathcal{S}equalstheidentity
operatoron\mathcal{W}.
| Toprovethat\mathcal{S}\circ\mathcal{T} |     | equalstheidentityoperatoron\mathcal{V},letv\in\mathcal{V}. |     |     |     | Then |
| -------------- | --- | ------------------------------------ | --- | --- | --- | ---- |
\mathcal{T}((\mathcal{S}\circ\mathcal{T})v)=(\mathcal{T}\circ\mathcal{S})(\mathcal{T}v)=\mathcal{I}(\mathcal{T}v)=\mathcal{T}v.
Thisequationimpliesthat(\mathcal{S}\circ\mathcal{T})v=v(because\mathcal{T}isinjective). Thus\mathcal{S}\circ\mathcal{T}equals
theidentityoperatoron\mathcal{V}.
Tocompletetheproof,weneedtoshowthat\mathcal{S}islinear. Todothis,suppose
| w ,w | \in\mathcal{W}. Then |     |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- | --- |
1 2
|     | \mathcal{T}(\mathcal{S}(w | )+\mathcal{S}(w ))=\mathcal{T}(\mathcal{S}(w | ))+\mathcal{T}(\mathcal{S}(w | ))=w | +w  | .   |
| --- | ----- | -------------- | -------- | ---- | --- | --- |
|     |       | 1 2            | 1        | 2    | 1   | 2   |
Thus\mathcal{S}(w )+\mathcal{S}(w )istheuniqueelementof\mathcal{V} that\mathcal{T} mapstow +w . Bythe
|                                  | 1   | 2   |       |       |     | 1 2             |
| -------------------------------- | --- | --- | ----- | ----- | --- | --------------- |
|                                  |     |     | +w    | )+\mathcal{S}(w |     |                 |
| definitionof\mathcal{S},thisimpliesthat\mathcal{S}(w |     |     | )=\mathcal{S}(w |       | ).  | Hence\mathcal{S}satisfies |
|                                  |     |     | 1 2   | 1     | 2   |                 |
theadditivepropertyrequiredforlinearity.
Theproofofhomogeneityissimilar. Specifically,ifw\in\mathcal{W} and \lambda\in\mathbf{F},then
|     |     | \mathcal{T}(\lambda\mathcal{S}(w))= | \lambda\mathcal{T}(\mathcal{S}(w))= | \lambdaw. |     |     |
| --- | --- | --------- | --------- | --- | --- | --- |
Thus \lambda\mathcal{S}(w)istheuniqueelementof\mathcal{V} that\mathcal{T} mapsto \lambdaw. Bythedefinitionof
| \mathcal{S},thisimpliesthat\mathcal{S}(\lambdaw)= |     | \lambda\mathcal{S}(w). | Hence\mathcal{S}islinear,asdesired. |     |     |     |
| ----------------------- | --- | ------ | ------------------------- | --- | --- | --- |
For a linear map from a vector space to itself, you might wonder whether
injectivityalone,orsurjectivityalone,isenoughtoimplyinvertibility. Oninfinitedimensionalvectorspaces,neitherconditionaloneimpliesinvertibility,asillustratedbythenextexample,whichusestwofamiliarlinearmapsfrom Example3.3.

| --- | ------------------- | --- | --- | --- | --- | --- |
neitherinjectivitynorsurjectivityimpliesinvertibility
**3.64 例：** • Themultiplicationbyx2 linearmapfrom𝒫(\mathbf{R})to𝒫(\mathbf{R})(see3.3)isinjective
butitisnotinvertiblebecauseitisnotsurjective(thepolynomial1isnotin
therange).
| Thebackwardshiftlinearmapfrom\mathbf{F}\infty |     |     |     | to\mathbf{F}\infty                        |     |     |
| ------------------------------- | --- | --- | --- | --------------------------- | --- | --- |
| •                               |     |     |     | (see3.3)issurjectivebutitis |     |     |
notinvertiblebecauseitisnotinjective[thevector(1,0,0,0,…)isinthenull
space].
Inviewoftheexampleabove,thenextresultisremarkable—itstatesthatfor
alinearmapfromafinite-dimensionalvectorspacetoavectorspaceofthesame
dimension, either injectivity or surjectivity alone implies the other condition.
Notethatthehypothesisbelowthatdim\mathcal{V} =dim\mathcal{W} isautomaticallysatisfiedin
| theimportantspecialcasewhere\mathcal{V} |                                          |     | isfinite-dimensionaland\mathcal{W} |      |       | =\mathcal{V}. |
| ----------------------------- | ---------------------------------------- | --- | ------------------------ | ---- | ----- | --- |
|                               | injectivityisequivalenttosurjectivity(if |     |                          | dim\mathcal{V} | =dim\mathcal{W} | <\infty) |
3.65
Supposethat\mathcal{V} and\mathcal{W} arefinite-dimensionalvectorspaces,dim\mathcal{V} =dim\mathcal{W},
| and\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}).     | Then |             |     |               |     |
| ---- | ------------ | ---- | ----------- | --- | ------------- | --- |
|      | isinvertible |      | isinjective |     | issurjective. |     |
|      | \mathcal{T}            | ⟺    | \mathcal{T}           | ⟺   | \mathcal{T}             |     |
Proof Thefundamentaltheoremoflinearmaps(3.21)statesthat
dim\mathcal{V} =dimnull\mathcal{T}+dimrange\mathcal{T}.
3.66
If\mathcal{T} isinjective(whichby3.15isequivalenttotheconditiondimnull\mathcal{T} =0),
thentheequationaboveimpliesthat
|                   | dimrange\mathcal{T}                        | =dim\mathcal{V}-dimnull\mathcal{T}        |     | =dim\mathcal{V}      | =dim\mathcal{W}, |     |
| ----------------- | -------------------------------- | --------------------- | --- | ---------- | ------ | --- |
| whichimpliesthat\mathcal{T} |                                  | issurjective(by2.39). |     |            |        |     |
| Conversely,if\mathcal{T}    | issurjective,then3.66impliesthat |                       |     |            |        |     |
|                   | dimnull\mathcal{T}                         | =dim\mathcal{V}-dimrange\mathcal{T}       |     | =dim\mathcal{V}-dim\mathcal{W} |        | =0, |
| whichimpliesthat\mathcal{T} |                                  | isinjective.          |     |            |        |     |
Thuswehaveshownthat\mathcal{T} isinjectiveifandonlyif\mathcal{T} issurjective. Thusif
\mathcal{T} iseitherinjectiveorsurjective,then\mathcal{T} isbothinjectiveandsurjective,which
impliesthat\mathcal{T} isinvertible. Hence\mathcal{T} isinvertibleifandonlyif\mathcal{T} isinjectiveif
| andonlyif\mathcal{T} | issurjective. |     |     |     |     |     |
| ---------- | ------------- | --- | --- | --- | --- | --- |
Thenextexampleillustratesthepowerofthepreviousresult. Althoughitis
possibletoprovetheresultintheexamplebelowwithoutusinglinearalgebra,the
proofusinglinearalgebraiscleanerandeasier.

| --- | --- | --------- | --- | ---------------------------- |
$$((x2+5x+7)p)″$$
**3.67 例：** thereexistsapolynomialpsuchthat =q
Thelinearmap
p↦((x2+5x+7)p)″
from𝒫(\mathbf{R})toitselfisinjective,asyoucanshow. Thuswearetemptedtouse3.65
toshowthatthismapissurjective. However,Example3.64showsthatthemagic
of3.65doesnotapplytotheinfinite-dimensionalvectorspace𝒫(\mathbf{R}). Wewill
getaroundthisproblembyrestrictingattentiontothefinite-dimensionalvector
space𝒫 (\mathbf{R}).
m
Supposeq\in𝒫(\mathbf{R}). Thereexistsanonnegativeintegermsuchthatq\in𝒫 (\mathbf{R}).
m
| Define\mathcal{T}∶ 𝒫 | (\mathbf{R})\rightarrow𝒫 | (\mathbf{R})by |     |     |
| ---------- | ----- | ----- | --- | --- |
m m
\mathcal{T}p=((x2+5x+7)p)″.
Multiplyinganonzeropolynomialby(x2+5x+7)increasesthedegreeby2,and
thendifferentiatingtwicereducesthedegreeby2. Thus\mathcal{T} isindeedalinearmap
from𝒫 (\mathbf{R})toitself.
m
Every polynomial whose second derivative equals 0 is of the form ax +b,
| wherea,b\in\mathbf{R}. | Thusnull\mathcal{T} | ={0}. | Hence\mathcal{T} | isinjective. |
| ----------- | --------- | ----- | ------ | ------------ |
Thus \mathcal{T} issurjective(by3.65), whichmeans thatthereexistsapolynomial
p\in𝒫 (\mathbf{R})suchthat((x2+5x+7)p)″ =q,asclaimedinthetitleofthisexample.
m
Exercise35in Section6Agivesasimilarbutmorespectacularexampleof
using3.65.
Thehypothesisintheresultbelowthatdim\mathcal{V} =dim\mathcal{W}holdsintheimportant
specialcaseinwhich\mathcal{V} isfinite-dimensionaland\mathcal{W} =\mathcal{V}. Thusinthatcase,the
equation\mathcal{S}\mathcal{T} =\mathcal{I}impliesthat\mathcal{S}\mathcal{T} =\mathcal{T}\mathcal{S},eventhoughwedonothavemultiplicative
| commutativityofarbitrarylinearmapsfrom\mathcal{V} |      |                                         |     | to\mathcal{V}. |
| --------------------------------------- | ---- | --------------------------------------- | --- | ---- |
| 3.68 \mathcal{S}\mathcal{T}                                 | =\mathcal{I} ⟺ | \mathcal{T}\mathcal{S}=\mathcal{I} (onvectorspacesofthesamedimension) |     |      |
Suppose\mathcal{V}and\mathcal{W}arefinite-dimensionalvectorspacesofthesamedimension,
| \mathcal{S}\inℒ(\mathcal{W},\mathcal{V}),and\mathcal{T}        |     | \inℒ(\mathcal{V},\mathcal{W}).  | Then\mathcal{S}\mathcal{T}       | =\mathcal{I} ifandonlyif\mathcal{T}\mathcal{S}=\mathcal{I}. |
| -------------------- | --- | --------- | ------------ | ------------------- |
| Proof Firstsuppose\mathcal{S}\mathcal{T} |     | =\mathcal{I}. Ifv\in\mathcal{V} | and\mathcal{T}v=0,then |                     |
$$v=\mathcal{I}v=(\mathcal{S}\mathcal{T})v=\mathcal{S}(\mathcal{T}v)=\mathcal{S}(0)=0.$$
Thus\mathcal{T} isinjective(by3.15). Because\mathcal{V} and\mathcal{W} havethesamedimension,this
| impliesthat\mathcal{T} | isinvertible(by3.65). |     |     |     |
| ------------ | --------------------- | --- | --- | --- |
Nowmultiplybothsidesoftheequation\mathcal{S}\mathcal{T} =\mathcal{I} by\mathcal{T}-1 ontheright,getting
\mathcal{S}=\mathcal{T}-1.
| Thus\mathcal{T}\mathcal{S}=\mathcal{T}\mathcal{T}-1 | =\mathcal{I},asdesired. |     |     |     |
| ----------- | ------------- | --- | --- | --- |
Toprovetheimplicationintheotherdirection,simplyreversetherolesof\mathcal{S}
and\mathcal{T} (and\mathcal{V} and\mathcal{W})inthedirectionwehavealreadyproved,showingthatif
| \mathcal{T}\mathcal{S}=\mathcal{I},then\mathcal{S}\mathcal{T} | =\mathcal{I}. |     |     |     |
| ----------- | --- | --- | --- | --- |

| -------- | ---------- | --- | --- | --- |
| Isomorphic | Vector Spaces |     |     |     |
| ---------- | ------------- | --- | --- | --- |
Thenextdefinitioncapturestheideaoftwovectorspacesthatareessentiallythe
same,exceptforthenamesoftheirelements.
| 3.69 definition: | isomorphism,isomorphic |     |     |     |
| ---------------- | ---------------------- | --- | --- | --- |
• Anisomorphismisaninvertiblelinearmap.
• Twovectorspacesarecalledisomorphicifthereisanisomorphismfrom
onevectorspaceontotheotherone.
| Thinkofanisomorphism\mathcal{T}∶ |     | \mathcal{V} \rightarrow\mathcal{W} asrelabelingv | \in\mathcal{V} as\mathcal{T}v \in\mathcal{W}. | This |
| ---------------------- | --- | ------------------ | ----------- | ---- |
viewpointexplainswhytwoisomorphicvectorspaceshavethesamevectorspace
properties. Theterms“isomorphism”and“invertiblelinearmap”meanthesame
thing. Use“isomorphism”whenyouwanttoemphasizethatthetwospacesare
essentiallythesame.
Itcanbedifficulttodeterminewhethertwomathematicalstructures(suchas
groupsortopologicalspaces)areessentiallythesame,differingonlyinthenames
oftheelementsofunderlyingsets. However,thenextresultshowsthatweneed
tolookatonlyasinglenumber(thedimension)todeterminewhethertwovector
spacesareisomorphic.
3.70 dimensionshowswhethervectorspacesareisomorphic
Twofinite-dimensionalvectorspacesover\mathbf{F}areisomorphicifandonlyifthey
havethesamedimension.
Proof Firstsuppose\mathcal{V} and\mathcal{W} areisomorphicfinite-dimensionalvectorspaces.
Thusthereexistsanisomorphism\mathcal{T} from\mathcal{V} onto\mathcal{W}. Because\mathcal{T} isinvertible,we
| havenull\mathcal{T} ={0}andrange\mathcal{T} |             | =\mathcal{W}. Thus      |        |     |
| ----------------------- | ----------- | ------------- | ------ | --- |
|                         | dimnull\mathcal{T} =0 | and dimrange\mathcal{T} | =dim\mathcal{W}. |     |
Theformula
=dimnull\mathcal{T}+dimrange\mathcal{T}
dim\mathcal{V}
$$(thefundamentaltheoremoflinearmaps,whichis3.21)thusbecomestheequation$$
dim\mathcal{V} =dim\mathcal{W},completingtheproofinonedirection.
Toprovetheotherdirection,suppose\mathcal{V} and\mathcal{W} arefinite-dimensionalvector
spacesofthesamedimension. Letv ,…,v beabasisof\mathcal{V} andw ,…,w bea
|                |                    | 1 n          | 1   | n   |
| -------------- | ------------------ | ------------ | --- | --- |
| basisof\mathcal{W}. Let\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W})bedefinedby |              |     |     |
|                | \mathcal{T}(c v +⋯+c         | v )=c w +⋯+c | w . |     |
|                | 1 1                | n n 1 1      | n n |     |
Then\mathcal{T} isawell-definedlinearmapbecausev ,…,v isabasisof\mathcal{V}. Also,\mathcal{T}
1 n
is surjective because w ,…,w spans \mathcal{W}. Furthermore, null\mathcal{T} = {0} because
|     | 1   | n   |     |     |
| --- | --- | --- | --- | --- |
w ,…,w islinearlyindependent. Thus\mathcal{T}isinjective. Because\mathcal{T}isinjectiveand
1 n
surjective,itisanisomorphism(see3.63). Hence\mathcal{V} and\mathcal{W} areisomorphic.

| --- | --- | --- | --------- | ---------------------------- | --- | --- | --- | --- |
Thepreviousresultimpliesthateach
Everyfinite-dimensionalvectorspace
| finite-dimensionalvectorspace\mathcal{V} |     |     | isiso- |     |     |     |     |     |
| ------------------------------ | --- | --- | ------ | --- | --- | --- | --- | --- |
isisomorphictosome\mathbf{F}n.Thuswhynot
\mathbf{F}n,
morphic to where n = dim\mathcal{V}. For juststudy\mathbf{F}n insteadofmoregeneral
| example, | if m is | a nonnegative | integer, |        |         |           |      |       |
| -------- | ------- | ------------- | -------- | ------ | ------- | --------- | ---- | ----- |
|          |         |               |          | vector | spaces? | To answer | this | ques- |
$$(\mathbf{F})isisomorphicto\mathbf{F}m+1.$$
| then𝒫 |     |     |     | tion,notethataninvestigationof |     |     |     | \mathbf{F}n  |
| ----- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
m
Recallthatthenotation\mathbf{F}m,n denotes wouldsoonleadtoothervectorspaces.
thevectorspaceofm-by-nmatriceswith Forexample,wewouldencounterthe
entriesin\mathbf{F}. Ifv ,…,v isabasisof\mathcal{V} nullspaceandrangeoflinearmaps.
|     |     | 1 n |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
andw ,…,w isabasisof\mathcal{W},thenfor Althougheachofthesevectorspaces
| 1   | m   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
each \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}), we have a matrix isisomorphictosome\mathbf{F}m,thinkingof
|            | \mathbf{F}m,n. |           |            | themthatwayoftenaddscomplexity |     |     |     |     |
| ---------- | ----- | --------- | ---------- | ------------------------------ | --- | --- | --- | --- |
| ℳ(\mathcal{T})       | \in     | Thus once | bases have |                                |     |     |     |     |
| been fixed | for \mathcal{V} | and \mathcal{W},    | ℳ becomes  | a butnonewinsight.             |     |     |     |     |
\mathbf{F}m,n.
| function | from ℒ(\mathcal{V},\mathcal{W}) |     | to Notice |     |     |     |     |     |
| -------- | ----------- | --- | --------- | --- | --- | --- | --- | --- |
that3.35and3.38showthatℳisalin-
| earmap. | Thislinearmapisactuallyan |     |     |     |     |     |     |     |
| ------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
isomorphism,aswenowshow.
| 3.71     | ℒ(\mathcal{V},\mathcal{W})and | \mathbf{F}m,n        | areisomorphic |      |              |     |         |     |
| -------- | --------- | ----------- | ------------- | ---- | ------------ | --- | ------- | --- |
|          | ,…,v      |             |               | ,…,w |              |     | Thenℳis |     |
| Supposev |           | isabasisof\mathcal{V} | andw          |      | isabasisof\mathcal{W}. |     |         |     |
|          | 1         | n           |               | 1    | m            |     |         |     |
anisomorphismbetweenℒ(\mathcal{V},\mathcal{W})and\mathbf{F}m,n.
Proof Wealreadynotedthatℳislinear. Weneedtoprovethatℳisinjective
andsurjective.
| Webeginwithinjectivity. |     |     | If\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})andℳ(\mathcal{T})=0,then\mathcal{T}v |     |     |     |     | =0for |
| ----------------------- | --- | --- | --------------------------- | --- | --- | --- | --- | ----- |
k
eachk =1,…,n. Becausev ,…,v isabasisof\mathcal{V},thisimplies\mathcal{T} =0. Thusℳ
|     |     |     | 1 n |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
isinjective(by3.15).
Toprovethatℳissurjective,suppose\mathcal{A} \in \mathbf{F}m,n. Bythelinearmaplemma
| (3.4),thereexists\mathcal{T} |     | \inℒ(\mathcal{V},\mathcal{W})suchthat |     |     |     |     |     |     |
| ------------------ | --- | --------------- | --- | --- | --- | --- | --- | --- |
m
|     |     |     | \mathcal{T}v = | \sum\mathcal{A} j,k w |     |     |     |     |
| --- | --- | --- | ---- | -------- | --- | --- | --- | --- |
|     |     |     | k    |          | j   |     |     |     |
$$j=1$$
Becauseℳ(\mathcal{T})equals\mathcal{A},therangeofℳequals\mathbf{F}m,n,as
| foreachk | = 1,…,n. |     |     |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
desired.
Nowwecandeterminethedimensionofthevectorspaceoflinearmapsfrom
onefinite-dimensionalvectorspacetoanother.
dimℒ(\mathcal{V},\mathcal{W})=(dim\mathcal{V})(dim\mathcal{W})
3.72
Thenℒ(\mathcal{V},\mathcal{W})isfinite-dimensional
Suppose\mathcal{V}and\mathcal{W}arefinite-dimensional.
and
dimℒ(\mathcal{V},\mathcal{W})=(dim\mathcal{V})(dim\mathcal{W}).
Proof Thedesiredresultfollowsfrom3.71,3.70,and3.40.

| -------- | ---------- | --- | --- | --- |
| Linear Maps | Thought | of as Matrix | Multiplication |     |
| ----------- | ------- | ------------ | -------------- | --- |
Previouslywedefinedthematrixofalinearmap. Nowwedefinethematrixofa
vector.
| 3.73 definition: | matrixofavector,ℳ(v) |              |             |                |
| ---------------- | -------------------- | ------------ | ----------- | -------------- |
| Supposev\in\mathcal{V}       | andv ,…,v            | isabasisof\mathcal{V}. | Thematrixof | vwithrespectto |
|                  | 1                    | n            |             |                |
thisbasisisthen-by-1matrix
b
⎛ 1 ⎞
|     |     | ℳ(v)=⎜ | ⎜ ⎟ ⎟ , |     |
| --- | --- | ------ | ------- | --- |
⎜ ⋮ ⎟
⎝ b ⎠
n
| whereb ,…,b             | arethescalarssuchthat |       |                      |             |
| ----------------------- | --------------------- | ----- | -------------------- | ----------- |
| 1                       | n                     |       |                      |             |
|                         |                       | v=b v | +⋯+b v .             |             |
|                         |                       | 1 1   | n n                  |             |
| Thematrixℳ(v)ofavectorv |                       | \in     | \mathcal{V} dependsonthebasisv | ,…,v of\mathcal{V},as |
1 n
wellasonv. However,thebasisshouldbeclearfromthecontextandthusitis
notincludedinthenotation.
matrixofavector
**3.74 例：** • Thematrixofthepolynomial2-7x+5x3+x4 withrespecttothestandard
| basisof𝒫 | (\mathbf{R})is |     |     |     |
| -------- | ----- | --- | --- | --- |
|     |     | ⎛   | ⎞      |     |
| --- | --- | --- | ------ | --- |
|     |     | ⎜   | ⎟      |     |
|     |     | ⎜ ⎜ | -7 ⎟ ⎟ |     |
|     |     | ⎜   | ⎟      |     |
|     |     | ⎜ ⎜ | 0 ⎟ ⎟. |     |
|     |     | ⎜   | ⎟      |     |
|     |     | ⎜ ⎜ | ⎟ ⎟    |     |
|     |     | ⎜   | 5 ⎟    |     |
|     |     | ⎝   | 1 ⎠    |     |
\in\mathbf{F}n
• Thematrixofavectorx withrespecttothestandardbasisisobtainedby
writingthecoordinatesofxastheentriesinann-by-1matrix. Inotherwords,
,…,x )\in\mathbf{F}n,then
ifx =(x
1 n
x
⎛ 1 ⎞
|     |     | ℳ(x)=⎜ | ⎜ ⋮ ⎟ ⎟ ⎟. |     |
| --- | --- | ------ | ---------- | --- |
⎜
⎝ x ⎠
n
Occasionally we want to think of elements of \mathcal{V} as relabeled to be n-by-1
matrices. Onceabasisv ,…,v ischosen,thefunctionℳthattakesv \in\mathcal{V} to
|     | 1   | n   |     |     |
| --- | --- | --- | --- | --- |
onto\mathbf{F}n,1
| ℳ(v)isanisomorphismof\mathcal{V} |     |     | thatimplementsthisrelabeling. |     |
| ---------------------- | --- | --- | ----------------------------- | --- |
Recallthatif\mathcal{A}isanm-by-nmatrix, then\mathcal{A} denotesthekth columnof\mathcal{A},
\cdot,k
thought of as an m-by-1 matrix. In the next result, ℳ(\mathcal{T}v ) is computed with
k
| respecttothebasisw | ,…,w | of\mathcal{W}. |     |     |
| ------------------ | ---- | ---- | --- | --- |
|                    | 1    | m    |     |     |

| --- | --- | --- | --------- | ---------------------------- | --- | --- | --- |
| ℳ(\mathcal{T})     | =ℳ(\mathcal{T}v       |     |      |             |     |           |          |
| -------- | ----------- | --- | ---- | ----------- | --- | --------- | -------- |
| 3.75     | \cdot,k         | k   | )    |             |     |           |          |
| Suppose\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W})andv |     | ,…,v | isabasisof\mathcal{V} |     | andw ,…,w | isabasis |
|          |             |     | 1    | n           |     | 1         | m        |
Thenthekth
| of\mathcal{W}. Let1 | \leq k         | \leq n. |     | columnofℳ(\mathcal{T}), |     | whichisdenotedby |     |
| --------- | ----------- | ---- | --- | ------------- | --- | ---------------- | --- |
| ℳ(\mathcal{T})      | ,equalsℳ(\mathcal{T}v | ).   |     |               |     |                  |     |
| \cdot,k       |             | k    |     |               |     |                  |     |
Proof Thedesiredresultfollowsimmediatelyfromthedefinitionsofℳ(\mathcal{T})and
ℳ(\mathcal{T}v ).
k
Thenextresultshowshowthenotionsofthematrixofalinearmap,thematrix
ofavector,andmatrixmultiplicationfittogether.
3.76 linearmapsactlikematrixmultiplication
Suppose \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}) and v \in \mathcal{V}. Suppose v ,…,v is a basis of \mathcal{V} and
1 n
,…,w
| w   | isabasisof\mathcal{W}. |     | Then |     |     |     |     |
| --- | ------------ | --- | ---- | --- | --- | --- | --- |
| 1   | m            |     |      |     |     |     |     |
ℳ(\mathcal{T}v)=ℳ(\mathcal{T})ℳ(v).
|                  |     | +⋯+b  |      |               | ,…,b |            |     |
| ---------------- | --- | ----- | ---- | ------------- | ---- | ---------- | --- |
| Proof Supposev=b |     | 1 v 1 |      | n v n ,whereb | 1    | n \in\mathbf{F}. Thus |     |
|                  |     |       | \mathcal{T}v=b | \mathcal{T}v +⋯+b       | \mathcal{T}v   | .          |     |
| 3.77             |     |       |      | 1 1           | n    | n          |     |
Hence
|     |     | ℳ(\mathcal{T}v)=b | ℳ(\mathcal{T}v    | )+⋯+b |     | ℳ(\mathcal{T}v ) |     |
| --- | --- | ------- | ------- | ----- | --- | ------ | --- |
|     |     |         | 1       | 1     |     | n n    |     |
|     |     |         | =b ℳ(\mathcal{T}) | +⋯+b  |     | ℳ(\mathcal{T})   |     |
|     |     |         | 1       | \cdot,1   |     | n \cdot,n  |     |
=ℳ(\mathcal{T})ℳ(v),
where the first equality follows from 3.77 and the linearity of ℳ, the second
equalitycomesfrom3.75,andthelastequalitycomesfrom3.50.
|             |        |     |         |          |     | \mathbf{F}n,1 \mathbf{F}m,1, |            |
| ----------- | ------ | --- | ------- | -------- | --- | ---------- | ---------- |
| Each m-by-n | matrix | \mathcal{A}   | induces | a linear | map | from to    | namely the |
matrixmultiplicationfunctionthattakesx \in\mathbf{F}n,1 to\mathcal{A}x \in\mathbf{F}m,1. Theresultabove
canbeusedtothinkofeverylinearmap(fromafinite-dimensionalvectorspace
toanotherfinite-dimensionalvectorspace)asamatrixmultiplicationmapafter
| suitablerelabelingviatheisomorphismsgivenbyℳ. |     |     |     |     |     |     | \inℒ(\mathcal{V},\mathcal{W}) |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- |
Specifically,if\mathcal{T}
andweidentifyv\in\mathcal{V} withℳ(v)\in\mathbf{F}n,1,thentheresultabovesaysthatwecan
identify\mathcal{T}vwithℳ(\mathcal{T})ℳ(v).
Becausetheresultaboveallowsustothink(viaisomorphisms)ofeachlinear
mapasmultiplicationon\mathbf{F}n,1
bysomematrix\mathcal{A},keepinmindthatthespecific
matrix\mathcal{A}dependsnotonlyonthelinearmapbutalsoonthechoiceofbases. One
ofthethemesofmanyofthemostimportantresultsinlaterchapterswillbethe
choiceofabasisthatmakesthematrix\mathcal{A}assimpleaspossible.
Inthisbook,weconcentrateonlinearmapsratherthanonmatrices. However,
sometimesthinkingoflinearmapsasmatrices(orthinkingofmatricesaslinear
maps)givesimportantinsightsthatwewillfinduseful.

| -------- | --- | ---------- | --- | --- | --- | --- | --- |
Noticethatnobasesareinsightinthestatementofthenextresult. Although
ℳ(\mathcal{T})inthenextresultdependsonachoiceofbasesof\mathcal{V} and\mathcal{W},thenextresult
showsthatthecolumnrankofℳ(\mathcal{T})isthesameforallsuchchoices(because
range\mathcal{T} doesnotdependonachoiceofbasis).
| 3.78 dimensionof                      |     | range\mathcal{T} | equalscolumnrankof |     |          | ℳ(\mathcal{T}) |               |
| ------------------------------------- | --- | ------ | ------------------ | --- | -------- | ---- | ------------- |
| Suppose\mathcal{V}and\mathcal{W}arefinite-dimensionaland\mathcal{T} |     |        |                    |     | \inℒ(\mathcal{V},\mathcal{W}). |      | Thendimrange\mathcal{T} |
equalsthecolumnrankofℳ(\mathcal{T}).
Proof Supposev ,…,v isabasisof\mathcal{V}andw ,…,w isabasisof\mathcal{W}. Thelinear
|                 |     | 1 n                        |     |     | 1   | m   |                  |
| --------------- | --- | -------------------------- | --- | --- | --- | --- | ---------------- |
| mapthattakesw\in\mathcal{W} |     | toℳ(w)isanisomorphismfrom\mathcal{W} |     |     |     |     | ontothespace\mathbf{F}m,1 |
ofm-by-1columnvectors. Therestrictionofthisisomorphismtorange\mathcal{T} [which
equalsspan(\mathcal{T}v ,…,\mathcal{T}v )by Exercise10in Section3B]isanisomorphismfrom
|     | 1   | n   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
range\mathcal{T} onto span(ℳ(\mathcal{T}v ),…,ℳ(\mathcal{T}v )). For each k \in {1,…,n}, the m-by-1
|            |                       |     | 1   | n   |      |     |     |
| ---------- | --------------------- | --- | --- | --- | ---- | --- | --- |
| matrixℳ(\mathcal{T}v | )equalscolumnkofℳ(\mathcal{T}). |     |     |     | Thus |     |     |
k
|     |     | dimrange\mathcal{T} | = thecolumnrankofℳ(\mathcal{T}), |     |     |     |     |
| --- | --- | --------- | ---------------------- | --- | --- | --- | --- |
asdesired.
| Change | of Basis |     |     |     |     |     |     |
| ------ | -------- | --- | --- | --- | --- | --- | --- |
In Section3Cwedefinedthematrix
|     |     | ℳ(\mathcal{T},(v | ,…,v | ),(w | ,…,w | ))  |     |
| --- | --- | ------ | ---- | ---- | ---- | --- | --- |
|     |     |        | 1    | n    | 1    | m   |     |
ofalinearmap\mathcal{T} from\mathcal{V} toapossiblydifferentvectorspace\mathcal{W},wherev ,…,v
1 n
,…,w
isabasisof\mathcal{V}andw 1 m isabasisof\mathcal{W}. Forlinearmapsfromavectorspace
toitself,weusuallyusethesamebasisforboththedomainvectorspaceandthe
targetvectorspace. Whenusingasinglebasisinbothcapacities,weoftenwrite
thebasisonlyonce. Inotherwords,if\mathcal{T} \in ℒ(\mathcal{V})andv ,…,v isabasisof\mathcal{V},
|                       |     |     |      |     |     |     | 1 n |
| --------------------- | --- | --- | ---- | --- | --- | --- | --- |
| thenthenotationℳ(\mathcal{T},(v |     |     | ,…,v |     |     |     |     |
$$))isdefinedbytheequation$$
|     |        |      | 1 n       |     |      |      |          |
| --- | ------ | ---- | --------- | --- | ---- | ---- | -------- |
|     | ℳ(\mathcal{T},(v | ,…,v | ))=ℳ(\mathcal{T},(v |     | ,…,v | ),(v | ,…,v )). |
|     |        | 1    | n         |     | 1    | n    | 1 n      |
Ifthebasisv ,…,v isclearfromthecontext,thenwecanwritejustℳ(\mathcal{T}).
1 n
| 3.79 definition:            |     | identitymatrix,I |                 |     |     |     |     |
| --------------------------- | --- | ---------------- | --------------- | --- | --- | --- | --- |
| Supposenisapositiveinteger. |     |                  | Then-by-nmatrix |     |     |     |     |
|                             |     |                  | ⎛               |     | ⎞   |     |     |
|                             |     |                  | ⎜               |     | ⎟   |     |     |
|                             |     |                  | ⎜ ⎜             | ⋱   | ⎟ ⎟ |     |     |
|                             |     |                  | ⎝               |     | ⎠   |     |     |
with1’sonthediagonal(theentrieswheretherownumberequalsthecolumn
number)and0’selsewhereiscalledtheidentitymatrixandisdenotedby\mathcal{I}.

| --- | --- | --- | --------- | --- | ---------------------------- | --- | --- | --- |
Inthedefinitionabove,the0inthelowerleftcornerofthematrixindicatesthat
allentriesbelowthediagonalare0,andthe0intheupperrightcornerindicates
thatallentriesabovethediagonalare0.
Withrespecttoeachbasisof\mathcal{V},thematrixoftheidentityoperator\mathcal{I} \inℒ(\mathcal{V})
istheidentitymatrix\mathcal{I}. Notethatthesymbol\mathcal{I} isusedtodenoteboththeidentity
operatorandtheidentitymatrix. Thecontextindicateswhichmeaningof\mathcal{I} is
intended. Forexample,considertheequationℳ(\mathcal{I})=\mathcal{I};ontheleftside\mathcal{I}denotes
theidentityoperator,andontherightside\mathcal{I} denotestheidentitymatrix.
If\mathcal{A}isasquarematrix(meaningithasthesamenumberofrowsascolumns)
| withthesamesizeas\mathcal{I},then\mathcal{A}\mathcal{I} |     |     |     | =\mathcal{I}\mathcal{A}=\mathcal{A},asyoushouldverify. |     |     |     |     |
| ------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
invertible,inverse,\mathcal{A}-1
**3.80 定义：** Asquarematrix\mathcal{A}iscalledinvertibleifthereisasquarematrix\mathcal{B}ofthesame
sizesuchthat\mathcal{A}\mathcal{B}=\mathcal{B}\mathcal{A}=\mathcal{I};wecall\mathcal{B}theinverseof\mathcal{A}anddenoteitby\mathcal{A}-1.
Thesameproofasusedin3.60shows
|         |         |            |        |         | Some        | mathematicians | use           | the terms |
| ------- | ------- | ---------- | ------ | ------- | ----------- | -------------- | ------------- | --------- |
| that if | \mathcal{A} is an | invertible | square | matrix, |             |                |               |           |
|         |         |            |        |         | nonsingular |                | and singular, | which     |
thenthereisauniquematrix\mathcal{B}suchthat
meanthesameasinvertibleandnon-
|      |      | (and thus | the | notation |             |     |     |     |
| ---- | ---- | --------- | --- | -------- | ----------- | --- | --- | --- |
| \mathcal{A}\mathcal{B} = | \mathcal{B}\mathcal{A} = | \mathcal{I}         |     |          | invertible. |     |     |     |
\mathcal{B}=\mathcal{A}-1 isjustified).
-1
| If\mathcal{A}isaninvertiblematrix,then(\mathcal{A}-1) |     |     |           |     | =\mathcal{A}because |     |     |     |
| --------------------------------- | --- | --- | --------- | --- | --------- | --- | --- | --- |
|                                   |     |     | \mathcal{A}-1\mathcal{A}=\mathcal{A}\mathcal{A}-1 |     | =\mathcal{I}.       |     |     |     |
Also, if \mathcal{A} and \mathcal{C} are invertible square matrices of the same size, then \mathcal{A}\mathcal{C} is
| invertibleand(\mathcal{A}\mathcal{C})-1 |     | =\mathcal{C}-1\mathcal{A}-1 |     |     |     |     |     |     |
| ------------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
because
$$(\mathcal{A}\mathcal{C})(\mathcal{C}-1\mathcal{A}-1)=\mathcal{A}(\mathcal{C}\mathcal{C}-1)\mathcal{A}-1$$
=\mathcal{A}\mathcal{I}\mathcal{A}-1
=\mathcal{A}\mathcal{A}-1
=\mathcal{I},
andsimilarly(\mathcal{C}-1\mathcal{A}-1)(\mathcal{A}\mathcal{C})=\mathcal{I}.
The next result holds because we defined matrix multiplication to make it
true—see3.43andthematerialprecedingit. Nowwearejustbeingmoreexplicit
aboutthebasesinvolved.
3.81 matrixofproductoflinearmaps
Suppose \mathcal{T} \in ℒ(\mathcal{U},\mathcal{V}) and \mathcal{S} \in ℒ(\mathcal{V},\mathcal{W}). If u ,…,u is a basis of \mathcal{U},
|         |                  |      |           |      |                  | 1    | m         |       |
| ------- | ---------------- | ---- | --------- | ---- | ---------------- | ---- | --------- | ----- |
| ,…,v    |                  |      |           | ,…,w |                  |      |           |       |
| v       | isabasisof\mathcal{V},andw |      |           |      | isabasisof\mathcal{W},then |      |           |       |
| 1       | n                |      |           | 1    | p                |      |           |       |
| ℳ(\mathcal{S}\mathcal{T},(u |                  | ,…,u | ),(w ,…,w | ))=  |                  |      |           |       |
|         | 1                | m    | 1         | p    |                  |      |           |       |
|         | ℳ(\mathcal{S},(v           | ,…,v | ),(w      | ,…,w | ))ℳ(\mathcal{T},(u         | ,…,u | ),(v ,…,v |       |
|         |                  | 1    | n         | 1    | p                | 1    | m 1       | n )). |

92 Chapter 3 Linear Maps
Thenextresultdealswiththematrixoftheidentityoperator\mathcal{I} withrespectto
twodifferentbases. Notethatthekth columnofℳ(\mathcal{I},(u ,…,u ),(v ,…,v ))
1 n 1 n
consists of the scalars needed to write u as a linear combination of the basis
k
v ,…,v .
1 n
Inthestatementofthenextresult,\mathcal{I} denotestheidentityoperatorfrom\mathcal{V} to\mathcal{V}.
Intheproof,\mathcal{I} alsodenotesthen-by-nidentitymatrix.
3.82 matrixofidentityoperatorwithrespecttotwobases
Supposethatu ,…,u andv ,…,v arebasesof\mathcal{V}. Thenthematrices
1 n 1 n
ℳ(\mathcal{I},(u ,…,u ),(v ,…,v )) and ℳ(\mathcal{I},(v ,…,v ),(u ,…,u ))
1 n 1 n 1 n 1 n
areinvertible,andeachistheinverseoftheother.
Proof In3.81,replacew withu ,andreplace\mathcal{S}and\mathcal{T} with\mathcal{I},getting
k k
\mathcal{I} =ℳ(\mathcal{I},(v ,…,v ),(u ,…,u ))ℳ(\mathcal{I},(u ,…,u ),(v ,…,v )).
1 n 1 n 1 n 1 n
Nowinterchangetherolesoftheu’sandv’s,getting
\mathcal{I} =ℳ(\mathcal{I},(u ,…,u ),(v ,…,v ))ℳ(\mathcal{I},(v ,…,v ),(u ,…,u )).
1 n 1 n 1 n 1 n
Thesetwoequationsabovegivethedesiredresult.
**3.83 例：** matrixofidentityoperatoron\mathbf{F}2 withrespecttotwobases
Consider the bases (4,2),(5,3) and (1,0),(0,1) of \mathbf{F}2. Because \mathcal{I}(4,2) =
4(1,0)+2(0,1)and\mathcal{I}(5,3)=5(1,0)+3(0,1),wehave
4 5
ℳ(\mathcal{I},((4,2),(5,3)),((1,0),(0,1)))=( ).
2 3
Theinverseofthematrixaboveis
3 -5
⎛ ⎜ 2 2 ⎞ ⎟,
⎝ -1 2 ⎠
asyoushouldverify. Thus3.82impliesthat
3 -5
ℳ(\mathcal{I},((1,0),(0,1)),((4,2),(5,3)))= ⎛ ⎜ 2 2 ⎞ ⎟.
⎝ -1 2 ⎠
Ournextresultshowshowthematrixof\mathcal{T} changeswhenwechangebases. In
thenextresult,wehavetwodifferentbasesof\mathcal{V},eachofwhichisusedasabasisfor
thedomainspaceandasabasisforthetargetspace. Recallourshorthandnotation
thatallowsustodisplayabasisonlyoncewhenitisusedinbothcapacities:
ℳ(\mathcal{T},(u ,…,u ))=ℳ(\mathcal{T},(u ,…,u ),(u ,…,u )).
1 n 1 n 1 n

| --- | --- | --- | --------- | --- | ---------------------------- | --- | --- | --- |
change-of-basisformula
3.84
| Suppose\mathcal{T} | \inℒ(\mathcal{V}).   |      | Supposeu | ,…,u | andv         | ,…,v | arebasesof\mathcal{V}. | Let |
| -------- | -------- | ---- | -------- | ---- | ------------ | ---- | ------------ | --- |
|          |          |      |          | 1    | n            | 1    | n            |     |
|          | \mathcal{A}=ℳ(\mathcal{T},(u |      | ,…,u     | ))   | and \mathcal{B}=ℳ(\mathcal{T},(v |      | ,…,v ))      |     |
|          |          |      | 1        | n    |              |      | 1 n          |     |
| and\mathcal{C}     | =ℳ(\mathcal{I},(u  | ,…,u | ),(v     | ,…,v | )). Then     |      |              |     |
|          |          | 1    | n        | 1    | n            |      |              |     |
\mathcal{A}=\mathcal{C}-1\mathcal{B}\mathcal{C}.
| Proof | In3.81,replacew |             | withu | andreplace\mathcal{S}with\mathcal{I},getting |           |      |     |     |
| ----- | --------------- | ----------- | ----- | ------------------------ | --------- | ---- | --- | --- |
|       |                 |             | k     | k                        |           |      |     |     |
| 3.85  |                 | \mathcal{A}=\mathcal{C}-1ℳ(\mathcal{T},(u |       |                          | ,…,u ),(v | ,…,v | )), |     |
|       |                 |             |       |                          | 1 n       | 1    | n   |     |
wherewehaveused3.82.
Again use 3.81, this time replacing w with v . Also replace \mathcal{T} with \mathcal{I} and
|     |     |     |     |     | k   | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
replace\mathcal{S}with\mathcal{T},getting
|     |     | ℳ(\mathcal{T},(u | ,…,u |     | ),(v ,…,v |     |     |     |
| --- | --- | ------ | ---- | --- | --------- | --- | --- | --- |
$$))=\mathcal{B}\mathcal{C}.$$
|     |     |     | 1   | n   | 1   | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Substitutingtheequationaboveinto3.85givestheequation\mathcal{A}=\mathcal{C}-1\mathcal{B}\mathcal{C}.
Theproofofthenextresultisleftasanexercise.
matrixofinverseequalsinverseofmatrix
3.86
Suppose that v ,…,v is a basis of \mathcal{V} and \mathcal{T} \in ℒ(\mathcal{V}) is invertible. Then
|     |     | 1   | n   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ℳ(\mathcal{T}-1) = (ℳ(\mathcal{T}))-1, where both matrices are with respect to the basis
| v ,…,v      | .   |                                  |     |         |                                    |     |                 |     |
| ----------- | --- | -------------------------------- | --- | ------- | ---------------------------------- | --- | --------------- | --- |
| 1           | n   |                                  |     |         |                                    |     |                 |     |
| Exercises   | 3D  |                                  |     |         |                                    |     |                 |     |
| 1 Suppose\mathcal{T}  |     | \inℒ(\mathcal{V},\mathcal{W})isinvertible.             |     |         | Showthat\mathcal{T}-1                        |     | isinvertibleand |     |
|             |     |                                  |     | (\mathcal{T}-1)-1 | =\mathcal{T}.                                |     |                 |     |
| Suppose\mathcal{T}    |     | ℒ(\mathcal{U},\mathcal{V})and\mathcal{S}                       |     |         | ℒ(\mathcal{V},\mathcal{W})arebothinvertiblelinearmaps. |     |                 |     |
| 2           |     | \in                                |     | \in       |                                    |     |                 |     |
| Provethat\mathcal{S}\mathcal{T} |     | \inℒ(\mathcal{U},\mathcal{W})isinvertibleandthat(\mathcal{S}\mathcal{T})-1 |     |         |                                    |     | =\mathcal{T}-1\mathcal{S}-1.        |     |
3 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \in ℒ(\mathcal{V}). Provethatthefollowing
areequivalent.
| (a) | \mathcal{T} isinvertible. |     |             |     |                |     |           |     |
| --- | --------------- | --- | ----------- | --- | -------------- | --- | --------- | --- |
| (b) | \mathcal{T}v ,…,\mathcal{T}v        |     | isabasisof\mathcal{V} |     | foreverybasisv |     | ,…,v of\mathcal{V}. |     |
|     | 1               | n   |             |     |                |     | 1 n       |     |
| (c) | \mathcal{T}v ,…,\mathcal{T}v        |     | isabasisof\mathcal{V} |     | forsomebasisv  |     | ,…,v of\mathcal{V}. |     |
|     | 1               | n   |             |     |                |     | 1 n       |     |
4 Suppose \mathcal{V} is finite-dimensional and dim\mathcal{V} > 1. Prove that the set of
| noninvertiblelinearmapsfrom\mathcal{V} |     |     |     |     | toitselfisnotasubspaceofℒ(\mathcal{V}). |     |     |     |
| ---------------------------- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- |

| --- | -------- | --- | ---------- | --- | --- | --- | --- | --- |
5 Suppose\mathcal{V} isfinite-dimensional,\mathcal{U} isasubspaceof\mathcal{V},and\mathcal{S} \in ℒ(\mathcal{U},\mathcal{V}).
Provethatthereexistsaninvertiblelinearmap\mathcal{T} from\mathcal{V} toitselfsuchthat
|     | \mathcal{T}u=\mathcal{S}uforeveryu\in\mathcal{U} |     |     | ifandonlyif\mathcal{S}isinjective. |     |     |     |     |
| --- | ---------------- | --- | --- | ------------------------ | --- | --- | --- | --- |
6 Suppose that \mathcal{W} is finite-dimensional and \mathcal{S},\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Prove that
|     | null\mathcal{S}=null\mathcal{T} |     | ifandonlyifthereexistsaninvertible\mathcal{E}\inℒ(\mathcal{W})suchthat |     |     |     |     |     |
| --- | ----------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
\mathcal{S}=\mathcal{E}\mathcal{T}.
7 Suppose that \mathcal{V} is finite-dimensional and \mathcal{S},\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Prove that
range\mathcal{S} = range\mathcal{T} ifandonlyifthereexistsaninvertible\mathcal{E} \in ℒ(\mathcal{V})such
that\mathcal{S}=\mathcal{T}\mathcal{E}.
8 Suppose\mathcal{V} and\mathcal{W} arefinite-dimensionaland\mathcal{S},\mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}). Provethat
|     | thereexistinvertible\mathcal{E} |     | \in   | ℒ(\mathcal{V})and\mathcal{E} | \in   | ℒ(\mathcal{W})suchthat\mathcal{S} |     | = \mathcal{E} \mathcal{T}\mathcal{E} if |
| --- | --------------------- | --- | --- | -------- | --- | ------------- | --- | --------- |
|     |                       |     | 1   |          | 2   |               |     | 2 1       |
andonlyifdimnull\mathcal{S}=dimnull\mathcal{T}.
isfinite-dimensionaland\mathcal{T}∶
| 9   | Suppose\mathcal{V} |     |     |     | \mathcal{V} \rightarrow\mathcal{W} | isasurjectivelinearmap |     |     |
| --- | -------- | --- | --- | --- | ---- | ---------------------- | --- | --- |
of \mathcal{V} onto \mathcal{W}. Prove that there is a subspace \mathcal{U} of \mathcal{V} such that \mathcal{T}| is an
\mathcal{U}
|     | isomorphismof\mathcal{U}        |                   | onto\mathcal{W}. |                |     |                    |               |     |
| --- | --------------------- | ----------------- | ------ | -------------- | --- | ------------------ | ------------- | --- |
|     | Here\mathcal{T}|                | meansthefunction\mathcal{T} |        | restrictedto\mathcal{U}. |     | Thus\mathcal{T}|             | isthefunction |     |
|     |                       | \mathcal{U}                 |        |                |     |                    | \mathcal{U}             |     |
|     | whosedomainis\mathcal{U},with\mathcal{T}| |                   |        | definedby\mathcal{T}|    |     | (u)=\mathcal{T}uforeveryu\in\mathcal{U}. |               |     |
|     |                       |                   |        | \mathcal{U}              | \mathcal{U}   |                    |               |     |
10 Suppose\mathcal{V} and\mathcal{W} arefinite-dimensionaland\mathcal{U} isasubspaceof\mathcal{V}. Let
|     |                                                    |     | ℰ={\mathcal{T}   | \inℒ(\mathcal{V},\mathcal{W})∶\mathcal{U}    |     | \subseteqnull\mathcal{T}}. |                |     |
| --- | -------------------------------------------------- | --- | ------ | ------------ | --- | -------- | -------------- | --- |
|     | (a) Showthatℰisasubspaceofℒ(\mathcal{V},\mathcal{W}).                  |     |        |              |     |          |                |     |
|     | (b) Findaformulafordimℰintermsofdim\mathcal{V},dim\mathcal{W},anddim\mathcal{U}. |     |        |              |     |          |                |     |
|     | Hint:Define\Phi∶                                      |     | ℒ(\mathcal{V},\mathcal{W}) | ℒ(\mathcal{U},\mathcal{W})by\Phi(\mathcal{T}) |     |          | . Whatisnull\Phi? |     |
|     |                                                    |     |        | \rightarrow            |     | =        | \mathcal{T}| \mathcal{U}           |     |
Whatisrange\Phi?
| 11  | Suppose\mathcal{V}                     | isfinite-dimensionaland\mathcal{S},\mathcal{T}   |                 |      | \inℒ(\mathcal{V}). |                | Provethat |          |
| --- | ---------------------------- | ---------------------------- | --------------- | ---- | ------ | -------------- | --------- | -------- |
|     |                              |                              | \mathcal{S}\mathcal{T} isinvertible | ⟺    | \mathcal{S}and\mathcal{T}  | areinvertible. |           |          |
|     |                              | isfinite-dimensionaland\mathcal{S},\mathcal{T},\mathcal{U} |                 |      |        | \inℒ(\mathcal{V})and\mathcal{S}\mathcal{T}\mathcal{U}    |           |          |
| 12  | Suppose\mathcal{V}                     |                              |                 |      |        |                |           | =\mathcal{I}. Show |
|     | that\mathcal{T} isinvertibleandthat\mathcal{T}-1 |                              |                 | =\mathcal{U}\mathcal{S}. |        |                |           |          |
13 Showthattheresultin Exercise12canfailwithoutthehypothesisthat\mathcal{V} is
finite-dimensional.
14 Proveorgiveacounterexample: If\mathcal{V} isafinite-dimensionalvectorspace
|     | and\mathcal{R},\mathcal{S},\mathcal{T} | \inℒ(\mathcal{V})aresuchthat\mathcal{R}\mathcal{S}\mathcal{T} |     |     | issurjective,then\mathcal{S}isinjective. |     |     |     |
| --- | -------- | ------------------- | --- | --- | ------------------------------ | --- | --- | --- |
15 Suppose \mathcal{T} \in ℒ(\mathcal{V}) and v ,…,v is a list in \mathcal{V} such that \mathcal{T}v ,…,\mathcal{T}v
|     |                                 |            |      | 1 m     |        |                           |     | 1 m |
| --- | ------------------------------- | ---------- | ---- | ------- | ------ | ------------------------- | --- | --- |
|     | spans\mathcal{V}.                         | Provethatv | ,…,v | spans\mathcal{V}. |        |                           |     |     |
|     |                                 |            | 1    | m       |        |                           |     |     |
|     | Provethateverylinearmapfrom\mathbf{F}n,1 |            |      |         | to\mathbf{F}m,1 |                           |     |     |
| 16  |                                 |            |      |         |        | isgivenbyamatrixmultipli- |     |     |
cation. Inotherwords,provethatif\mathcal{T} \inℒ(\mathbf{F}n,1,\mathbf{F}m,1),thenthereexistsan
\in\mathbf{F}n,1.
|     | m-by-nmatrix\mathcal{A}suchthat\mathcal{T}x |     |     | =\mathcal{A}xforeveryx |     |     |     |     |
| --- | ----------------------- | --- | --- | ------------ | --- | --- | --- | --- |

| --- | --- | --- | --------- | ---------------------------- | --- | --- | --- |
| 17 Suppose\mathcal{V} | isfinite-dimensionaland\mathcal{S}\inℒ(\mathcal{V}). |     |     |     |     | Define𝒜\inℒ(ℒ(\mathcal{V}))by |     |
| ----------- | ------------------------------ | --- | --- | --- | --- | ----------------- | --- |
𝒜(\mathcal{T})=\mathcal{S}\mathcal{T}
| for\mathcal{T} \inℒ(\mathcal{V}).                              |                                     |     |     |     |     |     |     |
| ---------------------------------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
| (a) Showthatdimnull𝒜=(dim\mathcal{V})(dimnull\mathcal{S}).   |                                     |     |     |     |     |     |     |
| (b) Showthatdimrange𝒜=(dim\mathcal{V})(dimrange\mathcal{S}). |                                     |     |     |     |     |     |     |
| Showthat\mathcal{V}                                | andℒ(\mathbf{F},\mathcal{V})areisomorphicvectorspaces. |     |     |     |     |     |     |
Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Provethat\mathcal{T} hasthesame
matrixwithrespecttoeverybasisof\mathcal{V} ifandonlyif\mathcal{T} isascalarmultiple
oftheidentityoperator.
20 Supposeq \in 𝒫(\mathbf{R}). Provethatthereexistsapolynomialp \in 𝒫(\mathbf{R})such
that
q(x)=(x2+x)p″(x)+2xp′(x)+p(3)
| forallx                           | \in\mathbf{R}. |     |     |     |           |         |           |
| --------------------------------- | --- | --- | --- | --- | --------- | ------- | --------- |
|                                   |     |     |     |     | forallj,k | =1,…,n. |           |
| 21 Supposenisapositiveintegerand\mathcal{A} |     |     |     | j,k | \in\mathbf{F}        |         | Provethat |
thefollowingareequivalent(notethatinbothpartsbelow,thenumberof
equationsequalsthenumberofvariables).
$$(a) The trivial solution x = ⋯ = x = 0 is the only solution to the$$
|     |     |     | 1   |     | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
homogeneoussystemofequations
n
|     |     |     |     | \sum\mathcal{A}  | x =0 |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- |
1,k k
$$k=1$$
⋮
n
|     |     |     |     | \sum\mathcal{A}  | x =0. |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- |
n,k k
$$k=1$$
$$(b) Foreveryc ,…,c \in\mathbf{F},thereexistsasolutiontothesystemofequations$$
|     |     | 1 n |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
n
|     |     |     |     | \sum\mathcal{A}  | x =c |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- |
|     |     |     |     | 1,k | k 1  |     |     |
$$k=1$$
⋮
n
|     |     |     |     | \sum\mathcal{A}  | x =c . |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- |
|     |     |     |     | n,k | k n    |     |     |
$$k=1$$
| 22 Suppose\mathcal{T}     | \inℒ(\mathcal{V})andv   |      | ,…,v           | isabasisof\mathcal{V}. |     | Provethat        |     |
| --------------- | ----------- | ---- | -------------- | ------------ | --- | ---------------- | --- |
|                 |             |      | 1              | n            |     |                  |     |
|                 | ℳ(\mathcal{T},(v      | ,…,v | ))isinvertible |              | ⟺   | \mathcal{T} isinvertible.  |     |
|                 |             | 1    | n              |              |     |                  |     |
| 23 Supposethatu |             | ,…,u | andv ,…,v      | arebasesof\mathcal{V}. |     | Let\mathcal{T} \inℒ(\mathcal{V})besuch |     |
|                 | 1           | n    | 1              | n            |     |                  |     |
| that\mathcal{T}v          | =u foreachk |      | =1,…,n.        | Provethat    |     |                  |     |
k k
|     | ℳ(\mathcal{T},(v | ,…,v | ))=ℳ(\mathcal{I},(u |     | ,…,u | ),(v ,…,v |     |
| --- | ------ | ---- | --------- | --- | ---- | --------- | --- |
$$)).$$
|     |     | 1   | n   |     | 1   | n 1 | n   |
| --- | --- | --- | --- | --- | --- | --- | --- |
24 Suppose\mathcal{A}and\mathcal{B}aresquarematricesofthesamesizeand\mathcal{A}\mathcal{B} = \mathcal{I}. Prove
that\mathcal{B}\mathcal{A}=\mathcal{I}.

| -------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| 3E Products |           | and Quotients |     | of  | Vector Spaces |     |     |     |
| ----------- | --------- | ------------- | --- | --- | ------------- | --- | --- | --- |
| Products    | of Vector | Spaces        |     |     |               |     |     |     |
Asusualwhendealingwithmorethanonevectorspace,allvectorspacesinuse
shouldbeoverthesamefield.
| 3.87 definition: |      | productofvectorspaces |     |     |     |     |     |     |
| ---------------- | ---- | --------------------- | --- | --- | --- | --- | --- | --- |
| Suppose\mathcal{V}         | ,…,\mathcal{V} | arevectorspacesover\mathbf{F}. |     |     |     |     |     |     |
1 m
| • Theproduct |     | \mathcal{V} \times⋯\times\mathcal{V} | isdefinedby |     |     |     |     |     |
| ------------ | --- | ------ | ----------- | --- | --- | --- | --- | --- |
|              |     | 1      | m           |     |     |     |     |     |
$$)∶v$$
|                           | \mathcal{V} \times⋯\times\mathcal{V}                    |           | ={(v        | ,…,v  | \in\mathcal{V} ,…,v     |     | \in\mathcal{V} }. |     |
| ------------------------- | ------------------------- | --------- | ----------- | ----- | ----------- | --- | ----- | --- |
|                           | 1                         | m         | 1           | m     | 1 1         | m   | m     |     |
| • Additionon\mathcal{V}             |                           | \times⋯\times\mathcal{V}      | isdefinedby |       |             |     |       |     |
|                           |                           | 1         | m           |       |             |     |       |     |
|                           | (u                        | ,…,u )+(v | ,…,v        | )=(u  | +v ,…,u     |     | +v ). |     |
|                           |                           | 1 m       | 1           | m     | 1 1         | m   | m     |     |
| • Scalarmultiplicationon\mathcal{V} |                           |           | \times⋯\times\mathcal{V}        |       | isdefinedby |     |       |     |
|                           |                           |           | 1           | m     |             |     |       |     |
|                           |                           | \lambda(v       | ,…,v        | )=(\lambdav | ,…,\lambdav       | ).  |       |     |
|                           |                           |           | 1           | m     | 1 m         |     |       |     |
| 3.88 example:             | productofthevectorspaces𝒫 |           |             |       | (\mathbf{R})and\mathbf{R}3    |     |       |     |
Elementsof𝒫 (\mathbf{R})\times\mathbf{R}3 arelistsoflengthtwo,withthefirstiteminthelist
| anelementof𝒫 | (\mathbf{R})andtheseconditeminthelistanelementof\mathbf{R}3. |     |     |     |     |     |     |     |
| ------------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Forexample,(5-6x+4x2,(3,8,7))and(x+9x5,(2,2,2))areelementsof
| 𝒫 (\mathbf{R})\times\mathbf{R}3. | Theirsumisdefinedby |     |     |     |     |     |     |     |
| --------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
$$(5-6x+4x2,(3,8,7))+(x+9x5,(2,2,2))$$
=(5-5x+4x2+9x5,(5,10,9)).
Also,2(5-6x+4x2,(3,8,7))=(10-12x+8x2,(6,16,14)).
Thenextresultshouldbeinterpretedtomeanthattheproductofvectorspaces
is a vector space with the operations of addition and scalar multiplication as
definedby3.87.
3.89 productofvectorspacesisavectorspace
| Suppose\mathcal{V} | ,…,\mathcal{V} | arevectorspacesover\mathbf{F}. |     |     | Then\mathcal{V} | \times⋯\times\mathcal{V} | isavector |     |
| -------- | ---- | --------------------- | --- | --- | ----- | ---- | --------- | --- |
|          | 1    | m                     |     |     |       | 1    | m         |     |
spaceover\mathbf{F}.
Theproofoftheresultaboveislefttothereader. Notethattheadditiveidentity
of \mathcal{V} \times⋯\times\mathcal{V} is (0,…,0), where the 0 in the kth slot is the additive identity
| 1                            | m   |     |     |      |      |       |       |     |
| ---------------------------- | --- | --- | --- | ---- | ---- | ----- | ----- | --- |
|                              |     |     |     | ,…,v |      |       | ,…,-v |     |
| of\mathcal{V} . Theadditiveinverseof(v |     |     |     | )\in\mathcal{V}  | \times⋯\times\mathcal{V} | is(-v |       | ).  |
| k                            |     |     | 1   | m    | 1    | m     | 1     | m   |

| --- | --- | --------- | --- | ---------------------------------- | --- | --- | --- | --- |
|     |     | \mathbf{R}2\times\mathbf{R}3 | \neq\mathbf{R}5 | but\mathbf{R}2\times\mathbf{R}3 | isisomorphicto\mathbf{R}5 |     |     |     |
| --- | --- | ----- | --- | -------- | ---------------- | --- | --- | --- |
**3.90 例：** | Elementsofthevectorspace\mathbf{R}2\times\mathbf{R}3 |     |     |     |         | arelists  |     |     |     |
| ----------------------------- | --- | --- | --- | ------- | --------- | --- | --- | --- |
|                               |     |     |     | ,x ),(x | ,x ,x )), |     |     |     |
$$((x$$
|        |       |           |              | 1 2   | 3 4 5       |     |     |     |
| ------ | ----- | --------- | ------------ | ----- | ----------- | --- | --- | --- |
| wherex | ,x ,x | ,x ,x \in\mathbf{R}. | Elementsof\mathbf{R}5 |       | arelists    |     |     |     |
|        | 1 2   | 3 4 5     |              |       |             |     |     |     |
|        |       |           |              | (x ,x | ,x ,x ,x ), |     |     |     |
|        |       |           |              | 1 2   | 3 4 5       |     |     |     |
| wherex | ,x ,x | ,x ,x \in\mathbf{R}. |              |       |             |     |     |     |
|        | 1 2   | 3 4 5     |              |       |             |     |     |     |
Althoughelementsof\mathbf{R}2\times\mathbf{R}3and\mathbf{R}5looksimilar,theyarenotthesamekind
ofobject. Elementsof\mathbf{R}2\times\mathbf{R}3 arelistsoflengthtwo(withthefirstitemitselfa
listoflengthtwoandtheseconditemalistoflengththree),andelementsof\mathbf{R}5
| arelistsoflengthfive. |     | Thus\mathbf{R}2\times\mathbf{R}3 |     |     | doesnotequal\mathbf{R}5. |     |     |     |
| --------------------- | --- | --------- | --- | --- | --------------- | --- | --- | --- |
Thelinearmap
Thisisomorphismissonaturalthat
|        |         |          |     |       | we should                            | think | of it as a relabel- |     |
| ------ | ------- | -------- | --- | ----- | ------------------------------------ | ----- | ------------------- | --- |
| ((x ,x | ),(x ,x | ,x ))↦(x | ,x  | ,x ,x | ,x )                                 |       |                     |     |
| 1 2    | 3       | 4 5      | 1   | 2 3   | 4 5 ing. Somepeopleinformallysaythat |       |                     |     |
is an isomorphism of the vector space \mathbf{R}2\times\mathbf{R}3equals\mathbf{R}5,whichisnottechni-
| \mathbf{R}2 \mathbf{R}3 |      |            |       | \mathbf{R}5. | callycorrectbutwhichcapturesthe |     |     |     |
| ----- | ---- | ---------- | ----- | --- | ------------------------------- | --- | --- | --- |
| \times     | onto | the vector | space |     | Thus                            |     |     |     |
thesetwovectorspacesareisomorphic,al- spiritofidentificationviarelabeling.
thoughtheyarenotequal.
Thenextexampleillustratestheideathatwewilluseintheproofof3.92.
|               |     |          | 𝒫 (\mathbf{R})\times\mathbf{R}2 |     |     |     |     |     |
| ------------- | --- | -------- | -------- | --- | --- | --- | --- | --- |
| 3.91 example: |     | abasisof |          |     |     |     |     |     |
| Considerthislistoflengthfiveofelementsof𝒫 |     |     |     |     | (\mathbf{R})\times\mathbf{R}2: |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- |
$$(1,(0,0)),(x,(0,0)),(x2,(0,0)),(0,(1,0)),(0,(0,1)).$$
$$(\mathbf{R})\times\mathbf{R}2.$$
| Thelistaboveislinearlyindependentanditspans𝒫 |     |     |     |     |     |     | Thusitisabasis |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- |
of𝒫 (\mathbf{R})\times\mathbf{R}2.
3.92 dimensionofaproductisthesumofdimensions
| Suppose\mathcal{V} | ,…,\mathcal{V} | arefinite-dimensionalvectorspaces. |     |     |     | Then\mathcal{V} | \times⋯\times\mathcal{V} |     |
| -------- | ---- | ---------------------------------- | --- | --- | --- | ----- | ---- | --- |
|          | 1    | m                                  |     |     |     |       | 1    | m   |
isfinite-dimensionaland
|     |     | dim(\mathcal{V} | \times⋯\times\mathcal{V} | )=dim\mathcal{V} | +⋯+dim\mathcal{V} |     | .   |     |
| --- | --- | ----- | ---- | ------ | ------- | --- | --- | --- |
|     |     |       | 1    | m      | 1       | m   |     |     |
Proof Chooseabasisofeach\mathcal{V} . Foreachbasisvectorofeach\mathcal{V} ,considerthe
|     |     |     |     | k   |     |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
elementof\mathcal{V} \times⋯\times\mathcal{V} thatequalsthebasisvectorinthekthslotand0intheother
1 m
slots. Thelistofallsuchvectorsislinearlyindependentandspans\mathcal{V} \times⋯\times\mathcal{V} .
|                   |     |        |     |                              |     |     | 1       | m   |
| ----------------- | --- | ------ | --- | ---------------------------- | --- | --- | ------- | --- |
| Thusitisabasisof\mathcal{V} |     |        |     | . Thelengthofthisbasisisdim\mathcal{V} |     |     | +⋯+dim\mathcal{V} | ,   |
|                   |     | 1 \times⋯\times\mathcal{V} | m   |                              |     |     | 1       | m   |
asdesired.

98 Chapter 3 Linear Maps
Inthenextresult,themapΓissurjectivebythedefinitionof\mathcal{V} +⋯+\mathcal{V} . Thus
1 m
thelastwordintheresultbelowcouldbechangedfrom“injective”to“invertible”.
3.93 productsanddirectsums
Suppose that \mathcal{V} ,…,\mathcal{V} are subspaces of \mathcal{V}. Define a linear map
1 m
Γ ∶\mathcal{V} \times⋯\times\mathcal{V} \rightarrow\mathcal{V} +⋯+\mathcal{V} by
1 m 1 m
Γ(v ,…,v )=v +⋯+v .
1 m 1 m
Then\mathcal{V} +⋯+\mathcal{V} isadirectsumifandonlyifΓisinjective.
1 m
Proof By 3.15, Γ is injective if and only if the only way to write 0 as a sum
v +⋯+v ,whereeachv isin\mathcal{V} ,isbytakingeachv equalto0. Thus1.45
1 m k k k
showsthatΓisinjectiveifandonlyif\mathcal{V} +⋯+\mathcal{V} isadirectsum,asdesired.
1 m
3.94 asumisadirectsumifandonlyifdimensionsaddup
Suppose \mathcal{V} is finite-dimensional and \mathcal{V} ,…,\mathcal{V} are subspaces of \mathcal{V}. Then
1 m
\mathcal{V} +⋯+\mathcal{V} isadirectsumifandonlyif
1 m
dim(\mathcal{V} +⋯+\mathcal{V} )=dim\mathcal{V} +⋯+dim\mathcal{V} .
1 m 1 m
Proof The map Γ in 3.93 is surjective. Thus by the fundamental theorem of
linearmaps(3.21),Γisinjectiveifandonlyif
dim(\mathcal{V} +⋯+\mathcal{V} )=dim(\mathcal{V} \times⋯\times\mathcal{V} ).
1 m 1 m
Combining3.93and3.92nowshowsthat\mathcal{V} +⋯+\mathcal{V} isadirectsumifandonly
1 m
if
dim(\mathcal{V} +⋯+\mathcal{V} )=dim\mathcal{V} +⋯+dim\mathcal{V} ,
1 m 1 m
asdesired.
Inthespecialcasem=2,analternativeproofthat\mathcal{V} +\mathcal{V} isadirectsumif
1 2
andonlyifdim(\mathcal{V} +\mathcal{V} )=dim\mathcal{V} +dim\mathcal{V} canbeobtainedbycombining1.46
1 2 1 2
and2.43.
Webeginourapproachtoquotientspacesbydefiningthesumofavectoranda
subset.
**3.95 记号：** v+\mathcal{U}
Supposev\in\mathcal{V} and\mathcal{U} \subseteq\mathcal{V}. Thenv+\mathcal{U} isthesubsetof\mathcal{V} definedby
v+\mathcal{U} ={v+u∶u\in\mathcal{U}}.

| --- | --------- | ---------------------------------- | --- |
\mathbf{R}2
| 3.96 example: | sumofavectorandaone-dimensionalsubspaceof |     |     |
| ------------- | ----------------------------------------- | --- | --- |
Suppose
| ={(x,2x)\in\mathbf{R}2          |                      | ∶x   |     |
| -------------------- | -------------------- | ---- | --- |
| \mathcal{U}                    |                      | \in\mathbf{R}}. |     |
| Hence\mathcal{U} isthelinein\mathbf{R}2 | throughtheoriginwith |      |     |
slope2. Thus
$$(17,20)+\mathcal{U}$$
\mathbf{R}2
| is the line in | that contains | the point (17,20) |     |
| -------------- | ------------- | ----------------- | --- |
andhasslope2.
| Because |     |     | (17,20)+\mathcal{U}isparallel |
| ------- | --- | --- | ------------------- |
tothesubspace\mathcal{U}.
| (10,20)\in\mathcal{U} | and (17,20)\in(17,20)+\mathcal{U}, |     |     |
| --------- | ---------------------- | --- | --- |
weseethat(17,20)+\mathcal{U}isobtainedbymoving\mathcal{U}
totherightby7units.
translate
**3.97 定义：** | Forv\in\mathcal{V}        | and\mathcal{U} asubsetof\mathcal{V},thesetv+\mathcal{U} |     | issaidtobeatranslateof\mathcal{U}. |
| ------------- | ------------------------- | --- | ------------------------ |
| 3.98 example: | translates                |     |                          |
• If\mathcal{U} isthelinein\mathbf{R}2 definedby\mathcal{U} ={(x,2x)\in\mathbf{R}2 ∶x \in\mathbf{R}},thenalllinesin
\mathbf{R}2 withslope2aretranslatesof\mathcal{U}. See Example3.96aboveforadrawingof
\mathcal{U} andoneofitstranslates.
• Moregenerally,if\mathcal{U} isalinein\mathbf{R}2,thenthesetofalltranslatesof\mathcal{U} istheset
| ofalllinesin\mathbf{R}2 | thatareparallelto\mathcal{U}. |     |     |
| -------------- | ------------------- | --- | --- |
• If\mathcal{U} = {(x,y,0) \in \mathbf{R}3 ∶ x,y \in \mathbf{R}},thenthetranslatesof\mathcal{U} aretheplanesin
\mathbf{R}3
thatareparalleltothexy-plane\mathcal{U}.
• Moregenerally,if\mathcal{U} isaplanein\mathbf{R}3,thenthesetofalltranslatesof\mathcal{U} isthe
setofallplanesin\mathbf{R}3
|                  | thatareparallelto\mathcal{U} |     | (see,forexample,Exercise7). |
| ---------------- | ------------------ | --- | --------------------------- |
| 3.99 definition: | quotientspace,\mathcal{V}/\mathcal{U}  |     |                             |
Suppose\mathcal{U} isasubspaceof\mathcal{V}. Thenthequotientspace\mathcal{V}/\mathcal{U} isthesetofall
| translatesof\mathcal{U}. | Thus |     |     |
| -------------- | ---- | --- | --- |
∶v\in\mathcal{V}}.
\mathcal{V}/\mathcal{U} ={v+\mathcal{U}

| --- | -------- | ---------- | --- | --- | --- | --- | --- |
quotientspaces
**3.100 例：** ∶x
| • If\mathcal{U} | ={(x,2x)\in\mathbf{R}2 |     | \in\mathbf{R}},then\mathbf{R}2/\mathcal{U}isthesetofalllinesin\mathbf{R}2thathave |     |     |     |     |
| ----- | ----------- | --- | ------------------------------------------ | --- | --- | --- | --- |
slope2.
• If\mathcal{U} isalinein\mathbf{R}3containingtheorigin,then\mathbf{R}3/\mathcal{U} isthesetofalllinesin\mathbf{R}3
parallelto\mathcal{U}.
• If\mathcal{U} isaplanein\mathbf{R}3 containingtheorigin,then\mathbf{R}3/\mathcal{U} isthesetofallplanesin
\mathbf{R}3
parallelto\mathcal{U}.
|     | Ournextgoalistomake\mathcal{V}/\mathcal{U} |     | intoavectorspace. |     |     | Todothis,wewillneed |     |
| --- | ---------------------- | --- | ----------------- | --- | --- | ------------------- | --- |
thenextresult.
3.101 twotranslatesofasubspaceareequalordisjoint
| Suppose\mathcal{U} | isasubspaceof\mathcal{V}     |       | andv,w\in\mathcal{V}.  |     | Then             |     |     |
| -------- | ------------------ | ----- | ---------- | --- | ---------------- | --- | --- |
|          | v-w\in\mathcal{U}              | ⟺ v+\mathcal{U} | =w+\mathcal{U}       |     | ⟺ (v+\mathcal{U})\cap(w+\mathcal{U})\neq\emptyset. |     |     |
| Proof    | Firstsupposev-w\in\mathcal{U}. |       | Ifu\in\mathcal{U},then |     |                  |     |     |
v+u=w+((v-w)+u)\inw+\mathcal{U}.
| Thusv+\mathcal{U}           | \subseteqw+\mathcal{U}.                    | Similarly,w+\mathcal{U} |                           | \subseteqv+\mathcal{U}. | Thusv+\mathcal{U}         |     | =w+\mathcal{U},completing |
| ----------------- | ------------------------ | ------------- | ------------------------- | ----- | --------------- | --- | --------------- |
| theproofthatv-w\in\mathcal{U} |                          | impliesv+\mathcal{U}    |                           | =w+\mathcal{U}. |                 |     |                 |
|                   | Theequationv+\mathcal{U}           | =w+\mathcal{U}          | impliesthat(v+\mathcal{U})\cap(w+\mathcal{U})\neq\emptyset. |       |                 |     |                 |
|                   | Nowsuppose(v+\mathcal{U})\cap(w+\mathcal{U})\neq\emptyset. |               |                           |       | Thusthereexistu |     | ,u \in\mathcal{U} suchthat  |
1 2
|           |     |                                       | v+u | =w+u | .   |     |     |
| --------- | --- | ------------------------------------- | --- | ---- | --- | --- | --- |
| Thusv-w=u |     | . Hencev-w\in\mathcal{U},showingthat(v+\mathcal{U})\cap(w+\mathcal{U})\neq\emptyset |     |      |     |     |     |
|           |     | 2 -u 1                                |     |      |     |     |     |
impliesv-w\in\mathcal{U},whichcompletestheproof.
Nowwecandefineadditionandscalarmultiplicationon\mathcal{V}/\mathcal{U}.
| 3.102 | definition: | additionandscalarmultiplicationon\mathcal{V}/\mathcal{U} |     |     |     |     |     |
| ----- | ----------- | ------------------------------------ | --- | --- | --- | --- | --- |
Suppose\mathcal{U} isasubspaceof\mathcal{V}. Thenadditionandscalarmultiplicationare
| definedon\mathcal{V}/\mathcal{U} |     | by  |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- |
$$(v+\mathcal{U})+(w+\mathcal{U})=(v+w)+\mathcal{U}$$
\lambda(v+\mathcal{U})=(\lambdav)+\mathcal{U}
| forallv,w\in\mathcal{V} |     | andall \lambda\in\mathbf{F}. |     |     |     |     |     |
| ----------- | --- | ----------- | --- | --- | --- | --- | --- |
Aspartoftheproofofthenextresult,wewillshowthatthedefinitionsabove
makesense.

Section3E Productsand Quotientsof Vector Spaces 101
3.103 quotientspaceisavectorspace
Suppose\mathcal{U}isasubspaceof\mathcal{V}. Then\mathcal{V}/\mathcal{U},withtheoperationsofadditionand
scalarmultiplicationasdefinedabove,isavectorspace.
multiplicationon\mathcal{V}/\mathcal{U} isthattherepresentationofatranslateof\mathcal{U} isnotunique.
Specifically,supposev ,v ,w ,w \in\mathcal{V} aresuchthat
1 2 1 2
v +\mathcal{U} =v +\mathcal{U} and w +\mathcal{U} =w +\mathcal{U}.
1 2 1 2
Toshowthatthedefinitionofadditionon\mathcal{V}/\mathcal{U}givenabovemakessense,wemust
showthat(v +w )+\mathcal{U} =(v +w )+\mathcal{U}.
1 1 2 2
By3.101,wehave
v -v \in\mathcal{U} and w -w \in\mathcal{U}.
1 2 1 2
Because\mathcal{U} isasubspaceof\mathcal{V} andthusisclosedunderaddition,thisimpliesthat
$$(v -v )+(w -w )\in\mathcal{U}. Thus(v +w )-(v +w )\in\mathcal{U}. Using3.101again,$$
1 2 1 2 1 1 2 2
weseethat
$$(v +w )+\mathcal{U} =(v +w )+\mathcal{U},$$
1 1 2 2
asdesired. Thusthedefinitionofadditionon\mathcal{V}/\mathcal{U} makessense.
Similarly, suppose \lambda \in \mathbf{F}. We are still assuming that v + \mathcal{U} = v + \mathcal{U}.
1 2
Because\mathcal{U} isasubspaceof\mathcal{V} andthusisclosedunderscalarmultiplication,we
have \lambda(v -v )\in\mathcal{U}. Thus \lambdav - \lambdav \in\mathcal{U}. Hence3.101impliesthat
1 2 1 2
$$(\lambdav )+\mathcal{U} =(\lambdav )+\mathcal{U}.$$
1 2
Thusthedefinitionofscalarmultiplicationon\mathcal{V}/\mathcal{U} makessense.
Nowthatadditionandscalarmultiplicationhavebeendefinedon\mathcal{V}/\mathcal{U},the
verificationthattheseoperationsmake\mathcal{V}/\mathcal{U} intoavectorspaceisstraightforward
andislefttothereader. Notethattheadditiveidentityof\mathcal{V}/\mathcal{U} is0+\mathcal{U} (which
equals\mathcal{U})andthattheadditiveinverseofv+\mathcal{U} is(-v)+\mathcal{U}.
Thenextconceptwillleadtoacomputationofthedimensionof\mathcal{V}/\mathcal{U}.
**3.104 定义：** quotientmap,\pi
Suppose\mathcal{U} isasubspaceof\mathcal{V}. Thequotientmap\pi∶ \mathcal{V} \rightarrow\mathcal{V}/\mathcal{U} isthelinear
mapdefinedby
$$\pi(v)=v+\mathcal{U}$$
foreachv\in\mathcal{V}.
Thereadershouldverifythat\pi isindeedalinearmap. Although\pi depends
on\mathcal{U}aswellas\mathcal{V},thesespacesareleftoutofthenotationbecausetheyshouldbe
clearfromthecontext.

| -------- | ---------- | --- | --- | --- |
dimensionofquotientspace
3.105
| Suppose\mathcal{V} isfinite-dimensionaland\mathcal{U}         |                    | isasubspaceof\mathcal{V}. | Then          |      |
| ----------------------------------------- | ------------------ | --------------- | ------------- | ---- |
|                                           | dim\mathcal{V}/\mathcal{U} =dim\mathcal{V}-dim\mathcal{U}. |                 |               |      |
| Proof Let\pidenotethequotientmapfrom\mathcal{V}to\mathcal{V}/\mathcal{U}. |                    |                 | Ifv\in\mathcal{V},thenv+\mathcal{U} | =0+\mathcal{U} |
ifandonlyifv\in\mathcal{U} (by3.101),whichimpliesthatnull\pi =\mathcal{U}. Thedefinitionof
\pi impliesrange\pi =\mathcal{V}/\mathcal{U}. Thefundamentaltheoremoflinearmaps(3.21)now
| impliesdim\mathcal{V} =dim\mathcal{U}+dim\mathcal{V}/\mathcal{U},whichgivesthedesiredresult. |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- |
Each linear map \mathcal{T} on \mathcal{V} induces a linear map \mathcal{T} ̃ on \mathcal{V}/(null\mathcal{T}), as defined
below.
\mathcal{T} ̃
**3.106 记号：** ̃∶
| Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). | Define\mathcal{T} | \mathcal{V}/(null\mathcal{T})\rightarrow\mathcal{W} | by  |     |
| ----------------- | ------- | ----------- | --- | --- |
̃
\mathcal{T} (v+null\mathcal{T})=\mathcal{T}v.
̃
Toshowthatthedefinitionof\mathcal{T} makessense,supposeu,v\in\mathcal{V} aresuchthat
u+null\mathcal{T} = v+null\mathcal{T}. By3.101,wehaveu-v \in null\mathcal{T}. Thus\mathcal{T}(u-v) = 0.
̃
Hence \mathcal{T}u = \mathcal{T}v. Thus the definition of \mathcal{T} indeed makes sense. The routine
̃
verificationthat\mathcal{T} isalinearmapfrom\mathcal{V}/(null\mathcal{T})to\mathcal{W} islefttothereader.
Thenextresultshowsthatwecanthinkof\mathcal{T} ̃ asamodifiedversionof\mathcal{T},with
adomainthatproducesaone-to-onemap.
| 3.107 nullspaceandrangeof | \mathcal{T} ̃  |     |     |     |
| ------------------------- | ---- | --- | --- | --- |
| Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}).         | Then |     |     |     |
̃
| (a) \mathcal{T}\circ\pi =\mathcal{T},where\pi | isthequotientmapof\mathcal{V} |     | onto\mathcal{V}/(null\mathcal{T}); |     |
| ----------------- | ------------------- | --- | -------------- | --- |
̃
$$(b) \mathcal{T} isinjective;$$
̃
$$(c) range\mathcal{T} =range\mathcal{T};$$
$$(d) \mathcal{V}/(null\mathcal{T})andrange\mathcal{T}areisomorphicvectorspaces.$$
Proof
$$(a) Ifv\in\mathcal{V},then(\mathcal{T} ̃ \circ\pi)(v)=\mathcal{T} ̃ (\pi(v))=\mathcal{T} ̃ (v+null\mathcal{T})=\mathcal{T}v,asdesired.$$
̃
$$(b) Suppose v \in \mathcal{V} and \mathcal{T} (v+null\mathcal{T}) = 0. Then \mathcal{T}v = 0. Thus v \in null\mathcal{T}.$$
Hence3.101impliesthatv+null\mathcal{T} =0+null\mathcal{T}. Thisimpliesthatnull\mathcal{T} ̃
=
| {0+null\mathcal{T}}. Hence\mathcal{T}    | ̃ isinjective,asdesired. |          |     |     |
| -------------------- | ------------------------ | -------- | --- | --- |
|                      | ̃                        | ̃        |     |     |
| (c) Thedefinitionof\mathcal{T} | showsthatrange\mathcal{T}          | =range\mathcal{T}. |     |     |
$$(d) Now(b)and(c)implythatifwethinkof\mathcal{T} ̃ asmappingintorange\mathcal{T},then\mathcal{T} ̃$$
isanisomorphismfrom\mathcal{V}/(null\mathcal{T})ontorange\mathcal{T}.

Section3E Productsand Quotientsof Vector Spaces 103
Exercises 3E
1 Suppose\mathcal{T}isafunctionfrom\mathcal{V}to\mathcal{W}. Thegraphof\mathcal{T}isthesubsetof\mathcal{V}\times\mathcal{W}
definedby
graphof\mathcal{T} ={(v,\mathcal{T}v)\in\mathcal{V}\times\mathcal{W} ∶v\in\mathcal{V}}.
Provethat\mathcal{T} isalinearmapifandonlyifthegraphof\mathcal{T} isasubspaceof
\mathcal{V}\times\mathcal{W}.
Formally,afunction\mathcal{T}from\mathcal{V} to\mathcal{W} isasubset\mathcal{T}of \mathcal{V}\times\mathcal{W} suchthatfor
eachv \in \mathcal{V},thereexistsexactlyoneelement(v,w) \in \mathcal{T}. Inotherwords,
formallyafunctioniswhatiscalledaboveitsgraph. Wedonotusually
thinkoffunctionsinthisformalmanner. However,ifwedobecomeformal,
thenthisexercisecouldberephrasedasfollows: Provethatafunction\mathcal{T}
from\mathcal{V}to\mathcal{W}isalinearmapifandonlyif \mathcal{T}isasubspaceof \mathcal{V}\times\mathcal{W}.
2 Supposethat\mathcal{V} ,…,\mathcal{V} arevectorspacessuchthat\mathcal{V} \times⋯\times\mathcal{V} isfinite1 m 1 m
dimensional. Provethat\mathcal{V} isfinite-dimensionalforeachk =1,…,m.
k
3 Suppose\mathcal{V} ,…,\mathcal{V} arevectorspaces. Provethatℒ(\mathcal{V} \times⋯\times\mathcal{V} ,\mathcal{W})and
1 m 1 m
ℒ(\mathcal{V} ,\mathcal{W})\times⋯\timesℒ(\mathcal{V} ,\mathcal{W})areisomorphicvectorspaces.
1 m
Thereisnoassumptionintheexerciseaboveorinthetwofollowingexercises
thatthevectorspacesarefinite-dimensional.
4 Suppose\mathcal{W} ,…,\mathcal{W} arevectorspaces. Provethatℒ(\mathcal{V},\mathcal{W} \times⋯\times\mathcal{W} )and
1 m 1 m
ℒ(\mathcal{V},\mathcal{W} )\times⋯\timesℒ(\mathcal{V},\mathcal{W} )areisomorphicvectorspaces.
1 m
5 Formapositiveinteger,define\mathcal{V}m by
\mathcal{V}m =\mathcal{V}⏟\times⋯\times\mathcal{V}.
mtimes
Provethat\mathcal{V}m andℒ(\mathbf{F}m,\mathcal{V})areisomorphicvectorspaces.
6 Supposethatv,xarevectorsin\mathcal{V} andthat\mathcal{U},\mathcal{W} aresubspacesof\mathcal{V} such
thatv+\mathcal{U} =x+\mathcal{W}. Provethat\mathcal{U} =\mathcal{W}.
7 Let\mathcal{U} = {(x,y,z) \in \mathbf{R}3 ∶ 2x+3y+5z = 0}. Suppose\mathcal{A} \subseteq \mathbf{R}3. Provethat
\mathcal{A}isatranslateof\mathcal{U} ifandonlyifthereexistsc \in\mathbf{R} suchthat
\mathcal{A}={(x,y,z)\in\mathbf{R}3 ∶2x+3y+5z=c}.
8 (a) Suppose \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}) and c \in \mathcal{W}. Prove that {x \in \mathcal{V} ∶ \mathcal{T}x = c} is
eithertheemptysetorisatranslateofnull\mathcal{T}.
$$(b) Explainwhythesetofsolutionstoasystemoflinearequationssuchas$$
3.27iseithertheemptysetorisatranslateofsomesubspaceof\mathbf{F}n.
9 Provethatanonemptysubset\mathcal{A}of\mathcal{V} isatranslateofsomesubspaceof\mathcal{V} if
andonlyif \lambdav+(1- \lambda)w\in\mathcal{A}forallv,w\in\mathcal{A}andall \lambda\in\mathbf{F}.
10 Suppose \mathcal{A} = v +\mathcal{U} and \mathcal{A} = w +\mathcal{U} for some v,w \in \mathcal{V} and some
1 1 2 2
subspaces \mathcal{U} ,\mathcal{U} of \mathcal{V}. Prove that the intersection \mathcal{A} \cap \mathcal{A} is either a
1 2 1 2
translateofsomesubspaceof\mathcal{V} oristheemptyset.

| --- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
|     |                                                    |      |                  | ,…)\in\mathbf{F}\infty                  | ∶x                       |      |     |          |      |
| --- | -------------------------------------------------- | ---- | ---------------- | ----------------------- | ------------------------ | ---- | --- | -------- | ---- |
| 11  | Suppose\mathcal{U}                                           | ={(x | ,x               |                         | \neq0foronlyfinitelymanyk}. |      |     |          |      |
|     |                                                    |      | 1                | 2                       | k                        |      |     |          |      |
|     | (a) Showthat\mathcal{U}                                      |      | isasubspaceof\mathbf{F}\infty. |                         |                          |      |     |          |      |
|     | (b) Provethat\mathbf{F}\infty/\mathcal{U}                                  |      |                  | isinfinite-dimensional. |                          |      |     |          |      |
| 12  | Supposev                                           | ,…,v | \in\mathcal{V}.              | Let                     |                          |      |     |          |      |
|     |                                                    | 1    | m                |                         |                          |      |     |          |      |
|     |                                                    |      | +⋯+              | ∶                       | ,…,\lambda                     | and  | +⋯+ |          |      |
|     | \mathcal{A}={\lambda                                               | 1 v  | 1                | \lambda m v m \lambda 1             |                          | m \in\mathbf{F} | \lambda 1 | \lambda m =1}. |      |
|     | (a) Provethat\mathcal{A}isatranslateofsomesubspaceof\mathcal{V}.       |      |                  |                         |                          |      |     |          |      |
|     | (b) Provethatif\mathcal{B}isatranslateofsomesubspaceof\mathcal{V}and{v |      |                  |                         |                          |      |     | ,…,v     | }\subseteq\mathcal{B}, |
|     |                                                    |      |                  |                         |                          |      |     | 1        | m    |
then\mathcal{A}\subseteq\mathcal{B}.
$$(c) Prove that \mathcal{A} is a translate of some subspace of \mathcal{V} of dimension less$$
thanm.
13 Suppose\mathcal{U} isasubspaceof\mathcal{V} suchthat\mathcal{V}/\mathcal{U} isfinite-dimensional. Prove
|     | that\mathcal{V}        | isisomorphicto\mathcal{U}\times(\mathcal{V}/\mathcal{U}). |                     |     |     |       |          |     |      |
| --- | ------------ | ---------------------- | ------------------- | --- | --- | ----- | -------- | --- | ---- |
| 14  | Suppose\mathcal{U}and\mathcal{W} |                        | aresubspacesof\mathcal{V}and\mathcal{V} |     |     | =\mathcal{U}\oplus\mathcal{W}. | Supposew |     | ,…,w |
1 m
|     | isabasisof\mathcal{W}. |                | Provethatw | +\mathcal{U},…,w |        | +\mathcal{U} isabasisof\mathcal{V}/\mathcal{U}. |                  |     |     |
| --- | ------------ | -------------- | ---------- | ------ | ------ | ----------------- | ---------------- | --- | --- |
|     |              |                |            | 1      |        | m                 |                  |     |     |
| 15  | Suppose\mathcal{U}     | isasubspaceof\mathcal{V} |            | andv   | +\mathcal{U},…,v |                   | +\mathcal{U} isabasisof\mathcal{V}/\mathcal{U} |     | and |
1 m
|     | ,…,u                   |              |     |            | ,…,v                     | ,u  | ,…,u         |     |     |
| --- | ---------------------- | ------------ | --- | ---------- | ------------------------ | --- | ------------ | --- | --- |
|     | u                      | isabasisof\mathcal{U}. |     | Provethatv |                          |     | isabasisof\mathcal{V}. |     |     |
|     | 1                      | n            |     |            | 1                        | m   | 1 n          |     |     |
| 16  | Suppose\phi\inℒ(\mathcal{V},\mathbf{F})and\phi\neq0. |              |     |            | Provethatdim\mathcal{V}/(null\phi)=1. |     |              |     |     |
17 Suppose \mathcal{U} is a subspace of \mathcal{V} such that dim\mathcal{V}/\mathcal{U} = 1. Prove that there
exists\phi\inℒ(\mathcal{V},\mathbf{F})suchthatnull\phi=\mathcal{U}.
18 Supposethat\mathcal{U} isasubspaceof\mathcal{V} suchthat\mathcal{V}/\mathcal{U} isfinite-dimensional.
|     | (a) Showthatif\mathcal{W} |     | isafinite-dimensionalsubspaceof\mathcal{V} |     |     |     | and\mathcal{V} | =\mathcal{U}+\mathcal{W}, |     |
| --- | --------------- | --- | -------------------------------- | --- | --- | --- | ---- | ----- | --- |
|     | thendim\mathcal{W}        |     | \geqdim\mathcal{V}/\mathcal{U}.                         |     |     |     |      |       |     |
$$(b) Provethatthereexistsafinite-dimensionalsubspace\mathcal{W} of\mathcal{V} suchthat$$
|     | dim\mathcal{W} | =dim\mathcal{V}/\mathcal{U} |     | and\mathcal{V} =\mathcal{U}\oplus\mathcal{W}. |     |     |     |     |     |
| --- | ---- | ------- | --- | ---------- | --- | --- | --- | --- | --- |
19 Suppose\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})and\mathcal{U} isasubspaceof\mathcal{V}. Let\pi denotethequotient
|     | mapfrom\mathcal{V} | onto\mathcal{V}/\mathcal{U}.     |     | Provethatthereexists\mathcal{S} |     |     | \in ℒ(\mathcal{V}/\mathcal{U},\mathcal{W})suchthat |     |     |
| --- | -------- | ------------ | --- | --------------------- | --- | --- | ------------------ | --- | --- |
|     | \mathcal{T} =\mathcal{S}\circ\pi   | ifandonlyif\mathcal{U} |     | \subseteqnull\mathcal{T}.               |     |     |                    |     |     |

| --- | --- | --- | --------- | ------- | --- |
### 3F Duality
| Dual Space | and Dual | Map |     |     |     |
| ---------- | -------- | --- | --- | --- | --- |
Linearmapsintothescalarfield\mathbf{F} playaspecialroleinlinearalgebra,andthus
theygetaspecialname.
| 3.108 definition: | linearfunctional |     |     |     |     |
| ----------------- | ---------------- | --- | --- | --- | --- |
Alinearfunctionalon\mathcal{V} isalinearmapfrom\mathcal{V} to\mathbf{F}. Inotherwords,alinear
functionalisanelementofℒ(\mathcal{V},\mathbf{F}).
linearfunctionals
**3.109 例：** | Define\phi∶ | \mathbf{R}3  |                      |                          |     |     |
| -------- | --- | -------------------- | ------------------------ | --- | --- |
| •        | \rightarrow\mathbf{R}  | by\phi(x,y,z)=4x-5y+2z. | Then\phiisalinearfunctional |     |     |
on\mathbf{R}3.
|              | \mathbf{F}n. | Define\phi∶ \mathbf{F}n |        |            |     |
| ------------ | --- | ----------- | ------ | ---------- | --- |
| • Fix(c ,…,c | ) \in | \rightarrow \mathbf{F} by\phi(x   | ,…,x ) | = c x +⋯+c | x . |
| 1            | n   |             | 1 n    | 1 1        | n n |
Then\phiisalinearfunctionalon\mathbf{F}n.
Define\phi∶
| •   | 𝒫(\mathbf{R})\rightarrow\mathbf{R} | by  |     |     |     |
| --- | ------ | --- | --- | --- | --- |
\phi(p)=3p″(5)+7p(4).
Then\phiisalinearfunctionalon𝒫(\mathbf{R}).
| • Define\phi∶ | 𝒫(\mathbf{R})\rightarrow\mathbf{R} | by  |     |     |     |
| ---------- | ------ | --- | --- | --- | --- |
|     |     | \phi(p)=\int | p   |     |     |
| --- | --- | ------ | --- | --- | --- |
| foreachp\in𝒫(\mathbf{R}). |     | Then\phiisalinearfunctionalon𝒫(\mathbf{R}). |     |     |     |
| -------------- | --- | ------------------------------- | --- | --- | --- |
Thevectorspaceℒ(\mathcal{V},\mathbf{F})alsogetsaspecialnameandspecialnotation.
| 3.110 definition: | dualspace,\mathcal{V}′ |     |     |     |     |
| ----------------- | ------------ | --- | --- | --- | --- |
Thedualspaceof\mathcal{V},denotedby\mathcal{V}′,isthevectorspaceofalllinearfunctionals
| on\mathcal{V}. Inotherwords,\mathcal{V}′ |       | =ℒ(\mathcal{V},\mathbf{F}). |     |     |     |
| -------------------- | ----- | -------- | --- | --- | --- |
| 3.111 dim\mathcal{V}′          | =dim\mathcal{V} |          |     |     |     |
Suppose\mathcal{V} isfinite-dimensional. Then\mathcal{V}′ isalsofinite-dimensionaland
dim\mathcal{V}′ =dim\mathcal{V}.
Proof By3.72wehave
dim\mathcal{V}′
=dimℒ(\mathcal{V},\mathbf{F})=(dim\mathcal{V})(dim\mathbf{F})=dim\mathcal{V},
asdesired.

| -------- | --- | ---------- | --- | --- | --- | --- |
Inthefollowingdefinition,thelinearmaplemma(3.4)impliesthateach\phi is
j
welldefined.
| 3.112 definition: | dualbasis |     |     |     |     |     |
| ----------------- | --------- | --- | --- | --- | --- | --- |
Ifv ,…,v isabasisof\mathcal{V},thenthedualbasisofv ,…,v isthelist\phi ,…,\phi
| 1 n |     |     |     |     | 1 n | 1 n |
| --- | --- | --- | --- | --- | --- | --- |
ofelementsof\mathcal{V}′,whereeach\phi
|     |     |     | j isthelinearfunctionalon\mathcal{V} |     |     | suchthat |
| --- | --- | --- | -------------------------- | --- | --- | -------- |
|     |     |     | ⎧ {1                       | ifk | =j, |          |
\phi(v )=
|     |     |     | j k ⎨ {0 | ifk | \neqj. |     |
| --- | --- | --- | -------- | --- | --- | --- |
⎩
|     | thedualbasisofthestandardbasisof |     |     |     | \mathbf{F}n  |     |
| --- | -------------------------------- | --- | --- | --- | --- | --- |
**3.113 例：** Suppose n is a positive integer. For 1 \leq j \leq n, define \phi to be the linear
j
functionalon\mathbf{F}n thatselectsthejth coordinateofavectorin\mathbf{F}n. Thus
|           |            |     | \phi(x ,…,x | )=x |     |     |
| --------- | ---------- | --- | -------- | --- | --- | --- |
|           |            |     | j 1      | n   | j   |     |
| foreach(x | ,…,x )\in\mathbf{F}n. |     |          |     |     |     |
1 n
| Lete ,…,e | bethestandardbasisof\mathbf{F}n. |     |          | Then |     |     |
| --------- | ----------------------- | --- | -------- | ---- | --- | --- |
| 1         | n                       |     |          |      |     |     |
|           |                         |     | ⎧ {1     | ifk  | =j, |     |
|           |                         |     | \phi(e )= ⎨ |      |     |     |
|           |                         |     | j k {0   | ifk  | \neqj. |     |
⎩
| ,…,\phi  |                                   |     |     |     | ,…,e | of\mathbf{F}n. |
| ----- | --------------------------------- | --- | --- | --- | ---- | ----- |
| Thus\phi | isthedualbasisofthestandardbasise |     |     |     |      |       |
| 1     | n                                 |     |     |     | 1 n  |       |
Thenextresultshowsthatthedualbasisofabasisof\mathcal{V} consistsofthelinear
functionalson\mathcal{V} thatgivethecoefficientsforexpressingavectorin\mathcal{V} asalinear
combinationofthebasisvectors.
3.114 dualbasisgivescoefficientsforlinearcombination
| Supposev | ,…,v | isabasisof\mathcal{V} | and\phi | ,…,\phi | isthedualbasis. | Then |
| -------- | ---- | ----------- | ---- | ---- | --------------- | ---- |
|          | 1 n  |             |      | 1    | n               |      |
|          |      | v=\phi         | (v)v | +⋯+\phi | (v)v            |      |
|          |      |             | 1 1  |      | n n             |      |
foreachv\in\mathcal{V}.
| Proof Supposev\in\mathcal{V}. |     | Thenthereexistc |     | ,…,c | \in\mathbf{F} suchthat |     |
| ----------------- | --- | --------------- | --- | ---- | ----------- | --- |
1 n
|       |     |     | v=c v | +⋯+c | v . |     |
| ----- | --- | --- | ----- | ---- | --- | --- |
| 3.115 |     |     | 1 1   |      | n n |     |
Ifj \in{1,…,n},thenapplying\phi tobothsidesoftheequationabovegives
j
\phi(v)=c.
|     |     |     | j   | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Substitutingthevaluesforc ,…,c givenbytheequationaboveinto3.115shows
1 n
| thatv=\phi (v)v | +⋯+\phi | (v)v | .   |     |     |     |
| ------------ | ---- | ---- | --- | --- | --- | --- |
| 1            | 1    | n    | n   |     |     |     |

| --- | --- | --- | --- | --- | --- | --------- | ------- |
Thenextresultshowsthatthedualbasisisindeedabasisofthedualspace.
Thustheterminology“dualbasis”isjustified.
3.116 dualbasisisabasisofthedualspace
Suppose\mathcal{V} isfinite-dimensional. Thenthedualbasisofabasisof\mathcal{V} isabasis
of\mathcal{V}′.
Proof Supposev ,…,v isabasisof\mathcal{V}. Let\phi ,…,\phi denotethedualbasis.
|     |     | 1   | n   |     | 1   | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Toshowthat\phi ,…,\phi isalinearlyindependentlistofelementsof\mathcal{V}′,suppose
|        |                | 1   | n   |     |     |     |     |
| ------ | -------------- | --- | --- | --- | --- | --- | --- |
| a ,…,a | \in\mathbf{F} aresuchthat |     |     |     |     |     |     |
1 n
+⋯+a
| 3.117 |     |     | a \phi |     | \phi =0. |     |     |
| ----- | --- | --- | --- | --- | ----- | --- | --- |
|       |     |     | 1   | 1   | n n   |     |     |
Now
|          |         |                     | (a \phi +⋯+a |     | \phi )(v )=a |     |             |
| -------- | ------- | ------------------- | --------- | --- | --------- | --- | ----------- |
|          |         |                     | 1 1       |     | n n k     | k   |             |
| foreachk | =1,…,n. | Thus3.117showsthata |           |     | =⋯=a      | =0. | Hence\phi ,…,\phi |
|          |         |                     |           |     | 1         | n   | 1 n         |
islinearlyindependent.
Because \phi ,…,\phi is a linearly independent list in \mathcal{V}′whose length equals
|       | 1   | n   |     |     |      |                        |     |
| ----- | --- | --- | --- | --- | ---- | ---------------------- | --- |
| dim\mathcal{V}′ |     |     |     |     | ,…,\phi | isabasisof\mathcal{V}′(see2.38). |     |
$$(by3.111),wecanconcludethat\phi$$
|     |     |     |     |     | 1   | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Inthedefinitionbelow,notethatif\mathcal{T} isalinearmapfrom\mathcal{V} to\mathcal{W} then\mathcal{T}′ isa
| linearmapfrom\mathcal{W}′ |             | to\mathcal{V}′.      |               |     |                  |     |           |
| --------------- | ----------- | ---------- | ------------- | --- | ---------------- | --- | --------- |
| 3.118           | definition: | dualmap,\mathcal{T}′ |               |     |                  |     |           |
| Suppose\mathcal{T}        | \inℒ(\mathcal{V},\mathcal{W}).    |            | Thedualmapof\mathcal{T} |     | isthelinearmap\mathcal{T}′ |     | \inℒ(\mathcal{W}′,\mathcal{V}′) |
definedforeach\phi\in\mathcal{W}′by
\mathcal{T}′(\phi)=\phi\circ\mathcal{T}.
If\mathcal{T} \inℒ(\mathcal{V},\mathcal{W})and\phi\in\mathcal{W}′,then\mathcal{T}′(\phi)isdefinedabovetobethecomposition
ofthelinearmaps\phiand\mathcal{T}. Thus\mathcal{T}′(\phi)isindeedalinearmapfrom\mathcal{V} to\mathbf{F};in
otherwords,\mathcal{T}′(\phi)\in\mathcal{V}′.
Thefollowingtwobulletpointsshowthat\mathcal{T}′ isalinearmapfrom\mathcal{W}′ to\mathcal{V}′.
| If\phi,\psi | \in\mathcal{W}′,then |     |     |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- | --- | --- |
•
|          | \mathcal{T}′(\phi+\psi)=(\phi+\psi)\circ\mathcal{T} |               |     | =\phi\circ\mathcal{T}+\psi\circ\mathcal{T} |           | =\mathcal{T}′(\phi)+\mathcal{T}′(\psi). |     |
| -------- | --------------- | ------------- | --- | -------- | --------- | ------------- | --- |
| • If \lambda\in\mathbf{F} | and\phi\in\mathcal{W}′,then    |               |     |          |           |               |     |
|          |                 | \mathcal{T}′(\lambda\phi)=(\lambda\phi)\circ\mathcal{T} |     |          | = \lambda(\phi\circ\mathcal{T})= | \lambda\mathcal{T}′(\phi).       |     |
Theprimenotationappearswithtwounrelatedmeaningsinthenextexample:
| \mathcal{D}′  |     |     |     |     |     | p′  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
denotes the dual of the linear map \mathcal{D}, and denotes the derivative of a
polynomialp.

| --- | -------- | ---------- | --- | --- | --- | --- | --- |
dualmapofthedifferentiationlinearmap
**3.119 例：** | Define\mathcal{D}∶ | 𝒫(\mathbf{R})\rightarrow𝒫(\mathbf{R})by\mathcal{D}p=p′. |     |     |     |     |     |     |
| -------- | ----------------- | --- | --- | --- | --- | --- | --- |
• Suppose \phi is the linear functional on 𝒫(\mathbf{R}) defined by \phi(p) = p(3). Then
\mathcal{D}′(\phi)isthelinearfunctionalon𝒫(\mathbf{R})givenby
$$(\mathcal{D}′(\phi))(p)=(\phi\circ\mathcal{D})(p)=\phi(\mathcal{D}p)=\phi(p′)=p′(3).$$
Thus\mathcal{D}′(\phi)isthelinearfunctionalon𝒫(\mathbf{R})takingptop′(3).
| Suppose | is  | the linear | functional | on  | 𝒫(\mathbf{R}) defined | by   | 1p. Then |
| ------- | --- | ---------- | ---------- | --- | ------------ | ---- | -------- |
| •       | \phi   |            |            |     |              | \phi(p) | = \int      |
\mathcal{D}′(\phi)isthelinearfunctionalon𝒫(\mathbf{R})givenby
$$(\mathcal{D}′(\phi))(p)=(\phi\circ\mathcal{D})(p)$$
=\phi(\mathcal{D}p)
=\phi(p′)
|     |     |     |     |     | =\int p′ |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- |
=p(1)-p(0).
Thus\mathcal{D}′(\phi)isthelinearfunctionalon𝒫(\mathbf{R})takingptop(1)-p(0).
Inthenextresult,(a)and(b)implythatthefunctionthattakes\mathcal{T} to\mathcal{T}′ isa
linearmapfromℒ(\mathcal{V},\mathcal{W})toℒ(\mathcal{W}′,\mathcal{V}′).
In(c)below,notethereversaloforderfrom\mathcal{S}\mathcal{T} ontheleftto\mathcal{T}′\mathcal{S}′ontheright.
3.120 algebraicpropertiesofdualmaps
| Suppose\mathcal{T}   | \inℒ(\mathcal{V},\mathcal{W}). |                 | Then            |     |     |     |     |
| ---------- | -------- | --------------- | --------------- | --- | --- | --- | --- |
| (a) (\mathcal{S}+\mathcal{T})′ | =\mathcal{S}′+\mathcal{T}′   |                 | forall\mathcal{S}\inℒ(\mathcal{V},\mathcal{W}); |     |     |     |     |
| (b) (\lambda\mathcal{T})′  | = \lambda\mathcal{T}′    | forall          | \lambda\in\mathbf{F};            |     |     |     |     |
| (c) (\mathcal{S}\mathcal{T})′  | =\mathcal{T}′\mathcal{S}′    | forall\mathcal{S}\inℒ(\mathcal{W},\mathcal{U}). |                 |     |     |     |     |
Proof Theproofsof(a)and(b)arelefttothereader.
Toprove(c),suppose\phi\in\mathcal{U}′.
Then
| (\mathcal{S}\mathcal{T})′(\phi)=\phi\circ(\mathcal{S}\mathcal{T})=(\phi\circ\mathcal{S})\circ\mathcal{T} |        |         |            | =\mathcal{T}′(\phi\circ\mathcal{S})=\mathcal{T}′(\mathcal{S}′(\phi))=(\mathcal{T}′\mathcal{S}′)(\phi), |                          |         |               |
| ----------------------- | ------ | ------- | ---------- | ----------------------------- | ------------------------ | ------- | ------------- |
| where the               | first, | third,  | and fourth | equal-                        |                          |         | ∗             |
|                         |        |         |            |                               | Somebooksusethenotation\mathcal{V} |         | and           |
| ities above             | hold   | because | of         | the defini-                   | ∗                        |         |               |
|                         |        |         |            |                               | \mathcal{T} for duality            | instead | of \mathcal{V}′ and \mathcal{T}′. |
tionofthedualmap,thesecondequality However,herewereservethenotation
holdsbecausecompositionoffunctions ∗fortheadjoint,whichwillbeintro\mathcal{T}
is associative, and the last equality fol- ducedwhenwestudylinearmapson
lowsfromthedefinitionofcomposition. innerproductspacesin Chapter 7.
| The       | equation    | above | shows   | that    |     |     |     |
| --------- | ----------- | ----- | ------- | ------- | --- | --- | --- |
| (\mathcal{S}\mathcal{T})′(\phi)  | = (\mathcal{T}′\mathcal{S}′)(\phi) |       | for all | \phi \in \mathcal{U}′. |     |     |     |
| Thus(\mathcal{S}\mathcal{T})′ | =\mathcal{T}′\mathcal{S}′.      |       |         |         |     |     |     |

Section3F Duality 109
Null Space and Range of Dual of Linear Map
Ourgoalinthissubsectionistodescribenull\mathcal{T}′ andrange\mathcal{T}′ intermsofrange\mathcal{T}
andnull\mathcal{T}. Todothis,wewillneedthenextdefinition.
**3.121 定义：** annihilator,\mathcal{U}0
For\mathcal{U} \subseteq\mathcal{V},theannihilator of\mathcal{U},denotedby\mathcal{U}0,isdefinedby
\mathcal{U}0 ={\phi\in\mathcal{V}′ ∶\phi(u)=0forallu\in\mathcal{U}}.
**3.122 例：** elementofanannihilator
Suppose\mathcal{U} isthesubspaceof𝒫(\mathbf{R})consistingofpolynomialmultiplesofx2.
If\phiisthelinearfunctionalon𝒫(\mathbf{R})definedby\phi(p)=p′(0),then\phi\in\mathcal{U}0.
For \mathcal{U} \subseteq \mathcal{V}, the annihilator \mathcal{U}0 is a subset of the dual space \mathcal{V}′. Thus \mathcal{U}0
dependsonthevectorspacecontaining\mathcal{U},soanotationsuchas\mathcal{U}0 wouldbe
\mathcal{V}
moreprecise. However,thecontainingvectorspacewillalwaysbeclearfromthe
context,sowewillusethesimplernotation\mathcal{U}0.
**3.123 例：** theannihilatorofatwo-dimensionalsubspaceof \mathbf{R}5
Let e ,e ,e ,e ,e denote the standard basis of \mathbf{R}5; let \phi ,\phi ,\phi ,\phi ,\phi \in
1 2 3 4 5 1 2 3 4 5
$$(\mathbf{R}5) ′ denotethedualbasisofe ,e ,e ,e ,e . Suppose$$
1 2 3 4 5
\mathcal{U} =span(e ,e )={(x ,x ,0,0,0)\in\mathbf{R}5 ∶x ,x \in\mathbf{R}}.
1 2 1 2 1 2
Wewanttoshowthat\mathcal{U}0 =span(\phi ,\phi ,\phi ).
3 4 5
Recall (see 3.113) that \phi is the linear functional on \mathbf{R}5 that selects the jth
j
coordinate: \phi(x ,x ,x ,x ,x )=x.
j 1 2 3 4 5 j
Firstsuppose\phi\inspan(\phi ,\phi ,\phi ). Thenthereexistc ,c ,c \in\mathbf{R} suchthat
3 4 5 3 4 5
\phi=c \phi +c \phi +c \phi . If(x ,x ,0,0,0)\in\mathcal{U},then
3 3 4 4 5 5 1 2
\phi(x ,x ,0,0,0)=(c \phi +c \phi +c \phi )(x ,x ,0,0,0)=0.
1 2 3 3 4 4 5 5 1 2
Thus\phi\in\mathcal{U}0. Hencewehaveshownthatspan(\phi ,\phi ,\phi )\subseteq\mathcal{U}0.
3 4 5
To show the inclusion in the other direction, suppose that \phi \in \mathcal{U}0. Becausethedualbasisisabasisof(\mathbf{R}5) ′ ,thereexistc ,c ,c ,c ,c \in\mathbf{R} suchthat
1 2 3 4 5
\phi=c \phi +c \phi +c \phi +c \phi +c \phi . Becausee \in\mathcal{U} and\phi\in\mathcal{U}0,wehave
1 1 2 2 3 3 4 4 5 5 1
$$0=\phi(e )=(c \phi +c \phi +c \phi +c \phi +c \phi )(e )=c .$$
1 1 1 2 2 3 3 4 4 5 5 1 1
Similarly, e \in \mathcal{U} and thus c = 0. Hence \phi = c \phi + c \phi + c \phi . Thus
2 2 3 3 4 4 5 5
\phi\inspan(\phi ,\phi ,\phi ),whichshowsthat\mathcal{U}0 \subseteqspan(\phi ,\phi ,\phi ).
3 4 5 3 4 5
Thus\mathcal{U}0 =span(\phi ,\phi ,\phi ).
3 4 5

| --- | -------- | --- | ---------- | --- | --- | --- | --- | --- |
theannihilatorisasubspace
3.124
| Suppose\mathcal{U} |     | \subseteq\mathcal{V}. Then\mathcal{U}0 | isasubspaceof\mathcal{V}′. |     |     |     |     |     |
| -------- | --- | ---------- | ---------------- | --- | --- | --- | --- | --- |
Proof Notethat0\in\mathcal{U}0 (here0isthezerolinearfunctionalon\mathcal{V})becausethe
| zerolinearfunctionalappliedtoeveryvectorin\mathcal{U} |     |     |     |     |     | equals0\in\mathbf{F}. |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- |
Suppose\phi,\psi \in \mathcal{U}0. Thus\phi,\psi \in \mathcal{V}′ and\phi(u) = \psi(u) = 0foreveryu \in \mathcal{U}.
Ifu\in\mathcal{U},then
$$(\phi+\psi)(u)=\phi(u)+\psi(u)=0+0=0.$$
| Thus\phi+\psi |     | \in\mathcal{U}0. |     |     |     |     |     |     |
| ------- | --- | ---- | --- | --- | --- | --- | --- | --- |
Similarly,\mathcal{U}0 isclosedunderscalarmultiplication. Thus1.34impliesthat\mathcal{U}0
isasubspaceof\mathcal{V}′.
Thenextresultshowsthatdim\mathcal{U}0
|     |     |     |     | isthedifferenceofdim\mathcal{V} |     |     | anddim\mathcal{U}. | For |
| --- | --- | --- | --- | --------------------- | --- | --- | -------- | --- |
example,thisshowsthatif\mathcal{U} isatwo-dimensionalsubspaceof\mathbf{R}5,then\mathcal{U}0 isa
| three-dimensionalsubspaceof(\mathbf{R}5) |     |     |     | ′   |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
,asin Example3.123.
Thenextresultcanbeprovedfollowingthepatternof Example3.123: choosea
| basisu                              | ,…,u | of\mathcal{U},extendtoabasisu |     | ,…,u | ,…,u | of\mathcal{V},let\phi           | ,…,\phi | ,…,\phi |
| ----------------------------------- | ---- | ------------------- | --- | ---- | ---- | ------------------ | ---- | ---- |
|                                     | 1    | m                   |     | 1    | m    | n                  | 1    | m n  |
| bethedualbasisof\mathcal{V}′,andthenshowthat\phi |      |                     |     |      | ,…,\phi | isabasisof\mathcal{U}0,which |      |      |
|                                     |      |                     |     |      | m+1  | n                  |      |      |
implies the desired result. You should construct the proof just outlined, even
thoughaslickerproofispresentedhere.
3.125 dimensionoftheannihilator
| Suppose\mathcal{V} |     | isfinite-dimensionaland\mathcal{U} |     | isasubspaceof\mathcal{V}. |     |     | Then |     |
| -------- | --- | ------------------------ | --- | --------------- | --- | --- | ---- | --- |
dim\mathcal{U}0
=dim\mathcal{V}-dim\mathcal{U}.
Proof Let i \in ℒ(\mathcal{U},\mathcal{V}) be the inclusion map defined by i(u) = u for each
|                       | Thusi′ | isalinearmapfrom\mathcal{V}′ |                      | to\mathcal{U}′. |                               |     |     |     |
| --------------------- | ------ | ------------------ | -------------------- | ----- | ----------------------------- | --- | --- | --- |
| u\in\mathcal{U}.                  |        |                    |                      |       | Thefundamentaltheoremoflinear |     |     |     |
| maps(3.21)appliedtoi′ |        |                    | showsthat            |       |                               |     |     |     |
|                       |        |                    | dimrangei′+dimnulli′ |       | =dim\mathcal{V}′.                       |     |     |     |
|                       | nulli′ |                    | \mathcal{U}0                   |       |                               |     |     |     |
However, = (as can be seen by thinking about the definitions) and
| dim\mathcal{V}′ | =dim\mathcal{V} | (by3.111),sowecanrewritetheequationaboveas |                  |     |        |     |     |     |
| ----- | ----- | ------------------------------------------ | ---------------- | --- | ------ | --- | --- | --- |
| 3.126 |       |                                            | dimrangei′+dim\mathcal{U}0 |     | =dim\mathcal{V}. |     |     |     |
If \phi \in \mathcal{U}′, then \phi can be extended to a linear functional \psi on \mathcal{V} (see, for
example,Exercise13in Section3A).Thedefinitionofi′ showsthati′(\psi)=\phi.
| Thus\phi\inrangei′,whichimpliesthatrangei′ |     |     |            |        | =\mathcal{U}′. | Hence |     |     |
| ------------------------------------- | --- | --- | ---------- | ------ | ---- | ----- | --- | --- |
|                                       |     |     | dimrangei′ | =dim\mathcal{U}′ |      |       |     |     |
=dim\mathcal{U},
| andthen3.126becomestheequationdim\mathcal{U}+dim\mathcal{U}0 |     |     |     |     |     | =dim\mathcal{V},asdesired. |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | ---------------- | --- | --- |

| --- | --- | --- | --- | --------- | --- | ------- | --- |
The next result can be a useful tool to show that a subspace is as big as
possible—see(a)—ortoshowthatasubspaceisassmallaspossible—see(b).
3.127 conditionfortheannihilatortoequal{0}orthewholespace
| Suppose\mathcal{V} isfinite-dimensionaland\mathcal{U} |     |     | isasubspaceof\mathcal{V}. |     |     | Then |     |
| --------------------------------- | --- | --- | --------------- | --- | --- | ---- | --- |
| (a) \mathcal{U}0                            | =\mathcal{V}; |     |                 |     |     |      |     |
={0} ⟺ \mathcal{U}
| (b) \mathcal{U}0 =\mathcal{V}′ | ⟺ \mathcal{U} ={0}. |     |     |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- | --- | --- |
Proof Toprove(a),wehave
|     | \mathcal{U}0  | ={0} ⟺ | dim\mathcal{U}0 | =0    |     |     |     |
| --- | --- | ------ | ----- | ----- | --- | --- | --- |
|     |     | ⟺      | dim\mathcal{U}  | =dim\mathcal{V} |     |     |     |
=\mathcal{V},
⟺ \mathcal{U}
wherethesecondequivalencefollowsfrom3.125andthethirdequivalencefollows
from2.39.
Similarly,toprove(b)wehave
|     | \mathcal{U}0  | =\mathcal{V}′ | dim\mathcal{U}0 | =dim\mathcal{V}′ |     |     |     |
| --- | --- | --- | ----- | ------ | --- | --- | --- |
⟺
|     |     |     | dim\mathcal{U}0 | =dim\mathcal{V} |     |     |     |
| --- | --- | --- | ----- | ----- | --- | --- | --- |
⟺
|     |     | ⟺   | dim\mathcal{U}    | =0  |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- |
|     |     | ⟺   | \mathcal{U} ={0}, |     |     |     |     |
whereonedirectionofthefirstequivalencefollowsfrom2.39,thesecondequivalencefollowsfrom3.111,andthethirdequivalencefollowsfrom3.125.
Theproofof(a)inthenextresultdoesnotusethehypothesisthat\mathcal{V} and\mathcal{W}
arefinite-dimensional.
3.128 thenullspaceof\mathcal{T}′
| Suppose\mathcal{V} and\mathcal{W}      | arefinite-dimensionaland\mathcal{T} |     |     | \inℒ(\mathcal{V},\mathcal{W}). |     | Then |     |
| ------------------ | ------------------------- | --- | --- | -------- | --- | ---- | --- |
| null\mathcal{T}′ =(range\mathcal{T})0; |                           |     |     |          |     |      |     |
$$(a)$$
| (b) dimnull\mathcal{T}′ | =dimnull\mathcal{T}+dim\mathcal{W}-dim\mathcal{V}. |     |     |     |     |     |     |
| ------------- | -------------------- | --- | --- | --- | --- | --- | --- |
Proof
| (a) Firstsuppose\phi\innull\mathcal{T}′. |     | Thus0=\mathcal{T}′(\phi)=\phi\circ\mathcal{T}. |     |     | Hence |     |     |
| ------------------------- | --- | ---------------- | --- | --- | ----- | --- | --- |
foreveryv\in\mathcal{V}.
$$0=(\phi\circ\mathcal{T})(v)=\phi(\mathcal{T}v)$$
| Thus\phi\in(range\mathcal{T})0. |     | Thisimpliesthatnull\mathcal{T}′ |     |     | \subseteq(range\mathcal{T})0. |     |     |
| ---------------- | --- | --------------------- | --- | --- | ----------- | --- | --- |
Toprovetheinclusionintheoppositedirection,nowsuppose\phi\in(range\mathcal{T})0.
=\mathcal{T}′(\phi).
| Thus\phi(\mathcal{T}v)=0foreveryvectorv\in\mathcal{V}. |     |     |     | Hence0=\phi\circ\mathcal{T} |     |     | Inother |
| ----------------------------- | --- | --- | --- | ---------- | --- | --- | ------- |
words, \phi \in null\mathcal{T}′, whichshowsthat(range\mathcal{T})0 \subseteq null\mathcal{T}′, completingthe
proofof(a).

| -------- | ---------- | --- | --- |
$$(b) Wehave$$
dimnull\mathcal{T}′ =dim(range\mathcal{T})0
=dim\mathcal{W}-dimrange\mathcal{T}
=dim\mathcal{W}-(dim\mathcal{V}-dimnull\mathcal{T})
=dimnull\mathcal{T}+dim\mathcal{W}-dim\mathcal{V},
where the first equality comes from (a), the second equality comes from
3.125,andthethirdequalitycomesfromthefundamentaltheoremoflinear
maps(3.21).
Thenextresultcanbeusefulbecausesometimesitiseasiertoverifythat\mathcal{T}′
| isinjectivethantoshowdirectlythat\mathcal{T} |                                | issurjective.   |      |
| ---------------------------------- | ------------------------------ | --------------- | ---- |
| 3.129 \mathcal{T}                            | surjectiveisequivalentto\mathcal{T}′     | injective       |      |
| Suppose\mathcal{V}                           | and\mathcal{W} arefinite-dimensionaland\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}).        | Then |
|                                    | \mathcal{T} issurjective ⟺               | \mathcal{T}′ isinjective. |      |
|     | \mathcal{T} \inℒ(\mathcal{V},\mathcal{W})issurjective | ⟺ range\mathcal{T}    | =\mathcal{W}   |
| --- | --------------------- | ----------- | ---- |
|     |                       | ⟺ (range\mathcal{T})0 | ={0} |
|     |                       | ⟺ null\mathcal{T}′    | ={0} |
⟺ \mathcal{T}′ isinjective,
where the second equivalence comes from 3.127(a) and the third equivalence
comesfrom3.128(a).
therangeof\mathcal{T}′
3.130
| Suppose\mathcal{V}       | and\mathcal{W} arefinite-dimensionaland\mathcal{T} | \inℒ(\mathcal{V},\mathcal{W}). | Then |
| -------------- | ------------------------------ | -------- | ---- |
| (a) dimrange\mathcal{T}′ | =dimrange\mathcal{T};                    |          |      |
| (b) range\mathcal{T}′    | =(null\mathcal{T})0.                     |          |      |
Proof
$$(a) Wehave$$
|     | dimrange\mathcal{T}′ =dim\mathcal{W}′-dimnull\mathcal{T}′ |     |     |
| --- | --------------------------- | --- | --- |
=dim\mathcal{W}-dim(range\mathcal{T})0
=dimrange\mathcal{T},
wherethefirstequalitycomesfrom3.21,thesecondequalitycomesfrom
3.111and3.128(a),andthethirdequalitycomesfrom3.125.

| --- | --- | --- | --- | --------- | --- | ------- | --- |
|                   |     | range\mathcal{T}′. |                  |     | \mathcal{W}′  |           | \mathcal{T}′(\psi). |
| ----------------- | --- | -------- | ---------------- | --- | --- | --------- | ------ |
| (b) Firstsuppose\phi |     | \in        | Thusthereexists\psi |     | \in   | suchthat\phi | =      |
Ifv\innull\mathcal{T},then
\phi(v)=(\mathcal{T}′(\psi))v=(\psi\circ\mathcal{T})(v)=\psi(\mathcal{T}v)=\psi(0)=0.
| Hence\phi\in(null\mathcal{T})0.                           |     |     | Thisimpliesthatrange\mathcal{T}′ |     | \subseteq(null\mathcal{T})0.  |     |     |
| ------------------------------------------ | --- | --- | ---------------------- | --- | ----------- | --- | --- |
| Wewillcompletetheproofbyshowingthatrange\mathcal{T}′ |     |     |                        |     | and(null\mathcal{T})0 |     |     |
havethe
| samedimension. |     | Todothis,notethat |     |     |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- | --- | --- |
dimrange\mathcal{T}′
=dimrange\mathcal{T}
=dim\mathcal{V}-dimnull\mathcal{T}
=dim(null\mathcal{T})0,
wherethefirstequalitycomesfrom(a),thesecondequalitycomesfrom3.21,
andthethirdequalitycomesfrom3.125.
Thenextresultshouldbecomparedto3.129.
| 3.131    | \mathcal{T} injectiveisequivalentto\mathcal{T}′ |                           | surjective |               |     |      |     |
| -------- | --------------------------- | ------------------------- | ---------- | ------------- | --- | ---- | --- |
| Suppose\mathcal{V} | and\mathcal{W}                        | arefinite-dimensionaland\mathcal{T} |            | \inℒ(\mathcal{V},\mathcal{W}).      |     | Then |     |
|          |                             | isinjective               | \mathcal{T}′         | issurjective. |     |      |     |
|          |                             | \mathcal{T}                         | ⟺          |               |     |      |     |
|     |     | \mathcal{T} isinjective | ⟺ null\mathcal{T}    | ={0} |      |     |     |
| --- | --- | ------------- | ---------- | ---- | ---- | --- | --- |
|     |     |               | ⟺ (null\mathcal{T})0 |      | =\mathcal{V}′  |     |     |
|     |     |               | ⟺ range\mathcal{T}′  |      | =\mathcal{V}′, |     |     |
wherethesecondequivalencefollowsfrom3.127(b)andthethirdequivalence
followsfrom3.130(b).
| Matrix | of Dual | of Linear | Map |     |     |     |     |
| ------ | ------- | --------- | --- | --- | --- | --- | --- |
Thesettingforthenextresultistheassumptionthatwehaveabasisv ,…,v
|                            |     |     |            |                        |     |     | 1 n  |
| -------------------------- | --- | --- | ---------- | ---------------------- | --- | --- | ---- |
| of\mathcal{V},alongwithitsdualbasis\phi |     |     | ,…,\phi of\mathcal{V}′. | Wealsohaveabasisw      |     |     | ,…,w |
|                            |     |     | 1 n        |                        |     |     | 1 m  |
| of\mathcal{W},alongwithitsdualbasis\psi |     |     | ,…,\psi of\mathcal{W}′. | Thusℳ(\mathcal{T})iscomputedwith |     |     |      |
|                            |     |     | 1 m        |                        |     |     |      |
respecttothebasesjustmentionedof\mathcal{V} and\mathcal{W},andℳ(\mathcal{T}′)iscomputedwith
respecttothedualbasesjustmentionedof\mathcal{W}′ and\mathcal{V}′. Usingthesebasesgives
thefollowingprettyresult.
|     | matrixof | \mathcal{T}′ istransposeofmatrixof |     | \mathcal{T}   |     |     |     |
| --- | -------- | ------------------------ | --- | --- | --- | --- | --- |
3.132
| Suppose\mathcal{V} | and\mathcal{W} | arefinite-dimensionaland\mathcal{T} |     | \inℒ(\mathcal{V},\mathcal{W}). |     | Then |     |
| -------- | ---- | ------------------------- | --- | -------- | --- | ---- | --- |
t
|     |     |     | ℳ(\mathcal{T}′)=(ℳ(\mathcal{T})) | .   |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- |

| -------- | ---------- | --- | --- | --- |
=ℳ(\mathcal{T}′).
| Proof Let\mathcal{A}=ℳ(\mathcal{T})and\mathcal{C} |     | Suppose1\leqj | \leqmand1\leqk | \leqn. |
| ------------------- | --- | ---------- | -------- | --- |
Fromthedefinitionofℳ(\mathcal{T}′)wehave
n
\mathcal{T}′(\psi)=
\sum\mathcal{C} r,j \phi .
|     | j   | r   |     |     |
| --- | --- | --- | --- | --- |
$$r=1$$
Theleftsideoftheequationaboveequals\psi \circ\mathcal{T}. Thusapplyingbothsidesofthe
j
| equationabovetov | gives |     |     |     |
| ---------------- | ----- | --- | --- | --- |
k
n
|     | (\psi \circ\mathcal{T})(v | )= \sum\mathcal{C} \phi | (v ) |     |
| --- | -------- | ------- | ---- | --- |
|     | j k      | r,j     | r k  |     |
$$r=1$$
=\mathcal{C} .
k,j
Wealsohave
|     | (\psi \circ\mathcal{T})(v )=\psi(\mathcal{T}v | )   |     |     |
| --- | --------------- | --- | --- | --- |
|     | j k             | j k |     |     |
m
|     |     | =\psi(\sum\mathcal{A} | w )   |     |
| --- | --- | ----- | ----- | --- |
|     |     | j     | r,k r |     |
$$r=1$$
m
|     |     | = \sum\mathcal{A} r,k \psi(w | )   |     |
| --- | --- | ------------ | --- | --- |
|     |     |              | j r |     |
$$r=1$$
=\mathcal{A} j,k .
Comparing the last line of the last two sets of equations, we have \mathcal{C} = \mathcal{A} .
k,j j,k
t,asdesired.
Thus\mathcal{C} =\mathcal{A}t. Inotherwords,ℳ(\mathcal{T}′)=(ℳ(\mathcal{T}))
Now we use duality to give an alternative proof that the column rank of a
matrixequalstherowrankofthematrix. Thisresultwaspreviouslyprovedusing
differenttools—see3.57.
3.133 columnrankequalsrowrank
Suppose\mathcal{A}\in\mathbf{F}m,n.
Thenthecolumnrankof\mathcal{A}equalstherowrankof\mathcal{A}.
Proof Define\mathcal{T}∶ \mathbf{F}n,1 \rightarrow \mathbf{F}m,1 by\mathcal{T}x = \mathcal{A}x. Thusℳ(\mathcal{T}) = \mathcal{A},whereℳ(\mathcal{T})is
| computedwithrespecttothestandardbasesof\mathbf{F}n,1 |     |     | and\mathbf{F}m,1. |     |
| ------------------------------------------- | --- | --- | -------- | --- |
Now
columnrankof\mathcal{A}=columnrankofℳ(\mathcal{T})
=dimrange\mathcal{T}
=dimrange\mathcal{T}′
=columnrankofℳ(\mathcal{T}′)
=columnrankof\mathcal{A}t
=rowrankof\mathcal{A},
wherethesecondequalitycomesfrom3.78,thethirdequalitycomesfrom3.130(a),
thefourthequalitycomesfrom3.78,thefifthequalitycomesfrom3.132,andthe
lastequalityfollowsfromthedefinitionsofrowandcolumnrank.
See Exercise8in Section7Aforanotheralternativeproofoftheresultabove.

| --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --- |
| Exercises |     | 3F  |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 Explainwhyeachlinearfunctionalissurjectiveoristhezeromap.
Givethreedistinctexamplesoflinearfunctionalson\mathbf{R}[0,1].
3 Suppose\mathcal{V} isfinite-dimensionalandv \in \mathcal{V} withv \neq 0. Provethatthere
|     | exists\phi\in\mathcal{V}′ |     | suchthat\phi(v)=1. |     |     |     |     |     |     |
| --- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
4 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{U} isasubspaceof\mathcal{V} suchthat\mathcal{U} \neq\mathcal{V}.
Provethatthereexists\phi\in\mathcal{V}′suchthat\phi(u)=0foreveryu\in\mathcal{U}but\phi\neq0.
| 5   | Suppose\mathcal{T}                     | \inℒ(\mathcal{V},\mathcal{W})andw |     |             | ,…,w | isabasisofrange\mathcal{T}. |             | Henceforeach |     |
| --- | ---------------------------- | ----------- | --- | ----------- | ---- | ----------------- | ----------- | ------------ | --- |
|     |                              |             |     | 1           | m    |                   |             |              |     |
|     | v\in\mathcal{V},thereexistuniquenumbers\phi |             |     |             |      | (v),…,\phi           | (v)suchthat |              |     |
|     |                              |             |     |             | 1    |                   | m           |              |     |
|     |                              |             |     |             | +⋯+\phi |                   | ,           |              |     |
|     |                              |             |     | \mathcal{T}v=\phi 1 (v)w | 1    | m (v)w            | m           |              |     |
,…,\phi
|     | thus defining |      | functions | \phi                       | from | \mathcal{V} to | \mathbf{F}. Show | that each | of the |
| --- | ------------- | ---- | --------- | ----------------------- | ---- | ---- | ------- | --------- | ------ |
|     |               |      |           | 1                       | m    |      |         |           |        |
|     | functions\phi    | ,…,\phi |           | isalinearfunctionalon\mathcal{V}. |      |      |         |           |        |
|     |               | 1    | m         |                         |      |      |         |           |        |
6 Suppose \phi,\beta \in \mathcal{V}′. Prove that null\phi \subseteq null\beta if and only if there exists
|     | c \in\mathbf{F} suchthat\beta=c\phi. |       |                              |                  |     |                          |     |        |        |
| --- | ------------------ | ----- | ---------------------------- | ---------------- | --- | ------------------------ | --- | ------ | ------ |
| 7   | Supposethat\mathcal{V}       |       | ,…,\mathcal{V}                         | arevectorspaces. |     | Provethat(\mathcal{V}              |     | \times⋯\times\mathcal{V}   | )′ and |
|     |                    |       | 1                            | m                |     |                          |     | 1      | m      |
|     | ′\times⋯\times\mathcal{V}              |       | ′ areisomorphicvectorspaces. |                  |     |                          |     |        |        |
|     | \mathcal{V} 1                | m     |                              |                  |     |                          |     |        |        |
|     |                    | ,…,v  |                              |                  |     | ,…,\phi isthedualbasisof\mathcal{V}′. |     |        |        |
| 8   | Supposev           |       | isabasisof\mathcal{V}and\phi              |                  |     |                          |     |        | Define |
|     |                    | 1     | n                            |                  |     | 1 n                      |     |        |        |
|     | Γ∶ \mathcal{V} \rightarrow\mathbf{F}n           | and\Lambda∶ | \mathbf{F}n                           | \rightarrow\mathcal{V} by            |     |                          |     |        |        |
|     | Γ(v)=(\phi            |       | (v),…,\phi                      | (v))             | and | \Lambda(a ,…,a                 | )=a | v +⋯+a | v .    |
|     |                    |       | 1                            | n                |     | 1                        | n   | 1 1    | n n    |
ExplainwhyΓand\Lambdaareinversesofeachother.
Suppose is a positive integer. Show that the dual basis of the basis
| 9   |          | m   |        |     |      |        |     |     |     |
| --- | -------- | --- | ------ | --- | ---- | ------ | --- | --- | --- |
|     | 1,x,…,xm | of𝒫 | (\mathbf{R})is\phi | ,\phi  | ,…,\phi | ,where |     |     |     |
|     |          |     | m      | 0 1 | m    |        |     |     |     |
p(k)(0)
|     |     |     |     | \phi   | (p)= | .   |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     |     |     | k    | k!  |     |     |     |
Herep(k)denotesthekthderivativeof p,withtheunderstandingthatthe0th
|     | derivativeof |     | pisp. |     |     |     |     |     |     |
| --- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
10 Supposemisapositiveinteger.
|     | (a) Showthat1,x-5,…,(x-5)m |     |     |     | isabasisof𝒫 |     | (\mathbf{R}). |     |     |
| --- | -------------------------- | --- | --- | --- | ----------- | --- | ---- | --- | --- |
m
$$(b) Whatisthedualbasisofthebasisin(a)?$$
11 Supposev ,…,v isabasisof\mathcal{V} and\phi ,…,\phi isthecorrespondingdual
|     |            | 1        | n   |                |     | 1   | n   |     |     |
| --- | ---------- | -------- | --- | -------------- | --- | --- | --- | --- | --- |
|     | basisof\mathcal{V}′. | Suppose\psi |     | \in\mathcal{V}′. Provethat |     |     |     |     |     |
+⋯+\psi(v
|     |     |     |     | \psi =\psi(v | )\phi  |     | )\phi . |     |     |
| --- | --- | --- | --- | ------ | --- | --- | ---- | --- | --- |
|     |     |     |     |        | 1 1 |     | n n  |     |     |

| -------- | --- | ---------- | --- | --- | --- | --- | --- |
| 12 Suppose\mathcal{S},\mathcal{T}       | \inℒ(\mathcal{V},\mathcal{W}). |     |         |      |     |     |     |
| ------------------- | -------- | --- | ------- | ---- | --- | --- | --- |
| (a) Provethat(\mathcal{S}+\mathcal{T})′ |          |     | =\mathcal{S}′+\mathcal{T}′. |      |     |     |     |
| Provethat(\lambda\mathcal{T})′      |          |     | \lambda\mathcal{T}′     |      |     |     |     |
| (b)                 |          | =   | forall  | \lambda\in\mathbf{F}. |     |     |     |
Thisexerciseasksyoutoverify(a)and(b)in3.120.
13 Showthatthedualmapoftheidentityoperatoron\mathcal{V} istheidentityoperator
on\mathcal{V}′.
| 14 Define\mathcal{T}∶ | \mathbf{R}3 \rightarrow\mathbf{R}2 | by  |     |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- | --- |
\mathcal{T}(x,y,z)=(4x+5y+6z,7x+8y+9z).
Suppose \phi ,\phi denotes the dual basis of the standard basis of \mathbf{R}2 and
1 2
| \psi ,\psi ,\psi                              | denotesthedualbasisofthestandardbasisof\mathbf{R}3. |          |                          |     |          |       |     |
| ------------------------------------ | ------------------------------------------ | -------- | ------------------------ | --- | -------- | ----- | --- |
| 1 2                                  | 3                                          |          |                          |     |          |       |     |
| (a) Describethelinearfunctionals\mathcal{T}′(\phi |                                            |          |                          |     | )and\mathcal{T}′(\phi | ).    |     |
| (b) Write\mathcal{T}′(\phi                        |                                            | )and\mathcal{T}′(\phi | )aslinearcombinationsof\psi |     |          | ,\psi ,\psi | .   |
|                                      |                                            | 1        | 2                        |     |          | 1 2 3 |     |
| 15 Define\mathcal{T}∶                          | 𝒫(\mathbf{R})\rightarrow𝒫(\mathbf{R})by                                |          |                          |     |          |       |     |
$$(\mathcal{T}p)(x)=x2p(x)+p″(x)$$
| foreachx    | \in\mathbf{R}. |       |            |     |             |          |            |
| ----------- | --- | ----- | ---------- | --- | ----------- | -------- | ---------- |
|             |     | 𝒫(\mathbf{R})′ |            |     | \phi(p)=p′(4). |          |            |
| (a) Suppose | \phi   | \in     | is defined |     | by          | Describe | the linear |
functional\mathcal{T}′(\phi)on𝒫(\mathbf{R}).
$$(b) Suppose\phi\in𝒫(\mathbf{R})′ isdefinedby\phi(p)=\int 1p. Evaluate(\mathcal{T}′(\phi))(x3).$$
| Suppose\mathcal{W} | isfinite-dimensionaland\mathcal{T} |     |     |     | \inℒ(\mathcal{V},\mathcal{W}). | Provethat |     |
| -------- | ------------------------ | --- | --- | --- | -------- | --------- | --- |
\mathcal{T}′
|     |     |     |     | =0 ⟺ | \mathcal{T} =0. |     |     |
| --- | --- | --- | --- | ---- | ----- | --- | --- |
17 Suppose\mathcal{V} and\mathcal{W} arefinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Provethat\mathcal{T} is
| invertibleifandonlyif\mathcal{T}′ |     |     | \inℒ(\mathcal{W}′,\mathcal{V}′)isinvertible. |     |     |     |     |
| ----------------------- | --- | --- | ---------------------- | --- | --- | --- | --- |
18 Suppose \mathcal{V} and \mathcal{W} are finite-dimensional. Prove that the map that takes
| \mathcal{T} \in ℒ(\mathcal{V},\mathcal{W}) |     | to \mathcal{T}′ | \in ℒ(\mathcal{W}′,\mathcal{V}′) |     | is an isomorphism | of ℒ(\mathcal{V},\mathcal{W}) | onto |
| ---------- | --- | ----- | ---------- | --- | ----------------- | --------- | ---- |
ℒ(\mathcal{W}′,\mathcal{V}′).
| Suppose\mathcal{U} | \subseteq\mathcal{V}. | Explainwhy |     |     |     |     |     |
| -------- | --- | ---------- | --- | --- | --- | --- | --- |
|     |     |     | \mathcal{U}0 ={\phi\in\mathcal{V}′ |     | ∶\mathcal{U}  |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- |
\subseteqnull\phi}.
20 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{U} isasubspaceof\mathcal{V}. Showthat
∶\phi(v)=0forevery\phi\in\mathcal{U}0}.
\mathcal{U} ={v\in\mathcal{V}
| 21 Suppose\mathcal{V}     | isfinite-dimensionaland\mathcal{U} |     |              |     | and\mathcal{W} aresubspacesof\mathcal{V}. |     |     |
| --------------- | ------------------------ | --- | ------------ | --- | --------------------- | --- | --- |
| (a) Provethat\mathcal{W}0 |                          | \subseteq\mathcal{U}0 | ifandonlyif\mathcal{U} |     | \subseteq\mathcal{W}.                   |     |     |
| (b) Provethat\mathcal{W}0 |                          | =\mathcal{U}0 | ifandonlyif\mathcal{U} |     | =\mathcal{W}.                   |     |     |

| --- | --- | --- | --- | --------- | --- | ------- |
| 22 Suppose\mathcal{V}        | isfinite-dimensionaland\mathcal{U} |         |     | and\mathcal{W} aresubspacesof\mathcal{V}. |     |     |
| ------------------ | ------------------------ | ------- | --- | --------------------- | --- | --- |
| (a) Showthat(\mathcal{U}+\mathcal{W})0 |                          | =\mathcal{U}0\cap\mathcal{W}0. |     |                       |     |     |
| (b) Showthat(\mathcal{U}\cap\mathcal{W})0 |                          | =\mathcal{U}0+\mathcal{W}0. |     |                       |     |     |
23 Suppose\mathcal{V} isfinite-dimensionaland\phi ,…,\phi \in\mathcal{V}′. Provethatthefollow-
|     |     |     |     | 1 m |     |     |
| --- | --- | --- | --- | --- | --- | --- |
ingthreesetsareequaltoeachother.
| (a) span(\phi | ,…,\phi | )   |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- | --- |
1 m
$$))0$$
| (b) ((null\phi | )\cap⋯\cap(null\phi |            |     |          |     |     |
| ----------- | ---------- | ---------- | --- | -------- | --- | --- |
|             | 1          | m          |     |          |     |     |
| (c) {\phi\in\mathcal{V}′   | ∶(null\phi    | )\cap⋯\cap(null\phi |     | )\subseteqnull\phi} |     |     |
|             |            | 1          |     | m        |     |     |
24 Suppose\mathcal{V} isfinite-dimensionalandv ,…,v \in \mathcal{V}. Definealinearmap
|     |     |     |     | 1 m |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Γ∶
| \mathcal{V}′ \rightarrow\mathbf{F}m         | byΓ(\phi)=(\phi(v |             | ),…,\phi(v                  | )). |     |     |
| -------------- | ----------- | ----------- | ------------------------ | --- | --- | --- |
|                |             | 1           |                          | m   |     |     |
| (a) Provethatv |             | ,…,v spans\mathcal{V} | ifandonlyifΓisinjective. |     |     |     |
|                |             | 1 m         |                          |     |     |     |
$$(b) Provethatv ,…,v islinearlyindependentifandonlyifΓissurjective.$$
|          |                          | 1 m |     |           |                  |     |
| -------- | ------------------------ | --- | --- | --------- | ---------------- | --- |
| Suppose\mathcal{V} | isfinite-dimensionaland\phi |     |     | ,…,\phi \in\mathcal{V}′. | Definealinearmap |     |
| 25       |                          |     |     | 1 m       |                  |     |
Γ∶
| \mathcal{V} \rightarrow\mathbf{F}m          | byΓ(v)=(\phi | (v),…,\phi      | (v)).                    |     |     |     |
| -------------- | --------- | ------------ | ------------------------ | --- | --- | --- |
|                |           | 1            | m                        |     |     |     |
| (a) Provethat\phi |           | ,…,\phi spans\mathcal{V}′ | ifandonlyifΓisinjective. |     |     |     |
|                |           | 1 m          |                          |     |     |     |
,…,\phi
$$(b) Provethat\phi islinearlyindependentifandonlyifΓissurjective.$$
|     |     | 1 m |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
isfinite-dimensionaland\Omegaisasubspaceof\mathcal{V}′.
| 26 Suppose\mathcal{V} |     |                              |     |     |     | Provethat |
| ----------- | --- | ---------------------------- | --- | --- | --- | --------- |
|             |     | \Omega={v\in\mathcal{V} ∶\phi(v)=0forevery\phi\in\Omega}0. |     |     |     |           |
27 Suppose \mathcal{T} \in ℒ(𝒫 (\mathbf{R})) and null\mathcal{T}′ = span(\phi), where \phi is the linear
| functionalon𝒫 |     | (\mathbf{R})definedby\phi(p)=p(8). |     | Provethat |     |     |
| ------------- | --- | ---------------------- | --- | --------- | --- | --- |
|     |     | range\mathcal{T} ={p\in𝒫 |     | (\mathbf{R})∶p(8)=0}. |     |     |
| --- | --- | ------------ | --- | ------------ | --- | --- |
28 Suppose\mathcal{V} isfinite-dimensionaland\phi ,…,\phi isalinearlyindependentlist
|                 |            |            | 1   | m            |     |     |
| --------------- | ---------- | ---------- | --- | ------------ | --- | --- |
| in\mathcal{V}′. Provethat |            |            |     |              |     |     |
|                 | dim((null\phi | )\cap⋯\cap(null\phi |     | ))=(dim\mathcal{V})-m. |     |     |
|                 |            | 1          |     | m            |     |     |
\inℒ(\mathcal{V},\mathcal{W}).
| 29 Suppose\mathcal{V}      | and\mathcal{W} | arefinite-dimensionaland\mathcal{T} |                     |                    |     |         |
| ---------------- | ---- | ------------------------- | ------------------- | ------------------ | --- | ------- |
| Provethatif\phi\in\mathcal{W}′  |      | andnull\mathcal{T}′                 |                     |                    |     |         |
| (a)              |      |                           | =span(\phi),thenrange\mathcal{T} |                    |     | =null\phi. |
| (b) Provethatif\psi |      | \in\mathcal{V}′ andrange\mathcal{T}′            |                     | =span(\psi),thennull\mathcal{T} |     | =null\psi. |
30 Suppose\mathcal{V} isfinite-dimensionaland\phi ,…,\phi isabasisof\mathcal{V}′. Showthat
|                      |     |                   |     | 1 n  |     |     |
| -------------------- | --- | ----------------- | --- | ---- | --- | --- |
| thereexistsabasisof\mathcal{V} |     | whosedualbasisis\phi |     | ,…,\phi | .   |     |
|                      |     |                   |     | 1    | n   |     |
Leti∶
| 31 Suppose\mathcal{U}        | isasubspaceof\mathcal{V}. |                                  | \mathcal{U}   | \rightarrow\mathcal{V} betheinclusionmapdefined |      |     |
| ------------------ | --------------- | -------------------------------- | --- | --------------------------- | ---- | --- |
| byi(u)=u.          | Thusi′          | \inℒ(\mathcal{V}′,\mathcal{U}′).                       |     |                             |      |     |
| (a) Showthatnulli′ |                 | =\mathcal{U}0.                             |     |                             |      |     |
|                    |                 | isfinite-dimensional,thenrangei′ |     |                             | =\mathcal{U}′. |     |
| (b) Provethatif\mathcal{V}   |                 |                                  |     |                             |      |     |
$$(c) Provethatif \mathcal{V} isfinite-dimensional, then i′̃ isanisomorphismfrom$$
\mathcal{V}′/\mathcal{U}0 onto\mathcal{U}′.
Theisomorphismin(c)isnaturalinthatitdoesnotdependonachoiceof
basisineithervectorspace.

| -------- | ---------- | --- | --- |
Thedoubledualspaceof\mathcal{V},denotedby\mathcal{V}″,isdefinedtobethedualspace
| of\mathcal{V}′. Inotherwords,\mathcal{V}″ | =(\mathcal{V}′)′. Define\Lambda∶ | \mathcal{V} \rightarrow\mathcal{V}″ | by  |
| --------------------- | ---------------- | ----- | --- |
$$(\Lambdav)(\phi)=\phi(v)$$
andeach\phi\in\mathcal{V}′.
foreachv\in\mathcal{V}
| (a) Showthat\Lambdaisalinearmapfrom\mathcal{V} |     | to\mathcal{V}″. |     |
| ------------------------------ | --- | ----- | --- |
=(\mathcal{T}′)′.
| (b) Showthatif\mathcal{T} | \inℒ(\mathcal{V}),then\mathcal{T}″\circ\Lambda | =\Lambda\circ\mathcal{T},where\mathcal{T}″ |     |
| --------------- | -------------- | ------------ | --- |
$$(c) Showthatif\mathcal{V} isfinite-dimensional,then\Lambdaisanisomorphismfrom\mathcal{V}$$
onto\mathcal{V}″.
Suppose\mathcal{V}isfinite-dimensional. Then\mathcal{V}and\mathcal{V}′areisomorphic,butfinding
anisomorphismfrom\mathcal{V}onto\mathcal{V}′generallyrequireschoosingabasisof \mathcal{V}.
from\mathcal{V}onto\mathcal{V}″doesnotrequireachoice
Incontrast,theisomorphism\Lambda
ofbasisandthusisconsideredmorenatural.
33 Suppose\mathcal{U} isasubspaceof\mathcal{V}. Let\pi∶ \mathcal{V} \rightarrow\mathcal{V}/\mathcal{U} betheusualquotientmap.
Thus\pi′ \inℒ((\mathcal{V}/\mathcal{U})′,\mathcal{V}′).
| (a) Showthat\pi′  | isinjective. |     |     |
| --------------- | ------------ | --- | --- |
| Showthatrange\pi′ | =\mathcal{U}0.         |     |     |
$$(b)$$
| (c) Concludethat\pi′ | isanisomorphismfrom(\mathcal{V}/\mathcal{U})′ |     | onto\mathcal{U}0. |
| ------------------ | ------------------------- | --- | ------- |
Theisomorphismin(c)isnaturalinthatitdoesnotdependonachoiceof
basisineithervectorspace. Infact,thereisnoassumptionherethatanyof
thesevectorspacesarefinite-dimensional.
