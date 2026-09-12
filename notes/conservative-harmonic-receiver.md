# A conservative receiver and the origin of a correlation scale

A finite harmonic receiver has a vanishing long-window action observable at
fixed centre velocity. An increasing periodic chain instead has plateau
$\Theta\sqrt{m/k}$ when its size tends to infinity first, with mode energy
$\Theta$ and spring stiffness $k$. A common hard particle-speed ceiling on
the stated phase preparation forces this plateau to close. The comparison
locates the positive scale in the low-frequency weights and energy preparation.

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
are derived here with fixed-energy phases. Six exact identities, four finite
ring spectrum/cosecant comparisons and four Riemann-bound tests were recorded
before the hard no-Python-verification rule; the handoff records that history.
The new uncommitted verification script and output were withdrawn under the rule.
Current mathematical verification uses the written proofs and source review. The next
mechanism must retain bounded velocities while supplying low-frequency response;
its preparation dependence remains a separate selection test.

## 8. What information survives a cut?

The fixed-energy two-body receiver gives an exact cut-state countertest:
position-only stationary conditional kernels fail composition, while retaining
momentum restores it. Independently refreshing direction at every inserted cut
preserves one-time position marginals but freezes terminal position as the mesh
shrinks. These are C062–C063; the full maps and proof are in
[the cut-state note](classical-cut-state.md), with the [B33 audit](../references/batches/B33.md).

With $q=x-X$, $\mu=mM/(m+M)$, $\omega=\sqrt{k/\mu}$ and
$A=\sqrt{2E/k}$, uniform phase on the energy ellipse gives the conditional
one-segment positions

$$q'=q\cos\omega t\ \pm\sqrt{A^2-q^2}\sin\omega t$$

with equal weights. Thus the full mean after $s+t$ is $q\cos\omega(s+t)$,
whereas independent conditional composition gives $q\cos\omega s\cos\omega t$.
The missing interface variable is $p_s=\mu\dot q_s$ in
$q_{s+t}=q_s\cos\omega t+p_s\sin\omega t/(\mu\omega)$.
It has momentum units. Keeping this full internal state composes exactly;
marginalizing the true joint path law also preserves all cut restrictions.

For $N$ independent resets at intervals $T/N$, direct iteration gives

$$\mathbb E Q_N=q[\cos(\omega T/N)]^N,$$
$$\mathbb E Q_N^2=\frac{A^2}{2}
 +\left(q^2-\frac{A^2}{2}\right)[\cos(2\omega T/N)]^N.$$

The first limit is $q$ and the second is $q^2$, proving terminal conditional
$L^2$ convergence to the starting position. Under the original stationary
preparation the reset two-time correlation tends to $A^2/2$, while the true
value is $(A^2/2)\cos\omega T$. A cut that only observes the motion performs
no reset and leaves the true correlation unchanged.

The normalized orbital action is $J=(2\pi)^{-1}\oint p\,dq=E/\omega$:
integrating $\mu\omega A^2\sin^2\phi$ over a cycle proves the formula.
Uniform-phase covariance also has square-root determinant $E/\omega$.
Cooling $E\downarrow0$ at fixed Hamiltonian closes both, with exact phase-state
composition intact. R04 extends this test to a third body, as follows.

## 9. A third body: exact memory and recoverable history

Retaining tagged momentum leaves receiver memory in the equal-mass open
three-body chain. At zero centre position and momentum, let $x=x_1$,
$y=x_2-x_3$, $\mu=3m/2$, $\nu=m/2$, $P=\mu\dot x$ and $Q=\nu\dot y$.
Physical tagged momentum is $p_1=2P/3$. The internal Hamiltonian is

$$H=\frac{P^2}{2\mu}+\frac{Q^2}{2\nu}
+\frac{9k}{8}x^2-\frac{3k}{4}xy+\frac{5k}{8}y^2.$$

For fixed microcanonical energy $E>0$, eliminate $y,Q$ exactly. With
$g=3k/4$, $d=5k/4$ and $\Omega^2=5k/(2m)$,

$$\mu\ddot x+\frac{9k}{5}x
+\int_0^t\frac{9k}{20}\cos\Omega(t-s)\dot x(s)\,ds=F_0(t),$$

$$F_0(t)=g\left(y_0-\frac gd x_0\right)\cos\Omega t
+\frac{gQ_0}{\nu\Omega}\sin\Omega t.$$

These inherited quadratures carry the receiver information across a cut.
The kernel has stiffness units; its convolution is a force. The full proof
in [R04](three-body-cut-memory.md) also recovers the hidden pair from tagged
phase at two sufficiently close times. The relevant block determinant is
$g^2\delta^4/(12\mu\nu)+O(\delta^6)$; inverse entries grow up to
$\delta^{-3}$. Exact recovery and finite-precision physical readout therefore
pose different requirements.

The internal frequencies are $\sqrt{k/m}$ and $\sqrt{3k/m}$, and modal
actions are $E_j/\omega_j$. Cooling scales the actions to zero while keeping
the memory kernel fixed. C064–C065 and [B34](../references/batches/B34.md)
record this derived specialization of harmonic-bath elimination and
observability. R05 supplies the following readout test.

## 10. Readout precision and a scalable classical instrument

Two sequential classical probes read the tagged pair with vanishing error and
back-reaction under increasingly concentrated preparations. With canonical
probe pairs $(q,\pi)$, $(r,\rho)$ and integrated interaction Hamiltonians
$G_x=\alpha x\pi$, $G_P=\beta P\rho$, the pre-cut estimates and kicks are

$$\widehat x=x+q/\alpha,\qquad
\widehat P=P+r/\beta-\alpha\pi,$$
$$d_x=\beta\rho,\qquad d_P=-\alpha\pi.$$

Here $\alpha$ is dimensionless and $\beta$ has units $T/M$. For incoming
rectangular support half-widths $(s_q,t_q,s_r,t_r)$, the intrinsic support
accuracy-disturbance products are $s_qt_q$ and $s_rt_r$, in action units.
Both can approach zero across ordinary positive-volume classical preparations.

At fixed horizon $T$, put $\eta=(T/N)/t_*$ with fixed time unit $t_*$.
Widths $O(\eta^4)$ yield hidden-state recovery error $O(\eta)$ after the
cubic inverse amplification, including the intervening kick. The accumulated
state disturbance is $O(\eta^3)$ uniformly over the horizon. The original
receiver preparation stays fixed, while fresh probe count and total fixed-mass
probe mass grow as $O(\eta^{-1})$.

C066–C067, the [full readout proof](classical-readout-refinement.md) and
[B35](../references/batches/B35.md) specify this externally switched impulsive
instrument. Its ideal position records and shrinking probe widths leave
preparation and recording resources open. R06 supplies the finite-duration
construction below; readout conditioning and canonical reaction alone have
not excluded zero action.

## 11. Finite-duration readout with an autonomous clock

One mechanical clock and four free probes suffice for delayed reconstruction
of the three-body receiver at fixed total apparatus mass. Let $(s,p_s)$ be the
clock pair, $(q_j,\pi_j)$ the probe pairs, and all five masses be positive and
fixed. With fixed stiffness $K$ and dimensionless $0<\lambda\le\lambda_0$,
the autonomous Hamiltonian is

