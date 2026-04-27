---
title: Chapter 5
source: Clippings/LADR4e.pdf
created: 2026-04-23
type: chapter
tags:
  - book
  - chapter
---

# Chapter 5
Eigenvalues and Eigenvectors
Linearmapsfromonevectorspacetoanothervectorspaceweretheobjectsof
studyin Chapter 3. Nowwebeginourinvestigationofoperators,whicharelinear
mapsfromavectorspacetoitself. Theirstudyconstitutesthemostimportant
partoflinearalgebra.
Tolearnaboutanoperator,wemighttryrestrictingittoasmallersubspace.
Askingforthatrestrictiontobeanoperatorwillleadustothenotionofinvariant
subspaces. Eachone-dimensionalinvariantsubspacearisesfromavectorthat
theoperatormapsintoascalarmultipleofthevector. Thispathwillleadusto
eigenvectorsandeigenvalues.
Wewillthenproveoneofthemostimportantresultsinlinearalgebra: every
operatoronafinite-dimensionalnonzerocomplexvectorspacehasaneigenvalue.
Thisresultwillallowustoshowthatforeachoperatoronafinite-dimensional
complexvectorspace,thereisabasisofthevectorspacewithrespecttowhich
thematrixoftheoperatorhasatleastalmosthalfitsentriesequalto0.
standingassumptionsforthischapter
• \mathbf{F} denotes\mathbf{R} or\mathbf{C}.
• \mathcal{V} denotesavectorspaceover\mathbf{F}.
Hans-Peter Postel CCBY
Statueof Leonardoof Pisa(1170–1250,approximatedates),alsoknownas Fibonacci.
Exercise21in Section5Dshowshowlinearalgebracanbeusedtofind
theexplicitformulaforthe Fibonaccisequenceshownonthefrontcover.

| --- | --- | --------- | ------------------ | --- |
| 5A Invariant | Subspaces |     |     |     |
| ------------ | --------- | --- | --- | --- |
Eigenvalues
| 5.1 definition: | operator |     |     |     |
| --------------- | -------- | --- | --- | --- |
Alinearmapfromavectorspacetoitselfiscalledanoperator.
| Suppose\mathcal{T} \inℒ(\mathcal{V}). |      | Ifm\geq2and |                        |              |
| --------------- | ---- | -------- | ---------------------- | ------------ |
|                 |      |          | Recall that we defined | the notation |
| \mathcal{V} =\mathcal{V}            | \oplus⋯\oplus\mathcal{V} | ,        | ℒ(\mathcal{V})tomeanℒ(\mathcal{V},\mathcal{V}).      |              |
1 m
whereeach\mathcal{V} isanonzerosubspaceof\mathcal{V}, thentounderstandthebehaviorof
k
\mathcal{T} weonlyneedtounderstandthebehaviorofeach\mathcal{T}| ; here\mathcal{T}| denotesthe
\mathcal{V} k \mathcal{V} k
restrictionof\mathcal{T}tothesmallerdomain\mathcal{V} . Dealingwith\mathcal{T}| shouldbeeasierthan
|     |     | k   | \mathcal{V}   |     |
| --- | --- | --- | --- | --- |
k
| dealingwith\mathcal{T} | because\mathcal{V} | isasmallervectorspacethan\mathcal{V}. |     |     |
| ------------ | -------- | --------------------------- | --- | --- |
k
However, ifweintendtoapplytoolsusefulinthestudyofoperators(such
astakingpowers),thenwehaveaproblem: \mathcal{T}| maynotmap\mathcal{V} intoitself;in
|     |     |     | \mathcal{V} k | k   |
| --- | --- | --- | --- | --- |
otherwords,\mathcal{T}| maynotbeanoperatoron\mathcal{V} . Thusweareledtoconsideronly
|     | \mathcal{V}   |     | k   |     |
| --- | --- | --- | --- | --- |
k
decompositionsof\mathcal{V}oftheformaboveinwhich\mathcal{T}mapseach\mathcal{V} intoitself. Hence
k
| wenowgiveanametosubspacesof\mathcal{V} |                                            |     | thatgetmappedintothemselvesby\mathcal{T}. |     |
| ---------------------------- | ------------------------------------------ | --- | ------------------------------- | --- |
| 5.2 definition:              | invariantsubspace                          |     |                                 |     |
| \inℒ(\mathcal{V}).                       | Asubspace\mathcal{U}of\mathcal{V}iscalledinvariantunder\mathcal{T}if\mathcal{T}u\in\mathcal{U} |     |                                 |     |
Suppose\mathcal{T}
foreveryu\in\mathcal{U}.
| Thus\mathcal{U} isinvariantunder\mathcal{T} |     | if\mathcal{T}| isanoperatoron\mathcal{U}. |     |     |
| ----------------------- | --- | --------------------- | --- | --- |
\mathcal{U}
| 5.3 example: | subspaceinvariantunderdifferentiationoperator |     |     |     |
| ------------ | --------------------------------------------- | --- | --- | --- |
p′.
| Supposethat\mathcal{T} | \in ℒ(𝒫(\mathbf{R}))isdefinedby\mathcal{T}p |     | = Then𝒫 | (\mathbf{R}),whichisa |
| ------------ | ---------------------- | --- | ------- | ------------ |
subspaceof𝒫(\mathbf{R}),isinvariantunder\mathcal{T}becauseifp\in𝒫(\mathbf{R})hasdegreeatmost4,
thenp′ alsohasdegreeatmost4.
**5.4 例：** fourinvariantsubspaces,notnecessarilyalldifferent
\inℒ(\mathcal{V}),thenthefollowingsubspacesof\mathcal{V}
| If\mathcal{T}                                 |     |     | areallinvariantunder\mathcal{T}. |     |
| ----------------------------------- | --- | --- | ---------------------- | --- |
| {0} Thesubspace{0}isinvariantunder\mathcal{T} |     |     | becauseifu\in{0},thenu=0 |     |
andhence\mathcal{T}u=0\in{0}.
| \mathcal{V} Thesubspace\mathcal{V} |     | isinvariantunder\mathcal{T} | becauseifu\in\mathcal{V},then\mathcal{T}u\in\mathcal{V}. |     |
| -------------- | --- | ----------------- | ---------------------- | --- |
null\mathcal{T} Thesubspacenull\mathcal{T} isinvariantunder\mathcal{T} becauseifu\innull\mathcal{T},then
\mathcal{T}u=0,andhence\mathcal{T}u\innull\mathcal{T}.
range\mathcal{T} The subspace range\mathcal{T} is invariant under \mathcal{T} because if u \in range\mathcal{T},
then\mathcal{T}u\inrange\mathcal{T}.

| -------- | -------------------------- | --- |
Must an operator \mathcal{T} \in ℒ(\mathcal{V}) have any invariant subspaces other than {0}
and \mathcal{V}? Later we will see that this question has an affirmative answer if \mathcal{V} is
finite-dimensionalanddim\mathcal{V} > 1(for\mathbf{F} = \mathbf{C})ordim\mathcal{V} > 2(for\mathbf{F} = \mathbf{R}); see
5.19and Exercise29in Section5B.
The previous example noted that null\mathcal{T} and range\mathcal{T} are invariant under \mathcal{T}.
However,thesesubspacesdonotnecessarilyprovideeasyanswerstothequestion
aboveabouttheexistenceofinvariantsubspacesotherthan{0}and\mathcal{V},because
null\mathcal{T}mayequal{0}andrange\mathcal{T}mayequal\mathcal{V}(thishappenswhen\mathcal{T}isinvertible).
Wewillreturnlatertoadeeperstudyofinvariantsubspaces. Nowweturnto
aninvestigationofthesimplestpossiblenontrivialinvariantsubspaces—invariant
subspacesofdimensionone.
Takeanyv\in\mathcal{V} withv\neq0andlet\mathcal{U} equalthesetofallscalarmultiplesofv:
={\lambdav∶ \lambda\in\mathbf{F}}=span(v).
\mathcal{U}
Then\mathcal{U}isaone-dimensionalsubspaceof\mathcal{V}(andeveryone-dimensionalsubspace
of\mathcal{V} isofthisformforanappropriatechoiceofv). If\mathcal{U} isinvariantunderan
| operator\mathcal{T} | \inℒ(\mathcal{V}),then\mathcal{T}v\in\mathcal{U},andhencethereisascalar | \lambda\in\mathbf{F} suchthat |
| --------- | ------------------------------------- | ------------ |
\mathcal{T}v= \lambdav.
Conversely, if \mathcal{T}v = \lambdav for some \lambda \in \mathbf{F}, then span(v) is a one-dimensional
| subspaceof\mathcal{V} | invariantunder\mathcal{T}. |     |
| ----------- | ---------------- | --- |
Theequation\mathcal{T}v= \lambdav,whichwehavejustseenisintimatelyconnectedwith
one-dimensionalinvariantsubspaces,isimportantenoughthatthescalars \lambdaand
vectorsvsatisfyingitaregivenspecialnames.
| 5.5 definition: | eigenvalue |     |
| --------------- | ---------- | --- |
Suppose\mathcal{T} \in ℒ(\mathcal{V}). Anumber \lambda \in \mathbf{F} iscalledaneigenvalueof\mathcal{T} ifthere
| existsv\in\mathcal{V} | suchthatv\neq0and\mathcal{T}v= | \lambdav.        |
| --------- | ----------------- | ---------- |
| In the    | definition above, | we require |
Thewordeigenvalueishalf-German,
| that v \neq 0 | because every scalar | \lambda \in \mathbf{F} |
| ---------- | -------------------- | ----- |
half-English. The Germanprefixeigen
| satisfies\mathcal{T}0= | \lambda0. |     |
| ------------ | --- | --- |
means“own”inthesenseofcharac-
| The comments | above show | that \mathcal{V} |
| ------------ | ---------- | ------ |
terizinganintrinsicproperty.
hasaone-dimensionalsubspaceinvariant
| under\mathcal{T} ifandonlyif\mathcal{T} | hasaneigenvalue. |     |
| ------------------- | ---------------- | --- |
| 5.6 example:        | eigenvalue       |     |
| Defineanoperator\mathcal{T}   | \inℒ(\mathbf{F}3)by         |     |
\mathcal{T}(x,y,z)=(7x+3z,3x+6y+9z,-6y)
for (x,y,z) \in \mathbf{F}3. Then \mathcal{T}(3,1,-1) = (18,6,-6) = 6(3,1,-1). Thus 6 is an
eigenvalueof\mathcal{T}.

| --- | --- | --- | --- | --------- | --- | ------------------ | --- |
Theequivalencesinthenextresult,alongwithmanydeepresultsinlinear
algebra,arevalidonlyinthecontextoffinite-dimensionalvectorspaces.
5.7 equivalentconditionstobeaneigenvalue
Suppose\mathcal{V} isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V}),and \lambda\in\mathbf{F}. Thenthefollowing
areequivalent.
$$(a) \lambdaisaneigenvalueof\mathcal{T}.$$
| (b)   | \mathcal{T}- \lambda\mathcal{I}      | isnotinjective.  |             | Reminder:  |         | \mathcal{I} \in ℒ(\mathcal{V}) is        | the identity |
| ----- | ---------- | ---------------- | ----------- | ---------- | ------- | ------------------ | ------------ |
|       |            |                  |             | operator.  |         | Thus\mathcal{I}v=vforallv\in\mathcal{V}. |              |
| (c)   | \mathcal{T}- \lambda\mathcal{I}      | isnotsurjective. |             |            |         |                    |              |
| (d)   | \mathcal{T}- \lambda\mathcal{I}      | isnotinvertible. |             |            |         |                    |              |
|       | Conditions | (a)              | and (b) are | equivalent | because | the equation       |              |
| Proof |            |                  |             |            |         |                    | \mathcal{T}v = \lambdav      |
is equivalent to the equation (\mathcal{T} - \lambda\mathcal{I})v = 0. Conditions (b), (c), and (d) are
equivalentby3.65.
| 5.8 | definition: | eigenvector |     |     |     |     |     |
| --- | ----------- | ----------- | --- | --- | --- | --- | --- |
\inℒ(\mathcal{V})and
| Suppose\mathcal{T}      |     |     | \lambda\in\mathbf{F}isaneigenvalueof\mathcal{T}. |              |     | Avectorv\in\mathcal{V}iscalled |     |
| ------------- | --- | --- | --------------------- | ------------ | --- | ------------------ | --- |
| aneigenvector |     | of\mathcal{T} | correspondingto       | \lambdaifv\neq0and\mathcal{T}v= |     | \lambdav.                |     |
In other words, a nonzero vector v \in \mathcal{V} is an eigenvector of an operator
\inℒ(\mathcal{V})ifandonlyif\mathcal{T}visascalarmultipleofv. Because\mathcal{T}v= \lambdavifandonly
\mathcal{T}
if(\mathcal{T}-\lambda\mathcal{I})v=0,avectorv\in\mathcal{V} withv\neq0isaneigenvectorof\mathcal{T}corresponding
| to \lambdaifandonlyifv\innull(\mathcal{T}- |          |                                 | \lambda\mathcal{I}). |     |     |     |     |
| ------------------------ | -------- | ------------------------------- | ---- | --- | --- | --- | --- |
| 5.9                      | example: | eigenvaluesandeigenvectors      |      |     |     |     |     |
|                          | Suppose\mathcal{T} | \inℒ(\mathbf{F}2)isdefinedby\mathcal{T}(w,z)=(-z,w). |      |     |     |     |     |
isacounterclockwiserotationby90\circ
| (a) | Firstconsiderthecase\mathbf{F} |     | =\mathbf{R}. | Then\mathcal{T} |     |     |     |
| --- | --------------------- | --- | --- | ----- | --- | --- | --- |
about the origin in \mathbf{R}2. An operator has an eigenvalue if and only if there
existsanonzerovectorinitsdomainthatgetssentbytheoperatortoascalar
multipleofitself. A90\circ counterclockwiserotationofanonzerovectorin\mathbf{R}2
cannotequalascalarmultipleofitself. Conclusion: if\mathbf{F} =\mathbf{R},then\mathcal{T} hasno
eigenvalues(andthushasnoeigenvectors).
$$(b) Nowconsiderthecase\mathbf{F} = \mathbf{C}. Tofindeigenvaluesof\mathcal{T},wemustfindthe$$
|     | scalars\lambdasuchthat\mathcal{T}(w,z)= |     | \lambda(w,z)hassomesolutionotherthanw=z=0. |     |     |     |     |
| --- | ----------------------- | --- | ------------------------------------ | --- | --- | --- | --- |
Theequation\mathcal{T}(w,z)= \lambda(w,z)isequivalenttothesimultaneousequations
|     | 5.10 |     | -z= | \lambdaw, | w= \lambdaz. |     |     |
| --- | ---- | --- | --- | --- | ------ | --- | --- |
Substitutingthevalueforwgivenbythesecondequationintothefirstequation
gives
-z= \lambda2z.

| -------- | -------------------------- | --- | --- | --- |
Nowzcannotequal0[otherwise5.10impliesthatw=0;wearelookingfor
solutionsto5.10suchthat(w,z)isnotthe0vector],sotheequationabove
leadstotheequation
|                               |     |     | -1= \lambda2.      |     |
| ----------------------------- | --- | --- | ------------ | --- |
| Thesolutionstothisequationare |     |     | \lambda=iand \lambda=-i. |     |
Youcanverifythatiand-iareeigenvaluesof\mathcal{T}. Indeed,theeigenvectors
correspondingtotheeigenvalueiarethevectorsoftheform(w,-wi),with
w \in \mathbf{C} and w \neq 0. Furthermore, the eigenvectors corresponding to the
eigenvalue-iarethevectorsoftheform(w,wi),withw\in\mathbf{C} andw\neq0.
Inthenextproof,weagainusetheequivalence
|     |     | \mathcal{T}v= \lambdav ⟺ | (\mathcal{T}- \lambda\mathcal{I})v=0. |     |
| --- | --- | -------- | ----------- | --- |
5.11 linearlyindependenteigenvectors
Suppose\mathcal{T} \in ℒ(\mathcal{V}). Theneverylistofeigenvectorsof\mathcal{T} correspondingto
| distincteigenvaluesof\mathcal{T} |     | islinearlyindependent. |     |     |
| ---------------------- | --- | ---------------------- | --- | --- |
Proof Supposethedesiredresultisfalse. Thenthereexistsasmallestpositive
integermsuchthatthereexistsalinearlydependentlistv ,…,v ofeigenvectors
1 m
,…,\lambda
of \mathcal{T} corresponding to distinct eigenvalues \lambda of \mathcal{T} (note that m \geq 2
|     |     |     | 1   | m   |
| --- | --- | --- | --- | --- |
becauseaneigenvectoris,bydefinition,nonzero). Thusthereexista ,…,a \in\mathbf{F},
1 m
noneofwhichare0(becauseoftheminimalityofm),suchthat
|         |                                           | a v +⋯+a | v =0. |     |
| ------- | ----------------------------------------- | -------- | ----- | --- |
|         |                                           | 1 1      | m m   |     |
| Apply\mathcal{T}- | \lambda \mathcal{I} tobothsidesoftheequationabove,getting |          |       |     |
m
+⋯+a
|     | a (\lambda - \lambda | )v  | (\lambda -    | \lambda )v =0. |
| --- | -------- | --- | ------- | -------- |
|     | 1 1      | m 1 | m-1 m-1 | m m-1    |
Becausetheeigenvalues \lambda ,…,\lambda aredistinct,noneofthecoefficientsabove
1 m
equal0. Thusv ,…,v isalinearlydependentlistofm-1eigenvectorsof\mathcal{T}
1 m-1
correspondingtodistincteigenvalues,contradictingtheminimalityofm. This
contradictioncompletestheproof.
Theresultaboveleadstoashortproofoftheresultbelow,whichputsanupper
boundonthenumberofdistincteigenvaluesthatanoperatorcanhave.
operatorcannothavemoreeigenvaluesthandimensionofvectorspace
5.12
Suppose\mathcal{V} isfinite-dimensional. Theneachoperatoron\mathcal{V} hasatmostdim\mathcal{V}
distincteigenvalues.
Proof Let \mathcal{T} \in ℒ(\mathcal{V}). Suppose \lambda ,…,\lambda are distinct eigenvalues of \mathcal{T}. Let
|     |     | 1   | m   |     |
| --- | --- | --- | --- | --- |
v ,…,v becorrespondingeigenvectors. Then5.11impliesthatthelistv ,…,v
1 m 1 m
| islinearlyindependent. |     | Thusm\leqdim\mathcal{V} | (see2.22),asdesired. |     |
| ---------------------- | --- | ---------- | -------------------- | --- |

| --- | --- | --- | --- | --------- | --- | ------------------ |
| Polynomials | Applied |     | to Operators |     |     |     |
| ----------- | ------- | --- | ------------ | --- | --- | --- |
The main reason that a richer theory exists for operators (which map a vector
spaceintoitself)thanformoregenerallinearmapsisthatoperatorscanberaised
topowers. Inthissubsectionwedefinethatnotionandtheconceptofapplyinga
polynomialtoanoperator. Thisconceptwillbethekeytoolthatweuseinthe
nextsectionwhenweprovethateveryoperatoronanonzerofinite-dimensional
complexvectorspacehasaneigenvalue.
If\mathcal{T} isanoperator,then\mathcal{T}\mathcal{T} makessense(see3.7)andisalsoanoperatoron
thesamevectorspaceas\mathcal{T}. Weusuallywrite\mathcal{T}2 insteadof\mathcal{T}\mathcal{T}. Moregenerally,
wehavethefollowingdefinitionof\mathcal{T}m.
\mathcal{T}m
**5.13 记号：** \inℒ(\mathcal{V})andmisapositiveinteger.
Suppose\mathcal{T}
=\mathcal{T}⏟⋯\mathcal{T}.
• \mathcal{T}m \inℒ(\mathcal{V})isdefinedby\mathcal{T}m
mtimes
| \mathcal{T}0 isdefinedtobetheidentityoperator\mathcal{I} |     |     |     |     | on\mathcal{V}. |     |
| ------------------------------------ | --- | --- | --- | --- | ---- | --- |
•
| isinvertiblewithinverse\mathcal{T}-1,then\mathcal{T}-m |     |     |     |     |     | \inℒ(\mathcal{V})isdefinedby |
| ---------------------------------- | --- | --- | --- | --- | --- | ---------------- |
• If\mathcal{T}
=(\mathcal{T}-1)m.
\mathcal{T}-m
| Youshouldverifythatif\mathcal{T} |     |      | isanoperator,then |     |       |       |
| ---------------------- | --- | ---- | ----------------- | --- | ----- | ----- |
|                        |     |      | =\mathcal{T}m+n             |     | (\mathcal{T}m)n |       |
|                        |     | \mathcal{T}m\mathcal{T}n |                   |     | and   | =\mathcal{T}mn, |
wheremandnarearbitraryintegersif\mathcal{T}isinvertibleandarenonnegativeintegers
if\mathcal{T} isnotinvertible.
Havingdefinedpowersofanoperator,wecannowdefinewhatitmeansto
applyapolynomialtoanoperator.
p(\mathcal{T})
**5.14 记号：** | Suppose\mathcal{T}   | \inℒ(\mathcal{V})andp\in𝒫(\mathbf{F})isapolynomialgivenby |        |     |        |        |           |
| ---------- | ---------------------------------- | ------ | --- | ------ | ------ | --------- |
|            |                                    | p(z)=a |     | +a z+a | z2+⋯+a | zm        |
|            |                                    |        | 0   | 1      | 2      | m         |
| forallz\in\mathbf{F}. | Thenp(\mathcal{T})istheoperatoron\mathcal{V}           |        |     |        |        | definedby |
|            |                                    |        | \mathcal{I}+a | \mathcal{T}+a    | \mathcal{T}2+⋯+a | \mathcal{T}m.       |
p(\mathcal{T})=a
|     |     |     | 0   | 1   | 2   | m   |
| --- | --- | --- | --- | --- | --- | --- |
Thisisanewuseofthesymbolpbecauseweareapplyingptooperators,not
justelementsof\mathbf{F}. Theideahereisthattoevaluatep(\mathcal{T}),wesimplyreplacezwith
\mathcal{T}intheexpressiondefiningp. Notethattheconstantterma inp(z)becomesthe
operatora \mathcal{I} (whichisareasonablechoicebecausea =a z0 andthusweshould
| 0        |       |                 |     |     |     | 0 0 |
| -------- | ----- | --------------- | --- | --- | --- | --- |
| replacea | witha | \mathcal{T}0,whichequalsa |     | \mathcal{I}). |     |     |

| -------- | -------------------------- | --- | --- | --- |
apolynomialappliedtothedifferentiationoperator
**5.15 例：** Suppose\mathcal{D}\inℒ(𝒫(\mathbf{R}))isthedifferentiationoperatordefinedby\mathcal{D}q=q′and
| pisthepolynomialdefinedbyp(x)=7-3x+5x2. |     | Thenp(\mathcal{D})=7\mathcal{I}-3\mathcal{D}+5\mathcal{D}2. |     |     |
| --------------------------------------- | --- | ------------------- | --- | --- |
Thus
$$(p(\mathcal{D}))q=7q-3q′+5q″$$
foreveryq\in𝒫(\mathbf{R}).
| Ifwefixanoperator\mathcal{T} | \inℒ(\mathcal{V}),thenthefunctionfrom𝒫(\mathbf{F})toℒ(\mathcal{V})given |     |     |     |
| ------------------ | ---------------------------------------- | --- | --- | --- |
byp↦p(\mathcal{T})islinear,asyoushouldverify.
| 5.16 definition: | productofpolynomials |     |     |     |
| ---------------- | -------------------- | --- | --- | --- |
Ifp,q\in𝒫(\mathbf{F}),thenpq\in𝒫(\mathbf{F})isthepolynomialdefinedby
$$(pq)(z)=p(z)q(z)$$
forallz\in\mathbf{F}.
The order does not matter in taking products of polynomials of a single
operator,asshownby(b)inthenextresult.
5.17 multiplicativeproperties
| Supposep,q\in𝒫(\mathbf{F})and\mathcal{T} | \inℒ(\mathcal{V}). |                 |                |     |
| ------------------- | ------ | --------------- | -------------- | --- |
|                     |        | Informal proof: | When a product | of  |
Then
polynomialsisexpandedusingthedis-
| (a) (pq)(\mathcal{T})=p(\mathcal{T})q(\mathcal{T});  |     | tributiveproperty,      | itdoesnotmatter |     |
| ---------------------- | --- | ----------------------- | --------------- | --- |
| (b) p(\mathcal{T})q(\mathcal{T})=q(\mathcal{T})p(\mathcal{T}). |     | whetherthesymboliszor\mathcal{T}. |                 |     |
Proof
|                  | m          | n             |      |     |
| ---------------- | ---------- | ------------- | ---- | --- |
|                  | azj        | zk            |      |     |
| (a) Supposep(z)= | \sum andq(z)= | \sumb forallz\in\mathbf{F}. | Then |     |
|                  | j          | k             |      |     |
|                  | j=0        | k=0           |      |     |
m n
zj+k.
|     | (pq)(z)= | \sum \sumab j k |     |     |
| --- | -------- | --------- | --- | --- |
$$j=0k=0$$
Thus
m n
\mathcal{T}j+k
|     | (pq)(\mathcal{T})= | \sum \sumab |     |     |
| --- | -------- | ----- | --- | --- |
j k
$$j=0k=0$$
m n
|     | =(\sum | a\mathcal{T}j)(\sumb | \mathcal{T}k) |     |
| --- | --- | ------- | --- | --- |
|     |     | j       | k   |     |
$$j=0 k=0$$
=p(\mathcal{T})q(\mathcal{T}).
$$(b) Using(a)twice,wehavep(\mathcal{T})q(\mathcal{T})=(pq)(\mathcal{T})=(qp)(\mathcal{T})=q(\mathcal{T})p(\mathcal{T}).$$

