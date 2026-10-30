# Tangent-groupoid scaling and the quantum construction of Newton motion

**Scaling result, 2026-10-30.** For a nonnegative scalar potential on the
line, coordinate/time dilation has an exact action on the full quantum
Hamiltonian, its kernels and its normalized endpoint bridges. With
$\hbar=\epsilon S_0$, $t=\epsilon T$ and $x-y=\epsilon v$, the rescaled
Hamiltonian has supplied action $S_0$ and potential $V(q+\epsilon X)$.
For $V\in C^3$ with bounded second and third derivatives, its heat kernel
has a locally uniform tangent limit and an explicit second-order potential
correction. The scale/composition comparison in
[§7](#7-interacting-kernels-under-tangent-scaling) retains the whole interaction.
Normalizing each transition separately generally destroys its semigroup law;
normalizing a complete endpoint bridge preserves refinement consistency.
The local tangent limit and the scaling that resolves a quantum well retain
different information, as [§8](#8-which-zoom-resolves-a-quantum-well) makes precise.

**State result, 2026-10-27.** The tangent groupoid carries a continuous field
of observable algebras whose positive-parameter fibers are quantum and
whose zero fiber is classical. After fixing an action unit $S_0$ and
setting $\hbar=\epsilon S_0$, the finite quantum products and classical
initial-value construction of
[the quantum product theorem](quantum-blocks-construct-newton.md) define
compatible states on these fibers. On every compact time interval,
their values on smooth Weyl observables converge to the classical point
state with an explicit $O(\hbar+|\pi|)$ bound, for **every joint
schedule** with $\hbar,|\pi|\to0$.

The result is a state-level limit for the specified coherent
preparations and smooth potentials with bounded derivatives of order
at least two, including the third derivative used for the rate. The quartic
extension in the quantum product theorem uses cutoff Hamiltonians; it does not
establish this estimate for uncut quartic quantum evolution. The result
neither makes the finite-product propagator uniformly
close to the exact quantum propagator as $\hbar\to0$, nor makes a quantum
superposition a single classical trajectory. The groupoid parameter is a
geometric deformation parameter until the identification $\hbar=\epsilon
S_0$ is chosen. The time mesh is an additional scale.

The [wall construction](dirichlet-wall-impulse.md) treats boundary domains
and impact separately; the whole-line theorem here does not cover that
problem. The [classical construction](balaban-ode-lesson.md) and
[quantum product theorem](quantum-blocks-construct-newton.md) supply the
dynamics used below.

The groupoid and strict quantization are established: in particular,
Cariñena, Clemente-Gallardo, Follana, Gracia-Bondía, Rivero and Várilly,
[Connes' Tangent Groupoid and Strict Quantization](https://arxiv.org/abs/math/9802102)
(§§3.1--3.3, selected passages read; see the repository companion), already includes the
user's work. Landsman--Ramazan's
[continuous-field construction](https://arxiv.org/abs/math-ph/0001005)
(abstract) supplies the general Lie-groupoid setting. The following
state estimate applies the quantum product theorem's finite-slice bounds to
that established structure; no literature priority claim is made.

## 1. What the parameter joins

For $M=\mathbb R$, the tangent groupoid is
$$
 \mathbb T M=(M\times M\times(0,1])\ \sqcup\ (TM\times\{0\}).
 \tag{1}
$$
At $\epsilon>0$, pair arrows compose as
$(x,y,\epsilon)(y,z,\epsilon)=(x,z,\epsilon)$; at zero,
$(q,v,0)(q,w,0)=(q,v+w,0)$. A local chart near the zero fiber is
$$
 (q,v,\epsilon)\longmapsto
 \big(q+\epsilon v/2,\ q-\epsilon v/2,\ \epsilon\big).
 \tag{2}
$$
Thus $v=(x-y)/\epsilon$ is a **tangent coordinate**, not automatically
a physical velocity. A physical time interpretation requires a
separate identification of units and scaling.

The groupoid $C^*$-algebra is a continuous field with fibers
$$
 \mathcal A_\epsilon\simeq\mathcal K(L^2(\mathbb R))
 \quad(\epsilon>0),\qquad
 \mathcal A_0\simeq C_0(T^*\mathbb R).
 \tag{3}
$$
At zero, Fourier transformation takes tangent-vector convolution to
pointwise multiplication of functions of $(q,p)$. The positive fibers
are abstractly isomorphic, but the continuous field specifies how
families of their elements approach a classical observable.

Choose an action unit $S_0>0$ and set
$$\hbar=\epsilon S_0.\tag{4}$$
For $a\in C_c^\infty(T^*\mathbb R)$, Weyl quantization has kernel
$$
 K_\epsilon^a(x,y)=\frac1{2\pi\epsilon S_0}
 \int_{\mathbb R}e^{i(x-y)p/(\epsilon S_0)}
       a\!\left(\frac{x+y}{2},p\right)dp.\tag{5}
$$
In chart (2),
$$
 \epsilon K_\epsilon^a
  \big(q+\epsilon v/2,q-\epsilon v/2\big)
 =\frac1{2\pi S_0}\int e^{ivp/S_0}a(q,p)dp.\tag{6}
$$
The rescaled kernel is the inverse Fourier transform of the zero-fiber
symbol. The established strict-quantization construction makes
$\epsilon\mapsto\operatorname{Op}_{\epsilon S_0}^W(a)$, together with
$a$ at zero, a continuous section. Equation (6) displays the chart
and normalization in this flat case; it is not a new proof of the
general continuous-field theorem.

## 2. The dynamics and the unbounded objects

For the potential and hypotheses of the quantum product theorem define
$$
 H_\hbar=P^2/(2m)+V(Q),\qquad U_\hbar(t)=e^{-itH_\hbar/\hbar}.\tag{7}
$$
The $H_\hbar$ are unbounded operators and the $U_\hbar(t)$ are generally
multipliers, not elements of the compact-operator fibers. At $\hbar>0$
their adjoint action defines automorphisms of the compact operators:
$$\alpha_\hbar^t(A)=U_\hbar(t)^*AU_\hbar(t).\tag{8}$$
The quantum product theorem constructs the unique classical phase-space flow
$\Phi_t(q,p)$ before it is used here. On the zero fiber put
$$\alpha_0^t(a)=a\circ\Phi_t.\tag{9}$$
This is classical Hamiltonian evolution with
$H_{\rm cl}=p^2/(2m)+V(q)$.

For $a\in C_c^\infty(T^*\mathbb R)$, Weyl--Egorov compatibility for
the smooth subquadratic potentials of the quantum product theorem gives, for
fixed $T$,
$$
 \sup_{|t|\le T}
 \|\alpha_\hbar^t(\operatorname{Op}_\hbar^W(a))
      -\operatorname{Op}_\hbar^W(a\circ\Phi_t)\|
 \le C_{a,T}\hbar^2.\tag{10}
$$
Here is the relevant estimate. The finite-time flow has bounded
derivatives on compact sets under the stated hypotheses, so
$a_s=a\circ\Phi_s$ is smooth, compactly supported, and has uniform
symbol bounds for $|s|\le T$. The kinetic commutator is exact. The
potential-commutator remainder after removing its classical first-order
term has kernel
$$
 \frac{i}{\hbar}\left[V(x)-V(y)-(x-y)V'\!\left(\frac{x+y}{2}\right)\right]
 K_\hbar^{a_s}(x,y).\tag{10a}
$$
The bracket is bounded by $\|V'''\|_\infty|x-y|^3/24$. Rapid decay of
the Fourier transform of $a_s$ in its momentum variable, the change
$x-y=\hbar z$, and Schur's test bound the operator norm by $C_{a,T}\hbar^2$.
Integrating this commutator remainder by Duhamel's formula gives (10).
This uses the standard Weyl calculus and the flow already constructed
in the quantum product theorem; it is not being used to prove that flow exists.

## 3. A quantitative state on every fiber

Use the coherent packet $\psi_\hbar^{q_0,p_0}$ of equation (16) in the
quantum product theorem. For a partition $\pi$, let $\psi_{\hbar,\pi,j}$ be the
state after its first $j$ kick--drift cells, and let
$z_{\hbar,\pi}(t_j)=(q_j,p_j)$ be its means. Denote the constructed
classical state by $z(t)=\Phi_t(q_0,p_0)$. Define
$$
 I_a=(2\pi)^{-2}\int_{\mathbb R^2}
 |\widehat a(\xi,\eta)|\big(|\xi|+m\omega|\eta|\big)
 \,d\xi\,d\eta<\infty.\tag{11}
$$
Here $\widehat a$ is the ordinary Fourier transform in $(q,p)$.
Also put
$$
 J_a=\frac1{2(2\pi)^2}\int_{\mathbb R^2}
 |\widehat a(\xi,\eta)|\big(|\xi|+m\omega|\eta|\big)^2
 \,d\xi\,d\eta<\infty.\tag{11a}
$$
Using the exact Fourier representation of Weyl quantization,
$$\operatorname{Op}_\hbar^W(a)
 =(2\pi)^{-2}\int\widehat a(\xi,\eta)
             e^{i(\xi Q+\eta P)}d\xi\,d\eta,\tag{12}$$
set $A=\xi(Q-q_j)+\eta(P-p_j)$. The scalar phase
$e^{i(\xi q_j+\eta p_j)}$ factors out, $\langle A\rangle_j=0$, and
spectral calculus gives
$|\langle e^{iA}\rangle_j-1|
 \le\tfrac12\langle A^2\rangle_j$. Consequently,
$$
 |\langle\operatorname{Op}_\hbar^W(a)\rangle_j-a(q_j,p_j)|
 \le J_a\!\left[
 \operatorname{sd}(Q)_j+\frac{\operatorname{sd}(P)_j}{m\omega}
 \right]^2.\tag{13}
$$
Indeed $\langle A^2\rangle_j=\|A\psi_{\hbar,\pi,j}\|^2$ and the triangle
inequality bounds $\|A\psi_{\hbar,\pi,j}\|$ by the weighted sum of the
two standard deviations. No Gaussian-shape assumption is needed after
the first step. Fourier inversion also gives
$|a(z)-a(z')|\le I_a\|z-z'\|_\omega$.

The quantum product theorem's estimates (19) and (26) therefore give, at every
partition vertex $t_j\in[0,T]$,
$$
 \left|\langle\psi_{\hbar,\pi,j},\operatorname{Op}_\hbar^W(a)
                         \psi_{\hbar,\pi,j}\rangle-a(z(t_j))\right|
 \le J_a C^2 e^{2\beta T}\hbar+
 I_aG_T(C_\delta|\pi|+C_\hbar\hbar).\tag{14}
$$
The constants $C,\beta,G_T,C_\delta,C_\hbar$ are explicitly defined in
that document and depend on the common $\hbar_0,T,V,m,\omega$ and initial
data, not on $\hbar$ or the number of cells. No differentiability of an
unbounded quantum expectation is used in this step.

With $\hbar=\epsilon S_0$, choose any $\alpha>0$ and a time unit $T_0>0$
so that $|\pi_\epsilon|\le T_0\epsilon^\alpha$. Equation (14) yields
$$
 \langle\operatorname{Op}_{\epsilon S_0}^W(a)\rangle_{\pi_\epsilon}
 \longrightarrow a(\Phi_t(q_0,p_0))
 \quad\text{at vertices tending to }t,\tag{15}
$$
with error $O(\epsilon+\epsilon^\alpha)$ at vertices equal to
$t$. Such a vertex can be inserted in each partition. There is no
constraint here on $|\pi_\epsilon|/\hbar$.

This means that the vector states on the positive fibers approach the
point-evaluation state on the zero fiber, for the specified family of
preparations. For an arbitrary continuous section $A$, approximate
$A(0)\in C_0(T^*\mathbb R)$ uniformly by compactly supported smooth
symbols. Continuity of the field and the norm-one bound on states
extend (15) from these symbols to $A$. At fixed $\hbar$, taking the mesh
limit recovers the exact unitary state as in the quantum product theorem.
Both routes thus reach the same zero-fiber state; equality or
closeness of the two quantum vectors along an arbitrary joint schedule
has **not** been established.

## 4. A precise two-scale test on Euclidean increments

The preceding theorem concerns real-time operator states. It does not
claim that Euclidean sample paths are real-time trajectories. The
following free Gaussian calculation shows why the groupoid coordinate,
the action parameter and the duration must not be conflated.

Consider a drifted free reference increment
$$Y-X=u\delta+\sqrt{\frac{\hbar\delta}{m}}\,Z,
 \qquad Z\sim N(0,1).\tag{16}$$
Set $\hbar=\epsilon S_0$ and $\delta=T_0\epsilon^\alpha$ with
$\alpha>0$. The physical-time difference quotient is
$$\frac{Y-X}{\delta}
 =u+\sqrt{\frac{S_0}{mT_0}}\,
       \epsilon^{(1-\alpha)/2}Z,\tag{17}$$
whereas the tangent-groupoid chart variable is
$$v_\epsilon=\frac{Y-X}{\epsilon}
 =uT_0\epsilon^{\alpha-1}
  +\sqrt{\frac{S_0T_0}{m}}\,
       \epsilon^{(\alpha-1)/2}Z.\tag{18}$$

- If $0<\alpha<1$, the physical-time quotient concentrates at $u$,
  but $v_\epsilon$ is not tight.
- If $\alpha=1$, $v_\epsilon$ converges in law to a nondegenerate
  Gaussian of mean $uT_0$ and variance $S_0T_0/m$.
- If $\alpha>1$, $v_\epsilon\to0$ in probability, while the
  physical-time quotient is not tight.

This is an exact diagnostic for the Euclidean Gaussian reference,
not a probability law for real-time Feynman paths. It also does not
contradict (15): a groupoid observable is obtained after the Fourier
and operator construction, whereas (18) examines a single sampled
Euclidean increment.

## 5. Where blocking sits in the groupoid picture

For each $\epsilon>0$ the quantum product theorem supplies a complete tower
$\rho_{\epsilon,n}$ of normalized conditional densities on dyadic
time samples. The relation
$$\rho_{\epsilon,n}
 =\mathbb E_{0,\epsilon}[
          \rho_{\epsilon,n+1}\mid\mathcal F_n]\tag{19}$$
is exact and retains all generated interactions. The integer $n$
counts an integration/coarse-graining operation; $\epsilon$ labels the
deformation field (4). The conditional maps are generally not
invertible, so they are not automatically arrows of the tangent
groupoid.

Equation (15) connects these scales for the real-time **observable
states** even when they are tied by a single chosen schedule. It does
not follow from the $1/Z_{\epsilon}$ Euclidean bound, which need not
be uniform in $\epsilon$, and it does not promote Euclidean
minimization into real-time Newton dynamics.

The zoom action on the tangent groupoid is a geometric rescaling of
near-diagonal arrows. It is useful for organizing a comparison with RG,
but it is not by itself an integration of fluctuations or a theorem
that the physical action constant runs. Likewise, the real-time
Hamilton principal action composes by stationary elimination on a
specified noncaustic branch; infimal convolution is appropriate for
a genuine minimizing Euclidean problem or a separately proved special
case. The kernel calculation below makes this distinction explicit.

## 6. Regulators and a normalized blocking test

The connection is already part of Rivero's work. The appendix to his
[1997 tangent-groupoid note](https://arxiv.org/pdf/dg-ga/9710026)
(pp. 7--8, passages read) constructs a **toy RG triangle**: a dilation
rescales a bare sequence approaching the tangent boundary to a chosen
nonzero reference slice, with limits at different slices related by
rescalings. His [1998 Feynman-formula proposal](https://arxiv.org/pdf/quant-ph/9803035)
(pp. 2--3, equations (5)--(10), passages read) similarly distinguishes
two regulators and calls its controlled objects bare, renormalized and
dressed series. Its control transformation is left unspecified; its
control constant is arbitrary. The
[1999 strict-quantization paper](../docs/CarinenaEtAl_TangentGroupoid_1999.md)
with Rivero and coauthors supplies the groupoid quantization framework.
These are the provenance of the present question, not a claim that the
recent calculation invented the groupoid/RG connection.

The different appearances of epsilon need an explicit dictionary. Let
$\epsilon_G$ be a dimensionless groupoid deformation parameter; in the
specified [state formulation](groupoid-quantum-newton-states.md), choosing
$\epsilon_G=\hbar/S_0$ assigns the dimensionful phase constant to that
parameter. Let $\eta=|\pi|/T_0$ be a dimensionless mesh scale, and let
$\alpha_\pi$ be an action-dimensional bare phase regulator. A possible
control map, already recorded in the
[1998 test](rivero-1998-conjecture-central-forces.md), is
$$
 S_\pi^{\rm bare}=Z_S(\eta)S_\pi,\qquad
 \hbar_{\rm eff}=\frac{\alpha_\pi}{Z_S(\eta)}.
$$
For example, the *specified* choices $Z_S(\eta)=\eta$ and
$\alpha_\pi=\eta\hbar$ give
$e^{iS_\pi^{\rm bare}/\alpha_\pi}=e^{iS_\pi/\hbar}$ at every mesh.
This algebra illustrates how a vanishing bare regulator can coexist
with a fixed positive effective action; substituting the same regulator
into an unscaled action would give a different phase.

**An exact Gaussian blocking test.** Let $m>0$, $u\in\mathbb R$ and
let $a\ge0$ be an action-dimensional parameter. Define a normalized
transition kernel by
$$K^u_{a,t}(x,dy)=\mathcal N(x+ut,at/m)(dy),\qquad t>0,$$
with zero variance interpreted as a Dirac measure. For $a=\hbar>0$
and $u=0$ this is the free Euclidean quantum kernel; arbitrary $u$
gives the drifted Gaussian reference, not a real-time path measure.
Integrating out an intermediate position preserves $a$ exactly:
$$K^u_{a,t}K^u_{a,v}=K^u_{a,t+v}.$$
If time and position are then rescaled by $t_{\rm old}=r t_{\rm new}$,
$x_{\rm old}=s x_{\rm new}$ with $r,s>0$, the normalized kernel obeys
$$
 K^u_{a,rt}(sx,sB)=K^{ru/s}_{ra/s^2,t}(x,B)
 \quad\text{for every Borel set }B.
$$
These identities follow from adding independent Gaussian increments and
rescaling their means and variances; they include $a=0$. Under the
diffusive choice $r=b$, $s=\sqrt b$, the action coefficient stays
fixed. When $u=0$, every $a\ge0$ is a fixed point of this particular
normalized block-and-rescale map. At $a=0$, retaining $u$ gives the
deterministic free Newton motion $x(t)=x(0)+ut$. Thus this exact free
RG control neither selects a positive action nor excludes the classical
branch. It is an illustrative Gaussian comparison, not a result about
all interacting blocking maps or complete record instruments; compare
the [free increment](groupoid-quantum-newton-states.md) and the
[action-normalization identity](refinement-composition-and-limit.md).

**The two-regulator bridge and a residual action.** For the free Gaussian
endpoint bridge on a partition with $d=N-1$ interior points, whitening
the quadratic action gives $2\Delta S/a\sim\chi_d^2$ and hence
$$\mathbb E\Delta S=\frac{da}{2},\qquad
  \operatorname{Var}(\Delta S)=\frac{da^2}{2}.$$
If the maximum cell length and $a_N$ tend to zero while $d a_N\to\ell$,
the bridges can be coupled to converge uniformly almost surely to the
classical chord, while $\Delta S\to\ell/2$ in $L^2$. This uses one
Brownian bridge and its polygonal interpolations. For equal cells
$\tau=T/N$ and $a_N=b\tau$, the supplied $b$ has energy units and
$\ell=bT$. The positive residual is selected by the scaling; at every
finite mesh the action distribution has values arbitrarily near zero.

The separately controlled reference family fixes $m_R,\kappa_R>0$ and
chooses $m_B=\alpha_\pi m_R/\kappa_R$, so its normalized free kernels
are preserved as $\alpha_\pi\to0$; the bare mass then tends to zero.
This is different from the preceding fixed-mass limit and does not
derive the reference action. The
[regulator manuscript](../papers/regulator-limits.tex), Proposition 2
and its running-coefficient section, contains the full arbitrary-partition
proof and source reading; the [PDF](../out/papers/regulator-limits.pdf),
[B08](../references/batches/B08.md) and its
[derivation](../papers/regulator-limits.tex) retain the detailed record.
The manuscript also gives a bounded-speed shrinking sine example with a
fixed action defect and growing acceleration, and a separate scalar
stationary-phase/delta-weight calculation. Those examples motivate testing
which independent force or derivative bounds suppress such a defect; they
do not make the defect universal or identify it with $\hbar$.

The interacting scalar comparison in §7 now gives an exact dilation map
commuting with kernel composition and endpoint-bridge marginalization.
It uses an already defined Hamiltonian and retains its complete kernels;
it supplies no closed finite list of effective couplings. The wider RG
question is uniform control of generated interactions at the required
physical times and preparations, and any independent universal calibration
of the action. Geometric zoom, coarse-graining and running parameters can
participate in that construction; they remain different operations. The
[corrected groupoid comparison](groupoid-quantum-newton-states.md#geometric-zoom-and-kernel-composition) and
[scale correspondence](../research/refinement-correspondences.md)
keep these claims and their corrections distinct.


### Geometric zoom and kernel composition

The adiabatic zoom acts by $(x,y,\epsilon)\mapsto(x,y,\lambda^{-1}\epsilon)$
and $(x,v,0)\mapsto(x,\lambda v,0)$. Debord--Skandalis
[2014](https://doi.org/10.1016/j.aim.2014.02.012) and van Erp--Yuncken
[2019](https://arxiv.org/pdf/1511.01041) (§1.1 and §4.1, Definition 17,
passages read; Debord--Skandalis metadata only) relate this
geometry to pseudodifferential kernels homogeneous modulo smoothing terms;
the zero-fiber restriction gives their principal symbols. This source result
identifies geometric structure, not a Wilsonian integration or a law for
physical $\hbar$. Earlier identifications of all three were too broad.

The user's 2003 note
([Rivero, "Flashes of noncommutativity", arXiv:math/0302285](https://arxiv.org/abs/math/0302285),
full read) introduces the groupoid over configuration space with arrows
$(x,y,u)$, $u$ an elapsed time, and law $(x,y,u)\circ(y,z,v)=(x,z,u+v)$. Its
convolution algebra has product
$(AB)(x,z,t)=\int\!\!\int A(x,y,r)\,B(y,z,t-r)\,dy\,dr$; Fourier transformation
in $t$ gives, with $\varepsilon\sim1/\hat t$, the product of the $\varepsilon>0$ part of the
tangent groupoid, so the latter's algebra sits inside the former's
(the 2003 note's second flash). Refining a trajectory is factoring an
arrow $(x,z,u)$ through intermediate points and times, which is Newton's
insertion of $t_{2.6}$.

For endpoint functions define min-plus convolution by
$$
 (A\otimes B)(x,z):=\inf_y\{A(x,y)+B(y,z)\}.
$$
It eliminates the intermediate endpoint; it does not add the action
on each individual composable pair of arrows.

**Proposition 1.** For $M>0$, constant force $F$, and $u>0$, set
$$S_u(x,y)=\frac{M(y-x)^2}{2u}+\frac{Fu}2(x+y)-\frac{F^2u^3}{24M}.$$
Then $(S_u)_{u>0}$ is a semigroup of kernels under min-plus convolution:
$S_r\otimes S_v=S_{r+v}$ for $r,v>0$. This is the corrected action
$\ell_u$ of [the refinement note](refinement-composition-and-limit.md),
equation (2). The corresponding constant-force unitary propagators
satisfy $U_{r+v}=U_rU_v$; their kernels compose by integration over
the intermediate position, in the oscillatory/distributional sense
where the real-time integrals are not absolutely convergent.

*Proof.* The sum $S_r(x,y)+S_v(y,z)$ is a strictly convex quadratic in
$y$ with unique minimizer
$$y_*=\frac{vx+rz}{r+v}-\frac{Frv}{2M}.$$
Substitution gives $S_{r+v}(x,z)$. Equivalently, $y_*$ is the value
at time $r$ of the action-minimizing constant-force path joining $x$
to $z$. The unitary law follows from the self-adjoint Hamiltonian;
its kernel statement is operator composition. $\square$

The min-plus law is not an ordinary groupoid morphism. For free motion
with $M=1$, $S_1(0,1)+S_1(1,0)=1$, whereas $S_2(0,0)=0$.
The equality holds only after minimizing over the intermediate point
($y=0$ in this example).

The displayed $S$ is the exact discrete Lagrangian of discrete mechanics
([Marsden and West 2001](https://doi.org/10.1017/S096249290100006X),
metadata), and discrete Lagrangian mechanics on groupoids is
[Weinstein's (1996)](https://doi.org/10.1090/fic/007/10) (metadata). The
kick--drift--kick cell $S_\delta=K_{F\delta/2}D_\delta K_{F\delta/2}$ of the refinement note is
the variational (Störmer--Verlet) integrator of the trapezoidal discrete
Lagrangian $L_\delta$, and the cubic counterterm turns $L_\delta$ into the exact one.
The laws of Proposition 1 can be related through a Euclidean Laplace
limit: under coercivity and regularity conditions,
$-\hbar\log\int e^{-S/\hbar}dy\to\inf_y S$ as $\hbar\to0$
([Litvinov 2005](https://doi.org/10.1090/conm/377/06982), metadata).
This does not turn an oscillatory real-time integral into a probability
integral, nor make every stationary real-time branch a global minimum.


## 7. Interacting kernels under tangent scaling

Here the kinetic energy, mass and potential are specified. The conclusions
do not follow from the groupoid law without those dynamical inputs. Work
on $\mathbb R$, with $m,S_0>0$ and $V\ge0$. For the estimates assume
$V\in C^3$ and bounded $V''$ and $V'''$. Use the nonnegative Friedrichs
Hamiltonians
$$H_{a,V}=-\frac{a^2}{2m}\partial_x^2+V(x),\qquad a>0.$$
Their Euclidean kernels $K_{a,V}(t;x,y)$ are those of
$e^{-tH_{a,V}/a}$. The action-dimensional $a$ is a family parameter;
the semiclassical family below sets $a=\hbar=\epsilon S_0$. Neither
$\epsilon$ nor a duration is being assigned the units of physical $\hbar$.

### Exact dilation and composition

For dimensionless $r,s>0$ and a fixed centre $q$, put
$$
 (D_{q,s}f)(X)=s^{1/2}f(q+sX),\qquad
 a'=\frac{ra}{s^2},\qquad
 V_{r,s,q}(X)=\frac{r^2}{s^2}V(q+sX).
 \tag{20}
$$
Direct differentiation gives the exact operator identity
$$
 \frac r a D_{q,s}H_{a,V}D_{q,s}^{-1}
 =\frac1{a'}H_{a',V_{r,s,q}}.
 \tag{21}
$$
Unitary conjugation preserves the Friedrichs domains and proves (21)
also for the closed forms. Spectral calculus therefore gives
$$
 s K_{a,V}(rt;q+sX,q+sY)
 =K_{a',V_{r,s,q}}(t;X,Y).
 \tag{22}
$$
The same conjugation holds for real-time unitary propagators; their
kernels need not be positive functions. We use (22) as a probability
calculation only in Euclidean time.

Keeping $m$ fixed in (20) is a declared normalization, not an invariant
meaning of action running. Equivalently keep $a$ fixed, use
$m'=ms^2/r$ and $\widehat V(X)=rV(q+sX)$, and obtain the same rescaled
kernel from $H_{a,m',\widehat V}$. Here the extra mass subscript makes
the kinetic coefficient explicit. Physical calibration must distinguish
these parametrizations; the coordinate/time identity alone cannot do so.

Composition commutes with this dilation. Indeed, substituting
$z=q+sZ$ in $K(r(t+u))=\int K(rt)K(ru)\,dz$ cancels exactly one
kernel Jacobian and gives the composition law for the right side of
(22). For an endpoint bridge with $N$ cells, the $N$ kernel factors
contribute $s^{-N}$, its $N-1$ internal integrations contribute
$s^{N-1}$, and division by the total endpoint kernel contributes $s$.
Their product is one. Thus the normalized bridge and every marginal
transform exactly, before or after eliminating any subset of inserted
points. No generated term is dropped. This extends the free comparison
in §6 to a specified interacting Hamiltonian; the dilation itself is
invertible, whereas eliminating bridge points generally is not.

### Inserted points and the boundary product

The user's insertion question distinguishes the arrow law from the
kernel law. At fixed $\epsilon>0$, composable arrows have exactly
$(x-y)+(y-z)=x-z$. In symmetric chart coordinates write
$u=(x-y)/\epsilon$, $v-u=(y-z)/\epsilon$ and $q=(x+z)/2$.
The two factors have different centres:
$$
 q_1=\frac{x+y}{2}=q+\frac\epsilon2(v-u),\qquad
 q_2=\frac{y+z}{2}=q-\frac\epsilon2u.
 \tag{22a}
$$
For kernels $A_\epsilon,B_\epsilon$ with absolutely convergent product,
put $\kappa^A_\epsilon(q,v)=\epsilon
A_\epsilon(q+\epsilon v/2,q-\epsilon v/2)$, and similarly for $B$.
Substitution of $y=x-\epsilon u$ in the product integral gives
$$
 \kappa^{AB}_\epsilon(q,v)=\int
 \kappa^A_\epsilon\!\left(q+\tfrac\epsilon2(v-u),u\right)
 \kappa^B_\epsilon\!\left(q-\tfrac\epsilon2u,v-u\right)du.
 \tag{22b}
$$
The tangent-bundle law at zero still permits the decomposition
$v=u+(v-u)$, but the separate finite-scale centres have collapsed to
the same $q$. Its convolution is consequently fibrewise; Fourier
transformation makes its product commutative. The exact positive-scale
formula retains the shifts, rather than merely adding two tangent
vectors at an unchanged base point. Thus the bare zero-fibre bundle
does not retain where an intermediate finite-scale point was inserted.

For heat kernels with durations $t,u>0$, refinement additionally requires
integrating $K(t;x,y)K(u;y,z)$ over that inserted point to obtain
$K(t+u;x,z)$. The product at one chosen $y$ is one integrand, not the
whole composed kernel. A duration split is extra data beyond the ordinary
pair-groupoid arrow; the time-graded formulation in §6 records it.
This is compatible with (22b) and with the distinction between elimination
and pointwise action addition already proved there.

### The matched tangent limit

Take $a=\epsilon S_0$ and $r=s=\epsilon$. Equations (20)--(22) become
$$
 \widetilde H_{\epsilon,q}
 =-\frac{S_0^2}{2m}\partial_X^2+V(q+\epsilon X),
 \tag{23a}
$$
$$
 \epsilon K_{\epsilon S_0,V}
       (\epsilon T;q+\epsilon X,q+\epsilon Y)
 =K_{S_0,V(q+\epsilon\,\cdot)}(T;X,Y).
 \tag{23b}
$$
The potential on the right tends locally to $V(q)$. On
$C_c^\infty$, the operators consequently converge to
$H_{0,q}=-S_0^2\partial_X^2/(2m)+V(q)$ in norm on each test vector.
Fix an energy $E_{\rm ref}>0$. For $f$ in this core,
$$
 \begin{aligned}
 &(\widetilde H_{\epsilon,q}+E_{\rm ref})^{-1}
                         (H_{0,q}+E_{\rm ref})f-f\\
 &\quad=(\widetilde H_{\epsilon,q}+E_{\rm ref})^{-1}
                 (H_{0,q}-\widetilde H_{\epsilon,q})f\longrightarrow0.
 \end{aligned}
$$
The resolvents have norm at most $E_{\rm ref}^{-1}$ and
$(H_{0,q}+E_{\rm ref})C_c^\infty$ is dense, so convergence extends
strongly to every vector. Continuous functional calculus gives strong
convergence of the heat operators. Local kernel convergence, with a
rate, follows independently from the bridge calculation below.
There is no claim of operator-norm convergence on this one fixed
$L^2$ space: for a harmonic potential every positive-$\epsilon$ heat
operator is compact, while the limiting free heat operator times
$e^{-TV(q)/S_0}$ is not. A norm limit of compact operators would be compact.
This comparison under dilation is distinct from continuity of the
groupoid field with different zero and positive fibers.

For the symmetric chart $X=v/2$, $Y=-v/2$, define
$$
 \kappa_\epsilon(q,v;T)
 =\epsilon K_{\epsilon S_0,V}
       (\epsilon T;q+\epsilon v/2,q-\epsilon v/2).
 \tag{24}
$$
Then, locally uniformly in $q,v$ and in $T$ bounded away from zero and
infinity,
$$
 \kappa_\epsilon(q,v;T)\longrightarrow
 \kappa_0(q,v;T)
 =\sqrt{\frac m{2\pi S_0T}}
   \exp\!\left[-\frac{mv^2}{2S_0T}-\frac{TV(q)}{S_0}\right].
 \tag{25}
$$
The tangent Fourier transform is exactly
$$
 \int e^{-ivp/S_0}\kappa_0(q,v;T)\,dv
 =\exp\!\left[-\frac T{S_0}
              \left(\frac{p^2}{2m}+V(q)\right)\right].
 \tag{26}
$$
At fixed $q$, tangent-vector convolution of these Gaussian kernels
adds $T$; after Fourier transformation this is multiplication of the
displayed classical heat symbols. The boundary value is the
semiclassical symbol of the specified family $H_{\epsilon S_0,V}$.
It is not the ordinary principal symbol of a fixed second-order
operator, for which $V$ is lower order. Nor is (26) a real-time path
probability or a claim that every heat operator lies in a compact-operator
fiber. For example, a constant potential gives bounded multipliers,
not elements of $\mathcal K(L^2(\mathbb R))$, and its symbol does not
vanish at spatial infinity.

This scaling follows a family of near-diagonal arrows as well as changing
the physical duration. It is not a single orbit of the adiabatic zoom
in §6, which fixes the positive-fiber endpoints. The kinetic variance
$\hbar t/m=\epsilon^2 S_0T/m$ explains why the tangent displacement
is order $\epsilon$ here. At fixed positive physical $\hbar$, a
short-time diffusive displacement instead has order $\sqrt t$.

### The first surviving potential correction

Write $B_s$, $0\le s\le1$, for a standard real Brownian bridge and put
$$
 \sigma^2=\frac{S_0T}{m},\qquad
 \xi_s=(\tfrac12-s)v+\sigma B_s,\qquad
 A_\epsilon=\frac T{S_0}\int_0^1 V(q+\epsilon\xi_s)\,ds.
$$
The Feynman--Kac bridge formula gives
$$
 \kappa_\epsilon
 =\sqrt{\frac m{2\pi S_0T}}e^{-mv^2/(2S_0T)}
     \mathbb E e^{-A_\epsilon}.
 \tag{27}
$$
The formula is established: [Simon 1999](https://arxiv.org/pdf/math-ph/9907022),
Theorem 1.1 and equations (1.1)--(1.3), printed pp. 1--2, passages read.
The Brownian-bridge expansion is also standard Wigner--Kirkwood machinery;
see [Jizba--Zatloukal 2014](https://arxiv.org/pdf/1309.0206),
§IV, equations (34)--(42), passages read. The constants and local
remainder used here are derived next; no novelty is asserted for the method.

Let $I_1=\int_0^1\xi_s ds$ and $I_2=\int_0^1\xi_s^2 ds$.
The bridge covariance $\min(s,u)-su$ gives
$$
 \mathbb EI_1=0,\qquad
 \mathbb EI_1^2=\frac{\sigma^2}{12},\qquad
 \mathbb EI_2=\frac{v^2}{12}+\frac{\sigma^2}{6}.
$$
For example, integrating the covariance first in $u$ gives
$s(1-s)/2$, and its integral in $s$ is $1/12$.
Differentiating $\mathbb E e^{-A_\epsilon}$ twice at zero therefore yields
$$
 \kappa_\epsilon=\kappa_0
          [1+\epsilon^2 C(q,v,T)+O(\epsilon^3)],
 \tag{28a}
$$
$$
 C=\frac{T^3[V'(q)]^2}{24mS_0}
    -\frac{T V''(q)v^2}{24S_0}
    -\frac{T^2V''(q)}{12m}.
 \tag{28b}
$$
There is no linear term in this symmetric endpoint kernel. To justify
the expansion, $V\ge0$ bounds $e^{-A_\theta}$ by one for real
$\theta$. Bounded $V''$ gives
$|V'(q+\theta\xi)|\le |V'(q)|+\|V''\|_\infty|\theta\xi|$.
The first three derivatives of $e^{-A_\theta}$ are consequently bounded
by polynomials in $\int|\xi_s|^jds$, $j\le3$, with locally uniform
coefficients for $|\theta|\le1$. All required Gaussian moments are finite.
For an explicit remainder bound put $\beta=T/S_0$,
$G=|V'(q)|$, $L=\|V''\|_\infty$, $M=\|V'''\|_\infty$ and
$U_j=\int_0^1|\xi_s|^jds$. Define
$$
 \begin{aligned}
 \mathcal M(q,v,T)=\mathbb E\big[&\beta^3(GU_1+LU_2)^3\\
 &+3\beta^2 L(GU_1+LU_2)U_2+\beta M U_3\big].
 \end{aligned}
$$
The absolute value of the relative remainder in (28a) is at most
$\epsilon^3 e^{\beta V(q)}\mathcal M(q,v,T)/6$, for $0\le\epsilon\le1$.
This follows from $|\partial_\theta^3 e^{-A_\theta}|\le
|A'_\theta|^3+3|A'_\theta A''_\theta|+|A'''_\theta|$ and the bounds
above. The Gaussian moment constant is finite and locally uniform.
There is no uniform assertion over all $q$, all durations or arbitrary
singular potentials.

### Normalization that survives refinement

The full normalized bridge on the rescaled path $\xi$ has density
$$
 R_\epsilon=\frac{e^{-A_\epsilon}}{\mathbb E e^{-A_\epsilon}}
 =1-\epsilon\frac{T V'(q)}{S_0}I_1+O_{L^1}(\epsilon^2)
 \tag{29}
$$
relative to its free bridge. The same differentiation bounds prove this
$L^1$ expansion, with its normalizer bounded away from zero on the
stated compact sets. Thus the bridge changes at first order even though
the integrated symmetric kernel changes only at second order. In physical
coordinates its mean is
$$
 \mathbb E[q+\epsilon\xi_s]
 =q+\epsilon(\tfrac12-s)v
   -\epsilon^2\frac{T^2V'(q)}{2m}s(1-s)+O(\epsilon^3).
 \tag{30}
$$
Here the expectation is under the interacting bridge. The covariance
$\operatorname{Cov}(\xi_s,I_1)=\sigma^2s(1-s)/2$ proves the correction;
Gaussian moments justify the same expansion with the inserted $\xi_s$.
Its sign agrees with the Euclidean stationary equation $m\ddot q=+V'(q)$,
and must not be substituted for the real-time Newton force.

This comparison is uniform over refinements at the level of lifted
densities. On any partition of $[0,1]$, replace the integral in
$A_\epsilon$ by the endpoint trapezoidal sum and call it
$A_{\epsilon,\pi}$. For every continuous bridge path,
$$
 \sup_\pi\left|A_{\epsilon,\pi}-\frac{TV(q)}{S_0}\right|
 \le\frac T{S_0}\sup_s|V(q+\epsilon\xi_s)-V(q)|\longrightarrow0.
$$
All weights lie in $[0,1]$, so dominated convergence gives
$\sup_\pi\|R_{\epsilon,\pi}-1\|_{L^1}\to0$. At fixed $\epsilon$,
ordinary mesh refinement gives $R_{\epsilon,\pi}\to R_\epsilon$ in
$L^1$. Free polygonal interpolation converges uniformly pathwise as
$|\pi|\to0$. Therefore any joint schedule $\epsilon\to0$, $|\pi|\to0$
has the free rescaled bridge as its weak path limit. No relation between
the dimensionless mesh and $\epsilon$ is required. Total variation is
asserted for densities lifted to the common free path space, not for
polygon-supported measures against a non-polygonal Brownian law.
Exact projective consistency belongs to the complete heat-kernel bridges;
trapezoidal single-cell weights acquire generated terms when blocked.

Dividing each transition by its row integral is a different operation.
For $V(x)=m\omega^2x^2/2$, the Mehler kernel is
$$
 K_{a,V}(t;x,y)=\sqrt{\frac{m\omega}{2\pi a\sinh\omega t}}
 \exp\!\left[-\frac{m\omega[(x^2+y^2)\cosh\omega t-2xy]}
                  {2a\sinh\omega t}\right].
$$
It solves the heat equation with the delta initial condition.
Completing the square shows that its row-normalized transition is
$$
 N_t(x,dy)=\mathcal N\!\left(
       \frac{x}{\cosh\omega t},\frac{a}{m\omega}\tanh\omega t
                                      \right)(dy).
 \tag{31}
$$
The mean of $N_tN_u$ is $x/(\cosh\omega t\cosh\omega u)$, whereas
that of $N_{t+u}$ is $x/\cosh\omega(t+u)$. For $x\ne0$, $t,u>0$
they differ. Hence this normalized family is not a semigroup.
A genuine Markov semigroup, when a positive ground state exists, is the
[ground-state transform](constructive-qft-one-time.md#3-arbitrary-time-refinement),
which retains the eigenfunction ratios and vacuum-energy factor.

## 8. Which zoom resolves a quantum well?

The ordinary tangent chart samples distances of order $\epsilon$ and,
in (23), durations of order $\epsilon$. It freezes the potential locally.
To resolve a well rather than a diagonal kernel, use a different scaling.
For the separate model $V(x)=\lambda x^{2k}$, $k\ge1$, $\lambda>0$,
set $\hbar=\epsilon S_0$, $q=0$ and
$$
 s=\epsilon^{1/(k+1)},\qquad
 r=\epsilon^{(1-k)/(k+1)}.
 \tag{32}
$$
Equations (20)--(22) now give $a'=S_0$ and
$V_{r,s,0}(X)=\lambda X^{2k}$ exactly. Equivalently,
$$
 D_{0,s}H_{\epsilon S_0,V}D_{0,s}^{-1}
 =\epsilon^{2k/(k+1)}H_{S_0,V}.
 \tag{33}
$$
The equal exponents follow by balancing
$\epsilon^2/s^2=s^{2k}$. This is the standard homogeneous spectral
dilation, not a new gap theorem; the
[quartic construction](constructive-qft-one-time.md#2-a-vacuum-and-a-gap-from-the-hamiltonian)
already gives its $k=2$ case, and
[matrix-model scaling](low-dimensional-mass-gap.md#2-the-exact-hbar-scaling-of-spectra-for-homogeneous-potentials)
has its own operator and invariant-sector conditions.

| Limit, with $S_0$ fixed | Position scale | Physical duration scale | What remains |
| --- | --- | --- | --- |
| Matched ordinary tangent kernel | $\epsilon$ | $\epsilon$ | Free tangent heat kernel times $e^{-TV(q)/S_0}$ |
| Harmonic well, $k=1$ | $\epsilon^{1/2}$ | $1$ | Full fixed-action harmonic dynamics |
| Quartic well, $k=2$ | $\epsilon^{1/3}$ | $\epsilon^{-1/3}$ | Full fixed-action quartic dynamics |

The durations multiply a fixed reference time, and the position factors
multiply a fixed reference length or the coordinate $X$ in (20).
The two monomial gaps scale respectively as $\epsilon$ and
$\epsilon^{4/3}$ by (33); their existence is supplied by the confining
Hamiltonians. The growing quartic duration lies outside the bounded-$T$
local estimate (28). A well-resolving quantum limit therefore cannot be
inferred from that ordinary tangent estimate. It is a different rescaled
family; it does not replace the commutative zero fiber of (3).

All these constructions admit any supplied $S_0>0$. They construct no
independent action floor, and no preferred dimensional normalization of
the groupoid parameter. Identifying a particular member with measured
physical $\hbar$ still requires physical information. Normalized free
refinement at action zero remains the classical countermodel in §6.

## 9. Consequence for STATE

The constructed $0+1$ quantum family, the semiclassical Newton flow and
the user's tangent-groupoid framework meet in a state theorem with a
joint mesh/action error bound. The scalar scaling question now also has
an exact dilation/composition map, a controlled local interacting heat
kernel and a refinement-compatible normalized bridge. Ordinary tangent
and well-resolving limits use different spatial and temporal scales.
The strong product limit remains a fixed-$\hbar$ theorem. Physical
calibration, uniform control over growing times or noncompact preparations,
and four-dimensional Yang--Mills construction remain separate obligations.