$$H_\lambda=H+\frac{p_s^2}{2M_c}
 +\sum_{j=1}^4\frac{\pi_j^2}{2M_j}
 +\lambda K\sum_{j=1}^4f_j(s)X(x)R(q_j).$$

The functions $X,R$ are bounded smooth coordinate cutoffs, equal to their
arguments on the admitted trajectories. Fixed smooth bumps $f_j$ switch the
couplings as a prepared clock moves through them. Pulse widths and observation
time $T>0$ stay fixed. The interaction forces are globally bounded; harmonic
forces are uniformly bounded on the fixed receiver energy preparation and
bounded apparatus energy class. All kinetic terms are positive.

The reference output $x^0(t)$ determines $z_0=(x_0,P_0,y_0,Q_0)$: its first
four derivative rows have triangular diagonal
$1,1/\mu,g/\mu,g/(\mu\nu)$. Analyticity supplies four independent time
evaluation rows. Choosing sufficiently narrow but fixed positive-width bumps
preserves independence of the integrated matrix

$$\mathcal A_{j\cdot}=K\int_0^T f_j(s_0+vt)e_x\Phi_t\,dt.$$

For incoming apparatus support widths $b$ in fixed component units, Hamilton's
equations and finite-horizon integration give

$$\boldsymbol\pi(T)=\boldsymbol\pi(0)-\lambda\mathcal A z_0
 +O(\lambda b+\lambda^3),\qquad
\sup_t\|z(t)-\Phi_tz_0\|=O(\lambda b+\lambda^2).$$

These estimates include clock reaction. The clock leaves the pulse supports
with positive momentum, after which the four probe momenta are conserved.
Exact access to them gives the calibrated estimate
$\widehat z_0=-\mathcal A^{-1}\boldsymbol\pi(T)/\lambda$, with error
$O(b/\lambda+b+\lambda^2)$. Choosing $b=\lambda^3$ makes reconstruction
and disturbance both $O(\lambda^2)$ at fixed nonzero clock mean energy.
Initial canonical position error times maximum canonical momentum disturbance
is then $O(L_*P_*\lambda^4)$, in action units for fixed units $L_*,P_*$.

C068–C069 and [the full autonomous proof](autonomous-finite-readout.md)
specify the compact preparation domain, cutoff continuation and uniform
estimates; [B37](../references/batches/B37.md) audits the pointer and
observability precedents. The result uses increasingly precise preparation,
exact final records and known dynamics. All reported cuts may be refined from
the same four records after fixed latency $T$. R07 supplies the following
separate new-information test. The upper mass, duration and force resources
alone leave the autonomous readout's action product with zero infimum.

## 12. A delayed observer with an unresolved force

A single-particle information task yields a sharp prediction lower bound.
Keep exact records through time zero, including $(q_0,p_0)$, but allow no
new record before the prediction time $\ell>0$. Let the unknown external
force be any measurable $f$ with $|f|\le F$. This explicitly differs from
the reconstructed known dynamics above. For mass $m>0$,

$$v:=p(\ell)-p_0=\int_0^\ell f(s)ds,\qquad
u:=q(\ell)-q_0-p_0\ell/m=\frac1m\int_0^\ell(\ell-s)f(s)ds.$$

The forces $+F$ and $-F$ have identical accessible records. Their endpoint
separations imply worst-case prediction errors of at least $F\ell^2/(2m)$
and $F\ell$. Inertial prediction attains both, so the product of coordinate
minimax errors is exactly $F^2\ell^3/(2m)$, in action units.

The joint region carries more information than these two error bars. Writing
$d=v/(F\ell)$ and $z=mu/(F\ell^2)$, it is exactly

$$-1\le d\le1,\qquad |z-d/2|\le(1-d^2)/4.$$

At fixed impulse, maximal early positive force and maximal late negative
force give the upper boundary; reversing their order gives the lower one.
Convex combinations fill the region. Integrating its width gives canonical
area $2F^2\ell^3/(3m)$, without a $2\pi$ normalization. This area describes
admissible alternatives, not a lower action for each individual motion.

C070–C071: [proof](causal-force-information.md), [source audit](../references/batches/B38.md).
The area closes with force budget or delay. R08 supplies the cut-composition result below.

## 13. Exact cuts and observed-position information

At fixed total horizon $T=a+b$, an unobserved cut preserves the bounded-force
reachable set exactly. Write $S_b(q,p)=(q+bp/m,p)$ and let $K_t$ be the
increment lens above with duration $t$. Splitting and concatenating admissible
force inputs proves

$$K_T=S_bK_a+K_b.$$

The sum is Minkowski addition; every finite unobserved refinement therefore
leaves the old endpoint region and its canonical area unchanged. Replacing
$K_a$ by its marginal rectangle admits incompatible position–momentum pairs
and strictly enlarges the propagated set.

An exact, non-disturbing phase-state record at the cut leaves a translate of
$K_b$, with area $2F^2b^3/(3m)$. An exact position record instead leaves a
momentum interval of width

$$D=Fa\,[\sqrt{2-4\zeta}+\sqrt{2+4\zeta}-2],\qquad
\zeta=\frac{m(q_a-q_0-p_0a/m)}{Fa^2}\in[-1/2,1/2].$$

Its terminal area is $2F^2b^3/(3m)+Fb^2D/m$. To obtain the added area,
shear the momentum segment vertically: each convex section lengthens by $D$
over a transverse width $Fb^2/m$. As $b\to0$, this area vanishes uniformly,
but the central-record momentum width tends to $2(\sqrt2-1)FT$.
Area closure alone therefore does not establish momentum recovery.

C072–C073: [proof and assumptions](reachable-cut-composition.md),
[B39 audit](../references/batches/B39.md). The finite-precision extension follows.

## 14. Finite precision and residual delay

A record $|q-y|\le\varepsilon$ clips the cut lens to a convex set $C$ with
position interval $[l,r]$. Let its increasing momentum-fibre endpoints be
$L(q),U(q)$, its area $A_C$, its width $w=r-l$, and
$D_*=U(r)-L(l)$. The exact terminal set is $S_bC+K_b$, with area

$$|S_bC+K_b|=A_C+\frac{2F^2b^3}{3m}+2Fbw+\frac{Fb^2}{m}D_*.$$

After the inverse shear, each future-force segment adds a transverse width
$w+sD_*/m$; integrating its extrusion gives the two mixed terms. Exact
position and unobserved full-lens records recover the preceding formulas.
Since $w\le2\varepsilon$, $D_*\le2Fa$ and $A_C\le2Fa w$,

$$|S_bC+K_b|\le4FT\varepsilon+\frac{2F^2ab^2}{m}
+\frac{2F^2b^3}{3m}\longrightarrow0$$

for every joint precision/delay limit at fixed $F,m,T=a+b$.
Central records still leave finite momentum uncertainty. R10 therefore tests
two position records, separating recovery of both coordinates from area closure.
C074–C075: [complete formula and proof](finite-precision-cut.md),
[B40 audit](../references/batches/B40.md).

## 15. Two records and recovery of momentum

