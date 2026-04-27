---
title: Chapter 1
source: Clippings/LADR4e.pdf
created: 2026-04-23
type: chapter
tags:
  - book
  - chapter
---

# Chapter 1
Linearalgebraisthestudyoflinearmapsonfinite-dimensionalvectorspaces.
Eventuallywewilllearnwhatallthesetermsmean. Inthischapterwewilldefine
vectorspacesanddiscusstheirelementaryproperties.
Inlinearalgebra,bettertheoremsandmoreinsightemergeifcomplexnumbers
areinvestigatedalongwithrealnumbers. Thuswewillbeginbyintroducingthe
complexnumbersandtheirbasicproperties.
Wewillgeneralizetheexamplesofaplaneandofordinaryspaceto\mathbf{R}n and
\mathbf{C}n,whichwethenwillgeneralizetothenotionofavectorspace. Aswewillsee,
avectorspaceisasetwithoperationsofadditionandscalarmultiplicationthat
satisfynaturalalgebraicproperties.
Then our next topic will be subspaces, which play a role for vector spaces
analogoustotheroleplayedbysubsetsforsets. Finally, wewilllookatsums
of subspaces (analogous to unions of subsets) and direct sums of subspaces
$$(analogoustounionsofdisjointsets).$$
Pierre Louis Dumesnil,Nils Forsberg
RenéDescartesexplaininghisworkto Queen Christinaof Sweden.
Vectorspacesareageneralizationofthedescriptionofaplane
usingtwocoordinates,aspublishedby Descartesin1637.

2 Chapter 1 Vector Spaces
### 1A \mathbf{R}n and \mathbf{C}n
Youshouldalreadybefamiliarwithbasicpropertiesoftheset\mathbf{R} ofrealnumbers.
Complex numbers were invented so that we can take square roots of negative
numbers. Theideaistoassumewehaveasquarerootof-1,denotedbyi,that
obeystheusualrulesofarithmetic. Herearetheformaldefinitions.
**1.1 定义：** complexnumbers,\mathbf{C}
• Acomplexnumber isanorderedpair(a,b),wherea,b \in \mathbf{R},butwewill
writethisasa+bi.
• Thesetofallcomplexnumbersisdenotedby\mathbf{C}:
\mathbf{C} ={a+bi ∶a,b\in\mathbf{R}}.
• Additionandmultiplicationon\mathbf{C} aredefinedby
$$(a+bi)+(c+di)=(a+c)+(b+d)i,$$
$$(a+bi)(c+di)=(ac-bd)+(ad+bc)i;$$
herea,b,c,d \in\mathbf{R}.
Ifa\in\mathbf{R},weidentifya+0iwiththerealnumbera. Thuswethinkof\mathbf{R} asa
subsetof\mathbf{C}. Weusuallywrite0+biasjustbi,andweusuallywrite0+1iasjusti.
Tomotivatethedefinitionofcomplex
Thesymboliwasfirstusedtodenote
multiplicationgivenabove,pretendthat \sqrt-1by Leonhard Eulerin1777.
weknewthati2 = -1andthenusethe
usual rules of arithmetic to derive the formula above for the product of two
complexnumbers. Thenusethatformulatoverifythatweindeedhave
i2 =-1.
Donotmemorizetheformulafortheproductoftwocomplexnumbers—you
canalwaysrederiveitbyrecallingthati2 =-1andthenusingtheusualrulesof
arithmetic(asgivenby1.3). Thenextexampleillustratesthisprocedure.
**1.2 例：** complexarithmetic
Theproduct(2+3i)(4+5i)canbeevaluatedbyapplyingthedistributiveand
commutativepropertiesfrom1.3:
$$(2+3i)(4+5i)=2\cdot(4+5i)+(3i)(4+5i)$$
=2\cdot4+2\cdot5i+3i\cdot4+(3i)(5i)
=8+10i+12i-15
=-7+22i.

Section1A \mathbf{R}n and\mathbf{C}n 3
Ourfirstresultstatesthatcomplexadditionandcomplexmultiplicationhave
thefamiliarpropertiesthatweexpect.
1.3 propertiesofcomplexarithmetic
commutativity
\alpha+\beta=\beta+\alphaand\alpha\beta=\beta\alphaforall\alpha,\beta\in\mathbf{C}.
associativity
$$(\alpha+\beta)+ \lambda=\alpha+(\beta+ \lambda)and(\alpha\beta)\lambda=\alpha(\beta\lambda)forall\alpha,\beta,\lambda\in\mathbf{C}.$$
identities
\lambda+0= \lambdaand \lambda1= \lambdaforall \lambda\in\mathbf{C}.
additiveinverse
Forevery\alpha\in\mathbf{C},thereexistsaunique\beta\in\mathbf{C} suchthat\alpha+\beta=0.
multiplicativeinverse
Forevery\alpha\in\mathbf{C} with\alpha\neq0,thereexistsaunique\beta\in\mathbf{C} suchthat\alpha\beta=1.
distributiveproperty
\lambda(\alpha+\beta)= \lambda\alpha+ \lambda\betaforall \lambda,\alpha,\beta\in\mathbf{C}.
Thepropertiesaboveareprovedusingthefamiliarpropertiesofrealnumbers
andthedefinitionsofcomplexadditionandmultiplication. Thenextexample
shows how commutativity of complex multiplication is proved. Proofs of the
otherpropertiesaboveareleftasexercises.
**1.4 例：** commutativityofcomplexmultiplication
Toshowthat\alpha\beta=\beta\alphaforall\alpha,\beta\in\mathbf{C},suppose
\alpha=a+bi and \beta=c+di,
wherea,b,c,d \in \mathbf{R}. Thenthedefinitionofmultiplicationofcomplexnumbers
showsthat
\alpha\beta=(a+bi)(c+di)
=(ac-bd)+(ad+bc)i
and
\beta\alpha=(c+di)(a+bi)
=(ca-db)+(cb+da)i.
Theequationsaboveandthecommutativityofmultiplicationandadditionofreal
numbersshowthat\alpha\beta=\beta\alpha.

| -------- | ------------ | --- | --- |
Next,wedefinetheadditiveandmultiplicativeinversesofcomplexnumbers,
and then use those inverses to define subtraction and division operations with
complexnumbers.
-\alpha,subtraction,1/\alpha,division
**1.5 定义：** Suppose\alpha,\beta\in\mathbf{C}.
| • Let-\alphadenotetheadditiveinverseof\alpha. |     |     | Thus-\alphaistheuniquecomplex |
| ----------------------------------- | --- | --- | ------------------------ |
numbersuchthat
\alpha+(-\alpha)=0.
| • Subtractionon\mathbf{C} | isdefinedby |     |     |
| ---------------- | ----------- | --- | --- |
\beta-\alpha=\beta+(-\alpha).
• For\alpha\neq0,let1/\alphaand denotethemultiplicativeinverseof\alpha. Thus1/\alphais
\alpha
theuniquecomplexnumbersuchthat
\alpha(1/\alpha)=1.
• For\alpha\neq0,divisionby\alphaisdefinedby
\beta/\alpha=\beta(1/\alpha).
Sothatwecanconvenientlymakedefinitionsandprovetheoremsthatapply
tobothrealandcomplexnumbers,weadoptthefollowingnotation.
| 1.6 notation:        | \mathbf{F}   |                  |      |
| -------------------- | --- | ---------------- | ---- |
| Throughoutthisbook,\mathbf{F} |     | standsforeither\mathbf{R} | or\mathbf{C}. |
Thusifweproveatheoreminvolving
Theletter\mathbf{F}isusedbecause\mathbf{R}and\mathbf{C}
| \mathbf{F},wewillknowthatitholdswhen\mathbf{F} |     | is  |     |
| ---------------------------- | --- | --- | --- |
areexamplesofwhatarecalledfields.
| replacedwith\mathbf{R} | andwhen\mathbf{F} | isreplaced |     |
| ------------- | -------- | ---------- | --- |
with\mathbf{C}.
Elementsof\mathbf{F} arecalledscalars. Theword“scalar”(whichisjustafancy
wordfor“number”)isoftenusedwhenwewanttoemphasizethatanobjectisa
number,asopposedtoavector(vectorswillbedefinedsoon).
| For\alpha\in\mathbf{F} | andmapositiveinteger,wedefine\alpham |     | todenotetheproductof\alpha |
| ------ | ------------------------------- | --- | --------------------- |
withitselfmtimes:
|     |     | \alpham = \alpha⏟⋯\alpha. |     |
| --- | --- | ---------- | --- |
mtimes
Thisdefinitionimpliesthat
|     | (\alpham)n | =\alphamn | (\alpha\beta)m =\alpham\betam |
| --- | ----- | ---- | ----------- |
and
| forall\alpha,\beta\in\mathbf{F} | andallpositiveintegersm,n. |     |     |
| ----------- | -------------------------- | --- | --- |

Section1A \mathbf{R}n and\mathbf{C}n 5
Lists
Beforedefining\mathbf{R}n and\mathbf{C}n,welookattwoimportantexamples.
**1.7 例：** \mathbf{R}2 and \mathbf{R}3
• Theset\mathbf{R}2,whichyoucanthinkofasaplane,isthesetofallorderedpairsof
realnumbers:
\mathbf{R}2 ={(x,y)∶x,y \in\mathbf{R}}.
• Theset\mathbf{R}3,whichyoucanthinkofasordinaryspace,isthesetofallordered
triplesofrealnumbers:
\mathbf{R}3 ={(x,y,z)∶x,y,z\in\mathbf{R}}.
Togeneralize\mathbf{R}2 and\mathbf{R}3 tohigherdimensions,wefirstneedtodiscussthe
conceptoflists.
**1.8 定义：** list,length
• Supposenisanonnegativeinteger. Alist oflengthnisanorderedcollectionofnelements(whichmightbenumbers,otherlists,ormoreabstract
objects).
• Twolistsareequalifandonlyiftheyhavethesamelengthandthesame
elementsinthesameorder.
Lists are often written as elements
Many mathematicians call a list of
separatedbycommasandsurroundedby
lengthnann-tuple.
parentheses. Thusalistoflengthtwois
anorderedpairthatmightbewrittenas(a,b). Alistoflengththreeisanordered
triplethatmightbewrittenas(x,y,z). Alistoflengthnmightlooklikethis:
$$(z ,…,z ).$$
1 n
Sometimeswewillusethewordlistwithoutspecifyingitslength. Remember,
however,thatbydefinitioneachlisthasafinitelengththatisanonnegativeinteger.
Thusanobjectthatlookslike(x ,x ,…),whichmightbesaidtohaveinfinite
1 2
length,isnotalist.
Alistoflength0lookslikethis: (). Weconsidersuchanobjecttobealist
sothatsomeofourtheoremswillnothavetrivialexceptions.
Listsdifferfromfinitesetsintwoways: inlists,ordermattersandrepetitions
havemeaning;insets,orderandrepetitionsareirrelevant.
**1.9 例：** listsversussets
• Thelists(3,5)and(5,3)arenotequal,butthesets{3,5}and{5,3}areequal.
• Thelists(4,4)and(4,4,4)arenotequal(theydonothavethesamelength),
althoughthesets{4,4}and{4,4,4}bothequaltheset{4}.

