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
two marks. Any finite schedule of marks reaches exactly the cut measure's
spent action over $\kappa$, so a single cut at fraction $s$ carries
$d^2=3s(1-s)K_\tau/\kappa$ ([cut-measure note](cut-measure-newton.md), Proposition 7). Static shapes behave
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
(§2b). Newton's own Rule III (1713) separates division by reason, certain,
from division by the powers of nature, "incertum", to be settled by one
experiment (§4b), and his *Opticks* posits the permanent least bodies that
the *Pacidius* named, for the sake of lasting natures (§4c). Galileo in 1638
already argues the beginning of fall from the graded vanishing of its
record, the records reading in practice (§4d). The Newton-age dispute
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
continuity axioms is added. A second pass on §§2b, 4b and 4c (same day):
REFINE, applied; page and speaker corrections in the *Pacidius*, the Kepler
scaling corrected to $\lambda r(\lambda^{-3/2}t)$, the "convention" of the floor's value
qualified against a fourth constant ($e^2/(\kappa c)$), Corollary 3 read as a
confidence bound, the transfer of Rule III from parts of bodies to records
marked as ours, and Quaestio 23 of the 1706 *Optice* named.

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
$d^2=N\vartheta^2\Delta h^2/(2\delta^2)$, unbounded in $N$ whatever $\kappa$ is. The single cut is the case $N=2$ of Proposition 7 of the cut-measure note,
which treats every finite schedule. $\square$

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
statement about the preparation-ignorant observer. That observer is
Newton's in Book III, who reads forces from the phenomena, motions nobody
prepared; §10 of the paper prices the preparation route by the body's
spread along the way.

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
  and that transfer is ours. It has one textual support: Leibniz
  individuates things by discernible difference, "deux choses individuelles
  ne sauroient estre parfaitement semblables" (1704, §3), so results that
  differ are, for him, results that can in principle be told apart. A
  second support is an argument of ours from the law's general form,
  "Datis ordinatis etiam quaesita sunt ordinata": data and results are
  ordered alike, and measuring the data by discernibility while measuring
  the results by position mixes two orders.
  Proposition L shows what the test then
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
  (p. 617). Against it Charinus: "cùm enim magnitudo aut parvitas nihil ad
  rem faciat", animalcula as much smaller than us as a head is than the
  earth would find the same absurdity in their leaps, "omnia proportione
  sibi respondent" (p. 617); and Pacidius: the leaps are "semper ad minora
  ac minora propelli et nusquam consistere posse in natura rerum ... nulla
  autem ratio est, cur huic potius quàm illi corpusculorum gradui saltus
  illi miraculosi ascribantur, nisi atomos scilicet admittamus" (p. 618).
  Leibniz denies such atoms by the same argument. (Couturat's angle
  brackets for Leibniz's additions are dropped; the heading "Scripta in
  navi", p. 594, lies outside the local excerpt and is taken from the
  companion's metadata.)
- **What it commits him to.** Speed differences need no rests; rests mixed
  with motions either concede continuous motion or require leaps; a leap of
  any size needs a privileged grade of bodies, which sufficient reason
  refuses; hence no leaps, eleven years before the law of continuity.
- **What the theorem does with it.** The little rests are the
  velocity-switching processes of the [telegraph](telegraph-return-bridge.md)
  and [checkerboard](checkerboard-dynamics.md) notes: motion at one speed
  whose state switches at a rate $\omega=mc^2/K$ (there between the two
  directions; between motion and rest the structure is the same), with the
  mean speed set by the mixture; with one rate and symmetric switching the
  mean speed is fixed, so speed differences need state-dependent weights,
  the signed amplitudes of the checkerboard, which is where Leibniz's
  "capere non potuerunt" bites.
  Charinus's regress, rests made indefinitely small among little motions, is
  the limit $K\to0$, which converges to continuous motion at the mean speed;
  the regress is a limit, and its end is the zero branch. The radius answers
  the motive for the rests and leaves the rate open. Transcreation below the
  mesh is the paper's reading of al-Nazzam's leap. The animalcula argument
  is sound against a leap of fixed size: Newton's mechanics has the
  two-parameter similarity $x\to\lambda x$, $t\to\mu t$ (the dilations of the
  [fifth-postulate note](principia-fifth-postulate.md), the zoom of the
  [tangent-groupoid note](tangent-groupoid-trajectories.md)), and a length breaks it. A floor on action fixes no length of its own; a
  length appears only with a force and a mass, as the mesh $\tau_*$ and its
  sagitta do. Under $x\to\lambda x$, $t\to\lambda^2t$ at
  fixed mass, $F\to F/\lambda^3$ and $K_\tau=F^2\tau^3/(24m)$ is invariant, as is $mv^2\tau$, so
  animalcula scaled this way reach the same verdicts in the corresponding
  cases: "omnia proportione sibi respondent" survives on a one-parameter
  subgroup, the diffusive scaling of quantum paths. The dilemma between
  atoms and no leaps omits this option. What sufficient reason then asks
  for is a reason for an action scale. The composition results give one
  constant for all bodies ([rotation composition](rotation-composition-universality.md);
  $\kappa=mD$ in the [stochastic route](stochastic-route-velocitas-ultima.md)),
  so that scale converts units of mass, length and time, and its value is a
  convention of units so long as no second dimensionful constant forms a
  pure number with it: Newton's $G$ and $c$ do not, and the charge $e$ of §4c
  does, through $e^2/(\kappa c)$. The composition results rest on stated premises
  (interaction between bodies in the rotation note, the composition
  premises of the stochastic route), and both admit zero. The question sufficient reason leaves is zero or positive,
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
  exact. The best discernibility of any finite schedule of marks is the
  Newton cell action its cuts spend, over $\kappa$, and each added mark adds
  exactly its cut's share $3s(1-s)K_{\tau_i}/\kappa$, at every finite stage
  ([cut measure](cut-measure-newton.md), Proposition 7, with Theorems 1--2
  there; Proposition 4 gives the same decomposition as Cameron--Martin
  energy).
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

## 4b. Newton, Rule III (1713; 1726): division by reason and by nature

Newton, *Principia*, third edition (London, 1726), Book III, Regula III,
pp. 387--389; the commentary is already in the second edition (1713)
([companion](../docs/classics/Newton_Principia_1726_RegulaIII_la_OCR.md);
passage, OCR normalized by hand).

- **The text.** "Qualitates corporum quae intendi & remitti nequeunt,
  quaeque corporibus omnibus competunt in quibus experimenta instituere
  licet, pro qualitatibus corporum universorum habendae sunt" (p. 387),
  since "quae minui non possunt, non possunt auferri" and the analogy of
  nature is "simplex ... & sibi semper consona" (p. 388). Then: "partes
  indivisas in partes minores ratione distingui posse ex mathematica certum
  est. Utrum vero partes illae distinctae & nondum divisae per vires naturae
  dividi & ab invicem separari possint, incertum est. At si vel unico
  constaret experimento ..." (p. 388).
- **What it commits him to.** Qualities that admit no degrees and are found
  in every body within reach of experiment belong to all bodies, least
  parts included, because what cannot be diminished cannot be taken away.
  Division by reason is certain; division by the powers of nature is an
  empirical question, and one experiment would settle it.
- **What the theorem does with it.** The second commitment is the
  theorem's own division of labour. Geometry stays divisible (the paper's
  Proposition 1; the cut measure's shares for every schedule), and the mark
  mesh concerns what nature's powers can exhibit, which Newton declares
  uncertain and empirical. His single experiment has a counterpart here: the exhibition of a force by
  marks confined to a window shorter than $\tau_*$ (the paper's Corollary 3).
  Corollary 3 is a confidence bound, so one such exhibition at confidence
  $1-\epsilon$ refutes the floor at that $\kappa$ and lowers it; the passage to $\kappa=0$
  is the same rule-based step Newton takes to "in infinitum". Rule III
  speaks of the parts of bodies, and carrying division by nature's powers
  from parts of bodies to the division of a motion's record is our transfer. The first commitment meets the composition results. One constant
  for all bodies ($\kappa=mD$ in the stochastic route; rotation composition)
  makes the floor a quality without degrees in Rule III's sense ("quae
  intendi & remitti nequeunt"), so Rule III carries it from the bodies
  within reach of experiment to all bodies, and
  "quae minui non possunt, non possunt auferri" forbids taking it to zero in
  the least parts. Newton's rules thus make positivity empirical and universalize it once it
  is found in every body tested, which composition reduces to one body and
  its interactions; the settlement itself is experimental. This changes an
  attribution in the paper: the zero branch is the default reading of Book
  I's geometry, whose scholium (1687) treats vanishing quantities,
  "diminuendas sine limite", while Rule III (1713) leaves the division of
  material parts to experiment; its extension from matter to motion is ours.

**Newton on distinguishing motions.** The Scholium to the Definitions
(1726, pp. 9--11, same companion; the passage stands in the first edition,
recalled) sorts true from relative motion by what distinguishes them:
"Causae, quibus motus veri & relativi distinguuntur ab invicem, sunt vires
in corpora impressae ad motum generandum. Motus verus nec generatur nec
mutatur, nisi per vires in ipsum corpus motum impressas" (p. 9);
"Effectus, quibus motus absoluti & relativi distinguuntur ab invicem, sunt
vires recedendi ab axe motus circularis ... majores vel minores pro
quantitate motus" (p. 10); "Motus quidem veros corporum singulorum
cognoscere, & ab apparentibus actu discriminare, difficillimum est ...
Causa tamen non est prorsus desperata" (p. 11). Newton compares motions by
the effects that distinguish them, graded by the quantity of motion, which
is the Galileo comparison's question in his words: whether an impressed
force acts is decided by its effects. On the zero branch his
"difficillimum" is a practical difficulty; on the floor branch it becomes a
bound, the mesh below which no record decides at a given confidence.

## 4c. Newton, Query 31: permanent least bodies

Newton, *Opticks*, fourth edition (London, 1730), Book III, Query 31,
verbatim from the Project Gutenberg transcription
([companion](../docs/classics/Newton_Opticks_1730_fits_and_queries.md);
passage). The query goes back to Quaestio 23 of the Latin *Optice* (1706),
renumbered 31 in the English edition of 1717 (recalled, not read here).

- **The text.** "God in the Beginning form'd Matter in solid, massy, hard,
  impenetrable, moveable Particles, of such Sizes and Figures ... even so
  very hard, as never to wear or break in pieces; no ordinary Power being
  able to divide what God himself made one in the first Creation. While
  the Particles continue entire, they may compose Bodies of one and the
  same Nature and Texture in all Ages ... that Nature may be lasting, the
  Changes of corporeal Things are to be placed only in the various
  Separations and new Associations and Motions of these permanent
  Particles."
- **What it commits him to.** Least bodies of fixed sizes and figures,
  indivisible by any ordinary power, as the ground of the sameness of
  natures through time; all change is rearrangement and motion.
- **What the theorem does with it.** These are the atoms that the
  *Pacidius* names as the only reason to ascribe leaps to one grade of
  bodies, and Newton holds them, so on Leibniz's own terms Newton could
  place a floor at the atomic grade. The theorem needs no grade (§2b): a
  floor on action fixes no length, and Newton's particles supply lengths,
  one per species, with no universal action. His reason for them is
  stability, sameness of natures in all ages, and that reason does ask for
  a scale. In the mechanics of the *Principia* a body bound by an
  inverse-square force has no preferred size (if $r(t)$ is an orbit, so is $\lambda r(\lambda^{-3/2}t)$, Kepler's third law), so identical sizes for bound systems of one kind need a
  constant beyond Newton's. He supplies hardness by fiat. The
  [relativistic Kepler note](relativistic-kepler-threshold.md) shows that
  finite propagation speed, which Newton accepts (*Opticks* II.iii Prop.
  XI), turns singular inverse-square binding into an action threshold $|L|>k/c$;
  the threshold fixes no size, since circular radii still range over
  $(0,\infty)$ for $|L|>k/c$, and an action constant of the quantum kind fixes
  sizes dynamically, Bohr's radius $a_0=\hbar^2/(m_ee^2)$ in Gaussian units being the
  standard case. Query 31 thus states, as a premise about matter, the need
  for a scale that the Galileo comparison states as a premise about
  records. The two premises are independent: Query 31 posits lengths, the
  Galileo comparison an action, and each text stops at its own. Its "no ordinary Power" agrees with Rule III's "per vires naturae
  ... incertum": division by nature is bounded by the powers available,
  the form the floor takes as a law about what nature can exhibit.

## 4d. Galileo, 1638: the beginning of fall read from its record

Galileo, *Discorsi*, Giornata terza, Favaro VIII, 198--200
([companion](../docs/classics/Galileo_Discorsi_GiornataTerza_Favaro_it_wikisource.md);
passage, from the Wikisource transcription).

- **The text.** Sagredo: a body falling from rest passes through every
  degree, "grado alcuno non sia di velocità così piccolo, o vogliamo dir di
  tardità così grande, nel quale non si sia trovato costituito l'istesso
  mobile dopo la partita dall'infinita tardità, cioè dalla quiete", which
  the imagination resists "mentre che il senso ci mostra, un grave cadente
  venir subito con gran velocità" (pp. 198--199). Salviati answers with a
  stake driven into yielding ground: from a finger's height, "che farà di
  più che se, senza percossa, vi fusse posto sopra? certo pochissimo: ed
  operazione del tutto impercettibile sarebbe, se si elevasse quanto è
  grosso un foglio. E perché l'effetto della percossa si regola dalla
  velocità del medesimo percuziente, chi vorrà dubitare che lentissimo sia
  'l moto e più che minima la velocità, dove l'operazione sua sia
  impercettibile?" (p. 200). And from reason: since velocity is "augumentabile
  e menomabile in infinito", no reason makes the body enter ten degrees
  rather than four, two, one, a half, a hundredth (p. 200).
- **What it commits him to.** The beginning of fall passes through all
  degrees of slowness; the effect of a percussion is graded by the
  velocity and vanishes, to sense, for the smallest drops; from an
  imperceptible effect one may infer a minimal velocity; and sufficient
  reason forbids a jump into any finite degree.
- **What the theorem does with it.** Galileo argues the continuity of the
  motion from the graded vanishing of its record, outcomes measured by how
  perceptible they are, which is the records reading of §2 practised
  forty-nine years before Leibniz published the law. The fall from rest is
  Newton's comparison with the initial velocity zero, $F=mg$ and
  $\tau=\sqrt{2h/g}$, so $K_\tau=m\,g^{1/2}(2h)^{3/2}/24$, and Corollary 3 of the paper gives,
  on the floor branch and for an observer ignorant of the initial state, a
  least height below which no record decides at confidence $1-\epsilon$ that the
  weight fell rather than was set down:
  $$h_*=\tfrac12\bigl(96\,z_{1-\epsilon}^2\,\kappa/(m\,g^{1/2})\bigr)^{2/3},$$
  about $2\times10^{-22}$ m for a kilogram with $\kappa=\hbar/2$ and $z\approx2$. Galileo's sheet of
  paper is therefore a threshold of sense, some eighteen orders of
  magnitude above the threshold of law, and his inference from
  imperceptible to minimal holds on both branches. What the floor adds is
  that the imperceptibility of the smallest drops becomes a law for the
  preparation-ignorant observer; Galileo's release from rest is a known
  preparation, which §10 of the paper prices separately. His argument from
  reason is the one the *Pacidius* repeats (§2b), and it rules out a jump
  into a finite degree of speed, which a floor on records does not assert.

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
discernibility, a result of the mark model worth citing on its own. Newton's Rule III places the physical limit among empirical questions and
supplies, with the composition results, the rule that universalizes a
floor found in every body tested, so the zero branch is the default reading
of Book I's geometry; Newton's stated physics in Book III leaves the
division of material parts to experiment. For the
scholion: three Leibniz entries (1676, 1687, 1704), Newton's Rule III and
Query 31, Galileo's stake (1638), and the Galileo--Cavalieri--Guldin layer
are supplied with their three obligations;
the paper's §9 carries a pointer. §§1--4 are refereed (Fable, REFINE,
applied), and §§2b, 4b and 4c by a second Fable pass (REFINE, applied); §4d awaits a referee.
