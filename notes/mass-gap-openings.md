# Openings for the mass gap, and why it is not special to SU(3)

Recorded 2026-09-23 at the user's request and **parked**: the Planck-gap
paper comes first, and none of these is being attacked now, except
possibly the fourth, which is the link from the Planck-gap work. The note
answers two questions the user asked and corrects one statement of the
map.

**The gap is expected for every compact simple non-abelian group.**
Lattice evidence shows gapped glueball spectra for $SU(N)$ from $N=2$ to
large $N$, with masses smooth in $1/N^2$, and for the other classical
groups; the dividing line is between abelian and non-abelian, since
compact $U(1)$ in four dimensions has a proven massless phase at weak
coupling. $SU(3)$ fixes the constants; a method that works will almost
surely be group-general.

**A precision on the map.** The [position note](mass-gap-position.md)
says that the conjecture is T2$'$ together with T3, given T4, and the
[obligations map](mass-gap-obligations-lattice.md) says that T3
presupposes T2$'$. T3 needs less: a gap $\delta_\infty(g)>0$ on some
interval $(0,g_1)$ along the scaling curve. T2$'$, a gap at every lattice
coupling, is a property of a particular lattice action, and for the
Wilson action it fails for $SU(N\ge5)$, where a first-order bulk
transition occurs at intermediate coupling. For $SU(3)$ with the Wilson
action the bulk behaviour is a crossover, so T2$'$ remains plausible
there; the conditional theorem of the
[conditional-theorem note](mass-gap-conditional-theorem.md), stated along
the trajectory, needs no T2$'$ at all.

**Four openings,** ranked by how directly they reach the place where the
map ends, the control of about six blocking steps at order-one coupling.

1. Curvature: the Bakry--Émery criterion and its multiscale form.
2. The centre-stabilized theory on $\mathbb R^3\times S^1$ at small radius.
3. Three dimensions first.
4. The Planck-gap link: Simon's valley lifting, a floor that holds for
   every state.

## 1. Evidence across groups

