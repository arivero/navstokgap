# A tangent-groupoid formulation of the quantum construction of Newton motion

**Result, 2026-10-27.** The tangent groupoid carries a continuous field
of observable algebras whose positive-parameter fibers are quantum and
whose zero fiber is classical. After fixing an action unit $S_*$ and
setting $h=\epsilon S_*$, the finite quantum products and classical
initial-value construction of
[the first document](quantum-blocks-construct-newton.md) define
compatible states on these fibers. On every compact time interval,
their values on smooth Weyl observables converge to the classical point
state with an explicit $O(\sqrt h+|\pi|)$ bound, for **every joint
schedule** with $h,|\pi|\to0$.

The result is a state-level limit for the specified coherent
preparations and globally bounded-Hessian potentials. The quartic
extension in the first document uses cutoff Hamiltonians; it does not
establish this estimate for uncut quartic quantum evolution. The result
neither makes the finite-product propagator uniformly
close to the exact quantum propagator as $h\to0$, nor makes a quantum
superposition a single classical trajectory. The groupoid parameter is a
geometric deformation parameter until the identification $h=\epsilon
S_*$ is chosen. The time mesh is an additional scale.

The [didactic guide](newton-dimock-balaban-guide.md) introduces the
Dimock--Balaban comparison and the point-particle examples. Its
Dirichlet hard-wall calculation is a separate construction; the
whole-line groupoid and state theorem below do not automatically cover
that boundary problem.

