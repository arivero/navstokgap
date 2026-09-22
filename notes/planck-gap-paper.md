# The cost of a mark: Newton's vanishing sagitta and a floor of order $\hbar$

**Abstract.** Newton reads a force off a trajectory by letting the
sagitta and the area between the inertial tangent and the curve go to
zero, keeping their ratio to the time. We show that the same comparison,
once it must be *recorded*, has a floor. For every protocol of marks, of
any number and at any times, whose resolution and recoil are Gaussian,
uncorrelated, and obey $\delta_j\Delta_j\ge\kappa$, deciding between free and forced motion over
a duration $\tau$ at error probability $\epsilon$ requires

$$\tau\Delta E=\frac{F^2\tau^3}{2m}\ \ge\ 48\,z_{1-\epsilon}^2\,\kappa,$$

and for a mark realized by coupling the body's position to a probe, the
error operator and the impulse delivered are canonically conjugate, so
$\kappa\ge\hbar/2$ exactly. The constant $48$ is sharp, approached by
dense protocols. The floor is about $65\hbar$ at five per cent error, and
insertion of marks finer than
$\tau_*=(48z_{1-\epsilon}^2m\hbar/F^2)^{1/3}$ records free motion only.
A correlation $\rho$ between a mark's error and its recoil multiplies the
floor by $\sqrt{(1-\rho)/(1+\rho)}$, and a three-mark protocol attains
that dependence, so the floor is a statement about marks whose
uncertainty ellipse has bounded shape as well as area. For probes in any
state, Gaussian or not, one statement survives: the sagitta times the
total undetermined impulse the marks deliver is at least
$8(1-2\epsilon)\hbar$, whatever their resolution. The part of the
signal that no preparation can move is a phase: Newton's polygon
inscribed in the parabola agrees with it classically at every vertex and
differs quantum mechanically by $F^2\sum_j\tau_j^3/(24m\hbar)$, the
parabolic segments of the chords times $F/2v\hbar$, whatever the state of
the body.
The historical claim is that Newton's *Opticks* contains both factors of
$\kappa$, one of them measured as the $1/89000$th part of an inch, and
that the single proposition joining them to a floor is an indeterminacy
about the fits which Newton formulated the negation of. The distance
between his system and a positive $h$ is therefore one nameable
proposition, and that proposition is Robertson's inequality for his
corpuscle.

Draft, 2026-09-17. Synthesis of the
[mark-floor](newton-mark-floor.md),
[derivation](planck-gap-derivation.md),
[probabilistic](planck-gap-probabilistic.md) and
[mark-cost](mark-cost-and-statistical-floor.md) and
[polygon-lift](polygon-lift-phase.md) notes, which hold the
proofs in full. Two obligations remain before submission and are stated
in §9. Exploratory; no ledger promotion.

## 1. The question

Galileo's comparison is an inertial horizontal line against a falling
parabola. With mass $m$, transverse force $F$, horizontal speed $v$ and
duration $\tau$, the two paths are $q_{\mathrm I}(t)=(vt,0)$ and
$q_{\mathrm F}(t)=(vt,Ft^2/2m)$, and the region between them has

$$A=\frac{vF\tau^3}{6m},\qquad s(\tau)=\frac{F\tau^2}{2m},\qquad
\Delta E=\frac{F^2\tau^2}{2m},\qquad \frac{3F}{v}A=\tau\Delta E. \tag{1}$$

The sagitta $s$, the area $A$ and the product $\tau\Delta E$ all scale as
powers of $\tau$ and vanish together. Newton's Lemma X makes the first
displacement quadratic in the time; Lemma XI, Corollaries 4 and 5, make
the curved segment one third of the tangent triangle with both cubic in
the time; Proposition VI reads the force off the limit $2ms/\tau^2$; and
Proposition I builds an orbit as a polygon struck by impulses at its
vertices, the number of vertices "augmented in infinitum". The construction
is designed so that the quantities in (1) disappear and their ratios
survive.

Our question is what stops that refinement when the trajectory has to be
recorded rather than contemplated, and whether the stopping point can be
reached from materials Newton possessed.

The answer has four parts. The geometry alone supplies no floor (§2).
Recording supplies one, which is set by a single number $\kappa$ with
the dimensions of action, and every protocol of marks faces the same
bound in the same combination $F^2\tau^3/m$ (§3). Quantum kinematics
fixes $\kappa\ge\hbar/2$ by an exact and elementary argument (§4).
Newton's optics supplies both factors of $\kappa$ and denies the
inequality between them (§§5--6). Newton also attempted a preface founded
on the ancients, and the ancient arguments that bear on his own method
are the ones he passed over; stated as premises about records they
generate a hierarchy whose first rung is Zeno's arrow and whose second is
the comparison above (§7).

## 2. The geometry has no floor

**Proposition 1.** For every partition $0=t_0<\dots<t_n=\tau$ with steps
$\tau_j$ and mesh $|\pi|$, the vertex impulse $F\tau_j$, the step sagitta
$F\tau_j^2/2m$ and the step area $vF\tau_j^3/6m$ tend to zero with the
mesh; the areas sum to at most $vF\tau|\pi|^2/6m$; and
$2m\,s(\tau_j)/\tau_j^2=F$ exactly at every step.

The proof is immediate from (1). Berkeley's objection, that evanescent
increments are "neither finite Quantities nor Quantities infinitely
small, nor yet nothing", is answered inside the geometry by the limit
ratio, which is what Newton's closing Scholium to Book I Section I
provides. A floor must therefore come from the act of marking the curve,
and the reading of "inserting a point" used here is physical: a point of
the trajectory is inserted by making a mark on the body at a time.

## 3. Marks, and the floor they impose

**Definitions.** A **mark** at time $t_j$ leaves a datum about the
transverse coordinate. Its **resolution** $\delta_j$ is the spread of the
resulting position estimate's error; its **recoil** $\Delta_j$ is the
spread of the transverse impulse it delivers to the body. A protocol is a
finite set of marks; it **decides** the comparison at error probability
$\epsilon$ when some test on the full record does so with equal priors.
A model satisfies the **mark trade-off** with constant $\kappa$ when
every available mark has $\delta\Delta\ge\kappa$.

**The statistical model.** Mark $j$ returns $R_j=y(t_j)+\xi_j$ with
$\xi_j$ centred Gaussian of standard deviation $\delta_j$, and delivers
an impulse $\iota_j$, centred Gaussian of standard deviation $\Delta_j$,
independently, so that

$$y(t)=y_0+v_0t+\theta P(t)+\frac1m\sum_j\iota_j(t-t_j)_+,\qquad
P(t)=\frac{Ft^2}{2m},$$

