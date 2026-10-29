# Lifting a Lipschitz Newton certificate to quantum mechanics

**Result, 2026-10-27; written derivation, unrefereed.** A classical
kick--drift existence certificate for a one-dimensional conservative
force with a global Lipschitz constant supplies the model-dependent
estimates for a specified noncommutative quantum construction. For
every supplied $\hbar>0$ it gives the Schrödinger representation, an
essentially self-adjoint Hamiltonian, a strongly continuous unitary
group, and arbitrary-partition convergence of the quantum kick--drift
products. On coherent preparations the same classical polygons and
quantum products agree at their vertices to $O(\sqrt\hbar)$,
uniformly in the mesh on a fixed time interval. Together with the
classical certificate this gives the requested joint observable limit.

This is a **bounded instance**, not a proof of the universal
constructive lifting conjecture formulated below.
The input includes the conservative action and a globally Lipschitz
force; the background analytic toolkit includes Nelson's commutator
theorem and the graph-domain propagation result cited below. No
lower bound on $V$ or derivatives beyond the Lipschitz force are
assumed. This real-time theorem does not construct a Euclidean
probability measure for a potential unbounded below.

The loss of the earlier $O(\hbar)$ rate is necessary at this level of
regularity: $V(q)=q|q|/2$ has globally Lipschitz force, but a centered
coherent packet has a momentum error of exact order $\sqrt\hbar$ at
small fixed positive times. No claim of literature priority is made.

**Targeted advisor check (GPT-6.1 Sol, 2026-10-27): ACCEPT.** The
advisor checked the $C^{1,1}$ domain and commutator estimates, the
fixed-action product and packet bounds, the square-root example,
and the connection to the conjecture. Following the check, explicit
grounded graph estimates, bounded extensions, the Duhamel integral,
the all-$L^2$ Cauchy modulus and the kick domain are included below. The
review is an internal model check, not independent peer review.

## Constructive lifting: the conjecture and its quantifiers

A proof may contain mathematical information that its author never
expresses in quantum terminology. Under the conjecture, a construction
of classical motion would also give enough control to construct quantum
evolution from the same mechanical data. A direct classical proof that
never mentions a Hilbert space therefore does not by itself refute this
interpretation. One must determine whether its assumptions and estimates
permit the quantum construction.

Literal textual inclusion would be a much stronger requirement on how
people write proofs. Conversely, appending an unrelated quantum existence
theorem to any classical proof would make containment uninformative. The
intended requirement is an explicit construction whose convergence uses
the classical data and estimates. Fix a named background analytic toolkit
before the test. Every model-dependent hypothesis needed to apply those
theorems must be supplied by the classical inputs or proved from them;
adding a new dynamical restriction would weaken the containment claim.

The word consistency also needs an identified object. Logical
consistency concerns the absence of contradictions in specified axioms.
Existence of a mathematical model can establish relative consistency
within the mathematical foundation used to construct it. Existence of
motion, uniqueness from initial data, continuous dependence, and
continuation for all time are different analytic properties. The present
programme addresses these analytic constructions and their relation to
quantum dynamics. It has not formulated a reduction between formal
arithmetical consistency statements for two axiomatic theories.

A Hilbert-space representation alone would admit a classical example.
For a complete Hamiltonian flow preserving phase volume, the operators
$(U(t)f)(z)=f(\Phi_{-t}(z))$ form a strongly continuous unitary group on
$L^2$ of phase space. Stone's theorem gives a self-adjoint generator;
multiplying it by any $h>0$ writes the same group as $e^{-itH_h/h}$.
Multiplication observables commute, and concentrating probability
packets recover the classical trajectory. This Koopman representation
would satisfy the weaker target without constructing the required
noncommutative quantum observables.

Fix a class $\mathcal A$ of mechanical actions, their state spaces,
initial or boundary data, and finite refinement rules. A classical
existence certificate means explicit estimates sufficient to construct
the classical dynamics. For a polygon proof these may include a common
bounded region on each finite time interval, a stability estimate and a
force-balance residual tending to zero with the mesh. The admissible
certificates must be specified before testing a proposed lift; defining
them to include quantum convergence would assume the conclusion.

**Constructive lifting conjecture.** Fix the action class, certificate
schema, quantum target and named background analytic toolkit. One
construction procedure for that class takes any admissible mechanical
data and classical certificate as input and constructs a compatible
quantum family $Q_\hbar$ for $\hbar\in E\subset(0,\infty)$ with
$0\in\overline E$. Every model-dependent hypothesis used in the quantum
construction must be supplied by those inputs or proved from them.
The procedure must identify which certificate estimates control quantum
refinement and the recovery of the classical dynamics on the stated
preparations and observables. Additional dynamical restrictions cannot
be introduced to complete the proof.