| -------- | --- | ------------ | --- | --- | --- | --- |
\mathbf{F}n
Todefinethehigher-dimensionalanaloguesof\mathbf{R}2 and\mathbf{R}3,wewillsimplyreplace
\mathbf{R} with\mathbf{F} (whichequals\mathbf{R} or\mathbf{C})andreplacethe2or3withanarbitrarypositive
integer.
| 1.10 notation: | n   |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- |
Fixapositiveintegernfortherestofthischapter.
\mathbf{F}n,coordinate
**1.11 定义：** \mathbf{F}n isthesetofalllistsoflengthnofelementsof\mathbf{F}:
|     | \mathbf{F}n  | ={(x | ,…,x )∶x | \in\mathbf{F} fork | =1,…,n}. |     |
| --- | --- | ---- | -------- | ------- | -------- | --- |
|     |     |      | 1 n      | k       |          |     |
For(x ,…,x ) \in \mathbf{F}n andk \in {1,…,n},wesaythatx isthekth coordinate
| 1         | n   |     |     |     | k   |     |
| --------- | --- | --- | --- | --- | --- | --- |
| of(x ,…,x | ).  |     |     |     |     |     |
| 1         | n   |     |     |     |     |     |
If\mathbf{F} =\mathbf{R} andnequals2or3,thenthedefinitionaboveof\mathbf{F}n agreeswithour
| previousnotionsof\mathbf{R}2 |     | and\mathbf{R}3. |     |     |     |     |
| ------------------- | --- | ------ | --- | --- | --- | --- |
\mathbf{C}4
**1.12 例：** \mathbf{C}4 isthesetofalllistsoffourcomplexnumbers:
|     |                      | \mathbf{C}4   |          | )∶z           |            |     |
| --- | -------------------- | ---- | -------- | ------------- | ---------- | --- |
|     |                      | ={(z | ,z ,z ,z | ,z            | ,z ,z \in\mathbf{C}}. |     |
|     |                      |      | 1 2 3 4  | 1             | 2 3 4      |     |
| Ifn | 4, wecannotvisualize |      | \mathbf{R}n as    |               |            |     |
| \geq   |                      |      |          | Read Flatland: |            |     |
ARomanceof Many
| a physical | object. | Similarly, | \mathbf{C}1 can be |     |     |     |
| ---------- | ------- | ---------- | --------- | --- | --- | --- |
Dimensions,by Edwin A.Abbott,for
| thoughtofasaplane,butforn\geq2,the |     |     |     | anamusingaccountofhow\mathbf{R}3would |     |     |
| ------------------------------- | --- | --- | --- | ---------------------------- | --- | --- |
humanbraincannotprovideafullimage beperceivedbycreatureslivingin\mathbf{R}2.
\mathbf{C}n.
of However, even if n is large, we This novel, published in 1884, may
canperformalgebraicmanipulationsin helpyouimagineaphysicalspaceof
| \mathbf{F}n aseasilyasin\mathbf{R}2 |                                            | or\mathbf{R}3. |             |                       |         |       |
| ----------------- | ------------------------------------------ | ----- | ----------- | --------------------- | ------- | ----- |
|                   |                                            |       | Forexample, | fourormoredimensions. |         |       |
| additionin\mathbf{F}n      | isdefinedasfollows.                        |       |             |                       |         |       |
| 1.13 definition:  | additionin\mathbf{F}n                               |       |             |                       |         |       |
| Additionin\mathbf{F}n      | isdefinedbyaddingcorrespondingcoordinates: |       |             |                       |         |       |
|                   | (x ,…,x                                    | )+(y  | ,…,y        | )=(x                  | +y ,…,x | +y ). |
|                   | 1                                          | n     | 1 n         | 1                     | 1 n     | n     |
Oftenthemathematicsof\mathbf{F}nbecomescleanerifweuseasinglelettertodenote
alistofnnumbers,withoutexplicitlywritingthecoordinates. Forexample,the
nextresultisstatedwithxandyin\mathbf{F}n eventhoughtheproofrequiresthemore
|                        |     |     | ,…,x       | ,…,y |      |     |
| ---------------------- | --- | --- | ---------- | ---- | ---- | --- |
| cumbersomenotationof(x |     |     | 1 n )and(y | 1    | n ). |     |

| --- | --- | --- | --------- | -------- |
commutativityofadditionin\mathbf{F}n
1.14
| Ifx,y \in\mathbf{F}n,thenx+y |     | =y+x.     |           |                 |
| ----------------- | --- | --------- | --------- | --------------- |
| Proof Supposex    | =(x | ,…,x )\in\mathbf{F}n | andy =(y  | ,…,y )\in\mathbf{F}n. Then |
|                   | 1   | n         | 1         | n               |
|                   | x+y | =(x ,…,x  | )+(y ,…,y | )               |
|                   |     | 1         | n 1       | n               |
|                   |     | =(x +y    | ,…,x +y   | )               |
|                   |     | 1         | 1 n n     |                 |
|                   |     | +x        | ,…,y +x   |                 |
|                   |     | =(y       |           | )               |
|                   |     | 1         | 1 n n     |                 |
|                   |     | =(y ,…,y  | )+(x ,…,x | )               |
|                   |     | 1         | n 1       | n               |
=y+x,
wherethesecondandfourthequalitiesaboveholdbecauseofthedefinitionof
additionin\mathbf{F}n andthethirdequalityholdsbecauseoftheusualcommutativityof
additionin\mathbf{F}.
Ifasingleletterisusedtodenotean
|     |     |     | Thesymbol | means“endofproof”. |
| --- | --- | --- | --------- | ------------------ |
elementof\mathbf{F}n,thenthesameletterwith
appropriatesubscriptsisoftenusedwhen
coordinates must be displayed. For example, if x \in \mathbf{F}n, then letting x equal
$$(x ,…,x )isgoodnotation,asshownintheproofabove. Evenbetter,workwith$$
1 n
justxandavoidexplicitcoordinateswhenpossible.
| 1.15 notation: | 0   |     |     |     |
| -------------- | --- | --- | --- | --- |
Let0denotethelistoflengthnwhosecoordinatesareall0:
$$0=(0,…,0).$$
Hereweareusingthesymbol0intwodifferentways—ontheleftsideofthe
equationabove,thesymbol0denotesalistoflengthn,whichisanelementof\mathbf{F}n,
whereasontherightside,each0denotesanumber. Thispotentiallyconfusing
practiceactuallycausesnoproblemsbecausethecontextshouldalwaysmake
clearwhich0isintended.
| 1.16 example: | contextdetermineswhich0isintended |     |     |     |
| ------------- | --------------------------------- | --- | --- | --- |
Considerthestatementthat0isanadditiveidentityfor\mathbf{F}n:
\in\mathbf{F}n.
|     |     | x+0=x | forallx |     |
| --- | --- | ----- | ------- | --- |
Herethe0aboveisthelistdefinedin1.15,notthenumber0,becausewehave
| notdefinedthesumofanelementof\mathbf{F}n |     |     | (namely,x)andthenumber0. |     |
| ------------------------------- | --- | --- | ------------------------ | --- |

| -------- | --- | ------------ | --- | --- | --- | --- |
| Apicturecanaidourintuition. |     |     |     |     | Wewill |     |
| --------------------------- | --- | --- | --- | --- | ------ | --- |
drawpicturesin\mathbf{R}2becausewecansketch
| this space | on    | two-dimensional |     | surfaces |     |     |
| ---------- | ----- | --------------- | --- | -------- | --- | --- |
| such as    | paper | and computer    |     | screens. | A   |     |
typicalelementof\mathbf{R}2
isapointv=(a,b).
| Sometimes | we  | think | of v | not as | a point    |                  |
| --------- | --- | ----- | ---- | ------ | ---------- | ---------------- |
|           |     |       |      |        | Elementsof | \mathbf{R}2canbethoughtof |
butasanarrowstartingattheoriginand
| endingat(a,b),asshownhere. |     |     |              | Whenwe |     | aspointsorasvectors. |
| -------------------------- | --- | --- | ------------ | ------ | --- | -------------------- |
| thinkofanelementof\mathbf{R}2       |     |     | asanarrow,we |        |     |                      |
refertoitasavector.
Whenwethinkofvectorsin\mathbf{R}2asarrows,we
canmoveanarrowparalleltoitself(notchanging
itslengthordirection)andstillthinkofitasthe
| samevector. | Withthatviewpoint,youwilloften |     |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- | --- |
gainbetterunderstandingbydispensingwiththe
coordinateaxesandtheexplicitcoordinatesand Avector.
justthinkingofthevector,asshowninthefigurehere. Thetwoarrowsshown
herehavethesamelengthandsamedirection,sowethinkofthemasthesame
vector.
| Whenever |     | we use | pictures | in  | \mathbf{R}2 or |     |
| -------- | --- | ------ | -------- | --- | ----- | --- |
Mathematicalmodelsoftheeconomy
| use the | somewhat |     | vague | language | of  |     |
| ------- | -------- | --- | ----- | -------- | --- | --- |
canhavethousandsofvariables,say
pointsandvectors,rememberthatthese
|     |     |     |     |     | x ,…,x | ,whichmeansthatwemust |
| --- | --- | --- | --- | --- | ------ | --------------------- |
arejustaidstoourunderstanding,notsub- workin\mathbf{R}5000. Suchaspacecannotbe
| stitutes | for the | actual | mathematics |     | that |     |
| -------- | ------- | ------ | ----------- | --- | ---- | --- |
dealtwithgeometrically. However,the
we will develop. Although we cannot algebraicapproachworkswell. Thus
drawgoodpicturesinhigh-dimensional
oursubjectiscalledlinearalgebra.
spaces,theelementsofthesespacesare
asrigorouslydefinedaselementsof\mathbf{R}2.
For example, (2,-3,17,\pi,\sqrt2) is an element of \mathbf{R}5, and we may casually
refertoitasapointin\mathbf{R}5 oravectorin\mathbf{R}5 withoutworryingaboutwhetherthe
geometryof\mathbf{R}5
hasanyphysicalmeaning.
Recallthatwedefinedthesumoftwoelementsof\mathbf{F}n tobetheelementof\mathbf{F}n
obtainedbyadding corresponding coordinates; see 1.13. As wewill nowsee,
additionhasasimplegeometricinterpretationinthespecialcaseof\mathbf{R}2.
Supposewehavetwovectorsuandvin\mathbf{R}2
| thatwewanttoadd. |     |     | Movethevectorvparallel |     |     |     |
| ---------------- | --- | --- | ---------------------- | --- | --- | --- |
toitselfsothatitsinitialpointcoincideswiththe
| end point | of the | vector | u,  | as shown | here. The |     |
| --------- | ------ | ------ | --- | -------- | --------- | --- |
sumu+vthenequalsthevectorwhoseinitial
pointequalstheinitialpointofuandwhoseend
point equals the end point of the vector v, as Thesumoftwovectors.
shownhere.
Inthenextdefinition,the0ontherightsideofthedisplayedequationisthe
list0\in\mathbf{F}n.

Section1A \mathbf{R}n and\mathbf{C}n 9
**1.17 定义：** additiveinversein\mathbf{F}n,-x
Forx \in \mathbf{F}n,theadditiveinverseofx,denotedby-x,isthevector-x \in \mathbf{F}n
suchthat
x+(-x)=0.
Thusifx =(x ,…,x ),then-x =(-x ,…,-x ).
1 n 1 n
Theadditiveinverseofavectorin\mathbf{R}2 isthe
vectorwiththesamelengthbutpointinginthe
opposite direction. The figure here illustrates
thiswayofthinkingabouttheadditiveinverse
in\mathbf{R}2. Asyoucansee,thevectorlabeled-xhas
thesamelengthasthevectorlabeledxbutpoints Avectoranditsadditiveinverse.
intheoppositedirection.
Havingdealtwithadditionin\mathbf{F}n, wenowturntomultiplication. Wecould
defineamultiplicationin\mathbf{F}n inasimilarfashion,startingwithtwoelementsof
\mathbf{F}n andgettinganotherelementof\mathbf{F}n bymultiplyingcorrespondingcoordinates.
Experience shows that this definition is not useful for our purposes. Another
typeofmultiplication,calledscalarmultiplication,willbecentraltooursubject.
Specifically,weneedtodefinewhatitmeanstomultiplyanelementof\mathbf{F}n byan
elementof\mathbf{F}.
**1.18 定义：** scalarmultiplicationin\mathbf{F}n
Theproduct ofanumber \lambdaandavectorin\mathbf{F}n iscomputedbymultiplying
eachcoordinateofthevectorby \lambda:
\lambda(x ,…,x )=(\lambdax ,…,\lambdax );
1 n 1 n
here \lambda\in\mathbf{F} and(x ,…,x )\in\mathbf{F}n.
1 n
ScalarmultiplicationhasanicegeoScalarmultiplicationin\mathbf{F}nmultiplies
metricinterpretationin\mathbf{R}2. If \lambda>0and
togetherascalarandavector,getting
x \in\mathbf{R}2,then \lambdaxisthevectorthatpoints avector. Incontrast,thedotproductin
in the same direction as x and whose \mathbf{R}2or\mathbf{R}3multipliestogethertwoveclengthis \lambdatimesthelengthofx. Inother torsandgetsascalar. Generalizations
words,toget \lambdax,weshrinkorstretchx ofthedotproductwillbecomeimporbyafactorof \lambda,dependingonwhether tantin Chapter 6.
\lambda<1or \lambda>1.
If \lambda < 0 and x \in \mathbf{R}2, then \lambdax is the
vectorthatpointsinthedirectionopposite
tothatofxandwhoselengthis|\lambda|times
thelengthofx,asshownhere.
Scalarmultiplication.

| --------------------- | --- | --- |
| Digression on Fields |     |     |
| -------------------- | --- | --- |
Afield isasetcontainingatleasttwodistinctelementscalled0and1,alongwith
operationsofadditionandmultiplicationsatisfyingallpropertieslistedin1.3.
Thus\mathbf{R} and\mathbf{C} arefields,asisthesetofrationalnumbersalongwiththeusual
operationsofadditionandmultiplication. Anotherexampleofafieldistheset
{0,1}withtheusualoperationsofadditionandmultiplicationexceptthat1+1is
definedtoequal0.
Inthisbookwewillnotdealwithfieldsotherthan\mathbf{R} and\mathbf{C}. However,many
ofthedefinitions,theorems,andproofsinlinearalgebrathatworkforthefields
\mathbf{R} and \mathbf{C} also work without change for arbitrary fields. If you prefer to do so,
throughoutmuchofthisbook(exceptfor Chapters6and7,whichdealwithinner
product spaces) you can think of \mathbf{F} as denoting an arbitrary field instead of \mathbf{R}
or\mathbf{C}. Forresults(exceptintheinnerproductchapters)thathaveasahypothesis
that\mathbf{F} is\mathbf{C},youcanprobablyreplacethathypothesiswiththehypothesisthat\mathbf{F}
isanalgebraicallyclosedfield,whichmeansthateverynonconstantpolynomial
withcoefficientsin\mathbf{F} hasazero. Afewresults,suchas Exercise13in Section
| 1C,requirethehypothesison\mathbf{F} | that1+1\neq0. |     |
| -------------------------- | ---------- | --- |
Exercises 1A
1 Showthat\alpha+\beta=\beta+\alphaforall\alpha,\beta\in\mathbf{C}.
| 2 Showthat(\alpha+\beta)+ | \lambda=\alpha+(\beta+ | \lambda)forall\alpha,\beta,\lambda\in\mathbf{C}. |
| ---------------- | ------- | ---------------- |
3 Showthat(\alpha\beta)\lambda=\alpha(\beta\lambda)forall\alpha,\beta,\lambda\in\mathbf{C}.
| Showthat \lambda(\alpha+\beta)= | \lambda\alpha+ \lambda\betaforall | \lambda,\alpha,\beta\in\mathbf{C}. |
| ---------------- | ------------ | -------- |
suchthat\alpha+\beta=0.
5 Showthatforevery\alpha\in\mathbf{C},thereexistsaunique\beta\in\mathbf{C}
6 Showthatforevery\alpha \in \mathbf{C} with\alpha \neq 0,thereexistsaunique\beta \in \mathbf{C} such
that\alpha\beta=1.
Showthat
-1+\sqrt3i
isacuberootof1(meaningthatitscubeequals1).
8 Findtwodistinctsquarerootsofi.
| 9 Findx \in\mathbf{R}4 suchthat           |               |              |
| ------------------------------ | ------------- | ------------ |
|                                | (4,-3,1,7)+2x | =(5,9,-6,8). |
| 10 Explainwhytheredoesnotexist |               | \lambda\in\mathbf{C} suchthat |
\lambda(2-3i,5+4i,-6+7i)=(12-5i,7+22i,-32-9i).

| --- | --- | --- | --- | --- | --------- | -------- |
Showthat(x+y)+z=x+(y+z)forallx,y,z\in\mathbf{F}n.
| 12 Showthat(ab)x |           | =a(bx)forallx     |              | \in\mathbf{F}n andalla,b\in\mathbf{F}. |           |      |
| ---------------- | --------- | ----------------- | ------------ | ---------------- | --------- | ---- |
| 13 Showthat1x    | =xforallx |                   | \in\mathbf{F}n.         |                  |           |      |
| 14 Showthat      | \lambda(x+y)=   |                   | \lambdax+ \lambdayforall | \lambda\in\mathbf{F}              | andallx,y | \in\mathbf{F}n. |
| Showthat(a+b)x   |           | =ax+bxforalla,b\in\mathbf{F} |              |                  | andallx   | \in\mathbf{F}n. |
“Canyoudoaddition?” the White Queenasked. “What’soneandoneandone
andoneandoneandoneandoneandoneandoneandone?”
| “Idon’tknow,”said Alice. |     |     | “Ilostcount.” |     |     |     |
| ----------------------- | --- | --- | ------------- | --- | --- | --- |
—Throughthe Looking Glass,Lewis Carroll

| -------- | ------------ | --- | --- |
| 1B Definition | of Vector | Space |     |
| ------------- | --------- | ----- | --- |
The motivation for the definition of a vector space comes from properties of
additionandscalarmultiplicationin\mathbf{F}n: Additioniscommutative,associative,
andhasanidentity. Everyelementhasanadditiveinverse. Scalarmultiplication
isassociative. Scalarmultiplicationby1actsasexpected. Additionandscalar
multiplicationareconnectedbydistributiveproperties.
We will define a vector space to be a set \mathcal{V} with an addition and a scalar
multiplicationon\mathcal{V} thatsatisfythepropertiesintheparagraphabove.
| 1.19 definition: | addition,scalarmultiplication |     |     |
| ---------------- | ----------------------------- | --- | --- |
isafunctionthatassignsanelementu+v\in\mathcal{V}
• Anadditiononaset\mathcal{V}
toeachpairofelementsu,v\in\mathcal{V}.
• A scalar multiplication on a set \mathcal{V} is a function that assigns an element
| \lambdav\in\mathcal{V} | toeach \lambda\in\mathbf{F} andeachv\in\mathcal{V}. |     |     |
| ---- | ---------------------- | --- | --- |
Nowwearereadytogivetheformaldefinitionofavectorspace.
| 1.20 definition: | vectorspace |     |     |
| ---------------- | ----------- | --- | --- |
Avectorspaceisaset\mathcal{V}alongwithanadditionon\mathcal{V}andascalarmultiplication
on\mathcal{V} suchthatthefollowingpropertieshold.
commutativity
u+v=v+uforallu,v\in\mathcal{V}.
associativity
| (u+v)+w | = u+(v+w)and(ab)v | = a(bv)forallu,v,w | \in \mathcal{V} andfor |
| ------- | ----------------- | ------------------ | ---------- |
alla,b\in\mathbf{F}.
additiveidentity
| Thereexistsanelement0\in\mathcal{V} |     | suchthatv+0=vforallv\in\mathcal{V}. |     |
| ----------------------- | --- | ----------------------- | --- |
additiveinverse
| Foreveryv\in\mathcal{V},thereexistsw\in\mathcal{V} |     | suchthatv+w=0. |     |
| -------------------------- | --- | -------------- | --- |
multiplicativeidentity
1v=vforallv\in\mathcal{V}.
distributiveproperties
| a(u+v)=au+avand(a+b)v=av+bvforalla,b\in\mathbf{F} |     |     | andallu,v\in\mathcal{V}. |
| -------------------------------------- | --- | --- | ------------ |
Thefollowinggeometriclanguagesometimesaidsourintuition.
| 1.21 definition: | vector,point |     |     |
| ---------------- | ------------ | --- | --- |
Elementsofavectorspacearecalledvectorsorpoints.

| --- | --- | --------- | ----------------------- | --- |
Thescalarmultiplicationinavectorspacedependson\mathbf{F}. Thuswhenweneed
tobeprecise,wewillsaythat\mathcal{V} isavectorspaceover \mathbf{F} insteadofsayingsimply
|     | Forexample,\mathbf{R}n |     | isavectorspaceover\mathbf{R},and\mathbf{C}n |     |
| --- | ------------- | --- | ------------------------- | --- |
that\mathcal{V} isavectorspace. isa
vectorspaceover\mathbf{C}.
| 1.22 definition:    | realvectorspace,complexvectorspace |                              |     |     |
| ------------------- | ---------------------------------- | ---------------------------- | --- | --- |
| • Avectorspaceover\mathbf{R} |                                    | iscalledarealvectorspace.    |     |     |
| • Avectorspaceover\mathbf{C} |                                    | iscalledacomplexvectorspace. |     |     |
Usuallythechoiceof\mathbf{F} iseitherclearfromthecontextorirrelevant. Thuswe
oftenassumethat\mathbf{F}islurkinginthebackgroundwithoutspecificallymentioningit.
Withtheusualoperationsofaddition
Thesimplestvectorspaceis{0},which
| andscalarmultiplication,\mathbf{F}n |     | isavector |     |     |
| -------------------------- | --- | --------- | --- | --- |
containsonlyonepoint.
| spaceover\mathbf{F},asyoushouldverify. |                                      | The |     |     |
| ----------------------------- | ------------------------------------ | --- | --- | --- |
| exampleof\mathbf{F}n                   | motivatedourdefinitionofvectorspace. |     |     |     |
\mathbf{F}\infty
**1.23 例：** \mathbf{F}\infty isdefinedtobethesetofallsequencesofelementsof\mathbf{F}:
|     | \mathbf{F}\infty ={(x | ,x ,…)∶x | \in\mathbf{F} fork =1,2,…}. |     |
| --- | ------- | -------- | ---------------- | --- |
1 2 k
Additionandscalarmultiplicationon\mathbf{F}\infty
aredefinedasexpected:
|     | (x ,x ,…)+(y | ,y ,…)=(x  | +y ,x    | +y ,…), |
| --- | ------------ | ---------- | -------- | ------- |
|     | 1 2          | 1 2        | 1 1 2    | 2       |
|     | \lambda(x          | ,x ,…)=(\lambdax | ,\lambdax ,…). |         |
|     |              | 1 2        | 1 2      |         |
Withthesedefinitions,\mathbf{F}\infty becomesavectorspaceover\mathbf{F},asyoushouldverify.
Theadditiveidentityinthisvectorspaceisthesequenceofall0’s.
Ournextexampleofavectorspaceinvolvesasetoffunctions.
| 1.24 notation:   | \mathbf{F}\mathcal{S}                                |     |     |     |
| ---------------- | --------------------------------- | --- | --- | --- |
| If\mathcal{S}isaset,then\mathbf{F}\mathcal{S} | denotesthesetoffunctionsfrom\mathcal{S}to\mathbf{F}. |     |     |     |
•
| • For f,g | \in\mathbf{F}\mathcal{S},thesum           | f +g \in\mathbf{F}\mathcal{S} isthefunctiondefinedby |                            |     |
| --------- | -------------------- | ------------------------------- | -------------------------- | --- |
|           |                      | (f +g)(x)=                      | f(x)+g(x)                  |     |
| forallx   | \in\mathcal{S}.                  |                                 |                            |     |
| • For \lambda\in\mathbf{F} | and f \in\mathbf{F}\mathcal{S},theproduct | \lambdaf                              | \in\mathbf{F}\mathcal{S} isthefunctiondefinedby |     |
|           |                      | (\lambdaf)(x)=                        | \lambdaf(x)                      |     |
| forallx   | \in\mathcal{S}.                  |                                 |                            |     |

| -------- | ------------ | --- | --- | --- |
Asanexampleofthenotationabove,if\mathcal{S}istheinterval[0,1]and\mathbf{F} =\mathbf{R},then
\mathbf{R}[0,1] isthesetofreal-valuedfunctionsontheinterval[0,1].
Youshouldverifyallthreebulletpointsinthenextexample.
| 1.25 example: | \mathbf{F}\mathcal{S} isavectorspace |     |     |     |
| ------------- | ----------------- | --- | --- | --- |
• If \mathcal{S} is a nonempty set, then \mathbf{F}\mathcal{S} (with the operations of addition and scalar
multiplicationasdefinedabove)isavectorspaceover\mathbf{F}.
isthefunction0∶\mathcal{S}\rightarrow\mathbf{F}
• Theadditiveidentityof\mathbf{F}\mathcal{S} definedby
0(x)=0
| forallx | \in\mathcal{S}. |     |     |     |
| ------- | --- | --- | --- | --- |
∶\mathcal{S}\rightarrow\mathbf{F}
| • For f | \in\mathbf{F}\mathcal{S},theadditiveinverseof |     | f isthefunction-f | definedby |
| ------- | ------------------------ | --- | ----------------- | --------- |
$$(-f)(x)=-f(x)$$
| forallx          | \in\mathcal{S}. |                |     |     |
| ---------------- | --- | -------------- | --- | --- |
| Thevectorspace\mathbf{F}n |     | isaspecialcase |     |     |
Theelementsofthevectorspace\mathbf{R}[0,1]
| of the | vector space | \mathbf{F}\mathcal{S} because | each |     |
| ------ | ------------ | ---------- | ---- | --- |
arereal-valuedfunctionson[0,1],not
| (x ,…,x    | ) \in \mathbf{F}n can            | be thought | of as                             |     |
| ---------- | --------------------- | ---------- | --------------------------------- | --- |
| 1          | n                     |            | lists. Ingeneral,avectorspaceisan |     |
| afunctionx | fromtheset{1,2,…,n}to |            |                                   |     |
abstractentitywhoseelementsmight
\mathbf{F}bywritingx(k)insteadofx forthekth belists,functions,orweirdobjects.
k
| coordinateof(x | ,…,x | ). Inotherwords, |     |     |
| -------------- | ---- | ---------------- | --- | --- |
|                | 1    | n                |     |     |
wecanthinkof\mathbf{F}n as\mathbf{F}{1,2,…,n}. Similarly,wecanthinkof\mathbf{F}\infty as\mathbf{F}{1,2,…}.
Soonwewillseefurtherexamplesofvectorspaces,butfirstweneedtodevelop
someoftheelementarypropertiesofvectorspaces.
Thedefinitionofavectorspacerequiresittohaveanadditiveidentity. The
nextresultstatesthatthisidentityisunique.
1.26 uniqueadditiveidentity
Avectorspacehasauniqueadditiveidentity.
Proof Suppose 0 and 0′ are both additive identities for some vector space \mathcal{V}.
Then
0′ =0′+0=0+0′ =0,
wherethefirstequalityholdsbecause0isanadditiveidentity,thesecondequality
comesfromcommutativity,andthethirdequalityholdsbecause0′ isanadditive
| identity. | Thus0′ =0,provingthat\mathcal{V} |     | hasonlyoneadditiveidentity. |     |
| --------- | ---------------------- | --- | --------------------------- | --- |
Eachelementvinavectorspacehasanadditiveinverse,anelementwinthe
vectorspacesuchthatv+w = 0. Thenextresultshowsthateachelementina
vectorspacehasonlyoneadditiveinverse.

Section1B Definitionof Vector Space
uniqueadditiveinverse
1.27
Everyelementinavectorspacehasauniqueadditiveinverse.
Supposewandw′
| Proof Suppose\mathcal{V}          | isavectorspace. | Letv\in\mathcal{V}. | areadditive |
| ----------------------- | --------------- | ------- | ----------- |
| inversesofv. Then       |                 |         |             |
| w=w+0=w+(v+w′)=(w+v)+w′ |                 | =0+w′   | =w′.        |
Thusw=w′,asdesired.
Becauseadditiveinversesareunique,thefollowingnotationnowmakessense.
| 1.28 notation: | -v,w-v |     |     |
| -------------- | ------ | --- | --- |
| Letv,w\in\mathcal{V}.      | Then   |     |     |
-vdenotestheadditiveinverseofv;
•
• w-visdefinedtobew+(-v).
Almostallresultsinthisbookinvolvesomevectorspace. Toavoidhavingto
restatefrequentlythat\mathcal{V}isavectorspace,wenowmakethenecessarydeclaration
onceandforall.
| 1.29 notation:         | \mathcal{V}                         |     |     |
| ---------------------- | ------------------------- | --- | --- |
| Fortherestofthisbook,\mathcal{V} | denotesavectorspaceover\mathbf{F}. |     |     |
Inthenextresult,0denotesascalar(thenumber0\in\mathbf{F})ontheleftsideofthe
equationandavector(theadditiveidentityof\mathcal{V})ontherightsideoftheequation.
1.30 thenumber0timesavector
0v=0foreveryv\in\mathcal{V}.
Forv\in\mathcal{V},wehave
| Proof            |     | Theresultin1.30involvestheadditive  |     |
| ---------------- | --- | ----------------------------------- | --- |
| 0v=(0+0)v=0v+0v. |     | identityof\mathcal{V}andscalarmultiplication. |     |
Theonlypartofthedefinitionofavectorspacethatconnectsvectoraddition
Addingtheadditiveinverseof0vtoboth
sidesoftheequationabovegives0=0v, and scalar multiplication is the dis-
|     |     | tributiveproperty. Thusthedistribu- |     |
| --- | --- | ----------------------------------- | --- |
asdesired.
tivepropertymustbeusedintheproof
of1.30.
Inthenextresult,0denotestheaddi-
| tiveidentityof\mathcal{V}. | Althoughtheirproofs |     |     |
| ---------------- | ------------------- | --- | --- |
aresimilar,1.30and1.31arenotidentical. Moreprecisely,1.30statesthatthe
productofthescalar0andanyvectorequalsthevector0,whereas1.31statesthat
theproductofanyscalarandthevector0equalsthevector0.

16 Chapter 1 Vector Spaces
1.31 anumbertimesthevector 0
a0=0foreverya\in\mathbf{F}.
Proof Fora\in\mathbf{F},wehave
a0=a(0+0)=a0+a0.
Addingtheadditiveinverseofa0tobothsidesoftheequationabovegives0=a0,
asdesired.
Nowweshowthatifanelementof\mathcal{V} ismultipliedbythescalar-1,thenthe
resultistheadditiveinverseoftheelementof\mathcal{V}.
1.32 thenumber -1timesavector
$$(-1)v=-vforeveryv\in\mathcal{V}.$$
Proof Forv\in\mathcal{V},wehave
v+(-1)v=1v+(-1)v=(1+(-1))v=0v=0.
This equation says that (-1)v, when added to v, gives 0. Thus (-1)v is the
additiveinverseofv,asdesired.
Exercises 1B
1 Provethat-(-v)=vforeveryv\in\mathcal{V}.
2 Supposea\in\mathbf{F},v\in\mathcal{V},andav=0. Provethata=0orv=0.
3 Suppose v,w \in \mathcal{V}. Explain why there exists a unique x \in \mathcal{V} such that
v+3x =w.
4 Theemptysetisnotavectorspace. Theemptysetfailstosatisfyonlyone
oftherequirementslistedinthedefinitionofavectorspace(1.20). Which
one?
5 Show that in the definition of a vector space (1.20), the additive inverse
conditioncanbereplacedwiththeconditionthat
0v=0forallv\in\mathcal{V}.
Herethe0ontheleftsideisthenumber0,andthe0ontherightsideisthe
additiveidentityof\mathcal{V}.
Thephrasea“conditioncanbereplaced”inadefinitionmeansthatthe
collectionofobjectssatisfyingthedefinitionisunchangediftheoriginal
conditionisreplacedwiththenewcondition.

| --- | --- | --- | --------- | ----------------------- | --- | --- | --- |
6 Let\inftyand-\inftydenotetwodistinctobjects,neitherofwhichisin\mathbf{R}. Define
anadditionandscalarmultiplicationon\mathbf{R}\cup{\infty,-\infty}asyoucouldguess
fromthenotation. Specifically,thesumandproductoftworealnumbersis
| asusual,andfort\in\mathbf{R} |     | define       |     |        |       |        |     |
| ----------------- | --- | ------------ | --- | ------ | ----- | ------ | --- |
|                   |     | ⎧ {-\infty ift<0, |     |        | ⎧ {\infty  | ift<0, |     |
|                   |     | {            |     |        | {     |        |     |
|                   | t\infty= | ⎨0 ift=0,    |     | t(-\infty)= | ⎨0    | ift=0, |     |
|                   |     | {            |     |        | {     |        |     |
|                   |     | { ⎩\infty ift>0,  |     |        | { ⎩-\infty | ift>0, |     |
and
t+\infty=\infty+t=\infty+\infty=\infty,
t+(-\infty)=(-\infty)+t=(-\infty)+(-\infty)=-\infty,
\infty+(-\infty)=(-\infty)+\infty=0.
Withtheseoperationsofadditionandscalarmultiplication,is\mathbf{R}\cup{\infty,-\infty}
| avectorspaceover\mathbf{R}? |     | Explain. |     |     |     |     |     |
| ------------------ | --- | -------- | --- | --- | --- | --- | --- |
Let\mathcal{V}\mathcal{S}denotethesetoffunctionsfrom\mathcal{S}to\mathcal{V}.
7 Suppose\mathcal{S}isanonemptyset.
Defineanaturaladditionandscalarmultiplicationon\mathcal{V}\mathcal{S},andshowthat\mathcal{V}\mathcal{S}
isavectorspacewiththesedefinitions.
| 8 Suppose\mathcal{V}                          | isarealvectorspace. |     |     |     |             |     |           |
| ----------------------------------- | ------------------- | --- | --- | --- | ----------- | --- | --------- |
| • Thecomplexificationof\mathcal{V},denotedby\mathcal{V} |                     |     |     |     | ,equals\mathcal{V}\times\mathcal{V}. |     | Anelement |
\mathbf{C}
| of\mathcal{V} | isanorderedpair(u,v),whereu,v |     |     |     | \in   | \mathcal{V},butwewritethisas |     |
| --- | ----------------------------- | --- | --- | --- | --- | ------------------ | --- |
\mathbf{C}
u+iv.
| • Additionon\mathcal{V} |     | isdefinedby |     |     |     |     |     |
| ------------- | --- | ----------- | --- | --- | --- | --- | --- |
\mathbf{C}
|                                  |     | (u +iv )+(u  | +iv | )=(u | +u )+i(v    |     | +v ) |
| -------------------------------- | --- | ------------ | --- | ---- | ----------- | --- | ---- |
|                                  |     | 1 1          | 2   | 2    | 1 2         | 1   | 2    |
| forallu                          |     | ,v ,u ,v \in\mathcal{V}. |     |      |             |     |      |
|                                  | 1   | 1 2 2        |     |      |             |     |      |
| • Complexscalarmultiplicationon\mathcal{V} |     |              |     |      | isdefinedby |     |      |
\mathbf{C}
$$(a+bi)(u+iv)=(au-bv)+i(av+bu)$$
| foralla,b\in\mathbf{R} |     | andallu,v\in\mathcal{V}. |     |     |     |     |     |
| ----------- | --- | ------------ | --- | --- | --- | --- | --- |
Provethatwiththedefinitionsofadditionandscalarmultiplicationasabove,
\mathcal{V} isacomplexvectorspace.
\mathbf{C}
Think of \mathcal{V} as a subset of \mathcal{V} by identifying u \in \mathcal{V} with u + i0. The
\mathbf{C}
construction of \mathcal{V} from \mathcal{V} can then be thought of as generalizing the
\mathbf{C}
\mathbf{C}nfrom\mathbf{R}n.
constructionof

| -------- | ------------ | --- | --- | --- |
### 1C Subspaces
Byconsideringsubspaces,wecangreatlyexpandourexamplesofvectorspaces.
| 1.33 definition: | subspace |     |     |     |
| ---------------- | -------- | --- | --- | --- |
Asubset\mathcal{U} of\mathcal{V} iscalledasubspaceof\mathcal{V} if\mathcal{U} isalsoavectorspacewiththe
sameadditiveidentity,addition,andscalarmultiplicationason\mathcal{V}.
Thenextresultgivestheeasiestway
|                  |          | Some people     | use the terminology |           |
| ---------------- | -------- | --------------- | ------------------- | --------- |
| to check whether | a subset | of a vector     |                     |           |
|                  |          | linearsubspace, | which               | means the |
spaceisasubspace.
sameassubspace.
1.34 conditionsforasubspace
Asubset\mathcal{U} of\mathcal{V} isasubspaceof\mathcal{V} ifandonlyif\mathcal{U} satisfiesthefollowing
threeconditions.
additiveidentity
0\in\mathcal{U}.
closedunderaddition
| u,w\in\mathcal{U} | impliesu+w\in\mathcal{U}. |     |     |     |
| ----- | ------------- | --- | --- | --- |
closedunderscalarmultiplication
| a\in\mathbf{F} andu\in\mathcal{U} | impliesau\in\mathcal{U}.         |     |     |     |
| ---------- | -------------------- | --- | --- | --- |
| Proof If\mathcal{U}  | isasubspaceof\mathcal{V},then\mathcal{U} |     |     |     |
Theadditiveidentityconditionabove
satisfiesthethreeconditionsabovebythe
couldbereplacedwiththecondition
definitionofvectorspace. that\mathcal{U}isnonempty(becausethentak-
| Conversely, | suppose \mathcal{U} | satisfies the |                   |         |
| ----------- | --------- | ------------- | ----------------- | ------- |
|             |           | ing u \in       | \mathcal{U} and multiplying | it by 0 |
threeconditionsabove. Thefirstcondi- would imply that 0 \in \mathcal{U}). However,
tionensuresthattheadditiveidentityof if a subset of is indeed a sub\mathcal{U} \mathcal{V}
\mathcal{V} isin\mathcal{U}. Thesecondconditionensures space, then usually the quickest way
thatadditionmakessenseon\mathcal{U}. Thethird toshowthat\mathcal{U}isnonemptyistoshow
conditionensuresthatscalarmultiplica- that0\in\mathcal{U}.
tionmakessenseon\mathcal{U}.
If u \in \mathcal{U}, then -u [which equals (-1)u by 1.32] is also in \mathcal{U} by the third
conditionabove. Henceeveryelementof\mathcal{U} hasanadditiveinversein\mathcal{U}.
Theotherpartsofthedefinitionofavectorspace,suchasassociativityand
commutativity,areautomaticallysatisfiedfor\mathcal{U} becausetheyholdonthelarger
| space\mathcal{V}. Thus\mathcal{U} | isavectorspaceandhenceisasubspaceof\mathcal{V}. |     |     |     |
| ------------- | ------------------------------------- | --- | --- | --- |
Thethreeconditionsintheresultaboveusuallyenableustodeterminequickly
whetheragivensubsetof\mathcal{V} isasubspaceof\mathcal{V}. Youshouldverifyallassertions
inthenextexample.

| --- | --- | --- | --- | --- | --------- | --- | --------- |
subspaces
**1.35 例：** (a) Ifb\in\mathbf{F},then
|                 |     | {(x             | ,x ,x | ,x )\in\mathbf{F}4 | ∶x =5x | +b} |     |
| --------------- | --- | --------------- | ----- | ------- | ------ | --- | --- |
|                 |     |                 | 1 2   | 3 4     | 3      | 4   |     |
| isasubspaceof\mathbf{F}4 |     | ifandonlyifb=0. |       |         |        |     |     |
Thesetofcontinuousreal-valuedfunctionsontheinterval[0,1]isasubspace
$$(b)$$
of\mathbf{R}[0,1].
isasubspaceof\mathbf{R}\mathbf{R}.
$$(c) Thesetofdifferentiablereal-valuedfunctionson\mathbf{R}$$
$$(d) Thesetofdifferentiablereal-valuedfunctions f ontheinterval(0,3)such$$
f′(2)=bisasubspaceof\mathbf{R}(0,3)
| that |     |     |     |     | ifandonlyifb=0. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
$$(e) Thesetofallsequencesofcomplexnumberswithlimit0isasubspaceof\mathbf{C}\infty.$$
| Verifying | some | of the | items | above |     |     |     |
| --------- | ---- | ------ | ----- | ----- | --- | --- | --- |
Theset{0}isthesmallestsubspaceof
shows the linear structure underlying \mathcal{V},and\mathcal{V}itselfisthelargestsubspace
| ---------------- | --- | ------------------- | --- | --- | ------------------------------- | --- | --- |
|                  |     |                     |     |     | of \mathcal{V}. Theemptysetisnotasubspace |     |     |
requires the result that the sum of two of \mathcal{V} because a subspace must be a
continuousfunctionsiscontinuous. As vectorspaceandhencemustcontainat
anotherexample,(d)aboverequiresthe leastoneelement,namely,anadditive
| resultthatforaconstantc,thederivative |     |     |     |     | identity. |     |     |
| ------------------------------------- | --- | --- | --- | --- | --------- | --- | --- |
| ofcf equalsctimesthederivativeof      |     |     |     | f.  |           |     |     |
Thesubspacesof\mathbf{R}2 areprecisely{0},alllinesin\mathbf{R}2 containingtheorigin,
and\mathbf{R}2. Thesubspacesof\mathbf{R}3areprecisely{0},alllinesin\mathbf{R}3containingtheorigin,
allplanesin\mathbf{R}3 containingtheorigin,and\mathbf{R}3. Toprovethatalltheseobjectsare
indeedsubspacesisstraightforward—thehardpartistoshowthattheyarethe
onlysubspacesof\mathbf{R}2 and\mathbf{R}3. Thattaskwillbeeasierafterweintroducesome
additionaltoolsinthenextchapter.
Sums of Subspaces
Whendealingwithvectorspaces,weare
Theunionofsubspacesisrarelyasub-
| usuallyinterestedonlyinsubspaces, |     |     |     | as  |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
space(see Exercise12),whichiswhy
opposedtoarbitrarysubsets. Thenotion weusuallyworkwithsumsratherthan
ofthesumofsubspaceswillbeuseful.
unions.
| 1.36     | definition:                               | sumofsubspaces   |     |     |           |     |                 |
| -------- | ----------------------------------------- | ---------------- | --- | --- | --------- | --- | --------------- |
| Suppose\mathcal{V} | ,…,\mathcal{V}                                      | aresubspacesof\mathcal{V}. |     |     | Thesumof\mathcal{V} |     | ,…,\mathcal{V} ,denotedby |
|          | 1                                         | m                |     |     |           | 1   | m               |
| +⋯+\mathcal{V}     |                                           |                  |     |     |           |     | ,…,\mathcal{V}            |
| \mathcal{V} 1      | m ,isthesetofallpossiblesumsofelementsof\mathcal{V} |                  |     |     |           |     | 1 m . More      |
precisely,
|     | \mathcal{V} +⋯+\mathcal{V} |     | ={v +⋯+v |     | ∶v \in\mathcal{V} | ,…,v | \in\mathcal{V} }. |
| --- | ------ | --- | -------- | --- | ----- | ---- | ----- |
|     | 1      | m   | 1        | m   | 1 1   |      | m m   |

| -------- | ------------ | --- | --- | --- |
Let’slookatsomeexamplesofsumsofsubspaces.
| 1.37 example: | asumofsubspacesof |     | \mathbf{F}3  |     |
| ------------- | ----------------- | --- | --- | --- |
Suppose\mathcal{U}isthesetofallelementsof\mathbf{F}3whosesecondandthirdcoordinates
equal0,and\mathcal{W} isthesetofallelementsof\mathbf{F}3 whosefirstandthirdcoordinates
equal0:
|                |     | ∶x  |                    | ∶y   |
| -------------- | --- | --- | ------------------ | ---- |
| \mathcal{U} ={(x,0,0)\in\mathbf{F}3 |     | \in\mathbf{F}} | and \mathcal{W} ={(0,y,0)\in\mathbf{F}3 | \in\mathbf{F}}. |
Then
|     | \mathcal{U}+\mathcal{W} | ={(x,y,0)\in\mathbf{F}3 | ∶x,y \in\mathbf{F}}, |     |
| --- | --- | ------------ | --------- | --- |
asyoushouldverify.
| 1.38 example: | asumofsubspacesof |     | \mathbf{F}4  |     |
| ------------- | ----------------- | --- | --- | --- |
Suppose
| ={(x,x,y,y)\in\mathbf{F}4 | ∶x,y |     | ={(x,x,x,y)\in\mathbf{F}4 | ∶x,y |
| -------------- | ---- | --- | -------------- | ---- |
| \mathcal{U}              |      | \in\mathbf{F}} | and \mathcal{W}          | \in\mathbf{F}}. |
Using words rather than symbols, we could say that \mathcal{U} is the set of elements
of\mathbf{F}4 whosefirsttwocoordinatesequaleachotherandwhosethirdandfourth
isthesetofelementsof\mathbf{F}4whosefirst
| coordinatesequaleachother. |     | Similarly,\mathcal{W} |     |     |
| -------------------------- | --- | ----------- | --- | --- |
threecoordinatesequaleachother.
Tofindadescriptionof\mathcal{U}+\mathcal{W},consideratypicalelement(a,a,b,b)of\mathcal{U}and
| atypicalelement(c,c,c,d)of\mathcal{W},wherea,b,c,d |     |     | \in\mathbf{F}. Wehave |     |
| ---------------------------------------- | --- | --- | ---------- | --- |
$$(a,a,b,b)+(c,c,c,d)=(a+c,a+c,b+c,b+d),$$
whichshowsthateveryelementof\mathcal{U}+\mathcal{W} hasitsfirsttwocoordinatesequalto
| eachother. Thus |     |                |            |     |
| --------------- | --- | -------------- | ---------- | --- |
|                 | \mathcal{U}+\mathcal{W} | \subseteq{(x,x,y,z)\in\mathbf{F}4 | ∶x,y,z\in\mathbf{F}}. |     |
1.39
| Toprovetheinclusionintheotherdirection,supposex,y,z\in\mathbf{F}. |     |     |     | Then |
| ------------------------------------------------------ | --- | --- | --- | ---- |
$$(x,x,y,z)=(x,x,y,y)+(0,0,0,z-y),$$
wherethefirstvectorontherightisin\mathcal{U} andthesecondvectorontherightis
in\mathcal{W}. Thus(x,x,y,z) \mathcal{U}+\mathcal{W},showingthattheinclusion1.39alsoholdsin
\in
| theoppositedirection. | Hence |     |     |     |
| --------------------- | ----- | --- | --- | --- |
∶x,y,z\in\mathbf{F}},
|     | \mathcal{U}+\mathcal{W} | ={(x,x,y,z)\in\mathbf{F}4 |     |     |
| --- | --- | -------------- | --- | --- |
isthesetofelementsof\mathbf{F}4
whichshowsthat\mathcal{U}+\mathcal{W} whosefirsttwocoordinates
equaleachother.
Thenextresultstatesthatthesumofsubspacesisasubspace,andisinfactthe
smallestsubspacecontainingallthesummands(whichmeansthateverysubspace
containingallthesummandsalsocontainsthesum).

| --- | --- | --- | --- | --- | --------- | --------- | --- |
sumofsubspacesisthesmallestcontainingsubspace
1.40
| Suppose\mathcal{V}    |     | ,…,\mathcal{V}        | aresubspacesof\mathcal{V}. |     | Then\mathcal{V} +⋯+\mathcal{V} | isthesmallest |     |
| ----------- | --- | ----------- | ---------------- | --- | ---------- | ------------- | --- |
|             |     | 1 m         |                  |     | 1          | m             |     |
| subspaceof\mathcal{V} |     | containing\mathcal{V} | ,…,\mathcal{V}             | .   |            |               |     |
|             |     |             | 1                | m   |            |               |     |
Proof Thereadercanverifythat\mathcal{V} +⋯+\mathcal{V} containstheadditiveidentity0
1 m
andisclosedunderadditionandscalarmultiplication. Thus1.34impliesthat
| \mathcal{V} +⋯+\mathcal{V}    |               | isasubspaceof\mathcal{V}. |                 |     |                                  |     |     |
| --------- | ------------- | --------------- | --------------- | --- | -------------------------------- | --- | --- |
| 1         |               | m               |                 |     |                                  |     |     |
|           | Thesubspaces\mathcal{V} |                 | ,…,\mathcal{V} areallcon- |     |                                  |     |     |
|           |               | 1               | m               |     | Sumsofsubspacesinthetheoryofvec- |     |     |
| tainedin\mathcal{V} |               | +⋯+\mathcal{V}            | (toseethis,con- |     |                                  |     |     |
|           |               | 1               | m               |     | torspacesareanalogoustounionsof  |     |     |
sidersumsv +⋯+v whereallexcept subsetsinsettheory. Giventwosub-
|           |     | 1        | m                |     |                                  |     |     |
| --------- | --- | -------- | ---------------- | --- | -------------------------------- | --- | --- |
| oneofthev |     | ’sare0). | Conversely,every |     |                                  |     |     |
|           |     | k        |                  |     | spacesofavectorspace,thesmallest |     |     |
subspaceof\mathcal{V}containing\mathcal{V} ,…,\mathcal{V} con- subspacecontainingthemistheirsum.
1 m
| tains | \mathcal{V} +⋯+\mathcal{V} | (because | subspaces |     |                                    |     |     |
| ----- | ------ | -------- | --------- | --- | ---------------------------------- | --- | --- |
|       | 1      | m        |           |     | Analogously,giventwosubsetsofaset, |     |     |
mustcontainallfinitesumsoftheirele- thesmallestsubsetcontainingthemis
| ments).     | Thus\mathcal{V} | +⋯+\mathcal{V}        | isthesmallest |     | theirunion. |     |     |
| ----------- | ----- | ----------- | ------------- | --- | ----------- | --- | --- |
|             |       | 1           | m             |     |             |     |     |
| subspaceof\mathcal{V} |       | containing\mathcal{V} | ,…,\mathcal{V}          | .   |             |     |     |
1 m
| Suppose\mathcal{V} |     | ,…,\mathcal{V} aresubspacesof\mathcal{V}. |     | Everyelementof\mathcal{V} |     | +⋯+\mathcal{V} | canbe |
| -------- | --- | --------------------- | --- | --------------- | --- | ---- | ----- |
|          |     | 1 m                   |     |                 |     | 1    | m     |
writtenintheform
|     |     |     | v   | +⋯+v | ,   |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     | 1    | m   |     |     |
where each v \in \mathcal{V} . Of special interest are cases in which each vector in
|     |     | k   | k   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
+⋯+\mathcal{V} canberepresentedintheformaboveinonlyoneway. Thissituation
| \mathcal{V} 1 |     | m   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
issoimportantthatitgetsaspecialname(directsum)andaspecialsymbol(\oplus).
| 1.41     | definition:                     | directsum,\oplus        |                                    |     |                  |      |      |
| -------- | ------------------------------- | ------------------ | ---------------------------------- | --- | ---------------- | ---- | ---- |
| Suppose\mathcal{V} |                                 | ,…,\mathcal{V}               | aresubspacesof\mathcal{V}.                   |     |                  |      |      |
|          |                                 | 1 m                |                                    |     |                  |      |      |
| •        | Thesum\mathcal{V}                         | +⋯+\mathcal{V}               | iscalledadirectsumifeachelementof\mathcal{V} |     |                  |      | +⋯+\mathcal{V} |
|          |                                 | 1                  | m                                  |     |                  | 1    | m    |
|          | canbewritteninonlyonewayasasumv |                    |                                    |     | +⋯+v ,whereeachv |      | \in\mathcal{V} . |
|          |                                 |                    |                                    |     | 1 m              |      | k k  |
| •        | If\mathcal{V} +⋯+\mathcal{V}                        | isadirectsum,then\mathcal{V} |                                    |     | \oplus⋯\oplus\mathcal{V} denotes\mathcal{V}    | +⋯+\mathcal{V} | ,    |
|          | 1                               | m                  |                                    |     | 1 m              | 1    | m    |
withthe\oplusnotationservingasanindicationthatthisisadirectsum.
adirectsumoftwosubspaces
**1.42 例：** Suppose\mathcal{U}isthesubspaceof\mathbf{F}3ofthosevectorswhoselastcoordinateequals0,
isthesubspaceof\mathbf{F}3
| and\mathcal{W} |                |     | ofthosevectorswhosefirsttwocoordinatesequal0: |     |                |        |     |
| ---- | -------------- | --- | --------------------------------------------- | --- | -------------- | ------ | --- |
|      | \mathcal{U} ={(x,y,0)\in\mathbf{F}3 |     | ∶x,y \in\mathbf{F}}                                      | and | \mathcal{W} ={(0,0,z)\in\mathbf{F}3 | ∶z\in\mathbf{F}}. |     |
Then\mathbf{F}3 =\mathcal{U}\oplus\mathcal{W},asyoushouldverify.

| --- | --------------------- | --- | --- | --- | --- |
\approx7\pi
adirectsumofmultiplesubspaces
**1.43 例：** | Suppose\mathcal{V} | isthesubspaceof\mathbf{F}n |     | of                          |     |     |
| -------- | ----------------- | --- | --------------------------- | --- | --- |
|          | k                 |     | Toproduce\oplusin TEX,type\oplus. |     |     |
thosevectorswhosecoordinatesareall0,
exceptpossiblyinthekth slot;forexample,\mathcal{V} ={(0,x,0,…,0)\in\mathbf{F}n ∶x \in\mathbf{F}}.
Then
|     |     | \mathbf{F}n =\mathcal{V} | \oplus⋯\oplus\mathcal{V} , |     |     |
| --- | --- | ----- | ------ | --- | --- |
|     |     |       | 1 n    |     |     |
asyoushouldverify.
Sometimesnonexamplesaddtoourunderstandingasmuchasexamples.
asumthatisnotadirectsum
**1.44 例：** Suppose
|     | \mathcal{V}   | ={(x,y,0)\in\mathbf{F}3 | ∶x,y \in\mathbf{F}}, |     |     |
| --- | --- | ------------ | --------- | --- | --- |
|     |     | ={(0,0,z)\in\mathbf{F}3 | ∶z\in\mathbf{F}}, |     |     |
| --- | --- | ------------ | ------ | --- | --- |
\mathcal{V}
∶y
|     | \mathcal{V}   | ={(0,y,y)\in\mathbf{F}3 | \in\mathbf{F}}. |     |     |
| --- | --- | ------------ | ---- | --- | --- |
| Then\mathbf{F}3 | =\mathcal{V} +\mathcal{V} +\mathcal{V} | becauseeveryvector(x,y,z)\in\mathbf{F}3 |     | canbewrittenas |     |
| ------ | -------- | ---------------------------- | --- | -------------- | --- |
|        | 1 2 3    |                              |     |                |     |
$$(x,y,z)=(x,y,0)+(0,0,z)+(0,0,0),$$
wherethefirstvectorontherightsideisin\mathcal{V} ,thesecondvectorisin\mathcal{V} ,andthe
| ---------------- | --- | --- | --- | --- | --- |
| thirdvectorisin\mathcal{V} | .   |     |     |     |     |
However,\mathbf{F}3 doesnotequalthedirectsumof\mathcal{V} ,\mathcal{V} ,\mathcal{V} ,becausethevector
|                                            |     |     | 1   | 2 3             |     |
| ------------------------------------------ | --- | --- | --- | --------------- | --- |
| (0,0,0)canbewritteninmorethanonewayasasumv |     |     |     | +v +v ,witheach |     |
1 2 3
v \in\mathcal{V} . Specifically,wehave
k k
$$(0,0,0)=(0,1,0)+(0,0,1)+(0,-1,-1)$$
and,ofcourse,
$$(0,0,0)=(0,0,0)+(0,0,0)+(0,0,0),$$
wherethefirstvectorontherightsideofeachequationaboveisin\mathcal{V} ,thesecond
vectorisin\mathcal{V} ,andthethirdvectorisin\mathcal{V} . Thusthesum\mathcal{V} +\mathcal{V} +\mathcal{V} isnota
|     | 2   |     | 3   | 1 2 | 3   |
| --- | --- | --- | --- | --- | --- |
directsum.
Thedefinitionofdirectsumrequires
|     |     |     | The symbol | \oplus, which is a | plus sign |
| --- | --- | --- | ---------- | ------------- | --------- |
everyvectorinthesumtohaveaunique insideacircle,remindsusthatweare
| representation | as an appropriate | sum. |     |     |     |
| -------------- | ----------------- | ---- | --- | --- | --- |
dealingwithaspecialtypeofsumof
Thenextresultshowsthatwhendeciding subspaces—eachelementinthedirect
| whether | a sum of subspaces | is a direct |     |     |     |
| ------- | ------------------ | ----------- | --- | --- | --- |
sumcanberepresentedinonlyoneway
sum,weonlyneedtoconsiderwhether0 asasumofelementsfromthespecified
| canbeuniquelywrittenasanappropriate |     |     | subspaces. |     |     |
| ----------------------------------- | --- | --- | ---------- | --- | --- |
sum.

| --- | --- | --- | --- | --- | --- | --------- | --------- | --- |
conditionforadirectsum
1.45
| Suppose\mathcal{V}                           |     | ,…,\mathcal{V} | aresubspacesof\mathcal{V}. |     |     | Then\mathcal{V} +⋯+\mathcal{V} | isadirectsumif |      |
| ---------------------------------- | --- | ---- | ---------------- | --- | --- | ---------- | -------------- | ---- |
|                                    | 1   |      | m                |     |     | 1          | m              |      |
| andonlyiftheonlywaytowrite0asasumv |     |      |                  |     |     | +⋯+v       | ,whereeachv    | \in\mathcal{V} , |
|                                    |     |      |                  |     |     | 1          | m              | k k  |
| isbytakingeachv                    |     |      | equalto0.        |     |     |            |                |      |
k
Proof Firstsuppose\mathcal{V} +⋯+\mathcal{V} isadirectsum. Thenthedefinitionofdirect
|     |     |     | 1   |     | m   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
sumimpliesthattheonlywaytowrite0asasumv +⋯+v ,whereeachv \in\mathcal{V} ,
|                 |     |     |           |     |     | 1   | m   | k k |
| --------------- | --- | --- | --------- | --- | --- | --- | --- | --- |
| isbytakingeachv |     |     | equalto0. |     |     |     |     |     |
k
| Nowsupposethattheonlywaytowrite0asasumv |     |     |     |     |     |     | +⋯+v ,whereeach |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- |
1 m
| v \in        | \mathcal{V} ,isbytakingeachv |      |     | equalto0.    |      | Toshowthat\mathcal{V} | +⋯+\mathcal{V} | isadirect |
| ---------- | ------------------ | ---- | --- | ------------ | ---- | ----------- | ---- | --------- |
| k          | k                  |      |     | k            |      |             | 1 m  |           |
| sum,letv\in\mathcal{V} |                    | +⋯+\mathcal{V} |     | . Wecanwrite |      |             |      |           |
|            |                    | 1    | m   |              |      |             |      |           |
|            |                    |      |     | v=v          | +⋯+v |             |      |           |
|            |                    |      |     |              | 1    | m           |      |           |
for some v \in \mathcal{V} ,…,v \in \mathcal{V} . To show that this representation is unique,
|     | 1   | 1   | m   |     | m   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
supposewealsohave
|        |     |      |      | v=u                                   | +⋯+u      | ,   |     |     |
| ------ | --- | ---- | ---- | ------------------------------------- | --------- | --- | --- | --- |
|        |     |      |      |                                       | 1         | m   |     |     |
| whereu | \in\mathcal{V}  | ,…,u | \in\mathcal{V}   | . Subtractingthesetwoequations,wehave |           |     |     |     |
|        | 1   | 1    | m    | m                                     |           |     |     |     |
|        |     |      | 0=(v |                                       | -u )+⋯+(v | -u  | ).  |     |
|        |     |      |      | 1                                     | 1         | m   | m   |     |
,…,v
| Becausev | -u       | \in\mathcal{V}     |       | -u       | \in\mathcal{V}   | ,theequationaboveimpliesthateach |                  |     |
| -------- | -------- | ------ | ----- | -------- | ---- | -------------------------------- | ---------------- | --- |
|          | 1        | 1      | 1     | m        | m    | m                                |                  |     |
| v -u     | equals0. | Thusv  |       | =u ,…,v  | =u   | ,asdesired.                      |                  |     |
| k        | k        |        | 1     | 1        | m    | m                                |                  |     |
| The      | next     | result | gives | a simple | con- |                                  |                  |     |
|          |          |        |       |          |      | Thesymbol                        | ⟺ usedbelowmeans |     |
ditionfortestingwhetherasumoftwo
“ifandonlyif”;thissymbolcouldalso
| subspacesisadirectsum. |     |     |     |     |     | bereadtomean“isequivalentto”. |     |     |
| ---------------------- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- |
1.46 directsumoftwosubspaces
| Suppose\mathcal{U} |                                  | and\mathcal{W} | aresubspacesof\mathcal{V}. |              |     | Then                  |       |     |
| -------- | -------------------------------- | ---- | ---------------- | ------------ | --- | --------------------- | ----- | --- |
|          |                                  | \mathcal{U}+\mathcal{W}  |                  | isadirectsum |     |                       |       |     |
|          |                                  |      |                  |              |     | ⟺ \mathcal{U}\cap\mathcal{W}                 | ={0}. |     |
| Proof    | Firstsupposethat\mathcal{U}+\mathcal{W}isadirectsum. |      |                  |              |     | Ifv\in\mathcal{U}\cap\mathcal{W},then0=v+(-v), |       |     |
wherev \in \mathcal{U} and-v \in \mathcal{W}. Bytheuniquerepresentationof0asthesumofa
vectorin\mathcal{U} andavectorin\mathcal{W},wehavev = 0. Thus\mathcal{U}\cap\mathcal{W} = {0},completing
theproofinonedirection.
| Toprovetheotherdirection,nowsuppose\mathcal{U}\cap\mathcal{W} |     |     |     |     |     |     | ={0}. Toprovethat\mathcal{U}+\mathcal{W} |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- |
isadirectsum,supposeu\in\mathcal{U},w\in\mathcal{W},and
$$0=u+w.$$
To complete the proof, we only need to show that u = w = 0 (by 1.45). The
equation above implies that u = -w \in \mathcal{W}. Thus u \in \mathcal{U} \cap\mathcal{W}. Hence u = 0,
whichbytheequationaboveimpliesthatw=0,completingtheproof.

| --- | -------- | ------------ | --- | --- | --- | --- | --- |
| The      | result | above deals    | only | with |                    |               |        |
| -------- | ------ | -------------- | ---- | ---- | ------------------ | ------------- | ------ |
|          |        |                |      |      | Sums of subspaces  | are analogous | to     |
| the case | of     | two subspaces. | When | ask- |                    |               |        |
|          |        |                |      |      | unions of subsets. | Similarly,    | direct |
ing about a possible direct sum with sums of subspaces are analogous to
| more | than | two subspaces, | it  | is not |                          |     |           |
| ---- | ---- | -------------- | --- | ------ | ------------------------ | --- | --------- |
|      |      |                |     |        | disjointunionsofsubsets. |     | Notwosub- |
enough to test that each pair of the spacesofavectorspacecanbedisjoint,
subspaces intersect only at 0. To see because both contain 0. So disjointthis, consider Example 1.44. In that ness is replaced, at least in the case
nonexample of a direct sum, we have oftwosubspaces,withtherequirement
| \mathcal{V} \cap\mathcal{V}      | =\mathcal{V}  | \cap\mathcal{V} =\mathcal{V} | \cap\mathcal{V} ={0}. |     | thattheintersectionequal{0}. |     |     |
| --------- | --- | ----- | -------- | --- | ---------------------------- | --- | --- |
| 1         | 2   | 1 3 2 | 3        |     |                              |     |     |
| Exercises |     | 1C    |          |     |                              |     |     |
1 Foreachofthefollowingsubsetsof\mathbf{F}3,determinewhetheritisasubspace
of\mathbf{F}3.
|     | (a)     | ,x ,x )\in\mathbf{F}3 | ∶x  | +2x | +3x     |     |     |
| --- | ------- | ---------- | --- | --- | ------- | --- | --- |
|     | {(x     | 1 2 3      | 1   | 2   | 3 =0}   |     |     |
|     | (b) {(x | ,x ,x )\in\mathbf{F}3 | ∶x  | +2x | +3x =4} |     |     |
|     |         | 1 2 3      | 1   | 2   | 3       |     |     |
∶x
|     | (c) {(x | ,x ,x )\in\mathbf{F}3 | x   | x =0} |     |     |     |
| --- | ------- | ---------- | --- | ----- | --- | --- | --- |
|     |         | 1 2 3      | 1   | 2 3   |     |     |     |
|     |         | )\in\mathbf{F}3       | ∶x  |       |     |     |     |
|     | (d) {(x | ,x ,x      |     | =5x   | }   |     |     |
|     |         | 1 2 3      | 1   | 3     |     |     |     |
2 Verifyallassertionsaboutsubspacesin Example1.35.
3 Showthatthesetofdifferentiablereal-valuedfunctions f ontheinterval
f′(-1)=3f(2)isasubspaceof\mathbf{R}(-4,4).
$$(-4,4)suchthat$$
4 Supposeb\in\mathbf{R}. Showthatthesetofcontinuousreal-valuedfunctions f on
|     |                           |     |     | 1   | bisasubspaceof\mathbf{R}[0,1] |     |             |
| --- | ------------------------- | --- | --- | --- | -------------------- | --- | ----------- |
|     | theinterval[0,1]suchthat\int |     |     | f   | =                    |     | ifandonlyif |
$$b=0.$$
|     | Is\mathbf{R}2 | asubspaceofthecomplexvectorspace\mathbf{C}2? |     |     |     |     |     |
| --- | ---- | ----------------------------------- | --- | --- | --- | --- | --- |
|     | Is{(a,b,c)\in\mathbf{R}3 |     | ∶a3 =b3}asubspaceof\mathbf{R}3? |     |     |     |     |
| --- | ------------- | --- | ---------------------- | --- | --- | --- | --- |
6 (a)
|     | (b) Is{(a,b,c)\in\mathbf{C}3 |     | ∶a3 =b3}asubspaceof\mathbf{C}3? |     |     |     |     |
| --- | ----------------- | --- | ---------------------- | --- | --- | --- | --- |
isanonemptysubsetof\mathbf{R}2
| 7   | Proveorgiveacounterexample: |     |     |     | If\mathcal{U} |     | suchthat |
| --- | --------------------------- | --- | --- | --- | --- | --- | -------- |
\mathcal{U} is closed under addition and under taking additive inverses (meaning
isasubspaceof\mathbf{R}2.
|     | -u\in\mathcal{U} | wheneveru\in\mathcal{U}),then\mathcal{U} |     |     |     |     |     |
| --- | ---- | ------------------ | --- | --- | --- | --- | --- |
8 Giveanexampleofanonemptysubset\mathcal{U} of\mathbf{R}2 suchthat\mathcal{U} isclosedunder
|     | scalarmultiplication,but\mathcal{U} |     |                                              | isnotasubspaceof\mathbf{R}2. |     |     |     |
| --- | ------------------------- | --- | -------------------------------------------- | ------------------- | --- | --- | --- |
|     | Afunction                 | f∶  | iscalledperiodicifthereexistsapositivenumber |                     |     |     |     |
| 9   |                           | \mathbf{R} \rightarrow | \mathbf{R}                                            |                     |     |     |     |
psuchthat f(x) = f(x+p)forallx \in \mathbf{R}. Isthesetofperiodicfunctions
|     | from\mathbf{R} | to\mathbf{R} asubspaceof\mathbf{R}\mathbf{R}? |     | Explain. |     |     |     |
| --- | ----- | ------------------ | --- | -------- | --- | --- | --- |
10 Suppose\mathcal{V} and\mathcal{V} aresubspacesof\mathcal{V}. Provethattheintersection\mathcal{V} \cap\mathcal{V}
|     |     | 1 2 |     |     |     |     | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
isasubspaceof\mathcal{V}.

| --- | --- | --- | --- | --- | --- | --------- | --------- | --- |
11 Provethattheintersectionofeverycollectionofsubspacesof\mathcal{V}isasubspace
of\mathcal{V}.
12 Provethattheunionoftwosubspacesof\mathcal{V} isasubspaceof\mathcal{V} ifandonlyif
oneofthesubspacesiscontainedintheother.
13 Provethattheunionofthreesubspacesof\mathcal{V} isasubspaceof\mathcal{V} ifandonly
ifoneofthesubspacescontainstheothertwo.
Thisexerciseissurprisinglyharderthan Exercise12,possiblybecausethis
exerciseisnottrueifwereplace\mathbf{F}withafieldcontainingonlytwoelements.
14 Suppose
|     |                  |     |                                           | ∶x  |     |     |               | ∶x   |
| --- | ---------------- | --- | ----------------------------------------- | --- | --- | --- | ------------- | ---- |
|     | \mathcal{U} ={(x,-x,2x)\in\mathbf{F}3 |     |                                           | \in\mathbf{F}} | and | \mathcal{W}   | ={(x,x,2x)\in\mathbf{F}3 | \in\mathbf{F}}. |
|     | Describe\mathcal{U}+\mathcal{W}      |     | usingsymbols,andalsogiveadescriptionof\mathcal{U}+\mathcal{W} |     |     |     |               | that |
usesnosymbols.
| 15  | Suppose\mathcal{U} | isasubspaceof\mathcal{V}. |     |     | Whatis\mathcal{U}+\mathcal{U}? |     |     |     |
| --- | -------- | --------------- | --- | --- | ---------- | --- | --- | --- |
16 Istheoperationofadditiononthesubspacesof\mathcal{V} commutative? Inother
|     | words,if\mathcal{U} | and\mathcal{W} | aresubspacesof\mathcal{V},is\mathcal{U}+\mathcal{W} |     |     |     | =\mathcal{W}+\mathcal{U}? |     |
| --- | --------- | ---- | --------------------- | --- | --- | --- | ----- | --- |
17 Is the operation of addition on the subspaces of \mathcal{V} associative? In other
|     | words,if\mathcal{V} | ,\mathcal{V}  | ,\mathcal{V} aresubspacesof\mathcal{V},is |        |     |     |       |     |
| --- | --------- | --- | --------------------- | ------ | --- | --- | ----- | --- |
|     |           | 1 2 | 3                     |        |     |     |       |     |
|     |           |     | (\mathcal{V}                    | +\mathcal{V} )+\mathcal{V} | =\mathcal{V}  | +(\mathcal{V} | +\mathcal{V} )? |     |
|     |           |     | 1                     | 2      | 3   | 1   | 2 3   |     |
18 Does the operation of addition on the subspaces of \mathcal{V} have an additive
|     | identity? | Whichsubspaceshaveadditiveinverses? |     |     |     |     |     |     |
| --- | --------- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
19 Proveorgiveacounterexample: If\mathcal{V} ,\mathcal{V} ,\mathcal{U} aresubspacesof\mathcal{V} suchthat
| --- | ----- | ---- | --- | --- | ----- | --- | --- | --- |
|     |       |      |     | \mathcal{V}   | +\mathcal{U} =\mathcal{V} | +\mathcal{U}, |     |     |
|     | then\mathcal{V} | =\mathcal{V} . |     |     |       |     |     |     |
20 Suppose
∶x,y
|     |                |     | \mathcal{U} ={(x,x,y,y)\in\mathbf{F}4 |            |     |       | \in\mathbf{F}}. |     |
| --- | -------------- | --- | ---------------- | ---------- | --- | ----- | ---- | --- |
|     |                |     | of\mathbf{F}4             | suchthat\mathbf{F}4 |     |       |      |     |
|     | Findasubspace\mathcal{W} |     |                  |            |     | =\mathcal{U}\oplus\mathcal{W}. |      |     |
21 Suppose
|     |                | \mathcal{U}   | ={(x,y,x+y,x-y,2x)\in\mathbf{F}5 |            |     |       | ∶x,y \in\mathbf{F}}. |     |
| --- | -------------- | --- | --------------------- | ---------- | --- | ----- | --------- | --- |
|     | Findasubspace\mathcal{W} |     | of\mathbf{F}5                  | suchthat\mathbf{F}5 |     | =\mathcal{U}\oplus\mathcal{W}. |           |     |
22 Suppose
|     |                     |     | ={(x,y,x+y,x-y,2x)\in\mathbf{F}5 |       |                                    |     | ∶x,y |     |
| --- | ------------------- | --- | --------------------- | ----- | ---------------------------------- | --- | ---- | --- |
|     |                     | \mathcal{U}   |                       |       |                                    |     | \in\mathbf{F}}. |     |
|     | Findthreesubspaces\mathcal{W} |     |                       | ,\mathcal{W} ,\mathcal{W} | of\mathbf{F}5,noneofwhichequals{0},suchthat |     |      |     |
\mathbf{F}5
|     | =\mathcal{U}\oplus\mathcal{W} | \oplus\mathcal{W}  | \oplus\mathcal{W}  | .   |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- |

| -------- | ------------ | --- | --- |
23 Proveorgiveacounterexample: If\mathcal{V} ,\mathcal{V} ,\mathcal{U} aresubspacesof\mathcal{V} suchthat
|          |      | 1 2         |     |
| -------- | ---- | ----------- | --- |
|          | \mathcal{V} =\mathcal{V} | \oplus\mathcal{U} and \mathcal{V} =\mathcal{V} | \oplus\mathcal{U}, |
| then\mathcal{V} =\mathcal{V} | .    |             |     |
Hint:Whentryingtodiscoverwhetheraconjectureinlinearalgebraistrue
orfalse,itisoftenusefultostartbyexperimentingin\mathbf{F}2.
f∶
| 24 Afunction | \mathbf{R} \rightarrow\mathbf{R} iscalledevenif |             |     |
| ------------ | ------------------- | ----------- | --- |
|              |                     | f(-x)= f(x) |     |
f∶
| forallx \in\mathbf{R}. | Afunction | \mathbf{R} \rightarrow\mathbf{R} iscalledodd | if  |
| ----------- | --------- | ---------------- | --- |
f(-x)=-f(x)
for all x \in \mathbf{R}. Let \mathcal{V} denote the set of real-valued even functions on \mathbf{R}
e
and let \mathcal{V} denote the set of real-valued odd functions on \mathbf{R}. Show that
o
| \mathbf{R}\mathbf{R}      | .   |     |     |
| ------- | --- | --- | --- |
| =\mathcal{V} e \oplus\mathcal{V} | o   |     |     |
