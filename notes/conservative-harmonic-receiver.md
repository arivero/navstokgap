# A conservative receiver and the origin of a correlation scale

A finite harmonic receiver with fixed centre velocity has a vanishing
long-window displacement-action observable. Random centre velocity instead
adds a ballistic term. The exact normal-mode formula identifies the quantity
that must lose uniform control before a large receiver can sustain a positive
plateau: its low-frequency displacement weight.

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
coordinate and the preparation. This is the next selection test.

The finite model yields no physical-time attraction from the invariant
preparation: the observable already has no $t$ dependence. Next specify an
increasing spring network, its energy allocation and tagged spectral measure,
then compare taking receiver size and observation duration to infinity in
opposite orders. Derive any surviving constant from these mechanical inputs.
Mesh refinement of the same smooth trajectories is a third, distinct limit.

## 5. Source input and reproduction

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
Run `python3 scripts/harmonic_receiver_checks.py` for the exact modal,
two-body and three-body checks. C047 has coordinator proof review and a
sequential Luna-low prior-art audit. Its limits concern the stated observable
and preparation class.