Positions recorded at $t_1=T-b-\delta$ and $t_2=T-b$, with errors bounded
by $\varepsilon_1,\varepsilon_2$, give the momentum estimate
$\widehat p=m(y_2-y_1)/\delta$. Define

$$B=\frac{m(\varepsilon_1+\varepsilon_2)}\delta+\frac{F\delta}2.
\qquad R_p=B+Fb,\qquad
R_q=\varepsilon_2+\frac{bB}{m}+\frac{Fb^2}{2m}.$$

These errors of $\widehat p$ and $\widehat q_T=y_2+b\widehat p/m$ are
simultaneously attained by constant force and adverse record errors.
The compatible-set area is at most $4R_qR_p$. If $\delta,b\to0$ and
$(\varepsilon_1+\varepsilon_2)/\delta\to0$, both coordinates are recovered.

For equal errors, the established finite-difference optimum is
$\delta_*=2\sqrt{m\varepsilon/F}$. Choosing positive delay $b=\delta_*$
gives $R_p=4\sqrt{mF\varepsilon}$, $R_q=7\varepsilon$, and an action-error
product $28\sqrt{mF}\varepsilon^{3/2}\to0$. R11 tests minimax lower bounds.
C076–C077: [proof](two-position-recovery.md),
[exact prior-art match](../references/batches/B41.md).

## 16. A gap that survives dense noisy records

At fixed position tolerance $\varepsilon>0$, even the entire noisy position
history leaves a sharp momentum uncertainty. Put
$d=2\sqrt{m\varepsilon/F}$, $t_2=T-b$, $t_1=t_2-d$, and assume $t_2\ge2d$.
Starting from zero displacement and velocity, forces $-F,+F$ for successive
times $d/2$ prepare displacement $-\varepsilon$ with zero velocity at $t_1$.
Force $+F$ for the next $d$ reaches $+\varepsilon$ and momentum $Fd$.
The entire observed displacement stays in $[-\varepsilon,\varepsilon]$.

This trajectory and its opposite have the same initial state and admit the
same inertial position record, with opposite allowed record errors. Continuing
their forces through the blind interval yields terminal half-separations

$$P_*=Fd+Fb,\qquad
Q_*=\varepsilon+\frac{Fdb}{m}+\frac{Fb^2}{2m}.$$

Every estimator has worst-case coordinate errors at least $P_*,Q_*$.
The preceding two-record estimator attains both; these are therefore exact
coordinate minimax risks for two records and for the complete noisy history.
At zero blind delay their product is
$2\sqrt{mF}\varepsilon^{3/2}>0$. Densifying records preserves this bound;
improving their tolerance closes it.

The construction is established in Seeber–Haimovich Proposition 3.1. R11
connects it to reachable fibres and delayed phase prediction. The general
principle is that, for symmetric convex inputs and bounded linear record
errors, the central compatible fibre maximizes scalar output uncertainty:
any compatible pair has an admissible half-difference, and the symmetric
central pair realizes its diameter.

C078–C079: [proof and precise information classes](indistinguishable-phase-bound.md),
[B42 audit](../references/batches/B42.md). The following composition test
settles the proposed transfer to mass universality.


## 17. Worst-case composition and the cost of aggregate records

Product bounded-force/error classes add scalar minimax radii linearly. For
positive masses with known initial states, complete position records of errors
$\varepsilon_i>0$, forces $|f_i|\le F_i$ and common terminal time
$T\ge\max_i4\sqrt{m_i\varepsilon_i/F_i}$, put
$M=\sum_i m_i$, $E=\sum_i m_i\varepsilon_i/M$ and $F_\Sigma=\sum_iF_i$.
With all constituent records retained, the exact centre position and total
momentum risks are

$$Q_A=E,\qquad P_A=2\sum_i\sqrt{m_iF_i\varepsilon_i}.$$

The central compatible fibre is a Cartesian product. Its support in a scalar
sum direction is the sum of the supports, attained by aligned symmetric
extremizers; R11's midpoint argument converts that radius into exact minimax
risk. For n identical constituents the product is therefore $H_A=nH_1$.
It does not obey A08's invariant variance-coefficient law.

Keeping only the weighted sum of the records gives exactly the single-body
force/error class $(M,F_\Sigma,E)$. To lift any aggregate force f and error e
back to the original constituents, choose
$f_i=F_i f/F_\Sigma$ and $e_i=\varepsilon_i e/E$, preserving each initial
state. Thus its exact risks are

$$Q_B=E,\qquad P_B=2\sqrt{M F_\Sigma E}\ge P_A.$$

Equality holds precisely when $F_i/(m_i\varepsilon_i)$ is common to all
constituents. Otherwise losing the individual records strictly increases the
momentum risk in the same mechanical model.

If mass-only nonnegative coordinate radii are closed under product composition
for every positive mass, additivity forces $Q(m)=q_*$, $P(m)=p_*m$.
Their action product is extensive; a mass-independent product must be zero.
Fixed acceleration bound $F(m)=am$ and common precision realize the positive
extensive case, whose value still comes from a and the record band. R13 next
examines the finite-horizon regime before the hidden pair can be prepared.

C080–C081: [complete proof and information classes](minimax-composition.md),
[B43 audit](../references/batches/B43.md). These products multiply coordinate
minimax risks and are not simultaneous error lower bounds on each motion.

## 18. Exact recovery before the preparation time

The complete noisy history has exact finite-horizon phase risks even before
R11's hidden pair can be fully prepared. Keep known initial data, arbitrary
measurable forces bounded by F, position errors bounded by epsilon, and no
speed ceiling. With $\tau=\sqrt{m\varepsilon/F}$ and $s=T/\tau$,

$$Q(T)=\varepsilon\min\{s^2/2,1\},\qquad
P(T)=\sqrt{mF\varepsilon}\,V(s),$$

$$V(s)=\begin{cases}
s,&0\le s\le\sqrt2,\\
\sqrt{2s^2+4}-s,&\sqrt2\le s\le4,\\
2,&s\ge4.
\end{cases}$$

In scaled coordinates, the hidden path obeys $x(0)=x'(0)=0$,
$|x''|\le1$, $|x|\le1$. Its terminal velocity v is bounded by s.
Putting negative acceleration first minimizes terminal position at fixed v,
giving $x(s)\ge(v^2+2sv-s^2)/4$ and the middle upper bound. Integrating
$x'(t)\ge v-(s-t)$ over the final v time units gives $v^2/2\le2$.
The lower envelope of these three bounds is V. Constant positive acceleration
attains the first branch. Negative acceleration for
$h=s-\sqrt{s^2/2+1}$ followed by positive acceleration attains the middle;
its minimum position is $-h^2\ge-1$ and endpoint position is 1.
The prepared R11 pair attains the final branch. Each momentum extremizer also
maximizes endpoint position, so a blind interval b has exact risks

$$P_b=P(T)+Fb,\qquad Q_b=Q(T)+bP(T)/m+Fb^2/(2m).$$

