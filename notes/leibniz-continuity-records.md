# Leibniz's law of continuity, read on records, selects a positive action floor for motions

**Result, 2026-09-29 (Claude; written derivation and passage readings;
refereed by Fable with REFINE, corrections applied).** In the mark model of
the [Planck paper](planck-gap-paper.md) (§3), the infimum of the error with
which a non-adaptive protocol, read by tests invariant under the unknown
initial position and velocity, decides Newton's comparison, inertia against
a constant force $F$ over a cell of duration $\tau$, is

$$P_*(F)=\Phi\Bigl(-\tfrac12\sqrt{K_\tau/\kappa}\Bigr),\qquad K_\tau=\frac{F^2\tau^3}{24\,m},$$

for a mark floor $\kappa>0$, while $P_*(F)=0$ for every $F\ne0$ when $\kappa=0$; at
$F=0$ the cases coincide and $P_*=\frac12$. The infimum is approached by dense
protocols. **The best verdict over these protocols is continuous in the
force at $F=0$ if and only if $\kappa>0$**; each single protocol gives a
continuous verdict on both branches. The same holds on Zeno's rung, rest
against uniform motion, with $mv^2\tau/(8\kappa)$ in place of $K_\tau/(4\kappa)$, attained by
two marks. A single cut at fraction $s$ carries exactly the discernibility
$d^2=3s(1-s)K_\tau/\kappa$, the cut measure's share (§3). Static shapes behave
differently: when the read coordinate has no dynamics in the window, the
best verdict jumps at zero for every $\kappa$. The equivalence concerns the
observer ignorant of the preparation; a protocol that knows it (Yuen's, in
§3 of the paper) decides at every force for every $\kappa$.

Leibniz published the law of continuity in July 1687, the year of the
*Principia*, as a test of laws of motion: when two cases approach and are
lost in one another, their outcomes must do the same. He measures the
difference of the cases by discernibility, describing the nearly equal case
of a collision as one "dont à peine ce cas peut estre distingué" (§2).
Applying the same measure to the outcomes is our step. Read that way, the
law holds for Newton's comparison exactly when $\kappa>0$. Read with outcomes
measured by positions and velocities, as Leibniz applied it, it holds on
both branches. The fork that every route of this programme reaches
(positivity as a premise, the zero branch admissible) is therefore located
between a reading Leibniz made and one he did not, and the programme's thesis, that quantization is a
consistency condition on laws which Newton's continuum limit missed, has a
period form: Leibniz's "preuve ou examen" of laws of motion, applied to
their records. His *petites perceptions* (1704) supply the graded, additive
discernibility that the records reading needs (§3), and his *Pacidius* (1676)
the proportion argument against leaps, which a floor on action meets
(§2b). The Newton-age dispute
over indivisibles, Galileo, Cavalieri and Guldin between 1621 and 1647,
concerned static figures, where the theorem imposes no floor and Newton's
limit doctrine is the right answer (§4).

