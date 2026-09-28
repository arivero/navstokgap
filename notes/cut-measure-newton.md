# Newton's cell action as a measure on cuts

**After refereeing (Fable, 2026-09-28).** Theorems 1--2, Corollary 3's
arithmetic and the quotations were re-derived and accepted. Corrections
applied: Proposition 4 now names the Kullback--Leibler divergence, the
shift $\delta x$, the phase $K_\tau/\varepsilon$ and the Cameron--Martin normalizer, and its
link to Rivero 1998 is stated as a counterpart; Corollary 5 separates a
floor on a cell's action from a floor on a cut's share (a factor $\frac34$ for
halving); §3 labels the two-quarter-cut schedule a construction and adds
the alternating reading favoured by 𣃈必半; the Lévy--Ciesielski comparison
names the right quantity.

**Result, 2026-09-27 (atlas §1b, user remarks on arbitrary cuts and on
the rod).** Let a constant force $F$ act on a body of mass $m$ over a cell
of duration $\tau$, and let $\delta x$ be the chord minus the parabola (the chord
is the inertial comparison path with the same endpoints). Its Galileo action

$$K_\tau=\frac m2\int_0^\tau\dot{\delta x}^2\,dt=\frac{F^2\tau^3}{24m}$$

(the [two-path note](galileo-two-path-interference.md) writes the same
quantity as $(F/4v)A=\tau\Delta E/12$) behaves as a measure on the process of
cutting the cell.

- **Theorem 1 (one cut).** A cut at fraction $s\in(0,1)$ spends exactly
  $3s(1-s)K_\tau$, and this share equals the Cameron--Martin energy
  $\frac m2\int\dot\phi^2$ of the Schauder hat $\phi$ that the cut inserts, of height
  the sagitta $Fs(1-s)\tau^2/(2m)$.
- **Theorem 2 (any cut sequence).** The hats of successive cuts are
  orthogonal in the energy $\int\dot f\dot g$, so the spent shares add. Along any
  sequence of cuts, at any positions and in any order, the total spent
  equals $K_\tau-\sum_iK_{\tau_i}$ over the current pieces, and it tends to $K_\tau$
  iff the mesh $\max_i\tau_i$ tends to zero; the remainder is at most
  $K_\tau\max_i\tau_i^2/\tau^2$.