The proposed interpretation requires a single construction procedure for
the chosen class, rather than a separate unexplained choice for each
certificate. A certificate schema must not exclude a counterexample
after the test begins. A theorem for one class would establish a bounded
lifting result; extending it to every classical existence proof remains
the universal conjecture.

Existence at one isolated $\hbar>0$ cannot itself formulate an $\hbar\to0$
limit. The lifting statement therefore requires a family indexed by
positive values accumulating at zero. Requiring every sufficiently small
positive $\hbar$, or every $\hbar>0$, strengthens that requirement. The current
smooth-potential example constructs the quantum theory for every $\hbar>0$.
This family requirement makes the proposed lifting statement more
specific than a bare assertion that some quantum theory exists.

The word compatible requires an observable statement. In the current
example, fix $z_0$, a finite $T>0$, a time $t\in[0,T]$ and
$a\in C_c^\infty(T^*\mathbb R)$. For the specified coherent preparations
and partition vertices $t_j\to t$, the required limit is
$$
 \left\langle\psi_{\hbar,\pi}(t_j),
       \operatorname{Op}_\hbar^W(a)\psi_{\hbar,\pi}(t_j)\right\rangle
 \longrightarrow a(\Phi_t(z_0)),
 \qquad \hbar,|\pi|\longrightarrow0. 	ag{C}
$$
Here $z_0$ is the initial canonical state, $\Phi_t$ the constructed
classical flow, $\psi_{\hbar,\pi}(t_j)$ the state after the first $j$ quantum
cells, and $\operatorname{Op}_\hbar^W$ Weyl quantization. Partitions containing
$t$ permit $t_j=t$. The limit holds along every joint schedule with
$\hbar,|\pi|\to0$. A different action class may require different preparations,
observables and topologies while retaining its specified noncommutative
quantum target. Equation (1) does not require convergence of every quantum
state to a single classical point.

The common-hypothesis implication $\mathcal H\Rightarrow[C\ \mathrm{and}\ (\forall\hbar>0)Q_\hbar]$ is weaker than extracting the quantum construction from every certificate of $C$. The theorem below covers the declared conservative $C^{1,1}$ class. The [smooth quantum construction](quantum-blocks-construct-newton.md) separately supplies a Euclidean law and an $O(\hbar)$ mean rate under stronger derivative and lower-bound assumptions; the present rate is sharp at the weaker regularity.

The [1998 stationary-phase test](rivero-1998-conjecture-central-forces.md) preserves the action differences, Hessian square-root weights and signatures lost by a classical critical-point distribution. Its fixed-partition remainder is not a uniform quantum refinement estimate. Classical completion at a cusp or wall also need not select a unique quantum preparation or boundary condition ([cusp](cusp-quantum-preparation-selection.md), [wall](dirichlet-wall-impulse.md)). Neither the lifting conjecture nor this bounded theorem derives a universal positive physical action.

## 1. The input certificate and quantum target

Let $m>0$, $V\in C^1(\mathbb R;\mathbb R)$, and suppose
$$|V'(x)-V'(y)|\le L|x-y|,\qquad L\ge0.\tag{1}$$
Thus $V\in C^{1,1}$ and $V''$ exists almost everywhere with
$|V''|\le L$. The input is the mechanical action with kinetic term
$p^2/(2m)$ and potential $V$, the initial point $z_0=(q_0,p_0)$, and
the classical kick--drift polygons
$$
 p_{j+1}^{\rm cl}=p_j^{\rm cl}-s_jV'(q_j^{\rm cl}),\qquad
 q_{j+1}^{\rm cl}=q_j^{\rm cl}+s_jp_{j+1}^{\rm cl}/m.\tag{2}
$$
Take their linear interpolation for a partition $\pi$ of $[0,T]$.
The usual Lipschitz certificate supplies a unique limit $z(t)$ and
$$\sup_{t\le T}\|z_\pi^{\rm cl}(t)-z(t)\|_\omega
 \le R_T^{\rm cl}|\pi|,\qquad
 \|(q,p)\|_\omega=|q|+\frac{|p|}{m\omega}.\tag{3}$$
For example, the proof in the
[ODE lesson](balaban-ode-lesson.md) uses a common bounded region,
force-balance residual and Gronwall stability. Here $\omega>0$ is a
fixed auxiliary unit; $R_T^{\rm cl}$ depends only on the classical
data and $T$. No quantum convergence is included in the certificate.

