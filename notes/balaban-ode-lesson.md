# Constructing Newton motion: refinement, continuation and regularity

**Maintained result.** For a globally Lipschitz acceleration, arbitrary positive
partitions and independently mixed kick--drift orders construct the same unique
initial-value motion, with an explicit error proportional to the mesh. A
conservative logarithmic force family shows the exact limit of that sufficient
hypothesis: an unbounded slope still permits unique motion when $0<\beta\le2$;
finite-time arrival and waiting branches occur for $\beta>2$. Local action tends
to zero in both regimes. These are classical existence and uniqueness statements,
with no positive action premise.

For a continuous outward central force, the departure of one moving orbit
from its inertial tangent at successive half-times determines whether a
body initially at rest at the centre can leave. The short-time force
coefficient converges uniformly over bounded-speed orbits in both cases.
Allowing the force to change sign gives two explicit laws with the same
moving positions, velocities and accelerations at all those times and
opposite answers about rest.

The polygon proof uses standard stability, consistency and Gronwall arguments.
The arrival test is a direct energy calculation, not the general first-order
Osgood criterion. Teschl [@TeschlODE2012, §2.7, pp.54--56 and Problem 2.25,
p.58; passages read] supplies the Euler compactness background; López Pouso
[@LopezPouso2005; metadata and abstract read] treats a broader second-order
problem whose full theorem is not used here. See the
[source companion](../docs/Teschl_ODE_2012.md). Internal Terra/Sol checks of the
written arguments were model reviews, not independent peer review or novelty
evidence.

## 1. Start with a finite Newton polygon

Let $m>0$ be the mass and $f(q)=F(q)/m$ the acceleration. The desired
motion would satisfy
$$\dot q=v,\qquad\dot v=f(q),\qquad(q(0),v(0))=(q_0,v_0).\tag{1}$$

For now we do not assume that a solution exists. Given a positive time
step $\tau$, define a drift and a force kick by
$$
 D_\tau(q,v)=(q+\tau v,v),\qquad
 K_\tau(q,v)=(q,v+\tau f(q)).
 \tag{2}
$$

A step can kick first, $D_\tau K_\tau$, or drift first,
$K_\tau D_\tau$. The first choice uses the force at the old position;
the second uses the force at the new position. Both give a finite
piecewise straight trajectory with impulses. Neither is assumed to
agree exactly with the unknown continuous motion.

Fix $T>0$, take any finite positive partition of $[0,T]$, choose either ordering in
each cell, and compose the maps chronologically. There is no equal-step
or nesting requirement. When a time is inserted, recompute the later
states from the fixed initial state and the prescribed force rule.

Existence of the limit requires two kinds of estimates. Stability bounds
how differences grow. Consistency bounds the error in the finite force
balance. The two together will construct the ODE solution.

## 2. Lipschitz control supplies stability

Assume for this construction that
$$|f(q)-f(Q)|\le\Lambda|q-Q|\quad(q,Q\in\mathbb R),\qquad\Lambda\ge0.
\tag{3}$$

The quantity $\Lambda$ has units of inverse time squared. Choose a
reference frequency $\rho>0$ and use the length-valued phase-space norm
$$
 \|(q,v)\|_\rho=|q|+\frac{|v|}{\rho},\qquad
 \alpha=\max(\rho,\Lambda/\rho),\quad
 \beta=\rho+\Lambda/\rho,\quad b=|f(0)|/\rho.
 \tag{4}
$$

There is no action constant in these definitions. Directly from (2),
$$
 \operatorname{Lip}(D_\tau)\le1+\rho\tau,\qquad
 \operatorname{Lip}(K_\tau)\le1+\Lambda\tau/\rho.
 \tag{5}
$$

Thus either cell map has Lipschitz constant at most $e^{\beta\tau}$.
The constants multiply under composition, and their exponents add.
Every finite polygon therefore has the same upper amplification
$e^{\beta T}$, independently of the number and placement of vertices.