- **Corollary 3 (the rod and the Mohist schedules).** Halving only the
  remaining piece each day, the schedule of the stick in *Zhuangzi* 33,
  spends $\frac67K_\tau$, and so does one halving a day taken alternately from
  the front and the back. Removing a quarter from each end each day (two
  quarter-cuts a day, a construction motivated by the Mohist "taking from
  front and back") spends $\frac{27}{28}K_\tau$. All three leave a definite share
  unspent forever, because they keep cut-off pieces of fixed length.
- **Proposition 4 (weight of a cut).** Under the Euclidean path measure
  of a free particle with diffusion constant $\hbar/m$ (Wiener measure), the
  force signal in one cut has Kullback--Leibler divergence exactly
  (spent share)$/\hbar$. In real time the same share, divided by the action
  resolution, is the phase of the two-path comparison.
- **Proposition 6 (the mark mesh as a Cameron--Martin threshold;
  2026-09-28, not refereed).** Under the same path measure, the optimal
  equal-prior test between force $F$ and no force in a cell, observing the
  whole path with pinned ends, errs with probability $\Phi(-\sqrt{K_\tau/2\hbar})$. It
  reaches $\epsilon$ iff $K_\tau\ge2z_{1-\epsilon}^2\hbar$, which is exactly the Planck paper's mark
  mesh $\tau_*=(48z_{1-\epsilon}^2m\hbar/F^2)^{1/3}$, obtained there from real-time Gaussian
  marks with Robertson's bound.
- **Corollary 5 (a floor counts the cuts).** If every exhibited cut must
  spend at least an action $\kappa>0$, at most $K_\tau/\kappa$ cuts can be exhibited,
  whatever the schedule. For halving refinement, level $n$ is exhibited
  iff $\frac34K_\tau8^{-n}\ge\kappa$. The Planck paper's mark mesh
  $\tau_*=(48z_{1-\epsilon}^2m\hbar/F^2)^{1/3}$ is the cell whose action is $2z_{1-\epsilon}^2\hbar$;
  its own halving spends $\frac32z_{1-\epsilon}^2\hbar$.

Theorems 1 and 2 are elementary, and their content lies in the reading
they give: Newton's refinement is a process that spends a fixed, finite
action, with the nested additivity of the Lévy--Ciesielski construction
of the Brownian bridge. Proposition 4 makes the correspondence exact: the
action is the Cameron--Martin energy of the force's shift, decomposed
over the hats. Corollary 5 is a consistency statement. It says where
a floor, if present, stops the cutting, and leaves the necessity question
of the [fifth-postulate note](principia-fifth-postulate.md) where it was.

## 1. One cut

Put $C=F^2/(24m)$, so $K_\tau=C\tau^3$. On $[0,\tau]$ the parabola with
acceleration $F/m$ and the chord through its endpoints differ by

$$\delta x(t)=\frac F{2m}\,t(\tau-t),\qquad
\dot{\delta x}(t)=\frac Fm\Bigl(\frac\tau2-t\Bigr),$$

so $\frac m2\int_0^\tau\dot{\delta x}^2dt=\frac m2\cdot\frac{F^2}{m^2}\cdot\frac{\tau^3}{12}=C\tau^3$.

Cut at $t_c=s\tau$. The polygon through the three points $0,s\tau,\tau$
differs from the chord by the hat $\phi$ of height
$h=\delta x(s\tau)=Fs(1-s)\tau^2/(2m)$, linear on $[0,s\tau]$ and on $[s\tau,\tau]$. The
polygon differs from the parabola, on each piece, by the chord-minus-
parabola of that piece: $\delta x=\phi+\delta x_1+\delta x_2$ with $\delta x_j$ supported on
piece $j$ and vanishing at its ends.

*Orthogonality.* $\dot\phi$ is constant on each piece and $\int_{\rm piece}\dot{\delta x_j}=0$, so
$\int\dot\phi\,\dot{\delta x_j}=0$; the $\delta x_j$ have disjoint supports. Hence

$$K_\tau=\frac m2\int\dot\phi^2+K_{s\tau}+K_{(1-s)\tau}.$$

*The hat's energy.* $\frac m2\int\dot\phi^2=\frac m2h^2\bigl(\frac1{s\tau}+\frac1{(1-s)\tau}\bigr)
=\frac{mh^2}{2s(1-s)\tau}=\frac{F^2s(1-s)\tau^3}{8m}=3s(1-s)C\tau^3.$
The same number follows from $\tau^3=(s\tau)^3+((1-s)\tau)^3+3s(1-s)\tau^3$, which is the
algebraic form of Theorem 1. The share is largest for halving, $\frac34K_\tau$. $\square$

## 2. Any cut sequence

Each later cut acts inside one current piece, and Theorem 1 applies to
that piece with its own $s$. The new hat is supported in the piece and
vanishes at its ends; every earlier hat is linear there. The argument of
§1 gives orthogonality to all earlier hats and to the other pieces'
remainders. After any finite set of cuts, with pieces $\tau_i$ ($\sum\tau_i=\tau$),

$$K_\tau=\sum_{\rm cuts}\frac m2\int\dot\phi_{\rm cut}^2+\sum_iK_{\tau_i},\qquad
\sum_iK_{\tau_i}=C\sum_i\tau_i^3\le C\tau\max_i\tau_i^2 .$$

The remainder vanishes iff the mesh does ($\sum_i\tau_i^3\ge(\max_i\tau_i)^3$). The
positions and the order enter only through which pieces are cut, never
through the total. $\square$

This is the Schauder (Lévy--Ciesielski) expansion of $\delta x$ in the
Cameron--Martin space $H^1_0[0,\tau]$, adapted to an arbitrary nested cut
sequence; for dyadic cuts it is the textbook expansion
([Ciesielski 1961](https://doi.org/10.1090/S0002-9947-1961-0132591-2); metadata). The
[reachability note](reachable-cut-composition.md) has the same cubic law
for the area $2F^2t^3/(3m)$ of the reachable lens of a cut. The bridge's own
conditional variance shows the same nested additivity with a quadratic
law: for diffusion constant $D$, $\int_0^L{\rm Var}(X_u\mid{\rm ends})\,du=DL^2/6$, and a cut
at fraction $s$ removes $Ds(1-s)L^2/3$ of it.

## 3. The rod and the two Mohist schedules

*Zhuangzi* 33 (dialecticians' list,
[text](../docs/classics/Zhuangzi_33_Tianxia_zh_wikisource.md)):
一尺之捶，日取其半，萬世不竭, "a one-foot stick, each day take half, in ten
thousand generations it is not exhausted." Mohist Canon B (B60 in
Graham's numbering; [canon](../docs/classics/Mozi_Canons_B_JingXia_zh_wikisource.md)):
非半弗𣃈，則不動，說在端, "without halving there is no cutting and no
moving; the explanation lies in the point (端)", with the explanation
([text](../docs/classics/Mozi_Canons_B_Explanations_JingShuoXia_zh_wikisource.md))
前則中無爲半，猶端也。前後取，則端中也 (working gloss: "going forward, at the
middle nothing serves as a half: it is like a point; taking from front
and back, the point is in the middle"), which continues 𣃈必半, "cutting
must be by halves".

*One-ended schedule.* Day $k$ halves the remaining piece, of length
$\tau2^{-(k-1)}$, and spends $\frac34C\tau^38^{-(k-1)}$. The total is
$\frac34\cdot\frac87K_\tau=\frac67K_\tau$; the pieces taken away keep $\sum_{k\ge1}8^{-k}K_\tau=\frac17K_\tau$.

*Alternating schedule* (the reading favoured by 𣃈必半). One halving a
day, taking the half alternately from the front and from the back. Each
day is one halving of the remaining piece, so the spending is that of the
one-ended schedule, $\frac67K_\tau$; the remainder converges to the point
$\frac\tau2+\frac\tau8+\dots=\frac{2\tau}3$.

*Two quarter-cuts a day* (a construction motivated by 前後取; the text does
not fix the fractions). Day $k$ cuts the remaining piece $r=\tau2^{-(k-1)}$ at
$s=\frac14$ and $s=\frac34$, keeping the middle half. The two cuts spend
$C r^3\bigl(1-2\cdot\frac1{64}-\frac18\bigr)=\frac{27}{32}Cr^3$ (equivalently $\frac9{16}+\frac9{32}$ by two applications
of Theorem 1), and the total is $\frac{27}{32}\cdot\frac87K_\tau=\frac{27}{28}K_\tau$, with $\frac1{28}K_\tau$ kept
in the pieces taken away. The contrast $\frac67$ against $\frac{27}{28}$ is between one
half-cut and two quarter-cuts a day, whichever ends are cut.

All three schedules converge to a point, the Mohist 端: the end, the
point $2\tau/3$, and the midpoint. If 中 in 端中 means the midpoint, the
explanation fits the symmetric schedule, while 𣃈必半 fits the alternating
one. What each author is
committed to, and what the theorem does with it:

- The dialecticians hold that the halving never ends. Theorem 2 agrees
  for the figure and adds a price: their schedule spends only $\frac67$ of the
  action, since it never cuts again what it took away.
- The Mohists hold that the halving ends at a point. Theorem 2 agrees
  that each schedule converges to a point, and the point carries no
  action. The unhalvable 端 as a least magnitude is a reading the theorem
  leaves aside, as the [Planck paper](planck-gap-paper.md) already records.
- Newton's scholium closing Book I, Section I, takes the geometers' side
  (divisibility without end). Theorem 2 is that side made quantitative:
  refinement exhausts the action only when every piece is cut again.

The parallel with Zeno's dichotomy (Aristotle, *Physics* VI.9) is
recorded as convergence; transmission would need evidence this note does
not have.

## 4. The weight of a cut

Take the Euclidean path measure of a free particle with diffusion
constant $\hbar/m$: Brownian motion $X$ with $E[X_t^2]=\hbar t/m$, pinned at the
cell's endpoints. Given the endpoints of a piece of length $L$, the value
at fraction $s$ is Gaussian with variance $\hbar s(1-s)L/m$, independent of
the finer hats and of the other pieces, by the Markov property of the
bridge (the Lévy construction, for any nested sequence). A force $F$ shifts
the mean of that value by the sagitta $h=Fs(1-s)L^2/(2m)$. The
Kullback--Leibler divergence of the shifted from the free law (the
expected log-likelihood ratio, which here also equals the ratio evaluated
at the shift) is

$$\frac{h^2}{2\,\hbar s(1-s)L/m}=\frac{mh^2}{2s(1-s)L\,\hbar}
=\frac{3s(1-s)CL^3}{\hbar},$$

the spent share of Theorem 1 divided by $\hbar$. By the chain rule the
divergences add over cuts, and along a sequence with mesh tending to zero
they sum to $K_\tau/\hbar$, the Cameron--Martin exponent for the shift $\delta x$. The
Cameron--Martin density factorizes over cuts, each contributing the
normalizing factor $e^{-3s(1-s)CL^3/\hbar}$. This is the Euclidean counterpart of
the real-time two-path phase $K_\tau/\varepsilon$ of the two-path note (the same number
with $\varepsilon$ in the role of $\hbar$), and of the product-over-cuts structure that
§7 of the [fifth-postulate note](principia-fifth-postulate.md) reads in the
time-step partition of [Rivero 1998](https://arxiv.org/abs/quant-ph/9803035).
For $\hbar\to0$ every cut, however small, is decisive; for $\hbar>0$ the cuts whose
share falls below $\hbar$ carry little evidence (under one nat). $\square$

## 5. A floor counts the cuts

If every cut that a record exhibits must spend at least $\kappa>0$, Theorem 2
gives at most $K_\tau/\kappa$ such cuts, for every schedule. For halving
refinement the $2^n$ cuts of level $n$ each spend $\frac34K_\tau8^{-n}$, so the
exhibited levels are those with $8^n\le 3K_\tau/(4\kappa)$.

Two floors must be kept apart: $\kappa$ here floors the share a cut spends,
$3s(1-s)K_L$, while the thresholds in the other notes floor the action of a
cell, $K_\tau$; for halving the two differ by the factor $\frac34$. The Planck
paper's eq. (2) is $K_\tau\ge2z_{1-\epsilon}^2\hbar$: $\tau_*$ is the cell with
$K_{\tau_*}=2z_{1-\epsilon}^2\hbar$, whose halving spends $\frac32z_{1-\epsilon}^2\hbar$. The round-3
resolution threshold $\tau\ge(24m\varepsilon d_{n,\eta}/F^2)^{1/3}$ is $K_\tau\ge\varepsilon d_{n,\eta}$, that is
$\kappa=\frac34\varepsilon d_{n,\eta}$ in cut-share form. Corollary 5 thus places a floor, when
one is given, at a definite depth of the cut process; it supplies no
floor.

## 5b. The mark mesh from the path measure (Proposition 6)

Keep the measure of §4: Brownian motion with $E[X_t^2]=\hbar t/m$, the
Euclidean free-particle measure, whose diffusion coefficient $\hbar/2m$ is
the one of [Nelson (1966)](https://doi.org/10.1103/PhysRev.150.1079)
(metadata). For the whole cell, the laws with and without the force are
Gaussian measures differing by the shift $\delta x$, with Cameron--Martin norm
$\|\delta x\|^2=(m/\hbar)\int\dot{\delta x}^2=2K_\tau/\hbar$. The log-likelihood ratio is the affine
function $\langle\delta x,X\rangle-\frac12\|\delta x\|^2$ of one Gaussian statistic of variance $\|\delta x\|^2$
whose mean moves by $\|\delta x\|^2$, so the Neyman--Pearson test with equal priors
thresholds that statistic halfway and errs with probability

$$p_{\rm err}=\Phi\Bigl(-\tfrac12\|\delta x\|\Bigr)=\Phi\Bigl(-\sqrt{K_\tau/2\hbar}\Bigr).$$

Hence $p_{\rm err}\le\epsilon$ iff $K_\tau\ge2z_{1-\epsilon}^2\hbar$, that is $\tau\Delta E=12K_\tau\ge24z_{1-\epsilon}^2\hbar$ and
$\tau\ge\tau_*=(48z_{1-\epsilon}^2m\hbar/F^2)^{1/3}$: eq. (2) of the
[Planck paper](planck-gap-paper.md), including its "about $65\hbar$ at
$\epsilon=0.05$" ($2z_{0.95}^2=5.41$). A single cut observed alone gives
$\Phi(-\sqrt{{\rm share}/2\hbar})$ in the same way. $\square$

The Planck paper reaches (2) from real-time Gaussian marks whose record
and recoil obey Robertson's bound $\hbar/2$; here the same constant comes from
the Euclidean path measure $e^{-S/\hbar}$ through the Cameron--Martin theorem
alone. The agreement is exact, and both routes supply $\hbar$: this is a
second derivation of the mesh, with the necessity question of the
[fifth-postulate note](principia-fifth-postulate.md) unchanged. What it
adds is the reading of the floor on recording the inertial--parabola
difference as the distinguishability threshold of the force in the
free-particle path measure.

## 6. Consequence for STATE

Atlas §1b: the Newton row of "cuts at any position" is proved here
(Theorems 1--2, Corollary 3), with the Lévy--Ciesielski identification
and the Euclidean weight of a cut (Proposition 4). The necessity question
is unchanged. On the gauge side of §1b the free-field defect of a cut at
fraction $s$ is (5) scaled by $4s(1-s)$ in its size bound
([Corollary 2$_s$](series-parallel-gauge-refinement.md)); the $U(1)$ Theorem 5
holds for every cut fraction (Corollary 5$_s$ there).