Product constituent records still give $Q_A=\sum_i m_iQ_i/M$ and
$P_A=\sum_iP_i$. Retaining only their centre record gives the single-body
formula with $(M,F_\Sigma,E)$ at every horizon. Position information is
strictly lost exactly when some $F_iT^2/2<m_i\varepsilon_i$ and another
$F_jT^2/2>m_j\varepsilon_j$. Thus the transient can lose both phase
coordinates. For equal m and epsilon, forces F and 16F at
$T=\sqrt{m\varepsilon/F}$ give

$$Q_A=3\varepsilon/4,\quad Q_B=\varepsilon,\quad
P_A=9\sqrt{mF\varepsilon},\quad
P_B=(\sqrt{714}-17)\sqrt{mF\varepsilon}>P_A.$$

Identical copies retain $H_A=H_B=nH_1(T)$. At fixed precision the early
product is $F^2T^3/(2m)$; at fixed positive T it closes as precision improves.
R14 tests a shared apparatus error budget that prevents freely aligned
full-width errors. C082–C083: [complete written proof](finite-horizon-minimax.md)
and [B44 bounded audit](../references/batches/B44.md).

## 19. Shared error geometry controls composition

For n identical constituents with known initial phases, force ceiling F and
complete position records, impose one pointwise apparatus budget
$\|e(t)\|_r\le\varepsilon$, $1\le r\le\infty$. Set
$E_n=\varepsilon n^{-1/r}$, with $1/\infty=0$. Averaging has error at
most E_n by the norm inequality, and force at most nF at mass nm. Equal
errors and forces lift every such scalar experiment. Equal displacement
paths also lift its entire central compatible fibre. Thus retaining all
records or only their average gives identical scalar centre minimax risks:

$$Q_n=E_n\min(s_n^2/2,1),\qquad
P_n=n\sqrt{mFE_n}\,V(s_n),\qquad
s_n=T\sqrt{F/(mE_n)},$$

where V is section 18's function. For $s_n\ge4$,

$$\boxed{H_n^{\rm sat}=n^{1-3/(2r)}H_1^{\rm sat},\qquad
H_1^{\rm sat}=2\sqrt{mF}\,\varepsilon^{3/2}.}$$

A quadratic budget gives $n^{1/4}$; $r=3/2$ gives copy-count invariance.
R15 tests independent block budgets against this shared preparation.
C084–C085: [proof and scope](shared-record-budget.md),
[B45 audit](../references/batches/B45.md).

## 20. Independent block apparatuses restore extensive scaling

For k independently budgeted blocks of a identical constituents, with the
same pointwise $\ell^r$ error allowance epsilon per block, put
$E=\varepsilon a^{-1/r}$ and $N=ka$. Product compatible fibres add their
scalar target radii. Thus for all constituent records, all block-average
records, or only the centre record, the risks equal the one-body risks at
mass Nm, force bound NF and precision E. At
$T\ge4\sqrt{mE/F}$,

$$H_{\rm blocks}=k a^{1-3/(2r)}H_1,\qquad
H_{\rm global}=(ka)^{1-3/(2r)}H_1.$$

Here the second apparatus has only one global allowance epsilon. At $r=3/2$
the products are $kH_1$ and $H_1$ respectively. Matching global-budget centre
risks with separate blocks requires reducing each allowance to
$\varepsilon k^{-1/r}$. For finite r and $k>1$ this still gives different
error sets: a Cartesian product of block balls is strictly contained in the
matching global ball. Equal centre risks do not establish equal preparations.

For unequal effective block precisions $E_j$, retained block records instead
give

$$Q=\sum_j(n_j/N)q(T,E_j),\qquad P=\sum_j n_jp(T,E_j),$$

using section 18's one-constituent functions. Keeping only the centre record gives
the risks at precision $\bar E=\sum_j(n_j/N)E_j$. In saturation, strict
concavity of the square root makes momentum risk larger unless all $E_j$ agree.
R16 tests contraction of finite mechanical record errors at fixed apparatus
parameters. C086–C087: [proof](block-apparatus-composition.md) and
[B46 audit](../references/batches/B46.md).

## 21. Exact calibration at fixed nonzero coupling

Keep section 11's apparatus and one sufficiently small positive coupling
$\lambda$ fixed. Its nominal four-momentum map has the uniform expansion

$$F_\lambda(z)=-\lambda\mathcal A z+\mathcal R_\lambda(z),
\qquad\|\mathcal R_\lambda\|_{C^1}\le C\lambda^3.$$

Differentiating the smooth flow preserves the probe $O(\lambda)$ and
receiver/clock reaction $O(\lambda^2)$ bounds. The integrated record
remainder is therefore cubic in coupling also in first derivative. On a convex
neighbourhood of the energy shell, the matrix margin alpha>0 gives

$$\|F_\lambda(z)-F_\lambda(w)\|\ge
\tfrac12\lambda\alpha\|z-w\|.$$

Let incoming apparatus uncertainty have width b, and the four final-record
errors have width rho, in fixed component units. The exact nonlinear
minimum-residual calibration on the compact receiver shell then satisfies

$$\|\widehat z-z\|\le\frac4{\lambda\alpha}(C_\lambda b+\rho).$$

Thus reconstruction error vanishes as b and rho shrink with coupling, masses
and duration fixed. Momentum disturbance remains bounded by
$CP_*(\lambda b+\lambda^2)$, so its product with position-reconstruction
error also vanishes. Exact calibration and improving record access are supplied
resources. R17 holds incoming width positive to test whether unknown probe
momenta can hide distinct receiver states. C088–C089:
[proof and domain](fixed-coupling-calibration.md), [B47 audit](../references/batches/B47.md).

## 22. Positive preparation width leaves exact record ambiguity

Keep the four final momentum records as the only data, with a fixed positive
incoming apparatus box of half-width $b$ and sufficiently small coupling
$\lambda>0$. In fixed component units the derivative of final records with
respect to incoming probe momenta $u$ is uniformly within $1/2$ of $I$. The nominal
receiver derivative is bounded by $L\lambda$. Thus the map

$$T_w(u)=u-G_\lambda(w,u)+F_\lambda(z_*)$$

contracts the ball $\|u\|\le b/2$ into itself whenever
$\|w-z_*\|\le b/(4L\lambda)$. Its fixed point supplies exact nonlinear record
compensation, with an interior preparation margin.

At the shell point $z_*=(0,0,\sqrt{2E/d},0)$, completing the square gives the
local chart

$$y=\frac gd x+\sqrt{\frac{2E-(a-g^2/d)x^2-P^2/\mu}{d}},\qquad Q=0.$$

Let $r_0$ be a fixed dimensionless chart-square radius and $C_0$ its Lipschitz
bound in fixed length/momentum units $L_*,P_*$. With

$$r=\min(r_0,b/(4LC_0\lambda)),$$

the entire square $|x|\le L_*r$, $|P|\le P_*r$ has one common exact record.
Every initial-state estimator therefore has worst-case errors

$$\epsilon_x\ge L_*r,\qquad\epsilon_P\ge P_*r,\qquad
\mathcal H_{\rm rec}\ge L_*P_*r^2>0.$$

The compatible fibre's canonical $(x,P)$ projection has area at least
$4L_*P_*r^2$. This reconstruction bound depends on the positive product
preparation support and four-record access; its small-b rate matches section
21's upper bound. R18 reveals incoming momenta and tests whether unknown
probe positions still hide receiver changes. C090–C091:
[proof and domain](fixed-preparation-ambiguity.md), [B48 audit](../references/batches/B48.md).