with $\theta=0$ under the inertial hypothesis and $\theta=1$ under the
falling one, and $y_0,v_0$ unknown. Tests are invariant under the two
unknowns, so the statistic is $u^{\mathsf T}R$ with $\sum_iu_i=0$ and
$\sum_iu_it_i=0$, and the optimal invariant test has error probability
$\Phi(-d/2)$ with $d^2=\sup(u^{\mathsf T}P)^2/(u^{\mathsf T}\Sigma u)$
over such $u$.

**Theorem 2.** For every protocol satisfying the mark trade-off with
constant $\kappa$,

$$d^2\ \le\ \frac{F^2\tau^3}{24\,m\kappa},$$

independently of the number of marks and of their times, and the
constant is sharp. Hence deciding at error probability $\epsilon$
requires

$$F^2\tau^3\ \ge\ 96\,z_{1-\epsilon}^2\,m\kappa,\qquad
\tau\Delta E\ \ge\ 48\,z_{1-\epsilon}^2\,\kappa,\qquad
A\ \ge\ \frac{16\,z_{1-\epsilon}^2\,v\kappa}{F},$$

with $z_{1-\epsilon}=\Phi^{-1}(1-\epsilon)$.

*Proof.* The noise enters $R$ in two ways: $\xi_j$ affects $R_j$ alone,
and $\iota_j$ affects $R_i$ for $i>j$ with coefficient $(t_i-t_j)/m$.
Hence

$$u^{\mathsf T}\Sigma u=\sum_j\delta_j^2u_j^2
+\sum_j\frac{\Delta_j^2}{m^2}S_j^2,\qquad S_j=\sum_{i>j}u_i(t_i-t_j),$$

and the arithmetic--geometric mean inequality applied termwise gives
$u^{\mathsf T}\Sigma u\ge\frac{2\kappa}{m}\sum_j|u_j||S_j|$.

Introduce $N(w)=\sum_{i:t_i>w}u_i$ and $T(w)=\int_w^\tau N$. Since
$\sum_iu_i=0$, $N$ vanishes for $w<0$ and for $w\ge t_k$; $T$ is
continuous, piecewise linear, zero on $[\tau,\infty)$, and zero on
$(-\infty,0]$ as well, since $T(0)=\int_0^\tau N=\sum_iu_it_i=0$ by the
invariance under $v_0$; it has $T'=-N$ jumping by $u_j$ at $t_j$ and
$T(t_j)=S_j$. Two identities follow. Fubini and one integration by
parts, using $P'(0)=0$ and $T(\tau)=0$, give

$$u^{\mathsf T}P=\int_0^\tau P'N=-\int_0^\tau P'T'=\int_0^\tau P''T
=\frac Fm\int_0^\tau T;$$

and since $T'$ has bounded variation with jumps $u_j$ and no other
variation, while $TT'$ vanishes at both ends,

$$\sum_ju_jT(t_j)=\int_{\mathbb R}T\,dT'=-\int_{\mathbb R}T'^2=-E,
\qquad E=\int_0^\tau T'^2 .$$

Therefore $\sum_j|u_j||S_j|\ge E$ and $u^{\mathsf T}\Sigma u\ge2\kappa E/m$.
Since $T$ vanishes at both ends of $[0,\tau]$, the Poincaré inequality
$(\int_0^\tau T)^2\le\frac{\tau^3}{12}\int_0^\tau T'^2$ applies, with
equality for $T\propto w(\tau-w)$ (the Euler--Lagrange equation is
$T''=$ const), and

$$\frac{(u^{\mathsf T}P)^2}{u^{\mathsf T}\Sigma u}
\le\frac{(F/m)^2\frac{\tau^3}{12}E}{2\kappa E/m}=\frac{F^2\tau^3}{24m\kappa}.$$

Finally $\Phi(-d/2)\le\epsilon$ requires $d\ge2z_{1-\epsilon}$. For
sharpness, take marks dense in $[0,\tau]$ with weights making $N$
approximate $2w-\tau$, so that $T$ approximates $w(\tau-w)$; the interior
weights are negative where $T$ is positive, so every $u_jS_j$ has one
sign and $\sum_j|u_j||S_j|=E$; balance each mark,
$\delta_j|u_j|=\Delta_j|S_j|/m$, so the arithmetic--geometric step is an
equality; and make the end marks sharp, which costs nothing since
$S=T=0$ there. Every inequality then becomes an equality in the
limit. $\square$

Three features of the proof carry the paper's claim to universality. The
certificate $u$ ranges over all invariant tests, so no monitoring scheme
is privileged. The function $T$ encodes the whole protocol in one
object, and the bound depends on it only through the Dirichlet energy
$E$, which cancels. And the exponent $3$ on $\tau$ comes from the
Poincaré constant of the interval, $\tau^3/12$, which is where the
combination in (1) originates.

**Corollary 3 (insertion).** Marks inside a window of duration $\tau'$,
used by themselves, record the force only if
$F^2\tau'^3\ge96z_{1-\epsilon}^2m\kappa$. So insertion stops at

$$\tau_*=\left(\frac{96\,z_{1-\epsilon}^2\,m\kappa}{F^2}\right)^{1/3},$$

and finer marks are consistent with free motion at the stated
confidence. Newton's polygon may be refined past $\tau/\tau_*$ vertices,
and its impulses remain in the geometry, though no record exhibits them.

**A worst-case counterpart.** If the marks instead confine position and
impulse to intervals with certainty, the same three steps run with a
separating hyperplane in place of the optimal test direction and give
$F^2\tau^3>9m\kappa$ for every protocol, with two marks sufficing above
$36m\kappa$. There the initial velocity is bounded by the preparation's
recoil width instead of being free, so $T$ need not vanish at $0$ and the
Cauchy--Schwarz step is the one available. That version has no quantum instance, since certain
position confinement forces full-support momentum by Paley--Wiener; it
is recorded here because it shows that the argument depends on the
quadratic structure rather than on any probabilistic assumption.

## 4. The cost of a mark is the probe's uncertainty product

**Theorem 4.** Let a mark be realized by the impulsive coupling of the
body's position to a probe,
$U=\exp(-\tfrac{i}{\hbar}\lambda\hat y\hat P_A)$ with
$[\hat Q_A,\hat P_A]=i\hbar$, the pointer $\hat Q_A$ being read
afterwards. Then

$$U^\dagger\hat Q_AU=\hat Q_A+\lambda\hat y,\qquad
U^\dagger\hat pU=\hat p-\lambda\hat P_A,$$

