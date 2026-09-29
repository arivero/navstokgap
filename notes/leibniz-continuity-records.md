# Leibniz's law of continuity, read on records, selects a positive action floor for motions

**Result, 2026-09-29 (Claude; written derivation and passage readings,
unrefereed).** In the mark model of the [Planck paper](planck-gap-paper.md)
(§3), the least error with which any admissible protocol decides Newton's
comparison, inertia against a constant force $F$ over a cell of duration
$\tau$ with unknown initial position and velocity, is

$$P_*(F)=\Phi\Bigl(-\tfrac12\sqrt{K_\tau/\kappa}\Bigr),\qquad K_\tau=\frac{F^2\tau^3}{24\,m},$$

for a mark floor $\kappa>0$, while $P_*(F)=0$ for every $F\ne0$ when $\kappa=0$; at
$F=0$ the cases coincide and $P_*=\frac12$. **The best verdict is continuous in the
force at $F=0$ if and only if $\kappa>0$.** The same holds on Zeno's rung, rest
against uniform motion, with $mv^2\tau/(8\kappa)$ in place of $K_\tau/(4\kappa)$. Static
shapes behave differently: there the best verdict jumps at zero for every
$\kappa$, because reading a shape disturbs nothing.

Leibniz stated the law of continuity in July 1687, the year of the
*Principia*, as a test of laws of motion: when two cases approach and are
lost in one another, their outcomes must do the same, and he describes the
nearly equal case of a collision as one "dont à peine ce cas peut estre
distingué" (§2). Read with outcomes measured by how well they can be told
apart, the law holds for Newton's comparison exactly when $\kappa>0$. Read with
outcomes measured by positions and velocities, it holds on both branches.
The fork that every route of this programme reaches (positivity as a
premise, the zero branch admissible) is therefore located inside one
Newton-age text, and the programme's thesis, that quantization is a
consistency condition on laws which Newton's continuum limit missed, has a
period form: Leibniz's "preuve ou examen" of laws of motion, applied to
their records. His *petites perceptions* (1704) supply the graded, additive
discernibility that the records reading needs (§3). The Newton-age dispute
over indivisibles, Galileo, Cavalieri and Guldin between 1621 and 1647,
concerned static figures, where the theorem imposes no floor and Newton's
limit doctrine is the right answer (§4).

## 1. The proposition

**Setting.** The statistical model of the Planck paper, §3: mark $j$ at time
$t_j$ returns the position with Gaussian error of standard deviation
$\delta_j$ and delivers an independent Gaussian impulse of standard deviation
$\Delta_j$; every available mark obeys $\delta_j\Delta_j\ge\kappa$; protocols are
non-adaptive and tests are invariant under the unknown $y_0,v_0$. The
optimal invariant test errs with probability $\Phi(-d/2)$, and Theorem 2 of
the paper gives $d^2\le K_\tau/\kappa$ for every protocol, with a sharp constant.

**Proposition L.** Let $P_*(F)$ be the infimum of the error over admissible
protocols and invariant tests. Then $P_*(F)=\Phi(-\frac12\sqrt{K_\tau/\kappa})$ if
$\kappa>0$, and $P_*(F)=0$ for $F\ne0$ if $\kappa=0$. For Zeno's rung (rest against
speed $v$, unknown initial position),
$P_*(v)=\Phi(-\sqrt{mv^2\tau/(8\kappa)})$ if $\kappa>0$ and $P_*(v)=0$ for $v\ne0$ if $\kappa=0$.
For a static taper $\vartheta$ read at two heights, $P_*(\vartheta)=0$ for $\vartheta\ne0$ and every
$\kappa\ge0$.