The groupoid and strict quantization are established: in particular,
Cariñena, Clemente-Gallardo, Follana, Gracia-Bondía, Rivero and Várilly,
[Connes' Tangent Groupoid and Strict Quantization](https://arxiv.org/abs/math/9802102)
(abstract and the prior repository companion), already includes the
user's work. Landsman--Ramazan's
[continuous-field construction](https://arxiv.org/abs/math-ph/0001005)
(abstract) supplies the general Lie-groupoid setting. The following
state estimate applies the first document's finite-slice bounds to
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
$$h=\epsilon S_*.\tag{4}$$
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

For the potential and hypotheses of the first document define
$$
 H_h=P^2/(2m)+V(Q),\qquad U_h(t)=e^{-itH_h/h}.\tag{7}
$$
The $H_h$ are unbounded operators and the $U_h(t)$ are generally
multipliers, not elements of the compact-operator fibers. At $h>0$
their adjoint action defines automorphisms of the compact operators:
$$\alpha_h^t(A)=U_h(t)^*AU_h(t).\tag{8}$$
The first document constructs the unique classical phase-space flow
$\Phi_t(q,p)$ before it is used here. On the zero fiber put
$$\alpha_0^t(a)=a\circ\Phi_t.\tag{9}$$
This is classical Hamiltonian evolution with
$H_{\rm cl}=p^2/(2m)+V(q)$.

For $a\in C_c^\infty(T^*\mathbb R)$, Weyl--Egorov compatibility for
the smooth subquadratic potentials of the first document gives, for
fixed $T$,
$$
 \sup_{|t|\le T}
 \|\alpha_h^t(\operatorname{Op}_h^W(a))
      -\operatorname{Op}_h^W(a\circ\Phi_t)\|
 \le C_{a,T}h^2.\tag{10}
$$
Here is the relevant estimate. The finite-time flow has bounded
derivatives on compact sets under the stated hypotheses, so
$a_s=a\circ\Phi_s$ is smooth, compactly supported, and has uniform
symbol bounds for $|s|\le T$. The kinetic commutator is exact. The
potential-commutator remainder after removing its classical first-order
term has kernel
$$
 \frac{i}{h}\left[V(x)-V(y)-(x-y)V'\!\left(\frac{x+y}{2}\right)\right]
 K_h^{a_s}(x,y).\tag{10a}
$$
The bracket is bounded by $\|V'''\|_\infty|x-y|^3/24$. Rapid decay of
the Fourier transform of $a_s$ in its momentum variable, the change
$x-y=hz$, and Schur's test bound the operator norm by $C_{a,T}h^2$.
Integrating this commutator remainder by Duhamel's formula gives (10).
This uses the standard Weyl calculus and the flow already constructed
in the first document; it is not being used to prove that flow exists.

## 3. A quantitative state on every fiber

Use the coherent packet $\psi_h^{q_0,p_0}$ of equation (16) in the
first document. For a partition $\pi$, let $\psi_{h,\pi,j}$ be the
state after its first $j$ kick--drift cells, and let
$z_{h,\pi}(t_j)=(q_j,p_j)$ be its means. Denote the constructed
classical state by $z(t)=\Phi_t(q_0,p_0)$. Define
$$
 I_a=(2\pi)^{-2}\int_{\mathbb R^2}
 |\widehat a(\xi,\eta)|\big(|\xi|+m\omega|\eta|\big)
 \,d\xi\,d\eta<\infty.\tag{11}
$$
Here $\widehat a$ is the ordinary Fourier transform in $(q,p)$.
Using the exact Fourier representation of Weyl quantization,
$$\operatorname{Op}_h^W(a)
 =(2\pi)^{-2}\int\widehat a(\xi,\eta)
             e^{i(\xi Q+\eta P)}d\xi\,d\eta,\tag{12}$$
and the spectral bound $\|(e^{iA}-1)\psi\|\le\|A\psi\|$,
$$
 |\langle\operatorname{Op}_h^W(a)\rangle_j-a(q_j,p_j)|
 \le I_a\!\left[
 \operatorname{sd}(Q)_j+\frac{\operatorname{sd}(P)_j}{m\omega}
 \right].\tag{13}
$$
The phase factor $e^{i(\xi q_j+\eta p_j)}$ is removed before applying
the inequality to the self-adjoint linear combination of centered
$Q,P$. Fourier inversion also gives
$|a(z)-a(z')|\le I_a\|z-z'\|_\omega$.

The first document's estimates (19) and (26) therefore give, at every
partition vertex $t_j\in[0,T]$,
$$
 \left|\langle\psi_{h,\pi,j},\operatorname{Op}_h^W(a)
                         \psi_{h,\pi,j}\rangle-a(z(t_j))\right|
 \le I_a\!\left[
 C e^{\beta T}\sqrt h+
 G_T(C_\delta|\pi|+C_h\sqrt h)\right].\tag{14}
$$
The constants $C,\beta,G_T,C_\delta,C_h$ are explicitly defined in
that document and depend on the common $h_0,T,V,m,\omega$ and initial
data, not on $h$ or the number of cells. No differentiability of an
unbounded quantum expectation is used in this step.

With $h=\epsilon S_*$, choose any $\alpha>0$ and a time unit $T_*>0$
so that $|\pi_\epsilon|\le T_*\epsilon^\alpha$. Equation (14) yields
$$
 \langle\operatorname{Op}_{\epsilon S_*}^W(a)\rangle_{\pi_\epsilon}
 \longrightarrow a(\Phi_t(q_0,p_0))
 \quad\text{at vertices tending to }t,\tag{15}
$$
with error $O(\epsilon^{1/2}+\epsilon^\alpha)$ at vertices equal to
$t$. Such a vertex can be inserted in each partition. There is no
constraint here on $|\pi_\epsilon|/h$.

This means that the vector states on the positive fibers approach the
point-evaluation state on the zero fiber, for the specified family of
preparations. For an arbitrary continuous section $A$, approximate
$A(0)\in C_0(T^*\mathbb R)$ uniformly by compactly supported smooth
symbols. Continuity of the field and the norm-one bound on states
extend (15) from these symbols to $A$. At fixed $h$, taking the mesh
limit recovers the exact unitary state as in the first document.
Both routes thus reach the same zero-fiber state; equality or
closeness of the two quantum vectors along an arbitrary joint schedule
has **not** been established.

## 4. A precise two-scale test on Euclidean increments

The preceding theorem concerns real-time operator states. It does not
claim that Euclidean sample paths are real-time trajectories. The
following free Gaussian calculation shows why the groupoid coordinate,
the action parameter and the duration must not be conflated.

Consider a drifted free reference increment
$$Y-X=u\delta+\sqrt{\frac{h\delta}{m}}\,Z,
 \qquad Z\sim N(0,1).\tag{16}$$
Set $h=\epsilon S_*$ and $\delta=T_*\epsilon^\alpha$ with
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

For each $\epsilon>0$ the first document supplies a complete tower
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
case. The older [groupoid note](tangent-groupoid-trajectories.md) is
to be read with these qualifications.

## 6. Consequence for STATE

The constructed $0+1$ quantum family, the semiclassical Newton flow and
the user's tangent-groupoid framework now meet in a concrete state
theorem with a joint mesh/action error bound. The strong operator
product limit remains a fixed-$h$ theorem; the Euclidean density tower
and the real-time coherent states have distinct roles. No positive
universal action scale or four-dimensional Yang--Mills result follows.

**Targeted advisor check (GPT-6.1 Sol, 2026-10-27).** An internal
mathematical review checked the chart and Fourier normalizations, the
state and Gaussian-scale bounds, the extension to continuous sections,
and the estimate (10). It is not independent peer review of the
underlying continuous-field theorem or of the literature.