## 23. Position uncertainty survives incoming momentum calibration

Revealing the four incoming probe momenta still leaves a common-record shell
patch for one fixed admissible pulse design. On the zero-incoming-momentum,
nominal-clock slice, the derivative with respect to initial probe positions is

$$D_qG_\lambda=\lambda^2 B(z)+O(\lambda^3).$$

Both receiver and clock reaction contribute to $B$. Ordered disjoint pulses
make it lower triangular. For pulses
$f_j(s_0+vt)=\phi((t-t_j)/\delta)$ with $x_j=x^0(t_j)\ne0$, its diagonal obeys

$$B_{jj}=-\frac{K^2x_j^2\delta}{M_cv^2}\int\phi^2+O(\delta^2).$$

Choose independent signal times avoiding the isolated zeros of $x^0$ and
then a sufficiently small positive duration $\delta$, held fixed thereafter.
Every diagonal is nonzero. The clock contribution, of order $\delta$, dominates
the receiver's order-$\delta^3$ term.

In fixed component units, multiplication by $(\lambda^2 B(z_*))^{-1}$ gives
a contraction on the position ball $b/2$ whenever
$\|w-z_*\|\le\lambda b/(4C)$. Its fixed point preserves all eight initial
and final momentum records exactly. Using section 22's shell chart gives

$$r=\min\left(r_0,\frac{\lambda b}{4CC_0}\right),\qquad
\epsilon_x\epsilon_P\ge L_*P_*r^2,\qquad
\operatorname{area}_{x,P}\ge4L_*P_*r^2.$$

These bounds quantify the unknown position support; at fixed width their
displayed lower bound closes with coupling. R19 adds final pointer positions
and known initial clock position and momentum to test uniform joint recovery.
C092–C093: [proof and domain](position-preparation-ambiguity.md),
[B49 audit](../references/batches/B49.md).

## 24. Full pointer records remove the fixed-position ambiguity

With initial clock data $c$ and probe momenta $u$ revealed, all eight final pointer
coordinates determine both receiver state $z$ and unknown incoming positions $q$.
The initial positions occupy a fixed positive box. Clock data may range over a
fixed sufficiently small known-data box, on which the free signal matrices $A_c$
have a uniform inverse margin $\alpha>0$. Free drift is $d_j(u)=T u_j/M_j$.

In fixed component units the scaled exact record map satisfies

$$F(z,q)=\left(\frac{\pi(T)-u}{\lambda},q(T)-d(u)\right)
 =(-A_c z,q)+R(z,q),\qquad ||R||_{C^1}\le C\lambda.$$

The receiver and clock reactions are uniformly order $\lambda$ on this fixed
preparation domain. Integrating the pointer equations and their variations
gives the displayed estimate on a convex neighbourhood of the energy ball
times the position box. For $\beta=\min(\alpha,1)$ and $C\lambda\le\beta/2$, segment
integration yields the global bound

$$||F(v)-F(w)||\ge\tfrac12\beta||v-w||.$$

Thus exact joint records remove section 23's ambiguity. If final momentum and
position errors are at most $\rho_\pi$ and $\rho_q$ in fixed units, a minimum-residual
fit on the shell times the box gives

$$\epsilon_x\epsilon_P\le\frac{16L_*P_*}{\beta^2}
 \max(\rho_\pi/\lambda,\rho_q)^2\longrightarrow0$$

as both record errors vanish at fixed positive coupling. Preparation widths,
masses and observation time stay fixed. Exact incoming clock/momentum data
and improving simultaneous final position/momentum access are supplied
resources. This is delayed reconstruction; disturbance need only stay bounded.
R20 hides the initial clock data and tests an exact common-record shell family.
C094–C095: [proof and domain](full-pointer-recovery.md),
[B50 audit](../references/batches/B50.md).

## 25. A hidden clock leaves an exact receiver phase interval

With clock offset and speed hidden, eight exact final pointer records admit
an energy-preserving receiver phase family for a fixed admissible pulse design.
Incoming probe momenta remain known at zero. Write clock data as $c=(s,v)$,
receiver flow as $\exp(Mt)$, and $H_s(z)=z^TGz/2$. Section 24's scaled map
extends smoothly to zero coupling. The implicit-function theorem solves

$$F_{\lambda,c}(z_\lambda(c),q_\lambda(c))=Y_\lambda,\qquad
z_0(c)=A_c^{-1}A_{c_0}z_*.$$

Interior supports give $\partial_s A=-AM/v$. Consequently the offset
derivative is $Mz_*/v_0$ and preserves receiver energy at zero coupling.
For four pulses at times of order a small design duration $\varepsilon$,
the independent observation rows $e_xM^n$, $n=0,1,2,3$, give

$$\det A_{s_0,v}=D(r\varepsilon)^{10}(1+O(\varepsilon)),
\quad r=v_0/v,\quad D\ne0,$$
$$\operatorname{tr}(-A^{-1}\partial_v A)=10/v_0+O(\varepsilon)>0.$$

The exponent counts four integration factors and derivative orders
$0+1+2+3$. Fix this design. Positive trace supplies a shell point with
$\partial_v H_s(z_0(c))>0$ and both canonical phase derivatives nonzero.
A second implicit equation therefore solves $H_s(z_\lambda(c))=E$ for
$v=v_\lambda(s)$, with

$$v'_\lambda(s_0)=O(\lambda),\qquad
z'_\lambda(s_0)=Mz_*/v_0+O(\lambda).$$

On a small fixed clock-offset interval of half-width $\sigma$, both canonical
derivatives retain magnitudes at least $k_x,k_P>0$. Clock-speed and incoming
position adjustments are $O(\lambda\sigma)$, preserving preparation margins.
Common-record endpoints then imply

$$\epsilon_x\epsilon_P\ge k_xk_P\sigma^2>0.$$

This action-valued product is a clock-preparation cost. The family is a curve,
so the result asserts coordinate risks rather than positive canonical area.
R21 reveals offset alone and tests local recovery through energy transversality.
C096–C097: [proof and domain](hidden-clock-ambiguity.md),
[B51 audit](../references/batches/B51.md).

## 26. Clock position and exact energy permit stable local recovery

Revealing initial clock position alone removes section 25's phase ambiguity
on a fixed local receiver preparation patch. Initial clock speed remains
unknown, incoming probe momenta are known at zero, and the initial receiver
energy is supplied exactly. Use the same fixed transverse pulse design and
shell point $z_*$ as in section 25. In fixed component units, append energy to
the eight scaled records:

$$\mathcal G_\lambda(z,q,v)
 =\big(F_\lambda(z,q,v),H_s(z)/E_*\big),\qquad
 F_0(z,q,v)=(-A_{s_0,v}z,q).$$

The derivative kernel at zero coupling obeys

$$dq=0,\qquad dz=Bz_*\,dv,\qquad
 B=-A_0^{-1}(\partial_v A)_0,\qquad
 (z_*^T GBz_*)\,dv=0.$$