We also need a bound on the states themselves, because consistency
involves the force along the polygon. For either cell map $M_\tau$,
$$
 \|M_\tau z\|_\rho\le e^{\beta\tau}\|z\|_\rho
                         +\tau e^{\beta\tau}b.
 \tag{6}
$$

For a kick-first cell, the inhomogeneous term is actually at most
$\tau(1+\rho\tau)b$; for a drift-first cell it is $\tau b$.
Iterating (6) gives the common vertex bound
$$R=e^{\beta T}(\|z_0\|_\rho+Tb).\tag{7}$$

In particular $|q_j|\le R$, $|v_j|\le\rho R$, and
$|f(q_j)|\le A:=|f(0)|+\Lambda R$. A very irregular partition has not
created a new force or stability constant.

## 3. The polygons construct the ODE solution

Linearly interpolate both vertex coordinates to obtain
$z_\pi(t)=(q_\pi(t),v_\pi(t))$. The displayed velocity is continuous;
it differs from the physical constant velocity along each straight
polygon segment by at most that cell's kick. This distinction disappears
with the mesh.

Let $\delta=|\pi|$ be the maximum cell duration. In a kick-first cell,
with elapsed time $s\in[0,\tau]$,
$$
 \dot q_\pi-v_\pi=(\tau-s)f(q_j),\qquad
 \dot v_\pi-f(q_\pi)=f(q_j)-f(q_\pi).
 \tag{8}
$$

In a drift-first cell the analogous expressions are
$-sf(q_{j+1})$ and $f(q_{j+1})-f(q_\pi)$. The bounds in (7) give, for
almost every time,
$$
 \|\dot z_\pi-\mathcal F(z_\pi)\|_\rho\le C\delta,
 \quad\mathcal F(q,v)=(v,f(q)),\quad C=|f(0)|+2\Lambda R.
 \tag{9}
$$

The vector field $\mathcal F$ is Lipschitz with constant $\alpha$ in
the norm (4). Two polygons with the same initial state consequently
satisfy
$$
 \sup_{t\le T}\|z_\pi(t)-z_\sigma(t)\|_\rho
 \le C\frac{e^{\alpha T}-1}{\alpha}
                        (|\pi|+|\sigma|).
 \tag{10}
$$

To verify this estimate, integrate the two residual equations (9),
subtract, and apply the elementary integral Gronwall inequality. That
inequality follows by integrating the differential inequality for an
upper bound after multiplying by $e^{-\alpha t}$.

Completeness of continuous path space now constructs a uniform limit
$z(t)$. The residual integral tends to zero; the Lipschitz bound passes
$\mathcal F(z_\pi)$ to $\mathcal F(z)$ under the time integral. Hence
$$z(t)=z_0+\int_0^t\mathcal F(z(s))\,ds.\tag{11}$$

The limit is differentiable and solves (1). Applying the same difference
estimate with zero residual proves uniqueness. Letting one mesh tend to
zero in (10) gives a quantitative error for any other partition.
Both kick orders, mixed arbitrarily, lead to the same solution.
Since $T$ was arbitrary, the global Lipschitz hypothesis constructs
forward motion for every finite time.

This is the first analogy with Balaban: one proves bounds for each
finite description before appealing to a limiting object. The limit
follows from estimates uniform in the refinement. Nothing in this
argument requires choosing $\hbar>0$.

## 4. Local continuation and velocity-dependent forces

For locally Lipschitz acceleration, extend it from a bounded region and apply
the construction until the trajectory leaves that region. Continuation then
requires bounds preventing escape from every compact phase-space region.

For $V\in C^1$ with locally Lipschitz $\nabla V$, (1) has a unique
local solution, by the usual Cauchy--Lipschitz theorem. Along it,
$$E(q,v)=\tfrac12m|v|^2+V(q),\qquad \frac d{dt}E=0.$$
If $V$ is bounded below, (2) bounds $|v|$. On any finite interval
$|q(t)|\le |q_0|+|t|\sup|v|$, so $(q,v)$ remains in a compact set.
The local continuation theorem then gives a unique solution for all
positive and negative times. Coercivity of $V$ is a stronger condition
than is needed for this finite-time argument.

