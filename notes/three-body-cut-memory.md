# Tagged momentum and the memory of a third body

An equal-mass three-body spring chain requires receiver information at a cut
even when the tagged body's position and momentum are retained. Eliminating
the receiver gives an exact cosine memory kernel and two initial-data terms.
Two sufficiently close exact tagged phase observations recover the missing
state. This closes R04's finite-receiver test: memory supplies classical
interface information, while the available action scales remain preparation
dependent.

Proof status: C064–C065, accepted by written derivation and coordinator review,
2026-09-10. Literature status: established harmonic-bath elimination and
observability ingredients; explicit finite-chain formulas are derived
specializations. [B34](../references/batches/B34.md) records bounded coverage.

## 1. One fixed mechanical experiment

Take three particles on the line with equal mass $m>0$ and two springs of
stiffness $k>0$:

$$
H=\sum_{i=1}^3\frac{p_i^2}{2m}
 +\frac{k}{2}\big[(x_1-x_2)^2+(x_2-x_3)^2\big].
$$

Fix centre position and total momentum to zero. Write

$$x=x_1,\qquad y=x_2-x_3,\qquad
x_2=\frac{-x+y}{2},\quad x_3=\frac{-x-y}{2}.$$

The restricted kinetic energy is $3m\dot x^2/4+m\dot y^2/4$.
Consequently the canonical momenta are $P=\mu\dot x$, $Q=\nu\dot y$,
where $\mu=3m/2$ and $\nu=m/2$. **The physical tagged momentum is
$p_1=(2/3)P$.** Retaining $(x,P)$ therefore retains precisely the same
information as $(x_1,p_1)$; the rescaling accounts for centre reduction.

Put

$$a=\frac{9k}{4},\quad g=\frac{3k}{4},\quad d=\frac{5k}{4}.
\qquad
H=\frac{P^2}{2\mu}+\frac{Q^2}{2\nu}
 +\frac a2x^2-gxy+\frac d2y^2.$$

Here $ad-g^2=9k^2/4>0$, so the reduced quadratic Hamiltonian is positive
definite. Its phase domain is $\mathbb R^4$ and all trajectories are global
and smooth. Fix $E>0$ and the normalized microcanonical Liouville measure
$\delta(H-E)\,dx\,dP\,dy\,dQ$ throughout the cut experiment. This invariant
preparation has compact support. Energy conservation gives
$|\dot x_i|\le\sqrt{2E/m}$; choosing $E<mc^2/2$ supplies a hard particle
speed ceiling in this frame. As in A10, this is a Newtonian spring model,
with a speed-bounded preparation rather than a relativistic signal law.

## 2. Exact elimination at any cut

Hamilton's equations give

$$\mu\ddot x=-ax+gy,\qquad \nu\ddot y=gx-dy.$$

Let $\Omega^2=d/\nu=5k/(2m)$. Starting a segment at time zero,

$$
y(t)=y_0\cos\Omega t+\frac{Q_0}{\nu\Omega}\sin\Omega t
 +\frac{g}{\nu\Omega}\int_0^t\sin\Omega(t-s)x(s)\,ds.
$$

Substitution gives the exact reduced equation

$$
\mu\ddot x(t)+ax(t)
-\frac{g^2}{\nu\Omega}\int_0^t\sin\Omega(t-s)x(s)\,ds
=g y_0\cos\Omega t+\frac{gQ_0}{\nu\Omega}\sin\Omega t.
$$

Integration by parts rewrites it as

$$
\boxed{\mu\ddot x(t)+a_{\rm eff}x(t)
 +\int_0^t\Gamma(t-s)\dot x(s)\,ds=F_0(t)},
$$

where

$$
a_{\rm eff}=a-\frac{g^2}{d}=\frac{9k}{5},\qquad
\Gamma(t)=\frac{g^2}{d}\cos\Omega t=\frac{9k}{20}\cos\Omega t,
$$

$$
F_0(t)=g\left(y_0-\frac gd x_0\right)\cos\Omega t
 +\frac{gQ_0}{\nu\Omega}\sin\Omega t.
$$

The kernel has stiffness units $M/T^2$; its velocity convolution and $F_0$
have force units $ML/T^2$. Under the chosen preparation $F_0$ is a random
function determined by initial data, with its two quadratures correlated
through the energy constraint. No independent noise is introduced at later
cuts. The oscillatory memory is reversible, rather than a positive friction
coefficient describing irreversible energy loss.

At a cut $\tau$, the same formulas hold with $t$ replaced by $t-\tau$ and
$(x_0,y_0,Q_0)$ by $(x_\tau,y_\tau,Q_\tau)$. The inherited $(y_\tau,Q_\tau)$
encodes everything needed from earlier history. One may carry this pair or
carry the equivalent memory and its initial quadratures.

## 3. What fails when only tagged phase is carried

Write $u=(x,P)$, $w=(y,Q)$ and block the exact linear flow as

$$\binom{u_t}{w_t}
=\Phi_t\binom{u_0}{w_0},\qquad
\Phi_t=\begin{pmatrix}A_t&B_t\\C_t&D_t\end{pmatrix}.$$

Then

$$u_{s+t}=A_tu_s+B_tw_s,\qquad
A_{s+t}=A_tA_s+B_tC_s.$$