- **$SU(N)$.** Glueball masses and string tensions computed for $N$ from
  $2$ to about $12$ are finite and extrapolate smoothly in $1/N^2$ (Lucini
  and Panero, [Phys. Rep. **526**, 93, 2013](https://doi.org/10.1016/j.physrep.2013.01.001),
  metadata; Lucini and Teper,
  [JHEP **2001**(06), 050](https://doi.org/10.1088/1126-6708/2001/06/050),
  metadata).
- **$G_2$.** The exceptional group has a trivial centre and still shows
  confinement behaviour and a first-order deconfinement transition (Pepe
  and Wiese, [Nucl. Phys. B **768**, 21, 2007](https://doi.org/10.1016/j.nuclphysb.2006.12.024),
  metadata), so the centre is not what the gap rests on.
- **$U(1)$.** Four-dimensional compact $U(1)$ has a massless Coulomb
  phase at weak coupling (Guth, [PRD **21**, 2291, 1980](https://doi.org/10.1103/PhysRevD.21.2291);
  Fröhlich and Spencer, [CMP **83**, 411, 1982](https://doi.org/10.1007/BF01213610);
  metadata), which is why the [abelian note](abelian-misses-the-box.md)
  separates the groups by the running, $b_0=0$ against
  $b_0=11N/(48\pi^2)$. In three dimensions compact $U(1)$ is gapped at
  every coupling (Polyakov, [Nucl. Phys. B **120**, 429, 1977](https://doi.org/10.1016/0550-3213(77)90086-4);
  proved by Göpfert and Mack, [CMP **82**, 545, 1982](https://doi.org/10.1007/BF01961240);
  metadata), with a gap that vanishes in physical units in the continuum.

**Bulk transitions depend on the action.** With the standard Wilson
plaquette action, "the bulk transition is a rapid cross-over if $N\le4$
but becomes an increasingly strong first order transition for $N\ge5$";
for $N=3$ a negative adjoint term avoids the bulk phase altogether
(Rindlisbacher, Rummukainen and Salami,
[arXiv:2306.14319](https://arxiv.org/abs/2306.14319), passage). In the
plane of fundamental and adjoint couplings, a line of first-order
transitions ends at a critical point near the Wilson axis (Bhanot and
Creutz, [PRD **24**, 3212, 1981](https://doi.org/10.1103/PhysRevD.24.3212),
metadata). By Corollary 3 of the
[gapped-set note](gapped-set-critical-coupling.md), a first-order
transition at $g_b$ gives $\delta_\infty(g_b)=0$ through vacuum
coexistence, so the gapped set $\mathcal G$ has a hole there while the
physical gap, which lives at $g\to0$, is untouched. The statement the
conjecture needs is $\mathcal G\supseteq(0,g_1)$ for some $g_1>0$, joined
to T3 along the scaling curve.

### Why $N\ge5$ differs, and what sits beside the $SU(3)$ Wilson axis

Give the lattice action a fundamental coupling $\beta_F$ and an adjoint
coupling $\beta_A$. In the $(\beta_F,\beta_A)$ plane a line of first-order
bulk transitions ends at a critical point (Bhanot and Creutz 1981). For
small $N$ the Wilson axis $\beta_A=0$ passes beside the endpoint and shows
a rapid crossover; from $N=5$ it crosses the line, and the transition
strengthens with $N$. The large-$N$ limit makes a non-analyticity between
strong and weak lattice coupling unavoidable. In two dimensions, where
the lattice theory is exactly solvable, it is analytic at every finite
$N$ and has a third-order transition at a critical 't Hooft coupling at
$N=\infty$ (Gross and Witten,
[PRD **21**, 446, 1980](https://doi.org/10.1103/PhysRevD.21.446); Wadia,
[PLB **93**, 403, 1980](https://doi.org/10.1016/0370-2693(80)90353-6);
metadata). In four dimensions the large-$N$ transition is first order,
and at finite $N$ it survives as a genuine transition from $N=5$ and is
smoothed into a crossover below.

For $SU(3)$ the endpoint matters twice.

- **It realizes the second-order branch.** Approaching the endpoint, "the
  mass of the $0^{++}$ glueball decreases ... while the other glueball
  masses appear unchanged", which is "consistent with the notion that the
  bulk transition line ends in a critical endpoint with the continuum
  limit there being a $\phi^4$ theory with a diverging correlation length
  only in the $0^{++}$ channel" (Heller,
  [PLB **362**, 123, 1995](https://doi.org/10.1016/0370-2693(95)01186-T);
  [hep-lat/9508009](https://arxiv.org/abs/hep-lat/9508009), abstract). So
  lattice $SU(3)$ has a second continuum limit at a finite point of its
  two-coupling plane, a scalar theory, and the statement that the
  asymptotically free limit is the only one concerns families that avoid
  that point, such as the Wilson axis.
- **It sits beside the point where the map places H2.** The
  [bands note](confinement-scale-bands.md) scaled the continuum ratio
  $r_0m_{0^{++}}=4.21$ to $\beta_W=5.7$ and found $\xi/a=0.70$. Near there
  the Wilson axis passes beside the endpoint, where the scalar glueball
  softens, so the lattice $\xi/a$ at $\beta_W\simeq5.7$ is likely larger,
  and the measured lattice value should replace the scaled one. The
  conditional theorem allows the remedy: blocking generates adjoint and
  higher-representation terms anyway, so the reference interaction
  $\Phi_0$ of H2 can be taken at a small negative adjoint coupling, away
  from the endpoint. For $N=3$ such an action avoids the bulk phase, as
  Rindlisbacher, Rummukainen and Salami report from earlier work
  (arXiv:2306.14319, passage).

### What the problem statement itself points to

Jaffe and Witten's official description, held as a
[local PDF](../docs/JaffeWitten_YangMills.pdf), names in its §6.6 four
routes to the gap (passage), and two of them are openings 1 and 4 below:

- a "duality transformation", with Debye screening in the Coulomb gas,
  proved through the sine-Gordon representation, as the model;
- the quartic potential $(A\wedge A)^2$ (Feynman,
  [Nucl. Phys. B **188**, 479, 1981](https://doi.org/10.1016/0550-3213(81)90005-5)),
  which "may be tied to curvature in the space of connections" (Singer,
  [Phys. Scripta **24**, 817, 1981](https://doi.org/10.1088/0031-8949/24/5/002)):
  opening 1;
- "certain quantum mechanics problems with potentials involving flat
  directions ... do lead to bound states" (Simon 1983): opening 4;
- the $1/N$ expansion ('t Hooft 1974): gauge theory with $SU(N)$, $SO(N)$
  or $Sp(N)$ "may be equivalent to a string theory with $1/N$ as the
  string coupling constant", which "might give a clear-cut explanation of
  the mass gap and confinement and perhaps a good starting point for a
  rigorous proof (for sufficiently large $N$)". Maldacena's paper is cited
  there as "surprising progress along these lines for certain strongly
  coupled four-dimensional gauge systems with matter, but as of yet there
  is no effective approach to the gauge theory without fermions." Earlier,
  §6.1 allows that "there might some day be an asymptotic solution in a
  large $N$ limit."

**Chronology.** Maldacena's conjecture was posted in November 1997
([hep-th/9711200](https://arxiv.org/abs/hep-th/9711200)); Witten's
holographic account of non-supersymmetric Yang--Mills, in which "the
spontaneous breaking of the center of the gauge group, magnetic
confinement, and the mass gap are coded in classical geometry", in March
1998 ([hep-th/9803131](https://arxiv.org/abs/hep-th/9803131), abstract);
supergravity glueball masses in agreement with lattice ratios in June 1998
(Csáki, Ooguri, Oz and Terning,
[hep-th/9806021](https://arxiv.org/abs/hep-th/9806021), abstract); the
Clay problems in May 2000. The statement was written with holography in
hand, by one of its authors, and records no effective approach to the
pure gauge theory. The usual reasons, not checked here against a primary
text, are that the tractable supergravity regime is the opposite limit
from the continuum one, with Kaluza--Klein modes at the glueball scale,
and that it holds at large $N$ only.

**The large-$N$ thread.** It runs through Witten's own work: the $1/N$
expansion for baryons ([Nucl. Phys. B **160**, 57, 1979](https://doi.org/10.1016/0550-3213(79)90232-3))
and for the $U(1)$ problem
([Nucl. Phys. B **156**, 269, 1979](https://doi.org/10.1016/0550-3213(79)90031-2)),
and the large-$N$ lattice transition with Gross (1980), the
non-analyticity behind the $N\ge5$ bulk transition above. This programme
records the route and does not adopt it: the conjecture is posed for every
compact simple group, so a proof for sufficiently large $N$ would leave
$SU(3)$ open unless it came with explicit control down to $N=3$; and at
large $N$ a lattice route meets the bulk transition, which it would have
to avoid with a bulk-preventing action or with the centre-stabilized
volume independence of opening 2, itself a large-$N$ construction.

**The panorama with $\hbar$ explicit.** This repository writes the action
as $S=-\frac{\hbar}{4g^2}\int F^a_{\mu\nu}F^{a\mu\nu}\,d^3x\,c\,dt$ with $g$
dimensionless ([G07](low-dimensional-mass-gap.md), Proposition 7), so the
weight $e^{iS/\hbar}$ contains $g$ alone and $\hbar$ is hidden inside it:
with a classical coupling $g_{\rm cl}$, $S=-\frac1{4g_{\rm cl}^2}\int\cdots$,
one has $g^2=\hbar g_{\rm cl}^2$. Three consequences follow.

- *The 't Hooft limit is a classical limit.* A diagram with $E$
  propagators, $V$ vertices and genus $h$ carries $(\hbar\lambda_{\rm cl})^{E-V}N^{2-2h}$
  with $\lambda_{\rm cl}=g_{\rm cl}^2N$ ('t Hooft,
  [Nucl. Phys. B **72**, 461, 1974](https://doi.org/10.1016/0550-3213(74)90154-0),
  metadata). The loop parameter is $\lambda=\hbar g_{\rm cl}^2N$, so
  $N\to\infty$ at fixed $\lambda$ is $\hbar\to0$ with $\hbar N$ fixed at fixed
  $g_{\rm cl}$, and $1/N^2=(\hbar g_{\rm cl}^2/\lambda)^2$: the genus
  expansion is an expansion in $\hbar^2$. Yaffe formulates large-$N$
  limits in general as classical mechanics
  ([Rev. Mod. Phys. **54**, 407, 1982](https://doi.org/10.1103/RevModPhys.54.407),
  metadata). In holography it is literal: the bulk Newton constant in
  anti-de Sitter units is of order $1/N^2$, so the bulk loop expansion is
  the $1/N^2$ expansion.
- *The gap is non-perturbative in $\hbar$.* With the two-loop scale of
  the [obligations map](mass-gap-obligations-lattice.md) §5 and
  $b_0=11N/(48\pi^2)$, $mc^2\propto\frac{\hbar c}a\exp\bigl(-\frac{24\pi^2}{11\,\hbar g_{\rm cl}^2N}\bigr)$
  times a power of $\hbar g_{\rm cl}^2N$: at fixed $N$, $a$ and $g_{\rm cl}$
  it vanishes faster than any power of $\hbar$, the way a tunnelling
  splitting does, which gives one precise reading of Jaffe and Witten's
  remark that the gap is "not classically visible". It depends on $\hbar$ and $N$
  only through $\hbar N$, so the 't Hooft limit is the classical limit
  along which the gap survives.
- *The small volume is a power of $\hbar$.* G07's zero-mode gap
  $\delta_1g^{2/3}\hbar c/L$ is $\delta_1\hbar^{4/3}g_{\rm cl}^{2/3}c/L$: a floor
  of the Planck-gap kind, a power of $\hbar$ from the zero-point energy that
  lifts the valleys. The two regimes meet at the crossover $z\simeq2$ of
  the [valley note](torus-valley-potential.md). Opening 4 lives in the
  power-law regime, where the Planck-gap methods apply; the
  infinite-volume gap lives in the non-perturbative one.

## 2. The openings

### Opening 1: curvature

The configuration space of lattice gauge theory is a product of copies
of the group, and a compact simple group carries positive Ricci
curvature: for $SU(N)$ with the metric $\langle X,Y\rangle=\operatorname{Tr}(XY^*)$,
$\operatorname{Ric}=\frac N2\,g$. The Bakry--Émery criterion turns a
positive lower bound on $\operatorname{Ric}+\operatorname{Hess}S$ into a
log-Sobolev and a Poincaré inequality, that is into a spectral gap of the
Langevin dynamics and exponential decay of correlations (Bakry and Émery,
[LNM 1123, 177, 1985](https://doi.org/10.1007/BFb0075847), metadata). A
flat group, $U(1)$, gets nothing from the first term, which lines up with
the abelian failure.

Shen, Zhu and Zhu use exactly this to prove, for lattice Yang--Mills with
't Hooft coupling $\beta N$ in any dimension $d>1$, uniqueness of the
infinite-volume measure, log-Sobolev and Poincaré inequalities and
exponential decay of correlations, "a strictly positive mass gap", for
$|\beta|<1/(16(d-1))$ when the group is $SU(N)$
([CMP **400**, 2022](https://doi.org/10.1007/s00220-022-04609-1);
[arXiv:2204.12737](https://arxiv.org/abs/2204.12737), abstract). In the
Wilson normalization of this repository, $\beta_W=2N/g^2$ with weight
$e^{(\beta_W/N)\sum\operatorname{Re}\operatorname{Tr}U_p}$, their $\beta$ is
$\beta_W/N^2$, so for $SU(3)$ in four dimensions the condition is
$\beta_W<3/16$, that is

$$g^2>32 .$$

That conversion is ours and must be checked against their definitions.
If it stands, the curvature method already beats this repository's
strong-coupling thresholds, $g^2\ge176$ for the Wilson transfer matrix
([note](wilson-strong-coupling-explicit.md)), $g^2\ge388$ for
Kogut--Susskind ([note](kogut-susskind-strong-coupling-explicit.md)) and
$g^2>444$ by Dobrushin ([note](dobrushin-uniqueness-wilson.md)), and
narrows band B of the [bands note](confinement-scale-bands.md) from
$\beta_W\in(0.0135,5.7)$ to $\beta_W\in(0.19,5.7)$.

The weak side is where the multiscale form enters. Bauerschmidt and
Bodineau derive "a multiscale generalisation of the Bakry--Émery
criterion" through the Polchinski renormalization equation, "effective
for measures which are far from log-concave", and prove optimal
log-Sobolev inequalities for the continuum sine-Gordon model at
$\beta<6\pi$ ([CPAM **74**, 2020](https://doi.org/10.1002/cpa.21926);
[arXiv:1907.12308](https://arxiv.org/abs/1907.12308), abstract). Its
output is a spectral gap controlled at every scale, which is the form of
hypothesis H1 in the conditional theorem. It also sits outside the family
closed in [flow-before-decimation](flow-before-decimation.md): that note
closes every criterion that depends on the perturbation through a norm,
and a curvature bound is a lower bound on a Hessian.

The risk is concrete. After a blocking step the effective action is a
function on the coarse configuration manifold, and the criterion needs
$\operatorname{Ric}+\operatorname{Hess}S_{\rm eff}$ bounded below at every
scale. At weak coupling the Hessian is degenerate along gauge orbits and
along the abelian valleys, and the curvature of the group has to carry
those directions. **First note if opened:** check the conversion to
$g^2>32$; compute the curvature budget for $SU(2)$ and $SU(3)$ against
the Hessian of the Wilson action; and state exactly what lower bound one
blocking step must preserve.

### Opening 2: the centre-stabilized theory at small radius

Ünsal and Yaffe add a double-trace deformation that keeps centre
symmetry unbroken; on $\mathbb R^3\times S^1$ at small radius "the
deformed Yang--Mills theory has a mass gap and exhibits linear
confinement", by an analytic semiclassical treatment, and "there are no
order parameters which distinguish the small and large radius regimes"
([PRD **78**, 065035, 2008](https://doi.org/10.1103/PhysRevD.78.065035),
abstract). The mechanism at small radius is Polyakov's monopole plasma,
which Göpfert and Mack made rigorous for three-dimensional compact $U(1)$
at every coupling. **Target if opened:** a rigorous mass gap for the
deformed theory at small radius, with explicit constants. That would be a
theorem about a deformed theory; carrying it to $\mathbb R^4$ is the
adiabatic-continuity conjecture.

### Opening 3: three dimensions first

In three dimensions $g^2$ has the dimensions of energy, the theory is
superrenormalizable, and the coupling at lattice scale is $g^2a/\hbar c$,
which vanishes as a power of $a$. The weak-side deficit of twelve orders
of magnitude found in
[the small-field threshold note](small-field-step-decay-and-threshold.md)
comes from the logarithmic running of four dimensions, and in three
dimensions the ultraviolet steps shrink geometrically, so the
constant-chasing that failed in four dimensions may close. The
[one-function note](three-dimensional-gap-one-function.md) reduces the
problem to a lower bound $f(x)\ge f_->0$ on one function of one variable.
A three-dimensional gap uniform in the spacing is open and would be a
major result by itself.

### Opening 4: the Planck-gap link

The small-volume mechanism of [G07](low-dimensional-mass-gap.md) and
[G08](action-floor-yang-mills-gap.md) is Simon's: along the flat valleys
of the commutator potential the transverse modes are oscillators whose
frequency grows with the distance along the valley, and their zero-point
energy lifts the valley (Simon,
[Ann. Phys. **146**, 209, 1983](https://doi.org/10.1016/0003-4916(83)90057-X),
metadata). In its simplest form, for fixed $x$,

$$\frac{\hat p_y^2}{2m}+\frac12m\Omega(x)^2\hat y^2\ \ge\ \frac12\hbar\,\Omega(x),$$

an operator inequality that holds in every state. The
[torus-valley note](torus-valley-potential.md) finds the field-theory
version term by term: the linear term $2|a|$ of the valley potential is
the zero-point energy of the $k=0$ charged modes.

The Planck-gap work sharpens what kind of floor this is. Its floors that
rest on second moments of a prepared state fall to squeezing and to grid
states, and the ones that survive rest on the commutator alone: the
phase between Newton's polygon and the parabola, and the cost of
disturbance. Simon's inequality is of the surviving kind, a spectral
statement, so the valley lifting is the mass-gap instance of the lesson
the Planck paper draws. **First step if opened:** hypothesis (H3) of
the [Feshbach note](weak-coupling-feshbach-reduction.md), the gap of the
zero-mode Hamiltonian $h_3$ plus the even valley potential $U(a)$, proved
by a Simon-type operator inequality with every constant explicit. That is
the lower side of the small-volume corner S at weak coupling, and it
stays within reach of the Planck-gap methods.

## 3. Consequence for STATE

The mass-gap track stays paused. This note records the four openings
and the answer on groups: the gap is expected for every compact simple
non-abelian group, and $SU(3)$ is the group that fixes the constants. The
map's statement that the conjecture is T2$'$ with T3 is too strong:
T3, with a gap on an interval $(0,g_1)$ along the scaling curve, is what
is needed, and T2$'$ fails for $SU(N\ge5)$ with the Wilson action. If one
opening is taken up next, it is the fourth, which uses the Planck-gap
methods directly; the first carries the most promise, and its first
check is the conversion of Shen, Zhu and Zhu's threshold to $g^2>32$.