| --- | --- | --- | --- | --------- | --- | ------------------ | --- |
Weobservedearlierthatif\mathcal{T} \inℒ(\mathcal{V}),thenthesubspacesnull\mathcal{T} andrange\mathcal{T}
areinvariantunder\mathcal{T} (see5.4). Nowweshowthatthenullspaceandtherangeof
| everypolynomialof\mathcal{T}  |     | arealsoinvariantunder\mathcal{T}. |                       |     |     |     |     |
| ------------------- | --- | ----------------------- | --------------------- | --- | --- | --- | --- |
| nullspaceandrangeof |     |                         | p(\mathcal{T})areinvariantunder |     |     |     |     |
| 5.18                |     |                         |                       |     |     | \mathcal{T}   |     |
Suppose \mathcal{T} \in ℒ(\mathcal{V}) and p \in 𝒫(\mathbf{F}). Then nullp(\mathcal{T}) and rangep(\mathcal{T}) are
invariantunder\mathcal{T}.
| Proof Supposeu\innullp(\mathcal{T}). |     |     | Thenp(\mathcal{T})u=0. |     |     | Thus |     |
| ------------------------ | --- | --- | ------------ | --- | --- | ---- | --- |
$$(p(\mathcal{T}))(\mathcal{T}u)=(p(\mathcal{T})\mathcal{T})(u)=(\mathcal{T}p(\mathcal{T}))(u)=\mathcal{T}(p(\mathcal{T})u)=\mathcal{T}(0)=0.$$
| Hence\mathcal{T}u\innullp(\mathcal{T}).   |     | Thusnullp(\mathcal{T})isinvariantunder\mathcal{T},asdesired. |                    |     |     |                  |      |
| ------------------- | --- | ---------------------------------------- | ------------------ | --- | --- | ---------------- | ---- |
| Supposeu\inrangep(\mathcal{T}). |     |                                          | Thenthereexistsv\in\mathcal{V} |     |     | suchthatu=p(\mathcal{T})v. | Thus |
\mathcal{T}u=\mathcal{T}(p(\mathcal{T})v)=p(\mathcal{T})(\mathcal{T}v).
| Hence\mathcal{T}u\inrangep(\mathcal{T}).    |     |           | Thusrangep(\mathcal{T})isinvariantunder\mathcal{T},asdesired. |      |                                 |     |     |
| --------------------- | --- | --------- | ----------------------------------------- | ---- | ------------------------------- | --- | --- |
| Exercises             | 5A  |           |                                           |      |                                 |     |     |
| 1 Suppose\mathcal{T}            |     | \inℒ(\mathcal{V})and\mathcal{U} | isasubspaceof\mathcal{V}.                           |      |                                 |     |     |
| (a) Provethatif\mathcal{U}      |     |           | \subseteqnull\mathcal{T},then\mathcal{U}                              |      | isinvariantunder\mathcal{T}.              |     |     |
| (b) Provethatifrange\mathcal{T} |     |           | \subseteq\mathcal{U},then\mathcal{U}                                  |      | isinvariantunder\mathcal{T}.              |     |     |
|                       |     | \inℒ(\mathcal{V})and\mathcal{V} |                                           | ,…,\mathcal{V} |                                 |     |     |
| 2 Supposethat\mathcal{T}        |     |           |                                           |      | aresubspacesof\mathcal{V}invariantunder\mathcal{T}. |     |     |
|                       |     |           |                                           | 1    | m                               |     |     |
| Provethat\mathcal{V}            |     | +⋯+\mathcal{V}      | isinvariantunder\mathcal{T}.                        |      |                                 |     |     |
|                       |     | 1         | m                                         |      |                                 |     |     |
3 Suppose \mathcal{T} \in ℒ(\mathcal{V}). Prove that the intersection of every collection of
| subspacesof\mathcal{V} |     | invariantunder\mathcal{T} |     | isinvariantunder\mathcal{T}. |     |     |     |
| ------------ | --- | --------------- | --- | ------------------ | --- | --- | --- |
4 Proveorgiveacounterexample: If\mathcal{V} isfinite-dimensionaland\mathcal{U} isasubspace of that is invariant under every operator on \mathcal{V}, then or
|     | \mathcal{V}   |     |     |     |     | \mathcal{U}   | = {0} |
| --- | --- | --- | --- | --- | --- | --- | ----- |
\mathcal{U} =\mathcal{V}.
5 Suppose\mathcal{T} \inℒ(\mathbf{R}2)isdefinedby\mathcal{T}(x,y)=(-3y,x). Findtheeigenvalues
of\mathcal{T}.
6 Define\mathcal{T} \inℒ(\mathbf{F}2)by\mathcal{T}(w,z)=(z,w). Findalleigenvaluesandeigenvectorsof\mathcal{T}.
|           | \inℒ(\mathbf{F}3)by\mathcal{T}(z |     | ,z  | ,z      | ,0,5z |                            |     |
| --------- | ----------- | --- | --- | ------- | ----- | -------------------------- | --- |
| 7 Define\mathcal{T} |             |     | 1 2 | 3 )=(2z | 2     | 3 ). Findalleigenvaluesand |     |
eigenvectorsof\mathcal{T}.
8 Suppose\mathcal{P} \inℒ(\mathcal{V})issuchthat\mathcal{P}2 =\mathcal{P}. Provethatif \lambdaisaneigenvalueof\mathcal{P},
| then | \lambda=0or | \lambda=1. |     |     |     |     |     |
| ---- | ----- | ---- | --- | --- | --- | --- | --- |

| --- | -------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Define\mathcal{T}∶ |     | 𝒫(\mathbf{R})\rightarrow𝒫(\mathbf{R})by\mathcal{T}p=p′. |     |     |                                   |     |     |     |     |
| -------- | --- | ----------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
| 9        |     |                   |     |     | Findalleigenvaluesandeigenvectors |     |     |     |     |
of\mathcal{T}.
10 Define\mathcal{T} \inℒ(𝒫 (\mathbf{R}))by(\mathcal{T}p)(x)=xp′(x)forallx \in\mathbf{R}. Findalleigenvaluesandeigenvectorsof\mathcal{T}.
\inℒ(\mathcal{V}),and\alpha\in\mathbf{F}.
| 11 Suppose\mathcal{V} |                                                  | isfinite-dimensional,\mathcal{T} |     |      |                         |     | Provethatthereex- |     |          |
| ----------- | ------------------------------------------------ | ---------------------- | --- | ---- | ----------------------- | --- | ----------------- | --- | -------- |
| ists\delta       | >0suchthat\mathcal{T}-\lambda\mathcal{I}isinvertibleforall\lambda\in\mathbf{F}suchthat0<|\alpha- |                        |     |      |                         |     |                   |     | \lambda|<\delta.    |
| 12 Suppose\mathcal{V} |                                                  | =\mathcal{U}\oplus\mathcal{W},where\mathcal{U}            |     | and\mathcal{W} | arenonzerosubspacesof\mathcal{V}. |     |                   |     | Define   |
|             | ℒ(\mathcal{V})                                             | by \mathcal{P}(u+w)              |     | for  | each                    | and | each              | \mathcal{W}.  | Find all |
| \mathcal{P}           | \in                                                |                        | =   | u    | u \in                     | \mathcal{U}   | w                 | \in   |          |
eigenvaluesandeigenvectorsof\mathcal{P}.
| 13 Suppose\mathcal{T} |            | \inℒ(\mathcal{V}).                          | Suppose\mathcal{S}\inℒ(\mathcal{V})isinvertible. |     |     |     |     |     |     |
| ----------- | ---------- | ------------------------------- | -------------------------- | --- | --- | --- | --- | --- | --- |
| (a)         | Provethat\mathcal{T} | and\mathcal{S}-1\mathcal{T}\mathcal{S}havethesameeigenvalues. |                            |     |     |     |     |     |     |
$$(b) Whatistherelationshipbetweentheeigenvectorsof\mathcal{T} andtheeigenvectorsof\mathcal{S}-1\mathcal{T}\mathcal{S}?$$
| 14 Giveanexampleofanoperatoron\mathbf{R}4 |     |     |     |     | thathasno(real)eigenvalues. |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- |
15 Suppose \mathcal{V} is finite-dimensional, \mathcal{T} \in ℒ(\mathcal{V}), and \lambda \in \mathbf{F}. Show that \lambda is
an eigenvalue of if and only if is an eigenvalue of the dual operator
|     |     | \mathcal{T}   |     |     | \lambda   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
\mathcal{T}′ \inℒ(\mathcal{V}′).
16 Suppose v ,…,v is a basis of \mathcal{V} and \mathcal{T} \in ℒ(\mathcal{V}). Prove that if \lambda is an
|     |     | 1 n |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eigenvalueof\mathcal{T},then
|     |     | |\lambda|\leqnmax{∣ℳ(\mathcal{T}) |     |     | ∣∶1\leqj,k |     | \leqn}, |     |     |
| --- | --- | -------------- | --- | --- | ------- | --- | ---- | --- | --- |
j,k
| whereℳ(\mathcal{T}) |     | denotestheentryinrowj,columnkofthematrixof\mathcal{T} |     |     |     |     |     |     | with |
| --------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
j,k
| respecttothebasisv |     |     | ,…,v | .   |     |     |     |     |     |
| ------------------ | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|                    |     |     | 1    | n   |     |     |     |     |     |
See Exercise19in Section6Aforadifferentboundon|\lambda|.
| 17 Suppose\mathbf{F} |     | =\mathbf{R},\mathcal{T} \inℒ(\mathcal{V}),and                        |     | \lambda\in\mathbf{R}. | Provethat |     | \lambdaisaneigenvalueof\mathcal{T} |     |     |
| ----------- | --- | ------------------------------------- | --- | ---- | --------- | --- | ------------------ | --- | --- |
| ifandonlyif |     | \lambdaisaneigenvalueofthecomplexification\mathcal{T} |     |      |           |     |                    | .   |     |
\mathbf{C}
|     | See Exercise33in Section3Bforthedefinitionof |     |     |     |     |     | \mathcal{T} . |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
\mathbf{C}
ℒ(\mathcal{V}),and
| 18 Suppose\mathbf{F}                         |     | = \mathbf{R},\mathcal{T} \in |             |             | \lambda \in \mathbf{C}. Provethat   |        | \lambdaisaneigenvalueof |     |     |
| ----------------------------------- | --- | ------- | ----------- | ----------- | ------------------ | ------ | ----------------- | --- | --- |
| thecomplexification\mathcal{T}                |     |         | ifandonlyif |             | \lambdaisaneigenvalueof\mathcal{T} |        |                   | .   |     |
|                                     |     |         | \mathbf{C}           |             |                    |        |                   | \mathbf{C}   |     |
| 19 Showthattheforwardshiftoperator\mathcal{T} |     |         |             |             | \inℒ(\mathbf{F}\infty)definedby    |        |                   |     |     |
|                                     |     |         | \mathcal{T}(z         | ,z ,…)=(0,z |                    | ,z ,…) |                   |     |     |
|                                     |     |         | 1           | 2           |                    | 1 2    |                   |     |     |
hasnoeigenvalues.
20 Definethebackwardshiftoperator\mathcal{S}\inℒ(\mathbf{F}\infty)by
|     |                         |     | \mathcal{S}(z ,z | ,z ,…)=(z |                    | ,z ,…). |     |     |     |
| --- | ----------------------- | --- | ------ | --------- | ------------------ | ------- | --- | --- | --- |
|     |                         |     | 1      | 2 3       |                    | 2 3     |     |     |     |
| (a) | Showthateveryelementof\mathbf{F} |     |        |           | isaneigenvalueof\mathcal{S}. |         |     |     |     |
| (b) | Findalleigenvectorsof\mathcal{S}. |     |        |           |                    |         |     |     |     |

| ----------- | ------------------ | --------- | ------------------ | --- | --- | ------ |
| 21 Suppose\mathcal{T} | \inℒ(\mathcal{V})isinvertible. |           |                    |     |     |        |
$$(a) Suppose \lambda \in \mathbf{F} with \lambda \neq 0. Provethat \lambdaisaneigenvalueof\mathcal{T} ifand$$
1 isaneigenvalueof\mathcal{T}-1.
onlyif
\lambda
| (b) Provethat\mathcal{T} | and\mathcal{T}-1 | havethesameeigenvectors. |     |     |     |     |
| -------------- | ------ | ------------------------ | --- | --- | --- | --- |
\inℒ(\mathcal{V})andthereexistnonzerovectorsuandwin\mathcal{V}
| 22 Suppose\mathcal{T} |     |       |     |        |     | suchthat |
| ----------- | --- | ----- | --- | ------ | --- | -------- |
|             |     | \mathcal{T}u=3w | and | \mathcal{T}w=3u. |     |          |
Provethat3or-3isaneigenvalueof\mathcal{T}.
23 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{S},\mathcal{T} \in ℒ(\mathcal{V}). Provethat\mathcal{S}\mathcal{T} and\mathcal{T}\mathcal{S}
havethesameeigenvalues.
ℒ(\mathbf{F}n)
24 Suppose \mathcal{A} is an n-by-n matrix with entries in \mathbf{F}. Define \mathcal{T} \in by
| \mathcal{T}x =\mathcal{A}x,whereelementsof\mathbf{F}n                          |     |     | arethoughtofasn-by-1columnvectors. |     |     |            |
| ------------------------------------------------- | --- | --- | ---------------------------------- | --- | --- | ---------- |
| (a) Supposethesumoftheentriesineachrowof\mathcal{A}equals1. |     |     |                                    |     |     | Provethat1 |
isaneigenvalueof\mathcal{T}.
$$(b) Supposethesumoftheentriesineachcolumnof\mathcal{A}equals1. Provethat$$
1isaneigenvalueof\mathcal{T}.
| Suppose\mathcal{T} | \in ℒ(\mathcal{V})andu,wareeigenvectorsof\mathcal{T} |     |     |     | suchthatu+wisalso |     |
| -------- | ------------------------------ | --- | --- | --- | ----------------- | --- |
aneigenvectorof\mathcal{T}. Provethatuandwareeigenvectorsof\mathcal{T} corresponding
tothesameeigenvalue.
\inℒ(\mathcal{V})issuchthateverynonzerovectorin\mathcal{V}
| 26 Suppose\mathcal{T}     |     |                                         |     |     | isaneigenvector |     |
| --------------- | --- | --------------------------------------- | --- | --- | --------------- | --- |
| of\mathcal{T}. Provethat\mathcal{T} |     | isascalarmultipleoftheidentityoperator. |     |     |                 |     |
27 Supposethat\mathcal{V} isfinite-dimensionalandk \in{1,…,dim\mathcal{V}-1}. Suppose
\mathcal{T} \in ℒ(\mathcal{V}) is such that every subspace of \mathcal{V} of dimension k is invariant
| under\mathcal{T}. | Provethat\mathcal{T} | isascalarmultipleoftheidentityoperator. |     |     |     |     |
| ------- | ---------- | --------------------------------------- | --- | --- | --- | --- |
28 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \in ℒ(\mathcal{V}). Provethat\mathcal{T} hasatmost
| 1+dimrange\mathcal{T} | distincteigenvalues. |     |     |     |     |     |
| ----------- | -------------------- | --- | --- | --- | --- | --- |
29 Suppose\mathcal{T} \in ℒ(\mathbf{R}3)and-4, 5, and\sqrt7 areeigenvaluesof\mathcal{T}. Provethat
| thereexistsx | \in\mathbf{R}3 | suchthat\mathcal{T}x-9x | =(-4,5,\sqrt7). |     |     |     |
| ------------ | --- | ------------- | ----------- | --- | --- | --- |
30 Suppose\mathcal{T} \in ℒ(\mathcal{V})and(\mathcal{T} -2\mathcal{I})(\mathcal{T} -3\mathcal{I})(\mathcal{T} -4\mathcal{I}) = 0. Suppose \lambdaisan
| eigenvalueof\mathcal{T}.      | Provethat                    | \lambda=2or            | \lambda=3or | \lambda=4.         |                 |      |
| ------------------- | ---------------------------- | ---------------- | ----- | ------------ | --------------- | ---- |
| 31 Giveanexampleof\mathcal{T} |                              | \inℒ(\mathbf{R}2)suchthat\mathcal{T}4 |       | =-\mathcal{I}.         |                 |      |
| 32 Suppose\mathcal{T}         | \inℒ(\mathcal{V})hasnoeigenvaluesand\mathcal{T}4   |                  |       |              | =\mathcal{I}. Provethat\mathcal{T}2 | =-\mathcal{I}. |
| 33 Suppose\mathcal{T}         | \inℒ(\mathcal{V})andmisapositiveinteger. |                  |       |              |                 |      |
| (a) Provethat\mathcal{T}      | isinjectiveifandonlyif\mathcal{T}m     |                  |       | isinjective. |                 |      |
| (b) Provethat\mathcal{T}      | issurjectiveifandonlyif\mathcal{T}m    |                  |       |              | issurjective.   |      |

| --- | ----------------------------------- | --- | --- | --- | --- |
34 Suppose \mathcal{V} is finite-dimensional and v ,…,v \in \mathcal{V}. Prove that the list
1 m
v ,…,v islinearlyindependentifandonlyifthereexists\mathcal{T} \inℒ(\mathcal{V})such
|     | 1 m |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
thatv ,…,v areeigenvectorsof\mathcal{T} correspondingtodistincteigenvalues.
1 m
35 Suppose that \lambda ,…,\lambda is a list of distinct real numbers. Prove that the
1 n
liste\lambda x,…,e\lambda x islinearlyindependentinthevectorspaceofreal-valued
|     | 1 n |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
functionson\mathbf{R}.
|     | Hint:Let\mathcal{V} =span(e\lambda1x,…,e\lambdanx),anddefineanoperator\mathcal{D}\inℒ(\mathcal{V})by |     |     |     |     |
| --- | -------------------------------------------------------- | --- | --- | --- | --- |
|     | \mathcal{D}f = f′. Findeigenvaluesandeigenvectorsof                |     |     | \mathcal{D}.  |     |
36 Supposethat \lambda ,…,\lambda isalistofdistinctpositivenumbers. Provethatthe
1 n
list cos(\lambda x),…,cos(\lambda is linearly independent in the vector space of
|     | 1   | n x) |     |     |     |
| --- | --- | ---- | --- | --- | --- |
real-valuedfunctionson\mathbf{R}.
37 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Define𝒜\inℒ(ℒ(\mathcal{V}))by
𝒜(\mathcal{S})=\mathcal{T}\mathcal{S}
foreach\mathcal{S}\inℒ(\mathcal{V}).
|     |     | Provethatthesetofeigenvaluesof\mathcal{T} |     | equalsthesetof |     |
| --- | --- | ------------------------------- | --- | -------------- | --- |
eigenvaluesof𝒜.
38 Suppose \mathcal{V} is finite-dimensional, \mathcal{T} \in ℒ(\mathcal{V}), and \mathcal{U} is a subspace of \mathcal{V}
|     |                  | Thequotientoperator | \inℒ(\mathcal{V}/\mathcal{U})isdefinedby |     |     |
| --- | ---------------- | ------------------- | ------------------ | --- | --- |
|     | invariantunder\mathcal{T}. |                     | \mathcal{T}/\mathcal{U}                |     |     |
$$(\mathcal{T}/\mathcal{U})(v+\mathcal{U})=\mathcal{T}v+\mathcal{U}$$
foreachv\in\mathcal{V}.
$$(a) Showthatthedefinitionof\mathcal{T}/\mathcal{U} makessense(whichrequiresusingthe$$
|     | conditionthat\mathcal{U} | isinvariantunder\mathcal{T})andshowthat\mathcal{T}/\mathcal{U} |     |     | isanoperator |
| --- | -------------- | -------------------------------- | --- | --- | ------------ |
on\mathcal{V}/\mathcal{U}.
|     | (b) Showthateacheigenvalueof\mathcal{T}/\mathcal{U} |     | isaneigenvalueof\mathcal{T}. |     |     |
| --- | ------------------------------- | --- | ------------------ | --- | --- |
39 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Provethat\mathcal{T} hasaneigenvalueifandonlyifthereexistsasubspaceof\mathcal{V} ofdimensiondim\mathcal{V}-1that
isinvariantunder\mathcal{T}.
40 Suppose\mathcal{S},\mathcal{T} \inℒ(\mathcal{V})and\mathcal{S}isinvertible. Supposep\in𝒫(\mathbf{F})isapolynomial.
Provethat
p(\mathcal{S}\mathcal{T}\mathcal{S}-1)=\mathcal{S}p(\mathcal{T})\mathcal{S}-1.
41 Suppose\mathcal{T} \inℒ(\mathcal{V})and\mathcal{U} isasubspaceof\mathcal{V} invariantunder\mathcal{T}. Provethat
\mathcal{U} isinvariantunderp(\mathcal{T})foreverypolynomialp\in𝒫(\mathbf{F}).
| 42  | Define\mathcal{T} \inℒ(\mathbf{F}n)by\mathcal{T}(x                       | ,x ,x ,…,x              | )=(x | ,2x ,3x ,…,nx | ).  |
| --- | ----------------------------------------- | ----------------------- | ---- | ------------- | --- |
|     |                                           | 1 2 3                   | n    | 1 2 3         | n   |
|     | (a) Findalleigenvaluesandeigenvectorsof\mathcal{T}. |                         |      |               |     |
|     | (b) Findallsubspacesof\mathbf{F}n                  | thatareinvariantunder\mathcal{T}. |      |               |     |
\inℒ(\mathcal{V}).
| 43  | Supposethat\mathcal{V}isfinite-dimensional,dim\mathcal{V} |     | >1,and\mathcal{T} |     | Provethat |
| --- | ------------------------------------- | --- | ------- | --- | --------- |
{p(\mathcal{T})∶p\in𝒫(\mathbf{F})}\neqℒ(\mathcal{V}).

| --- | --- | --------- | --- | -------------------- |
| 5B The    | Minimal Polynomial |            |     |               |
| --------- | ------------------ | ---------- | --- | ------------- |
| Existence | of Eigenvalues     | on Complex |     | Vector Spaces |
Nowwecometooneofthecentralresultsaboutoperatorsonfinite-dimensional
complexvectorspaces.
5.19 existenceofeigenvalues
Everyoperatoronafinite-dimensionalnonzerocomplexvectorspacehasan
eigenvalue.
Proof Suppose\mathcal{V} isafinite-dimensionalcomplexvectorspaceofdimension
| n>0and\mathcal{T} | \inℒ(\mathcal{V}). Choosev\in\mathcal{V} |     | withv\neq0. | Then |
| ------- | ---------------- | --- | -------- | ---- |
v,\mathcal{T}v,\mathcal{T}2v,…,\mathcal{T}nv
isnotlinearlyindependent,because\mathcal{V} hasdimensionnandthislisthaslength
n+1. Hencesomelinearcombination(withnotallthecoefficientsequalto0)
ofthevectorsaboveequals0. Thusthereexistsanonconstantpolynomialpof
smallestdegreesuchthat
p(\mathcal{T})v=0.
Bythefirstversionofthefundamentaltheoremofalgebra(see4.12),there
Hencethereexistsapolynomialq\in𝒫(\mathbf{C})such
exists \lambda\in\mathbf{C}suchthatp(\lambda)=0.
that
|             |             | p(z)=(z-                   | \lambda)q(z)      |     |
| ----------- | ----------- | -------------------------- | ----------- | --- |
| foreveryz\in\mathbf{C} | (see4.6).   | Thisimplies(using5.17)that |             |     |
|             | 0=p(\mathcal{T})v=(\mathcal{T}- |                            | \lambda\mathcal{I})(q(\mathcal{T})v). |     |
Becauseqhassmallerdegreethanp,weknowthatq(\mathcal{T})v\neq0. Thustheequation
| aboveimpliesthat | \lambdaisaneigenvalueof\mathcal{T} |     | witheigenvectorq(\mathcal{T})v. |     |
| ---------------- | ------------------ | --- | --------------------- | --- |
Theproofabovemakescrucialuseofthefundamentaltheoremofalgebra.
Thecommentfollowing Exercise16helpsexplainwhythefundamentaltheorem
ofalgebraissotightlyconnectedtotheresultabove.
Thehypothesisintheresultabovethat\mathbf{F} = \mathbf{C} cannotbereplacedwiththe
hypothesisthat\mathbf{F} =\mathbf{R},asshownby Example5.9. Thenextexampleshowsthat
thefinite-dimensionalhypothesisintheresultabovealsocannotbedeleted.
**5.20 例：** anoperatoronacomplexvectorspacewithnoeigenvalues
Define\mathcal{T} \in ℒ(𝒫(\mathbf{C}))by(\mathcal{T}p)(z) = zp(z). Ifp \in 𝒫(\mathbf{C})isanonzeropolynomial,thenthedegreeof\mathcal{T}pisonemorethanthedegreeofp,andthus\mathcal{T}pcannot
| equalascalarmultipleofp. |     | Hence\mathcal{T} | hasnoeigenvalues. |     |
| ------------------------ | --- | ------ | ----------------- | --- |
Because𝒫(\mathbf{C})isinfinite-dimensional,thisexampledoesnotcontradictthe
resultabove.