Smoothness alone does not guarantee global existence. For $m=1$,
$V(q)=-q^4/4$, $q_0>0$ and $v_0=q_0^2/\sqrt2$, the zero-energy
solution
$$q(t)=\frac{q_0}{1-q_0t/\sqrt2}$$
escapes to infinity at $t=\sqrt2/q_0$. A force singularity can also
stop a classical solution: for example, a radial attractive Kepler
trajectory can reach $r=0$ in finite time. A rule for continuing through
the singular point is further data.

In three dimensions the Lorentz force, with a static scalar potential
and a static magnetic field, gives
$$
 \dot q=v,\qquad m\dot v=-\nabla V(q)+e\,v\times B(q).
$$
It is not a force depending on position alone. If $\nabla V$ and $B$
are defined and locally Lipschitz on all of $\mathbb R^3$, the full
phase-space vector field is locally
Lipschitz, so local existence and uniqueness still hold. Moreover
$v\cdot(v\times B)=0$, hence the conservative energy is conserved. If $V$ is
bounded below, the same speed and position bounds as above prove global
existence and uniqueness, even if $B$ is not globally bounded.

For instance, if $V$ is constant and $B=B_0\hat z$, the field rotates the transverse
velocity with cyclotron frequency $eB_0/m$ and leaves the longitudinal
velocity constant. A velocity-dependent force is thus not an exception
to the ODE theory; its dependence must be included in the phase-space
vector field being estimated.

If $B=\nabla\times A$ on $\mathbb R^3$, the quantum Hamiltonian is
$$H_{\hbar,A}=\frac1{2m}(-i\hbar\nabla-eA(q))^2+V(q).$$
The kinetic momenta generally do not commute:
$[\pi_i,\pi_j]=i\hbar e(\partial_iA_j-\partial_jA_i)$.
A positive scalar Brownian-bridge density does not directly cover this
magnetic problem: a magnetic Euclidean representation contains a phase.
The [coherent-packet theorem](quantum-blocks-construct-newton.md) treats the scalar Hamiltonian; it does not prove this magnetic extension.

An endpoint problem fixes $q(0)$ and $q(T)$ rather than initial velocity.
It has a separate possible singularity. For the harmonic oscillator the
full phase-space derivative is
$$
 \begin{pmatrix}
 \cos\omega T&\sin(\omega T)/\omega\\
 -\omega\sin(\omega T)&\cos\omega T
 \end{pmatrix},\qquad \det=1.
$$

The position response to initial velocity is
$\sin(\omega T)/\omega$. It vanishes at a conjugate time while the full
phase-space map stays invertible. The corresponding endpoint action
Hessian can fail to invert even though the initial-value motion remains
unique. The time-blocking note gives a finite-polygon determinant that
approaches this singularity under refinement.

Therefore a failure of one position-only generating function is not,
by itself, a failure of Newton's dynamics. A physical completion argument
has to establish which extra information the complete theory needs and
why it cannot be retained classically.

## 5. The conservative arrival criterion

Near zero let $a$ be continuous, odd, positive on $(0,r_0)$, zero at
zero and smooth away from zero. Consider
$$
 \ddot q=a(q),\qquad W(q)=\int_0^q a(s)\,ds\quad(q\ge0),
 \qquad V(q)=-mW(|q|),\quad m>0.
 \tag{L1}
$$

Assume a bounded continuous global extension of the force, smooth away
from zero, by cutting off the potential outside a neighborhood of zero.
The [bounded-cusp argument](newton-cusp-preparation-floor.md), section 1,
then gives global existence and bounds preventing escape. The issue
remaining here is uniqueness, not existence.

