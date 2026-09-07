# Lagrange, Mécanique analytique, Part II, Section III: general properties of motion, including least action

> Source: [Wikisource](https://fr.wikisource.org/wiki/M%C3%A9canique_analytique/Partie_2/Section_3); local HTML rendering `Lagrange_MecaniqueAnalytique_P2S3_Oeuvres_wikisource.html`, retrieved 2026-09-08 with `action=render`.
> Metadata: Joseph-Louis Lagrange, *Mécanique analytique*, Seconde Partie, Section III, Œuvres tome XI, pp. 273–324 (Paris: Gauthier-Villars; date as for Section I).
> Extraction: `pandoc -f html -t gfm-raw_html` on the rendered page; the Wikisource header and page links are kept in the transcription.
> Rights: public-domain original text; the Wikisource transcription is CC BY-SA, with contributors credited through the source page history.

## Source digest

The text supplies the derivation of the conservation laws and of the least-action property from the general formula of dynamics; §VI, ‘Propriétés relatives à la moindre action’, from paragraph 39, states the principle as the stationarity of the sum of m·u·ds under conservation of vis viva. Reading level: `passage` for the anchor below and `full-read` of the transcription for structure.

## Passage anchor

Section §VI, paragraph 39: “Nous allons maintenant considérer le quatrième principe, celui de la moindre action”; displayed formulae are carried as LaTeX in the transcription.

## Transcription (Wikisource rendering)

[Joseph-Louis Lagrange](//fr.wikisource.org/wiki/Auteur:Joseph-Louis_Lagrange "Auteur:Joseph-Louis Lagrange")

[Mécanique analytique](//fr.wikisource.org/wiki/M%C3%A9canique_analytique "Mécanique analytique")

[Gauthier-Villars](//fr.wikisource.org/wiki/Cat%C3%A9gorie:%C3%89diteur_-_Gauthier-Villars "Catégorie:Éditeur - Gauthier-Villars"), 1868 ([Œuvres de Lagrange](//fr.wikisource.org/wiki/%C5%92uvres_de_Lagrange "Œuvres de Lagrange"). Tome XI, p. 273-324).

◄  [SECT. II](//fr.wikisource.org/wiki/M%C3%A9canique_analytique/Partie_2/Section_2 "Mécanique analytique/Partie 2/Section 2")

[SECT. IV](//fr.wikisource.org/wiki/M%C3%A9canique_analytique/Partie_2/Section_4 "Mécanique analytique/Partie 2/Section 4")  ►

Deuxième partie

book[Mécanique analytique](//fr.wikisource.org/wiki/M%C3%A9canique_analytique "Mécanique analytique")[Joseph-Louis Lagrange](//fr.wikisource.org/wiki/Auteur:Joseph-Louis_Lagrange "Auteur:Joseph-Louis Lagrange")[Gauthier-Villars](//fr.wikisource.org/wiki/Cat%C3%A9gorie:%C3%89diteur_-_Gauthier-Villars "Catégorie:Éditeur - Gauthier-Villars")1868ParisT[Œuvres de Lagrange](//fr.wikisource.org/wiki/%C5%92uvres_de_Lagrange "Œuvres de Lagrange"). Tome XIDeuxième partieJoseph Louis de Lagrange - Œuvres, Tome 11.djvuJoseph Louis de Lagrange - Œuvres, Tome 11.djvu/3273-324 

###  SECTION TROISIÈME.

PROPRIÉTÉS GÉNÉRALES DU MOUVEMENT DÉDUITES DE LA FORMULE PRÉCÉDENTE.

------------------------------------------------------------------------

1\. Considérons un système de corps disposés les uns par rapport aux autres et liés ensemble comme l’on voudra, mais sans qu’il y ait aucun point ou obstacle fixe qui gêne leur mouvement ; il est évident que, dans ce cas, les conditions du système ne peuvent dépendre que de la position respective des corps entre eux ; par conséquent, les équations de condition ne pourront contenir d’autres fonctions des coordonnées que les expressions des distances mutuelles des corps. Cette considération fournit, pour le mouvement d’un système, des équations générales indépendantes de la nature du système et analogues à celles que nous avons trouvées pour l’équilibre dans la première Partie (Sect. III, § I).

§ I. *Propriétés relatives au centre de gravité*.

2\. Soient $x^{\prime},\, y^{\prime},\ z^{\prime}$ les coordonnées d’un corps quelconque déterminé du système, tandis que $x,\ y,\ z$ représentent, en générale, les coordonnées d’un autre corps quelconque. Faisons, ce qui est toujours permis,

$x = x^{\prime} + \xi,\qquad y = y^{\prime} + \eta,\qquad z = z^{\prime} + \zeta\,;$

il est visible que les quantités $x^{\prime},\ y^{\prime},\ z^{\prime}$ n’entreront point dans les expressions des distances mutuelles des corps, mais que ces distances ne dépendront que des différentes quantités $\xi,\,\eta,\ \zeta$ qui expriment proprement les coordonnées des différents corps, rapportés à celui qui répond à $x^{\prime},\, y^{\prime},\, z^{\prime}\,;$ par conséquent, les équations de condition du système seront entre les seules variables $\xi,\,\eta,\,\zeta$ et ne renfermeront point $x^{\prime},\, y^{\prime},\, z^{\prime}.$

Donc, si dans la formule générale de la Dynamique (sect. II, art. 5) on réduit toutes les variations à $\delta x,\,\delta y,\,\delta z$ et qu’on substitue, pour $\delta x,\,\delta y,\,\delta z$ leurs valeurs $\delta x^{\prime} + \delta\xi,\ \delta y^{\prime} + \delta\eta,\ \delta z^{\prime} + \delta\zeta,$ les variations $\delta x^{\prime},\,\delta y^{\prime},\,\delta z^{\prime}$ seront indépendantes de toutes les autres et arbitraires en elles-mêmes ; ainsi, il faudra égaler séparément à zéro la totalité des termes affectés de chacune de ces variations, ce qui donnera trois équations générales et indépendantes de la constitution particulière du système.

Les forces intérieures par lesquelles les corps pourraient agir les uns sur les autres, et que nous dénotons par ${\bar{P},\,\bar{Q}},\ldots,$ comme dans la première Partie (sect. II, art. 2), n’entreront point dans ces équations, parce que, les distances mutuelles $\overline{p},\overline{q},\ldots$ étant indépendantes de $x^{\prime},y^{\prime},z^{\prime},$ les variations $\delta\overline{p},\delta\overline{q},\ldots,$ relatives à ces variables, seront nulles.

À l’égard des forces extérieures ${P,\, Q,\, R},\ldots,$ si on les réduit aux trois forces $X,\, Y,\, Z$ dirigées suivant les coordonnées $x,\, y,\, z$ et tendantes à les diminuer, d’après les formules données dans la première Partie (sect. V, Chap. I), on a

$P\,\delta p + Q\,\delta q + R\,\delta r + \ldots = X\,\delta x + Y\,\delta y + Z\,\delta z,$

et la formule générale devient

_(S)$m\left( \frac{d^{2}x}{dt^{2}} + X \right)\delta x +$_(S)$m\left( \frac{d^{2}y}{dt^{2}} + Y \right)\delta y +$_(S)$m\left( \frac{d^{2}z}{dt^{2}} + Z \right)\delta z = 0,$

laquelle, en n’ayant égard qu’aux variations $\delta x^{\prime},\,\delta y^{\prime},\,\delta z^{\prime},$ qui sont indépendantes de toutes les autres, donnera

$\delta x^{\prime}$_(S)$m\left( \frac{d^{2}x}{dt^{2}} + X \right) + \delta y^{\prime}$_(S)$m\left( \frac{d^{2}y}{dt^{2}} + Y \right) + \delta z^{\prime}$_(S)$m\left( \frac{d^{2}z}{dt^{2}} + Z \right) = 0\,;$

d’où l’on tire sur-le-champ ces trois équations

_(S)$m\left( \frac{d^{2}x}{dt^{2}} + X \right) = 0,$

_(S)$m\left( \frac{d^{2}y}{dt^{2}} + Y \right) = 0,$

_(S)$m\left( \frac{d^{2}z}{dt^{2}} + Z \right) = 0,$

lesquelles auront toujours lieu dans le mouvement d’un système quelconque de corps, lorsque le système est entièrement libre.

3\. Supposons maintenant que le corps auquel répondent les coordonnées $x^{\prime},\, y^{\prime},\, z^{\prime}$ soit placé dans le centre de gravité de tout le système. On aura, par les propriétés connues de ce centre (Part. I, sect. III, § IV), les équations

_(S)$m\xi = 0,\qquad$_(S)$m\eta = 0,\qquad$_(S)$m\zeta = 0,$

lesquelles, en différentiant par rapport à $t,$ donneront celles-ci :

_(S)$m\frac{d^{2}\xi}{dt^{2}} = 0,\qquad$_(S)$m\frac{d^{2}\eta}{dt^{2}} = 0,\qquad$_(S)$m\frac{d^{2}\zeta}{dt^{2}} = 0.$

Donc on aura

_(S)$m\frac{d^{2}x}{dt^{2}} =$_(S)$m\frac{d^{2}x^{\prime}}{dt^{2}} = \frac{d^{2}x^{\prime}}{dt^{2}}$_(S)$m,$

parce que $x^{\prime},$ ayant la même valeur pour tous les corps, est indépendante du signe _(S) ; on aura pareillement

_(S)$m\frac{d^{2}y}{dt^{2}} = \frac{d^{2}y^{\prime}}{dt^{2}}$_(S)$m,\qquad$_(S)$m\frac{d^{2}z}{dt^{2}} = \frac{d^{2}z^{\prime}}{dt^{2}}$_(S)$m.$

Ainsi les trois équations de l’article précédent prendront cette forme plus simple :

$\frac{d^{2}x^{\prime}}{dt^{2}}$_(S)$m +$_(S)${mX} = 0,$

$\frac{d^{2}y^{\prime}}{dt^{2}}$_(S)$m +$_(S)${mY} = 0,$

$\frac{d^{2}z^{\prime}}{dt^{2}}$_(S)$m +$_(S)${mZ} = 0.$

Ces équations serviront à déterminer le mouvement du centre de gravité de tous les corps, indépendamment du mouvement particulier de chacun d’eux ; et, comme les valeurs de _(S)${mX},$ _(S)${mY},$ _(S)${mZ},$ ne renferment point les forces intérieures du système, le mouvement de ce centre ne dépendra point de l’action mutuelle que les corps peuvent exercer les uns sur les autres, mais seulement des forces accélératrices qui sollicitent chaque corps. C’est en quoi consiste le principe général de la *conservation du mouvement du centre de gravité*.

Ce principe subsiste aussi dans le cas où les corps, dans leurs mouvements, viendraient à se choquer ; car, de quelque nature que soient les corps, on peut toujours imaginer que leur action dans le choc se fasse par le moyen d’un ressort interposé entre les corps et qui, après la compression, tende à se rétablir ou non suivant que les corps seront élastiques ou non. De cette manière, l’effet du choc sera le produit de forces de la nature de celles que nous avons désignées par ${\bar{P},\,\bar{Q}},\ldots$ et qui disparaissent dans la formule générale (art. 2).

4\. On voit, au reste, que les équations du mouvement du centre de gravité sont les mêmes que celles du mouvement d’un seul corps qui serait animé à la fois par toutes les forces accélératrices qui agissent sur les différents corps du système. En effet, si l’on conçoit que tous ces corps soient réunis en un point qui réponde aux coordonnées $x^{\prime},\, y^{\prime},\, z^{\prime},$ on a alors, dans la formule générale,

$x = x^{\prime},\qquad y = y^{\prime},\qquad z = z^{\prime}\,;$

et, égalant à zéro la totalité des termes affectés de chacune des trois variations $\delta x^{\prime},\,\delta y^{\prime},\,\delta z^{\prime},$ on aura les mêmes équations que ci-dessus.

De là résulte ce théorème général :

*Le mouvement du centre de gravité d’un système libre de corps, disposés, les uns par rapport aux autres, comme l’on voudra, est toujours le même que si les corps étaient tous réunis dans un seul point et qu’en même temps chacun d’eux fût animé des mêmes forces accélératrices que dans leur état naturel.*

5\. Ce théorème a encore lieu lorsque les corps qui composent un système libre ne reçoivent que des impulsions quelconques ; car, en substituant, dans l’équation de l’article 11 de la Section précédente, $\delta x^{\prime} + \delta\xi,$ $\delta y^{\prime} + \delta\eta,$ $\delta z^{\prime} + \delta\zeta$ à la place de $\delta x,\delta y,\delta z,$ et réduisant les forces ${P,Q,R},\ldots$ aux forces ${X,Y,Z},\ldots$ on prouvera, comme dans l’article 2, que les variations $\delta x^{\prime},\,\delta y^{\prime},$ $\delta z^{\prime}$ doivent demeurer arbitraires, ce qui donnera les trois équations

_(S)$(m\overset{˙}{x} + X) = 0,\quad$_(S)$(m\overset{˙}{y} + Y) = 0,\quad$_(S)$(m\overset{˙}{z} + Z) = 0.$

Or, si l’on rapporte les coordonnées $x^{\prime},\, y^{\prime},\, z^{\prime}$ au centre de gravité du système, on a, par les propriétés de ce centre,

$x^{\prime}$_(S)$m =$_(S)$mx,\quad y^{\prime}$_(S)$m =$_(S)$my,\quad z^{\prime}$_(S)$m =$_(S)$mz,\quad$

Donc aussi, en différentiant relativement à $t,$ et faisant

$\begin{matrix}
{dx =} & {\overset{˙}{x}\ dt,\qquad} & {dy =} & {\overset{˙}{y}\ dt,\qquad} & {dz =} & {\overset{˙}{z}\ dt,} \\
{dx^{\prime} =} & {{\overset{˙}{x}}^{\prime}dt,} & {dy^{\prime} =} & {{\overset{˙}{y}}^{\prime}dt,} & {dz^{\prime} =} & {{\overset{˙}{z}}^{\prime}dt,}
\end{matrix}$

on aura

${\overset{˙}{x}}^{\prime}$_(S)$m =$_(S)$m\overset{˙}{x},\quad{\overset{˙}{y}}^{\prime}$_(S)$m =$_(S)$m\overset{˙}{y},\quad{\overset{˙}{z}}^{\prime}$_(S)$m =$_(S)$m\overset{˙}{z}$

et, par conséquent,

${\overset{˙}{x}}^{\prime}$_(S)$m +$_(S)$X = 0,\quad{\overset{˙}{y}}^{\prime}$_(S)$m +$_(S)$Y = 0,\quad{\overset{˙}{z}}^{\prime}$_(S)$m +$_(S)$Z = 0,$

ce qui fait voir que les vitesses ${\overset{˙}{x}}^{\prime},\,{\overset{˙}{y}}^{\prime},\,{\overset{˙}{z}}^{\prime}$ imprimées au centre de gravité sont les mêmes que si tous les corps, étant réunis dans ce centre, recevaient à la fois les impulsions ${X,\, Y,\, Z}.$

6\. La formule générale (art. 2), après la substitution $\delta x^{\prime} + \delta\xi,$ $\delta y^{\prime} + \delta\eta,$ $\delta z^{\prime} + \delta\zeta$ à la place de $\delta x,\,\delta y,\,\delta z$ et l’évanouissement des termes affectés de $\delta x^{\prime},\,\delta y^{\prime},\,\delta z^{\prime},$ se réduira à

_(S)$m\left( \frac{d^{2}x}{dt^{2}}\delta\xi + \frac{d^{2}y}{dt^{2}}\delta\eta + \frac{d^{2}z}{dt^{2}}\delta\zeta + X\delta\xi + Y\delta\eta + Z\delta\zeta \right) = 0.$

Substituant $x^{\prime} + \xi,\, y^{\prime} + \eta,\, z^{\prime} + \zeta$ pour $x,\, y,\, z$ dans les différentielles $d^{2}x,\, d^{2}y,$ $d^{2}z,$ et faisant sortir hors du signe _(S) les différentielles $d^{2}x^{\prime},d^{2}y^{\prime},$ $d^{2}z^{\prime},$ les termes affectés de ces différentielles seront

$\frac{d^{2}x^{\prime}}{dt^{2}}$_(S)$m\,\delta\xi + \frac{d^{2}y^{\prime}}{dt^{2}}$_(S)$m\,\delta\eta + \frac{d^{2}z^{\prime}}{dt^{2}}$_(S)$m\,\delta\zeta.$

Mais, en rapportant au centre de gravité les coordonnées $x^{\prime},y^{\prime},z^{\prime},$ on a (art. 3)

_(S)$m\xi = 0,\qquad$_(S)$m\eta = 0,\qquad$_(S)$m\zeta = 0\,;$

donc aussi, en différentiant par $\delta,$ on aura

_(S)$m\delta\xi = 0,\qquad$_(S)$m\delta\eta = 0,\qquad$_(S)$m\delta\zeta = 0,$

ce qui fait évanouir les termes dont il s’agit.

Ainsi la formule générale se réduira à

_(S)$m\left( \frac{d^{2}\xi}{dt^{2}}\delta\xi + \frac{d^{2}\eta}{dt^{2}}\delta\eta + \frac{d^{2}\zeta}{dt^{2}}\delta\zeta + X\delta\xi + Y\delta\eta + Z\delta\zeta \right) = 0,$

qui est tout à fait semblable à la première formule, les coordonnées $x,\, y,\, z,$ dont l’origine est fixe dans l’espace, étant changées en $\xi,\,\eta,\,\zeta,$ dont l’origine est au centre de gravité.

On peut conclure de là^([\[1\]](#cite_note-1)), en général, que, dans un système libre, on aura, par rapport au centre de gravité, les mêmes équations et les mêmes propriétés que par rapport à un point fixe hors du système.

§ II. — *Propriétés relatives aux aires*.

7\. Considérons maintenant le mouvement du système autour d’un point fixe, et supposons qu’il soit entièrement libre de tourner en tout sens autour de ce point. En faisant abstraction des mouvements respectifs des corps du système les uns à l’égard des autres, la rotation autour de chacun des trois axes des $x,\, y,\, z$ fournira, comme on l’a vu dans la première Partie (sect. III, art. 8), les expressions suivantes des variations $\delta x,\,\delta y,\,\delta z,$

$\delta x = z\,\delta\omega - y\,\delta\varphi,\qquad\delta y = x\,\delta\varphi - z\,\delta\psi,\,\qquad\delta z = y\,\delta\psi - x\,\delta\omega,$

dans lesquelles $\delta\varphi,\,\delta\omega,\delta\psi$ sont les rotations élémentaires par rapport aux trois axes des $z,\, y,\, x,$ qui doivent demeurer arbitraires.

Ces expressions sont générales pour les variations des coordonnées de tous les corps du système, et il ne s’agira que de les substituer dans la formule de l’article 5 de la Section précédente, après avoir réduit toutes les variations à $\delta x,\,\delta y,\,\delta z,$ et d’égaler ensuite à zéro séparément les quantités affectées des trois indéterminées $\delta\varphi,\,\delta\omega,\delta\psi.$

On trouvera d’abord, comme dans l’article cité de la première Partie, que la variation $\delta\bar{p}$ devient nulle, et qu’ainsi les termes dus aux forces intérieures $\bar{P}$ du système, ne renfermant point les variations $\delta\varphi,\,\delta\omega,\delta\psi,\,$ ne donneront rien dans les équations dont il s’agit. On trouve aussi, comme on l’a vu dans le même article, que la variation $\delta p$ est nulle lorsque la force $P$ tend vers l’origine des coordonnées, et qu’ainsi cette force n’entrera point dans les mêmes équations.

En faisant donc simplement pour $\delta x,\,\delta y,\,\delta z$ les substitutions indiquées, après avoir changé les forces ${P,Q,R},\ldots$ en ${X,Y,Z},$ comme ci-dessus (art. 2), on aura, relativement aux variations $\delta\varphi,\,\delta\omega,\delta\psi,\,$ l’équation

_(S)$m\begin{Bmatrix}
 & {\left( x\frac{d^{2}y}{dt^{2}} - y\frac{d^{2}x}{dt^{2}} + Yx - Xy \right)\delta\varphi} \\
 + & {\left( z\frac{d^{2}x}{dt^{2}} - x\frac{d^{2}z}{dt^{2}} + Xz\, - Zx \right)\delta\omega} \\
 + & {\left( y\frac{d^{2}z}{dt^{2}}\, - z\frac{d^{2}y}{dt^{2}} + Zy\, - Yz \right)\delta\psi}
\end{Bmatrix} = 0\,;$

et, comme les variations $\delta\varphi,\,\delta\psi,\,\delta\omega$ sont les mêmes pour tous les corps du système, elles n’entreront pas sous le signe d’intégration _(S) ; de sorte qu’on aura les trois équations relatives à chacune de ces variations

_(S)$m\left( x\frac{d^{2}y}{dt^{2}} - y\frac{d^{2}x}{dt^{2}} + xY - yX \right) = 0,$

_(S)$m\left( z\frac{d^{2}x}{dt^{2}} - x\frac{d^{2}z}{dt^{2}} + zX - xZ \right) = 0,$

_(S)$m\left( y\frac{d^{2}z}{dt^{2}} - z\frac{d^{2}y}{dt^{2}} + yZ - zY \right) = 0.$

Ces équations auront lieu à la fois, lorsque le système aura la liberté de tourner autour de chacun des trois axes, c’est-à-dire toutes les fois que le système sera disposé de manière à pouvoir pirouetter librement en tout sens autour du point fixe qui est l’origine des coordonnées.

Et il est bon de remarquer que ces équations ont toujours lieu indépendamment de l’action mutuelle des corps, de quelque manière que cette action puisse s’exercer, même par le choc mutuel des corps du système, comme dans l’article 3 et par la même raison ; elles sont, de plus, indépendantes des forces qui tendraient vers le point fixe où est l’origine des coordonnées.

8\. Pour se former une idée plus nette de ces équations, on remarquera :

1^(o) Que les quantités

$xd^{2}y - yd^{2}x,\quad zd^{2}x - xd^{2}z,\quad yd^{2}z - zd^{2}y$

sont les différentielles de celles-ci

$xdy - ydx,\quad zdx - xdz,\quad ydz - zdy,$

lesquelles représentent le double des secteurs élémentaires décrits par le corps $m$ sur le plan des $xy,$ des $xz$ et des $yz,$ c’est-à-dire sur les plans perpendiculaires aux axes des $z,$ des $y$ et des $x.$ En effet, si dans

$xdy - ydx$

on substitue pour $x$ et $y$ les valeurs $\rho\cos\varphi,\,\rho\sin\varphi,$ on a

$\rho^{2}\delta\varphi$

double de l’aire comprise entre le rayon vecteur $\rho$ et le rayon consécutif qui fait avec lui l’angle $d\varphi\,;$

2^(o) Que les quantités $X,\, Y,\, Z$ représentent les forces qui sollicitent chaque corps $m$ suivant les coordonnées $x,\, y,\, z$ et vers leur origine, et qui résultent de toutes les forces ${P,\, Q,\, R},\ldots$ agissantes sur ce corps suivant des directions quelconques (sect. II, art. 5), et qu’ainsi les quantités

$yX - xY,\qquad xZ - zX,\qquad zY - yZ$

expriment les moments des forces qui tendent à faire tourner les corps autour de chacun des trois axes des coordonnées $z,\, y,\, x,$ en prenant le mot *moment*, dans le sens ordinaire, pour le produit de la force et de la perpendiculaire menée sur sa direction.

9\. Si le système n’était animé par aucune force extérieure, ou s’il l’était seulement par des forces tendantes au point que nous avons pris pour l’origine des coordonnées, les trois équations précédentes se réduiraient à celles-ci

_(S)$m\left( x\frac{d^{2}y}{dt^{2}} - y\frac{d^{2}x}{dt^{2}} \right) = 0,$

_(S)$m\left( z\frac{d^{2}x}{dt^{2}} - x\frac{d^{2}z}{dt^{2}} \right) = 0,$

_(S)$m\left( y\frac{d^{2}z}{dt^{2}} - z\frac{d^{2}y}{dt^{2}} \right) = 0,$

lesquelles, étant intégrées par rapport à la variable $t,$ donneront, en prenant trois constantes arbitraires ${A,B,C},$

_(S)$m\left( x\frac{d^{2}y}{dt^{2}} - y\frac{d^{2}x}{dt^{2}} \right) = C,$

_(S)$m\left( z\frac{d^{2}x}{dt^{2}} - x\frac{d^{2}z}{dt^{2}} \right) = B,$

_(S)$m\left( y\frac{d^{2}z}{dt^{2}} - z\frac{d^{2}y}{dt^{2}} \right) = A.$

Ces dernières équations renferment évidemment le *principe des aires*, dont nous avons parlé dans la première Section.

10\. Il est à propos de remarquer que ces équations sont dans le cas de l’article 10 de la Section précédente ; de sorte qu’on y peut introduire trois nouvelles constantes arbitraires, par le changement des axes des coordonnées.

Soient $x^{\prime},\, y^{\prime},\, z^{\prime}$ les nouvelles coordonnées ; on aura également

_(S)$m\left( x^{\prime}\frac{d^{2}y^{\prime}}{dt^{2}} - y^{\prime}\frac{d^{2}x^{\prime}}{dt^{2}} \right) = C^{\prime},$

_(S)$m\left( z^{\prime}\frac{d^{2}x^{\prime}}{dt^{2}} - x^{\prime}\frac{d^{2}z^{\prime}}{dt^{2}} \right) = B^{\prime},$

_(S)$m\left( y^{\prime}\frac{d^{2}z^{\prime}}{dt^{2}} - z^{\prime}\frac{d^{2}y^{\prime}}{dt^{2}} \right) = A^{\prime},$

les quantités $A^{\prime},\, B^{\prime},\, C^{\prime}$ étant aussi des constantes arbitraires, mais différentes de ${A,\, B,\, C}.$

Substituons maintenant dans l’expression $x\, dy - y\, dx$ les valeurs de $x,\, y$ en $x^{\prime},\, y^{\prime},\, z^{\prime}$ données dans l’article cité de la même Section : on aura

$\begin{matrix}
{xdy - ydx =} & {+ (\alpha\beta^{\prime}} & - & {\beta\alpha^{\prime})(x^{\prime}} & {dy^{\prime} - y^{\prime}} & {dx^{\prime}) + (\gamma\alpha^{\prime} - \alpha\gamma^{\prime})(z^{\prime}dx^{\prime} - x^{\prime}dz^{\prime})} \\
 & {+ (\beta\gamma^{\prime}} & - & {\gamma\beta^{\prime})(y^{\prime}} & {dz^{\prime} - z^{\prime}} & {dy^{\prime}).}
\end{matrix}$

On trouvera de même

$\begin{matrix}
{zdx - xdz =} & {+ (\beta\alpha^{''}} & - & {\alpha\beta^{''})(x^{\prime}} & {dx^{\prime} - y^{\prime}} & {dz^{\prime}) + (\alpha\gamma^{''} - \gamma\alpha^{''})(z^{\prime}dx^{\prime} - x^{\prime}dz^{\prime})} \\
 & {+ (\gamma\beta^{''}} & - & {\beta\gamma^{''})(y^{\prime}} & {dz^{\prime} - z^{\prime}} & {dy^{\prime}),}
\end{matrix}$

$\begin{matrix}
{ydz - zdy =} & {+ (\alpha^{\prime}\beta^{''}} & - & {\beta^{\prime}\alpha^{''})(x^{\prime}} & {dy^{\prime} - y^{\prime}} & {dx^{\prime}) + (\gamma^{\prime}\alpha^{''} - \alpha^{\prime}\gamma^{''})(z^{\prime}dx^{\prime} - x^{\prime}dz^{\prime})} \\
 & {+ (\gamma^{\prime}\beta^{''}} & - & {\beta^{\prime}\gamma^{''})(y^{\prime}} & {dz^{\prime} - z^{\prime}} & {dy^{\prime}).}
\end{matrix}$

Si l’on affecte tous les termes de ces équations du signe _(S), après les avoir multipliées par $m$ et divisées par $dt,$ et qu’on y substitue, à la place des intégrales affectées de _(S), leurs valeurs ${A,\, B,\, C},$ ${A^{\prime},\, B^{\prime},\, C^{\prime}},$ on aura

$\begin{matrix}
{C =} & {(\alpha\beta^{\prime}} & - & {\beta\alpha^{\prime})C^{\prime}} & + & {(\gamma\alpha^{\prime}} & - & {\alpha\gamma^{\prime})B^{\prime}} & + & {(\beta\gamma^{\prime}} & - & {\gamma\beta^{\prime})A^{\prime},} \\
{B =} & {(\beta\alpha^{''}} & - & {\alpha\beta^{''})C^{\prime}} & + & {(\alpha\gamma^{''}} & - & {\gamma\alpha^{''})B^{\prime}} & + & {(\gamma\beta^{''}} & - & {\beta\gamma^{''})A^{\prime},} \\
{A =} & {(\alpha^{\prime}\beta^{''}} & - & {\beta^{\prime}\alpha^{''})C^{\prime}} & + & {(\gamma^{\prime}\alpha^{''}} & - & {\alpha^{\prime}\gamma^{''})B^{\prime}} & + & {(\gamma^{\prime}\beta^{''}} & - & {\beta^{\prime}\gamma^{''})A^{\prime}.}
\end{matrix}$

On peut réduire ces formules à une expression plus simple, en observant que l’on a identiquement

$\begin{matrix}
 & {(\alpha\beta^{\prime} - \beta\alpha^{\prime})^{2} + (\beta\alpha^{''} - \alpha\beta^{''})^{2} + (\alpha^{\prime}\beta^{''} - \beta^{\prime}\alpha^{''})^{2}} \\
 & {\qquad = \left( \alpha^{2} + \alpha'^{2} + \alpha^{\prime}'^{2} \right)\left( \beta^{2} + \beta'^{2} + \beta^{\prime}'^{2} \right) - (\alpha\beta + \alpha^{\prime}\beta^{\prime} + \alpha^{''}\beta^{''})^{2},}
\end{matrix}$

quantité qui se réduit à l’unité, en vertu des équations de condition de la première Partie (sect. III, art. 10). On a, de plus, ces équations identiques

$\begin{matrix}
{\alpha(\alpha^{\prime}\beta^{''} - \beta^{\prime}\alpha^{''}) + \alpha^{\prime}(\beta\alpha^{''} - \alpha\beta^{''}) + \alpha^{''}(\alpha\beta^{\prime} - \beta\alpha^{\prime}) =} & {0,} \\
{\beta(\alpha^{\prime}\beta^{''} - \beta^{\prime}\alpha^{''}) + \beta^{\prime}\,(\beta\alpha^{''} - \alpha\beta^{''}) + \beta^{''}(\alpha\beta^{\prime} - \beta\alpha^{\prime}) =} & {0,} \\
 &
\end{matrix}$

Si donc on compare ces équations avec les trois équations de condition

$\gamma^{2} + \gamma^{2} + \gamma^{2} = 1,\quad\alpha\gamma + \alpha^{\prime}\gamma^{\prime} + \alpha^{''}\gamma^{''} = 0,\quad\beta\gamma + \beta^{\prime}\gamma^{\prime} + \beta^{''}\gamma^{''} = 0,$

il est facile de conclure de cette comparaison qu’on aura

$\alpha^{\prime}\beta^{''} - \beta^{\prime}\alpha^{''} = \gamma,\quad\beta\alpha^{''} - \alpha\beta^{''} = \gamma^{\prime},\quad\alpha\beta^{\prime} - \beta\alpha^{\prime} = \gamma^{''}.$

Les quantités $\gamma,\gamma^{\prime},\gamma^{''}$ pourraient avoir également le signe $- \,;$ mais comme, dans la coïncidence des axes des $x^{\prime},\, y^{\prime},\, z^{\prime}$ avec ceux des $x,\, y,\, z$, on doit avoir (Part. I, sect. III, art. 11)

$\alpha = 1,\ \ \beta = 0,\ \ \gamma = 0,\ \ \alpha^{\prime} = 0,\ \ \beta^{\prime} = 1,\ \ \gamma^{\prime} = 0,\ \ \alpha^{''} = 0,\ \ \beta^{''} = 0,\ \ \gamma^{''} = 1,$

cette condition ne peut avoir lieu qu’en prenant $\gamma^{''}$ positivement, et par conséquent aussi $\gamma^{\prime}$ et $\gamma.$

On trouvera, de la même manière,

$\begin{matrix}
{\gamma^{\prime}\alpha^{''} - \alpha^{\prime}\gamma^{''} =} & {\beta,\quad} & {\quad\alpha\gamma^{''} - \gamma\alpha^{''} =} & {\beta^{\prime},\quad} & {\quad\gamma\alpha^{\prime} - \alpha\gamma^{\prime} =} & {\beta^{''},} \\
{\gamma^{\prime}\beta^{''} - \beta^{\prime}\gamma^{''} =} & {\alpha,} & {\quad\gamma\beta^{''} - \beta\gamma^{''} =} & {\alpha^{\prime},} & {\quad\beta\gamma^{\prime} - \gamma\beta^{\prime} =} & {\alpha^{''}\,;}
\end{matrix}$

de sorte que l’on aura

$\begin{matrix}
{A =} & \alpha & {A^{\prime} +} & \beta & {B^{\prime} +} & \gamma & {C^{\prime},} \\
{B =} & \alpha^{\prime} & {A^{\prime} +} & \beta^{\prime} & {B^{\prime} +} & \gamma^{\prime} & {C^{\prime},} \\
{C =} & \alpha^{''} & {A^{\prime} +} & \beta^{''} & {B^{\prime} +} & \gamma^{''} & {C^{\prime}\,;}
\end{matrix}$

d’où l’on tire, par les équations de condition de l’article 10 (Part. 1, sect. III),

$\begin{matrix}
{A^{\prime} =} & {{A\alpha + B\alpha^{\prime} + C\alpha^{''}},} \\
{B^{\prime} =} & {{A\beta + B\beta^{\prime} + C\beta^{''}},} \\
{C^{\prime} =} & {A\gamma + B\gamma^{\prime} + C\gamma^{''}}
\end{matrix}$

et

${A^{2} + B^{2} + C^{2} = A'^{2} + B'^{2} + C'^{2}}.$

Il résulte de cette dernière équation qu’on a, en général,

$\quad\left\lbrack \operatorname{} \right.$_(S)$\left. \operatorname{}m\left( x\ \frac{dy}{dt}\  - y\ \frac{dx}{dt}\,\  \right) \right\rbrack^{2} + \left\lbrack \operatorname{} \right.$_(S)$\left. \operatorname{}m\left( z\ \frac{dx}{dt}\  - x\ \frac{dz}{dt}\,\  \right) \right\rbrack^{2} +$$\left\lbrack \operatorname{} \right.$_(S)$\left. \operatorname{}m\left( y\ \frac{dz}{dt}\  - z\ \frac{dy}{dt}\  \right) \right\rbrack^{2},$

$= \left\lbrack \operatorname{} \right.$_(S)$\left. \operatorname{}m\left( x^{\prime}\frac{dy^{\prime}}{dt} - y^{\prime}\frac{dx^{\prime}}{dt} \right) \right\rbrack^{2} + \left\lbrack \operatorname{} \right.$_(S)$\left. \operatorname{}m\left( z^{\prime}\frac{dx^{\prime}}{dt} - x^{\prime}\frac{dz^{\prime}}{dt} \right) \right\rbrack^{2} +$$\left\lbrack \operatorname{} \right.$_(S)$\left. \operatorname{}m\left( y^{\prime}\frac{dz^{\prime}}{dt} - z^{\prime}\frac{dy^{\prime}}{dt} \right) \right\rbrack^{2},$

d’où l’on peut conclure que la fonction

$\quad\left\lbrack \operatorname{} \right.$_(S)$\left. \operatorname{}m\left( x\frac{dy}{dt} - y\frac{dx}{dt} \right) \right\rbrack^{2} + \left\lbrack \operatorname{} \right.$_(S)$\left. \operatorname{}m\left( z\frac{dx}{dt} - x\frac{dz}{dt} \right) \right\rbrack^{2} +$$\left\lbrack \operatorname{} \right.$_(S)$\left. \operatorname{}m\left( y\frac{dz}{dt} - z\frac{dy}{dt} \right) \right\rbrack^{2},$

a toujours une valeur indépendante du plan de projection et de la position des axes des coordonnées $x,\, y,\, z$ dans l’espace, pourvu que ces coordonnées soient rectangulaires entre elles.

11\. Ces expressions de $A,\, B,\, C$ en $A^{\prime},\, B^{\prime},\, C^{\prime}$ qu’on vient de trouver sont semblables à celles de $x,\, y,\, z$ en $x^{\prime},\, y^{\prime},\, z^{\prime}$ de l’article 9 de la Section précédente ; par conséquent, si l’on prend

$x^{\prime} = A^{\prime},\quad y^{\prime} = B^{\prime},\quad z^{\prime} = C^{\prime},$

on aura

$A = x,\quad B = y,\quad C = z,$

et réciproquement

$x = A,\quad y = B,\quad z = C$

donnera

$A^{\prime} = x^{\prime},\quad B^{\prime} = y^{\prime},\quad C^{\prime} = z^{\prime}\,;$

c’est-à-dire que $A,\, B,\, C$ et $A^{\prime},\, B^{\prime},\, C^{\prime}$ seront deux systèmes de coordonnées qui répondent à un même point, le premier étant relatif aux axes des $x,\, y,\, z$ et le second aux axes des $x^{\prime},\, y^{\prime},\, z^{\prime}.$

On voit tout de suite par là qu’on peut faire

$A^{\prime} = 0,\qquad B^{\prime} = 0,$

en faisant passer l’axe des $C^{\prime}$ ou $z^{\prime}$ par le point auquel répondent les coordonnées ${A,\, B,\, C},$ et qu’alors la coordonnée $C^{\prime}$ aura sa plus grande valeur égale à $\sqrt{A^{2} + B^{2} + C^{2}}.$ On aura, dans ce cas,

${A = \gamma C^{\prime},\quad B = \gamma^{\prime}C^{\prime},\quad C = \gamma^{''}C^{\prime}},$

et il est facile de voir que les coefficients $\gamma,\,\gamma^{\prime},\,\gamma^{''}$ ne seront autre chose que les cosinus des angles que la ligne $C^{\prime}$ fait avec les axes des ${A,\, B,\, C}.$

Ainsi la résolution des équations

_(S)$m\left( x^{\prime}\frac{dy^{\prime}}{dt} - y^{\prime}\frac{dx^{\prime}}{dt} \right) = C^{\prime},$

_(S)$m\left( z^{\prime}\frac{dx^{\prime}}{dt} - x^{\prime}\frac{dz^{\prime}}{dt} \right) = 0,\ $

_(S)$m\left( y^{\prime}\frac{dz^{\prime}}{dt} - z^{\prime}\frac{dy^{\prime}}{dt} \right) = 0\ \,$

donnera celle des équations

_(S)$m\left( x\frac{dy}{dt} - y\frac{dx}{dt} \right) = \gamma^{''}C^{\prime},$

_(S)$m\left( z\frac{dx}{dt} - x\frac{dz}{dt} \right) = \gamma^{\prime}C^{\prime},$

_(S)$m\left( y\frac{dz}{dt} - z\frac{dy}{dt} \right) = \gamma C^{\prime},$

les quantités $\gamma,\,\gamma^{\prime},\,\gamma^{''}$ étant trois constantes telles que

$\gamma^{2} + \gamma'^{2} + \gamma^{\prime}'^{2} = 1$

et dont deux sont arbitraires.

Le plan perpendiculaire à l’axe des $C^{\prime},$ lorsque $C^{\prime}$ devient un maximum, est celui que M. Laplace nomme *plan invariable*, et dont il a le premier démontré l’existence et la position.

Cette position est facile à déterminer par les équations

${A = \gamma C^{\prime},\qquad B = \gamma^{\prime}C^{\prime},\qquad C = \gamma^{''}C^{\prime}}\,;$

car, puisque les quantités $\gamma,\,\gamma^{\prime},\,\gamma^{''}$ sont les cosinus des angles que l’axe des $C^{\prime}$ ou $z^{\prime},$ qui est perpendiculaire au plan variable, fait avec les axes des $x,\, y,\, z$ du système, en nommant ces angles $l,\, m,\, n,$ on aura, à cause de

${C^{\prime} = \sqrt{A^{2} + B^{2} + C^{2}}},$

$\cos l = \frac{A}{\sqrt{A^{2} + B^{2} + C^{2}}},\quad\cos m = \frac{B}{\sqrt{A^{2} + B^{2} + C^{2}}},$

$\cos n = \frac{C}{\sqrt{A^{2} + B^{2} + C^{2}}}.$

12\. Si le système est libre, c’est-à-dire s’il n’y a aucun des points du système qui doive être fixe, on peut prendre l’origine, supposée fixe, des coordonnées $x,\, y,\, z$ partout où l’on voudra ; par conséquent, les propriétés des aires et des moments que nous venons de démontrer auront lieu par rapport à un point fixe quelconque pris à volonté dans l’espace.

Mais, par ce que nous avons démontré dans l’article 6, ces mêmes propriétés auront lieu également par rapport au centre de gravité de tout le système, soit que ce centre soit fixe ou non. En effet, si, dans le s trois équations de l’article 7, on substitue pour $x,\, y,\, z$ les quantités $x^{\prime} + \xi,\ y^{\prime} + \eta,\ z^{\prime} + \zeta,$ en rapportant, comme dans l’article 3, les coordonnées $x^{\prime},\, y^{\prime},\, z^{\prime}$ au centre de gravité du système, et qu’on ait égard aux trois équations de ce dernier article, on aura ces transformées

_(S)$m\left( \xi\frac{d^{2}\eta}{dt^{2}} - \eta\frac{d^{2}\xi}{dt^{2}} + \xi Y - \eta X \right) = 0,$

_(S)$m\left( \zeta\frac{d^{2}\xi}{dt^{2}} - \xi\frac{d^{2}\zeta}{dt^{2}} + \zeta X - \xi Z \right) = 0,$

_(S)$m\left( \eta\frac{d^{2}\zeta}{dt^{2}} - \zeta\frac{d^{2}\eta}{dt^{2}} + \eta Z - \zeta Y \right) = 0,$

qui sont, comme l’on voit, semblables à celles de l’article 7, et dont toute la différence consiste en ce que, à la place des coordonnées $x,$ $y,z$ partant d’un point fixe, il y a les coordonnées $\xi,\,\eta,\,\zeta$ dont l’origine est dans le centre de gravité du système.

Ainsi, lorsque les forces accélératrices sont nulles, on aura les intégrales

_(S)$m\left( \xi\frac{d\eta}{dt} - \eta\frac{d\xi}{dt} \right) = C,$

_(S)$m\left( \zeta\frac{d\xi}{dt} - \xi\frac{d\zeta}{dt} \right) = B,$

_(S)$m\left( \eta\frac{d\zeta}{dt} - \zeta\frac{d\eta}{dt} \right) = A,$

sur lesquelles on pourra faire des remarques analogues à celles que nous avons faites sur les équations de l’article 9.

13\. Quand un des corps du système est retenu fixement par un obstacle quelconque, en plaçant dans ce corps l’origine des coordonnées, on a le cas de l’article 7. Mais, si deux corps du système sont supposés fixes, on regardera la ligne qui passe par ces deux corps comme un axe fixe autour duquel le système peut tourner librement, et, prenant cet axe pour celui des coordonnées $z,$ on aura simplement, par le même article,

$\delta x = - y\,\delta\varphi,\quad\delta y = x\,\delta\varphi,$

$\delta\varphi$ étant la rotation élémentaire autour de cet axe, laquelle doit demeurer indéterminée. On n’aura ainsi qu’une seule équation relative à cette variation $\delta\varphi,$ laquelle sera

_(S)$m\left( x\frac{d^{2}y}{dt^{2}} - y\frac{d^{2}x}{dt^{2}} + xY - yX \right) = 0\,;$

et lorsque le moment $xY - yX$ des forces extérieures par rapport à l’axe de rotation est nul, on aura par l’intégration, comme dans l’article 9,

_(S)$m\left( x\frac{dy}{dt} - y\frac{dx}{dt} \right) = C,$

équation qui donne le principe des aires par rapport au plan des $xy$ perpendiculaire à l’axe de rotation, et sur lequel les aires décrites par les corps doivent être projetées.

Si trois corps du système étaient supposés fixes, alors la position de chacun des autres corps dans l’espace serait déterminée par ses distances à ces trois corps, et il n’y aurait plus de variations indépendantes de la nature du système et de la disposition respective des corps entre eux, d’où l’on pût déduire des équations générales pour le mouvement d’un système quelconque.

§ III. — *Propriétés relatives aux rotations produites par des forces d’impulsion*.

14\. Quand un, système libre de tourner en tout sens autour d’un point fixe reçoit des impulsions quelconques, on peut aussi employer, dans l’équation de l’article 11 de la Section précédente, les expressions de $\delta x,\,\delta y,\,\delta z$ de l’article 7, après avoir réduit à $X,\, Y,\, Z$ les forces d’impulsion ${P,\, Q,\, R},\ldots$ et, en égalant séparément à zéro les termes multipliés par les variations $\delta\varphi,\,\delta\omega,\,\delta\psi,$ on aura les trois équations

_(S)$\left\lbrack m(x\overset{˙}{y} - y\overset{˙}{x}) + xY - yX \right\rbrack = 0,$

_(S)$\left\lbrack m(z\,\overset{˙}{x} - x\overset{˙}{z}\,) + z\, X - xZ \right\rbrack = 0,$

_(S)$\left\lbrack m(y\overset{˙}{z}\, - z\,\overset{˙}{y}) + y\ Z\, - zY \right\rbrack = 0,$

pour le premier instant du mouvement produit par les impulsions ${X,\, Y,\, Z}.$

Dans les systèmes qui sont tout à fait libres, on peut prendre le point fixe partout où l’on veut dans l’espace, et les équations précédentes auront toujours lieu par rapport à ce point.

15\. Dans ces systèmes, on peut aussi rapporter leurs rotations à trois axes qui passent par le centre de gravité ; car, en faisant, comme dans l’article 5,

$\delta x = \delta x^{\prime} + \delta\xi,\quad\delta y = \delta y^{\prime} + \delta\eta,\quad\delta z = \delta z^{\prime} + \delta\zeta,$

les variations $\delta x^{\prime},\,\delta y^{\prime},\,\delta z^{\prime}$ donneront d’abord les trois équations relatives au mouvement du centre de gravité trouvées dans ce même article.

Il restera ensuite l’équation

_(S)$\left\lbrack (m\overset{˙}{x} + X)\delta\xi + (m\overset{˙}{y} + Y)\delta\eta + (m\overset{˙}{z} + Z)\delta\zeta \right\rbrack = 0.$

Or, en rapportant les rotations $\delta\psi,\,\delta\omega,\,\delta\varphi$ aux axes des coordonnées $\xi,\,\eta,\,\zeta,$ et n’ayant égard qu’à ces rotations, on a, comme dans l’article 7,

$\delta\xi = \zeta\,\delta\omega - \eta\,\delta\varphi,\quad\delta\eta = \xi\,\delta\varphi - \zeta\,\delta\psi,\quad\delta\zeta = \eta\,\delta\psi - \xi\,\delta\omega,$

et les trois variations indéterminées $\delta\psi,\delta\omega,\delta\varphi$ donneront les trois équations

_(S)$\left\lbrack m(\xi\overset{˙}{y} - \eta\overset{˙}{x}) + \xi Y - \eta X \right\rbrack = 0,$

_(S)$\left\lbrack m(\zeta\overset{˙}{x} - \xi\overset{˙}{z}) + \zeta X - \xi Z \right\rbrack = 0,$

_(S)$\left\lbrack m(\eta\overset{˙}{z} - \zeta\overset{˙}{y}) + \eta Z - \zeta Y \right\rbrack = 0,$

Mais

$\overset{˙}{x} = {\overset{˙}{x}}^{\prime} + \overset{˙}{\xi},\qquad\overset{˙}{y} = {\overset{˙}{y}}^{\prime} + \overset{˙}{\eta},\qquad\overset{˙}{z} = {\overset{˙}{z}}^{\prime} + \overset{˙}{\zeta}\,;$

donc, substituant ces valeurs, faisant sortir hors du signe _(S) les quantités ${\overset{˙}{x}}^{\prime},\,{\overset{˙}{y}}^{\prime},\,{\overset{˙}{z}}^{\prime},$ qui ne se rapportent qu’au centre de gravité, et observant que, par les propriétés de ce centre, on a

_(S)$m\xi = 0,\quad$_(S)$m\eta = 0,\quad$_(S)$m\zeta = 0,$

les trois équations précédentes deviendront

_(S)$\left\lbrack m(\xi\overset{˙}{\eta} - \eta\overset{˙}{\xi}) + \xi Y - \eta X \right\rbrack = 0,$

_(S)$\left\lbrack m(\zeta\overset{˙}{\xi} - \xi\overset{˙}{\zeta}) + \zeta X - \xi Z \right\rbrack = 0,$

_(S)$\left\lbrack m(\eta\overset{˙}{\zeta} - \zeta\,\overset{˙}{\eta}) + \eta Z - \zeta Y \right\rbrack = 0,$

qui sont tout à fait semblables à celles de l’article précédent, et dans lesquelles les coordonnées $\xi,\,\eta,\,\zeta$ ont leur origine au centre de gravité, et les vitesses $\overset{˙}{\xi},\,\overset{˙}{\eta},\,\overset{˙}{\zeta}$ sont relatives à ce centre.

Ainsi les équations relatives à un point fixé subsistent aussi, lorsque le système est libre, par rapport à son centre de gravité.

16\. Les équations que nous venons de trouver, pour l’effet des impulsions dans le premier instant, ont lieu aussi dans les instants suivants, s’il n’y a point de forces accélératrices, en regardant comme constants les termes qui dépendent des impulsions ${X,\, Y,\, Z}\,;$ car, $\overset{˙}{x},\,\overset{˙}{y},\,\overset{˙}{z}$ étant les vitesses parallèlement aux axes des $x,\, y,\, z,$ on a

$dx = \overset{˙}{x}dt,\quad dy = \overset{˙}{y}dt,\quad dz = \overset{˙}{z}dt,$

et les équations de l’article 9 deviennent

_(S)$m(x\overset{˙}{y} - y\overset{˙}{x}) = C,$

_(S)$m(z\overset{˙}{x} - x\overset{˙}{z}) = B,$

_(S)$m(y\overset{˙}{z}\, - z\,\overset{˙}{y}) = A,$

lesquelles, étant comparées à celles de l’article 14, donnent

$C =$_(S)$(yX - xY),$

$B =$_(S)$(xZ - zX),$

$A =$_(S)$(zY - yZ),$

Ainsi on a les valeurs des constantes $A,\, B,\, C$ exprimées par les impulsions primitives données à chaque corps ; et l’on voit que ces valeurs ne sont autre chose que les sommes des moments de ces impulsions par rapport aux axes des $x,$ des $y$ et des $z.$

Il en sera de même des équations relatives au centre de gravité, en comparant les équations de l’article 12 avec celles de l’article 15.

17\. Si l’on ne considère que les mouvements de rotation par rapport aux trois axes des coordonnées $x,\, y,\, z,$ et qu’on désigne par $\overset{˙}{\psi},\overset{˙}{\omega},\overset{˙}{\varphi}$ les vitesses de ces rotations, les variations $\delta x,\,\delta y,\,\delta z$ seront proportionnelles aux vitesses $\overset{˙}{x},\,\overset{˙}{y},\,\overset{˙}{z},$ et les variations $\delta\psi,\,\delta\omega,\,\delta\varphi$ seront en même temps proportionnelles aux vitesses $\overset{˙}{\psi},\overset{˙}{\omega},\overset{˙}{\varphi}\,;$ les formules de l’article 7 donneront ainsi

$\overset{˙}{x} = z\overset{˙}{\omega} - y\overset{˙}{\varphi},\qquad\overset{˙}{y} = x\overset{˙}{\varphi} - z\overset{˙}{\psi},\qquad\overset{˙}{z} = y\overset{˙}{\psi} - x\overset{˙}{\omega}.$

Ces valeurs de $x,\, y,\, z$ ne sont que les parties qui dépendent des trois rotations ; pour avoir les valeurs complètes des vraies vitesses $\overset{˙}{x},\,\overset{˙}{y},\,\overset{˙}{z},$ il faut y ajouter les parties qui dépendent du changement de situation des corps du système entre eux, et qui sont indépendantes des rotations.

Mais lorsque le système est invariable, ce qui a lieu dans tous les corps solides d’une figure quelconque, ces parties des vitesses sont nulles et les valeurs de $x,\, y,\, z$ se réduisent simplement à celles que nous venons de donner. On pourra donc substituer ces valeurs dans les équations précédentes et, faisant sortir hors du signe _(S) les quantités $\overset{˙}{\psi},\,\overset{˙}{\omega},\,\overset{˙}{\varphi},$ on aura, pour un solide de figure quelconque, en mettant l’élément $Dm$ à la place de $m$ (sect. 11, art. 7), les équations

$\overset{˙}{\varphi}$_(S)$\left( x^{2} + y^{2} \right){Dm} - \overset{˙}{\psi}$_(S)$xz{Dm} - \overset{˙}{\omega}$_(S)$yz{Dm = C},$

$\overset{˙}{\omega}\,$_(S)$\left( x^{2} + z^{2}\, \right){Dm} - \overset{˙}{\psi}$_(S)$xy{Dm} - \overset{˙}{\varphi}$_(S)$yz{Dm = B},$

$\overset{˙}{\psi}\ $_(S)$\left( y^{2} + z^{2}\, \right){Dm} - \overset{˙}{\omega}$_(S)$xy{Dm} - \overset{˙}{\varphi}$_(S)$xz{Dm = A},$

par lesquelles on pourra déterminer les vitesses des rotations initiales $\psi,\,\omega,\,\varphi,$ produites par les impulsions $X,\, Y,\, Z$ appliquées à des points quelconques du corps et dont les moments par rapport aux axes des $x,\, y,\, z$ sont ${A,\, B,\, C}.$

Comme les vitesses de rotation sont proportionnelles aux angles infiniment petits décrits en même temps par les rotations respectives, il s’ensuit de ce qu’on a démontré dans la première Partie (sect. III, art. 11) que les trois vitesses $\overset{˙}{\psi},\,\overset{˙}{\omega},\,\overset{˙}{\varphi}$ se composent en une seule vitesse $\overset{˙}{\theta}$ telle que

$\overset{˙}{\theta} = \sqrt{\overset{˙}{\psi^{2}} + \overset{˙}{\omega^{2}} + \overset{˙}{\varphi^{2}}},$

avec laquelle le corps tournera réellement autour d’un axe *instantané*, faisant, avec les axes des $x,\, y,\, z,$ des angles $\lambda,\mu,\nu,$ tels que

$\cos\lambda = \frac{\overset{˙}{\psi}}{\overset{˙}{\theta}},\qquad\cos\mu = \frac{\overset{˙}{\omega}}{\overset{˙}{\theta}},\qquad\cos\nu = \frac{\overset{˙}{\varphi}}{\overset{˙}{\theta}}.$

Ainsi les trois équations précédentes donneront la position de l’axe autour duquel le corps tournera dans le premier instant, et la vitesse de rotation autour de cet axe. C’est celui qu’on appelle *axe spontané de rotation*.

18\. Dans les instants suivants, le corps continuera à tourner par sa force d’inertie, et les trois équations qu’on vient de trouver auront encore lieu, en regardant comme constants les termes qui contiennent les forces d’impulsion ${X,\, Y,\, Z},$ comme on l’a vu dans l’article 16 ; mais les quantités _(S)$\left( x^{2} + y^{2} \right){Dm},$ _(S)$xy{Dm},\ldots$ deviendront variables à raison de la variation des coordonnées $x,\, y,\, z$ pendant la rotation.

Mais une conséquence remarquable qu’on tire de ces équations, c’est que, dans un instant quelconque, le corps a le même mouvement de rotation qu’il recevrait dans cet instant par l’impulsion des mêmes forces qui l’ont mis d’abord en mouvement, si ces forces lui étaient appliquées de manière à produire les mêmes moments autour des axes des $x,\, y,\, z.$

Et comme ces équations ne sont que les équations générales de l’article 16 pour un système quelconque de corps, appliquées à un corps solide de figure quelconque, il s’ensuit que, si le système qui a reçu des impulsions primitives devient, par l’action mutuelle et successive des corps, un système invariable ou un solide quelconque, les mêmes équations auront encore lieu ; de sorte que le solide aura à chaque instant le même mouvement de rotation qu’il recevrait par les mêmes impulsions primitives, si elles lui étaient appliquées immédiatement de manière à produire les mêmes moments.

Donc aussi une masse fluide, agitée primitivement par des forces quelconques, abandonnée ensuite à elle-même et devenue solide par l’attraction mutuelle de ses parties, aura, à chaque instant, le même mouvement de rotation que les forces primitives lui imprimeraient si elles agissaient de la même manière sur la masse solide.

19\. Les trois équations de l’article 17 donneront les valeurs des moments $A,\, B,\, C$ de toutes les forces primitives, en connaissant la position instantanée du corps et ses trois vitesses de rotation $\overset{˙}{\psi},\,\overset{˙}{\omega},\,\overset{˙}{\varphi}$ par rapport aux axes fixes des $x,\, y,\, z,$ ou la vitesse composée $\overset{˙}{\theta}$ autour de l’axe instantané, avec les angles $\lambda,\mu,\nu$ de cet axe avec les axes fixes des $x,\, y,\, z\,;$ et réciproquement, ayant ces moments, on peut en déduire les valeurs des vitesses de rotation.

On voit aussi par ces équations que les moments seront nuls si les vitesses sont nulles ; mais, les moments étant supposés nuls, il ne s’ensuit pas évidemment que les vitesses de rotation doivent être nulles. Car, en faisant

$A = 0,\qquad B = 0,\qquad C = 0,$

on a trois équations linéaires entre $\overset{˙}{\psi},\,\overset{˙}{\omega},\,\overset{˙}{\varphi}$ et il faudrait prouver que ces trois équations ne peuvent pas subsister ensemble, à moins de supposer $\overset{˙}{\psi} = 0,\,\overset{˙}{\omega} = 0,\,\overset{˙}{\varphi} = 0.$

En éliminant deux de ces inconnues, on a une équation qui donne la troisième inconnue nulle ou arbitraire, mais avec la condition

_(S)$\left( x^{2} + y^{2} \right){Dm} \times$_(S)$\left( x^{2} + z^{2} \right){Dm} \times$_(S)$\left( y^{2} + z^{2} \right){Dm}$

$= +$_(S)$\left( x^{2} + y^{2} \right){Dm} \times ($_(S)$xy\,{Dm})^{2} +$_(S)$\left( x^{2} + z^{2} \right){Dm} \times ($_(S)$xz\,{Dm})^{2}$

$+$_(S)$\left( y^{2} + z^{2} \right){Dm} \times ($_(S)$yz\,{Dm})^{2} + 2$_(S)$xy\,{Dm} \times$_(S)$xz\,{Dm} \times$_(S)$yz\,{Dm}\,;$

et il faudrait prouver que cette condition est impossible à remplir, ce qui paraît très difficile^([\[2\]](#cite_note-2)). Mais nous démontrerons plus bas (art. 31) que, lorsque les moments sont nuls, toute rotation s’évanouit aussi.

D’où nous pouvons d’abord conclure qu’il est impossible qu’un système de points isolés ou une masse fluide quelconque puisse former un corps solide qui ait un mouvement de rotation, à moins que les impulsions primitives n’aient été telles qu’il en soit résulté un moment par rapport à l’axe de cette rotation.

20\. Par les transformations exposées dans l’article 10, on peut changer les trois équations de l’article 17 en des équations semblables dans lesquelles les quantités $x,\, y,\, z,$ $A,\, B,\, C$ soient remplacées par les quantités analogues $x^{\prime},\, y^{\prime},\, z^{\prime},$ ${A^{\prime},\, B^{\prime},\, C^{\prime}}.$

Désignons par $\overset{˙}{\psi^{\prime}},\overset{˙}{\omega^{\prime}},\overset{˙}{\varphi^{\prime}}$ les vitesses de rotation par rapport aux nouveaux axes des $x^{\prime},\, y^{\prime},\, z^{\prime}\,;$ on aura aussi

$\begin{matrix}
{dx^{\prime} =} & {{\overset{˙}{x}}^{\prime}dt = (z^{\prime}\overset{˙}{\omega^{\prime}} - y^{\prime}\overset{˙}{\varphi^{\prime}})dt,} \\
{dy^{\prime} =} & {{\overset{˙}{y}}^{\prime}dt = (x^{\prime}\overset{˙}{\varphi^{\prime}} - z^{\prime}\overset{˙}{\psi^{\prime}})dt,} \\
{dz^{\prime} =} & {{\overset{˙}{z}}^{\prime}dt = (y^{\prime}\overset{˙}{\psi^{\prime}} - x^{\prime}\overset{˙}{\omega^{\prime}})dt\,;}
\end{matrix}$

et les trois premières équations de l’article 10 deviendront, par ces substitutions, en changeant $m$ en ${Dm},$

$\overset{˙}{\varphi^{\prime}}$_(S)$\left( x'^{2} + y'^{2} \right){Dm} - \overset{˙}{\psi^{\prime}}$_(S)$x^{\prime}z^{\prime}{Dm} - \overset{˙}{\omega^{\prime}}$_(S)$y^{\prime}z^{\prime}{Dm = C^{\prime}},$

$\overset{˙}{\omega^{\prime}}$_(S)$\left( z'^{2} + x'^{2} \right){Dm} - \overset{˙}{\psi^{\prime}}$_(S)$x^{\prime}y^{\prime}{Dm} - \overset{˙}{\varphi^{\prime}}$_(S)$y^{\prime}z^{\prime}{Dm = B^{\prime}},$

$\overset{˙}{\psi^{\prime}}$_(S)$\left( y'^{2} + z'^{2} \right){Dm} - \overset{˙}{\omega^{\prime}}$_(S)$x^{\prime}y^{\prime}{Dm} - \overset{˙}{\varphi^{\prime}}$_(S)$x^{\prime}z^{\prime}{Dm = A^{\prime}},$

dans lesquelles on aura, par le même article,

$\begin{matrix}
 & {{A^{\prime} = A\alpha + B\alpha^{\prime} + C\alpha^{''}},} \\
 & {{B^{\prime} = A\beta\, + B\beta^{\prime} + C\beta^{''}},} \\
 & {{C^{\prime} = A\gamma\  + B\gamma^{\prime} + C\gamma^{''}}.}
\end{matrix}$

Ces équations ont l’avantage que la position des axes de rotation y est entièrement arbitraire, puisqu’elle ne dépend que des quantités $\alpha,\,\beta,\,\gamma,\,\alpha^{\prime},\ldots\,;$ et, comme elles ne sont que du premier ordre, rien n’empêche de donner à ces axes une position différente d’un instant à l’autre et de les prendre de manière qu’ils soient fixes dans l’intérieur du corps et, par conséquent, mobiles avec lui dans l’espace. Alors les quantités _(S)$\left( x'^{2} + y'^{2} \right){Dm},$ _(S)$x^{\prime}y^{\prime}{Dm}\ldots$ deviendront constantes ; mais les quantités $A^{\prime},\, B^{\prime},\, C^{\prime}$ seront variables, à cause de la variabilité des quantités $\alpha,\beta,\gamma,$ $\alpha^{\prime},\ldots.$ Nous donnerons dans la suite des moyens directs de parvenir à ces équations, qui sont d’une grande utilité dans le problème de la rotation des corps.

21\. On a vu dans l’article 16 que les constantes $A,\, B,\, C$ expriment les sommes des moments des impulsions primitives données aux corps, relativement aux axes des $x,\, y,\, z.$ Or il est facile de prouver que les quantités $\alpha,\alpha^{\prime},\alpha^{''}$ représentent les cosinus des angles que l’axe des $x^{\prime}$ fait avec les axes des $x,\, y,\, z\,;$ que les quantités $\beta,\,\beta^{\prime},\,\beta^{''}$ représentent les cosinus des angles que l’axe des $y^{\prime}$ fait avec les mêmes axes des $x,\, y,\, z,$ et que les quantités $\gamma,\gamma^{\prime},\gamma^{''}$ représentent les cosinus des angles que l’axe des $z^{\prime}$ fait avec ces mêmes axes. Donc, par ce qu’on a démontré dans la première Partie sur la composition des moments (sect. III, art. 16), les trois quantités $A^{\prime},\, B^{\prime},\, C^{\prime}$ seront les moments des mêmes impulsions rapportés aux axes des $x^{\prime},\, y^{\prime},\, z^{\prime},$ c’est-à-dire aux axes de rotation fixes dans le corps et mobiles dans l’espace. Ainsi l’on pourra appliquer à ces axes les mêmes conclusions qu’on a trouvées dans l’article 19.

§ IV. — *Propriétés des axes fixes de rotation d’un corps libre
de figure quelconque*.

22\. Nous réservons pour un Chapitre particulier la solution complète du problème général de la rotation d’un corps solide de figure quelconque ; nous allons seulement examiner ici le cas où l’axe instantané de rotation demeure immobile dans l’espace, ou au moins toujours parallèle à lui-même lorsque le corps a un mouvement progressif, parce que ce cas se résout facilement par les formules du paragraphe précédent et qu’il conduit aux belles propriétés des axes qu’on nomme *principaux*, ou *axes naturels de rotation*.

Reprenons les équations fondamentales de l’article 17 ; faisons, pour abréger,

$l =$_(S)$x^{2}{Dm},\qquad m =$_(S)$y^{2}{Dm},\qquad n =$_(S)$z^{2}{Dm},$

$f =$_(S)$yz{Dm},\qquad\; g =$_(S)$xz{Dm},\qquad h =$_(S)$xy{Dm},$

et substituons pour $\overset{˙}{\psi},\,\overset{˙}{\omega},\,\overset{˙}{\varphi}$ leurs valeurs $\overset{˙}{\theta}\cos\lambda,\,\overset{˙}{\theta}\cos\mu,\,\overset{˙}{\theta}\cos\nu,$ $\overset{˙}{\theta}$ étant la vitesse de rotation autour de l’axe instantané qui fait les angles $\lambda,\,\mu,\,\nu$ avec les axes fixes des $x,\, y,\, z\,;$ ces équations deviendront ainsi, en les divisant par $\overset{˙}{\theta},$

$\begin{matrix}
 & {(m} & + & {n)} & {\cos\lambda -} & {h\cos\mu -} & {g\cos\nu =} & {\frac{A}{\overset{˙}{\theta}},} \\
 & {(l} & + & {n)} & {\cos\mu -} & {h\cos\lambda -} & {f\cos\nu =} & {\frac{B}{\overset{˙}{\theta}},} \\
 & {(l} & + & {m)} & {\cos\nu -} & {g\cos\lambda -} & {f\cos\mu =} & {\frac{C}{\overset{˙}{\theta}}.}
\end{matrix}$

23\. Les six quantités $l,\, m,\, n,\, f,\, g,\, h$ sont variables ; en les différentiant, substituant pour $dx,\, dy,\, dz,$ les quantités $\overset{˙}{x}dt,\overset{˙}{y}dt,\overset{˙}{z}dt,$ et ensuite pour $\overset{˙}{x},\,\overset{˙}{y},\,\overset{˙}{z}$ leurs valeurs (article cité), on aura

$\begin{matrix}
{dl\ \  =} & {2(g\cos\mu - h\cos\nu)\overset{˙}{\theta}dt,} \\
{dm =} & {2(h\cos\nu - f\cos\lambda)\overset{˙}{\theta}dt,} \\
{dn\  =} & {2(f\cos\lambda - g\cos\mu)\overset{˙}{\theta}dt,} \\
{df\; =} & {\left\lbrack (m - n\ )\cos\lambda + g\cos\nu - h\cos\mu \right\rbrack\overset{˙}{\theta}dt,} \\
{dg\; =} & {\left\lbrack (n\; - l\ \ )\cos\mu + h\cos\lambda - f\cos\nu \right\rbrack\overset{˙}{\theta}dt,} \\
{dh\  =} & {\left\lbrack (l\ \; - m)\cos\nu + f\cos\mu - g\cos\lambda \right\rbrack\overset{˙}{\theta}dt.}
\end{matrix}$

Ces six équations, jointes aux trois de l’article précédent, renferment la solution générale ; mais nous ne considérons ici que le cas où les angles $\lambda,\,\mu,\,\nu$ demeurent invariables, et il s’agit de voir sous quelles conditions ces quantités peuvent être constantes.

24\. Pour cela, il n’y a qu’à différentier les trois premières équations dans cette supposition, et y substituer les valeurs des différentielles $dl,$ $dm,\ldots\,;$ on aura, après avoir divisé par $\overset{˙}{\theta}dt,$ ces trois-ci :

$\begin{matrix}
{f\left( \cos^{2}\nu - \cos^{2}\mu \right) - g\cos\lambda\cos\mu + h\cos\lambda\cos\nu} & \\
{+ (m - n)\cos\mu\cos\nu} & {= - \frac{A}{\overset{˙}{\theta}\,\!^{2}}\frac{d\overset{˙}{\theta}}{dt},} \\
{f\cos\lambda\cos\mu + g\left( \cos^{2}\lambda - \cos^{2}\nu \right) - h\cos\mu\cos\nu} & \\
{+ (n - l\ \ )\cos\lambda\cos\nu} & {= - \frac{B}{\overset{˙}{\theta}\,\!^{3}}\frac{d\overset{˙}{\theta}}{dt},} \\
{- f\cos\lambda\cos\nu + g\cos\mu\cos\nu + h\left( \cos^{2}\mu - \cos^{2}\lambda \right)} & \\
{+ (l\, - m)\cos\lambda\cos\mu} & {= - \frac{C}{\overset{˙}{\theta}\,\!^{3}}\frac{d\overset{˙}{\theta}}{dt}.}
\end{matrix}$

Si l’on ajoute ces trois équations ensemble, après, avoir multiplié la première par $\cos\lambda,$ la deuxième par $\cos\mu,$ la troisième par $\cos\nu,$ on a l’équation

$\frac{A\cos\lambda + B\cos\mu + C\cos\nu}{{\overset{˙}{\theta}}^{3}}\frac{d\overset{˙}{\theta}}{dt} = 0,$

laquelle donne

$d\overset{˙}{\theta} = 0,$

ou bien

${A\cos\lambda + B\cos\mu + C\cos\nu} = 0.$

Nous verrons plus bas (art. 38) que la quantité

${A\overset{˙}{\psi} + B\overset{˙}{\omega} + C\overset{˙}{\varphi}},$

qui est la même chose que

$({A\cos\lambda + B\cos\mu + C\cos\nu})\overset{˙}{\theta},$

exprime la force vive du corps, laquelle ne peut jamais être nulle tant que le corps est en mouvement.

Il faut donc supposer en général

$d\overset{˙}{\theta} = 0,$

et, par conséquent, la vitesse de rotation $\overset{˙}{\theta}$ constante. Alors les trois équations ci-dessus se réduisent à deux, qui donnent les rapports des $\cos\lambda,\,\cos\mu,$ $\cos\nu\,;$ et, comme on a

$\cos^{2}\lambda + \cos^{2}\mu + \cos^{2}\nu = 1,$

ces rapports suffiront pour déterminer les trois cosinus.

25\. Supposons

$s = \frac{\cos\mu}{\cos\lambda},\qquad u = \frac{\cos\nu}{\cos\lambda}\,;$

les trois équations précédentes deviendront, à cause de $d\overset{˙}{\theta} = 0,$

$\begin{matrix}
 & {f\left( u^{2} - s^{2} \right)} & - & {gs} & + & {hu} & + & {(m} & - & n & ) & {su} & = & {0,} \\
 & {g\left( 1\ \; - u^{2} \right)} & - & {hsu} & + & {fs} & + & {(n} & - & l & ) & u & = & {0,} \\
 & {h\left( s^{2}\, - 1 \right)} & + & {gsu} & - & {fu} & + & {(l} & - & m & ) & s & = & 0.
\end{matrix}$

La dernière donne

$u = \frac{h\left( s^{2} - 1 \right) + (l - m)s}{f - gs}\,;$

cette valeur étant substituée dans la première ou dans la seconde, ou plutôt dans la somme de ces deux, après avoir multiplié l’une par $g$ et l’autre par $f,$ pour en chasser le terme en $u^{2},$ on a

$\left\lbrack gh(m - n) + f\left( g^{2} - h^{2} \right) \right\rbrack s^{2}$

$\begin{matrix}
{+ \left\lbrack g(l - m)(m - n) + fh(n - 2l + m) + g\left( g^{2} + h^{2} - f^{2} \right) \right\rbrack s^{2}} & \\
{+ \left\lbrack f(l - m)(m - n) + gh(n - 2m + l) + f\left( f^{2} + h^{2} - g^{2} \right) \right\rbrack s\ \ } & \\
{+ fh(l - n) + g\left( f^{2} - h^{2} \right)} & {= 0.}
\end{matrix}$

Cette équation, étant du troisième degré, aura nécessairement une racine réelle ; ainsi l’on aura une valeur de $s$ et une valeur correspondante de $u,$ par le moyen desquelles on pourra déterminer la position d’un axe invariable et de rotation uniforme. Mais, comme cette détermination dépend des quantités $l,\, m,$ $n,\, f,\, g,\, h$ qui varient avec le temps $t,$ il faut encore prouver que la variabilité de ces quantités n’influe point sur la valeur des deux quantités $s$ et $u.$

26\. Pour y parvenir, nommons $P,\, Q,\, R$ les premiers membres des trois équations de l’article 22 ; les premiers membres des équations de l’article 24 seront $\frac{dP}{\overset{˙}{\theta}dt},\,\frac{dQ}{\overset{˙}{\theta}dt},\,\frac{dR}{\overset{˙}{\theta}dt},$ en y mettant pour $dl,\, dm,\ldots$ leurs valeurs. Or il est facile de voir qu’on a, par la substitution de ces mêmes valeurs,

$\begin{matrix}
{dP =} & {(R\cos\mu - Q\cos\nu)\overset{˙}{\theta}dt,} \\
{dQ =} & {(P\cos\nu - R\cos\lambda)\overset{˙}{\theta}dt,} \\
{dR =} & {(Q\cos\lambda - P\cos\mu)\overset{˙}{\theta}dt.}
\end{matrix}$

D’après ces équations, dans lesquelles $\lambda,\,\mu,\,\nu$ et $\overset{˙}{\theta}$ sont des quantités constantes, il est facile de voir que, si les valeurs de $\frac{dP}{dt},\,\frac{dQ}{dt},\,\frac{dR}{dt}$ sont nulles lorsque $t$ est nul ou égal à une quantité quelconque donnée, celles de $\frac{d^{2}P}{dt^{2}},\,\frac{d^{2}Q}{dt^{2}},\,\frac{d^{2}R}{dt^{2}},$ de $\frac{d^{3}P}{dt^{3}},\frac{d^{3}Q}{dt^{3}},\frac{d^{3}R}{dt^{3}},$ et ainsi de suite à l’infini, seront aussi nulles pour la même valeur de $t.$

Or on sait, par le théorème de Taylor, que la valeur d’une fonction $\frac{dP}{dt}$ de $t,$ lorsque $t$ devient $t + t^{\prime},$ devient en même temps

$\frac{dP}{dt} + \frac{d^{2}P}{dt^{2}}t^{\prime} + \frac{1}{2}\frac{d^{3}P}{dt^{3}}t'^{2} + \frac{1}{2.3}\frac{d^{4}P}{dt^{4}}t'^{3} + \ldots.$

Donc, si $\frac{dP}{dt}$ est nul lorsque l’on a $t^{\prime} = 0,$ on aura toujours

$\frac{dP}{dt} = 0,$

quel que soit $t^{\prime}.$ Et la même chose aura lieu pour les valeurs de $\frac{dQ}{dt}$ et $\frac{dR}{dt}.$

Il s’ensuit de là que, si les équations de l’article 25, qui ne sont que les transformées des équations $\frac{dP}{dt} = 0,\,\frac{dQ}{dt} = 0,\,\frac{dR}{dt} = 0,$ ont lieu dans un instant quelconque, elles auront lieu, quel que soit le temps $t,$ dans l’hypothèse des quantités $s$ et $u$ constantes. Par conséquent, les valeurs de ces quantités seront indépendantes de la variabilité des quantités $l,\, m,\, n,\, f,\, g,\, h\,;$ de sorte qu’il suffira de déterminer les valeurs de ces dernières quantités pour une position quelconque du corps à l’égard des axes fixes des $x,\, y,\, z,$ pour avoir celles des quantités $s$ et $u$ qui déterminent la position de l’axe de rotation, lequel doit demeurer immobile dans l’espace ou du moins toujours parallèle à lui-même si le corps a un mouvement progressif.

Et comme cet axe, par sa nature, est fixe dans l’intérieur du corps pendant un instant, puisque le corps est censé tourner autour de lui, il s’ensuit qu’il y doit toujours demeurer fixe ; car il est évident que si, dans l’instant suivant, il changeait de place dans le corps, il changerait nécessairement de place dans l’espace, ce qui est contre l’hypothèse.

27\. Ayant trouvé la position de cet axe dans l’espace, rien n’empêche de supposer qu’il coïncide avec l’axe des $x,$ dont la position est arbitraire.

On pourra ainsi supposer $\lambda = 0$ et, par conséquent, $\cos\lambda = 1,$ ce qui donnera

$s = 0,\qquad u = 0.$

De là on trouve, par les équations de l’article 25,

$g = 0,\qquad h = 0.$

Ainsi cet axe a la propriété qu’en le prenant pour l’axe des $x,$ les valeurs des deux intégrales _(S)$xy\,{Dm},$ _(S)$xz\,{Dm}$ (art. 22) deviennent nulles.

Supposons maintenant dans nos formules

$g = 0,\qquad h = 0,$

et désignons par $f^{\prime},\, l^{\prime},\, m^{\prime},\, n^{\prime}$ ce que deviennent les quantités $f,\, l,\, m,\, n$ dans ce cas. Cette supposition donne d’abord

$s = 0,\qquad u = 0\,;$

c’est le cas précédent. Ensuite elle donne aussi $s$ et $u$ infinis et, par conséquent,

$\cos\lambda = 0,\qquad\lambda = 90^{\circ}\,;$

cette valeur répond aux deux autres racines de l’équation en $s$ du troisième degré et, par conséquent, à la position des deux autres axes. Or la première des équations en $s$ et $u$ (art. 25) devient, lorsque $g$ et $h$ sont nuls,

$f^{\prime}\left( u^{2} - s^{2} \right) + (m^{\prime} - n^{\prime})su = 0,$

et, substituant pour $s$ et $u$ leurs valeurs,

$f^{\prime}(cos^{2}\nu - \cos^{2}\mu) + (m^{\prime} - n^{\prime})\cos\mu\cos\nu = 0\,;$

mais, en faisant $\cos\lambda = 0$ dans

$\cos^{2}\lambda + \cos^{2}\mu + \cos^{2}\nu = 1,$

on a

$\cos\nu = \sqrt{1 - \cos^{2}\mu} = \sin\mu\,;$

et l’équation précédente se réduit à celle-ci

${tang}2\mu = \frac{2f^{\prime}}{m^{\prime} - n^{\prime}},$

laquelle donne pour l’angle $\mu$ deux valeurs dont l’une surpasse l’autre de $90^{\circ}.$

Ainsi, ayant pris l’axe des $x$ dans le premier axe de rotation, les deux autres axes de rotation uniforme seront dans le plan des $yz$ et feront avec l’axe des $y$ les angles $\mu$ et $\mu + 90^{\circ},$ de manière que les trois axes de rotation seront rectangulaires entre eux, comme ceux des coordonnées. On pourra donc prendre aussi ces deux derniers axes pour ceux des $y$ et des $z\,;$ on aura alors

$\mu = 0$

et, par conséquent,

$f^{\prime} = 0\,;$

de sorte que la valeur de l’intégrale _(S)$yz\,{Dm}$ sera aussi nulle.

28\. Il existe donc, pour chaque corps solide, quelles que soient sa figure et sa constitution, et par rapport à un point quelconque du corps, trois axes rectangulaires, qui se coupent dans ce point, autour desquels le corps peut tourner librement et uniformément ; et ces trois axes sont déterminés par les conditions suivantes

_(S)$xy\,{Dm} = 0,\qquad$_(S)$xz\,{Dm} = 0,\qquad$_(S)$yz\,{Dm} = 0,$

en prenant ces axes pour ceux des coordonnées $x,\, y,\, z.$

Lorsque ces axes passent par le centre de gravité, on les nomme axes *principaux*, d’après Euler, à qui on en doit la connaissance ; on les nomme aussi *axes naturels de rotation* ou, en général, *axes principaux*, soit qu’ils passent par le centre de gravité ou non.

29\. En faisant

$f = 0,\qquad g = 0,\qquad h = 0,$

ce qui a lieu par rapport aux trois axes principaux, on a aussi, par les équations de l’article 23,

$\frac{dl}{dt} = 0,\qquad\frac{dm}{dt} = 0,\qquad\frac{dn}{dt} = 0,$

ce qui fait voir que les quantités $l,\, m,\, n$ sont alors les plus grandes ou les plus petites. Pour pouvoir distinguer les maxima et les minima, il n’y aura qu’à chercher les valeurs de $\frac{d^{2}l}{dt^{2}},\,\frac{d^{2}m}{dt^{2}},\,\frac{d^{2}n}{dt^{2}}\,;$ et l’on trouvera, à cause de $\overset{˙}{\theta}$ constante,

$\begin{matrix}
{\frac{d^{2}l}{dt^{2}}\ \  =} & {2\left\lbrack (n\  - l\ \ )\cos^{2}\mu - (l\ \  - m)\cos^{2}\nu \right\rbrack\overset{˙}{\theta}\,\!^{2},} \\
{\frac{d^{2}m}{dt^{2}} =} & {2\left\lbrack (l\ \  - m)\cos^{2}\nu - (m - n\ )\cos^{2}\lambda \right\rbrack\overset{˙}{\theta}\,\!^{2},} \\
{\frac{d^{2}n}{dt^{2}}\  =} & {2\left\lbrack (m - n\ )\cos^{2}\lambda - (n\  - l\ \ )\cos^{2}\mu \right\rbrack\overset{˙}{\theta}\,\!^{2}.}
\end{matrix}$

Donc, si $l > m,\, m > n,$ la valeur de $\frac{d^{2}l}{dt^{2}}$ sera toujours négative, celle de $\frac{d^{2}n}{dt^{2}}$ toujours positive, et celle de $\frac{d^{2}m}{dt^{2}}$ pourra être positive ou négative par conséquent, $l$ sera toujours un maximum, $n$ un minimum, et $m$ ne sera ni l’un ni l’autre. On voit aussi que $\frac{d^{2}l}{dt^{2}} + \frac{d^{2}m}{dt^{2}}$ aura toujours une valeur négative, et $\frac{d^{2}m}{dt^{2}} + \frac{d^{2}n}{dt^{2}}$ aura toujours une valeur positive ; de sorte que la quantité $l + m$ sera toujours un maximum, et $m + n$ un minimum.

Les quantités $l + m,\, l + n,\, m + n,$ qui expriment les sommes des produits de chaque molécule du corps par le carré de sa distance aux trois axes des $z,\, y,\, x,$ se nomment, d’après Euler, *moments d’inertie* du corps relativement à ces axes ; ils sont pour le mouvement de rotation ce que les simples masses sont pour le mouvement progressif, puisque c’est par ces moments qu’il faut diviser les moments des forces d’impulsion pour avoir les vitesses de rotation autour des mêmes axes.

C’est par la considération des plus grands et des plus petits moments d’inertie qu’Euler a trouvé les axes principaux ; maintenant, on les détermine ordinairement par les trois conditions

_(S)$xy\,{Dm} = 0,\qquad$_(S)$xz\,{Dm} = 0,\qquad$_(S)$yz\,{Dm} = 0.$

30\. Puisqu’on est assuré, par l’analyse de l’article 27, que l’équation en $s$ (art. 25) a ses trois racines réelles, il sera toujours facile de les trouver en comparant cette équation, dégagée de son second terme, avec l’équation connue

$x^{3} - 3r^{2}x - 2r^{2}\cos\varphi = 0,$

dont les trois racines sont

$2r\cos\frac{\varphi}{3},\qquad - 2r\cos\left( 60^{\circ} + \frac{\varphi}{3} \right),\qquad - 2r\cos\left( 60^{\circ} - \frac{\varphi}{3} \right).$

On aura ainsi les trois valeurs de $s,$ que nous désignerons par $s,\, s^{\prime},\, s^{''},$ et les valeurs correspondantes $u,\, u^{\prime},\, u^{''}.$ Et, si l’on désigne de même par $\lambda,\,\lambda^{\prime},\,\lambda^{''}$ les angles que les trois axes principaux font avec l’axe des $x,$ par $\mu,\,\mu^{\prime},\,\mu^{''}$ les angles qu’ils font avec l’axe des $y,$ et par $\nu,\,\nu^{\prime},\,\nu^{''}$ ceux que ces mêmes axes font avec l’axe des $z,$ on aura, par les articles 24 et 25,

$\begin{matrix}
{\cos\lambda =} & {\frac{1}{\sqrt{1 + s^{2} + u^{2}}},} \\
{\cos\mu =} & {\frac{s}{\sqrt{1 + s^{2} + u^{2}}},} \\
{\cos\nu =} & {\frac{u}{\sqrt{1 + s^{2} + u^{2}}},}
\end{matrix}$

et l’on aura des expressions semblables en marquant les lettres, $\lambda,\,\mu,\,\nu,\, s,\, u$ d’un trait ou de deux. Ainsi la détermination des trois axes principaux pourra toujours s’effectuer par ces formules dans tout corps solide de figure quelconque, homogène ou non, pourvu que l’on connaisse les valeurs des quantités $f,\, g,\, h,\, l,\, m,\, n$ pour une position quelconque donnée du corps, relativement aux axes fixes des $x,\, y,\, z.$

En substituant ces valeurs de $\cos\lambda,\,\cos\mu,\,\cos\nu$ dans les trois équations de l’article 22, on aura les valeurs des moments $A,\, B,\, C$ qui seront nécessaires pour faire tourner le corps, avec une vitesse constante donnée $\overset{˙}{\theta},$ autour d’un axe fixe dans l’espace, dont la position sera donnée par les mêmes angles $\lambda,\,\mu,\,\nu$ et qui sera en même temps un des trois axes principaux du corps, selon qu’on prendra pour $s$ et $u$ l’une des trois racines de l’équation en $s.$

31\. Comme ces trois axes sont toujours perpendiculaires entre eux, on pourra les prendre pour les axes des $x^{\prime},\, y^{\prime},\, z^{\prime}$ dans les formules de l’article 20. On aura ainsi, par la nature de ces axes,

_(S)$x^{\prime}y^{\prime}\,{Dm} = 0,\qquad$_(S)$x^{\prime}z^{\prime}\,{Dm} = 0,\qquad$_(S)$y^{\prime}z^{\prime}\,{Dm} = 0.$

et si l’on fait

$l^{\prime} =$_(S)$x'^{2}\,{Dm} = 0,\quad m^{\prime} =$_(S)$y'^{2}\,{Dm} = 0,\quad n^{\prime} =$_(S)$z'^{2}\,{Dm} = 0,$

les trois équations de l’article cité prendront cette forme très simple

$\begin{matrix}
{(m^{\prime} + n^{\prime}\ )\overset{˙}{\psi}\,\!^{\prime} =} & {A^{\prime},} \\
{(l^{\prime}\ \  + m^{\prime})\overset{˙}{\omega}\,\!^{\prime} =} & {B^{\prime},} \\
{(l^{\prime}\ \  + n^{\prime}\ )\overset{˙}{\varphi}\,\!^{\prime} =} & {C^{\prime},} \\
 &
\end{matrix}$

par lesquelles on a tout de suite les vitesses de rotation $\overset{˙}{\psi}\,\!^{\prime},\,\overset{˙}{\omega}\,\!^{\prime},\,\overset{˙}{\varphi}\,\!^{\prime}$ autour des trois axes principaux.

C’est ici le lieu de démontrer la proposition que nous avons indiquée dans l’article 19. En effet, en faisant

$A = 0,\qquad B = 0,\qquad C = 0,$

on aura aussi (art. 20)

$A^{\prime} = 0,\qquad B^{\prime} = 0,\qquad C^{\prime} = 0\,;$

donc les équations précédentes donneront

$\overset{˙}{\psi}\,\!^{\prime} = 0,\qquad\overset{˙}{\omega}\,\!^{\prime} = 0,\qquad\overset{˙}{\varphi}\,\!^{\prime} = 0,$

puisque les quantités $l,\, m,\, n$ ne peuvent jamais être nulles pour un corps de trois dimensions. D’où l’on doit conclure qu’il ne peut y avoir de mouvement de rotation si les moments primitifs sont nuls.

Quand, parmi les trois moments ${A^{\prime},\, B^{\prime},\, C^{\prime}},$ deux sont nuls, comme $B^{\prime}$ et $C^{\prime},$ ce qui a lieu lorsque l’impulsion se fait dans le plan des $y^{\prime}z^{\prime},$ les deux vitesses de rotation $\overset{˙}{\omega},\,\overset{˙}{\varphi}$ seront aussi nulles et le corps tournera autour de l’axe principal des $x^{\prime}$ avec la vitesse $\overset{˙}{\psi}\,\!^{\prime}.$ Or, par les formules de l’article 20, on a

${A'^{2} + B'^{2} + C'^{2} = A^{2} + B^{2} + C^{2}},$

à cause des équations de condition entre les quantités $\alpha,\beta,\gamma,\alpha^{\prime},\ldots\,;$ donc, faisant

$B^{\prime} = 0,\qquad C^{\prime} = 0,$

on aura

${A^{\prime} = \sqrt{A^{2} + B^{2} + C^{2}}},$

et, par conséquent, $A^{\prime}$ sera constant ; donc, par la première équation, la vitesse $\overset{˙}{\psi}\,\!^{\prime}$ sera aussi constante.

32\. À l’égard des valeurs de $l^{\prime},\, m^{\prime},\, n^{\prime},$ il sera facile de les déduire de celles de $l,\, m,\, n,\, f,\, g,\, h\,;$ car les expressions de $x,\, y,\, z$ en $x^{\prime},\, y^{\prime},\, z^{\prime},$ en vertu des équations de condition (Part. I, sect. III, art. 10), donnent réciproquement

$\begin{matrix}
{x^{\prime} =} & {\alpha x + \alpha^{\prime}y + \alpha^{''}z,} \\
{y^{\prime} =} & {\beta x\, + \beta^{\prime}y + \beta^{''}z,} \\
{z^{\prime} =} & {\gamma x\  + \gamma^{\prime}y + \gamma^{''}z.}
\end{matrix}$

Or, en prenant les axes des $x^{\prime},\, y^{\prime},\, z^{\prime}$ pour les axes principaux, on voit par l’article 21 que les quantités $\alpha,\,\alpha^{\prime},\,\alpha^{''}$ sont identiques avec $\cos\lambda,\,\cos\mu,$ $\cos\nu,$ que, pareillement $\beta,\,\beta^{\prime},\,\beta^{''}$ seront identiques avec $\cos\lambda^{\prime},\,\cos\mu^{\prime},$ $\cos\nu^{\prime},$ et $\gamma,\,\gamma^{\prime},\,\gamma^{''}$ avec $\cos\lambda^{''},\,\cos\mu^{''},\,\cos\nu^{''}.$ Ainsi, en substituant les valeurs de ces cosinus données ci-dessus (art. 20), on aura

$\begin{matrix}
{x^{\prime} =} & {\frac{x + sy\ \  + uz}{\sqrt{1 + s^{2}\ \  + u^{2}}},} \\
{y^{\prime} =} & {\frac{x + s^{\prime}y\ \  + u^{\prime}z}{\sqrt{1 + s'^{2}\  + u'^{2}}},} \\
{z^{\prime} =} & {\frac{x + s^{''}y + u^{''}z}{\sqrt{1 + s^{\prime}'^{2} + u^{\prime}'^{2}}}\,;}
\end{matrix}$

d’où l’on tirera, en carrant et intégrant après avoir multiplié par ${Dm},$

$\begin{matrix}
{l^{\prime} =} & {\frac{l + s^{2}m + u^{2}n + 2sh + 2ug + 2suf}{1 + s^{2} + u^{2}},} \\
{m^{\prime} =} & {\frac{l + s'^{2}m + u'^{2}n + 2s^{\prime}h + 2u^{\prime}g + 2s^{\prime}u^{\prime}f}{1 + s'^{2} + u'^{2}},} \\
{n^{\prime} =} & {\frac{l + s^{\prime}'^{2}m + u^{\prime}'^{2}n + 2s^{''}h + 2u^{''}g + 2s^{''}u^{''}f}{1 + s^{\prime}'^{2} + u^{\prime}'^{2}},} \\
 &
\end{matrix}$

On trouve, dans la plupart des Traités de Mécanique, la détermination des axes principaux dans différents corps ; dans ceux dont la forme est symétrique, l’axe de figure est toujours un des axes principaux on peut trouver ensuite les deux autres par la formule de l’article 27.

§ V. — *Propriétés relatives aux forces vives*.

33\. En général, de quelque manière que les différents corps qui composent un système soient disposés ou liés entre eux, pourvu que cette disposition soit indépendante du temps, c’est-à-dire que les équations de condition entre les coordonnées des différents corps ne renferment point la variable $t,$ il est clair qu’on pourra toujours, dans la formule générale de la Dynamique, supposer les variations $\delta x,\,\delta y,\,\delta z$ égales aux différentielles $dx,\, dy,\, dz$ qui représentent les espaces effectifs parcourus par les corps dans l’instant $dt,$ tandis que les variations dont nous parlons doivent représenter les espaces quelconques que les corps pourraient parcourir dans le même instant, eu égard à leur disposition mutuelle.

Cette supposition n’est que particulière et ne peut fournir, par conséquent, qu’une seule équation ; mais, étant indépendante de la forme du système, elle a l’avantage de donner une équation générale pour le mouvement de quelque système que ce soit.

Substituant donc dans la formule de l’article 5 (Section précédente), à la place des variations $\delta x,\,\delta y,\,\delta z,$ les différentielles $dx,\, dy,\, dz,$ et, par conséquent aussi, les différentielles $dp,\, dq,\, dr,\ldots$ au lieu des variations $\delta p,\,\delta q,$ $\delta r,\ldots$ qui dépendent de $\delta x,\,\delta y,\,\delta z,$ on aura cette équation générale, pour quelque système de corps que ce soit,

_(S)$m\left( \frac{d^{2}x}{dt^{2}}dx + \frac{d^{2}y}{dt^{2}}dy + \frac{d^{2}z}{dt^{2}}dz + Pdp + Qdq + Rdr + \ldots \right) = 0.$

34\. Dans le cas où la quantité

$Pdp + Qdq + Rdr + \ldots$

est intégrable, lequel a lieu lorsque les forces ${P,\, Q,\, R},\ldots$ tendent à des centres fixes ou à des corps du même système et sont fonctions des distances $p,\, q,\, r,\ldots,$ en faisant

$Pdp + Qdq + Rdr + \ldots = d\Pi,$

l’équation précédente devient

_(S)$m\left( \frac{d^{2}x}{dt^{2}}dx + \frac{d^{2}y}{dt^{2}}dy + \frac{d^{2}z}{dt^{2}}dz + d\Pi \right) = 0,$

dont l’intégrale est

_(S)$m\left\lbrack \frac{1}{2}\left( \frac{d^{2}x}{dt^{2}} + \frac{d^{2}y}{dt^{2}} + \frac{d^{2}z}{dt^{2}} \right) + \Pi \right\rbrack = H,$

dans laquelle $H$ désigne une constante arbitraire, égale à la valeur du premier membre de l’équation dans un instant donné.

Cette dernière équation renferme le principe connu sous le nom de *conservation des forces vives*. En effet, $dx^{2} + dy^{2} + dz^{2}$ étant le carré de l’espace que le corps parcourt dans l’instant $dt,$

$\frac{d^{2}x}{dt^{2}} + \frac{d^{2}y}{dt^{2}} + \frac{d^{2}z}{dt^{2}}$

sera le carré de sa vitesse, et

$m\left( \frac{dx^{2}}{dt^{2}} + \frac{dy^{2}}{dt^{2}} + \frac{dz^{2}}{dt^{2}} \right)$

sa force vive. Donc

_(S)$m\left( \frac{dx^{2}}{dt^{2}} + \frac{dy^{2}}{dt^{2}} + \frac{dz^{2}}{dt^{2}} \right)$

sera la somme des forces vives de tous les corps, ou la force vive de tout le système ; et l’on voit, par l’équation dont il s’agit, que cette force vive est égale à la quantité

$2H - 2$_(S)$\Pi m,$

laquelle dépend simplement des forces accélératrices qui agissent sur les corps, et nullement de leur liaison mutuelle, de sorte que la force vive du système est à chaque instant la même que les corps auraient acquise si, étant animés par les mêmes puissances, ils s’étaient mus librement chacun sur la ligne qu’il a décrite. C’est ce qui a fait donner le nom de *conservation des forces vives* à cette propriété du mouvement.

35\. Ce principe a lieu aussi lorsqu’on rapporte les mouvements des corps à leur centre de gravité ; car, en nommant, comme ci-dessus, (art. 3) $x^{\prime},\, y^{\prime},\, z^{\prime}$ les trois coordonnées du centre de gravité, et faisant

$x = x^{\prime} + \xi,\qquad y = y^{\prime} + \eta,\qquad z = z^{\prime} + \zeta,$

les coordonnées auront leur origine dans le centre de gravité. On aura ainsi

$\frac{1}{2}$_(S)$m\left( \frac{dx^{2}}{dt^{2}} + \frac{dy^{2}}{dt^{2}} + \frac{dz^{2}}{dt^{2}} \right)$

$= \frac{1}{2}\left( \frac{dx'^{2}}{dt^{2}} + \frac{dy'^{2}}{dt^{2}} + \frac{dz'^{2}}{dt^{2}} \right)$_(S)$m + \frac{1}{2}$_(S)$m\left( \frac{d\xi^{2}}{dt^{2}} + \frac{d\eta^{2}}{dt^{2}} + \frac{d\zeta^{2}}{dt^{2}} \right)$

$+ \frac{dx^{\prime}}{dt}$_(S)$m\frac{d\xi}{dt} + \frac{dy^{\prime}}{dt}$_(S)$m\frac{d\eta}{dt} + \frac{dz^{\prime}}{dt}$_(S)$m\frac{d\zeta}{dt}.$

Par la nature du centre de gravité, on a (article cité)

_(S)$m\frac{d\xi}{dt} = 0,\qquad$_(S)$m\frac{d\eta}{dt} = 0,\qquad$_(S)$m\frac{d\zeta}{dt} = 0.$

Donc, l’équation précédente étant différentiée et retranchée de celle de l’article 33, on aura

$\frac{d^{2}x^{\prime}}{dt^{2}}dx^{\prime} + \frac{d^{2}y^{\prime}}{dt^{2}}dy^{\prime} + \frac{d^{2}z^{\prime}}{dt^{2}}dz^{\prime}$_(S)$m +$_(S)$m\left( \frac{d^{2}\xi}{dt^{2}}d\xi + \frac{d^{2}\eta}{dt^{2}}d\eta + \frac{d^{2}\zeta}{dt^{2}}d\zeta \right)$

$+$_(S)$m(Pdp + Qdq + Rdr + \ldots) = 0.$

Mettons à la place de

$Pdp + Qdq + Rdr + \ldots$

la quantité équivalente

$Xdx + Ydy + Zdz,$

et substituons pour $dx,\, dy,\, dz$ les valeurs $dx^{\prime} + d\xi,\, dy^{\prime} + d\eta,$ $dz^{\prime} + d\zeta\,;$ la dernière équation se réduira, en vertu des équations différentielles de l’article 3, à celle-ci

_(S)$m\left( \frac{d^{2}\xi}{dt^{2}}d\xi + \frac{d^{2}\eta}{dt^{2}}d\eta + \frac{d^{2}\zeta}{dt^{2}}d\zeta \right) +$_(S)$m(Xd\xi + Yd\eta + Zd\zeta) = 0.$

qui est analogue à celle de l’article 33, mais où la quantité

$Xd\xi + Yd\xi + Zd\zeta$

ne sera intégrable qu’*autant que* les forces seront dirigées vers les corps mêmes du système et proportionnelles à des fonctions des distances. Dans ce cas, on aura

$\frac{1}{2}$_(S)$m\left( \frac{d\xi^{2}}{dt^{2}} + \frac{d\eta^{2}}{dt^{2}} + \frac{d\zeta^{2}}{dt^{2}} \right) = H,$

équation qui renferme la *conservation des forces vives* par rapport au centre de gravité.

36\. Au reste, il n’en est pas du principe des *forces vives* comme de ceux du *centre de gravité* et *des aires*, qui ont lieu, quelle que soit l’action que les corps du système puissent exercer les uns sur les autres, même en se choquant, parce que toutes les forces intérieures disparaissent des équations qui renferment ces deux principes.

L’équation de la conservation des forces vives contient tous les termes dus aux forces tant extérieures qu’intérieures et n’est indépendante que de l’action des corps provenant de leur liaison mutuelle. Aussi ce principe a-t-il lieu dans le mouvement des fluides non élastiques, tant qu’ils forment une masse continue et qu’il n’y a point de choc entre leurs parties et, si la quantité de *forces vives* est la même avant et après le choc des corps élastiques, c’est qu’on suppose que les corps se sont rétablis après le choc dans le même état où ils étaient auparavant ; de sorte que les termes $\int Pdp$ de l’expression $\Pi,$ qui proviennent des forces $P$ dues au ressort des corps, et dont la valeur est la plus grande lorsque la compression est à son terme, décroissent ensuite par degrés égaux pendant la restitution et redeviennent nuls à la fin du choc. C’est uniquement dans cette hypothèse que la conservation des forces vives peut avoir lieu dans le choc des corps élastiques.

Dans tout autre cas, lorsqu’il y a des changements brusques dans les vitesses de quelques corps du système, la force vive totale se trouve diminuée de la quantité des forces vives dues aux forces accélératrices qui ont pu produire ces changements ; et cette quantité peut toujours s’estimer par la somme des masses multipliées par les carrés des vitesses que ces masses ont perdues, ou sont censées avoir perdues dans les changements brusques des vitesses réelles des corps. C’est le théorème que M. Carnot avait trouvé dans le choc des corps durs.

37\. On peut aussi, dans l’équation de l’article 11 de la Section précédente, supposer les variations $\delta x,\,\delta y,\,\delta z$ proportionnelles aux vitesses $\overset{˙}{x},\,\overset{˙}{y},\,\overset{˙}{z}$ que les corps reçoivent par l’impulsion. On aura ainsi l’équation

_(S)$\left\lbrack m\left( \overset{˙}{x}\,\!^{2} + \overset{˙}{y}\,\!^{2} + \overset{˙}{z}\,\!^{2} \right) + X\overset{˙}{x} + Y\overset{˙}{y} + Z\overset{˙}{z} \right\rbrack = 0,$

dans laquelle la partie _(S)$m\left( {\overset{˙}{x}}^{2} + {\overset{˙}{y}}^{2} + {\overset{˙}{z}}^{2} \right)$ représente la force vive de tout le système.

Cette équation, étant combinée avec les trois équations de l’article 14, donne lieu à une propriété *de maximis et minimis* relative à la ligne autour de laquelle le système tourne au premier instant, lorsqu’il a reçu une impulsion quelconque, ligne qu’on peut aussi nommer *axe de rotation spontané*.

Si l’on nomme $\alpha,\,\beta,\,\gamma$ les parties des vitesses $\overset{˙}{x},\,\overset{˙}{y},\,\overset{˙}{z}$ qui dépendent du changement de position respective des corps du système^([\[3\]](#cite_note-3)), et qu’on les ajoute à celles qui résultent des rotations (art. 17), on aura les valeurs complètes de $\overset{˙}{x},\,\overset{˙}{y},\,\overset{˙}{z},$ exprimées ainsi :

$\overset{˙}{x} = z\overset{˙}{\omega} - y\overset{˙}{\varphi} + \alpha,\qquad\overset{˙}{y} = x\overset{˙}{\varphi} - z\overset{˙}{\psi} + \beta,\qquad\overset{˙}{z} = y\overset{˙}{\psi} - x\overset{˙}{\omega} + \gamma.$

Supposons maintenant qu’on différentie ces valeurs, en ne regardant que $\overset{˙}{\psi},\,\overset{˙}{\omega},\,\overset{˙}{\varphi}$ comme variables, et qu’on dénote ces différentielles par la caractéristique $\delta$^([\[4\]](#cite_note-4)), on aura

$\delta\overset{˙}{x} = z\delta\overset{˙}{\omega} - y\delta\overset{˙}{\varphi},\qquad\delta\overset{˙}{y} = x\delta\overset{˙}{\varphi} - z\delta\overset{˙}{\psi},\qquad\delta\overset{˙}{z} = y\delta\overset{˙}{\psi} - x\delta\overset{˙}{\omega}.$

Or les trois équations de l’article 14, étant multipliées respectivement par $\delta\overset{˙}{\varphi},\,\delta\overset{˙}{\omega},\,\delta\overset{˙}{\psi}$ et ajoutées ensemble, en faisant passer sous le signe _(S) les différentielles $\delta\overset{˙}{\varphi},\,\delta\overset{˙}{\omega},\,\delta\overset{˙}{\psi}$ qui sont les mêmes pour tous les corps, donnent, par la substitution des valeurs précédentes,

_(S)$\left\lbrack m(\overset{˙}{x}\delta\overset{˙}{x} + \overset{˙}{y}\delta\overset{˙}{y} + \overset{˙}{z}\delta\overset{˙}{z}) + X\delta\overset{˙}{x} + Y\delta\overset{˙}{y} + Z\delta\overset{˙}{z} \right\rbrack = 0.$

Mais l’équation de la force vive trouvée ci-dessus, étant différentiée relativement à $\delta$^([\[5\]](#cite_note-5)), donne

_(S)$\left\lbrack 2m(\overset{˙}{x}\delta\overset{˙}{x} + \overset{˙}{y}\delta\overset{˙}{y} + \overset{˙}{z}\delta\overset{˙}{z}) + X\delta\overset{˙}{x} + Y\delta\overset{˙}{y} + Z\delta\overset{˙}{z} \right\rbrack = 0.$

Donc on a, par la comparaison de ces deux équations,

_(S)$m(\overset{˙}{x}\delta\overset{˙}{x} + \overset{˙}{y}\delta\overset{˙}{y} + \overset{˙}{z}\delta\overset{˙}{z}) = 0$

et, par conséquent,

$\delta$_(S)$m\left( \overset{˙}{x}\,\!^{2} + \overset{˙}{y}\,\!^{2} + \overset{˙}{z}\,\!^{2} \right) = 0,$

ce qui fait voir que la force vive que le système acquiert par l’impulsion est toujours un maximum ou un minimum^([\[6\]](#cite_note-6)), par rapport aux rotations relatives aux trois axes ; et, comme ces trois rotations se composent en une rotation unique autour de l’axe spontané, il s’ensuit que la position de cet axe est toujours telle que la force vive de tout le système est la plus petite ou la plus grande, par rapport à ce même axe.

Euler avait démontré cette propriété de l’axe spontané de rotation pour les corps solides d’une figure quelconque ; on voit par l’analyse précédente qu’elle est générale pour un système de corps unis entre eux d’une manière invariable ou non, lorsque ces corps reçoivent des impulsions quelconques.

38\. Lorsque le système est un corps solide qui peut tourner librement autour d’un point et qui n’est animé par aucune force accélératrice, on peut tirer de la combinaison de l’équation des *forces vives* avec celle des aires une relation digne d’être remarquée par sa simplicité, et qui ne l’avait pas encore été, que je sache, entre les vitesses de rotation $\overset{˙}{\psi},\,\overset{˙}{\omega},\,\overset{˙}{\varphi}$ par rapport aux trois axes fixes des coordonnées $x,\, y,\, z.$ Dans ce cas, on a simplement (art. 17)

$\begin{matrix}
{dx =} & {\overset{˙}{x}dt = (z\overset{˙}{\omega}\, - y\overset{˙}{\varphi})dt,} \\
{dy =} & {\overset{˙}{y}dt = (x\overset{˙}{\varphi} - z\overset{˙}{\psi})dt,} \\
{dz =} & {\overset{˙}{z}dt = (y\overset{˙}{\psi}\, - x\overset{˙}{\omega})dt.}
\end{matrix}$

Donc, si l’on ajoute ensemble les trois dernières équations de l’article 9, après les avoir multipliées par $\overset{˙}{\varphi},\overset{˙}{\omega},\overset{˙}{\psi},$ qu’on fasse passer ces quantités sous le signe _(S) et qu’on substitue $\frac{dx}{dt},\,\frac{dy}{dt},\,\frac{dz}{dt}$ à la place de leurs valeurs, on aura

_(S)$m\left( \frac{dx^{2}}{dt^{2}} + \frac{dy^{2}}{dt^{2}} + \frac{dz^{2}}{dt^{2}} \right) = A\overset{˙}{\psi} + B\overset{˙}{\omega} + C\overset{˙}{\varphi}\,;$

mais l’équation de l’article 34 donne, lorsque $\Pi = 0,$

$\frac{1}{2}$_(S)$m\left( \frac{dx^{2}}{dt^{2}} + \frac{dy^{2}}{dt^{2}} + \frac{dz^{2}}{dt^{2}} \right) = H.$

Donc on aura

$A\overset{˙}{\psi} + B\overset{˙}{\omega} + C\overset{˙}{\varphi} = 2H,$

$A,B,C$ étant les moments des forces primitives d’impulsion et $H$ étant une constante arbitraire, qui doit être nécessairement positive.

Si, dans cette équation, on substitue pour $A,\, B,\, C$ les expressions de l’article 11,

$\gamma C^{\prime},\qquad\gamma^{\prime}C^{\prime},\qquad\gamma^{''}C^{\prime},$

ou

$C^{\prime}\cos l,\qquad C^{\prime}\cos m,\qquad C^{\prime}\cos n,$

et pour $\overset{˙}{\psi},\overset{˙}{\omega},\overset{˙}{\varphi}$ celles de l’article 17,

$\overset{˙}{\theta}\cos\lambda,\qquad\overset{˙}{\theta}\cos\mu,\qquad\overset{˙}{\theta}\cos\nu,$

on aura

$\overset{˙}{\theta}(\cos l\cos\lambda + \cos m\cos\mu + \cos n\cos\nu) = \frac{2H}{C^{\prime}}.$

Dans cette formule, $l,\, m,\, n$ sont les angles que l’axe perpendiculaire au *plan invariable* fait avec les axes fixes des $x,\, y,\, z,$ et $\lambda,\,\mu,\,\nu$ sont les angles que l’axe instantané de la rotation composée, dont $\overset{˙}{\theta}$ est la vitesse, fait avec les mêmes axes ; donc, si l’on nomme $\sigma$ l’angle que l’axe instantané de rotation fait avec l’axe perpendiculaire au plan invariable, on aura, par une formule connue,

$\cos\sigma = \cos l\cos\lambda + \cos m\cos\mu + \cos n\cos\nu$

et, par conséquent,

$\overset{˙}{\theta}\cos\sigma = \frac{2H}{C^{\prime}},$

où la quantité $\frac{2H}{C^{\prime}}$ est une constante qui dépend de l’état initial ; ce qui donne un rapport, indépendant de la figure du corps, entre la vitesse réelle de rotation à chaque instant et la position de l’axe de rotation relativement au plan invariable.

Au reste, si l’on prend le plan des $xy$ de manière qu’il passe par le centre du corps et par la droite suivant laquelle se fait l’impulsion, les constantes $A$ et $B$ deviendront nulles (art. 16), et l’équation générale trouvée ci-dessus se réduira à

$C\overset{˙}{\varphi} = 2H,$

laquelle fait voir que la vitesse de rotation par rapport à l’axe des $z,$ c’est-à-dire parallèlement au plan de l’impulsion, demeure toujours la même.

§ VI. — *Propriétés relatives à la moindre action*.

39\. Nous allons maintenant considérer le quatrième principe, celui de la *moindre action*.

En nommant $u$ la vitesse de chaque corps $m$ du système, on a

$u^{2} = \frac{d^{2}x}{dt^{2}} + \frac{d^{2}y}{dt^{2}} + \frac{d^{2}z}{dt^{2}},$

et l’équation des forces vives (art. 34) devient

_(S)$m\left( \frac{u^{2}}{2} + \Pi \right) = H,$

laquelle, étant différentiée par rapport à la caractéristique $\delta,$ donne

_(S)$m(u\delta u + \delta\Pi) = 0.$

Or, $\Pi$ étant une fonction de $p,\, q,\, r,\ldots$ on a

$\delta\Pi = P\delta p + Q\delta q + R\delta r + \ldots.$

Donc

_(S)$m(P\delta p + Q\delta q + R\delta r + \ldots) = -$_(S)$mu\delta u.$

Et cette équation aura toujours lieu, pourvu que

$Pdp + Qdq + Rdr + \ldots$

soit une quantité intégrable et que la liaison des corps soit indépendante du temps ; elle cesserait d’être vraie si l’une de ces conditions n’avait pas lieu.

Qu’on substitue maintenant l’expression précédente dans la formule générale de la Dynamique (sect. II, art. 5), elle deviendra

_(S)$m\left( \frac{d^{2}x}{dt^{2}}\delta x + \frac{d^{2}y}{dt^{2}}\delta y + \frac{d^{2}z}{dt^{2}}\delta z - u\delta u \right) = 0.$

Or

$\begin{matrix}
{d^{2}x\,\delta x + d^{2}y\,\delta y + d^{2}z\,\delta z =} & {d(dx\,\delta x + dy\,\delta y + dz\,\delta z)} \\
 & {- dx\, d\,\delta x - dy\, d\,\delta y - dz\, d\,\delta z.}
\end{matrix}$

Mais, parce que les caractéristiques $d$ et $\delta$ représentent des différences ou variations tout à fait indépendantes les unes des autres, les quantités $d\delta x,\, d\delta y,\, d\delta z$ doivent être la même chose que $\delta dx,\,\delta dy,\,\delta dz.$ D’ailleurs, il est visible que

$dx\,\delta dx + dy\,\delta dy + dz\,\delta dz = \frac{1}{2}\delta\left( dx^{2} + dy^{2} + dz^{2} \right).$

Donc on aura

$d^{2}x\delta x + d^{2}y\delta y + d^{2}z\delta z = d(dx\,\delta x + dy\,\delta y + dz\,\delta z) - \frac{1}{2}\delta\left( dx^{2} + dy^{2} + dz^{2} \right).$

Soit $s$ l’espace ou l’arc décrit par le corps $m$ dans le temps $t\,;$ on aura

$ds = \sqrt{dx^{2} + dy^{2} + dz^{2}},\qquad dt = \frac{ds}{u}.$

Donc

$d^{2}x\delta x + d^{2}y\delta y + d^{2}z\delta z = d(dx\,\delta x + dy\,\delta y + dz\,\delta z) - ds\,\delta\, ds\,;$

et, de là,

$\frac{d^{2}x}{dt^{2}}\delta x + \frac{d^{2}y}{dt^{2}}\delta y + \frac{d^{2}z}{dt^{2}}\delta z = \frac{d(dx\,\delta x + dy\,\delta y + dz\,\delta z)}{dt^{2}} - u^{2}\frac{\delta\, ds}{ds}.$

Ainsi la formule générale dont il s’agit deviendra

_(S)$m\left\lbrack \frac{d(dx\,\delta x + dy\,\delta y + dz\,\delta z)}{dt^{2}} - u^{2}\frac{\delta\, ds}{ds} - u\,\delta u \right\rbrack = 0,$

ou, en multipliant tous les termes par l’élément constant $dt = \frac{ds}{u}$ et remarquant que $u\,\delta\, ds + ds\,\delta u = \delta(u\, ds),$

_(S)$m\left\lbrack \frac{d(dx\,\delta x + dy\,\delta y + dz\,\delta z)}{dt} - \delta(u\, ds) \right\rbrack = 0.$

Comme le signe intégral _(S) n’a aucun rapport aux signes différentiels $d$ et $\delta,$ on peut faire sortir ceux-ci hors de celui-là ; et l’équation précédente prendra cette forme

$d$_(S)$m\left( \frac{dx}{dt}\delta x + \frac{dy}{dt}\delta y + \frac{dz}{dt}\delta z \right) - \delta$_(S)$mu\, ds = 0.$

Intégrons par rapport au signe différentiel $d,$ et dénotons cette intégration par le signe intégral ordinaire $\int\,;$ nous aurons

_(S)$m\left( \frac{dx}{dt}\delta x + \frac{dy}{dt}\delta y + \frac{dz}{dt}\delta z \right) - \int\delta$_(S)$mu\, ds = {const}.$

Or le signe $\int,$ dans l’expression

$\int\delta$_(S)$mu\, ds,$

ne pouvant regarder que les variables $u$ et $s$ et n’ayant aucune relation avec les signes _(S) et $\delta,$ il est clair que cette expression est la même chose que celle-ci

$\delta$_(S)$m\int u\, ds\,;$

et, si l’on suppose que, dans les points où commencent les intégrales $\int u\, ds,$ on ait

$\delta x = 0,\qquad\delta y = 0,\qquad\delta z = 0,$

il faudra que la constante arbitraire soit nulle, parce que le premier membre de l’équation devient nul dans ces points. Ainsi on aura, dans ce cas,

$\delta$_(S)$m\int u\, ds =$_(S)$m\left( \frac{dx}{dt}\delta x + \frac{dy}{dt}\delta y + \frac{dz}{dt}\delta z \right).$

Donc, si l’on suppose de plus que les variations $\delta x,\,\delta y,\,\delta z$ soient aussi nulles pour les points où les intégrales $\int u\, ds$ finissent, on aura simplement

$\delta$_(S)$m\int u\, ds = 0,$

c’est-à-dire que la variation de la quantité _(S)$m\int u\, ds$ sera nulle ; par conséquent, cette quantité sera un maximum ou un minimum.

De là résulte donc ce théorème général :

*Dans le mouvement d’un système quelconque de corps animés par des forces mutuelles d’attraction, ou tendantes à des centres fixes, et proportionnelles à des fonctions quelconques des distances, les courbes décrites par les différents corps, et leurs vitesses, sont nécessairement telles que la somme des produits de chaque masse par l’intégrale de la vitesse multipliée par l’élément de la courbe est un maximum ou un minimum, pourvu que l’on regarde les premiers et les derniers points de chaque courbe comme donnés, en sorte que les variations des coordonnées répondantes à ces points soient nulles.*

C’est le théorème dont nous avons parlé à la fin de la première Section, sous le nom de *Principe de la moindre action*^([\[7\]](#cite_note-7)).

40\. Mais ce théorème ne contient pas seulement une propriété très remarquable du mouvement des corps, il peut encore servir à déterminer ce mouvement. En effet, puisque la formule _(S)$m\int u\, ds$ doit être un maximum ou un minimum, il n’y a qu’à chercher, par la méthode des *variations*, les conditions qui peuvent la rendre telle ; et, en employant l’équation générale de là conservation des forces vives, on trouvera toujours toutes les équations nécessaires pour déterminer le mouvement de chaque corps. Car, pour le maximum ou minimum, il faut que la variation soit nulle et que, par conséquent, on ait

$\delta$_(S)$m\int u\, ds = 0\,;$

et de là, en pratiquant dans un ordre rétrograde les opérations exposées ci-dessus, on trouvera la même formule générale d’où l’on était parti.

Pour rendre cette méthode plus sensible, nous allons l’exposer ici en peu de mots. La condition du maximum ou minimum donne, en général,

$\delta$_(S)$m\int u\, ds = 0,$

et, faisant passer le signe différentiel $\delta$ sous les signes _(S) et $\int$ (ce qui est évidemment permis par la nature de ces différents signes), on aura l’équation

_(S)$m\int\delta(u\, ds) = 0,$

ou bien, en exécutant la différentiation par $\delta,$

_(S)$m\int(ds\,\delta u + u\,\delta\, ds) = 0.$

Je considère d’abord la partie

_(S)$m\int ds\,\delta u\,;$

en mettant pour $ds$ sa valeur $u\, dt,$ elle devient

_(S)$m\int u\,\delta u\, dt,$

ou, changeant l’ordre des signes _(S) et $\int,$ qui sont absolument indépendants l’un de l’autre,

$\int dt$_(S)$mu\,\delta u.$

Or l’équation générale du principe des forces vives donne (art. 34)

_(S)$mu^{2} = 2H + 2$_(S)${mH},$

$d\Pi$ étant égal à

$P\,\delta p + Q\,\delta q + R\,\delta r + \ldots\,;$

donc, différentiant suivant $\delta,$ on aura

_(S)$mu\,\delta u = -$_(S)$m\,\delta\Pi = -$_(S)$m(P\,\delta p + Q\,\delta q + R\,\delta r + \ldots).$

parce que, $\Pi$ étant supposée une fonction algébrique de $p,\, q,\, r,\ldots$ la différentielle $\delta\Pi$ est la même que $d\Pi,$ en changeant seulement $d$ en $\delta.$ Ainsi la quantité

_(S)$m\int ds\,\delta u$

se réduira à cette forme

$- \int dt$_(S) $m(P\,\delta p + Q\,\delta q + R\,\delta r + \ldots).$

Je considère ensuite l’autre partie

_(S)$m\int u\,\delta\, ds,$

et j’y substitue, à la place de $ds,$ sa valeur exprimée par des coordonnées rectangles, ou par d’autres variables quelconques. En employant les coordonnées rectangles $x,\, y,\, z,$ on a

$ds = \sqrt{dx^{2} + dy^{2} + dz^{2}}\,;$

donc, différentiant suivant $\delta,$

$\delta\, ds = \frac{dx}{ds}\delta\, dx + \frac{dy}{ds}\delta\, dy + \frac{dz}{ds}\delta\, dz,$

ou bien, en transposant les signes $d,\,\delta,$ et écrivant $d\,\delta$ au lieu de $\delta\, d,$ ce qui est toujours permis à cause de l’indépendance de ces signes,

$\delta\, ds = \frac{dx}{ds}d\,\delta x + \frac{dy}{ds}d\,\delta y + \frac{dz}{ds}d\,\delta z\,;$

on aura ainsi, en substituant cette valeur et mettant $dt$ à la place de $\frac{ds}{u},$

$\int u\,\delta\, ds = \int\left( \frac{dx}{dt}d\,\delta x + \frac{dy}{dt}d\,\delta y + \frac{dz}{dt}d\,\delta z \right).$

Comme il se trouve ici, sous le signe intégral $\int,$ des différentielles des variations $\delta x,\,\delta y,\,\delta z,$ il faut les faire disparaître par l’opération connue des intégrations par parties, suivant les principes de la méthode des variations. On transformera donc la quantité $\int\frac{dx}{dt}d\,\delta x$ en celle-ci, qui lui est équivalente,

$\frac{dx}{dt}\,\delta x - \int\delta x\, d\frac{dx}{dt}\,;$

et, supposant que les deux termes de la courbe soient donnés, en sorte que les coordonnées qui répondent au commencement et à la fin de l’intégrale ne varient point, on aura simplement

$\int\frac{dx}{dt}d\,\delta x = - \int\delta x\, d\frac{dx}{dt}.$

On trouvera de même

$\int\frac{dy}{dt}d\,\delta y = - \int\delta y\, d\frac{dy}{dt}$

et, pareillement,

$\int\frac{dz}{dt}d\,\delta z = - \int\delta z\, d\frac{dz}{dt}\,;$

de sorte qu’on aura cette transformée

$\int u\,\delta\, ds = - \int\left( \delta x\, d\frac{dx}{dt} + \delta y\, d\frac{dy}{dt} + \delta z\, d\frac{dz}{dt} \right).$

Donc la quantité

_(S)$m\int u\,\delta\, ds$

deviendra, en transposant les signes _(S) et $\int$ et supposant $dt$ constant,

$- \int dt$_(S)$m\left( \delta x\, d\frac{d^{2}x}{dt^{2}} + \delta y\, d\frac{d^{2}y}{dt^{2}} + \delta z\, d\frac{d^{2}z}{dt^{2}} \right).$

L’équation du maximum ou minimum sera donc

$\int dt$_(S)$m\left( P\,\delta p + Q\,\delta q + R\,\delta r + \ldots + \frac{d^{2}x}{dt^{2}}\delta x + \frac{d^{2}y}{dt^{2}}\delta y + \frac{d^{2}z}{dt^{2}}\delta z \right) = 0,$

laquelle devant avoir lieu, en général, pour toutes les variations possibles, il faudra que la quantité sous le signe $\int$ soit nulle à chaque instant ; on aura ainsi l’équation indéfinie

_(S)$m\left( P\,\delta p + Q\,\delta q + R\,\delta r + \ldots + \frac{d^{2}x}{dt^{2}}\delta x + \frac{d^{2}y}{dt^{2}}\delta y + \frac{d^{2}z}{dt^{2}}\delta z \right) = 0,$

équation qui est la même chose que la formule générale de la Dynamique (sect. 11, art. 5), et qui donnera par conséquent, comme celle-ci, toutes les équations nécessaires pour la solution du problème.

41\. Au lieu des coordonnées $x,\, y,\, z,$ on peut employer d’autres indéterminées quelconques, et tout se réduit à exprimer l’élément de l’arc $ds$ en fonction de ces indéterminées. Qu’on prenne, par exemple, le rayon ou la distance rectiligne à l’origine des coordonnées, qu’on nommera $\rho,$ avec deux angles, dont l’un $\psi$ soit l’inclinaison de ce rayon sur le plan des $xy$ et l’autre $\varphi$ soit l’angle de la projection du même rayon sur ce plan avec l’axe des $x\,;$ on aura

$z = \rho\sin\psi,\quad y = \rho\cos\psi\sin\varphi,\quad x = \rho\cos\psi\cos\varphi,$

et, de là, on trouvera

$ds^{2} = dx^{2} + dy^{2} + dz^{2} = d\rho^{2} + \rho^{2}\left( d\psi^{2} + \cos^{2}\psi\, d\varphi^{2} \right),$

expression qu’on pourrait aussi trouver directement par la Géométrie. Différentiant donc par $\delta$ et changeant $\delta d$ en $d\delta,$ on aura

$\begin{matrix}
{ds\,\delta\, ds =} & {d\rho\, d\,\delta\rho + \rho\left( d\psi^{2} + \cos^{2}\psi\, d\varphi^{2} \right)\delta\rho} \\
 & {+ \rho^{2}\left( d\psi\, d\,\delta\psi - \sin\psi\cos\psi\, d\varphi^{2}\delta\psi + \cos^{2}\psi\, d\varphi\, d\,\delta\varphi \right)\,;}
\end{matrix}$

d’où, en divisant par $dt = \frac{ds}{u}$ et en intégrant, on aura

$\begin{matrix}
{\int u\,\delta\, ds =} & {\int dt\left\lbrack \frac{d\rho}{dt}\frac{d\,\delta\rho}{dt} + \rho\left( \frac{d\psi^{2}}{dt^{2}} + \cos^{2}\psi\frac{d\varphi^{2}}{dt^{2}} \right)\delta\rho \right\rbrack} \\
 & {+ \int dt\left( \rho^{2}\frac{d\psi}{dt}\frac{d\,\delta\psi}{dt} - \rho^{2}\sin\psi\cos\psi\frac{d\varphi^{2}}{dt^{2}}\delta\psi + \rho^{2}\cos^{2}\psi\frac{d\varphi}{dt}\frac{d\,\delta\varphi}{dt} \right).}
\end{matrix}$

On fera disparaître de dessous le signe $\int$ les doubles signes $d\,\delta$ par des intégrations par parties et l’on rejettera d’abord les termes qui contiendraient des variations hors du signe $\int,$ parce que ces variations, devant alors se rapporter aux extrémités de l’intégrale, deviennent nulles par la supposition que les premiers et derniers points des courbes décrites par les corps soient donnés et invariables. On aura ainsi cette transformée

$\int u\,\delta ds = - \int du\,\delta s = - \int dt\left\{ \left( \frac{d^{2}\rho}{dt^{2}} - \rho\frac{d\psi^{2}}{dt^{2}} - \rho\cos^{2}\psi\frac{\varphi^{2}}{t^{2}} \right)\delta\rho\begin{matrix}
 \\
 \\
 \\
 \\

\end{matrix} \right.$

$\left. \operatorname{} + \left\lbrack \rho^{2}\sin\psi\cos\psi\frac{d\varphi^{2}}{dt^{2}} + \frac{d\left( \rho^{2}\frac{d\psi}{dt} \right)}{dt} \right\rbrack\delta\psi + \frac{d\left( \cos^{2}\psi\frac{d\varphi}{dt} \right)}{dt}\delta\varphi \right\}\,;$

par conséquent, l’équation du maximum ou minimum sera

$\int dt$_(S)$m\left\{ P\,\delta p + Q\,\delta q + R\,\delta r + \ldots + \left( \frac{d^{2}\rho}{dt^{2}} - \rho\frac{d\varphi^{2}}{dt^{2}} - \rho\cos^{2}\psi\frac{d\varphi^{2}}{dt^{2}} \right)\delta\rho\begin{matrix}
 \\
 \\
 \\
 \\

\end{matrix} \right.$

$\left. \operatorname{} + \left\lbrack \rho^{2}\sin\psi\cos\psi\frac{d\varphi^{2}}{dt^{2}} + \frac{d\left( \rho^{2}\frac{d\psi}{dt} \right)}{dt} \right\rbrack\delta\psi + \frac{d\left( \cos^{2}\psi\frac{d\varphi}{dt} \right)}{dt}\delta\varphi \right\} = 0.$

Égalant à zéro la quantité qui est sous le signe $\int,$ on aura une équation indéfinie, analogue à celle de l’article précédent, mais qui, au lieu de variations $\delta x,\,\delta y,\,\delta z,$ contiendra les $\delta\rho,\,\delta\varphi,\,\delta\psi\,;$ et l’on en tirera les équations nécessaires pour la solution du problème, en réduisant d’abord toutes les variations au plus petit nombre possible et faisant ensuite des équations séparées des termes affectés de chacune des variations restantes.

En employant d’autres indéterminées, on aura des formules différentes, et l’on sera assuré d’avoir toujours, dans chaque cas, les formules les plus simples que la nature des indéterminées puisse comporter. *Voir* le second Volume des *Mémoires de l’Académie de Turin*, où l’on a employé cette méthode pour résoudre différents problèmes de Mécanique^([\[8\]](#cite_note-8)).

42\. Au reste, puisque $ds = u\, dt,$ la formule

_(S)$m\int u\, ds,$

qui est un maximum ou un minimum, peut aussi se mettre sous la forme _(S)$m\int u^{2}dt,$ ou

$\int dt$_(S)$m\, u^{2},$

dans laquelle _(S)$m\, u^{2},$ exprime la force vive de tout le système dans un instant quelconque. Ainsi le principe dont il s’agit se réduit proprement à ce que la somme des forces vives instantanées de tous les corps, depuis le moment où ils partent des points donnés jusqu’à celui où ils arrivent à d’autres points donnés, soit un maximum ou un minimum. On pourrait donc l’appeler, avec plus de fondement, le *principe de la* *plus grande* ou *plus petite force vive ;* et cette manière de l’envisager aurait l’avantage d’être générale, tant pour le mouvement que pour l’équilibre, puisque nous avons vu, dans la troisième Section de la I^(re) Partie (art. 22), que la force vive d’un système est toujours la plus grandie ou la plus petite dans la situation d’équilibre.

![Séparateur](//upload.wikimedia.org/wikipedia/commons/thumb/7/74/Sep4.svg/120px-Sep4.svg.png?utm_source=fr.wikisource.org&utm_campaign=parser&utm_content=thumbnail)

1.  [↑](#cite_ref-1) Cette conclusion est trop absolue. L’équation différentielle qui lie $\xi,\,\eta,\,\zeta$ est, en effet, de même forme que celle qui lie $x,\, y,\, z\,;$ mais les forces $X,\, Y,\, Z$ n’auront pas des expressions de même forme par rapport aux deux systèmes de variables. Ainsi, par exemple, si l’on considère deux points qui s’attirent mutuellement avec une force réciproquement proportionnelle au carré de la distance, ils décriront des ellipses par rapport aux axes mobiles passant par le centre de gravité. Par rapport à des axes fixes, les trajectoires seraient beaucoup plus compliquées. (*J. Bertrand.*)

2.  [↑](#cite_ref-2) On trouvera à la fin du Volume la démonstration de ce théorème, qui n’offre pas, à beaucoup près, la difficulté que Lagrange semble lui attribuer. M. Binet en a publié une depuis longtemps dans le *Bulletin de la Société philomathique*. (*J. Bertrand.*)

3.  [↑](#cite_ref-3) Ces quantités $\alpha,\,\,\beta,\,\,\gamma$ ne sont pas suffisamment définies. Quel que soit, en effet, le déplacement d’un système variable de forme, on peut le regarder comme résultant d’un mouvement *arbitraire* imprimé au système solidifié, puis d’un second mouvement produisant le changement de position respective des points considérés. L’indétermination des quantités $\alpha,\,\beta,\,\gamma$ rend cet article 37 extrêmement obscur. Je dois avouer qu’il m’a été impossible de comprendre le raisonnement de Lagrange et d’attacher même aucun sens précis au théorème qui termine le paragraphe. Les notes qui suivent se rapportent donc au seul cas d’un système solide. (*J. Bertrand.*)

    Tout en souscrivant aux remarques précédentes, nous proposerons l’interprétation suivante du résultat obtenu par Lagrange : si, dans les formules qui donnent $\overset{˙}{x},\,\overset{˙}{y},\,\overset{˙}{z},$ on considère $\alpha,\,\beta,\,\gamma$ comme des fonctions données de $x,\, y,\, z$ et $\overset{˙}{\omega},\,\overset{˙}{\varphi},\,\overset{˙}{\psi},$ comme des arbitraires variables, cela revient à considérer tous les mouvements du système dans lesquels la déformation est la même au bout d’un instant infiniment petit ; car, si l’on cherche, par exemple, la dérivée de la distance de deux points du système par rapport au temps, on reconnaît aisément que cette dérivée ne dépend nullement des arbitraires $\overset{˙}{\omega},\,\overset{˙}{\varphi},\,\overset{˙}{\psi}$ et demeure, par conséquent, la même quand ces arbitraires prennent toutes les valeurs possibles. Le théorème de Lagrange peut donc s’énoncer comme il suit :

    *Si l’on compare le mouvement que prend le système sous les impulsions données à tous ceux dans lesquels la déformation serait la même au bout d’un instant infiniment petit, la force vive acquise par le système dans le mouvement naturel sera toujours un maximum ou un minimum.*

    Il résulte d’ailleurs de la démonstration donnée par M. Bertrand dans la note suivante que cette *force vive sera toujours un maximum*.

    Au reste, la proposition de Lagrange est comprise comme cas particulier dans un théorème très général que l’on doit à Sturm, et que l’on trouvera énoncé dans une Note insérée aux *Comptes rendus de l’Académie des Sciences*, tome XIII, page 1045, et démontré dans un Mémoire posthume de Sturm publié par M. Prouhet. (*Voir* Sturm, *Leçons de Mécanique*, t. II.) G. D.

4.  [↑](#cite_ref-4) Ces variations, représentées par la caractéristique $\delta,$ se rapportent aux changements qu’éprouvent les vitesses par suite de l’introduction de liaisons nouvelles, les forces motrices restant les mêmes. Ainsi, par exemple, dans le cas d’un corps solide, les variations $\delta$ peuvent résulter de l’introduction d’un axe fixe dans le système. (*J. Bertrand.*)

5.  [↑](#cite_ref-5) Si l’on suppose que les variations désignées par $\delta$ soient finies, on aura, en différentiant l’équation des forces vives,

    _(S)$\left\{ 2m(\overset{˙}{x}\delta\overset{˙}{x} + \overset{˙}{y}\delta\overset{˙}{y} + \overset{˙}{z}\delta\overset{˙}{z}) + m\left\lbrack (\delta\overset{˙}{x})^{2} + (\delta\overset{˙}{y})^{2} + (\delta\overset{˙}{z})^{2} \right\rbrack + X\delta\overset{˙}{x} + Y\delta\overset{˙}{y} + Z\delta\overset{˙}{z} \right\} = 0\,;$

    et si l’on continue le raisonnement en ayant égard aux nouveaux termes introduits par cette hypothèse, on trouvera

    $\delta$_(S)$m\left( \overset{˙}{x}\,\!^{2} + \overset{˙}{y}\,\!^{2} + \overset{˙}{z}\,\!^{2} \right) = -$_(S)$m\left\lbrack (\delta\overset{˙}{x})^{2} + (\delta\overset{˙}{y})^{2} + (\delta\overset{˙}{z})^{2} \right\rbrack,$

    ce qui montre que l’accroissement des forces vives est négatif et égal à la somme des forces vives dues aux vitesses perdues par les différents points. (*J. Bertrand.*)

6.  [↑](#cite_ref-6) Il résulte de la note précédente qu’elle est toujours un maximum. Cette remarque a été faite pour la première fois par M. Delaunay, qui la justifie d’une manière très différente. (*Journal de Liouville*, I^(re) série, t. V, p. 255.) (*J. Bertrand.*)

7.  [↑](#cite_ref-7) L’intégrale _(S)$m\int u\, ds$ est un maximum ou un minimum, si on la compare aux intégrales analogues relatives à tout autre mouvement du système qui serait produit par les mêmes forces et dans lequel, malgré l’introduction de liaisons nouvelles laissant subsister le principe des forces vives, les positions initiales et finales resteraient les mêmes. Peut-être cet énoncé, qui résulte évidemment de la démonstration, n’est-il pas rendu assez explicite dans le texte. (*J. Bertrand.*)

    On pourra consulter, au sujet de ce principe, un article d’Olinde Rodrigues inséré dans la *Correspondance de l’École Polytechnique*, t. III, p. 159, et les *Vorlesungen über Dynamik* de Jacobi. G. D.

8.  [↑](#cite_ref-8) *Voir* aussi une Note remarquable d’Olinde Rodrigues ; *Correspondance sur l’École Polytechnique*, tome III, page 159. (*J. Bertrand.*)