The positive transverse factor established in section 25 makes the reference
derivative $J$ invertible. Put $\gamma=1/\|J^{-1}\|$. Continuity and uniform $C^1$
convergence give one fixed convex neighbourhood $U$ and $\lambda_0>0$ with

$$\sup_U||D\mathcal G_\lambda-J||\le\gamma/2,\qquad
||\mathcal G_\lambda(w)-\mathcal G_\lambda(w')||
 \ge\tfrac12\gamma||w-w'||.$$

The second inequality follows by integrating along the segment inside $U$.
Choose a compact shell patch times independent positive probe-position and
clock-speed boxes contained in $U$. On this physical set the energy outputs
agree, so the eight records alone determine all unknowns. For final momentum
and position error bounds $\rho_\pi,\rho_q$, a minimum-residual fit gives

$$||\widehat w-w||\le\frac4\gamma
 \max(\rho_\pi/\lambda,\rho_q),\qquad
\epsilon_x\epsilon_P\le\frac{16L_*P_*}{\gamma^2}
 \max(\rho_\pi/\lambda,\rho_q)^2.$$

The canonical product has action units and closes with record error at fixed
positive coupling and fixed local preparation. Initial clock momentum is
recovered as well. The zero-coupling extension is a proof device; physical
recovery requires a nonzero signal. Exact energy and knowledge of the local
patch are supplied information. R22 tests distinct-speed common records
across the entire shell. C098–C099:
[proof and domain](clock-position-local-recovery.md),
[B52 audit](../references/batches/B52.md).

## 27. Full-shell recovery fails at two distinct clock speeds

The local preparation patch in section 26 carries genuine information.
With the full receiver energy shell admitted, a fixed early-pulse design
gives distinct-speed preparations with identical eight final pointer records.
Clock offset and receiver energy remain known.

Let $O$ have rows $e_xM^n$, $n=0,1,2,3$. Factoring the pulse moment matrix
before inversion gives, for a small fixed design duration $\varepsilon$,

$$B_\varepsilon=-A_{v_0}^{-1}\partial_v A_{v_0}
=\frac1{v_0}O^{-1}\operatorname{diag}(1,2,3,4)O+O(\varepsilon).$$

For $Q=0$, its limiting energy response is

$$v_0 z^TGB^{(0)}z=g(x-y)(9x-5y)+\frac{2P^2}{\mu}.$$

Take $x=L>0$, $P=p>0$ sufficiently small and vary $y$ from zero to $7L/5$,
normalizing the entire path onto $H_s=E$. The endpoint energy responses have
opposite signs and both canonical coordinates stay positive. Choose the
design first and then a small fixed speed separation $d_v>0$. Equality of
scaled zero-coupling records at $v_0$ and $v_1=v_0+d_v$ gives

$$z'=A_{v_1}^{-1}A_{v_0}z=z+d_v B_\varepsilon z+O(d_v^2).$$

The energy mismatch changes sign along the path, while both coordinate
separations are bounded below by positive multiples of $d_v$. Intermediate
value supplies an actual equal-energy pair.

At positive coupling solve the exact eight-record equation at the second
speed for receiver state and incoming positions. Its invertible leading
derivative gives uniform $O(\lambda)$ continuation along the compact path.
For sufficiently small coupling the endpoint signs, preparation margins and
canonical separations persist. Another intermediate-value argument gives
exact equal-energy, equal-record states, and consequently

$$\epsilon_x\epsilon_P\ge\frac{c_xc_Pd_v^2}{16}>0.$$

This action-valued risk depends on the allowed speed interval and full-shell
preparation. R23 adds the persistent final clock momentum to test global
recovery from physical clock information. C100–C101:
[proof and domain](global-clock-speed-ambiguity.md), [B53 audit](../references/batches/B53.md).

## 28. A final clock-momentum record restores global recovery

Add the persistent final clock momentum to the eight pointer records, with
initial clock position still known. The nine records determine receiver state,
incoming probe positions and initial clock speed on a whole bounded domain.
Exact receiver energy and the local-patch prior are unnecessary.

In fixed component units, including clock momentum unit $M_cV_*$, the map is

$$\mathcal F_\lambda(z,q,v)=
\left(\pi(T)/\lambda,q(T),p_s(T)/M_c\right)
=L(z,q,v)+R_\lambda,\qquad L=(-A_vz,q,v),\quad
\|R_\lambda\|_{C^1}\le C\lambda.$$

The last block includes the exact reaction

$$p_s(T)=M_cv-\lambda K\sum_j\int_0^T f'_j(s(t))x(t)q_j(t)\,dt.$$

Let $\alpha$ be a uniform lower bound for $A_v$, and
$D=\sup\|(\partial_v A_v)z\|$ on the fixed convex preparation domain.
The speed and position blocks bound their input differences directly;
the receiver block then yields

$$\|L(w)-L(w')\|\ge\beta\|w-w'\|,\qquad
\beta=\min(1,\alpha/(1+D)).$$

Subtracting the remainder's Lipschitz bound gives an exact inverse margin
$\beta/2$ whenever $C\lambda\le\beta/2$. This is a global estimate for a
nonlinear leading map, rather than a pointwise rank argument.
For final record errors $\rho_\pi,\rho_q,\rho_c$, a compact minimum-residual
fit gives

$$\epsilon_x\epsilon_P\le\frac{16L_*P_*}{\beta^2}
\max(\rho_\pi/\lambda,\rho_q,\rho_c)^2.$$

The action-valued error product closes with record precision at fixed coupling
and positive preparation widths. Clock back-reaction is jointly calibrated;
the final momentum is not substituted as an exact initial momentum. Joint
record access remains supplied. R24 adds final clock position and hides
initial offset. C102–C103: [proof and domain](final-clock-momentum-recovery.md),
[B54 audit](../references/batches/B54.md).

## 29. Full clock records replace its initial preparation data

Add final clock position at the known time $T$, and make its initial offset
unknown. With the initial probe momenta still known at zero, all ten final
apparatus coordinates recover receiver state, incoming probe positions and
both initial clock coordinates on a bounded domain.

Use clock units $S_*,V_*$ and $\theta=TV_*/S_*$. The leading dimensionless
map and exact remainder are

$$L(z,q,s,v)=(-A_{s,v}z,q,s+\theta v,v),\qquad
\mathcal F_\lambda=L+R_\lambda,\quad\|R_\lambda\|_{C^1}\le C\lambda.$$

The extra reaction term in physical clock position is exactly

$$s(T)-s-vT=-\frac{\lambda K}{M_c}\sum_j
\int_0^T(T-t)f'_j(s(t))x(t)q_j(t)\,dt.$$

Let $d$ be the leading output difference. Inverting the clock shear gives
$|\Delta v|\le d$ and $|\Delta s|\le(1+\theta)d$. With uniform signal
inverse margin $\alpha$ and bounds $D_s,D_v$ for its parameter derivatives
applied to receiver states, the receiver difference obeys

$$\alpha\|\Delta z\|\le[1+D_s(1+\theta)+D_v]d.$$

These bounds give a global leading inverse margin

$$\beta=\min\{(1+\theta)^{-1},
\alpha/[1+D_s(1+\theta)+D_v]\}>0.$$

The remainder reduces it by at most $C\lambda$, giving margin $\beta/2$
at small positive coupling. For final pointer and clock errors set
$\delta=\max(\rho_\pi/\lambda,\rho_q,\rho_s,\rho_c)$; compact fitting yields
$\epsilon_x\epsilon_P\le16L_*P_*\delta^2/\beta^2$.

Sections 24–29 isolate the information trade: final clock phase replaces
initial clock calibration, while exact incoming probe momenta remain shared
preparation data. The [comparison table](full-clock-phase-recovery.md)
collects all six cases. R25 makes the entire incoming apparatus state unknown
and tests compensation even with full final records. C104–C105:
[proof and domain](full-clock-phase-recovery.md), [B55 audit](../references/batches/B55.md).

## 30. Unknown full apparatus preparation hides the receiver shell

With all incoming apparatus coordinates unknown in a fixed positive box,
all ten exact final coordinates admit receiver-shell ambiguity. At sufficiently
weak coupling, the worst-case coordinate risks equal their no-record values.

Let $\eta$ denote the ten initial apparatus coordinates in fixed component
units, centred at $\eta_*$. The unscaled final-record map $G_\lambda$ has free
limit $S\eta$, where $S$ sends each apparatus pair $(q,p)$ of mass $M$ to
$(q+Tp/M,p)$. Thus $F_\lambda=S^{-1}G_\lambda$ satisfies uniformly on the
convex receiver energy ball and a small fixed apparatus box

$$\|D_\eta F_\lambda-I\|\le1/2,\qquad
\|D_zF_\lambda\|\le L\lambda.$$

For a nominal shell point $z_*$, the map
$\eta\mapsto\eta-F_\lambda(w,\eta)+F_\lambda(z_*,\eta_*)$
contracts the radius-$b/2$ preparation ball whenever
$\|w-z_*\|\le b/(4L\lambda)$. Its fixed point gives

$$G_\lambda(w,\eta(w))=G_\lambda(z_*,\eta_*),\qquad
\|\eta(w)-\eta_*\|\le2L\lambda\|w-z_*\|\le b/2.$$

At fixed $b>0$, take $\lambda\le\min(\lambda_0,b/(4LD))$, where
$D=\max_{H_s(w)=E}\|w-z_*\|$. One full record then hides the whole shell.
Writing $k_x=a-g^2/d>0$, its canonical projection is the ellipse
$k_xx^2+P^2/\mu\le2E$. Common-record endpoints force both semiaxis errors;
the constant estimator $(0,0)$ attains them over the entire admitted class:

$$R_x=\sqrt{2E/k_x},\qquad R_P=\sqrt{2\mu E},\qquad
\inf_{(\widehat x,\widehat P)}\epsilon_x\epsilon_P
=2E\sqrt{\mu/k_x}.$$

The projected compatible area is $\pi$ times this action-valued product.
The fixed-width weak-coupling condition supplies the admissibility margin;
receiver energy and stiffness supply the saturated value. Exact initial
apparatus energy is not supplied. R26 imposes that extra scalar constraint on
$\eta(w)$. C106–C107: [proof and limits](full-apparatus-preparation-ambiguity.md),
[B56 audit](../references/batches/B56.md).

## 31. Exact initial energies leave an antipodal ambiguity

Supply the initial apparatus energy $H_0=M_cv_0^2/2$ as well as receiver
energy $E$. An exact common-record receiver pair still exists. Choose a
receiver shell point $z_*$ and prescribe terminal zero probe phase, clock
position $s_0+v_0T$, and

$$z(T)=r\Phi_Tz_*,\qquad
p_s(T)=\sqrt{2M_c[H_0+E(1-r^2)]}.$$

Terminal total energy is exactly $E+H_0$. Backward Hamiltonian flow gives
initial receiver state $Z_\lambda(r)$; at zero coupling its energy is $r^2E$.
The derivative $2E$ at $r=1$ supplies an implicit adjustment with
$H_s(Z_\lambda(r_\lambda))=E$. Endpoint pulses vanish, so conservation gives
initial apparatus energy $H_0$ exactly. Terminal zero probes imply

$$r_\lambda=1+O(\lambda^2),\qquad Z_\lambda=z_*+O(\lambda^2),$$

while the full incoming apparatus displacement is $O(\lambda)$ and fits
inside half the fixed preparation box for sufficiently small coupling.

The simultaneous sign involution
$(z,q,\pi,s,p_s)\mapsto(-z,-q,-\pi,s,p_s)$ preserves the equations in the
linear cutoff regions. It leaves the clock and both quadratic energies
unchanged. Because terminal probes vanish, both preparations have identical
complete final apparatus records and exactly opposite initial receiver states.

Put $k_x=a-g^2/d$ and choose
$z_*=(\sqrt{E/k_x},\sqrt{\mu E},(g/d)\sqrt{E/k_x},0)$.
Common-record endpoints then give

$$\epsilon_x\epsilon_P\ge |(Z_\lambda)_x(Z_\lambda)_P|
\longrightarrow E\sqrt{\mu/k_x}>0.$$

The limit concerns the displayed lower bound, with action units. It is
energy-dependent and supplies neither exact minimax saturation nor positive
area. R27 tests a known nonzero initial probe displacement; breaking this
involution must be distinguished from proving global recovery. C108–C109:
[proof and domain](energy-constrained-apparatus-ambiguity.md),
[B57 audit](../references/batches/B57.md).

## 32. One calibrated displacement leaves full receiver ambiguity

Fix a known nonzero incoming probe displacement $q_1=c$, with
$|c|/L_1<b/4$, while retaining exact initial energies $E,H_0$ and all ten final
apparatus coordinates. Full receiver recovery still fails for sufficiently
small positive coupling. The new proof uses a preparation chart rather than
the sign involution, which would send $c$ to $-c$.

Before the pulses, solve the apparatus energy for positive clock momentum,

$$p_s=\sqrt{2M_c\left(H_0-\sum_{j=1}^4\frac{\pi_j^2}{2M_j}\right)}.$$

Eight independent apparatus coordinates remain: $q_2,q_3,q_4$, the four probe
momenta and $s$. On the receiver shell use $x,P,Q$ near zero and solve

$$y=\frac gd x+
\sqrt{\frac{2E-k_xx^2-P^2/\mu-Q^2/\nu}{d}},\qquad k_x=a-g^2/d>0.$$

In fixed component units this gives an injective eleven-coordinate chart
$\Psi$ containing a closed parameter ball of radius $r>0$, independent of
coupling, with strict radicands and half-box preparation margins. Its boundary
is $S^{10}$. The continuous map taking each chart point to its ten final
apparatus coordinates has an equal-image antipodal pair by Borsuk–Ulam.
Both preparations have exactly the supplied energies and calibration.

For the inverse-shear record $F_\lambda$, the uniform ambient bounds give

$$\|D_\eta F_\lambda-I\|\le\tfrac12,\qquad
\|D_zF_\lambda\|\le L\lambda.$$

Hence equal records imply
$\|\eta_+-\eta_-\|_2\le2L\lambda\|z_+-z_-\|_2$.
The eleven chart coordinates are a projection of the full initial state;
the antipodal parameter distance is $2r$. Therefore the full receiver-state
minimax risk in these fixed Euclidean component units obeys

$$R_z\ge\frac12\|z_+-z_-\|_2
\ge\frac{r}{\sqrt{1+4L^2\lambda^2}}>0.$$

This is a dimensionless full-state error bound. The difference may lie in
internal coordinates; R28 tests separation in both $x$ and $P$ and a possible
canonical error product. C110–C111:
[proof and margins](calibrated-displacement-ambiguity.md),
[B58 theorem audit](../references/batches/B58.md).

## 33. Calibrated records still hide both canonical coordinates

A fixed smooth pulse design preserves a positive canonical risk product under
R27's nonzero calibration $q_1=c$, both exact initial energies and all ten final
apparatus coordinates. Let $\eta_c$ have only $q_1=c$ nonzero among probe
coordinates. The exact record compensator about a receiver shell point
$\bar z$ satisfies

$$G_\lambda(w,\eta_\lambda(w))=G_\lambda(\bar z,\eta_c),\qquad
\|\eta_\lambda(w)-\eta_c\|\le2L\lambda\|w-\bar z\|.$$

Put $h(t)=f_1(s_0+v_0t)$. Dividing the calibration and initial apparatus-energy
residuals by $\lambda$ gives smooth zero-coupling limits
$-(K/M_1)A(w-\bar z)$ and $-Kc B(w-\bar z)$, where

$$A(w)=\int_0^T th(t)x_w(t)\,dt,\qquad
B(w)=\int_0^T h(t)\dot x_w(t)\,dt.$$

A first pulse near a small fixed $\tau$ makes the normalized rows approximate
$x(\tau)$ and $P(\tau)/\mu$. Their kernel contains a direction close to
$\Phi_{-\tau}(0,0,Y,0)$, whose initial canonical components are
$gY\tau^2/(2\mu)+O(\tau^4)$ and $-gY\tau+O(\tau^3)$. Both are nonzero.
A positive fixed pulse width preserves this property; three further disjoint
pulses retain R06's four-record signal rank.

In the two-dimensional kernel plane choose $\bar z$ on $H_s=E$ orthogonal
to that direction $v$ in the energy inner product. Then $dH_s,A,B$ are
independent. The implicit-function theorem applied to the divided residuals,
receiver energy and a curve parameter gives exact common-record states
$w_\lambda(t)$. A fixed rectangle $|t|\le\delta$, $0<\lambda\le\lambda_1$
retains preparation margins and canonical derivatives of magnitude at least
$|v_x|/2$ and $|v_P|/2$. Its endpoints imply

$$\epsilon_x\epsilon_P\ge\frac{\delta^2|v_xv_P|}{4}>0.$$

The action-valued bound is uniform on this coupling interval and depends on
preparation, energy and pulse design. C112–C113: [proof and limits](calibrated-canonical-ambiguity.md),
[B59 audit](../references/batches/B59.md). R29 adds a second calibrated
displacement and tests local versus global recovery.

## 34. A second calibration leaves two locally recoverable branches

Add $q_2=0$ while retaining $q_1=c\ne0$, both exact initial energies and
the ten final apparatus records. The new divided compensator residual has
limit $-(K/M_2)A_2(w-z_{\rm bar})$, where $A_2=\int t f_2 x_w$.
The three linear rows are now $A_1,B_1,A_2$.

Choose narrow positive pulses near $\tau$ and $2\tau$. Their limiting rows
are $x(\tau),\dot x(\tau),x(2\tau)$. On their kernel the state at $\tau$
has form $(0,0,Y,Q)$, with $Y=-Q\tau/(3\nu)+O(\tau^3)$, and its initial
canonical components obey

$$v_x=-\frac{gQ}{3\mu\nu}\tau^3+O(\tau^5),\qquad
v_P=\frac{5gQ}{6\nu}\tau^2+O(\tau^4).$$

Fix sufficiently small times and positive widths, preserving rank three
and these nonzero components. The resulting kernel line meets the receiver
energy shell at $\pm z_{\rm bar}$. At both points the derivative rows
$dH_s,A_1,B_1,A_2$ are independent. The exact scaled residual equations
therefore have two continued roots

$$w_+(\lambda)=z_{\rm bar},\qquad
w_-(\lambda)=-z_{\rm bar}+O(\lambda).$$

The compensating apparatus preparations preserve both calibrations, both
energies, one exact complete record and the positive box margins. At each
fixed positive coupling, eliminating the apparatus-record derivative proves
a local inverse of the augmented map around each root. It does not choose
between them globally. Common-record endpoint inequalities give

$$\epsilon_x\epsilon_P\ge
\tfrac14|(w_+-w_-)_x(w_+-w_-)_P|
\longrightarrow |(z_{\rm bar})_x(z_{\rm bar})_P|>0.$$

This is a preparation-dependent action-risk lower bound, not an area or
exact minimax value. R30 adds $q_3=0$ and tests a uniform global inverse,
including its record conditioning. C114–C115:
[proof and domain](two-calibration-branches.md), [B60 audit](../references/batches/B60.md).

## 35. Three calibrations restore global recovery on a fixed box

Calibrate $q_1=c\ne0$, $q_2=q_3=0$ and supply exact initial apparatus
energy $H_0$, together with all ten final apparatus coordinates at known $T$.
On a bounded convex receiver energy ball, a sufficiently small fixed box
about the calibrated apparatus centre admits a uniform global inverse.
The exact receiver energy is unnecessary. The box may be smaller than R29's
original preparation box; its radius stays fixed in the precision limit.

Choose a third positive smooth pulse detecting the kernel of $A_1,B_1,A_2$.
Analytic observability guarantees such a pulse, so the four rows

$$L=(-K A_1/M_1,-K A_2/M_2,-K A_3/M_3,-Kc B_1)^T$$

are independent. Write $a=S^{-1}Y$ for the inverse free shear of a final
record, and let $\eta_\lambda(w,a)$ be the uniform apparatus inverse chart.
For $C=(q_1,q_2,q_3,H_{\rm app})$ the map

$$D_\lambda(w,a)=
\frac{C(\eta_\lambda(w,a))-C(a)}{\lambda}$$

extends jointly smoothly to zero coupling. Its receiver derivative at the
nominal record is $L$ throughout the receiver ball. Shrinking the apparatus
neighbourhood and coupling gives a uniform margin
$\|L^{-1}(D_wD_\lambda-L)\|\le1/2$.
Segment integration over the convex receiver domain then proves global
injectivity for the exact constrained class.

For two admitted records the same estimate gives
$\|w-w'\|\le K_z\|Y-Y'\|/\lambda$. Minimum-residual fitting of a
record with error at most $\delta$ therefore yields, in physical units,

$$\epsilon_x\epsilon_P\le
4L_*P_*K_z^2(\delta/\lambda)^2.$$

This action-unit product closes at fixed positive coupling as record error
vanishes, with preparation width fixed. Joint limits require
$\delta/\lambda\to0$ for this bound. C116–C117:
[proof and domain](three-calibration-global-recovery.md),
[B61 audit](../references/batches/B61.md). R31 tests errors in the supplied
calibrations and apparatus energy; the current theorem assumes both exact.