Conservation of $E=m\dot q^2/2+V(q)$ follows by the chain rule since
$V\in C^1$. Any solution starting at rest at zero has $E=0$. On a
positive departing segment its velocity must be
$$
 \dot q=\sqrt{2W(q)},\qquad
 \mathcal T(q)=\int_0^q\frac{ds}{\sqrt{2W(s)}}.
 \tag{L2}
$$

**Arrival criterion.** If $\mathcal T(q)=\infty$ for one, hence every
small $q>0$, rest is the unique local solution from $(0,0)$. If
$\mathcal T(q)<\infty$, the inverse $Q=\mathcal T^{-1}$ constructs
departures $q(t)=\pm Q(t-t_0)$ after every waiting time $t_0$.

For the first implication, a nonconstant solution has an excursion of
one sign starting from zero. Its velocity cannot vanish inside that
excursion because $W>0$, and separation of variables would give a
finite value for the divergent integral (L2). For the converse,
$Q'=\sqrt{2W(Q)}$ and $Q''=a(Q)$. Both tend to zero at departure,
so adjoining rest gives a $C^2$ Newton trajectory. Reversing the two
departures supplies two different incoming full states that merge at
zero in finite time, exactly as in the cusp note.

For $a(q)=c q^\alpha$ this test reproduces the familiar $\alpha<1$
nonuniqueness threshold: its integrand is proportional to
$q^{-(1+\alpha)/2}$. The logarithmic family below tests the more delicate
border where no power-law Lipschitz constant exists.

### Exact logarithmic threshold

Fix $\Omega,\ell>0$, $\beta>0$ and put $r=\beta/2$. For sufficiently
small $q>0$, with $L=\log(\ell/q)>\max\{1,r\}$, set
$$
 W(q)=\frac{\Omega^2}{2}q^2 L^\beta,\qquad
 a(q)=\Omega^2q\bigl(L^\beta-rL^{\beta-1}\bigr).
 \tag{L3}
$$

Extend $a$ oddly near zero and the potential with a smooth cutoff
farther out. This gives a bounded $C^1$ potential and continuous
bounded force; $a(0)=0$ since $q L^\beta\to0$. Its derivative on the
positive side is
$$
 a'(q)=\Omega^2\left[L^\beta-\frac{3\beta}{2}L^{\beta-1}
              +\frac{\beta(\beta-1)}2L^{\beta-2}\right],
 \tag{L4}
$$

which diverges for every $\beta>0$. Thus none of these forces is
locally Lipschitz at zero.

Nevertheless the energy-zero speed and arrival integral are exact:
$$
 \dot q=\Omega qL^r,\qquad
 \mathcal T(q)=\frac1\Omega\int_L^\infty u^{-r}\,du.
 \tag{L5}
$$

Consequently rest is unique for $\beta\le2$. For $\beta>2$,
$$
 \mathcal T(q)=\frac{L^{1-r}}{\Omega(r-1)},\qquad
 Q(t)=\ell\exp\left(-[\Omega(r-1)t]^{-1/(r-1)}\right).
 \tag{L6}
$$

The formula for $Q$ is valid until the departure leaves the region
where (L3) is used. It is flat to every order at $t=0$, so an exactly
resting body and one that leaves after a delay satisfy the same
Newton equation and initial data.

For $\beta\le2$ the *whole* extended IVP is unique. Away from zero
this is ordinary local Lipschitz uniqueness. At zero with nonzero
initial velocity, the conserved-energy first-order equation has a
nonzero square root and a $C^1$ right-hand side near the crossing, so
it gives unique passage. At zero velocity the arrival criterion applies.
Bounded force then gives a global reversible point flow. Its dependence
on initial state is continuous: common finite-time bounds give
compactness for any converging initial sequence; every subsequential
limit solves the same unique IVP. Thus all subsequences have the same
limit. A divergent local slope has not destroyed reversible mechanics.

At the borderline $\beta=2$, the outgoing energy-zero solution from
$q_0>0$ is particularly informative:
$$
 q(t)=\ell\left(\frac{q_0}{\ell}\right)^{e^{-\Omega t}},
 \qquad \dot q(0)=\Omega q_0\log(\ell/q_0).
 \tag{L7}
