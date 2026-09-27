# Rivero's consistency conjecture: quartic paths and central-force angles

**Result, 2026-09-27.** The quartic oscillator supplies three precise tests
of the user's 1998 proposal. Its real-time path integral exists as a strong
operator limit for every supplied action constant $h>0$. Its halved
critical-point functional already fails to recover the classical Dirac
measure on a two-cell partition with three stationary paths (Theorem 1).
Branch selection repairs the classical iterated limit; in Euclidean time
there is also a positive, non-quadratic construction in which both iterated
limits and every joint zero-resolution limit agree (Theorems 2--3).

For Newton's central-force polygon, angular momentum and equal areas
survive every central kick. Requiring a separated angular phase to descend
to the angle circle gives $L=n h$, or $\oint L\,d\theta=2\pi n h$
(Theorem 4). This condition uses an additional coherent-state premise.
For one fixed orbit it permits $h=|L|/n\to0$. Hooke and Kepler radial
actions give the corresponding Keller--Maslov conditions explicitly;
even a fixed torus satisfying both conditions admits a sequence
$h\downarrow0$ (Theorem 5). These are consistency relations between a
phase constant and orbit data. Selection of one universal positive value
requires a further premise.

The tests and proofs below develop the question in
[the fifth-postulate note, §7](principia-fifth-postulate.md), using
[the time-graded groupoid](tangent-groupoid-trajectories.md) and
[the insertion laws, §§2--3](refinement-composition-and-limit.md).
The constructions assemble established stationary phase, product formulas
and semiclassical quantization.

## 1. Two regulators and three meanings of consistency

Use mass $m>0$, duration $T>0$, fixed endpoints, and a partition
$\pi=(0=t_0<\cdots<t_N=T)$. Write $\tau_j=t_{j+1}-t_j$ and
$\varepsilon'=|\pi|=\max_j\tau_j$. The symmetric discrete action is

$$
S_\pi(q)=\sum_{j=0}^{N-1}\left\{
\frac{m(q_{j+1}-q_j)^2}{2\tau_j}
-\frac{\tau_j}{2}[V(q_j)+V(q_{j+1})]\right\}. \tag{1}
$$

The action resolution $\varepsilon$ and the constant $h$ have units of
action. Throughout this note **$h$ denotes a reduced phase constant**:
when identified with quantum mechanics, $h=\hbar$ and the ordinary Planck
constant is $h_P=2\pi h$. Time steps always use $\tau$ or $\varepsilon'$.

