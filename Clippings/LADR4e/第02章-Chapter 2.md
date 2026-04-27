---
title: Chapter 2
source: Clippings/LADR4e.pdf
created: 2026-04-23
type: chapter
tags:
  - book
  - chapter
---

# Chapter 2
Finite-Dimensional Vector Spaces
Inthelastchapterwelearnedaboutvectorspaces. Linearalgebrafocusesnot
on arbitrary vector spaces, but on finite-dimensional vector spaces, which we
introduceinthischapter.
Webeginthischapterbyconsideringlinearcombinationsoflistsofvectors.
Thisleadsustothecrucialconceptoflinearindependence. Thelineardependence
lemmawillbecomeoneofourmostusefultools.
Alistofvectorsinavectorspacethatissmallenoughtobelinearlyindependent
andbigenoughsothelinearcombinationsofthelistfillupthevectorspaceis
calledabasisofthevectorspace. Wewillseethateverybasisofavectorspace
hasthesamelength,whichwillallowustodefinethedimensionofavectorspace.
Thischapterendswithaformulaforthedimensionofthesumoftwosubspaces.
standingassumptionsforthischapter
• \mathbf{F} denotes\mathbf{R} or\mathbf{C}.
• \mathcal{V} denotesavectorspaceover\mathbf{F}.
Themainbuildingofthe Institutefor Advanced Study,in Princeton,New Jersey.
Paul Halmos(1916–2006)wrotethefirstmodernlinearalgebrabookinthisbuilding.
Halmos’slinearalgebrabookwaspublishedin1942(secondeditionpublishedin1958).
Thetitleof Halmos’sbookwasthesameasthetitleofthischapter.

| -------- | ------------------------------ | --- | --- |
| 2A Span | and Linear | Independence |     |
| ------- | ---------- | ------------ | --- |
Wehavebeenwritinglistsofnumberssurroundedbyparentheses,andwewill
continuetodosoforelementsof\mathbf{F}n;forexample,(2,-7,8)\in\mathbf{F}3. However,now
we need to consider lists of vectors (which may be elements of \mathbf{F}n or of other
vectorspaces). Toavoidconfusion,wewillusuallywritelistsofvectorswithout
surroundingparentheses. Forexample,(4,1,6),(9,5,7)isalistoflengthtwoof
vectorsin\mathbf{R}3.
| 2.1 notation: | listofvectors |     |     |
| ------------- | ------------- | --- | --- |
Wewillusuallywritelistsofvectorswithoutsurroundingparentheses.
| Linear | Combinations | and Span |     |
| ------ | ------------ | -------- | --- |
Asumofscalarmultiplesofthevectorsinalistiscalledalinearcombinationof
thelist. Hereistheformaldefinition.
| 2.2 definition: | linearcombination |     |     |
| --------------- | ----------------- | --- | --- |
Alinearcombinationofalistv ,…,v ofvectorsin\mathcal{V} isavectoroftheform
1 m
|              |                        | a v +⋯+a v | ,   |
| ------------ | ---------------------- | ---------- | --- |
|              |                        | 1 1 m m    |     |
| wherea       | ,…,a \in\mathbf{F}.               |            |     |
|              | 1 m                    |            |     |
| 2.3 example: | linearcombinationsin\mathbf{R}3 |            |     |
$$(17,-4,2) (2,1,-3),(1,-2,4),$$
| •   | is a linear | combination of | whichis a listof |
| --- | ----------- | -------------- | ---------------- |
lengthtwoofvectorsin\mathbf{R}3,because
$$(17,-4,2)=6(2,1,-3)+5(1,-2,4).$$
• (17,-4,5)isnotalinearcombinationof(2,1,-3),(1,-2,4),whichisalist
oflengthtwoofvectorsin\mathbf{R}3,becausetheredonotexistnumbersa ,a \in\mathbf{F}
1 2
suchthat
|     | (17,-4,5)=a | (2,1,-3)+a | (1,-2,4). |
| --- | ----------- | ---------- | --------- |
Inotherwords,thesystemofequations
|     |     | 17 =2a +a |     |
| --- | --- | --------- | --- |
1 2
-4=a -2a
1 2
|     |     | 5=-3a +4a |     |
| --- | --- | --------- | --- |
1 2
hasnosolutions(asyoushouldverify).

| --- | --- | --- | --------- | --- | ------------------------- | --- | --- | --- |
span
**2.4 定义：** Thesetofalllinearcombinationsofalistofvectorsv ,…,v in\mathcal{V} iscalled
|            |        |                       |        |       |      |     | 1             | m   |
| ---------- | ------ | --------------------- | ------ | ----- | ---- | --- | ------------- | --- |
| thespanofv |        | ,…,v ,denotedbyspan(v |        |       | ,…,v | ).  | Inotherwords, |     |
|            |        | 1 m                   |        |       | 1    | m   |               |     |
|            | span(v | ,…,v                  |        |       | +⋯+a | ∶a  | ,…,a          |     |
|            |        | 1                     | m )={a | 1 v 1 | m    | v m | 1 m \in\mathbf{F}}.      |     |
Thespanoftheemptylist()isdefinedtobe{0}.
| 2.5 | example: | span |     |     |     |     |     |     |
| --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
Thepreviousexampleshowsthatin\mathbf{F}3,
$$(17,-4,2)\inspan((2,1,-3),(1,-2,4));$$
•
• (17,-4,5)\notinspan((2,1,-3),(1,-2,4)).
2.6 spanisthesmallestcontainingsubspace
Thespanofalistofvectorsin\mathcal{V} isthesmallestsubspaceof\mathcal{V} containingall
vectorsinthelist.
| Proof | Supposev | ,…,v | isalistofvectorsin\mathcal{V}. |     |     |     |     |     |
| ----- | -------- | ---- | -------------------- | --- | --- | --- | --- | --- |
|       |          | 1    | m                    |     |     |     |     |     |
,…,v
Firstweshowthatspan(v 1 m )is Somemathematiciansusetheterminol-
| asubspaceof\mathcal{V}. |     | Theadditiveidentityis |     |     |     |     |     |     |
| ------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
ogylinearspan,whichmeansthesame
,…,v
| inspan(v    |      | )because                           |     |     | asspan. |     |     |     |
| ----------- | ---- | ---------------------------------- | --- | --- | ------- | --- | --- | --- |
|             | 1    | m                                  |     |     |         |     |     |     |
|             | 0=0v | +⋯+0v                              | .   |     |         |     |     |     |
|             |      | 1                                  | m   |     |         |     |     |     |
| Also,span(v |      | ,…,v )isclosedunderadditionbecause |     |     |         |     |     |     |
1 m
| (a v | +⋯+a | v )+(c | v +⋯+c |     | v )=(a | +c  | )v +⋯+(a | +c )v . |
| ---- | ---- | ------ | ------ | --- | ------ | --- | -------- | ------- |
| 1    | 1    | m m    | 1 1    |     | m m    | 1   | 1 1      | m m m   |
Furthermore,span(v ,…,v )isclosedunderscalarmultiplicationbecause
|            |     | 1                    | m    |     |           |     |        |     |
| ---------- | --- | -------------------- | ---- | --- | --------- | --- | ------ | --- |
|            |     | \lambda(a v                | +⋯+a | v   | )= \lambdaa v   | +⋯+ | \lambdaa v . |     |
|            |     | 1 1                  |      | m m | 1         | 1   | m m    |     |
| Thusspan(v |     | ,…,v )isasubspaceof\mathcal{V} |      |     | (by1.34). |     |        |     |
1 m
| Eachv | isalinearcombinationofv |     |     |     | ,…,v | (toshowthis,seta |     | =1andlet |
| ----- | ----------------------- | --- | --- | --- | ---- | ---------------- | --- | -------- |
|       | k                       |     |     |     | 1    | m                |     | k        |
theothera’sin2.2equal0). Thusspan(v ,…,v )containseachv . Conversely,
|     |     |     |     |     | 1   | m   |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
becausesubspacesareclosedunderscalarmultiplicationandaddition,everysubspaceof\mathcal{V} thatcontainseachv containsspan(v ,…,v ). Thusspan(v ,…,v )
|                          |             |                            | k                        |     |     | 1    | m       | 1 m |
| ------------------------ | ----------- | -------------------------- | ------------------------ | --- | --- | ---- | ------- | --- |
| isthesmallestsubspaceof\mathcal{V} |             |                            | containingallthevectorsv |     |     |      | ,…,v    | .   |
|                          |             |                            |                          |     |     |      | 1       | m   |
| 2.7                      | definition: | spans                      |                          |     |     |      |         |     |
|                          | ,…,v        |                            |                          |     |     | ,…,v |         |     |
| Ifspan(v                 |             | )equals\mathcal{V},wesaythatthelistv |                          |     |     |      | spans\mathcal{V}. |     |
|                          | 1           | m                          |                          |     |     | 1    | m       |     |