$$

While it remains in the logarithmic region, it stays continuous as
$q_0\downarrow0$ at every fixed finite time,
although its position sensitivity diverges. This is a genuine example
of unique stable motion without a Lipschitz dependence bound at rest.

The general first-order Osgood sufficient test applied directly to a
modulus of size $s[\log(1/s)]^\beta$ reaches only $\beta\le1$.
The stronger range $1<\beta\le2$ above uses the conservative Newton
structure and energy; failure of that first-order sufficient test is
not a proof of nonuniqueness.

### What one moving orbit determines about rest

**6.1 Sol Max, 2026-11-18.** In the 1713 *Principia*, Lemma X,
Corollary 4 relates initial displacement divided by time squared to
force. Proposition VI invokes it for the departure from an orbital
tangent. The following is a modern question about the same quadratic
coefficient. Can it converge uniformly under refinement even though a
body at rest has several continuations? We use a diameter orbit.
Proposition VI's geometric ratios are defined at positive radius.
[Newton, 1713, Book I](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00082)
(Lemma X and Proposition VI, passages).

Write the force as $m\mathbf a(q)$, with $m>0$. On a compact region
$K$ where $\mathbf a$ is continuous, let $\omega_K$ be its modulus of
continuity. Every exact orbit staying in $K$ at speed at most $V$ obeys

$$
 \left|\frac{2[q(t+s)-q(t)-s\dot q(t)]}{s^2}
                 -\mathbf a(q(t))\right|\le \omega_K(Vs). \tag{D1}
$$

The quotient averages the acceleration with the unit-mass weight
$2(s-u)/s^2$ on $0\le u\le s$. This is the integral form of
Newton's equation in (1). Thus even for a family of trajectories the
coefficient converges uniformly, with the same bound on every inserted
cell of duration $s$.

Now take $\mathbf a(q)=a(r)q/r$ for $0<r\le r_0$ and
$\mathbf a(0)=0$, where $a$ is continuous, $a(0)=0$, $a\ge0$,
and $W(r)=\int_0^r a(u)\,du>0$ for $r>0$. The magnitude $a$ may
oscillate. Start a radial solution $x_v$ at the centre with any
speed $v>0$. Its radius increases uniquely by
$\dot x_v=\sqrt{v^2+2W(x_v)}$. Take $H>0$ small enough that
$x_v(H)\le r_0$ and $\dot x_v\le 2v$. Define the dimensionless
excess over the inertial tangent and a sum with units of time by

$$
 d(s)=\frac{x_v(s)-vs}{vs},\qquad
 t_n=2^{-n}H,\qquad
 S_v(H)=\sum_{n=0}^\infty\frac{t_n}{\sqrt{d(t_n)}}. \tag{D2}
$$

**Criterion.** Rest at the centre is the unique forward motion locally
if $S_v(H)=\infty$. If $S_v(H)<\infty$, a body can wait for any time
and then leave along any ray. More precisely, the zero-energy travel
time $\mathcal T$ in (L2) obeys

$$
 \frac{S_v(H)}8\le \mathcal T(x_v(H))
            \le\frac{2}{\sqrt3} S_v(H). \tag{D3}
$$

The rest criterion in (L2) is the usual conservative quadrature.
Angular momentum from rest is zero, so every departing excursion
lies on a ray. Comparison (D3) uses positions of the moving orbit
alone, with no differentiation of its tangent excess. [López Pouso,
2005](https://doi.org/10.1112/S0024610705006319) (abstract, general
scalar existence criterion).

To prove (D3), put $z(s)=\dot x_v(s)/v-1$. Outward acceleration gives
nondecreasing $0\le z\le1$. Its average $d(s)$ satisfies
$z(s/2)/2\le d(s)\le z(s)$ and is nondecreasing. Changing variables
$r=x_v(s)$ in (L2) gives