*Proof.* For $\kappa>0$, $\Phi(-d/2)$ decreases in $d$, and the supremum of $d^2$ over
protocols is $K_\tau/\kappa$ by the sharpness in Theorem 2; hence the infimum of
the error. For $\kappa=0$, marks with $\Delta_j=0$ and arbitrary $\delta_j>0$ are
admissible; take three marks at distinct times and weights $u$ with
$\sum u_i=\sum u_it_i=0$, so that $u^{\mathsf T}P=\frac F{2m}\sum u_it_i^2\ne0$ while
$u^{\mathsf T}\Sigma u=\sum\delta_i^2u_i^2\to0$; then $d\to\infty$. Zeno's rung is Theorem 9(i)
of the paper, whose bound $d^2\le mv^2\tau/(2\kappa)$ two marks attain. The static
case is Theorem 9(iii): with $N$ marks of resolution $\delta$ at each height,
$d^2=N\vartheta^2\Delta h^2/(2\delta^2)$, unbounded in $N$ whatever $\kappa$ is. $\square$

For $\kappa>0$ the verdict is Lipschitz at $F=0$ with constant
$\tau^{3/2}/(2\sqrt{2\pi}\sqrt{24m\kappa})$, which diverges as $\kappa\to0$: the zero branch is
the singular limit of a family of continuous verdict functions, the
pattern of an order of limits. Quantum mechanics agrees with the model on
the split between the two kinds of case. A static parameter can be
estimated without limit by repetition, while the dynamical comparison in a
fixed window has the $N$-independent bound that the paper's quantum results
supply.

## 2. Leibniz, 1687: the law of continuity as a test of laws

Leibniz, "Lettre de M. L. sur un principe general utile à l'explication
des loix de la nature", *Nouvelles de la République des Lettres*, July
1687, in Gerhardt, *Die philosophischen Schriften* III (1887), 51--55
([companion](../docs/classics/Leibniz_PrincipeGeneral_1687_Gerhardt3_OCR.md);
passage, OCR normalized by hand).

- **The text.** "Lorsque la difference de deux cas peut estre diminuée au
  dessous de toute grandeur donnée *in datis* ou dans ce qui est posé, il
  faut qu'elle se puisse trouver aussi diminuée au dessous de toute
  grandeur donnée *in quaesitis* ou dans ce qui en resulte ... *Datis
  ordinatis etiam quaesita sunt ordinata*" (p. 52). "Le repos peut estre
  consideré comme une vistesse infinement petite, ou comme une tardité
  infinie", so that the rule of rest must be a particular case of the rule
  of motion, "autrement ... ce sera une marque asseurée, que les regles sont
  mal concertées" (pp. 52--53). Against Descartes's second rule of
  collision, a body B made "aussi petite que l'on voudra" larger than C
  should reflect a little less, and C a little more, "qu'au cas de l'égalité
  dont à peine ce cas peut estre distingué" (p. 53). And the exemption: "dans
  les choses composées quelques fois un petit changement peut faire un
  grand effect, comme par exemple une estincelle tombant dans une grande
  masse de la poudre à canon", while "à l'égard des principes ou choses
  simples, rien de semblable ne sçauroit arriver" (p. 54).