so the error operator $\hat N=\hat Q_A/\lambda$ and the delivered impulse
$\hat D=-\lambda\hat P_A$ satisfy $[\hat N,\hat D]=-i\hbar$ and

$$\kappa=\delta\Delta=\Delta\hat N\cdot\Delta\hat D
=\Delta\hat Q_A\cdot\Delta\hat P_A\ \ge\ \frac\hbar2$$

for every probe state, pure or mixed.

*Proof.* With $A=\tfrac{i}{\hbar}\lambda\hat y\hat P_A$ the commutators
$[A,\hat Q_A]=\lambda\hat y$ and $[A,\hat p]=-\lambda\hat P_A$ are
central, so the Baker--Campbell--Hausdorff series terminates and gives the
two displayed relations, while $\hat y$ and $\hat P_A$ are unchanged.
Estimating the body's position by $\hat Q_A/\lambda$ leaves the error
$\hat N=\hat Q_A/\lambda$, and $[\hat N,\hat D]=-[\hat Q_A,\hat P_A]=-i\hbar$.
Robertson's inequality closes it. $\square$

The coupling strength cancels, so the cost is a property of the mark
rather than of how hard it is made. The record and the recoil are
themselves incompatible, since $[\hat Q_A+\lambda\hat y,-\lambda\hat P_A]=-i\hbar\lambda$,
which is why no reading of the pointer determines the impulse. A
deterministic probe, whose later position records fix its momentum, has
$\kappa=0$ and no floor; this is the exact point at which classical
record models differ.

For Gaussian probe states whose position and momentum are uncorrelated,
and the linear dynamics of the comparison, the Wigner function is a
probability density evolving classically, so the statistical model of
§3 reproduces the quantum experiment exactly. With Theorem 4,

$$\tau\Delta E\ \ge\ 24\,z_{1-\epsilon}^2\,\hbar,\qquad
\tau_*=\left(\frac{48\,z_{1-\epsilon}^2\,m\hbar}{F^2}\right)^{1/3}, \tag{2}$$

about $65\hbar$ at $\epsilon=0.05$ and $24\hbar$ at $\epsilon=0.16$.

**Correlated marks.** A probe whose position and momentum are correlated
delivers an error and a recoil with correlation
$\rho=-\operatorname{Cov}(\hat Q_A,\hat P_A)/(\Delta\hat Q_A\Delta\hat P_A)$,
and the Robertson--Schrödinger inequality gives
$\delta^2\Delta^2(1-\rho^2)\ge\hbar^2/4$. The cross terms enter the proof
of Theorem 2 as $2c_ju_jS_j/m$, and
$ax^2+2cxy+by^2\ge2(\sqrt{ab}-|c|)|x||y|$ replaces the
arithmetic--geometric step, so every protocol whose marks have
$|\rho_j|\le\rho$ needs

$$\tau\Delta E\ \ge\ 24\,z_{1-\epsilon}^2\,\hbar\,\sqrt{\frac{1-\rho}{1+\rho}} , \tag{3}$$

sharp by the dense construction of Theorem 2 with every mark at
correlation $\rho$ of the helpful sign. Three marks at $0,\tau/2,\tau$
with the test $R_1-2R_2+R_3$ come within a factor $4/3$, since the outer marks' recoils are invisible to the
test and the middle mark's noise $-2\xi_2+(\tau/2m)\iota_2$ is one
quadrature of its probe: they decide once
$\tau\Delta E\ge32z^2\hbar\sqrt{(1-\rho)/(1+\rho)}$, at every force as
$\rho\to1$. This is the back-action evasion of Yuen's contractive states
(PRL **51**, 719, 1983). The proofs are in the
[mark-cost note](mark-cost-and-statistical-floor.md), Theorem C and
Proposition D.

### The part no preparation can move

Both escapes from the floor, a correlated probe here and an unbalanced
aperture in §8, stretch an uncertainty ellipse of fixed area. A quantity
immune to that must be a c-number, and the comparison supplies one.
Newton's polygon of Proposition I inscribed in the parabola, with each
step's impulse $F\tau_j$ split equally between its ends, moves uniformly
along each chord and has the parabola's position and velocity at every
vertex, so classically the two are the same state there.

**Theorem 6.** For every partition of $[0,\tau]$ into steps $\tau_j$, the
two evolutions satisfy $W_{\rm poly}=e^{i\theta_N}W_F$ with

$$\theta_N=\frac{F^2}{24m\hbar}\sum_j\tau_j^3=\frac{F}{2v\hbar}\sum_jS_j,$$

$S_j=vF\tau_j^3/12m$ being the parabolic segment cut off by the $j$-th
chord. Inserting a vertex at fraction $\lambda$ of a step lowers
$\theta_N$ by $F^2\tau_j^3\lambda(1-\lambda)/(8m\hbar)$, the inscribed
triangle over $\hbar$, so midpoint halving removes it in the proportions
of Archimedes' exhaustion. The same increments composed in reverse order
differ by the phase $\Phi_N=F^2(\tau^3-\sum_j\tau_j^3)/(6m\hbar)$, and
$\Phi_N+4\theta_N=\tau\Delta E/3\hbar$ for every partition.

The proof uses the Weyl relations alone: an impulse $J$ at time $t$ is a
phase-space displacement, two histories with equal endpoints differ by
the enclosed phase-plane area over $\hbar$ times the identity, and the
per-step lobe is $F^2\tau_j^3/24m$ (the
[polygon-lift note](polygon-lift-phase.md) has it in full). Since
$W_{\rm poly}W_F^\dagger$ is a multiple of the identity, no preparation of
the body, squeezed or mixed, changes $\theta_N$. A control qubit that
selects the history reads it at single-shot error
$\frac12(1-|\sin(\theta_N/2)|)$, so one step is told from its chord at
error $\epsilon$ only if
$\tau_j\ge(48m\hbar\arcsin(1-2\epsilon)/F^2)^{1/3}$, for every state of the
body. The single chord lens and the closed loop of the earlier notes are
instances.

**Theorem 7 (every force law).** For a force history $f$ on an interval
of duration $\tau$, let $\mathcal K_\tau[f]=\int\frac12m(\dot y_f-\dot y_{\rm chord})^2dt
=\frac1{2m}\iint G_\tau ff$ be the kinetic action of the motion relative
to its chord, $G_\tau(s,u)=\min(s,u)(\tau-\max(s,u))/\tau$. Newton's
polygon, with each step's impulse split between its ends so as to match
the step's displacement, differs from the motion by the phase
$\sum_j\mathcal K_{\tau_j}[f]/\hbar$, which refinement never raises; and
every protocol of uncorrelated Gaussian marks has $d^2\le\mathcal K_\tau[f]/\kappa$,
sharp for $f$ of one sign. At $\kappa=\hbar/2$ the best recorded deflection
is twice the phase between the motion and its chord. The proofs are in
§6 of the [polygon-lift note](polygon-lift-phase.md). One functional of
the force history, the part of the motion that Newton's refinement
removes, is converted by $\hbar$ into a phase and by the mark cost into a
statistical distance; for a constant force it is the chord's segment
times $F/2v$.

