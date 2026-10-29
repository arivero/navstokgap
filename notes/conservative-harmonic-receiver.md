# A conservative receiver and the origin of a correlation scale

A finite harmonic receiver has a vanishing long-window action observable at
fixed centre velocity. An increasing periodic chain instead has plateau
$\Theta\sqrt{m/k}$ when its size tends to infinity first, with mode energy
$\Theta$ and spring stiffness $k$. A common hard particle-speed ceiling on
the stated phase preparation forces this plateau to close. The comparison
locates the positive scale in the low-frequency weights and energy preparation.
Sections 8–9 give the exact cut-state and memory proofs. The logically distinct
[apparatus construction](autonomous-finite-readout.md),
[calibration fibres](calibration-tolerance-recovery.md) and
[bounded-force information theory](causal-force-information.md) now carry their
full proofs without repeating them here. Historical coordinator/model checks
are internal written checks, not external peer review.

## 1. Hamiltonian and invariant preparation

Let $x,p\in\mathbb R^n$, $n\ge2$, $M=\operatorname{diag}(m_1,\ldots,m_n)$
with $m_i>0$, and let $K$ be a connected spring-network Laplacian. Thus
$K=K^T\ge0$ and $\ker K=\operatorname{span}\{\mathbf1\}$.
The Hamiltonian and equations are

$$
\mathcal H=\tfrac12p^TM^{-1}p+\tfrac12x^TKx,\qquad
\dot x=M^{-1}p,\quad\dot p=-Kx.
$$

Energy and total momentum are conserved. These linear equations give global
smooth trajectories. Write $D=M^{-1/2}KM^{-1/2}$ and choose an orthonormal
eigenbasis $e_0,e_1,\ldots,e_{n-1}$, with
$e_0=M^{1/2}\mathbf1/\sqrt{M_{\rm tot}}$ and positive eigenvalues
$\omega_j^2$ for $j\ge1$. Define canonical coordinates
$q_j=e_j^TM^{1/2}x$, $P_j=e_j^TM^{-1/2}p$.

Fix centre velocity $V_0=0$ and centre position. Assign internal mode energies
$E_j\ge0$, and independent phases $\phi_j$ uniform on $[0,2\pi)$. Then

$$
q_j(t)=\frac{\sqrt{2E_j}}{\omega_j}\cos(\omega_jt+\phi_j),\qquad
P_j(t)=-\sqrt{2E_j}\sin(\omega_jt+\phi_j).
$$

This is an invariant probability ensemble on the internal phase tori, even
when frequencies are commensurate. It is a preparation, not a mixing premise.
The total energy is $E=\sum_jE_j$, so
$|\dot x_i|\le\sqrt{2E/m_i}$ for every trajectory. Choosing
$E<\tfrac12(\min_i m_i)c^2$ puts all particles below $c$ in this frame.
These are Newtonian springs with a speed-bounded preparation; propagation of
signals and Lorentz covariance are separate model requirements.

## 2. Exact action observable and its limits (C047)

For tagged particle $i$, let $b_{ij}=e_{ji}/\sqrt{m_i}$, where $e_{ji}$
denotes component $i$ of vector $e_j$. Then
$v_i(t)=\sum_{j\ge1}b_{ij}P_j(t)$ has zero mean and covariance

$$
C_i(t)=\sum_{j\ge1}w_{ij}\cos(\omega_jt),\qquad
w_{ij}=b_{ij}^2E_j\ge0.
$$

Phase averaging gives this identity: distinct modes have zero cross covariance,
and one phase has $\mathbb E[P_j(t)P_j(0)]=E_j\cos(\omega_jt)$.
Integrating the covariance over the displacement square yields, for $\Delta>0$,

$$
\mathsf h_i(\Delta)=\frac{m_i}{\Delta}
\operatorname{Var}[x_i(t+\Delta)-x_i(t)]
=\frac{2m_i}{\Delta}\sum_{j\ge1}
\frac{w_{ij}}{\omega_j^2}[1-\cos(\omega_j\Delta)].
$$

The observable has action units and is independent of preparation time $t$.
Set $B_i=\sum_jw_{ij}/\omega_j^2$, with units of length squared. Then