- **What it commits him to.** A law of motion is tested from outside,
  before any inner discussion ("preuve ou examen ... avant même que de venir
  à une discussion interieure"), by whether its outcomes converge when its
  cases do. Rest is the limit of slow motion and equality the limit of
  inequality, and a rule that jumps at either is ill made. Composite
  amplifiers may magnify small differences into large effects; simple
  principles may not jump.
- **What the theorem does with it.** Leibniz applies the test to
  collision velocities, the geometric reading, and Newton's laws pass it
  on both branches. His own phrase for the nearly equal case, however, is
  a statement about discernibility, and Proposition L shows what the test
  demands when outcomes are measured that way: for Newton's comparison and
  for Zeno's rung, continuity holds exactly when $\kappa>0$. The exemption
  marks the boundary of the argument. An instrument is a composite
  amplifier, and finite amplification is allowed; the zero branch needs
  the supremum over all instruments the laws permit to jump, a jump in what
  the laws allow to be recorded, which is the level of principle if the
  mark trade-off is a law. Whether the verdict of the best possible record
  counts among "ce qui en resulte" is the premise, now stated in
  Leibniz's terms. The theorem also declines one extension: for static
  shapes the records reading fails on both branches, and Leibniz's letter
  applies the law to figures geometrically (the ellipse passing into the
  parabola, p. 52), which Proposition L shows to be the only reading that
  holds there.

Prior art, at metadata level: Mortensen, "The Leibniz Continuity Condition,
Inconsistency and Quantum Dynamics",
[*J. Philos. Logic* **26** (1997), 377--389](https://doi.org/10.1023/A:1004275928191),
treats the condition against quantum jumps at the instant of change; the
pairing of continuity with the identity of indiscernibles is the subject of
Russell's chapter "The Identity of Indiscernibles and the Law of
Continuity" in *A Critical Exposition of the Philosophy of Leibniz*. The
operational reading used here is the base-norm topology on states, in which
classical pure states are pairwise perfectly distinguishable; compare the
[Hardy audit](quantum-exclusion-premises.md), whose continuity axiom
concerns reversible paths between pure states.

## 3. Leibniz, 1704: small perceptions add

Leibniz, *Nouveaux essais*, Préface, written 1703--1705, in Gerhardt V
(1882), 47--49
([companion](../docs/classics/Leibniz_NouveauxEssais_Preface_Gerhardt5_OCR.md);
passage, OCR normalized by hand).

- **The text.** To hear the roar of the sea "il faut bien qu'on entende les
  parties qui composent ce tout, c'est à dire les bruits de chaque vague ...
  Car il faut qu'on en soit affecté un peu par le mouvement de cette vague
  ... autrement on n'auroit pas celle de cent mille vagues, puisque cent
  mille riens ne sauroient faire quelque chose" (p. 47). "La nature ne fait
  jamais des sauts ... jamais un mouvement ne naist immediatement du repos
  ny s'y reduit que par un mouvement plus petit" (p. 49). "En vertu des
  variations insensibles, deux choses individuelles ne sauroient estre
  parfaitement semblables" (p. 49).
- **What it commits him to.** Every effect, however small, registers a
  little; perception is graded and additive; noticeable perceptions come by
  degrees from insensible ones; distinct individuals always differ, by
  differences that can be insensible.
- **What the theorem does with it.** The cut measure makes the addition
  exact. Newton's cell action $K_\tau$ is spent additively over any sequence of
  cuts, a share $3s(1-s)K$ per cut at fraction $s$
  ([cut-measure note](cut-measure-newton.md), Theorems 1--2), and it is the
  Cameron--Martin energy of the force's shift (Proposition 4), so each cut
  carries a finite share of the whole comparison's discernibility and the
  shares add to $K_\tau/\kappa$. With $\kappa>0$ each cut is a *petite perception* of the
  force, insensible alone below the mark mesh and effective in the
  assembly; with $\kappa=0$ a single cut decides, and records of motion have no
  insensible parts. The zero branch can still place insensibility in the
  perceiver, as Leibniz's confusion of created substances does, graded from
  one substance to another. The [stochastic route](stochastic-route-velocitas-ultima.md)
  shows how composition turns graded constants into one ($\kappa=mD$ for every
  body), so the step from "every created perceiver is confused" to one
  universal floor is available as a reading; it is recorded here as a
  reading. The maxim on motion from rest is Galileo's passage through all
  degrees of slowness, stated at the beginning of motion, the regime of
  Lemma X ("ipso motus initio"); Zeno's rung of Proposition L is its
  records version.

## 4. The Newton-age dispute over indivisibles, 1621--1647

Book I's closing scholium prefers limits to indivisibles, "quoniam durior
est indivisibilium Hypothesis", without naming the dispute it settles. The
primary texts are held in `docs/classics`.

- **Galileo's bowl and cone** (*Discorsi*, Giornata prima, Favaro VIII,
  74--76, 78--80; [companion](../docs/classics/Galileo_Discorsi_GiornataPrima_Favaro_it_wikisource.md)).
  Every horizontal section of the bowl (cylinder minus hemisphere) equals
  the section of the inscribed cone, so the surfaces are "sempre eguali, e
  ... diminuendosi sempre egualmente, vadano a terminare l'una in un sol
  punto e l'altra nella circonferenza d'un cerchio ... perché in questa
  consequenza sola versa la nostra maraviglia". His conclusion: "questi
  attributi di maggioranza, minorità ed egualità non convenghino a
  gl'infiniti". *Commitment:* comparison fails among infinites and
  indivisibles. *The theorem:* the bowl is Democritus's third (bowl and cone
  are each a third of the cylinder), a static figure, so Theorem 9(iii) and
  Proposition L put no floor on it, and Newton's sentence that ultimate
  ratios are limits and never ratios of ultimate quantities dissolves the
  wonder: the ratio of sections is 1 at every cut, and point and circle are
  never compared. Leibniz reverses Galileo's conclusion in 1687: equality
  is an infinitely small inequality, so the attributes extend by continuity.
