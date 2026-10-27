# From multiscale quantum mechanics to Newton's initial-value problem

**Result, 2026-10-27.** For a smooth nonnegative potential on the line
with bounded second and higher derivatives, we construct Euclidean
$0+1$ quantum mechanics at every supplied $h>0$ using time refinement
and a normalized density at every dyadic scale. The reference
fluctuations are Gaussian Brownian bridges, and the full interaction
and large-field configurations are retained. Real-time evolution is
the unitary group of the reconstructed self-adjoint Hamiltonian.

For every initial $(q_0,p_0)$, means of finite quantum time-slice
products are a Cauchy family as both $h$ and the time mesh tend to zero.
An explicit estimate controls both scales simultaneously. Their limit solves
$\dot q=p/m$, $\dot p=-V'(q)$; it is the unique solution. An explicit
bound compares any two positive values of $h$. The proof does not
assume a classical trajectory in advance. Its stability hypothesis and
Gronwall estimate are the same ingredients used by Cauchy--Lipschitz,
so the construction is a different route, not a weakening of that
theorem. Smooth confining potentials with locally Lipschitz force,
including the positive quartic, follow by a cutoff and energy conservation.

This note is a new assembly of standard Feynman--Kac, conditional
expectation and unitary-conjugation ingredients; no priority claim is made.
The normalized-density architecture is inspired by Dimock--Balaban,
not an import of their four-dimensional Yang--Mills estimates. The
construction assumes a positive action parameter $h$, and does not
prove it necessary. A separate tangent-groupoid formulation follows
only after this theorem.

**Targeted advisor check (GPT-6.1 Sol, 2026-10-27).** The finite-step
identities, constants, joint Cauchy estimate, domain argument, quartic
energy barrier and cusp counterexample were checked in writing.
This is not an independent proof audit of the imported Wiener,
Feynman--Kac, self-adjointness or spectral theorems.

## 1. Hypotheses and the quantum theory to be constructed

Let $m>0$ and let $V:\mathbb R\to\mathbb R$ be $C^\infty$, $V\ge0$,
with all derivatives of order at least two bounded. Set
$$L=\sup_x|V''(x)|<\infty.\tag{1}$$
Thus $V'$ is globally Lipschitz with constant $L$ and $V$ grows at most
quadratically. A nonlinear confining example is
$$V(x)=\tfrac12m\omega_0^2x^2+\lambda[1-\cos(x/\ell)],
\qquad\omega_0,\lambda,\ell>0.\tag{2}$$
Its curvature is bounded, while the force is not linear.

For each $h>0$, set
$$H_h=-\frac{h^2}{2m}\frac{d^2}{dx^2}+V(x)\tag{3}$$
on $L^2(\mathbb R)$. Its Friedrichs realization is nonnegative and
self-adjoint; for this smooth bounded-below class the restriction to
$C_c^\infty(\mathbb R)$ is a core. Put
$$U_h(t)=e^{-itH_h/h}.\tag{4}$$
The spectral theorem makes $U_h$ a strongly continuous unitary group.
No classical ODE solution is used to define it. If $V(x)\to\infty$
at infinity, compactness of the form embedding and positivity
improvement additionally give the unique vacuum and positive spectral
gap as in [the preceding construction](constructive-qft-one-time.md).
They are not required for the initial-value theorem below.

## 2. Finite time weights and arbitrary refinement

Fix endpoints $x,y$, duration $T>0$, and a partition
$\pi=(0=t_0<\cdots<t_N=T)$. Write $\delta_j=t_{j+1}-t_j$ and
$$
 S_\pi^E(q)=\sum_j
 \left\{\frac{m(q_{j+1}-q_j)^2}{2\delta_j}
 +\frac{\delta_j}{2}[V(q_j)+V(q_{j+1})]\right\}.
 \tag{5}
$$
The normalized finite-lattice measure has endpoints $q_0=x,q_N=y$
and density proportional to $e^{-S_\pi^E/h}$ in the internal coordinates.

Let $B$ be the Brownian bridge from $x$ to $y$ with variance parameter
$h/m$ and mean $b(t)=x+(y-x)t/T$. Its covariance is
$$\operatorname{Cov}[B(s),B(t)]
=\frac hm\left(\min(s,t)-\frac{st}{T}\right).\tag{6}$$
With $p_h(t;u,v)=\sqrt{m/(2\pi ht)}
 \exp[-m(v-u)^2/(2ht)]$, the normalized kinetic factor
