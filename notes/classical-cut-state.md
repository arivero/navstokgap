# What a classical cut must retain

A position-only cut loses the direction of motion of a fixed-energy spring
receiver. Exact segment laws then fail the composition law; independently
refreshing the missing direction at every cut converges to a frozen position.
Retaining canonical momentum restores exact composition on every partition.
The required datum has momentum units, and the available orbital action remains
set by the prepared energy.

## 1. Fixed experiment and exact maps

Use A10's two-body receiver with masses $m,M>0$, stiffness $k>0$, zero
centre position and total momentum. Put $q=x-X$, $\mu=mM/(m+M)$ and
$p=\mu\dot q$. The full internal phase state is $z=(q,p)$ and

$$H=\frac{p^2}{2\mu}+\frac{kq^2}{2},\qquad
\omega=\sqrt{k/\mu},\qquad
\Phi_t=\begin{pmatrix}
\cos\omega t&\sin\omega t/(\mu\omega)\\
-\mu\omega\sin\omega t&\cos\omega t
\end{pmatrix}.
$$

Fix $E>0$, $A=\sqrt{2E/k}$ and uniform phase on the ellipse $H=E$:
$q=A\cos\phi$, $p=-\mu\omega A\sin\phi$. This invariant preparation,
the Hamiltonian and the observable $q$ stay fixed throughout refinement.
The tagged position is $x=Mq/(m+M)$, so all position conclusions transfer by
this fixed factor. The maximum relative speed is $A\omega$; choosing $E$
small enough enforces any prescribed positive particle-speed ceiling.

Write $P(q,p)=q$, and let $L(q)$ be the conditional phase-state law given
position. For $|q|<A$, it gives equal weights to
$p=\pm\mu\omega\sqrt{A^2-q^2}$; at $q=\pm A$ it is the point mass at
$p=0$. This specifies a version even at the zero-probability endpoints.
The stationary position density is $[\pi\sqrt{A^2-q^2}]^{-1}$ on $(-A,A)$.
On probability laws define $U_t=(\Phi_t)_\#$, $P_\#\nu$ by projection, and
$L\rho=\int L(q)\rho(dq)$. The exact one-segment stationary conditional kernel is
$K_t=P_\#U_tL$; it is not a Markov transition semigroup for the position process. The following diagram names both procedures:

$$
\begin{array}{ccccc}
L\delta_q&\xrightarrow{U_s}&U_sL\delta_q
 &\xrightarrow{U_t}&U_{t+s}L\delta_q\\
&&\downarrow P_\#&&\downarrow P_\#\\
&&K_s\delta_q&\xrightarrow{K_t}&K_tK_s\delta_q.
\end{array}
$$

The upper route gives $K_{t+s}\delta_q$ after final projection. The lower
route inserts the operation $LP_\#$ at the interface. This operation replaces
the history-conditioned momentum law by its stationary conditional law.
It is an additional reset, whereas an observational cut simply records $q$.
Marginalizing the true joint path law retains all its correlations and is
restriction-consistent on every finite partition.

## 2. Composition defect and its missing information

For a starting position $q$, the exact kernel is the equally weighted pair

$$q'=q\cos\omega t\ \pm\sqrt{A^2-q^2}\sin\omega t.$$

In particular $\mathbb E[q_t\mid q_0=q]=q\cos\omega t$. Independently
composing these kernels gives mean $q\cos\omega s\cos\omega t$, while
the full route gives $q\cos\omega(s+t)$. Their difference (full minus reset)
is $-q\sin\omega s\sin\omega t$, which is generically nonzero. For example,
at $q=A/2$ and $s=t=\pi/(2\omega)$ the full mean is $-A/2$ and the reset
mean is zero. Thus these stationary two-time conditional kernels do not form
a semigroup.

The general block identity explains the missing term. Writing
$\Phi_t=\left(\begin{smallmatrix}a_t&b_t\\c_t&d_t\end{smallmatrix}\right)$,
its retained-to-retained block obeys
$a_{t+s}=a_ta_s+b_tc_s$. Here
$b_tc_s=-\sin\omega t\sin\omega s$: propagation into momentum and back
is lost by multiplying only the position blocks. The interface equation is
$q_{s+t}=a_tq_s+b_tp_s$. Momentum $p_s$ has units $ML/T$ and $b_t$ has
units $T/M$; their product supplies a length. No action parameter is needed
to close this equation.