| --- | -------- | -------------------------- | --- | --- | --- | --- |
| Eigenvalues |     | and the | Minimal | Polynomial |     |     |
| ----------- | --- | ------- | ------- | ---------- | --- | --- |
Inthissubsectionweintroduceanimportantpolynomialassociatedwitheach
| operator. | Webeginwiththefollowingdefinition. |                 |     |     |     |     |
| --------- | ---------------------------------- | --------------- | --- | --- | --- | --- |
| 5.21      | definition:                        | monicpolynomial |     |     |     |     |
Amonicpolynomialisapolynomialwhosehighest-degreecoefficientequals1.
Forexample,thepolynomial2+9z2+z7 isamonicpolynomialofdegree7.
5.22 existence,uniqueness,anddegreeofminimalpolynomial
Suppose\mathcal{V}isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Thenthereisauniquemonic
polynomialp \in 𝒫(\mathbf{F})ofsmallestdegreesuchthatp(\mathcal{T}) = 0. Furthermore,
degp\leqdim\mathcal{V}.
|     | Ifdim\mathcal{V} | = 0,then\mathcal{I} | isthezerooperatoron\mathcal{V} |     |     | andthuswetakeptobe |
| --- | ------ | --------- | -------------------- | --- | --- | ------------------ |
Proof
theconstantpolynomial1.
Now use induction on dim\mathcal{V}. Thus assume that dim\mathcal{V} > 0 and that the
desiredresultistrueforalloperatorsonallvectorspacesofsmallerdimension.
Letu \in \mathcal{V} besuchthatu \neq 0. Thelistu,\mathcal{T}u,…,\mathcal{T}dim\mathcal{V}uhaslength1+dim\mathcal{V}
andthusislinearlydependent. Bythelineardependencelemma(2.19),thereis
asmallestpositiveintegerm\leqdim\mathcal{V} suchthat\mathcal{T}muisalinearcombinationof
| u,\mathcal{T}u,…,\mathcal{T}m-1u.             |     | Thusthereexistscalarsc |        |       | ,c ,c ,…,c   | \in\mathbf{F} suchthat |
| ------------------------- | --- | ---------------------- | ------ | ----- | ------------ | ----------- |
|                           |     |                        |        |       | 0 1 2        | m-1         |
| 5.23                      |     | c u+c                  | \mathcal{T}u+⋯+c |       | \mathcal{T}m-1u+\mathcal{T}mu=0. |             |
|                           |     | 0                      | 1      | m-1   |              |             |
| Defineamonicpolynomialq\in𝒫 |     |                        |        | (\mathbf{F})by |              |             |
m
zm-1+zm.
|     |     | q(z)=c | +c  | z+⋯+c |     |     |
| --- | --- | ------ | --- | ----- | --- | --- |
|     |     |        | 0   | 1     | m-1 |     |
Then5.23impliesthatq(\mathcal{T})u=0.
Ifkisanonnegativeinteger,then
q(\mathcal{T})(\mathcal{T}ku)=\mathcal{T}k(q(\mathcal{T})u)=\mathcal{T}k(0)=0.
Thelineardependencelemma(2.19)showsthatu,\mathcal{T}u,…,\mathcal{T}m-1uislinearlyindependent. Thustheequationaboveimpliesthatdimnullq(\mathcal{T})\geqm. Hence
dimrangeq(\mathcal{T})=dim\mathcal{V}-dimnullq(\mathcal{T})\leqdim\mathcal{V}-m.
Becauserangeq(\mathcal{T})isinvariantunder\mathcal{T} (by5.18),wecanapplyourinduction
hypothesistotheoperator\mathcal{T}| onthevectorspacerangeq(\mathcal{T}). Thusthere
rangeq(\mathcal{T})
isamonicpolynomials\in𝒫(\mathbf{F})with
|     |     | degs\leqdim\mathcal{V}-m |     | and | s(\mathcal{T}| | )=0. |
| --- | --- | ----------- | --- | --- | ---- | ---- |
rangeq(\mathcal{T})
| Henceforallv\in\mathcal{V} |     | wehave |     |     |     |     |
| -------------- | --- | ------ | --- | --- | --- | --- |
$$((sq)(\mathcal{T}))(v)=s(\mathcal{T})(q(\mathcal{T})v)=0$$
| becauseq(\mathcal{T})v\inrangeq(\mathcal{T})ands(\mathcal{T})|    |     |     |     |           | =s(\mathcal{T}|         | )=0. Thussqisa |
| --------------------------------- | --- | --- | --- | --------- | ------------- | -------------- |
|                                   |     |     |     | rangeq(\mathcal{T}) |               | rangeq(\mathcal{T})      |
| monicpolynomialsuchthatdegsq\leqdim\mathcal{V} |     |     |     |           | and(sq)(\mathcal{T})=0. |                |

Section5B The Minimal Polynomial
The paragraph above shows that there is a monic polynomial of degree at
mostdim\mathcal{V} thatwhenappliedto\mathcal{T} givesthe0operator. Thusthereisamonic
polynomialofsmallestdegreewiththisproperty,completingtheexistencepart
ofthisresult.
Letp\in𝒫(\mathbf{F})beamonicpolynomialofsmallestdegreesuchthatp(\mathcal{T})=0.
Toprovetheuniquenesspartoftheresult, supposer \in 𝒫(\mathbf{F})isamonicpolynomial of the same degree as p and r(\mathcal{T}) = 0. Then (p-r)(\mathcal{T}) = 0 and also
| deg(p-r)<degp. | Ifp-rwerenotequalto0,thenwecoulddividep-rby |     |     |     |
| -------------- | ------------------------------------------- | --- | --- | --- |
thecoefficientofthehighest-orderterminp-rtogetamonicpolynomial(of
smallerdegreethanp)thatwhenappliedto\mathcal{T}givesthe0operator. Thusp-r =0,
asdesired.
Thepreviousresultjustifiesthefollowingdefinition.
minimalpolynomial
**5.24 定义：** Suppose\mathcal{V}isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Thentheminimalpolynomial
of\mathcal{T} istheuniquemonicpolynomialp\in𝒫(\mathbf{F})ofsmallestdegreesuchthat
p(\mathcal{T})=0.
| Tocomputetheminimalpolynomialofanoperator\mathcal{T} |     |     | \in ℒ(\mathcal{V}),weneedto |     |
| ------------------------------------------ | --- | --- | --------------- | --- |
findthesmallestpositiveintegermsuchthattheequation
c \mathcal{I}+c \mathcal{T}+⋯+c \mathcal{T}m-1 =-\mathcal{T}m
0 1 m-1
hasasolutionc ,c ,…,c \in \mathbf{F}. Ifwepickabasisof\mathcal{V} andreplace\mathcal{T} inthe
0 1 m-1
equationabovewiththematrixof\mathcal{T},thentheequationabovecanbethoughtof
asasystemof(dim\mathcal{V})2 linearequationsinthemunknownsc ,c ,…,c \in\mathbf{F}.
|     |     |     | 0 1 | m-1 |
| --- | --- | --- | --- | --- |
Gaussianeliminationoranotherfastmethodofsolvingsystemsoflinearequations
cantelluswhetherasolutionexists,testingsuccessivevaluesm=1,2,…until
a solution exists. By 5.22, a solution exists for some smallest positive integer
| m\leqdim\mathcal{V}.                     | Theminimalpolynomialof\mathcal{T}       | isthenc           | +c z+⋯+c | zm-1+zm. |
| --------------------------- | ----------------------------- | ----------------- | -------- | -------- |
|                             |                               | 0                 | 1        | m-1      |
| Evenfaster(usually),pickv\in\mathcal{V} | withv\neq0andconsidertheequation |                   |          |          |
|                             | v+c \mathcal{T}v+⋯+c                    | \mathcal{T}dim\mathcal{V}-1v=-\mathcal{T}dim\mathcal{V}v. |          |          |
| 5.25                        | c                             |                   |          |          |
|                             | 0 1 dim\mathcal{V}-1                    |                   |          |          |
Use a basis of \mathcal{V} to convert the equation above to a system of dim\mathcal{V} linear
equationsindim\mathcal{V} unknownsc ,c ,…,c . Ifthissystemofequationshasa
0 1 dim\mathcal{V}-1
,c ,…,c
| uniquesolutionc | (ashappensmostofthetime),thenthescalars |     |     |     |
| --------------- | --------------------------------------- | --- | --- | --- |
0 1 dim\mathcal{V}-1
c ,c ,…,c ,1arethecoefficientsoftheminimalpolynomialof\mathcal{T} (because
| 0 1 | dim\mathcal{V}-1 |     |     |     |
| --- | ------ | --- | --- | --- |
5.22statesthatthedegreeoftheminimalpolynomialisatmostdim\mathcal{V}).
| Consider | operators on \mathbf{R}4 (thought |     |     |     |
| -------- | ------------------------ | --- | --- | --- |
Theseestimatesarebasedontesting
| ofas4-by-4matriceswithrespecttothe |     | millionsofrandommatrices. |     |     |
| ---------------------------------- | --- | ------------------------- | --- | --- |
standardbasis),andtakev = (1,0,0,0)
intheparagraphabove. Thefastermethoddescribedaboveworksonover99.8%
ofthe4-by-4matriceswithintegerentriesintheinterval[-10,10]andonover
99.999%ofthe4-by-4matriceswithintegerentriesin[-100,100].

146 Chapter 5 Eigenvaluesand Eigenvectors
Thenextexampleillustratesthefasterprocedurediscussedabove.
**5.26 例：** minimalpolynomialofanoperatoron\mathbf{F}5
Suppose\mathcal{T} \inℒ(\mathbf{F}5)and
0 0 0 0 -3
⎛ ⎞
⎜ ⎟
⎜ 1 0 0 0 6 ⎟
⎜ ⎟
⎜ ⎟
ℳ(\mathcal{T})=⎜ ⎜ 0 1 0 0 0 ⎟ ⎟
⎜ ⎟
⎜ ⎟
⎜ ⎜ 0 0 1 0 0 ⎟ ⎟
⎝ 0 0 0 1 0 ⎠
withrespecttothestandardbasise ,e ,e ,e ,e . Takingv=e for5.25,wehave
1 2 3 4 5 1
\mathcal{T}e =e , \mathcal{T}4e =\mathcal{T}(\mathcal{T}3e )=\mathcal{T}e =e ,
1 2 1 1 4 5
\mathcal{T}2e =\mathcal{T}(\mathcal{T}e )=\mathcal{T}e =e , \mathcal{T}5e =\mathcal{T}(\mathcal{T}4e )=\mathcal{T}e =-3e +6e .
1 1 2 3 1 1 5 1 2
\mathcal{T}3e =\mathcal{T}(\mathcal{T}2e )=\mathcal{T}e =e ,
1 1 3 4
Thus3e -6\mathcal{T}e =-\mathcal{T}5e . Theliste ,\mathcal{T}e ,\mathcal{T}2e ,\mathcal{T}3e ,\mathcal{T}4e ,whichequalsthelist
1 1 1 1 1 1 1 1
e ,e ,e ,e ,e ,islinearlyindependent,sonootherlinearcombinationofthislist
1 2 3 4 5
equals-\mathcal{T}5e . Hencetheminimalpolynomialof\mathcal{T} is3-6z+z5.
Recallthatbydefinition,eigenvaluesofoperatorson\mathcal{V} andzerosofpolynomialsin𝒫(\mathbf{F})mustbeelementsof\mathbf{F}. Inparticular,if\mathbf{F} = \mathbf{R},theneigenvalues
andzerosmustberealnumbers.
5.27 eigenvaluesarethezerosoftheminimalpolynomial
Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}).
$$(a) Thezerosoftheminimalpolynomialof\mathcal{T} aretheeigenvaluesof\mathcal{T}.$$
$$(b) If\mathcal{V} isacomplexvectorspace,thentheminimalpolynomialof\mathcal{T} hasthe$$
form
$$(z- \lambda )⋯(z- \lambda ),$$
1 m
where \lambda ,…,\lambda isalistofalleigenvaluesof\mathcal{T},possiblywithrepetitions.
1 m
Proof Letpbetheminimalpolynomialof\mathcal{T}.
$$(a) Firstsuppose \lambda\in\mathbf{F} isazeroofp. Thenpcanbewrittenintheform$$
p(z)=(z- \lambda)q(z),
where q is a monic polynomial with coefficients in \mathbf{F} (see 4.6). Because
p(\mathcal{T})=0,wehave
$$0=(\mathcal{T}- \lambda\mathcal{I})(q(\mathcal{T})v)$$
forallv\in\mathcal{V}. Becausedegq=(degp)-1andpistheminimalpolynomial
of\mathcal{T},thereexistsatleastonevectorv\in\mathcal{V}suchthatq(\mathcal{T})v\neq0. Theequation
abovethusimpliesthat \lambdaisaneigenvalueof\mathcal{T},asdesired.

Section5B The Minimal Polynomial 147
To prove that every eigenvalue of \mathcal{T} is a zero of p, now suppose \lambda \in \mathbf{F} is
aneigenvalueof\mathcal{T}. Thusthereexistsv \in \mathcal{V} withv \neq 0suchthat\mathcal{T}v = \lambdav.
Repeatedapplicationsof\mathcal{T}tobothsidesofthisequationshowthat\mathcal{T}kv= \lambdakv
foreverynonnegativeintegerk. Thus
p(\mathcal{T})v=p(\lambda)v.
Becausepistheminimalpolynomialof\mathcal{T},wehavep(\mathcal{T})v = 0. Hencethe
equationaboveimpliesthatp(\lambda)=0. Thus \lambdaisazeroofp,asdesired.
$$(b) Togetthedesiredresult,use(a)andthesecondversionofthefundamental$$
theoremofalgebra(see4.13).
Anonzeropolynomialhasatmostasmanydistinctzerosasitsdegree(see4.8).
Thus(a)ofthepreviousresult,alongwiththeresultthattheminimalpolynomial
ofanoperatoron\mathcal{V} hasdegreeatmostdim\mathcal{V},givesanalternativeproofof5.12,
whichstatesthatanoperatoron\mathcal{V} hasatmostdim\mathcal{V} distincteigenvalues.
Every monic polynomial is the minimal polynomial of some operator, as
shownby Exercise16,whichgeneralizes Example5.26. Thus5.27(a)showsthat
findingexactexpressionsfortheeigenvaluesofanoperatorisequivalenttothe
problemoffindingexactexpressionsforthezerosofapolynomial(andthusis
notpossibleforsomeoperators).
**5.28 例：** Anoperatorwhoseeigenvaluescannotbefoundexactly
Let\mathcal{T} \inℒ(\mathbf{C}5)betheoperatordefinedby
\mathcal{T}(z ,z ,z ,z ,z )=(-3z ,z +6z ,z ,z ,z ).
1 2 3 4 5 5 1 5 2 3 4
Thematrixof\mathcal{T} withrespecttothestandardbasisof\mathbf{C}5 isthe5-by-5matrixin
Example5.26. Asweshowedinthatexample,theminimalpolynomialof\mathcal{T} is
thepolynomial
3-6z+z5.
Nozeroofthepolynomialabovecanbeexpressedusingrationalnumbers,
rootsofrationalnumbers,andtheusualrulesofarithmetic(aproofofthiswould
takeusconsiderablybeyondlinearalgebra). Becausethezerosofthepolynomial
abovearetheeigenvaluesof\mathcal{T} [by5.27(a)],wecannotfindanexactexpression
foranyeigenvalueof\mathcal{T} inanyfamiliarform.
Numericaltechniques,whichwewillnotdiscusshere,showthatthezeros
ofthepolynomialabove,andthustheeigenvaluesof\mathcal{T},areapproximatelythe
followingfivecomplexnumbers:
-1.67, 0.51, 1.40, -0.12+1.59i, -0.12-1.59i.
Note that the two nonreal zeros of this polynomial are complex conjugates of
eachother,asweexpectforapolynomialwithrealcoefficients(see4.14).

148 Chapter 5 Eigenvaluesand Eigenvectors
Thenextresultcompletelycharacterizesthepolynomialsthatwhenappliedto
anoperatorgivethe0operator.
5.29 q(\mathcal{T})=0 ⟺ qisapolynomialmultipleoftheminimalpolynomial
Suppose\mathcal{V} isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V}),andq\in𝒫(\mathbf{F}). Thenq(\mathcal{T})=0
ifandonlyifqisapolynomialmultipleoftheminimalpolynomialof\mathcal{T}.
Proof Letpdenotetheminimalpolynomialof\mathcal{T}.
Firstsupposeq(\mathcal{T})=0. Bythedivisionalgorithmforpolynomials(4.9),there
existpolynomialss,r \in𝒫(\mathbf{F})suchthat
5.30 q=ps+r
anddegr <degp. Wehave
$$0=q(\mathcal{T})=p(\mathcal{T})s(\mathcal{T})+r(\mathcal{T})=r(\mathcal{T}).$$
Theequationaboveimpliesthatr =0(otherwise,dividingrbyitshighest-degree
coefficientwouldproduceamonicpolynomialthatwhenappliedto\mathcal{T} gives0;
thispolynomialwouldhaveasmallerdegreethantheminimalpolynomial,which
wouldbeacontradiction). Thus5.30becomestheequationq=ps. Henceqisa
polynomialmultipleofp,asdesired.
To prove the other direction, now suppose q is a polynomial multiple of p.
Thusthereexistsapolynomials\in𝒫(\mathbf{F})suchthatq=ps. Wehave
q(\mathcal{T})=p(\mathcal{T})s(\mathcal{T})=0s(\mathcal{T})=0,
asdesired.
Thenextresultisaniceconsequenceoftheresultabove.
5.31 minimalpolynomialofarestrictionoperator
Suppose\mathcal{V} isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V}),and\mathcal{U} isasubspaceof\mathcal{V} thatis
invariantunder\mathcal{T}. Thentheminimalpolynomialof\mathcal{T}isapolynomialmultiple
oftheminimalpolynomialof\mathcal{T}| .
\mathcal{U}
Proof Supposepistheminimalpolynomialof\mathcal{T}. Thusp(\mathcal{T})v=0forallv\in\mathcal{V}.
Inparticular,
p(\mathcal{T})u=0forallu\in\mathcal{U}.
Thusp(\mathcal{T}| ) = 0. Now5.29,appliedtotheoperator\mathcal{T}| inplaceof\mathcal{T},implies
\mathcal{U} \mathcal{U}
thatpisapolynomialmultipleoftheminimalpolynomialof\mathcal{T}| .
\mathcal{U}
See Exercise25foraresultaboutquotientoperatorsthatisanalogoustothe
resultabove.
Thenextresultshowsthattheconstanttermoftheminimalpolynomialofan
operatordetermineswhethertheoperatorisinvertible.

| --- | --- | --- | --- | --------- | --- | -------------------- | --- | --- | --- |
|      |     | notinvertible |     | constanttermofminimalpolynomialof |     |     |     | is0 |     |
| ---- | --- | ------------- | --- | --------------------------------- | --- | --- | --- | --- | --- |
| 5.32 | \mathcal{T}   |               | ⟺   |                                   |     |     |     | \mathcal{T}   |     |
Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \in ℒ(\mathcal{V}). Then\mathcal{T} isnotinvertibleif
| andonlyiftheconstanttermoftheminimalpolynomialof\mathcal{T} |          |                                     |     |     |                        |     |     | is0. |     |
| ------------------------------------------------- | -------- | ----------------------------------- | --- | --- | ---------------------- | --- | --- | ---- | --- |
| Proof                                             | Suppose\mathcal{T} | \inℒ(\mathcal{V})andpistheminimalpolynomialof\mathcal{T}. |     |     |                        |     |     | Then |     |
|                                                   |          | \mathcal{T} isnotinvertible                   |     | ⟺   | 0isaneigenvalueof\mathcal{T}     |     |     |      |     |
|                                                   |          |                                     |     | ⟺   | 0isazeroofp            |     |     |      |     |
|                                                   |          |                                     |     | ⟺   | theconstanttermofpis0, |     |     |      |     |
wherethefirstequivalenceholdsby5.7,thesecondequivalenceholdsby5.27(a),
andthelastequivalenceholdsbecausetheconstanttermofpequalsp(0).
| Eigenvalues |     | on Odd-Dimensional |     |     | Real | Vector | Spaces |     |     |
| ----------- | --- | ------------------ | --- | --- | ---- | ------ | ------ | --- | --- |
Thenextresultwillbethekeytoolthatweusetoshowthateveryoperatoronan
odd-dimensionalrealvectorspacehasaneigenvalue.
5.33 even-dimensionalnullspace
ℒ(\mathcal{V})
| Suppose\mathbf{F} |     | = \mathbf{R} and\mathcal{V} | isfinite-dimensional. |                                      |     | Supposealsothat\mathcal{T} |     | \in   |     |
| -------- | --- | -------- | --------------------- | ------------------------------------ | --- | ---------------- | --- | --- | --- |
| andb,c   | \in\mathbf{R}  | withb2   | <4c.                  | Thendimnull(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})isanevennumber. |     |                  |     |     |     |
Proof Recallthatnull(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})isinvariantunder\mathcal{T}(by5.18). Byreplacing
\mathcal{V}withnull(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})andreplacing\mathcal{T}with\mathcal{T}restrictedtonull(\mathcal{T}2+b\mathcal{T}+c\mathcal{I}),
| wecanassumethat\mathcal{T}2+b\mathcal{T}+c\mathcal{I} |         |        |     | =0;wenowneedtoprovethatdim\mathcal{V} |     |     |      | iseven. |     |
| ----------------------- | ------- | ------ | --- | --------------------------- | --- | --- | ---- | ------- | --- |
|                         | Suppose | andv\in\mathcal{V} |     | aresuchthat\mathcal{T}v=              |     | \lambdav. | Then |         |     |
\lambda\in\mathbf{R}
|     | 0=(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})v=(\lambda2+b\lambda+c)v=((\lambda+ |     |     |     |     |     | b) 2 | b2  |     |
| --- | ----------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- |
|     |                               |     |     |     |     |     | +c-  | )v. |     |
Theterminlargeparenthesesaboveisapositivenumber. Thustheequationabove
| impliesthatv=0. |     | Hencewehaveshownthat\mathcal{T} |     |     |     | hasnoeigenvectors. |     |     |     |
| --------------- | --- | --------------------- | --- | --- | --- | ------------------ | --- | --- | --- |
Let\mathcal{U}beasubspaceof\mathcal{V}thatisinvariantunder\mathcal{T}andhasthelargestdimension
amongallsubspacesof\mathcal{V} thatareinvariantunder\mathcal{T} andhaveevendimension. If
\mathcal{U} =\mathcal{V},thenwearedone;otherwiseassumethereexistsw\in\mathcal{V} suchthatw\notin\mathcal{U}.
|            | Let | span(w,\mathcal{T}w).      |     | Then                               | is invariant |     | under because |       |     |
| ---------- | --- | ---------------- | --- | ---------------------------------- | ------------ | --- | ------------- | ----- | --- |
|            | \mathcal{W}   | =                |     | \mathcal{W}                                  |              |     | \mathcal{T}             | \mathcal{T}(\mathcal{T}w) | =   |
| -b\mathcal{T}w-cw.   |     | Furthermore,dim\mathcal{W} |     | =2becauseotherwisewwouldbeaneigen- |              |     |               |       |     |
| vectorof\mathcal{T}. |     | Now              |     |                                    |              |     |               |       |     |
dim(\mathcal{U}+\mathcal{W})=dim\mathcal{U}+dim\mathcal{W}-dim(\mathcal{U}\cap\mathcal{W})=dim\mathcal{U}+2,
where \mathcal{U} \cap\mathcal{W} = {0} because otherwise \mathcal{U} \cap\mathcal{W} would be a one-dimensional
subspaceof\mathcal{V}thatisinvariantunder\mathcal{T}(impossiblebecause\mathcal{T}hasnoeigenvectors).
Because\mathcal{U}+\mathcal{W}isinvariantunder\mathcal{T},theequationaboveshowsthatthereexists
asubspaceof\mathcal{V} invariantunder\mathcal{T} ofevendimensionlargerthandim\mathcal{U}. Thusthe
| assumptionthat\mathcal{U} |     | \neq\mathcal{V}  | wasincorrect. |     | Hence\mathcal{V} | hasevendimension. |     |     |     |
| --------------- | --- | --- | ------------- | --- | ------ | ----------------- | --- | --- | --- |

| -------- | -------------------------- | --- | --- |
Thenextresultstatesthatonodd-dimensionalvectorspaces,everyoperator
hasaneigenvalue. Wealreadyknowthisresultforfinite-dimensionalcomplex
vector spaces (without the odd hypothesis). Thus in the proof below, we will
| assumethat\mathbf{F} | =\mathbf{R}. |     |     |
| ----------- | --- | --- | --- |
5.34 operatorsonodd-dimensionalvectorspaceshaveeigenvalues
Everyoperatoronanodd-dimensionalvectorspacehasaneigenvalue.
Proof Suppose\mathbf{F} =\mathbf{R} and\mathcal{V} isfinite-dimensional. Letn=dim\mathcal{V},andsuppose
nisanoddnumber. Let\mathcal{T} \inℒ(\mathcal{V}). Wewilluseinductiononninstepsofsize
twotoshowthat\mathcal{T} hasaneigenvalue. Togetstarted,notethatthedesiredresult
holdsifdim\mathcal{V} =1becausetheneverynonzerovectorin\mathcal{V} isaneigenvectorof\mathcal{T}.
Nowsupposethatn\geq3andthedesiredresultholdsforalloperatorsonall
odd-dimensionalvectorspacesofdimensionlessthann. Letpdenotetheminimal
polynomialof\mathcal{T}. Ifpisapolynomialmultipleofx-\lambdaforsome \lambda\in\mathbf{R},then \lambdais
aneigenvalueof\mathcal{T} [by5.27(a)]andwearedone. Thuswecanassumethatthere
existb,c \in\mathbf{R} suchthatb2 <4candpisapolynomialmultipleofx2+bx+c(see
4.16).
Thereexistsamonicpolynomialq\in𝒫(\mathbf{R})suchthatp(x)=q(x)(x2+bx+c)
| forallx \in\mathbf{R}. | Now |     |     |
| ----------- | --- | --- | --- |
$$0=p(\mathcal{T})=(q(\mathcal{T}))(\mathcal{T}2+b\mathcal{T}+c\mathcal{I}),$$
| whichmeansthatq(\mathcal{T})equals0onrange(\mathcal{T}2+b\mathcal{T}+c\mathcal{I}). |     | Becausedegq<degp |     |
| ------------------------------------------- | --- | ---------------- | --- |
andpistheminimalpolynomialof\mathcal{T},thisimpliesthatrange(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})\neq\mathcal{V}.
Thefundamentaltheoremoflinearmaps(3.21)tellsusthat
| dim\mathcal{V} | =dimnull(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})+dimrange(\mathcal{T}2+b\mathcal{T}+c\mathcal{I}). |     |     |
| ---- | -------------------------------------- | --- | --- |
Because dim\mathcal{V} is odd (by hypothesis) and dimnull(\mathcal{T}2 +b\mathcal{T} +c\mathcal{I}) is even (by
5.33),theequationaboveshowsthatdimrange(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})isodd.
| Hencerange(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})isasubspaceof\mathcal{V} |     | thatisinvariantunder\mathcal{T} | (by |
| ---------------------------------- | --- | --------------------- | --- |
5.18)andthathasodddimensionlessthandim\mathcal{V}. Ourinductionhypothesisnow
impliesthat\mathcal{T} restrictedtorange(\mathcal{T}2+b\mathcal{T}+c\mathcal{I})hasaneigenvalue,whichmeans
that\mathcal{T} hasaneigenvalue.
See Exercise23in Section8Band Exercise10in Section9Cforalternative
proofsoftheresultabove.
| Exercises 5B |     |     |     |
| ------------ | --- | --- | --- |
1 Suppose\mathcal{T} \inℒ(\mathcal{V}). Provethat9isaneigenvalueof\mathcal{T}2 ifandonlyif3or
-3isaneigenvalueof\mathcal{T}.
| 2 Suppose\mathcal{V} | isacomplexvectorspaceand\mathcal{T} | \in ℒ(\mathcal{V})hasnoeigenvalues. |     |
| ---------- | ------------------------- | ----------------------- | --- |
Provethateverysubspaceof\mathcal{V} invariantunder\mathcal{T} iseither{0}orinfinitedimensional.

