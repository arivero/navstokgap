# Time blocking, Newton polygons and explicit quantum action

A bounded inward central force admits a unique classical passage through
the centre at nonzero speed. At a zero-speed encounter with a bounded
repulsive force, two continuations of the same incoming orbit obey the
same force balance after every time insertion and have equal action on
every cell. A detector at a fixed time distinguishes them. Two shrinking
source profiles select the opposite returns, yet the fraction of incoming
classical flux that reaches either core tends to zero as an exact power
of its radius. [Central-force passage](#central-force-passage-under-point-insertion).

For repulsive inverse-square scattering, three incident energies make a
different test possible. A sum of measured angular yields must vanish
for every common classical distribution of impact parameters, including
a sharply concentrated beam. An observed excess over the calibration
error gives a lower bound on a trial action in the spin-zero Coulomb
exchange model. [Three-energy test](#a-three-energy-test-of-central-force-trajectories).

In a potassium waveguide, the fraction crossing a repulsive barrier at
high laser power bounds how many low-power atoms could have turned
near it. At the reported preparation's nominal widths, at least ten
percentage points of the incident flux need another explanation if the
beam presents the same axial potential to every atom. A second image
would locate the returning atoms. The same bound applies to outward
motion through a spherical shell. [Two barrier powers](#locating-a-turn-with-two-barrier-powers).

When the orbit returns through the same barrier, the exterior flight
times alone bound a late population on the far side by an earlier
population near the barrier. The unknown static force inside cancels.
[Two images of a returning orbit](#two-images-of-a-returning-orbit).

Individual rubidium atoms also return after spreading across a tilted
lattice. Three site counts test whether a Newtonian atom can turn after
crossing several downhill cells. On a discrete clock two different
actions can give exactly the same complete site record.
[A single atom returning in a tilted lattice](#a-single-atom-returning-in-a-tilted-lattice).

For an alpha particle leaving lead-208, an exterior population gain on a
fixed clock would bound a trial action if the same radial barrier covers
every way out. Separate scattering and decay experiments test how much
work a classical alternative must supply. [Polonium escape](#a-clock-on-escape-through-a-central-force-barrier).

Electron transmission through argon supplies a single-energy comparison
without identical-particle exchange. A finite annulus of exterior Newton
orbits would miss the measured exit aperture if the polarization force
has at least half its asymptotic strength beyond $0.50$ nm, with the upper
control specified below. The published attenuation fixes the size of the
discrepancy such a force calibration would have to explain.
For a freely moving charge coupled to a localized, linearly polarizable
target, two clocked response measurements suffice to bound how much the
delayed force changes the outgoing angle.
[Argon transmission](#an-exterior-force-test-with-argon) and
[free-charge calibration](#two-pulse-tests-for-a-freely-moving-charge).

At lower energy the relevant orbits move out into the weak field of the
atom. Their angular momenta tend to zero, yet they give a positive lower
limit for relative speed times momentum-transfer cross section. Three
finite work readings give a separate test at a specified energy, allowing
charge penetration and nonlinear electrostatic relaxation.
[Work measurements and the threshold rate](#three-work-readings-and-the-low-energy-limit).

At 77 K a double shutter recorded an argon electron drift of 36 m/s.
An exterior force comparison bounds both this drift, with a measurable
allowance for heating, and the displacement of a field-free thermal
packet at a fixed time. The latter uses one final position per
electron. [The thermal shutter and displacement tests](#a-thermal-test-with-two-shutters).

Three helium-3 gas measurements test a central force without specifying
its strength at any radius. Every fixed classical pair potential gives
a concave second virial coefficient as a function of inverse temperature.
The published values bend the other way. A classical atom with thermally
populated internal states can reproduce the three readings. In the normal
liquid, the heat needed to warm a fixed volume independently tests whether
those atoms retain three mobile, thermally equilibrated momenta apiece.
[Gas pressure](#helium-pressure-at-three-temperatures) and
[liquid calorimetry](#how-many-atomic-motions-can-the-measured-heat-support).
In a helium isotope mixture the vapour and liquid compositions also
test constrained atomic motion. Their measured enrichment fixes a
minimum isotope-dependent work for a classical explanation.
[Isotope exchange](#isotope-exchange-as-a-test-of-central-forces).

**First calculation, 2026-10-27; written derivation, unrefereed.** In
one spatial coordinate and one time variable, the same discrete Green
function controls three operations: constructing a Newton polygon on an
arbitrary time partition, solving its nonlinear boundary-value problem,
and bounding the inverse action Hessian used to integrate fluctuations.
A force Lipschitz constant gives bounds uniform in the number and placement
of inserted times. The quadratic fluctuation covariance contains an explicit
factor of $\hbar$; this first calculation does not derive its positivity.

**Targeted second opinion (GPT-6.1 Terra, 2026-10-27).** Terra read this
note and checked the Green row sum, Hessian/response bounds, Gaussian
covariance, oscillator determinant and constant-force signs without finding
an algebraic error. This was a targeted written check, not a full independent
proof review. The arbitrary-cut interpretation below came from that pass.

The time lattice has one dimension. Sections 1–6 place one mechanical
coordinate at each time. The central-force calculation places a particle
in three-dimensional space at each time. The force polygons are modern
constructions. The Galileo observable remains the displacement between
the inertial line and the falling parabola.

We assemble standard Green-function, contraction and Gaussian-elimination
arguments. No literature novelty is claimed. The source ingredient is
Balaban's controlled effective density under blocking, described in his
[ICM overview](../docs/balaban/Balaban_UltravioletStability_ICM1986_1987.md),
printed pp. 1260--1262 (text read), and Dimock's
[small-field exposition](../docs/balaban/Dimock_BalabanI_1108.1335v2.md),
sections 2.1, 2.4, 4.5 and Theorem 14 (selected passages read). The
[existing refinement note](refinement-composition-and-limit.md) constructs
constant-force and harmonic limits. The [cut-measure note](cut-measure-newton.md),
Proposition 7, already uses nodal exactness of the same one-dimensional
Green function. The [Rivero test](rivero-1998-conjecture-central-forces.md),
section 2, supplies the determinant/Schur identity and its branch caveat.

## 1. Actions and the constant to be investigated

Let $m,T>0$, $x,y\in\mathbb R$, and
$\pi=(0=t_0<\cdots<t_N=T)$. Write
$\tau_j=t_{j+1}-t_j$ and $w_j=(\tau_{j-1}+\tau_j)/2$ for interior vertices.
For a potential $V$ define

$$
 S_\pi^\sigma(q)=\sum_{j=0}^{N-1}
 \frac{m(q_{j+1}-q_j)^2}{2\tau_j}
 +\sigma\sum_{j=0}^{N-1}\frac{\tau_j}{2}
       [V(q_j)+V(q_{j+1})],\qquad q_0=x,\ q_N=y.
 \tag{1}
$$

The real-time Newton action is $S_\pi^R=S_\pi^{-1}$, with weight
$e^{iS_\pi^R/\hbar}$ when $\hbar>0$. The Euclidean action is
$S_\pi^E=S_\pi^{+1}$, with weight $e^{-S_\pi^E/\hbar}$.
Their stationary equations have opposite potential signs. They must not
be interchanged when interpreting a background as a Newton trajectory.
At $\hbar=0$ these exponential expressions are not defined; the classical
stationary equation is defined directly. No relativistic premise or $c$
is used in this calculation. Ordinary Planck action is $h_P=2\pi\hbar$.

For real time put $f=-V'/m$, the acceleration. Section 2 needs only a
Lipschitz function $f$, even without first specifying $V$. A Lipschitz
condition is a sufficient uniqueness and stability condition; continuity
alone can give local existence. Neither statement alone guarantees
continuation for all times or uniqueness of a two-endpoint problem.

## 2. Arbitrary intermediate times

Let $\ell(t)=x+(y-x)t/T$ and

$$
 G(t,s)=\min(t,s)-\frac{ts}{T}.
 \tag{2}
$$

This is the positive Dirichlet Green function of $-d^2/dt^2$. Define the
polygon map, with piecewise-linear output, by

$$
 (\mathcal T_\pi q)(t)=\ell(t)
       -\sum_{j=1}^{N-1}w_jG(t,t_j)f(q(t_j)).
 \tag{3}
$$

**Lemma 1 (the exact row sum).** At every vertex,

$$
 \sum_{j=1}^{N-1}w_jG(t_i,t_j)=\frac{t_i(T-t_i)}2.
 \tag{4}
$$

At every $t\in[0,T]$ the sum is at most $T^2/8$.

*Proof.* For fixed $t_i$, the function $s\mapsto G(t_i,s)$ is linear
on each partition interval and vanishes at the endpoints. Its trapezoidal
integral is therefore exact, and its integral is $t_i(T-t_i)/2$.
As a function of $t$, the sum in (4) is the linear interpolant of that
concave quadratic. It lies below the quadratic, whose maximum is $T^2/8$.
This proof uses no ratio between consecutive time steps. $\square$

Assume $|f(u)-f(v)|\le\Lambda|u-v|$ for all $u,v$, and put

$$\theta=\frac{\Lambda T^2}{8}<1.\tag{5}$$

**Proposition 2 (one bound for every polygon).** The map (3) has a
unique fixed polygon. Its slopes $v_j=(q_{j+1}-q_j)/\tau_j$ satisfy

$$v_j-v_{j-1}=w_jf(q_j).\tag{6}$$

The continuous map

$$
 (\mathcal Tq)(t)=\ell(t)-\int_0^T G(t,s)f(q(s))\,ds
 \tag{7}
$$

has a unique fixed point, which is $C^2$ and solves
$\ddot q=f(q)$ with the two prescribed endpoints. Every sequence of
partitions with $|\pi|\to0$ converges to this solution. Neither nesting
nor equal intervals is required.

*Proof.* Lemma 1 bounds the Lipschitz constants of (3) and (7) in the
supremum norm by $\theta$. Repeated application converges because the
successive differences form a geometric series. This proves existence
and uniqueness in the complete polygon space or in $C([0,T])$.
The derivative of $G(\cdot,t_j)$ jumps by $-1$ at $t_j$, giving (6).
Differentiating (7) gives the continuous equation.

Inserting a vertex changes its neighbours' weights $w_j$ as well as the
new solution. It does not add one kick while freezing the old force
history. Retained vertices need not remain fixed when the trapezoidal
action itself is refined.

For a quantitative limit, write $B=\|f(q)\|_\infty$ and
$U=\|\dot q\|_\infty$ for the continuous solution. For every fixed $t$,
$s\mapsto G(t,s)f(q(s))$ is Lipschitz with constant at most
$B+T\Lambda U/4$. On an interval of length $\tau$, replacing its integral
by the endpoint trapezoid has error at most half that constant times
$\tau^2$. Hence

$$
 \|q_\pi-q\|_\infty\le
 \frac{T|\pi|}{2(1-\theta)}
       \left(B+\frac{T\Lambda U}{4}\right).
 \tag{8}
$$

Indeed, subtract the two fixed-point equations and absorb the
$\theta\|q_\pi-q\|_\infty$ term. The constants in (8) belong to the
fixed solution and interval, not to the partition. $\square$

For a force Lipschitz only in a tube $|q(t)-\ell(t)|\le r$, the same
proof holds within that tube if $\theta<1$ and

$$
 \frac{T^2}{8}\big(B_0+\Lambda r\big)\le r,
 \qquad B_0=\sup_t|f(\ell(t))|.
 \tag{9}
$$

This makes the closed tube invariant. Uniqueness is then asserted only
inside it. Equation (9) is a finite version of a small-field domain that
survives the construction; it cannot justify discarding paths outside it
from a statistical or oscillatory integral.

## 3. The action Hessian and elimination

Let $\mathsf K_\pi$ be the Dirichlet stiffness matrix, with diagonal
$1/\tau_{j-1}+1/\tau_j$ and adjacent entries $-1/\tau_j$, and let
$\mathsf W_\pi=\operatorname{diag}(w_j)$. The tent function (2) gives

$$
 (\mathsf K_\pi^{-1})_{ij}=G(t_i,t_j),\qquad
 \|\mathsf K_\pi^{-1}\mathsf W_\pi\|_{\infty\to\infty}
       \le\frac{T^2}{8}.
 \tag{10}
$$

The first identity follows by taking the slope jump of that tent at each
node; the second is Lemma 1. In particular, for $V\in C^2$ with
$|V''|\le m\Lambda$, the Hessian of (1) obeys

$$
 \mathsf H_\pi^\sigma
   =m\mathsf K_\pi+\sigma\mathsf W_\pi
             \operatorname{diag}(V''(q_j))
   \ \ge\ m(1-\theta)\mathsf K_\pi.
 \tag{11}
$$

To see the quadratic-form inequality, the nonnegative matrix
$\mathsf K_\pi^{-1}\mathsf W_\pi$ has spectral radius at most its maximum
row sum. It is similar to the positive symmetric matrix
$\mathsf W_\pi^{1/2}\mathsf K_\pi^{-1}\mathsf W_\pi^{1/2}$.
Thus $\mathsf W_\pi\le(T^2/8)\mathsf K_\pi$, which proves (11).
The factor $1-\theta$ is uniform over arbitrary partitions.

For a physical force source $J_j$, inserted as a linear action term
$\sum_jw_jJ_jq_j$, the stationary response therefore has the bound

$$
 \|\delta q\|_\infty\le
 \frac{T^2}{8m(1-\theta)}\|\delta J\|_\infty.
 \tag{12}
$$

Here the bound is for the differential response. It follows directly
by factoring $\mathsf H_\pi^\sigma$ as
$m\mathsf K_\pi(I+\mathsf K_\pi^{-1}\mathsf W_\pi
\sigma\operatorname{diag}(V'')/m)$ and using a Neumann series.

With the global curvature bound, (11) makes the finite action coercive
and strictly convex in its interior vertices. Eliminating some vertices
by minimization is then unambiguous, and its Hessian is the Schur
complement

$$
 \mathsf H_{BB}-\mathsf H_{BA}\mathsf H_{AA}^{-1}\mathsf H_{AB}.
 \tag{13}
$$

Successive eliminations associate. With only a local tube, this is a
statement on the chosen nondegenerate branch. In particular, for the
real-time positive quartic potential the unrestricted action is unbounded
below, as the Rivero note already records; local control is not a global
minimization theorem. Nor does the eliminated action generally retain
only the original kinetic and potential terms.

## 4. What the same inverse says when $\hbar$ is present

At a Euclidean background, its Gaussian fluctuation reference has density
proportional to
$\exp[-\eta^T\mathsf H_\pi^E\eta/(2\hbar)]$ and covariance

$$
 \mathsf C_{\pi,\hbar}^E=\hbar(\mathsf H_\pi^E)^{-1},\qquad
 (\mathsf C_{\pi,\hbar}^E)_{jj}
 \le\frac{\hbar}{m(1-\theta)}\frac{t_j(T-t_j)}{T}
 \le\frac{\hbar T}{4m(1-\theta)}.
 \tag{14}
$$

These are exact Gaussian statements. For a nonlinear action they do not
assert the covariance bound for its full measure without a further
argument. In real time, normalized quadratic Fresnel integration gives
the algebraic centered second moment $i\hbar(\mathsf H_\pi^R)^{-1}$,
which is not a probability covariance.

For one block of Gaussian variables, integration retains both the Schur
complement (13) and a determinant factor: respectively
$(2\pi\hbar)^{|A|/2}(\det\mathsf H_{AA}^E)^{-1/2}$ in Euclidean time
and $(2\pi i\hbar)^{|A|/2}(\det\mathsf H_{AA}^R)^{-1/2}$ when the
real Hessian is positive. Determinants, normalization and any higher
interactions must accompany the stationary action. These are the extra
data that Balaban's effective-density viewpoint instructs us to retain.

Equations (11)--(14) identify the connection to ODE control: the curvature
constant that makes the background construction stable also controls the
Gaussian fluctuations for every positive supplied $\hbar$. They do not
create the multiplier $\hbar$ in (14).

## 5. Written controls: Galileo and the oscillator

**Constant force.** For $V(q)=-Fq$, $\Lambda=0$. Equation (7) is exactly

$$q(t)=\ell(t)+\frac{F}{2m}t(t-T).\tag{15}$$

By (4), every polygon has these same vertex positions. The fluctuation
Hessian is the free one for either action sign, and the Euclidean covariance is
$(\hbar/m)G(t_i,t_j)$. For a single inserted midpoint of a cell of length
$T$, its variance is $\hbar T/(4m)$; for an unequal cut at $u$ it is
$\hbar u(T-u)/(mT)$. The deterministic vertex survives at $\hbar=0$;
the Gaussian width tends to zero. This uses precisely the Galileo
comparison already normalized in the refinement note.

**One arbitrary cut (Terra's connection).** Split $T=u+v$ and let
$H_u$ be the piecewise-linear hat of height one at $u$, zero at the
cell endpoints. Then

$$
 \int_0^T(H_u')^2dt=\frac{T}{uv},\qquad
 a_F=-\frac{Fuv}{2m},\qquad
 \frac m2\int_0^T(a_FH_u')^2dt
       =\frac{F^2uvT}{8m}=K_T-K_u-K_v.
 \tag{15a}
$$

where $K_s=F^2s^3/(24m)$. The free bridge's conditional inserted-vertex
innovation has variance $s_u^2=\hbar uv/(mT)$. For the two equal-variance
Gaussian vertex laws, with means separated by $a_F$, direct integration
of their log-density ratio gives

$$
 D\big(N(a_F,s_u^2)\,\|\,N(0,s_u^2)\big)
       =\frac{a_F^2}{2s_u^2}
       =\frac{K_T-K_u-K_v}{\hbar}.
 \tag{15b}
$$

Here $D$ is relative entropy in nats. Successive bridge innovations
factor into independent Gaussian hat coefficients: conditioned on a
cell's endpoints, its inserted value has the variance above, and the
two residual bridges are independent. The hats are also orthogonal in
the Dirichlet energy because each finer hat has zero derivative integral
inside a cell where an older hat has constant derivative.

Thus classical vertex elimination, conditional Gaussian normalization
and the cut energy are related by one Schur factorization. The
cut-measure note already proves the additive action budget; the useful
connection here is to the blocking variables. Equation (15b) assumes
these Gaussian laws. It does not establish a physical bound on the
information in complete apparatus records.

**Oscillator and caustics.** Let $V=m\omega^2q^2/2$, $\omega>0$.
Its initial-value equation has the unique explicit solution
$q(t)=q(0)\cos\omega t+\dot q(0)\sin\omega t/\omega$ for all times.
Nevertheless its two-endpoint problem loses uniqueness at
$T=\pi/\omega$ when $y=-x$; for other $y$ it has no solution at that time.
A singular boundary Hessian therefore need not mean a failure of
initial-value mechanics.

On a uniform $N$-cell partition, $\tau=T/N$, $N\ge2$, the first
Dirichlet eigenvalue of the difference operator is
$4\tau^{-2}\sin^2(\pi/(2N))$. Its Hessian first becomes singular at

$$
 T_N=\frac{2N}{\omega}\sin\frac{\pi}{2N}
       \longrightarrow\frac\pi\omega.
 \tag{16}
$$

This checks the partition-independent sufficient window
$\omega^2T^2<8$: $T_2=\sqrt8/\omega$, while the continuum caustic is
later. An ODE Lipschitz constant cannot exclude those later caustics.

For an exact Gaussian control, suppose $T<\sqrt8/\omega$ and set
$\alpha=2\arcsin(\omega\tau/2)$. The determinant ratio is

$$
 R_N=\frac{\det\mathsf H_\pi^R}{\det(m\mathsf K_\pi)}
     =\frac{\sin(N\alpha)}{N\sin\alpha}
       \longrightarrow\frac{\sin(\omega T)}{\omega T}.
 \tag{17}
$$

Indeed the determinant of the tridiagonal matrix with diagonal
$2-\omega^2\tau^2=2\cos\alpha$ and off-diagonal $-1$ satisfies
$D_n=2\cos\alpha D_{n-1}-D_{n-2}$, with $D_0=1,D_1=2\cos\alpha$.
Thus $D_{N-1}=\sin(N\alpha)/\sin\alpha$; the free determinant is $N$.
For $N=2$, (17) gives $R_2=1-\omega^2\tau^2/2$, also obtained by
completing the single midpoint square.

With the usual free normalization for each cell, finite Gaussian
integration gives the real-time kernel

$$
 K^\pi_\hbar(y,x)=
 \sqrt{\frac{m}{2\pi i\hbar T}}\,R_N^{-1/2}
           e^{iS_\pi^R(q_\pi)/\hbar}.
 \tag{18}
$$

The prefactor follows from
$\det\mathsf K_\pi=T/\prod_j\tau_j$ and completing the quadratic form.
The determinant identity follows by the same tridiagonal recurrence, or
by successive free one-vertex eliminations. Equation (18) retains the
same $\hbar$ at every depth. Reversing the sign of the oscillator term
would put $1+\omega^2\tau^2/2$ in the two-cell determinant and remove the
real-time conjugate point. This sign test distinguishes the Euclidean
and Newton constructions.

## 6. Large fields, continuation and the next scale question

A local Lipschitz bound controls a local construction. To continue an
initial-value solution, one also needs control preventing escape from
every bounded phase-space region. In the confining example
$V(q)=\lambda q^4/4$, $\lambda>0$, conservation of a fixed classical
energy $E>0$ gives

$$
 |q|\le R_E=(4E/\lambda)^{1/4},\qquad
 |p|\le\sqrt{2mE},\qquad
 |f'|\le\frac{3\lambda R_E^2}{m}.
 \tag{19}
$$

These bounds permit continuation of the initial-value solution. Applying
the local polygon lemma to a whole tube may require a larger radius
than $R_E$ and the invariance condition (9). For the inverted quartic,
$q(t)=q_0/[1-q_0\sqrt{\lambda/(2m)}t]$, $q_0>0$, is instead a
finite-time escape solution. Its force is locally Lipschitz everywhere.
This is an explicit reason to distinguish local control from continuation.
Balaban's large-field estimates address weighted integrals over all
field regions; that is a statistical obligation distinct from trajectory
continuation.

Keeping $\hbar$ explicit in the positive quartic Euclidean action,
set $t=Ts$ and $q=\sqrt{\hbar T/m}\,z$. Then

$$
 \frac{S^E}{\hbar}
 =\int_0^1\left[\frac{(z')^2}{2}+\frac g4z^4\right]ds,
 \qquad g=\frac{\lambda\hbar T^3}{m^2}.
 \tag{20}
$$

For the zero-endpoint free reference, the Brownian-bridge reflection
bound is

$$
 \mathbb P\!\left(\sup|q|>b\sqrt{\hbar T/m}\right)
       \le2e^{-2b^2},\qquad b>0.
 \tag{21}
$$

It follows by applying the positive and negative one-sided reflection
bounds and a union bound; the Rivero note, section 3, supplies the same
calculation. On this small-field tube the real quartic curvature gives
$\theta\le3b^2g/8$. Thus the natural perturbation parameter combines
force curvature, the observation interval and the explicitly supplied
quantum width. For the interacting normalized measure, its denominator
and its own large-field contribution still require control; (21) alone
is not that result.

The next useful test is to retain the normalized fluctuation and
large-field terms through repeated time insertion, and determine which
physical premise would fix their action multiplier independently of the
weight $e^{-S^E/\hbar}$ or $e^{iS^R/\hbar}$. The existing
[quartic zero-limit theorem](rivero-1998-conjecture-central-forces.md)
prevents treating refinement consistency alone as that premise. A loss
of boundary invertibility also needs the oscillator countertest above
before it is used to argue for completion of Newton's dynamics.

A complementary construction suggested by Terra is to control the
initial-value polygon flow and its tangent map under arbitrary insertion.
Their composition is causal and remains meaningful through the oscillator's
boundary caustics. Comparing that description with the endpoint action
would separate loss of one coordinate description from an actual need
for additional physical dynamics.

## Central-force passage under point insertion

In the 1713 *Principia*, Book I, Proposition I, Corollary 4 compares
forces by the inward sagittas of arcs traversed in equal times as the
arcs shrink. In Proposition VI Newton explicitly points to the new
Corollary 4 of Lemma X as another proof of the orbital force rule.
Does this local force information determine where the body emerges
from a small neighbourhood of the centre? Use one spatial position
at a fixed time as the readout. [1687, Book I, Lemma X and
Proposition I](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00077)
and [1713, Book I, Lemma X and Propositions I and VI](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00082)
(diplomatic transcriptions, passages).

**Finite inward force.** Take $m>0$ and
$F(q)=-f(r)q/r$, $r=|q|$, with $f\ge0$, continuous force at zero,
locally Lipschitz away from zero and $|F|\le F_*$. The potential
$V$ has its minimum at the centre. Nonzero angular momentum prevents
arrival there at finite energy. A radial arrival from a point with
$E>V(0)$ crosses with the nonzero velocity fixed by its incoming
direction and energy. The radial travel integral
$\int dr/\sqrt{2(E-V(r))/m}$ fixes its clock on either side.
At the minimum energy a body at rest at the centre stays there by
energy conservation. These statements give uniqueness through the
centre without bounding $f'$. With a globally bounded force, compactness
and uniqueness then give convergence of the usual kick–drift polygons
on each finite time interval, including for changing positive time
partitions. [Classical polygon construction and compactness argument](balaban-ode-lesson.md)
(passage).

The impulse estimate is uniform over these force profiles. Suppose a ray enters
a ball of radius $b$ at speed at least $v_0>0$ and $bF_*/m\le v_0^2/2$.
Attraction gives $|\dot q|\ge v_0$ inside. Hence
$(r^2)''=2|\dot q|^2+2q\cdot F/m\ge v_0^2$. Integrating on each side
of closest approach bounds the time inside by $2\sqrt2\,b/v_0$ and
the change in momentum by $2\sqrt2\,F_*b/v_0$. In particular no
shrinking ball with this fixed force bound can reverse a finite
incoming momentum. This is a classical restriction on trajectories.

**A bounded central force at a turning point.** Fix a ruler distance
$R$, inertial mass $m$ and $A>0$ with units energy/length$^{3/2}$.
In three spatial dimensions take $V_0(r)=-Ar^{3/2}$ up to $2R$. The
force points outward and tends continuously to zero at the origin. For
$r>2R$ continue its magnitude by the inverse square law matched at $2R$.
For each $0<b<R$, keep this exterior potential for $r\ge b$ and use
$V_{b,\pm}(r)=-A b^{3/2}v_\pm(r/b)$ inside, with

$$
 v_+(u)=\tfrac14+\tfrac34u^2,\qquad
 v_-(u)=1-\tfrac32(1-u)+\tfrac38(1-u)^4,\qquad 0\le u\le1.
$$

Both profiles have $v(1)=1$ and $v'(1)=3/2$. Both derivatives
increase from zero, with $v_-'(u)=\tfrac32[1-(1-u)^3]$. Thus every
core has a finite, outward, radially nondecreasing force and a
Lipschitz gradient of the potential. A spherical distribution of like
charges can source each profile because its enclosed charge is
proportional to the nondecreasing function $r^2|F(r)|$.
The maximum force difference is at most $3A\sqrt b/2$ and the maximum
potential difference is $3A b^{3/2}/8$. Each force converges
uniformly to $F_0$, since all three magnitudes inside $b$ are at most
$3A\sqrt b/2$ and they agree outside. At the centre $v_+(0)=1/4$
and $v_-(0)=-1/8$. A diameter orbit of energy zero passes the first
centre and turns before the second. Here zero energy is referred to
$V_0(0)$ in both runs. The incoming state at $q=R e_1$ has the same
inward momentum $p_R=\sqrt{2mA}R^{3/4}$ for every $b$.

Write $p_b=\sqrt{2mA}b^{3/4}$, $t_b=mb/p_b$ and $J_b=bp_b$.
Let $u_+=0$ and let $u_-$ be the simple zero of $v_-$. The time
and ordinary mechanical action between entering the core and leaving
it are respectively

$$
 2t_b\int_{u_\pm}^1\frac{du}{\sqrt{v_\pm(u)}},
 \qquad 2J_b\int_{u_\pm}^1\sqrt{v_\pm(u)}\,du .
$$

At $E=0$, $\int p\cdot dq$ equals the time action. All four integrals
are finite. Inserting intermediate points on the trajectory adds the
corresponding integrals exactly. Halving $b$ scales the time by
$2^{-1/4}$ and the action by $2^{-7/4}$ in either core. The exterior
inward travel time to $b$ is $4(t_R-t_b)$, where $t_R=mR/p_R$.
Thus at the *same clock time* $T=8t_R$ the two positions tend to
$-Re_1$ and $+Re_1$. The trajectories are unique and reversible for
each fixed $b$.

**Point insertion with the source held fixed.** Now use the single
potential $V_0$ throughout. Put $t_*=4t_R$, so $T=2t_*$. Through the
common arrival the signed diameter coordinate is
$x(t)=R(1-t/t_*)^4$. After arrival the two continuations are
$x_\pm(t)=\pm R(t/t_*-1)^4$, with $p=m\dot x$. Both have zero
velocity and acceleration at the join. From rest there, the signed
force estimate $2m x_\pm(t_*+\delta)/\delta^2$ tends to zero on both
branches. Newton's short-time measurement returns the correct force
even where it cannot determine the later side. For any outgoing time cell
their actions coincide since $m\dot x^2/2-V_0(x)$ is the same for
the two signs. On the first duration $\delta$ after arrival it is
the integral of $m\dot x^2$, namely $16mR^2\delta^7/(7t_*^8)$.
The finite-force cusp, its waiting solutions and reversible classical
dynamics on entire histories are established in the
[arrival argument](newton-cusp-preparation-floor.md) (passage).

One can test this on time nodes using only the given force law.
On a cell of duration $\tau$, interpolate $F_0$ at its initial,
midpoint and final positions by a quadratic $B(u)$ in elapsed time.
At $s=\tau/2,\tau$ impose the impulse and displacement balances

$$
 p(s)=p(0)+\int_0^s B(u)\,du,\qquad
 x(s)=x(0)+s p(0)/m+\frac1m\int_0^s(s-u)B(u)\,du .
$$

Start with a partition containing $t_*$. On each branch the force in
time is quadratic on each side of the join, so its interpolant is
exact. Both sets of nodes solve the *same* implicit cell equations on
every subdivision, however fine. Selecting a root would supply a
branch rule. Grant a detector independent position and clock error
bounds $\delta_x\le R/4$ and $\delta_t\le t_R/4$, held fixed as the
mesh and $b$ shrink. Throughout that clock window the limiting distance
is at least $R(15/16)^4>R/2$. The explicit exterior travel time gives
uniform convergence there for the two finite-core returns as well.
Recording the side therefore separates them at these fixed resolutions.
[Lagrange interpolation, DLMF §3.3(i)](https://dlmf.nist.gov/3.3.i)
(passage).

**What the incoming flux sees.** At the incoming sphere
$r=R$ on the same energy shell, write $p_\perp$ for the two tangential
momentum components and $L=R|p_\perp|$. The normalized inward
Liouville flux is uniform on $|p_\perp|<p_R$ for each entry point:
the normal speed cancels the Jacobian of the energy delta function.
A ray reaches $b$ precisely when $L<J_b$, up to tangency. Outside
that disk both motions agree at every time. Consequently even the
joint incoming and outgoing record has total-variation distance
bounded by

$$
  (J_b/J_R)^2=(b/R)^{7/2},\qquad J_R=Rp_R .
$$

A preparation of density at most $C$ relative to that flux has the
same bound times $C$, by coupling the same incoming rays. This
normalizes crossings of a section at fixed energy. The diameter
preparation is singular with respect to flux. At $L=0$, an energy
error smaller than $Ab^{3/2}/8$ still puts the incoming energy
between the two core maxima. Thus
energy resolution and concentration in angular momentum are physical
inputs when asking whether the orbit discrepancy can be observed as
$b$ shrinks. Refinement of a written polygon provides neither.

**The two limits on the same position record.** For a trial reduced
action $a>0$ compare the two Schrödinger Hamiltonians with kinetic
energy $-a^2\Delta/(2m)$ and the displayed potentials. In core units
$z=q/b$, $s=t/t_b$, $\xi=a/J_b$, and
$w(z)=-V_{b,\pm}(b|z|)/(Ab^{3/2})$, the generator in
$i\xi\partial_s$ is $-\xi^2\Delta_z/2-w/2$. The exterior matching
radius $2R/b$ is part of $w$. The real-time kernel acquires a factor
$b^{-3}$, canceled at each inserted position by $d^3q=b^3d^3z$.
The launch coordinate and momentum magnitude become $R/b$ and
$p_R/p_b$. The clock reads $T/t_b$ and the detector tolerances are
$\delta_x/b$ and $\delta_t/t_b$. [Exact propagator dilation, (20)–(22)](groupoid-quantum-newton-states.md#7-interacting-kernels-under-tangent-scaling)
(passage).

The event is $Q_1(T)>0$ in both. The unitary Duhamel estimate bounds
the absolute difference $D(a,b)$ between event probabilities for
*every* common incoming state by

$$
 D(a,b)\le \min\{1,\,3AT b^{3/2}/(8a)\}.
$$

Indeed the norm distance of the two evolved unit vectors bounds
the difference of any event probabilities, with purification covering
mixed inputs. A common clock jitter of size $\delta_t$ replaces $T$
by $T+\delta_t$ in the upper bound. To compare the two orders choose
the same family of incoming Gaussians in both. Each is centered at the
specified incoming state with component standard deviations
$R\sqrt{a/(2J_R)}$ and $p_R\sqrt{a/(2J_R)}$. For each fixed $b$ the
forces are globally Lipschitz. The usual quadratic moment estimate
concentrates this packet on its Newton trajectory as $a\downarrow0$.
In three dimensions the derivative of the summed moment
$\langle|Q-q(t)|^2+|P-p(t)|^2/(m\omega)^2\rangle$ is bounded above by
$(\omega+\operatorname{Lip}(F)/(m\omega))$ times that moment for any
$\omega>0$. Its initial value is $O(a)$. The estimate is only being
used at *fixed* $b$. [Lipschitz packet bounds, §4](lipschitz-certificate-quantum-lift.md)
(passage). For all sufficiently small fixed $b$ the two classical
endpoints stay strictly on opposite sides throughout the detector
window. The same conclusions hold with the stated bounded readout
errors, since the moment bound is uniform on that window. Thus

$$
 \lim_{b\downarrow0}\lim_{a\downarrow0}D(a,b)=1,\qquad
 \lim_{a\downarrow0}\lim_{b\downarrow0}D(a,b)=0 .
$$

Holding $a>0$ fixed is sufficient for stability against the two core
changes. Stability also holds along joint paths with $a\to0$ and
$AT b^{3/2}/a\to0$, and under the classical flux bound above.
No positive lower bound on physical
$\hbar$ follows from either limiting order. Here $a/J_R$ is the
dimensionless trial action, $h_P=2\pi\hbar$ if $a=\hbar$, $b$ is a
source radius, and the time mesh is a separate regulator. Semiclassical
branch selection for rough Hamiltonians has substantial prior art.
[Athanassoulis and Paul](https://arxiv.org/abs/1011.1651) (abstract)
and [cusp-preparation comparison](cusp-quantum-preparation-selection.md)
(passage).

**Newtonian inverse-square attraction.** There is also a finite-angle
test for the actual Kepler force. Give two transparent uniform source
spheres the same total strength $\kappa$ (energy times length) and
radii $b$ and $b/2$.
Their exterior potential is $-\kappa/r$ and the interior force of a
sphere of radius $d$ is $-\kappa q/d^3$. These are Newton's spherical
attraction results. [Motte 1729, Book I, Section XII, Propositions LXXIII–LXXIV](https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_%281729%29/Book_1/Section_12)
(passages). At zero energy and $L=\sqrt{m\kappa b}$ the point-mass
periapsis is $b/2$. Take identical incoming data at a fixed exterior
radius $R>b$. The Kepler parabola has $r=b/(1+\cos\theta)$, so the
narrow source gives an angular advance $\pi$ between the crossings
of $r=b$.

For the wider source use $b$ as length and
$t_K=\sqrt{mb^3/\kappa}$ as time. In the orbital plane the interior
solution from entry is $(\cos s-\sin s,\sin s)$ since the inward and
tangential velocity components have unit magnitude in these units.
It exits at $s=\arctan 2$ at $(-1,2)/\sqrt5$. Thus the two return
angles at $R$ differ by exactly $\arctan 2$, independent of $b$.
The times inside $r=b$ are $(4/3)t_K$ and $(\arctan 2)t_K$ for the
narrow and wide sources. Each inner action is $O(\sqrt{m\kappa b})$.
The angular effect explains which part of an action estimate must
survive point insertion. For either orbit let
$G(E,L)=2\int_{r_{\min}}^R\sqrt{2m(E-V(r))-L^2/r^2}\,dr$.
At a simple turning point the endpoint term vanishes and
$-\partial_L G$ is the unwrapped angle between the two crossings of
$R$ along the orbit. The inner contributions to $G$ shrink as
$O(\sqrt{m\kappa b})$, but their $L$ derivatives differ by
$\arctan 2$ at the specified $L$. [Hamilton, 1834, law of varying action](../docs/classics/Hamilton_GeneralMethodDynamics_1834_Wilkins.md)
(passage).

Here the peak force grows as $b^{-2}$ and the entry speed as
$b^{-1/2}$. The affected disk of incoming flux has fraction $b/R$
for the Kepler exterior. This tests near-radial preparations as the
source shrinks. The [Coulomb propagation estimate](self-sufficiency-contrast.md)
concerns fixed collision-free intervals. Smoothing and the order of
the angular-momentum and source limits have a literature.
[Castelli and Terracini](https://arxiv.org/abs/0905.1579) (abstract;
their positive smoothing result concerns logarithmic singularities).

**Scope of the Bałaban comparison.** Blocking here means eliminating
intermediate times on a one-dimensional chain while retaining the
entrance and exit data. The calculation identifies the set on which
control of the exit fails and its weight under a specified law.
Bałaban's gauge construction retains effective densities after block
integration, with large-field estimates and gauge constraints.
[Bałaban, ICM 1986, pp. 1260–1262](../docs/balaban/Balaban_UltravioletStability_ICM1986_1987.md)
(passage). The positive flux above is an ordinary trajectory
measure. Integration over chiral lattice fermions uses Grassmann
variables, and the phase of the integration measure must be chosen
consistently under gauge transformations. Reflection positivity tests a
form on reflected observables and enters Hilbert-space reconstruction.
These are distinct conditions. [Lüscher, §§3–5](https://arxiv.org/pdf/hep-lat/9904009)
(passage) and [Osterwalder and Seiler](https://doi.org/10.1016/0003-4916(78)90039-8)
(abstract, lattice gauge theory). The committee's 10 November 2026
assessment concerns a pure-gauge Wightman scaling limit. Uniqueness
and a positive physical mass gap remain open there. [Committee assessment
and submission scope](https://github.com/yang-mills-group/YM) (passage).

## A three-energy test of central-force trajectories

Newton's force measurement and an outgoing orbit direction give an
action difference in mechanical units. Consider two equal masses in a
nonrelativistic elastic collision. Write $\mu$ for their reduced mass,
$v$ for their incident relative speed, $E=\mu v^2/2$, and $\kappa>0$
for the coefficient of the repulsive potential $\kappa/r$ (energy times
length). With $d=\kappa/(\mu v^2)$ the Rutherford orbit gives the impact
parameter $b=d\cot(\theta/2)$ for the labelled centre-of-mass deflection
$0<\theta<\pi$. The turning radius is $d+\sqrt{d^2+b^2}\ge 2d$.
Any change of force confined strictly inside $2d$ leaves every such
incoming classical orbit intact. Deflections outside that region,
including atomic screening or multiple collisions, require an
independent error bound. [Rutherford, 1911, §2, pp. 672–674](https://www.physics.utoronto.ca/~phy326/cc/Rutherford1911.pdf)
(passage, applied to relative motion).

If the outgoing particles are unlabelled, the two possible angles are
$\theta$ and $\pi-\theta$. Their relative angular characteristic action,
set to zero at $\pi/2$, has magnitude

$$
 |\Delta W|=\frac{2\kappa}{v}u,\qquad u=|\log\cot(\theta/2)|.
$$

Indeed Hamilton's endpoint variation gives the angular momentum as
the magnitude of the angular derivative. The two alternative derivatives
enter the difference with the same sign and their magnitudes sum to
$\mu v d[\cot(\theta/2)+\tan(\theta/2)]=2\kappa/(v\sin\theta)$.
The difference uses a common large-radius reference, so the common
radial action constant drops out. This supplies a mechanical action
coordinate for the detector, before specifying any rule for phases.
[Hamilton, 1834, law of varying action](../docs/classics/Hamilton_GeneralMethodDynamics_1834_Wilkins.md)
(passage).

**Three settings on one incoming ensemble.** Count each collision once
and accept the full azimuth. With a target at rest the smaller of the
two laboratory fork angles is $\alpha\le\pi/4$ and $u=\log\cot\alpha$.
Choose a dimensionless angular displacement $U$ and a fixed width
$0<w<U$. Choose incident energies so that $d_\pm=d_0 e^{\pm U}$
($E_\pm=E_0e^{\mp U}$). For any reference length $b_{\rm ref}>0$ set
$X=\log(b/b_{\rm ref})$ and $s_j=\log(d_j/b_{\rm ref})$. The classical
observation at setting $j$ is exactly $u_j=|X-s_j|$, including both
possible assignments of the outgoing particles. A head-on collision
lies outside the finite angular windows below.

Let $H_w(y)=(1-|y|/w)_+$ and let $Y_j[h]$ be the sum of the event
weights $h(u)$ divided by the integrated luminosity in that run.
For a thin uniform target the latter is the incident particle count
times its areal number density, so $Y_j$ has units of area. The
incoming impact measure per unit exposure may be
arbitrary, provided it is common across the three settings. Define

$$
 C=Y_+[H_w]+Y_-[H_w]-Y_0[H_w(\,\cdot-U)] .
$$

Then **$C=0$ for Newton trajectories**. For each individual $X$, the
two disjoint triangular windows centered at $s_0\pm U$ sum exactly to
$H_w(|X-s_0|-U)$. Integration proves the identity even for point
masses in the incoming law. The reference length cancels. It is enough
that $(X,\zeta)$ have one joint law when the actual Coulomb length is
$d_je^\zeta$ in run $j$. The same identity then holds pointwise in
$X-\zeta$. Thus even a common fractional energy spread correlated
with impact parameter is allowed. A common error in the absolute
force strength also cancels. Time insertion leaves the continuum
deflection unchanged on these collision-free orbits.

The detector weight is Lipschitz with constant $1/w$. If the measured
$u_j$ differs from the ideal value by at most $e_j$, the classical
residual obeys $|C|\le M(e_++e_-+e_0)/w$. Here $M$ is an upper bound on
the common impact measure of the union of the three preimages, enlarged
by their error margins. A discrepancy $\epsilon_j$ between the actual
and common input measures, measured by the largest absolute difference
on weights between zero and one on that union, adds $\sum_j\epsilon_j$
to the bound. The $\epsilon_j$ and $M$ have units of area. Uncertainties
in efficiency, backgrounds, luminosity and sampling enter in the
units of $C$. A detector distance and pixel width set the angular
error $\delta\alpha$. On an acceptance enlarged to
$\alpha\ge\alpha_{\min}>0$ within the folded half, its contribution to
$e_j$ is at most $2\delta\alpha/\sin(2\alpha_{\min})$. A flight
length $\ell$ and an independent clock interval $t$ give
$s_j=\log(\kappa t^2/(\mu b_{\rm ref}\ell^2))$. Thus calibrated errors
in $\ell,t$ propagate directly to $s_j$. The clock and position
resolutions stay fixed while the mathematical time mesh shrinks.

Run normalization can also be eliminated for the classical test.
At three widths $w_k<U$, let $N_{jk}$ be the background- and
efficiency-corrected weighted counts with the above windows. If only
the three positive run exposures are unknown, the middle-setting row
$(N_{0k})_k$ must be a positive linear combination of the other two
rows with the same coefficients at all widths in the mean. The matrix
of mean counts therefore has determinant zero. This tests relative
angular shapes alone when the aperture response is known.

**How accurately must the force be known?** Write the actual radial
force on a scattering orbit as $\kappa[1+g(r)]/r^2$, positive outwards.
Measure the polar angle $\phi$ from the incoming asymptote and let
$\Phi=\pi-\theta$ at exit. For $b>0$ and a repulsive scattering orbit
with $0<\Phi<\pi$, Binet's equation for $y=1/r$ is
$y''+y=-(d/b^2)[1+g(r)]$, with $y(0)=0$, $y'(0)=1/b$. At the exit
$y(\Phi)=0$. The sine Green function gives

$$
 \frac{b}{d}\tan(\theta/2)=1+\bar g,\qquad
 \bar g=\frac{\int_0^\Phi\sin(\Phi-\phi)\,g(r(\phi))\,d\phi}
                    {1-\cos\Phi}.
$$

This is a positive weighted average of the actual force error along
the orbit. It requires no bound on a force gradient. An independent
bound $|\bar g|\le\gamma<1$ adds at most $-\log(1-\gamma)$ to the
error $e_j$ above. A bound on $|g|$ from short-time force measurements
on the traversed annulus suffices if the tails are also controlled.
An outer portion of total polar angle $h$ with $|g|\le D$ contributes
at most $Dh/(1-\cos\Phi)$ to the average. This allows a screened tail
to be treated separately. [Binet's equation, *Motion in a central
potential*, §2](https://teorica.fis.ucm.es/artemio/Notas%20de%20curso/CM.pdf)
(passage).

There is a direct threshold for an ideal counter accepting $0\le u\le w$
with full azimuth, uniform incident fluence and one fixed speed. For any
ray it accepts, the force-error identity confines $b$ to
$[d(1-\gamma)e^{-w},d(1+\gamma)e^w]$. Dividing the area of this annulus
by the unperturbed aperture cross section gives

$$
 \frac{Y_{\rm actual}}{Y_{\rm Coulomb}}
 \le 1+\gamma^2+2\gamma\coth(2w).
$$

For a twofold excess one therefore needs
$\gamma\ge 1/(\sqrt{1+\coth^2(2w)}+\coth(2w))$. For $w=\log\cot40^\circ$
this is about $0.16$. The statement is independent of a phase law and
of the mathematical time partition. It bounds the largest orbit-averaged
force error on accepted rays if force alone is to account for
the ideal counter's excess. A real counter needs its measured angular
response in place of the ideal window.

**What an excess measures.** Take the established plane-wave Mott
cross section for identical spin-zero particles with uniform incident
fluence and only elastic Coulomb scattering. A finite beam requires
calibration of the incident directions, coherence and detector response
for this law to apply. In terms of a trial reduced action
$a>0$ and $\eta_j=\kappa/(a v_j)$, its full-azimuth cross section on
the folded half-sphere is

$$
 dY_j=4\pi d_j^2
       [\cosh(2u)+\cos(2\eta_j u)]\,du,\qquad u\ge0 .
$$

The first term is the sum of the two classical contributions. The
second is the exchange term, with argument $|\Delta W|/a$.
[Mott, 1930](https://doi.org/10.1098/rspa.1930.0006) (article metadata)
and [Canto, Hussein and Mittig, §III, Eqs. (9)–(10)](https://arxiv.org/html/1402.1858#S3)
(formula passages). At a *single* energy the bounded nonnegative
relative classical illumination

$$
 1+\frac{\cos(k\log(b/d))}{\cosh(2\log(b/d))}
$$

multiplies both branches by the same factor. Choosing the dimensionless
frequency $k=2\eta_j$ reproduces the entire angular distribution.
Independence of the target positions can exclude such a reweighting
physically. For example, translate one collision partner independently
and uniformly over a transverse area $A$. Conditional on an arbitrary
other impact point, the probability for the relative offset to lie in
a set $B$ is $|B|/|A|$ whenever its translated preimage is contained
in $A$. This guard condition suffices for the finite accepted annuli.
A homogeneous gas independent of the incident beam gives the same
area weighting in the thin-target approximation. The three-energy
identity also covers a common nonuniform illumination.

With $S_j=\sin(\eta_j w)/(\eta_j w)$, integration against the three
specified triangular weights gives

$$
 C_a=2\pi w\big[d_+^2 S_+^2+d_-^2 S_-^2
                 -2d_0^2 S_0^2\cos(2\eta_0 U)\big] .
$$

The half-window cosine integral at the origin is $w S_j^2/2$ and
the full translated one is $w S_0^2\cos(2\eta_0 U)$. Retaining a
finite $w$ is essential. If $|C_{\rm obs}|-\rho=C_{\rm low}>0$,
where $\rho$ bounds all errors relative to this ideal prediction at
the asserted confidence level, $|\sin|\le1$ gives the model bound

$$
 a\ \ge\ \kappa\sqrt{\frac{w C_{\rm low}}
 {2\pi(d_+^2v_+^2+d_-^2v_-^2+2d_0^2v_0^2)}} .
$$

For a common incoherent mixture of relative speeds as above, average
each $d_j^2v_j^2$ over the measured spread, assuming these moments
are finite and the uniform-fluence law applies at each speed. The
angular settings and the energy preparation in this bound are fixed
independently of $a$. With $U=\log4$ and monochromatic runs, for
example, $a_1=\kappa w/(\pi v_0)$ gives
$C_{a_1}=w d_0^2/(2\pi)$, whereas $a_1/2$ gives zero. Moreover $a_1/2$
and $a_1/4$ give exactly the same three weighted yields as the
classical uniform beam, since all three sine factors vanish for both.
These examples distinguish rejection of the classical prediction from
unique identification of a positive action.

The separation of $a_1$ from $a_1/2$ survives a finite incoming
speed band with the same detector. Let the actual speeds be $\lambda v_j$
with a common distribution of $|\lambda-1|\le\delta_v=1/100$. For an integer
$n>0$, $|\sin(n\pi/\lambda)/(n\pi/\lambda)|\le\delta_v$, while
$\sin(\pi/(2\lambda))/(\pi/(2\lambda))>1/2$ throughout this band. At $a_1$ the
minus-setting factor therefore exceeds $1/2$ and the middle one is
at most $\delta_v$ in magnitude. At $a_1/2$ all three are at most $\delta_v$.
Since the squared length ratios are $16,1,1/16$ and each $d_j^2$
acquires the same factor $\lambda^{-4}$, the difference of the two mean
contrasts is at least
$2\pi w d_0^2(1/64-21\delta_v^2)/(1+\delta_v)^4>0$. This leaves a positive
allowance for calibration error at fixed clock and angular resolution.
The exact equality of the other pair above was for monochromatic runs.

**What was actually measured.** Chadwick used a helium gas target,
graphite diaphragms admitting laboratory angles from $40$ to $50$
degrees, and argon runs at matched stopping power. He reported an
observed-to-classical ratio near two at the lowest speeds. The argon
standard assumes Coulomb scattering, and the different particle
energies at the screen could reduce helium counting efficiency in
the two slowest runs. This is evidence for a finite-aperture excess
independent of fitting a Mott amplitude.
For any *fixed* integrable angular response, its exchange contribution
vanishes as $a\downarrow0$ by the Riemann–Lebesgue lemma, also after
averaging a fixed speed distribution with integrable scattering weight.
Thus an independently calibrated excess in that aperture already excludes
the zero limit within the Mott family. Chadwick's apparatus had its own
angular response. [Chadwick, 1930, pp. 116–121](https://doi.org/10.1098/rspa.1930.0098)
([volume scan](https://archive.org/details/dli.ernet.27026), passages
read in the library OCR) and [Riemann–Lebesgue lemma, Theorem 2.13](https://www.iitg.ac.in/rksri/MA746%20Fourier%20Analysis%20Lecture%20notes%202025.pdf)
(statement).

Blackett and Champion recorded both outgoing arms for 428 forks among
56,820 photographed tracks. Their range and angle cuts and their
geometrical identification of helium events can be checked against the
cloud-chamber preparation. They report a discrepancy statistic of 15.3
for the classical and 1.04 for the Mott expectations in the upper six
cells. Their cell boundaries used the Mott phase, and they report
missed short spurs in the lower cells. Heydenburg and Temmer later
measured precise relative angular distributions below 400 keV. Their
absolute normalization below 2 MeV used a fitted scattering phase
shift. None of these published summaries gives the three matched
weighted yields or their calibration errors. A numerical value of
$C_{\rm low}$ for this test remains open.
[Blackett and Champion, 1931, pp. 382–388](https://doi.org/10.1098/rspa.1931.0011)
([volume scan](https://archive.org/details/dli.ernet.7436), passages
read in the library OCR) and [Heydenburg and Temmer, 1956](https://journals.aps.org/pr/abstract/10.1103/PhysRev.104.123)
(abstract).

## Locating a turn with two barrier powers

**6.1 Sol Max, 2026-11-18.** Eid et al. counted potassium atoms on
either side of a repulsive optical barrier. Among the plotted points,
more than 36% were on the reflected side near one-quarter laser power,
and more than 35% were transmitted near three-quarters power. In a
static one-dimensional Newtonian field, the atoms that cross at the
higher power set an upper bound on the work required everywhere they
pass. This limits the fraction that could have reversed in the same
region at lower power. It uses the power ratio and allows an unknown
barrier height, arbitrary optical sidelobes and a non-Gaussian launch.
Newton's 1713 Lemma X, Corollary 4, compares forces by nascent
displacements from rest in equal times. Here that comparison can
calibrate how much changing the illumination changes the force on
each part of the incident beam. The scattering and the camera counts
are a modern application. [Newton, 1713, Book I, Lemma X and
corollaries](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00082#par26)
(diplomatic transcription, passage).

**What was measured.** The same three-pixel mask was used throughout
this power scan. The central incident speed was about $3.7$ mm/s,
set by release distance in a guide of acceleration $g=0.20$ m/s$^2$.
The source reports a cold launch spread near $0.35$ mm/s, an estimated
rms size $3.5\,\mu{\rm m}$, and a thermal fraction near 20%. Read
the centres of the experimental circles in Fig. 3 in the following
rounded intervals. The inequalities leave room for reading the plot.
They carry no statistical confidence level.

| Fraction of full power | Recorded fraction used |
|---|---|
| $0.240$–$0.255$ | reflected side $>0.36$ |
| $0.745$–$0.760$ | transmitted side $>0.35$ |
| $0.895$–$0.910$ | transmitted side $>0.27$ |

The measured quantity is the atom number on each side when the two
clouds are separated. The authors point out that atoms still approaching
the barrier can enter the reflected count. Their thin-barrier fit and
their determination of the optical response from scattering are separate
from the plotted data used here. [Eid et al., Figs. 1–4](https://arxiv.org/html/2405.14466v1#S0.F3)
(apparatus passages and plotted data; [reading coverage](../docs/EidEtAl_OpticalBarriers_2024.md)).

**What a crossing bounds.** Set $z=0$ at the central light maximum.
In the guide use the potential $mg[P u(z)-z]$ at relative power $P$,
with $u\ge0$ measured in units of length relative to the dark guide.
The mass $m$ cancels from the trajectory test. Let the initial position
be $-d-X$, with $\mathbb E X=0$, $\mathbb E X^2\le s^2$ in the cold
part of the incident beam. Write

$$
 w=\frac{\mathbb E v_0^2}{2g},\qquad
 u_{\rm in}=\mathbb E[P_H u(-d-X)],\qquad
 c(p)=\sqrt{(1-p)/p}.
$$

The two mean energies per $mg$ are bounded at release, before selection
by either detector. They have dimensions of length. The static force
profile is common to both powers. Energy exchange with other atoms,
transverse motion and changes of internal state require independent
control for the axial law to apply.

Choose a left plane $-b$ and a right plane $L>-b$. If a fraction
$p$ or more of the cold atoms crosses the whole interval at high
power, every point in it satisfies

$$
 P_Hu(z)-z \ \le\ H=d+s\,c(p)+(w+u_{\rm in})/p .
$$

Indeed the incident specific energy in these units is
$d+X+v_0^2/(2g)+P_Hu(-d-X)$. It bounds the potential at each
crossed point. Conditional on a crossing, the mean of $X$ is at most
$s\,c(p)$ by Cauchy–Schwarz applied to the centred event indicator.
The two nonnegative terms contribute at most their total mean divided
by $p$. No independence of initial position and velocity is needed.

At low power the potential at the same points obeys

$$
 P_Lu(z)-z\ \le\ B=b+(H-b)/r,\qquad r=P_H/P_L>1 .
$$

At a longitudinal turn the kinetic energy vanishes. Since the
low-power launch energy is at least $d+X$, a turn in $[-b,L]$
requires $X\le B-d$. For $B<d$, the one-sided variance inequality
gives the cold fraction of such turns at most

$$
 q_{\rm turn}=\frac{s^2}{s^2+(d-B)^2}.
$$

The same moment inequality gives $\rho_b=s^2/[s^2+(d-b)^2]$ as an
upper bound on the fraction starting at or beyond $-b$ when $d>b$.
[Cantelli's inequality, Pinelis, Eq. (2)](https://arxiv.org/pdf/1011.6065#page=1)
(statement for a finite second moment).

**Size of the discrepancy.** Take $b=10\,\mu{\rm m}$ and count a
high-power transmission only beyond $L$. For illustration take the
reported preparation values as bounds, zero incident mean velocity
and negligible optical energy at release. They give
$d\simeq v_{\rm inc}^2/(2g)=34.2\,\mu{\rm m}$, $s=3.5\,\mu{\rm m}$,
$w<0.307\,\mu{\rm m}$ and $\rho_b<0.021$. Assign every member of a
20% thermal fraction the outcome most favourable to a classical fit
at each setting. At the first high power the cold crossing probability
is at least $(0.35-0.20)/0.80-\rho_b>0.16$. With $r\ge2.9$, one gets
$H<44.2\,\mu{\rm m}$, $B<21.8\,\mu{\rm m}$ and $q_{\rm turn}<0.075$.
Even counting every thermal atom, **less than 26%** of the incident
beam can turn in the interval. At least ten percentage points of the
reported reflected fraction would have to turn elsewhere, reach the
apparatus late, or be explained by changes in the source, forces or
counting. These fractions use a common incident denominator. Loss and
normalization errors must be carried into them.

The second high-power point checks the comparison away from the
largest plotted transmission in that part of the scan. Here $p>0.065$
and $r\ge3.5$, giving $H<52.3\,\mu{\rm m}$, $B<22.1\,\mu{\rm m}$
and $q_{\rm turn}<0.079$. Nor must the light vanish exactly at
release. For every one of the reported 36% to be a local return in
the first comparison, at least $q=0.20$ of the cold atoms must turn,
so $B\ge d-s c(q)=27.2\,\mu{\rm m}$. With the same bounds this
would require $u_{\rm in}>2.5\,\mu{\rm m}$. The optical work from
a dark reference to the launch cloud is measurable by integrating
the change in acceleration with position. The change can be measured
with the clocked displacements of [Lemma X](newton-insertion-action.md#lemma-x-and-the-measurement-of-initial-force).
Alternatively, at negligible launch light allow extra longitudinal
work up to $mg h_H$ gained at high power and $mg h_L$ lost at low
power along the relevant paths. These changes raise the allowed
low-power turning threshold by $h_H/r+h_L$. Accounting for all
36% as local returns then requires $h_H/r+h_L>5.4\,\mu{\rm m}$,
by $27.2-21.8$. This is a mechanical work tolerance for transverse
exchange, time-dependent fields or residual interatomic forces.

**A position measurement that locates the reversal.** On independently
chosen releases at *the same low power*, image the fraction $C_1$ to
the right of $-b$ at time $t_1$ and the fraction $C_2$ to its left
at $t_2>t_1$. A common trajectory ensemble puts at least
$C_1+C_2-1$ in both events. Each such atom starting left of $-b$
must have turned on its right. Let $e_L$ bound the fraction of all
launches that are cold, start left of $-b$, pass $L$ and return
behind $-b$ by $t_2$. For example, if the axial
acceleration stays positive beyond $L$ up to the furthest accessible
position, then $e_L=0$. For the first high-power setting the null
prediction, with the numerical bounds above, is

$$
 C_1+C_2-1\ \le\ 0.20+0.80(\rho_b+q_{\rm turn})+e_L
                \ <\ 0.277+e_L .
$$

If the late image confirms $C_2\ge0.36$ behind the specified plane,
an early fraction $C_1>0.917+e_L$ would cross this ceiling before
other errors. Finite imaging resolution works with two separated
position windows: count early images securely right of the plane and
late images securely left. Similarly score high images only beyond
the right guard. Any remaining leakage, loss or sampling error needs
a bound on incident counts. Independent finite shutter windows suffice
when the whole early window precedes the late one and the downstream
return allowance uses the latest late time. There is a single terminal
exposure per atom. Fig. 3 supplies neither this early occupancy nor
the guarded late fractions with their errors.

The downstream return allowance can itself be set by the clock and
ruler. Write $S$ for the actual low-power launch energy per $mg$.
Except for a cold fraction at most $\delta$, the conditional-mean
bound gives

$$
 S\le S_c=d+s c(\delta)+(w+u_{\rm in}/r)/\delta .
$$

Nonnegativity of the optical potential gives
$|\dot z|\le\sqrt{2g(z+S)}$. A trajectory that starts and ends left
of $-b$ and visits $L$ must cover the interval twice. Integrating the
inverse maximum speed, its elapsed time is at least
$2\sqrt{2/g}\,(\sqrt{L+S_c}-\sqrt{S_c-b})$ when $S_c>b$.
This remains true for radial speed in the shell below. Consequently
the latest late time $t_2$ guarantees $e_L\le\delta$ for the cold
trajectories initially left of the plane if

$$
 L>-b+t_2\sqrt{g(S_c-b)/2}+g t_2^2/8.
$$

For example, the nominal source with negligible launch light gives
$S_c<100\,\mu{\rm m}$ at $\delta=0.01$. A right plane at
$L=110\,\mu{\rm m}$ then suffices for $t_2\le30$ ms. One concrete
choice is a calibrated $1\,\mu{\rm m}$ spatial guard on each scored
side and terminal exposure windows of 18–19 and 29–30 ms at low
power, and 49–50 ms at high power. The high-power count must be
measured beyond this particular $L$. With the same lower fractions
$0.35$ and $0.36$ there and in the late left window, respectively,
$C_1>0.927$ would suffice before the remaining calibration and
statistical allowances. The times, guards and fraction specify a
proposed test. The published figures give no such timed triple.

**Checking the launch with two blank images.** The thermal assignment
and both fitted widths can be dropped in the axial guide. Choose the
power independently at release. On blank runs with the same preparation,
leave only the measured uniform acceleration on. At an early time
$t_a$ and a later time $t_b$, use separate terminal images to score
$Y(t)=z(t)+d-gt^2/2$. Ordinary trajectories give
$Y(t)=-X+v_0t$. This allows a test using only bounded position counts.

Use windows of 0–0.1 ms and 40.1–40.2 ms, respectively, with
calibrated time stamps or an allowance for the variation of $gt^2/2$
within a shutter. Let $e_a$ bound the fraction outside
$|Y(t_a)|\le8\,\mu{\rm m}$. Let $e_n,e_w$ bound the fractions
outside $|Y(t_b)|\le37$ and $192\,\mu{\rm m}$ in the *same* later
image. A fixed spatial guard and measured leakage can be included in
each of these bounds. Assume the high-power optical work at launch
is at most $mg$ times $1\,\mu{\rm m}$ for $|X|\le8.5\,\mu{\rm m}$.

* If the high-power fraction observed past $110\,\mu{\rm m}$ exceeds
  $e_a+e_n$, some transmitted trajectories also satisfy both narrow
  blank windows under the classical common-release hypothesis. This
  is a union bound across settings. On that overlap,
  $|v_0|\le(8+37)\,\mu{\rm m}/(40\,{\rm ms})=1.125$ mm/s and
  $|X|\le8.113\,\mu{\rm m}$. They start left of $-b$ and cross the
  whole interval. Substituting the upper launch energy gives
  $H<46.5\,\mu{\rm m}$ and $B<22.6\,\mu{\rm m}$ at $r\ge2.9$.
  The existence of even one such path bounds the common barrier.
* Outside a total fraction at most $e_a+e_w$, the wider windows give
  $|v_0|\le5$ mm/s and $|X|\le8.5\,\mu{\rm m}$. These low-power
  atoms have energy per $mg$ at least $25.7\,\mu{\rm m}$, too high
  to turn in the interval, and at most
  $34.2+8.5+62.5+1/2.9<106\,\mu{\rm m}$. The return-time bound
  therefore prevents them from passing $110\,\mu{\rm m}$ and
  returning behind $-10\,\mu{\rm m}$ by 30 ms.

Consequently the four independently timed exposures (two blank and
two low-power), together with the high-power terminal count, test

$$
 T_H>e_a+e_n
 \quad\Longrightarrow\quad C_1+C_2-1\le e_a+e_w .
$$

For example, upper tail fractions $0.17,0.17,0.02$, high transmission
above $0.35$ and late low-power occupancy at least $0.36$ would
make an early occupancy above $0.83$ decisive, with the inequalities
applied to simultaneous error bounds. This score requires no
measurement of position and velocity together. It uses the same
release, dark-guide acceleration, static scalar optical work and
calibrated image windows in every setting. The blank guide must be
ballistic to the stated accuracy. These blank and intermediate
counts are experimental inputs, not values inferred from Fig. 3.

**An explicit classical alternative to a common axial force.** Let
four transverse strips have incident fractions $0.38,0.25,0.09,0.28$.
In each strip take a smooth nonnegative axial light profile supported
in $|z|\le1\,\mu{\rm m}$ with its maximum at zero. Give the maxima
at low power the respective heights $70,20,10.5,5\,\mu{\rm m}$ in units
of $mg$. A single smooth optical intensity can have these four
plateaux across the beam, joined between the populated strips. Atoms
at rest transversely on a plateau feel only its axial force.

Make the third strip cold, with $X=0$. Split the remaining $0.91$
of the beam into $0.71$ cold and $0.20$ thermal. Take
$X=\pm3.5\sqrt{0.80/0.71}\,\mu{\rm m}$ on these other cold rays
and $X=\pm3.5\,\mu{\rm m}$ on the thermal rays, with equal signs.
The cold source has the specified rms size. Give the cold and thermal
atoms launch velocities $\pm0.35$ and $\pm2.6$ mm/s respectively,
with both signs equiprobable. All energies per $mg$ lie between 30
and $55\,\mu{\rm m}$. In the third strip the energy is about
$34.5\,\mu{\rm m}$. At powers $1,3,3.6$ times the low setting,
that strip passes, passes and reflects: its tilted peak is at most
$32.5\,\mu{\rm m}$ at the middle power and at least $37.8\,\mu{\rm m}$
at the highest. Only the strongest strip reflects at low power,
and only the weakest transmits at the highest power. A sufficiently
late side image gives $0.38$ reflected, $0.37$ transmitted and
$0.28$ transmitted at the respective settings. This fits all three
rounded readings and the launch spreads with ordinary trajectories.
Testing it requires
the axial work across the *occupied* transverse beam. For fixed strip
gains ranging by a factor $\kappa<r$, the calculation still holds with
$r/\kappa$ in place of $r$. At negligible launch light, fitting 36%
true local returns would require $\kappa\ge r(27.2-10)/(44.2-10)>1.45$
in this class. The remaining points of the power scan were not used
to choose the strips.

**Central motion and the action limit.** There is an exact central
version. Put the same potential on a shell with $z=R-R_B$, where $R$
is the radius, and launch inside the shell at $R_0>0$. For angular
momentum $J$, include the initial transverse energy
$J^2/(2mR_0^2)$ in $mgw$ when averaging over the source. The
centrifugal energy at each high-power crossing is nonnegative. At a
low-power radial turn outside $R_0$ it is at most its launch value.
Thus $P_Lu(z)-z\ge d+X$ there, and the moment and return-time
bounds apply to arbitrary admitted angular momenta. A launch to the
left of $-b$ ensures the required radial ordering for a return in
the interval. The two blank images give the stated ballistic bounds
on a radial ray with $J=0$. For $J\ne0$ the blank radial acceleration
also contains $J^2/(m^2R^3)$. If bounded by $c_*$, this adds at most
$c_*t^2/2$ to a blank displacement and must be allowed along with
the initial transverse energy. The potassium experiment implements an
axial guide. A shell with measured total launch kinetic energy would
test central orbits themselves.

For fixed smooth scalar forces, a strict excess in the guarded
finite-time observations would also exclude a sequence of canonical
reduced actions $a\downarrow0$. Keep the shell (smoothly extended
away from the admitted region), source bounds, power settings and
position responses fixed in physical units. Use normalized initial
density matrices, tight in position and momentum with the stated
second-moment bounds. Use a common low-power preparation at the two
times and, when using the blank-image test, the same release state
before the independent choice of field. Use bounded continuous
position scores supported on their assigned sides. For smooth
potentials with bounded derivatives of
order two and higher on finite time intervals, subsequential Wigner
measures are positive, have full mass by tightness, and propagate by
the classical Hamiltonian flow. Their moments obey the bounds by
truncation. They would reproduce those scores and violate the trajectory
inequality. This uses semiclassical transport for fixed potentials.
[Lions and Paul](https://doi.org/10.4171/RMI/143) (abstract, Wigner
measures and Liouville transport). If a reconstructed force profile
can itself develop structure on a length that vanishes with $a$, this
argument requires independent control of its derivatives.

The dimensional inputs are inertial mass if energies or action are
quoted, the driving acceleration, launch displacement and velocity
moments, work at release, the two plane positions, clock times and
gate widths, and the spatial response of the images. The experiment
uses 532 nm light and a projected pixel pitch of $0.196\,\mu{\rm m}$.
The shell also specifies $R_B$ and the source radii and angular momenta
if their energy contribution is measured separately.
Only the *ratio* of optical powers enters the bound. For example,
$t_*=\sqrt{d/g}$, $S_*=md^2/t_*$ express a trial action by $a/S_*$.
Neither the camera scale nor the clock follows this dilation. Refining
the mathematical orbit between the images leaves all these inputs fixed.

## Two images of a returning orbit

**6.1 Sol Max, 2026-11-18.** An atom seen far beyond a barrier in the
late image had to be inside a specified central interval in the early
image, under the clock conditions below. Counting this interval
on fresh releases gives a ceiling on the late population. The proof
allows an arbitrary static barrier, an arbitrarily slow first crossing,
and a different fixed barrier height for every ray. It uses the force
only on the two exterior excursions. Newton's 1713 Lemma X,
Corollary 4, suggests an independent way to check those exterior forces
by releasing test bodies from rest at known positions and comparing
their initial displacements. The return inequality is a modern
consequence of reversible radial motion. [Lemma X and its editions](newton-insertion-action.md#lemma-x-and-the-measurement-of-initial-force)
(historical passages).

**Why use the same barrier?** In the potassium experiment, at
$3.3$ mm/s and 75% power one two-pixel barrier transmitted about 70%.
At larger spacings two transmitted about 50%. The red data point near
$3.3\,\mu{\rm m}$ separation is close to 11%. In an ideal guide with
downhill acceleration $g$, the effective potential on an identical,
disjoint downstream copy at the same offset is lower by $mgD$ for
centre spacing $D$. Every particle that passes the first must eventually
pass the copy, for any static gain it retains across both. The paper
reports that the two optical fields interfere. Its fit changes the
barrier heights with spacing, and the recorded counts are at finite
times. Neither the size of that change on each occupied ray nor a
common deadline for passage can be read from the single-barrier
fraction. [Eid et al., Fig. 5](https://arxiv.org/html/2405.14466v1#S0.F5)
(experimental points and discussion).

**The two counts.** Take a static scalar potential with unique
one-dimensional Hamiltonian motion on the admitted orbits. Let the
central interval be $[-b,b]$. Every good release starts at $x\le -A$,
where $A>b$, and first arrives at $-b$ between $\ell$ and $u$ on the
outward journey. Score the far side at $x\ge C>b$. For orbits reaching
$C$, suppose that an excursion from $b$ back to $b$ spends between
$r_-$ and $r_+$ on the right. An excursion from $-b$ back to $-b$
on the left spends at least $l_-$. A particle that escapes forever on
the left also obeys this lower bound. Let $e$ bound the fraction
outside the assumptions. Choose two terminal exposure times satisfying

$$
 u<t_1<\ell+r_- ,\qquad
 t_1+r_+<t_2<\ell+r_-+l_- .
$$

Then for any common release law,

$$
 \Pr\{x(t_2)\ge C\}\ \le\ \Pr\{|x(t_1)|\le b\}+e .
$$

To see the inclusion for one good ray, suppose it is far right at
$t_2$. After its first entrance at $-b$, an unsuccessful approach
to the barrier that sends it back past $-b$ fixes an inner turning
point for every later attempt on that energy orbit. A successful
approach cannot return to the left exterior by $t_1$, since it must
first spend at least $r_-$ on the right. Thus it cannot be in the
left exterior at $t_1$. If it is already in the right exterior at
$t_1$, that excursion ends by $t_1+r_+$. Before its next visit to the
right it must cross back along the accessible interval and make the
left excursion that reaches its original release radius. Its earliest
second visit is at or after $\ell+r_-+l_-$. All its right excursions
have the same turning point and duration. The late shutter falls
between visits. This excludes the right exterior at $t_1$ as well.
The textbook ingredients are conservation of energy and retracing of
one-dimensional orbits between turning points. [MIT, *Classical
Mechanics*, chapter 14](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter14.pdf)
(passage on energy diagrams).

**Rulers and clocks.** For harmonic exteriors of frequency
$\nu=\omega/(2\pi)$ about $x=0$, the standard oscillator law gives
the time outside a gate at distance $b$ on an excursion of amplitude
$M$ as $2\arccos(b/M)/\omega$. Use $M\ge C$ on the right and
$M\ge A$ on the left. [MIT, chapter 23, §23.2](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter23.pdf)
(oscillator solution).

One possible calibration takes
$b=15$, $C=50$, $A=60$ in micrometres, and
$1.39\le\nu\le1.41$ Hz. Then $r_+<360$ ms, $r_->285$ ms and
$l_->297$ ms, where the lower and upper bounds are obtained at the
corresponding frequency endpoints. With first arrivals between
$145$ and $200$ ms, the full early window $285$–$305$ ms and late
window $700$–$720$ ms satisfy both strict clock inequalities.
For instance the latest end of the first right excursion for a ray
already on the right in the early image is before $665$ ms. Its next
visit cannot start before $727$ ms. The exterior timing tolerances
must include any optical tails, displacement of the trap centre or
departure from harmonic motion.

The arrival allowance can itself be measured. Use one release image
for the fraction initially right of $-A$. Leave the interior barrier
off on two further releases in the same harmonic trap. Score the
fraction already past $-b$ at $145$–$150$ ms and the fraction still
behind $-b$ at $195$–$200$ ms. Starting left of $-b$, a particle in
the blank trap spends more than half a period to the right of that
negative gate after crossing it. Neither exposure can confuse first
arrival with return. Up to the first entrance the blank and test
orbits agree. The sum of these three fractions bounds all release
and arrival exceptions, with no fitted velocity distribution.
Any failure of the common static orbit or exterior timing inputs needs
its own allowance.

All probabilities refer to the same weighting of releases and particles.
For a camera with calibrated spatial error at most $d$ except for
probability $\eta$ per exposure, score the late image beyond $C+d$,
the early image inside $[-b-d,b+d]$, and enlarge each of the three
blank or release exception regions by $d$. Add $5\eta$ if the same
error bound applies to all five images. For smooth scores, use
minorants for the late count and majorants for the early central
count and the three exceptions, allowing room for the camera response.
Count missing particles against the bound or normalize to the measured
release. No particle is measured at both times.

**What finite force alone permits.** Let $H$ be the largest value
of the static potential in $[-b,b]$. A finite continuous force can
give a nonunique orbit at $E=H$. The [central cusp construction](#central-force-passage-under-point-insertion)
allows an arrival at rest to pass on the first visit and reflect on
the second, with the same conserved energy at every insertion.
For an example on these clocks, release at rest at $x=-M$ with
$M=75\,\mu{\rm m}$ in the $1.4$ Hz trap. Set $H=m\omega^2 M^2/2$.
On $|x|<d_c=0.10\,\mu{\rm m}$ prescribe the potential by

$$
 H-V(x)=\tfrac12 m\omega^2(M^2-x^2)\chi(|x|/d_c)^2,\qquad
 \chi(s)=s^{3/4}(7-3s)/4 .
$$

Join to the harmonic potential at $d_c$. The force matches there
since $\chi(1)=1$ and $\chi'(1)=0$. At zero the crest is proportional
to $-|x|^{3/2}$ relative to $H$, with finite continuous force. Each
half traversal of the modified interval adds less than $0.46$ ms
to its oscillator time, since $s^{3/4}\le\chi(s)\le1$ and
$\int_0^1(s^{-3/4}-1)\,ds=3$. The delay per half traversal is at
most $3d_c/(\omega\sqrt{M^2-d_c^2})$. The first entry at $-b$ is
at about $156$ ms. On either choice of side the absolute position
exceeds $50\,\mu{\rm m}$ throughout both shutters, by the oscillator
law with less than $1.84$ ms total delay through two encounters.
Let two fifths of the rays pass and then reflect back to the right,
one tenth pass both times, and one half reflect both times on the
left. This gives zero early central
occupancy, one half initially transmitted, and two fifths late far
right. The exterior force can be smoothly capped outside the visited
radii. This counterexample tests the finite-force premise at one
energy. Applying it to real atoms would require both the cusp and a
launch concentrated at its precise maximum.

**Four launch energies control the exception.** Choose one of $K$
settings with equal probability, independently of the fixed potential
sampled by the ray. Let the initial axial energy lie in a measured
interval $I_j$ for that setting. Allow an axial energy change of at
most $W$ in either direction at *every* time through readout, including
both encounters. Enlarge each $I_j$ by $W$ on both sides and keep
the enlarged intervals disjoint. For any fixed potential maximum
$H$, at most one setting's enlarged interval contains $H$. Below $H$
the ray cannot traverse the maximum. Above $H$ the radial speed
cannot vanish anywhere in $[-b,b]$, on either visit. Consequently
the time-ordering proof still applies on those settings, even if
the speed changes between visits. It needs the same exterior time
bounds on all their excursions. Averaging gives

$$
 \Pr\{\text{late far right}\}
 \ \le\ \Pr\{\text{early central}\}+e+1/K .
$$

Here $e$ includes violations of the preparation, work and exterior
bounds. Include the errors of any additional calibration images.
The argument
conditions on the potential before the settings are drawn, so unknown
static strip gains and atoms precisely at a cusp are allowed. A
setting-dependent change of the strip sampled on return would require
its own work bound.

For $K=4$ take release positions within $1\,\mu{\rm m}$ of
$-65,-75,-85,-95\,\mu{\rm m}$, and release speeds at most
$20\,\mu{\rm m/s}$. Blank harmonic images at release and a quarter
period bound these exceptions through $x(0)$ and $v(0)/\omega$,
including clock and frequency tolerances. In squared-length units
$2E/(m\omega^2)=x(0)^2+[v(0)/\omega]^2$, even the smallest gap
between bands exceeds $1100\,\mu{\rm m}^2$ ($74^2-66^2-2.3^2>1100$).
For illustration, allow $2W/(m\omega^2)\le100\,\mu{\rm m}^2$,
with harmonic motion in the exteriors. Each left excursion on the
high-energy branch reaches a magnitude at least
$\sqrt{64^2-100}\,\mu{\rm m}>60\,\mu{\rm m}$. Score the late far side
at $55\,\mu{\rm m}$ so any other right excursion of that ray reaches
at least $\sqrt{55^2-200}\,\mu{\rm m}>50\,\mu{\rm m}$, allowing
opposite work errors on the two visits. The same clock windows
therefore suffice with the stated first-arrival calibration. This
protocol permits a $0.25$ uncertain fraction from the barrier top
alone. For example, a far-side fraction of $0.40$ averaged over the
four equally weighted settings would leave $0.15$ for the early
central population and all remaining errors. It calls for finite
energy bands, finite resolution and an independent upper bound on
work transferred to an atom.

**What has been observed.** Wales et al. returned rubidium-85 atoms
to the same optical barrier in an axial magnetic trap. For the narrow
barrier the oscillation amplitude was about $75\,\mu{\rm m}$, the
probe pulse lasted $10\,\mu{\rm s}$, and the independently observed
trap-centre variation was $1.3\pm0.3\,\mu{\rm m}$ rms. At one nominal
offset of $-0.950\,\mu{\rm m}$ the ten archived post-return right-side
fractions range from $0.106$ to $0.783$ and average about $0.400$.
The record scores the whole right side and uses the detected total.
These are ten repeats at one offset. A large individual value cannot
be combined with an early image chosen from another repeat. In a
matched sample with the same mean, let $q$ bound the late fraction
on the right inside the far gate, with loss and normalization accounted
for. The trajectory comparison would require the early central fraction,
$q$ and the exceptional fraction together to account for about $0.400$,
within sampling and camera error.
[Wales et al., published Figs. 4–5 and Methods](https://doi.org/10.1038/s42005-020-0320-8)
(passages and figures) and [Durham supporting data](https://doi.org/10.15128/r1sf2685090)
(ten experimental rows; [edition and data coverage](../docs/WalesEtAl_SolitonReturn_2020.md)).

The preparation contained approximately 2,500 attractively interacting
atoms. Conserving the cloud's total energy permits exchange of axial
energy between atoms, especially where the two packets overlap. The
paper also reports transverse confinement. Its centre-of-mass trap
calibration, spliced images and absorption-image resolution estimate
do not bound the fraction of individual atoms that keep the same
axial energy on both visits. A singly occupied trap, or an independent
upper bound on this fraction of failures in the occupied trap, would
give the return measurement its one-particle interpretation.

**Central motion and trial action.** For $x=R-R_B$ on a shell within
$R>0$, add $J^2/(2mR^2)$ to the radial potential. Every fixed angular
momentum $J$ retraces the same *radii*. The inclusion uses only arrival
and exterior excursion times for that effective potential. The numerical
harmonic times apply directly to radial rays with $J=0$. For nonzero
$J$ the clock bounds must cover the centrifugal motion as well.

The dimensional inputs in the trajectory test are the gate and launch
lengths, $R_B$ for a shell, spatial response and centre offsets,
exterior frequency or measured flight durations, exposure and release
times and their uncertainties. For quantum transport, also fix the
inertial mass $m$, the single-particle potentials in energy units
including their spatial profiles, and the common preparation before
the choice of shutter or blank. One can specify that preparation by
tight position and mechanical momentum distributions constrained by the
blank images. In the exact fixed-mass dilation (20), lengths divide
by $s$, times by $r$ and $a'=ra/s^2$. The source gate, the camera
windows and the laboratory clock fix $s=r=1$ when those same physical
observations are compared. With $b$ and $\omega$ fixed,
$S_0=m\omega b^2$ is an action unit.
If only accelerations are calibrated, the exact pair
$(a,m,V)$ and $(2a,2m,2V)$ has the same $H/a$ and velocity operator.
Prepare both from the same spatial density operator with timed
potentials scaled in this way and a fixed spatial acceptance.
Every preparation propagator and the acceptance operator agree, so
the probability of acceptance and the conditional release state agree.
Every blank or test propagator also agrees, and the same pixel and
exposure functions give identical final probabilities. Mechanical
momenta scale by two. An independent mass calibration removes this
ambiguity.
[Interacting dilation and calibrated grating](groupoid-quantum-newton-states.md#9-action-calibration-with-a-clocked-grating)
(exact scaling).

For fixed smooth potentials, tight common initial states and fixed
guarded continuous responses, the finite-time Wigner transport
argument above applies to each shutter and blank. A measured strict
excess after allowances would exclude every sequence $a\downarrow0$
in that one-particle family, even as the orbit mesh tends to zero.
The published side counts supply neither that excess at the specified
gates nor a value for a universal physical $\hbar$.

## A single atom returning in a tilted lattice

**6.1 Sol Max, 2026-11-18.** A Newtonian atom that passes a lattice
crest downhill must have enough energy to pass the next identical
crest. Preiss et al. imaged individual rubidium atoms several cells
downhill at 5 ms and back near the source at 11 ms, in separately
stopped preparations. Three counts suffice to test the orbit law.
There is also an exact ambiguity between different trial actions if
the experiment stops only on clock ticks. The two claims use different
hypotheses. [Preiss et al., Fig. 1(b) and Methods](https://arxiv.org/pdf/1409.3100v2)
(figure and passages).

**A test using three positions.** Orient $x$ downhill. Let the potential
per unit mass be $p(x)-g x+u(x)$ with $g>0$, $p(x+d)=p(x)$ and $d$
the measured pitch. Up to the last exposure, bound the oscillation of
$u$ on the visited range by $B$, and the range of the specific axial
energy $e=\dot x^2/2+p(x)-g x+u(x)$ by $W$. Both allowances have
units of speed squared. The second covers unaccounted axial work.
Suppose the scoring process places the atom within $d$ of its reported
site $jd$. Use one preparation law, a common downhill orientation for
the retained guides and a stopping time chosen independently of the
launch. Each position event is measured on a separate set of releases.

| event | reported sites | implication for the true position |
|---|---|---|
| $A$, release | $j=0$ | $x_0\le d$ |
| $D$, 5 ms | $j=5,6,7$ downhill | $x_1\ge4d$ |
| $C$, 11 ms | $j=-1,0,1$ | $x_2\le2d$ |

A differentiable trajectory realizing all three reaches an interior
maximum $z\ge4d$ with zero speed. It previously crossed a point
$y\in[d,2d)$ with $z-y=nd$, $n\ge3$. Comparing the energies at the two
positions cancels $p$ and requires $gnd\le B+W$. Thus $B+W<3gd$
excludes the triple, regardless of the shape of a cell, a possible
finite-force cusp or the distribution of the initial speeds. No
bound involves the number of inserted times in the orbit.

For attempted launches let $s_i$ be the probability of acceptance at
stop $i$, and $q_i$ the probability of the indicated sites conditional
on acceptance there. Use the same launch and guide weights at each stop.
If the probability of any failure of the force, position or clock bounds
in a common trajectory description is at most $\eta$, then

$$
             s_0q_A+s_1q_D+s_2q_C\ \le\ 2+\eta .
$$

Indeed a good orbit can score at most twice, even if the acceptance
decision depends on position. Independent shutter choices sample its
three marginals. This requires the same undisturbed flight up to each
chosen shutter, with pinning errors charged to the position allowance.

In Fig. 1(b), $d=680$ nm. Reading the experimental density cells against
the printed probability scale gives $q_A>0.94$, $q_D>0.22$ on either
choice of downhill side and $q_C>0.92$, allowing for the colour steps.
The authors separately report $0.88(2)$ at the single origin site
near 11 ms in six adjacent guides. The three conservative graphical
readings sum to more than $2.08$. For instance, independently established
$s_i\ge0.98$ and simultaneous lower probability bounds of those sizes
would leave a margin greater than $0.038$ for $\eta$. The paper reports
about 98% initial loading and conditions on the final tube occupation.
The accepted fractions at each stop, simultaneous statistical bounds
and the error in freezing a moving atom are still needed. [Source
readings and apparatus](../docs/PreissEtAl_SingleAtomReturns_2015.md)
(original figure, Methods and thesis passages).

**Could a distant confining wall return the atom in time?** Replace
$-gx$ by $\tfrac12\Omega^2(x-X)^2$, with $X>0$. The bare acceleration
at the source is $\Omega^2 X$. A full period and centre of bare classical
oscillation determine these parameters in clock and ruler units.
Set $\delta=\operatorname{osc}u+W$ and choose $c>0$ with
$c^2\ge2[\operatorname{osc}(p+u)+W]$. At the phase-matched points
the energy comparison now gives

$$
  \tfrac12\Omega^2(z-y)(z+y-2X)\ge-\delta,\qquad
  z-X\ge w_*:=X-2d-\frac{2\delta}{3\Omega^2d}.
$$

Writing $v=z-X$, energy relative to the turn bounds the speed anywhere
on this excursion by $\sqrt{\Omega^2v^2+c^2}$. From release to return
the path length is at least $2v+2X-3d$. For $w_*\ge0$ and $2X>3d$
the elapsed time therefore satisfies

$$
 t_2-t_0\ \ge\
 \min\left\{\frac{2}{\Omega},
       \frac{2w_*+2X-3d}{\sqrt{\Omega^2w_*^2+c^2}}\right\}.
$$

The derivative of the length-to-speed ratio at $v$ has the sign of
$2c^2-(2X-3d)\Omega^2v$. Its minimum on $v\ge w_*$ is at the left
endpoint or the limit at infinity. An arbitrarily fast launch is
included.

For example, consider calibrated ranges $\Omega/(2\pi)=19$–$21$ Hz,
$X=31$–$33\,\mu{\rm m}$, $c\le8$ mm/s and
$\delta\le0.05(3d)\Omega^2X$. Then $v>26.5\,\mu{\rm m}$. In the
ratio use $X\ge31\,\mu{\rm m}$ and $\Omega<132\,{\rm s}^{-1}$ before
taking its endpoint and infinite-speed limits. They exceed 12.8 and
15.1 ms, respectively. This would exclude a return even at a latest
true stop of 11.2 ms. These are specifications for a calibration.
They must hold over each possible excursion, or the probability of
escape beyond the mapped region must be included in $\eta$. Geiger
measured the bare magnetic curvature in a lithium apparatus by timing
oscillations. The rubidium Fig. 1(b) still needs its own curvature,
optical work and freeze-time bounds. Inferring $g$ from a Bloch period
would use the action under test. [Geiger, §§4.3.4, 4.3.8 and 5.2](https://web.physics.ucsb.edu/~weld/publications/Geiger.pdf)
(passages).

**The central-force version.** Consider a particle moving outward
through concentric shells of radial pitch $d$, with specific potential
$p(R)+u(R)$ and conserved specific angular momentum $\ell$
(length squared per time). The centrifugal contribution is
$\ell^2/(2R^2)$. If a particle crosses $Y$ and turns farther out at
$Z$ of the same shell phase, conservation with the same work allowances
requires

$$
                 \frac{\ell^2}{2}(Y^{-2}-Z^{-2})\ \le\ B+W.
$$

In particular let $R_s$ be the outer source edge, and observe a far
event beyond $R_f>R_s+d$ followed by a return inside it. Choose
$Y\in[R_s,R_s+d)$ with $Z-Y$ an integer multiple of $d$.
If $|\ell|\ge\ell_{\min}>0$, the left side is at least
$\ell_{\min}^2[(R_s+d)^{-2}-R_f^{-2}]/2$. A finite launch segment
can calibrate this without an action input. Let the source pass two
position gates separated by time $h$ with the magnitude of its acceleration
bounded by $A_s$ between gates. Its final velocity differs from the
chord velocity by at most $A_sh/2$. Hence one may use the lower bound

$$
 |\ell|\ge
 \frac{|\mathbf r_0\times(\mathbf r_0-\mathbf r_{-h})|}{h}
 -R_s A_sh/2 .
$$

Take the infimum over the two gate widths and the calibrated interval
for $h$. The radial tilt then comes entirely from the orbit. An exactly
radial launch has zero centrifugal drop. The measured rubidium positions
were axial.

**Two actions on one clock.** Fix the ideal single-band chain on all
integer sites, inertial mass $m$, pitch $d$, hopping energy $J_b$,
and energy drop per cell $\Delta=mgd>0$. The site energies are
$E_c-n\Delta$ and each nearest-neighbour matrix element is $-J_b$.
Evolve with
$\exp(-itH/a)$ for trial reduced action $a>0$. Prepare a single atom in
a pinned lattice with zero hopping, condition a site measurement on
site zero and retain its success probability. For example, randomly load site
zero or one with equal probability using the same two source positions.
Any diagonal pinning hold preserves those populations. The initial
acceptance is one half for both actions and conditioning prepares the
same site state. Unpin for
the chosen elapsed time and repin. A fixed fluorescence exposure after
repinning has effects $\sum_n f_j(nd)|n\rangle\langle n|$, where $f_j$
is the calibrated spatial response, including missed counts. Pinned
phases do not enter any of these probabilities.

The Wannier–Stark ladder $E_c+n\Delta$ gives the period
$P_a=2\pi a/\Delta$ up to a scalar phase. For ideal switchings on a grid
of spacing $\tau=1$ ms, take

$$
                    \frac{1}{a_N}=\frac{1}{a}+\frac{2\pi N}{\Delta\tau},
                      \qquad N=1,2,\ldots .
$$

At every integer tick the two flight propagators differ only by a
scalar. All joint preparation and readout probabilities agree, including
rejected outcomes, while $a_N\downarrow0$. This ambiguity survives an
independently fixed pitch and clock. In the [fixed-mass continuum
dilation](groupoid-quantum-newton-states.md#7-interacting-kernels-under-tangent-scaling)
lengths divide by $s$, times by $r$ and $a'=ra/s^2$. Keeping both
physical standards fixes $s=r=1$. The lattice ambiguity instead uses
the discrete energy ladder and the specified times. Fixing $J_b$ in
joules is an extra input to this effective chain. Holding a continuum
optical potential fixed while changing $a$ generally changes $J_b$ and
can introduce other bands. Physical ramps also require their own time
responses. [Hartmann et al., Eqs. (18)–(20)](https://doi.org/10.1088/1367-2630/6/1/002)
and [Glück et al., §1.2](https://arxiv.org/pdf/quant-ph/0111132#page=8)
(passages).

**A finite-duration measurement that separates the pair.** Draw the
*true unpinned duration* independently and uniformly in a window of
width $b$ about each nominal stop. Read the origin site. Write
$C=|\bar q(11\,{\rm ms})-\bar q(5\,{\rm ms})|$ for the difference of
its two averaged probabilities. For any $[0,1]$-valued periodic site
probability of period $P_a$, the full periods in the two windows
cancel. If $r=b\bmod P_a$, the remaining integrals differ by at most
$r$, and also by at most $P_a-r$ upon taking their complements within
one period. Thus

$$
                C\le\frac{P_a}{2b},\qquad
                a\ge\frac{\Delta b}{\pi}C .
$$

Subtract statistical and readout allowances and the sum of the two
total-variation errors in the timing laws from an experimental lower
bound for $C$. This bound needs only the calibrated cell drop and
clock width once the single-band ladder holds. The 500 ms camera exposure in the rubidium apparatus
begins *after* pinning. It cannot be substituted for $b$.

For an explicit setting take $m=1.44\,10^{-25}$ kg, $d=680$ nm and
$g=0.50$ m/s$^2$ as specified mechanical inputs. Then
$\Delta=4.896\,10^{-32}$ J. Choose $T=11$ ms, $a_0=\Delta T/(2\pi)$
and $a_{10}=a_0/111$. Fix a detector that scores the pinned origin site
with unit probability and every other site with zero probability. Set
$4J_b/\Delta=z_1/\sin(5\pi/11)$, where $z_1=2.4048\ldots$ is the
first positive zero of $J_0$. The cited single-site return law is
$q(t)=J_0^2[(4J_b/\Delta)\sin(\pi t/P_a)]$. At $a_0$ its nominal
values are zero at 5 ms and one at 11 ms. Set $b=0.20$ ms. Throughout
either window the Bessel argument changes by less than
$2.45\pi(0.10/11)<0.070$. The integral representation gives
$|J_0'|\le1$. Consequently the slow pair member has
$C\ge(1-0.070)^2-0.070^2>0.85$. The fast member has
$C\le(11/111)/(2\cdot0.20)<0.25$. These are predictions for the
specified hopping and clock window. The experimental Fig. 1(b) used
another hopping setting. [Hartmann et al., Eq. (20)](https://doi.org/10.1088/1367-2630/6/1/002)
and [NIST DLMF, §10.9(i)](https://dlmf.nist.gov/10.9#i) (formulas).

The dimensional inputs to the action comparison are $m,d,g$ (or an
independently fixed $\Delta$), $J_b$, the pinned detector pitch and
spatial response, the launch and stop times, the tick $\tau$, and the
width $b$ when randomized. One may hold the post-pin exposure at 500 ms. For
the trajectory test the additional inputs are the axial work bounds
$B,W$ or $\Omega,X,c,\delta$, the freeze displacement and timing errors,
and the shell radii, launch gates, $h,A_s$ and $\ell_{\min}$ for shells. One can use $S_0=md^2/\tau$
as an action unit. The ratio $a/S_0$, the clock tick and an orbit
mesh are distinct. Only after physical calibration could $a$ be
identified with $\hbar$ and $2\pi a$ with $h_P$. For fixed smooth
continuum forces, tight common preparations and guarded continuous
position responses, the finite-time Wigner limit used above would
exclude a sequence $a\downarrow0$ if the classical count ceiling
were exceeded after allowances. Neither the axial data nor the
single-band contrast bound establishes universal action necessity.

## A clock on escape through a central-force barrier

**6.1 Sol Max, 2026-11-18.** How far does a force measured on an incoming
particle constrain an outgoing one? Polonium-212 emits an alpha particle
and leaves lead-208. One can also fire alpha particles at lead-208. If
the two preparations share a radial barrier of measured height and
width, any positive gain in exterior population in a fixed time gives
an explicit positive lower bound on the action in local Schrödinger
dynamics. The bound allows arbitrary motion inside the barrier. Gurney
and Condon already used the scattering–decay comparison for uranium
in their explanation of alpha decay. The question here is which
measurements suffice to bound the action without entering its value.
[Gurney and Condon, §4](https://doi.org/10.1103/PhysRev.33.127)
(historical passage) and [Gamow's independent 1928 treatment](https://doi.org/10.1007/BF01343196)
(publication metadata).

**What one returning trajectory measures.** The magnetic rigidity of
the emitted alpha gives $K_\alpha=8784.85\pm0.31$ keV. Adding the
daughter recoil for the two-body line gives relative energy
$Q\simeq8.95$ MeV. With incident alphas at $16.486$ MeV laboratory
energy, the elastic yield at $170^\circ$ is $0.997\pm0.049$ times
Rutherford in the digitization of Hudson and Davis's Fig. 1. Thus
the same pair is observed going out and coming back at quite different
energies. [Del Castillo et al., pp. 24–26](https://rmf.smf.mx/ojs/index.php/rmf/article/download/975/738)
(apparatus and Table I), [Hudson and Davis](https://doi.org/10.1103/PhysRevC.9.1521)
and [EXFOR C2798.002](https://github.com/IAEA-NDS/exfor_master/blob/d3e392e3e86a1c20e9094451d1e80a95fff5eaac/exforall/C27/C2798.x4#L53)
(figure digitization).

Take a Newtonian elastic ray at centre-of-mass energy $E_s$, with
impact parameter $b>0$, turning radius $r_m$, and signed, unwrapped
outward deflection $0<\Theta<\pi$. Set $U(\infty)=0$. Suppose
$U(r)\ge-B$ for $r\ge r_m$. In the central scattering quadrature,
replacing $U$ by $-B$ increases the denominator. Hence

$$
 \frac{\pi-\Theta}{2}
 =\int_{r_m}^\infty\frac{b\,dr}{r^2\sqrt{1-U(r)/E_s-b^2/r^2}}
 \ \ge\ \arcsin\!\frac{b}{r_m\sqrt{1+B/E_s}} .
$$

The turning condition $b^2/r_m^2=1-U(r_m)/E_s$ yields
$U(r_m)\ge E_s\sin^2(\Theta/2)-B\cos^2(\Theta/2)$.
No impact distribution enters. At $E_s\simeq16.17$ MeV an outward
bend of at least $160^\circ$ on a nonnegative exterior requires
$U(r_m)>15.6$ MeV, over $6.6$ MeV above the outgoing line. An
allowed negative depth $B$ costs at most $0.031 B$. The polar detector
does not identify the sign or winding of the deflection. The bound
also leaves the location and width of the high region open. On a
scalar force curve with $|U'|\le F_{\max}$ the potential stays above
$U(r_m)-F_{\max}D$ for the next outward distance $D$. Newton's
Lemma X, Corollary 4, suggests measuring that force independently by
initial displacements. Transferring it to every outgoing state is a
separate physical premise. [Chiron and Marcos, §II](https://arxiv.org/html/1601.00064)
(central scattering quadrature) and [Newton's two editions](newton-insertion-action.md#lemma-x-and-the-measurement-of-initial-force)
(historical passages).

**A bound from two position counts.** Let $a>0$ be the trial reduced
action and $\mu$ the reduced mass. Use the time-independent local
Hamiltonian $H_a=-a^2\nabla^2/(2\mu)+U$ in the relative coordinate.
Allow internal degrees of freedom, with $U$ acting on their Hilbert
space at each position. Assume a semibounded self-adjoint realization
whose quadratic form admits bounded Lipschitz position cutoffs. Fix
the energy band $[E_c-w,E_c+w]$ and its projector $P$. Require the
form bound $U\ge E_c+w+\Delta$ in **every admitted internal state**
throughout $R\le r\le R+D$, with $\Delta,D>0$. All energies use the
same separated-pair threshold. Define a position score $F$ that is
zero up to $R+D/3$, rises linearly to one at $R+2D/3$, and stays one
thereafter. Classical trajectories in the band have constant $F$ by
conservation of energy and continuity of the relative position.

Put $p_\Delta=\sqrt{2\mu\Delta}$ and $v_\Delta=p_\Delta/\mu$. For any
integer $N\ge1$, any density matrix in the band and any elapsed time
$T$, evolution with $i a\,\partial_t\psi=H_a\psi$ satisfies

$$
 |\langle F\rangle_T-\langle F\rangle_0|
 \le \frac{3T v_\Delta}{D}\sqrt{1+w/\Delta}
        \left(\frac{3N a}{D p_\Delta}\right)^{2N}.
$$

To see why the bound is uniform over preparations, put $d=D/(3N)$.
Take $\chi_0=1$. For $1\le j\le N$, let $\chi_j$ rise linearly from
zero at $R+(j-1)d$ to one at $R+jd$, stay one, and fall symmetrically
at the outer edge, vanishing outside the two ramps. Each cutoff and its
gradient are supported where the preceding cutoff equals one.
Set $X_j=\|\chi_jP\|$. For a unit vector $\psi=P\psi$ the
one-cutoff IMS identity and the shell bound give

$$
 \frac{\|a\nabla(\chi_j\psi)\|^2}{2\mu}
       +(w+\Delta)\|\chi_j\psi\|^2
 \le w X_j^2+\frac{a^2}{2\mu d^2}X_{j-1}^2 .
$$

Indeed $(H_a-E_c)\psi$ belongs to the band and has norm at most $w$,
so the localized energy pairing is bounded by $wX_j^2$. Discard
the kinetic term and take the supremum to get $X_j\le q^j$ with
$q=a/(d p_\Delta)$. Keeping the kinetic term then bounds
$\|a\nabla(\chi_N\psi)\|$ by $(a/d)\sqrt{1+w/\Delta}\,q^{N-1}$.
In the probability current paired against $\nabla F$, the state and
its gradient equal their $\chi_N$-localized versions. The absolute
rate of change of the score is therefore at most
$3X_N\|a\nabla(\chi_N\psi)\|/(\mu D)$. Time evolution preserves the
band. Integration and mixing give the displayed bound.
[Simon, Lemma 3.1](https://www.numdam.org/item/AIHPA_1983__38_3_295_0.pdf)
(IMS localization identity).

**Preparation and readout.** Use matched releases for the two counts.
A guarded outer detector gives a lower bound on $\langle F\rangle_T$
if a registered event guarantees that the pair is still outside at
$T$. Initial containment gives an upper bound on $\langle F\rangle_0$.
Both probabilities use all tagged parents in their denominator. Bound
false tags, loss, spatial and timing errors in converting the counts.
If at most $\eta<1$ of the prepared energy probability lies outside
the band, projecting and renormalizing changes either score by at most
$\sqrt{\eta}$, by purification and the fidelity bound on trace
distance. Subtract $2\sqrt{\eta}$ from the observed gain in addition
to the readout allowances. For a positive remainder $\delta$,

$$
 a\ \ge\ \frac{D p_\Delta}{3N}
 \left(\frac{\delta D}{3T v_\Delta\sqrt{1+w/\Delta}}\right)^{1/(2N)} .
$$

Under $a\mapsto s a$, the projector becomes the projector of $H_{sa}$
on the same physical energy interval. The preparation may change
arbitrarily within that constraint. Evolving to the same $T$ with
$H_{sa}$ and reading the same $F$ multiplies the gain ceiling by
$s^{2N}$. $N$ subdivides the proof only. The estimate needs neither an
attempt frequency inside the nucleus nor an exponential decay law.
[Fuchs and van de Graaf, Theorem 1](https://arxiv.org/abs/quant-ph/9712042)
(trace distance and fidelity).

For a sensitivity calculation take $R=16$ fm, $D=4$ fm,
$E_c=9.0$ MeV, $w=0.5$ MeV, $\Delta=2.0$ MeV, $T=300$ ns and
$\delta=1/4$. For instance, fix an exterior counter with a calibrated
linear response from zero at $1.0\,\mu{\rm m}$ to one at
$1.1\,\mu{\rm m}$. Its score lies below $F$. Average that score over
independent exposure times from 299 to 300 ns and use the latest time
in the bound. This specifies finite spatial and temporal resolutions
for the proposed readout. Bounding the initial population at
$r>R+D/3$ still requires a separate preparation measurement.
The electrostatic coefficient for charges $2e,82e$
is $C=164e^2/(4\pi\epsilon_0)\simeq236.2$ MeV fm. At $20$ fm the
Coulomb energy exceeds $11.8$ MeV. A measured maximum lowering of
$0.30$ MeV across the shell would thus suffice. With
$\mu c^2\simeq3.65\,10^3$ MeV we have $p_\Delta c>120$ MeV and
$v_\Delta<c/30$. The dimensionless ratio in parentheses is greater
than $2^{-54}$. Taking $N=18$ gives $a>3$ MeV fm$/c$. The inputs are
the two fragment masses, the charge and electrostatic force calibration,
the shell radii and work relative to the threshold, the band edges,
and the clock and position response with their errors. $c$ converts
mass and momentum units. The magnetic energy calibration uses measured
field, orbit radius and charge. None of these inputs uses a wavelength
converted to momentum by a supplied action.

**What the experiment leaves open.** Belli et al. find a
$295.1(4)$ ns half-life from selected beta–alpha pulse pairs. The
slope of that delay histogram does not give the absolute gain for
all tagged launches. Nor does one resolved alpha line bound their
total energy leakage. The incident angular yield does not establish
the proposed shell location or the $0.30$ MeV allowance in every
decay channel. [Belli et al., §§3.2–3.3, Fig. 9](https://arxiv.org/pdf/2107.04233v1)
(pulse selection and timing fit), [experimental source details](../docs/Polonium212_AlphaEscape.md).

A mechanical readout exists as well. Wang et al. calibrated the recoil
of a levitated silica sphere with electric impulses and detected alpha
decays in the same chain. Their selected impulse component measures
momentum deposited in the sphere. It leaves the point of release inside
the nucleus unresolved. [Wang et al., Figs. 3–4](https://arxiv.org/pdf/2402.13257v2)
(apparatus and recoil selection).

A zero-action alternative shows why a common force matters. Give the
incident pair the repulsive $C/r$ potential, consistent with the
selected low-energy Rutherford ratio. In an unobserved outgoing
internal state use $\widetilde U(r)=f(C/r)$, with $f(x)=x$ for
$x\le Q/4$, smoothly increasing to a plateau below $Q/2$. A localized
parent with energy $Q$ releases the pair at a chosen internal clock
time with radial kinetic energy $Q-\widetilde U(r_{\rm birth})>0$.
Sample its waiting time from the fitted delay law, allowing for the
flight and detector response. The fragments reach the same ordinary
Coulomb exterior with total kinetic energy tending to $Q$ and opposite
momenta. This model reproduces the named energy, delay scale and
elastic row. It predicts different forces on the two preparations
inside $4C/Q$. An independent bound on that difference and an absolute
exterior count would test it. The numerical action bound above remains
conditional on those measurements and on the specified dynamics.

## An exterior force test with argon

**6.1 Sol Max, 2026-11-18.** At $0.34$ eV Buckman and Lohmann report an
electron–argon attenuation cross section of $0.318$ square ångströms
(relative error $3.5\%$, one standard deviation). The question from Lemma X
is whether a separately measured radial force could produce so little
loss. The following comparison uses elastic trajectories and a physical
exit aperture. All assumptions about the atom's interior can be dropped
once the contributing rays are shown to turn outside it.
[Buckman and Lohmann, §§2–4 and Table 2](https://doi.org/10.1088/0022-3700/19/16/013)
(passages and data row).

**The independently measurable force coefficient.** Let $\alpha_v$ be
the static dipole polarizability expressed as a volume, so
$\mathbf p_{\rm ind}=4\pi\epsilon_0\alpha_v\mathbf E$. The induced-dipole
energy in a charge's field is $-C_4/r^4$ to leading order, with
$C_4=[e^2/(4\pi\epsilon_0)]\alpha_v/2$. Dielectric measurements on argon
give a molar polarizability $A_\epsilon=4.140686(10)$ cubic centimetres
per mole. Using $\alpha_v=3A_\epsilon/(4\pi N_A)$ and the electrostatic
coupling $1.44$ eV nm gives $C_4\simeq1.18\,10^{-3}$ eV nm$^4$.
These inputs can be calibrated by charge, force, length and particle
number. A dielectric measurement probes a weak, nearly uniform field.
It determines the coefficient at large distance. The accuracy of the
instantaneous radial force in an actual flyby is an additional measurement.
[Gaiser and Fellmuth, Table III](https://doi.org/10.1103/PhysRevLett.120.123203)
(method and data passage).

**A finite annulus with a known minimum deflection.** Let
$E=\mu v^2/2$ be the relative kinetic energy, $\mu$ the reduced mass,
and $p=\mu v$. Write $V(\infty)=0$ and assume a time-independent
central potential, locally $C^2$ outside $r_0$. Suppose that on
$r\ge r_0$ its inward force magnitude obeys
$$
 4(1-\gamma)C_4/r^5\ \le V'(r)\le\ 4(1+\gamma)C_4/r^5,
 \qquad 0\le\gamma<1 .
$$
Let $n(r)=\sqrt{1-V(r)/E}$, $\rho=r n(r)$ and
$B(r)=rV'(r)/[2(E-V(r))]$. Then
$d\log\rho/d\log r=1-B(r)$. Fix impact radii $b_1\le b\le b_2$. If
$$
 B_*=\frac{2(1+\gamma)C_4}{E r_0^4}<\tfrac12,\qquad
 b_1>r_0\sqrt{1+\frac{(1+\gamma)C_4}{E r_0^4}},
$$
then $0\le B\le B_*$ outside $r_0$ and the turning point
$\rho(r)=b$ lies in this exterior region. Use the usual central-orbit
quadrature, with $\chi$ positive for inward bending and
$\rho=b\sec u$. Subtracting its free angle gives
$$
 \chi(b)=2\int_0^{\pi/2}\frac{B(r(b\sec u))}{1-B(r(b\sec u))}\,du .
$$
Here $r(\rho)$ is the unique exterior inverse. This is the single-turning-point
formula of [Hendi, Henn and Leonhardt, Eqs. (1)–(4)](https://arxiv.org/pdf/cond-mat/0605637)
(passage, opposite sign convention). Since $n\ge1$ and
$B\ge 2(1-\gamma)C_4 n^2/(E\rho^4)$, the integral of $\cos^4u$
gives the finite bounds
$$
 \frac{3\pi(1-\gamma)C_4}{4E b^4}
 \ \le\ \chi(b)\ \le\ \frac{\pi B_*}{1-B_*}<\pi .
$$
The upper bound excludes a return to the forward detector after a full
turn. Neither bound needs the force inside $r_0$. Inserting times into
a convergent trajectory calculation leaves both inequalities intact.

**Putting the loss in the units of the experiment.** Take
$E\in[0.30,0.40]$ eV, $C_4\in[1.15,1.20]\,10^{-3}$ eV nm$^4$,
$\gamma=1/2$, $r_0=0.50$ nm and $[b_1,b_2]=[0.55,0.60]$ nm.
Throughout this band $B_*\le0.192$, $\rho(r_0)<0.525$ nm and
$\chi(b)>0.026$ rad. The annulus has area
$A=\pi(b_2^2-b_1^2)=0.0575\pi$ nm$^2$, or $18.06$ square ångströms.
Uniformly distributed independent gas atoms give this area per unit
target column for any fixed incident ray.

Buckman and Lohmann used a field-free tube of length $L=255$ mm
with a $D=2$ mm diameter exit. For a collision a distance $z$ upstream,
the undeflected and deflected rays can both cross that exit only if their
angle is at most $D/z$. The angle between the two unit directions is
bounded by their transverse slope difference, which is at most the
diameter of the disk divided by $z$. Thus for the upstream
half the angle is at most $2D/L<0.016$ rad. This uses only straight-line
flight and the measured lengths. In a calibration allowing up to
$0.004$ rad in total for the relative-to-laboratory angle, residual
fields, alignment and finite-distance propagation, take $\theta=0.020$
rad as the largest accepted relative deflection there. The margin is
positive at fixed length and clock resolution. The authors estimate an
energy resolution below $20$ meV at $0.4$ eV. A resolution width alone
gives no hard support for the energy distribution.
[Buckman and Lohmann, pp. 2548–2550, 2553–2556, 2561](https://doi.org/10.1088/0022-3700/19/16/013)
(instrument and resolution passages).

Let $Y$ be the gas-induced loss per unit column in the dilute limit,
normalized to the empty-cell detected current. Assume its linear term
is the single-atom loss minus the single-atom gain. A column scan
checks the range in which the measured slope applies. Write $f$ for a certified
lower fraction of reference fluence and gas column meeting the energy,
upstream-location and angular conditions, including the relative flux for
moving targets. More precisely, on the annulus these good encounters
dominate $fP(dE)\,2\pi b\,db$ per unit column for a probability $P$ on
the specified energy band. Let $G$ bound, in area units, the gain from
rays entering the counted output that would otherwise have missed it,
including migration between timing bins. All good encounters in that
annulus remove a reference count. The Newton prediction therefore obeys
$$
 Y_{\rm Newton}\ge f A-G .
$$
For $f=1/2$ and $G=0$ this exceeds $9.0$ square ångströms. Even a
conservative **trial** upper value $Y_{\rm hi}=0.40$ square ångströms
would suffice if $G=0$ and $f>0.023$. Ferch et al. independently measured
$0.311$ square ångströms at $0.345$ eV with a magnetic lens. Its angular
response differs from that of the field-free tube. Both experiments
discuss forward-scattering corrections using angular distributions.
Their quoted errors do not by themselves bound $G$ under an alternative
classical angular law. Pressure scans, column density, empty-cell
fluence, background and detector efficiency enter the comparison.
[Ferch et al., Table 1 and §§3.1, 4](https://doi.org/10.1088/0022-3700/18/5/017)
and [Buckman and Lohmann, §4](https://doi.org/10.1088/0022-3700/19/16/013)
(data and correction passages).

A way to control the gain independently is to admit only rays through
two upstream stops of radius $a_s=0.25$ mm a distance $L_s=L$ apart,
the second at the cell entrance. Every straight ray through both
would arrive within $a_s(1+2L/L_s)=0.75$ mm of the exit centre.
Pulse gates at the stops separated by $0.74$ microseconds, each with a
half-width of $5$ ns, select velocity using $L_s$ and a clock. The
on-axis flight interval of $0.73$–$0.75$ microseconds is inside the
declared energy band for electrons on stationary argon. The small
inclination, mass ratio, gas temperature and timing tails enter $f$.
Count the whole outgoing pulse with calibrated efficiency across the
exit. A wide time gate and an empty-cell beam profile are essential
to the bound on $G$. This is a proposed preparation. The two published
experiments did not report these guarded counts.

**What could calibrate the force independently?** The nominal traversal
time $r_0/v$ is $1.3$–$1.6$ fs. Spatial and temporal response can be
tested with different external fields. The following two estimates
specify what such measurements would control.

First consider a neutral spherical source whose static polarization
energy in an imposed potential is minus one half a positive, rotation-
invariant quadratic form. Suppose the responding charge is contained
inside $r_1=0.40$ nm and the form is continuous on the converging
exterior point-charge expansion there (for example the support is
strictly smaller than $r_1$ and the form is bounded on its potentials).
The different spherical harmonic degrees are orthogonal for this
form. Neutrality removes degree zero. Consequently the static energy
is $V_{\rm st}(r)=-\sum_{\ell\ge1}c_\ell/r^{2\ell+2}$, with
$c_\ell\ge0$ and $c_1=C_4$. Convergence at $r_1$ suffices to
differentiate at $r\ge r_0>r_1$. Zhang et al. distinguish a convergent exterior polarization series
for confined hydrogen from the asymptotic free-atom expansion.
[Zhang et al. (2012)](https://doi.org/10.1063/1.4705279) (abstract).

A single measurement of the work of bringing a charge from infinity
to $r_1$ now bounds the higher-order force on the whole annulus. Put
$u_1=-r_1^4V_{\rm st}(r_1)/C_4-1$. Each higher multipole contributes
a nonnegative weight to $u_1$. Its contribution to the fractional
force excess at $r$ equals that weight times
$(\ell+1)(r_1/r)^{2\ell-2}/2$. For $\ell\ge2$ these factors are at
most $(3/2)(0.40/0.50)^2=0.96$ because their successive ratios are
bounded by $(4/3)(0.40/0.50)^2<1$. Thus
$$
 0\le \frac{r^5 V'_{\rm st}(r)}{4C_4}-1\le0.96\,u_1,\qquad r\ge r_0 .
$$
For example, an independent upper limit $u_1\le1/4$ would leave a
fractional allowance of $0.26$ before the upper force tolerance $1.50$
is reached. Penetration by the probe, higher powers of field strength
and delayed response require their own control for real argon.

For a temporal check, prescribe a straight probe passage
$\mathbf r(t)=(b,0,vt)$ independently of the scattering experiment.
Write $K=|e|/(4\pi\epsilon_0)$, $\mathbf E(t)=K\mathbf r/r^3$ up to
overall sign, and $\alpha=4\pi\epsilon_0\alpha_v$. Model the *dipole*
by passive classical oscillator modes with positive static weights
$d\alpha(\nu)$ summing to $\alpha$, angular frequencies $\nu>0$ and
zero incoming excitation. Each mode of static weight $a$ obeys
$\ddot{\mathbf d}+\nu^2\mathbf d=a\nu^2\mathbf E(t)$.
All choices of $\nu$ give the same static response per unit weight.
At closest approach the retarded solution gives
$|\mathbf d(0)|/(a|\mathbf E(0)|)\le\pi\nu b/(2v)$ by integrating
$K/(b^2+v^2t^2)$ over the incoming half-line. An arbitrarily slow
classical dipole therefore defeats a static force calibration even
when its whole static work curve is known.

Conversely let $\tau_{\rm pol}=\alpha^{-1}\int\nu^{-1}\,d\alpha(\nu)$.
For the integrated force on the prescribed probe, the error from
using an instantaneous dipole obeys
$$
 \frac{|\mathbf I_{\rm ret}-\mathbf I_{\rm stat}|}{|\mathbf I_{\rm stat}|}
 \le \frac{8v\tau_{\rm pol}}{b},\qquad
 |\mathbf I_{\rm stat}|=\frac{3\pi\alpha K^2}{4vb^4}.
$$
In fact $\mathbf d-a\mathbf E$ is the retarded sine integral of
$-a\ddot{\mathbf E}/\nu$. Along the straight line,
$\|\nabla\mathbf E(t)\|\le2K/r(t)^3$ and
$|\ddot{\mathbf E}(s)|\le6Kv^2/r(s)^4$. For the latter, the squared
dimensionless coefficient is $45x^4-18x^2+9\le36$ for
$x=\hat{\mathbf r}\cdot\hat{\mathbf v}$. The integral of these two
even bounds over $s<t$ is half their full product integral, namely
$6\pi K^2/b^5$. Integration of the static transverse force and summing
the retarded errors over modes gives the displayed ratio. Masses enter
through $\mu^{-1}=m_e^{-1}+M_{\rm Ar}^{-1}$ when converting $E$ to $v$.

The frequencies in this moment are clock frequencies. For this mode
model the causal susceptibility has
$d\alpha(\nu)=(2/\pi)\operatorname{Im}\alpha(\nu+i0)\,d\nu/\nu$,
including line masses. Thus an independently calibrated absorption
spectrum can bound $\tau_{\rm pol}$ without converting photon energy
to frequency with $\hbar$. A bound $\tau_{\rm pol}\le9\,10^{-17}$ s
would put the integrated dipole error below one half throughout the
test annulus. The prominent argon lines near $105$ and $107$ nm have
inverse angular frequencies near $5.6\,10^{-17}$ s via $\lambda/(2\pi c)$.
Their positions and strengths alone do not bound the whole positive
moment. The straight-probe estimate controls a prescribed path. The
coupled calculation below allows the probe to turn and the target to
retain energy. [Ligtenberg et al., optical absorption measurements](https://doi.org/10.1103/PhysRevA.49.2363)
(abstract) and [NIST, Ar I resonance wavelengths](https://physics.nist.gov/PhysRefData/Handbook/Tables/argontable3.htm)
(table).

There is a numerical cross-check of the required timescale. Kumar and
Thakkar tabulate argon oscillator-strength moments $S_{-2}=11.08$ and
$S_{-3}=16.75$ in atomic units. Static dipole weights are proportional
to oscillator strengths divided by squared frequency. Their ratio
therefore gives $\tau_{\rm pol}=(16.75/11.08)t_{\rm at}\simeq
3.66\,10^{-17}$ s with the conventional atomic time
$t_{\rm at}=\hbar/E_{\rm h}$ ($E_{\rm h}$ is the Hartree energy).
It puts $8v\tau_{\rm pol}/b$ near $0.20$ at the fastest, closest
straight probe in the band. Their distribution combines absorption and
refractivity data with theoretical input and a sum-rule constraint.
For an independent test of action necessity the frequency integral must
be calibrated with lengths, clocks and field response, with spectral
coverage stated. [Kumar and Thakkar, §§II–III and Table I](https://doi.org/10.1063/1.3315418)
(method and moment table).

### Two pulse tests for a freely moving charge

**6.1 Sol Max, 2026-11-18.** Consider the reciprocal classical model
defined below, with its internal modes initially at rest. Given the
specified static work and two pulse readings, every incoming electron
with relative energy $0.33$–$0.35$ eV and impact radius $0.70$–$0.72$ nm
turns by more than $0.0133$ rad. In the first tenth of the field-free
cell the largest accepted turn is $0.0128$ rad under the angular
calibration above. The claim allows energy and angular momentum transfer
to the target and modes arbitrarily close to zero frequency.

**What is measured.** Retain the static exterior expansion above and write
$w_1=1$, $w_\ell=c_\ell/(C_4 r_1^{2\ell-2})$ and
$U=\sum_{\ell\ge2}w_\ell=-r_1^4 V_{\rm st}(r_1)/C_4-1$.
Each $c_\ell$ has units of energy times length$^{2\ell+2}$.
The dipole coefficient is measured in a uniform field. The equilibrium
work of a point charge at $r_1$ supplies $1+U$. Use the same source
position for the static and pulsed readings. The estimates below allow
$r_1=0.400\pm0.001$ nm. In each
angular degree assume a normalized positive distribution $P_\ell(d\nu)$
of undamped oscillator modes with angular frequencies $\nu>0$. Use the
same linear, isotropic response to the imposed fields and the passing
charge at the stated amplitudes. The equilibrium references must
include any slowly relaxing response. For a bounded unit drive of
duration $T$ starting from rest, an additional mode of static weight
$w$ changes the finite response by at most $w(\nu T)^2/2$, since
$|\nu\sin(\nu t)|\le\nu^2t$ for $t\ge0$. Its equilibrium contribution
is $w$. Finite pulse readings alone cannot certify that upper bound.

Apply an exponential envelope of rate $\sigma=2.5\,10^{14}$ s$^{-1}$
to two spatial profiles. The first imposes a uniform field and reads
the induced dipole along it. The second imposes the Coulomb potential
of a charge at $r_1$ and reads the induced potential there. At full
amplitude take the electron charge magnitude $|e|$ and a uniform field
of magnitude $|e|/(4\pi\epsilon_0 r_1^2)$, about $9$ V/nm. The
point-charge profile specifies the external field over the responding
region. Each readout is conjugate to the applied amplitude and is oriented
to give a positive static dipole contribution.
Normalize the induced potential by its equilibrium dipole magnitude
$2C_4/(|e|r_1^4)$, about $0.092$ V. A mode driven from the remote past
by $e^{\sigma t}$ follows with factor $\nu^2/(\nu^2+\sigma^2)$.
Thus the normalized static reading minus the pulse reading gives $d_1$
for the uniform profile and $d_1+d_H$ for the point-charge profile, where
$$
 h_\sigma(\nu)=\frac{\sigma^2}{\nu^2+\sigma^2},\qquad
 d_1=\int h_\sigma\,dP_1,\qquad
 d_H=\sum_{\ell\ge2}w_\ell\int h_\sigma\,dP_\ell .
$$
Both pulses may start at $t=-17/\sigma$ from rest. Integrate the
signal and the envelope over the last $1/\sigma$ before $t=0$ and
divide the former by the latter. The omitted past contributes at most
$e^{-17}\nu/\sqrt{\nu^2+\sigma^2}$ per unit static weight at any time
in the gate, by integration of the oscillator's sine kernel. The
envelope throughout the gate is at least $e^{-1}$, so the normalized
error is at most $e^{-16}$ per unit weight. Errors of both readings enter
the subtraction for $d_H$. The duration is $68$ fs and the gate is $4$ fs.
The following trial upper limits include those errors and the uncertainties
in the spatial profiles, drive amplitudes, readout gains and static references.
$$
 U\le1/8,\qquad d_1\le10^{-4},\qquad d_H\le1.2\,10^{-5}.
$$
The last limit corresponds to about $1.1$ microvolts after dipole
subtraction at the nominal radius and $C_4$.
Two targets can have the same static work at every radius and the same
complete dipole response while differing in the frequency of a
quadrupole of positive weight. The second pulse distinguishes them.

There is a check on the size of these proposed readings. In atomic
units put $\epsilon_i$ equal to a tabulated excitation energy,
$u=\sigma t_{\rm at}$ with $t_{\rm at}=2.42\,10^{-17}$ s, and
$\alpha_\ell=\sum_i f_i^{(\ell)}/\epsilon_i^2$.
The effective spectrum of Jiang et al. then gives the degree-$\ell$
deficit per unit weight as
$u^2\sum_i f_i^{(\ell)}/[\epsilon_i^2(\epsilon_i^2+u^2)]/\alpha_\ell$.
Their argon entries $\alpha_1=11.08$, $\alpha_2=52.80$,
$\alpha_3=536.4$ give $w_2\simeq0.083$ and $w_3\simeq0.015$ using
$w_\ell=(\alpha_\ell/\alpha_1)(a_0/r_1)^{2\ell-2}$ and the Bohr
radius $a_0=0.0529$ nm. Their Table 2 gives $d_1\simeq9.2\,10^{-5}$
and a combined quadrupole and octupole contribution to $d_H$ of about
$8.7\,10^{-6}$. These are fitted atomic-unit benchmarks. The higher
degrees, charge penetration, equilibrium work and a clocked response at
the proposed field strength still need independent calibration.
[Zhang et al., Eq. (1)](https://arxiv.org/pdf/1108.0150) (charge-potential convention) and
[Jiang et al., Eqs. (2)–(4), §3.21 and Ar rows of Tables 1–2](https://arxiv.org/pdf/1410.7957)
(method and table passages).

**Coupled motion.** Put $x=\mathbf r/b$, $s=v(t-t_*)/b$,
$\beta=r_1/b$ and $q=C_4/(Eb^4)$, with $E=\mu v^2/2$.
Let $f_\ell(x)=|x|^{-\ell-1}\mathbf Y_\ell(\hat x)$, using real spherical
harmonics normalized by $\mathbf Y_\ell(n)\cdot\mathbf Y_\ell(n')=
P_\ell^{\rm Leg}(n\cdot n')$, the Legendre polynomial. Primes here
denote $s$ derivatives. Each target coordinate $y_{\ell\nu}$ is driven
by the actual charge position. The reciprocal equations are
$$
 \begin{aligned}
 y_{\ell\nu}''+\omega^2y_{\ell\nu}&=\omega^2 f_\ell(x),\qquad
        \omega=\nu b/v,\\
 x''&=q\sum_{\ell\ge1}w_\ell\beta^{2\ell-2}
        Df_\ell(x)^T\int y_{\ell\nu}\,dP_\ell .
 \end{aligned}
$$
Indeed the mode potential is proportional to
$|y|^2/2-y\cdot f_\ell(x)$ with the displayed positive weight and
mode kinetic term $|y'|^2/(2\omega^2)$. Equilibrium gives $y=f_\ell$
and the measured static potential. Classical oscillator models of induced
dipoles are established. The model here assumes the convergent
exterior response of the preceding section, no incoming excitations
and no additional force on the exterior orbit.
[Lamoureux and Roux](https://doi.org/10.1063/1.1589749) (abstract, dipole model)
and [NIST DLMF 14.30.9](https://dlmf.nist.gov/14.30.E9) (harmonic addition formula).

Split the modes at $3\sigma$. Their total static weight on the slow
side is $S=\sum w_\ell P_\ell(\nu\le3\sigma)\le10(d_1+d_H)<0.0012$.
On the fast side $F=\{\nu>3\sigma\}$, $\nu^{-2}\le
10h_\sigma/(9\sigma^2)$. Write $\tau_{\ell,F}=\int_F\nu^{-1}\,dP_\ell$.
Cauchy–Schwarz, including the weights in the higher degrees, gives
$$
 \begin{aligned}
 T_F&=\tau_{1,F}+1.85\sum_{\ell\ge2}w_\ell\tau_{\ell,F}\\
 &\le\frac{\sqrt{10d_1/9}+1.85\sqrt{10U d_H/9}}{\sigma}
 <5.18\,10^{-17}\ {\rm s}.
 \end{aligned}
$$
Here $v<3.52\,10^5$ m/s for electron–argon relative motion,
$\Lambda=vT_F/b<0.0261$, and the preceding $C_4$ band gives
$0.0122<q<0.0152$. In mechanical units one needs $C_4/\mu$ in
length$^6$/time$^2$, since $q=2(C_4/\mu)/(v^2b^4)$. This allows
force per unit reduced mass, lengths and flight times to set the
comparison without a photon energy–frequency conversion. The possibly
divergent inverse moment of the slow modes never enters the orbit estimate.

Compare the moving charge with the static orbit $X$ of the same incoming
impact, velocity and asymptotic time offset. Write $F_{\rm st}(x)$ for
the right hand side at equilibrium, $r=|X|$ and $g(s)=\sqrt{1+s^2}$.
Energy and angular momentum give
$|X'|^2=1+q\sum w_\ell\beta^{2\ell-2}r^{-2\ell-2}$,
$|X\times X'|=1$. At $r=0.99$ the squared value of $r|X'|$ would
be at most $0.99^2+q(1+U\,0.58^2)/0.99^2<1$. Thus $r>0.99$,
$\beta/r<0.58$ and $|X'|<1.01$. Also
$$
 (r^2/2)''=1-q\sum_{\ell\ge1}\ell w_\ell\beta^{2\ell-2}r^{-2\ell-2}
 \ge 1-q(1+2U\,0.58^2)/0.99^4>0.98 .
$$
Choose $t_*$ at the unique static turning point. Twice integrating
gives $r\ge0.989g$. The single-turn quadrature above gives
$3\pi q/4\le\chi_X<\pi$ since the dipole is present, all the extra
forces are inward and $B(r)<2.3q/0.99^4<0.04$ along this orbit.

**The error in the outgoing angle.** For matching incoming asymptotes
let
$$
 D(s)=\sup_{t\le s}\max\bigl\{|x(t)-X(t)|/g(t),\,|x'(t)-X'(t)|\bigr\}.
$$
While $D\le0.028$ the segment between the two positions lies at radius
at least $a g$ with $a=0.96$, and $|x'|\le V=1.04$. On that segment
$|F_{\rm st}|\le F_0 q a^{-5}g^{-5}$, $F_0=2.3$, and
$\|DF_{\rm st}\|\le12q a^{-6}g^{-6}$. Indeed $\beta/a<0.60$.
Relative to the static dipole, a weight $w_\ell$ adds at most
$(\ell+1)0.36^{\ell-1}/2$ times its weight to the force bound and
$(\ell+1)(2\ell+3)0.36^{\ell-1}/10$ times its weight to the
derivative bound. Both maxima for $\ell\ge2$ occur at $\ell=2$.

For the time delay, denote $L(s)=|x''-F_{\rm st}(x)|$. Along the path
the oscillator solution gives $y-f=-\int_{-\infty}^s
\cos(\omega(s-t))\dot f(t)\,dt$. For a fast mode integrate once more
to get $|y-f|\le\omega^{-1}\int_{-\infty}^s|\ddot f(t)|\,dt$.
Use the first formula on slow modes. At radius $R$,
$\|Df_\ell\|\le(\ell+1)R^{-\ell-2}$ and
$|D^2f_\ell[u,u]|\le H_\ell |u|^2R^{-\ell-3}$.
Here $H_1=6$ from the dipole formula above and for $\ell\ge2$ one may
take $H_\ell=\sqrt{(\ell+1)(2\ell+1)(\ell+2)(2\ell+3)}$.
For the first bound the radial derivative has norm $(\ell+1)R^{-\ell-2}$
and is orthogonal to the angular derivatives. The squared gradient
trace is $\Delta |f_\ell|^2/2$ by harmonicity. The remaining tangential
trace is $\ell(\ell+1)R^{-2\ell-4}$. The squared Frobenius norm of the
Hessian is $\Delta^2|f_\ell|^2/4$, giving $H_\ell$.
In the product with the force derivative the factor relative to the
dipole is $(\ell+1)H_\ell\,0.36^{\ell-1}/12<1.85$ for $\ell\ge2$.
It equals $3\sqrt{420}\,0.36/12$ at degree two. At degrees three
and above use $H_\ell\le2(\ell+1)(\ell+2)$ and the decreasing product.
For two first derivatives the factor is $(\ell+1)^2
0.36^{\ell-1}/4\le1$.

Put $k_1=12\Lambda a^{-7}$, $k_2=4\Lambda a^{-6}$ and $k_0=4S a^{-6}$.
The preceding product bounds give $L(s)\le qg(s)^{-3}K(s)$, where a
nonnegative majorant is the solution of
$$
 \begin{aligned}
 K(s)&=\int_{-\infty}^s [\,A(t)+k_2qg(t)^{-6}K(t)\,]\,dt,\\
 A&=k_1V^2g^{-4}+k_0Vg^{-3}+k_2 F_0 q a^{-5}g^{-8}.
 \end{aligned}
$$
The three terms in $A$ come from $D^2f[x',x']$ on fast modes,
$Df\,x'$ on slow modes and $Df\,F_{\rm st}$ on fast modes.
The remaining $Df(x''-F_{\rm st})$ is the integral feedback above.
All sums are absolutely bounded on the exterior by the displayed
geometric factors. Equivalently, eliminating $y$ with the cosine formula
defines a causal, locally Lipschitz integral equation on exterior
position and velocity histories. To initialize from the free asymptote,
on a far incoming tail take $|x|\ge |s|/2$ and $|x'|\le2$.
The cosine formula gives $|y_{\ell\nu}|=O(|s|^{-\ell-1})$ uniformly
in $\nu$ for each $\ell$. In the norm used for $D$, the difference of
the forces for two such histories near the free line is bounded by a
constant times $|s|^{-5}D(s)$, using the same first-derivative and
Hessian estimates and summing the exterior geometric factors.
The twice-integrated map is a contraction sufficiently far in the past.
Local continuation applies while the orbit stays exterior.

Write $I_j=\int_{\mathbb R}g^{-j}ds$. Here $I_2=\pi$, $I_3=2$,
$I_4=\pi/2$, $I_5=4/3$, $I_6=3\pi/8$ and $I_8=5\pi/16$.
The integrating factor bound for $K$ is $\exp(q k_2 I_6)$.
An even nonnegative function integrated against the running integral
from $-\infty$ of another even function gives half the product of their
full integrals. Apply this to the bounds $g^{-2}$ or $g^{-3}$ and $A$,
even when the orbit itself is asymmetric. On every interval where
$D\le0.028$ this gives
$$
 \begin{aligned}
 \int gL\,ds&\le q B_{\rm lag},\qquad
 \int L\,ds\le (2/\pi)q B_{\rm lag},\\
 B_{\rm lag}&=\tfrac{\pi}{2}e^{q k_2 I_6}
       (k_1V^2 I_4+k_0 V I_3+k_2 F_0 q a^{-5} I_8)<1.15 .
 \end{aligned}
$$
For example $qk_2 I_6<0.0025$. Integrating the difference of the
two orbit equations with $|s-t|/g(s)\le g(t)$ gives
$D(s)\le q B_{\rm lag}+\int_{-\infty}^s12q a^{-6}g(t)^{-4}D(t)\,dt$.
Grönwall gives $D\le q B_{\rm lag}\exp(12q a^{-6}I_4)<1.67q<0.028$,
closing the estimate throughout the flyby. In particular the charge
stays at physical radius at least $0.96b>0.67$ nm.
[Newton stability argument, Eq. (10)](balaban-ode-lesson.md)
(integral Grönwall inequality).

A final integration of the velocity equation uses the stronger
unweighted lag bound and gives
$$
 |x'(+\infty)-X'(+\infty)|
 \le q[(2/\pi)B_{\rm lag}+12 a^{-6} I_5\sup D]<1.26q .
$$
The reference outgoing speed is one. A ball of radius $1.26q$ about
that velocity subtends an angle of at most $\arcsin(1.26q)<1.261q$.
Hence the actual angle is at least $(3\pi/4-1.261)q>0.0133$ rad.

If the equilibrium work alone gave $U\le0.01$, the clocked dipole
reading would suffice. Apply the slow-mode estimate to every higher
degree regardless of frequency. Its total weight together with the
slow dipole is at most $U+10d_1\le0.011$. Only the fast dipole
contributes to $\Lambda$, giving $\Lambda<0.0213$ and $B_{\rm lag}<1.12$.
The same angular conclusion follows. The tabulated quadrupole alone
exceeds that one-percent work allowance for argon.

**The transmitted count.** In the first tenth of the cell the aperture
and the stated angular tolerance give $D_{\rm exit}/(0.9L)+0.004
<0.0128$ rad, with $D_{\rm exit}=2$ mm and $L=255$ mm.
The annulus has area $\pi(0.72^2-0.70^2)$ nm$^2$, or $8.92$ square
ångströms. The same two $0.25$ mm radius stops separated by $255$ mm
can use gates $0.737$ microseconds apart, each of half-width $3$ ns.
Their on-axis flight times $0.731$–$0.743$ microseconds select energies
inside the declared band for a stationary atom. The free charge may
emerge with a different speed. Count the entire exit pulse and include
target motion, alignment, timing tails, beam fluence and detector
efficiency in the independently calibrated good fraction $f$ and gain
area $G$ defined above. The dilute loss again obeys $Y\ge fA-G$.
For example $f\ge0.08$ and $G\le0.10$ square ångströms would give
$Y>0.61$ square ångströms. The published $0.318$ square ångströms at
$0.34$ eV motivates this comparison. Neither the two material readings
nor the guarded transmission for this preparation has been established
by those data. No mathematical time step or quantum action enters
the prediction. Its failure would test the specified material dynamics
and preparation. The inference about a radial characteristic below
requires elastic central motion.

### Action discrepancy for an elastic central branch

Return here to the elastic $0.55$–$0.60$ nm annulus and its original
energy and acceptance bands.
For a deterministic elastic central branch use its radial characteristic
$W_E(J)$ with the free contribution subtracted and angular momentum
$J=p b$. Hamilton's deflection identity gives
$|(W_E-\widetilde W_E)'(J)|=|\chi-\widetilde\chi|$ with a common sign
and continuous winding convention. This is also the integrated scattering
function of [Hendi et al., Eq. (3)](https://arxiv.org/pdf/cond-mat/0605637)
(passage, with $p\,db=dJ$). Suppose an alternative branch reproduces
$Y\le Y_{\rm hi}$ under the same preparation and detector calibrations.
The mean area in the annulus on which its deflection is within $\theta$
of forward, modulo a full turn, is at least $[A-(Y_{\rm hi}+G)/f]_+$,
where $f>0$ and $[x]_+=\max(x,0)$. Indeed, every ray from the
complement in the good exposure would leave the aperture. On the
near-forward rays the angle error has magnitude at least
$\chi_*-\theta$, with $\chi_*=0.026$ rad. Integrating over $J$, using
$2\pi b\,db\le 2\pi b_2\,db$, yields
$$
 \int {\rm Var}_{[pb_1,pb_2]}(W_E-\widetilde W_E)\,P(dE)
 \ \ge\
 \frac{p_{\min}(\chi_*-\theta)}{2\pi b_2}
 \left[A-\frac{Y_{\rm hi}+G}{f}\right]_+ .
$$
Here $p_{\min}=\sqrt{2\mu E_{\min}}$ and $\operatorname{Var}$ is total
variation in angular momentum. Additive action constants cancel. With the
trial numbers $f=1/2$, $G=0$, $Y_{\rm hi}=0.40$ square ångströms this
exceeds $7\,10^{-38}$ J s. This bounds a change in the mechanical
scattering characteristic. A different classical force can produce such
a change. The inequality assigns no quantum of action to it.

**Why the finite-radius premise matters.** The smooth Newton potentials
$V_R(r)=-C_4/(r^2+R^2)^2$ have the same measured asymptotic coefficient
for every $R>0$. In the preceding quadrature
$B\le 2C_4/(ER^4)=\zeta$ at every radius. For $\zeta<1$ all
$b>0$ scatter with $0\le\chi\le\pi\zeta/(1-\zeta)$, and the head-on
ray crosses the regular centre along a straight line. Choosing $R$
large enough puts every deflection below any fixed positive angular
resolution, uniformly on the specified energy band. This gives a
classical countermodel to inferring a resolvable deflection from
static polarizability alone. The finite-radius and encounter-time
force calibration would exclude it. An action-dependent theory that
recovers the calibrated Newton loss as its action tends to zero would
then exclude an entire neighbourhood of zero if the measured deficit
exceeded its errors. The reported attenuations alone establish neither
that calibration nor a universal physical $\hbar$.

### Three work readings and the low-energy limit

**6.1 Sol Max, 2026-11-18.** For an equilibrated spherical atom and a
distinguishable negative test charge, the electrostatic binding energy
is convex in inverse distance. This allows three work readings to bound
the turn of an entire annulus without reconstructing a radial force or
truncating a multipole series. If the equilibrium potential has the
measured dipole coefficient in its asymptotic tail, the annulus can move
outward as the collision energy falls. The resulting low-energy
observable is the rate coefficient $vQ_{\rm mt}$, where $Q_{\rm mt}$
weights each elastic collision by the fraction of incident longitudinal
momentum it transfers.

**Why charge penetration has a sign.** Fix a point nucleus of charge
$+Ze$, a projectile of charge $-e$ with $e>0$, and
$\kappa=e^2/(4\pi\epsilon_0)$. A trial state $a$ of the target has
internal energy $H_a$, mobile electron number measure $n_a\ge0$ of mass
$Z$, and energy at clamped probe position $\mathbf R$
$$
 H_a-E_0-\frac{Z\kappa}{|\mathbf R|}
       +\kappa\int\frac{dn_a(x)}{|\mathbf R-x|}.
$$
Take the infimum over the same rotationally invariant family of states
at every $\mathbf R$, with $E_0$ the isolated minimum. Assume this
equilibrium work $W(r)$ is finite and continuous for $r>0$ and tends to
zero at infinity. An unpolarized spherical minimizing state gives
$W(r)\le0$ by the shell theorem. For a sphere of radius $d<|\mathbf R|$
centred at $\mathbf R$, the nuclear term has its centre value as its
average. Each repulsive electron kernel averages to
$1/\max(d,|\mathbf R-x|)$, at most its centre value, including for
electrons inside the averaging sphere. Every trial energy at the centre
therefore dominates the average of $W$ over that sphere. Taking the
infimum at the centre gives $\Delta W\le0$ in distributions. In radial
coordinates this is precisely convexity of $-W(1/u)$ in $u>0$.
Its value at $u=0$ is zero and it is nonnegative, so it is nondecreasing.
The sign uses a negative probe and negative mobile charges. Exchange
with the probe, magnetic forces and delayed relaxation are separate
physical assumptions. Newton's shell theorem applies to each frozen
state even when the minimum responds nonlinearly.
[Motte 1729, Book I, Section XII, Propositions LXX–LXXI](https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_%281729%29/Book_1/Section_12)
(passages). The variational treatment of an external potential also
applies to electronic ground-state energies. The sign argument itself
requires no quantum state law. [Lieb (1983)](https://doi.org/10.1002/qua.560240302)
(abstract, variational background).

**A finite preparation.** Choose an independently fixed length $\ell$
and relative kinetic energy $E=\mu v^2/2$. Write $u=\ell/r$ and
$w(u)=-W(\ell/u)/E$. Place the three clamped probes at dimensionless
inverse radii $u_A,u_B,u_C$ within $0.001$ of $0.65,0.75,0.80$,
respectively, on separate preparations of the same atom. Take as
independent readings
$$
 w(u_A)\ge0.17,\qquad w(u_B)\le0.35,\qquad
 w(u_C)-w(u_B)\le0.105 .
$$
For elastic motion in $W$, every impact radius
$2.41\le b^2/\ell^2\le2.75$ then gives a turn between $0.156$ and
$2.94$ rad. The calibration requires two works relative to infinity
and one work difference. A smooth exterior potential suffices for the
ordinary Newton orbit used here.

Indeed, at a turning point $u$ one has $b^2/\ell^2=(1+w(u))/u^2$.
This expression is above $2.75$ at $u_A$ and below $2.41$ at $u_B$.
For any intervening root put $t=r_{\min}/r$. The central-orbit
quadrature gives the angular advance from infinity to that root as
$$
 \Phi=\int_0^1\frac{(1-P(t))^{-1/2}}{\sqrt{1-t^2}}\,dt,\qquad
 P(t)=\frac{w(u)-w(tu)}{(1+w(u))(1-t^2)},\qquad \chi=2\Phi-\pi .
$$
Convexity gives $w(tu)\le t w(u)$. The integrand is thus at least that
of a Coulomb orbit with the same turning radius and binding energy.
Its deflection is $2\arcsin(w(u)/(2+w(u)))>0.156$. For the upper
bound every slope up to $u_B$ is at most $0.105/0.048$. For $t\le0.7$
use $P\le(0.35/1.35)/(1-0.7^2)$. For $t\ge0.7$ use
$P\le0.751(0.105/0.048)/(1.17\cdot1.7)$. In particular $P<1$
everywhere, so the incoming orbit reaches the root and turns there.
The respective factors $(1-P)^{-1/2}$ are below $1.43$ and $2.42$.
Thus $\Phi<1.43\arcsin(0.7)+2.42(\pi/2-\arcsin(0.7))<3.04$,
which excludes a full turn back into the aperture.
[Hendi et al., Eqs. (1)–(4)](https://arxiv.org/pdf/cond-mat/0605637)
(central-orbit quadrature) and [the Coulomb deflection formula used above](#a-three-energy-test-of-central-force-trajectories).

For example take $\ell=(C_*/E_*)^{1/4}\simeq0.315$ nm with the fixed
references $C_*=1.18\,10^{-3}$ eV nm$^4$ and $E_*=0.120$ eV. The
work stations are about $0.484$, $0.420$ and $0.394$ nm from the
nucleus. Over $0.118\le E\le0.122$ eV the three inequalities follow
from binding work at A of at least $20.74$ meV, binding work at B of at
most $41.30$ meV, and an increase from B to C of at most $12.39$ meV,
including measurement uncertainties. The annulus area is
$0.34\pi\ell^2>10.5$ square ångströms. The two upstream stops specified
above can use gates $1.240$ microseconds apart with $2$ ns half-widths
over $255$ mm. The admitted on-axis flight times select electrons
inside the stated energy band for stationary argon. With the upstream-half acceptance of
$0.020$ rad, good fraction $f\ge1/4$ and gain $G\le0.20$ square
ångströms, the loss would exceed $2.42$ square ångströms. Buckman and
Lohmann report $1.037$ square ångströms at $0.12$ eV with a $6.4\%$
relative standard deviation. They did not measure these three works or
the guarded counts. The adiabatic identification of the work gradient
with the force in a free encounter is also required at this energy.
[Buckman and Lohmann, Table 2 and §§2–4](https://doi.org/10.1088/0022-3700/19/16/013)
(data and apparatus passages).

**The outward annulus.** Now vary $E$, set $\ell_E=(C_4/E)^{1/4}$ and
assume the physical work obeys $r^4W(r)\to-C_4<0$. This is an
asymptotic material premise. For instance the bare interaction of a
spherical neutral cloud contributes $o(r^{-4})$ if its third radial
moment is finite. Its magnitude is then at most
$\kappa r^{-4}\int_{|x|>r}|x|^3\,dn_0(x)$. The induced response must
still give the stated coefficient. The weak uniform-field
polarizability by itself sets no finite onset radius. The scaled work
$w_E(u)=-W(\ell_E/u)/E$ tends to $u^4$ uniformly on bounded $u$ intervals.
All three preceding work inequalities eventually hold. For a stronger
momentum bound take turning radii with $m=u^4\in[1/4,0.64]$. In this
limit the quadrature becomes
$$
 b^2/\ell_E^2=m^{-1/2}+m^{1/2},\qquad
 \chi(m)=2\sqrt{1+m}\int_0^{\pi/2}(1-m\sin^2 z)^{-1/2}\,dz-\pi .
$$
The passage to this formula is uniform on the stated annulus. Away from
$t=1$ it follows from uniform work convergence. Near $t=1$ the
secants of the convex $w_E$ on either side bound its slopes, which
therefore converge uniformly to $4u^3$ on compact positive $u$
intervals. Thus $P$ stays uniformly below one there (its limiting
maximum is $2m/(1+m)$). The integrable majorant is a constant times
$(1-t^2)^{-1/2}$. The turning points are accessible from infinity.
The inverse-fourth-power scaling is classical Langevin physics. The
orbits used here stay outside the capture region.
[Grier et al., p. 1](https://arxiv.org/pdf/0808.3620) (capture
calculation, with twice the present convention for $C_4$).

At $m=1/4$ Jensen's inequality gives a turn at least
$\pi(\sqrt{1.25/(1-0.25/2)}-1)>0.61$. At $m=0.64$ the chord bound
for the convex integrand as a function of $\sin^2 z$ gives an upper
angle $\pi(\sqrt{1.64}(1+1/\sqrt{1-0.64})/2-1)<2.23$.
The angle increases with $m$ in this formula, and the annulus area
divided by $\ell_E^2$ tends to $0.45\pi$. For elastic scattering define
$Q_{\rm mt}(E)=2\pi\int_0^\infty(1-\cos\chi)\,b\,db$. Then
$$
 \liminf_{E\downarrow0}vQ_{\rm mt}(E)
 \ \ge\ 0.45\pi(1-\cos 0.61)\sqrt{2C_4/\mu}
 \ >\ 0.25\sqrt{2C_4/\mu}.
$$
Only the outgoing annulus is needed in the integral. If a ray is
captured, counting its full incident longitudinal momentum gives an
additional nonnegative contribution. The last rate is about
$5.1\,10^{-15}$ m$^3$/s for the nominal argon coefficient. Meanwhile
the incoming angular momenta are proportional to
$\sqrt{2\mu}\,C_4^{1/4}E^{1/4}$ and tend to zero. These two limits
refer to the same rays. Inserting additional mathematical times changes
neither.

The quiet reciprocal oscillator model above also reaches this threshold
along its **freely moving** paths. It needs no lower bound on mode
frequencies. In the earlier orbit variables compare with the *pure*
static dipole orbit $X$, taking $s=0$ at its turn. Here $q<0.24$ and
$(|X|^2/2)''=1-q/|X|^4\ge1-0.64$. Thus $|X|\ge0.6g(s)$ and
$|X'|\le\sqrt{1.64}$. While $D\le0.1$ the previous lag estimate
applies with $a=0.5$ and $V=1.4$. Put $z=(r_1/(ba))^2$, where
$U=\sum_{\ell\ge2}w_\ell$ at the fixed $r_1$ is finite.
As $E\downarrow0$, $z\to0$ and the static higher forces are bounded by
$3q a^{-5}Uz\,g^{-5}$. Use the slow-mode bound for every higher degree
and for dipole frequencies up to a fixed $\nu_c>0$. The squared
first-derivative factor for degree $\ell\ge2$ is at most
$(\ell+1)^2z^{\ell-1}/4\le3z$ once $z\le0.36$. Thus in the displayed
$B_{\rm lag}$ bound take $S=P_1((0,\nu_c])+3Uz$ and
$\Lambda=v/(b\nu_c)$. The static force and derivative constants $2.3$
and $12$ apply for sufficiently small $Uz,z$. Adding the static
higher-force integral gives
$$
 D\le q(B_{\rm lag}+3a^{-5}Uz I_4)\exp(12q a^{-6}I_4).
$$
First choose $\nu_c$ so that the slow dipole weight is arbitrarily
small, then lower $E$ so that $z$ and $\Lambda$ are small. The bound
closes $D<0.1$ and tends to zero uniformly on the annulus. The outgoing
velocities converge to the elastic reference velocities. The annular
rate bound persists for the angular moment, and for longitudinal
momentum transfer when other events have nonnegative mean loss. This
two-limit proof supplies no numerical crossover energy for real argon.

**Can finite data locate the onset?** A spherical shell of negative
charge $-Ze$ and radius $a$ can move by a vector of length at most
$d<a$ relative to its fixed positive nucleus, at elastic cost $ks^2/2$
for displacement $s$. At $r>a+d$ its minimizing displacement points
away from the probe. Its work is exactly
$$
 W_d(r)=\min_{0\le s\le d}\left\{\tfrac12ks^2+
 Z\kappa[(r+s)^{-1}-r^{-1}]\right\}.
$$
Every $d>0$ gives the same weak uniform-field polarizability
$(Ze)^2/k$ and the same $C_4=(Z\kappa)^2/(2k)$ since the minimizing
$s$ at large $r$ is asymptotic to $Z\kappa/(kr^2)$. Yet on any fixed
exterior radius band $0\le W'_d(r)\le2Z\kappa d/r^3$. A sufficiently
small $d$ makes the force arbitrarily weak on that band. The onset of
the threshold prediction is not uniform over targets with the same
measured polarizability. A support mass and an elastic displacement
stop give a classical mechanical realization.

The clocked observable for a velocity-selected beam is the loss of mean
longitudinal momentum per unit target column, divided by incident
momentum, with the angular acceptance and missing output included in
its errors. It yields $Q_{\rm mt}$ in elastic single-atom scattering.
To approach the threshold one must keep the target spacing and cell
dimensions large compared with $\ell_E$, use enough flight time to
resolve the relative speed, and control the target velocity spread.
At fixed nonzero target temperature a beam slowed to rest in the
laboratory samples a distribution of relative energies.
Milloy et al. give $Q_{\rm mt}=3.88$ square ångströms at $0.014$ eV,
fitting drift and diffusion measurements with quantum phase shifts
below $0.32$ eV. A finite scattering length in that fit gives
$vQ_{\rm mt}\to0$. Inferring an action scale from this extrapolation
would import the dynamics being tested.
[Milloy et al., §4 and Tables 1–2](https://www.publish.csiro.au/ph/pdf/PH770061)
(method and data passages) and [O'Malley, Rosenberg and Spruch (1962)](https://doi.org/10.1103/PhysRev.125.1300)
(abstract, polarization threshold theory).

**A finite current readout.** Prepare two dilute electron samples and
neutral targets with independently checked Maxwell velocities at the
same temperature $T$. Give the electrons opposite finite velocity
increments $\pm U\hat z$, keeping the target preparation the same.
Turn off the drive and measure both mean longitudinal velocities over
the same flight interval $\Delta t$. Let $D_n(t)$ be half their
difference at target number density $n$, so $D_n(0)=U$. After
empty-cell subtraction take the dilute slope
$$
 {\cal R}(T,U)=-\frac{1}{U\Delta t}
 \left.\frac{d}{dn}\big[D_n(\Delta t)-D_n(0)\big]\right|_{n=0}.
$$
Use completed, independent binary encounters in a homogeneous sample
and count the entire velocity distribution. In binary kinetics an
elastic encounter of relative velocity $\mathbf g$ changes the
electron velocity by $(\mu/m_e)(\mathbf g'-\mathbf g)$. The angular
integral of that change per unit time and density is
$-(\mu/m_e)\mathbf g\,gQ_{\rm mt}$. At first order in density the
field-free incident distributions stay fixed in the collision integral
over the gate. The drifted-Maxwell momentum-transfer law and its
constant rate for an exact inverse-speed cross section are established.
[Pinto and Galli, Eqs. (2)–(8) and case (b) after Eq. (16)](https://arxiv.org/pdf/0804.2856)
(binary elastic force, velocity average and polarization law).

Let $f_T(\mathbf g)$ be the centered, normalized Maxwell density of the
relative velocity with component variance $k_BT/\mu$. The two prepared
currents measure the positive average
$$
 \begin{aligned}
 {\cal R}(T,U)&=\frac{\mu}{m_e}\int gQ_{\rm mt}(\mu g^2/2)\,dP_{T,U},\\
 dP_{T,U}&=\frac{g_z}{2U}
 [f_T(\mathbf g-U\hat z)-f_T(\mathbf g+U\hat z)]\,d^3g .
 \end{aligned}
$$
The bracket has the sign of $g_z$ and the two means differ by $2U$,
so the weight is nonnegative and integrates to one at finite boost.
For any independently calibrated energy band on which $vQ_{\rm mt}\ge K$,
the raw readout therefore obeys $\mathcal R\ge(\mu/m_e)K P_{T,U}({\rm band})$.
For $U=\lambda\sqrt{k_BT/\mu}$ with fixed $\lambda>0$ the weight
concentrates at zero speed as $T$ falls. The same positive lower
rate consequently survives the thermal average with factor $\mu/m_e$.
A bounded low-energy cross section instead gives a vanishing rate if
the high-energy contribution vanishes on each fixed positive-energy
tail, as it does for polynomially bounded cross sections with these
Maxwell preparations.

For scale, a $1$ ns electric pulse with time integral
$m_eU/e\simeq5.7\,10^{-8}$ V s/m supplies $U=10^4$ m/s. In a
$10$ mm sensing region at $90$ K, use identical $50$ ps current gates
centred $1$ ns apart after switch-off. At first order in density the
current is affine in field-free time, so averaging in these equal
gates preserves its difference. The pulse, actual
relative speed distribution, field uniformity, drift during the gates,
detector response and losses at the boundaries need calibration. At
each energy the gate must encompass the binary encounter and the dilute
slope must resolve single collisions. Along a threshold sequence the
encounter duration grows as $\ell_E/v$ and the density must allow
$n\ell_E^3\ll1$. A fixed clock resolution permits longer gates.
Robertson's electron drift velocities at $89.6$ and $293$ K are
steady-field measurements. The opposite-boost, field-free decay is a
different measurement and would test the lower bound without an
inversion for phase shifts. [Robertson, Table 1 and §3](https://www.publish.csiro.au/ph/pdf/PH770039)
(instrument and drift data passages).

There is already a measurement of the **initial decay**. McPherson
excited the electron cyclotron motion with a $2.8$ GHz microwave pulse
and measured the decay of the emitted field. His lowest-speed row,
labelled $1.50\,10^5$ m/s, gives $(4.07^{+0.42}_{-0.41})\,10^4$
s$^{-1}$ after residual subtraction, normalized to $10^{-3}$ Torr at
$273.15$ K. At that reference pressure and temperature
$n_{\rm ref}=p/(k_BT_{\rm ref})=3.54\,10^{19}$ m$^{-3}$. The measured
decay per density is $1.15\,10^{-15}$ m$^3$/s, with reported upper
value below $1.28\,10^{-15}$ m$^3$/s. This calculation uses the
measured envelope slope, before the inversion for monoenergetic
collision frequencies. [McPherson, 1974 thesis, pp. 53, 59–62, Table 1](https://repository.gatech.edu/bitstreams/b6e6ee45-e4b3-49d9-b1a8-492a589e7bee/download)
(apparatus, slope and data passages) and
[McPherson, Feeney and Hooper (1976)](https://doi.org/10.1103/PhysRevA.13.167)
(abstract, published experiment).

To compare that slope with the bound, demodulate in the rotating
frame and assume that magnetic bending during a single encounter is
negligible and residual dephasing is controlled. For an isotropic
target the one-boost longitudinal collision integral equals the
opposite-boost difference by reflection. If $U(x)$ varies across the
waveguide and the detected initial current is in phase, weighting each
local $P_{T,|U(x)|}$ by its nonnegative contribution to the initial
signal gives a probability $P_{\rm eff}$. The initial logarithmic
decay then measures exactly the same positive average to binary order.
A rate $vQ_{\rm mt}\ge5.0\,10^{-15}$ m$^3$/s **certified on a finite
energy band** carrying at least $26\%$ of this weight would exceed the
reported upper value, allowing a further receiver error equal to the
remaining margin. The asymptotic bound does not specify that band.
The thesis assigned its absolute speed scale by matching the unfolded
minimum to Golden's earlier argon result and discussed the thermal and
waveguide averaging. Thus the small decay is an experimental datum,
while the overlap with a calibrated band remains to be established.
[McPherson, pp. 53, 67–82, 95](https://repository.gatech.edu/bitstreams/b6e6ee45-e4b3-49d9-b1a8-492a589e7bee/download)
(energy calibration and averaging passages).

One sufficient overlap test uses a velocity moment. The weight
$P_{T,U}$ has mean relative energy
$\mu U^2/2+5k_BT/2$, by the third moments of the shifted Maxwell
distributions. If the certified band extends from zero to $E_c$,
its weight is at least $[1-(\mu U^2/2+5k_BT/2)/E_c]_+$.
For the waveguide use the initial-signal-weighted mean of $U(x)^2$.
For the separately specified $90$ K, $10^4$ m/s preparation the mean
is below $19.7$ meV, so calibration through $27$ meV would cover more
than $26\%$. Those settings cannot be substituted for the 1974 pulse.

There is also an upper limit on what calibrating the pulse speed could
accomplish. For the prepared Maxwell distributions, completing the
square gives the Laplace transform of $E=\mu g^2/2$,
$$
 \int e^{-sE}\,dP_{T,U}
 =(1+s k_BT)^{-5/2}
 \exp\!\left[-\frac{s\mu U^2}{2(1+s k_BT)}\right].
$$
The first factor is the transform of a gamma law of shape $5/2$ and
scale $k_BT$. The second is a compound Poisson law with exponential
jumps of mean $k_BT$ and mean jump count $\mu U^2/(2k_BT)$. Convolution
and positive mixing over the waveguide cannot increase the maximum
density of the first law, which is less than $0.31/(k_BT)$. Thus if
the electrons and gas were at the sample's $303$ K (thesis, Appendix
VII), the $0.118$–$0.122$ eV band above would carry less than $4.8\%$
of the signal at **any** pulse amplitude. A force calibration confined
to that band could not meet the $26\%$ test. The thesis lists electron
thermal speed among the quantities it did not directly measure
(pp. 92–93).

The order of the energy and action limits matters. For a supplied
reduced action $h$, the exterior Schrödinger equation in units of
$\ell_E$ and $E$ has kinetic coefficient
$[h/(\sqrt{2\mu E}\,\ell_E)]^2$. With $J_*=\sqrt{2\mu E_*}\,\ell_{E_*}$
the schedule $E/E_*=(h/J_*)^4$ keeps this coefficient equal to one
while $h$ and $E$ tend to zero. The core boundary condition, clocked
preparation and readout still enter the measured rate. A finite discrepancy at a **fixed**
calibrated energy would exclude a neighbourhood of zero in any trial
family proved to recover this Newtonian readout there as $h\to0$.
The fitted zero-energy law supplies neither that finite discrepancy
nor a value of physical $\hbar$.

### A thermal test with two shutters

**6.1 Sol Max, 2026-11-18.** Pack and Phelps timed electrons between
two shutters in argon. At $77$ K and reduced electric field
$|\mathcal E|/n=6.25\,10^{-25}$ V m$^2$ their drift speed was
$36$ m/s. At $7.81\,10^{-25}$ V m$^2$ it was $44$ m/s. Here $n$ is
the neutral number density. Dutton attributes these rows to experiment
and the lowest-field row to a calculation. An older thermal microwave
determination reports an inferred argon collision probability, while its
displayed cavity ratios are for nitrogen. The shutter times provide a
comparison independent of the energy assigned to the Ramsauer minimum.
[Pack and Phelps (1961)](https://doi.org/10.1103/PhysRev.121.798)
(abstract, timing method), [Dutton, Table 1.6(b), p. 613](https://srd.nist.gov/jpcrdreprint/1.555525.pdf#page=38)
(tabulated Pack–Phelps measurements), and
[Phelps, Fundingsland and Brown, MIT report 211, pp. 6–8](https://hdl.handle.net/1721.1/4853)
(readout and preliminary argon result).

**Which mechanical measurement would decide the comparison?** Write
$B(r)=-V(r)>0$ for the binding work of the *moving* pair in the
elastic central model, with $B(\infty)=0$, and set
$p(r)=-d\log B/d\log r$. Fix $r_0=0.40$ nm and the dielectric
$C_4=1.18\,10^{-3}$ eV nm$^4$ measured above. Test the exterior laws
$$
 B(r)\ge 0.8 C_4/r^4,\qquad 7/2\le p(r)\le 9/2
 \quad(r\ge r_0).
$$
The slope is $rV'(r)/B(r)$. Thus work and the initial inward
displacement of a relative coordinate released from rest would
measure its denominator and numerator independently. The latter is
the force observable in Newton's 1713 Lemma X, Corollary 4, with the
reduced mass, clock and finite displacement error retained.
[Edition comparison and finite readout](newton-insertion-action.md#lemma-x-and-the-measurement-of-initial-force).

These tolerances admit higher multipoles. For the earlier confined
linear target with $B=\sum_{\ell\ge1}c_\ell/r^{2\ell+2}$ and
$c_\ell\ge0$, they have a finite test. The slope is the weighted
mean of $2\ell+2$ and its derivative in $\log r$ is minus the
variance. For a series convergent in a neighbourhood of
$r_a=0.36$ nm, it suffices to measure
$$
 B(r_a)/B(r_0)\le(r_0/r_a)^{9/2}\simeq1.607 .
$$
Indeed, the log secant majorizes every $p(r)$ outside $r_0$, and
$c_1=C_4$ supplies the lower work and slope. The first three Jiang
coefficients quoted above give a ratio about $1.56$ when truncated.
They do not bound the omitted response. Applying two static works to
a free electron requires independent control of the material response
during passage. A penetrating, nonlinear or delayed target need not
have this positive series.

**An exterior rate at every energy.** Set $E_c=50$ meV,
$K_*=\sqrt{2C_4/\mu}$ (units m$^3$/s), and $x=E/E_c$.
For every $E>0$ a subset of the escaping elastic trajectories has rate
$$
 K_A(E)=g\int_A(1-\cos\chi)\,d\sigma \ \ge\ K_*\,c(E),\qquad
 c(E)=\begin{cases}0.27,& x\le1,\\0.15\,x^{-3/2},&x>1.\end{cases}
$$
Here $g=\sqrt{2E/\mu}$ and $d\sigma$ is the impact-area measure.
The high-energy bound is needed since weakly scattered electrons can
contribute disproportionately to the drift.

Use $E_b=\min(E,E_c)$, $y=E/E_b$ and $\ell_b=(C_4/E_b)^{1/4}$.
Label the turning radius by $s=B(r)/E_b$. Take four adjacent intervals
with endpoints $0.16,0.25,0.36,0.49,0.64$. They all lie beyond
$r_0$, since $B(r_0)\ge36.8$ meV and $0.64E_b\le32$ meV.
At the turn $b^2=r^2(1+s/y)$, and
$$
 -\ell_b^{-2}\frac{db^2}{ds}
 =\frac{r^2}{\ell_b^2}
 \left[\frac{2}{p s}+\frac{2/p-1}{y}\right]
 \ge\sqrt{0.8/s}\left[\frac{4}{9s}-\frac59\right].
$$
The right side is positive up to $s=0.64$, including the path in
from infinity. On the four intervals its integrals exceed
$\sqrt{0.8}$ times $0.333,0.185,0.100,0.047$, respectively.
For the angle quadrature above put $t=r_{\min}/r$ and
$k=s/(y+s)$. The work at radius $r_{\min}/t$ is between
$t^{9/2}$ and $t^{7/2}$ times the turning work. Hence $P(t)$ is
between $k(1+3t^2/4)$ and $k(1+5t^2/4)$. These chord bounds
follow by writing $(1-z^a)/(1-z)$ as the mean of $a u^{a-1}$ on
$[z,1]$, with $z=t^2$ and $a=7/4,9/4$. Jensen's lower bound and the
upper chord for $(1-P)^{-1/2}$ give
$$
 \frac{1}{\sqrt{1-11k/8}}
 \ \le\ 1+\frac{\chi}{\pi}
 \ \le\ \tfrac12\left[(1-k)^{-1/2}+(1-9k/4)^{-1/2}\right].
$$
Here $k\le0.64/1.64$ keeps $\chi<3.4$ rad. At $y=1$ the lower
angles exceed $0.34,0.54,0.79,1.10$ rad. At $y\ge1$ they exceed
$0.29,0.43,0.57,0.70$ rad divided by $y$, using
$\chi\ge(11\pi/16)s/[(1+s)y]$. For each of these lower angles $u$,
$1-\cos(u/y)\ge(1-\cos u)/y^2$. The upper angle stays far enough
from a full turn for the same lower bound on the loss. Multiplying
the four area bounds by their angular losses and by
$\pi g\ell_b^2=\pi K_*\sqrt y$ gives the two stated constants.
The potential inside $r_0$ does not enter the calculation.

**Carrying the orbits through a finite measuring field.** Use dilute
independent binary encounters, a spatially homogeneous stationary
electron distribution $f$, and Maxwell target velocities at temperature
$T$ in the gas frame. Other collision channels may be included if
they conserve the electron population and have nonnegative entropy
dissipation relative to the same thermal equilibrium. Orient $z$ along
the electric force, write $v_d\ge0$ for the electron drift, and average
over independent electron and target velocities. With
$\mathbf g=\mathbf v_e-\mathbf v_a$ the finite-field test is
$$
 K_*\frac{\mu}{e}\frac{v_d}{|\mathcal E|/n}
 \ \le\ \mathcal B_f,\qquad
 \mathcal B_f=\left\langle\frac{\mu}{k_BT c(E)}
 \max\!\left(g_z^2,\frac{g_x^2+g_y^2}{2}\right)\right\rangle_f .
$$
This dimensionless velocity moment can be measured independently
of the scattering data. It includes the fast tail. A mean energy
alone would leave its fifth-power speed weight unbounded.

To see why finite target recoil is included, scale the electron and
relative velocities to unit thermal component variance,
$X=\sqrt{m_e/(k_BT)}\,\mathbf v_e$ and
$G=\sqrt{\mu/(k_BT)}\,\mathbf g$. In the equilibrium pair measure
$\mathbb E_0[G\mid X]=aX$, $a=\sqrt{\mu/m_e}$. Along a collision
the centre-of-mass velocity and $|G|$ are fixed. Put $h=f/f_0$,
where $f_0$ is the Maxwell electron density normalized to one.
For the annular collisions write
$$
 \mathcal D_A(u,w)=\tfrac12\,\mathbb E_0\int_A g\,d\sigma\,
                 (u'-u)(w'-w).
$$
The equilibrium incoming and outgoing measures agree by elastic time
reversal. The angular collision generator sends $\psi=G_z/K_A(E)$
to $-G_z$, so $\mathcal D_A(\psi,h)=a\langle X_z\rangle_f$.
The stationary entropy balance gives the total dissipation per density
as $e|\mathcal E|v_d/(n k_BT)$. It uses the field work and the usual
Maxwell detailed-balance identity, assuming finite dissipation and
no boundary entropy flux.
[Bisi, Cañizo and Lods, Eqs. (1.17)–(1.19), (3.2)](https://arxiv.org/pdf/1405.0366)
(reversible collision form; the mass factors here follow from the
elastic pair variables).

Cauchy–Schwarz with the logarithmic mean
$(h'-h)/(\log h'-\log h)\le(h+h')/2$ gives
$$
 a^2\langle X_z\rangle_f^2\ \le\
 \frac{e|\mathcal E|v_d}{n k_BT}\,
 \tfrac12\left\langle\int_A g\,d\sigma\,(\psi'-\psi)^2\right\rangle_f .
$$
In this last expectation the bath remains Maxwellian. At a fixed
$G$ the half angular integral is a convex combination
of $G_z^2/K_A$ and $(G_x^2+G_y^2)/(2K_A)$, because the azimuth is
uniform and the trace of the angular jump tensor for $G$ is
$2|G|^2K_A$. Substitution gives the finite-field test. The argument
permits truncation when the displayed integrals converge.

For the first measured shutter row the left side is about $6.67$,
using $\mu\simeq9.11\,10^{-31}$ kg and $K_*\simeq2.04\,10^{-14}$
m$^3$/s. At $77$ K a Maxwell relative law gives $\mathcal B_0<6.0$.
Its angular maximum has mean $(1+1/\sqrt3)/3$ on the unit sphere.
Weighting by $|G|^2/3$ gives the gamma energy law
$dP_T=t^{3/2}e^{-t}\,dt/\Gamma(5/2)$, $t=E/(k_BT)$. For
$z=E_c/(k_BT)>7.53$, the tail integral is
$$
 \int_{t>z}(t/z)^{3/2}\,dP_T
 =\frac{e^{-z}(z^3+3z^2+6z+6)}{\Gamma(5/2)z^{3/2}}<0.013 .
$$
Thus $\int dP_T/c(E)<1/0.27+0.013/0.15<3.80$ and the angular
maximum gives $\mathcal B_0<6.0$. If the driven laws approach
equilibrium with uniformly integrable fifth speed moments as the
field vanishes, averaging the angular combination *before* taking
its maximum gives $1/3$ for either component. The zero-field
density-normalized mobility is then at most
$3.80e/(\mu K_*)<3.3\,10^{25}$ (V m s)$^{-1}$. The two measured
finite-field ratios are $5.76\,10^{25}$ and $5.63\,10^{25}$ in
these units. For a comparison at finite field, an independently
bounded $\mathcal B_f\le6.2$ with a corrected measured left side above
$6.2$ would exclude the stated mechanical model at the actual field.
The shutter rows do not supply this velocity moment. Finite-field
heating, timing, wall losses, density and the exterior work remain
physical tests. The two measured mobilities are close at these
fields, but their agreement does not bound a rare fast tail.

**A field-free readout with fixed length and time resolution.** A
separate preparation eliminates the driven velocity moment. Release
an electron ensemble at a fixed origin with an independent Maxwell
velocity in a field-free uniform Maxwell gas at the same $T$. For the
reversible velocity process let $L$ be the nonnegative collision
operator per unit density, so the velocity semigroup is $e^{-ntL}$.
For an electron test function $u$, the same pair identity and ordinary
Cauchy–Schwarz give
$$
 a^2|\langle X_z,u\rangle_0|^2
 \le \left(\int dP_T/K_A\right)\langle u,Lu\rangle_0 .
$$
Indeed $\mathcal D_A(\psi,\psi)=\int dP_T/K_A$, and the other
reversible channels add nonnegative forms. The spectral representation
of the stationary velocity correlation then gives, for every finite
lag $\tau$,
$$
 \mathbb E[(z(\tau)-z(0))^2]
 \le \frac{2\tau k_BT}{n\mu K_*}\int\frac{dP_T}{c(E)} .
$$
Here the finite-time integral of $(\tau-s)e^{-ns\lambda}$ is at
most $\tau/(n\lambda)$ for each positive spectral value $\lambda$.
The form bound controls the inverse on the observed velocity,
without requiring a spectral gap.
[Pavliotis, §2, Eqs. (2.3)–(2.8)](../docs/Pavliotis_GreenKubo_2010.md)
(Green–Kubo and the Poisson equation). These steps use a stationary
Markov velocity law for completed independent encounters.

At $77$ K and $n=10^{23}$ m$^{-3}$ the coefficient multiplying
$2\tau$ is below $2.2$ m$^2$/s. Take the lag to be $1.000$
microsecond with an independent timing error at most $5$ ns, and bound
the rms initial longitudinal spread and final position error by
$10$ micrometres each. The observed rms displacement is then below
$2.13$ mm at the nominal material inputs. One may cap the squared
displacement at $(8\ {\rm mm})^2$ and score zero for an electron
absorbed at a wall or missing from the detector, normalizing to all
launches. This can only decrease the readout if a survivor follows
the field-free law until detection. The test uses the two masses,
$k_BT$, $C_4$, $r_0$, $E_c$, number density, and the stated length
and time calibrations. Preparation, fields, count backgrounds and
input uncertainties must enter the experimental bounds. Rhymes and
Crompton measured the cooling of the surviving population at absorbing
walls in argon. Their decay readout differs from the position moment
per launched electron used here.
[Rhymes and Crompton (1975), abstract and §1](https://doi.org/10.1071/PH750675)
(apparatus and boundary effect).

**Which small actions would a displacement excess exclude?** Take a
finite gas of $N$ distinguishable targets and one electron with a
supplied scalar Schrödinger dynamics. Keep this mechanical system fixed
as the trial reduced action $h$ varies. Mass-scale each position as
$q_i=\sqrt{m_i/m_e}\,x_i$ with conjugate momentum
$p_i^*=\sqrt{m_e/m_i}\,p_i$. Use the fixed units $L_*=1$ mm and
$\tau_*=1$ microsecond for $Q=q/L_*$, $P=p^*\tau_* /(m_e L_*)$,
and let $\epsilon=h\tau_* /(m_e L_*^2)$. The scaled Hamiltonian has
kinetic energy $|P|^2/2$. Suppose its potential has globally Lipschitz
gradient with dimensionless constant $\Lambda$; for a smooth physical
potential in the $q$ coordinates this can be taken to be
$(\tau_*^2/m_e)\sup\|\nabla_q^2 V\|$. This is a regular-core class.

Specify the initial classical phase-space law as a fixed probability
with finite second moments convolved with a centered Gaussian of
covariance $\sigma^2 I$ in the scaled coordinates. For example
$\sigma=10^{-3}$ corresponds to $1$ micrometre and $1$ m/s for the
electron. Include this variance within the prescribed thermal and
position spreads. For $\epsilon\le2\sigma^2$, use coherent packets of
variance $\epsilon/2$ in each scaled coordinate, mixing their centres
with the same probability convolved with the Gaussian of covariance
$(\sigma^2-\epsilon/2)I$. The Wigner law of the mixture is exactly the
fixed initial law for every such $h$. This specifies how the preparation
transforms. A single pure packet of adjustable physical size would
describe a different experiment. Coherent mixtures and their
quantum–classical quadratic cost are standard.
[Golse and Paul, §2, Definitions 2.1–2.2 and Theorem 2.4](https://arxiv.org/pdf/1510.06681)
(construction and estimates).

For clarity, pair each prepared packet with a classical initial point
drawn from its own Gaussian Wigner law. With $d=3(N+1)$ the combined
mean squared position and momentum error starts at $2d\epsilon$.
The Lipschitz packet estimate bounds this cost at time $t$ by
$2d\epsilon\exp[(1+\Lambda)t/\tau_*]$. In the drift substep its
derivative in scaled time is at most the cost, and in the kick substep
it is at most $\Lambda$ times the cost, by Cauchy–Schwarz for the full
position and momentum vectors. The same bound therefore holds against
the corresponding classical polygon on every partition, and passes
to the finite-time flow.
[Lipschitz lift, §§3–4](lipschitz-certificate-quantum-lift.md)
(product convergence and packet estimate). The final position map
$z\mapsto\min(|z|,8\ {\rm mm})$ is 1-Lipschitz. Coupling the
position outcome to the classical coordinate bounds the difference
of their rms readouts by $L_*\sqrt{2d\epsilon}\,
\exp[(1+\Lambda)t/(2\tau_*)]$. A position-dependent final detection
efficiency at most one only lowers the observed rms if missing counts
are scored zero. Earlier interactions with a detector or boundary
must be included in the dynamics or its error.

Let $\delta_{\rm gas}$ (length) bound any excess of the finite
classical gas over the binary-gas rms prediction at this preparation
and clock. If the experimental lower rms exceeds $2.13$ mm plus
$\delta_{\rm gas}$ and other input uncertainties by a length
$\delta>0$, the trial family obeys
$$
 h\ \ge\ \min\!\left\{
 \frac{2m_eL_*^2\sigma^2}{\tau_*},\
 \frac{m_e\delta^2}{2d\tau_*}
 e^{-(1+\Lambda)t_{\max}/\tau_*}\right\},
 \qquad t_{\max}=1.005\ {\rm microseconds}.
$$
Both terms have action units. The first sets the range of the common
preparation. The second follows from its readout. The finite-gas error
requires separate control of simultaneous encounters, boundaries and
the material response. No positive $\delta$ has been measured for this
preparation. The result supplies the small-action passage for the stated
regular system and leaves the independent physical necessity premise open.

## Helium pressure at three temperatures

**6.1 Sol Max, 2026-11-18.** In helium-3 the published second virial
coefficient at 3 K falls $6.244\ {\rm cm^3/mol}$ below the line between
the readings at 1.5 and 9 K when plotted against $1/T$. Every fixed
central pair potential for classical point atoms in thermal equilibrium
puts the middle reading on or above that line. This is a modern test
of what it means to reuse a force measured by Newton's Lemma X. A
displacement experiment determines force at a preparation. The further
premise here is that the same force acts at the same separation after
the gas is prepared at another temperature.
[Newton, 1713, Book I, Lemma X and Proposition VI](newton-insertion-action.md#lemma-x-and-the-measurement-of-initial-force)
(edition comparison and passages).

### A pressure inequality independent of the force profile

Let $\rho$ be molar density, $R_{\rm g}=N_Ak_B$ the molar gas constant,
$\beta=1/(k_BT)$ and $B(T)$ the coefficient of $\rho$ in
$p/(\rho R_{\rm g}T)=1+\rho B(T)+O(\rho^2)$. Take canonical
equilibrium, ordinary translational kinetic energy and a
temperature-independent pair potential $V(r)$ with a well-defined gas
branch and integrable Mayer functions at the three temperatures. The
classical second virial formula is
$$
 B_0(T)=\frac{N_A}{2}\int_{\mathbb R^3}
             [1-\exp(-\beta V(|\mathbf r|))]\,d^3\mathbf r .
$$
An impenetrable core is allowed. At each separation the integrand is
concave in $\beta$, including on the core. Hence for cold, middle and
warm temperatures with $\beta_m=w\beta_c+(1-w)\beta_w$,
$$
 \mathcal D[B]=w B(T_c)+(1-w)B(T_w)-B(T_m)\le0.
$$
The inequality survives pointwise limits of the three coefficients,
even for a succession of different core regularizations if each uses
one potential at all temperatures. It holds for repulsive and attractive
forces of arbitrary strength. For the established virial formula see
[Giese, Audette and York, Eqs. (6)–(9)](https://doi.org/10.1063/1.1587684)
(passage).

At $(T_c,T_m,T_w)=(1.50,3.00,9.00)\ {\rm K}$ the cold weight is
$w=2/5$. The reported experimental values are respectively
$-170.54\pm0.5$, $-86.31\pm0.5$ and $-19.75\pm0.3$, all in
$\mathrm{cm^3/mol}$. The interpolation gives $-80.066$ at 3 K.
Moving the endpoints down and the middle point up by their respective
quoted uncertainties leaves $\mathcal D[B]=5.364\ {\rm cm^3/mol}$.
This interval calculation assigns no coverage probability.
Aziz, Janzen and Moldover identify the measurements as corrected for
the third virial and credit Matacotta et al. and a private communication.
The comparison uses the experimental column.
[Aziz, Janzen and Moldover, p. 1588 and Table III](https://www.nist.gov/system/files/documents/2017/11/30/085_aziz_ab_initio_prl_1995.pdf)
(passages).

The mechanical readout can also be tested in the original experiment.
Matacotta et al. used a copper bulb of $1002.9\ {\rm cm^3}$ at
$273.16\ {\rm K}$ and four fillings. A pressure balance measured
$p=Mg/A$ using a calibrated piston area $A$, load mass $M$ and local
gravity $g$. Resistance thermometers used the NPL-75 gas scale down to
2.6 K and a magnetic scale below. The authors corrected for bulb
contraction, dead volume, pressure head and thermomolecular pressure.
Their density normalization used a **calculated**
$B(20.3\ {\rm K})=0.30\pm0.10\ {\rm cm^3/mol}$. Their finite-density
observable was $b(T,\rho)=[p/(\rho R_{\rm g}T)-1]/\rho$. These entries
come from a single filling before fitting its temperature dependence
or applying the later third-virial correction.

| $T$ (K) | $\rho$ ($\mathrm{mol/m^3}$) | $b$ ($\mathrm{cm^3/mol}$) |
|---:|---:|---:|
| 1.50899 | 274.497 | $-170.69$ |
| 3.00330 | 274.444 | $-87.33$ |
| 9.04158 | 274.338 | $-19.50$ |

The measured inverse temperatures give $0.402<w<0.404$ and hence
$6.7<\mathcal D[b]<7.1$ in $\mathrm{cm^3/mol}$. A common density
rescaling $\rho_i\mapsto s\rho_i$ changes the result to
$s^{-2}(\mathcal D[b]+(1-s)\mathcal D[1/\rho])$. At equal density the
offset cancels exactly. Here $|\mathcal D[1/\rho]|<2.2\ {\rm cm^3/mol}$
from the two extreme densities. Temperature-dependent calibration
errors enter separately. Since $b=B+\rho C+\cdots$, an independent bound
on the signed combination of density corrections is needed to extract
the dilute result from this filling alone. The authors report excess
scatter near 3 K and discuss the limited precision of their four-fill
comparison. The later table and the original bulb share these data.
[Matacotta et al., §§2–4 and Table 2](https://doi.org/10.1088/0026-1394/24/2/002)
(passages and experimental table).

### What the discrepancy measures about a trial action

Convergence to the classical gas at these three temperatures would
exclude a sequence of trial actions tending to zero that fits the
separated data. A quantitative version allows a steep core. In the
spin-independent two-body Schrödinger family let $h$ denote the trial
reduced action, $m$ the atomic mass, $\mu=m/2$ the reduced mass and
$\sigma=h\sqrt{\beta/\mu}$. Suppose $V\ge-E$, with $E\ge0$, and choose
a radius $a$ beyond the minimum. Assume the truncated potential $V_a$
(zero outside $a$) decreases to its minimum and then increases,
allowing flat pieces and a hard core. Let
$I_a=\int_{|\mathbf r|>a}|V|\,d^3\mathbf r$ be finite. For the direct
and exchange terms together,
$$
\begin{split}
 |B_h(T)-B_0(T;V_a)|&\le \varepsilon_T(h),\\
 \varepsilon_T(h)&=N_A e^{\beta E}
 \left[8\pi\left(a^2c_1\sigma+\frac{c_3\sigma^3}{3}\right)
       +\frac{\beta I_a}{2}+\frac{\lambda^3}{2^{5/2}}\right],\\
 \lambda&=h\sqrt{2\pi\beta/m},\qquad
 c_j=6(3/2)^{j/2}\Gamma(1+j/2).
\end{split}
$$
The direct thermal trace uses the relative Brownian-bridge average of
$\exp[-\beta\int_0^1 V(|\mathbf r+\sigma b_t|)\,dt]$ for a standard
three-dimensional unit bridge $b$. Replacing $V$ by $V_a$ costs at
most $N_A\beta e^{\beta E} I_a/2$ by translation in $\mathbf r$ and
the exponential's slope on $[-E,\infty)$. For a hard core, cap the
common repulsion first and then pass to the hard-core limit. The
absolute exchange contribution is at most its free spin-polarized
magnitude times $e^{\beta E}$, giving the last term. Unpolarized spin
one-half reduces the spin weight further.
[Garberoglio and Harvey, direct and exchange traces, Eqs. (9)–(18)](https://www.nist.gov/system/files/documents/mml/acmd/fluids_modeling/Harvey-Garberoglio-907690-2.pdf)
(formula passages).

To bound the remaining direct term, fix a bridge whose displacement
never exceeds $d=\sigma\sup_t|b_t|$. Its path weight lies between the
smallest and largest values of $f(r)=e^{-\beta V_a(r)}$ on the sampled
radii. At each level strictly between $0$ and $e^{\beta E}$, except
for plateau levels of measure zero, the region above that level has
at most two radial boundaries of radii $u\le a$. A level can contribute
to the difference from $f(|\mathbf r|)$ only within $d$ of a boundary.
Each shell has volume at most $8\pi u^2d+8\pi d^3/3$ by comparing the
cubes of $u+d$ and $(u-d)_+$. Integrate over levels, multiply by
$N_A/2$ and average. The one-coordinate bridge reflection formula and
a union bound give $\Pr(\sup_t |b_t|>z)\le6e^{-2z^2/3}$, so
$\mathbb E[d^j]\le c_j\sigma^j$. The same shell bound holds for
nonnegative quadrature weights of total one at any inserted times.
[Steck, *Stochastic Processes*, Eq. (6.17)](https://atomoptics.uoregon.edu/~dsteck/teaching/stochastic-processes/stochastic-notes.pdf)
(one-sided bridge formula).

If $D_*>0$ bounds the experimental $\mathcal D[B]$ from below after
all calibration allowances, then
$$
 w\varepsilon_{T_c}(h)+\varepsilon_{T_m}(h)
 +(1-w)\varepsilon_{T_w}(h)\ \ge\ D_* .
$$
When the left side at $h=0$ is smaller than $D_*$, the unique positive
root of the corresponding equality is a lower bound in action units.
For each fixed single well with integrable tail one can increase $a$
until this holds. A numerical bound uniform over a class needs
independent bounds on $a$, $E$ and $I_a$ (energy times volume), as well
as $m$, the three thermal energies and the molar volume scale. The
preparation fixes temperature and density, and the balance fixes force
per area. Refining the thermal trace changes none of these inputs. This
experiment uses equilibrium and has no microscopic flight-time readout.

### A classical atom that reproduces the three coefficients

For an explicit alternative give a classical atom three equilibrating
internal states. For an integer $K>1$ give them multiplicities
$(1,K^5,K^7)$ and energies $(0,e,2e)$ with $e=k_B(10\ {\rm K})\log K$.
Their free-atom Gibbs probabilities $p_j(T)$ are proportional to
multiplicity times the Boltzmann factor. At the three measurement
temperatures their respective dominant states approach probability one
as $K$ increases. The successive crossings of the dominant Boltzmann
weights occur at 2 K and 5 K.

Use a common hard core of radius $b=0.15$ nm. On the shell from $b$
to $a=0.50$ nm only like-state pairs interact, with well depth $U_j$.
All interactions vanish outside $a$. Put $v_b=2\pi N_A b^3/3$ and
$v_s=2\pi N_A(a^3-b^3)/3$. Given the three negative experimental
central values $B_j$ at $T_j$, set
$$
 U_j=k_BT_j\log[1+(v_b-B_j)/v_s].
$$
The classical second virial is
$v_b-v_s\sum_j p_j(T)^2(e^{\beta U_j}-1)$. At each $T_j$ this tends
to $B_j$. For example, $K=10^6$ gives $1-p_j(T_j)<2K^{-8/9}<10^{-5}$
at each temperature. The radii give $v_b<4.3$ and $153<v_s<155$ in
$\mathrm{cm^3/mol}$, so $U_j/k_B<2\ {\rm K}$ for all three wells.
The error at $T_j$ is bounded by
$2(1-p_j(T_j))v_s(e^{2/1.5}-1)<0.01\ {\rm cm^3/mol}$.
This single zero-action model fits all three quoted intervals.
The hard core bounds the number of neighbours in
the shell and makes the gas stable. Smoothing the potential steps and
taking steep repulsion changes the three integrals arbitrarily little.
The internal energies, multiplicities, shell radii and well depths are
inputs of this alternative. At 2 K the free-state weights are
$1,1,K^{-3}$. The first two states alone give an internal heat capacity
of at least $k_B(5\log K)^2/(2+K^{-3})^2$, over $1100\,k_B$ per atom
for this choice. Equilibrium calorimetry can distinguish it. This use
of the canonical energy variance is standard.
[Gibbs, 1902, Ch. VII](https://en.wikisource.org/wiki/Elementary_Principles_in_Statistical_Mechanics/Chapter_VII)
(canonical averages and fluctuations).

One can test this alternative even when higher density terms matter.
At fixed $T$, let $G(\rho,T)=\int_0^\rho b(T,s)\,ds$, the excess molar
Helmholtz free energy divided by $R_{\rm g}T$ relative to the same ideal
gas. This follows from $p=-(\partial F/\partial V)_T$ at fixed atom
number. Allow a temperature-independent microscopic energy with
arbitrary internal variables and many-body forces, ordinary separable
translational kinetic energy, canonical equilibrium and a single gas
phase on the integration path. If $q(T)$ is the free atom's internal
partition function, $G-\log q$ differs by a temperature-independent
constant from minus the log of the many-atom partition integral per
atom after integrating translational momenta. It is concave in
$x=1/T$ by Hölder's inequality, also in a thermodynamic limit in which
these free energies exist. Hence $\mathcal D[G]\le\mathcal D[\log q]$.
If independent calorimetry bounds the free atom's internal heat
capacity by $c\,k_B$ throughout the interval, then
$(\log q)''(x)\le c/x^2$. Subtracting $\log q$ from
$-c\log(x/x_m)$ gives a convex function, so
$$
 \mathcal D[G]\le c\left(\frac35\log 3-\frac25\log 2\right).
$$
This test uses pressure isotherms from zero to a common density and an
independent thermal bound. It accommodates rare internal states and
requires no cutoff radius or force fit. For example, if isotherms up to
$250\ {\rm mol/m^3}$ establish that $\mathcal D[b]$ stays within
$1\ {\rm cm^3/mol}$ of the dilute contrast, the lower value $5.364$
above would imply $\mathcal D[G]\ge0.001091$ and require
$c>0.0028$. This tolerance specifies the experimental precision needed
for that inference. The three tabulated
coefficients alone give neither that pressure integral nor the internal
heat capacity. They exclude the equilibrated point-atom pair potential
class at the stated accuracy. Independent necessity of a positive
physical action remains open.

### How many atomic motions can the measured heat support?

**6.1 Sol Max, 2026-11-18.** Warming normal liquid helium-3 from
30 to 50 mK at fixed molar volume
$32\,{\rm cm^3/mol}$ takes less than one fifth of the minimum heat for
equilibrated Newton atoms with independently mobile momenta. Adding
internal states, correlations or many-body positional forces cannot
close that difference. In a finite vessel the same measurement excludes
an interval of small positive trial actions for each fixed scalar
fermion Hamiltonian described below. A mechanical measurement suggested
by Lemma X would test the assumption that the atomic motions themselves
remain accessible in the liquid.

**The preparation and readout.** Greywall measured the constant-volume
heat capacity of pure normal liquid helium-3 from 7 mK to 2.5 K and
reported agreement with earlier measurements within about 5% between
30 and 500 mK. The Bell Laboratories calorimeter used a roughly
$12\,{\rm cm^3}$ cell, a $10\,{\rm k\Omega}$ heater and, below 150 mK,
a melting-pressure thermometer with a separately measured heat addendum.
The sample volume per mole, temperature change, heat delivered, cell
background and amount of helium set the comparison. The heater delivers
energy as the time integral of electrical power. The thermometer uses
an empirical pressure-to-temperature scale. Neither a pulse duration
nor that calibration measures the relaxation time of every putative
hidden motion. Equilibration is a premise of the comparison.
[Greywall, 1983](https://doi.org/10.1103/PhysRevB.27.2747) (abstract,
range and interlaboratory comparison) and [Greywall and Busch,
1982](https://doi.org/10.1103/PhysRevLett.49.146) (p. 146, apparatus).

Let $\nu$ be the amount in moles, $N=\nu N_A$, $R_{\rm g}=N_Ak_B$,
$T_c=0.030\,{\rm K}$, $T_w=0.050\,{\rm K}$ and $\Delta T=T_w-T_c$.
On this isochore Greywall's published interpolation has
$C_V/(\nu R_{\rm g})=T(b_1+b_3T^2+b_4T^3+b_5T^4)$. With $T$ in
kelvin, its coefficients are $b_i=\sum_{j=0}^3 a_{ij}/32^j$ in
$\mathrm{K}^{-i}$. Table I gives $b_1<3.3$, $b_3<0$, $b_4<1000$ and
$b_5<1000$ in these units. Thus the fitted $C_V/(\nu R_{\rm g})$ is
below $0.05(3.3+1000(0.05)^3+1000(0.05)^4)<0.172$ throughout the
interval. Use the looser allowance
$$
 \bar c=\frac{Q}{N k_B\Delta T}\le 0.30,\qquad
 Q=U(T_w)-U(T_c).
$$
This is a conservative envelope for the reported calorimetry, equivalent
to $Q/(\nu R_{\rm g})\le0.006\,{\rm K}$. We chose the margin on the
published interpolation. The paper reports calorimetry at a range of
temperatures without quoting a confidence interval for this integrated
20 mK rise. As a check on the readout, a separate calorimeter used
timed current pulses, measured its heater resistance and separated
bulk heat from the cell background by varying the filling. Its
pressure-controlled $4.99$ bar result was
$C/(\nu R_{\rm g}T)=2.39\,{\rm K}^{-1}$ in a colder normal-liquid
interval. The bound above uses Greywall's fixed-volume data.
[Kollar and Vollhardt](https://arxiv.org/html/cond-mat/9906222)
(§II, Eqs. 5 and 7, Table I, interpolation and temperature scale) and
[Alvesalo, Haavasoja and Manninen](https://doi.org/10.1007/BF00655140)
(§§2–3, Table II, heater, thermometry, background and normal phase).

**The classical exclusion.** Take a closed, fixed-volume Gibbs
preparation with temperature-independent Hamiltonian and phase-space
measure. Conditional on the configurations and internal variables $z$,
allow $d$ unrestricted momenta with energy
$\tfrac12(p-a(z))^\top M(z)^{-1}(p-a(z))+W(z)$, $M(z)>0$, and the
ordinary momentum volume element. Equipartition and the canonical
energy variance give
$$
 C_V(T)\ \ge\ \tfrac12 k_B\,\langle d\rangle_T,\qquad
 \frac{1}{N\Delta T}\int_{T_c}^{T_w}\langle d\rangle_T\,dT
       \ \le\ 2\bar c\ \le\ 0.60 .
$$
Indeed the conditional quadratic energy has variance
$d(k_BT)^2/2$ even if $d$ depends on the sector. The variance of
the conditional mean adds a nonnegative term. This use of the Gibbs
identities allows arbitrary correlations, annealed labels and
interactions in $W$. Ordinary point atoms have $d=3N$.
Fixing the total momentum removes at most three such directions
from the entire sample. Their minimum heat per mole over the interval
is $0.030 R_{\rm g}\,{\rm K}$ up to that finite-size correction.
Every mathematical subdivision of the heating interval gives the
same finite-heat inequality.
[Gibbs, 1902, Ch. VII](https://en.wikisource.org/wiki/Elementary_Principles_in_Statistical_Mechanics/Chapter_VII)
(passage, canonical fluctuations and quadratic momenta).

**An action bound for the same finite heat.** Put $\beta_i=1/(k_BT_i)$
for $i=c,w$, $\beta_m=(\beta_c+\beta_w)/2$ and
$J[f]=(f(\beta_c)+f(\beta_w))/2-f(\beta_m)$. For
$f=N^{-1}\log Z$, the change in its slope between the endpoints is
$Q/N$. Convexity bounds the midpoint difference by this slope change
times $(\beta_c-\beta_w)/4$ (the maximum of the triangular kernel for
the midpoint difference). For $3N$ classical momenta, integrating the
Gaussians leaves a log-convex positional partition integral. Hence
$$
 J[f_{\rm obs}]\le\frac{(\beta_c-\beta_w)Q}{4N}\le0.020,\qquad
 J[f_{\rm cl}]\ge\frac32\log
   \frac{\beta_m}{\sqrt{\beta_c\beta_w}}
   =\frac32\log\frac4{\sqrt{15}}>0.048 .
$$
The first inequality applies to any equilibrium model reproducing the
heat. Additive energy offsets and constant normalization of the
partition function cancel. The positive difference $\delta=0.028$ per
atom uses only the two temperatures and the heat allowance.

Consider $N$ identical spin-$\tfrac12$ atoms of mass $m$ with Dirichlet
walls in a bounded vessel $\Omega$ with piecewise smooth boundary.
Let $V$ be a fixed spin-independent permutation-symmetric scalar
potential, bounded below, with $e^{-\beta V}$ Riemann integrable and
positive in integral. This includes hard cores with null contact
boundaries, interpreted as Dirichlet exclusions on the allowed open
configurations. Write $Z_F^h$ for the fermionic trace with kinetic
operator $-h^2\sum_i\Delta_i/(2m)$, where $h$ is a trial reduced action,
and $\lambda_\beta=h\sqrt{2\pi\beta/m}$. In zero field sum over all spin
states. The matching classical reference is
$$
 Z_{\rm cl}^h=\frac{2^N}{N!}\lambda_\beta^{-3N}
          \int_{\Omega^N}e^{-\beta V(x)}\,dx .
$$
Take all grid cubes of side $\ell$ lying wholly in the vessel. In the
sum below $D$ ranges over ordered products of $N$ distinct such cubes.
Define the dimensionless loss of classical positional weight by
$$
 L_\beta(\ell)=
 \frac{\sum_D \ell^{3N}e^{-\beta\sup_D V}}
      {\int_{\Omega^N}e^{-\beta V(x)}\,dx},\qquad
 A_\beta(\ell)=-N^{-1}\log L_\beta(\ell).
$$
For $0<\lambda_\beta<\ell$ and positive $L_\beta$,
$$
 0\le\frac1N\log\frac{Z_{\rm cl}^h}{Z_F^h}
   \le A_\beta(\ell)-3\log(1-\lambda_\beta/\ell).
$$
For the left inequality apply Golden–Thompson on the antisymmetric
subspace. On its diagonal the free heat kernel is a determinant divided
by $N!$ on labelled coordinates including spin. Hadamard's inequality
bounds it by the product of diagonal one-particle kernels, each at
most $\lambda_\beta^{-3}$ by Dirichlet domination. Additional Dirichlet
hard-core exclusions can only reduce the trace, also relative to a
finite repulsive barrier filling each excluded region. Sending that
barrier to infinity gives the stated upper bound.
[Golden](https://doi.org/10.1103/PhysRev.137.B1127) (abstract, thermal
trace inequality) and [Ceperley](https://people.physics.illinois.edu/Ceperley/papers/059a.pdf)
(passage, free-particle density matrix, Eq. 32).

For the right inequality confine one atom to each of $N$ distinct
cubes, use Dirichlet walls, and replace $V$ there by its supremum.
Antisymmetrizing the disjoint cell products leaves one copy per
unordered cell set and $2^N$ spin choices. For fixed spin populations
the number of choices is $\binom{N}{N_\uparrow}$ on both sides
in place of $2^N$, so the comparison is unchanged. The variational principle
bounds their summed traces above by the full fermionic trace.
The one-dimensional cell trace is at least $\ell/\lambda_\beta-1$ by
the integral bound for the decreasing Dirichlet Gaussian sum. Taking
three factors per atom gives the displayed inequality. This argument
uses the sign of a free determinant only on its diagonal.

Write $A_*=(A_{\beta_c}+A_{\beta_w})/2$ at the same $\ell$. The
midpoint correction $N^{-1}\log(Z_{\rm cl}^h/Z_F^h)$ is nonnegative.
Thus a fermion model fitting the observed heat must satisfy, whenever
$A_*<\delta$,
$$
 h\ \ge\ \ell\sqrt{\frac{m}{2\pi\beta_c}}\,
                  \big[1-e^{-(\delta-A_*)/3}\big].
$$
If $\lambda_{\beta_c}\ge\ell$ this already holds. Otherwise average
the error at the two endpoints and use $\lambda_{\beta_w}\le
\lambda_{\beta_c}$. At fixed $N,\Omega,V$, $L_\beta(\ell)\to1$ on
successively halved grids by lower Riemann approximation. Walls and
particle coincidences have zero configuration volume. A positive
$\ell$ with $A_*<\delta$ therefore exists for each such model.
Obtaining a number in action units requires $m$, a physical length
$\ell$ and control of the classical weight on that length from the
vessel geometry, sample density and interaction energies. The grid
estimates that weight without imposing a minimum length. Uniformity
over changing potentials or increasing sample sizes remains open. Under
$h\mapsto a h$ with all preparation and calorimeter settings fixed,
$\lambda_\beta/\ell$ is multiplied by $a$ while the heat allowance
and $A_\beta$ are unchanged. Rescaling the bath temperature, atomic
mass or vessel dimensions to undo this would change measured inputs.

**What would a Lemma X measurement add?** For smooth, time-independent
ideal holonomic constraints and the atomic mass metric, the response to a small
constant force applied to atom $i$, read in one unit direction $e$,
is the corresponding diagonal entry of the mass-weighted orthogonal
projector $P$ onto allowed velocities. Operationally that entry is
the limit of
$2m\, e\cdot(\langle x_i(\tau)\rangle_F-\langle x_i(\tau)\rangle_0)/
(F\tau^2)$ for a force $Fe$ and matched initial ensembles, averaged
over their configurations. Smooth finite forces give the short-time
expansion away from impacts. The trace of $P$ counts the mobile
directions at each configuration. Thus for a uniformly sampled atom
and an isotropically sampled axis, the temperature-averaged mean
response is at most $2\bar c/3\le0.20$ in this constrained equilibrium
class. Unconstrained atoms give one. The required independent readout
measures mass, local applied force, elapsed time and displacement,
with control of the finite-time remainder and atom selection. A uniform
force tests only one collective profile per axis. [Udwadia and Kalaba](https://doi.org/10.1115/1.1459071)
(passage, constrained equations for forces doing zero virtual work).

Both the force and its readout can have finite resolution. In Cartesian
coordinates for equal atomic masses let $u$ be the desired unit vector
at the chosen atom. A force $F b$ and displacement sensor along $c$
give the initial response $c^\top P b$. Map the two profiles at their
physical spot widths and bound $\|b-u\|\le\zeta_F$ and
$\|c-u\|\le\zeta_x$. The spatial error in the normalized response is
at most $\zeta_F+\zeta_x+\zeta_F\zeta_x$ since $\|P\|\le1$.
For a timed exposure $\tau$, let $L$ bound, in inverse seconds, the
rate of change of the mean acceleration difference along $c$ in units
of $|F|/m$. The displacement averages the acceleration with weight
$2(\tau-s)/\tau^2$. If the error on the paired displacement is at most
$\sigma_x$ in metres, the additional error is bounded by
$$
       L\tau/3+2m\sigma_x/(|F|\tau^2).
$$
Both terms use apparatus calibrations independent of a time mesh.
With positive $L$ and $\sigma_x$ the best duration for this estimate
is $\tau=(12m\sigma_x/(|F|L))^{1/3}$ if the acceleration bound holds
that long. Shrinking the plotted time step cannot improve this
physical measurement.

Heat and a recoil spectrum have both been measured at the same nominal
temperature and pressure. At 500 mK and 10 bar the thermodynamic table gives
$C_P/(\nu R_{\rm g}T)=0.6964\,{\rm K}^{-1}$. Stability gives
$C_V\le C_P$, hence a pointwise classical ceiling of $0.2322$ on the
mean projected response using the tabulated value. Allowing
$C_V/(\nu R_{\rm g})\le0.40$ raises the ceiling to $0.267$.
Bryan et al. selected a nominal 800 meV incident neutron energy and a
mean scattering angle of $125^\circ$ at this temperature and pressure.
They compared the recoil line to a single-atom impulse profile with
instrumental resolution and final-state corrections.
[Kollar and Vollhardt](https://arxiv.org/pdf/cond-mat/9906222)
(Table IV, 10 bar) and [Bryan et al.](https://doi.org/10.1209/0295-5075/115/66001)
(experimental approach and extraction of kinetic energy).

For a mechanical comparison, deliver opposite impulses of magnitude
$I$ on matched preparations to a uniformly chosen atom along a random
axis, and read the work $W_\pm$ done on the sample. In the impulsive
limit the coordinates stay fixed, the momentum change is projected
onto allowed velocities, and
$m\langle W_++W_-\rangle/I^2$ equals the mean projector entry. The
opposite signs cancel the initial velocity. Suppose an instrument
determines the mean entry $r$ only on a fraction $\eta$ of these
uniformly assigned paired trials, with selection independent of the
sign and with the two works matched at fixed initial state or in
conditional mean. Nonnegativity of each projected squared impulse
makes $\eta r$ a lower bound for the unconditional entry. Thus
$\eta r>0.267$ would exclude even the constrained classical model
at the warmer state under the stated heat allowance. A calibrated
impulse, delivered work, mass and a lower bound on the represented
fraction suffice. Conditioning on detected scattering events alone
loses this last factor. For example, a fraction $s$ of freely mobile
atoms among fixed atoms has true mean entry $s$, yet gives unit
response on the mobile subset for every $s>0$. The published profile
measures scattering intensity in a selected energy and angle range.
It supplies neither the opposite-work measurement nor that uniform
sampling calibration. This is the remaining physical step between
the heat deficit and Newton's individual force readout.

### Isotope exchange as a test of central forces

**6.1 Sol Max, 2026-11-18.** At 1.598 K the helium-3 to helium-4
number ratio was about 31 times larger in vapour than in coexisting
liquid. If isotope substitution changes only inertial mass, even an
arbitrarily constrained classical Gibbs system allows an enrichment of
at most $(m_4/m_3)^{3/2}<1.54$. A classical model with additional
isotope-dependent forces must assign more than $k_B(4.68\,{\rm K})$
of mean potential work to interchanging the two labels in the sampled
environments if it retains the stated kinetic measure. Both the mass
bound and the work test include atoms that a recoil detector could miss.

**The bulk measurements.** Write $C_b=N_{3,b}/N_{4,b}$ for the number
ratio in phase $b$, and $\alpha=C_A/C_B$ for the enrichment of phase
$A$ relative to $B$. In Wansink's stable 1.598 K series the four
liquid ratios were $0.206$, $0.228$, $0.253$ and $0.281$ percent.
The corresponding vapour/liquid enrichments were $31.3$, $31.1$,
$31.1$ and $31.0$. We use $\alpha>29$ after decreasing the smallest
value by the author's overall 5% accuracy estimate. This margin is
applied to an individual measured isotherm without extrapolating to
zero concentration. The $454\,{\rm mm^3}$ copper vessel, measured
liquid volume, bath pressure, differential manometer and isotope mass
balance supplied the readout. The level and pressure were read at
30 and 60 s intervals while a superleak removed helium-4. The
reduction assumes local vapour/liquid equilibrium, retention of
helium-3 in the cell and an empirical dew-point calibration, with a
virial correction. Sommers's dew-point measurements used known
room-temperature gas compositions. [Wansink, 1957](https://www.lorentz.leidenuniv.nl/history/proefschriften/sources/Wansink_1957.pdf)
(Ch. I, §§2–6 and Table I) and [Sommers, 1952](https://doi.org/10.1103/PhysRev.88.113)
(abstract, calibration method).

One can dispense with the subtraction of two vapour inventories
used to infer the small liquid concentration. In the first row,
$V_L=13.65\,{\rm mm^3}$, the measured pressure excess is
$0.361\,{\rm mmHg}$ and the emptied-cell value is $0.572\,{\rm mmHg}$.
The latter gives $2.61\,\mu{\rm mol}$ of helium-3 in the whole vessel
from $\Delta P_{\max}V/(R_{\rm g}T)$ before the virial correction.
Take a loose upper allowance of $3.0\,\mu{\rm mol}$ for this inventory
and lower the calibrated vapour ratio from about $0.064$ to $0.050$.
If $\alpha\le1.54$, then $N_{4,L}\le1.54\,N_{3,L}/0.050$. Assigning
even the entire light-isotope inventory to the liquid would require
its total molar density to be below
$(1+1.54/0.050)(3.0/13.65)=6.99\,{\rm mol/L}$ to the displayed
precision. A direct liquid density measurement can test this prediction.
For scale, Ptukha measured $0.13982\,{\rm g/cm^3}$ at 1.604 K even at
10 mol percent helium-3, over $35\,{\rm mol/L}$, using a pycnometer
and a calibrated room-temperature gas volume. This check still uses
Wansink's dew-point and emptied-cell calibrations. [Wansink](https://www.lorentz.leidenuniv.nl/history/proefschriften/sources/Wansink_1957.pdf)
(Ch. I, Eqs. 3–14, Table I and film-inventory discussion) and
[Ptukha](https://jetp.ras.ru/cgi-bin/dn/e_007_01_0022.pdf)
(apparatus and density table, printed pp. 23–24).

There is a second measurement with the heater off. Zinov'eva and
Peshkov watched the liquid/liquid interface appear and disappear
during slow cooling and warming. In their first apparatus the two
branches meet the same tabulated temperature, $0.61\,{\rm K}$, at
helium-3 mole fractions $0.8499$ and $0.3028$. Interpreting these as
the endpoints of the coexistence line at saturated vapour pressure
gives an isotope odds ratio of about $13$. These are two separately
prepared bulk fills. The authors checked the influence of vapour
inventory by changing the size of the vapour space. The apparatus
used a 20 mm glass capsule, a cathetometer and a resistance thermometer
calibrated by helium-3 vapour pressure. Even fractions of $0.80$ and
$0.35$ would give an odds ratio above seven. [Zinov'eva and Peshkov,
1959](https://jetp.ras.ru/cgi-bin/dn/e_010_01_0022.pdf) (experimental
procedure and table on printed pp. 23–24).

**What inertial mass can change.** Consider an equilibrium mixture in
which either isotope may occupy any admissible atomic position. Allow
hidden internal coordinates, many-body forces and smooth ideal
holonomic constraints. For the mass-only comparison the constraint
surface, its statistical weights apart from the kinetic integral, and
the positional energy are invariant under changing the isotope at a
site. An isotope-specific constant energy or spin multiplicity can be
included in its activity. Let $z$ be the common ratio of isotope
activities in two coexisting phases, with these constants included.
An observation region and its sampling rule must be defined without
reference to the isotope of the atom to be counted.

At fixed configuration the induced kinetic mass matrix has the form
$G(m)=G_{\rm rest}+mB^\top B>0$, where $B$ maps generalized velocities
to the three Cartesian velocity components of the chosen atom and
$G_{\rm rest}\ge0$. Integrating the canonical momenta gives a weight
proportional to $\sqrt{\det G(m)}$. In the mechanical realization of
Lemma X above, the initial acceleration response of this atom to an
applied force at the same atom is $BG^{-1}B^\top$.
Consequently
$$
 \frac{d\log\sqrt{\det G(m)}}{d\log m}
    =\tfrac12\operatorname{tr}(mBG^{-1}B^\top)\ \in[0,3/2].
$$
The matrix in the trace is a positive contraction because
$mB^\top B\le G$. Integrating between the measured atomic masses gives
$$
 1\le\sqrt{\det G(m_4)/\det G(m_3)}\le K,\qquad
 K=(m_4/m_3)^{3/2}<1.54 .
$$
The conditional light/heavy odds at every position with the other
labels held fixed therefore lie between $z/K$ and $z$. Integrating
either inequality over a phase, with its other atoms and constraints,
preserves it. Thus $K^{-1}\le\alpha\le K$. Comparing these ratios
uses equilibration at a common temperature. Its absolute value is
needed only to express the work in energy units. Unconstrained Cartesian
atoms give exactly $\alpha=1$, the classical equilibrium isotope
result. The determinant bound covers partially frozen motions as
well. [Bigeleisen and Mayer](https://doi.org/10.1063/1.1746492)
(abstract, equilibrium isotope separation), [Fixman](https://doi.org/10.1073/pnas.71.8.3050)
(abstract, constrained kinetic determinant) and [NIST isotope masses](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=He)
(table).

**How much extra force is required?** Draw a tagged helium-3
environment in $A$ and a tagged helium-4 environment in $B$ from the
equilibrium number-weighted samples. Take independent draws so that
the two composition measurements enter through their product.
At fixed coordinates interchange the isotopes. Let $W$ be the change
in positional energy before the surroundings relax, and $D$ the ratio
of the final product of kinetic weights to the initial product. The
first substitution multiplies the kinetic weight by a factor in
$[1,K]$ and the reverse one by a factor in
$[1/K,1]$. Interchanging the labels again restores the original
pair. Integrating the changed weights cancels both activity factors
and gives the equilibrium perturbation identity
$$
 \frac1\alpha=\big\langle D e^{-\beta W}\big\rangle_{3A,4B},
 \qquad K^{-1}\le D\le K,\qquad \beta=1/(k_BT).
$$
This form uses phases at common isotope chemical potentials. In a
finite closed cell the same change of variables swaps two uniformly
chosen atoms in different regions within one configuration. The
left side then uses the ratio of the two *joint* probabilities of
opposite labellings. No product approximation is needed for that
version. For a mutual pair interaction the pair between the two
chosen atoms stays the same. [Zwanzig, 1954](https://doi.org/10.1063/1.1740409)
(equilibrium free-energy perturbation identity).

One can also test the two reported marginal concentrations in a
closed cell without inferring any joint probability. Fix positive
isotope counts $N_3,N_4$ and condition on the unlabelled geometry.
If $p_i$ is the probability that site $i$ is light, choose $j$
uniformly among the other sites. The ratio of probabilities of
$(3_i,4_j)$ and $(4_i,3_j)$ is precisely
$p_iN_4/[(1-p_i)N_3]$. The mass-only swap bounds this by $K$ and
its reciprocal by $K$, because the simultaneous mass changes have
opposite signs. Thus every site's odds lie between $N_3/(K N_4)$
and $K N_3/N_4$. The same interval contains the ratio of mean counts
in any isotope-blind window, even with fluctuating window occupancy.
In particular $\alpha\le K^2<2.38$ at fixed counts, already excluded
by the measured isotherm. With a uniform bound $|W|\le w$ on all
potential-energy changes, the same argument gives
$\alpha\le K^2e^{2\beta w}$. The observed enrichment therefore
requires some swaps costing more than $k_B(1.99\,{\rm K})$ even in
the closed-cell comparison. The stronger mean bound below uses the
common activities of coexisting phases.

Jensen's inequality and restriction of the positive integral to any
subset of swaps of cost at most $w$ give, respectively,
$$
 \langle W\rangle_{3A,4B}\ge k_BT\log(\alpha/K),\qquad
 \Pr_{3A,4B}(W\le w)\le K e^{\beta w}/\alpha .
$$
For the Leiden isotherm the first lower bound exceeds
$k_B(4.68\,{\rm K})$. The second says that fewer than one in ten of
the represented pairs can have cost at most $k_B(1\,{\rm K})$.
The probability bound continues to hold on the reversible subset if
some substitutions are forbidden and assigned infinite cost, provided
each counted swap has the same base-measure mapping and kinetic
bound. Arbitrary isotope-dependent state multiplicities or constraints
require a separate calibration of those weights. The gravitational
contribution is at most $(m_4-m_3)gH$ for a vertical separation $H$.
One metre gives less than $k_B(0.0012\,{\rm K})$ at terrestrial gravity.

For pairwise central forces define $F_{st}(r)=-v'_{st}(r)$ positive
outwards and normalize $v_{st}(\infty)=0$. Let $n^A_{3t}(r)$ count,
in mean, neighbours of isotope $t$ within $r$ of a helium-3 atom in
$A$, and define $n^B_{4t}$ in the other phase in the same way.
The isotope-dependent part of the pair work is exactly
$$
 \langle W_{\rm pair}\rangle =
 \sum_{t=3,4}\int_0^\infty
 [F_{4t}(r)-F_{3t}(r)]\,[n^A_{3t}(r)-n^B_{4t}(r)]\,dr .
$$
Indeed, substitution at one site costs $\sum_j(v_{4t_j}-v_{3t_j})(r_j)$.
Using $v_{st}(r_j)=\int_{r_j}^\infty F_{st}(r)\,dr$ and subtracting
the reverse substitution gives the formula when the absolute integrals
are finite. The counts are dimensionless. The two-body force can be
calibrated as reduced mass times the radial projection of the relative
vector acceleration, using lengths, elapsed times and a finite-time
error allowance as above. An upper bound for this integral plus wall,
field and isotope-specific many-body work below the measured threshold
would reject the classical explanation. Bounds on a representative
fraction of swaps suffice for the probability test.

Burgmans, Farrar and Lee found no discernible difference between the
helium-3/helium-4 and helium-4/helium-4 potentials within their angular
scattering fits. The fit inferred a mixed-pair well depth of
$k_B(10.57\,{\rm K})$ at $2.97$ ångströms by integrating the radial
Schrödinger equation. This supplies evidence for a common force. It
does not supply a classical, independently calibrated upper bound
for the weighted force integral or the many-body term. [Burgmans,
Farrar and Lee](https://doi.org/10.1063/1.432401) (abstract and
preprint, data analysis and isotope comparison).

For an explicit zero-action alternative take classical Cartesian
particles with any isotope-independent host potential. Add a smooth
radial one-body potential for helium-3 that is zero in the first
sampling region and $u$ in the second. Take helium-4's added potential
to be zero. The conditional local isotope odds then give exactly
$\alpha=e^{\beta u}$, independently of the host forces. Choosing
$u=k_B(1.598\,{\rm K})\log 31.1$ fits all four enrichment readings
within their stated accuracy. The added force vanishes inside both
plateaux. Its integral between them costs $k_B(5.49\,{\rm K})$ to
the accuracy displayed. This model reproduces the concentration
readout. The radial field and its spatial scale are additional
physical inputs. They are testable by work during passage. A force
measurement confined to the interior of each phase misses them.

The $2.01\,{\rm K}$ run tests this explanation with the same field.
For $C_B=0.210\%$ the measured $\alpha$ was $10.4$, while the simple
offset predicts more than 15. One hidden classical coordinate is
enough to reproduce both temperatures. Give the light isotope a
harmonic internal coordinate of a fixed mass with spring constants
$\kappa_A=49\kappa_B>0$ in the two regions. Its two classical
partition integrals have ratio $1/7$. Set the fixed offset to
$u=k_B(1.598\,{\rm K})\log(7\times31.1)$. The enrichment is now
$e^{\beta u}/7$. This gives $31.1$ for the stable series and about
$10.3$ at $2.01\,{\rm K}$ for the quoted neighbouring concentration.
The isotope-selective energy and stiffness can both be interpolated
smoothly between the regions. These are alternatives for the stated
ratio measurements. Identifying either with the liquid requires
independent force and internal-state data. [Wansink](https://www.lorentz.leidenuniv.nl/history/proefschriften/sources/Wansink_1957.pdf)
(Ch. I, Table I, 2.01 K series and §6 on its scatter).

Even exact forces in isolated atom pairs leave a possible many-body
interaction. Take a smooth radial function $\phi$ of finite range
$a$, with $0\le\phi\le1$ and zero slope at the origin. Put
$n_i=\sum_{j\ne i}\phi(r_{ij})$ and choose a smooth $s$ that is zero
for $n\le1$ and one for $n\ge2$, with $0\le s\le1$. Add
$u\sum_i b_i s(n_i)$ to the host energy, where $b_i=1$ for helium-3
and zero for helium-4. Substituting a light atom for a heavy one at
fixed positions costs exactly $u s(n_i)$. The conditional isotope
odds therefore have the same two plateaux as in the one-body example.
The added force on atom $i$ from the $ij$ separation is
$$
 -u[b_i s'(n_i)+b_j s'(n_j)]\phi'(r_{ij})\,
                   (x_i-x_j)/r_{ij}.
$$
These forces act along centre lines and satisfy action and reaction.
They vanish on every isolated two-body trajectory, at every speed and
separation. The many-body energy is stable for $u>0$. Its range and
coordination dependence are extra inputs. To use it for the actual
vapour and liquid one would need their populations of the two
environments. It establishes that arbitrarily accurate isolated-pair
measurements alone cannot bound the isotope-dependent work in a liquid.

**Does taking the trial action small restore the enrichment?** For
the mass-only hypothesis, fix a finite number of each isotope, the
physical masses, vessel, bath temperature and sampling regions. Take
a scalar Schrödinger Hamiltonian with a common label-independent,
continuous, bounded-below potential on configurations and Dirichlet
walls in a bounded vessel. Use Fermi statistics for helium-3 and
Bose statistics for helium-4 with spin-independent forces. For every
bounded position readout invariant under permutations within species,
the equilibrium mean tends as the trial reduced action $h\downarrow0$
to its full Cartesian classical mean. Consequently $\alpha_h\to1$
for the ratio of mean isotope counts when their limiting denominators
are positive. Thus a fixed model of this class fitting the measured
enrichment excludes an interval next to zero action.

To see that the statement also covers inserting times in the thermal
kernel, put $\lambda_s=h\sqrt{2\pi\beta/m_s}$. Divide each permutation
kernel by the free diagonal factor $\prod_i\lambda_{s_i}^{-3}$.
For the identity permutation the Brownian bridges shrink to their
initial positions. At any interior configuration the error for
potential quadrature weights that are nonnegative and sum to $\beta$ is controlled
by the variation of the potential over the bridges' full excursion,
uniformly in the number and placement of inserted times. For a
nonidentity within-species permutation $\sigma$ the absolute normalized
kernel, omitting a bounded spin multiplicity, is at most
$$
 e^{-\beta\inf V}
 \exp\!\left(-\pi\sum_i |x_i-x_{\sigma(i)}|^2/\lambda_{s_i}^2\right).
$$
This tends to zero off coincidence sets of measure zero.
Bounded readouts and finite
volume allow dominated convergence in the finite permutation sum.
The surviving spatial weight is proportional to $e^{-\beta V}$
with equal isotope odds at every label-independent site. This uses
the standard thermal kernel and trace limit. [Güneysu](https://arxiv.org/abs/1701.04998)
(abstract, semiclassical partition limit) and
[Ceperley](https://people.physics.illinois.edu/Ceperley/papers/059a.pdf)
(passage, permutation kernels). A numerical bound uniform over
potentials would require physical control of their spatial variation
and of the sampled populations. The explicit classical field above
shows why the concentration assay alone cannot supply that control
or select a universal physical action.

## 7. Consequence for STATE

Newton action necessity is the active priority. This note gives the first
$0+1$ background construction: arbitrary unequal polygons converge on a
stated Lipschitz-controlled interval; the same Green function controls
source response and the Gaussian width proportional to $\hbar$. Its
oscillator example separates boundary caustics from initial-value failure.
The return-side detector gives a common observable for the two orders
of the core and action limits. The incoming Liouville flux already
controls the sensitive trajectories classically. The open physical
question is whether observed return laws exclude zero action. The
three-energy collision identity removes arbitrary common impact
concentration from a classical comparison. Its use on real data
requires control of the accessible force, of how the ensemble changes
with the setting, and of the angular response. A lower bound from
Mott exchange also supplies that dynamical law. The physical premise
that would force a positive action for central motion in general
remains open. Three equilibrium work readings control nonlinear static
screening and charge penetration. The two-pulse test covers delayed
motion in its stated model. The thermal shutter test bypasses the
absolute microwave boost calibration. Its remaining premises are the
exterior binding work during passage and the driven velocity moment.
The field-free, finite-time position measurement dispenses with the
latter and has yet to be matched to data at the stated preparation.
The liquid-helium heat measurement excludes mobile classical Gibbs
atoms even with internal states. Isotope enrichment bounds the extra
work needed even with constrained atoms. An independent bound on the
isotope-dependent force during passage between the two environments
would test the remaining classical alternative.
The two-power barrier comparison needs guarded return counts and
independent control of the optical work across the occupied beam.
Returning through the same static barrier removes its interior force
profile from the two-image bound. Four launch energies bound the effect
of a nonunique barrier-top orbit. Applying this to rubidium requires
matched guarded counts and an independent bound on single-atom work.
With one atom per guide the remaining conditions are the work across
several cells, freeze and acceptance errors, and the time allowed for
a distant return. For a central orbit the centrifugal drop between
equal shell phases supplies the corresponding work in ruler and clock units.
For polonium the unresolved calibration is the radial work for every
outgoing channel and the absolute fraction outside on the decay clock.