On the fixed ellipse, position together with the sign of momentum suffices
away from the turning points, where momentum is zero. Uniformly in time the
phase state $(q,p)$ gives the unambiguous completion. An equivalent history
completion is two successive positions: if $\sin\omega\delta\ne0$, then

$$p_s=\mu\omega\frac{q_s\cos\omega\delta-q_{s-\delta}}
 {\sin\omega\delta}.$$

It becomes singular at half-period sampling, and its sensitivity to observation
error grows as $\delta\downarrow0$. Exact mathematical recoverability therefore
does not by itself establish a finite-precision physical readout.

## 3. Refining independent resets changes the motion

Let $T>0$ be fixed, $\delta=T/N$ and let $Q_N$ be the terminal position from
$N$ independently composed $K_\delta$ kernels, starting at $q$. Set
$c=\cos\omega\delta$. Conditional first and second moments give

$$\mathbb E Q_N=q c^N,\qquad
\mathbb E Q_N^2=\frac{A^2}{2}
 +\left(q^2-\frac{A^2}{2}\right)[\cos(2\omega\delta)]^N.$$

For the second formula, one step sends $q^2$ to
$q^2\cos(2\omega\delta)+A^2\sin^2\omega\delta$; subtract $A^2/2$ and
iterate. Since $N\delta^2=T^2/N\to0$, both cosine powers tend to one.
Consequently $\mathbb E[(Q_N-q)^2]\to0$. This is conditional terminal
$L^2$ convergence to a frozen position, at fixed $q,E,k,m,M,T$.
The full observational route remains $K_T$, independent of $N$, and is
nondegenerate for $|q|<A$ and $\sin\omega T\ne0$.

A directly measurable distinction survives averaging over the same stationary
preparation: the reset two-time correlation is
$(A^2/2)[\cos(\omega T/N)]^N\to A^2/2$, while the true correlation is
$(A^2/2)\cos\omega T$. Each reset kernel preserves the stationary one-time
position law, so equal one-time marginals conceal the change of experiment.
This limit concerns terminal and two-time observables; no path-topology limit
is asserted here.

## 4. Action bookkeeping and the selection obligation

The canonical orbital action with $1/(2\pi)$ normalization is

$$J=\frac1{2\pi}\oint p\,dq=\frac E\omega.$$

Indeed $p\,dq=\mu\omega A^2\sin^2\phi\,d\phi$ for increasing dynamical
phase, whose integral is $2\pi E/\omega$. Also uniform phase gives
$\langle q^2\rangle=E/k$, $\langle p^2\rangle=\mu E$ and
$\langle qp\rangle=0$, so $\sqrt{\det\operatorname{Cov}(q,p)}=E/\omega$.
Both have units $ML^2/T$. This normalization differs from A15's twice-area
estimator and is stated explicitly.

Within the single fixed preparation $J$ is conserved. Across preparations
$E\downarrow0$ at fixed Hamiltonian, $J\downarrow0$ and all the phase-state
composition identities still hold; $E=0$ supplies the equilibrium endpoint.
Thus exact classical cut composition in this experiment forces no positive
preparation-independent lower action. The present calculation settles a
candidate cut-state requirement and the classical-definition gate, while the
selection of a positive universal quantum-role parameter remains open.

## 5. Source construction and next experiment

I005's classical readings motivate retaining transition information across
cuts; its historical attributions remain in that idea entry. A10 and B23
supply the explicit spring receiver. Ford–Kac–Mazur p. 505, (2)–(5), supplies
the established harmonic propagator, and Zwanzig p. 219, (21)–(24), supplies
the complementary elimination-to-memory construction. The present fixed-energy
conditional kernels and reset limit are elementary consequences derived above.
[B33](../references/batches/B33.md) records bounded literature coverage and
[the review](../reviews/classical-cut-state-B33.md) records proof acceptance.

Next, retain tagged position **and momentum** while eliminating an independent
receiver mode in a three-body spring system. Determine the receiver memory
needed across a cut and whether finite observable history restores composition.
This distinguishes loss caused solely by omitting the observed body's velocity
from memory induced by a physical receiver. Keep Hamiltonian and preparation
fixed; trace any proposed action-valued observable to those inputs.