| --- | --- | ------------------------------ | --- |
\inℒ(\mathbf{F}n)isdefinedby
3 Supposenisanintegerwithn>1and\mathcal{T}
|                                           | ,…,x         | +⋯+x ,…,x | +⋯+x   |
| ----------------------------------------- | ------------ | --------- | ------ |
|                                           | \mathcal{T}(x 1 n )=(x | 1 n       | 1 n ). |
| (a) Findalleigenvaluesandeigenvectorsof\mathcal{T}. |              |           |        |
| (b) Findtheminimalpolynomialof\mathcal{T}.          |              |           |        |
Thematrixof \mathcal{T}withrespecttothestandardbasisof \mathbf{F}nconsistsofall1’s.
| 4 Suppose\mathbf{F} | = \mathbf{C},\mathcal{T} \in ℒ(\mathcal{V}),p | \in 𝒫(\mathbf{C})isanonconstantpolynomial,and |     |
| ---------- | -------------- | ---------------------------------- | --- |
\alpha \in \mathbf{C}. Prove that \alpha is an eigenvalueof p(\mathcal{T}) if and only if \alpha = p(\lambda) for
| someeigenvalue | \lambdaof\mathcal{T}. |     |     |
| -------------- | ----- | --- | --- |
5 Giveanexampleofanoperatoron\mathbf{R}2 thatshowstheresultin Exercise4
| doesnotholdif\mathbf{C} | isreplacedwith\mathbf{R}. |     |     |
| -------------- | ---------------- | --- | --- |
ℒ(\mathbf{F}2)
6 Suppose \mathcal{T} \in is defined by \mathcal{T}(w,z) = (-z,w). Find the minimal
polynomialof\mathcal{T}.
7 (a) Giveanexampleof\mathcal{S},\mathcal{T} \inℒ(\mathbf{F}2)suchthattheminimalpolynomialof
\mathcal{S}\mathcal{T} doesnotequaltheminimalpolynomialof\mathcal{T}\mathcal{S}.
$$(b) Suppose\mathcal{V} isfinite-dimensionaland\mathcal{S},\mathcal{T} \inℒ(\mathcal{V}). Provethatifatleast$$
oneof\mathcal{S},\mathcal{T} isinvertible,thentheminimalpolynomialof\mathcal{S}\mathcal{T} equalsthe
minimalpolynomialof\mathcal{T}\mathcal{S}.
| Hint:Showthatif | \mathcal{S}isinvertibleandp\in𝒫(\mathbf{F}),thenp(\mathcal{T}\mathcal{S})=\mathcal{S}-1p(\mathcal{S}\mathcal{T})\mathcal{S}. |     |     |
| --------------- | ------------------------------------------- | --- | --- |
8 Suppose\mathcal{T} \inℒ(\mathbf{R}2)istheoperatorofcounterclockwiserotationby1\circ. Find
theminimalpolynomialof\mathcal{T}.
Becausedim\mathbf{R}2
=2,thedegreeoftheminimalpolynomialof \mathcal{T}isatmost2.
Thustheminimalpolynomialof \mathcal{T}isnotthetemptingpolynomialx180+1,
| eventhough\mathcal{T}180 | =-\mathcal{I}. |     |     |
| -------------- | ---- | --- | --- |
9 Suppose\mathcal{T} \inℒ(\mathcal{V})issuchthatwithrespecttosomebasisof\mathcal{V},allentries
ofthematrixof\mathcal{T} arerationalnumbers. Explainwhyallcoefficientsofthe
| minimalpolynomialof\mathcal{T} | arerationalnumbers.    |               |           |
| -------------------- | ---------------------- | ------------- | --------- |
| 10 Suppose\mathcal{V}          | isfinite-dimensional,\mathcal{T} | \inℒ(\mathcal{V}),andv\in\mathcal{V}. | Provethat |
span(v,\mathcal{T}v,…,\mathcal{T}mv)=span(v,\mathcal{T}v,…,\mathcal{T}dim\mathcal{V}-1v)
forallintegersm\geqdim\mathcal{V}-1.
11 Suppose\mathcal{V} isatwo-dimensionalvectorspace,\mathcal{T} \inℒ(\mathcal{V}),andthematrixof
|                                     |      | a c   |           |
| ----------------------------------- | ---- | ----- | --------- |
| \mathcal{T} withrespecttosomebasisof\mathcal{V}         |      | is(   | ).        |
|                                     |      | b d   |           |
| (a) Showthat\mathcal{T}2-(a+d)\mathcal{T}+(ad-bc)\mathcal{I}      |      | =0.   |           |
| (b) Showthattheminimalpolynomialof\mathcal{T} |      |       | equals    |
|                                     | ⎧    |       | =0anda=d, |
|                                     | {z-a | ifb=c |           |
⎨ {z2-(a+d)z+(ad-bc)
|     | ⎩   | otherwise. |     |
| --- | --- | ---------- | --- |

| --- | -------- | -------------------------- | --- | --- | --- | --- |
ℒ(\mathbf{F}n)
| 12 Define | \mathcal{T} \in | by  | \mathcal{T}(x ,x | ,x ,…,x ) = | (x ,2x ,3x ,…,nx | ). Find |
| --------- | --- | --- | ------ | ----------- | ---------------- | ------- |
|           |     |     | 1      | 2 3 n       | 1 2 3            | n       |
theminimalpolynomialof\mathcal{T}.
Suppose \mathcal{V} is finite-dimensional, \mathcal{T} \in ℒ(\mathcal{V}), and p \in 𝒫(\mathbf{F}). Prove that
| thereexistsauniquer |     |     | \in𝒫(\mathbf{F})suchthatp(\mathcal{T})=r(\mathcal{T})anddegrislessthan |     |     |     |
| ------------------- | --- | --- | --------------------------------------- | --- | --- | --- |
thedegreeoftheminimalpolynomialof\mathcal{T}.
ℒ(\mathcal{V})hasminimalpolynomial
| 14 Suppose\mathcal{V}          |     | isfinite-dimensionaland\mathcal{T} |     | \in                              |     |     |
| -------------------- | --- | ------------------------ | --- | ------------------------------ | --- | --- |
| 4+5z-6z2-7z3+2z4+z5. |     |                          |     | Findtheminimalpolynomialof\mathcal{T}-1. |     |     |
15 Suppose\mathcal{V} isafinite-dimensionalcomplexvectorspacewithdim\mathcal{V} > 0
f∶
| and\mathcal{T}      | \inℒ(\mathcal{V}). | Define                    | \mathbf{C} \rightarrow\mathbf{R}             | by                |                  |     |
| --------- | ------ | ------------------------- | ---------------- | ----------------- | ---------------- | --- |
|           |        |                           | f(\lambda)=dimrange(\mathcal{T}- |                   | \lambda\mathcal{I}).             |     |
| Provethat | f      | isnotacontinuousfunction. |                  |                   |                  |     |
| Supposea  | ,…,a   | \in\mathbf{F}.                       | Let\mathcal{T}             | betheoperatoron\mathbf{F}n | whosematrix(with |     |
| 16        | 0      | n-1                       |                  |                   |                  |     |
respecttothestandardbasis)is
|     |     |     | 0   | -a   |          |     |
| --- | --- | --- | --- | ---- | -------- | --- |
|     |     | ⎛   |     |      | 0 ⎞      |     |
|     |     | ⎜   |     |      | ⎟        |     |
|     |     | ⎜ ⎜ | 1 0 | -a   | ⎟ ⎟      |     |
|     |     | ⎜   |     |      | 1 ⎟      |     |
|     |     | ⎜   | 1   | ⋱ -a | ⎟        |     |
|     |     | ⎜ ⎜ |     |      | 2 ⎟ ⎟ ⎟. |     |
⎜
|     |     | ⎜ ⎜ |     | ⋱    | ⋮ ⎟ ⎟ |     |
| --- | --- | --- | --- | ---- | ----- | --- |
|     |     | ⎜   |     |      | ⎟     |     |
|     |     | ⎜   |     | 0 -a | ⎟     |     |
|     |     | ⎜   |     |      | n-2 ⎟ |     |
|     |     | ⎝   |     | 1 -a | ⎠     |     |
n-1
Hereallentriesofthematrixare0exceptforall1’sonthelineunderthe
diagonalandtheentriesinthelastcolumn(someofwhichmightalsobe0).
| Showthattheminimalpolynomialof\mathcal{T} |     |     |          | isthepolynomial |     |     |
| ------------------------------- | --- | --- | -------- | --------------- | --- | --- |
|                                 |     | a   | +a z+⋯+a | zn-1+zn.        |     |     |
|                                 |     |     | 0 1      | n-1             |     |     |
Thematrixaboveiscalledthecompanionmatrixofthepolynomialabove.
Thisexerciseshowsthateverymonicpolynomialistheminimalpolynomial
|     | ofsomeoperator. | Henceaformulaoranalgorithmthatcouldproduce |     |     |     |     |
| --- | --------------- | ------------------------------------------ | --- | --- | --- | --- |
exacteigenvaluesforeachoperatoroneach\mathbf{F}ncouldthenproduceexact
zerosforeachpolynomial[by5.27(a)]. Thusthereisnosuchformulaor
algorithm. However,efficientnumericalmethodsexistforobtainingvery
goodapproximationsfortheeigenvaluesofanoperator.
17 Suppose\mathcal{V}isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V}),andpistheminimalpolynomial
| of\mathcal{T}.                          | Suppose | \mathbf{F}.  | Showthattheminimalpolynomialof\mathcal{T}- |     |     | isthe |
| ----------------------------- | ------- | --- | -------------------------------- | --- | --- | ----- |
|                               |         | \lambda \in |                                  |     |     | \lambda\mathcal{I}    |
| polynomialqdefinedbyq(z)=p(z+ |         |     |                                  | \lambda). |     |       |
18 Suppose\mathcal{V}isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V}),andpistheminimalpolynomial
of\mathcal{T}. Suppose \lambda\in\mathbf{F}\{0}. Showthattheminimalpolynomialof \lambda\mathcal{T} isthe
z
| polynomialqdefinedbyq(z)= |     |     |     | \lambdadegpp( ). |     |     |
| ------------------------- | --- | --- | --- | ---------- | --- | --- |
\lambda

Section5B The Minimal Polynomial 153
19 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Letℰbethesubspaceof
ℒ(\mathcal{V})definedby
ℰ={q(\mathcal{T})∶q\in𝒫(\mathbf{F})}.
Provethatdimℰequalsthedegreeoftheminimalpolynomialof\mathcal{T}.
20 Suppose\mathcal{T} \inℒ(\mathbf{F}4)issuchthattheeigenvaluesof\mathcal{T} are3,5,8. Provethat
$$(\mathcal{T}-3\mathcal{I})2(\mathcal{T}-5\mathcal{I})2(\mathcal{T}-8\mathcal{I})2 =0.$$
21 Suppose \mathcal{V} is finite-dimensional and \mathcal{T} \in ℒ(\mathcal{V}). Prove that the minimal
polynomialof\mathcal{T} hasdegreeatmost1+dimrange\mathcal{T}.
If dimrange\mathcal{T} <dim\mathcal{V}-1,thenthisexercisegivesabetterupperbound
than5.22forthedegreeoftheminimalpolynomialof \mathcal{T}.
22 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Provethat\mathcal{T} isinvertibleif
andonlyif\mathcal{I} \inspan(\mathcal{T},\mathcal{T}2,…,\mathcal{T}dim\mathcal{V}).
23 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Letn=dim\mathcal{V}. Provethat
ifv\in\mathcal{V},thenspan(v,\mathcal{T}v,…,\mathcal{T}n-1v)isinvariantunder\mathcal{T}.
24 Suppose\mathcal{V}isafinite-dimensionalcomplexvectorspace. Suppose\mathcal{T} \inℒ(\mathcal{V})
issuchthat5and6areeigenvaluesof\mathcal{T} andthat\mathcal{T} hasnoothereigenvalues.
Provethat(\mathcal{T}-5\mathcal{I})dim\mathcal{V}-1(\mathcal{T}-6\mathcal{I})dim\mathcal{V}-1 =0.
25 Suppose\mathcal{V} isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V}),and\mathcal{U} isasubspaceof\mathcal{V} that
isinvariantunder\mathcal{T}.
$$(a) Provethattheminimalpolynomialof\mathcal{T} isapolynomialmultipleofthe$$
minimalpolynomialofthequotientoperator\mathcal{T}/\mathcal{U}.
$$(b) Provethat$$
$$(minimalpolynomialof\mathcal{T}| )\times(minimalpolynomialof\mathcal{T}/\mathcal{U})$$
\mathcal{U}
isapolynomialmultipleoftheminimalpolynomialof\mathcal{T}.
Thequotientoperator\mathcal{T}/\mathcal{U}wasdefinedin Exercise38in Section5A.
26 Suppose\mathcal{V} isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V}),and\mathcal{U} isasubspaceof\mathcal{V} that
isinvariantunder\mathcal{T}. Provethatthesetofeigenvaluesof\mathcal{T} equalstheunion
ofthesetofeigenvaluesof\mathcal{T}| andthesetofeigenvaluesof\mathcal{T}/\mathcal{U}.
\mathcal{U}
27 Suppose \mathbf{F} = \mathbf{R}, \mathcal{V} is finite-dimensional, and \mathcal{T} \in ℒ(\mathcal{V}). Prove that the
minimalpolynomialof\mathcal{T} equalstheminimalpolynomialof\mathcal{T}.
\mathbf{C}
Thecomplexification\mathcal{T} wasdefinedin Exercise33of Section3B.
\mathbf{C}
28 Suppose \mathcal{V} is finite-dimensional and \mathcal{T} \in ℒ(\mathcal{V}). Prove that the minimal
polynomialof\mathcal{T}′ \inℒ(\mathcal{V}′)equalstheminimalpolynomialof\mathcal{T}.
Thedualmap\mathcal{T}′wasdefinedin Section3F.
29 Showthateveryoperatoronafinite-dimensionalvectorspaceofdimension
atleasttwohasaninvariantsubspaceofdimensiontwo.
Exercise6in Section5Cwillgiveanimprovementofthisresultwhen\mathbf{F} =\mathbf{C}.

| -------- | -------------------------- | --- | --- | --- | --- |
| 5C Upper-Triangular |     | Matrices |     |     |     |
| ------------------- | --- | -------- | --- | --- | --- |
In Chapter 3wedefinedthematrixofalinearmapfromafinite-dimensionalvector
spacetoanotherfinite-dimensionalvectorspace. Thatmatrixdependsonachoice
ofbasisofeachofthetwovectorspaces. Nowthatwearestudyingoperators,
whichmapavectorspacetoitself,theemphasisisonusingonlyonebasis.
| 5.35 definition: matrixofanoperator,ℳ(\mathcal{T}) |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- |
Suppose\mathcal{T} \inℒ(\mathcal{V}). Thematrixof \mathcal{T} withrespecttoabasisv ,…,v of\mathcal{V} is
1 n
then-by-nmatrix
|               |              |     | \mathcal{A} ⋯       | \mathcal{A}       |     |
| ------------- | ------------ | --- | --------- | ------- | --- |
|               |              |     | 1,1       | 1,n     |     |
|               |              |     | ⎛ ⎜       | ⎞ ⎟     |     |
|               | ℳ(\mathcal{T})=⎜       |     | ⋮         | ⋮ ⎟     |     |
|               |              |     | ⎜         | ⎟       |     |
|               |              |     | ⎝ \mathcal{A} n,1 ⋯ | \mathcal{A} n,n ⎠ |     |
| whoseentries\mathcal{A} | aredefinedby |     |           |         |     |
j,k
|     |     | \mathcal{T}v =\mathcal{A} | v +⋯+\mathcal{A} | v .   |     |
| --- | --- | ----- | ------ | ----- | --- |
|     |     | k     | 1,k 1  | n,k n |     |
ℳ(\mathcal{T},(v ,…,v
The notation 1 n )) is used if the basis is not clear from the
context.
Operatorshavesquarematrices(meaningthatthenumberofrowsequalsthe
numberofcolumns),ratherthanthemoregeneralrectangularmatricesthatwe
consideredearlierforlinearmaps.
| If \mathcal{T} is an operator | on  | \mathbf{F}n and | no ba- |     |     |
| ------------------- | --- | ------ | ------ | --- | --- |
Thekthcolumnofthematrixℳ(\mathcal{T})is
sisisspecified,assumethatthebasisin
|     |     |     | formed | from the coefficients | used to |
| --- | --- | --- | ------ | --------------------- | ------- |
questionisthestandardone(wherethe
|                            |     |          | write\mathcal{T}v   | asalinearcombinationof |     |
| -------------------------- | --- | -------- | --------- | ---------------------- | --- |
| kth basisvectoris1inthekth |     | slotand0 |           | k                      |     |
|                            |     |          | thebasisv | ,…,v .                 |     |
1 n
| inallotherslots). | Youcanthenthinkof |     |     |     |     |
| ----------------- | ----------------- | --- | --- | --- | --- |
thekth columnofℳ(\mathcal{T})as\mathcal{T} appliedtothekth basisvector,whereweidentify
n-by-1columnvectorswithelementsof\mathbf{F}n.
| 5.36 example: matrixofanoperatorwithrespecttostandardbasis |     |     |     |                  |     |
| ---------------------------------------------------------- | --- | --- | --- | ---------------- | --- |
| Define\mathcal{T} \inℒ(\mathbf{F}3)by\mathcal{T}(x,y,z)=(2x+y,5y+3z,8z).                  |     |     |     | Thenthematrixof\mathcal{T} |     |
| withrespecttothestandardbasisof\mathbf{F}3                          |     |     | is  |                  |     |
2 1 0
|     |     |        | ⎛ ⎜   | ⎞ ⎟   |     |
| --- | --- | ------ | ----- | ----- | --- |
|     |     | ℳ(\mathcal{T})=⎜ | 0 5   | 3 ⎟ , |     |
|     |     |        | ⎜     | ⎟     |     |
|     |     |        | ⎝ 0 0 | 8 ⎠   |     |
asyoushouldverify.
Acentralgoaloflinearalgebraistoshowthatgivenanoperator\mathcal{T} onafinitedimensionalvectorspace\mathcal{V},thereexistsabasisof\mathcal{V} withrespecttowhich\mathcal{T} has
areasonablysimplematrix. Tomakethisvagueformulationabitmoreprecise,
suchthatℳ(\mathcal{T})hasmany0’s.
wemighttrytochooseabasisof\mathcal{V}

Section5C Upper-Triangular Matrices 155
If \mathcal{V} is a finite-dimensional complex vector space, then we already know
enoughtoshowthatthereisabasisof\mathcal{V} withrespecttowhichthematrixof\mathcal{T}
has0’severywhereinthefirstcolumn,exceptpossiblythefirstentry. Inother
words,thereisabasisof\mathcal{V} withrespecttowhichthematrixof\mathcal{T} lookslike
\lambda
⎛ ⎞
⎜ ⎜ 0 ∗ ⎟ ⎟
⎜ ⎜ ⎟ ⎟;
⎜ ⎜ ⋮ ⎟ ⎟
⎝ 0 ⎠
here∗denotestheentriesinallcolumnsotherthanthefirstcolumn. Toprove
this,let \lambdabeaneigenvalueof\mathcal{T} (oneexistsby5.19)andletvbeacorresponding
eigenvector. Extendvtoabasisof\mathcal{V}. Thenthematrixof\mathcal{T} withrespecttothis
basishastheformabove. Soonwewillseethatwecanchooseabasisof\mathcal{V} with
respecttowhichthematrixof\mathcal{T} hasevenmore0’s.
**5.37 定义：** diagonalofamatrix
Thediagonalofasquarematrixconsistsoftheentriesonthelinefromthe
upperleftcornertothebottomrightcorner.
Forexample,thediagonalofthematrix
2 1 0
⎛ ⎞
⎜ ⎟
ℳ(\mathcal{T})=⎜ ⎜ 0 5 3 ⎟ ⎟
⎝ 0 0 8 ⎠
from Example5.36consistsoftheentries2,5,8,whichareshowninredinthe
matrixabove.
**5.38 定义：** upper-triangularmatrix
Asquarematrixiscalleduppertriangular ifallentriesbelowthediagonal
are0.
Forexample,the3-by-3matrixaboveisuppertriangular.
Typicallywerepresentanupper-triangularmatrixintheform
\lambda ∗
⎛ 1 ⎞
⎜ ⎟
⎜ ⎜ ⋱ ⎟ ⎟ ;
⎝ 0 \lambda n ⎠
the 0 in the matrix above indicates that Weoftenuse∗todenotematrixentries
all entries below the diagonal in this
thatwedonotknoworthatareirrelen-by-nmatrixequal0. Upper-triangular
vanttothequestionsbeingdiscussed.
matrices can be considered reasonably
simple—if n is large, then at least almost half the entries in an n-by-n uppertriangularmatrixare0.

| -------- | -------------------------- | --- | --- | --- |
Thenextresultprovidesausefulconnectionbetweenupper-triangularmatrices
andinvariantsubspaces.
5.39 conditionsforupper-triangularmatrix
Suppose \mathcal{T} \in ℒ(\mathcal{V}) and v ,…,v is a basis of \mathcal{V}. Then the following are
|     | 1   | n   |     |     |
| --- | --- | --- | --- | --- |
equivalent.
| (a) Thematrixof\mathcal{T} | withrespecttov     | ,…,v     | isuppertriangular. |     |
| ---------------- | ------------------ | -------- | ------------------ | --- |
|                  |                    | 1 n      |                    |     |
| ,…,v             |                    |          | =1,…,n.            |     |
| (b) span(v       | )isinvariantunder\mathcal{T} | foreachk |                    |     |
1 k
| (c) \mathcal{T}v \inspan(v | ,…,v )foreachk | =1,…,n. |     |     |
| -------------- | -------------- | ------- | --- | --- |
| k              | 1 k            |         |     |     |
Proof Firstsuppose(a)holds. Toprovethat(b)holds,supposek \in {1,…,n}.
\in{1,…,n},then
Ifj
|     | \mathcal{T}v  | \inspan(v ,…,v) |     |     |
| --- | --- | ------------- | --- | --- |
|     |     | j 1           | j   |     |
becausethematrixof\mathcal{T} withrespecttov ,…,v isuppertriangular. Because
|                     |      | 1                 | n   |     |
| ------------------- | ---- | ----------------- | --- | --- |
| span(v ,…,v)\subseteqspan(v | ,…,v | )ifj \leqk,weseethat |     |     |
| 1 j                 | 1    | k                 |     |     |
,…,v
|     | \mathcal{T}v  | j \inspan(v 1 | k ) |     |
| --- | --- | ----------- | --- | --- |
foreachj \in{1,…,k}. Thusspan(v ,…,v )isinvariantunder\mathcal{T},completingthe
1 k
proofthat(a)implies(b).
Now suppose (b) holds, so span(v ,…,v ) is invariant under \mathcal{T} for each
|     |     | 1 k |     |     |
| --- | --- | --- | --- | --- |
$$k =1,…,n. In particular, \mathcal{T}v \in span(v ,…,v ) for each k = 1,…,n. Thus$$
|     |     | k 1 | k   |     |
| --- | --- | --- | --- | --- |
$$(b)implies(c).$$
| Nowsuppose(c)holds,so\mathcal{T}v |     | \inspan(v ,…,v | )foreachk | =1,…,n. This |
| ----------------------- | --- | ------------ | --------- | ------------ |
|                         |     | k 1          | k         |              |
meansthatwhenwritingeach\mathcal{T}v asalinearcombinationofthebasisvectors
k
v ,…,v ,weneedtouseonlythevectorsv ,…,v . Henceallentriesunderthe
| 1 n |     | 1   | k   |     |
| --- | --- | --- | --- | --- |
diagonalofℳ(\mathcal{T})are0. Thusℳ(\mathcal{T})isanupper-triangularmatrix,completing
theproofthat(c)implies(a).
| Wehaveshownthat(a) | ⟹   | (b) ⟹ (c) ⟹ | (a),whichshowsthat(a),(b), |     |
| ------------------ | --- | ----------- | -------------------------- | --- |
and(c)areequivalent.
Thenextresulttellsusthatif\mathcal{T} \inℒ(\mathcal{V})andwithrespecttosomebasisof\mathcal{V}
wehave
∗
\lambda
|     |        | ⎛ 1 | ⎞     |     |
| --- | ------ | --- | ----- | --- |
|     | ℳ(\mathcal{T})=⎜ | ⎜ ⋱ | ⎟ ⎟ , |     |
|     |        | ⎜   | ⎟     |     |
|     |        | ⎝ 0 | \lambda ⎠   |     |
n
| then\mathcal{T} satisfiesasimpleequationdependingon |     |     | \lambda ,…,\lambda . |     |
| ----------------------------------------- | --- | --- | -------- | --- |
1 n
5.40 equationsatisfiedbyoperatorwithupper-triangularmatrix
| Suppose\mathcal{T} \inℒ(\mathcal{V})and\mathcal{V}                  | hasabasiswithrespecttowhich\mathcal{T} |                  |        | hasanupper- |
| ----------------------------------- | ---------------------------- | ---------------- | ------ | ----------- |
| triangularmatrixwithdiagonalentries |                              | \lambda ,…,\lambda           | . Then |             |
|                                     |                              | 1                | n      |             |
|                                     | (\mathcal{T}-                          | \lambda \mathcal{I})⋯(\mathcal{T}- \lambda \mathcal{I})=0. |        |             |
|                                     |                              | 1 n              |        |             |