### Every probe state: the record costs recoil

The floors above assume Gaussian probes, and the assumption is needed. A
grid state of the Gottesman--Kitaev--Preskill kind with a real
wavefunction has no position--momentum correlation, yet as the middle
probe of the three-mark protocol it turns the statistic into a comb of
spacing $\sqrt{2\pi\hbar\tau/m}$ with teeth as narrow as desired, and so
decides the comparison at any force whose signal is not a multiple of that
spacing. What holds for every probe state is a bound on the recoil.

**Theorem 8.** For every protocol of momentum-transfer marks with probes
in arbitrary states, deciding at error $\epsilon$ for every initial state of
the body requires
$1-2\epsilon\le\hbar^{-1}\min_{a,b}\sum_j\Delta_j|P(t_j)-a-bt_j|$, with
$\Delta_j$ the recoil spread of mark $j$. For the constant force,

$$s\sum_j\Delta_j\ \ge\ 8(1-2\epsilon)\hbar,\qquad s=\frac{F\tau^2}{2m}. \tag{4}$$

The proof moves the signal into the pointers: translating the body's
initial state along the best straight line turns the force into a
translation of each pointer by $\lambda_jc_j$, and a pointer registers a
translation only through the spread of its momentum, which is the impulse
the body receives. Mandelstam--Tamm and the triangle inequality over the
probes finish it. The correlated three-mark protocol reaches (4) within a
factor $\sqrt2z_{1-\epsilon}/(1-2\epsilon)$ at every squeezing. The
proofs, the grid construction and the tightness computation are in the
[recoil note](record-costs-recoil.md). This is M3 in its universal form:
the clause that carries $h>0$ for every probe is that a record of the
sagitta leaves the delivered impulse undetermined.

## 5. Both factors are in the *Opticks*

Newton's optics supplies the two spreads whose product is $\kappa$, in
the form of two least quantities of the probe.

**A least length, measured.** Book II Part III defines the interval of
the fits as "the space it passes between every return and the next
return" of the ray's disposition to be reflected, and Proposition XVIII
gives it: for the confine of yellow and orange passing perpendicularly
into air, "the Intervals of their Fits of easy Reflexion are the
$1/89000$th part of an Inch", that is about $0.285\,\mu\mathrm{m}$. A
datum obtained through the fits repeats with that period, so it locates
the corpuscle no better; Newton's rings are a gauge of exactly this kind.
This is $\Delta\hat Q_A$.

**A least impulse, posited.** Query 29 asks whether the rays of light are
"very small Bodies emitted from shining Substances", which gives each a
transverse momentum scale. Newton has no way to measure it. This is
$\Delta\hat P_A$.

**Colour dependence, measured.** Observation 13 of Book II Part I reports
the ratio of the red to the violet interval as "greater than as 3 to 2,
and less than as 13 to 8", and "By the most of my Observations it was as
14 to 9". Query 29 makes the violet corpuscles the least and the red the
biggest. The product $\Delta\hat Q_A\Delta\hat P_A$ is therefore colour
dependent on Newton-age evidence, and its universality across the
spectrum is what Planck's constant later supplies.

**Inflexion.** Query 1 asks whether bodies "act upon Light at a distance,
and by their action bend its Rays", most strongly at the least distance,
which is the effect that limits a mark's resolution when the beam is
narrowed to improve it.

**The interval times the momentum is a refraction invariant.** Book II
Part III Prop. XVII makes the intervals in two mediums "as the Sine of
Incidence to the Sine of Refraction", from Observation 10 of Part I, and
Prop. X takes light to be "swifter in Bodies than in Vacuo, in the
proportion of the Sines". Together they make $\Lambda v$, and so
$\Lambda p$, the same in every medium for each colour. A fit counted per
interval along the path therefore counts the Maupertuis action
$\int p\cdot dq$ in units of $\Lambda p$, and the inscribed polygon and the
parabola of Theorem 6 differ by $(F/v)\sum_jA_j/(2\Lambda p)$ fits, with
$A_j$ Lemma XI's tangent areas. Since the fit at arrival decides
reflection or transmission (Prop. XII), the two are optically different
corpuscles on Newton's own terms once that count reaches half an interval.
Extending Props. X and XVII to a continuously varying speed is ours, and
Prop. XV's oblique rule is more complicated than a count along the path.

All eight passages are held verbatim with line anchors in the
[source companion](../docs/classics/Newton_Opticks_1730_fits_and_queries.md),
from the fourth edition of 1730.

## 6. The junction, and the proposition Newton denied

Theorem 4 says what the missing premise is. In the mark-floor note it was
stated as M3, that a mark fixing the position within $\delta$ leaves the
delivered impulse undetermined within $\kappa/\delta$. Theorem 4
identifies $\kappa$ as the probe's own uncertainty product, so