$$
0\le\mathsf h_i(\Delta)\le\frac{4m_iB_i}{\Delta}\longrightarrow0
\quad(\Delta\to\infty).
$$

At short windows,
$\mathsf h_i(\Delta)=m_iC_i(0)\Delta+O(\Delta^3)$.
The finite cosine correlation has persistent memory; its ordinary improper
Green–Kubo integral need not exist. The finite-window formula above supplies
the relevant limit directly, without replacing the Hamiltonian dynamics by a
reversible dissipative generator.

## 3. Centre motion and the two-body receiver (C047)

An independent random constant centre velocity with variance $\sigma_0^2$
adds $m_i\sigma_0^2\Delta$ to $\mathsf h_i$. This follows from
$x_i(t+\Delta)-x_i(t)=V_0\Delta+$ internal displacement. The velocity
ensemble is stationary; for nonzero centre motion the absolute-position
ensemble need not be. A deterministic centre velocity contributes zero to
the variance and can be removed by a change of frame.

For two particles of masses $m,M_r$ coupled by a spring $k>0$, put
$\mu=mM_r/(m+M_r)$ and $\omega^2=k/\mu$. At zero total momentum,
$x_1=R+[M_r/(m+M_r)]r$, and assign relative energy $E$ with uniform phase.
The tagged response is

$$
\mathsf h_1(\Delta)=
\frac{2mE}{k\Delta}\left(\frac{M_r}{m+M_r}\right)^2
[1-\cos(\omega\Delta)].
$$

The spring is a genuine momentum receiver: $m\ddot x_1=-kr$ and
$M_r\ddot x_2=kr$. Its reversible exchange produces the oscillatory response
rather than the exponential memory law supplied by A02's refreshed bath.
Scaling every $E_j$ by $a^2$, $0<a\le1$, scales the entire response by $a^2$
while preserving the equations, conservation laws and speed margin.

## 4. What the large-receiver test must change (C047)

For a sequence of receivers and windows $\Delta_N\to\infty$, the bound
$\mathsf h_{i,N}(\Delta_N)\le4m_{i,N}B_{i,N}/\Delta_N$ shows that a
positive limiting response requires this upper bound to stay positive.
In particular, uniform control of $m_{i,N}B_{i,N}$ forces a zero limit.
Soft modes can enlarge $B_{i,N}$, but their weights depend on the measured
coordinate and the preparation. The periodic-chain construction below tests
this necessary growth condition explicitly.

The finite model yields no physical-time attraction from the invariant
preparation: the observable already has no $t$ dependence. The increasing spring network below specifies its energy allocation and tagged
spectral measure, and compares the two orders of receiver-size and observation-
duration limits. Its surviving constant comes from those mechanical inputs.
Mesh refinement of the same smooth trajectories is a third, distinct limit.

## 5. An increasing periodic chain (C048)

Take odd $N\ge3$ equal masses $m$ on a ring, with spring energy
$\frac{k}{2}\sum_{i=0}^{N-1}(x_{i+1}-x_i)^2$ (indices modulo $N$).
Fix the centre position and momentum. Give every real internal normal mode
energy $\Theta>0$ and independent uniform phase. Here $\Theta$ is a
preparation energy, and total energy is $(N-1)\Theta$.
The mode frequencies and tagged covariance are

$$
\omega_j=\Omega\sin(\pi j/N),\quad \Omega=2\sqrt{k/m},\qquad
C_N(t)=\frac{\Theta}{mN}\sum_{j=1}^{N-1}\cos(\omega_jt).
$$

The real sine/cosine eigenvectors have equal mode energies, so their paired
squared components sum to $2/N$ at each site. Applying §2 gives

$$
h_N(\Delta)=\frac{2\Theta}{N\Delta}\sum_{j=1}^{N-1}
\frac{1-\cos(\omega_j\Delta)}{\omega_j^2}.
$$

For each fixed $\Delta$, this Riemann sum converges to

$$
h_\infty(\Delta)=\frac{2m}{\Delta}\int_0^\Omega
\frac{1-\cos(\omega\Delta)}{\omega^2}\rho(\omega)\,d\omega,
\quad \rho(\omega)=\frac{2\Theta}{\pi m\sqrt{\Omega^2-\omega^2}}.
$$