| --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
Proof Letv ,…,v denoteabasisof\mathcal{V} withrespecttowhich\mathcal{T} hasanupper-
|     |     | 1   | n   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
triangular matrix with diagonal entries \lambda ,…,\lambda . Then \mathcal{T}v = \lambda v , which
|     |     |     |     |     | 1   | n   | 1   | 1 1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
meansthat(\mathcal{T}- \lambda \mathcal{I})v = 0,whichimpliesthat(\mathcal{T}- \lambda \mathcal{I})⋯(\mathcal{T}- \lambda \mathcal{I})v = 0
|                                          |     |     | 1   | 1   |     |     | 1          | m   | 1     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- |
| form=1,…,n(usingthecommutativityofeach\mathcal{T}- |     |     |     |     |     | \lambda\mathcal{I}  | witheach\mathcal{T}- |     | \lambda \mathcal{I}). |
|                                          |     |     |     |     |     |     | j          |     | k     |
Note that (\mathcal{T} - \lambda \mathcal{I})v \in span(v ). Thus (\mathcal{T} - \lambda \mathcal{I})(\mathcal{T} - \lambda \mathcal{I})v = 0 (by
|     |     |     | 2   | 2   | 1   |     | 1   | 2 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thepreviousparagraph), whichimpliesthat(\mathcal{T} - \lambda \mathcal{I})⋯(\mathcal{T} - \lambda \mathcal{I})v = 0for
|                                       |     |     |     |     |     | 1             |     | m 2   |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | ----- | --- |
| m=2,…,n(usingthecommutativityofeach\mathcal{T}- |     |     |     |     |     | \lambda\mathcal{I} witheach\mathcal{T}- |     | \lambda \mathcal{I}). |     |
|                                       |     |     |     |     |     | j             |     | k     |     |
Note that (\mathcal{T} - \lambda \mathcal{I})v \in span(v ,v ). Thus by the previous paragraph,
|      |        |     | 3      | 3   | 1 2                     |     |         |     |       |
| ---- | ------ | --- | ------ | --- | ----------------------- | --- | ------- | --- | ----- |
| (\mathcal{T}-\lambda | \mathcal{I})(\mathcal{T}-\lambda |     | \mathcal{I})(\mathcal{T}-\lambda | \mathcal{I})v | =0,whichimpliesthat(\mathcal{T}-\lambda |     | \mathcal{I})⋯(\mathcal{T}-\lambda |     | \mathcal{I})v = |
|      | 1      |     | 2      | 3 3 |                         |     | 1       | m   | 3     |
0form=3,…,n(usingthecommutativityofeach\mathcal{T}- \lambda\mathcal{I} witheach\mathcal{T}- \lambda \mathcal{I}).
|     |     |     |     |     |     |     | j   |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Continuingthispattern, weseethat(\mathcal{T} - \lambda \mathcal{I})⋯(\mathcal{T} - \lambda \mathcal{I})v = 0foreach
|     |     |     |     |     |     | 1   | n   | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
$$k =1,…,n. Thus(\mathcal{T}-\lambda \mathcal{I})⋯(\mathcal{T}-\lambda \mathcal{I})isthe0operatorbecauseitis0oneach$$
|     |     |     |     | 1   | n   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vectorinabasisof\mathcal{V}.
Unfortunatelynomethodexistsforexactlycomputingtheeigenvaluesofan
operatorfromitsmatrix. However,ifwearefortunateenoughtofindabasiswith
respecttowhichthematrixoftheoperatorisuppertriangular,thentheproblem
ofcomputingtheeigenvaluesbecomestrivial,asthenextresultshows.
5.41 determinationofeigenvaluesfromupper-triangularmatrix
Suppose\mathcal{T} \inℒ(\mathcal{V})hasanupper-triangularmatrixwithrespecttosomebasis
of\mathcal{V}. Thentheeigenvaluesof\mathcal{T} arepreciselytheentriesonthediagonalof
thatupper-triangularmatrix.
Proof Supposev ,…,v isabasisof\mathcal{V} withrespecttowhich\mathcal{T} hasanupper-
|     |     |     | 1   | n   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
triangularmatrix
∗
\lambda
|     |     |     |     |        | ⎛ 1 | ⎞   |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     | ℳ(\mathcal{T})=⎜ | ⎜   | ⎟ ⎟ |     |     |     |
|     |     |     |     |        | ⎜ ⋱ | ⎟.  |     |     |     |
|     |     |     |     |        | ⎝ 0 | \lambda ⎠ |     |     |     |
n
|            | Because\mathcal{T}v |           | = \lambda v       | ,weseethat | \lambda isaneigenvalueof\mathcal{T}. |      |         |         |     |
| ---------- | --------- | --------- | ----------- | ---------- | -------------------- | ---- | ------- | ------- | --- |
|            |           |           | 1 1         | 1          | 1                    |      |         |         |     |
|            | Supposek  | \in{2,…,n}. |             | Then(\mathcal{T}-\lambda   | \mathcal{I})v \inspan(v          |      | ,…,v ). | Thus\mathcal{T}-\lambda | \mathcal{I}   |
|            |           |           |             |            | k k                  | 1    | k-1     |         | k   |
| mapsspan(v |           | ,…,v      | )intospan(v |            | ,…,v ). Because      |      |         |         |     |
|            |           | 1         | k           |            | 1 k-1                |      |         |         |     |
|            | dimspan(v |           | ,…,v        | )=k        | and dimspan(v        | ,…,v | )=k-1,  |         |     |
|            |           |           | 1           | k          |                      | 1    | k-1     |         |     |
thisimpliesthat\mathcal{T}- \lambda \mathcal{I} restrictedtospan(v ,…,v )isnotinjective(by3.22).
|     |     |     |     | k   | 1   | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
,…,v
| Thusthereexistsv\inspan(v |     |     |     |     | )suchthatv\neq0and(\mathcal{T}- |     | \lambda   | \mathcal{I})v=0. | Thus |
| ----------------------- | --- | --- | --- | --- | ------------------ | --- | --- | ------ | ---- |
|                         |     |     |     | 1   | k                  |     |     | k      |      |
\lambda isaneigenvalueof\mathcal{T}. Hencewehaveshownthateveryentryonthediagonal
k
ofℳ(\mathcal{T})isaneigenvalueof\mathcal{T}.
To prove \mathcal{T} has no other eigenvalues, let q be the polynomial defined by
q(z)=(z- \lambda )⋯(z- \lambda ). Thenq(\mathcal{T})=0(by5.40). Henceqisapolynomial
|     |     | 1   |     | n   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
multipleoftheminimalpolynomialof\mathcal{T}(by5.29). Thuseveryzerooftheminimal
polynomialof\mathcal{T} isazeroofq. Becausethezerosoftheminimalpolynomialof
\mathcal{T} aretheeigenvaluesof\mathcal{T} (by5.27),thisimpliesthateveryeigenvalueof\mathcal{T} isa
zeroofq. Hencetheeigenvaluesof\mathcal{T} areallcontainedinthelist \lambda ,…,\lambda .
|     |     |     |     |     |     |     |     | 1   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| -------- | -------------------------- | --- | --- | --- | --- |
eigenvaluesviaanupper-triangularmatrix
**5.42 例：** | Define\mathcal{T} | \inℒ(\mathbf{F}3)by\mathcal{T}(x,y,z)=(2x+y,5y+3z,8z). |     |     | Thematrixof\mathcal{T} | with |
| ------- | --------------------------------- | --- | --- | ------------ | ---- |
respecttothestandardbasisis
2 1 0
|                                     |     | ⎛        | ⎞            |     |     |
| ----------------------------------- | --- | -------- | ------------ | --- | --- |
|                                     |     | ℳ(\mathcal{T})=⎜ ⎜ | ⎟ ⎟          |     |     |
|                                     |     | ⎜        | 0 5 3 ⎟.     |     |     |
|                                     |     | ⎝        | 0 0 8 ⎠      |     |     |
| Now5.41impliesthattheeigenvaluesof\mathcal{T} |     |          | are2,5,and8. |     |     |
Thenextexampleillustrates5.44: anoperatorhasanupper-triangularmatrix
withrespecttosomebasisifandonlyiftheminimalpolynomialoftheoperator
istheproductofpolynomialsofdegree1.
**5.43 例：** whether \mathcal{T} hasanupper-triangularmatrixcandependon\mathbf{F}
\inℒ(\mathbf{F}4)by
Define\mathcal{T}
|     | \mathcal{T}(z ,z ,z | ,z )=(-z | ,z ,2z +3z | ,z +3z ). |     |
| --- | --------- | -------- | ---------- | --------- | --- |
|     | 1 2       | 3 4      | 2 1 1      | 3 3 4     |     |
Thuswithrespecttothestandardbasisof\mathbf{F}4,thematrixof\mathcal{T}
is
|     |     | 0 -1    | 0 0     |     |     |
| --- | --- | ------- | ------- | --- | --- |
|     |     | ⎛       | ⎞       |     |     |
|     |     | ⎜       | ⎟       |     |     |
|     |     | ⎜ ⎜ 1 0 | 0 0 ⎟ ⎟ |     |     |
|     |     | ⎜       | ⎟.      |     |     |
|     |     | ⎜ 2 0   | 3 0 ⎟   |     |     |
|     |     | ⎜       | ⎟       |     |     |
|     |     | ⎝ 0 0   | 1 3 ⎠   |     |     |
Youcanaskacomputertoverifythattheminimalpolynomialof\mathcal{T} isthepolynomialpdefinedby
p(z)=9-6z+10z2-6z3+z4.
| Firstconsiderthecase\mathbf{F} |     | =\mathbf{R}. Thenthepolynomialpfactorsas |     |     |     |
| --------------------- | --- | ------------------------------- | --- | --- | --- |
p(z)=(z2+1)(z-3)(z-3),
withnofurtherfactorizationofz2+1astheproductoftwopolynomialsofdegree
Thus5.44statesthattheredoesnotexistabasisof\mathbf{R}4
1withrealcoefficients.
| withrespecttowhich\mathcal{T} | hasanupper-triangularmatrix. |                                 |     |     |     |
| ------------------- | ---------------------------- | ------------------------------- | --- | --- | --- |
| Nowconsiderthecase\mathbf{F} |                              | =\mathbf{C}. Thenthepolynomialpfactorsas |     |     |     |
p(z)=(z-i)(z+i)(z-3)(z-3),
whereallfactorsabovehavetheformz-\lambda . Thus5.44statesthatthereisabasisof
k
\mathbf{C}4withrespecttowhich\mathcal{T}hasanupper-triangularmatrix. Indeed,youcanverify
thatwithrespecttothebasis(4-3i,-3-4i,-3+i,1),(4+3i,-3+4i,-3-i,1),
$$(0,0,0,1),(0,0,1,0)of\mathbf{C}4,theoperator\mathcal{T} hastheupper-triangularmatrix$$
|     |     | i 0      | 0 0     |     |     |
| --- | --- | -------- | ------- | --- | --- |
|     |     | ⎛        | ⎞       |     |     |
|     |     | ⎜ ⎜ 0 -i | 0 0 ⎟ ⎟ |     |     |
|     |     | ⎜        | ⎟       |     |     |
|     |     | ⎜ ⎜      | ⎟. ⎟    |     |     |
|     |     | ⎜ 0 0    | 3 1 ⎟   |     |     |
|     |     | 0 0      | 0 3     |     |     |
|     |     | ⎝        | ⎠       |     |     |

Section5C Upper-Triangular Matrices 159
5.44 necessaryandsufficientconditiontohaveanupper-triangularmatrix
Suppose \mathcal{V} is finite-dimensional and \mathcal{T} \in ℒ(\mathcal{V}). Then \mathcal{T} has an uppertriangularmatrixwithrespecttosomebasisof\mathcal{V} ifandonlyiftheminimal
polynomialof\mathcal{T} equals(z- \lambda )⋯(z- \lambda )forsome \lambda ,…,\lambda \in\mathbf{F}.
1 m 1 m
Proof Firstsuppose\mathcal{T} hasanupper-triangularmatrixwithrespecttosomebasis
of\mathcal{V}. Let\alpha ,…,\alpha denotethediagonalentriesofthatmatrix. Defineapolynomial
1 n
q\in𝒫(\mathbf{F})by
q(z)=(z-\alpha )⋯(z-\alpha ).
1 n
Thenq(\mathcal{T})=0,by5.40. Henceqisapolynomialmultipleoftheminimalpolynomialof\mathcal{T},by5.29. Thustheminimalpolynomialof\mathcal{T}equals(z-\lambda )⋯(z-\lambda )
1 m
forsome \lambda ,…,\lambda \in\mathbf{F} with{\lambda ,…,\lambda }\subseteq{\alpha ,…,\alpha }.
1 m 1 m 1 n
To prove the implication in the other direction, now suppose the minimal
polynomialof\mathcal{T}equals(z-\lambda )⋯(z-\lambda )forsome \lambda ,…,\lambda \in\mathbf{F}. Wewilluse
1 m 1 m
inductiononm. Togetstarted,ifm=1thenz-\lambda istheminimalpolynomialof
\mathcal{T},whichimpliesthat\mathcal{T} = \lambda \mathcal{I},whichimpliesthatthematrixof\mathcal{T} (withrespect
toanybasisof\mathcal{V})isuppertriangular.
Now suppose m > 1 and the desired result holds for all smaller positive
integers. Let
\mathcal{U} =range(\mathcal{T}- \lambda \mathcal{I}).
m
Then\mathcal{U} isinvariantunder\mathcal{T} [thisisaspecialcaseof5.18withp(z)=z- \lambda ].
m
Thus\mathcal{T}| isanoperatoron\mathcal{U}.
\mathcal{U}
Ifu\in\mathcal{U},thenu=(\mathcal{T}- \lambda \mathcal{I})vforsomev\in\mathcal{V} and
m
$$(\mathcal{T}- \lambda \mathcal{I})⋯(\mathcal{T}- \lambda \mathcal{I})u=(\mathcal{T}- \lambda \mathcal{I})⋯(\mathcal{T}- \lambda \mathcal{I})v=0.$$
1 m-1 1 m
Hence(z-\lambda )⋯(z-\lambda )isapolynomialmultipleoftheminimalpolynomial
1 m-1
of\mathcal{T}| ,by5.29. Thustheminimalpolynomialof\mathcal{T}| istheproductofatmost
\mathcal{U} \mathcal{U}
m-1termsoftheformz- \lambda .
k
Byourinductionhypothesis,thereisabasisu ,…,u of\mathcal{U} withrespectto
1 \mathcal{M}
which\mathcal{T}| hasanupper-triangularmatrix. Thusforeachk \in{1,…,\mathcal{M}},wehave
\mathcal{U}
$$(using5.39)$$
5.45 \mathcal{T}u =(\mathcal{T}| )(u )\inspan(u ,…,u ).
k \mathcal{U} k 1 k
Extendu ,…,u toabasisu ,…,u ,v ,…,v of\mathcal{V}. Ifk \in{1,…,\mathcal{N}},then
1 \mathcal{M} 1 \mathcal{M} 1 \mathcal{N}
\mathcal{T}v =(\mathcal{T}- \lambda \mathcal{I})v + \lambda v .
k m k m k
Thedefinitionof\mathcal{U} showsthat(\mathcal{T}- \lambda \mathcal{I})v \in\mathcal{U} =span(u ,…,u ). Thusthe
m k 1 \mathcal{M}
equationaboveshowsthat
5.46 \mathcal{T}v \inspan(u ,…,u ,v ,…,v ).
k 1 \mathcal{M} 1 k
From5.45and5.46,weconclude(using5.39)that\mathcal{T} hasanupper-triangular
matrixwithrespecttothebasisu ,…,u ,v ,…,v of\mathcal{V},asdesired.
1 \mathcal{M} 1 \mathcal{N}

160 Chapter 5 Eigenvaluesand Eigenvectors
The set of numbers {\lambda ,…,\lambda } from the previous result equals the set of
1 m
eigenvaluesof\mathcal{T} (becausethesetofzerosoftheminimalpolynomialof\mathcal{T} equals
thesetofeigenvaluesof\mathcal{T},by5.27),althoughthelist \lambda ,…,\lambda intheprevious
1 m
resultmaycontainrepetitions.
In Chapter 8wewillimproveeventhewonderfulresultbelow;see8.37and
8.46.
5.47 if \mathbf{F} =\mathbf{C},theneveryoperatoron\mathcal{V} hasanupper-triangularmatrix
Suppose\mathcal{V}isafinite-dimensionalcomplexvectorspaceand\mathcal{T} \inℒ(\mathcal{V}). Then
\mathcal{T} hasanupper-triangularmatrixwithrespecttosomebasisof\mathcal{V}.
Proof Thedesiredresultfollowsimmediatelyfrom5.44andthesecondversion
ofthefundamentaltheoremofalgebra(see4.13).
Foranextensionoftheresultabovetotwooperators\mathcal{S}and\mathcal{T} suchthat
\mathcal{S}\mathcal{T} =\mathcal{T}\mathcal{S},
see5.80. Also,foranextensiontomorethantwooperators,see Exercise9(b)in
Section5E.
Caution: Ifanoperator\mathcal{T} \inℒ(\mathcal{V})hasanupper-triangularmatrixwithrespect
tosomebasisv ,…,v of\mathcal{V},thentheeigenvaluesof\mathcal{T} areexactlytheentrieson
1 n
thediagonalofℳ(\mathcal{T}),asshownby5.41,andfurthermorev isaneigenvectorof
\mathcal{T}. However,v ,…,v neednotbeeigenvectorsof\mathcal{T}. Indeed,abasisvectorv is
2 n k
aneigenvectorof\mathcal{T} ifandonlyifallentriesinthekth columnofthematrixof\mathcal{T}
are0,exceptpossiblythekth entry.
You may recall from a previous
The row echelon form of the matrix
coursethateverymatrixofnumberscan
ofanoperatordoesnotgiveusalist
bechangedtoamatrixinwhatiscalled
oftheeigenvaluesoftheoperator. In
rowechelonform. Ifonebeginswitha contrast, an upper-triangular matrix
squarematrix,thematrixinrowechelon withrespecttosomebasisgivesusa
formwillbeanupper-triangularmatrix. list of all the eigenvalues of the opDonotconfusethisupper-triangularma- erator. However, there is no method
trixwiththeupper-triangularmatrixof forcomputingexactlysuchanupperan operator with respect to some basis triangular matrix, even though 5.47
whoseexistenceisproclaimedby5.47(if guaranteesitsexistenceif \mathbf{F} =\mathbf{C}.
\mathbf{F} =\mathbf{C})—thereisnoconnectionbetween
theseupper-triangularmatrices.
Exercises 5C
1 Proveorgiveacounterexample: If\mathcal{T} \inℒ(\mathcal{V})and\mathcal{T}2hasanupper-triangular
matrixwithrespecttosomebasisof\mathcal{V},then\mathcal{T}hasanupper-triangularmatrix
withrespecttosomebasisof\mathcal{V}.

Section5C Upper-Triangular Matrices
2 Suppose \mathcal{A} and \mathcal{B} are upper-triangular matrices of the same size, with
| \alpha ,…,\alpha                                     | onthediagonalof\mathcal{A}and\beta | ,…,\beta onthediagonalof\mathcal{B}. |         |     |
| ------------------------------------------ | -------------------- | ---------------------- | ------- | --- |
| 1                                          | n                    | 1 n                    |         |     |
| Showthat\mathcal{A}+\mathcal{B}isanupper-triangularmatrixwith\alpha |                      |                        | +\beta ,…,\alpha | +\beta  |
$$(a)$$
|     |     |     | 1 1 | n n |
| --- | --- | --- | --- | --- |
onthediagonal.
| (b) Showthat\mathcal{A}\mathcal{B}isanupper-triangularmatrixwith\alpha |     |     | \beta ,…,\alpha | \beta onthe |
| --------------------------------------------- | --- | --- | ------ | ------- |
|                                               |     |     | 1 1    | n n     |
diagonal.
Theresultsinthisexerciseareusedintheproofof5.81.
3 Suppose\mathcal{T} \inℒ(\mathcal{V})isinvertibleandv ,…,v isabasisof\mathcal{V} withrespect
1 n
towhichthematrixof\mathcal{T} isuppertriangular,with \lambda ,…,\lambda onthediagonal.
1 n
Showthatthematrixof\mathcal{T}-1isalsouppertriangularwithrespecttothebasis
| v ,…,v | ,with |     |     |     |
| ------ | ----- | --- | --- | --- |
| 1      | n     |     |     |     |
1 1
,…,
\lambda \lambda
1 n
onthediagonal.
4 Giveanexampleofanoperatorwhosematrixwithrespecttosomebasis
containsonly0’sonthediagonal,buttheoperatorisinvertible.
Thisexerciseandtheexercisebelowshowthat5.41failswithoutthehypothesisthatanupper-triangularmatrixisunderconsideration.
5 Giveanexampleofanoperatorwhosematrixwithrespecttosomebasis
contains only nonzero numbers on the diagonal, but the operator is not
invertible.
ℒ(\mathcal{V}).
6 Suppose \mathbf{F} = \mathbf{C}, \mathcal{V} is finite-dimensional, and \mathcal{T} \in Prove that if
k \in{1,…,dim\mathcal{V}},then\mathcal{V} hasak-dimensionalsubspaceinvariantunder\mathcal{T}.
| 7 Suppose\mathcal{V} | isfinite-dimensional,\mathcal{T} | \inℒ(\mathcal{V}),andv\in\mathcal{V}. |     |     |
| ---------- | ---------------------- | ------------- | --- | --- |
$$(a) Provethatthereexistsauniquemonicpolynomialp ofsmallestdegree$$
v
| suchthatp | (\mathcal{T})v=0. |     |     |     |
| --------- | ------- | --- | --- | --- |
v
$$(b) Provethattheminimalpolynomialof\mathcal{T} isapolynomialmultipleofp .$$
v
8 Suppose \mathcal{V} is finite-dimensional, \mathcal{T} \in ℒ(\mathcal{V}), and there exists a nonzero
| vectorv\in\mathcal{V} | suchthat\mathcal{T}2v+2\mathcal{T}v=-2v. |     |     |     |
| --------- | -------------------- | --- | --- | --- |
$$(a) Provethatif\mathbf{F} =\mathbf{R},thentheredoesnotexistabasisof\mathcal{V} withrespect$$
| towhich\mathcal{T} | hasanupper-triangularmatrix. |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
$$(b) Prove that if and is an upper-triangular matrix that equals$$
|              | \mathbf{F} = \mathbf{C} \mathcal{A}                                  |     |     |     |
| ------------ | ---------------------------------------- | --- | --- | --- |
| thematrixof\mathcal{T} | withrespecttosomebasisof\mathcal{V},then-1+ior-1-i |     |     |     |
appearsonthediagonalof\mathcal{A}.
9 Suppose\mathcal{B}isasquarematrixwithcomplexentries. Provethatthereexists
aninvertiblesquarematrix\mathcal{A}withcomplexentriessuchthat\mathcal{A}-1\mathcal{B}\mathcal{A}isan
upper-triangularmatrix.

| -------- | --- | -------------------------- | --- | --- | --- |
| 10 Suppose\mathcal{T} | \inℒ(\mathcal{V})andv |     | ,…,v | isabasisof\mathcal{V}. | Showthatthefollowing |
| ----------- | --------- | --- | ---- | ------------ | -------------------- |
|             |           |     | 1 n  |              |                      |
areequivalent.
| (a) Thematrixof\mathcal{T} |     | withrespecttov |     | ,…,v | islowertriangular. |
| ---------------- | --- | -------------- | --- | ---- | ------------------ |
1 n
|            | ,…,v |                    |     |          | =1,…,n. |
| ---------- | ---- | ------------------ | --- | -------- | ------- |
| (b) span(v |      | )isinvariantunder\mathcal{T} |     | foreachk |         |
k n
| (c) \mathcal{T}v | \inspan(v | ,…,v | )foreachk | =1,…,n. |     |
| ------ | ------- | ---- | --------- | ------- | --- |
|        | k       | k    | n         |         |     |
Asquarematrixiscalledlowertriangularifallentriesabovethediagonal
are0.
\inℒ(\mathcal{V}),then
| 11 Suppose\mathbf{F} | =\mathbf{C}  | and\mathcal{V} | isfinite-dimensional. | Provethatif\mathcal{T} |     |
| ----------- | --- | ---- | --------------------- | ------------ | --- |
there exists a basis of \mathcal{V} with respect to which \mathcal{T} has a lower-triangular
matrix.
12 Suppose\mathcal{V} isfinite-dimensional,\mathcal{T} \inℒ(\mathcal{V})hasanupper-triangularmatrix
withrespecttosomebasisof\mathcal{V},and\mathcal{U} isasubspaceof\mathcal{V} thatisinvariant
under\mathcal{T}.
$$(a) Provethat\mathcal{T}| hasanupper-triangularmatrixwithrespecttosomebasis$$
\mathcal{U}
of\mathcal{U}.
$$(b) Prove that the quotient operator has an upper-triangular matrix$$
\mathcal{T}/\mathcal{U}
withrespecttosomebasisof\mathcal{V}/\mathcal{U}.
Thequotientoperator\mathcal{T}/\mathcal{U}wasdefinedin Exercise38in Section5A.
13 Suppose \mathcal{V} is finite-dimensional and \mathcal{T} \in ℒ(\mathcal{V}). Suppose there exists
a subspace \mathcal{U} of \mathcal{V} that is invariant under \mathcal{T} such that \mathcal{T}| has an upper\mathcal{U}
triangular matrix with respect to some basis of \mathcal{U} and also \mathcal{T}/\mathcal{U} has an
upper-triangularmatrixwithrespecttosomebasisof\mathcal{V}/\mathcal{U}. Provethat\mathcal{T}has
anupper-triangularmatrixwithrespecttosomebasisof\mathcal{V}.
14 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Provethat\mathcal{T} hasanuppertriangular matrix with respect to some basis of \mathcal{V} if and only if the dual
operator\mathcal{T}′ hasanupper-triangularmatrixwithrespecttosomebasisofthe
dualspace\mathcal{V}′.