For each $\hbar>0$ set, on $L^2(\mathbb R)$,
$$
 \begin{gathered}
 Qf(q)=qf(q),\quad P=-i\hbar\partial_q,\quad
 H_\hbar=P^2/(2m)+V(Q),\\
 K_{\hbar,s}=e^{-isV(Q)/\hbar},\quad
 D_{\hbar,s}=e^{-isP^2/(2m\hbar)}.
 \end{gathered}\tag{4}
$$
The self-adjoint $Q,P$ obey the Weyl relations and
$[Q,P]=i\hbar I$ on Schwartz space. Unlike the Koopman construction,
these observables are noncommutative.

## 2. The same force bound controls the operator domains

Fix $\hbar>0$ and calibrated units and put $N=1+Q^2+P^2$.
The input (1) implies
$$
 |V'(q)|\le |V'(0)|+L|q|,\qquad
 |V(q)|\le |V(0)|+|V'(0)||q|+\tfrac L2q^2.\tag{5}
$$
For $f\in\mathcal S$, integration by parts gives
$$
 2\operatorname{Re}\langle Q^2f,P^2f\rangle
  =2\|QPf\|^2-2\hbar^2\|f\|^2.\tag{5a}
$$
Together with $N\ge1$ and $PQ=QP-i\hbar$, this gives the
harmonic-oscillator graph bounds
$$
 \|Q^2f\|+\|P^2f\|+\|QPf\|+\|PQf\|
 \le C_\hbar\|Nf\|.\tag{5b}
$$
These estimates, (5), and the almost-everywhere bound on $V''$ imply on
$\mathcal S(\mathbb R)$
$$
 \|H_\hbar f\|\le C_\hbar\|Nf\|,\qquad
 \|[H_\hbar,N]f\|\le C_\hbar\|Nf\|.\tag{6}
$$
The commutator is a weak-derivative identity:
$$
 [H_\hbar,N]
 =-\frac{i\hbar}{m}(PQ+QP)
    +i\hbar\big(V'(Q)P+PV'(Q)\big).\tag{7}
$$
Products with $V'$ have the weak derivative $V''$; no third
derivative is used. For $f\in\mathcal S$, $H_\hbar f\in D(N)$,
so (6) gives
$$
 |\langle H_\hbar f,N^2f\rangle-\langle N^2f,H_\hbar f\rangle|
 \le2C_\hbar\langle f,N^2f\rangle.\tag{8}
$$
Schwartz space is a core for both $N$ and $N^2$. The first bound in
(6), together with the closedness of the eventual closure, also gives
$D(N)\subset D(\overline H_\hbar)$. Apply Nelson's commutator theorem
with comparison operator $N^2$: (6) gives its relative bound and (8)
its form-commutator bound. It follows that $H_\hbar$ is essentially
self-adjoint on $\mathcal S$.