[Rivero 1998, eqs. (1)--(10)](https://arxiv.org/pdf/quant-ph/9803035)
(full-read, three pages) proposes a critical-point distribution, its
halved oscillatory functional, a discretization with two regulators, and
a controlled limit with arbitrary positive $h$. The control map in
eq. (6) remains unspecified. The conjectural equivalence therefore needs
both a normalization and a topology. The following definitions supply
those for the tests here.

For $d=N-1$ internal coordinates, choose a reference length $b>0$ and put
$z_j=q_j/b$, so $\partial_{z_j}S_\pi$ has action units. With a smooth
compact cutoff $\chi$, supported away from degenerate critical points,
define a genuine regularization

$$
D_{\varepsilon,\pi}(O)=
\int\frac{\chi(z)O(z)}{(2\pi\varepsilon^2)^{d/2}}
\exp\left[-\frac{|\nabla_z S_\pi(z)|^2}{2\varepsilon^2}\right]dz.
$$

The change-of-variables formula at the finitely many critical points
$z_a$ gives

$$
D_{0,\pi}(O)=\sum_a
\frac{\chi(z_a)O(z_a)}{|\det S_\pi''(z_a)|}. \tag{2}
$$

The coordinate convention and determinant weights are part of the
definition. A normalized single-branch version is the point measure
$\delta_{z_a}$. Define separately the halved functional

$$
A_{\varepsilon,\pi}(O)=
(2\pi\varepsilon)^{-d/2}\int\chi(z)O(z)e^{iS_\pi(z)/\varepsilon}\,dz.
$$

If $\chi=1$ near all retained critical points, stationary phase gives

$$
A_{\varepsilon,\pi}(O)=
\sum_a\frac{O(z_a)e^{iS_\pi(z_a)/\varepsilon+i\pi\sigma_a/4}}
{\sqrt{|\det S_\pi''(z_a)|}}+O_\pi(\varepsilon), \tag{3}
$$

where $\sigma_a$ is the Hessian signature. For one critical point,
$|A(O)|^2\to D_{0,\pi}(|O|^2)$. The complex amplitude itself needs its
critical phase removed, or the ratio $A(O)/A(1)$. For several critical
points, (3) retains cross terms. Also, a squared amplitude is quadratic
in $O$, whereas (2) is linear in its test function. Equations (2)--(3)
state precisely the limited sense in which halving recovers a Dirac
measure.

The two proposed routes are now:

1. **Classical:** take $\varepsilon\downarrow0$ at fixed $\pi$ in (2),
   or in a branch-normalized (3), then refine the resulting discrete
   stationary paths. Convergence means weak convergence on continuous
   paths, or convergence against specified cylinder observables.
2. **Controlled at fixed $h$:** use free-kernel normalization on each
   cell and integrate $e^{iS_\pi/h}$ over the new vertices. Refine with
   $h>0$ fixed. In real time, convergence means strong operator convergence
   on $L^2$, allowing distributional coordinate kernels. A finite complex
   measure of bounded variation on all continuous paths is a stronger
   requirement and is not assumed here.

The second route implements Rivero's eqs. (7)--(8). Calling it a joint
limit of the *bare* regulators requires an explicit control map. For
example, with $\eta=\varepsilon'/T_0$ dimensionless, a prescribed rescaling
$S_\pi^{\rm bare}=Z_S S_\pi$ has effective phase constant
$h_{\rm eff}=\varepsilon/Z_S$. Taking $Z_S=\eta$ and
$\varepsilon=h\eta$ keeps $h_{\rm eff}=h$. Simply substituting
$\varepsilon=h\eta$ into $e^{iS_\pi/\varepsilon}$ changes the phase to
$S_\pi/(h\eta)$; obtaining $S_\pi/h$ requires the action/control
transformation as well. This specifies the dimensional form of a possible
control map; deriving that map remains an obligation.

**Conjecture R (a sharpened version to test).** For a specified action
class, boundary data, blocking maps and normalizations, existence of a
refinement-compatible classical critical-point distribution is equivalent
to existence of its controlled oscillatory continuum functional; the
classical limit of the latter recovers the former on a stated observable
class. Every quantifier here matters. A stronger *selection conjecture*
would also require these conditions to exclude all zero-action limits,
or to select a common $h>0$. The latter claim goes beyond existence.

There are three concrete theorem forms for “consistency”:

- **Classical elimination:** on a specified noncaustic branch,
  $S_{t+s}(x,y)=\operatorname{stat}_z[S_t(x,z)+S_s(z,y)]$ for the exact
  endpoint action. A minimum replaces stationarity when the branch is a
  genuine global minimizing problem. For real-time quartic mechanics,
  the unrestricted action is unbounded below; the $(\min,+)$ law in the
  groupoid note needs this qualification. Euclidean action restores a
  minimizing problem.
- **Oscillatory composition:** $U_h(t+s)=U_h(t)U_h(s)$, with intermediate
  coordinates integrated. Eliminating a vertex by stationary phase
  produces its Hessian factor and higher corrections as well as its
  stationary action. Exact integration carries those amplitudes along.
- **Compatibility of limits:** after specifying a common observable
  functional $F_{h,\pi}$, an estimate
  $|F_{h,\pi}(O)-F_{h,0}(O)|\le r(|\pi|,h)$ plus a controlled classical
  limit is sufficient along routes where $r\to0$. Uniformity in $h$
  would justify interchanging limits. The summable-defect theorem of the
  refinement note supplies such a criterion when its norm hypotheses
  hold. Determinant weights in (2) also need compatible pushforwards;
  meshwise existence alone does not supply them.

The determinant issue has an exact local formula. Write an insertion as
$S(z,y)$ and assume $S_y(z,y_*(z))=0$ defines one branch with invertible
$S_{yy}$. Set $S_{\rm eff}(z)=S(z,y_*(z))$. Integration of the two
Euler--Lagrange delta factors gives, locally on this branch,

$$
\int\delta(S_y(z,y))\,\delta(S_z(z,y))\,dy
=\frac{\delta(\nabla S_{\rm eff}(z))}
{|\det S_{yy}(z,y_*(z))|}.
$$

Indeed the first delta fixes $y=y_*(z)$ with the displayed Jacobian,
and $\nabla S_{\rm eff}=S_z$ there. At a joint critical point the same
identity follows from the Schur complement
$\det S''=\det S_{yy}\det S_{\rm eff}''$. Classical refinement therefore
has an explicit weight to transport; stationary phase transports its
square root, signature and higher corrections.

Thus even quadratic exactness presupposes a Gaussian normalization and
appropriate topology; focal times require distributional kernels. The
quartic test below separates the three theorem forms explicitly.

## 2. Quartic real time: a finite interference obstruction

Fix $V(q)=\lambda q^4$, $\lambda>0$, so $F(q)=-4\lambda q^3$.
Take endpoints zero, two cells of length $T/2$, and internal coordinate
$y$. Work in the physical $y$ coordinate; choosing $z=y/b$ multiplies
the following functionals by common coordinate factors and leaves the
failure of convergence unchanged. Equation (1) becomes

$$
f(y)=\frac{2my^2}{T}-\frac{\lambda T}{2}y^4.
$$

**Theorem 1.** A compact cutoff equal to one near the three critical
points gives a finite $\delta(f')$, while the squared halved functional
fails to converge as $\varepsilon\downarrow0$.

*Proof.* The critical points and their data are

$$
y_0=0,\qquad y_\pm=\pm\sqrt{\frac{2m}{\lambda T^2}},\qquad
f(y_\pm)=s_*:=\frac{2m^2}{\lambda T^3},
$$
$$
f''(0)=\frac{4m}{T},\qquad f''(y_\pm)=-\frac{8m}{T}.
$$

For $O=1$ on the cutoff support, put $a=\sqrt{T/(4m)}$ and
$b_1=\sqrt{T/(8m)}$. Equation (3) reads

$$
A_\varepsilon=a e^{i\pi/4}
+2b_1 e^{is_*/\varepsilon-i\pi/4}+O(\varepsilon),
$$
$$
|A_\varepsilon|^2=
\frac{3T}{4m}+\frac{T}{\sqrt2\,m}
\sin(s_*/\varepsilon)+O(\varepsilon). \tag{4}
$$

Sequences with $s_*/\varepsilon=2\pi k+\pi/2$ and
$2\pi k+3\pi/2$ give different limits. Meanwhile
$\int\chi\,\delta(f')dy=T/(2m)$ by (2). Even averaging away the
sine in (4) retains interference between $y_+$ and $y_-$, whose actions
coincide. A separate diagonalization or branch label would be needed.
$\square$

This is an obstruction to extending the halving identity to all critical
paths by one overall normalization. It appears before a continuum limit
or a choice of $h$. Retaining the pair of independent amplitudes also
introduces off-diagonal terms; it cannot be identified with (2) without
an additional prescription.

**Theorem 2 (two existing limits for the quartic).**

(a) On every partition, select only a small neighborhood of the zero
stationary path. Then $A_{\varepsilon,\pi}(O)/A_{\varepsilon,\pi}(1)$
converges to $O(0)$, and refining these branch measures gives the Dirac
measure on the zero path.

(b) For every $h>0$, the symmetric time-sliced operators converge strongly
on $L^2(\mathbb R)$ to the unitary quartic evolution, independently of
the sequence of partitions with mesh tending to zero:

$$
A_h=-\frac{h^2}{2m}\frac{d^2}{dq^2},\quad B=\lambda q^4,\quad
H_h=A_h+B,
$$
$$
Q_{h,\tau}=e^{-i\tau B/(2h)}e^{-i\tau A_h/h}e^{-i\tau B/(2h)},
\qquad Q_{h,\pi}\longrightarrow U_h(T)=e^{-iTH_h/h}. \tag{5}
$$

*Proof of (a).* At zero the Hessian of (1) is the positive definite
Dirichlet kinetic matrix: the quartic term has zero second derivative.
The inverse function theorem isolates this branch at each partition.
Equation (3) cancels its nonzero leading coefficient in the ratio. Its
polygon is identically zero on every partition, proving the outer limit.
This proves branch selection explicitly; its cutoff may depend on $\pi$.

*Proof of (b).* The positive polynomial Schrödinger operator is essentially
self-adjoint on $C_c^\infty(\mathbb R)$; see the continuous,
bounded-below case recorded in
[Simon 1999, p. 2](https://arxiv.org/pdf/math-ph/9907022)
(passage, Theorem 1.1 and following self-adjointness statement).
Its domain is $D(A_h)\cap D(B)$. For completeness, the estimate ensuring
this domain identification follows by integration by parts. With
$a_h=h^2/(2m)$,

$$
\|H_h f\|^2=a_h^2\|f''\|^2+\lambda^2\|q^4f\|^2
+2a_h\lambda\int q^4|f'|^2dq
-12a_h\lambda\int q^2|f|^2dq.
$$

The pointwise inequality
$12a_h\lambda q^2\le\lambda^2q^8/2+C_h$, with
$C_h=9a_h\lambda(6a_h/\lambda)^{1/3}$, absorbs the negative term.
Closure and smooth cutoff approximation give the stated domain and its
equivalent graph norm. Both factors in (5) are unitary, and on this
domain

$$
\tau^{-1}(Q_{h,\tau}-U_h(\tau))f\longrightarrow0.
$$

The difference quotients are uniformly bounded from the graph domain to
$L^2$. The orbit $\{U_h(s)f:0\le s\le T\}$ is compact in that domain,
so convergence is uniform on the orbit. Telescoping an arbitrary
partition therefore bounds the error by

$$
T\sup_{\substack{0<\tau\le|\pi|\\0\le s\le T}}
\frac{\|(Q_{h,\tau}-U_h(\tau))U_h(s)f\|}{\tau}\longrightarrow0.
$$

Density extends convergence to $L^2$. This is the product-formula
argument of [Teschl, Theorem 5.10, pp. 131--132](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf)
(passage), with the same telescoping proof for unequal cells.
The kernel of $Q_{h,\tau}$ has phase (1) and normalization
$(m/(2\pi i h\tau))^{1/2}$. Hence (5) is exactly the stated time slicing.
$\square$

Composition and $\|U_h(T)\|=1$ hold for every supplied $h>0$. The proof
gives convergence at fixed $h$, with graph estimates depending on $h$;
it makes no assertion of an unnormalized real-time amplitude limit as
$h\downarrow0$. Theorem 1 blocks the unrestricted classical-first
halved prescription, while (a) gives a precise classical-first repair.
An equivalence in Conjecture R must retain that distinction.

## 3. Quartic Euclidean time: a uniform two-limit theorem

A positive version gives a stronger existence test, with a direct
uniform estimate. Keep the quartic potential and endpoints zero; change
the action to

$$
S^E_\pi=\sum_j\frac{m(q_{j+1}-q_j)^2}{2\tau_j}+W_\pi,
\qquad W_\pi=\frac\lambda2\sum_j\tau_j(q_j^4+q_{j+1}^4).
$$

Let $\nu_{h,\pi}$ be the normalized density proportional to
$e^{-S^E_\pi/h}$, embedded as piecewise linear paths. Here $h$ is the
same action resolution called $\varepsilon$ in the classical-first route.

**Theorem 3.** For every $h>0$, arbitrary mesh refinement gives the
quartic Feynman--Kac bridge $\nu_h$ on $C([0,T])$. Both iterated limits,
and every joint limit $h\downarrow0$, $|\pi|\downarrow0$, give
$\delta_{q\equiv0}$. More precisely, for every $r>0$ and every partition,

$$
\nu_{h,\pi}(\|q\|_\infty>r)
\le 2\exp\left\{\frac{3\lambda hT^3}{16m^2}
-\frac{2mr^2}{hT}\right\}. \tag{6}
$$

*Proof.* Let $B_h$ be the zero-endpoint Brownian bridge with covariance

$$
\mathbb E[B_h(s)B_h(t)]=\frac hm
\left(\min(s,t)-\frac{st}{T}\right).
$$

Its values at the vertices have the normalized free kinetic density.
Thus $\nu_{h,\pi}$ is their polygonal interpolation, tilted by
$e^{-W_\pi(B_h)/h}/Z_{h,\pi}$. Continuity of bridge paths gives uniform
convergence of the interpolation and convergence of the trapezoidal
potential sum to $\lambda\int_0^T B_h^4dt$. The weights lie between
zero and one, and their expectation tends to a strictly positive value.
Dominated convergence proves the fixed-$h$ limit. Its identification
with the heat kernel of $H_h$, including diffusion coefficient $h/m$,
is the bounded-below Feynman--Kac formula
([Simon, Theorem 1.1](https://arxiv.org/pdf/math-ph/9907022), passage).
The unnormalized heat kernels obey exact convolution.

For uniformity in $h$, use
$\mathbb E B_h(t)^4=3[ht(T-t)/(mT)]^2\le3h^2T^2/(16m^2)$.
The trapezoidal weights sum to $T$, so Jensen gives

$$
Z_{h,\pi}\ge
\exp[-\mathbb E W_\pi/h]
\ge\exp[-3\lambda hT^3/(16m^2)].
$$

The interpolated supremum is bounded by the bridge supremum. Reflection
of Brownian motion at its first passage through $r$, followed by
conditioning on the final value zero, gives
$\mathbb P(\sup B_h>r)=e^{-2mr^2/(hT)}$; applying the same identity to
$-B_h$ gives the two-sided bound with factor two. Multiplying by
$Z_{h,\pi}^{-1}$ proves (6). It tends to zero uniformly in $\pi$ as
$h\downarrow0$; the limiting bridge obeys the same bound.
The unique Euclidean minimizing path is zero since every term of
$S^E$ is nonnegative and the endpoints vanish. This proves all the
claimed orders of limits. $\square$

This theorem concerns the Euclidean positive measure, with its stated
boundary data. Analytic continuation provides real-time operators through
the self-adjoint $H_h$; transferring probability estimates such as (6)
to oscillatory real-time path measures would require another argument.
Together, Theorems 1--3 give an explicit status for each limit: a failing
unrestricted halved classical limit, an existing selected classical
limit, an existing fixed-$h$ real-time continuum limit, and commuting
Euclidean limits with a bound. These consistency tests permit phase
constants approaching zero.

## 4. Proposition I: the polygon and the angle circle

Now use the plane, a central potential $V(r)$, and scalar signed angular
momentum $L=q\mathbin{\times}p$. Work on a regular segment away from
$r=0$. A central kick changes $p$ by $-a q$ for some scalar $a$, and a
drift changes $q$ by $\tau p/m$. Each separately preserves $L$.
The oriented area of the drift triangle is exactly

$$
\Delta\mathcal A=\frac12q_j\mathbin{\times}q_{j+1}
=\frac{\tau_j L}{2m}. \tag{7}
$$

This is the finite equal-area mechanism of Newton's Proposition I.
Symmetric kicks from (1) have the same property. Nonlinear forces
generally change old endpoints when a finite cell is split; their
consistent integrators converge on compact collision-free segments as
the mesh vanishes. Equation (7) remains exact at each mesh. These swept
areas serve the angular test here; the Galileo inertial--parabola defect
in the Planck programme remains a separate observable.

In polar coordinates the kinetic numerator in (1) is

$$
r_j^2+r_{j+1}^2-2r_jr_{j+1}\cos(\theta_{j+1}-\theta_j).
$$

The full discrete action and its exponential are single-valued under
every change of angular representative $\theta_j\mapsto\theta_j+2\pi k_j$,
for every $\varepsilon>0$. The angular discrete Euler--Lagrange equation
conserves

$$
L_j=\frac{m r_jr_{j+1}}{\tau_j}
\sin(\theta_{j+1}-\theta_j).
$$

Thus periodicity of the original path weight, together with the polygon
law, places no arithmetic restriction on $\varepsilon$.

An extra requirement arises when a *stationary state* is assembled from
a fixed angular-momentum branch. The separated Hamilton--Jacobi function
on the angular cover is
$S(r,\theta,t)=W_r(r;E,L)+L\theta-Et$.

**Theorem 4 (angular descent).** Assume the branch amplitude is a scalar,
single-valued function of $\theta$, and require its angular phase
$e^{iL\theta/h}$ to descend from $\mathbb R$ to $S^1$ with trivial
boundary holonomy. Then, necessarily and sufficiently,

$$
\frac Lh\in\mathbb Z,
\qquad \oint L\,d\theta=2\pi n h. \tag{8}
$$

*Proof.* Translation by $2\pi$ multiplies the phase by
$e^{2\pi iL/h}$. Its equality to one is (8). For lifted polygon
increments the product is
$\prod_j e^{iL\Delta\theta_j/h}=e^{iL\sum_j\Delta\theta_j/h}$;
inserting a vertex leaves it unchanged. Descent through a full turn
then imposes exactly the same condition, independently of the mesh.
$\square$

This is also the exact angular spectrum of $-ih\partial_\theta$ on
periodic scalar wavefunctions. Allowing a flat boundary phase
$\psi(\theta+2\pi)=e^{2\pi i\alpha}\psi(\theta)$ changes the relation to
$L/h\in\mathbb Z+\alpha$. The trivial scalar choice is an explicit
premise; neither central kicks nor angle periodicity chooses a state
space. Distinct winding paths remain distinct integration histories,
even when their endpoints agree.

For a fixed $\ell=|L|>0$, (8) permits precisely $h=\ell/n$ with
$n=1,2,\ldots$, whose infimum is zero. Holding the winding number $n$
fixed determines $h$ from that orbit. A bound $n\le N_*$ would produce
the conditional floor $h\ge\ell/N_*$, with both orbit scale and bound
supplied. A common $h$ for several prescribed orbits requires their
angular actions to be integer multiples of it; incommensurate actions
cannot all satisfy that exact-state premise.

## 5. Hooke and Kepler: radial actions and Maslov phases

For regular noncircular bound tori with $\ell=|L|>0$, define

$$
I_\theta=\ell,\qquad
I_r=\frac1\pi\int_{r_-}^{r_+}
\sqrt{2m(E-V(r))-\ell^2/r^2}\,dr.
$$

The angular cycle has no turning point. The radial cycle has two simple
turning points. Supplying the usual WKB transport and its caustic phase
gives the Keller--Maslov rule

$$
\exp\left[\frac{i}{h}\oint p\cdot dq-\frac{i\pi\mu}{2}\right]=1,
\qquad I=h(n+\mu/4). \tag{9}
$$

Here $\mu_\theta=0$, $\mu_r=2$. Each simple turning point contributes
$-\pi/2$ to the transported cycle phase, yielding
$I_r=h(n_r+1/2)$ and $I_\theta=h|n_\theta|$.
This is semiclassical state consistency, with WKB transport supplied;
the angular rule is exact on the stated scalar state space.
[Keller 1958](https://doi.org/10.1016/0003-4916(58)90032-0)
(metadata, *Annals of Physics* 4, 180--188) is the established source;
[Keller's later account](https://doi.org/10.1137/1027139)
(abstract) describes the integer and half-integer conditions from WKB.
We use (9) conditionally and derive the following mechanical actions.

**Hooke, $V=m\omega^2r^2/2$, $\omega>0$ (Proposition X).** The radial
period is $T_r=\pi/\omega$, since $r^2$ oscillates at $2\omega$.
Differentiating the action integral gives
$\partial I_r/\partial E=T_r/(2\pi)=1/(2\omega)$.
The circular orbit has $E_c=\omega\ell$ and $I_r=0$, hence

$$
I_r=\frac{E}{2\omega}-\frac\ell2,
\qquad E=\omega(2I_r+\ell). \tag{10}
$$

Equation (9) consequently gives the EBK values

$$E=h\omega(2n_r+|n_\theta|+1).$$

For a circle $\ell=m\omega R^2$, taking $R\downarrow0$ produces
arbitrarily small positive classical angular actions at fixed $m,\omega$.
The radial turning-point argument applies to noncircular tori; circular
orbits follow as the mechanical limit of (10), with a degenerate radial
cycle requiring its own wave analysis.

**Kepler, $V=-k/r$, $k>0$.** For $E<0$ and
$0<\ell<k\sqrt{m/(-2E)}$, the ellipse has two distinct positive radial
turning points. Its semimajor axis is $a=-k/(2E)$ and its period is
$T_r=2\pi\sqrt{ma^3/k}$. Thus
$\partial I_r/\partial E=k\sqrt m/(-2E)^{3/2}$.
At the circle $E_c=-mk^2/(2\ell^2)$, $I_r=0$, giving

$$
I_r=k\sqrt{\frac{m}{-2E}}-\ell,
\qquad E=-\frac{mk^2}{2(I_r+\ell)^2}. \tag{11}
$$

The planar EBK rule yields

$$E=-\frac{mk^2}{2h^2(n_r+|n_\theta|+1/2)^2}.$$

This is the planar action calculation; the three-dimensional Coulomb
problem has additional angular variables. The angular law alone fixes
$\ell/h$ and leaves $I_r$ free. Classical circles satisfy
$\ell=\sqrt{mkR}$, so $R\downarrow0$ also gives angular infimum zero
at fixed $m,k$, through regular circles of individually positive radius.

**Theorem 5 (even both cycle conditions allow $h\downarrow0$).**
Fix a Hooke or Kepler noncircular torus satisfying (9) at some $h_0>0$,
with integers $n_r\ge0$, $|n_\theta|\ge1$. The *same* actions satisfy
(9) at every

$$
h_j=\frac{h_0}{2j+1},\quad
n_{r,j}=(2j+1)n_r+j,\quad
n_{\theta,j}=(2j+1)n_\theta,\qquad j=0,1,\ldots . \tag{12}
$$

*Proof.* Substitution gives
$h_j(n_{r,j}+1/2)=h_0(n_r+1/2)$ and
$h_j|n_{\theta,j}|=h_0|n_\theta|$.
Equations (10)--(11) then preserve the energy and angular momentum.
$\square$

Some fixed tori admit no $h$ satisfying both exact EBK relations,
because their action ratio fails the required integer/half-integer
relation. Whenever one value exists, (12) excludes a positive lower
bound from these relations alone. Asymptotic WKB errors carry their
usual separate status; (12) is an exact statement about the proposed
cycle conditions.

Finally, the action in a closed spatial circuit must be identified
correctly. Write $W=\oint p\cdot dq=2\pi J_{\rm orb}$, whereas
$S_T=W-ET$. For Hooke, $J_{\rm orb}=2I_r+\ell=E/\omega$ and
$T=2\pi/\omega$, so $S_T=0$ on every ellipse. Imposing
$e^{iS_T/h}=1$ there gives no restriction whatever. For Kepler,
$J_{\rm orb}=I_r+\ell$ and $ET=-\pi J_{\rm orb}$, so
$S_T=3\pi J_{\rm orb}$. Equal configuration after a dynamical period
allows a stationary state to acquire its temporal phase
$e^{-iET/h}$. The spatial cycle condition (9) therefore uses $W$ and
the caustic phase, with time held separate. Identifying it with the
bare full-period halved action would change the condition.

## 6. Relation to the orbit bounds and Kepler threshold

The [closed-orbit force-action note](closed-orbit-force-action.md)
proves $J_{\rm orb}\ge m^2v_*^3/F_{\max}$ in Newtonian mechanics under a
uniform speed floor and force ceiling. For eccentric orbits this is the
total orbit action above; it differs from $I_\theta=\ell$.
The excitation and force hypotheses supply that bound. Combining it
with an integer rule would still require an upper bound on the integer
to bound $h$ from below.

On a circle $J_{\rm orb}=\ell$. The
[bound-orbit observable note](bound-orbit-action-observable.md)
gives $2\sqrt{\det\Sigma}=\ell$ for its uniform-phase preparation.
Equation (8) would turn this into $2\sqrt{\det\Sigma}=|n_\theta|h$
if that classical estimator is used to label an admitted angular action.
Identifying the classical ensemble with a quantum state would need an
additional preparation argument.

The [relativistic Kepler note](relativistic-kepler-threshold.md)
has a different, explicit mechanism: in the external singular potential
$-k/r$, regular bound motion requires $\ell>k/c$. Combining this
classical admissibility condition with angular descent gives

$$|n_\theta|h>k/c.$$

For fixed $h$ it excludes low angular integers. For a fixed integer it
requires $h>k/(c|n_\theta|)$. With unbounded integers it permits
arbitrarily small $h$; for a fixed allowed orbit use $h=\ell/n$.
The threshold remains coupling dependent and closes in the Newtonian
limit $c\to\infty$. A softened core has angular infimum zero already at
fixed $m,k,c$, as proved in that note. Thus the singular-core threshold,
the orbital action estimator, and the angular phase lattice each retain
their distinct hypotheses.

## 7. Consequence for STATE

Item 2 gains a tested form of the 1998 conjecture: quartic interference
requires a branch or diagonal prescription for critical-point recovery;
fixed-$h$ real-time refinement exists for all $h>0$, and a Euclidean
quartic test has commuting zero-resolution limits. Central-force
angular descent gives an orbit-dependent integer relation whose allowed
phase constants accumulate at zero, even with both EBK cycles imposed.
The constructive next obligation is a physically justified control and
observable prescription that addresses the interference in (4), together
with a scale-selection premise surviving the sequences (8) and (12).
These results settle the stated tests; the general controlled equivalence
in Conjecture R retains those explicit open obligations.