$\prod_jp_h(\delta_j;q_j,q_{j+1})/p_h(T;x,y)$ is exactly the joint
density of $B(t_j)$.
Define
$$W_\pi(B)=\sum_j\frac{\delta_j}{2}
       [V(B(t_j))+V(B(t_{j+1}))],\qquad
 Z_\pi=\mathbb E_0e^{-W_\pi(B)/h}.\tag{7}$$
The interpolated lattice measure is the pushforward of
$Z_\pi^{-1}e^{-W_\pi/h}d\mathbb P_0$ by polygonal interpolation.

Brownian continuity gives uniform convergence of this interpolation to
$B$, and $W_\pi\to\int_0^T V(B(t))dt$ almost surely, for every sequence
of partitions with $|\pi|\to0$. The weights lie in $[0,1]$.
Consequently dominated convergence constructs the limit
$$d\nu_h=Z_h^{-1}
 e^{-h^{-1}\int_0^T V(B(t))dt}d\mathbb P_0,\qquad
 Z_h=\mathbb E_0e^{-h^{-1}\int_0^T V(B(t))dt}>0.\tag{8}$$
It proves weak convergence of the polygonal measures on $C([0,T])$
and $L^1(\mathbb P_0)$ convergence of their **lifted densities**. The
polygonal measures themselves are not asserted to converge in total
variation to the non-polygonal path measure.

The normalization has an explicit finite-partition lower bound. Since
$V''\le L$, Taylor's inequality gives
$\mathbb EV(B(t))\le V(b(t))+\frac L2\operatorname{Var}B(t)$.
Writing $M_{xy}=\max_{z\in[x,y]}V(z)$, using
$\operatorname{Var}B(t)\le hT/(4m)$ and Jensen's inequality yields
$$Z_\pi\ge
 \exp\!\left[-\frac{TM_{xy}}h-\frac{LT^2}{8m}\right]
 \quad\text{for every partition.}\tag{9}$$
Thus normalization and large-field paths are included at every mesh.
The bound is finite for each $h>0$ but is not uniform as $h\to0$.

## 3. The exact all-scale retained density

For the dyadic partition let $\mathcal F_n$ be the sigma-algebra of
the $2^n+1$ vertex values, and let
$$\rho=\frac{d\nu_h}{d\mathbb P_0},\qquad
 \rho_n=\mathbb E_0[\rho\mid\mathcal F_n].\tag{10}$$
These are densities relative to the **normalized free bridge**.
Conditional expectation gives, exactly,
$$\rho_n=\mathbb E_0[\rho_{n+1}\mid\mathcal F_n],\quad
 \mathbb E_0\rho_n=1,\quad 0<\rho_n\le Z_h^{-1}.\tag{11}$$
At level $n+1$, conditional on level $n$, the reference midpoint of a
cell of length $\delta=T/2^n$ has mean $(a+b)/2$ and variance
$h\delta/(4m)$; reference midpoints in different cells are independent.
The *interacting* conditional law is the product of these Gaussian
reference laws multiplied by $\rho_{n+1}/\rho_n$. The latter density
must be retained; the interacting midpoint variables are not assumed
independent.

Dyadic evaluations generate the Borel sigma-algebra of continuous path
space. Hence the bounded martingale theorem gives
$$\rho_n\longrightarrow\rho\quad\text{in }L^1(\mathbb P_0)
 \text{ and almost surely.}\tag{12}$$
Equations (11)--(12) are an exact normalized blocking tower at all
scales. They use an already constructed Wiener measure as reference;
they do not claim a lattice-only construction or a four-dimensional
polymer estimate. In particular the $Z_h^{-1}$ bound does not give
control uniform in $h\downarrow0$.

The distinction between a finite lattice step and the complete
effective density can be seen explicitly. Before any blocking, integrate
the middle vertex $z$ of two cells of length $s$, with retained endpoints
$a,b$ and $\mu=(a+b)/2$. Its conditional potential is
$$F_\mu(z)=\frac m s(z-\mu)^2+sV(z).\tag{13}$$
For $2m/s-sL>0$, put $\kappa_s=2m/s-sL$. Then $F_\mu''\ge\kappa_s$;
there is a unique minimizer $z_*$ and the **normalized** conditional
law satisfies
$$\mathbb P(|z-z_*|\ge r\mid a,b)
 \le 2\exp[-\kappa_s r^2/(2h)].\tag{14}$$
Indeed, integration by parts gives
$\mathbb E(z-z_*)^{2n}\le(2n-1)!!(h/\kappa_s)^n$; expand the
hyperbolic cosine and optimize the exponential Markov bound.
Conditioned on all retained vertices, the eliminated vertices are
independent for this original nearest-neighbour lattice. After a
blocking step the generated action must be kept: (13)--(14) cannot be
iterated as though the original potential were unchanged.