Write $c_\hbar=\inf\sigma(N^2)$ and $G=N^2-c_\hbar\ge0$. Applying the
same estimate to the generator $H_\hbar/\hbar$ with $E_0=c_\hbar$,
using
[Energy-Limited Quantum Dynamics, Theorems 3.7--3.8](https://link.springer.com/article/10.1007/s00220-025-05282-w)
(statements and hypotheses read), shows that
$U_\hbar(t)=e^{-itH_\hbar/\hbar}$ preserves $D(N)$ and is strongly
continuous in its $N$-graph norm. Indeed $D(\sqrt G)=D(N)$ and
$\|\sqrt G f\|^2+c_\hbar\|f\|^2=\|Nf\|^2$. The constants in (6)--(8) follow
from $m,\hbar,L,V(0),V'(0)$; they are not additional assumptions on
the mechanical model.

## 3. A fixed-action quantum product estimate

The force certificate also controls the commutator of the two
factors. Write $T_\hbar=P^2/(2m)$ and, initially on Schwartz space,
$$[T_\hbar,V(Q)]
 =-\frac{i\hbar}{2m}\big(PV'(Q)+V'(Q)P\big).\tag{9}$$
It extends as a bounded map $D(N)\to L^2$. To justify the product
argument without assuming higher derivatives, mollify $V$ with an even
compactly supported unit-mass mollifier. The smooth $V_n$ satisfy
$\|V_n''\|_\infty\le L$ and have uniformly linearly growing first
derivatives. Moreover, Taylor's inequality gives
$$\|V_n-V\|_\infty
 \le \tfrac12L\,\varepsilon_n^2
          \int y^2\rho(y)\,dy\longrightarrow0.\tag{10}$$
This uniform bound holds even when $V$ is unbounded below.

For these $V_n$, define the finite constants
$$
 \eta_T=\hbar^{-1}\|[T_\hbar,N]N^{-1}\|,\quad
 \eta_V=\sup_n\hbar^{-1}\|[V_n(Q),N]N^{-1}\|,\quad
 B=\sup_n\|[T_\hbar,V_n(Q)]N^{-1}\|.\tag{11}
$$
Each commutator is initially computed on $\mathcal S$; the products
with $N^{-1}$ mean their unique bounded extensions from that core.
They are finite by (5) and the graph bounds above; their values can be
bounded from the classical data $m,L,V'(0)$ and the chosen
$\hbar$ and units. Use $\|Nf\|$ as an equivalent $N$-graph norm.
The induced graph norms of the kinetic, potential
and full groups are bounded by $e^{\eta_T|t|}$,
$e^{\eta_V|t|}$, and $e^{(\eta_T+\eta_V)|t|}$, respectively.

For smooth $V_n$, differentiation of
$U_n(s-r)D_rK_{n,r}$ and a second Duhamel integration give, on
Schwartz vectors,
$$
 \begin{aligned}
 (D_sK_{n,s}-U_n(s))f
 =-\frac1{\hbar^2}\int_0^s\!dr\int_0^r\!du\,
 U_n(s-r)D_{r-u}[T_\hbar,V_n(Q)]D_uK_{n,r}f.
 \end{aligned}\tag{11a}
$$
For each $n$, both finite factors preserve $\mathcal S$, so the
unbounded commutator here acts on a vector in its initial domain.
Taking norms in (11a) yields
$$
 \|(D_sK_{n,s}-U_n(s))f\|
 \le\frac{Bs^2}{2\hbar^2}
       e^{(\eta_T+\eta_V)s}\|Nf\|.\tag{12}
$$
The left factors in the integral are unitary; the commutator (9)
acts on $D_uK_{n,r}f$. Density extends (12) to $D(N)$.
Telescoping along the exact $U_n$ orbit and using the graph bound gives
$$
 \|U_{n,\pi}(T)f-U_n(T)f\|
 \le\frac{BT\,e^{(\eta_T+\eta_V)T}}{2\hbar^2}
      |\pi|\,\|Nf\|,\qquad f\in D(N).\tag{13}
$$
Equation (10) makes $U_n(t)\to U_\hbar(t)$ and each finite product
$U_{n,\pi}(T)\to U_{\hbar,\pi}(T)$ in operator norm for fixed
$\hbar,T,\pi$, by the bounded-perturbation Duhamel estimate.
The constants in (13) are uniform in $n$, so (13) passes to $V$.
It proves arbitrary-partition strong convergence for $f\in D(N)$;
density and unitarity extend convergence to all $L^2$ vectors. More
explicitly, if $C_{\hbar,T}$ is the coefficient of
$|\pi|\|Nf\|$ in (13), then for any $\psi\in L^2$
$$
 r_{\hbar,T,\psi}(\delta):=
 \inf_{f\in D(N)}\left[2\|\psi-f\|
              +C_{\hbar,T}\delta\|Nf\|\right]
 \longrightarrow0\quad(\delta\downarrow0).\tag{13a}
$$
Unitarity and (13) bound each product-to-unitary difference by
$r_{\hbar,T,\psi}(|\pi|)$; the triangle inequality gives the two-partition Cauchy criterion in the conjecture. The factor
$\hbar^{-2}B$ need not remain bounded as $\hbar\downarrow0$.

## 4. The classical and quantum polygons

Use the coherent packet of the
[quantum-blocks note](quantum-blocks-construct-newton.md), equation
(16), and let $(q_j,p_j)$ be the means after the first $j$ quantum
cells. The exact identities
$$
 K_s^*PK_s=P-sV'(Q),\qquad D_s^*QD_s=Q+sP/m\tag{14}
$$
hold on the propagated states; the $C^{1,1}$ potential preserves the
needed graph domain. In detail, $D(N)=H^2(\mathbb R)\cap D(Q^2)$,
and for $f\in D(N)$, weak differentiation gives
$$
 \begin{aligned}
 (K_s f)''=K_s\bigg(f''-\frac{2is}{\hbar}V'f'
 -\frac{is}{\hbar}V''f-\frac{s^2}{\hbar^2}(V')^2f\bigg).
 \end{aligned}\tag{14a}
$$
Here $V''\in L^\infty$, $V'$ grows at most linearly, and the
oscillator graph bound gives $qf',q^2f\in L^2$. Thus $K_s f\in H^2$
and $Q^2K_s f=K_sQ^2f\in L^2$. The drift preserves $D(N)$ by its
conjugation of $Q$ and the $QP,PQ$ graph bounds. Hence all finite
products preserve $D(N)$. Define
$$
 W_j=\operatorname{sd}Q_j+\frac{\operatorname{sd}P_j}{m\omega},
 \quad C=\sqrt{\frac2{m\omega}},\quad
 \beta=\omega+\frac{L}{m\omega}.\tag{15}
$$
As in the earlier note, (1) and (14) give
$$W_j\le C\sqrt\hbar\,e^{\beta t_j}.\tag{16}$$
No higher potential derivative or assumption of Gaussian shape after
the first step is used.

Put $e_j=\|(q_j,p_j)-(q_j^{\rm cl},p_j^{\rm cl})\|_\omega$.
For each kick,
$|\langle V'(Q)\rangle-V'(q_j^{\rm cl})|
 \le L(\operatorname{sd}Q_j+|q_j-q_j^{\rm cl}|)$.
The subsequent drift yields
$$
 e_{j+1}\le
 (1+s_j\omega)\!\left(1+\frac{s_jL}{m\omega}\right)e_j
 +\frac{s_jL}{m\omega}(1+s_j\omega)W_j.\tag{17}
$$
Since $e_0=0$, (16) and $1+x\le e^x$ imply the **mesh-uniform**
bound
$$
 e_j\le \frac{LC}{m\omega}\,t_j e^{\beta t_j}\sqrt\hbar.
 \tag{18}
$$
Combining this with the classical certificate (3) gives
$$
 \|(q_j,p_j)-z(t_j)\|_\omega
 \le \frac{LC}{m\omega}T e^{\beta T}\sqrt\hbar
       +R_T^{\rm cl}|\pi|.\tag{19}
$$
For $b\in C_c^\infty(\mathbb R^2)$, the Fourier/Weyl argument in
[the groupoid note](groupoid-quantum-newton-states.md), before its
second-order refinement, bounds the expectation error by a
symbol-dependent constant times the sum of $W_j$ and (19).
Therefore the observable limit required by the conjecture holds at
all partition vertices and along every joint schedule
$\hbar,|\pi|\to0$.

The proof uses the classical **input bound** (1) for both the graph
and packet estimates, while the certificate's polygon error (3)
controls recovery of the classical flow. The graph estimate (13) is a
separate fixed-$\hbar$ quantum estimate derived using the declared
operator toolkit; it is not assumed in (3). The input includes the
global action and its force bound, not merely the numerical convergence
rate of one orbit. A single trajectory need not determine $V$
elsewhere, so (13) is not claimed to follow from (3) alone.

## 5. Why the square-root rate cannot generally be improved

Set $m=1$ and
$$V(q)=\tfrac12q|q|,\qquad V'(q)=|q|.\tag{20}$$
The force is globally Lipschitz, and the classical solution from
$(0,0)$ is uniquely stationary. Define the unitary dilation
$(D_\hbar f)(q)=\hbar^{-1/4}f(q/\sqrt\hbar)$. Homogeneity gives
$$D_\hbar^{-1}H_\hbar D_\hbar=\hbar H_1,\qquad
 D_\hbar^{-1}P_\hbar D_\hbar=\sqrt\hbar\,P_1.\tag{21}$$
For the centered Gaussian $D_\hbar g_1$, the exact quantum momentum
is therefore $\langle P_\hbar\rangle_t=\sqrt\hbar\,f(t)$, where
$f(t)=\langle P_1\rangle_t$. Ehrenfest's identity gives
$$f'(0)=-\langle |Q|\rangle_{g_1}=-1/\sqrt\pi.\tag{22}$$
Thus $f(t)\ne0$ for every sufficiently small fixed $t>0$. The mean
error is exactly a nonzero multiple of $\sqrt\hbar$ there. This
counterexample does not contradict the $O(\hbar)$ theorem for bounded
$V'''$: $V'$ here has a corner at the origin.

## 6. Consequence for STATE

The bounded certificate-to-quantum test is affirmative for the
specified one-dimensional conservative $C^{1,1}$ action class. It
constructs the noncommutative target and a quantum product estimate
from the classical force data and the named analytic toolkit, and
uses the classical polygon certificate in the observable limit.
The universal conjecture, singular classical actions, quantum
completion uniqueness and independent positive-action necessity
remain open.