| -------- | ------------------------------ | --- | --- | --- |
alistthatspans\mathbf{F}n
**2.8 例：** | Supposenisapositiveinteger. |     | Wewanttoshowthat |     |     |
| --------------------------- | --- | ---------------- | --- | --- |
$$(1,0,…,0),(0,1,0,…,0),…,(0,…,0,1)$$
spans\mathbf{F}n. Herethekthvectorinthelistabovehas1inthekthslotand0inallother
slots.
,…,x )\in\mathbf{F}n.
| Suppose(x | 1 n Then        |                 |            |     |
| --------- | --------------- | --------------- | ---------- | --- |
| (x ,…,x   | )=x (1,0,…,0)+x | (0,1,0,…,0)+⋯+x | (0,…,0,1). |     |
| 1         | n 1             | 2               | n          |     |
Thus(x ,…,x )\inspan((1,0,…,0),(0,1,0,…,0),…,(0,…,0,1)),asdesired.
| 1   | n   |     |     |     |
| --- | --- | --- | --- | --- |
Nowwecanmakeoneofthekeydefinitionsinlinearalgebra.
| 2.9 definition: | finite-dimensionalvectorspace |     |     |     |
| --------------- | ----------------------------- | --- | --- | --- |
Avectorspaceiscalledfinite-dimensionalifsomelistofvectorsinitspans
thespace.
Example2.8aboveshowsthat\mathbf{F}nisa
Recallthatbydefinitioneverylisthas
finite-dimensionalvectorspaceforevery
finitelength.
positiveintegern.
Thedefinitionofapolynomialisnodoubtalreadyfamiliartoyou.
| 2.10 definition: | polynomial,𝒫(\mathbf{F}) |     |     |     |
| ---------------- | --------------- | --- | --- | --- |
Afunctionp∶
| •           | \mathbf{F} \rightarrow\mathbf{F} iscalledapolynomialwithcoefficientsin\mathbf{F} |               |     | ifthere |
| ----------- | ------------------------------------------- | ------------- | --- | ------- |
| exista ,…,a | \in\mathbf{F} suchthat                                 |               |     |         |
| 0           | m                                           |               |     |         |
|             | p(z)=a                                      | +a z+a z2+⋯+a | zm  |         |
|             | 0                                           | 1 2           | m   |         |
forallz\in\mathbf{F}.
• 𝒫(\mathbf{F})isthesetofallpolynomialswithcoefficientsin\mathbf{F}.
With the usual operations of addition and scalar multiplication, 𝒫(\mathbf{F}) is a
vectorspaceover\mathbf{F},asyoushouldverify. Hence𝒫(\mathbf{F})isasubspaceof\mathbf{F}\mathbf{F},the
| vectorspaceoffunctionsfrom\mathbf{F} |     | to\mathbf{F}. |     |     |
| --------------------------- | --- | ---- | --- | --- |
Ifapolynomial(thoughtofasafunctionfrom\mathbf{F} to\mathbf{F})isrepresentedbytwo
setsofcoefficients,thensubtractingonerepresentationofthepolynomialfrom
theotherproducesapolynomialthatisidenticallyzeroasafunctionon\mathbf{F} and
hencehasallzerocoefficients(ifyouareunfamiliarwiththisfact,justbelieve
it for now; we will prove it later—see 4.8). Conclusion: the coefficients of a
polynomialareuniquelydeterminedbythepolynomial. Thusthenextdefinition
uniquelydefinesthedegreeofapolynomial.

| --- | --- | ----------------------------------- | --- |
degreeofapolynomial,degp
**2.11 定义：** • A polynomial p \in 𝒫(\mathbf{F}) is said to have degree m if there exist scalars
,a ,…,a
| a   | \in\mathbf{F} witha | \neq0suchthatforeveryz\in\mathbf{F},wehave |     |
| --- | -------- | ---------------------------- | --- |
| 0 1 | m        | m                            |     |
zm.
|     |     | p(z)=a +a z+⋯+a |     |
| --- | --- | --------------- | --- |
|     |     | 0 1             | m   |
• Thepolynomialthatisidentically0issaidtohavedegree-\infty.
• Thedegreeofapolynomialpisdenotedbydegp.
Inthenextdefinition,weusetheconventionthat-\infty<m,whichmeansthat
| thepolynomial0isin𝒫 |     | (\mathbf{F}). |     |
| ------------------- | --- | ---- | --- |
m
𝒫
| 2.12 notation: | (\mathbf{F}) |     |     |
| -------------- | --- | --- | --- |
m
Formanonnegativeinteger,𝒫 (\mathbf{F})denotesthesetofallpolynomialswith
m
| coefficientsin\mathbf{F} | anddegreeatmostm. |     |     |
| --------------- | ----------------- | --- | --- |
Ifmisanonnegativeinteger,then𝒫 (\mathbf{F})=span(1,z,…,zm)[hereweslightly
m
abusenotationbylettingzkdenoteafunction]. Thus𝒫 (\mathbf{F})isafinite-dimensional
m
vectorspaceforeachnonnegativeintegerm.
| 2.13 definition: | infinite-dimensionalvectorspace |     |     |
| ---------------- | ------------------------------- | --- | --- |
Avectorspaceiscalledinfinite-dimensionalifitisnotfinite-dimensional.
| 2.14 example: | 𝒫(\mathbf{F})isinfinite-dimensional |     |     |
| ------------- | -------------------------- | --- | --- |
Consideranylistofelementsof𝒫(\mathbf{F}). Letmdenotethehighestdegreeof
thepolynomialsinthislist. Theneverypolynomialinthespanofthislisthas
Thuszm+1
| degreeatmostm. |     | isnotinthespanofourlist. | Hencenolistspans |
| -------------- | --- | ------------------------ | ---------------- |
𝒫(\mathbf{F}). Thus𝒫(\mathbf{F})isinfinite-dimensional.
Suppose v ,…,v \in \mathcal{V} and v \in span(v ,…,v ). By the definition of span,
| 1   | m   | 1   | m   |
| --- | --- | --- | --- |
,…,a
| thereexista | \in\mathbf{F}  | suchthat |     |
| ----------- | --- | -------- | --- |
1 m
|     |     | v=a v +⋯+a | v . |
| --- | --- | ---------- | --- |
|     |     | 1 1        | m m |
Considerthequestionofwhetherthechoiceofscalarsintheequationaboveis
| unique. Supposec | ,…,c | isanothersetofscalarssuchthat |     |
| ---------------- | ---- | ----------------------------- | --- |
1 m
|     |     | v=c v +⋯+c | v . |
| --- | --- | ---------- | --- |
|     |     | 1 1        | m m |
Subtractingthelasttwoequations,wehave
+⋯+(a
|     | 0=(a | -c )v | -c )v . |
| --- | ---- | ----- | ------- |
|     |      | 1 1 1 | m m m   |

| -------- | ------------------------------ | --- | --- |
Thuswehavewritten0asalinearcombinationof(v ,…,v ). Iftheonlyway
1 m
to do this is by using 0 for all the scalars in the linear combination, then each
a - c equals 0, which means that each a equals c (and thus the choice of
| k k |     |     | k k |
| --- | --- | --- | --- |
scalarswasindeedunique). Thissituationissoimportantthatwegiveitaspecial
name—linearindependence—whichwenowdefine.
linearlyindependent
**2.15 定义：** • Alistv ,…,v ofvectorsin\mathcal{V} iscalledlinearlyindependent iftheonly
|           | 1 m     |           |     |
| --------- | ------- | --------- | --- |
| choiceofa | ,…,a \in\mathbf{F} | thatmakes |     |
1 m
|          |     | a v +⋯+a | v =0 |
| -------- | --- | -------- | ---- |
|          |     | 1 1      | m m  |
| isa =⋯=a | =0. |          |      |
| 1        | m   |          |      |
Theemptylist()isalsodeclaredtobelinearlyindependent.
•
Thereasoningaboveshowsthatv ,…,v islinearlyindependentifandonlyif
|     |     | 1   | m   |
| --- | --- | --- | --- |
eachvectorinspan(v ,…,v )hasonlyonerepresentationasalinearcombination
|     | 1   | m   |     |
| --- | --- | --- | --- |
ofv ,…,v .
1 m
linearlyindependentlists
**2.16 例：** (a) Toseethatthelist(1,0,0,0),(0,1,0,0),(0,0,1,0)islinearlyindependentin
| \mathbf{F}4,supposea | ,a ,a |     |     |
| ----------- | ----- | --- | --- |
\in\mathbf{F} and
1 2 3
|     | a (1,0,0,0)+a | (0,1,0,0)+a | (0,0,1,0)=(0,0,0,0). |
| --- | ------------- | ----------- | -------------------- |
Thus
,a ,a ,0)=(0,0,0,0).
$$(a$$
1 2 3
Hence a = a = a = 0. Thus the list (1,0,0,0),(0,1,0,0),(0,0,1,0) is
|     | 1 2 3 |     |     |
| --- | ----- | --- | --- |
linearlyindependentin\mathbf{F}4.
$$(b) Supposemisanonnegativeinteger. Toseethatthelist1,z,…,zm islinearly$$
| independentin𝒫(\mathbf{F}),supposea |     | ,a         | ,…,a \in\mathbf{F} and |
| -------------------------- | --- | ---------- | ----------- |
|                            |     | 0 1        | m           |
|                            |     | a +a z+⋯+a | zm =0,      |
|                            |     | 0 1        | m           |
wherewethinkofbothsidesaselementsof𝒫(\mathbf{F}). Then
|     |     | +a z+⋯+a | zm  |
| --- | --- | -------- | --- |
|     |     | a        | =0  |
|     |     | 0 1      | m   |
forallz\in\mathbf{F}. Asdiscussedearlier(andasfollowsfrom4.8),thisimpliesthat
$$a = a = ⋯ = a = 0. Thus 1,z,…,zm is a linearly independent list in$$
| 0   | 1 m |     |     |
| --- | --- | --- | --- |
𝒫(\mathbf{F}).
$$(c) Alistoflengthoneinavectorspaceislinearlyindependentifandonlyifthe$$
vectorinthelistisnot0.
$$(d) Alistoflengthtwoinavectorspaceislinearlyindependentifandonlyif$$
neitherofthetwovectorsinthelistisascalarmultipleoftheother.

| --- | --- | --------- | ------------------------- | --- |
Ifsomevectorsareremovedfromalinearlyindependentlist,theremaining
listisalsolinearlyindependent,asyoushouldverify.
| 2.17 | definition: | linearlydependent |     |     |
| ---- | ----------- | ----------------- | --- | --- |
• Alistofvectorsin\mathcal{V} iscalledlinearlydependent ifitisnotlinearlyindependent.
Inotherwords,alistv ,…,v ofvectorsin\mathcal{V}islinearlydependentifthere
| •                                                 |          | 1 m                    |        |         |
| ------------------------------------------------- | -------- | ---------------------- | ------ | ------- |
| exista                                            | ,…,a     | \in\mathbf{F},notall0,suchthata   | v +⋯+a | v =0.   |
|                                                   | 1        | m                      | 1 1    | m m     |
| 2.18                                              | example: | linearlydependentlists |        |         |
| • (2,3,1),(1,-1,2),(7,3,8)islinearlydependentin\mathbf{F}3 |          |                        |        | because |
2(2,3,1)+3(1,-1,2)+(-1)(7,3,8)=(0,0,0).
• Thelist(2,3,1),(1,-1,2),(7,3,c)islinearlydependentin\mathbf{F}3 ifandonlyif
=8,asyoushouldverify.
c
• If some vector in a list of vectors in \mathcal{V} is a linear combination of the other
vectors,thenthelistislinearlydependent. (Proof: Afterwritingonevectorin
thelistasequaltoalinearcombinationoftheothervectors,movethatvector
totheothersideoftheequation,whereitwillbemultipliedby-1.)
• Everylistofvectorsin\mathcal{V} containingthe0vectorislinearlydependent. (This
isaspecialcaseofthepreviousbulletpoint.)
Thenextlemmaisaterrifictool. Itstatesthatgivenalinearlydependentlist
ofvectors,oneofthevectorsisinthespanofthepreviousones. Furthermore,we
canthrowoutthatvectorwithoutchangingthespanoftheoriginallist.
2.19 lineardependencelemma
,…,v
Suppose v is a linearly dependent list in \mathcal{V}. Then there exists
1 m
k \in{1,2,…,m}suchthat
|     |     | v \inspan(v | ,…,v ). |     |
| --- | --- | --------- | ------- | --- |
|     |     | k         | 1 k-1   |     |
Furthermore, ifk satisfiestheconditionaboveandthekth termisremoved
fromv ,…,v ,thenthespanoftheremaininglistequalsspan(v ,…,v ).
|     | 1 m |     |     | 1 m |
| --- | --- | --- | --- | --- |
Proof Because the list v ,…,v is linearly dependent, there exist numbers
|        |                     | 1 m |     |     |
| ------ | ------------------- | --- | --- | --- |
| a ,…,a | \in\mathbf{F},notall0,suchthat |     |     |     |
1 m
|                                           |     | a v +⋯+a | v =0. |          |
| ----------------------------------------- | --- | -------- | ----- | -------- |
|                                           |     | 1 1      | m m   |          |
| Letkbethelargestelementof{1,…,m}suchthata |     |          |       | \neq0. Then |
k
a a
|     |     | 1v   | k-1v    | ,   |
| --- | --- | ---- | ------- | --- |
|     |     | v =- | -⋯-     |     |
|     |     | k a  | 1 a k-1 |     |
k k
| whichprovesthatv |     | \inspan(v ,…,v | ),asdesired. |     |
| ---------------- | --- | ------------ | ------------ | --- |
|                  |     | k 1          | k-1          |     |

| --------------------------------------- | --- | --- | --- |
| Nowsupposekisanyelementof{1,…,m}suchthatv |     | \inspan(v | ,…,v ). |
| ----------------------------------------- | --- | ------- | ------- |
|                                           |     | k       | 1 k-1   |
| Letb ,…,b \in\mathbf{F} besuchthat                   |     |         |         |
1 k-1
| 2.20            | v =b v +⋯+b        | v .         |     |
| --------------- | ------------------ | ----------- | --- |
|                 | k 1 1              | k-1 k-1     |     |
| ,…,v            |                    | ,…,c        |     |
| Supposeu\inspan(v | ). Thenthereexistc | \in\mathbf{F} suchthat |     |
| 1               | m                  | 1 m         |     |
|                 | u=c v +⋯+c         | v .         |     |
|                 | 1 1                | m m         |     |
Intheequationabove,wecanreplacev withtherightsideof2.20,whichshows
k
thatuisinthespanofthelistobtainedbyremovingthekth termfromv ,…,v .
1 m
Thusremovingthekth termofthelistv ,…,v doesnotchangethespanofthe
1 m
list.
| Ifk =1inthelineardependencelemma,thenv |     | \inspan(v ,…,v | )means |
| -------------------------------------- | --- | ------------ | ------ |
|                                        |     | k 1          | k-1    |
thatv =0,becausespan()={0}. Notealsothatpartsoftheproofofthelinear
dependencelemmaneedtobemodifiedifk = 1. Ingeneral,theproofsinthe
restofthebookwillnotcallattentiontospecialcasesthatmustbeconsidered
involvinglistsoflength0,thesubspace{0},orothertrivialcasesforwhichthe
resultistruebutneedsaslightlydifferentproof. Besuretocheckthesespecial
casesyourself.
| 2.21 example: smallest | kinlineardependencelemma |     |     |
| ---------------------- | ------------------------ | --- | --- |
Considerthelist
$$(1,2,3),(6,5,4),(15,16,17),(8,9,7)$$
in\mathbf{R}3. Thislistoflengthfourislinearlydependent,aswewillsoonsee. Thusthe
\in{1,2,3,4}suchthatthekth
lineardependencelemmaimpliesthatthereexistsk
vectorinthislistisalinearcombinationofthepreviousvectorsinthelist. Let’s
seehowtofindthesmallestvalueofkthatworks.
Takingk = 1inthelineardependencelemmaworksifandonlyifthefirst
vectorinthelistequals0. Because(1,2,3)isnotthe0vector,wecannottake
$$k =1forthislist.$$
Takingk =2inthelineardependencelemmaworksifandonlyifthesecond
vectorinthelistisascalarmultipleofthefirstvector. However,theredoesnot
existc \in\mathbf{R} suchthat(6,5,4)=c(1,2,3). Thuswecannottakek =2forthislist.
Takingk = 3inthelineardependencelemmaworksifandonlyifthethird
vectorinthelistisalinearcombinationofthefirsttwovectors. Thusforthelist
| inthisexample,wewanttoknowwhetherthereexista,b\in\mathbf{R} |     | suchthat |     |
| ------------------------------------------------ | --- | -------- | --- |
$$(15,16,17)=a(1,2,3)+b(6,5,4).$$
Theequationaboveisequivalenttoasystemofthreelinearequationsinthetwo
unknownsa,b. Using Gaussianeliminationorappropriatesoftware,wefindthat
$$a=3,b=2isasolutionoftheequationabove,asyoucanverify. Thusforthe$$
listinthisexample,takingk =3isthesmallestvalueofkthatworksinthelinear
dependencelemma.

Section2A Spanand Linear Independence 35
Nowwecometoakeyresult. Itsaysthatnolinearlyindependentlistin\mathcal{V} is
longerthanaspanninglistin\mathcal{V}.
2.22 lengthoflinearlyindependentlist \leq lengthofspanninglist
Inafinite-dimensionalvectorspace,thelengthofeverylinearlyindependent
list of vectors is less than or equal to the length of every spanning list of
vectors.
Proof Supposethatu ,…,u islinearlyindependentin\mathcal{V}. Supposealsothat
1 m
w ,…,w spans\mathcal{V}. Weneedtoprovethatm\leqn. Wedosothroughtheprocess
1 n
describedbelowwithmsteps;notethatineachstepweaddoneoftheu’sand
removeoneofthew’s.
Step1
Let\mathcal{B}bethelistw ,…,w ,whichspans\mathcal{V}. Adjoiningu atthebeginningof
1 n 1
thislistproducesalinearlydependentlist(becauseu canbewrittenasalinear
combinationofw ,…,w ). Inotherwords,thelist
1 n
u ,w ,…,w
1 1 n
islinearlydependent.
Thusbythelineardependencelemma(2.19),oneofthevectorsinthelistabove
isalinearcombinationofthepreviousvectorsinthelist. Weknowthatu \neq0
becausethelistu ,…,u islinearlyindependent. Thusu isnotinthespan
1 m 1
ofthepreviousvectorsinthelistabove(becauseu isnotin{0},whichisthe
spanoftheemptylist). Hencethelineardependencelemmaimpliesthatwe
canremoveoneofthew’ssothatthenewlist\mathcal{B}(oflengthn)consistingofu
andtheremainingw’sspans\mathcal{V}.
Stepk,fork=2,…,m
Thelist\mathcal{B}(oflengthn)fromstepk-1spans\mathcal{V}. Inparticular,u isinthespanof
k
thelist\mathcal{B}. Thusthelistoflength(n+1)obtainedbyadjoiningu to\mathcal{B},placing
k
itjustafteru ,…,u ,islinearlydependent. Bythelineardependencelemma
1 k-1
$$(2.19),oneofthevectorsinthislistisinthespanofthepreviousones,and$$
becauseu ,…,u islinearlyindependent,thisvectorcannotbeoneoftheu’s.
1 k
Hencetherestillmustbeatleastoneremainingwatthisstep. Wecanremove
fromournewlist(afteradjoiningu intheproperplace)awthatisalinear
k
combinationofthepreviousvectorsinthelist,sothatthenewlist\mathcal{B}(oflength
n)consistingofu ,…,u andtheremainingw’sspans\mathcal{V}.
1 k
Afterstepm,wehaveaddedalltheu’sandtheprocessstops. Ateachstep
asweaddauto\mathcal{B},thelineardependencelemmaimpliesthatthereissomewto
remove. Thusthereareatleastasmanyw’sasu’s.

36 Chapter 2 Finite-Dimensional Vector Spaces
Thenexttwoexamplesshowhowtheresultabovecanbeusedtoshow,without
anycomputations,thatcertainlistsarenotlinearlyindependentandthatcertain
listsdonotspanagivenvectorspace.
**2.23 例：** nolistoflength4islinearlyindependentin\mathbf{R}3
Thelist(1,0,0),(0,1,0),(0,0,1),whichhaslengththree,spans\mathbf{R}3. Thusno
listoflengthlargerthanthreeislinearlyindependentin\mathbf{R}3.
Forexample,wenowknowthat(1,2,3),(4,5,8),(9,6,7),(-3,2,8),which
isalistoflengthfour,isnotlinearlyindependentin\mathbf{R}3.
**2.24 例：** nolistoflength3spans\mathbf{R}4
Thelist(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),whichhaslengthfour,is
linearlyindependentin\mathbf{R}4. Thusnolistoflengthlessthanfourspans\mathbf{R}4.
Forexample,wenowknowthat(1,2,3,-5),(4,5,8,3),(9,6,7,-1),which
isalistoflengththree,doesnotspan\mathbf{R}4.
Ourintuitionsuggeststhateverysubspaceofafinite-dimensionalvectorspace
shouldalsobefinite-dimensional. Wenowprovethatthisintuitioniscorrect.
2.25 finite-dimensionalsubspaces
Everysubspaceofafinite-dimensionalvectorspaceisfinite-dimensional.
Proof Suppose\mathcal{V} isfinite-dimensionaland\mathcal{U} isasubspaceof\mathcal{V}. Weneedto
provethat\mathcal{U} isfinite-dimensional. Wedothisthroughthefollowingmultistep
construction.
Step1
If\mathcal{U} = {0},then\mathcal{U} isfinite-dimensionalandwearedone. If\mathcal{U} \neq {0},then
chooseanonzerovectoru \in\mathcal{U}.
Stepk
If\mathcal{U} = span(u ,…,u ), then\mathcal{U} isfinite-dimensionalandwearedone. If
1 k-1
\mathcal{U} \neqspan(u ,…,u ),thenchooseavectoru \in\mathcal{U} suchthat
1 k-1 k
u \notinspan(u ,…,u ).
k 1 k-1
Aftereachstep,aslongastheprocesscontinues,wehaveconstructedalist
ofvectorssuchthatnovectorinthislistisinthespanofthepreviousvectors.
Thusaftereachstepwehaveconstructedalinearlyindependentlist,bythelinear
dependencelemma(2.19). Thislinearlyindependentlistcannotbelongerthan
anyspanninglistof\mathcal{V} (by2.22). Thustheprocesseventuallyterminates,which
meansthat\mathcal{U} isfinite-dimensional.

| --- | --------- | ------------------------- |
Exercises 2A
| 1 Findalistoffourdistinctvectorsin\mathbf{F}3 |             | whosespanequals |
| ------------------------------------ | ----------- | --------------- |
|                                      | {(x,y,z)\in\mathbf{F}3 | ∶x+y+z=0}.      |
2 Proveorgiveacounterexample: Ifv ,v ,v ,v spans\mathcal{V},thenthelist
1 2 3 4
|     | v -v ,v | -v ,v -v ,v |
| --- | ------- | ----------- |
|     | 1 2 2   | 3 3 4 4     |
alsospans\mathcal{V}.
,…,v \in{1,…,m},let
| 3 Supposev | isalistofvectorsin\mathcal{V}. | Fork |
| ---------- | -------------------- | ---- |
1 m
|     | w =v | +⋯+v . |
| --- | ---- | ------ |
k 1 k
| Showthatspan(v | ,…,v )=span(w | ,…,w ). |
| -------------- | ------------- | ------- |
|                | 1 m           | 1 m     |
4 (a) Showthatalistoflengthoneinavectorspaceislinearlyindependent
ifandonlyifthevectorinthelistisnot0.
$$(b) Showthatalistoflengthtwoinavectorspaceislinearlyindependent$$
ifandonlyifneitherofthetwovectorsinthelistisascalarmultipleof
theother.
5 Findanumbertsuchthat
$$(3,1,4),(2,-3,5),(5,9,t)$$
isnotlinearlyindependentin\mathbf{R}3.
6 Showthatthelist(2,3,1),(1,-1,2),(7,3,c)islinearlydependentin\mathbf{F}3 if
| andonlyifc =8. |     |     |
| -------------- | --- | --- |
7 (a) Show that if we think of \mathbf{C} as a vector space over \mathbf{R}, then the list
1+i,1-iislinearlyindependent.
$$(b) Show that if we think of \mathbf{C} as a vector space over \mathbf{C}, then the list$$
1+i,1-iislinearlydependent.
8 Supposev ,v ,v ,v islinearlyindependentin\mathcal{V}. Provethatthelist
1 2 3 4
|     | v -v ,v | -v ,v -v ,v |
| --- | ------- | ----------- |
|     | 1 2 2   | 3 3 4 4     |
isalsolinearlyindependent.
Proveorgiveacounterexample: Ifv ,v ,…,v isalinearlyindependent
| 9   |     | 1 2 m |
| --- | --- | ----- |
listofvectorsin\mathcal{V},then
|     | 5v -4v | ,v ,v ,…,v |
| --- | ------ | ---------- |
|     | 1      | 2 2 3 m    |
islinearlyindependent.

| --- | -------- | ------------------------------ | --- | --- | --- | --- |
10 Proveorgiveacounterexample: Ifv ,v ,…,v isalinearlyindependent
1 2 m
listofvectorsin\mathcal{V} and \lambda\in\mathbf{F} with \lambda\neq0,then \lambdav ,\lambdav ,…,\lambdav islinearly
|     |     |     |     | 1   | 2 m |     |
| --- | --- | --- | --- | --- | --- | --- |
independent.
11 Prove or give a counterexample: If v ,…,v and w ,…,w are linearly
|     |     |     | 1   | m   | 1 m |     |
| --- | --- | --- | --- | --- | --- | --- |
independentlistsofvectorsin\mathcal{V},thenthelistv +w ,…,v +w islinearly
|     |     |     |     | 1 1 | m m |     |
| --- | --- | --- | --- | --- | --- | --- |
independent.
12 Supposev ,…,v islinearlyindependentin\mathcal{V} andw \in \mathcal{V}. Provethatif
|             |        | 1 m                                |     |                   |          |     |
| ----------- | ------ | ---------------------------------- | --- | ----------------- | -------- | --- |
|             | +w,…,v | +wislinearlydependent,thenw\inspan(v |     |                   | ,…,v     |     |
| v           |        |                                    |     |                   | ).       |     |
|             | 1      | m                                  |     |                   | 1 m      |     |
| 13 Supposev |        | ,…,v islinearlyindependentin\mathcal{V}      |     | andw\in\mathcal{V}.           | Showthat |     |
|             |        | 1 m                                |     |                   |          |     |
|             | v ,…,v | ,wislinearlyindependent            | ⟺   | w\notinspan(v          | ,…,v     | ).  |
|             | 1      | m                                  |     |                   | 1 m      |     |
| Supposev    |        | ,…,v isalistofvectorsin\mathcal{V}.          |     | Fork \in{1,…,m},let |          |     |
| 14          |        | 1 m                                |     |                   |          |     |
+⋯+v
$$w =v .$$
k 1 k
Show that the list v ,…,v is linearly independent if and only if the list
1 m
| w   | ,…,w | islinearlyindependent. |     |     |     |     |
| --- | ---- | ---------------------- | --- | --- | --- | --- |
|     | 1 m  |                        |     |     |     |     |
15 Explain whythere does not exist a listof six polynomials that is linearly
| independentin𝒫 |     | (\mathbf{F}). |     |     |     |     |
| -------------- | --- | ---- | --- | --- | --- | --- |
| 16 Explainwhynolistoffourpolynomialsspans𝒫 |     |     |     | (\mathbf{F}). |     |     |
| ------------------------------------------ | --- | --- | --- | ---- | --- | --- |
Provethat\mathcal{V}isinfinite-dimensionalifandonlyifthereisasequencev ,v ,…
| --- | --- | --- | --- | --- | --- | --- |
ofvectorsin\mathcal{V} suchthatv ,…,v islinearlyindependentforeverypositive
1 m
integerm.
Provethat\mathbf{F}\infty
| 18  |     | isinfinite-dimensional. |     |     |     |     |
| --- | --- | ----------------------- | --- | --- | --- | --- |
19 Provethattherealvectorspaceofallcontinuousreal-valuedfunctionson
theinterval[0,1]isinfinite-dimensional.
| Suppose |     | ,p ,…,p are polynomials | in  | 𝒫 such | that      | for |
| ------- | --- | ----------------------- | --- | ------ | --------- | --- |
| 20      | p   | 0 1 m                   |     | m (\mathbf{F})  | p k (2) = | 0   |
eachk \in{0,…,m}. Provethatp ,p ,…,p isnotlinearlyindependentin
0 1 m
𝒫 (\mathbf{F}).
m

| --- | --- | --- | --------------- | --- |
### 2B Bases
In the previous section, we discussed linearly independent lists and we also
discussedspanninglists. Nowwebringtheseconceptstogetherbyconsidering
liststhathavebothproperties.
| 2.26 definition: | basis |     |     |     |
| ---------------- | ----- | --- | --- | --- |
Abasisof\mathcal{V} isalistofvectorsin\mathcal{V} thatislinearlyindependentandspans\mathcal{V}.
| 2.27 example: | bases |     |     |     |
| ------------- | ----- | --- | --- | --- |
$$(a) Thelist(1,0,…,0),(0,1,0,…,0),…,(0,…,0,1)isabasisof\mathbf{F}n,calledthe$$
standardbasisof\mathbf{F}n.
$$(b) Thelist(1,2),(3,5)isabasisof\mathbf{F}2. Notethatthislisthaslengthtwo,which$$
isthesameasthelengthofthestandardbasisof\mathbf{F}2. Inthenextsection,we
willseethatthisisnotacoincidence.
$$(c) Thelist(1,2,-4),(7,-5,6)islinearlyindependentin\mathbf{F}3 butisnotabasis$$
| of\mathbf{F}3 becauseitdoesnotspan\mathbf{F}3. |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- |
$$(d) Thelist(1,2),(3,5),(4,13)spans\mathbf{F}2butisnotabasisof\mathbf{F}2becauseitisnot$$
linearlyindependent.
$$(e) Thelist(1,1,0),(0,0,1)isabasisof{(x,x,y)\in\mathbf{F}3∶ x,y \in\mathbf{F}}.$$
$$(f) Thelist(1,-1,0),(1,0,-1)isabasisof$$
{(x,y,z)\in\mathbf{F}3∶
x+y+z=0}.
Thelist1,z,…,zm
| (g) | isabasisof𝒫 | (\mathbf{F}),calledthestandardbasisof𝒫 |     | (\mathbf{F}). |
| --- | ----------- | ----------------------------- | --- | ---- |
|     |             | m                             |     | m    |
Inadditiontothestandardbasis,\mathbf{F}n hasmanyotherbases. Forexample,
|     | (7,5),(-4,9) | and | (1,2),(3,5) |     |
| --- | ------------ | --- | ----------- | --- |
arebothbasesof\mathbf{F}2.
The next result helps explain why bases are useful. Recall that “uniquely”
means“inonlyoneway”.
criterionforbasis
2.28
| Alistv ,…,v | ofvectorsin\mathcal{V} | isabasisof\mathcal{V} | ifandonlyifeveryv\in\mathcal{V} | can |
| ----------- | ------------ | ----------- | ------------------- | --- |
| 1           | n            |             |                     |     |
bewrittenuniquelyintheform
|      |     | v=a v +⋯+a | v , |     |
| ---- | --- | ---------- | --- | --- |
| 2.29 |     | 1 1        | n n |     |
,…,a
| wherea | \in\mathbf{F}. |     |     |     |
| ------ | --- | --- | --- | --- |
| 1      | n   |     |     |     |

| --- | -------- | --- | ------------------------------ | --- | --- | --- | --- |
| Proof          | Firstsupposethatv |                     |          | ,…,v | isa  |                                     |     |
| -------------- | ----------------- | ------------------- | -------- | ---- | ---- | ----------------------------------- | --- |
|                |                   |                     |          | 1    | n    | Thisproofisessentiallyarepetitionof |     |
| basisof\mathcal{V}.      |                   | Letv\in\mathcal{V}.             | Becausev | ,…,v |      |                                     |     |
|                |                   |                     |          | 1    | n    | theideasthatledustothedefinitionof  |     |
| spans          | \mathcal{V}, there          | exist               | a ,…,a   | \in \mathbf{F}  | such | linearindependence.                 |     |
|                |                   |                     | 1        | n    |      |                                     |     |
| that2.29holds. |                   | Toshowthattherepre- |          |      |      |                                     |     |
sentationin2.29isunique,supposec ,…,c arescalarssuchthatwealsohave
|     |     |     |     |     | 1   | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
+⋯+c
|     |     |     |     | v=c | v   | v . |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 1 1 | n n |     |
Subtractingthelastequationfrom2.29,weget
|     |     |     | 0=(a | -c  | )v +⋯+(a | -c )v . |     |
| --- | --- | --- | ---- | --- | -------- | ------- | --- |
|     |     |     |      | 1 1 | 1        | n n n   |     |
Thisimpliesthateacha -c equals0(becausev ,…,v islinearlyindependent).
|     |     |     | k   | k   |     | 1 n |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
,…,a
Hence a = c = c . We have the desired uniqueness, completing the
|     | 1   | 1   | n   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
proofinonedirection.
Fortheotherdirection,supposeeveryv\in\mathcal{V} canbewrittenuniquelyinthe
formgivenby2.29. Thisimpliesthatthelistv ,…,v spans\mathcal{V}. Toshowthat
|     |                                |     |     |     |        | 1 n            |     |
| --- | ------------------------------ | --- | --- | --- | ------ | -------------- | --- |
|     | ,…,v                           |     |     |     |        | ,…,a           |     |
| v   | islinearlyindependent,supposea |     |     |     |        | \in\mathbf{F} aresuchthat |     |
| 1   | n                              |     |     |     |        | 1 n            |     |
|     |                                |     |     | 0=a | v +⋯+a | v .            |     |
|     |                                |     |     |     | 1 1    | n n            |     |
The uniqueness of the representation 2.29 (taking v = 0) now implies that
$$a =⋯=a =0. Thus v ,…,v is linearly independent and hence is a basis$$
| 1   |     | n   |     | 1 n |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
of\mathcal{V}.
Aspanninglistinavectorspacemaynotbeabasisbecauseitisnotlinearly
independent. Ournextresultsaysthatgivenanyspanninglist,some(possibly
none)ofthevectorsinitcanbediscardedsothattheremaininglistislinearly
independentandstillspansthevectorspace.
Asanexampleinthevectorspace\mathbf{F}2,iftheprocedureintheproofbelowis
appliedtothelist(1,2),(3,6),(4,7),(5,9),thenthesecondandfourthvectors
| willberemoved. |     |     | Thisleaves(1,2),(4,7),whichisabasisof\mathbf{F}2. |     |     |     |     |
| -------------- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
2.30 everyspanninglistcontainsabasis
Everyspanninglistinavectorspacecanbereducedtoabasisofthevector
space.
|       | Supposev |     | ,…,v | spans\mathcal{V}. | Wewanttoremovesomeofthevectorsfrom |     |     |
| ----- | -------- | --- | ---- | ------- | ---------------------------------- | --- | --- |
| Proof |          |     | 1 n  |         |                                    |     |     |
v ,…,v sothattheremainingvectorsformabasisof\mathcal{V}. Wedothisthroughthe
1 n
multistepprocessdescribedbelow.
|     | Startwith\mathcal{B}equaltothelistv |     |     | ,…,v | .   |     |     |
| --- | ------------------------- | --- | --- | ---- | --- | --- | --- |
1 n
Step1
|     | Ifv =0,thendeletev |     |     | from\mathcal{B}. | Ifv \neq0,thenleave\mathcal{B}unchanged. |     |     |
| --- | ------------------ | --- | --- | ------ | --------------------------- | --- | --- |
Stepk
If v is in span(v ,…,v ), then delete v from the list \mathcal{B}. If v is not in
|     | k           |     | 1                      | k-1 |     | k   | k   |
| --- | ----------- | --- | ---------------------- | --- | --- | --- | --- |
|     | span(v ,…,v |     | ),thenleave\mathcal{B}unchanged. |     |     |     |     |
|     | 1           | k-1 |                        |     |     |     |     |

Section2B Bases 41
Stop the process after step n, getting a list \mathcal{B}. This list \mathcal{B} spans \mathcal{V} because
ouroriginallistspanned\mathcal{V} andwehavediscardedonlyvectorsthatwerealready
inthespanofthepreviousvectors. Theprocessensuresthatnovectorin\mathcal{B}is
inthespanofthepreviousones. Thus\mathcal{B}islinearlyindependent, bythelinear
dependencelemma(2.19). Hence\mathcal{B}isabasisof\mathcal{V}.
Wenowcometoanimportantcorollaryofthepreviousresult.
2.31 basisoffinite-dimensionalvectorspace
Everyfinite-dimensionalvectorspacehasabasis.
Proof Bydefinition,afinite-dimensionalvectorspacehasaspanninglist. The
previousresulttellsusthateachspanninglistcanbereducedtoabasis.
Ournextresultisinsomesenseadualof2.30,whichsaidthateveryspanning
listcanbereducedtoabasis. Nowweshowthatgivenanylinearlyindependentlist,
wecanadjoinsomeadditionalvectors(thisincludesthepossibilityofadjoining
noadditionalvectors)sothattheextendedlistisstilllinearlyindependentbut
alsospansthespace.
2.32 everylinearlyindependentlistextendstoabasis
Everylinearlyindependentlistofvectorsinafinite-dimensionalvectorspace
canbeextendedtoabasisofthevectorspace.
Proof Supposeu ,…,u islinearlyindependentinafinite-dimensionalvector
1 m
space\mathcal{V}. Letw ,…,w bealistofvectorsin\mathcal{V} thatspans\mathcal{V}. Thusthelist
1 n
u ,…,u ,w ,…,w
1 m 1 n
spans \mathcal{V}. Applying the procedure of the proof of 2.30 to reduce this list to a
basisof\mathcal{V} producesabasisconsistingofthevectorsu ,…,u andsomeofthe
1 m
w’s(noneoftheu’sgetdeletedinthisprocedurebecauseu ,…,u islinearly
1 m
independent).
As an example in \mathbf{F}3, suppose we start with the linearly independent list
$$(2,3,4),(9,6,8). Ifwetakew ,w ,w tobethestandardbasisof\mathbf{F}3,thenapplying$$
1 2 3
theprocedureintheproofaboveproducesthelist
$$(2,3,4),(9,6,8),(0,1,0),$$
whichisabasisof\mathbf{F}3.
Asanapplicationoftheresultabove,
Using the same ideas but more adwe now show that every subspace of a
vanced tools, the next result can be
finite-dimensional vector space can be
provedwithoutthehypothesisthat\mathcal{V}
pairedwithanothersubspacetoforma isfinite-dimensional.
directsumofthewholespace.

42 Chapter 2 Finite-Dimensional Vector Spaces
2.33 everysubspaceof \mathcal{V} ispartofadirectsumequalto\mathcal{V}
Suppose\mathcal{V} isfinite-dimensionaland\mathcal{U} isasubspaceof\mathcal{V}. Thenthereisa
subspace\mathcal{W} of\mathcal{V} suchthat\mathcal{V} =\mathcal{U}\oplus\mathcal{W}.
Proof Because\mathcal{V} isfinite-dimensional,sois\mathcal{U} (see2.25). Thusthereisabasis
u ,…,u of\mathcal{U} (by2.31). Ofcourseu ,…,u isalinearlyindependentlistof
1 m 1 m
vectorsin\mathcal{V}. Hencethislistcanbeextendedtoabasisu ,…,u ,w ,…,w of\mathcal{V}
1 m 1 n
$$(by2.32). Let\mathcal{W} =span(w ,…,w ).$$
1 n
Toprovethat\mathcal{V} =\mathcal{U}\oplus\mathcal{W},by1.46weonlyneedtoshowthat
\mathcal{V} =\mathcal{U}+\mathcal{W} and \mathcal{U}\cap\mathcal{W} ={0}.
To prove the first equation above, suppose v \in \mathcal{V}. Then, because the list
u ,…,u ,w ,…,w spans\mathcal{V},thereexista ,…,a ,b ,…,b \in\mathbf{F} suchthat
1 m 1 n 1 m 1 n
$$v=a⏟u⏟⏟+⏟⋯+⏟a⏟u⏟+b⏟w⏟⏟+⏟⋯+⏟b⏟w⏟.$$
1 1 m m 1 1 n n
u w
We have v = u + w, where u \in \mathcal{U} and w \in \mathcal{W} are defined as above. Thus
v\in\mathcal{U}+\mathcal{W},completingtheproofthat\mathcal{V} =\mathcal{U}+\mathcal{W}.
Toshowthat\mathcal{U} \cap\mathcal{W} = {0}, supposev \in \mathcal{U} \cap\mathcal{W}. Thenthereexistscalars
a ,…,a ,b ,…,b \in\mathbf{F} suchthat
1 m 1 n
$$v=a u +⋯+a u =b w +⋯+b w .$$
1 1 m m 1 1 n n
Thus
a u +⋯+a u -b w -⋯-b w =0.
1 1 m m 1 1 n n
Becauseu ,…,u ,w ,…,w islinearlyindependent,thisimpliesthat
1 m 1 n
$$a =⋯=a =b =⋯=b =0.$$
1 m 1 n
Thusv=0,completingtheproofthat\mathcal{U}\cap\mathcal{W} ={0}.
Exercises 2B
1 Findallvectorspacesthathaveexactlyonebasis.
2 Verifyallassertionsin Example2.27.
3 (a) Let\mathcal{U} bethesubspaceof\mathbf{R}5 definedby
\mathcal{U} ={(x ,x ,x ,x ,x )\in\mathbf{R}5 ∶x =3x andx =7x }.
1 2 3 4 5 1 2 3 4
Findabasisof\mathcal{U}.
$$(b) Extendthebasisin(a)toabasisof\mathbf{R}5.$$
$$(c) Findasubspace\mathcal{W} of\mathbf{R}5 suchthat\mathbf{R}5 =\mathcal{U}\oplus\mathcal{W}.$$

| --- | --- | --- | --- | --- | --- | --------- | --- | ----- |
bethesubspaceof\mathbf{C}5
| 4 (a) | Let\mathcal{U} |     |     | definedby |     |     |     |     |
| ----- | ---- | --- | --- | --------- | --- | --- | --- | --- |
∶6z
|     | \mathcal{U} ={(z | ,z ,z | ,z ,z )\in\mathbf{C}5 |     | =z  | andz | +2z | +3z =0}. |
| --- | ------ | ----- | ---------- | --- | --- | ---- | --- | -------- |
|     |        | 1 2   | 3 4 5      |     | 1   | 2 3  | 4   | 5        |
Findabasisof\mathcal{U}.
| (b) | Extendthebasisin(a)toabasisof\mathbf{C}5. |     |                 |     |       |     |     |     |
| --- | -------------------------------- | --- | --------------- | --- | ----- | --- | --- | --- |
|     |                                  |     | of\mathbf{C}5 suchthat\mathbf{C}5 |     |       |     |     |     |
| (c) | Findasubspace\mathcal{W}                   |     |                 |     | =\mathcal{U}\oplus\mathcal{W}. |     |     |     |
5 Suppose \mathcal{V} is finite-dimensional and \mathcal{U},\mathcal{W} are subspaces of \mathcal{V} such that
\mathcal{V} = \mathcal{U} +\mathcal{W}. Provethatthereexistsabasisof\mathcal{V} consistingofvectorsin
\mathcal{U}\cup\mathcal{W}.
6 Proveorgiveacounterexample: Ifp ,p ,p ,p isalistin𝒫 (\mathbf{F})suchthat
|                       |     |      |       | 0   | 1 2              | 3   |     | 3           |
| --------------------- | --- | ---- | ----- | --- | ---------------- | --- | --- | ----------- |
|                       |     |      | ,p ,p | ,p  |                  |     | ,p  | ,p ,p       |
| noneofthepolynomialsp |     |      | 0 1   | 2 3 | hasdegree2,thenp |     | 0   | 1 2 3 isnot |
| abasisof𝒫             |     | (\mathbf{F}). |       |     |                  |     |     |             |
| 7 Supposev |     | ,v ,v ,v | isabasisof\mathcal{V}. | Provethat |       |     |     |     |
| ---------- | --- | -------- | ------------ | --------- | ----- | --- | --- | --- |
|            |     | 1 2 3 4  |              |           |       |     |     |     |
|            |     |          | v +v         | ,v +v     | ,v +v | ,v  |     |     |
|            |     |          | 1 2          | 2         | 3 3   | 4 4 |     |     |
isalsoabasisof\mathcal{V}.
8 Proveorgiveacounterexample: Ifv ,v ,v ,v isabasisof\mathcal{V} and\mathcal{U} isa
|             |     |           |           |     | 1 2 3  | 4   |          |        |
| ----------- | --- | --------- | --------- | --- | ------ | --- | -------- | ------ |
| subspaceof\mathcal{V} |     | suchthatv | ,v \in\mathcal{U}andv |     | \notin\mathcal{U}andv |     | \notin\mathcal{U},thenv | ,v isa |
|             |     |           | 1 2       |     | 3      |     | 4        | 1 2    |
basisof\mathcal{U}.
| 9 Supposev  |      | ,…,v isalistofvectorsin\mathcal{V}. |             |              | Fork         | \in{1,…,m},let |     |              |
| ----------- | ---- | ------------------------- | ----------- | ------------ | ------------ | ------------ | --- | ------------ |
|             |      | 1 m                       |             |              |              |              |     |              |
|             |      |                           | w           | =v +⋯+v      |              | .            |     |              |
|             |      |                           | k           | 1            | k            |              |     |              |
| Showthatv   |      | ,…,v                      | isabasisof\mathcal{V} | ifandonlyifw |              | ,…,w         |     | isabasisof\mathcal{V}. |
|             |      | 1 m                       |             |              |              | 1            | m   |              |
| 10 Suppose\mathcal{U} |      | and\mathcal{W} aresubspacesof\mathcal{V}      |             |              | suchthat\mathcal{V}    | =\mathcal{U}\oplus\mathcal{W}.        |     | Supposealso  |
| thatu       | ,…,u | isabasisof\mathcal{U}               | andw        | ,…,w         | isabasisof\mathcal{W}. |              |     | Provethat    |
|             | 1    | m                         |             | 1            | n            |              |     |              |
|             |      |                           | u ,…,u      | ,w           | ,…,w         |              |     |              |
|             |      |                           | 1           | m            | 1            | n            |     |              |
isabasisof\mathcal{V}.
11 Suppose\mathcal{V} isarealvectorspace. Showthatifv ,…,v isabasisof\mathcal{V} (asa
|     |     |     |     |     |     | 1   | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
realvectorspace),thenv ,…,v isalsoabasisofthecomplexification\mathcal{V}
|     |     |     | 1   | n   |     |     |     | \mathbf{C}   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
$$(asacomplexvectorspace).$$
See Exercise8in Section1Bforthedefinitionofthecomplexification\mathcal{V} .
\mathbf{C}

44 Chapter 2 Finite-Dimensional Vector Spaces
### 2C Dimension
Althoughwehavebeendiscussingfinite-dimensionalvectorspaces,wehavenot
yetdefinedthedimensionofsuchanobject. Howshoulddimensionbedefined?
Areasonabledefinitionshouldforcethedimensionof\mathbf{F}n toequaln. Noticethat
thestandardbasis
$$(1,0,…,0),(0,1,0,…,0),…,(0,…,0,1)$$
of\mathbf{F}n haslengthn. Thuswearetemptedtodefinethedimensionasthelengthof
abasis. However,afinite-dimensionalvectorspaceingeneralhasmanydifferent
bases,andourattempteddefinitionmakessenseonlyifallbasesinagivenvector
spacehavethesamelength. Fortunatelythatturnsouttobethecase,aswenow
show.
2.34 basislengthdoesnotdependonbasis
Anytwobasesofafinite-dimensionalvectorspacehavethesamelength.
Proof Suppose\mathcal{V} isfinite-dimensional. Let\mathcal{B} and\mathcal{B} betwobasesof\mathcal{V}. Then
1 2
\mathcal{B} islinearlyindependentin\mathcal{V} and\mathcal{B} spans\mathcal{V},sothelengthof\mathcal{B} isatmostthe
1 2 1
lengthof\mathcal{B} (by2.22). Interchangingtherolesof\mathcal{B} and\mathcal{B} ,wealsoseethatthe
2 1 2
lengthof\mathcal{B} isatmostthelengthof\mathcal{B} . Thusthelengthof\mathcal{B} equalsthelength
2 1 1
of\mathcal{B} ,asdesired.
Nowthatweknowthatanytwobasesofafinite-dimensionalvectorspace
havethesamelength,wecanformallydefinethedimensionofsuchspaces.
**2.35 定义：** dimension,dim\mathcal{V}
• The dimension of a finite-dimensional vector space is the length of any
basisofthevectorspace.
• Thedimensionofafinite-dimensionalvectorspace\mathcal{V} isdenotedbydim\mathcal{V}.
**2.36 例：** dimensions
• dim\mathbf{F}n =nbecausethestandardbasisof\mathbf{F}n haslengthn.
• dim𝒫 (\mathbf{F})=m+1becausethestandardbasis1,z,…,zmof𝒫 (\mathbf{F})haslength
m m
m+1.
• If\mathcal{U} = {(x,x,y) \in \mathbf{F}3∶ x,y \in \mathbf{F}},thendim\mathcal{U} = 2because(1,1,0),(0,0,1)
isabasisof\mathcal{U}.
• If \mathcal{U} = {(x,y,z) \in \mathbf{F}3∶ x + y + z = 0}, then dim\mathcal{U} = 2 because the list
$$(1,-1,0),(1,0,-1)isabasisof\mathcal{U}.$$

| --- | --- | --- | --- | --------- | --- | --------- |
Every subspace of a finite-dimensional vector space is finite-dimensional
$$(by2.25)andsohasadimension. Thenextresultgivestheexpectedinequality$$
aboutthedimensionofasubspace.
dimensionofasubspace
2.37
| If\mathcal{V} isfinite-dimensionaland\mathcal{U} |     |     | isasubspaceof\mathcal{V},thendim\mathcal{U} |     |     | \leqdim\mathcal{V}. |
| ---------------------------- | --- | --- | ----------------------- | --- | --- | ------ |
Proof Suppose \mathcal{V} is finite-dimensional and \mathcal{U} is a subspace of \mathcal{V}. Think of
a basis of \mathcal{U} as a linearly independent list in \mathcal{V}, and think of a basis of \mathcal{V} as a
| spanninglistin\mathcal{V}. | Nowuse2.22toconcludethatdim\mathcal{U} |            |      |          | \leqdim\mathcal{V}.       |               |
| ---------------- | ---------------------------- | ---------- | ---- | -------- | ------------ | ------------- |
| To check         | that a list                  | of vectors | in \mathcal{V} |          |              |               |
|                  |                              |            |      | The real | vector space | \mathbf{R}2 has dimen- |
| is a basis       | of \mathcal{V}, we must,               | according  | to   |          |              |               |
siontwo;thecomplexvectorspace\mathbf{C}
thedefinition,showthatthelistinques-
|     |     |     |     | has dimension | one. | As sets, \mathbf{R}2 can |
| --- | --- | --- | --- | ------------- | ---- | --------------- |
tionsatisfiestwoproperties: itmustbe be identified with \mathbf{C} (and addition is
linearlyindependentanditmustspan\mathcal{V}.
thesameonbothspaces,asisscalar
Thenexttworesultsshowthatifthelist multiplicationbyrealnumbers). Thus
inquestionhastherightlength,thenwe
whenwetalkaboutthedimensionof
only need to check that it satisfies one avectorspace,theroleplayedbythe
ofthetworequiredproperties. Firstwe choiceof \mathbf{F}cannotbeneglected.
provethateverylinearlyindependentlist
oftherightlengthisabasis.
2.38 linearlyindependentlistoftherightlengthisabasis
Suppose \mathcal{V} is finite-dimensional. Then every linearly independent list of
| vectorsin\mathcal{V} | oflengthdim\mathcal{V} |     | isabasisof\mathcal{V}. |     |     |     |
| ---------- | ------------ | --- | ------------ | --- | --- | --- |
Proof Supposedim\mathcal{V} =nandv ,…,v islinearlyindependentin\mathcal{V}. Thelist
|     |     |     | 1   | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
v ,…,v canbeextendedtoabasisof\mathcal{V}(by2.32). However,everybasisof\mathcal{V}has
1 n
lengthn,sointhiscasetheextensionisthetrivialone,meaningthatnoelements
| areadjoinedtov | ,…,v | . Thusv | ,…,v | isabasisof\mathcal{V},asdesired. |     |     |
| -------------- | ---- | ------- | ---- | ---------------------- | --- | --- |
|                | 1    | n       | 1    | n                      |     |     |
Thenextresultisausefulconsequenceofthepreviousresult.
subspaceoffulldimensionequalsthewholespace
2.39
Suppose that \mathcal{V} is finite-dimensional and \mathcal{U} is a subspace of \mathcal{V} such that
| dim\mathcal{U} =dim\mathcal{V}. | Then\mathcal{U}             | =\mathcal{V}. |     |                                |     |     |
| ----------- | ----------------- | --- | --- | ------------------------------ | --- | --- |
| Proof Letu  | ,…,u beabasisof\mathcal{U}. |     |     | Thusn = dim\mathcal{U},andbyhypothesiswe |     |     |
1 n
alsohaven=dim\mathcal{V}. Thusu ,…,u isalinearlyindependentlistofvectorsin\mathcal{V}
1 n
$$(becauseitisabasisof\mathcal{U})oflengthdim\mathcal{V}. From2.38,weseethatu ,…,u isa$$
1 n
basisof\mathcal{V}. Inparticulareveryvectorin\mathcal{V} isalinearcombinationofu ,…,u .
1 n
Thus\mathcal{U} =\mathcal{V}.

| -------- | ------------------------------ | --- | --- | --- |
\mathbf{F}2
| 2.40 example: | abasisof |     |     |     |
| ------------- | -------- | --- | --- | --- |
Considerthelist(5,7),(4,3)ofvectorsin\mathbf{F}2. Thislistoflengthtwoislinearly
independentin\mathbf{F}2 (becauseneithervectorisascalarmultipleoftheother). Note
that\mathbf{F}2 hasdimensiontwo. Thus2.38impliesthatthelinearlyindependentlist
$$(5,7),(4,3)oflengthtwoisabasisof\mathbf{F}2(wedonotneedtobothercheckingthat$$
itspans\mathbf{F}2).
|               | abasisofasubspaceof | 𝒫            |     |     |
| ------------- | ------------------- | ------------ | --- | --- |
| 2.41 example: |                     | 3 (\mathbf{R})        |     |     |
| Let\mathcal{U}          | bethesubspaceof𝒫    | (\mathbf{R})definedby |     |     |
\mathcal{U} ={p\in𝒫 (\mathbf{R})∶p′(5)=0}.
Tofindabasisof\mathcal{U},firstnotethateachofthepolynomials1,(x-5)2,and(x-5)3
isin\mathcal{U}.
| Supposea,b,c | \in\mathbf{R} and            |     |     |     |
| ------------ | ----------------- | --- | --- | --- |
|              | a+b(x-5)2+c(x-5)3 |     | =0  |     |
foreveryx \in\mathbf{R}. Withoutexplicitlyexpandingtheleftsideoftheequationabove,
cx3 x3
we can see that the left side has a term. Because the right side has no
term,thisimpliesthatc = 0. Becausec = 0,weseethattheleftsidehasabx2
term,whichimpliesthatb = 0. Becauseb = c = 0,wecanalsoconcludethat
$$a = 0. Thus the equation above implies that a = b = c = 0. Hence the list$$
1,(x-5)2,(x-5)3
|     | islinearlyindependentin\mathcal{U}. |       | Thus3\leqdim\mathcal{U}. | Hence |
| --- | ------------------------- | ----- | ----------- | ----- |
|     | 3\leqdim\mathcal{U}                    | \leqdim𝒫 | (\mathbf{R})=4,      |       |
wherewehaveused2.37.
Thepolynomialxisnotin\mathcal{U} becauseitsderivativeistheconstantfunction1.
Thus\mathcal{U} \neq𝒫 (\mathbf{R}). Hencedim\mathcal{U} \neq4(by2.39). Theinequalityabovenowimplies
Thusthelinearlyindependentlist1,(x-5)2,(x-5)3
| thatdim\mathcal{U}   | =3.                 |           |     | in\mathcal{U} has |
| ---------- | ------------------- | --------- | --- | ------- |
| lengthdim\mathcal{U} | andhenceisabasisof\mathcal{U} | (by2.38). |     |         |
Nowweprovethataspanninglistoftherightlengthisabasis.
spanninglistoftherightlengthisabasis
2.42
Suppose\mathcal{V} isfinite-dimensional. Theneverylistofvectorsin\mathcal{V} thatspans\mathcal{V}
| andhaslengthdim\mathcal{V} | isabasisof\mathcal{V}. |     |     |     |
| ---------------- | ------------ | --- | --- | --- |
Proof Suppose dim\mathcal{V} = n and v ,…,v spans \mathcal{V}. The list v ,…,v can be
|     |     | 1 n |     | 1 n |
| --- | --- | --- | --- | --- |
reducedtoabasisof\mathcal{V} (by2.30). However,everybasisof\mathcal{V} haslengthn,soin
thiscasethereductionisthetrivialone,meaningthatnoelementsaredeleted
| ,…,v  | ,…,v    |                        |     |     |
| ----- | ------- | ---------------------- | --- | --- |
| fromv | . Thusv | isabasisof\mathcal{V},asdesired. |     |     |
| 1     | n 1     | n                      |     |     |

Section2C Dimension 47
Thenextresultgivesaformulaforthedimensionofthesumoftwosubspaces
of a finite-dimensional vector space. This formula is analogous to a familiar
countingformula: thenumberofelementsintheunionoftwofinitesetsequals
thenumberofelementsinthefirstset,plusthenumberofelementsinthesecond
set,minusthenumberofelementsintheintersectionofthetwosets.
2.43 dimensionofasum
If\mathcal{V} and\mathcal{V} aresubspacesofafinite-dimensionalvectorspace,then
1 2
dim(\mathcal{V} +\mathcal{V} )=dim\mathcal{V} +dim\mathcal{V} -dim(\mathcal{V} \cap\mathcal{V} ).
1 2 1 2 1 2
Proof Letv ,…,v beabasisof\mathcal{V} \cap\mathcal{V} ;thusdim(\mathcal{V} \cap\mathcal{V} ) = m. Because
1 m 1 2 1 2
v ,…,v isabasisof\mathcal{V} \cap\mathcal{V} ,itislinearlyindependentin\mathcal{V} . Hencethislistcan
1 m 1 2 1
beextendedtoabasisv ,…,v ,u ,…,u of\mathcal{V} (by2.32). Thusdim\mathcal{V} =m+j.
1 m 1 j 1 1
Alsoextendv ,…,v toabasisv ,…,v ,w ,…,w of\mathcal{V} ;thusdim\mathcal{V} =m+k.
1 m 1 m 1 k 2 2
Wewillshowthat
2.44 v ,…,v ,u ,…,u,w ,…,w
1 m 1 j 1 k
isabasisof\mathcal{V} +\mathcal{V} . Thiswillcompletetheproof,becausethenwewillhave
1 2
dim(\mathcal{V} +\mathcal{V} )=m+j+k
1 2
=(m+j)+(m+k)-m
=dim\mathcal{V} +dim\mathcal{V} -dim(\mathcal{V} \cap\mathcal{V} ).
1 2 1 2
Thelist2.44iscontainedin\mathcal{V} \cup\mathcal{V} andthusiscontainedin\mathcal{V} +\mathcal{V} . The
1 2 1 2
spanofthislistcontains\mathcal{V} andcontains\mathcal{V} andhenceisequalto\mathcal{V} +\mathcal{V} . Thus
1 2 1 2
toshowthat2.44isabasisof\mathcal{V} +\mathcal{V} weonlyneedtoshowthatitislinearly
1 2
independent.
Toprovethat2.44islinearlyindependent,suppose
a v +⋯+a v +b u +⋯+bu +c w +⋯+c w =0,
1 1 m m 1 1 j j 1 1 k k
whereallthea’s,b’s,andc’sarescalars. Weneedtoprovethatallthea’s,b’s,
andc’sequal0. Theequationabovecanberewrittenas
2.45 c w +⋯+c w =-a v -⋯-a v -b u -⋯-bu,
1 1 k k 1 1 m m 1 1 j j
whichshowsthatc w +⋯+c w \in \mathcal{V} . Allthew’sarein\mathcal{V} ,sothisimplies
1 1 k k 1 2
thatc w +⋯+c w \in \mathcal{V} \cap\mathcal{V} . Becausev ,…,v isabasisof\mathcal{V} \cap\mathcal{V} ,we
1 1 k k 1 2 1 m 1 2
have
c w +⋯+c w =d v +⋯+d v
1 1 k k 1 1 m m
forsomescalarsd ,…,d . Butv ,…,v ,w ,…,w islinearlyindependent,so
1 m 1 m 1 k
thelastequationimpliesthatallthec’s(andd’s)equal0. Thus2.45becomesthe
equation
a v +⋯+a v +b u +⋯+bu =0.
1 1 m m 1 1 j j
Becausethelistv ,…,v ,u ,…,u islinearlyindependent,thisequationimplies
1 m 1 j
thatallthea’sandb’sare0,completingtheproof.

| -------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
For\mathcal{S}afiniteset,let#\mathcal{S}denotethenumberofelementsof\mathcal{S}. Thetablebelow
comparesfinitesetswithfinite-dimensionalvectorspaces,showingtheanalogy
between#\mathcal{S}(forsets)anddim\mathcal{V}(forvectorspaces),aswellastheanalogybetween
unionsofsubsets(inthecontextofsets)andsumsofsubspaces(inthecontextof
vectorspaces).
|               |     | sets |     |     |                                   |     | vectorspaces |     |     |
| ------------- | --- | ---- | --- | --- | --------------------------------- | --- | ------------ | --- | --- |
| \mathcal{S}isafiniteset |     |      |     |     | \mathcal{V}isafinite-dimensionalvectorspace |     |              |     |     |
| #\mathcal{S}            |     |      |     |     | dim\mathcal{V}                              |     |              |     |     |
forsubsets\mathcal{S} ,\mathcal{S} of\mathcal{S},theunion\mathcal{S} \cup\mathcal{S} forsubspaces\mathcal{V} ,\mathcal{V} of\mathcal{V},thesum\mathcal{V} +\mathcal{V}
|     | 1   | 2   |     | 1   | 2   |     | 1   | 2   | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
isthesmallestsubsetof\mathcal{S}containing\mathcal{S} 1 isthesmallestsubspaceof\mathcal{V}containing
| and\mathcal{S}     |        |            |       |     | \mathcal{V}     | and\mathcal{V}  |          |              |      |
| -------- | ------ | ---------- | ----- | --- | ----- | ----- | -------- | ------------ | ---- |
| #(\mathcal{S} \cup\mathcal{S}   | )      |            |       |     | dim(\mathcal{V} | +\mathcal{V}    | )        |              |      |
| 1        | 2      |            |       |     |       | 1     | 2        |              |      |
| =#\mathcal{S} +#\mathcal{S}  | -#(\mathcal{S}   | \cap\mathcal{S}         | )     |     | =dim\mathcal{V} |       | +dim\mathcal{V}    | -dim(\mathcal{V}       | \cap\mathcal{V} ) |
| 1        | 2      | 1          | 2     |     |       | 1     |          | 2 1          | 2    |
|          |        | +#\mathcal{S}        |       |     |       | +\mathcal{V}    |          | +dim\mathcal{V}        |      |
| #(\mathcal{S} 1 \cup\mathcal{S} | 2 )=#\mathcal{S} | 1          | 2     |     | dim(\mathcal{V} | 1     | 2 )=dim\mathcal{V} | 1            | 2    |
| ⟺ \mathcal{S}      | \cap\mathcal{S} =\emptyset  |            |       |     | ⟺     | \mathcal{V} \cap\mathcal{V}  | ={0}     |              |      |
| 1        | 2      |            |       |     |       | 1     | 2        |              |      |
| \mathcal{S} \cup⋯\cup\mathcal{S}   | is     | a disjoint | union | ⟺   | \mathcal{V}     | + ⋯ + | \mathcal{V} is     | a direct sum | ⟺    |
| 1        | m      |            |       |     | 1     |       | m        |              |      |
| #(\mathcal{S} \cup⋯\cup\mathcal{S} |        | )=#\mathcal{S}       | +⋯+#\mathcal{S} |     | dim(\mathcal{V} | +     | ⋯ + \mathcal{V}    | )            |      |
| 1        | m      | 1          |       | m   |       | 1     |          | m            |      |
|          |        |            |       |     | =dim\mathcal{V} |       | +⋯+dim\mathcal{V}  |              |      |
|          |        |            |       |     |       | 1     |          | m            |      |
Thelastrowabovefocusesontheanalogybetweendisjointunions(forsets)
anddirectsums(forvectorspaces). Theproofoftheresultinthelastboxabove
willbegivenin3.94.
Youshouldbeabletofindresultsaboutsetsthatcorrespond,viaanalogy,to
theresultsaboutvectorspacesin Exercises12through18.
| Exercises                | 2C  |     |     |     |                              |     |     |     |            |
| ------------------------ | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ---------- |
| Showthatthesubspacesof\mathbf{R}2 |     |     |     |     | areprecisely{0},alllinesin\mathbf{R}2 |     |     |     |            |
| 1                        |     |     |     |     |                              |     |     |     | containing |
theorigin,and\mathbf{R}2.
2 Showthatthesubspacesof\mathbf{R}3 areprecisely{0},alllinesin\mathbf{R}3 containing
| theorigin,allplanesin\mathbf{R}3 |     |     |     | containingtheorigin,and\mathbf{R}3. |     |     |     |     |     |
| ----------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
$$(\mathbf{F})∶p(6)=0}.$$
| 3 (a) | Let\mathcal{U} | ={p\in𝒫 |     |     | Findabasisof\mathcal{U}. |     |     |     |     |
| ----- | ---- | ----- | --- | --- | -------------- | --- | --- | --- | --- |
| (b) | Extendthebasisin(a)toabasisof𝒫 |     |     |     |     | (\mathbf{F}). |     |     |     |
| --- | ------------------------------ | --- | --- | --- | --- | ---- | --- | --- | --- |
| (c)   | Findasubspace\mathcal{W} |       | of𝒫           | (\mathbf{F})suchthat𝒫 |     |                | (\mathbf{F})=\mathcal{U}\oplus\mathcal{W}. |     |     |
| ----- | -------------- | ----- | ------------- | ------------ | --- | -------------- | -------- | --- | --- |
| 4 (a) | Let\mathcal{U}           | ={p\in𝒫 | (\mathbf{R})∶p″(6)=0}. |              |     | Findabasisof\mathcal{U}. |          |     |     |
| (b) | Extendthebasisin(a)toabasisof𝒫 |     |     |     |     | (\mathbf{R}). |     |     |     |
| --- | ------------------------------ | --- | --- | --- | --- | ---- | --- | --- | --- |
| (c) | Findasubspace\mathcal{W}                 |       | of𝒫             | (\mathbf{R})suchthat𝒫 |     |                | (\mathbf{R})=\mathcal{U}\oplus\mathcal{W}. |     |     |
| --- | ------------------------------ | ----- | --------------- | ------------ | --- | -------------- | -------- | --- | --- |
| (a) | Let\mathcal{U}                           | ={p\in𝒫 | (\mathbf{F})∶p(2)=p(5)}. |              |     | Findabasisof\mathcal{U}. |          |     |     |
| (b) | Extendthebasisin(a)toabasisof𝒫 |       |                 |              |     | (\mathbf{F}).           |          |     |     |
| (c) | Findasubspace\mathcal{W} |     | of𝒫 | (\mathbf{F})suchthat𝒫 |     |     | (\mathbf{F})=\mathcal{U}\oplus\mathcal{W}. |     |     |
| --- | -------------- | --- | --- | ------------ | --- | --- | -------- | --- | --- |

Section2C Dimension 49
6 (a) Let\mathcal{U} ={p\in𝒫 (\mathbf{F})∶p(2)=p(5)=p(6)}. Findabasisof\mathcal{U}.
$$(b) Extendthebasisin(a)toabasisof𝒫 (\mathbf{F}).$$
$$(c) Findasubspace\mathcal{W} of𝒫 (\mathbf{F})suchthat𝒫 (\mathbf{F})=\mathcal{U}\oplus\mathcal{W}.$$
4 4
7 (a) Let\mathcal{U} ={p\in𝒫 (\mathbf{R})∶ \int 1 p=0}. Findabasisof\mathcal{U}.
4 -1
$$(b) Extendthebasisin(a)toabasisof𝒫 (\mathbf{R}).$$
$$(c) Findasubspace\mathcal{W} of𝒫 (\mathbf{R})suchthat𝒫 (\mathbf{R})=\mathcal{U}\oplus\mathcal{W}.$$
4 4
8 Supposev ,…,v islinearlyindependentin\mathcal{V} andw\in\mathcal{V}. Provethat
1 m
dimspan(v +w,…,v +w)\geqm-1.
1 m
9 Supposemisapositiveintegerandp ,p ,…,p \in𝒫(\mathbf{F})aresuchthateach
0 1 m
p hasdegreek. Provethatp ,p ,…,p isabasisof𝒫 (\mathbf{F}).
k 0 1 m m
10 Supposemisapositiveinteger. For0\leqk \leqm,let
p (x)=xk(1-x)m-k.
k
Showthatp ,…,p isabasisof𝒫 (\mathbf{F}).
0 m m
Thebasisinthisexerciseleadstowhatarecalled Bernsteinpolynomials.
approximatecontinuousfunctionson[0,1].
11 Suppose\mathcal{U} and\mathcal{W} arebothfour-dimensionalsubspacesof\mathbf{C}6. Provethat
thereexisttwovectorsin\mathcal{U}\cap\mathcal{W} suchthatneitherofthesevectorsisascalar
multipleoftheother.
12 Supposethat\mathcal{U}and\mathcal{W}aresubspacesof\mathbf{R}8suchthatdim\mathcal{U} =3,dim\mathcal{W} =5,
and\mathcal{U}+\mathcal{W} =\mathbf{R}8. Provethat\mathbf{R}8 =\mathcal{U}\oplus\mathcal{W}.
13 Suppose\mathcal{U} and\mathcal{W} arebothfive-dimensionalsubspacesof\mathbf{R}9. Provethat
\mathcal{U}\cap\mathcal{W} \neq{0}.
14 Suppose\mathcal{V} isaten-dimensionalvectorspaceand\mathcal{V} ,\mathcal{V} ,\mathcal{V} aresubspaces
1 2 3
of\mathcal{V} withdim\mathcal{V} =dim\mathcal{V} =dim\mathcal{V} =7. Provethat\mathcal{V} \cap\mathcal{V} \cap\mathcal{V} \neq{0}.
1 2 3 1 2 3
15 Suppose \mathcal{V} is finite-dimensional and \mathcal{V} ,\mathcal{V} ,\mathcal{V} are subspaces of \mathcal{V} with
1 2 3
dim\mathcal{V} +dim\mathcal{V} +dim\mathcal{V} >2dim\mathcal{V}. Provethat\mathcal{V} \cap\mathcal{V} \cap\mathcal{V} \neq{0}.
1 2 3 1 2 3
16 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{U} isasubspaceof\mathcal{V} with\mathcal{U} \neq\mathcal{V}. Let
$$n = dim\mathcal{V} andm = dim\mathcal{U}. Provethatthereexistn-msubspacesof\mathcal{V},$$
eachofdimensionn-1,whoseintersectionequals\mathcal{U}.
17 Supposethat\mathcal{V} ,…,\mathcal{V} arefinite-dimensionalsubspacesof\mathcal{V}. Provethat
1 m
\mathcal{V} +⋯+\mathcal{V} isfinite-dimensionaland
1 m
dim(\mathcal{V} +⋯+\mathcal{V} )\leqdim\mathcal{V} +⋯+dim\mathcal{V} .
1 m 1 m
Theinequalityaboveisanequalityifandonlyif \mathcal{V} +⋯+\mathcal{V} isadirect
1 m
sum,aswillbeshownin3.94.

50 Chapter 2 Finite-Dimensional Vector Spaces
18 Suppose\mathcal{V} isfinite-dimensional,withdim\mathcal{V} =n\geq1. Provethatthereexist
one-dimensionalsubspaces\mathcal{V} ,…,\mathcal{V} of\mathcal{V} suchthat
1 n
\mathcal{V} =\mathcal{V} \oplus⋯\oplus\mathcal{V} .
1 n
19 Explainwhyyoumightguess,motivatedbyanalogywiththeformulafor
thenumberofelementsintheunionofthreefinitesets,thatif\mathcal{V} ,\mathcal{V} ,\mathcal{V} are
1 2 3
subspacesofafinite-dimensionalvectorspace,then
dim(\mathcal{V} +\mathcal{V} +\mathcal{V} )
1 2 3
=dim\mathcal{V} +dim\mathcal{V} +dim\mathcal{V}
1 2 3
-dim(\mathcal{V} \cap\mathcal{V} )-dim(\mathcal{V} \cap\mathcal{V} )-dim(\mathcal{V} \cap\mathcal{V} )
1 2 1 3 2 3
+dim(\mathcal{V} \cap\mathcal{V} \cap\mathcal{V} ).
1 2 3
Theneitherprovetheformulaaboveorgiveacounterexample.
20 Prove that if \mathcal{V} ,\mathcal{V} , and \mathcal{V} are subspaces of a finite-dimensional vector
1 2 3
space,then
dim(\mathcal{V} +\mathcal{V} +\mathcal{V} )
1 2 3
=dim\mathcal{V} +dim\mathcal{V} +dim\mathcal{V}
1 2 3
dim(\mathcal{V} \cap\mathcal{V} )+dim(\mathcal{V} \cap\mathcal{V} )+dim(\mathcal{V} \cap\mathcal{V} )
- 1 2 1 3 2 3
dim((\mathcal{V} +\mathcal{V} )\cap\mathcal{V} )+dim((\mathcal{V} +\mathcal{V} )\cap\mathcal{V} )+dim((\mathcal{V} +\mathcal{V} )\cap\mathcal{V} )
- 1 2 3 1 3 2 2 3 1 .
Theformulaabovemayseemstrangebecausetherightsidedoesnotlook
likeaninteger.
I at once gave up my former occupations, set down natural history and all its
progenyasadeformedandabortivecreation,andentertainedthegreatestdisdain
forawould-besciencewhichcouldneverevenstepwithinthethresholdofreal
knowledge. Inthismood Ibetookmyselftothemathematicsandthebranchesof
studyappertainingtothatscienceasbeingbuiltuponsecurefoundations,andso
worthyofmyconsideration.
—Frankenstein,Mary Wollstonecraft Shelley
