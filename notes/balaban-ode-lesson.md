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

At a point of nonzero speed and curvature, one finite inward force
gives opposite continuum orbits for the two orders of an impulse and a
free flight. A nonnegative spherical gravitating source restores unique
nonradial motion. For the branching force, uniform agreement of the
canonical products over a set of trial actions is equivalent to a
positive infimum of that set. A positive lower width for classical
ensembles gives the same refinement property. For the shrinking Gaussian
preparations the two theories also give the same probabilities for
each of the two limiting radii. The odds change when the impulse
interval is comparable to the position width times its squared logarithm.

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

## Tangent orbits under the two impulse orders

**6.1 Sol Max, 2026-11-18.** Newton used uniqueness in Book I,
Proposition XIII, Corollary 1. In 1687 he stated the converse from an
inverse-square force to a conic. On 11 October 1709 he sent Cotes the
additional sentences about curvature and mutually tangent orbits. They
appear in 1713. In 1726 he made the role of the body's speed explicit
twice in the added argument. All three versions give the launch speed
at the outset. Corollary 2 expressly excepts straight descent to the
centre. Proposition VI connects the orbital force to the short-time
displacement of Lemma X. These are claims about inverse-square conics
in Proposition XIII. Extending the uniqueness inference to a general
finite inward force is a mathematical question.
[1687, XIII.1](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00077#par109),
[1713, XIII.1](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00082#par140)
and [1726, XIII.1](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00087#par130)
(diplomatic passages). [Letter to Cotes and edition comparison](../docs/Newton_Principia_Motte1846.md#corollary-1-to-proposition-xiii).
Guicciardini discusses this revision in [*Reading the Principia*,
§8.6.2.1](https://doi.org/10.1017/CBO9780511524752) (historical analysis, passage).

### A circle with two tangent departures

Use length $R>0$, inverse time $\omega>0$ and inertial mass $m>0$.
In this section positions are in units $R$, times in $1/\omega$,
momenta in $mR\omega$ and energies in $mR^2\omega^2$. Write $r=|q|$.
Launch in the plane at $q_0=(1,0)$ with $v_0=(0,1)$. Specific angular
momentum in these units is one. The acceleration is $-g(r)q/r$. Fix
$b=e^{-20}$ and on $|y|=|r-1|\le b$ set

$$
 g(r)=r^{-3}-\alpha(y),\qquad
 \alpha(y)=y(L^4-2L^3),\quad L=\log(1/|y|),\qquad \alpha(0)=0. \tag{C1}
$$

The odd $\alpha$ is strictly increasing there since its derivative off zero
is $L^2(L^2-6L+6)>0$. Also $\alpha(b)<1/4$. Hence $g$ is positive and
strictly decreasing on the annulus. Extend $g$ linearly from zero to
$g(1-b)$ on the inside and by $g(1+b)(1+b)^2/r^2$ outside. This is
one continuous inward force, bounded by $3$ in acceleration units,
with a bounded $C^1$ potential $U$, $U'=g$. Its magnitude on the
departing outward branch decreases continuously near the join.

The same force occurs as a reciprocal interaction in a closed
Newtonian two-body Hamiltonian. Take positive inertial masses $m_1,m_2$
with reduced mass $m$ and pair potential
$mR^2\omega^2 U(|q_1-q_2|/R)$ in dimensional positions. The centre
of mass moves freely and the relative motion is exactly (C1).

The radial equation and angular velocity are $y''=\alpha(y)$ and
$\theta'=r^{-2}$. At the common energy, $|y'|=|y|L^2$ once $y\ne0$.
Besides the circle, either radial branch can leave after any waiting
time $s$. Their radii for $t>s$ are

$$
 r(t)=1\pm Y(t-s),\qquad Y(u)=e^{-1/u}\quad(u>0), \tag{C2}
$$

until $Y=b$. This is the logarithmic example (L3) translated to a
circular orbit by the centrifugal term. Integrating $r^{-2}$ gives
the angle with the common value at $s$. All time derivatives of the
two motions agree with the circle at the join. In physical units the
speed is $R\omega$, the acceleration magnitude is $R\omega^2$ and
the curvature is $1/R$ there. The same entire incoming arc, angular
momentum, energy and short-time force coefficient admit both futures.

### Which orbit the polygons select

Fix $0<T<1/40$ in the same time units and set $h=T/N$. Use exactly
the drift and kick of (2), with the same force and initial point in
each run. Drifting first converges to $r=1+Y(t)$. Kicking first
converges to $r=1-Y(t)$ on $[0,T]$. The order difference survives in
a position at a fixed positive time.

For either constant ordering the vertices satisfy
$q_{n+1}-2q_n+q_{n-1}=-h^2g(r_n)q_n/r_n$ at interior vertices and
$q_n\wedge q_{n+1}=h$. Here the wedge is the signed planar determinant.
The drift-first first radius is $\sqrt{1+h^2}$ and the kick-first one
is $\sqrt{1-h^2+h^4}$. Write $s_n=\pm(r_n-1)$, with the plus
sign for drift first. In both cases $s_0=0$ and $s_1\ge h^2/4$.

Velocities have norm at most $1+3T<2$ and the broken lines stay
within $2T$ of $q_0$. Compactness and the integral-equation residual
from §3, using the force's uniform continuity there, make every
subsequential limit an exact solution. Such a solution needs at least
$\int_0^b du/[u\log^2(1/u)]=1/20$ to leave the annulus, by the
radial energy integral. Thus all vertices lie in its interior for
large $N$. Compactness alone has yet to choose a branch.

Let $z=h^2/r_n^2$ and $B(w,z)=(w+\sqrt{w^2-z})^{-1}$. The radial
projection of $q_{n\pm1}$ on $q_n/r_n$ is
$\sqrt{r_{n\pm1}^2-z}$ by the determinant identity. The positive root
applies throughout the ball about $q_0$. Therefore

$$
 \frac{r_{n+1}-2r_n+r_{n-1}}{h^2}
 =-g(r_n)+\frac{B(r_{n+1},z)+B(r_{n-1},z)}{r_n^2}
 =\alpha(r_n-1)+e_n,\qquad |e_n|\le350h^2 . \tag{C3}
$$

For the constant, each neighbour differs in radius by at most $2h$.
Taylor's formula for $|q|$, with Hessian norm at most $2$ in the
ball, bounds the radial second difference by $(3+8)h^2$. For
$w\ge1/2$, $|B(w,z)-1/(2w)|\le z/(2w^3)\le16h^2$.
The first two derivatives of $1/(2w)$ have magnitude at most $2$ and
$8$. Summing its two Taylor expansions about $r_n$ costs at most
$(22+32)h^2$. Multiplication by $r_n^{-2}\le4$ gives (C3).

Since $\alpha(h^2/4)/h^2\to\infty$, induction in (C3) gives positive
increments of $s_n$ and second difference at least $h^2\alpha(s_n)/2$.
From level $w$, reaching $2w$ costs at most $2\sqrt{w/\alpha(w)}+h$
in time, by summing this lower acceleration until the level is reached.
For a fixed small $0<d<b/2$ use levels $w=d2^{-k}$. The mesh
contribution to the time to $d$ is at most
$h[2+\log_2(4d/h^2)]$ for sufficiently small $h$. The rest is at most

$$
 2\sqrt2\sum_{k\ge1}[\log(1/d)+k\log2]^{-2}
 \le \frac{2\sqrt2}{\log2\,\log(1/d)} . \tag{C4}
$$

For every $t>0$ first choose $d$ so the latter bound is less than
$t$, then take $h$ small. The signed radius has reached $d$ by $t$.
Every limit therefore departs immediately on its prescribed side.
The energy integral gives precisely (C2) with $s=0$, and the angular
equation fixes the full curve. This identifies every subsequential
limit. The closure on full classical histories in the
[cusp construction](newton-cusp-preparation-floor.md) retains the
branch as state information.

### What a nonnegative spherical source supplies

Newton's shell theorem gives a physically independent restriction on
the force law. Return to dimensional variables. Let $G>0$ and let
$M(r)$ be the enclosed mass of a finite nonnegative spherical source,
continuous at $r>0$, with $0<M(\infty)<\infty$. A point mass at zero
is allowed. The inward acceleration is $g(r)=GM(r)/r^2$. For every
nonzero specific angular momentum $j=|q\wedge\dot q|$, this force has
a unique global trajectory from each nonradial point state, including
when the radial speed vanishes. No derivative bound on the density is
needed. [Newton, 1713, Book I, Propositions LXX–LXXI](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00082#par469)
(spherical shell theorems, passages).

Write $\Phi'=g$, $\Phi(\infty)=0$ and
$U_j(r)=j^2/(2r^2)+\Phi(r)$ for the energy per unit mass at a radial
turn. Its unique stationary radius $R_c$ satisfies $GR_c M(R_c)=j^2$:
$rM(r)$ increases strictly wherever $M(r)>0$. For every $r>0$,
monotonicity of the enclosed mass gives
$\Phi(r)-\Phi(R_c)\ge GM(R_c)(1/R_c-1/r)$ on either side of $R_c$.
Consequently

$$
 U_j(r)-U_j(R_c)\ \ge\ \frac{j^2}{2}
               \left(\frac1r-\frac1{R_c}\right)^2 . \tag{C5}
$$

A point source attains equality. Starting at the circular energy
forces $r=R_c$. Elsewhere a radial turning point is simple, and its
nonzero radial acceleration fixes the continuation by the energy
quadrature. With nonzero radial velocity the same quadrature determines
the motion directly. Finally $U_j(r)\ge j^2/(2r^2)-GM(\infty)/r$
keeps every finite-energy orbit away from zero. The speed is bounded
on that exterior region, giving global continuation.

For (C1), $r^2g(r)<1$ just outside the unit circle while $g(1)=1$.
Its dimensionless Poisson density $(r^2g)'/(4\pi r^2)$ is signed.
It is constant in the core, zero beyond $1+b$ and integrable to
every finite power in the shell. Indeed the sole unbounded factor
there grows as $\log^4(1/|r-1|)$ and the integral for its $p$th
power is bounded by a constant times
$\int_{20}^{\infty} L^{4p}e^{-L}dL$. Continuity of $r^2g$ excludes
a surface delta at the joins. The squared field integral
$4\pi\int_0^\infty r^2g(r)^2dr$ is finite. Thus integrability of
the signed source and finiteness of its field integral allow the
order dependence in (C3).

This uniqueness survives source and time refinement together. Let
$M_k\to M$ uniformly on compact radial intervals in $(0,\infty)$ for
continuous enclosed masses as above. Fix the initial nonradial state
and a finite time interval. Choose an annulus containing the whole
limiting orbit strictly in its interior. Cut off all forces beyond a
slightly larger annulus with the same cutoff, equal to one on the first.
They now converge uniformly to a continuous bounded field.
The §3 compactness argument, with the uniform force difference added
to the residual, applies to arbitrary positive time partitions and
arbitrary choices of impulse order. Every limit follows the unique
orbit up to any first exit, which the orbit never makes. The original
polygons thus have the same limit along every joint refinement.
For a point source [the fixed-time Coulomb estimate, §5a](self-sufficiency-contrast.md)
also takes a supplied reduced action to zero at fixed noncollisional
initial position and momentum. Holding the nonzero angular momentum of
the orbit fixed is compatible with this limit.

### Uniform refinement over a set of trial actions

Use (C1) again, in its dimensionless variables. The fixed terminal
time is $T/\omega$ and an equal time cell lasts $h/\omega$ in physical
units. The dimensional reference action is $S_0=mR^2\omega$. Write $\epsilon=a/S_0$ for a
trial reduced action $a$. For $\epsilon>0$ take the canonical kinetic
and potential operators on $L^2(\mathbb R^2)$, $P=-i\epsilon\nabla$,
and the normalized state

$$
 \psi_\epsilon(x)=(\pi\epsilon)^{-1/2}
 \exp[-|x-q_0|^2/(2\epsilon)+i v_0\cdot(x-q_0)/\epsilon].
$$

Its coordinate and momentum standard deviations per component in
physical units are $R\sqrt{\epsilon/2}$ and
$mR\omega\sqrt{\epsilon/2}$. Use the same state for either impulse
placement. Fix a smooth radial function $0\le f\le1$, equal to zero
for $r\le1-Y(T)/2$ and one for $r\ge1+Y(T)/2$. Its transition width
in physical units is $R Y(T)$, independent of the partition and action.
Thus changing $a$ changes the preparation widths while the spatial
readout and its terminal time stay fixed.
For a step $s$ write $K_s=e^{-isU(Q)/\epsilon}$ and
$D_s=e^{-isP^2/(2\epsilon)}$. For each positive partition $\pi$ of
$[0,T]$ and a choice $\sigma$ of the order in every cell, let
$p_{a,\pi,\sigma}$ be the final expectation of $f(Q)$. At $a=0$ use
the two classical factors (2) on the point $(q_0,v_0)$ and evaluate $f$.

For any nonempty set $A\subset[0,\infty)$ of dimensional trial actions,
the following dichotomy holds for this one force, initial family and $f$:

$$
 \lim_{\delta\downarrow0}
 \sup_{\substack{a\in A,\ |\pi|\le\delta\\\sigma,\sigma'}}
 |p_{a,\pi,\sigma}-p_{a,\pi,\sigma'}|
 =\begin{cases}0,&\inf A>0,\\1,&\inf A=0.\end{cases} \tag{C6}
$$

**Arbitrarily small action.** At a fixed finite partition a localized
state follows its classical product as $a\downarrow0$. For the drift
this follows from the exact shear $Q\mapsto Q+sP$. A kick shifts
$P$ by $-s\nabla U(Q)$. For a state of unit norm localized near $q$
and any $l>0$, the norm of its force fluctuation is bounded by

$$
 \|[\nabla U(Q)-\nabla U(q)]\psi\|
 \le \omega_{\nabla U}(l)+2\|\nabla U\|_\infty
                                     \|(Q-q)\psi\|/l .
$$

Here $\nabla U$ is bounded and uniformly continuous. Starting with the
Gaussian, induction propagates vanishing position and momentum deviations
for the finitely many factors, first sending $a$ to zero and then $l$
to zero at each step. For all sufficiently fine uniform meshes the
classical terminal radii lie inside the opposite plateaus of $f$, by
(C2)–(C4). If $A$ accumulates at zero, take the small-action limit at
each such mesh within $A$. If $0\in A$ the classical products already
give the unit difference. This proves the second line of (C6).

**Positive action floor.** For fixed $\epsilon>0$ both products have
the same unitary continuum limit. The potential is a bounded real
multiplier. [Trotter, 1959](https://doi.org/10.1090/S0002-9939-1959-0108732-6)
(product formula). For the required uniformity, put
$B_\epsilon(t)=D_{-t}U(Q)D_t/\epsilon$. In the interaction picture
each split product evolves with $B_\epsilon$ frozen at the chosen
endpoint of each cell. On any compact positive $\epsilon$ interval
these operators are uniformly bounded and jointly strongly continuous
in $t,\epsilon$. The exact interaction-picture vector
$w_\epsilon(t)$ is norm-continuous in both variables by its integral
equation with bounded generator and the norm-continuous initial Gaussian.
Duhamel bounds the product error by

$$
 T\sup_{|s-t|\le\delta}
        \|(B_\epsilon(s)-B_\epsilon(t))w_\epsilon(t)\|.
$$

This tends uniformly to zero on the compact parameter interval.
For the large-$\epsilon$ tail, each split product differs from free
evolution by at most $T\|U\|_\infty/\epsilon$ in operator norm, by
telescoping. These bounds prove the first line of (C6).

The order effect also has a definite scale on equal cells $h=T/N$.
The products satisfy $(K_h D_h)^N=K_h(D_h K_h)^N K_h^{-1}$. Since
$f(Q)$ commutes with the final kick, their score difference is bounded
by the pure-state trace distance between $\psi_\epsilon$ and
$K_h^{-1}\psi_\epsilon$. Removing the phase $hU(q_0)/\epsilon$ bounds
this distance by $3h/\sqrt\epsilon$ using (C1) and the initial spatial
rms width. More precisely, if $h,\epsilon\to0$ with
$h/\sqrt\epsilon\to\lambda<\infty$, write $x=q_0+\sqrt\epsilon\,y$.
Differentiability at $q_0$, where $\nabla U(q_0)=(1,0)$, and dominated
convergence give overlap modulus $e^{-\lambda^2/4}$ by the Gaussian
Fourier transform. Thus the limiting upper bound on the score
difference is $\sqrt{1-e^{-\lambda^2/2}}$. Full separation requires
$a/S_0=o(h^2)$ along a vanishing-action sequence. Conversely (C6)
allows some such sequences. For $a/S_0=h$, the two constant orderings
agree in the limit in the sense that their difference vanishes.
[Pure-state distance](record-distance-path-length.md) (standard identity).

### The same refinement criterion for classical ensembles

Could (C6) by itself establish that the width comes from a physical
quantum of action? Keep the force, the partitions, the two classical
maps, $T$ and $f$ fixed. On classical phase space take the density
$(\pi w)^{-2}\exp[-(|q-q_0|^2+|p-v_0|^2)/w]$ for $w>0$ and the
point state for $w=0$. Each position and momentum marginal matches
the initial quantum one at $w=\epsilon$. Here $w$ is freely supplied
classical dispersion. At every $w$ the evolution uses only Newton's
equation.

For any nonempty width set $B\subset[0,\infty)$ the exact dichotomy
(C6) holds for the classical scores with $A$ replaced by $B$.
If $\inf B=0$, continuity of the finite products takes the concentrated
densities to their point-state answers, so (C3)–(C4) give the unit
difference. For $w>0$, the initial hypersurfaces
$|q\wedge p|=1$ have measure zero. Away from them every orbit is
unique. The field is locally Lipschitz away from $r=1$. At $r=1$,
nonzero radial speed gives unique passage by the energy integral and
zero radial speed gives a simple turn since $r''=|q\wedge p|^2-1\ne0$.
The bounded force then gives convergence of arbitrary refining polygons
for almost every initial state. On $w_0\le w\le w_1$ with $w_0>0$ the
densities have a common integrable Gaussian envelope. Dominated convergence
along any sequence of partitions and placements proves uniform agreement there.

For the remaining tail, every terminal polygon position lies within
$3T^2$ of the free position $q+Tp$, by summing the bounded kicks.
The free position has density bounded by $1/[\pi w(1+T^2)]$.
Whenever it lies outside the disk of radius $1+Y(T)/2+3T^2$
about zero, every ordering gives final score one. The probability of
that disk tends to zero as $w\to\infty$, uniformly in the ordering.

There is a distinct finite-ratio bound for these ensembles. For the
two constant orderings the initial momentum shift is $h\nabla U(q)$
up to sign. At each $q$ the equal-covariance Gaussian total-variation
formula gives $\operatorname{erf}(h|\nabla U(q)|/(2\sqrt w))$.
Averaging over position bounds the score difference. This upper bound
tends to $\operatorname{erf}(\lambda/2)$ at $h/\sqrt w\to\lambda$,
$w\downarrow0$. Both this and the quantum overlap bound concern
possible terminal differences. The next calculation gives the actual
terminal law.
[Devroye, Mehrabian and Reddad, p. 3](https://arxiv.org/pdf/1810.08693#page=3)
(equal-covariance formula).

Newton's letter uses point-state uniqueness in the inverse-square
conic argument. Equation (C5) justifies it classically in
a broader gravitational class. Equation (C6) identifies what would
exclude zero for the specified canonical family. One must independently
admit the force (C1), require agreement of impulse placements uniformly
over allowed actions, and justify the chosen state space and dynamics.
The historical passage supplies none of these extensions.

### Branch probabilities for shrinking Gaussian preparations

**6.1 Sol Max, 2026-11-18.** Keep the force (C1), the initial state,
the radial readout and $0<T<1/40$. Use equal cells $h=T/N$ and write
$\sigma=+1$ for a kick after each flight and $\sigma=-1$ for a kick
before each flight. Put $d=\sqrt{a/S_0}$ in the quantum family and
$d=\sqrt w$ in the classical ensemble. Let $\ell=\log(1/d)$ and take
$d\downarrow0$ and $h\downarrow0$ with $h/(d\ell^2)\to\lambda$,
$0\le\lambda\le\infty$.
For **both** evolutions the terminal radius converges in distribution to

$$
 (1-P_\sigma)\delta_{1-Y(T)}+P_\sigma\delta_{1+Y(T)},\qquad
 P_\sigma=\frac{1+\sigma\,\operatorname{erf}(\lambda/2)}2 .
 \tag{C7}
$$

Here $\operatorname{erf}(+\infty)=1$. In particular $h$ comparable
to $d$ gives equal branch weights in both orders. An order bias
survives at $h$ comparable to $d\ell^2$, and complete separation
holds exactly when $h/(d\ell^2)\to\infty$.

#### Which part of the initial preparation leaves on each side

First suppose $\lambda<\infty$. Let $x=(r_0-1)/d$, let $p_r$ be the
initial radial velocity and let
$\gamma$ be the square of the dimensionless angular momentum per unit
mass. First restrict $x$, $p_r/d$ and $(\gamma-1)/d$ to bounded sets.
During a flight $r''=\gamma/r^3$. At a kick the radial velocity
decreases by $h g(r)$. The determinant calculation (C3), now with
$z=h^2\gamma/r_n^2$ and the two $B$ terms multiplied by $\gamma$,
gives, for $y_n=r_n-1$,

$$
 \frac{y_{n+1}-2y_n+y_{n-1}}{h^2}
   =\alpha(y_n)+\frac{\gamma-1}{r_n^3}+O(h^2),\qquad
 \frac{y_1-y_0}{h}=p_r+h\bigl(\sigma/2+o(1)\bigr).
 \tag{C8}
$$

The second formula follows by taking the length of the first drift
vector, with the initial velocity changed only in the kick-first case.
The error in the first formula is uniform near the circle by the same
Taylor bounds as in (C3). All limiting trajectories stay strictly in
the annulus up to $T$ by (C2) and compactness.

In the variables $Z=y/d$, $u=t\ell^2$ the mesh is $h\ell^2\to0$.
On bounded $Z$ intervals $\alpha(dZ)/(d\ell^4)\to Z$ uniformly,
including at zero, since $|Z|\,|\log |Z||^k$ stays bounded near zero
for each $k\le4$. The other acceleration terms in (C8), divided by
$d\ell^4$, vanish. Thus on every bounded $u$ interval the scaled
positions and their difference quotients converge to the solution
of $Z''=Z$,

$$
 Z(u)=x\cosh u+(\sigma\lambda/2)\sinh u .                       \tag{C9}
$$

Uniformity on compact initial sets follows by summing the recurrence
for position and velocity and applying the Lipschitz estimate for the
limiting linear equation up to exit from a larger bounded interval.
For $|x+\sigma\lambda/2|\ge\eta>0$, (C9) and its derivative have
the sign of $x+\sigma\lambda/2$ and magnitude bounded below at some
fixed $u_*$, uniformly on the restricted set. At that node the signed
radius displacement is at least $c d$, for a fixed $c>0$, and is
increasing. Thereafter its signed second difference divided by $h^2$
is at least $\alpha(|y_n|)/2$, since $\alpha(cd)\gg d+h^2$ and
$\alpha$ is increasing. The level estimate (C4) applies from $cd$.
Its mesh contribution is $O(h\log(1/d))\to0$. Consequently the
limiting orbit leaves immediately on this side. This argument is
uniform for the indicated compact sets, including sets of initial
points which cross the circle during the short interval $u\le u_*$.

For the classical Gaussian, $x$ converges in law to a variable with
density $e^{-x^2}/\sqrt\pi$. The other two scaled initial quantities
are tight, as follows by expanding $q\wedge p$ and the radial
projection of $p$ at $(q_0,v_0)$. The dividing point
$x=-\sigma\lambda/2$ has limiting probability zero. Removing the
cutoffs gives $\Pr(x+\sigma\lambda/2>0)=P_\sigma$. This proves
the classical statement. More generally, if $p_r/(d\ell^2)\to v$,
the coefficient of $\sinh u$ in (C9) is $v+\sigma\lambda/2$.
Varying the impulse bias for this force therefore reads the distribution
of the single variable $x+v$ at its continuity points. Any atomless
law for that variable is realized classically by assigning it to $x$,
taking $v=0$ and fixing $\gamma=1$. Truncating $x$ to
$|x|\le1/(2d)$ keeps all initial radii positive and preserves the limit.

#### Quantum transport through the circle

In polar coordinates the coherent state's only angular factor is
$\exp(r e^{i\theta}/d^2)$. In $L^2(dr)$ the initial radial amplitude
in mode $k\ge0$ is therefore proportional to
$u_k(r)=r^{k+1/2}\exp(-r^2/(2d^2))$. Integrating these squared
amplitudes with their Fourier coefficients gives Poisson weights of
mean $d^{-2}$ for $k$. Every factor preserves $k$, and a radial
observable is diagonal in these modes. Discarding $|d^2k-1|>Md$
costs at most $M^{-2}$ in probability. The radial kinetic operator
in a retained mode is

$$
 -\tfrac12 d^4\partial_r^2+\frac{\gamma}{2r^2},
 \qquad \gamma=d^4(k^2-1/4)=1+O_M(d).
$$

Use smooth compact cutoffs in $x=(r-1)/d$ on the two sides of the
dividing point, leaving out $|x+\sigma\lambda/2|<\eta$. The initial
phase in each mode is constant. For either cutoff radial amplitude
$A_0$ and $j=0,1,2$ we have $\|\partial_r^j A_0\|\le C d^{-j} n_k$,
where $n_k$ is the norm of the full initial mode including its Fourier
coefficient. This follows by differentiating $u_k$ on $r=1+O(d)$
with $d^2k=1+O_M(d)$. Constants below may depend on these fixed
cutoffs, $T$ and a finite upper bound for $h/(d\ell^2)$.

Some rays cross $r=1$ before leaving. To control the wave at that
crossing, set $s=d/\ell$. In $\alpha$ replace $L(y)$ inside $|y|<s$
by $\log(1/s)+b_0(y/s)$ with $b_0$ smooth and even, zero for
$|y/s|\le1/2$ and equal to $\log(1/|y/s|)$ for $|y/s|\ge 1$,
with a smooth transition. Denote the modified potential by $\widetilde U$.
Its additive constant can be chosen so that it agrees with $U$ on
both sides of the strip, since the change of its derivative is odd
in $y$. Expanding the fourth power and using the bound on
$|Z|\,|\log |Z||^k$ gives

$$
 \|\widetilde U-U\|_\infty\le C s^2\ell^3 .
 \tag{C10}
$$

The modified forces converge uniformly to the original one and obey
the same scaled force limit in (C9). Thus all the retained rays of
the modified problem reach their prescribed branch, also for
$p_r=0$ and the modal $\gamma$ above.

Here are the uniform transport estimates needed to apply time-dependent
WKB to these shrinking amplitudes. Write $R_t(v)$ for the radial
position of a modified ray starting at radius $v$ with zero radial
velocity and set $J=\partial_v R_t$, $H=\partial_v^2R_t$,
$I=\partial_v^3R_t$. Primes on $J$ denote time derivatives. During a flight
$J''=-3\gamma R_t^{-4}J$. At a kick $J'$ gains
$h c_nJ$ with $c_n=-\widetilde g'(r_n)\ge0$. This holds throughout
the annulus for small $d$ because the leading term in the derivative
of the modified $\alpha$ in the strip is $\log^4(1/s)$.
We have $J(0)=1$ and initial derivative zero before any kick.
Use the sine and cosine solution formula with background coefficient
$10\ge3\gamma R_t^{-4}$. The remaining continuous source is
$(10-3\gamma R_t^{-4})J$ and the kick terms are positive.
Since $\sqrt{10}T<\pi/4$, the cosine is at least $1/2$ and the
sine is increasing. Up to a putative first zero this gives positivity
and, by comparing the formulas at two times, $J(t)\ge J(v')/2$
for $0\le v'\le t\le T$. In particular each cutoff evolves without
a caustic.

Define $t_1=2000\log\ell/\ell^2$ and $t_2=2t_1$ for large $\ell$.
Up to $t_2$, summing (C8) for
$|y_n|+|\Delta y_n|/(h\ell^2)$ gives
$|y_n|\le C d\exp(C\ell^2 t_2)<\sqrt d$. Here the modified
force term is bounded by $C\ell^4 |y_n|$ in the annulus. On this
short interval $c_n\ge\ell^4/100$ for small $d$. After
$u_*/\ell^2$ the signed nodal acceleration is also at least
$\ell^4|y_n|/100$ until $t_2$. These inequalities give

$$
 |R_t-1|\ge d\ell^8\quad(t_1\le t\le T),\qquad
 \frac{J(v')}{J(t)}\le C\ell^{-8}
       \quad(0\le v'\le t_1,\ t_2\le t\le T).                 \tag{C11}
$$

Indeed on a block of length $100/\ell^2$ the signed displacement,
once increasing, at least doubles by summing its lower acceleration.
For $J$ use the positive kick terms of the sine formula on the block.
The earlier terms contribute at least half the starting $J$. Each
later $J$ is at least half that value and
$\sin(\sqrt{10}\,t)/\sqrt{10}\ge t/2$ there. The sum of $h$ times
the remaining time over the kicks is at least one quarter of the
squared block length, since $h\ell^2\to0$. This again more than
doubles $J$. Each of the intervals from $u_*/\ell^2$ to $t_1$ and
from $t_1$ to $t_2$ contains $20\log\ell-O(1)$ blocks. Subsequently
the signed nodal increments stay positive. During a flight the
radius differs from linear interpolation by $O(h^2)$, by bounded
centrifugal acceleration. This proves (C11).

For clarity about diffraction, put $E_2=d|H|/J^2$ and
$E_3=d^2|I|/J^3$. Let $F_j$ denote the $j$th radial derivative
of the acceleration during flight or of the velocity increment per
unit $h$ at a kick, as appropriate, and use the sum of continuous
and impulse integrals $d\nu=dt+h\sum_n\delta_{t_n}$. The explicit
modified force bounds on the rays are

$$
 |F_2|\le C(1+\ell^3/\max(s,|y|)),\qquad
 |F_3|\le C(1+\ell^3/\max(s,|y|)^2).
$$

The Jacobi Green function is
$J(t)J(v')\int_{v'}^t J(u)^{-2}du\le4(t-v')J(t)/J(v')$.
This follows from the Wronskian, which is preserved across every
velocity jump. Differentiating the ray equation twice and three times
gives sources $F_2J^2$ and $F_3J^3+3F_2JH$. Put
$B_2=d\,|F_2|$, $B_3=d^2|F_3|$ and $D=J(v')/J(t)$. Then

$$
 \begin{aligned}
 E_2(t)&\le4\int_0^t(t-v')D B_2\,d\nu(v'),\\
 E_3(t)&\le4\int_0^t(t-v')D^2
          \bigl(B_3+3B_2 E_2(v')\bigr)d\nu(v').
 \end{aligned}                                                   \tag{C12}
$$

Up to $t_2$, $D\le2$, $B_2=O(\ell^4)$,
$B_3=O(\ell^5)$ and the time integral of $t-v'$ is at most
$2t(t+h)$. Hence $E_2=O((\log\ell)^2)$ and
$E_3=O(\ell(\log\ell)^2+(\log\ell)^4)$. After $t_2$, split each
integral at $t_1$. On its first part $D=O(\ell^{-8})$. On its
second part (C11) gives $B_2+B_3=O(d+\ell^{-5})$.
First applying the $E_2$ bound and then the $E_3$ bound gives
$E_2+E_3=o(1)$ uniformly for $t_2\le t\le T$.

Transport the half-density along these rays, so
$A(t,R_t(v))=A_0(v)/\sqrt{J(t,v)}$. Use the classical phase for each
flight and subtract $h\widetilde U$ at each kick. The standard
caustic-free WKB residual bounds the norm error from the flights by
$\tfrac12 d^2\int_0^T\|\partial_r^2A(t)\|dt$.
[Schubert, Vallejos and Toscano, §2, (20)–(22)](https://arxiv.org/pdf/1112.4056)
(transport and Duhamel estimate, passage). The amplitudes have compact
support away from the radial endpoint, and kicks preserve the norm.
Twice differentiating the transported half-density gives

$$
 d^2\|\partial_r^2 A(t)\|\le C n_k
 \sup_v\bigl(J^{-2}+E_2/J+E_2^2+E_3\bigr).
$$

On $[0,t_2]$ the integral of this bound is
$O(n_k(\log\ell)^3/\ell)=o(n_k)$. On $[t_2,T]$ it is $o(n_k)$
by (C11)–(C12). Using the **original** quantum kicks on the
approximate wave adds at most
$C n_k(t_1+h)s^2\ell^3/d^2=o(n_k)$ by (C10). After $t_1$ its
support is outside the modified strip. Unitarity propagates these
residual bounds through every factor. All errors are uniform over
retained modes, so their squared norms sum to $o(1)$.

For either cutoff the final approximate wave is supported at radii
converging uniformly to its selected radius. The two supports are
disjoint at $T$. Their masses equal their initial cutoff masses.
The full initial radial position law gives the same limiting $x$
density $e^{-x^2}/\sqrt\pi$ as in the classical calculation.
Letting the angular and radial cutoffs increase and $\eta$ decrease
to zero removes an arbitrarily small initial norm. This proves (C7)
for every bounded continuous radial score, including $f$.

#### Complete separation and the continuum dynamics

Suppose now $h/(d\ell^2)\to\infty$. Define $e$ by $eL_e^2=h$,
$L_e=\log(1/e)>2$. Then $d/e\to0$ and $L_e\sim\log(1/h)$.
In (C8) rescale the radius by $e$ and time by $L_e^{-2}$.
For every bounded initial cutoff the rescaled displacement starts
at zero in the limit and its initial difference quotient tends to
$\sigma/2$. Formula (C9) now reads $(\sigma/2)\sinh u$.
The same level estimate yields the immediate $\sigma$ branch for
the classical ensemble.

For the quantum state first consider subsequences with $\ell/L_e$
bounded. Keep the preparation width $d$ and smoothing width $s=d/\ell$.
The smoothed force has the same inner limit since its change is
$O(s\ell^3)=o(e L_e^4)$. Use $L_e$ in $t_1,t_2$. All rays on a
bounded initial cutoff now lie on the selected side after $u_*$.
The early upper bound is $Ce\exp(C L_e^2 t_2)<\sqrt e$. Equation (C11) then
gives $|R_t-1|\ge eL_e^8$ and $D=O(L_e^{-8})$ on its respective
intervals. The early bounds for $B_2,B_3$ are $O(L_e^4),O(L_e^5)$,
and their late sum is $O(d+L_e^{-5})$ since $d\le e$. Thus the same
transport proof gives vanishing norm error, including the smoothing
cost $O((t_1+h)\ell)$. There is just one outgoing radius.

If $\ell/L_e\to\infty$, $d$ tends to zero faster than every fixed
power of $h$. Compare the packet directly with its point polygon
$(q_n,p_n)$ in (C3). For $r_n=|q_n|=1+y_n$, $n\ge1$, put
$\Lambda_n=1+\log^2(1/|y_n|)$. The acceleration field $F$ satisfies

$$
 |F(x)-F(q_n)|\le C\Lambda_n^2 |x-q_n|.
$$

Within $|y_n|/2$ of $q_n$ this is the derivative bound from (C1).
For larger distances use its global short-distance modulus
$Cv(1+|\log v|^4)$ at distance $v$, obtained by integrating
$1+\log^4(1/|y|)$ across a radial interval of length $v$.
The direction factor is Lipschitz in the annulus, the core is linear
and the exterior has bounded derivative. In particular $F$ is
$1/2$-Hölder globally. This anchored estimate uses the same
moment argument as the [power-cusp propagation](cusp-quantum-preparation-selection.md).

At the first cell Hölder continuity and the exact drift and kick
shears bound both root-mean-square deviations from the point polygon
by $C\sqrt d$. For subsequent cells let
$E_n=\Lambda_n\|(Q-q_n)\psi_n\|+\|(P-p_n)\psi_n\|$. The signed
displacement grows along this polygon, so $\Lambda_n$ decreases.
The exact shears and the anchored bound give
$E_{n+1}\le(1+C h\Lambda_n)^2 E_n$ in either order. The initial
$|y_1|$ is at least $h^2/4$. By (C4) each level $v\le |y_n|<2v$
costs at most $C/\log^2(1/v)+O(h)$ in time. Summing over at most
$C\log(1/h)$ dyadic levels gives $\sum_{n\ge1}^{N-1}h\Lambda_n
=O(\log(1/h)+h\log^3(1/h))$. The amplification is at most a fixed
power of $1/h$, whereas $E_1=O(\Lambda_1\sqrt d)$ decays faster
than every such power. The terminal packet therefore selects the
same radius as the point polygon. Every subsequence has a further
subsequence in one of the two regimes for $\ell/L_e$. This completes
the joint limit in (C7), including $\lambda=\infty$.

For the exact continuum evolution, at each fixed positive $d$ the
products converge for the quantum state by the product formula and
for the classical ensemble by its almost-everywhere uniqueness.
For any sequence $d\downarrow0$ and any fixed bounded continuous
radial score, choose equal cells with $h<d^2$ and a score error
less than $d$ from that continuum evolution. Formula (C7) at
$\lambda=0$ gives the equal mixture for the exact dynamics as well.

In dimensional terms the inputs are $m,R,\omega$, the time $T/\omega$,
the cell duration $h/\omega$ and the specified preparation. They fix
$S_0=mR^2\omega$, the potential energy unit $mR^2\omega^2$, the
initial position and momentum deviations $Rd/\sqrt2$ and
$mR\omega d/\sqrt2$, and the readout width $R Y(T)$. The fixed
constants $b,T$ and the function of $|q_{\rm phys}|/R$ used for the score are
dimensionless. For a quantum sequence $a$ with $0<\lambda<\infty$,
the sequence $c a$ at the same cells, $c>0$, has parameter
$\lambda/\sqrt c$. Distinct $c$ therefore give different limiting
scores within the prescribed canonical family. The model with zero
quantum action and classical widths $w=a/S_0$ reproduces the entire
limiting radial law of the first sequence, including its order bias.
Equality is asserted for these limits and this observable family.

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
The moving-circle example now distinguishes uniform agreement over trial
actions from agreement at each fixed positive action. A nonnegative
spherical source admits order-independent classical refinement, including
at a circular orbit. Classical ensembles of positive lower width also
admit uniform refinement. Even the two branch probabilities at the
transition scale agree for matched preparations. In the scaled radial
variables the momentum unit is $mR\omega\,d\log^2(1/d)$. Its product
with $Rd$ exceeds the Gaussian action $a$ by a factor $\log^2(1/d)$. Whether
the central-force argument imposes any independent relation between
these two resolutions remains open.
