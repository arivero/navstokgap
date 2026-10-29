# A tangent-groupoid formulation of the quantum construction of Newton motion

**Result, 2026-10-27.** The tangent groupoid carries a continuous field
of observable algebras whose positive-parameter fibers are quantum and
whose zero fiber is classical. After fixing an action unit $S_*$ and
setting $\hbar=\epsilon S_*$, the finite quantum products and classical
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
geometric deformation parameter until the identification $h=\epsilon
S_*$ is chosen. The time mesh is an additional scale.

The [wall construction](dirichlet-wall-impulse.md) treats boundary domains
and impact separately; the whole-line theorem here does not cover that
problem. The [classical construction](balaban-ode-lesson.md) and
[quantum product theorem](quantum-blocks-construct-newton.md) supply the
dynamics used below.

The groupoid and strict quantization are established: in particular,
Cariñena, Clemente-Gallardo, Follana, Gracia-Bondía, Rivero and Várilly,
[Connes' Tangent Groupoid and Strict Quantization](https://arxiv.org/abs/math/9802102)
(abstract and the prior repository companion), already includes the
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

Choose an action unit $S_*>0$ and set
$$\hbar=\epsilon S_*.\tag{4}$$
For $a\in C_c^\infty(T^*\mathbb R)$, Weyl quantization has kernel
$$
 K_\epsilon^a(x,y)=\frac1{2\pi\epsilon S_*}
 \int_{\mathbb R}e^{i(x-y)p/(\epsilon S_*)}
       a\!\left(\frac{x+y}{2},p\right)dp.\tag{5}
$$
In chart (2),
$$
 \epsilon K_\epsilon^a
  \big(q+\epsilon v/2,q-\epsilon v/2\big)
 =\frac1{2\pi S_*}\int e^{ivp/S_*}a(q,p)dp.\tag{6}
$$
The rescaled kernel is the inverse Fourier transform of the zero-fiber
symbol. The established strict-quantization construction makes
$\epsilon\mapsto\operatorname{Op}_{\epsilon S_*}^W(a)$, together with
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
$x-y=hz$, and Schur's test bound the operator norm by $C_{a,T}\hbar^2$.
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
 I_aG_T(C_\delta|\pi|+C_hh).\tag{14}
$$
The constants $C,\beta,G_T,C_\delta,C_\hbar$ are explicitly defined in
that document and depend on the common $\hbar_0,T,V,m,\omega$ and initial
data, not on $\hbar$ or the number of cells. No differentiability of an
unbounded quantum expectation is used in this step.

With $\hbar=\epsilon S_*$, choose any $\alpha>0$ and a time unit $T_*>0$
so that $|\pi_\epsilon|\le T_*\epsilon^\alpha$. Equation (14) yields
$$
 \langle\operatorname{Op}_{\epsilon S_*}^W(a)\rangle_{\pi_\epsilon}
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
Set $\hbar=\epsilon S_*$ and $\delta=T_*\epsilon^\alpha$ with
$\alpha>0$. The physical-time difference quotient is
$$\frac{Y-X}{\delta}
 =u+\sqrt{\frac{S_*}{mT_*}}\,
       \epsilon^{(1-\alpha)/2}Z,\tag{17}$$
whereas the tangent-groupoid chart variable is
$$v_\epsilon=\frac{Y-X}{\epsilon}
 =uT_*\epsilon^{\alpha-1}
  +\sqrt{\frac{S_*T_*}{m}}\,
       \epsilon^{(\alpha-1)/2}Z.\tag{18}$$

- If $0<\alpha<1$, the physical-time quotient concentrates at $u$,
  but $v_\epsilon$ is not tight.
- If $\alpha=1$, $v_\epsilon$ converges in law to a nondegenerate
  Gaussian of mean $uT_*$ and variance $S_*T_*/m$.
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

The open RG problem is to construct a compatible control or blocking map
for the actual normalized kernels, states and generated interactions,
including the increments and all required limits, and then determine
whether its effective action has a universal physical identification.
Geometric zoom, coarse-graining and running parameters can participate
in one construction, but a geometric dilation alone does not establish
that construction or force $\hbar$ to run. The
[corrected groupoid comparison](groupoid-quantum-newton-states.md#geometric-zoom-and-kernel-composition) and
[scale correspondence](../research/refinement-correspondences.md)
keep these claims and their corrections distinct.


### Geometric zoom and kernel composition

The adiabatic zoom acts by $(x,y,\epsilon)\mapsto(x,y,\lambda^{-1}\epsilon)$
and $(x,v,0)\mapsto(x,\lambda v,0)$. Debord--Skandalis
[2014](https://doi.org/10.1016/j.aim.2014.02.012) and van Erp--Yuncken
[2019](https://doi.org/10.1515/crelle-2017-0035) (metadata read) relate this
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
kick--drift--kick cell $S_\hbar=K_{Fh/2}D_hK_{Fh/2}$ of the refinement note is
the variational (Störmer--Verlet) integrator of the trapezoidal discrete
Lagrangian $L_\hbar$, and the cubic counterterm turns $L_\hbar$ into the exact one.
The laws of Proposition 1 can be related through a Euclidean Laplace
limit: under coercivity and regularity conditions,
$-\hbar\log\int e^{-S/\hbar}dy\to\inf_y S$ as $\hbar\to0$
([Litvinov 2005](https://doi.org/10.1090/conm/377/06982), metadata).
This does not turn an oscillatory real-time integral into a probability
integral, nor make every stationary real-time branch a global minimum.


## 7. Consequence for STATE

The constructed $0+1$ quantum family, the semiclassical Newton flow and
the user's tangent-groupoid framework now meet in a concrete state
theorem with a joint mesh/action error bound. The strong operator
product limit remains a fixed-$\hbar$ theorem; the Euclidean density tower
and the real-time coherent states have distinct roles. No positive
universal action scale or four-dimensional Yang--Mills result follows.

**Targeted advisor check (GPT-6.1 Sol, 2026-10-27).** An internal
mathematical review checked the chart and Fourier normalizations, the
state and Gaussian-scale bounds, the extension to continuous sections,
and the estimate (10). It is not independent peer review of the
underlying continuous-field theorem or of the literature. The centered
$O(\hbar)$ state improvement in §3 is a subsequent written derivation and
was not part of that earlier check.