$$
 \mathcal T(x_v(H))
   =\int_0^H\frac{1+z(s)}{\sqrt{z(s)[2+z(s)]}}\,ds .
$$

For $0\le z\le1$ the factor $(1+z)/\sqrt{2+z}$ lies between
$1/\sqrt2$ and $2/\sqrt3$. If $I_d=\int_0^H ds/\sqrt{d(s)}$
and $I_z=\int_0^H ds/\sqrt{z(s)}$, the average bounds give
$I_z\le I_d\le2\sqrt2 I_z$. On $[t_{n+1},t_n]$, the endpoint
values of $1/\sqrt d$ bracket the integrand. Summing the two bounds
gives $S_v(H)/2\le I_d\le S_v(H)$ and proves (D3), including the
divergent case. The improper integral also equals the supremum of
lower sums on compact subintervals of $(0,H]$. Its finiteness is
independent of choosing dyadic subdivisions and of the nonzero speed
chosen in (D2).

For the force in (L3) let $L_s=\log(\ell/(vs))$. Since
$x_v(s)/(vs)\to1$, energy gives
$z(s)\sim\Omega^2s^2 L_s^\beta/2$. Averaging gives
$d(s)\sim\Omega^2s^2 L_s^\beta/6$, using
$\int_0^s u^2 L_u^\beta du\sim s^3 L_s^\beta/3$.
The terms of (D2) are therefore asymptotic to
$\sqrt6/(\Omega[L_H+n\log2]^{\beta/2})$.
Every member of the family has the uniform finite-force limit (D1).
The sum diverges for $0<\beta\le2$ and converges at every $\beta>2$,
where even an arbitrarily delayed departure obeys that same limit.
Here $r_0,\ell$ are lengths, $H$ is a time, $v,V$ are speeds and
$\Omega$ is an inverse time. Both outcomes occur in classical
mechanics with no action parameter.

### Two central forces with the same positions at successive half-times

Keep the work primitive $W(r)>0$ for $r>0$ and allow the radial
acceleration to reverse sign. The positions, velocities and accelerations
of a moving solution at the whole sequence $t_n=2^{-n}H$ can then agree
for two force laws whose solutions from rest have different uniqueness
properties. This pair uses autonomous potentials fixed across all $n$.

Fix $H,v,m>0$. Prescribe two increasing radius functions by
$x_i(t)=v\int_0^t(1+z_i(s))\,ds$ on $[0,H]$, starting with
$z_1(t)=(t/H)^{3/2}$. In each $I_n=[t_n/2,t_n]$ set
$u=2t/t_n-1$. Use the smooth step
$g(s)=\rho(s)/(\rho(s)+\rho(1-s))$, where $\rho(s)=e^{-1/s}$
for $s>0$ and is zero otherwise. Put
$\chi(u)=g(8u-1)g(5-8u)$ and $\psi(u)=8g'(8u-6)$.
Then $0\le\chi\le1$ is one on $[1/4,1/2]$, while the nonnegative
$\psi$ has disjoint support and integrates to one. Set

$$
 \begin{split}
 b_n&=\frac{2}{t_n}\int_{I_n}\chi(2s/t_n-1)
                     [z_1(s)-(s/H)^2]\,ds,\\
 z_2(t)&=(1-\chi(u))z_1(t)+\chi(u)(t/H)^2+b_n\psi(u).
 \end{split} \tag{D4}
$$

The subtracted and added integrals are equal on each $I_n$. Hence
$x_1(t_n)=x_2(t_n)$ by summing the intervals down to zero.
Both $z_i$ coincide in a neighbourhood of each node, so the speeds
and accelerations there also agree. Inside the interval,
$0\le b_n\le(t_n/H)^{3/2}$ and $z_2>0$. Differentiation gives
$|z_2'|\le C(t_n/H)^{1/2}/H$ with
$C=2(1+\|\chi'\|_\infty+\|\psi'\|_\infty)$.
Both $z_i$ thus extend to $C^1$ functions with value and derivative
zero at $t=0$.