This is a statement about limits of tagged covariances and increment variances;
it does not require a stationary absolute-position law for the infinite chain.
The density is integrable at its upper edge and continuous at zero. Splitting
at any fixed $0<a<\Omega$, the contribution from $[a,\Omega]$ is $O(1/\Delta)$.
In the lower interval substitute $y=\omega\Delta$. Dominated convergence,
using $(1-\cos y)/y^2\in L^1(0,\infty)$ and bounded $\rho$ on $[0,a]$,
gives

$$
\lim_{\Delta\to\infty}h_\infty(\Delta)
=\pi m\rho(0)=\frac{2\Theta}{\Omega}=\Theta\sqrt{m/k}.
$$

The integral $\int_0^\infty(1-\cos y)y^{-2}dy=\pi/2$ follows by
integration by parts and the Dirichlet sine integral. Thus

$$
\lim_{\Delta\to\infty}\lim_{N\to\infty}h_N(\Delta)=2\Theta/\Omega,
\qquad
\lim_{N\to\infty}\lim_{\Delta\to\infty}h_N(\Delta)=0.
$$

A joint regime is also explicit. Write
$f(z)=2(1-\cos z)/z^2=2\int_0^1(1-r)\cos(zr)\,dr$ with $f(0)=1$.
Then $|f'|\le1/3$. The integrand
$\Theta\Delta f(\Omega\Delta\sin\pi x)$ is Lipschitz with constant
at most $\pi\Theta\Omega\Delta^2/3$. A left Riemann sum error is at
most that constant divided by $2N$; removing its zero mode contributes
$\Theta\Delta/N$. Therefore

$$
|h_N(\Delta)-h_\infty(\Delta)|
\le\frac{\pi\Theta\Omega\Delta^2}{6N}+\frac{\Theta\Delta}{N}.
$$

At fixed $m,k,\Theta$, $\Omega\Delta_N\to\infty$ and
$(\Omega\Delta_N)^2/N\to0$ give the positive joint limit $2\Theta/\Omega$.
The action scale is selected by the input energy and spring timescale.

## 6. Energy and a common speed ceiling (C049)

The positive-plateau preparation has extensive total energy. Its phase support
also contains increasingly large tagged velocities. At site zero use the
standard real Fourier basis. Only the $(N-1)/2$ cosine modes contribute;
each has maximal velocity contribution $2\sqrt{\Theta/(mN)}$. Phases can
align, so the exact support maximum is

$$
\sup_{\phi}|v_0|=(N-1)\sqrt{\Theta/(mN)}.
$$

Every neighbourhood of the maximizing phases has positive preparation measure.
A common ceiling $|v_i|\le c$ for all supported trajectories thus requires
$\Theta_N\le mc^2N/(N-1)^2=O(1/N)$. This is a necessary condition
from one site; no sufficiency for all sites is inferred from that maximum.

Both bounded total energy and this necessary speed condition close the response
uniformly in the window. Indeed, $1-\cos z\le z^2/2$ gives
$h_N(\Delta)\le\Theta_N\Delta$. The identity
$\sum_{j=1}^{N-1}\csc^2(\pi j/N)=(N^2-1)/3$ gives

$$
h_N(\Delta)\le
\frac{4\Theta_N(N^2-1)}{3N\Omega^2\Delta},\qquad
\sup_{\Delta>0}h_N(\Delta)
\le\frac{2\Theta_N}{\Omega}\sqrt{\frac{N^2-1}{3N}}.
$$

The trigonometric identity follows by differentiating
$\sum_{j=0}^{N-1}\cot(x+\pi j/N)=N\cot(Nx)$ and subtracting the
$j=0$ singularity as $x\to0$. The last inequality uses
$\min(A\Delta,B/\Delta)\le\sqrt{AB}$.
For $\Theta_N=O(1/N)$ the uniform bound tends to zero. Thus this explicit
positive reservoir plateau uses a different preparation class from a family
with a common strict particle-speed ceiling. Its dependence on $\Theta$ also
leaves preparation-independent action selection open.

## 7. Source input and reproduction

