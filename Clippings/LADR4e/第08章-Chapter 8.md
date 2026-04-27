---
title: Chapter 8
source: Clippings/LADR4e.pdf
created: 2026-04-23
type: chapter
tags:
  - book
  - chapter
---

# Chapter 8
Operators on Complex Vector Spaces
Inthischapterwedelvedeeperintothestructureofoperators,withmostofthe
attentiononcomplexvectorspaces. Someoftheresultsinthischapterapplyto
bothrealandcomplexvectorspaces;thuswedonotmakeastandingassumption
that\mathbf{F} =\mathbf{C}. Also,aninnerproductdoesnothelpwiththismaterial,sowereturn
tothegeneralsettingofafinite-dimensionalvectorspace.
Evenonafinite-dimensionalcomplexvectorspace,anoperatormaynothave
enougheigenvectorstoformabasisofthevectorspace. Thuswewillconsiderthe
closelyrelatedobjectscalledgeneralizedeigenvectors. Wewillseethatforeach
operatoronafinite-dimensionalcomplexvectorspace,thereisabasisofthevector
space consisting of generalized eigenvectors of the operator. The generalized
eigenspacedecompositionthenprovidesagooddescriptionofarbitraryoperators
onafinite-dimensionalcomplexvectorspace.
Nilpotent operators, which are operators that when raised to some power
equal0,haveanimportantroleintheseinvestigations. Nilpotentoperatorsprovide
a key tool in our proof that every invertible operator on a finite-dimensional
complexvectorspacehasasquarerootandinourapproachto Jordanform.
Thischapterconcludesbydefiningthetraceandprovingitskeyproperties.
standingassumptionsforthischapter
• \mathbf{F} denotes\mathbf{R} or\mathbf{C}.
• \mathcal{V} denotesafinite-dimensionalnonzerovectorspaceover\mathbf{F}.
David Iliff CCBY-SA
The Long Roomofthe Old Libraryatthe Universityof Dublin,where William Hamilton
$$(1805–1865)wasastudentandthenafacultymember. Hamiltonprovedaspecialcase$$
ofwhatwenowcallthe Cayley–Hamiltontheoremin1853.

| --- | -------- | ------------------------------ | --- | --- | --- | --- | --- |
| 8A Generalized |           | Eigenvectors |                | and | Nilpotent | Operators |     |
| -------------- | --------- | ------------ | -------------- | --- | --------- | --------- | --- |
| Null Spaces    | of Powers |              | of an Operator |     |           |           |     |
Webeginthischapterwithastudyofnullspacesofpowersofanoperator.
8.1 sequenceofincreasingnullspaces
| Suppose\mathcal{T} | \inℒ(\mathcal{V}).     | Then    |           |     |           |      |     |
| -------- | ---------- | ------- | --------- | --- | --------- | ---- | --- |
|          | {0}=null\mathcal{T}0 | \subseteqnull\mathcal{T}1 | \subseteq⋯\subseteqnull\mathcal{T}k |     | \subseteqnull\mathcal{T}k+1 | \subseteq⋯ . |     |
Proof Suppose k is a nonnegative integer and v \in null\mathcal{T}k. Then \mathcal{T}kv = 0,
|       |              | \mathcal{T}k+1v | \mathcal{T}(\mathcal{T}kv) |        |           | null\mathcal{T}k+1. |       |
| ----- | ------------ | ----- | ------ | ------ | --------- | --------- | ----- |
| which | implies that | =     |        | = \mathcal{T}(0) | = 0. Thus | v \in       | Hence |
null\mathcal{T}k \subseteqnull\mathcal{T}k+1,asdesired.
Thefollowingresultstatesthatiftwo
|     |     |     |     | For | similar | results about decreasing |     |
| --- | --- | --- | --- | --- | ------- | ------------------------ | --- |
consecutivetermsinthesequenceofsub- sequencesofranges,see Exercises6,
| spaces | above are | equal, then | all later |     |     |     |     |
| ------ | --------- | ----------- | --------- | --- | --- | --- | --- |
7,and8.
termsinthesequenceareequal.
equalityinthesequenceofnullspaces
8.2
| Suppose\mathcal{T} | \inℒ(\mathcal{V})andmisanonnegativeintegersuchthat |     |        |            |     |     |     |
| -------- | -------------------------------------- | --- | ------ | ---------- | --- | --- | --- |
|          |                                        |     | null\mathcal{T}m | =null\mathcal{T}m+1. |     |     |     |
Then
|                                  | null\mathcal{T}m                  | =null\mathcal{T}m+1 | =null\mathcal{T}m+2         |              | =null\mathcal{T}m+3 |      |     |
| -------------------------------- | ----------------------- | --------- | ----------------- | ------------ | --------- | ---- | --- |
|                                  |                         |           |                   |              |           | =⋯ . |     |
| Proof                            | Letkbeapositiveinteger. |           | Wewanttoprovethat |              |           |      |     |
|                                  |                         |           | null\mathcal{T}m+k          | =null\mathcal{T}m+k+1. |           |      |     |
| Wealreadyknowfrom8.1thatnull\mathcal{T}m+k |                         |           |                   | \subseteqnull\mathcal{T}m+k+1. |           |      |     |
Toprovetheinclusionintheotherdirection,supposev\innull\mathcal{T}m+k+1. Then
\mathcal{T}m+1(\mathcal{T}kv)=\mathcal{T}m+k+1v=0.
Hence
|     |     | \mathcal{T}kv\innull\mathcal{T}m+1 |     | =null\mathcal{T}m. |     |     |     |
| --- | --- | ------------ | --- | -------- | --- | --- | --- |
Thus\mathcal{T}m+kv=\mathcal{T}m(\mathcal{T}kv)=0,whichmeansthatv\innull\mathcal{T}m+k.
Thisimpliesthat
| null\mathcal{T}m+k+1 | \subseteqnull\mathcal{T}m+k,completingtheproof. |     |     |     |     |     |     |
| ---------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
The result above raises the question of whether there exists a nonnegative
| integermsuchthatnull\mathcal{T}m |     |     | =null\mathcal{T}m+1. |     |     |     |     |
| ---------------------- | --- | --- | ---------- | --- | --- | --- | --- |
Thenextresultshowsthatthisequality
holds at least when m equals the dimension of the vector space on which \mathcal{T}
operates.

| --- | --------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
nullspacesstopgrowing
8.3
| Suppose\mathcal{T} |                                | \inℒ(\mathcal{V}).    | Then         |     |              |     |          |         |
| -------- | ------------------------------ | --------- | ------------ | --- | ------------ | --- | -------- | ------- |
|          |                                | null\mathcal{T}dim\mathcal{V} | =null\mathcal{T}dim\mathcal{V}+1 |     | =null\mathcal{T}dim\mathcal{V}+2 |     | =⋯ .     |         |
|          | Weonlyneedtoprovethatnull\mathcal{T}dim\mathcal{V} |           |              |     | =null\mathcal{T}dim\mathcal{V}+1 |     | (by8.2). | Suppose |
Proof
| thisisnottrue. |     | Then,by8.1and8.2,wehave |                      |     |     |               |     |     |
| -------------- | --- | ----------------------- | -------------------- | --- | --- | ------------- | --- | --- |
|                |     | {0}=null\mathcal{T}0              | ⊊null\mathcal{T}1 ⊊⋯⊊null\mathcal{T}dim\mathcal{V} |     |     | ⊊null\mathcal{T}dim\mathcal{V}+1, |     |     |
where the symbol ⊊ means “contained in but not equal to”. At each of the
strictinclusionsinthechainabove,thedimensionincreasesbyatleast1. Thus
dimnull\mathcal{T}dim\mathcal{V}+1 \geqdim\mathcal{V}+1,acontradictionbecauseasubspaceof\mathcal{V} cannot
havealargerdimensionthandim\mathcal{V}.
Itisnottruethat\mathcal{V} = null\mathcal{T} \oplusrange\mathcal{T} forevery\mathcal{T} \in ℒ(\mathcal{V}). However,the
nextresultcanbeausefulsubstitute.
|     | isthedirectsumof |     | null\mathcal{T}dim\mathcal{V} | and | range\mathcal{T}dim\mathcal{V} |     |     |     |
| --- | ---------------- | --- | --------- | --- | ---------- | --- | --- | --- |
8.4 \mathcal{V}
| Suppose\mathcal{T} |            | \inℒ(\mathcal{V}). | Then                    |              |     |     |     |     |
| -------- | ---------- | ------ | ----------------------- | ------------ | --- | --- | --- | --- |
|          |            |        | \mathcal{V} =null\mathcal{T}dim\mathcal{V}            | \oplusrange\mathcal{T}dim\mathcal{V}. |     |     |     |     |
| Proof    | Letn=dim\mathcal{V}. |        | Firstweshowthat         |              |     |     |     |     |
| 8.5      |            |        | (null\mathcal{T}n)\cap(range\mathcal{T}n)={0}. |              |     |     |     |     |
Suppose v \in (null\mathcal{T}n)\cap(range\mathcal{T}n). Then \mathcal{T}nv = 0, and there exists u \in \mathcal{V}
such that v = \mathcal{T}nu. Applying \mathcal{T}n to both sides of the last equation shows that
\mathcal{T}nv = \mathcal{T}2nu. Hence \mathcal{T}2nu = 0, which implies that \mathcal{T}nu = 0 (by 8.3). Thus
$$v=\mathcal{T}nu=0,completingtheproofof8.5.$$
|     | Now8.5impliesthatnull\mathcal{T}n+range\mathcal{T}n          |     |     |     | isadirectsum(by1.46). |     |        | Also, |
| --- | ---------------------------------------- | --- | --- | --- | --------------------- | --- | ------ | ----- |
|     | dim(null\mathcal{T}n\oplusrange\mathcal{T}n)=dimnull\mathcal{T}n+dimrange\mathcal{T}n |     |     |     |                       |     | =dim\mathcal{V}, |       |
wherethefirstequalityabovecomesfrom3.94andthesecondequalitycomes
fromthefundamentaltheoremoflinearmaps(3.21). Theequationaboveimplies
| thatnull\mathcal{T}n\oplusrange\mathcal{T}n |     |     | =\mathcal{V}(see2.39),asdesired. |     |     |     |     |     |
| ------------------ | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
Foranimprovementoftheresultabove,see Exercise19.
| 8.6 | example: | \mathbf{F}3 =null\mathcal{T}3\oplusrange\mathcal{T}3 |           | for   | \mathcal{T} \inℒ(\mathbf{F}3) |     |     |     |
| --- | -------- | ------------------ | --------- | ----- | -------- | --- | --- | --- |
|     | Suppose\mathcal{T} | \inℒ(\mathbf{F}3)isdefinedby  |           |       |          |     |     |     |
|     |          |                    | \mathcal{T}(z ,z ,z | )=(4z | ,0,5z    | ).  |     |     |
|     |          |                    | 1 2       | 3     | 2        | 3   |     |     |