Since $x_i'\ge v$, the assignments

$$
   a_i(x_i(t))=v z_i'(t),\qquad
   W_i(x_i(t))=v^2 z_i(t)(1+z_i(t)/2)
$$

define continuous accelerations with $a_i(0)=0$ on the same radial
interval. The second identity follows from $W_i'=a_i$ and $W_i(0)=0$.
The potentials $-mW_i(|q|)$ are $C^1$ at the origin. They admit
bounded-force extensions past the common outer radius. The first force
points outward. The second must turn inward on each sufficiently small
cell to reach $(t/H)^2$ from the larger $z_1(t_n/2)$, then turns
outward again.

For the first force (L2) is finite since $\int_0^H(t/H)^{-3/4}dt$
is finite. For the second, on the plateau $1/4\le u\le1/2$ one has
$1/\sqrt{z_2(t)}=H/t$. Its integral contributes at least $H/8$
on each cell. The travel-time integrand in the proof of (D3) is at
least $1/\sqrt{2z_2}$, so (L2) diverges. Thus the first force admits
arbitrary waiting followed by departure, while the second has unique
rest. Inserting a time inside a modified cell can distinguish the two
moving curves. Knowing the complete moving curve even determines
$W(x_v(t))=(\dot x_v(t)^2-v^2)/2$. Equality here concerns one
particular nested sequence accumulating at the initial instant.

### Crossing times and arbitrary-mesh polygons

Let $q_n=\ell e^{-n}$ with $n$ sufficiently large. Along the zero-energy
trajectory, the time for the annulus $q_{n+1}<q<q_n$ is
$$
 \tau_n=\frac1\Omega\int_n^{n+1}u^{-r}\,du,
 \qquad \tau_n\sim\frac1{\Omega n^r}.
 \tag{L8}
$$

On this annulus the local acceleration slope bound is of order
$\Lambda_n=\Omega^2n^\beta$. The short-cell scale
$\Lambda_n^{-1/2}$ is therefore of the same order as $\tau_n$.
One can subdivide an annulus crossing into a fixed number of shorter
steps to obtain a small local Lipschitz amplification parameter.
There is no uniform slope bound across all annuli.

The issue is whether infinitely many controlled annulus crossings
can fit into finite physical time:
$$
 \sum_{n\ge N}\tau_n
 \begin{cases}
 =\infty,&\beta\le2,\\
 <\infty,&\beta>2.
 \end{cases}
 \tag{L9}
$$

For $\beta\le2$, a zero-energy trajectory cannot reach the infinite-depth
boundary at zero in finite time. For $\beta>2$, perfectly regular
motion on each finite collection of annuli reaches that boundary in
finite time, and the branch datum is missing there. Local estimates
at every finite scale do not by themselves control their infinite
composition. This is the useful multiscale connection with the
Balaban lesson; it is not a transfer of his field-theory proof.

For the unique regime, arbitrary-mesh Euler polygons, and the lesson's
mixed kick--drift polygons, converge uniformly on every fixed finite
time interval. Bounded force gives common position and momentum bounds;
uniform continuity gives a vanishing integral residual; compactness
supplies solution subsequences; uniqueness makes the whole family
converge. No $O(\text{mesh})$ rate is asserted here.

In the nonunique regime, exact zero initial data make these deterministic
polygons remain at rest on every partition. However, preparations
$q_0\downarrow0$, $\dot q_0=\Omega q_0L_0^r\downarrow0$ have
$$
 L(t)=\left[L_0^{1-r}+\Omega(r-1)t\right]^{-1/(r-1)}
       \longrightarrow [\Omega(r-1)t]^{-1/(r-1)}.
 \tag{L10}
$$