| --- | --- | --------- | ----------------------- | --- | --- |
| 5D Diagonalizable |          | Operators |     |     |     |
| ----------------- | -------- | --------- | --- | --- | --- |
| Diagonal          | Matrices |           |     |     |     |
diagonalmatrix
**5.48 定义：** Adiagonalmatrixisasquarematrixthatis0everywhereexceptpossiblyon
thediagonal.
| 5.49 example: | diagonalmatrix |       |         |     |     |
| ------------- | -------------- | ----- | ------- | --- | --- |
|               |                | 8     | 0 0     |     |     |
|               |                | ⎛     | ⎞       |     |     |
|               |                | ⎜     | ⎟       |     |     |
|               |                | ⎜ ⎜ 0 | 5 0 ⎟ ⎟ |     |     |
|               |                | 0     | 0 5     |     |     |
|               |                | ⎝     | ⎠       |     |     |
isadiagonalmatrix.
Ifanoperatorhasadiagonalmatrix
|     |     |     | Every diagonal | matrix is upper | tri- |
| --- | --- | --- | -------------- | --------------- | ---- |
withrespecttosomebasis,thentheen- angular. Diagonalmatricestypically
| tries on | the diagonal | are precisely the |     |     |     |
| -------- | ------------ | ----------------- | --- | --- | --- |
havemanymore0’sthanmostuppereigenvaluesoftheoperator;thisfollows triangularmatricesofthesamesize.
from5.41(orfindaneasierdirectproof
fordiagonalmatrices).
diagonalizable
**5.50 定义：** Anoperatoron\mathcal{V}iscalleddiagonalizableiftheoperatorhasadiagonalmatrix
withrespecttosomebasisof\mathcal{V}.
| 5.51 example: | diagonalizationmayrequireadifferentbasis |     |     |     |     |
| ------------- | ---------------------------------------- | --- | --- | --- | --- |
\inℒ(\mathbf{R}2)by
Define\mathcal{T}
\mathcal{T}(x,y)=(41x+7y,-20x+74y).
| Thematrixof\mathcal{T} | withrespecttothestandardbasisof\mathbf{R}2 |     |     | is  |     |
| ------------ | --------------------------------- | --- | --- | --- | --- |
|              |                                   | (   | ),  |     |     |
|              |                                   | -20 | 74  |     |     |
whichisnotadiagonalmatrix. However,\mathcal{T} isdiagonalizable. Specifically,the
| matrixof\mathcal{T} | withrespecttothebasis(1,4),(7,5)is |     |     |     |     |
| --------- | ---------------------------------- | --- | --- | --- | --- |
|           |                                    | (   | )   |     |     |
0 46
because\mathcal{T}(1,4)=(69,276)=69(1,4)and\mathcal{T}(7,5)=(322,230)=46(7,5).

| -------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
For \lambda\in\mathbf{F},wewillfinditconvenienttohaveanameandanotationfortheset
| ofvectorsthatanoperator\mathcal{T} |     |                   | mapsto |     | \lambdatimesthevector. |     |     |     |
| ------------------------ | --- | ----------------- | ------ | --- | ---------------- | --- | --- | --- |
| 5.52 definition:         |     | eigenspace,\mathcal{E}(\lambda,\mathcal{T}) |        |     |                  |     |     |     |
Suppose\mathcal{T} \in ℒ(\mathcal{V})and \lambda \in \mathbf{F}. Theeigenspaceof\mathcal{T} correspondingto \lambdais
| thesubspace\mathcal{E}(\lambda,\mathcal{T})of\mathcal{V} |     |                | definedby |          |     |      |      |     |
| -------------------- | --- | -------------- | --------- | -------- | --- | ---- | ---- | --- |
|                      |     | \mathcal{E}(\lambda,\mathcal{T})=null(\mathcal{T}- |           | \lambda\mathcal{I})={v\in\mathcal{V} |     | ∶\mathcal{T}v= | \lambdav}. |     |
Hence\mathcal{E}(\lambda,\mathcal{T})isthesetofalleigenvectorsof\mathcal{T} correspondingto \lambda,along
withthe0vector.
| For\mathcal{T} | \inℒ(\mathcal{V})and |     | \lambda\in\mathbf{F},theset\mathcal{E}(\lambda,\mathcal{T})isasubspaceof\mathcal{V} |     |     |     |     | becausethenull |
| ---- | -------- | --- | ------------------------------ | --- | --- | --- | --- | -------------- |
spaceofeachlinearmapon\mathcal{V} isasubspaceof\mathcal{V}. Thedefinitionsimplythat \lambdais
| aneigenvalueof\mathcal{T} |     | ifandonlyif\mathcal{E}(\lambda,\mathcal{T})\neq{0}. |     |     |     |     |     |     |
| --------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
eigenspacesofanoperator
**5.53 例：** Supposethematrixofanoperator\mathcal{T} \inℒ(\mathcal{V})withrespecttoabasisv ,v ,v
1 2 3
| of\mathcal{V} isthematrixin Example5.49. |     |               |     | Then |               |     |       |     |
| ----------------------------- | --- | ------------- | --- | ---- | ------------- | --- | ----- | --- |
|                               |     | \mathcal{E}(8,\mathcal{T})=span(v |     | ),   | \mathcal{E}(5,\mathcal{T})=span(v |     | ,v ). |     |
|                               |     |               |     | 1    |               |     | 2 3   |     |
If \lambdaisaneigenvalueofanoperator\mathcal{T} \inℒ(\mathcal{V}),then\mathcal{T} restrictedto\mathcal{E}(\lambda,\mathcal{T})is
| justtheoperatorofmultiplicationby |     |     |     |     | \lambda.  |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
5.54 sumofeigenspacesisadirectsum
| Suppose\mathcal{T}            | \inℒ(\mathcal{V})and |                 | \lambda ,…,\lambda       | aredistincteigenvaluesof\mathcal{T}. |                         |           |     | Then |
| ------------------- | -------- | --------------- | ------------ | -------------------------- | ----------------------- | --------- | --- | ---- |
|                     |          |                 | 1            | m                          |                         |           |     |      |
|                     |          |                 | \mathcal{E}(\lambda          | ,\mathcal{T})+⋯+\mathcal{E}(\lambda                  |                         | ,\mathcal{T})       |     |      |
|                     |          |                 |              | 1                          |                         | m         |     |      |
| isadirectsum.       |          | Furthermore,if\mathcal{V} |              | isfinite-dimensional,then  |                         |           |     |      |
|                     |          | dim\mathcal{E}(\lambda          | ,\mathcal{T})+⋯+dim\mathcal{E}(\lambda |                            |                         | ,\mathcal{T})\leqdim\mathcal{V}. |     |      |
|                     |          |                 | 1            |                            |                         | m         |     |      |
| Proof Toshowthat\mathcal{E}(\lambda |          |                 | ,\mathcal{T})+⋯+\mathcal{E}(\lambda    |                            | ,\mathcal{T})isadirectsum,suppose |           |     |      |
|                     |          |                 | 1            |                            | m                       |           |     |      |
|                     |          |                 |              | v +⋯+v                     | =0,                     |           |     |      |
|                     |          |                 |              | 1                          | m                       |           |     |      |
where each v is in \mathcal{E}(\lambda ,\mathcal{T}). Because eigenvectors corresponding to distinct
|     | k   |     | k   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
eigenvaluesarelinearlyindependent(by5.11),thisimpliesthateachv equals0.
k
| Thus\mathcal{E}(\lambda     | ,\mathcal{T})+⋯+\mathcal{E}(\lambda    |                       | ,\mathcal{T})isadirectsum(by1.45),asdesired. |             |      |           |     |      |
| ----------- | ------------ | --------------------- | ---------------------------------- | ----------- | ---- | --------- | --- | ---- |
|             | 1            |                       | m                                  |             |      |           |     |      |
| Nowsuppose\mathcal{V} |              | isfinite-dimensional. |                                    |             | Then |           |     |      |
|             | ,\mathcal{T})+⋯+dim\mathcal{E}(\lambda |                       |                                    | ,\mathcal{T})=dim(\mathcal{E}(\lambda |      | ,\mathcal{T})\oplus⋯\oplus\mathcal{E}(\lambda |     | ,\mathcal{T})) |
dim\mathcal{E}(\lambda
|     | 1   |     |     | m   |     | 1   |     | m   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
\leqdim\mathcal{V},
wherethefirstlinefollowsfrom3.94andthesecondlinefollowsfrom2.37.

| --- | --- | --- | --- | --------- | --- | ----------------------- | --- | --- |
| Conditions |     | for | Diagonalizability |     |     |     |     |     |
| ---------- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
Thefollowingcharacterizationsofdiagonalizableoperatorswillbeuseful.
conditionsequivalenttodiagonalizability
5.55
Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \in ℒ(\mathcal{V}). Let \lambda ,…,\lambda denotethe
1 m
| distincteigenvaluesof\mathcal{T}. |     |     |     | Thenthefollowingareequivalent. |     |     |     |     |
| ----------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
$$(a) \mathcal{T} isdiagonalizable.$$
$$(b) \mathcal{V} hasabasisconsistingofeigenvectorsof\mathcal{T}.$$
| (c)   | \mathcal{V} =\mathcal{E}(\lambda      | ,\mathcal{T})\oplus⋯\oplus\mathcal{E}(\lambda |                         |              | ,\mathcal{T}). |      |     |     |
| ----- | ----------- | --------- | ----------------------- | ------------ | ---- | ---- | --- | --- |
|       |             | 1         |                         | m            |      |      |     |     |
| (d)   | dim\mathcal{V}        | =dim\mathcal{E}(\lambda   |                         | ,\mathcal{T})+⋯+dim\mathcal{E}(\lambda |      | ,\mathcal{T}). |     |     |
|       |             |           | 1                       |              |      | m    |     |     |
| Proof | Anoperator\mathcal{T} |           | \inℒ(\mathcal{V})hasadiagonalmatrix |              |      |      |     |     |
|       |             |           |                         |              | \lambda    | 0    |     |     |
|       |             |           |                         | ⎛ ⎜          | 1    | ⎞ ⎟  |     |     |
|       |             |           |                         | ⎜            |      | ⋱ ⎟  |     |     |
|       |             |           |                         | ⎜            |      | ⎟    |     |     |
|       |             |           |                         | ⎝            | 0    | \lambda ⎠  |     |     |
n
withrespecttoabasisv ,…,v of\mathcal{V} ifandonlyif\mathcal{T}v = \lambda v foreachk. Thus
|     |     |     | 1   | n   |     |     | k k k |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- |
$$(a)and(b)areequivalent.$$
Suppose(b)holds;thus\mathcal{V} hasabasisconsistingofeigenvectorsof\mathcal{T}. Hence
everyvectorin\mathcal{V} isalinearcombinationofeigenvectorsof\mathcal{T},whichimpliesthat
|     |     |     |     | \mathcal{V} =\mathcal{E}(\lambda | ,\mathcal{T})+⋯+\mathcal{E}(\lambda | ,\mathcal{T}). |     |     |
| --- | --- | --- | --- | ------ | --------- | ---- | --- | --- |
|     |     |     |     |        | 1         | m    |     |     |
Now5.54showsthat(c)holds,provingthat(b)implies(c).
That(c)implies(d)followsimmediatelyfrom3.94.
Finally,suppose(d)holds;thus
| 5.56                  |     |     | dim\mathcal{V} | =dim\mathcal{E}(\lambda                                  | ,\mathcal{T})+⋯+dim\mathcal{E}(\lambda |     | ,\mathcal{T}). |      |
| --------------------- | --- | --- | ---- | ---------------------------------------- | ------------ | --- | ---- | ---- |
|                       |     |     |      |                                          | 1            |     | m    |      |
|                       |     |     |      | ,\mathcal{T});putallthesebasestogethertoformalistv |              |     |      | ,…,v |
| Chooseabasisofeach\mathcal{E}(\lambda |     |     |      | k                                        |              |     |      | 1 n  |
ofeigenvectorsof\mathcal{T},wheren=dim\mathcal{V} (by5.56). Toshowthatthislistislinearly
independent,suppose
|     |     |     |     | a v | +⋯+a | v =0, |     |     |
| --- | --- | --- | --- | --- | ---- | ----- | --- | --- |
|     |     |     |     | 1   | 1    | n n   |     |     |
wherea ,…,a \in\mathbf{F}. Foreachk =1,…,m,letu denotethesumofalltheterms
|     | 1         | n    |      |           |      | k               |     |     |
| --- | --------- | ---- | ---- | --------- | ---- | --------------- | --- | --- |
| av  | suchthatv | \in\mathcal{E}(\lambda | ,\mathcal{T}). | Thuseachu |      | isin\mathcal{E}(\lambda ,\mathcal{T}),and |     |     |
| j   | j         | j    | k    |           |      | k k             |     |     |
|     |           |      |      | u         | +⋯+u | =0.             |     |     |
|     |           |      |      |           | 1    | m               |     |     |
Becauseeigenvectorscorrespondingtodistincteigenvaluesarelinearlyindependent(see5.11),thisimpliesthateachu equals0. Becauseeachu isasumof
|     |     |     |     |     |     | k   | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
termsav,wherethev’swerechosentobeabasisof\mathcal{E}(\lambda ,\mathcal{T}),thisimpliesthat
|     | j j |     | j   |     |     |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
alla’sequal0. Thusv ,…,v islinearlyindependentandhenceisabasisof\mathcal{V}
|           | j   |                                       | 1   | n   |     |     |     |     |
| --------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
| (by2.38). |     | Thus(d)implies(b),completingtheproof. |     |     |     |     |     |     |
Foradditionalconditionsequivalenttodiagonalizability,see5.62,Exercises5
and15inthissection,Exercise24in Section7B,and Exercise15in Section8A.

166 Chapter 5 Eigenvaluesand Eigenvectors
Asweknow,everyoperatoronanonzerofinite-dimensionalcomplexvector
space has an eigenvalue. However, not every operator on a nonzero finitedimensionalcomplexvectorspacehasenougheigenvectorstobediagonalizable,
asshownbythenextexample.
**5.57 例：** anoperatorthatisnotdiagonalizable
Defineanoperator\mathcal{T} \inℒ(\mathbf{F}3)by\mathcal{T}(a,b,c)=(b,c,0). Thematrixof\mathcal{T} with
respecttothestandardbasisof\mathbf{F}3 is
0 1 0
⎛ ⎞
⎜ ⎟
⎜ ⎜ 0 0 1 ⎟ ⎟ ,
⎝ 0 0 0 ⎠
whichisanupper-triangularmatrixbutisnotadiagonalmatrix.
Asyoushouldverify,0istheonlyeigenvalueof\mathcal{T} andfurthermore
\mathcal{E}(0,\mathcal{T})={(a,0,0)\in\mathbf{F}3 ∶a\in\mathbf{F}}.
Henceconditions(b),(c),and(d)of5.55fail(ofcourse,becausetheseconditions
areequivalent,itissufficienttocheckthatonlyoneofthemfails). Thuscondition
$$(a)of5.55alsofails. Hence\mathcal{T} isnotdiagonalizable,regardlessofwhether\mathbf{F} =\mathbf{R}$$
or\mathbf{F} =\mathbf{C}.
Thenextresultshowsthatifanoperatorhasasmanydistincteigenvaluesas
thedimensionofitsdomain,thentheoperatorisdiagonalizable.
5.58 enougheigenvaluesimpliesdiagonalizability
Suppose\mathcal{V}isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V})hasdim\mathcal{V}distincteigenvalues.
Then\mathcal{T} isdiagonalizable.
Proof Suppose\mathcal{T} hasdistincteigenvalues \lambda ,…,\lambda . Foreachk,letv \in\mathcal{V}
1 dim\mathcal{V} k
beaneigenvectorcorrespondingtotheeigenvalue\lambda . Becauseeigenvectorscorrek
spondingtodistincteigenvaluesarelinearlyindependent(see5.11),v ,…,v
1 dim\mathcal{V}
islinearlyindependent.
Alinearlyindependentlistofdim\mathcal{V}vectorsin\mathcal{V}isabasisof\mathcal{V}(see2.38);thus
v ,…,v isabasisof\mathcal{V}. Withrespecttothisbasisconsistingofeigenvectors,
1 dim\mathcal{V}
\mathcal{T} hasadiagonalmatrix.
In later chapters we will find additional conditions that imply that certain
operatorsarediagonalizable. Forexample,seetherealspectraltheorem(7.29)
andthecomplexspectraltheorem(7.31).
Theresultabovegivesasufficientconditionforanoperatortobediagonalizable. However, this condition is not necessary. For example, the operator \mathcal{T}
on\mathbf{F}3 definedby\mathcal{T}(x,y,z)=(6x,6y,7z)hasonlytwoeigenvalues(6and7)and
dim\mathbf{F}3 =3,but\mathcal{T} isdiagonalizable(bythestandardbasisof\mathbf{F}3).

| --- | --- | --- | --------- | --- | ----------------------- | --- | --- |
| The | next example | illustrates |     | the im- |     |     |     |
| --- | ------------ | ----------- | --- | ------- | --- | --- | --- |
Foraspectacularapplicationofthese
| portance | of diagonalization, |     | which | can |             |              |           |
| -------- | ------------------- | --- | ----- | --- | ----------- | ------------ | --------- |
|          |                     |     |       |     | techniques, | see Exercise | 21, which |
be used to compute high powers of an shows how to use diagonalization to
operator, taking advantage of the equa- findanexactformulaforthenthterm
| tion\mathcal{T}kv          | \lambdakvifvisaneigenvectorof |     |     |     |                         |     |     |
| ---------------- | ----------------------- | --- | --- | --- | ----------------------- | --- | --- |
|                  | =                       |     |     |     | ofthe Fibonaccisequence. |     |     |
| \mathcal{T} witheigenvalue |                         | \lambda.  |     |     |                         |     |     |
usingdiagonalizationtocompute\mathcal{T}100
**5.59 例：** Define\mathcal{T} \in ℒ(\mathbf{F}3)by\mathcal{T}(x,y,z) = (2x+y,5y+3z,8z). Withrespecttothe
| standardbasis,thematrixof\mathcal{T} |     |     | is  |         |          |     |     |
| -------------------------- | --- | --- | --- | ------- | -------- | --- | --- |
|                            |     |     |     | 2 1     | 0        |     |     |
|                            |     |     |     | ⎛       | ⎞        |     |     |
|                            |     |     |     | ⎜ ⎜ 0 5 | 3 ⎟ ⎟ ⎟. |     |     |
⎜
|     |     |     |     | ⎝ 0 0 | 8 ⎠ |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- |
Thematrixaboveisanupper-triangularmatrixbutitisnotadiagonalmatrix. By
5.41,theeigenvaluesof\mathcal{T} are2,5,and8. Because\mathcal{T} isanoperatoronavector
spaceofdimensionthreeand\mathcal{T} hasthreedistincteigenvalues,5.58assuresus
thatthereexistsabasisof\mathbf{F}3
|     |     |     | withrespecttowhich\mathcal{T} |     | hasadiagonalmatrix. |     |     |
| --- | --- | --- | ------------------- | --- | ------------------- | --- | --- |
Tofindthisbasis,weonlyhavetofindaneigenvectorforeacheigenvalue. In
otherwords,wehavetofindanonzerosolutiontotheequation
|     |     |     | \mathcal{T}(x,y,z)= |     | \lambda(x,y,z) |     |     |
| --- | --- | --- | --------- | --- | -------- | --- | --- |
for \lambda = 2,thenfor \lambda = 5,andthenfor \lambda = 8. Solvingthesesimpleequations
shows that for we have an eigenvector (1,0,0), for we have an
|                           | \lambda   | = 2 |                                |     |     | \lambda = 5 |     |
| ------------------------- | --- | --- | ------------------------------ | --- | --- | ----- | --- |
| eigenvector(1,3,0),andfor |     |     | \lambda=8wehaveaneigenvector(1,6,6). |     |     |       |     |
Thus(1,0,0),(1,3,0),(1,6,6)isabasisof\mathbf{F}3consistingofeigenvectorsof\mathcal{T},
| andwithrespecttothisbasisthematrixof\mathcal{T} |     |     |     |         | isthediagonalmatrix |     |     |
| ------------------------------------- | --- | --- | --- | ------- | ------------------- | --- | --- |
|                                       |     |     |     | 2 0     | 0                   |     |     |
|                                       |     |     |     | ⎛       | ⎞                   |     |     |
|                                       |     |     |     | ⎜       | ⎟                   |     |     |
|                                       |     |     |     | ⎜ ⎜ 0 5 | 0 ⎟ ⎟.              |     |     |
|                                       |     |     |     | 0 0     | 8                   |     |     |
|                                       |     |     |     | ⎝       | ⎠                   |     |     |
Tocompute\mathcal{T}100(0,0,1),forexample,write(0,0,1)asalinearcombination
ofourbasisofeigenvectors:
|              |     | (0,0,1)=                              | 1(1,0,0)- | 1(1,3,0)+       | 1(1,6,6). |                |     |
| ------------ | --- | ------------------------------------- | --------- | --------------- | --------- | -------------- | --- |
| Nowapply\mathcal{T}100 |     | tobothsidesoftheequationabove,getting |           |                 |           |                |     |
| \mathcal{T}100(0,0,1)= |     | 1(\mathcal{T}100(1,0,0))-                       |           | 1(\mathcal{T}100(1,3,0))+ |           | 1(\mathcal{T}100(1,6,6)) |     |
= 1(2100(1,0,0)-2\cdot5100(1,3,0)+8100(1,6,6))
|     |     | = 1(2100-2\cdot5100+8100, |     |     | 6\cdot8100-6\cdot5100, | 6\cdot8100). |     |
| --- | --- | --------------------- | --- | --- | -------------- | -------- | --- |

| -------- | -------------------------- | --- | --- | --- | --- |
Wesawearlierthatanoperator\mathcal{T}onafinite-dimensionalvectorspace\mathcal{V}hasan
upper-triangularmatrixwithrespecttosomebasisof\mathcal{V} ifandonlyiftheminimal
polynomialof\mathcal{T} equals(z- \lambda )⋯(z- \lambda )forsome \lambda ,…,\lambda \in\mathbf{F} (see5.44).
|     |     | 1   | m   | 1   | m   |
| --- | --- | --- | --- | --- | --- |
Aswepreviouslynoted(see5.47),thisconditionisalwayssatisfiedif\mathbf{F} =\mathbf{C}.
Ournextresult5.62statesthatanoperator\mathcal{T} \inℒ(\mathcal{V})hasadiagonalmatrix
withrespecttosomebasisof\mathcal{V} ifandonlyiftheminimalpolynomialof\mathcal{T} equals
$$(z- \lambda )⋯(z- \lambda )forsomedistinct \lambda ,…,\lambda \in \mathbf{F}. Beforeformallystating$$
| 1   | m   |     | 1   | m   |     |
| --- | --- | --- | --- | --- | --- |
thisresult,wegivetwoexamplesofusingit.
diagonalizable,butwithnoknownexacteigenvalues
**5.60 例：** | Define\mathcal{T} | \inℒ(\mathbf{C}5)by  |              |        |       |       |
| ------- | --------- | ------------ | ------ | ----- | ----- |
|         | \mathcal{T}(z ,z ,z | ,z ,z )=(-3z | ,z +6z | ,z ,z | ,z ). |
|         | 1 2       | 3 4 5        | 5 1    | 5 2   | 3 4   |
Thematrixof\mathcal{T} isshownin Example5.26,whereweshowedthattheminimal
is3-6z+z5.
polynomialof\mathcal{T}
Asmentionedin Example5.28,noexactexpressionisknownforanyofthe
zerosofthispolynomial,butnumericaltechniquesshowthatthezerosofthis
polynomialareapproximately-1.67, 0.51, 1.40, -0.12+1.59i, -0.12-1.59i.
The software that produces these approximations is accurate to more than
threedigits. Thustheseapproximationsaregoodenoughtoshowthatthefive
numbersabovearedistinct. Theminimalpolynomialof\mathcal{T} equalsthefifthdegree
monicpolynomialwiththesezeros. Now5.62showsthat\mathcal{T} isdiagonalizable.
showingthatanoperatorisnotdiagonalizable
**5.61 例：** | Define\mathcal{T}      | \inℒ(\mathbf{F}3)by                          |           |         |     |        |
| ------------ | --------------------------------- | --------- | ------- | --- | ------ |
|              | ,z ,z                             | +3z       | +4z ,6z | +2z | ,7z    |
|              | \mathcal{T}(z 1 2                           | 3 )=(6z 1 | 2 3     | 2   | 3 3 ). |
| Thematrixof\mathcal{T} | withrespecttothestandardbasisof\mathbf{F}3 |           |         | is  |        |
|              |                                   | 6 3       | 4       |     |        |
|              |                                   | ⎛         | ⎞       |     |        |
|              |                                   | ⎜         | ⎟       |     |        |
|              |                                   | ⎜ ⎜ 0 6   | 2 ⎟ ⎟.  |     |        |
|              |                                   | 0 0       | 7       |     |        |
|              |                                   | ⎝         | ⎠       |     |        |
Thematrixaboveisanupper-triangularmatrixbutisnotadiagonalmatrix. Might
\mathcal{T} haveadiagonalmatrixwithrespecttosomeotherbasisof\mathbf{F}3?
Toanswerthisquestion,wewillfindtheminimalpolynomialof\mathcal{T}. Firstnote
thattheeigenvaluesof\mathcal{T} arethediagonalentriesofthematrixabove(by5.41).
Thusthezerosoftheminimalpolynomialof\mathcal{T}are6,7[by5.27(a)]. Thediagonal
ofthematrixabovetellsusthat(\mathcal{T}-6\mathcal{I})2(\mathcal{T}-7\mathcal{I})=0(by5.40). Theminimal
polynomialof\mathcal{T} hasdegreeatmost3(by5.22). Puttingallthistogether,wesee
| thattheminimalpolynomialof\mathcal{T}             |                | iseither(z-6)(z-7)or(z-6)2(z-7). |     |     |                   |
| --------------------------------------- | -------------- | -------------------------------- | --- | --- | ----------------- |
| Asimplecomputationshowsthat(\mathcal{T}-6\mathcal{I})(\mathcal{T}-7\mathcal{I}) |                |                                  |     | \neq   | 0. Thustheminimal |
| polynomialof\mathcal{T}                           | is(z-6)2(z-7). |                                  |     |     |                   |
| Now5.62showsthat\mathcal{T}                       |                | isnotdiagonalizable.             |     |     |                   |