$$\text{M3 for Newton's corpuscle}\quad\Longleftrightarrow\quad
\Delta\hat Q_A\cdot\Delta\hat P_A\ \ge\ \text{a positive constant},$$

which is Robertson's inequality stated in Newton's two quantities. The
floor also uses a clause M3 carries implicitly, that the undetermined
impulse is unrelated to the mark's error; eq. (3) prices that clause.
With M3, §§3--4 give the floor and the insertion mesh from Newton's own
materials, with $\kappa=\Lambda p$ in place of $\hbar/2$; the
identification $\Lambda=\lambda/2$, $p=h/\lambda$ makes $\Lambda p=h/2$,
which differs from $\hbar/2$ by $\pi$.

Newton denied M3, and the denial is explicit rather than inferred.
Proposition XII of Book II Part III states that every ray is "put into a
certain transient Constitution or State, which in the progress of the Ray
returns at equal Intervals, and disposes the Ray at every return to be
easily transmitted". The disposition is a determinate periodic property
carried by the ray, so its fate at a surface is fixed by its phase, and
what a prior record fails to supply is knowledge rather than
determination. On that reading a probe's position and momentum are both
definite, later records can recover the impulse it delivered, $\kappa=0$,
and the comparison has no floor. The countermodel is explicit: let the
corpuscle travel freely after the mark to a screen at distance $D$, and
two position records fix its transverse momentum to within
$p(\delta+\delta_s)/D$, which vanishes as $D$ grows.

The historical claim is therefore narrow and checkable. Newton's optics
contains both factors of the product that bounds the recorded
comparison; his mathematics contains the comparison and takes it to zero;
and the one proposition that would join them is an indeterminacy about
the fits whose negation he asserted in print. The gap between the
*Principia*'s vanishing sagitta and the *Opticks*' finite interval of
fits follows from that single commitment, and the separation of the two
books is incidental to it. No counterfactual about what Newton might have
discovered is needed, and none is offered.

Theorem 6 adds a second junction, and it holds without any bound on
shape. The premise that Theorem 6 uses is the central extension, that an
impulse $J$ and a displacement $d$ compose only up to the phase $Jd/\hbar$
of their parallelogram, where Newton's Corollary I composes them exactly.
Newton's fits already carry a phase whose rate is proportional to
momentum, with the refraction invariant $\Lambda p$ as its unit, and his
determinism in Prop. XII does not touch it. So one of the two quantum
premises, the one that squeezing cannot evade, is present in the
*Opticks* in working form; what it lacks is the universality of
$\Lambda p$ across colours.

## 7. Newton and the classics

### What Newton attempted

In the early 1690s Newton drafted a set of Classical Scholia to
Propositions IV to IX of Book III, arguing that the oldest philosophers
had known universal gravitation and its inverse-square law, so that the
*Principia* recovered a lost wisdom rather than announcing a novelty. He
never printed them. He did pass material to David Gregory, whose
*Astronomiae physicae et geometricae elementa* of 1702 opens with the
programmatic sentence that lest the physics delivered here seem something
new and unheard of in astronomy, *eandem vetustissimis Philosophis notam
... ostendam*, I shall show it was known to the most ancient
philosophers, naming Anaxagoras, Archelaus, Euripides and Pythagoras.
That preface is the printed witness closest to the unpublished scholia,
and the [source companion](../docs/classics/Gregory_AstronomiaeElementa_Praefatio_1702_OCR.md)
holds its programmatic paragraph. The scholarship is Casini, "Newton: The
Classical Scholia", *History of Science* **22** (1984), 1--46, and
Mosley, "The Origins and Sources of Newton's Classical Scholia",
*Erudition and the Republic of Letters* **9** (2024), 171--217, both
verified at metadata level here and both still to be read.

So Newton did attempt a preface founded on the classics, and the attempt
was doxographic. He sought ancient authority for a law he had already
proved, and the authority he sought was for the *conclusions* of Book III.

### The ancient arguments he passed over

The ancient material that bears on the *method* of Book I is the debate
over division and the cut, and it is absent from the scholia. Six
positions, each held here in a primary witness:

- **Democritus's cone** (Plutarch, *De communibus notitiis* 39). Cut a
  cone by a plane parallel to the base: are the surfaces of the two
  adjacent sections equal or unequal? If equal, the cone is a cylinder;
  if unequal, it is stepped. Chrysippus answers that the surfaces are
  neither equal nor unequal while the bodies are unequal, and Plutarch
  calls that a licence to write whatever comes to mind.
- **Zeno's arrow** (Aristotle, *Physics* VI.9). At every now the flying
  arrow occupies a space equal to itself and so is at rest, and what is
  at rest at every now does not move. Aristotle's diagnosis is that the
  argument assumes time to be composed of nows.
- **The Mohist endpoint** (*Mozi*, Canons and Explanations). Halving
  terminates at an endpoint that cannot itself be halved.
- **Liu Hui's cutting** (commentary on the *Nine Chapters*, 263 CE). The
  finer the cutting the smaller the loss; cut and cut again until it
  cannot be cut, and the polygon coincides with the circle with nothing
  lost.
- **Hui Shi's stick** (*Zhuangzi* 33). A stick one foot long, halved
  every day, is not exhausted in ten thousand generations.
- **The leap and the time-atom** (al-Shahrastani on al-Nazzam; Maimonides,
  *Guide* I.73). The interval is divisible, yet it is crossed by leaps;
  and for the kalam, time is composed of atoms.
- **The Vaiśeṣika arrow** (*Vaiśeṣikasūtra* 5.1.16--18, layered, c. 100
  BCE--200 CE, attribution to Kaṇāda traditional). The arrow's particular
  conjunctions are *ayugapat*, non-simultaneous, and that is the ground of
  the plurality of its motions; impulsion causes only the **first** motion,
  and each later one is caused by the *saṃskāra* deposited by the motion
  before it, until the impression is spent and gravity takes over.
- **Sound produced from sound** (*Vaiśeṣikasūtra* 2.2.36--37 in the
  Candrānanda recension, 2.2.31 in the vulgate). Sound arises from
  conjunction, from disjunction, and from sound, and is non-eternal, so what
  reaches the ear is a later member of a generated chain. Vātsyāyana's
  *Nyāyabhāṣya*, within the window at about 400 to 450 CE, argues the point
  from observation: the axe-blow is still heard at a distance after the
  axe-wood contact has ceased.
- **No motion at all** (Vasubandhu, *Abhidharmakośabhāṣya* ad IV.2, c.
  350--450 CE). *na gatir yasmāt saṃskṛtaṃ kṣaṇikam*, there is no motion,
  because the conditioned is momentary; everything conditioned "is destroyed
  in the very place where it arose", so its passage to another place is
  impossible. Zeno concludes this and treats it as absurd; Vasubandhu
  concludes it and accepts it.
- **A medium that permits motion** (Umāsvāti, *Tattvārthasūtra* 5.17--18,
  c. 2nd--5th c. CE). *gatisthityupagrahau dharmādharmayor upakāraḥ*: the
  assisting of motion and of rest is the function of *dharma* and
  *adharma*. These substances push nothing; they are the standing condition
  without which motion could not occur, and space is given the separate
  office of accommodation.
- **Sound as spreading waves** (Diogenes Laertius VII.158, reporting Stoic
  doctrine). Hearing occurs when the air between is struck, "a vibration
  which spreads spherically and then forms waves and strikes upon the ears,
  just as the water in a reservoir forms wavy circles when a stone is thrown
  into it". The same water-ring image carries the Vaiśeṣika *vīcī-santāna*,
  so the model is attested independently in both traditions.
- **Continuity that fails below sense** (Epicurus, *Letter to Herodotus*
  61--62, in Diogenes Laertius X). Atoms travel at equal speed through the
  void, and in aggregates they "move in different directions in times so
  short as to be appreciable only by the reason, but frequently collide
  until the continuity of their motion is appreciated by sense"; the
  assumption that continuity persists below observation "is not true in the
  case before us".
- **Least partless bodies** (Diodorus Cronus, reported at Sextus Empiricus,
  *Pyrrhoneion Hypotyposeis* III.32). Listed in the doxography of material
  principles between the atoms of Democritus and Epicurus and the unjointed
  masses of Heraclides. Diodorus argued from those minima that "a thing
  never is moving, but it has moved", the Greek twin of Vasubandhu's *na
  gatiḥ* three centuries earlier; the formula is at *Adversus Mathematicos*
  X and is cited here without being read.
- **The voice as spherical waves** (Vitruvius, *De architectura* V.3.6--7,
  c. 25 BCE). The voice is propelled "by an infinite number of circles
  similar to those generated in standing water when a stone is cast
  therein", but "whereas the circles in water only spread horizontally, the
  voice, on the contrary, extends vertically as well as horizontally", so
  the water-ring image is corrected into a spherical wave by argument from
  the disanalogy.
- **The sling, applied to an orbit** (Plutarch, *De facie in orbe lunae*
  923C--D, c. 100 CE). "The moon is saved from falling by its very motion
  and the rapidity of its revolution, just as missiles placed in slings are
  kept from falling by being whirled around in a circle", with 923D adding
  that "each thing is governed by its natural motion unless it be diverted
  by something else".

Lemmas X and XI perform exactly the operation these positions dispute.
The scholia cite the ancients for what Book III concludes and leave them
silent on how Book I proceeds.

The last four entries differ in kind from the rest, and they matter most
here. The Greek and Chinese items are paradoxes about division, which set
a problem. The Indian entries answer it, and they answer it three
different ways: the arrow's flight is many motions carried by an
impression (Vaiśeṣika), or it is no motion at all because each thing
perishes where it arose (Vasubandhu), or it is possible only because a
medium stands ready to permit it (Umāsvāti). Each also carries a stopping
rule for division: the Nyāya *paramāṇu* than which nothing is smaller, the
directional-parts reductio by which a touched atom would have parts, and
the Jain atom that has no space-points at all. The Vaiśeṣika sūtras in
particular state a **positive theory of propagation**: motion is a succession of numerically distinct events, each
carried to the next by a quantity the previous one deposits, and
transmission through a medium is a chain in which what arrives is a later
member than what was sent. That is the structure Theorem 2 quantifies. Its
protocol-universality holds because the signal is a phase-space path whose
total variation is unchanged by subdivision, which is the modern form of
the claim that impulsion supplies only the first motion while the
impression carries the rest. An ancient author had therefore already
framed propagation as a bounded succession rather than a continuous
traversal, and Newton's classical preface reached for none of it.

### The hierarchy the ancient premises generate

Read as premises about records rather than about geometry, the cone and
the arrow are the first members of a sequence whose next member is
Newton's comparison. The apparatus of §3 covers all of them; what changes
is the order of the signal against the nuisance it must beat.

**Theorem 5.** In the model of §3, with every mark obeying
$\delta_j\Delta_j\ge\kappa$:

(i) *The arrow.* Distinguishing rest from uniform motion at speed $v$,
with the initial position unknown, requires

$$m\,v^2\tau\ \ge\ 8\,z_{1-\epsilon}^2\,\kappa,
\qquad\text{that is}\qquad \tau\,E_{\rm kin}\ \ge\ 4\,z_{1-\epsilon}^2\,\kappa .$$

(ii) *Newton.* Distinguishing uniform motion from constant force, with
the initial position and velocity unknown, requires
$F^2\tau^3/m\ge96z_{1-\epsilon}^2\kappa$, which is Theorem 2.

(iii) *The cone.* Measuring a static taper requires nothing. With no
recoil to propagate, the deflection grows without bound as marks
accumulate, so a static solid has no floor.

*Proof.* For (i) the nuisance is the constant, so $u$ ranges over vectors
with $\sum_iu_i=0$ alone. With $P(t)=vt$ the identity of §3 reads
$u^{\mathsf T}P=v\sum_iu_it_i=v\,T(0)$, and $T(\tau)=0$ with
Cauchy--Schwarz gives $|T(0)|=|\int_0^\tau T'|\le\sqrt\tau\sqrt E$. The
noise bound $u^{\mathsf T}\Sigma u\ge2\kappa E/m$ needs only
$\sum_iu_i=0$ and so is unchanged. Hence
$d^2\le v^2\tau E\,m/(2\kappa E)=m v^2\tau/(2\kappa)$, and
$d\ge2z_{1-\epsilon}$ gives the claim. For (ii) the nuisance is the
linear space, $u^{\mathsf T}P=\frac Fm\int_0^\tau T$, and the proof of
Theorem 2 applies. For (iii) the marks leave the object unchanged, so
$\Sigma=\operatorname{diag}(\delta_j^2)$; with $N$ marks of resolution
$\delta$ at each of two heights separated by $\Delta h$, the taper
$\vartheta$ gives $d^2=N\vartheta^2\Delta h^2/(2\delta^2)$, unbounded in
$N$. $\square$

The two dynamical cases share one invariant. If the signal is the $n$-th
order departure $P$ with $P(0)=\dots=P^{(n-1)}(0)=0$, the quantity the
theorem bounds below is

$$m\,\bigl(P^{(n)}\bigr)^2\,\tau^{2n-1}\ \gtrsim\ \kappa ,$$

which has the dimensions of action for every $n$: at $n=1$ it is
$mv^2\tau$, twice the kinetic energy times the duration, and at $n=2$ it
is $F^2\tau^3/m$, twice $\tau\Delta E$. Newton's comparison is the second
rung of a ladder whose first rung is Zeno's.

### Why the arrow and not the sling

One feature of the list needs saying. Almost every ancient entry is
rectilinear or static, while the case Newton uses to **define** centripetal
force is the sling: Definition V has the stone whirled about in a sling
endeavouring to recede from the hand, and names the force that "retains it
in its orbit" after the planets "perpetually drawn aside from the
rectilinear motions, which otherwise they would pursue".

The exception is Plutarch, and it is a pointed one. *De facie* 923C has the
moon kept from falling "just as missiles placed in slings are kept from
falling by being whirled around in a circle", which is Newton's apparatus
applied to Newton's case a millennium and a half earlier. The inference
runs the other way: for Plutarch the whirling *prevents* the fall, so speed
sustains; for Newton the cord *pulls the stone inward*, and what it diverts
is a straight line that would need no cause. The same object supports
opposite accounts, and what separates them is which motion is taken to be
free. Plutarch's next clause, that "each thing is governed by its natural
motion unless it be diverted by something else", is as near as the passage
comes, with natural motion still doing the work inertia later does. Newton
had read him: the Classical Scholia name Plutarch among the ancients said
to have known the doctrine of gravitation, so the sling was available in a
text he was mining for authority while writing the propositions it models.

Theorem 5 explains why the exception stayed isolated, and Aristotle supplies
the other half of the reason. *De caelo* I.2 makes uniform circular motion
the natural motion of the aether, needing no cause, which is the exact
inverse of Definition V. For the heavens, then, curved motion was the default
and straight motion the anomaly, so the sling illustrates a conclusion
already held rather than posing a problem. The claim that the ancients treat
rest as natural holds below the moon and is incomplete above it; the
reference is at metadata level here. The ancient question is the
first rung, whether the thing moves at all, with position as the only
nuisance. The sling is the second rung, whether a force acts, with uniform
motion as a further nuisance, and that rung cannot be stated until
straight-line motion is held to need no account. Ancient physics largely
does not hold that, so the sling has no work to do in it. The Vaiśeṣika
comes closest by charging only the first motion to impulsion, and stops
short of making a straight continuation free and a curved one costly.

Indian sources do supply one whirled object, and use it for a third
purpose again. The firebrand circle, *alātacakra*, appears in Vasubandhu
(Pradhan 189.23--24) to argue that because contact with the parts is
successive, the awareness of a whole is really of the parts, and at
Pradhan 33.9 with *āśuvṛttyā*, by rapid action. That is an argument about
sampling, and it is the ancient form of what Theorem 5 says about records:
below the mesh a succession is indistinguishable from the continuous thing
it mimics. The [companion note](arrow-not-sling.md) sets this out.

### What each ancient premise buys

- **Zeno.** His conclusion holds of records: below
  $\tau_{\rm arrow}=8z^2\kappa/(mv^2)$ every mark is consistent with
  rest. Aristotle's diagnosis explains why, since a now carries no
  record and every datum is a window.
- **The Vaiśeṣika arrow and the chain of sounds.** These supply the
  positive half the Greek material lacks. Theorem 5's ladder is their
  statement made quantitative: the succession is real, each step carries a
  bounded quantity to the next, and reading any one step costs $\kappa$.
  The sound chain is the case where an ancient author asserts a finite
  propagation time and argues it from an experiment, which is the premise
  Newton's determinate fits deny for light.
- **Vasubandhu.** His conclusion is what the theorem says about *records*
  rather than about the world. Below the mesh every mark is consistent with
  rest, so no recorded instant exhibits motion and travel is never
  displayed, only inferred from enough instants together. The theorem
  declines his further step from the records to the world, and Theorem 5(i)
  measures exactly how many instants are needed.
- **Epicurus.** His is the closest ancient statement to what the theorems
  say about records. Motion presents itself as continuous to sense and is a
  succession below it, and he names the fallacy of extrapolating the
  observed continuity downward. He draws the boundary where sense fails;
  Theorem 5 draws it at a mesh computed from the mark cost, which is the
  difference between a threshold that is reported and one that is derived.
- **Umāsvāti.** The Jain medium is the one ancient category with no
  counterpart in the theorem, and its absence is informative. Theorems 2
  and 5 need no medium: what they price is the mark, not the motion.
  A doctrine on which motion requires a permitting substance predicts
  nothing about the cost of observing it, which is the respect in which
  this entry sets a limit on how far the reconstruction reaches.
- **Democritus and Chrysippus.** The dilemma about adjacent sections
  dissolves with resolution alone, and case (iii) shows it needs no
  action floor. Adjacent recorded sections are equal, and the inequality
  of the bodies is recovered cumulatively, which is Chrysippus's answer
  given a definite sense. This corrects a heuristic recorded earlier in
  this programme, that the cone is the arrow rotated into Euclidean
  time: the static problem lacks back-action, and back-action is the
  entire source of the floor.
- **The Mohists and Liu Hui.** They are right about records. Cutting
  stops, and the endpoint is the mesh
  $\tau_*=(96z^2m\kappa/F^2)^{1/3}$, which is Corollary 3.
- **Hui Shi.** He is right about geometry, which is Proposition 1: the
  halving never ends, and nothing in the figure resists it.
- **Al-Nazzam.** The recorded trajectory below the mesh is his leap. The
  interval stays divisible, and the crossing is exhibited only in
  finitely many steps.
- **The kalam time-atom.** Denied. The mesh depends on $F$, on $m$ and on
  the confidence demanded, so it is a dynamical resolution rather than a
  universal atom of time. A floor on action coexists with a continuum of
  instants, and Theorem 5 shows the mesh moving as the force changes.

The section's claim about Newton is therefore double. He looked to the
ancients for authority and found the wrong ancients, taking the
doxography of gravitation while passing over the dispute about division
that his own Lemmas turn on. And the premise that would have converted
that dispute into a theorem, an indeterminacy in the least parts of
light, is one the atomists supply in the form of a least part and one he
denied in the single place where he had a measurement.

## 8. What the theorem does not give

**Preparations of unbounded extent.** Theorem 2 concerns protocols that
mark the trajectory. A protocol that prepares once, waits and measures
once faces a different bound. In that case the two hypotheses differ by
the phase-space displacement $(-F t^2/2m,\ Ft)$, whose components have
product exactly $\tau\Delta E$, and Mandelstam--Tamm in the geometric form
of [Anandan and Aharonov](https://doi.org/10.1103/PhysRevLett.65.1697)
(PRL **65**, 1697, 1990), with Helstrom's
discrimination bound (*Quantum Detection and Estimation Theory*, 1976),
gives

$$\frac{F\tau L}{\hbar}+\frac{F\tau^2P}{2m\hbar}\ \ge\ 1-2\epsilon,
\qquad\tau\Delta E\ \ge\ \frac{2m(1-2\epsilon)^2\hbar^2\tau}{(2mL+\tau P)^2},$$

for an apparatus whose position and momentum spreads are bounded by $L$
and $P$. The floor equals $(1-2\epsilon)^2\hbar^2/(4LP)$ at the balanced
aperture $L=\tau P/2m$ and falls to zero as either side grows at fixed
area, so a squeezed state of area $\hbar/2$ evades it as a large one
does. In Newton's quantities the first inequality is
$F\tau\cdot L+\frac{F\tau^2}{2m}\cdot P\ge(1-2\epsilon)\hbar$, the
impulse of Proposition I against the position aperture plus the sagitta
of Lemma X against the momentum aperture. It holds for every finite adaptive
protocol of instruments, because the displacement is a phase-space path
whose total variation does not grow when it is subdivided. The bound is
tight: two narrow packets separated by $\pi\hbar/(F\tau)$ decide the
comparison with error probability of order $\tau\Delta E/\hbar$, for
arbitrarily small $\tau\Delta E$, at the price of an apparatus whose
extent diverges. So the floor of order $\hbar$ requires either that the
trajectory be marked or that the laboratory be bounded, and a
non-Gaussian preparation of unbounded extent evades it.

**Prior art.** The combination $F^2\tau^3\gtrsim m\hbar$ is the standard
quantum limit for detecting a force on a free mass (Braginsky and
Khalili, *Quantum Measurement*, 1992; the canonical statement is Caves,
Thorne, Drever, Sandberg and Zimmermann, *Rev. Mod. Phys.* **52**, 341,
1980), and its status has been disputed since Yuen's objection: Caves
defended it (PRL **54**, 2465, 1985) and Ozawa exhibited a measurement
breaking it for free-mass position (PRL **60**, 385, 1988). That
non-Gaussian preparations beat the limit, which is §7's counterexample,
is stated as a principle by Giovannetti, Lloyd and Maccone (*Science*
**306**, 1330, 2004). The contribution here is universality over protocols
with an explicit constant, the exact mark cost of Theorem 4, and the
identification of the premise. The inequality itself is not new.

**The classical theorem belongs to a literature it does not cite.**
Worst-case recovery of a linear functional from noisy linear data is optimal
recovery in the sense of Micchelli and Rivlin (1977), and the apparatus
series this programme built, together with Theorem 1's worst-case form, are
results of that kind; information-based complexity (Traub, Wasilkowski and
Woźniakowski, 1988) is the same setting. The invariant-test step of
Theorem 2 is standard (Lehmann and Romano). A referee from either community
will ask why these go unmentioned, and the honest answer is that the
theorems were derived without them.

**Instruments outside the momentum-transfer class.** Theorem 4 holds
where $[\hat N,\hat D]=-i\hbar$. Its coupling is von Neumann's (1932), its
inequality Robertson's (1929), and its ancestor the Heisenberg microscope
(1927); Bohr and Rosenfeld (1933) and Araki and Yanase (1960) are where
limits of this kind from field measurability and from conservation laws are
set. The class is wider than it looks. For any coupling and any pointer,
the commutation of the pointer with the body's momentum after the mark
gives $[\hat N,\hat D]=-i\hbar-[\hat y,\hat D]-[\hat N,\hat p]$ (the
joint-measurement argument of Arthurs and Goodman, PRL **60**, 2447, 1988),
so every mark whose error and impulse do not depend on the body has
conjugate error and impulse; if it also leaves the position alone it is a
von Neumann mark on some canonical pair of the apparatus; and Theorem 8
holds for all such marks, position-displacing ones included
([additive-noise note](additive-noise-marks.md)). For every instrument,
body-dependent noise included, the offset between the hypotheses must be
carried through each mark, and that costs the spread of
$c_j\hat D_j-mc_j'\hat X_j$, with $\hat D_j$ and $\hat X_j$ the mark's
momentum and position disturbances; for the constant force,

$$\frac s8\sum_j\Delta(\hat D_j)+\frac J2\sum_j\Delta(\hat X_j)\ \ge\ (1-2\epsilon)\hbar,\qquad J=F\tau,$$

the sagitta paired with the momentum disturbance and the impulse with the
position disturbance, as in the aperture bound
([disturbance note](record-costs-disturbance.md)). The reading error does
not enter, so Ozawa's relation (PRA **67**, 042105, 2003) is not needed;
the calibration relation of Busch, Lahti and Werner (PRL **111**, 160405,
2013) is likewise unused. No error--disturbance relation is used above.

## 9. Obligations before submission

Two, both on the history side, and both stated so that a reader can see
what the present draft rests on.

1. **Historiography, to be read rather than cited.** On the *Opticks*
   side, Shapiro's *Fits, Passions, and Paroxysms* (1993) on the theory of
   fits and how determinate Newton meant it, which is where §6's central
   claim must be tested, and Sabra's *Theories of Light from Descartes to
   Newton* (1981) for the context of Query 29. On the *Principia* side,
   Guicciardini's *Reading the Principia* (1999) and his *Isaac Newton on
   Mathematical Certainty and Method* (2009) for what the limit arguments
   of §2 were for, De Gandt's *Force and Geometry* (1995) directly on the
   sagitta, and Bertoloni Meli's *Thinking with Objects* (2006) on the
   sling and the pendulum as objects to think with. On the scholia,
   McGuire and Rattansi, "Newton and the 'Pipes of Pan'" (1966), beside
   Casini and Mosley. On the ancient comparison, Sorabji's *Time,
   Creation and the Continuum* (1983), which treats Zeno, Diodorus
   Cronus, Epicurean minima and kalām atoms together; von Rospatt (1995)
   on momentariness; Dhanani (1994) on kalām atomism and the Indian
   influence question; and Lloyd and Sivin's *The Way and the Word*
   (2002) as the methodological standard that protects §7 from the charge
   of naive parallelism. Clagett (1959) for impetus, where Philoponus'
   *rhopē* is the Western counterpart of *saṃskāra*.
2. **Editions.** The *Opticks* passages come from a transcription of the
   1730 fourth edition and should be cited from that printing; the
   *Principia* passages should be cited from Cohen and Whitman in place
   of the Motte text used here.

Three mathematical items remain open and are not obligations of the
paper: extending Theorem 4 beyond the momentum-transfer class; the
general force law, for which the proof of Theorem 2 already pairs
$\int_0^\tau P''T$ against the Dirichlet energy and so bounds a norm of
$P''$; and closing the constants between the worst-case form, the
statistical form of Theorem 2 and the single-shot form of §7.

## 10. Consequence for STATE

This is the synthesis the goal asked for: the Planck gap established
with Newton-age arguments and their modern equivalents, in one document
whose historical and technical halves are load-bearing for each other.
The foundations content is Theorems 2 and 4 with §7's honest
positioning; the history content is §§5--7, resting on the source
companions; the junction is the identification of M3 with Robertson's
inequality for the corpuscle. STATE's queue reduces to §9's
obligations and the three open mathematical items.

Revision, 2026-09-22: both quantum floors needed a bound on the shape of
an uncertainty ellipse, since the aperture corollary and the mark floor
each fall to zero under squeezing at fixed area. Eq. (3) and the
$(L,P)$ form of §8 are the corrected statements. A floor with no shape
bound needs a quantity that squeezing cannot move, and Theorem 6
supplies it: the phase between Newton's inscribed polygon and the
parabola, whose Newton-age form is the fits count of §5. The same day
Theorem 2's constant became sharp, $48$ in place of $9$, because the
invariance under $v_0$ pins $T$ at both ends of the interval.