**After refereeing (Claude Fable, 2026-09-29).** REFINE, applied. The
mathematics of Proposition L checked, including the $\kappa=0$ case and the
static case; its equivalence at $F=0$ needs only Theorem 2's inequality.
Fable supplied the exact single-cut share $3s(1-s)K_\tau/\kappa$, now in §1 and §3.
Corrections: the non-adaptive, preparation-ignorant hypotheses are stated
up front (Yuen's protocol jumps for every $\kappa$); the transfer of Leibniz's
discernibility from the cases to the outcomes, the reading of his gunpowder
exemption (with its counter-reading) and the confinement to motions are
marked as ours; "distingué" and "sçauroit" are flagged as reconstructed
from the OCR; the Epicurus, al-Nazzam and Galileo wordings of §4 are
softened to what the texts say; prior art on statistical distance and on
continuity axioms is added.

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
$\kappa\ge0$, when the read coordinate has no dynamics in the window (a clamped
figure, or one of effectively infinite mass). For a single cut, marks at
$0,s\tau,\tau$, the best $d^2$ is exactly $3s(1-s)K_\tau/\kappa$.

*Proof.* For $\kappa>0$, $\Phi(-d/2)$ decreases in $d$, and the supremum of $d^2$ over
protocols is $K_\tau/\kappa$ by the sharpness in Theorem 2; hence the infimum of
the error. For $\kappa=0$, marks with $\Delta_j=0$ and arbitrary $\delta_j>0$ are
admissible; take three marks at distinct times and weights $u$ with
$\sum u_i=\sum u_it_i=0$, so that $u^{\mathsf T}P=\frac F{2m}\sum u_it_i^2\ne0$ while
$u^{\mathsf T}\Sigma u=\sum\delta_i^2u_i^2\to0$; then $d\to\infty$ (the same holds at fixed $\delta$ by
repetition, since $\Delta=0$ turns the motion into a static figure). The
equivalence at $F=0$ needs only Theorem 2's inequality, whose proof is
complete: $d^2\le K_\tau/\kappa$ gives $P_*\ge\Phi(-\frac12\sqrt{K_\tau/\kappa})\to\frac12$; the sharpness fixes
only the exact value. Zeno's rung is Theorem 9(i)
of the paper, whose bound $d^2\le mv^2\tau/(2\kappa)$ two marks attain. The static
case is Theorem 9(iii): with $N$ marks of resolution $\delta$ at each height,
$d^2=N\vartheta^2\Delta h^2/(2\delta^2)$, unbounded in $N$ whatever $\kappa$ is. For one cut, the
constraints force $u\propto(-(1-s),1,-s)$; then $S_0=S_2=0$ and
$S_1=-s(1-s)\tau u_1$, so the noise is at least
$\delta_1^2u_1^2+\Delta_1^2S_1^2/m^2\ge(2\kappa/m)s(1-s)\tau u_1^2$ by the arithmetic--geometric
mean, with equality for sharp end marks (their kicks do not propagate) and
$\delta_1=\Delta_1s(1-s)\tau/m$; the signal is $(F\tau^2/2m)^2s^2(1-s)^2u_1^2$, and the ratio
is $F^2\tau^3s(1-s)/(8m\kappa)=3s(1-s)K_\tau/\kappa$. $\square$

For $\kappa>0$ the verdict is Lipschitz at $F=0$ with constant
$\tau^{3/2}/(2\sqrt{2\pi}\sqrt{24m\kappa})$, which diverges as $\kappa\to0$: the zero branch is
the singular limit of a family of continuous verdict functions, the
pattern of an order of limits. Here $N$ counts marks on one body inside
one window, Newton's single trajectory; repeating the whole experiment on
fresh preparations multiplies $d^2$ on either kind of case. The paper's
quantum results (§§4--6) reproduce the split for the observer ignorant of
the preparation: a static parameter can be estimated without limit by
repeated marks, while the dynamical comparison in a fixed window keeps the
$N$-independent bound. With knowledge of the preparation (Yuen's protocol)
a single sharp mark decides at every force, so the proposition is a
statement about the preparation-ignorant observer.

## 2. Leibniz, 1687: the law of continuity as a test of laws

Leibniz, "Lettre de M. L. sur un principe general utile à l'explication
des loix de la nature", *Nouvelles de la République des Lettres*, July
1687, in Gerhardt, *Die philosophischen Schriften* III (1887), 51--55
([companion](../docs/classics/Leibniz_PrincipeGeneral_1687_Gerhardt3_OCR.md);
passage, OCR normalized by hand; where the OCR misreads accents, the
reconstructed letters are flagged).

- **The text.** "Lorsque la difference de deux cas peut estre diminuée au
  dessous de toute grandeur donnée *in datis* ou dans ce qui est posé, il
  faut qu'elle se puisse trouver aussi diminuée au dessous de toute
  grandeur donnée *in quaesitis* ou dans ce qui en resulte ... *Datis
  ordinatis etiam quaesita sunt ordinata*" (p. 52). "Le repos peut estre
  consideré comme une vistesse infinement petite, ou comme une tardité
  infinie", so that the rule of rest must be a particular case of the rule
  of motion, "autrement ... ce sera une marque asseurée, que les regles sont
  mal concertées" (pp. 52--53). Against Descartes's second rule of
  collision, after "une augmentation aussi petite que l'on voudra du corps
  B auparavant égal à C", B should reflect a little less and C a little
  more "qu'au cas de l'égalité dont à peine ce cas peut estre distingué"
  (p. 53; the OCR reads "distinguo", and the final letter awaits the page
  image). And the exemption: "dans
  les choses composées quelques fois un petit changement peut faire un
  grand effect, comme par exemple une estincelle tombant dans une grande
  masse de la poudre à canon", while "à l'égard des principes ou choses
  simples, rien de semblable ne sçauroit arriver" (p. 54; OCR "scauroit").
- **What it commits him to.** A law of motion is tested from outside,
  before any inner discussion ("preuve ou examen ... avant même que de venir
  à une discussion interieure"), by whether its outcomes converge when its
  cases do. Rest is the limit of slow motion and equality the limit of
  inequality, and a rule that jumps at either is ill made. Composite
  amplifiers may magnify small differences into large effects; simple
  principles may not jump.
- **What the theorem does with it.** Leibniz applies the test to
  collision velocities, the geometric reading, and Newton's laws pass it
  on both branches. His phrase measures the difference *in datis* by
  discernibility: the nearly equal collision can scarcely be told from the
  equal one. The records reading applies the same measure *in quaesitis*,
  and that transfer is ours. Proposition L shows what the test then
  demands: for Newton's comparison and for Zeno's rung, continuity of the
  best verdict holds exactly when $\kappa>0$. The exemption marks the boundary
  of the argument. An instrument is a composite amplifier, and finite
  amplification is allowed; the zero branch needs the supremum over all
  instruments the laws permit to jump, a jump in what the laws allow to be
  recorded, which is the level of principle if the mark trade-off is a law.
  That mapping of Leibniz's line between composites and simple principles
  onto the line between one instrument and the laws' supremum is ours, and
  it has a counter-reading: Leibniz exempts effects for which "on en peut
  rendre raison par les principes generaux mêmes" (p. 54), and a Leibnizian
  can explain the $\kappa=0$ jump from $\kappa=0$ mechanics by ever finer instruments.
  Whether the verdict of the best possible record counts among "ce qui en
  resulte" is the premise, now stated in Leibniz's terms. The theorem also
  confines the reading: for static shapes the records reading fails on
  both branches. Leibniz applies the law to geometry and physics alike
  ("absolument necessaire dans la Geometrie, mais il reussit encor dans la
  physique", p. 52), so the confinement to motions is a physical choice of
  ours, resting on back-action; its textual defence is that Leibniz uses the
  law as a test of laws of nature, and a taper is a datum rather than a law.

Prior art, at metadata level (Crossref verified 2026-09-29 where a DOI is
given): Mortensen, "The Leibniz Continuity Condition, Inconsistency and
Quantum Dynamics",
[*J. Philos. Logic* **26** (1997), 377--389](https://doi.org/10.1023/A:1004275928191),
treats the condition against quantum jumps at the instant of change; the
pairing of continuity with the identity of indiscernibles is Chapter V of
Russell, *A Critical Exposition of the Philosophy of Leibniz* (1900).
Leibniz repeats the test against Descartes's rules of collision in the
*Animadversiones in partem generalem Principiorum Cartesianorum* (1692) and
the *Specimen dynamicum* (1695), so the 1687 "preuve ou examen" is a settled
method (recalled, not read here). The condition used here is continuity of
the parametrized family of recorded states in statistical distance
([Wootters 1981](https://doi.org/10.1103/PhysRevD.23.357);
[Braunstein and Caves 1994](https://doi.org/10.1103/PhysRevLett.72.3439)),
in which classical pure states are pairwise perfectly distinguishable. It is
weaker than Hardy's continuity axiom, which asks for a continuous reversible
transformation between pure states (see the
[Hardy audit](quantum-exclusion-premises.md)); continuity axioms separate
classical from quantum theory also in
[Masanes and Müller 2011](https://doi.org/10.1088/1367-2630/13/6/063001) and
[Chiribella, D'Ariano and Perinotti 2011](https://doi.org/10.1103/PhysRevA.84.012311).

## 2b. Leibniz, 1676: little rests, leaps and the animalcula

Leibniz, *Pacidius Philalethi. Prima de motu philosophia*, headed "Scripta
in navi qua ex Anglia in Hollandiam trajeci. 1676 Octob.", in Couturat,
*Opuscules et fragments inédits* (1903), 594--627
([companion](../docs/classics/Leibniz_Pacidius_1676_Couturat1903_OCR.md);
passage, OCR normalized by hand).

- **The text.** "Ex veteribus Empedocles et ex recentioribus docti quidam
  Viri quietulas quasdam interspersas asseruêre" (p. 605), because they
  "capere non potuerunt quomodo motus unus alio celerior esse possit, sine
  quiete interspersa" (p. 606). Charinus concedes the regress: "tametsi
  indefinite progrederer subdividendo ac quietulas indefinite exiguas atque
  indesignabiles, motulis ejusdem naturae miscerem, opus tamen et
  tempusculis atque lineolis foret" (p. 606), and a rotating radius gives
  unequal speeds without any rest. A leap is transcreation: the body is
  "extingui et annihilari, et in B momento post iterum emergere ac recreari"
  (p. 617). Against it, "cùm enim magnitudo aut parvitas nihil ad rem
  faciat", animalcula as much smaller than us as a head is than the earth
  would find the same absurdity in their leaps, "omnia proportione sibi
  respondent", so the leaps are "semper ad minora ac minora propelli et
  nusquam consistere posse in natura rerum ... nulla autem ratio est, cur
  huic potius quàm illi corpusculorum gradui saltus illi miraculosi
  ascribantur, nisi atomos scilicet admittamus" (pp. 617--618). Leibniz
  denies such atoms by the same argument.
- **What it commits him to.** Speed differences need no rests; rests mixed
  with motions either concede continuous motion or require leaps; a leap of
  any size needs a privileged grade of bodies, which sufficient reason
  refuses; hence no leaps, eleven years before the law of continuity.
- **What the theorem does with it.** The little rests are the
  velocity-switching processes of the [telegraph](telegraph-return-bridge.md)
  and [checkerboard](checkerboard-dynamics.md) notes: motion at one speed
  whose state switches at a rate $\omega=mc^2/K$ (there between the two
  directions; between motion and rest the structure is the same), with the
  mean speed set by the mixture.
  Charinus's regress, rests made indefinitely small among little motions, is
  the limit $K\to0$, which converges to continuous motion at the mean speed;
  the regress is a limit, and its end is the zero branch. The radius answers
  the motive for the rests and leaves the rate open. Transcreation below the
  mesh is the paper's reading of al-Nazzam's leap. The animalcula argument
  is sound against a leap of fixed size: Newton's mechanics has the
  two-parameter similarity $x\to\lambda x$, $t\to\mu t$ (the dilations of the
  [fifth-postulate note](principia-fifth-postulate.md), the zoom of the
  [tangent-groupoid note](tangent-groupoid-trajectories.md)), and a length
  breaks it. A floor on action fixes no length. Under $x\to\lambda x$, $t\to\lambda^2t$ at
  fixed mass, $F\to F/\lambda^3$ and $K_\tau=F^2\tau^3/(24m)$ is invariant, as is $mv^2\tau$, so
  animalcula scaled this way reach the same verdicts in the corresponding
  cases: "omnia proportione sibi respondent" survives on a one-parameter
  subgroup, the diffusive scaling of quantum paths. The dilemma between
  atoms and no leaps omits this option. What sufficient reason then asks
  for is a reason for an action scale. The composition results give one
  constant for all bodies ([rotation composition](rotation-composition-universality.md);
  $\kappa=mD$ in the [stochastic route](stochastic-route-velocitas-ultima.md)),
  so that scale converts units of mass, length and time and its value is a
  convention. The question sufficient reason leaves is zero or positive,
  which §1 settles for motions under the records reading of the 1687 law.
  Leibniz between 1676 and 1704 thus supplies the objection and the reply:
  proportion forbids a privileged size, which a floor on action does not
  need, and continuity of outcomes read on discernibility requires the floor.

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
- **What the theorem does with it.** The mark model makes the addition
  exact. A single cut at fraction $s$ carries the discernibility
  $3s(1-s)K_\tau/\kappa$ (Proposition L), which is the share of Newton's cell action
  that the [cut measure](cut-measure-newton.md) assigns to that cut
  (Theorems 1--2), and nested cuts add their shares toward $K_\tau/\kappa$ in the
  balanced dense limit (the orthogonal hats of Theorem 2 there;
  Proposition 4 gives the same decomposition as Cameron--Martin energy).
  The doctrine has two halves, and they fall differently. "Cent mille
  riens ne sauroient faire quelque chose" asks that every share be
  positive, which holds for every $\kappa\ge0$. "Insensible alone" asks that a
  share be unable to decide by itself, and that half selects the floor:
  with $\kappa>0$ a cut shorter than the mark mesh cannot exhibit the force alone
  and contributes in the assembly, while with $\kappa=0$ a single cut decides and
  records of motion have no insensible parts. The zero branch can still
  place insensibility in the perceiver, as Leibniz's confusion of created
  substances does, graded from one substance to another; the
  [stochastic route](stochastic-route-velocitas-ultima.md) shows how
  composition turns graded constants into one ($\kappa=mD$ for every body), and
  the step from confused perceivers to one universal floor is recorded here
  as a reading. The maxim on motion from rest is Galileo's passage through all
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
  Proposition L put no floor on it, and Newton's scholium to Lemma XI
  declines the question that makes the wonder: ultimate ratios are limits of
  ratios, never ratios of ultimate quantities, so the ratio of sections is 1
  at every cut and point and circle are never compared. Leibniz takes the
  opposite side from Galileo in 1687, without engaging his paradox:
  equality is an infinitely small inequality, so the attributes extend to
  the limiting case by continuity.
- **Cavalieri's reply** (letter 2992 of 1634, Opere XVI 136--138;
  [companion](../docs/classics/Galileo_Opere_XVI_indivisibles_letters_1634-1636_OCR.md)).
  Equal parts are removed "essendo noi arrivati al nullo piano tanto nel
  cono quanto nella scodella", and "non mi dichiaro di componere il continuo
  d'indivisibili, ma solo mostro che i continui hanno la proportione delli
  aggregati di questi indivisibili". *Commitment:* ratios of aggregates of
  sections, with no claim of composition. *The theorem:* the cut measure keeps exactly this stance, a statement
  about aggregates of cuts (shares summing to $K_\tau$ for every schedule); it
  composes no continuum, and the mark mesh bounds exhibition while leaving
  division free.
- **Galileo's wheel** (Favaro VIII, 69--72, same companion). A smaller
  concentric wheel covers the larger wheel's line with its own sides "con
  l'interposizione di cento mila spazii vacui traposti", and for circles
  "sì come i lati non son quanti, ma bene infiniti, così gl'interposti vacui
  non son quanti, ma infiniti"; Simplicio hears in it "quei vacui
  disseminati di certo filosofo antico", and Salviati's retort about the one "il quale negava la Providenza
  divina" points to Epicurus without naming him. *Commitment:* a continuum composed of
  infinitely many unquantified indivisibles, partly full and partly void,
  crossed by leaps across the voids. *The theorem:* in 1638 Galileo publishes as consistent a structure that
  converges with al-Nazzam's leap; no transmission evidence is known, and
  the entry records convergence. The paper's reading of the leap applies: below the mesh a record is consistent with a leap, the interval
  stays divisible, and the crossing is exhibited in finitely many steps.
- **Guldin** (*Centrobaryca* IV, 1641, preface p. 4;
  [companion](../docs/classics/Guldin_Centrobaryca_LiberIV_1641_pages.md)):
  "Galileus profecto in eodem Dialogo de Motu locali, disputans de
  infinito, de proprietatibus finitorum, quas infinitis applicare minime
  liceat, contra ipsum concludit." (The companion's transcription is read
  from the page images by one reader.) *Commitment:* Galileo's own principle
  refutes Cavalieri. *The theorem:* it sides with Guldin and Newton on
  composition (no least magnitude follows from $\kappa$) and with Cavalieri on
  ratios of aggregates.

The four entries share one feature that sharpens the paper's §9. The
seventeenth-century dispute Newton answered concerned static figures, and
there the theorem agrees with his answer and imposes nothing. The floor
enters only where a record carries back-action, in the lemmas applied to
motion, and the dispute about motion is the one he passed over.

## 5. Consequence for STATE

For the Newton goal: for the observer ignorant of the preparation, using
non-adaptive protocols, positivity of the action floor is equivalent in the
mark model to the records reading of Leibniz's 1687 law of continuity for
laws of motion (Proposition L). The zero branch keeps
the geometric reading, which Leibniz himself applied, so the fork stands;
it now lies between a reading Leibniz made and one he did not, with his
measure of the cases, "à peine distingué", and the "insensible alone" half
of his doctrine of small perceptions on the side of the floor, and statics
showing why the reading must be confined to motions, by a physical choice
of ours. A single cut carries exactly the cut measure's share of the
discernibility, a result of the mark model worth citing on its own. For the scholion: three Leibniz entries (1676, 1687, 1704) and the
Galileo--Cavalieri--Guldin layer are supplied with their three obligations;
the paper's §9 carries a pointer. §§1--4 are refereed (Fable, REFINE,
applied); §2b awaits a referee.