| --- | -------- | --- | ------------------------------ | --- | --- | --- | --- |
|           |      | ,0,0)∶z |              |     | )∶z       |     |           |
| --------- | ---- | ------- | ------------ | --- | --------- | --- | --------- |
| Thennull\mathcal{T} | ={(z |         | \in\mathbf{F}}andrange\mathcal{T} |     | ={(z ,0,z | ,z  | \in\mathbf{F}}. Thus |
|           |      | 1       | 1            |     | 1 3       | 1 3 |           |
null\mathcal{T} \caprange\mathcal{T} \neq {0}. Hencenull\mathcal{T} +range\mathcal{T} isnotadirectsum. Alsonote
\neq\mathbf{F}3. However,wehave\mathcal{T}3(z
| thatnull\mathcal{T}+range\mathcal{T} |     |     |     |     | ,z ,z )=(0,0,125z |     | ). Thus |
| ---------------- | --- | --- | --- | --- | ----------------- | --- | ------- |
|                  |     |     |     |     | 1 2 3             |     | 3       |
weseethat
| null\mathcal{T}3 |      |     | ,0)∶z      | range\mathcal{T}3 |          | )∶z |      |
| ------ | ---- | --- | ---------- | ------- | -------- | --- | ---- |
|        | ={(z | ,z  | ,z \in\mathbf{F}} and |         | ={(0,0,z |     | \in\mathbf{F}}. |
|        |      | 1 2 | 1 2        |         |          | 3   | 3    |
Hence\mathbf{F}3=null\mathcal{T}3\oplusrange\mathcal{T}3,asexpectedby8.4.
| Generalized |     | Eigenvectors |     |     |     |     |     |
| ----------- | --- | ------------ | --- | --- | --- | --- | --- |
Someoperatorsdonothaveenougheigenvectorstoleadtogooddescriptionsof
theirbehavior. Thusinthissubsectionweintroducetheconceptofgeneralized
eigenvectors,whichwillplayamajorroleinourdescriptionofthestructureofan
operator.
Tounderstandwhyweneedmorethaneigenvectors,let’sexaminethequestion
ofdescribinganoperatorbydecomposingitsdomainintoinvariantsubspaces. Fix
\mathcal{T} \inℒ(\mathcal{V}). Weseektodescribe\mathcal{T} byfindinga“nice”directsumdecomposition
,
|     |     |     | \mathcal{V} =\mathcal{V} \oplus⋯\oplus\mathcal{V} |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- |
1 n
whereeach\mathcal{V} isasubspaceof\mathcal{V}invariantunder\mathcal{T}. Thesimplestpossiblenonzero
k
invariantsubspacesareone-dimensional. Adecompositionasaboveinwhich
each\mathcal{V} isaone-dimensionalsubspaceof\mathcal{V} invariantunder\mathcal{T} ispossibleifand
k
onlyif\mathcal{V} hasabasisconsistingofeigenvectorsof\mathcal{T} (see5.55). Thishappensif
| andonlyif\mathcal{V} |        | hasaneigenspacedecomposition |                  |     |            |     |     |
| ---------- | ------ | ---------------------------- | ---------------- | --- | ---------- | --- | --- |
| 8.7        |        |                              | \mathcal{V} =\mathcal{E}(\lambda ,\mathcal{T})\oplus⋯\oplus\mathcal{E}(\lambda |     | ,\mathcal{T}),       |     |     |
|            |        |                              | 1                |     | m          |     |     |
| where      | \lambda ,…,\lambda | arethedistincteigenvaluesof\mathcal{T} |                  |     | (see5.55). |     |     |
|            | 1      | m                            |                  |     |            |     |     |
Thespectraltheoreminthepreviouschaptershowsthatif\mathcal{V}isaninnerproduct
space,thenadecompositionoftheform8.7holdsforeveryself-adjointoperator
if\mathbf{F} =\mathbf{R} andforeverynormaloperatorif\mathbf{F} =\mathbf{C}becauseoperatorsofthosetypes
| haveenougheigenvectorstoformabasisof\mathcal{V} |     |     |     |     | (see7.29and7.31). |     |     |
| ------------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- |
However, a decomposition of the form 8.7 may not hold for more general
operators,evenonacomplexvectorspace. Anexamplewasgivenbytheoperator
in5.57,whichdoesnothaveenougheigenvectorsfor8.7tohold. Generalized
eigenvectorsandgeneralizedeigenspaces,whichwenowintroduce,willremedy
thissituation.
| 8.8                    | definition: | generalizedeigenvector |                     |     |           |     |           |
| ---------------------- | ----------- | ---------------------- | ------------------- | --- | --------- | --- | --------- |
| Suppose\mathcal{T}               |             | \inℒ(\mathcal{V})and               | \lambdaisaneigenvalueof\mathcal{T}. |     | Avectorv  | \in\mathcal{V}  | iscalleda |
| generalizedeigenvector |             |                        | of\mathcal{T} correspondingto |     | \lambdaifv\neq0and |     |           |
\lambda\mathcal{I})kv=0
$$(\mathcal{T}-$$
forsomepositiveintegerk.

| --------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
| Anonzerovectorv\in\mathcal{V}  |     |     |                 | isageneral- |             |             |             |
| ------------------ | --- | --- | --------------- | ----------- | ----------- | ----------- | ----------- |
|                    |     |     |                 |             | Generalized | eigenvalues | are not de- |
| izedeigenvectorof\mathcal{T} |     |     | correspondingto | \lambda           |             |             |             |
finedbecausedoingsowouldnotlead
| ifandonlyif |     |     |     |     | toanythingnew. | Reason: | if (\mathcal{T}-\lambda\mathcal{I})k |
| ----------- | --- | --- | --- | --- | -------------- | ------- | ---------- |
isnotinjectiveforsomepositiveinte-
$$(\mathcal{T}- \lambda\mathcal{I})dim\mathcal{V}v=0,$$
gerk,then\mathcal{T}-\lambda\mathcal{I}isnotinjective,and
|     |     |     |     |     | hence | \lambdaisaneigenvalueof | \mathcal{T}.  |
| --- | --- | --- | --- | --- | ----- | ----------------- | --- |
asfollowsfromapplying8.1and8.3to
| theoperator\mathcal{T}- |     | \lambda\mathcal{I}. |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- |
As we know, an operator on a complex vector space may not have enough
eigenvectors to form a basis of the domain. The next result shows that on a
complexvectorspacethereareenoughgeneralizedeigenvectorstodothis.
8.9 abasisofgeneralizedeigenvectors
Suppose \mathbf{F} = \mathbf{C} and \mathcal{T} \in ℒ(\mathcal{V}). Then there is a basis of \mathcal{V} consisting of
generalizedeigenvectorsof\mathcal{T}.
Proof Let n = dim\mathcal{V}. We will use induction on n. To get started, note that
thedesiredresultholdsifn = 1becausetheneverynonzerovectorin\mathcal{V} isan
eigenvectorof\mathcal{T}.
| Now | suppose | n   | > 1 and | the de- |     |     |     |
| --- | ------- | --- | ------- | ------- | --- | --- | --- |
Thisstepiswhereweusethehypothesis
| sired result | holds | for  | all smaller   | values |       |                |         |
| ------------ | ----- | ---- | ------------- | ------ | ----- | -------------- | ------- |
|              |       |      |               |        | that\mathbf{F} | =\mathbf{C},becauseif \mathbf{F} | =\mathbf{R}then\mathcal{T} |
| of dim\mathcal{V}.     | Let   | \lambda be | an eigenvalue | of \mathcal{T}.  |       |                |         |
maynothaveanyeigenvalues.
| Applying8.4to\mathcal{T}- |     |     | \lambda\mathcal{I} showsthat |               |     |       |     |
| --------------- | --- | --- | ------------ | ------------- | --- | ----- | --- |
|                 |     |     | \mathcal{V} =null(\mathcal{T}-   | \lambda\mathcal{I})n\oplusrange(\mathcal{T}- |     | \lambda\mathcal{I})n. |     |
Ifnull(\mathcal{T}- \lambda\mathcal{I})n =\mathcal{V},theneverynonzerovectorin\mathcal{V} isageneralizedeigenvectorof\mathcal{T},andthusinthiscasethereisabasisof\mathcal{V} consistingofgeneralized
eigenvectorsof\mathcal{T}. Hencewecanassumethatnull(\mathcal{T}- \lambda\mathcal{I})n \neq\mathcal{V},whichimplies
\lambda\mathcal{I})n
| thatrange(\mathcal{T}- |     |     | \neq{0}. |     |     |     |     |
| ------------ | --- | --- | ----- | --- | --- | --- | --- |
Also,null(\mathcal{T}- \lambda\mathcal{I})n \neq{0},because \lambdaisaneigenvalueof\mathcal{T}. Thuswehave
|     |     |     | 0<dimrange(\mathcal{T}- |     | \lambda\mathcal{I})n |     |     |
| --- | --- | --- | ------------- | --- | ---- | --- | --- |
<n.
Furthermore,range(\mathcal{T}-\lambda\mathcal{I})nisinvariantunder\mathcal{T}[by5.18withp(z)=(z-\lambda)n].
Let\mathcal{S}\inℒ(range(\mathcal{T}- \lambda\mathcal{I})n)equal\mathcal{T} restrictedtorange(\mathcal{T}- \lambda\mathcal{I})n. Ourinduction
hypothesisappliedtotheoperator\mathcal{S}impliesthatthereisabasisofrange(\mathcal{T}-\lambda\mathcal{I})n
consisting of generalized eigenvectors of \mathcal{S}, which of course are generalized
Adjoiningthatbasisofrange(\mathcal{T}-\lambda\mathcal{I})ntoabasisofnull(\mathcal{T}-\lambda\mathcal{I})n
eigenvectorsof\mathcal{T}.
| givesabasisof\mathcal{V} |     | consistingofgeneralizedeigenvectorsof\mathcal{T}. |     |     |     |     |     |
| -------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
If\mathbf{F} = \mathbf{R} anddim\mathcal{V} > 1, thensomeoperatorson\mathcal{V} havethepropertythat
thereexistsabasisof\mathcal{V} consistingofgeneralizedeigenvectorsoftheoperator,
and(unlikewhathappenswhen\mathbf{F} =\mathbf{C})otheroperatorsdonothavethisproperty.
See Exercise11foranecessaryandsufficientconditionthatdetermineswhether
anoperatorhasthisproperty.

| -------- | ------------------------------ | --- | --- |
generalizedeigenvectorsofanoperatoron\mathbf{C}3
**8.10 例：** Define\mathcal{T} \inℒ(\mathbf{C}3)by
|     | \mathcal{T}(z ,z ,z )=(4z | ,0,5z ) |     |
| --- | --------------- | ------- | --- |
|     | 1 2 3           | 2 3     |     |
foreach(z ,z ,z )\in\mathbf{C}3. Aroutineuseofthedefinitionofeigenvalueshowsthat
| 1 2 3 |     |     |     |
| ----- | --- | --- | --- |
theeigenvaluesof\mathcal{T} are0and5. Furthermore,theeigenvectorscorrespondingto
theeigenvalue0arethenonzerovectorsoftheform(z ,0,0),andtheeigenvectors
correspondingtotheeigenvalue5arethenonzerovectorsoftheform(0,0,z ).
Hencethisoperatordoesnothaveenougheigenvectorstospanitsdomain\mathbf{C}3.
Wecomputethat\mathcal{T}3(z ,z ,z )=(0,0,125z ). Thus8.1and8.3implythatthe
|     | 1 2 3 | 3   |     |
| --- | ----- | --- | --- |
generalizedeigenvectorsof\mathcal{T} correspondingtotheeigenvalue0arethenonzero
| vectorsoftheform(z | ,z ,0). |     |     |
| ------------------ | ------- | --- | --- |
1 2
| Wealsohave(\mathcal{T}-5\mathcal{I})3(z | ,z ,z )=(-125z | +300z ,-125z | ,0). Thusthe |
| ------------------- | -------------- | ------------ | ------------ |
|                     | 1 2 3          | 1 2          | 2            |
generalizedeigenvectorsof\mathcal{T} correspondingtotheeigenvalue5arethenonzero
| vectorsoftheform(0,0,z | ).  |     |     |
| ---------------------- | --- | --- | --- |
Theparagraphsaboveshowthateachofthestandardbasisvectorsof\mathbf{C}3 isa
generalizedeigenvectorof\mathcal{T}. Thus\mathbf{C}3indeedhasabasisconsistingofgeneralized
eigenvectorsof\mathcal{T},aspromisedby8.9.
Ifvisaneigenvectorof\mathcal{T} \in ℒ(\mathcal{V}),thenthecorrespondingeigenvalue \lambdais
uniquelydeterminedbytheequation\mathcal{T}v= \lambdav,whichcanbesatisfiedbyonlyone
\lambda \in \mathbf{F} (becausev \neq 0). However,ifvisageneralizedeigenvectorof\mathcal{T},thenit
isnotobviousthattheequation(\mathcal{T}- \lambda\mathcal{I})dim\mathcal{V}v=0canbesatisfiedbyonlyone
\lambda\in\mathbf{F}. Fortunately,thenextresulttellsusthatalliswellonthisissue.
8.11 generalizedeigenvectorcorrespondstoauniqueeigenvalue
\inℒ(\mathcal{V}).
| Suppose\mathcal{T} | Theneachgeneralizedeigenvectorof\mathcal{T} |     | correspondsto |
| -------- | --------------------------------- | --- | ------------- |
onlyoneeigenvalueof\mathcal{T}.
Proof Supposev\in\mathcal{V} isageneralizedeigenvectorof\mathcal{T} correspondingtoeigenvalues\alphaand\lambdaof\mathcal{T}. Letmbethesmallestpositiveintegersuchthat(\mathcal{T}-\alpha\mathcal{I})mv=0.
| Letn=dim\mathcal{V}. Then |     |     |     |
| --------------- | --- | --- | --- |
$$0=(\mathcal{T}- \lambda\mathcal{I})nv$$
\lambda)\mathcal{I})nv
=((\mathcal{T}-\alpha\mathcal{I})+(\alpha-
n
|     | = \sumb (\alpha- \lambda)n-k(\mathcal{T}-\alpha\mathcal{I})kv, |     |     |
| --- | ----------------------- | --- | --- |
k
$$k=0$$
whereb =1andthevaluesoftheotherbinomialcoefficientsb donotmatter.
| 0   |     |     | k   |
| --- | --- | --- | --- |
Applytheoperator(\mathcal{T}-\alpha\mathcal{I})m-1 tobothsidesoftheequationabove,getting
$$0=(\alpha- \lambda)n(\mathcal{T}-\alpha\mathcal{I})m-1v.$$
Because(\mathcal{T}-\alpha\mathcal{I})m-1v\neq0,theequationaboveimpliesthat\alpha=
\lambda,asdesired.

| --- | --------- | --- | -------------------------------------------- | --- | --- | --- |
Wesawearlier(5.11)thateigenvectorscorrespondingtodistincteigenvalues
arelinearlyindependent. Nowweproveasimilarresultforgeneralizedeigenvectors,withaproofthatroughlyfollowsthepatternoftheproofofthatearlier
result.
8.12 linearlyindependentgeneralizedeigenvectors
Suppose that \mathcal{T} \in ℒ(\mathcal{V}). Then every list of generalized eigenvectors of \mathcal{T}
| correspondingtodistincteigenvaluesof\mathcal{T} |     |     |     |     | islinearlyindependent. |     |
| ------------------------------------- | --- | --- | --- | --- | ---------------------- | --- |
Proof Supposethedesiredresultisfalse. Thenthereexistsasmallestpositive
integermsuchthatthereexistsalinearlydependentlistv ,…,v ofgeneralized
1 m
eigenvectorsof\mathcal{T} correspondingtodistincteigenvalues \lambda ,…,\lambda of\mathcal{T} (notethat
1 m
m\geq2becauseageneralizedeigenvectoris,bydefinition,nonzero). Thusthere
exista ,…,a \in\mathbf{F},noneofwhichare0(becauseoftheminimalityofm),such
|     | 1   | m   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
that
|     |     |     |     | a v +⋯+a | v =0. |     |
| --- | --- | --- | --- | -------- | ----- | --- |
|     |     |     |     | 1 1      | m m   |     |
Letn=dim\mathcal{V}. Apply(\mathcal{T}-\lambda \mathcal{I})ntobothsidesoftheequationabove,getting
m
| 8.13     |             | a (\mathcal{T}- | \lambda   | \mathcal{I})nv +⋯+a  | (\mathcal{T}- \lambda \mathcal{I})nv | =0. |
| -------- | ----------- | ----- | --- | ---------- | ---------- | --- |
|          |             | 1     | m   | 1 m-1      | m          | m-1 |
| Supposek | \in{1,…,m-1}. |       |     | Then       |            |     |
|          |             |       |     | (\mathcal{T}- \lambda \mathcal{I})nv | \neq0         |     |
|          |             |       |     | m          | k          |     |
becauseotherwisev wouldbeageneralizedeigenvectorof\mathcal{T} correspondingto
k
thedistincteigenvalues \lambda and \lambda ,whichwouldcontradict8.11. However,
|     |     |           |     | k m          |           |             |
| --- | --- | --------- | --- | ------------ | --------- | ----------- |
|     | (\mathcal{T}- | \lambda \mathcal{I})n((\mathcal{T}- |     | \lambda \mathcal{I})nv )=(\mathcal{T}- | \lambda \mathcal{I})n((\mathcal{T}- | \lambda \mathcal{I})nv )=0. |
|     |     | k         |     | m k          | m         | k k         |
Thusthelasttwodisplayedequationsshowthat(\mathcal{T}-\lambda \mathcal{I})nv isageneralized
m k
| eigenvectorof\mathcal{T} |     | correspondingtotheeigenvalue |     |     | \lambda . | Hence |
| -------------- | --- | ---------------------------- | --- | --- | --- | ----- |
k
|     |     |     |     | \mathcal{I})nv ,…,(\mathcal{T}- | \mathcal{I})nv |     |
| --- | --- | --- | --- | ----------- | ---- | --- |
|     |     |     | (\mathcal{T}- | \lambda m 1       | \lambda m  | m-1 |
isalinearlydependentlist(by8.13)ofm-1generalizedeigenvectorscorrespondingtodistincteigenvalues,contradictingtheminimalityofm. Thiscontradiction
completestheproof.
| Nilpotent                   |             | Operators |     |                         |     |     |
| --------------------------- | ----------- | --------- | --- | ----------------------- | --- | --- |
| 8.14                        | definition: | nilpotent |     |                         |     |     |
| Anoperatoriscallednilpotent |             |           |     | ifsomepowerofitequals0. |     |     |
Thusanoperator\mathcal{T} \inℒ(\mathcal{V})isnilpotentifandonlyifeverynonzerovectorin
\mathcal{V} isageneralizedeigenvectorof\mathcal{T} correspondingtotheeigenvalue0.

| -------- | ------------------------------ | --- | --- | --- | --- |
nilpotentoperators
**8.15 例：** \inℒ(\mathbf{F}4)definedby
$$(a) Theoperator\mathcal{T}$$
|                      |     | \mathcal{T}(z ,z ,z | ,z )=(0,0,z | ,z ) |     |
| -------------------- | --- | --------- | ----------- | ---- | --- |
|                      |     | 1 2       | 3 4         | 1 2  |     |
| isnilpotentbecause\mathcal{T}2 |     | =0.       |             |      |     |
Theoperatoron\mathbf{F}3
| (b) |     | whosematrix(withrespecttothestandardbasis)is |          |     |     |
| --- | --- | -------------------------------------------- | -------- | --- | --- |
|     |     | -3                                           | 9 0      |     |     |
|     |     | ⎛                                            | ⎞        |     |     |
|     |     | ⎜ ⎜ -7                                       | 9 6 ⎟ ⎟  |     |     |
|     |     | ⎜                                            | ⎟        |     |     |
|     |     | ⎝                                            | 4 0 -6 ⎠ |     |     |
isnilpotent,ascanbeshownbycubingthematrixabovetogetthezeromatrix.
$$(c) Theoperatorofdifferentiationon𝒫 (\mathbf{R})isnilpotentbecausethe(m+1)th$$
m
derivativeofeverypolynomialofdegreeatmostmequals0. Notethaton
thisspaceofdimensionm+1,weneedtoraisethenilpotentoperatortothe
powerm+1togetthe0operator.
Thenextresultshowsthatwhenrais-
|                 |          |             | The Latinword | nilmeansnothingor |       |
| --------------- | -------- | ----------- | ------------ | ----------------- | ----- |
| ing a nilpotent | operator | to a power, | we           |                   |       |
|                 |          |             | zero; the    | Latin word potens | means |
neverneedtouseapowerhigherthanthe havingpower. Thusnilpotentliterally
| dimension | of the space. | For a slightly |     |     |     |
| --------- | ------------- | -------------- | --- | --- | --- |
meanshavingapowerthatiszero.
strongerresult,see Exercise18.
8.16 nilpotentoperatorraisedtodimensionofdomainis0
| Suppose\mathcal{T} | \inℒ(\mathcal{V})isnilpotent. | Then\mathcal{T}dim\mathcal{V} | =0. |     |     |
| -------- | ----------------- | --------- | --- | --- | --- |
Proof Because\mathcal{T} isnilpotent,thereexistsapositiveintegerksuchthat\mathcal{T}k =0.
Thusnull\mathcal{T}k =\mathcal{V}. Now8.1and8.3implythatnull\mathcal{T}dim\mathcal{V} =\mathcal{V}. Thus\mathcal{T}dim\mathcal{V} =0.
8.17 eigenvaluesofnilpotentoperator
| Suppose\mathcal{T} | \inℒ(\mathcal{V}). |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
$$(a) If \mathcal{T} is nilpotent, then 0 is an eigenvalue of \mathcal{T} and \mathcal{T} has no other$$
eigenvalues.
| (b) If\mathbf{F} | =\mathbf{C} and0istheonlyeigenvalueof\mathcal{T},then\mathcal{T} |     |     | isnilpotent. |     |
| ------- | ----------------------------------- | --- | --- | ------------ | --- |
Proof
$$(a) Toprove(a),suppose\mathcal{T} isnilpotent. Hencethereisapositiveintegermsuch$$
that\mathcal{T}m = 0. Thisimpliesthat\mathcal{T} isnotinjective. Thus0isaneigenvalue
of\mathcal{T}.

Section8A Generalized Eigenvectorsand Nilpotent Operators 305
Toshowthat\mathcal{T} hasnoothereigenvalues, suppose \lambdaisaneigenvalueof\mathcal{T}.
Thenthereexistsanonzerovectorv\in\mathcal{V} suchthat
\lambdav=\mathcal{T}v.
Repeatedlyapplying\mathcal{T} tobothsidesofthisequationshowsthat
\lambdamv=\mathcal{T}mv=0.
Thus \lambda=0,asdesired.
$$(b) Suppose\mathbf{F} =\mathbf{C} and0istheonlyeigenvalueof\mathcal{T}. By5.27(b),theminimal$$
polynomialof\mathcal{T} equalszmforsomepositiveintegerm. Thus\mathcal{T}m =0. Hence
\mathcal{T} isnilpotent.
Exercise23showsthatthehypothesisthat\mathbf{F} =\mathbf{C} cannotbedeletedin(b)of
theresultabove.
Givenanoperatoron\mathcal{V},wewanttofindabasisof\mathcal{V} suchthatthematrixof
theoperatorwithrespecttothisbasisisassimpleaspossible,meaningthatthe
matrixcontainsmany0’s. Thenextresultshowsthatif\mathcal{T}isnilpotent,thenwecan
chooseabasisof\mathcal{V} suchthatthematrixof\mathcal{T} withrespecttothisbasishasmore
thanhalfofitsentriesequalto0. Laterinthischapterwewilldoevenbetter.
8.18 minimalpolynomialandupper-triangularmatrixofnilpotentoperator
Suppose\mathcal{T} \inℒ(\mathcal{V}). Thenthefollowingareequivalent.
$$(a) \mathcal{T} isnilpotent.$$
$$(b) Theminimalpolynomialof\mathcal{T} iszm forsomepositiveintegerm.$$
$$(c) Thereisabasisof\mathcal{V} withrespecttowhichthematrixof\mathcal{T} hastheform$$
0 ∗
⎛ ⎞
⎜ ⎟
⎜ ⎜ ⋱ ⎟ ⎟ ,
⎝ 0 0 ⎠
whereallentriesonandbelowthediagonalequal0.
Proof Suppose(a)holds,so\mathcal{T} isnilpotent. Thusthereexistsapositiveinteger
n such that \mathcal{T}n = 0. Now 5.29 implies that zn is a polynomial multiple of the
minimal polynomial of \mathcal{T}. Thus the minimal polynomial of \mathcal{T} is zm for some
positiveintegerm,provingthat(a)implies(b).
Nowsuppose(b)holds,sotheminimalpolynomialof\mathcal{T}iszmforsomepositive
integerm. Thisimplies,by5.27(a),that0(whichistheonlyzeroofzm)isthe
onlyeigenvalueof\mathcal{T}. Thisfurtherimplies,by5.44,thatthereisabasisof\mathcal{V} with
respecttowhichthematrixof\mathcal{T} isuppertriangular. Thisalsoimplies,by5.41,
thatallentriesonthediagonalofthismatrixare0,provingthat(b)implies(c).
Nowsuppose(c)holds. Then5.40impliesthat\mathcal{T}dim\mathcal{V} =0. Thus\mathcal{T}isnilpotent,
provingthat(c)implies(a).

306 Chapter 8 Operatorson Complex Vector Spaces
Exercises 8A
1 Suppose\mathcal{T} \inℒ(\mathcal{V}). Provethatifdimnull\mathcal{T}4 =8anddimnull\mathcal{T}6 =9,then
dimnull\mathcal{T}m =9forallintegersm\geq5.
2 Suppose \mathcal{T} \in ℒ(\mathcal{V}), m is a positive integer, v \in \mathcal{V}, and \mathcal{T}m-1v \neq 0 but
\mathcal{T}mv=0. Provethatv,\mathcal{T}v,\mathcal{T}2v,…,\mathcal{T}m-1vislinearlyindependent.
Theresultinthisexerciseisusedintheproofof8.45.
3 Suppose\mathcal{T} \inℒ(\mathcal{V}). Provethat
\mathcal{V} =null\mathcal{T}\oplusrange\mathcal{T} ⟺ null\mathcal{T}2 =null\mathcal{T}.
4 Suppose\mathcal{T} \inℒ(\mathcal{V}), \lambda\in\mathbf{F},andmisapositiveintegersuchthattheminimal
polynomialof\mathcal{T} isapolynomialmultipleof(z- \lambda)m. Provethat
dimnull(\mathcal{T}- \lambda\mathcal{I})m \geqm.
5 Suppose\mathcal{T} \inℒ(\mathcal{V})andmisapositiveinteger. Provethat
dimnull\mathcal{T}m \leqmdimnull\mathcal{T}.
Hint:Exercise21in Section3Bmaybeuseful.
6 Suppose\mathcal{T} \inℒ(\mathcal{V}). Showthat
\mathcal{V} =range\mathcal{T}0 \supseteqrange\mathcal{T}1 \supseteq⋯\supseteqrange\mathcal{T}k \supseteqrange\mathcal{T}k+1 \supseteq⋯ .
7 Suppose\mathcal{T} \inℒ(\mathcal{V})andmisanonnegativeintegersuchthat
range\mathcal{T}m =range\mathcal{T}m+1.
Provethatrange\mathcal{T}k =range\mathcal{T}m forallk >m.
8 Suppose\mathcal{T} \inℒ(\mathcal{V}). Provethat
range\mathcal{T}dim\mathcal{V} =range\mathcal{T}dim\mathcal{V}+1 =range\mathcal{T}dim\mathcal{V}+2 =⋯ .
9 Suppose\mathcal{T} \inℒ(\mathcal{V})andmisanonnegativeinteger. Provethat
null\mathcal{T}m =null\mathcal{T}m+1 ⟺ range\mathcal{T}m =range\mathcal{T}m+1.
10 Define\mathcal{T} \in ℒ(\mathbf{C}2)by\mathcal{T}(w,z) = (z,0). Findallgeneralizedeigenvectors
of\mathcal{T}.
11 Suppose that \mathcal{T} \in ℒ(\mathcal{V}). Prove that there is a basis of \mathcal{V} consisting of
generalizedeigenvectorsof\mathcal{T} ifandonlyiftheminimalpolynomialof\mathcal{T}
equals(z- \lambda )⋯(z- \lambda )forsome \lambda ,…,\lambda \in\mathbf{F}.
1 m 1 m
Assume\mathbf{F} =\mathbf{R}becausethecase\mathbf{F} =\mathbf{C}followsfrom5.27(b)and8.9.
Thisexercisestatesthattheconditionfortheretobeabasisof \mathcal{V}consisting
ofgeneralizedeigenvectorsof \mathcal{T}isthesameastheconditionfortheretobe
abasiswithrespecttowhich\mathcal{T}hasanupper-triangularmatrix(see5.44).
Caution: If \mathcal{T} has an upper-triangular matrix with respect to a basis
v ,…,v of \mathcal{V}, then v is an eigenvector of \mathcal{T} but it is not necessarily
1 n 1
truethatv ,…,v aregeneralizedeigenvectorsof \mathcal{T}.
2 n

| --------- | -------------------------------------------- | --- | --- | --- |
12 Suppose\mathcal{T} \inℒ(\mathcal{V})issuchthateverynonzerovectorin\mathcal{V} isageneralized
eigenvectorof\mathcal{T}. Provethatthereexists \lambda\in\mathbf{F} suchthat\mathcal{T}- \lambda\mathcal{I} isnilpotent.
13 Suppose\mathcal{S},\mathcal{T} \inℒ(\mathcal{V})and\mathcal{S}\mathcal{T} isnilpotent. Provethat\mathcal{T}\mathcal{S}isnilpotent.
14 Suppose\mathcal{T} \inℒ(\mathcal{V})isnilpotentand\mathcal{T} \neq0. Prove\mathcal{T} isnotdiagonalizable.
15 Suppose\mathbf{F} =\mathbf{C}and\mathcal{T} \inℒ(\mathcal{V}). Provethat\mathcal{T}isdiagonalizableifandonlyif
| everygeneralizedeigenvectorof\mathcal{T} |     | isaneigenvectorof\mathcal{T}. |     |     |
| ------------------------------ | --- | ------------------- | --- | --- |
For\mathbf{F} =\mathbf{C},thisexerciseaddsanotherequivalencetothelistofconditions
fordiagonalizabilityin5.55.
$$(a) Giveanexampleofnilpotentoperators\mathcal{S},\mathcal{T} onthesamevectorspace$$
| suchthatneither\mathcal{S}+\mathcal{T} | nor\mathcal{S}\mathcal{T}                  | isnilpotent. |                   |     |
| ------------------ | ---------------------- | ------------ | ----------------- | --- |
| (b) Suppose\mathcal{S},\mathcal{T}     | \inℒ(\mathcal{V})arenilpotentand\mathcal{S}\mathcal{T} |              | =\mathcal{T}\mathcal{S}. Provethat\mathcal{S}+\mathcal{T} | and |
\mathcal{S}\mathcal{T} arenilpotent.
\inℒ(\mathcal{V})isnilpotentandmisapositiveintegersuchthat\mathcal{T}m
| 17 Suppose\mathcal{T} |     |     |     | =0. |
| ----------- | --- | --- | --- | --- |
isinvertibleandthat(\mathcal{I}-\mathcal{T})-1 =\mathcal{I}+\mathcal{T}+⋯+\mathcal{T}m-1.
| (a) Provethat\mathcal{I}-\mathcal{T}                            |                                       |                       |     |     |
| ------------------------------------------- | ------------------------------------- | --------------------- | --- | --- |
| (b) Explainhowyouwouldguesstheformulaabove. |                                       |                       |     |     |
| 18 Suppose\mathcal{T}                                 | \inℒ(\mathcal{V})isnilpotent.                     | Provethat\mathcal{T}1+dimrange\mathcal{T} | =0. |     |
| If dimrange\mathcal{T}                                | <dim\mathcal{V}-1,thenthisexerciseimproves8.16. |                       |     |     |
| 19 Suppose\mathcal{T}                                 | \inℒ(\mathcal{V})isnotnilpotent.                  | Showthat              |     |     |
\mathcal{V} =null\mathcal{T}dim\mathcal{V}-1\oplusrange\mathcal{T}dim\mathcal{V}-1.
Foroperatorsthatarenotnilpotent,thisexerciseimproves8.4.
20 Suppose\mathcal{V} isaninnerproductspaceand\mathcal{T} \inℒ(\mathcal{V})isnormalandnilpotent.
| Provethat\mathcal{T} | =0. |     |     |     |
| ---------- | --- | --- | --- | --- |
21 Suppose\mathcal{T} \inℒ(\mathcal{V})issuchthatnull\mathcal{T}dim\mathcal{V}-1 \neqnull\mathcal{T}dim\mathcal{V}. Provethat\mathcal{T} is
nilpotentandthatdimnull\mathcal{T}k
|     |     | =kforeveryintegerkwith0\leqk | \leqdim\mathcal{V}. |     |
| --- | --- | ------------------------- | ------ | --- |
Suppose \mathcal{T} \in ℒ(\mathbf{C}5) is such that range\mathcal{T}4 \neq range\mathcal{T}5. Prove that \mathcal{T} is
nilpotent.
23 Giveanexampleofanoperator\mathcal{T} onafinite-dimensionalrealvectorspace
| suchthat0istheonlyeigenvalueof\mathcal{T} |     | but\mathcal{T} | isnotnilpotent. |     |
| ------------------------------- | --- | ---- | --------------- | --- |
Thisexerciseshowsthattheimplication(b) ⟹ (a)in8.17doesnothold
| withoutthehypothesisthat\mathbf{F} |     | =\mathbf{C}. |     |     |
| ------------------------- | --- | --- | --- | --- |
Foreachitemin Example8.15,findabasisofthedomainvectorspacesuch
thatthematrixofthenilpotentoperatorwithrespecttothatbasishasthe
upper-triangularformpromisedby8.18(c).
25 Supposethat\mathcal{V} isaninnerproductspaceand\mathcal{T} \inℒ(\mathcal{V})isnilpotent. Show
thatthereisanorthonormalbasisof\mathcal{V} withrespecttowhichthematrixof
\mathcal{T} hastheupper-triangularformpromisedby8.18(c).

| --- | -------- | --- | ------------------------------ | --- | --- | --- | --- | --- |
| 8B          | Generalized |             | Eigenspace |     | Decomposition |     |     |     |
| ----------- | ----------- | ----------- | ---------- | --- | ------------- | --- | --- | --- |
| Generalized |             | Eigenspaces |            |     |               |     |     |     |
generalizedeigenspace,\mathcal{G}(\lambda,\mathcal{T})
**8.19 定义：** Suppose\mathcal{T} \inℒ(\mathcal{V})and \lambda\in\mathbf{F}. Thegeneralizedeigenspaceof\mathcal{T} correspondingto \lambda,denotedby\mathcal{G}(\lambda,\mathcal{T}),isdefinedby
|     | \mathcal{G}(\lambda,\mathcal{T})={v\in\mathcal{V} |     |     | ∶(\mathcal{T}- \lambda\mathcal{I})kv=0forsomepositiveintegerk}. |     |     |     |     |
| --- | ----------- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
Thus\mathcal{G}(\lambda,\mathcal{T})isthesetofgeneralizedeigenvectorsof\mathcal{T} correspondingto \lambda,
alongwiththe0vector.
Becauseeveryeigenvectorof\mathcal{T} isageneralizedeigenvectorof\mathcal{T} (takek =1
inthedefinitionofgeneralizedeigenvector),eacheigenspaceiscontainedinthe
correspondinggeneralizedeigenspace. Inotherwords,if\mathcal{T} \inℒ(\mathcal{V})and \lambda\in\mathbf{F},
then\mathcal{E}(\lambda,\mathcal{T})\subseteq\mathcal{G}(\lambda,\mathcal{T}).
The next result implies that if \mathcal{T} \in ℒ(\mathcal{V}) and \lambda \in \mathbf{F}, then the generalized
eigenspace\mathcal{G}(\lambda,\mathcal{T})isasubspaceof\mathcal{V}
$$(becausethenullspaceofeachlinearmap$$
on\mathcal{V} isasubspaceof\mathcal{V}).
8.20 descriptionofgeneralizedeigenspaces
|          |                          | \inℒ(\mathcal{V})and |     | Then\mathcal{G}(\lambda,\mathcal{T})=null(\mathcal{T}- |                              |     | \lambda\mathcal{I})dim\mathcal{V}. |      |
| -------- | ------------------------ | -------- | --- | ------------------ | ---------------------------- | --- | -------- | ---- |
| Suppose\mathcal{T} |                          |          |     | \lambda\in\mathbf{F}.               |                              |     |          |      |
|          | Supposev\innull(\mathcal{T}-\lambda\mathcal{I})dim\mathcal{V}. |          |     |                    | Thedefinitionsimplyv\in\mathcal{G}(\lambda,\mathcal{T}). |     |          | Thus |
Proof
| \mathcal{G}(\lambda,\mathcal{T})\supseteqnull(\mathcal{T}- |     |     | \lambda\mathcal{I})dim\mathcal{V}. |     |     |     |     |     |
| -------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
Conversely, suppose v \in \mathcal{G}(\lambda,\mathcal{T}). Thus there is a positive integer k such
that v \in null(\mathcal{T} - \lambda\mathcal{I})k. From 8.1 and 8.3 (with \mathcal{T} - \lambda\mathcal{I} replacing \mathcal{T}), we get
v\innull(\mathcal{T}-\lambda\mathcal{I})dim\mathcal{V}. Thus\mathcal{G}(\lambda,\mathcal{T})\subseteqnull(\mathcal{T}-\lambda\mathcal{I})dim\mathcal{V},completingtheproof.
generalizedeigenspacesofanoperatoron\mathbf{C}3
**8.21 例：** |     | Define\mathcal{T}                                  | \inℒ(\mathbf{C}3)by |     |           |       |                     |     |     |
| --- | ---------------------------------------- | -------- | --- | --------- | ----- | ------------------- | --- | --- |
|     |                                          |          |     | \mathcal{T}(z ,z ,z | )=(4z | ,0,5z ).            |     |     |
|     |                                          |          |     | 1 2       | 3     | 2 3                 |     |     |
|     | In Example8.10,wesawthattheeigenvaluesof\mathcal{T} |          |     |           |       | are0and5,andwefound |     |     |
thecorrespondingsetsofgeneralizedeigenvectors. Takingtheunionofthosesets
with{0},wehave
|            |     |     | ,0)∶z |        |     |                | )∶z |      |
| ---------- | --- | --- | ----- | ------ | --- | -------------- | --- | ---- |
| \mathcal{G}(0,\mathcal{T})={(z |     | ,z  |       | ,z \in\mathbf{C}} | and | \mathcal{G}(5,\mathcal{T})={(0,0,z |     | \in\mathbf{C}}. |
|            |     | 1   | 2     | 1 2    |     |                | 3   | 3    |
Notethat\mathbf{C}3=\mathcal{G}(0,\mathcal{T})\oplus\mathcal{G}(5,\mathcal{T}).

| --- | --------- | --- | ---------------------------------- | --- | --- | --- | --- |
In Example8.21,thedomainspace\mathbf{C}3
isthedirectsumofthegeneralized
eigenspacesoftheoperator\mathcal{T} inthatexample. Ournextresultshowsthatthis
behaviorholdsingeneral. Specifically,thefollowingmajorresultshowsthatif
\mathbf{F} = \mathbf{C} and\mathcal{T} \in ℒ(\mathcal{V}),then\mathcal{V} isthedirectsumofthegeneralizedeigenspaces
of\mathcal{T},eachofwhichisinvariantunder\mathcal{T} andonwhich\mathcal{T} isanilpotentoperator
plusascalarmultipleoftheidentity. Thusthenextresultachievesourgoalof
decomposing\mathcal{V} intoinvariantsubspacesonwhich\mathcal{T} hasaknownbehavior.
Aswewillsee,theprooffollowsfromputtingtogetherwhatwehavelearned
aboutgeneralizedeigenspacesandthenusingourresultthatforeachoperator
\mathcal{T} \inℒ(\mathcal{V}),thereexistsabasisof\mathcal{V} consistingofgeneralizedeigenvectorsof\mathcal{T}.
8.22 generalizedeigenspacedecomposition
| Suppose\mathbf{F} |     | and\mathcal{T} | ℒ(\mathcal{V}). | Let ,…,\lambda | bethedistincteigenvalues |     |     |
| -------- | --- | ---- | ----- | -------- | ------------------------ | --- | --- |
|          | = \mathbf{C} |      | \in     | \lambda 1      | m                        |     |     |
of\mathcal{T}. Then
| (a) \mathcal{G}(\lambda | ,\mathcal{T})isinvariantunder\mathcal{T} |     |     | foreachk | =1,…,m; |     |     |
| ------- | -------------------- | --- | --- | -------- | ------- | --- | --- |
k
| (b) (\mathcal{T}- | \lambda \mathcal{I})| | isnilpotentforeachk |     | =1,…,m; |     |     |     |
| ------- | ----- | ------------------- | --- | ------- | --- | --- | --- |
k \mathcal{G}(\lambda k ,\mathcal{T})
| (c) \mathcal{V} =\mathcal{G}(\lambda | ,\mathcal{T})\oplus⋯\oplus\mathcal{G}(\lambda |     | ,\mathcal{T}). |     |     |     |     |
| ---------- | --------- | --- | ---- | --- | --- | --- | --- |
|            | 1         |     | m    |     |     |     |     |
Proof
\in{1,…,m}.
| (a) Supposek |     |     | Then8.20showsthat |        |         |     |     |
| ------------ | --- | --- | ----------------- | ------ | ------- | --- | --- |
|              |     |     | ,\mathcal{T})=null(\mathcal{T}-       |        | \mathcal{I})dim\mathcal{V}. |     |     |
|              |     |     | \mathcal{G}(\lambda               |        | \lambda       |     |     |
|              |     |     | k                 |        | k       |     |     |
|              |     |     |                   | )dim\mathcal{V}, |         |     | ,\mathcal{T}) |
Thus 5.18, with p(z) = (z - \lambda k implies that \mathcal{G}(\lambda k is invariant
under\mathcal{T},proving(a).
$$(b) Supposek \in{1,…,m}. Ifv\in\mathcal{G}(\lambda ,\mathcal{T}),then(\mathcal{T}-\lambda \mathcal{I})dim\mathcal{V}v=0(by8.20).$$
|      |         |       |        | k          |      | k     |               |
| ---- | ------- | ----- | ------ | ---------- | ---- | ----- | ------------- |
| Thus | ((\mathcal{T} - \lambda | \mathcal{I})|   | ) dim\mathcal{V} | = 0. Hence | (\mathcal{T} - | \lambda \mathcal{I})| | is nilpotent, |
|      |         | k \mathcal{G}(\lambda | ,\mathcal{T})    |            |      | k \mathcal{G}(\lambda | ,\mathcal{T})           |
|      |         |       | k      |            |      |       | k             |
proving(b).
| (c) Toshowthat\mathcal{G}(\lambda |     | ,\mathcal{T})+⋯+\mathcal{G}(\lambda |     | ,\mathcal{T})isadirectsum,suppose |     |     |     |
| ----------------- | --- | --------- | --- | ----------------------- | --- | --- | --- |
|                   |     | 1         |     | m                       |     |     |     |
|                   |     |           | v   | +⋯+v                    | =0, |     |     |
|                   |     |           | 1   | m                       |     |     |     |
where each v is in \mathcal{G}(\lambda ,\mathcal{T}). Because generalized eigenvectors of \mathcal{T} cor-
|     | k   |     | k   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
respondingtodistincteigenvaluesarelinearlyindependent(by8.12), this
| impliesthateachv |     | equals0. | Thus\mathcal{G}(\lambda | ,\mathcal{T})+⋯+\mathcal{G}(\lambda |     | ,\mathcal{T})isadirectsum |     |
| ---------------- | --- | -------- | ------- | --------- | --- | --------------- | --- |
|                  |     | k        |         | 1         |     | m               |     |
$$(by1.45).$$
Finally,eachvectorin\mathcal{V} canbewrittenasafinitesumofgeneralizedeigen-
| vectorsof\mathcal{T} | (by8.9). |     | Thus   |           |      |     |     |
| ---------- | -------- | --- | ------ | --------- | ---- | --- | --- |
|            |          |     | \mathcal{V} =\mathcal{G}(\lambda | ,\mathcal{T})\oplus⋯\oplus\mathcal{G}(\lambda | ,\mathcal{T}), |     |     |
|            |          |     |        | 1         | m    |     |     |
proving(c).
| Fortheanalogousresultwhen\mathbf{F} |     |     |     | =\mathbf{R},see Exercise8. |     |     |     |
| -------------------------- | --- | --- | --- | ---------------- | --- | --- | --- |

| -------- | ------------------------------ | --- | --- | --- |
| Multiplicity | of an Eigenvalue |     |     |     |
| ------------ | ---------------- | --- | --- | --- |
If\mathcal{V} isacomplexvectorspaceand\mathcal{T} \inℒ(\mathcal{V}),thenthedecompositionof\mathcal{V} providedbythegeneralizedeigenspacedecomposition(8.22)canbeapowerfultool.
Thedimensionsofthesubspacesinvolvedinthisdecompositionaresufficiently
importanttogetaname,whichisgiveninthenextdefinition.
| 8.23 definition: | multiplicity |     |     |     |
| ---------------- | ------------ | --- | --- | --- |
Suppose\mathcal{T} \inℒ(\mathcal{V}). Themultiplicityofaneigenvalue \lambdaof\mathcal{T} isdefinedto
•
bethedimensionofthecorrespondinggeneralizedeigenspace\mathcal{G}(\lambda,\mathcal{T}).
| • Inotherwords,themultiplicityofaneigenvalue |     |     |     | \lambdaof\mathcal{T} equals |
| -------------------------------------------- | --- | --- | --- | ----------- |
\lambda\mathcal{I})dim\mathcal{V}.
dimnull(\mathcal{T}-
The second bullet point above holds because \mathcal{G}(\lambda,\mathcal{T}) = null(\mathcal{T} - \lambda\mathcal{I})dim\mathcal{V}
$$(see8.20).$$
| 8.24 example: | multiplicityofeacheigenvalueofanoperator |       |             |            |
| ------------- | ---------------------------------------- | ----- | ----------- | ---------- |
| Suppose\mathcal{T}      | \inℒ(\mathbf{C}3)isdefinedby                        |       |             |            |
|               | \mathcal{T}(z ,z ,z                                | )=(6z | +3z +4z ,6z | +2z ,7z ). |
|               | 1 2                                      | 3     | 1 2 3       | 2 3 3      |
| Thematrixof\mathcal{T}  | (withrespecttothestandardbasis)is        |       |             |            |
|               |                                          |       | 6 3 4       |            |
|               |                                          | ⎛     | ⎞           |            |
|               |                                          | ⎜     | ⎟           |            |
|               |                                          | ⎜     | 0 6 2 ⎟ ⎟.  |            |
⎜
|     |     |     | 0 0 7 |     |
| --- | --- | --- | ----- | --- |
|     |     | ⎝   | ⎠     |     |
Theeigenvaluesof\mathcal{T} arethediagonalentries6and7,asfollowsfrom5.41. You
| canverifythatthegeneralizedeigenspacesof\mathcal{T} |     |     |     | areasfollows:          |
| ----------------------------------------- | --- | --- | --- | ---------------------- |
| \mathcal{G}(6,\mathcal{T})=span((1,0,0),(0,1,0))              |     |     | and | \mathcal{G}(7,\mathcal{T})=span((10,2,1)). |
Thustheeigenvalue6hasmultiplicity2
Inthisexample,themultiplicityofeach
| and the eigenvalue | 7 has | multiplicity | 1.  |     |
| ------------------ | ----- | ------------ | --- | --- |
eigenvalueequalsthenumberoftimes
| Thedirectsum\mathbf{C}3= | \mathcal{G}(6,\mathcal{T})\oplus\mathcal{G}(7,\mathcal{T}) |     |     |     |
| --------------- | ------------- | --- | --- | --- |
thateigenvalueappearsonthediagois the generalized eigenspace decom- nalofanupper-triangularmatrixrep-
| position promised | by 8.22. | A   | basis |     |
| ----------------- | -------- | --- | ----- | --- |
resentingtheoperator. Thisbehavior
of \mathbf{C}3 consisting of generalized eigen- alwayshappens,aswewillseein8.31.
| vectors of | \mathcal{T}, as promised | by 8.9, | is  |     |
| ---------- | -------------- | ------- | --- | --- |
$$(1,0,0),(0,1,0),(10,2,1). Theredoesnotexistabasisof\mathbf{C}3consistingofeigenvectorsofthisoperator.$$
Intheexampleabove,thesumofthemultiplicitiesoftheeigenvaluesof\mathcal{T}
equals3,whichisthedimensionofthedomainof\mathcal{T}. Thenextresultshowsthat
thisholdsforalloperatorsonfinite-dimensionalcomplexvectorspaces.

Section8B Generalized Eigenspace Decomposition 311
8.25 sumofthemultiplicitiesequalsdim\mathcal{V}
Suppose \mathbf{F} = \mathbf{C} and \mathcal{T} \in ℒ(\mathcal{V}). Then the sum of the multiplicities of all
eigenvaluesof\mathcal{T} equalsdim\mathcal{V}.
$$(8.22)andtheformulaforthedimensionofadirectsum(see3.94).$$
Thetermsalgebraicmultiplicityandgeometricmultiplicityareusedinsome
books. Incaseyouencounterthisterminology,beawarethatthealgebraicmultiplicityisthesameasthemultiplicitydefinedhereandthegeometricmultiplicity
isthedimensionofthecorrespondingeigenspace. Inotherwords,if\mathcal{T} \inℒ(\mathcal{V})
and \lambdaisaneigenvalueof\mathcal{T},then
algebraicmultiplicityof \lambda=dimnull(\mathcal{T}- \lambda\mathcal{I})dim\mathcal{V} =dim\mathcal{G}(\lambda,\mathcal{T}),
geometricmultiplicityof \lambda=dimnull(\mathcal{T}- \lambda\mathcal{I})=dim\mathcal{E}(\lambda,\mathcal{T}).
Notethatasdefinedabove,thealgebraicmultiplicityalsohasageometricmeaning
asthedimensionofacertainnullspace. Thedefinitionofmultiplicitygivenhere
iscleanerthanthetraditionaldefinitionthatinvolvesdeterminants;9.62implies
thatthesedefinitionsareequivalent.
If\mathcal{V} isaninnerproductspace,\mathcal{T} \inℒ(\mathcal{V})isnormal,and \lambdaisaneigenvalue
of\mathcal{T},thenthealgebraicmultiplicityof \lambdaequalsthegeometricmultiplicityof \lambda,
ascanbeseenfromapplying Exercise27in Section7Atothenormaloperator
\mathcal{T}-\lambda\mathcal{I}. Asaspecialcase,thesingularvaluesof\mathcal{S}\inℒ(\mathcal{V},\mathcal{W})(here\mathcal{V} and\mathcal{W} are
bothfinite-dimensionalinnerproductspaces)dependonthemultiplicities(either
∗
algebraicorgeometric)oftheeigenvaluesoftheself-adjointoperator\mathcal{S} \mathcal{S}.
Thenextdefinitionassociatesamonicpolynomialwitheachoperatorona
finite-dimensionalcomplexvectorspace.
**8.26 定义：** characteristicpolynomial
Suppose\mathbf{F} =\mathbf{C}and\mathcal{T} \inℒ(\mathcal{V}). Let \lambda ,…,\lambda denotethedistincteigenvalues
1 m
of\mathcal{T},withmultiplicitiesd ,…,d . Thepolynomial
1 m
$$(z- \lambda 1 )d 1⋯(z- \lambda m )d m$$
iscalledthecharacteristicpolynomialof\mathcal{T}.
**8.27 例：** thecharacteristicpolynomialofanoperator
Suppose\mathcal{T} \inℒ(\mathbf{C}3)isdefinedasin Example8.24. Becausetheeigenvaluesof
\mathcal{T}are6,withmultiplicity2,and7,withmultiplicity1,weseethatthecharacteristic
polynomialof\mathcal{T} is(z-6)2(z-7).

| --- | -------- | ------------------------------ | --- | --- | --- | --- | --- | --- |
degreeandzerosofcharacteristicpolynomial
8.28
| Suppose\mathbf{F}                           | =\mathbf{C}  | and\mathcal{T} | \inℒ(\mathcal{V}). | Then |                |     |     |     |
| ---------------------------------- | --- | ---- | ------ | ---- | -------------- | --- | --- | --- |
| (a) thecharacteristicpolynomialof\mathcal{T} |     |      |        |      | hasdegreedim\mathcal{V}; |     |     |     |
$$(b) thezerosofthecharacteristicpolynomialof\mathcal{T} aretheeigenvaluesof\mathcal{T}.$$
Our result about the sum of the multiplicities (8.25) implies (a). The
Proof
definitionofthecharacteristicpolynomialimplies(b).
Mosttextsdefinethecharacteristicpolynomialusingdeterminants(thetwo
definitionsareequivalentby9.62). Theapproachtakenhere,whichisconsiderably
simpler,leadstothefollowingniceproofofthe Cayley–Hamiltontheorem.
Cayley–Hamiltontheorem
8.29
Suppose\mathbf{F} =\mathbf{C},\mathcal{T} \inℒ(\mathcal{V}),andqisthecharacteristicpolynomialof\mathcal{T}. Then
q(\mathcal{T})=0.
Proof Let \lambda ,…,\lambda bethedistincteigenvaluesof\mathcal{T},andletd =dim\mathcal{G}(\lambda ,\mathcal{T}).
|          | 1                       | m   |        |     |                                  |              | k          | k   |
| -------- | ----------------------- | --- | ------ | --- | -------------------------------- | ------------ | ---------- | --- |
| Foreachk | \in{1,…,m},weknowthat(\mathcal{T}-\lambda |     |        |     | \mathcal{I})|                              | isnilpotent. | Thuswehave |     |
|          |                         |     |        |     | k \mathcal{G}(\lambda                            | k ,\mathcal{T})        |            |     |
|          |                         | \mathcal{I})d |        |     | Arthur Cayley(1821–1895)published |              |            |     |
| (\mathcal{T}-      | \lambda                       | k|  | ,\mathcal{T}) =0 |     |                                  |              |            |     |
|          | k                       | \mathcal{G}(\lambda | k      |     |                                  |              |            |     |
threemathematicspapersbeforecom-
| (by8.16)foreachk |     | \in{1,…,m}. |     |     |     |     |     |     |
| ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
pletinghisundergraduatedegree.
| The generalized |     | eigenspace |     | decom- |     |     |     |     |
| --------------- | --- | ---------- | --- | ------ | --- | --- | --- | --- |
position (8.22) states that every vector in \mathcal{V} is a sum of vectors in
\mathcal{G}(\lambda ,\mathcal{T}),…,\mathcal{G}(\lambda ,\mathcal{T}). Thus to prove that q(\mathcal{T}) = 0, we only need to show
| 1         |         | m           |     |     |     |     |     |     |
| --------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
| thatq(\mathcal{T})| |         | =0foreachk. |     |     |     |     |     |     |
|           | \mathcal{G}(\lambda ,\mathcal{T}) |             |     |     |     |     |     |     |
k
| Fixk | \in{1,…,m}. | Wehave   |     |       |       |          |     |     |
| ---- | --------- | -------- | --- | ----- | ----- | -------- | --- | --- |
|      |           | q(\mathcal{T})=(\mathcal{T}- |     | \lambda \mathcal{I})d | 1⋯(\mathcal{T}- | \lambda \mathcal{I})d m. |     |     |
|      |           |          |     | 1     |       | m        |     |     |
The operators on the right side of the equation above all commute, so we can
move the factor (\mathcal{T} - \lambda \mathcal{I})d to be the last term in the expression on the right.
k k
| Because(\mathcal{T}- | \lambda   | \mathcal{I})d k| | =0,wehaveq(\mathcal{T})| |     |     | =0,asdesired. |     |     |
| ---------- | --- | ------ | -------------- | --- | --- | ------------- | --- | --- |
|            | k   | \mathcal{G}(\lambda    | k ,\mathcal{T})          |     | \mathcal{G}(\lambda | k ,\mathcal{T})         |     |     |
Thenextresultimpliesthatiftheminimalpolynomialofanoperator\mathcal{T} \inℒ(\mathcal{V})
hasdegreedim\mathcal{V}(ashappensalmostalways—seetheparagraphsfollowing5.24),
thenthecharacteristicpolynomialof\mathcal{T} equalstheminimalpolynomialof\mathcal{T}.
characteristicpolynomialisamultipleofminimalpolynomial
8.30
Suppose\mathbf{F} =\mathbf{C} and\mathcal{T} \inℒ(\mathcal{V}). Thenthecharacteristicpolynomialof\mathcal{T} isa
polynomialmultipleoftheminimalpolynomialof\mathcal{T}.
Proof Thedesiredresultfollowsfromthe Cayley–Hamiltontheorem(8.29)and
5.29.

| --- | --------- | ---------------------------------- | --- | --- | --- | --- |
Now we can prove that the result suggested by Example 8.24 holds for all
operatorsonfinite-dimensionalcomplexvectorspaces.
8.31 multiplicityofaneigenvalueequalsnumberoftimesondiagonal
| Suppose\mathbf{F} | =\mathbf{C} and\mathcal{T} | \inℒ(\mathcal{V}). Supposev | ,…,v | isabasisof\mathcal{V} | suchthat |     |
| -------- | ------- | --------------- | ---- | ----------- | -------- | --- |
1 n
ℳ(\mathcal{T},(v ,…,v ))isuppertriangular. Thenthenumberoftimesthateach
1 n
eigenvalue \lambdaof\mathcal{T} appearsonthediagonalofℳ(\mathcal{T},(v ,…,v ))equalsthe
|                |                     |     |     | 1   | n   |     |
| -------------- | ------------------- | --- | --- | --- | --- | --- |
| multiplicityof | \lambdaasaneigenvalueof\mathcal{T}. |     |     |     |     |     |
Proof Let\mathcal{A} = ℳ(\mathcal{T},(v ,…,v )). Thus\mathcal{A}isanupper-triangularmatrix. Let
1 n
\lambda ,…,\lambda denotetheentriesonthediagonalof\mathcal{A}. Thusforeachk \in {1,…,n},
1 n
wehave
|          |         | \mathcal{T}v =u            | + \lambda v       |     |             |     |
| -------- | ------- | ---------------- | ----------- | --- | ----------- | --- |
|          |         | k                | k k k       |     |             |     |
| forsomeu | \inspan(v | ,…,v ). Henceifk | \in{1,…,n}and |     | \lambda \neq0,then\mathcal{T}v | is  |
|          | k 1     | k-1              |             |     | k           | k   |
notalinearcombinationof\mathcal{T}v ,…,\mathcal{T}v . Thelineardependencelemma(2.19)
|     |     | 1 k-1 |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- |
nowimpliesthatthelistofthose\mathcal{T}v suchthat \lambda \neq0islinearlyindependent.
|     |     | k   | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Let d denote the number of indices k \in {1,…,n} such that \lambda = 0. The
k
conclusionofthepreviousparagraphimpliesthat
|     |     | dimrange\mathcal{T} | \geqn-d. |     |     |     |
| --- | --- | --------- | ----- | --- | --- | --- |
Becausen=dim\mathcal{V} =dimnull\mathcal{T}+dimrange\mathcal{T},theinequalityaboveimpliesthat
| 8.32 |     | dimnull\mathcal{T} | \leqd. |     |     |     |
| ---- | --- | -------- | --- | --- | --- | --- |
Thematrixoftheoperator\mathcal{T}n withrespecttothebasisv ,…,v istheupper-
|     |     |     |     |     | 1 n |     |
| --- | --- | --- | --- | --- | --- | --- |
triangularmatrix\mathcal{A}n,whichhasdiagonalentries \lambdan,…,\lambdan[see Exercise2(b)in
|     |     |     |     | 1 n |     |     |
| --- | --- | --- | --- | --- | --- | --- |
\lambdan
| Section5C]. | Because | =0ifandonlyif | \lambda =0,thenumberoftimesthat0 |     |     |     |
| ----------- | ------- | ------------- | -------------------------- | --- | --- | --- |
|             |         | k             | k                          |     |     |     |
appearsonthediagonalof\mathcal{A}n equalsd. Thusapplying8.32with\mathcal{T} replacedwith
\mathcal{T}n,wehave
| 8.33 |     | dimnull\mathcal{T}n | \leqd. |     |     |     |
| ---- | --- | --------- | --- | --- | --- | --- |
For \lambdaaneigenvalueof\mathcal{T},letm denotethemultiplicityof \lambdaasaneigenvalue
\lambda
of\mathcal{T} andletd denotethenumberoftimesthat \lambdaappearsonthediagonalof\mathcal{A}.
\lambda
| Replacing\mathcal{T} | in8.33with\mathcal{T}- | \lambda\mathcal{I},weseethat |     |     |     |     |
| ---------- | ------------ | ------------ | --- | --- | --- | --- |
| 8.34       |              | m            | \leqd  |     |     |     |
\lambda \lambda
foreacheigenvalue \lambdaof\mathcal{T}. Thesumofthemultiplicitiesm overalleigenvalues
\lambda
\lambdaof\mathcal{T} equalsn,thedimensionof\mathcal{V} (by8.25). Thesumofthenumbersd over
\lambda
alleigenvalues \lambdaof\mathcal{T} alsoequalsn,becausethediagonalof\mathcal{A}haslengthn.
Thus summing both sides of 8.34 over all eigenvalues of produces an
|     |     |     |     |     | \lambda \mathcal{T} |     |
| --- | --- | --- | --- | --- | --- | --- |
equality. Hence 8.34 must actually be an equality for each eigenvalue \lambda of \mathcal{T}.
Thusthemultiplicityof \lambdaasaneigenvalueof\mathcal{T}equalsthenumberoftimesthat
\lambdaappearsonthediagonalof\mathcal{A},asdesired.

| --- | -------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
\approx100\pi
| Block        | Diagonal | Matrices |           |       |       |     |                |     |          |
| ------------ | -------- | -------- | --------- | ----- | ----- | --- | -------------- | --- | -------- |
| To interpret | our      | results  | in matrix | form, |       |     |                |     |          |
|              |          |          |           |       | Often | we  | can understand |     | a matrix |
wemakethefollowingdefinition,gener-
|               |            |                      |            |         | better             | by thinking |     | of it as | composed |
| ------------- | ---------- | -------------------- | ---------- | ------- | ------------------ | ----------- | --- | -------- | -------- |
| alizing       | the notion | of                   | a diagonal | matrix. | ofsmallermatrices. |             |     |          |          |
| Ifeachmatrix\mathcal{A} |            | inthedefinitionbelow |            |         |                    |             |     |          |          |
k
isa1-by-1matrix,thenweactuallyhaveadiagonalmatrix.
| 8.35 | definition: | blockdiagonalmatrix |     |     |     |     |     |     |     |
| ---- | ----------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
Ablockdiagonalmatrixisasquarematrixoftheform
|     |     |     |     | \mathcal{A}     | 0   |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     | ⎛ 1   |     | ⎞   |     |     |     |
|     |     |     |     | ⎜     |     | ⎟ , |     |     |     |
|     |     |     |     | ⎜ ⎜ ⋱ |     | ⎟ ⎟ |     |     |     |
|     |     |     |     | 0     | \mathcal{A}   |     |     |     |     |
|     |     |     |     | ⎝     | m   | ⎠   |     |     |     |
where\mathcal{A} ,…,\mathcal{A} aresquarematriceslyingalongthediagonalandallother
1 m
entriesofthematrixequal0.
| 8.36 example: |     | ablockdiagonalmatrix |     |     |     |     |     |     |     |
| ------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
The5-by-5matrix
|     |     |     | ( 4   | ) 0 | 0   | 0   | 0   |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     |     | ⎛ ⎜   |     |     |     |     | ⎞ ⎟ |     |
|     |     |     | ⎜     |     |     |     |     | ⎟   |     |
|     |     |     | ⎜ ⎜ 0 | 2   | -3  | 0   | 0   | ⎟ ⎟ |     |
|     |     |     | ⎜     | ⎛   | ⎞   |     |     | ⎟   |     |
|     |     |     | ⎜ ⎜   | ⎜   | ⎟   |     |     | ⎟ ⎟ |     |
|     |     | \mathcal{A}=⎜ |       |     |     |     |     | ⎟   |     |
|     |     |     | ⎜ 0   | ⎝ 0 | 2 ⎠ | 0   | 0   | ⎟   |     |
|     |     |     | ⎜ ⎜   |     |     |     |     | ⎟ ⎟ |     |
|     |     |     | ⎜     |     |     |     |     | ⎟   |     |
|     |     |     | ⎜ ⎜ 0 | 0   | 0   | 1   | 7   | ⎟ ⎟ |     |
|     |     |     | ⎜     |     |     | ⎛ ⎜ | ⎞ ⎟ | ⎟   |     |
|     |     |     | ⎝ 0   | 0   | 0   | 0   | 1   | ⎠   |     |
|     |     |     |       |     |     | ⎝   | ⎠   |     |     |
isablockdiagonalmatrixwith
|     |     |     |     | \mathcal{A}   | 0   |       |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     | ⎛ 1 |     | ⎞     |     |     |     |
|     |     |     |     | ⎜   |     | ⎟     |     |     |     |
|     |     |     | \mathcal{A}=⎜ | ⎜   | \mathcal{A}   | ⎟ ⎟ , |     |     |     |
|     |     |     |     | ⎜   | 2   | ⎟     |     |     |     |
|     |     |     |     | ⎜   |     | ⎟     |     |     |     |
|     |     |     |     | ⎝ 0 | \mathcal{A}   | ⎠     |     |     |     |
where
|     |     |      |      | 2   | -3  |     | 1   | 7   |     |
| --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |      |      | ⎛   | ⎞   |     | ⎛   | ⎞   |     |
|     | \mathcal{A}   | =( 4 | ), \mathcal{A} | = ⎜ | ⎟,  | \mathcal{A}   | = ⎜ | ⎟.  |     |
|     |     |      |      | ⎝ 0 | 2 ⎠ |     | ⎝ 0 | 1 ⎠ |     |
Heretheinnermatricesinthe5-by-5matrixaboveareblockedofftoshowhow
wecanthinkofitasablockdiagonalmatrix.
Note that in the example above, each of \mathcal{A} , \mathcal{A} , \mathcal{A} is an upper-triangular
|     |     |     |     |     |     | 1 2 | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
matrix whose diagonal entries are all equal. The next result shows that with
respecttoanappropriatebasis,everyoperatoronafinite-dimensionalcomplex
vectorspacehasamatrixofthisform. Notethatthisresultgivesusmanymore
zerosinthematrixthanareneededtomakeituppertriangular.

| --- | --- | --------- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
blockdiagonalmatrixwithupper-triangularblocks
8.37
Suppose\mathbf{F} =\mathbf{C} and\mathcal{T} \inℒ(\mathcal{V}). Let \lambda ,…,\lambda bethedistincteigenvaluesof
|     |     |     |     | 1   | m   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
\mathcal{T}, withmultiplicitiesd ,…,d . Thenthereisabasisof\mathcal{V} withrespectto
|        |                                  |     | 1   | m     |       |     |     |     |     |
| ------ | -------------------------------- | --- | --- | ----- | ----- | --- | --- | --- | --- |
| which\mathcal{T} | hasablockdiagonalmatrixoftheform |     |     |       |       |     |     |     |     |
|        |                                  |     |     | \mathcal{A}     | 0     |     |     |     |     |
|        |                                  |     |     | ⎛ 1   | ⎞     |     |     |     |     |
|        |                                  |     |     | ⎜ ⎜   | ⎟ ⎟ , |     |     |     |     |
|        |                                  |     |     | ⎜ ⋱   | ⎟     |     |     |     |     |
|        |                                  |     |     | ⎝ 0 \mathcal{A} | ⎠     |     |     |     |     |
m
| whereeach\mathcal{A} |     | isad | -by-d | upper-triangularmatrixoftheform |      |     |     |     |     |
| ---------- | --- | ---- | ----- | ------------------------------- | ---- | --- | --- | --- | --- |
|            |     | k k  | k     |                                 |      |     |     |     |     |
|            |     |      |       | \lambda                               | ∗    |     |     |     |     |
|            |     |      |       | ⎛ k                             | ⎞    |     |     |     |     |
|            |     |      |       | ⎜                               | ⎟    |     |     |     |     |
|            |     |      | \mathcal{A}     | =⎜ ⎜ ⋱                          | ⎟ ⎟. |     |     |     |     |
k
|       |         |         |         | 0                     | \lambda   |                       |     |     |     |
| ----- | ------- | ------- | ------- | --------------------- | --- | --------------------- | --- | --- | --- |
|       |         |         |         | ⎝                     | k ⎠ |                       |     |     |     |
|       | Each(\mathcal{T}- |         |         | isnilpotent(see8.22). |     | Foreachk,chooseabasis |     |     |     |
| Proof |         | \lambda k \mathcal{I})| | \mathcal{G}(\lambda ,\mathcal{T}) |                       |     |                       |     |     |     |
k
of \mathcal{G}(\lambda ,\mathcal{T}), which is a vector space of dimension d , such that the matrix of
|     | k           |                                      |     |     |     | k   |                   |     |     |
| --- | ----------- | ------------------------------------ | --- | --- | --- | --- | ----------------- | --- | --- |
|     |             | withrespecttothisbasisisasin8.18(c). |     |     |     |     | Thuswithrespectto |     |     |
| (\mathcal{T}- | \lambda k \mathcal{I})| \mathcal{G}(\lambda | ,\mathcal{T})                                  |     |     |     |     |                   |     |     |
k
| thisbasis,thematrixof\mathcal{T}|               |     |     |     | ,whichequals(\mathcal{T} |     | - \lambda \mathcal{I})| |         | + \lambda | \mathcal{I}| ,    |
| ------------------------------------- | --- | --- | --- | -------------- | --- | ------- | ------- | --- | ------- |
|                                       |     |     | \mathcal{G}(\lambda | ,\mathcal{T})            |     | k       | \mathcal{G}(\lambda ,\mathcal{T}) | k   | \mathcal{G}(\lambda ,\mathcal{T}) |
| lookslikethedesiredformshownabovefor\mathcal{A} |     |     |     | k              | .   |         | k       |     | k       |
k
Thegeneralizedeigenspacedecomposition(8.22)showsthatputtingtogether
,\mathcal{T})’schosenabovegivesabasisof\mathcal{V}.
| thebasesofthe\mathcal{G}(\lambda |     | k   |     |     |     |     | Thematrixof\mathcal{T} |     | with |
| ---------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- |
respecttothisbasishasthedesiredform.
| 8.38         | example:                  | blockdiagonalmatrixviageneralizedeigenvectors |     |       |       |     |     |         |        |
| ------------ | ------------------------- | --------------------------------------------- | --- | ----- | ----- | --- | --- | ------- | ------ |
|              | Let\mathcal{T} \inℒ(\mathbf{C}3)bedefinedby\mathcal{T}(z |                                               |     | ,z ,z | )=(6z | +3z | +4z | ,6z +2z | ,7z ). |
|              |                           |                                               |     | 1 2   | 3     | 1 2 | 3   | 2       | 3 3    |
| Thematrixof\mathcal{T} |                           | (withrespecttothestandardbasis)is             |     |       |       |     |     |         |        |
|              |                           |                                               |     | 6 3   | 4     |     |     |         |        |
|              |                           |                                               |     | ⎛ ⎜   | ⎞ ⎟   |     |     |         |        |
|              |                           |                                               |     | ⎜ 0 6 | 2 ⎟ , |     |     |         |        |
|              |                           |                                               |     | ⎜     | ⎟     |     |     |         |        |
|              |                           |                                               |     | ⎝ 0 0 | 7 ⎠   |     |     |         |        |
whichisanupper-triangularmatrixbutisnotoftheformpromisedby8.37.
|     | Aswesawin Example8.24,theeigenvaluesof\mathcal{T} |     |     |     |                        | are6and7;also, |     |     |     |
| --- | -------------------------------------- | --- | --- | --- | ---------------------- | -------------- | --- | --- | --- |
|     | \mathcal{G}(6,\mathcal{T})=span((1,0,0),(0,1,0))           |     |     | and | \mathcal{G}(7,\mathcal{T})=span((10,2,1)). |                |     |     |     |
Wealsosawthatabasisof\mathbf{C}3 consistingofgeneralizedeigenvectorsof\mathcal{T} is
$$(1,0,0),(0,1,0),(10,2,1).$$
| Thematrixof\mathcal{T} |     | withrespecttothisbasisis |     |     |       |     |     |     |     |
| ------------ | --- | ------------------------ | --- | --- | ----- | --- | --- | --- | --- |
|              |     |                          |     | 6 3 | 0     |     |     |     |     |
|              |     |                          | ⎛   |     |       | ⎞   |     |     |     |
|              |     |                          | ⎜   | ( ) |       | ⎟   |     |     |     |
|              |     |                          | ⎜   | 0 6 | 0     | ⎟ , |     |     |     |
|              |     |                          | ⎜   |     |       | ⎟   |     |     |     |
|              |     |                          |     | 0 0 | ( 7 ) |     |     |     |     |
|              |     |                          | ⎝   |     |       | ⎠   |     |     |     |
whichisamatrixoftheblockdiagonalformpromisedby8.37.

| -------- | --- | ------------------------------ | --- | --- | --- | --- |
| Exercises | 8B  |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- |
1 Define\mathcal{T} \inℒ(\mathbf{C}2)by\mathcal{T}(w,z)=(-z,w). Findthegeneralizedeigenspaces
correspondingtothedistincteigenvaluesof\mathcal{T}.
Provethat\mathcal{G}(\lambda,\mathcal{T})=\mathcal{G}(1,\mathcal{T}-1)forevery
| 2 Suppose\mathcal{T} | \inℒ(\mathcal{V})isinvertible. |     |     |     |     |     |
| ---------- | ------------------ | --- | --- | --- | --- | --- |
\lambda
| \lambda\in\mathbf{F}       | with \lambda\neq0. |         |      |                |            |       |
| --------- | --------- | ------- | ---- | -------------- | ---------- | ----- |
|           |           | ℒ(\mathcal{V}).   | ℒ(\mathcal{V}) |                |            |       |
| 3 Suppose | \mathcal{T} \in       | Suppose | \mathcal{S} \in  | is invertible. | Prove that | \mathcal{T} and |
\mathcal{S}-1\mathcal{T}\mathcal{S}havethesameeigenvalueswiththesamemultiplicities.
| 4 Supposedim\mathcal{V} |                                  | \geq2and\mathcal{T}              | \inℒ(\mathcal{V})issuchthatnull\mathcal{T}dim\mathcal{V}-2\neqnull\mathcal{T}dim\mathcal{V}-1. |     |                       |       |
| ------------- | -------------------------------- | ------------------- | --------------------------------------- | --- | --------------------- | ----- |
| Provethat\mathcal{T}    | hasatmosttwodistincteigenvalues. |                     |                                         |     |                       |       |
| 5 Suppose\mathcal{T}    | \inℒ(\mathcal{V})and3and8areeigenvaluesof\mathcal{T}.  |                     |                                         |     | Letn=dim\mathcal{V}.            | Prove |
| that\mathcal{V}         | =(null\mathcal{T}n-2)\oplus(range\mathcal{T}n-2).         |                     |                                         |     |                       |       |
| Suppose\mathcal{T}      | \inℒ(\mathcal{V})and                         | \lambdaisaneigenvalueof\mathcal{T}. |                                         |     | Explainwhytheexponent |       |
ofz- \lambdainthefactorizationoftheminimalpolynomialof\mathcal{T} isthesmallest
\lambda\mathcal{I})m|
| positiveintegermsuchthat(\mathcal{T}- |     |     |     | \mathcal{G}(\lambda,\mathcal{T}) =0. |     |     |
| --------------------------- | --- | --- | --- | ---------- | --- | --- |
7 Suppose\mathcal{T} \inℒ(\mathcal{V})and \lambdaisaneigenvalueof\mathcal{T} withmultiplicityd. Prove
| that\mathcal{G}(\lambda,\mathcal{T})=null(\mathcal{T}- |     | \lambda\mathcal{I})d. |     |     |     |     |
| ------------------ | --- | ----- | --- | --- | --- | --- |
Ifd<dim\mathcal{V},thenthisexerciseimproves8.20.
8 Suppose\mathcal{T} \inℒ(\mathcal{V})and \lambda ,…,\lambda arethedistincteigenvaluesof\mathcal{T}. Prove
|     |     | 1   | m   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
that
|     |     | \mathcal{V} =\mathcal{G}(\lambda | ,\mathcal{T})\oplus⋯\oplus\mathcal{G}(\lambda |     | ,\mathcal{T}) |     |
| --- | --- | ------ | --------- | --- | --- | --- |
|     |     |        | 1         | m   |     |     |
ifandonlyiftheminimalpolynomialof\mathcal{T} equals(z- \lambda )k 1⋯(z- \lambda )k m
|                          |     |     |        |     | 1   | m   |
| ------------------------ | --- | --- | ------ | --- | --- | --- |
| forsomepositiveintegersk |     |     | ,…,k . |     |     |     |
|                          |     |     | 1 m    |     |     |     |
The case follows immediately from 5.27(b) and the generalized
\mathbf{F} = \mathbf{C}
eigenspacedecomposition(8.22);thusthisexerciseisinterestingonlywhen
\mathbf{F} =\mathbf{R}.
9 Suppose \mathbf{F} = \mathbf{C} and \mathcal{T} \in ℒ(\mathcal{V}). Prove that there exist \mathcal{D},\mathcal{N} \in ℒ(\mathcal{V})
suchthat\mathcal{T} =\mathcal{D}+\mathcal{N},theoperator\mathcal{D}isdiagonalizable,\mathcal{N} isnilpotent,and
\mathcal{D}\mathcal{N} =\mathcal{N}\mathcal{D}.
| Suppose\mathcal{V} | isacomplexinnerproductspace,e |     |     |     | ,…,e isanorthonormal |     |
| -------- | ----------------------------- | --- | --- | --- | -------------------- | --- |
| 10       |                               |     |     | 1   | n                    |     |
basis of \mathcal{V}, and \mathcal{T} \in ℒ(\mathcal{V}). Let \lambda ,…,\lambda be the eigenvalues of \mathcal{T}, each
|                                       |     |         | 1    | n         |     |     |
| ------------------------------------- | --- | ------- | ---- | --------- | --- | --- |
| includedasmanytimesasitsmultiplicity. |     |         |      | Provethat |     |     |
|                                       |     | |2+⋯+|\lambda | |2   | ‖2+⋯+‖\mathcal{T}e  | ‖2. |     |
|                                       |     | |\lambda      | \leq‖\mathcal{T}e |           |     |     |
|                                       |     | 1       | n    | 1         | n   |     |
Seethecommentafter Exercise5in Section7A.
11 Give an example of an operator on \mathbf{C}4 whose characteristic polynomial
equals(z-7)2(z-8)2.

| --- | --------- | ---------------------------------- | --- | --- | --- | --- |
\mathbf{C}4
12 Give an example of an operator on whose characteristic polynomial
equals(z-1)(z-5)3andwhoseminimalpolynomialequals(z-1)(z-5)2.
13 Give an exampleof an operator on \mathbf{C}4 whose characteristic and minimal
polynomialsbothequalz(z-1)2(z-3).
14 Giveanexampleofanoperatoron\mathbf{C}4whosecharacteristicpolynomialequals
z(z-1)2(z-3)andwhoseminimalpolynomialequalsz(z-1)(z-3).
Let\mathcal{T}betheoperatoron\mathbf{C}4definedby\mathcal{T}(z
| 15  |     |     |     | ,z  | ,z ,z )=(0,z | ,z ,z ). Find |
| --- | --- | --- | --- | --- | ------------ | ------------- |
|     |     |     |     | 1 2 | 3 4          | 1 2 3         |
thecharacteristicpolynomialandtheminimalpolynomialof\mathcal{T}.
| Let\mathcal{T} betheoperatoron\mathbf{C}6 |     |     | definedby |     |     |     |
| ---------------------- | --- | --- | --------- | --- | --- | --- |
|     |     | ,z ,z | ,z ,z ,z )=(0,z |     | ,z ,0,z ,0). |     |
| --- | --- | ----- | --------------- | --- | ------------ | --- |
\mathcal{T}(z
|     |     | 1 2 3 | 4 5 6 |     | 1 2 4 |     |
| --- | --- | ----- | ----- | --- | ----- | --- |
Findthecharacteristicpolynomialandtheminimalpolynomialof\mathcal{T}.
17 Suppose\mathbf{F} =\mathbf{C}and\mathcal{P} \inℒ(\mathcal{V})issuchthat\mathcal{P}2 =\mathcal{P}. Provethatthecharacteristicpolynomialof\mathcal{P}iszm(z-1)n,wherem=dimnull\mathcal{P}andn=dimrange\mathcal{P}.
18 Suppose\mathcal{T} \inℒ(\mathcal{V})and \lambdaisaneigenvalueof\mathcal{T}. Explainwhythefollowing
fournumbersequaleachother.
$$(a) Theexponentofz- \lambdainthefactorizationoftheminimalpolynomial$$
of\mathcal{T}.
| (b) Thesmallestpositiveintegermsuchthat(\mathcal{T}- |     |     |     |     | \lambda\mathcal{I})m| | =0. |
| ------------------------------------------ | --- | --- | --- | --- | ----- | --- |
\mathcal{G}(\lambda,\mathcal{T})
$$(c) Thesmallestpositiveintegermsuchthat$$
|     |     | null(\mathcal{T}- | \lambda\mathcal{I})m =null(\mathcal{T}- |     | \lambda\mathcal{I})m+1. |     |
| --- | --- | ------- | ------------- | --- | ------- | --- |
$$(d) Thesmallestpositiveintegermsuchthat$$
|     |     | range(\mathcal{T}- | \lambda\mathcal{I})m =range(\mathcal{T}- |     | \lambda\mathcal{I})m+1. |     |
| --- | --- | -------- | -------------- | --- | ------- | --- |
19 Suppose\mathbf{F} =\mathbf{C} and\mathcal{S}\inℒ(\mathcal{V})isaunitaryoperator. Provethattheconstant
terminthecharacteristicpolynomialof\mathcal{S}hasabsolutevalue1.
| 20 Supposethat\mathbf{F} | =\mathbf{C}  | and\mathcal{V} | ,…,\mathcal{V} arenonzerosubspacesof\mathcal{V} |     |     | suchthat |
| --------------- | --- | ---- | --------------------------- | --- | --- | -------- |
|                 |     | 1    | m                           |     |     |          |
|                 |     |      | \mathcal{V} =\mathcal{V} \oplus⋯\oplus\mathcal{V}                   |     | .   |          |
|                 |     |      | 1                           |     | m   |          |
Suppose \mathcal{T} \in ℒ(\mathcal{V}) and each \mathcal{V} is invariant under \mathcal{T}. For each k, let p
k k
denotethecharacteristicpolynomialof\mathcal{T}| . Provethatthecharacteristic
\mathcal{V} k
| polynomialof\mathcal{T} | equalsp | ⋯p  | .   |     |     |     |
| ------------- | ------- | --- | --- | --- | --- | --- |
|               |         | 1   | m   |     |     |     |
Supposep,q\in𝒫(\mathbf{C})aremonicpolynomialswiththesamezerosandqisa
polynomialmultipleofp. Provethatthereexists\mathcal{T} \in ℒ(\mathbf{C}degq)suchthat
thecharacteristicpolynomialof\mathcal{T} isqandtheminimalpolynomialof\mathcal{T} isp.
This exercise implies that every monic polynomial is the characteristic
polynomialofsomeoperator.

| --- | -------- | --- | ------------------------------ | --- | --- | --- | --- | --- |
22 Suppose\mathcal{A}and\mathcal{B}areblockdiagonalmatricesoftheform
|     |        |      | \mathcal{A}                                      |     | 0   |       | \mathcal{B}   | 0       |
| --- | ------ | ---- | -------------------------------------- | --- | --- | ----- | --- | ------- |
|     |        |      | ⎛                                      | 1   | ⎞   |       | ⎛ 1 | ⎞       |
|     |        | \mathcal{A}=⎜  | ⎜                                      | ⋱   | ⎟ ⎟ | , \mathcal{B}=⎜ | ⎜ ⋱ | ⎟ ⎟ ,   |
|     |        |      | ⎜                                      |     | ⎟   |       | ⎜   | ⎟       |
|     |        |      | ⎝                                      | 0   | \mathcal{A} ⎠ |       | ⎝ 0 | \mathcal{B} ⎠     |
|     |        |      |                                        |     | m   |       |     | m       |
|     | where\mathcal{A} | and\mathcal{B} | aresquarematricesofthesamesizeforeachk |     |     |       |     | =1,…,m. |
|     |        | k    | k                                      |     |     |       |     |         |
Showthat\mathcal{A}\mathcal{B}isablockdiagonalmatrixoftheform
|     |     |     |     |      | \mathcal{A} \mathcal{B}   |     | 0    |     |
| --- | --- | --- | --- | ---- | ----- | --- | ---- | --- |
|     |     |     |     |      | ⎛ ⎜ 1 | 1   | ⎞ ⎟  |     |
|     |     |     |     | \mathcal{A}\mathcal{B}=⎜ |       | ⋱   | ⎟ ⎟. |     |
⎜
|     |     |     |     |     | ⎝ 0 | \mathcal{A}   | \mathcal{B} ⎠ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
m m
| 23  | Suppose\mathbf{F}               | =\mathbf{R},\mathcal{T} | \inℒ(\mathcal{V}),and |     | \lambda\in\mathbf{C}.                   |     |     |     |
| --- | ---------------------- | ---- | --------- | --- | ---------------------- | --- | --- | --- |
|     | (a) Showthatu+iv\in\mathcal{G}(\lambda,\mathcal{T} |      |           |     | )ifandonlyifu-iv\in\mathcal{G}(\lambda,\mathcal{T} |     |     | ).  |
|     |                        |      |           |     | \mathbf{C}                      |     |     | \mathbf{C}   |
$$(b) Show that the multiplicity of as an eigenvalue of equals the$$
|     |                |     |                    |     |     | \lambda   |     | \mathcal{T} \mathbf{C} |
| --- | -------------- | --- | ------------------ | --- | --- | --- | --- | --- |
|     | multiplicityof |     | \lambdaasaneigenvalueof\mathcal{T} |     |     |     | .   |     |
\mathbf{C}
$$(c) Use(b)andtheresultaboutthesumofthemultiplicities(8.25)toshow$$
|     | thatifdim\mathcal{V} |     | isanoddnumber,then\mathcal{T} |     |     |     | hasarealeigenvalue. |     |
| --- | ---------- | --- | ------------------- | --- | --- | --- | ------------------- | --- |
\mathbf{C}
$$(d) Use (c) and the result about real eigenvalues of \mathcal{T} (Exercise 17 in$$
\mathbf{C}
Section 5A) to show that if dim\mathcal{V} is an odd number, then has an
\mathcal{T}
eigenvalue(thusgivinganalternativeproofof5.34).
See Exercise33in Section3Bforthedefinitionofthecomplexification\mathcal{T} .
\mathbf{C}

| --------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| 8C Consequences |          | of        | Generalized | Eigenspace |     |     | Decomposition |     |
| --------------- | -------- | --------- | ----------- | ---------- | --- | --- | ------------- | --- |
| Square          | Roots of | Operators |             |            |     |     |               |     |
Recallthatasquarerootofanoperator\mathcal{T} \inℒ(\mathcal{V})isanoperator\mathcal{R}\inℒ(\mathcal{V})such
that\mathcal{R}2 =\mathcal{T} (see7.36). Everycomplexnumberhasasquareroot,butnotevery
operatoronacomplexvectorspacehasasquareroot. Forexample,theoperator
on\mathbf{C}3definedby\mathcal{T}(z ,z ,z )=(z ,z ,0)doesnothaveasquareroot,asyouare
|     |     | 1 2 | 3   | 2 3 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
askedtoshowin Exercise1. Thenoninvertibilityofthatoperatorisnoaccident,
aswewillsoonsee. Webeginbyshowingthattheidentityplusanynilpotent
operatorhasasquareroot.
8.39 identityplusnilpotenthasasquareroot
| Suppose\mathcal{T} | \inℒ(\mathcal{V})isnilpotent. |     |     | Then\mathcal{I}+\mathcal{T} | hasasquareroot. |     |     |     |
| -------- | ----------------- | --- | --- | ------- | --------------- | --- | --- | --- |
Considerthe Taylorseriesforthefunction\sqrt1+x:
Proof
| 8.40 |     | \sqrt1+x | =1+a | x+a | x2+⋯ | .   |     |     |
| ---- | --- | ---- | ---- | --- | ---- | --- | --- | --- |
Wedonotfindanexplicitformulafor
|     |     |     |     | Because |     | 1,  | the formula | above |
| --- | --- | --- | --- | ------- | --- | --- | ----------- | ----- |
a 1 =
| thecoefficientsorworryaboutwhether |               |     |         |               |     | 2   | x               |     |
| ---------------------------------- | ------------- | --- | ------- | ------------- | --- | --- | --------------- | --- |
|                                    |               |     |         | impliesthat1+ |     |     | isagoodestimate |     |
| the infinite                       | sum converges |     | because | we            |     |     | 2               |     |
for\sqrt1+xwhenxissmall.
usethisequationonlyasmotivation.
| Because | \mathcal{T} is nilpotent, |     | \mathcal{T}m = | 0 for |     |     |     |     |
| ------- | --------------- | --- | ---- | ----- | --- | --- | --- | --- |
somepositiveintegerm. In8.40,supposewereplacexwith\mathcal{T} and1with\mathcal{I}. Then
theinfinitesumontherightsidebecomesafinitesum(because\mathcal{T}k = 0forall
| k \geqm). | Thusweguessthatthereisasquarerootof\mathcal{I}+\mathcal{T} |     |     |        |       | oftheform |     |     |
| ------ | -------------------------------------- | --- | --- | ------ | ----- | --------- | --- | --- |
|        |                                        | \mathcal{I}+a | \mathcal{T}+a | \mathcal{T}2+⋯+a | \mathcal{T}m-1. |           |     |     |
|        |                                        |     | 1   | 2      | m-1   |           |     |     |
Havingmadethisguess,wecantrytochoosea ,a ,…,a suchthattheoperator
|     |     |     |     |     | 1 2 | m-1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
abovehasitssquareequalto\mathcal{I}+\mathcal{T}.
Now
\mathcal{T}m-1)2
|     | (\mathcal{I}+a \mathcal{T}+a | \mathcal{T}2+a  | \mathcal{T}3+⋯+a           |            |      |       |        |     |
| --- | -------- | ----- | ---------------- | ---------- | ---- | ----- | ------ | --- |
|     | 1        | 2     | 3                | m-1        |      |       |        |     |
|     |          |       |                  | +a2)\mathcal{T}2+(2a |      |       | )\mathcal{T}3+⋯  |     |
|     | =\mathcal{I}+2a    | \mathcal{T}+(2a |                  |            |      | +2a a |        |     |
|     |          | 1     | 2                | 1          | 3    | 1 2   |        |     |
|     |          | +(2a  | +termsinvolvinga |            | ,…,a |       | )\mathcal{T}m-1. |     |
|     |          | m-1   |                  |            | 1    | m-2   |        |     |
Wewantthe right sideof the equationaboveto equal\mathcal{I} +\mathcal{T}. Hence choosea
+a2
| suchthat2a | =1(thusa |     | =1/2). | Next,choosea |     | suchthat2a |     | =0(thus |
| ---------- | -------- | --- | ------ | ------------ | --- | ---------- | --- | ------- |
|            | 1        | 1   |        |              | 2   |            | 2   | 1       |
$$a = -1/8). Thenchoosea suchthatthecoefficientof\mathcal{T}3 ontherightsideof$$
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
theequationaboveequals0(thusa =1/16). Continueinthisfashionforeach
$$k =4,…,m-1,ateachstepsolvingfora sothatthecoefficientof\mathcal{T}kontheright$$
k
sideoftheequationaboveequals0. Actuallywedonotcareabouttheexplicit
formulaforthea ’s. Weonlyneedtoknowthatsomechoiceofthea ’sgivesa
|     | k   |     |     |     |     |     |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
squarerootof\mathcal{I}+\mathcal{T}.

320 Chapter 8 Operatorson Complex Vector Spaces
Thepreviouslemmaisvalidonrealandcomplexvectorspaces. However,the
resultbelowholdsonlyoncomplexvectorspaces. Forexample,theoperatorof
multiplicationby-1ontheone-dimensionalrealvectorspace\mathbf{R} hasnosquare
root.
Fortheproofbelow,weneedtoknowthateveryz\in\mathbf{C} has
asquarerootin\mathbf{C}. Toshowthis,write
$$z=r(cos\theta+isin\theta),$$
whereristhelengthofthelinesegmentinthecomplexplane
fromtheorigintozand\thetaistheangleofthatlinesegmentwith
thepositivehorizontalaxis. Then
Representation
\sqrt
r(cos\theta +isin\theta)
ofacomplex
2 2
numberwith
isasquarerootofz,asyoucanverifybyshowingthatthesquare
polar
ofthecomplexnumberaboveequalsz. coordinates.
8.41 over\mathbf{C},invertibleoperatorshavesquareroots
Suppose\mathcal{V} isacomplexvectorspaceand\mathcal{T} \inℒ(\mathcal{V})isinvertible. Then\mathcal{T}has
asquareroot.
Proof Let \lambda ,…,\lambda bethedistincteigenvaluesof\mathcal{T}. Foreachk,thereexistsa
1 m
nilpotentoperator\mathcal{T} \inℒ(\mathcal{G}(\lambda ,\mathcal{T}))suchthat\mathcal{T}| = \lambda \mathcal{I}+\mathcal{T} [see8.22(b)].
k k \mathcal{G}(\lambda ,\mathcal{T}) k k
k
Because\mathcal{T} isinvertible,noneofthe \lambda ’sequals0,sowecanwrite
k
\mathcal{T}
\mathcal{T}| = \lambda (\mathcal{I}+ k)
\mathcal{G}(\lambda k ,\mathcal{T}) k \lambda
k
for each k. Because \mathcal{T} /\lambda is nilpotent, \mathcal{I} +\mathcal{T} /\lambda has a square root (by 8.39).
k k k k
Multiplyingasquarerootofthecomplexnumber \lambda byasquarerootof\mathcal{I}+\mathcal{T} /\lambda ,
k k k
weobtainasquareroot\mathcal{R} of\mathcal{T}| .
k \mathcal{G}(\lambda ,\mathcal{T})
k
Bythegeneralizedeigenspacedecomposition(8.22),atypicalvectorv\in\mathcal{V}
canbewrittenuniquelyintheform
$$v=u +⋯+u ,$$
1 m
where each u is in \mathcal{G}(\lambda ,\mathcal{T}). Using this decomposition, define an operator
k k
\mathcal{R}\inℒ(\mathcal{V})by
\mathcal{R}v=\mathcal{R} u +⋯+\mathcal{R} u .
1 1 m m
Youshouldverifythatthisoperator\mathcal{R}isasquarerootof\mathcal{T},completingtheproof.
Byimitatingthetechniquesinthissubsection,youshouldbeabletoprovethat
if\mathcal{V} isacomplexvectorspaceand\mathcal{T} \inℒ(\mathcal{V})isinvertible,then\mathcal{T} hasakth root
foreverypositiveintegerk.

Section8C Consequencesof Generalized Eigenspace Decomposition 321
Weknowthatif\mathcal{V} isacomplexvectorspace,thenforevery\mathcal{T} \inℒ(\mathcal{V})thereisa
basisof\mathcal{V} withrespecttowhich\mathcal{T} hasaniceupper-triangularmatrix(see8.37).
Inthissubsectionwewillseethatwecandoevenbetter—thereisabasisof\mathcal{V}
withrespecttowhichthematrixof\mathcal{T} contains0’severywhereexceptpossiblyon
thediagonalandthelinedirectlyabovethediagonal.
Webeginbylookingattwoexamplesofnilpotentoperators.
**8.42 例：** nilpotentoperatorwithnicematrix
Let\mathcal{T} betheoperatoron\mathbf{C}4 definedby
\mathcal{T}(z ,z ,z ,z )=(0,z ,z ,z ).
1 2 3 4 1 2 3
Then\mathcal{T}4 =0;thus\mathcal{T}isnilpotent. Ifv=(1,0,0,0),then\mathcal{T}3v,\mathcal{T}2v,\mathcal{T}v,visabasis
of\mathbf{C}4. Thematrixof\mathcal{T} withrespecttothisbasisis
0 1 0 0
⎛ ⎞
⎜ ⎟
⎜ 0 0 1 0 ⎟
⎜ ⎜ ⎟ ⎟.
⎜ ⎜ 0 0 0 1 ⎟ ⎟
⎝ 0 0 0 0 ⎠
Thenextexampleofanilpotentoperatorhasmorecomplicatedbehaviorthan
theexampleabove.
**8.43 例：** nilpotentoperatorwithslightlymorecomplicatedmatrix
Let\mathcal{T} betheoperatoron\mathbf{C}6 definedby
\mathcal{T}(z ,z ,z ,z ,z ,z )=(0,z ,z ,0,z ,0).
1 2 3 4 5 6 1 2 4
Then\mathcal{T}3 =0;thus\mathcal{T} isnilpotent. Incontrasttothenicebehaviorofthenilpotent
operatorofthepreviousexample,forthisnilpotentoperatortheredoesnotexist
avectorv \in \mathbf{C}6suchthat\mathcal{T}5v,\mathcal{T}4v,\mathcal{T}3v,\mathcal{T}2v,\mathcal{T}v,visabasisof\mathbf{C}6. However,if
wetakev =(1,0,0,0,0,0),v =(0,0,0,1,0,0),andv =(0,0,0,0,0,1),then
1 2 3
\mathcal{T}2v ,\mathcal{T}v ,v ,\mathcal{T}v ,v ,v is a basis of \mathbf{C}6. The matrix of \mathcal{T} with respect to this
1 1 1 2 2 3
basisis
0 1 0 0 0 0
⎛ ⎜ ⎜ ⎜ ⎛ ⎜ ⎜ ⎜ 0 0 1 ⎞ ⎟ ⎟ ⎟ 0 0 0 ⎞ ⎟ ⎟ ⎟
⎜ ⎟
⎜ ⎜ ⎝ 0 0 0 ⎠ 0 0 0 ⎟ ⎟
⎜ ⎜ ⎟ ⎟.
⎜ 0 0 0 0 1 0 ⎟
⎜ ⎜ ( ) ⎟ ⎟
⎜ ⎜ 0 0 0 0 0 0 ⎟ ⎟
⎝ 0 0 0 0 0 ( 0 ) ⎠
Heretheinnermatricesareblockedofftoshowthatwecanthinkofthe6-by-6
matrixaboveasablockdiagonalmatrixconsistingofa3-by-3blockwith1’son
thelineabovethediagonaland0’selsewhere,a2-by-2blockwith1abovethe
diagonaland0’selsewhere,anda1-by-1blockcontaining0.

322 Chapter 8 Operatorson Complex Vector Spaces
Our next goal is to show that every nilpotent operator \mathcal{T} \in ℒ(\mathcal{V}) behaves
similarlytotheoperatorinthepreviousexample. Specifically,thereisafinite
collectionofvectorsv ,…,v \in\mathcal{V} suchthatthereisabasisof\mathcal{V} consistingof
1 n
thevectorsoftheform\mathcal{T}jv ,askvariesfrom1tonandjvaries(inreverseorder)
k
from0tothelargestnonnegativeintegerm
k
suchthat\mathcal{T}m kv
k
\neq0. Withrespectto
thisbasis,thematrixof\mathcal{T} lookslikethematrixinthepreviousexample. More
specifically,\mathcal{T} hasablockdiagonalmatrixwithrespecttothisbasis,witheach
blockasquarematrixthatis0everywhereexceptonthelineabovethediagonal.
Inthenextdefinition,thediagonalofeach\mathcal{A} isfilledwithsomeeigenvalue
k
\lambda of\mathcal{T},thelinedirectlyabovethediagonalof\mathcal{A} isfilledwith1’s,andallother
k k
entriesin\mathcal{A} are0(tounderstandwhyeach \lambda isaneigenvalueof\mathcal{T},see5.41).
k k
The \lambda ’sneednotbedistinct. Also,\mathcal{A} maybea1-by-1matrix(\lambda )containing
k k k
just an eigenvalue of \mathcal{T}. If each \lambda is 0, then the next definition captures the
k
behaviordescribedintheparagraphabove(recallthatif\mathcal{T} isnilpotent,then0is
theonlyeigenvalueof\mathcal{T}).
**8.44 定义：** Jordanbasis
Suppose\mathcal{T} \inℒ(\mathcal{V}). Abasisof\mathcal{V}iscalleda Jordanbasisfor\mathcal{T}ifwithrespect
tothisbasis\mathcal{T} hasablockdiagonalmatrix
\mathcal{A} 0
⎛ 1 ⎞
⎜ ⎟
⎜ ⋱ ⎟
⎜ ⎟
⎝ 0 \mathcal{A} p ⎠
inwhicheach\mathcal{A} isanupper-triangularmatrixoftheform
k
\lambda 1 0
⎛ k ⎞
⎜ ⎟
⎜ ⋱ ⋱ ⎟
\mathcal{A} =⎜ ⎜ ⎟ ⎟.
k ⎜ ⎜ ⋱ 1 ⎟ ⎟
⎝ 0 \lambda ⎠
k
Mostoftheworkinprovingthateveryoperatoronafinite-dimensionalcomplex vector space has a Jordan basis occurs in proving the special case below
ofnilpotentoperators. Thisspecialcaseholdsonrealvectorspacesaswellas
complexvectorspaces.
8.45 everynilpotentoperatorhasa Jordanbasis
Suppose\mathcal{T} \in ℒ(\mathcal{V})isnilpotent. Thenthereisabasisof\mathcal{V} thatisa Jordan
basisfor\mathcal{T}.
Proof Wewillprovethisresultbyinductionondim\mathcal{V}. Togetstarted,notethat
the desired result holds if dim\mathcal{V} = 1 (because in that case, the only nilpotent
operatoristhe0operator). Nowassumethatdim\mathcal{V} >1andthatthedesiredresult
holdsonallvectorspacesofsmallerdimension.

| ---------------------------------------------------------- | --- | --- | --- | --- |
\mathcal{T}m
Let m be the smallest positive integer such that = 0. Thus there exists
| u\in\mathcal{V} suchthat\mathcal{T}m-1u\neq0. | Let |     |     |     |
| -------------------- | --- | --- | --- | --- |
\mathcal{U} =span(u,\mathcal{T}u,…,\mathcal{T}m-1u).
Thelistu,\mathcal{T}u,…,\mathcal{T}m-1uislinearlyindependent(see Exercise2in Section8A).
If\mathcal{U} =\mathcal{V},thenwritingthislistinreverseordergivesa Jordanbasisfor\mathcal{T} andwe
| aredone. Thuswecanassumethat\mathcal{U} |     | \neq\mathcal{V}. |     |     |
| ----------------------------- | --- | --- | --- | --- |
Notethat\mathcal{U} isinvariantunder\mathcal{T}. Byourinductionhypothesis,thereisabasis
of\mathcal{U} thatisa Jordanbasisfor\mathcal{T}| . Thestrategyofourproofisthatwewillfinda
\mathcal{U}
subspace\mathcal{W} of\mathcal{V} suchthat\mathcal{W} isalsoinvariantunder\mathcal{T} and\mathcal{V} =\mathcal{U}\oplus\mathcal{W}. Again
byourinductionhypothesis,therewillbeabasisof\mathcal{W} thatisa Jordanbasisfor
\mathcal{T}| . Puttingtogetherthe Jordanbasesfor\mathcal{T}| and\mathcal{T}| ,wewillhavea Jordan
| \mathcal{W}   |     |     | \mathcal{U} \mathcal{W} |     |
| --- | --- | --- | --- | --- |
basisfor\mathcal{T}.
| Let\phi\in\mathcal{V}′ besuchthat\phi(\mathcal{T}m-1u)\neq0. |     | Let |     |     |
| ----------------------------- | --- | --- | --- | --- |
∶\phi(\mathcal{T}kv)=0foreachk
| \mathcal{W}   | ={v\in\mathcal{V} |     | =0,…,m-1}. |     |
| --- | ----- | --- | ---------- | --- |
Then\mathcal{W}isasubspaceof\mathcal{V}thatisinvariantunder\mathcal{T}(theinvarianceholdsbecause
| ifv \in \mathcal{W} then\phi(\mathcal{T}k(\mathcal{T}v)) | = 0fork | = 0,…,m-1, | wherethecasek | = m-1 |
| --------------------- | ------- | ---------- | ------------- | ----- |
holdsbecause\mathcal{T}m
|     | =0). Wewillshowthat\mathcal{V} |     | =\mathcal{U}\oplus\mathcal{W},whichbytheprevious |     |
| --- | -------------------- | --- | ----------------------- | --- |
paragraphwillcompletetheproof.
| Toshowthat\mathcal{U}+\mathcal{W}   | isadirectsum,supposev\in\mathcal{U}\cap\mathcal{W}withv\neq0. |             |     | Because |
| --------------- | --------------------------------- | ----------- | --- | ------- |
| v\in\mathcal{U},thereexistc | ,…,c                              | \in\mathbf{F} suchthat |     |         |
0 m-1
|     | v=c u+c | \mathcal{T}u+⋯+c | \mathcal{T}m-1u. |     |
| --- | ------- | ------ | ------ | --- |
|     | 0       | 1      | m-1    |     |
Letj bethesmallestindexsuchthatc \neq 0. Apply\mathcal{T}m-j-1 tobothsidesofthe
j
equationabove,getting
\mathcal{T}m-j-1v=c\mathcal{T}m-1u,
j
\mathcal{T}m
where we have used the equation = 0. Now apply \phi to both sides of the
equationabove,getting
\phi(\mathcal{T}m-j-1v)=c\phi(\mathcal{T}m-1u)\neq0.
j
| Theequationaboveshowsthatv\notin\mathcal{W}. |                        | Hencewehaveprovedthat\mathcal{U}\cap\mathcal{W} |     | ={0}, |
| ----------------------------- | ---------------------- | ------------------------ | --- | ----- |
| whichimpliesthat\mathcal{U}+\mathcal{W}           | isadirectsum(see1.46). |                          |     |       |
| Toshowthat\mathcal{U}\oplus\mathcal{W}                 | =\mathcal{V},define\mathcal{S}∶            | \mathcal{V} \rightarrow\mathbf{F}m                    | by  |       |
\mathcal{S}v=(\phi(v),\phi(\mathcal{T}v),…,\phi(\mathcal{T}m-1v)).
| Thusnull\mathcal{S}=\mathcal{W}. | Hence |     |     |     |
| ------------ | ----- | --- | --- | --- |
dim\mathcal{W} =dimnull\mathcal{S}=dim\mathcal{V}-dimrange\mathcal{S}\geqdim\mathcal{V}-m,
wherethesecondequalitycomesfromthefundamentaltheoremoflinearmaps
$$(3.21). Usingtheinequalityabove,wehave$$
| dim(\mathcal{U}\oplus\mathcal{W})=dim\mathcal{U}+dim\mathcal{W} |                              | \geqm+(dim\mathcal{V}-m)=dim\mathcal{V}. |     |     |
| ------------------ | ---------------------------- | ----------------- | --- | --- |
| Thus\mathcal{U}\oplus\mathcal{W} =\mathcal{V}         | (by2.39),completingtheproof. |                   |     |     |

| -------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
| Now the | generalized | eigenspace |     | de-     |        |             |     |      |
| ------- | ----------- | ---------- | --- | ------- | ------ | ----------- | --- | ---- |
|         |             |            |     | Camille | Jordan | (1838–1922) |     | pub- |
compositionallowsustoextendtheprelishedaproofof8.46in1870.
viousresulttooperatorsthatmaynotbe
nilpotent. Doingthisrequiresthatwedealwithcomplexvectorspaces.
8.46 Jordanform
| Suppose\mathbf{F} | = \mathbf{C} and\mathcal{T} | \in   | ℒ(\mathcal{V}). Thenthereisabasisof\mathcal{V} |     |     | thatisa Jordan |     |     |
| -------- | -------- | --- | -------------------------- | --- | --- | ------------- | --- | --- |
basisfor\mathcal{T}.
Proof Let\lambda ,…,\lambda bethedistincteigenvaluesof\mathcal{T}. Thegeneralizedeigenspace
1 m
decompositionstatesthat
|     |     | \mathcal{V} =\mathcal{G}(\lambda | ,\mathcal{T})\oplus⋯\oplus\mathcal{G}(\lambda |     | ,\mathcal{T}), |     |     |     |
| --- | --- | ------ | --------- | --- | ---- | --- | --- | --- |
|     |     |        | 1         |     | m    |     |     |     |
whereeach(\mathcal{T}- \lambda \mathcal{I})| isnilpotent(see8.22). Thus8.45impliesthatsome
|     | k   | \mathcal{G}(\lambda k ,\mathcal{T}) |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- |
basis of each \mathcal{G}(\lambda ,\mathcal{T}) is a Jordan basis for (\mathcal{T} - \lambda \mathcal{I})| . Put these bases
|     | k   |     |     |     | k   | \mathcal{G}(\lambda ,\mathcal{T}) |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- |
k
| togethertogetabasisof\mathcal{V} |                         |              | thatisa Jordanbasisfor\mathcal{T}. |             |     |         |          |         |
| ---------------------- | ----------------------- | ------------ | ----------------------- | ----------- | --- | ------- | -------- | ------- |
| Exercises              | 8C                      |              |                         |             |     |         |          |         |
| Suppose                |                         | ℒ(\mathbf{C}3)        | is the operator         | defined     | by  | ,z ,z   |          | ,z ,0). |
| 1                      | \mathcal{T} \in                     |              |                         |             |     | \mathcal{T}(z 1 2 | 3 ) =    | (z 2 3  |
| Provethat\mathcal{T}             | doesnothaveasquareroot. |              |                         |             |     |         |          |         |
| 2 Define\mathcal{T}              | \inℒ(\mathbf{F}5)by\mathcal{T}(x             |              | ,x ,x                   | ,x ,x )=(2x |     | ,3x ,-x | ,4x ,0). |         |
|                        |                         |              | 1 2                     | 3 4 5       |     | 2 3     | 4 5      |         |
| (a) Showthat\mathcal{T}          |                         | isnilpotent. |                         |             |     |         |          |         |
$$(b) Findasquarerootof\mathcal{I}+\mathcal{T}.$$
3 Suppose\mathcal{V} isacomplexvectorspace. Provethateveryinvertibleoperator
| on\mathcal{V} | hasacuberoot. |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
4 Suppose \mathcal{V} is a real vector space. Prove that the operator -\mathcal{I} on \mathcal{V} has a
| squarerootifandonlyifdim\mathcal{V} |                                                  |     |     | isanevennumber. |     |     |     |     |
| ------------------------- | ------------------------------------------------ | --- | --- | --------------- | --- | --- | --- | --- |
| Suppose\mathcal{T}                  | \inℒ(\mathbf{C}2)istheoperatordefinedby\mathcal{T}(w,z)=(-w-z,9w+5z). |     |     |                 |     |     |     |     |
Finda Jordanbasisfor\mathcal{T}.
6 Findabasisof𝒫 (\mathbf{R})thatisa Jordanbasisforthedifferentiationoperator
| \mathcal{D}on𝒫 | (\mathbf{R})definedby\mathcal{D}p=p′. |     |     |     |     |     |     |     |
| ---- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
|            | \inℒ(\mathcal{V})isnilpotentandv |     |     | ,…,v |                     |     |     |       |
| ---------- | -------------------- | --- | --- | ---- | ------------------- | --- | --- | ----- |
| 7 Suppose\mathcal{T} |                      |     |     |      | isa Jordanbasisfor\mathcal{T}. |     |     | Prove |
1 n
thattheminimalpolynomialof\mathcal{T}iszm+1,wheremisthelengthofthelongest
consecutivestringof1’sthatappearsonthelinedirectlyabovethediagonal
| inthematrixof\mathcal{T} |     | withrespecttov |     | ,…,v | .   |     |     |     |
| -------------- | --- | -------------- | --- | ---- | --- | --- | --- | --- |
|                |     |                |     | 1    | n   |     |     |     |
8 Suppose\mathcal{T} \inℒ(\mathcal{V})andv ,…,v isabasisof\mathcal{V} thatisa Jordanbasisfor\mathcal{T}.
|     |     |     | 1   | n   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Describethematrixof\mathcal{T}2
withrespecttothisbasis.

| --------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
9 Suppose\mathcal{T} \in ℒ(\mathcal{V})isnilpotent. Explainwhythereexist v ,…,v \in \mathcal{V}
|                         |           |          |                                      |                 |     | 1 n |
| ----------------------- | --------- | -------- | ------------------------------------ | --------------- | --- | --- |
| andnonnegativeintegersm |           |          | ,…,m suchthat(a)and(b)belowbothhold. |                 |     |     |
|                         |           | 1        | n                                    |                 |     |     |
| (a) \mathcal{T}m                  | 1v ,…,\mathcal{T}v  | ,v ,…,\mathcal{T}m | nv ,…,\mathcal{T}v                             | ,v isabasisof\mathcal{V}. |     |     |
|                         | 1         | 1 1      | n n                                  | n               |     |     |
| \mathcal{T}m                      | +1v =⋯=\mathcal{T}m | +1v      |                                      |                 |     |     |
| (b)                     | 1         | n        | =0.                                  |                 |     |     |
|                         | 1         |          | n                                    |                 |     |     |
10 Suppose\mathcal{T} \inℒ(\mathcal{V})andv ,…,v isabasisof\mathcal{V} thatisa Jordanbasisfor\mathcal{T}.
|     |     | 1   | n   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Describe the matrix of with respect to the basis ,…,v obtained by
|     |     | \mathcal{T}   |     |     | v n 1 |     |
| --- | --- | --- | --- | --- | ----- | --- |
reversingtheorderofthev’s.
11 Suppose\mathcal{T} \inℒ(\mathcal{V}). Explainwhyeveryvectorineach Jordanbasisfor\mathcal{T} is
ageneralizedeigenvectorof\mathcal{T}.
12 Suppose\mathcal{T} \inℒ(\mathcal{V})isdiagonalizable. Showthatℳ(\mathcal{T})isadiagonalmatrix
withrespecttoevery Jordanbasisfor\mathcal{T}.
|             | \inℒ(\mathcal{V})isnilpotent. |     |              | ,…,v |               |     |
| ----------- | ----------------- | --- | ------------ | ---- | ------------- | --- |
| 13 Suppose\mathcal{T} |                   |     | Provethatifv |      | arevectorsin\mathcal{V} | and |
1 n
| m ,…,m | arenonnegativeintegerssuchthat |                |          |     |             |     |
| ------ | ------------------------------ | -------------- | -------- | --- | ----------- | --- |
| 1      | n                              |                |          |     |             |     |
|        | \mathcal{T}m 1v                          | ,…,\mathcal{T}v ,v ,…,\mathcal{T}m | nv ,…,\mathcal{T}v | ,v  | isabasisof\mathcal{V} |     |
|        |                                | 1 1 1          | n        | n n |             |     |
and
|        |          | \mathcal{T}m 1 +1v            | =⋯=\mathcal{T}m | n +1v =0, |     |     |
| ------ | -------- | ------------------- | ----- | --------- | --- | --- |
|        |          |                     | 1     | n         |     |     |
| then\mathcal{T}m | 1v ,…,\mathcal{T}m | nv isabasisofnull\mathcal{T}. |       |           |     |     |
|        | 1        | n                   |       |           |     |     |
Thisexerciseshowsthat n = dimnull\mathcal{T}. Thusthepositiveinteger nthat
appears above depends only on \mathcal{T} and not on the specific Jordan basis
chosenfor\mathcal{T}.
\inℒ(\mathcal{V}).
| 14 Suppose\mathbf{F} | =\mathbf{C}  | and\mathcal{T} | Provethattheredoesnotexistadirectsum |     |     |     |
| ----------- | --- | ---- | ------------------------------------ | --- | --- | --- |
decompositionof\mathcal{V} intotwononzerosubspacesinvariantunder\mathcal{T} ifand
\lambda)dim\mathcal{V}
| onlyiftheminimalpolynomialof\mathcal{T} |     |     | isoftheform(z- |     |     | forsome |
| ----------------------------- | --- | --- | -------------- | --- | --- | ------- |
\lambda\in\mathbf{C}.

| -------- | ------------------------------ | --- | --- | --- |
| 8D Trace: | A Connection | Between | Matrices | and Operators |
| --------- | ------------ | ------- | -------- | ------------- |
Webeginthissectionbydefiningthetraceofasquarematrix. Afterdeveloping
somepropertiesofthetraceofasquarematrix,wewillusethisconcepttodefine
thetraceofanoperator.
| 8.47 definition: | traceofamatrix |     |     |     |
| ---------------- | -------------- | --- | --- | --- |
Suppose\mathcal{A}isasquarematrixwithentriesin\mathbf{F}. Thetraceof\mathcal{A},denotedtr\mathcal{A},
isdefinedtobethesumofthediagonalentriesof\mathcal{A}.
| 8.48 example: | traceofa3-by-3matrix |     |     |     |
| ------------- | -------------------- | --- | --- | --- |
Suppose
|     |     | 3 -1    | -2      |     |
| --- | --- | ------- | ------- | --- |
|     |     | ⎛ ⎜     | ⎞ ⎟     |     |
|     |     | \mathcal{A}=⎜ 5 2 | -3 ⎟ ⎟. |     |
⎜
|     |     | ⎝ 1 6 | 0 ⎠ |     |
| --- | --- | ----- | --- | --- |
Thediagonalentriesof\mathcal{A},whichareshowninredabove,are3,2,and0. Thus
tr\mathcal{A}=3+2+0=5.
Matrixmultiplicationisnotcommutative,butthenextresultshowsthatthe
orderofmatrixmultiplicationdoesnotmattertothetrace.
8.49 traceof\mathcal{A}\mathcal{B}equalstraceof\mathcal{B}\mathcal{A}
| Suppose\mathcal{A}isanm-by-nmatrixand\mathcal{B}isann-by-mmatrix. |     |     |     | Then |
| --------------------------------------------- | --- | --- | --- | ---- |
tr(\mathcal{A}\mathcal{B})=tr(\mathcal{B}\mathcal{A}).
Suppose
Proof
|     | \mathcal{A}     | ⋯ \mathcal{A}   | \mathcal{B}     | ⋯ \mathcal{B}   |
| --- | ----- | ----- | ----- | ----- |
|     | ⎛ 1,1 | 1,n ⎞ | ⎛ 1,1 | 1,m ⎞ |
|     | \mathcal{A}=⎜ ⎜ | ⎟ ⎟   | \mathcal{B}=⎜ ⎜ | ⎟ ⎟   |
|     | ⎜ ⋮   | ⋮ ⎟,  | ⎜ ⋮   | ⋮ ⎟.  |
|     | ⎜     | ⎟     | ⎜     | ⎟     |
|     | ⎝ \mathcal{A}   | ⋯ \mathcal{A} ⎠ | ⎝ \mathcal{B}   | ⋯ \mathcal{B} ⎠ |
|     | m,1   | m,n   | n,1   | n,m   |
Thejthtermonthediagonalofthem-by-mmatrix\mathcal{A}\mathcal{B}equals\sumn
\mathcal{A} j,k \mathcal{B} k,j . Thus
$$k=1$$
m n
tr(\mathcal{A}\mathcal{B})=
|     | \sum \sum\mathcal{A} | j,k \mathcal{B} k,j |     |     |
| --- | ---- | --------- | --- | --- |
$$j=1k=1$$
n m
|     | = \sum \sum | \mathcal{B} \mathcal{A} |     |     |
| --- | ----- | --- | --- | --- |
k,j j,k
$$k=1j=1$$
n
|     | = \sum(kth | termondiagonalofthen-by-nmatrix\mathcal{B}\mathcal{A}) |     |     |
| --- | ------- | ---------------------------------- | --- | --- |
$$k=1$$
=tr(\mathcal{B}\mathcal{A}),
asdesired.

| --------- | --------------------------------------------- | --- | --- | --- | --- |
| Wewanttodefinethetraceofanoperator\mathcal{T} |     |     |     | \in ℒ(\mathcal{V})tobethetraceofthe |     |
| ----------------------------------- | --- | --- | --- | ----------------------- | --- |
matrixof\mathcal{T} withrespecttosomebasisof\mathcal{V}. However,thisdefinitionshouldnot
dependonthechoiceofbasis. Thefollowingresultwillmakethispossible.
traceofmatrixofoperatordoesnotdependonbasis
8.50
| Suppose\mathcal{T} | \inℒ(\mathcal{V}). Supposeu |      | ,…,u andv   | ,…,v arebasesof\mathcal{V}. | Then |
| -------- | --------------- | ---- | ----------- | ----------------- | ---- |
|          |                 |      | 1 n 1       | n                 |      |
|          | trℳ(\mathcal{T},(u        | ,…,u | ))=trℳ(\mathcal{T},(v | ,…,v )).          |      |
|          |                 | 1    | n           | 1 n               |      |
Proof Let \mathcal{A} = ℳ(\mathcal{T},(u ,…,u )) and \mathcal{B} = ℳ(\mathcal{T},(v ,…,v )). The change-
|     |     | 1   | n   | 1 n |     |
| --- | --- | --- | --- | --- | --- |
of-basisformulatellsusthatthereexistsaninvertiblen-by-nmatrix\mathcal{C}suchthat
| \mathcal{A}=\mathcal{C}-1\mathcal{B}\mathcal{C}(see3.84). |     | Thus |     |     |     |
| ----------------- | --- | ---- | --- | --- | --- |
tr\mathcal{A}=tr((\mathcal{C}-1\mathcal{B})\mathcal{C})
=tr(\mathcal{C}(\mathcal{C}-1\mathcal{B}))
=tr((\mathcal{C}\mathcal{C}-1)\mathcal{B})
=tr\mathcal{B},
wherethesecondlinecomesfrom8.49.
Becauseof8.50,thefollowingdefinitionnowmakessense.
| 8.51 definition: | traceofanoperator                         |               |      |     |     |
| ---------------- | ----------------------------------------- | ------------- | ---- | --- | --- |
| Suppose\mathcal{T}         | \inℒ(\mathcal{V}). Thetraceof\mathcal{T},denotedtr\mathcal{T},isdefinedby |               |      |     |     |
|                  |                                           | tr\mathcal{T} =trℳ(\mathcal{T},(v | ,…,v | )), |     |
|                  |                                           |               | 1    | n   |     |
| wherev ,…,v      | isanybasisof\mathcal{V}.                            |               |      |     |     |
| 1                | n                                         |               |      |     |     |
ℒ(\mathcal{V})and
| Suppose\mathcal{T} | \in   | \lambdaisaneigenvalueof\mathcal{T}. |     | Recallthatwedefinedthe |     |
| -------- | --- | ------------------- | --- | ---------------------- | --- |
multiplicityof \lambdatobethedimensionofthegeneralizedeigenspace\mathcal{G}(\lambda,\mathcal{T})(see
\lambda\mathcal{I})dim\mathcal{V}
8.23); weprovedthatthismultiplicityequalsdimnull(\mathcal{T} - (see8.20).
Recallalsothatif\mathcal{V} isacomplexvectorspace,thenthesumofthemultiplicities
| ofalleigenvaluesof\mathcal{T} | equalsdim\mathcal{V} |     | (see8.25). |     |     |
| ------------------- | ---------- | --- | ---------- | --- | --- |
In the following result, the sum of the eigenvalues “with each eigenvalue
,…,\lambda
includedasmanytimesasitsmultiplicity”meansthatif\lambda arethedistinct
|                |                     |     |                    | 1 m |     |
| -------------- | ------------------- | --- | ------------------ | --- | --- |
| eigenvaluesof\mathcal{T} | withmultiplicitiesd |     | ,…,d ,thenthesumis |     |     |
|                |                     |     | 1 m                |     |     |
|                |                     | d   | \lambda +⋯+d \lambda           | .   |     |
|                |                     | 1   | 1 m m              |     |     |
Orifyouprefertoworkwithalistofnot-necessarily-distincteigenvalues,with
eacheigenvalueincludedasmanytimesasitsmultiplicity,thentheeigenvalues
| couldbedenotedby | \lambda ,…,\lambda | (wherenequalsdim\mathcal{V})andthesumis |           |     |     |
| ---------------- | ------ | ----------------------------- | --------- | --- | --- |
|                  | 1      | n                             |           |     |     |
|                  |        |                               | \lambda +⋯+ \lambda . |     |     |
|                  |        |                               | 1 n       |     |     |

| --- | -------- | --- | ------------------------------ | --- | --- | --- |
oncomplexvectorspaces,traceequalssumofeigenvalues
8.52
| Suppose\mathbf{F} | =\mathbf{C}  | and\mathcal{T} | \inℒ(\mathcal{V}). | Thentr\mathcal{T} | equalsthesumoftheeigenvalues |     |
| -------- | --- | ---- | ------ | ------- | ---------------------------- | --- |
of\mathcal{T},witheacheigenvalueincludedasmanytimesasitsmultiplicity.
Proof There is a basis of \mathcal{V} with respect to which \mathcal{T} has an upper-triangular
matrixwiththediagonalentriesofthematrixconsistingoftheeigenvaluesof\mathcal{T},
witheacheigenvalueincludedasmanytimesasitsmultiplicity—see8.37. Thus
thedefinitionofthetraceofanoperatoralongwith8.50,whichallowsustousea
basisofourchoice,impliesthattr\mathcal{T} equalsthesumoftheeigenvaluesof\mathcal{T},with
eacheigenvalueincludedasmanytimesasitsmultiplicity.
traceofanoperatoron\mathbf{C}3
**8.53 例：** | Suppose\mathcal{T}         |     | \inℒ(\mathbf{C}3)isdefinedby |                                   |        |         |               |
| ---------------- | --- | ----------------- | --------------------------------- | ------ | ------- | ------------- |
|                  | \mathcal{T}(z | ,z ,z             | )=(3z                             | -z -2z | ,3z +2z | -3z ,z +2z ). |
|                  |     | 1 2               | 3                                 | 1 2    | 3 1 2   | 3 1 2         |
| Thenthematrixof\mathcal{T} |     |                   | withrespecttothestandardbasisof\mathbf{C}3 |        |         | is            |
|                  |     |                   |                                   | 3 -1   | -2      |               |
|                  |     |                   |                                   | ⎛ ⎜    | ⎞ ⎟     |               |
|                  |     |                   |                                   | ⎜ 3 2  | -3 ⎟ ⎟. |               |
⎜
|                                                     |     |     |     | ⎝ 1 2 | 0 ⎠ |     |
| --------------------------------------------------- | --- | --- | --- | ----- | --- | --- |
| Addingupthediagonalentriesofthismatrix,weseethattr\mathcal{T} |     |     |     |       |     | =5. |
The eigenvalues of \mathcal{T} are 1, 2+3i, and 2-3i, each with multiplicity 1, as
youcanverify. Thesumoftheseeigenvalues,eachincludedasmanytimesasits
multiplicity,is1+(2+3i)+(2-3i),whichequals5,asexpectedby8.52.
Thetracehasacloseconnectionwiththecharacteristicpolynomial. Suppose
\mathbf{F} =\mathbf{C},\mathcal{T} \inℒ(\mathcal{V}),and \lambda ,…,\lambda aretheeigenvaluesof\mathcal{T},witheacheigenvalue
|     |     |     | 1   | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
included as many times as its multiplicity. Then by definition (see 8.26), the
| characteristicpolynomialof\mathcal{T} |     |     |     | equals      |      |     |
| --------------------------- | --- | --- | --- | ----------- | ---- | --- |
|                             |     |     |     | (z- \lambda )⋯(z- | \lambda ). |     |
|                             |     |     |     | 1           | n    |     |
Expandingthepolynomialabove,wecanwritethecharacteristicpolynomialof\mathcal{T}
intheform
|     |     | zn-(\lambda | +⋯+ | \lambda )zn-1+⋯+(-1)n(\lambda |     | ⋯\lambda ). |
| --- | --- | ----- | --- | ----------------- | --- | ----- |
|     |     |       | 1   | n                 |     | 1 n   |
The expression above immediately leads to the next result. Also see 9.65,
| whichdoesnotrequirethehypothesisthat\mathbf{F} |     |     |     |     | =\mathbf{C}. |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- |
8.54 traceandcharacteristicpolynomial
| Suppose\mathbf{F}               | =\mathbf{C}and\mathcal{T} |     | \inℒ(\mathcal{V}). | Letn=dim\mathcal{V}.                        | Thentr\mathcal{T}equalsthenegative |     |
| ---------------------- | ------ | --- | ------ | --------------------------------- | ------------------------ | --- |
| ofthecoefficientofzn-1 |        |     |        | inthecharacteristicpolynomialof\mathcal{T}. |                          |     |

| --------- | --------------------------------------------- | --- | --- | --- |
Thenextresultgivesaniceformulaforthetraceofanoperatoronaninner
productspace.
8.55 traceonaninnerproductspace
Suppose\mathcal{V} isaninnerproductspace,\mathcal{T} \inℒ(\mathcal{V}),ande ,…,e isanorthonor-
|              |          |            | 1     | n   |
| ------------ | -------- | ---------- | ----- | --- |
| malbasisof\mathcal{V}. | Then     |            |       |     |
|              | tr\mathcal{T} =\langle\mathcal{T}e | ,e \rangle+⋯+\langle\mathcal{T}e | ,e \rangle. |     |
|              |          | 1 1        | n n   |     |
Proof Thedesiredformulafollowsfromtheobservationthattheentryinrowk,
| columnkofℳ(\mathcal{T},(e | ,…,e ))equals\langle\mathcal{T}e | ,e  | \rangle[use6.30(a)withv=\mathcal{T}e | ].  |
| --------------- | ---------------- | --- | -------------------- | --- |
|                 | 1 n              | k   | k                    | k   |
Thealgebraicpropertiesofthetraceasdefinedonsquarematricestranslate
toalgebraicpropertiesofthetraceasdefinedonoperators,asshowninthenext
result.
8.56 traceislinear
| Thefunctiontr∶ | ℒ(\mathcal{V})\rightarrow\mathbf{F} isalinearfunctionalonℒ(\mathcal{V})suchthat |     |     |     |
| -------------- | ---------------------------------------- | --- | --- | --- |
tr(\mathcal{S}\mathcal{T})=tr(\mathcal{T}\mathcal{S})
| forall\mathcal{S},\mathcal{T} \inℒ(\mathcal{V}). |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
Proof Chooseabasisof\mathcal{V}. Allmatricesofoperatorsinthisproofwillbewith
| respecttothatbasis. | Suppose\mathcal{S},\mathcal{T} | \inℒ(\mathcal{V}). |     |     |
| ------------------- | ---------- | ------ | --- | --- |
If \lambda\in\mathbf{F},then
| tr(\lambda\mathcal{T})=trℳ(\lambda\mathcal{T})=tr(\lambdaℳ(\mathcal{T}))= |     |     | \lambdatrℳ(\mathcal{T})= | \lambdatr\mathcal{T}, |
| ------------------------- | --- | --- | -------- | ----- |
where the first and last equalities come from the definition of the trace of an
operator, the second equality comes from 3.38, and the third equality follows
fromthedefinitionofthetraceofasquarematrix.
Also,
tr(\mathcal{S}+\mathcal{T})=trℳ(\mathcal{S}+\mathcal{T})=tr(ℳ(\mathcal{S})+ℳ(\mathcal{T}))=trℳ(\mathcal{S})+trℳ(\mathcal{T})=tr\mathcal{S}+tr\mathcal{T},
where the first and last equalities come from the definition of the trace of an
operator, the second equality comes from 3.35, and the third equality follows
fromthedefinitionofthetraceofasquarematrix. Thetwoparagraphsabove
| showthattr∶ ℒ(\mathcal{V})\rightarrow\mathbf{F} | isalinearfunctionalonℒ(\mathcal{V}). |     |     |     |
| ------------------ | -------------------------- | --- | --- | --- |
Furthermore,
tr(\mathcal{S}\mathcal{T})=trℳ(\mathcal{S}\mathcal{T})=tr(ℳ(\mathcal{S})ℳ(\mathcal{T}))=tr(ℳ(\mathcal{T})ℳ(\mathcal{S}))=trℳ(\mathcal{T}\mathcal{S})=tr(\mathcal{T}\mathcal{S}),
where the second and fourth equalities come from 3.43 and the crucial third
equalitycomesfrom8.49.
The equations tr(\mathcal{S}\mathcal{T}) = tr(\mathcal{T}\mathcal{S}) and tr\mathcal{I} = dim\mathcal{V} uniquely characterize the
traceamongthelinearfunctionalsonℒ(\mathcal{V})—see Exercise10.

| -------- | --- | ------------------------------ | --- | --- |
| Theequationtr(\mathcal{S}\mathcal{T}) |     | = tr(\mathcal{T}\mathcal{S})leads |     |     |
| ----------------- | --- | ------------- | --- | --- |
Thestatementofthenextresultdoes
toournextresult,whichdoesnotholdon
notinvolvetraces,buttheshortproof
infinite-dimensional vector spaces (see usestraces. Whensomethinglikethis
| Exercise | 13). However, | additional | hy- |     |
| -------- | ------------- | ---------- | --- | --- |
happensinmathematics,thenusually
potheseson\mathcal{S},\mathcal{T},and\mathcal{V}leadtoaninfinite- a good definition lurks in the back-
| dimensionalgeneralizationoftheresult |           |              | ground. |     |
| ------------------------------------ | --------- | ------------ | ------- | --- |
| below, with                          | important | applications | to      |     |
quantumtheory.
| 8.57 identityoperatorisnotthedifferenceof |     |             |                       | \mathcal{S}\mathcal{T} and \mathcal{T}\mathcal{S} |
| ----------------------------------------- | --- | ----------- | --------------------- | --------- |
| Theredonotexistoperators\mathcal{S},\mathcal{T}               |     |             | \inℒ(\mathcal{V})suchthat\mathcal{S}\mathcal{T}-\mathcal{T}\mathcal{S}=\mathcal{I}. |           |
| Proof Suppose\mathcal{S},\mathcal{T}                          |     | \inℒ(\mathcal{V}). Then |                       |           |
tr(\mathcal{S}\mathcal{T}-\mathcal{T}\mathcal{S})=tr(\mathcal{S}\mathcal{T})-tr(\mathcal{T}\mathcal{S})=0,
wherebothequalitiescomefrom8.56. Thetraceof\mathcal{I}equalsdim\mathcal{V},whichisnot0.
| Because\mathcal{S}\mathcal{T}-\mathcal{T}\mathcal{S}and\mathcal{I} |     | havedifferenttraces,theycannotbeequal. |     |     |
| ---------------- | --- | -------------------------------------- | --- | --- |
| Exercises        | 8D  |                                        |     |     |
Suppose \mathcal{V} is an inner product space and v,w \in \mathcal{V}. Define an operator
| \mathcal{T} \inℒ(\mathcal{V})by\mathcal{T}u=\langleu,v\ranglew. |                  |     | Findaformulafortr\mathcal{T}. |     |
| ------------------- | ---------------- | --- | ------------------- | --- |
| 2 Suppose\mathcal{P}          | \inℒ(\mathcal{V})satisfies\mathcal{P}2 |     | =\mathcal{P}. Provethat       |     |
tr\mathcal{P} =dimrange\mathcal{P}.
3 Suppose\mathcal{T} \inℒ(\mathcal{V})and\mathcal{T}5 =\mathcal{T}. Provethattherealandimaginarypartsof
tr\mathcal{T} arebothintegers.
| 4 Suppose\mathcal{V} | isaninnerproductspaceand\mathcal{T} |     |     | \inℒ(\mathcal{V}). Provethat |
| ---------- | ------------------------- | --- | --- | ---------------- |
tr\mathcal{T} ∗ =tr\mathcal{T}.
5 Suppose \mathcal{V} is an inner product space. Suppose \mathcal{T} \in ℒ(\mathcal{V}) is a positive
| operatorandtr\mathcal{T} |     | =0. Provethat\mathcal{T} | =0. |     |
| -------------- | --- | -------------- | --- | --- |
Suppose is an inner product space and \mathcal{P},\mathcal{Q} ℒ(\mathcal{V}) are orthogonal
| 6            | \mathcal{V}                                |     |     | \in   |
| ------------ | -------------------------------- | --- | --- | --- |
| projections. | Provethattr(\mathcal{P}\mathcal{Q})\geq0.               |     |     |     |
| 7 Suppose\mathcal{T}   | \inℒ(\mathbf{C}3)istheoperatorwhosematrixis |     |     |     |
51 -12 -21
|     |     | ⎛ ⎜ |        | ⎞ ⎟      |
| --- | --- | --- | ------ | -------- |
|     |     | ⎜   | 60 -40 | -28 ⎟ ⎟. |
⎜
|     |     | ⎝   | 57 -68 | 1 ⎠ |
| --- | --- | --- | ------ | --- |
Someonetellsyou(accurately)that-48and24areeigenvaluesof\mathcal{T}. Without
usingacomputerorwritinganythingdown,findthethirdeigenvalueof\mathcal{T}.

| ---------------- | -------------------------------------- | --- | --- | --- |
8 Proveorgiveacounterexample: If\mathcal{S},\mathcal{T} \inℒ(\mathcal{V}),thentr(\mathcal{S}\mathcal{T})=(tr\mathcal{S})(tr\mathcal{T}).
9 Suppose\mathcal{T} \in ℒ(\mathcal{V})issuchthattr(\mathcal{S}\mathcal{T}) = 0forall\mathcal{S} \in ℒ(\mathcal{V}). Provethat
\mathcal{T} =0.
10 Provethatthetraceistheonlylinearfunctional\tau∶ ℒ(\mathcal{V})\rightarrow\mathbf{F} suchthat
\tau(\mathcal{S}\mathcal{T})=\tau(\mathcal{T}\mathcal{S})
forall\mathcal{S},\mathcal{T} \inℒ(\mathcal{V})and\tau(\mathcal{I})=dim\mathcal{V}.
Hint:Supposethat v ,…,v isabasisof \mathcal{V}. For j,k \in {1,…,n},define
1 n
| \inℒ(\mathcal{V})by\mathcal{P} | +⋯+a         |           | v. Provethat |     |
| -------- | ------------ | --------- | ------------ | --- |
| \mathcal{P} j,k    | j,k (a 1 v 1 | n v n )=a | k j          |     |
⎧ ifj=k,
{1
|     | \tau(\mathcal{P} | )= ⎨ |     |     |
| --- | --- | ---- | --- | --- |
j,k { ⎩0 ifj\neqk.
| Thenfor\mathcal{T} \inℒ(\mathcal{V}),usetheequation\mathcal{T} |     |     | =\sumn \sumn | ℳ(\mathcal{T}) \mathcal{P} toshow |
| ------------------------------ | --- | --- | ------ | ------------- |
|                                |     |     | k=1    | j=1 j,k j,k   |
that\tau(\mathcal{T})=tr\mathcal{T}.
11 Suppose\mathcal{V} and\mathcal{W} areinnerproductspacesand\mathcal{T} \inℒ(\mathcal{V},\mathcal{W}). Provethatif
e ,…,e isanorthonormalbasisof\mathcal{V} and f ,…, f isanorthonormalbasis
| 1 n |     |     | 1   | m   |
| --- | --- | --- | --- | --- |
of\mathcal{W},then
n m
∗
|     | tr(\mathcal{T} \mathcal{T})= | \sum \sum|\langle\mathcal{T}e | , f\rangle|2. |     |
| --- | -------- | ------- | ------- | --- |
k j
$$k=1j=1$$
Thenumbers\langle\mathcal{T}e , f\ranglearetheentriesofthematrixof \mathcal{T}withrespecttothe
k j
| orthonormalbasese | ,…,e | and f ,…, | f . Thesenumbersdependonthe |     |
| ----------------- | ---- | --------- | --------------------------- | --- |
|                   | 1 n  | 1         | m                           |     |
bases,buttr(\mathcal{T} ∗ \mathcal{T})doesnotdependonachoiceofbases. Thusthisexercise
showsthatthesumofthesquaresoftheabsolutevaluesofthematrixentries
doesnotdependonwhichorthonormalbasesareused.
| 12 Suppose\mathcal{V} and\mathcal{W} | arefinite-dimensionalinnerproductspaces. |     |     |     |
| ---------------- | ---------------------------------------- | --- | --- | --- |
∗
| (a) Provethat\langle\mathcal{S},\mathcal{T}\rangle=tr(\mathcal{T} |     | \mathcal{S})definesaninnerproductonℒ(\mathcal{V},\mathcal{W}). |     |     |
| ----------------------- | --- | -------------------------------- | --- | --- |
$$(b) Suppose e ,…,e is an orthonormal basis of \mathcal{V} and f ,…, f is an$$
|                      | 1 n                                 |     |     | 1 m |
| -------------------- | ----------------------------------- | --- | --- | --- |
| orthonormalbasisof\mathcal{W}. | Showthattheinnerproductonℒ(\mathcal{V},\mathcal{W})from |     |     |     |
$$(a)isthesameasthestandardinnerproducton\mathbf{F}mn,whereweidentify$$
eachelementofℒ(\mathcal{V},\mathcal{W})withitsmatrix(withrespecttothebasesjust
mentioned)andthenwithanelementof\mathbf{F}mn.
\inℒ(\mathcal{V},\mathcal{W})asdefinedby7.86isnot
Caution: Thenormofalinearmap\mathcal{T}
thesameasthenormthatcomesfromtheinnerproductin(a)above. Unless
explicitlystatedotherwise,alwaysassumethat‖\mathcal{T}‖referstothenormas
definedby7.86. Thenormthatcomesfromtheinnerproductin(a)iscalled
the Frobeniusnormorthe Hilbert–Schmidtnorm.
13 Find\mathcal{S},\mathcal{T} \inℒ(𝒫(\mathbf{F}))suchthat\mathcal{S}\mathcal{T}-\mathcal{T}\mathcal{S}=\mathcal{I}.
Hint:Makeanappropriatemodificationoftheoperatorsin Example3.9.
Thisexerciseshowsthatadditionalhypothesesareneededon\mathcal{S}and\mathcal{T}to
extend8.57tothesettingofinfinite-dimensionalvectorspaces.