Thus composing full segments and then projecting retains the excursion into
the receiver and back. Multiplying only retained blocks discards $B_tC_s$.
At fixed energy, the states $x=P=Q=0$,
$y=\pm\sqrt{2E/d}$ have identical tagged phase but opposite tagged
accelerations $gy/\mu$. They establish that tagged phase alone cannot
determine a unique future over the preparation's support.

For conditional laws, let $L(u)$ be a version of the microcanonical
conditional receiver law given $u$, and $\mathcal P$ the tagged projection.
The exact one-segment conditional kernel is
$K_t=\mathcal P_\#(\Phi_t)_\#L$. Composing such kernels inserts
$L\mathcal P_\#$ at a cut: it refreshes the receiver from its stationary
conditional law instead of carrying the law conditioned on the full observed
history. The deterministic block identity identifies the lost channel; no
particular reset-refinement limit is claimed here. Marginalizing the true
joint path law instead preserves every coarse observation on every partition.

## 4. Finite-history recovery

The differential history gives a direct completion:

$$y(t)=\frac{\mu\ddot x(t)+ax(t)}g,\qquad
Q(t)=\frac\nu g\big[\mu x^{(3)}(t)+a\dot x(t)\big].$$

There is also an exact two-time phase completion. For a separation $\delta>0$,

$$u_t=A_\delta u_{t-\delta}+B_\delta w_{t-\delta}.$$

If $B_\delta$ is invertible, solve this equation for $w_{t-\delta}$ and
propagate to $w_t=C_\delta u_{t-\delta}+D_\delta w_{t-\delta}$.
Taylor expansion of the displayed Hamilton equations gives, in the row order
$(x,P)$ and column order $(y,Q)$,

$$
B_\delta=
\begin{pmatrix}
\dfrac{g}{2\mu}\delta^2+O(\delta^4)&
\dfrac{g}{6\mu\nu}\delta^3+O(\delta^5)\\
g\delta+O(\delta^3)&
\dfrac{g}{2\nu}\delta^2+O(\delta^4)
\end{pmatrix},
$$

$$\det B_\delta=\frac{g^2}{12\mu\nu}\delta^4+O(\delta^6).$$

The leading coefficient is positive, so every sufficiently small positive
$\delta$ permits exact recovery. Since $\Phi_\delta$ is analytic, exceptional
sampling separations are isolated zeros of this determinant on finite
intervals away from zero. For the local coefficients, differentiate
$\ddot x=(-ax+gy)/\mu$ and $\dot P=-ax+gy$: dependence on initial $y$
first enters $x$ at order two and $P$ at order one, while dependence on initial
$Q$ enters one order later. This also verifies the remainder parities.

Exact recovery becomes poorly conditioned as $\delta\downarrow0$: the
inverse block has entries growing as high as $\delta^{-3}$ in fixed physical
units. The observed difference must be known with correspondingly increasing
precision. This is an observability requirement, not a derived minimum action
or minimum time. It gives R05 a concrete physical question: what receiver and
back-reaction are required to obtain these observations at fixed precision?

## 5. What survives refinement, and what sets its scale

Observational refinement leaves the full flow and the kernel $\Gamma$
unchanged. The surviving interface object is a receiver phase pair or its
equivalent memory, with position and momentum units. Its existence follows
from the nonzero spring coupling.

For comparison with action, the chain Laplacian has eigenvalues $0,k,3k$,
with eigenvectors proportional to $(1,1,1)$, $(1,0,-1)$ and $(1,-2,1)$.
The two internal normal frequencies are therefore
$\omega_1=\sqrt{k/m}$ and $\omega_2=\sqrt{3k/m}$. In canonical normal
coordinates each modal action, normalized by $1/(2\pi)$ around its own
cycle on the invariant torus, is $J_j=E_j/\omega_j$. Hence at total energy $E$,

$$\frac E{\omega_2}\le J_1+J_2\le\frac E{\omega_1}.$$

The lower bound is a bound at supplied positive energy. Across preparations,
scale every coordinate and momentum by $b>0$ while keeping $m,k$ fixed.
Energy and both actions scale by $b^2$; the flow, memory kernel and sampling
invertibility conditions remain the same. The force and speed amplitudes
decrease with $b$. Thus genuine receiver memory survives as a structural law
while all these prepared action scales approach zero.

The next selection test should address physical acquisition of interface
information, rather than infer an action floor from memory alone. Specify a
mechanical readout and its disturbance, then test whether arbitrary refinement
at fixed useful accuracy remains possible under its independently stated
resources. The present finite receiver supplies the exact baseline for that
experiment.

## Source route

Zwanzig (1973), printed p. 219, equations (21)–(24), supplies the established
harmonic-bath elimination route; [B23's companion](../docs/batches/B23/harmonic-receiver-source-companion.md)
records the cached original and coverage. [R03](classical-cut-state.md)
supplies the projection/reset distinction. The finite-history reconstruction
is a linear observability calculation, with the explicit block determinant
derived above. Hermann–Krener (1977), printed p. 733, Theorem 3.1 supplies
the general local weak observability framework, rather than the sampled
determinant formula. [B34's companion](../docs/batches/B34/receiver-memory-source-companion.md)
records three primary pages, and the [coordinator review](../reviews/three-body-memory-B34.md)
checks their scope and the derivation.