- **Cavalieri's reply** (letter 2992 of 1634, Opere XVI 136--138;
  [companion](../docs/classics/Galileo_Opere_XVI_indivisibles_letters_1634-1636_OCR.md)).
  Equal parts are removed "essendo noi arrivati al nullo piano tanto nel
  cono quanto nella scodella", and "non mi dichiaro di componere il continuo
  d'indivisibili, ma solo mostro che i continui hanno la proportione delli
  aggregati di questi indivisibili". *Commitment:* ratios of aggregates of
  sections, with no claim of composition. *The theorem:* the cut measure
  keeps exactly this stance, a statement about aggregates of cuts (shares
  summing to $K_\tau$ for every schedule) that composes nothing, and the mark
  mesh bounds what can be exhibited without bounding what can be cut.
- **Galileo's wheel** (Favaro VIII, 68--72, same companion). A smaller
  concentric wheel covers the larger wheel's line with its own sides "con
  l'interposizione di cento mila spazii vacui traposti", and for circles
  "sì come i lati non son quanti, ma bene infiniti, così gl'interposti vacui
  non son quanti, ma infiniti"; Simplicio hears in it "quei vacui
  disseminati di certo filosofo antico", and Salviati's retort about the
  denier of Providence names Epicurus. *Commitment:* a continuum composed of
  infinitely many unquantified indivisibles, partly full and partly void,
  crossed by leaps across the voids. *The theorem:* Galileo publishes
  al-Nazzam's leap in 1638 as consistent. The paper's reading of the leap
  applies: below the mesh a record is consistent with a leap, the interval
  stays divisible, and the crossing is exhibited in finitely many steps.
- **Guldin** (*Centrobaryca* IV, 1641, preface p. 4;
  [companion](../docs/classics/Guldin_Centrobaryca_LiberIV_1641_pages.md)):
  "Galileus profecto in eodem Dialogo de Motu locali, disputans de
  infinito, de proprietatibus finitorum, quas infinitis applicare minime
  liceat, contra ipsum concludit." *Commitment:* Galileo's own principle
  refutes Cavalieri. *The theorem:* it sides with Guldin and Newton on
  composition (no least magnitude follows from $\kappa$) and with Cavalieri on
  ratios of aggregates.

The four entries share one feature that sharpens the paper's §9. The
seventeenth-century dispute Newton answered concerned static figures, and
there the theorem agrees with his answer and imposes nothing. The floor
enters only where a record carries back-action, in the lemmas applied to
motion, and the dispute about motion is the one he passed over.

## 5. Consequence for STATE

For the Newton goal: positivity of the action floor is equivalent, in the
mark model, to Leibniz's 1687 law of continuity for laws of motion with
outcomes measured by discernibility (Proposition L). The zero branch keeps
the geometric reading, which Leibniz himself applied, so the fork stands;
it is now a choice between two readings of one Newton-age principle, with
Leibniz's phrase "à peine distingué" and his doctrine of small perceptions
on the side of the floor, and statics showing why the reading must be
confined to motions. For the scholion: two Leibniz entries and the
Galileo--Cavalieri--Guldin layer are supplied with their three obligations;
a pointer belongs in the paper's §9. To be refereed (Astra or Fable): the
proposition, the passage readings, and whether the records reading is fair
to Leibniz.