This is the precise $0+1$ version of the source lesson: retain the
entire normalized effective density, not merely its background minimizer
or an unnormalized large-field action cost. Compare
[Dimock I](../docs/balaban/Dimock_BalabanI_1108.1335v2.md),
sections 2.1, 2.4 and 4.5, and
[Dimock II](../docs/balaban/Dimock_BalabanII_1212.5562v2.md),
introduction and sections 3.13--3.14 (selected passages read there).
The latter papers treat a three-dimensional scalar theory, not (3).

## 4. From the Euclidean limit to real-time quantum mechanics

The Feynman--Kac theorem identifies the kernel of $e^{-TH_h/h}$ as
$K_h(T;x,y)=p_h(T;x,y)Z_h(x,y)$; (8) is the corresponding
**normalized bridge**, not the kernel itself. It also makes
the semigroup reflection positive in the ground-state construction when
a normalizable ground state exists. Real time is defined by the
self-adjoint operator through (4), not by treating the Euclidean
probability law as a real-time probability law.

For finite real-time steps use the kick--drift product
$$T_{h,s}=D_{h,s}K_{h,s},\quad
K_{h,s}=e^{-isV(Q)/h},\quad D_{h,s}=e^{-isP^2/(2mh)},
\quad P=-ih\,\partial_x.\tag{15}$$
The factors are unitary. Its products converge strongly to $U_h(T)$
under arbitrary positive partitions at each fixed $h>0$. Here is the
needed arbitrary-partition argument.

Write $c_h=h^2/(2m)$, and take $f\in C_c^\infty$. Integration by parts
gives
$$
 \|H_hf\|^2=c_h^2\|f''\|^2+\|Vf\|^2
 +2c_h\int V|f'|^2-c_h\int V''|f|^2
 \ge c_h^2\|f''\|^2+\|Vf\|^2-c_hL\|f\|^2.\tag{15a}
$$
Since $C_c^\infty$ is an operator core, closure identifies
$D(H_h)=D(P^2)\cap D(V)$ and controls the two component graph norms.
For $f$ in this domain, $(T_{h,s}-I)f/s\to-iH_hf/h$ strongly,
and these difference quotients are uniformly bounded from the
$H_h$ graph domain to $L^2$. The orbit
$\{U_h(t)f:0\le t\le T\}$ is graph-norm compact. Thus the local
first-order error is uniform on the orbit, and a telescoping sum over
the cells proves the limit; density and unitarity extend it to all
$L^2$ vectors. This is the argument used for the symmetric product in
[Rivero 1998 test, Theorem 2(b)](rivero-1998-conjecture-central-forces.md),
now written for kick--drift. It is a strong operator statement, not a
finite complex measure on path space.

The Euclidean stationary equation is
$m\ddot q=+V'(q)$, whereas real-time Newton motion satisfies
$m\ddot q=-V'(q)$. Euclidean concentration cannot be used as a
Newton trajectory by silently changing that sign.

## 5. A joint quantum and time-mesh construction of Newton motion

Fix $\omega>0$, initial $(q_0,p_0)$, and the coherent packet
$$
 \psi_h(x)=\left(\frac{m\omega}{\pi h}\right)^{1/4}
 \exp\!\left[-\frac{m\omega(x-q_0)^2}{2h}
            +\frac{i p_0(x-q_0)}h\right].\tag{16}
$$
Its position and momentum means are $q_0,p_0$, with standard
deviations $\sqrt{h/(2m\omega)}$ and $\sqrt{hm\omega/2}$.

For a partition $\pi$, apply the unitary kick and drift (15)
successively. Let $q_j,p_j$ be the resulting means at $t_j$, and put
$$W_j=\operatorname{sd}(Q)_j+
          \frac{\operatorname{sd}(P)_j}{m\omega},\quad
 C=\sqrt{\frac2{m\omega}},\quad
 \beta=\omega+\frac{L}{m\omega},\quad
 a=\max\!\left(\omega,\frac L{m\omega}\right).\tag{17}$$
No Gaussian assumption is made about the state after the first step.

The exact conjugation identities are
$$K_{h,s}^*QK_{h,s}=Q,\quad
 K_{h,s}^*PK_{h,s}=P-sV'(Q),\quad
 D_{h,s}^*QD_{h,s}=Q+sP/m,\quad
 D_{h,s}^*PD_{h,s}=P.\tag{18}$$