Thus they converge to the nonzero departure (L6) at fixed small $t>0$.
For each positive $q_0$, choose a fine enough polygon to approximate
that regular trajectory; a diagonal sequence then has vanishing mesh
and vanishing initial error but a departing limit. Refinement is not
jointly stable with preparation refinement at zero. This is a stronger
failure than an unbounded numerical error estimate, while keeping the
exact-zero polygon's resting limit explicit.

### Vanishing local action and a quantum residual

The positive outgoing momentum is $p(q)=m\Omega qL^r$. Its canonical
action from zero to $q$ is
$$
 \mathcal J(q)=\int_0^q p(s)\,ds
       =m\Omega\ell^2\int_L^\infty e^{-2u}u^r\,du.
 \tag{L11}
$$

For $L>r/2$, elementary bounds give
$$
 \frac{m\Omega}2q^2L^r
 \le\mathcal J(q)
 \le\frac{m\Omega q^2L^r}{2-r/L}.
 \tag{L12}
$$

The lower bound uses $u^r\ge L^r$; the upper bound uses
$(L+v)^r\le L^r e^{rv/L}$ after writing $u=L+v$. Therefore
$\mathcal J(q)\sim(m\Omega/2)q^2L^r\to0$ for every $\beta>0$.
The temporal threshold (L9) creates no positive action threshold.

There is still a concrete quantum comparison. In the local region
$V=-p(q)^2/(2m)$, take the stationary energy-zero test functions
$$
 \psi_\pm(q)=p(q)^{-1/2}
          \exp\left(\pm\frac{i}{\hbar}\mathcal J(q)\right),
 \qquad H_\hbar=-\frac{\hbar^2}{2m}\frac{d^2}{dq^2}+V(q).
 \tag{L13}
$$

Their eikonal and first-derivative transport terms cancel exactly.
Writing $b(q)=p(q)^{-1/2}$ gives $H_\hbar\psi_\pm
=-(\hbar^2/2m)b''e^{\pm i\mathcal J/\hbar}$ and the exact local ratio
$$
 \frac{|H_\hbar\psi_\pm|}{|V\psi_\pm|}
 =\left[\frac{\hbar}{m\Omega q^2L^r}\right]^2
       \left|\frac34-\frac rL+\frac{r(r+2)}{4L^2}\right|
 \sim\frac{3\hbar^2}{16\mathcal J(q)^2}.
 \tag{L14}
$$

For example, the differentiation behind this identity is
$p'/p=(1-r/L)/q$ and
$p''/p=-r[1-(r-1)/L]/(q^2L)$; then
$b''/b=3(p'/p)^2/4-p''/(2p)$.
Equation (L14) is a local residual identity, not an error bound for
a normalized state or the full propagator.

At fixed $\hbar>0$, action comparable with $\hbar$ makes the local
residual of this trajectory ansatz order one even in the classically
unique regime. Every
sufficiently small positive $\hbar$ defines a radius $q_\hbar$ by
$\mathcal J(q_\hbar)=\hbar$, and that radius tends to zero as
$\hbar\to0$. The bounded-potential Hamiltonian has global unitary
dynamics at each positive $\hbar$ by the cusp note's held
Kato--Rellich input. These facts neither require $\hbar=0$ to be a
member of the same state theory nor select a positive numerical lower
bound across the family. No relativistic ingredient or $c$ is used.

## 6. Consequence for STATE

Initial-value construction, continuation, endpoint caustics and finite-time
mergers have different hypotheses. Unbounded force slope alone establishes no
merger and no action floor. Uniform convergence of the Lemma X coefficient
holds even at a centre that admits delayed departures. For outward radial
forces (D2) decides uniqueness from one moving orbit. The sign-changing
counterexample (D4) delimits that inference. The [cusp preparation theorem](newton-cusp-preparation-floor.md)
uses an actual full-state merger and additional preparation laws. The separate
[endpoint blocking argument](balaban-newton-time-blocking.md) retains inverse
Hessians, normalization and source response; the
[nonlinear cell](newton-nonlinear-time-cell.md) controls a supplied positive
weight. Neither operation follows solely from constructing a classical orbit.