| --- | --- | --- | --- | --------- | ----------------------- | --- | --- | --- |
necessaryandsufficientconditionfordiagonalizability
5.62
Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Then\mathcal{T} isdiagonalizableif
| andonlyiftheminimalpolynomialof\mathcal{T}equals(z-\lambda |     |     |        |     |     |     | )⋯(z-\lambda | )forsome |
| ------------------------------------------ | --- | --- | ------ | --- | --- | --- | ------ | -------- |
|                                            |     |     |        |     |     |     | 1      | m        |
| listofdistinctnumbers                      |     |     | \lambda ,…,\lambda | \in\mathbf{F}. |     |     |        |          |
|                                            |     |     | 1      | m   |     |     |        |          |
Proof Firstsuppose\mathcal{T} isdiagonalizable. Thusthereisabasisv ,…,v of\mathcal{V}
|     |     |     |     |     |     |     |     | 1 n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
consistingofeigenvectorsof\mathcal{T}. Let \lambda ,…,\lambda bethedistincteigenvaluesof\mathcal{T}.
|                          |     |     |       |         | 1 m   |         |      |     |
| ------------------------ | --- | --- | ----- | ------- | ----- | ------- | ---- | --- |
| Thenforeachv,thereexists |     |     | \lambda     | with(\mathcal{T}- | \lambda \mathcal{I})v | =0.     | Thus |     |
|                          | j   |     | k     |         | k     | j       |      |     |
|                          |     |     | (\mathcal{T}- \lambda | \mathcal{I})⋯(\mathcal{T}-  | \lambda     | \mathcal{I})v =0, |      |     |
|                          |     |     |       | 1       | m     | j       |      |     |
whichimpliesthattheminimalpolynomialof\mathcal{T} equals(z- \lambda )⋯(z- \lambda ).
|     |     |     |     |     |     |     |     | 1 m |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
To prove the implication in the other direction, now suppose the minimal
polynomial of \mathcal{T} equals (z- \lambda )⋯(z- \lambda ) for some list of distinct numbers
|        |          |     |     | 1   | m   |     |     |     |
| ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| \lambda ,…,\lambda | \in\mathbf{F}. Thus |     |     |     |     |     |     |     |
1 m
| 5.63 |     |     | (\mathcal{T}- | \lambda \mathcal{I})⋯(\mathcal{T}- | \lambda   | \mathcal{I})=0. |     |     |
| ---- | --- | --- | --- | -------- | --- | ----- | --- | --- |
|      |     |     |     | 1        | m   |       |     |     |
We will prove that \mathcal{T} is diagonalizable by induction on m. To get started,
supposem=1. Then\mathcal{T}-\lambda \mathcal{I} =0,whichmeansthat\mathcal{T}isascalarmultipleofthe
| identityoperator,whichimpliesthat\mathcal{T} |     |     |     |     | isdiagonalizable. |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
Nowsupposethatm>1andthedesiredresultholdsforallsmallervaluesof
m. Thesubspacerange(\mathcal{T}- \lambda \mathcal{I})isinvariantunder\mathcal{T} [thisisaspecialcaseof
m
5.18withp(z)=z-\lambda ]. Thus\mathcal{T} restrictedtorange(\mathcal{T}-\lambda \mathcal{I})isanoperatoron
|          |       | m   |     |     |     |     | m   |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| range(\mathcal{T}- | \lambda \mathcal{I}). |     |     |     |     |     |     |     |
m
| Ifu\inrange(\mathcal{T}-\lambda |              | \mathcal{I}),thenu=(\mathcal{T}-\lambda |     |         | \mathcal{I})vforsomev\in\mathcal{V},and5.63implies |          |          |     |
| ------------- | ------------ | ------------- | --- | ------- | ---------------------------- | -------- | -------- | --- |
|               |              | m             |     |         | m                            |          |          |     |
| 5.64          | (\mathcal{T}- \lambda \mathcal{I})⋯(\mathcal{T}- |               | \lambda   | \mathcal{I})u=(\mathcal{T}- |                              | \lambda \mathcal{I})⋯(\mathcal{T}- | \lambda \mathcal{I})v=0. |     |
|               | 1            |               | m-1 |         |                              | 1        | m        |     |
Hence(z-\lambda )⋯(z-\lambda )isapolynomialmultipleoftheminimalpolynomial
|     | 1   | m-1 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
of\mathcal{T} restrictedtorange(\mathcal{T}- \lambda \mathcal{I})[by5.29]. Thusbyourinductionhypothesis,
m
| thereisabasisofrange(\mathcal{T}- |     |     | \lambda   | \mathcal{I})consistingofeigenvectorsof\mathcal{T}. |     |     |     |     |
| ----------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
m
| Supposethatu |     | \in range(\mathcal{T}- |     | \lambda \mathcal{I})\capnull(\mathcal{T}- |     | \lambda \mathcal{I}). | Then\mathcal{T}u | = \lambda u. Now |
| ------------ | --- | ---------- | --- | ------------ | --- | ----- | ------ | ---------- |
|              |     |            |     | m            |     | m     |        | m          |
5.64impliesthat
|     |     | 0=(\mathcal{T}- |     | \lambda \mathcal{I})⋯(\mathcal{T}- |     | \lambda \mathcal{I})u   |     |     |
| --- | --- | ----- | --- | -------- | --- | ------- | --- | --- |
|     |     |       |     | 1        |     | m-1     |     |     |
|     |     |       | =(\lambda | - \lambda )⋯(\lambda |     | - \lambda )u. |     |     |
|     |     |       | m   | 1        | m   | m-1     |     |     |
,…,\lambda
Because \lambda aredistinct,theequationaboveimpliesthatu = 0. Hence
1 m
| range(\mathcal{T}- | \lambda \mathcal{I})\capnull(\mathcal{T}- |     | \lambda   | \mathcal{I})={0}. |     |     |     |     |
| -------- | ------------ | --- | --- | ------- | --- | --- | --- | --- |
|          | m            |     | m   |         |     |     |     |     |
Thusrange(\mathcal{T}-\lambda \mathcal{I})+null(\mathcal{T}-\lambda \mathcal{I})isadirectsum(by1.46)whosedimension
|     |     | m   |     | m   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
isdim\mathcal{V} (by3.94and3.21). Hencerange(\mathcal{T}-\lambda \mathcal{I})\oplusnull(\mathcal{T}-\lambda \mathcal{I})=\mathcal{V}. Every
|     |     |     |     |     |     | m   |     | m   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
nonzero vector in null(\mathcal{T} - \lambda \mathcal{I}) is an eigenvector of \mathcal{T} with eigenvalue \lambda .
m m
Earlierinthisproofwesawthatthereisabasisofrange(\mathcal{T}- \lambda \mathcal{I})consistingof
m
eigenvectorsof\mathcal{T}. Adjoiningtothatbasisabasisofnull(\mathcal{T}- \lambda \mathcal{I})givesabasis
m
of\mathcal{V} consistingofeigenvectorsof\mathcal{T}. Thematrixof\mathcal{T} withrespecttothisbasisis
adiagonalmatrix,asdesired.

170 Chapter 5 Eigenvaluesand Eigenvectors
Noformulaexistsforthezerosofpolynomialsofdegree5orgreater. However,
thepreviousresultcanbeusedtodeterminewhetheranoperatoronacomplex
vectorspaceisdiagonalizablewithoutevenfindingapproximationsofthezeros
oftheminimalpolynomial—see Exercise15.
Thenextresultwillbeakeytoolwhenweprovearesultaboutthesimultaneous
diagonalizationoftwooperators;see5.76. Notehowtheuseofacharacterization
ofdiagonalizableoperatorsintermsoftheminimalpolynomial(see5.62)leads
toashortproofofthenextresult.
5.65 restrictionofdiagonalizableoperatortoinvariantsubspace
Suppose\mathcal{T} \inℒ(\mathcal{V})isdiagonalizableand\mathcal{U}isasubspaceof\mathcal{V}thatisinvariant
under\mathcal{T}. Then\mathcal{T}| isadiagonalizableoperatoron\mathcal{U}.
\mathcal{U}
Proof Becausetheoperator\mathcal{T} isdiagonalizable,theminimalpolynomialof\mathcal{T}
equals(z- \lambda )⋯(z- \lambda )forsomelistofdistinctnumbers \lambda ,…,\lambda \in\mathbf{F} (by
1 m 1 m
5.62). The minimal polynomial of \mathcal{T} is a polynomial multiple of the minimal
polynomialof\mathcal{T}| (by5.31). Hencetheminimalpolynomialof\mathcal{T}| hastheform
\mathcal{U} \mathcal{U}
requiredby5.62,whichshowsthat\mathcal{T}| isdiagonalizable.
\mathcal{U}
Gershgorin Disk Theorem
**5.66 定义：** Gershgorindisks
Suppose\mathcal{T} \inℒ(\mathcal{V})andv ,…,v isabasisof\mathcal{V}. Let\mathcal{A}denotethematrixof
1 n
\mathcal{T} withrespecttothisbasis. AGershgorindiskof\mathcal{T} withrespecttothebasis
v ,…,v isasetoftheform
1 n
n
{z\in\mathbf{F} ∶|z-\mathcal{A} |\leq \sum|\mathcal{A} |},
j,j j,k
$$k=1$$
k\neqj
wherej \in{1,…,n}.
Becausetherearenchoicesforjinthedefinitionabove,\mathcal{T} hasnGershgorin
disks. If\mathbf{F} =\mathbf{C},thenforeachj \in{1,…,n},thecorresponding Gershgorindisk
isacloseddiskin\mathbf{C} centeredat\mathcal{A} ,whichisthejth entryonthediagonalof\mathcal{A}.
j,j
Theradiusofthiscloseddiskisthesumoftheabsolutevaluesoftheentriesin
rowjof\mathcal{A},excludingthediagonalentry. If\mathbf{F} =\mathbf{R},thenthe Gershgorindisksare
closedintervalsin\mathbf{R}.
Inthespecialcasethatthesquarematrix\mathcal{A}aboveisadiagonalmatrix,each
Gershgorin disk consists of a single point that is a diagonal entry of \mathcal{A} (and
eacheigenvalueof\mathcal{T} isoneofthosepoints,asrequiredbythenextresult). One
consequenceofournextresultisthatifthenondiagonalentriesof\mathcal{A}aresmall,
theneacheigenvalueof\mathcal{T} isnearadiagonalentryof\mathcal{A}.

| --- | --- | --- | --------- | --- | ----------------------- | --- | --- |
Gershgorindisktheorem
5.67
| Suppose\mathcal{T} | \inℒ(\mathcal{V})andv |     | ,…,v | isabasisof\mathcal{V}. | Theneacheigenvalueof\mathcal{T} |     |     |
| -------- | --------- | --- | ---- | ------------ | --------------------- | --- | --- |
|          |           |     | 1    | n            |                       |     |     |
iscontainedinsome Gershgorindiskof\mathcal{T} withrespecttothebasisv ,…,v .
1 n
Proof Suppose \lambda \in \mathbf{F} isaneigenvalueof\mathcal{T}. Letw \in \mathcal{V} beacorresponding
| eigenvector. | Thereexistc |     | ,…,c | \in\mathbf{F} suchthat |     |     |     |
| ------------ | ----------- | --- | ---- | ----------- | --- | --- | --- |
|              |             |     | 1 n  |             |     |     |     |
| 5.68         |             |     | w=c  | v +⋯+c      | v . |     |     |
|              |             |     |      | 1 1         | n n |     |     |
Let\mathcal{A}denotethematrixof\mathcal{T} withrespecttothebasisv ,…,v . Applying\mathcal{T}
1 n
tobothsidesoftheequationabovegives
n
|      |     |     | \lambdaw= | \sumc \mathcal{T}v |     |     |     |
| ---- | --- | --- | --- | ----- | --- | --- | --- |
| 5.69 |     |     |     | k k   |     |     |     |
$$k=1$$
|      |     |     |     | n n     |              |     |     |
| ---- | --- | --- | --- | ------- | ------------ | --- | --- |
|      |     |     | =   | \sumc \sum    | \mathcal{A} v          |     |     |
|      |     |     |     | k       | j,k j        |     |     |
|      |     |     |     | k=1 j=1 |              |     |     |
|      |     |     |     | n n     |              |     |     |
| 5.70 |     |     | =   | \sum(\sum\mathcal{A}    | j,k c k )v j | .   |     |
|      |     |     |     | j=1 k=1 |              |     |     |
Letj \in{1,…,n}besuchthat
|     |     |     | |c|=max{|c | |,…,|c | |}. |     |     |
| --- | --- | --- | ---------- | ------ | --- | --- | --- |
|     |     |     | j          | 1      | n   |     |     |
Using5.68,weseethatthecoefficientofv ontheleftsideof5.69equals \lambdac,
j j
whichmustequalthecoefficientofv ontherightsideof5.70. Inotherwords,
j
n
|     |     |     | \lambdac  | = \sum\mathcal{A} | c .   |     |     |
| --- | --- | --- | --- | ---- | ----- | --- | --- |
|     |     |     |     | j    | j,k k |     |     |
$$k=1$$
Subtract\mathcal{A} c fromeachsideoftheequationaboveandthendividebothsides
j,j j
byc toget
j
n
c
|     |     |     | |\lambda-\mathcal{A} | |=∣\sum | \mathcal{A} k∣ |     |     |
| --- | --- | --- | ---- | ---- | ---- | --- | --- |
|     |     |     |      | j,j  | j,kc |     |     |
j
$$k=1$$
k\neqj
n
|     |     |     |     | \leq \sum|\mathcal{A} | |.  |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- |
j,k
$$k=1$$
k\neqj
| Thus \lambdaisinthejth |     | Gershgorindiskwithrespecttothebasisv |     |     |     |     | ,…,v . |
| ---------------- | --- | ------------------------------------ | --- | --- | --- | --- | ------ |
|                  |     |                                      |     |     |     |     | 1 n    |
Exercise22givesaniceapplication
| ofthe Gershgorindisktheorem. |     |        |                 |     | for Semyon | Aronovich | Gershgorin, |
| --------------------------- | --- | ------ | --------------- | --- | ---------- | --------- | ----------- |
| Exercise                    | 23  | states | that the radius | of  |            |           |             |
whopublishedthisresultin1931.
each Gershgorindiskcouldbechanged
tothesumoftheabsolutevaluesofcorrespondingcolumnentries(insteadofrow
entries),excludingthediagonalentry,andthetheoremabovewouldstillhold.

| -------- | -------------------------- | --- | --- | --- |
| Exercises | 5D  |     |     |     |
| --------- | --- | --- | --- | --- |
1 Suppose\mathcal{V} isafinite-dimensionalcomplexvectorspaceand\mathcal{T} \inℒ(\mathcal{V}).
Provethatif\mathcal{T}4
| (a)                            | =\mathcal{I},then\mathcal{T} | isdiagonalizable. |          |     |
| ------------------------------ | -------- | ----------------- | -------- | --- |
| (b) Provethatif\mathcal{T}4              | =\mathcal{T},then\mathcal{T} | isdiagonalizable. |          |     |
| (c) Giveanexampleofanoperator\mathcal{T} |          | \inℒ(\mathbf{C}2)suchthat\mathcal{T}4  | =\mathcal{T}2 and\mathcal{T} | is  |
notdiagonalizable.
2 Suppose \mathcal{T} \in ℒ(\mathcal{V}) has a diagonal matrix \mathcal{A} with respect to some basis
of \mathcal{V}. Prove that if \lambda \in \mathbf{F}, then \lambda appears on the diagonal of \mathcal{A} precisely
dim\mathcal{E}(\lambda,\mathcal{T})times.
3 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Provethatiftheoperator
| \mathcal{T} isdiagonalizable,then\mathcal{V} | =null\mathcal{T}\oplusrange\mathcal{T}. |     |     |     |
| ------------------------ | -------------- | --- | --- | --- |
4 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \in ℒ(\mathcal{V}). Provethatthefollowing
areequivalent.
| (a) \mathcal{V} | =null\mathcal{T}\oplusrange\mathcal{T}. |     |     |     |
| ----- | -------------- | --- | --- | --- |
| (b) \mathcal{V} | =null\mathcal{T}+range\mathcal{T}. |     |     |     |
$$(c) null\mathcal{T}\caprange\mathcal{T} ={0}.$$
5 Suppose \mathcal{V} is a finite-dimensional complex vector space and \mathcal{T} \in ℒ(\mathcal{V}).
| Provethat\mathcal{T} | isdiagonalizableifandonlyif |              |     |     |
| ---------- | --------------------------- | ------------ | --- | --- |
|            | \mathcal{V} =null(\mathcal{T}-                  | \lambda\mathcal{I})\oplusrange(\mathcal{T}- | \lambda\mathcal{I}) |     |
| forevery   | \lambda\in\mathbf{C}.                        |              |     |     |
6 Suppose\mathcal{T} \in ℒ(\mathbf{F}5)anddim\mathcal{E}(8,\mathcal{T}) = 4. Provethat\mathcal{T} -2\mathcal{I} or\mathcal{T} -6\mathcal{I} is
invertible.
| 7 Suppose\mathcal{T} | \inℒ(\mathcal{V})isinvertible. | Provethat |     |     |
| ---------- | ------------------ | --------- | --- | --- |
\mathcal{E}(\lambda,\mathcal{T})=\mathcal{E}(1,\mathcal{T}-1)
\lambda
| forevery                       | \lambda\in\mathbf{F} with \lambda\neq0.            |                |                    |     |
| ------------------------------ | ------------------------ | -------------- | ------------------ | --- |
| Suppose\mathcal{V}                       | isfinite-dimensionaland\mathcal{T} | \inℒ(\mathcal{V}).         | Let ,…,\lambda denotethe |     |
| 8                              |                          |                | \lambda 1 m              |     |
| distinctnonzeroeigenvaluesof\mathcal{T}. |                          | Provethat      |                    |     |
|                                | dim\mathcal{E}(\lambda ,\mathcal{T})+⋯+dim\mathcal{E}(\lambda      | ,\mathcal{T})\leqdimrange\mathcal{T}. |                    |     |
|                                | 1                        | m              |                    |     |
| Suppose\mathcal{R},\mathcal{T}                     | ℒ(\mathbf{F}3)eachhave2,6,7       |                |                    |     |
| 9                              | \in                        | aseigenvalues. | Provethatthere     |     |
existsaninvertibleoperator\mathcal{S}\inℒ(\mathbf{F}3)suchthat\mathcal{R}=\mathcal{S}-1\mathcal{T}\mathcal{S}.
10 Find\mathcal{R},\mathcal{T} \inℒ(\mathbf{F}4)suchthat\mathcal{R}and\mathcal{T}eachhave2,6,7aseigenvalues,\mathcal{R}and
\mathcal{T} havenoothereigenvalues,andtheredoesnotexistaninvertibleoperator
\mathcal{S}\inℒ(\mathbf{F}4)suchthat\mathcal{R}=\mathcal{S}-1\mathcal{T}\mathcal{S}.