Both finite factors preserve Schwartz space under the stated derivative
bounds, so (18) is valid on each propagated Gaussian. For the kick,
the triangle inequality in $L^2$ and
$\operatorname{sd}[V'(Q)]\le L\,\operatorname{sd}(Q)$ give
$\operatorname{sd}(P)_{\rm after}\le
\operatorname{sd}(P)_{\rm before}+sL\,\operatorname{sd}(Q)$.
For the drift the analogous bound adds $s\,\operatorname{sd}(P)/m$
to the position deviation. Therefore
$$W_{j+1}\le
 (1+s\omega)\left(1+\frac{sL}{m\omega}\right)W_j,
\qquad
 W_j\le C\sqrt h\,e^{\beta T}.\tag{19}$$
These are finite-step statements for the full quantum state.

The means obey
$$p_{j+1}=p_j-s_j\langle V'(Q)\rangle_j,\qquad
 q_{j+1}=q_j+\frac{s_jp_{j+1}}m.\tag{20}$$
Fix $h_0>0$, restrict $0<h\le h_0$, and use the phase-space norm
$\|(q,p)\|_\omega=|q|+|p|/(m\omega)$. Define
$$\begin{gathered}
 b=\frac{|V'(0)|+LC\sqrt{h_0}e^{\beta T}}{m\omega},\\
 R_T=e^{\beta T}\big(\|(q_0,p_0)\|_\omega+Tb\big),\qquad
 F_T=|V'(0)|+L(R_T+C\sqrt{h_0}e^{\beta T}),\\
 C_\delta=\frac{F_T+LR_T}{m},\qquad
 C_h=\frac{LCe^{\beta T}}{m\omega},\qquad
 G_T=\frac{e^{aT}-1}{a}.
 \tag{21}
\end{gathered}$$
Equation (19) and (20) imply recursively that every vertex mean has
$\|(q_j,p_j)\|_\omega\le R_T$ and
$|\langle V'(Q)\rangle_j|\le F_T$, independently of $h$ and $\pi$.
For example, the recurrence for the norm is bounded by
$R_{j+1}\le e^{\beta s_j}R_j+s_jbe^{\omega s_j}$.

Linearly interpolate the mean vertices, writing
$z_{h,\pi}(t)=(q_{h,\pi}(t),p_{h,\pi}(t))$. Put
$\mathcal F(q,p)=(p/m,-V'(q))$. On every cell the two components of the
residual are bounded by
$$
 |\dot q_{h,\pi}-p_{h,\pi}/m|
     \le |\pi|F_T/m,\quad
 |\dot p_{h,\pi}+V'(q_{h,\pi})|
     \le LC\sqrt h\,e^{\beta T}+L|\pi|\,\omega R_T.\tag{22}
$$
Consequently
$$\|\dot z_{h,\pi}-\mathcal F(z_{h,\pi})\|_\omega
 \le C_\delta|\pi|+C_h\sqrt h.\tag{23}$$
The first residual is the difference between the interpolated momentum
and its post-kick value; the second is the sum of the packet's force
variance and the motion of the interpolated position.

The vector field $\mathcal F$ has Lipschitz constant at most $a$ in
this norm. Integrating the residuals of two products with common
initial data, and applying Gronwall, gives
$$
 \sup_{t\le T}\|z_{h,\pi}(t)-z_{k,\sigma}(t)\|_\omega
 \le G_T\!\left[
 C_\delta(|\pi|+|\sigma|)
 +C_h(\sqrt h+\sqrt k)\right].\tag{24}
$$
Thus the means are Cauchy in $C([0,T],\mathbb R^2)$ as the two scales
$h$ and $|\pi|$ tend to zero **in any joint order**. Let $z=(q,p)$
be their limit. Equation (23) passes to the integral equation
$$q(t)=q_0+\int_0^t\frac{p(s)}m\,ds,\qquad
 p(t)=p_0-\int_0^tV'(q(s))\,ds.\tag{25}$$
It is continuously differentiable and solves Newton's initial-value
problem. Uniqueness follows from the same Gronwall inequality with
zero residual. The construction extends to negative time using
inverse unitary steps, or by replacing $p$ by $-p$ and reversing time.

Letting $(k,|\sigma|)\to(0,0)$ in (24) yields the explicit joint bound
$$
 \sup_{t\le T}\|z_{h,\pi}(t)-z(t)\|_\omega
 \le G_T\big(C_\delta|\pi|+C_h\sqrt h\big).\tag{26}
$$
The constants are independent of the number of cells and of $h$ in
$(0,h_0]$. Equation (26) is an observable-level statement about the
packet means; it is not an operator-norm estimate on real-time
propagators and does not assert a real-time positive path measure.

Finally fix $h>0$. At a fixed $t$, choose partitions containing $t$.
Section 4 gives strong $L^2$ convergence of the product state to
$U_h(t)\psi_h$. Equations (19)--(21) bound its position and momentum
second moments uniformly. Strong $L^2$ convergence gives convergence
of bounded position and momentum cutoffs, and the uniform second
moments make the first-moment tails at most $O(R^{-1})$. The first
moments therefore converge to those of $U_h(t)\psi_h$. For a general
refining partition, use the product truncated at the last vertex before
$t$; the same graph-norm telescoping argument is uniform on compact
time intervals. The bounds on vertex momenta and forces make the
interpolated means equi-Lipschitz. Pointwise identification therefore
upgrades to uniform convergence on $[0,T]$. Passing to the limit in
(26) gives
$$
 \sup_{t\le T}
 \left\|(\langle Q\rangle_t,\langle P\rangle_t)-z(t)\right\|_\omega
 \le G_T C_h\sqrt h.\tag{27}
$$
This uses no differentiation of an unbounded quantum observable.
It also proves the claimed consistency of the two limiting orders for
these means. The construction assumes a semiclassical family
$h\downarrow0$; a single fixed-positive-$h$ theory does not have
simultaneously sharp position and momentum.

The Cauchy estimate and its domain argument are the present assembly.
The broader relation between coherent quantum packets and classical
orbits is established prior work, including
[Hepp, 1974](https://doi.org/10.1007/BF01646348)
(introduction and theorem statements); no claim of literature novelty
is made for this semiclassical mechanism.

## 6. Quartic extension and the limits of the implication

Let $V(q)=\lambda q^4/4$ with $\lambda>0$. Its Hessian is unbounded,
so (26) does not apply globally with a single $L$. For fixed initial
data choose a smooth nonnegative $V_R$ with bounded derivatives of
order at least two, agreeing with $V$ on $[-R,R]$. Apply the construction to
$V_R$. As long as its trajectory is inside that interval,
$$E=\frac{p^2}{2m}+\frac{\lambda q^4}{4}
 =\frac{p_0^2}{2m}+\frac{\lambda q_0^4}{4}\tag{28}$$
by the chain rule. Choosing $R>(4E/\lambda)^{1/4}$ rules out a first
exit, so the constructed trajectory solves the original quartic
equation for all finite times. Local Lipschitz uniqueness identifies
different choices of cutoff. The same argument applies to smooth
confining potentials whose derivative is locally Lipschitz, with an
appropriate compact energy sublevel. The cutoff quantum means are not
claimed here to be those of the uncut quartic Hamiltonian.

Quantum existence does **not** alone imply classical uniqueness.
The bounded $C^1$ potential in
[the cusp note](newton-cusp-preparation-floor.md), with
$V(q)=-\frac23|q|^{3/2}$ near zero, has a bounded-perturbation
self-adjoint quantum Hamiltonian; adding a constant makes $V\ge0$
without changing the force. Yet, while remaining in that
neighbourhood, Newton's equation with $m=1$ admits both rest and
$$q(t)=\begin{cases}
0,&t\le t_0,\\
(t-t_0)^4/144,&t\ge t_0,
\end{cases}\tag{29}$$
for any waiting time $t_0\ge0$. Thus extra force regularity, or some
independent selection rule, is necessary for the uniqueness conclusion.

## 7. Comparison with Cauchy--Lipschitz

The direct theorem works with the integral operator on phase-space
paths; Lipschitz continuity gives a contraction locally, then global
continuation under the global hypothesis. The earlier
[polygon lesson](balaban-ode-lesson.md) gives a comparable
refinement/Cauchy proof.

The route above first constructs a quantum family and then proves that
its means form a Cauchy family as $h\downarrow0$. Its quantitative
inputs are normalized multiscale Euclidean control, self-adjoint
real-time evolution, a packet variance estimate, and the **same**
Lipschitz/Gronwall stability that makes Cauchy--Lipschitz work. It gives
the explicit approximation (26) and places the classical path beside
quantum dynamics, but it invokes substantially more machinery and
does not establish an ODE theorem beyond Cauchy--Lipschitz.

## 8. Consequence for STATE

The user-directed first document gives a complete scoped existence and
classical-limit construction. The subsequent
[tangent-groupoid formulation](groupoid-quantum-newton-states.md)
places its observables and dynamics in a continuous field, keeping the
deformation parameter, time mesh and coarse-graining distinct while
relating their observable-state limits along chosen joint schedules.
