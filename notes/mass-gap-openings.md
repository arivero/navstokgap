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