Ford–Kac–Mazur, printed p. 505, (2)–(5), supplies the matrix harmonic
propagator. Their canonical preparation excludes zero eigenvalues at that
stage; ours fixes the centre and uses compact fixed-energy phase tori.
Zwanzig, p. 219, (21)–(24), supplies a complementary reduced-description
route: eliminate harmonic bath coordinates to obtain a cosine memory kernel.
That friction kernel differs from the tagged velocity covariance calculated
here. Its continuum replacement must be propagated through the tracer equation
before identifying a displacement coefficient.

[B23](../references/batches/B23.md) records the established ingredients,
derived finite-network consequence and bounded reading coverage.
Historical modal, two-body and three-body checks accompany C047's proof.
C047 has coordinator proof review and a
sequential Luna-low prior-art audit. Its limits concern the stated observable
and preparation class.

[B24](../references/batches/B24.md) audits §§5–6 against Ford–Kac–Mazur's
cyclic Fourier construction and its finite-sum/infinite-chain distinction,
printed p. 506, (12)–(24). The tagged density, plateau and speed-support bounds
are derived here with fixed-energy phases. The written mode, Riemann-sum and speed-support derivations above supply
the checks used here. Their preparation dependence remains a separate
selection question; historical computational checks are not proof premises.

## 8. What information survives a cut?

**C062–C063; written derivation and B33/coordinator review.**

A position-only cut loses the direction of motion of a fixed-energy spring
receiver. Exact segment laws then fail the composition law; independently
refreshing the missing direction at every cut converges to a frozen position.
Retaining canonical momentum restores exact composition on every partition.
The required datum has momentum units, and the available orbital action remains
set by the prepared energy.

### 8.1. Fixed experiment and exact maps

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

### 8.2. Composition defect and its missing information

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

### 8.3. Refining independent resets changes the motion

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

### 8.4. Action bookkeeping and the selection obligation

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

### 8.5. Source construction and next experiment

I005's classical readings motivate retaining transition information across
cuts; its historical attributions remain in that idea entry. A10 and B23
supply the explicit spring receiver. Ford–Kac–Mazur p. 505, (2)–(5), supplies
the established harmonic propagator, and Zwanzig p. 219, (21)–(24), supplies
the complementary elimination-to-memory construction. The present fixed-energy
conditional kernels and reset limit are elementary consequences derived above.
[B33](../references/batches/B33.md) records bounded literature coverage and
[the review](../reviews/classical-cut-state-B33.md) records proof acceptance.

The next section retains tagged position **and momentum** while eliminating an
independent receiver mode in a three-body spring system. It determines the
receiver memory needed across a cut and when finite observable history restores
composition, distinguishing omitted observed-body velocity from memory induced
by a physical receiver. Hamiltonian and preparation remain fixed, so the
action-valued observables can be traced to those inputs.

## 9. A third body: exact memory and recoverable history

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

### 9.1. One fixed mechanical experiment

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

### 9.2. Exact elimination at any cut

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

### 9.3. What fails when only tagged phase is carried

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

### 9.4. Finite-history recovery

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

### 9.5. What survives refinement, and what sets its scale

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

### 9.6. Source route

Zwanzig (1973), printed p. 219, equations (21)–(24), supplies the established
harmonic-bath elimination route; [B23's companion](../docs/batches/B23/harmonic-receiver-source-companion.md)
records the cached original and coverage. Section 8 (R03)
supplies the projection/reset distinction. The finite-history reconstruction
is a linear observability calculation, with the explicit block determinant
derived above. Hermann–Krener (1977), printed p. 733, Theorem 3.1 supplies
the general local weak observability framework, rather than the sampled
determinant formula. [B34's companion](../docs/batches/B34/receiver-memory-source-companion.md)
records three primary pages, and the [coordinator review](../reviews/three-body-memory-B34.md)
checks their scope and the derivation.

## Consequence for STATE

Finite receiver memory requires retained classical interface information, not
a positive universal action. The infinite-chain plateau uses supplied modal
energy and a specific thermodynamic order of limits; a common hard speed
ceiling closes this preparation’s plateau. Readout, complete-record recovery
and preparation-dependent ambiguity are proved in the separate canonical
treatments linked above. None constructs the local finite apparatus needed
for cusp-history branching or selects physical $\hbar$.