| --- | --- | --------- | --- | ----------------------- | --- | --- | --- |
\inℒ(\mathbf{C}3)suchthat6and7areeigenvaluesof\mathcal{T}andsuchthat\mathcal{T}does
11 Find\mathcal{T}
nothaveadiagonalmatrixwithrespecttoanybasisof\mathbf{C}3.
Suppose\mathcal{T} \inℒ(\mathbf{C}3)issuchthat6and7areeigenvaluesof\mathcal{T}. Furthermore,
suppose\mathcal{T} doesnothaveadiagonalmatrixwithrespecttoanybasisof\mathbf{C}3.
| Provethatthereexists(z |     | ,z  | ,z )\in\mathbf{C}3 | suchthat |     |     |     |
| ---------------------- | --- | --- | ------- | -------- | --- | --- | --- |
1 2 3
|     | ,z  | ,z )=(6+8z |     | ,7+8z | ,13+8z |     |     |
| --- | --- | ---------- | --- | ----- | ------ | --- | --- |
|     | \mathcal{T}(z |            |     |       |        | ).  |     |
|     | 1   | 2 3        |     | 1     | 2      | 3   |     |
13 Suppose\mathcal{A}isadiagonalmatrixwithdistinctentriesonthediagonaland\mathcal{B}
| isamatrixofthesamesizeas\mathcal{A}. |     |     |     | Showthat\mathcal{A}\mathcal{B}=\mathcal{B}\mathcal{A}ifandonlyif\mathcal{B}isa |     |     |     |
| -------------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- |
diagonalmatrix.
14 (a) Giveanexampleofafinite-dimensionalcomplexvectorspaceandan
onthatvectorspacesuchthat\mathcal{T}2
| operator\mathcal{T} |     |     |     |     | isdiagonalizablebut\mathcal{T} |     | is  |
| --------- | --- | --- | --- | --- | -------------------- | --- | --- |
notdiagonalizable.
$$(b) Suppose \mathbf{F} = \mathbf{C}, k is a positive integer, and \mathcal{T} \in ℒ(\mathcal{V}) is invertible.$$
| Provethat\mathcal{T} | isdiagonalizableifandonlyif\mathcal{T}k |     |     |     |     | isdiagonalizable. |     |
| ---------- | ----------------------------- | --- | --- | --- | --- | ----------------- | --- |
15 Suppose\mathcal{V} isafinite-dimensionalcomplexvectorspace,\mathcal{T} \inℒ(\mathcal{V}),andp
istheminimalpolynomialof\mathcal{T}. Provethatthefollowingareequivalent.
$$(a) \mathcal{T} isdiagonalizable.$$
$$(b) There does not exist \lambda \in \mathbf{C} such that p is a polynomial multiple of$$
$$(z- \lambda)2.$$
| (c) panditsderivativep′ |     | havenozerosincommon. |     |     |     |     |     |
| ----------------------- | --- | -------------------- | --- | --- | --- | --- | --- |
Thegreatestcommondivisorofpandp′
| (d)      |        |         |     |       | istheconstantpolynomial1. |            |      |
| -------- | ------ | ------- | --- | ----- | ------------------------- | ---------- | ---- |
| The      |        |         | of  | p and | p′ is the monic           | polynomial | q of |
| greatest | common | divisor |     |       |                           |            |      |
largestdegreesuchthatpandp′arebothpolynomialmultiplesof q. The
Euclideanalgorithmforpolynomials(lookitup)canquicklydetermine
the greatest common divisor of two polynomials, without requiring any
informationaboutthezerosofthepolynomials. Thustheequivalenceof (a)
and (d)aboveshowsthatwecandeterminewhether \mathcal{T} isdiagonalizable
| withoutknowinganythingaboutthezerosof |     |     |     |     | p.  |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
16 Supposethat\mathcal{T} \inℒ(\mathcal{V})isdiagonalizable. Let \lambda ,…,\lambda denotethedistinct
|     |     |     |     |     | 1   | m   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
eigenvaluesof\mathcal{T}. Provethatasubspace\mathcal{U} of\mathcal{V} isinvariantunder\mathcal{T} ifand
| onlyifthereexistsubspaces\mathcal{U} |         |     | ,…,\mathcal{U} | of\mathcal{V} | suchthat\mathcal{U} | \subseteq \mathcal{E}(\lambda | ,\mathcal{T})for |
| -------------------------- | ------- | --- | ---- | --- | --------- | ----- | ------ |
|                            |         |     | 1    | m   |           | k     | k      |
| eachkand\mathcal{U}                  | =\mathcal{U} \oplus⋯\oplus\mathcal{U} |     | .    |     |           |       |        |
|                            | 1       |     | m    |     |           |       |        |
Suppose\mathcal{V} isfinite-dimensional. Provethatℒ(\mathcal{V})hasabasisconsistingof
diagonalizableoperators.
18 Supposethat\mathcal{T} \inℒ(\mathcal{V})isdiagonalizableand\mathcal{U} isasubspaceof\mathcal{V} thatis
invariantunder\mathcal{T}. Provethatthequotientoperator\mathcal{T}/\mathcal{U} isadiagonalizable
operatoron\mathcal{V}/\mathcal{U}.
Thequotientoperator\mathcal{T}/\mathcal{U}wasdefinedin Exercise38in Section5A.

174 Chapter 5 Eigenvaluesand Eigenvectors
19 Proveorgiveacounterexample: If\mathcal{T} \inℒ(\mathcal{V})andthereexistsasubspace\mathcal{U}
of\mathcal{V}thatisinvariantunder\mathcal{T}suchthat\mathcal{T}| and\mathcal{T}/\mathcal{U}arebothdiagonalizable,
\mathcal{U}
then\mathcal{T} isdiagonalizable.
See Exercise 13 in Section 5C for an analogous statement about uppertriangularmatrices.
20 Suppose\mathcal{V} isfinite-dimensionaland\mathcal{T} \inℒ(\mathcal{V}). Provethat\mathcal{T} isdiagonalizableifandonlyifthedualoperator\mathcal{T}′ isdiagonalizable.
21 The Fibonaccisequence\mathcal{F} ,\mathcal{F} ,\mathcal{F} ,… isdefinedby
0 1 2
\mathcal{F} =0, \mathcal{F} =1, and\mathcal{F} =\mathcal{F} +\mathcal{F} forn\geq2.
0 1 n n-2 n-1
Define\mathcal{T} \inℒ(\mathbf{R}2)by\mathcal{T}(x,y)=(y,x+y).
$$(a) Showthat\mathcal{T}n(0,1)=(\mathcal{F} ,\mathcal{F} )foreachnonnegativeintegern.$$
n n+1
$$(b) Findtheeigenvaluesof\mathcal{T}.$$
$$(c) Findabasisof\mathbf{R}2 consistingofeigenvectorsof\mathcal{T}.$$
$$(d) Usethesolutionto(c)tocompute\mathcal{T}n(0,1). Concludethat$$
1 1+\sqrt5 n 1-\sqrt5 n
\mathcal{F} = [( ) -( ) ]
n \sqrt5 2 2
foreachnonnegativeintegern.
$$(e) Use(d)toconcludethatifnisanonnegativeinteger,thenthe Fibonacci$$
number\mathcal{F} istheintegerthatisclosestto
n
1 1+\sqrt5 n
$$( ) .$$
\sqrt5 2
Each\mathcal{F} isanonnegativeinteger,eventhoughtherightsideoftheformula
n
in(d)doesnotlooklikeaninteger. Thenumber
1+\sqrt5
iscalledthegoldenratio.
22 Suppose\mathcal{T} \inℒ(\mathcal{V})and\mathcal{A}isann-by-nmatrixthatisthematrixof\mathcal{T} with
respecttosomebasisof\mathcal{V}. Provethatif
n
|\mathcal{A} |> \sum|\mathcal{A} |
j,j j,k
$$k=1$$
k\neqj
foreachj \in{1,…,n},then\mathcal{T} isinvertible.
Thisexercisestatesthatifthediagonalentriesofthematrixof \mathcal{T}arelarge
comparedtothenondiagonalentries,then\mathcal{T}isinvertible.
23 Supposethedefinitionofthe Gershgorindisksischangedsothattheradiusof
thekthdiskisthesumoftheabsolutevaluesoftheentriesincolumn(instead
ofrow)kof\mathcal{A},excludingthediagonalentry. Showthatthe Gershgorindisk
theorem(5.67)stillholdswiththischangeddefinition.

| --- | --- | --- | --- | --------- | ------------------ | --- | --- |
| 5E  | Commuting |     | Operators |     |     |     |     |
| --- | --------- | --- | --------- | --- | --- | --- | --- |
commute
**5.71 定义：** |     | Twooperators\mathcal{S}and\mathcal{T} |     |     | onthesamevectorspacecommuteif\mathcal{S}\mathcal{T} |     |     | =\mathcal{T}\mathcal{S}. |
| --- | ----------------- | --- | --- | ------------------------------- | --- | --- | ---- |
•
• Twosquarematrices\mathcal{A}and\mathcal{B}ofthesamesizecommuteif\mathcal{A}\mathcal{B}=\mathcal{B}\mathcal{A}.
Forexample,if\mathcal{I} istheidentityoperatoron\mathcal{V} and \lambda\in\mathbf{F},then \lambda\mathcal{I} commutes
witheveryoperatoron\mathcal{V}.
As another example, if \mathcal{T} is an operator then \mathcal{T}2 and \mathcal{T}3 commute. More
generally,ifp,q\in𝒫(\mathbf{F}),thenp(\mathcal{T})andq(\mathcal{T})commute[see5.17(b)].
| ---- | -------- | -------------------------------------- | --- | --- | --- | --- | --- |
Supposemisanonnegativeinteger. Let𝒫 (\mathbf{C}2,\mathbf{C})denotethecomplexvector
m
spaceofpolynomials(withcoefficientsin\mathbf{C})intwovariablesandofdegreeat
most m, with the usual operations of addition and scalar multiplication of \mathbf{C}valuedfunctions. Thustheelementsof𝒫 (\mathbf{C}2,\mathbf{C})arefunctionspfrom\mathbf{C}2 to\mathbf{C}
m
oftheform
|      |     |     |     | p(w,z)= | wjzk, |     |     |
| ---- | --- | --- | --- | ------- | ----- | --- | --- |
| 5.73 |     |     |     | \sum       | a j,k |     |     |
j+k\leqm
wheretheindicesjandktakeonallnonnegativeintegervaluessuchthatj+k \leqm,
eacha isin\mathbf{C},andwjzk denotesthefunctionon\mathbf{C}2 definedby(w,z)↦wjzk.
j,k
|     |     |     | ,\mathcal{D}  | \inℒ(𝒫 (\mathbf{C}2,\mathbf{C}))by |     |     |     |
| --- | --- | --- | --- | -------------- | --- | --- | --- |
Defineoperators\mathcal{D}
|     |      |       | w z  | m          |      |       |            |
| --- | ---- | ----- | ---- | ---------- | ---- | ----- | ---------- |
|     |      | 𝜕p    |      |            | 𝜕p   |       |            |
|     | \mathcal{D} p= | =     | \sum ja | wj-1zk and | \mathcal{D} p= | = \sum   | ka wjzk-1, |
|     | w    | 𝜕w    | j,k  |            | z 𝜕z |       | j,k        |
|     |      | j+k\leqm |      |            |      | j+k\leqm |            |
wherepisasin5.73. Theoperators\mathcal{D} and\mathcal{D} arecalledpartialdifferentiation
|     |     |     |     | w   | z   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
operatorsbecauseeachoftheseoperatorsdifferentiateswithrespecttooneofthe
variableswhilepretendingthattheothervariableisaconstant.
|     | Theoperators\mathcal{D} |     | and\mathcal{D} | commutebecauseifpisasin5.73,then |     |     |     |
| --- | ------------- | --- | ---- | -------------------------------- | --- | --- | --- |
|     |               | w   |      | z                                |     |     |     |
wj-1zk-1
|     |     | (\mathcal{D} w | \mathcal{D} z )p= | \sum jka j,k | =(\mathcal{D} | z \mathcal{D} w )p. |     |
| --- | --- | ---- | ------- | --------- | --- | --------- | --- |
j+k\leqm
|     | Theequation\mathcal{D} |     |       | on𝒫     | (\mathbf{C}2,\mathbf{C})illustratesamoregeneralresult |     |     |
| --- | ------------ | --- | ----- | ------- | ----------------------------------- | --- | --- |
|     |              | w \mathcal{D} | z = \mathcal{D} | z \mathcal{D} w m |                                     |     |     |
thattheorderofpartialdifferentiationdoesnotmatterfornicefunctions.
|     | Commuting | matrices |     | are unusual. |     |     |     |
| --- | --------- | -------- | --- | ------------ | --- | --- | --- |
All214,358,881(whichequals118)or-
| For | example, | there are | 214,358,881 | or- |     |     |     |
| --- | -------- | --------- | ----------- | --- | --- | --- | --- |
deredpairsofthe2-by-2matricesun-
| dered | pairs | of 2-by-2 | matrices | all of |     |     |     |
| ----- | ----- | --------- | -------- | ------ | --- | --- | --- |
derconsiderationwerecheckedbya
| whose | entries | are integers |     | in the inter- |     |     |     |
| ----- | ------- | ------------ | --- | ------------- | --- | --- | --- |
computertodiscoverthatonly674,609
| val                            | [-5,5]. | Only about | 0.3% | of these |                  |     |                   |
| ------------------------------ | ------- | ---------- | ---- | -------- | ---------------- | --- | ----------------- |
|                                |         |            |      |          | of these ordered |     | pairs of matrices |
| orderedpairsofmatricescommute. |         |            |      |          | commute.         |     |                   |

| -------- | -------------------------- | --- | --- | --- |
Thenextresultshowsthattwooperatorscommuteifandonlyiftheirmatrices
$$(withrespecttothesamebasis)commute.$$
5.74 commutingoperatorscorrespondtocommutingmatrices
| Suppose\mathcal{S},\mathcal{T} | \inℒ(\mathcal{V})andv | ,…,v isabasisof\mathcal{V}. | Then\mathcal{S}and\mathcal{T} | commute |
| ---------- | --------- | ----------------- | --------- | ------- |
1 n
| ifandonlyifℳ(\mathcal{S},(v | ,…,v | ))andℳ(\mathcal{T},(v | ,…,v ))commute. |     |
| ----------------- | ---- | ----------- | --------------- | --- |
|                   | 1    | n           | 1 n             |     |
|     | \mathcal{S}and\mathcal{T} commute | ⟺ \mathcal{S}\mathcal{T} =\mathcal{T}\mathcal{S} |     |     |
| --- | ------------- | -------- | --- | --- |
⟺ ℳ(\mathcal{S}\mathcal{T})=ℳ(\mathcal{T}\mathcal{S})
⟺ ℳ(\mathcal{S})ℳ(\mathcal{T})=ℳ(\mathcal{T})ℳ(\mathcal{S})
⟺ ℳ(\mathcal{S})andℳ(\mathcal{T})commute,
asdesired.
Thenextresultshowsthatiftwooperatorscommute,theneveryeigenspace
foroneoperatorisinvariantundertheotheroperator. Thisresult,whichwewill
useseveraltimes,isoneofthemainreasonswhyapairofcommutingoperators
behavesbetterthanapairofoperatorsthatdoesnotcommute.
eigenspaceisinvariantundercommutingoperator
5.75
| Suppose\mathcal{S},\mathcal{T} | \inℒ(\mathcal{V})commuteand | \lambda\in\mathbf{F}. | Then\mathcal{E}(\lambda,\mathcal{S})isinvariantunder\mathcal{T}. |     |
| ---------- | --------------- | ---- | ---------------------------- | --- |
Supposev\in\mathcal{E}(\lambda,\mathcal{S}).
| Proof |                                | Then |      |     |
| ----- | ------------------------------ | ---- | ---- | --- |
|       | \mathcal{S}(\mathcal{T}v)=(\mathcal{S}\mathcal{T})v=(\mathcal{T}\mathcal{S})v=\mathcal{T}(\mathcal{S}v)=\mathcal{T}(\lambdav)= |      | \lambda\mathcal{T}v. |     |
Theequationaboveshowsthat\mathcal{T}v\in\mathcal{E}(\lambda,\mathcal{S}). Thus\mathcal{E}(\lambda,\mathcal{S})isinvariantunder\mathcal{T}.
Supposewehavetwooperators,eachofwhichisdiagonalizable. Ifwewant
todocomputationsinvolvingbothoperators(forexample,involvingtheirsum),
thenwewantthetwooperatorstobediagonalizablebythesamebasis,which
accordingtothenextresultispossiblewhenthetwooperatorscommute.
| 5.76 simultaneousdiagonalizability |     | ⟺   | commutativity |     |
| ---------------------------------- | --- | --- | ------------- | --- |
Twodiagonalizableoperatorsonthesamevectorspacehavediagonalmatrices
withrespecttothesamebasisifandonlyifthetwooperatorscommute.
Proof Firstsuppose\mathcal{S},\mathcal{T} \in ℒ(\mathcal{V})havediagonalmatriceswithrespecttothe
samebasis. Theproductoftwodiagonalmatricesofthesamesizeisthediagonal
matrixobtainedbymultiplyingthecorrespondingelementsofthetwodiagonals.
Thusanytwodiagonalmatricesofthesamesizecommute. Thus\mathcal{S}and\mathcal{T}commute,
by5.74.

| --- | --- | --- | --------- | ------------------ | --- | --- |
Toprovetheimplicationintheotherdirection,nowsupposethat\mathcal{S},\mathcal{T} \inℒ(\mathcal{V})
are diagonalizable operators that commute. Let \lambda ,…,\lambda denote the distinct
1 m
| eigenvaluesof\mathcal{S}. |     | Because\mathcal{S}isdiagonalizable,5.55(c)showsthat |           |      |     |     |
| --------------- | --- | ----------------------------------------- | --------- | ---- | --- | --- |
|                 |     | \mathcal{V} =\mathcal{E}(\lambda                                    | ,\mathcal{S})\oplus⋯\oplus\mathcal{E}(\lambda | ,\mathcal{S}). |     |     |
| 5.77            |     |                                           | 1         | m    |     |     |
Foreachk = 1,…,m,thesubspace\mathcal{E}(\lambda ,\mathcal{S})isinvariantunder\mathcal{T} (by5.75).
k
Because \mathcal{T} is diagonalizable, 5.65 implies that \mathcal{T}| is diagonalizable for
\mathcal{E}(\lambda ,\mathcal{S})
k
each k. Hence for each k = 1,…,m, there is a basis of \mathcal{E}(\lambda ,\mathcal{S}) consisting of
k
eigenvectorsof \mathcal{T}. Putting these bases togethergivesa basis of (because of
\mathcal{V}
5.77),witheachvectorinthisbasisbeinganeigenvectorofboth\mathcal{S}and\mathcal{T}. Thus\mathcal{S}
and\mathcal{T} bothhavediagonalmatriceswithrespecttothisbasis,asdesired.
See Exercise2foranextensionoftheresultabovetomorethantwooperators.
Suppose\mathcal{V} isafinite-dimensionalnonzerocomplexvectorspace. Thenevery
operatoron\mathcal{V} hasaneigenvector(see5.19). Thenextresultshowsthatiftwo
operatorson\mathcal{V}commute,thenthereisavectorin\mathcal{V}thatisaneigenvectorforboth
operators(butthetwocommutingoperatorsmightnothaveacommoneigenvalue).
Foranextensionofthenextresulttomorethantwooperators,see Exercise9(a).
commoneigenvectorforcommutingoperators
5.78
Everypairofcommutingoperatorsonafinite-dimensionalnonzerocomplex
vectorspacehasacommoneigenvector.
Proof Suppose \mathcal{V} is a finite-dimensional nonzero complex vector space and
\mathcal{S},\mathcal{T} ℒ(\mathcal{V})
|     | \in commute. | Let | \lambda beaneigenvalueof | \mathcal{S} (5.19 | tellsusthat | \mathcal{S} does |
| --- | ---------- | --- | ------------------ | ------- | ----------- | ------ |
indeed have an eigenvalue). Thus \mathcal{E}(\lambda,\mathcal{S}) \neq {0}. Also, \mathcal{E}(\lambda,\mathcal{S}) is invariant
under\mathcal{T} (by5.75).
| Thus\mathcal{T}| |     | hasaneigenvector(againusing5.19),whichisaneigenvector |     |     |     |     |
| ------ | --- | ----------------------------------------------------- | --- | --- | --- | --- |
\mathcal{E}(\lambda,\mathcal{S})
forboth\mathcal{S}and\mathcal{T},completingtheproof.
**5.79 例：** commoneigenvectorforpartialdifferentiationoperators
| Let𝒫 | (\mathbf{C}2,\mathbf{C})beasin Example5.72andlet\mathcal{D} |     |     | ,\mathcal{D} \inℒ(𝒫 | (\mathbf{C}2,\mathbf{C}))bethe |     |
| ---- | ------------------------------ | --- | --- | ------- | ------------ | --- |
|      | m                              |     |     | w z     | m            |     |
commutingpartialdifferentiationoperatorsinthatexample. Asyoucanverify,0
| istheonlyeigenvalueofeachoftheseoperators. |     |     |     | Also |     |     |
| ------------------------------------------ | --- | --- | --- | ---- | --- | --- |
m
∶a
|     |     | \mathcal{E}(0,\mathcal{D} )={\suma | zk  | ,…,a \in\mathbf{C}}, |     |     |
| --- | --- | ----------- | --- | --------- | --- | --- |
|     |     | w           | k 0 | m         |     |     |
$$k=0$$
m
|     |     | )={\sumcwj | ∶c   |      |     |     |
| --- | --- | ------- | ---- | ---- | --- | --- |
|     |     | \mathcal{E}(0,\mathcal{D}   | ,…,c | \in\mathbf{C}}. |     |     |
|     |     | z       | j 0  | m    |     |     |
$$j=0$$
Theintersectionofthesetwoeigenspacesisthesetofcommoneigenvectorsof
thetwooperators. Because\mathcal{E}(0,\mathcal{D} )\cap\mathcal{E}(0,\mathcal{D} )isthesetofconstantfunctions,
|     |     |     | w   | z   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
weseethat\mathcal{D} and\mathcal{D} indeedhaveacommoneigenvector,aspromisedby5.78.
|     | w   | z   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

| --- | -------- | --- | -------------------------- | --- | --- | --- | --- |
The next result extends 5.47 (the existence of a basis that gives an uppertriangularmatrix)totwocommutingoperators.
5.80 commutingoperatorsaresimultaneouslyuppertriangularizable
Suppose \mathcal{V} is a finite-dimensional complex vector space and \mathcal{S},\mathcal{T} are
commutingoperatorson\mathcal{V}. Thenthereisabasisof\mathcal{V} withrespecttowhich
| both\mathcal{S}and\mathcal{T} |     | haveupper-triangularmatrices. |     |     |     |     |     |
| --------- | --- | ----------------------------- | --- | --- | --- | --- | --- |
Proof Letn = dim\mathcal{V}. Wewilluseinductiononn. Thedesiredresultholdsif
$$n=1becauseall1-by-1matricesareuppertriangular. Nowsupposen>1and$$
thedesiredresultholdsforallcomplexvectorspaceswhosedimensionisn-1.
Let v be any common eigenvector of \mathcal{S} and \mathcal{T} (using 5.78). Hence \mathcal{S}v \in
1 1
| span(v | )and\mathcal{T}v | \inspan(v |     | ). Let\mathcal{W} beasubspaceof\mathcal{V} |      | suchthat |     |
| ------ | ------ | ------- | --- | ---------------------- | ---- | -------- | --- |
|        |        |         |     | \mathcal{V} =span(v              | )\oplus\mathcal{W}; |          |     |
| see2.33fortheexistenceof\mathcal{W}. |     |     |     | Definealinearmap\mathcal{P}∶ |     | \mathcal{V} \rightarrow\mathcal{W} | by  |
| -------------------------- | --- | --- | --- | ------------------ | --- | ---- | --- |
+w)=w
\mathcal{P}(av
| foreacha\in\mathbf{C} |     | andeachw\in\mathcal{W}. |          | Define\mathcal{S} | ̂,\mathcal{T} ̂ \inℒ(\mathcal{W})by |     |     |
| ---------- | --- | ----------- | -------- | ------- | ------------- | --- | --- |
|            |     |             | ̂        |         | ̂             |     |     |
|            |     |             | \mathcal{S}w=\mathcal{P}(\mathcal{S}w) | and     | \mathcal{T}w=\mathcal{P}(\mathcal{T}w)      |     |     |
for each w \in \mathcal{W}. To apply our induction hypothesis to \mathcal{S} ̂ and \mathcal{T}, ̂ we must first
showthatthesetwooperatorson\mathcal{W} commute. Todothis,supposew\in\mathcal{W}. Then
| thereexistsa\in\mathbf{C} |      | suchthat       |     |        |             |              |     |
| -------------- | ---- | -------------- | --- | ------ | ----------- | ------------ | --- |
|                | ̂ ̂  | ̂              |     | ̂      |             |              |     |
|                | (\mathcal{S} \mathcal{T} | )w=\mathcal{S} (\mathcal{P}(\mathcal{T}w))=\mathcal{S} |     | (\mathcal{T}w-av | )=\mathcal{P}(\mathcal{S}(\mathcal{T}w-av | ))=\mathcal{P}((\mathcal{S}\mathcal{T})w), |     |
where the last equality holds because v is an eigenvector of \mathcal{S} and \mathcal{P}v = 0.
| --- | --- | --- | --- | --- | --- | --- | --- |
Similarly,
̂ ̂
$$(\mathcal{T}\mathcal{S})w=\mathcal{P}((\mathcal{T}\mathcal{S})w).$$
Becausetheoperators\mathcal{S}and\mathcal{T} commute,thelasttwodisplayedequationsshow
| that(\mathcal{S}\mathcal{T})w=(\mathcal{T}\mathcal{S})w. | ̂̂  | ̂ ̂ | Hence\mathcal{S}and\mathcal{T} | ̂ ̂ commute. |     |     |     |
| ---------------- | --- | --- | ---------- | ------------ | --- | --- | --- |
Thus we can use our induction hypothesis to state that there exists a basis
̂ ̂
v ,…,v of\mathcal{W}suchthat\mathcal{S} and\mathcal{T} bothhaveupper-triangularmatriceswithrespect
2 n
| tothisbasis. |                              | Thelistv | ,…,v | isabasisof\mathcal{V}. |             |     |     |
| ------------ | ---------------------------- | -------- | ---- | ------------ | ----------- | --- | --- |
|              |                              |          | 1    | n            |             |     |     |
|              | Ifk \in{2,…,n},thenthereexista |          |      | ,b           | \in\mathbf{C} suchthat |     |     |
k k
|     |     |      |        | +\mathcal{S} ̂ and |         | +\mathcal{T} ̂    |     |
| --- | --- | ---- | ------ | -------- | ------- | ------- | --- |
|     |     | \mathcal{S}v k | =a k v | 1 v k    | \mathcal{T}v k =b | k v 1 v | k . |
Because\mathcal{S} ̂ and\mathcal{T} ̂ haveupper-triangularmatriceswithrespecttov ,…,v ,weknow
|     |     |     |     |     |     |     | 2 n |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | ̂   |     |     | ̂   |     |     |     |
that \mathcal{S} v \in span(v ,…,v ) and \mathcal{T} v \in span(v ,…,v ). Hence the equations
|     | k   | 2   | k   | k   | 2   | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
aboveimplythat
|     |     | \mathcal{S}v \inspan(v | ,…,v | ) and | \mathcal{T}v \inspan(v | ,…,v | ).  |
| --- | --- | ---------- | ---- | ----- | ---------- | ---- | --- |
|     |     | k          | 1    | k     | k          | 1    | k   |
Thus\mathcal{S}and\mathcal{T}haveupper-triangularmatriceswithrespecttov ,…,v ,asdesired.
1 n
Exercise9(b)extendstheresultabovetomorethantwooperators.

Section5E Commuting Operators 179
Ingeneral,itisnotpossibletodeterminetheeigenvaluesofthesumorproduct
oftwooperatorsfromtheeigenvaluesofthetwooperators. However,thenext
resultshowsthatsomethingnicehappenswhenthetwooperatorscommute.
5.81 eigenvaluesofsumandproductofcommutingoperators
Suppose\mathcal{V} isafinite-dimensionalcomplexvectorspaceand\mathcal{S},\mathcal{T} arecommutingoperatorson\mathcal{V}. Then
• everyeigenvalueof\mathcal{S}+\mathcal{T} isaneigenvalueof\mathcal{S}plusaneigenvalueof\mathcal{T},
• everyeigenvalueof\mathcal{S}\mathcal{T} isaneigenvalueof\mathcal{S}timesaneigenvalueof\mathcal{T}.
Proof There is a basis of \mathcal{V} with respect to which both \mathcal{S} and \mathcal{T} have uppertriangularmatrices(by5.80). Withrespecttothatbasis,
ℳ(\mathcal{S}+\mathcal{T})=ℳ(\mathcal{S})+ℳ(\mathcal{T}) and ℳ(\mathcal{S}\mathcal{T})=ℳ(\mathcal{S})ℳ(\mathcal{T}),
asstatedin3.35and3.43.
The definition of matrix addition shows that each entry on the diagonal of
ℳ(\mathcal{S}+\mathcal{T})equalsthesumofthecorrespondingentriesonthediagonalsofℳ(\mathcal{S})
andℳ(\mathcal{T}). Similarly,becauseℳ(\mathcal{S})andℳ(\mathcal{T})areupper-triangularmatrices,
thedefinitionofmatrixmultiplicationshowsthateachentryonthediagonalof
ℳ(\mathcal{S}\mathcal{T})equalstheproductofthecorrespondingentriesonthediagonalsofℳ(\mathcal{S})
andℳ(\mathcal{T}). Furthermore,ℳ(\mathcal{S}+\mathcal{T})andℳ(\mathcal{S}\mathcal{T})areupper-triangularmatrices
$$(see Exercise2in Section5C).$$
Everyentryonthediagonalofℳ(\mathcal{S})isaneigenvalueof\mathcal{S},andeveryentry
on the diagonal of ℳ(\mathcal{T}) is an eigenvalue of \mathcal{T} (by 5.41). Every eigenvalue
of \mathcal{S} + \mathcal{T} is on the diagonal of ℳ(\mathcal{S} + \mathcal{T}), and every eigenvalue of \mathcal{S}\mathcal{T} is on
the diagonal of ℳ(\mathcal{S}\mathcal{T}) (these assertions follow from 5.41). Putting all this
together,weconcludethateveryeigenvalueof\mathcal{S}+\mathcal{T} isaneigenvalueof\mathcal{S}plus
aneigenvalueof\mathcal{T}, andeveryeigenvalueof\mathcal{S}\mathcal{T} isaneigenvalueof\mathcal{S}timesan
eigenvalueof\mathcal{T}.
Exercises 5E
1 Give an example of two commuting operators \mathcal{S},\mathcal{T} on \mathbf{F}4 such that there
isasubspaceof\mathbf{F}4 thatisinvariantunder\mathcal{S}butnotunder\mathcal{T} andthereisa
subspaceof\mathbf{F}4 thatisinvariantunder\mathcal{T} butnotunder\mathcal{S}.
2 Suppose ℰ is a subset of ℒ(\mathcal{V}) and every element of ℰ is diagonalizable.
Provethatthereexistsabasisof\mathcal{V} withrespecttowhicheveryelementofℰ
hasadiagonalmatrixifandonlyifeverypairofelementsofℰcommutes.
Thisexerciseextends5.76,whichconsidersthecaseinwhichℰcontains
onlytwoelements. Forthisexercise,ℰmaycontainanynumberofelements,
andℰmayevenbeaninfiniteset.

180 Chapter 5 Eigenvaluesand Eigenvectors
3 Suppose\mathcal{S},\mathcal{T} \inℒ(\mathcal{V})aresuchthat\mathcal{S}\mathcal{T} =\mathcal{T}\mathcal{S}. Supposep\in𝒫(\mathbf{F}).
$$(a) Provethatnullp(\mathcal{S})isinvariantunder\mathcal{T}.$$
$$(b) Provethatrangep(\mathcal{S})isinvariantunder\mathcal{T}.$$
See5.18forthespecialcase\mathcal{S}=\mathcal{T}.
4 Prove or give a counterexample: If \mathcal{A} is a diagonal matrix and \mathcal{B} is an
upper-triangularmatrixofthesamesizeas\mathcal{A},then\mathcal{A}and\mathcal{B}commute.
5 Provethatapairofoperatorsonafinite-dimensionalvectorspacecommute
ifandonlyiftheirdualoperatorscommute.
See3.118forthedefinitionofthedualofanoperator.
6 Supposethat\mathcal{V} isanonzerofinite-dimensionalcomplexvectorspaceand
\mathcal{S},\mathcal{T} \inℒ(\mathcal{V})commute. Provethatthereexist\alpha,\lambda\in\mathbf{C} suchthat
range(\mathcal{S}-\alpha\mathcal{I})+range(\mathcal{T}- \lambda\mathcal{I})\neq\mathcal{V}.
7 Suppose \mathcal{V} is a complex vector space, \mathcal{S} \in ℒ(\mathcal{V}) is diagonalizable, and
\mathcal{T} \inℒ(\mathcal{V})commuteswith\mathcal{S}. Provethatthereisabasisof\mathcal{V} suchthat\mathcal{S}has
adiagonalmatrixwithrespecttothisbasisand\mathcal{T} hasanupper-triangular
matrixwithrespecttothisbasis.
8 Suppose m = 3 in Example 5.72 and \mathcal{D} ,\mathcal{D} are the commuting partial
x y
differentiation operators on 𝒫(\mathbf{R}2) from that example. Find a basis of
𝒫(\mathbf{R}2) with respect to which \mathcal{D} and \mathcal{D} each have an upper-triangular
3 x y
matrix.
9 Suppose\mathcal{V} isafinite-dimensionalnonzerocomplexvectorspace. Suppose
thatℰ\subseteqℒ(\mathcal{V})issuchthat\mathcal{S}and\mathcal{T} commuteforall\mathcal{S},\mathcal{T} \inℰ.
$$(a) Provethatthereisavectorin\mathcal{V} thatisaneigenvectorforeveryelement$$
ofℰ.
$$(b) Provethatthereisabasisof\mathcal{V} withrespecttowhicheveryelementof$$
ℰhasanupper-triangularmatrix.
Thisexerciseextends5.78and5.80,whichconsiderthecaseinwhichℰ
containsonlytwoelements. Forthisexercise,ℰmaycontainanynumberof
elements,andℰmayevenbeaninfiniteset.
10 Giveanexampleoftwocommutingoperators\mathcal{S},\mathcal{T} onafinite-dimensional
realvectorspacesuchthat\mathcal{S}+\mathcal{T} hasaneigenvaluethatdoesnotequalan
eigenvalueof\mathcal{S}plusaneigenvalueof\mathcal{T} and\mathcal{S}\mathcal{T} hasaneigenvaluethatdoes
notequalaneigenvalueof\mathcal{S}timesaneigenvalueof\mathcal{T}.
Thisexerciseshowsthat5.81doesnotholdonrealvectorspaces.
