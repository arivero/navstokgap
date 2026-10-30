# Classical apparatus: construction, complete records and stable recovery

A finite autonomous Hamiltonian apparatus can reconstruct a known spring
receiver after a fixed latency with arbitrarily small error and disturbance.
At fixed nonzero coupling, exact nonlinear calibration instead permits
vanishing reconstruction error with bounded disturbance. Complete final clock
records replace initial clock calibration, provided incoming probe momenta
are known. These are different limits of one apparatus; none derives a
positive universal action. The complementary preparation obstructions and
calibration thresholds are proved in
[the calibration treatment](calibration-tolerance-recovery.md).

This treatment consolidates C066–C069, C088–C089, C094–C105 and the
construction lemmas used by C090–C123. Historical coordinator/model checks
were internal written checks, not external peer review; novelty is unassessed.
Source reading levels and the original internal checks remain in the linked
B35, B37, B47 and B50–B55 records. All estimates below are written derivations.

## Receiver and one autonomous apparatus

The reduced three-body receiver of
[the receiver treatment](conservative-harmonic-receiver.md#9-a-third-body-exact-memory-and-recoverable-history)
has state $z=(x,P,y,Q)$ and

$$H_s=\frac{P^2}{2\mu}+\frac{Q^2}{2\nu}
 +\frac a2x^2-gxy+\frac d2y^2,\qquad
(\mu,\nu,a,g,d)=(3m/2,m/2,9k/4,3k/4,5k/4).$$

Here $m,k>0$, $ad-g^2>0$, and $P$ is canonical; physical tagged momentum
is $2P/3$. Write $\Phi_t=e^{Mt}$ for its free flow and $G$ for its positive
energy matrix, $H_s=z^TGz/2$. Fix $E,T>0$ and a compact convex receiver
neighbourhood $Z$ containing $\{H_s\le E\}$, with an open enlargement for
derivatives. Apparatus preparation and all norms use fixed positive component
length/momentum units, including receiver units $L_*,P_*$. Constants may
depend on these units, the design and $T$; they are not uniform as $T\to0$.

Add a clock $(s,p_s)$ of mass $M_c>0$ and four probes $(q_j,\pi_j)$ of
masses $M_j>0$. With fixed stiffness $K>0$ and dimensionless coupling
$0<\lambda\le\lambda_0$, take

$$H_\lambda=H_s+\frac{p_s^2}{2M_c}+\sum_{j=1}^4\frac{\pi_j^2}{2M_j}
 +\lambda K\sum_{j=1}^4 f_j(s)X(x)R(q_j).$$

$X,R$ are bounded smooth coordinate cutoffs, equal to their arguments on
fixed trajectory neighbourhoods. Smooth nonnegative compactly supported
$f_j$ have disjoint supports strictly inside the nominal clock path
$s_0+v_0t$, $0<t<T$, $v_0>0$, with fixed endpoint margins. All five masses,
pulse shapes, widths, derivatives and $T$ are fixed before any coupling or
precision limit. Kinetic energy is positive; a fixed additive constant makes
the bounded interaction plus Hamiltonian nonnegative. The finite-dimensional
potential assumes neither spatial locality nor finite signal speed.

Energy conservation bounds receiver coordinates and momenta on the admitted
energy class. Bounded cutoffs bound interaction forces globally. Together
with compact initial apparatus boxes these give uniform force and speed
ceilings over the fixed horizon; harmonic forces have no asserted global
ceiling outside that energy class. Reducing $\lambda_0$ after design meets
any positive apparatus-force ceiling and preserves cutoff margins, pulse
traversal and positive clock momentum. Persistent momenta are stored after
the clock exits all supports. Position records are at the known time $T$;
unlimited bounded storage space is not asserted.

## Four signals and the common smooth-flow estimates

The free output's first four derivative rows are

$$x=x_0,\quad \dot x=P_0/\mu,\quad
\ddot x=(-ax_0+gy_0)/\mu,\quad
x^{(3)}=-aP_0/\mu^2+gQ_0/(\mu\nu).$$

They form an invertible triangular observation matrix, with diagonal
$1,1/\mu,g/\mu,g/(\mu\nu)$. Analyticity implies that the evaluation rows
$e_x\Phi_t$ span four dimensions on any open time interval. Otherwise an
annihilated vector would have identically zero output and all four initial
coordinates zero. Select four independent evaluation times and then
sufficiently narrow, positive, fixed pulse widths. Row-normalized pulse
integrals approach these evaluation rows, so

$$A_{c,j\cdot}=K\int_0^T f_j(s+vt)e_x\Phi_t\,dt,\qquad c=(s,v),$$

are invertible. In a small fixed clock rectangle a uniform inverse margin
$\|A_ch\|\ge\alpha\|h\|$, $\alpha>0$, follows by continuity.
$A_cz$ has momentum units before component conversion.

In the linear cutoff regions the exact equations and integrals include

$$\dot\pi_j=-\lambda Kf_j(s)x,\quad
\dot P=-ax+gy-\lambda K\sum_jf_j(s)q_j,\quad
\dot p_s=-\lambda K\sum_jf'_j(s)xq_j,$$

$$\pi_j(T)-u_j=-\lambda K\int_0^T f_j(s(t))x(t)dt,$$
$$q_j(T)-q_j-Tu_j/M_j
=-\frac{\lambda K}{M_j}\int_0^T(T-t)f_j(s(t))x(t)dt,$$
$$p_s(T)-M_cv=-\lambda K\sum_j\int_0^T f'_j(s(t))x(t)q_j(t)dt,$$
$$s(T)-s-vT=-\frac{\lambda K}{M_c}\sum_j
 \int_0^T(T-t)f'_j(s(t))x(t)q_j(t)dt.$$

Primes on pulses mean derivatives with respect to clock position. On a
fixed compact preparation domain, variation of constants and the smooth
finite-time variational equations bound coupled minus free trajectories by
$O(\lambda)$ in $C^1$ in every initial variable. The same is true of the
integrands and their initial derivatives. Dividing the momentum integral by
$\lambda$ gives a smooth extension at zero coupling. Thus every scaled map
below has a uniform $O_{C^1}(\lambda)$ remainder on a convex enlarged domain.
Clock reaction is included, rather than replaced by an external clock.
Smoothness also holds for a small signed coupling interval used only for
Taylor proofs; physical coupling is positive.

Two reusable estimates organize all the recovery statements. If
$F=L+R$ on a convex domain, $L$ has a global inverse margin $\beta>0$,
and $\|DR\|\le\beta/2$, segment integration gives

$$\|F(w)-F(w')\|\ge\tfrac\beta2\|w-w'\|.$$

For a compact physical subset, a minimum-residual fit to data with error
$\delta$ exists. Its exact output and the true output differ by at most
$2\delta$, hence

$$\|\widehat w-w\|\le4\delta/\beta,\qquad
\epsilon_x\epsilon_P\le16L_*P_*\delta^2/\beta^2.$$

These are sufficient stability bounds, not exact positive-error minimax
constants. Segments need only stay in the enlarged convex domain, not on an
energy shell. A pointwise rank calculation alone does not give this result.

## Quiet preparation and fixed-coupling calibration

First prepare all ten apparatus coordinates in a full rectangular box of
half-width $b>0$ about zero probe phase and $(s_0,M_cv_0)$. Each box has
positive phase volume. Probe force integration gives $q,\pi=O(b+\lambda)$;
receiver forcing then gives

$$z(t)-\Phi_tz_0=O(\lambda b+\lambda^2),\qquad
(s(t),p_s(t))-(s_0+v_0t,M_cv_0)=O(b+\lambda^2).$$

Finite-time continuation justifies the linear cutoff equations uniformly.
Inserting these estimates in the momentum integrals gives

$$\boldsymbol\pi(T)=\boldsymbol\pi(0)-\lambda A z_0
 +O(\lambda b+\lambda^3).$$

Consequently the first-order inverse $-A^{-1}\boldsymbol\pi(T)/\lambda$
has error $O(b/\lambda+b+\lambda^2)$. Taking $b=\lambda^3$ makes both
reconstruction and receiver disturbance $O(\lambda^2)$, with exact final
momentum access. With final momentum error $\rho$, add $O(\rho/\lambda)$;
$\rho=O(\lambda^3)$ retains the rate. For

$$\mathcal U=\epsilon_x\sup_{0\le t\le T}|P(t)-P^0(t)|,$$

one obtains $0\le\mathcal U\le C L_*P_*\lambda^4\to0$.
Clock mean energy, apparatus mass and duration stay fixed; incoming phase
volume and record errors shrink. Reporting $\Phi_{t_i}\widehat z_0$ on
any partition uses these same four records after latency $T$. This does not
supply fresh causal measurements at every cut or recover an unknown force.

At nominal apparatus data the probes are $O(\lambda)$, and receiver/clock
reaction is $O(\lambda^2)$. Differentiating their equations in $z_0$ preserves
these orders: reaction derivatives contain $\lambda$ times a probe or its
variation. The nominal nonlinear four-momentum map therefore obeys

$$F_\lambda(z)=-\lambda A z+\mathcal R_\lambda(z),\qquad
\|\mathcal R_\lambda\|_{C^1}\le C\lambda^3.$$

For small positive coupling its lower Lipschitz margin is
$\lambda\alpha/2$. Fix one such coupling. Apparatus uncertainty $b$ and
record error $\rho$ perturb the nominal record by at most
$C_\lambda b+\rho$. Minimum-residual calibration on $H_s=E$ gives

$$\|\widehat z-z\|\le\frac4{\lambda\alpha}(C_\lambda b+\rho).$$

Thus exact nonlinear calibration removes the first-order inverse's fixed
$O(\lambda^2)$ systematic remainder. At fixed coupling, shrinking $b,\rho$
closes both reconstruction-coordinate product and $\mathcal U$, while
receiver disturbance need only stay bounded. Exact model knowledge is
supplied; no computational-efficiency or uncertain-model theorem is claimed.
The record perturbations are contained in a small norm ball, without proving
that every point of an independently specified oracle-error ball is realized.

## Complete records replace clock preparation data

Known incoming probe momenta are denoted $u$. When the clock data $c$ are
known, subtract the known free drift $d_j(u)=Tu_j/M_j$ and use

$$F_{\lambda,c,u}(z,q)=((\pi(T)-u)/\lambda,q(T)-d(u))
 =(-A_cz,q)+O_{C^1}(\lambda).$$

The leading inverse margin is $\beta=\min(\alpha,1)$. Eight final pointer
coordinates recover $z,q$ globally on the fixed bounded domain, with
$\delta=\max(\rho_\pi/\lambda,\rho_q)$. Unknown incoming positions may
have fixed positive widths. The bound above gives product
$16L_*P_*\delta^2/\beta^2$. The special position-response rank used in
[the calibration obstruction](calibration-tolerance-recovery.md#incomplete-records-and-preparation-width)
is unnecessary for this recovery theorem.

If initial offset is known but speed is hidden, set $u=0$ and add final
clock momentum. The leading map of the nine scaled records is

$$L(z,q,v)=(-A_vz,q,v).$$

Let $D=\sup\|(\partial_v A_v)z\|$ on the domain. For output distance
$d$, its last blocks give $|\Delta v|,\|\Delta q\|\le d$, and the first
gives $\alpha\|\Delta z\|\le(1+D)d$. Hence the global inverse margin is
$\beta=\min(1,\alpha/(1+D))$. The $O_{C^1}(\lambda)$ remainder reduces
it at most to $\beta/2$. Use
$\delta=\max(\rho_\pi/\lambda,\rho_q,\rho_c)$ in the common bound.
This recovers speed jointly with reaction; $p_s(T)/M_c$ is not substituted
as an exact initial speed. Exact receiver energy and a local-patch prior
are unnecessary.

If initial offset also is hidden, add final clock position at $T$. With
clock units $S_*,V_*$ and $\theta=TV_*/S_*$ the ten-record leading map is

$$L(z,q,s,v)=(-A_{s,v}z,q,s+\theta v,v).$$

Let $D_s,D_v$ bound the signal's clock derivatives applied to receiver
states. The inverse clock shear gives $|\Delta v|\le d$ and
$|\Delta s|\le(1+\theta)d$, so an inverse margin is

$$\beta=\min\{(1+\theta)^{-1},
 \alpha/[1+D_s(1+\theta)+D_v]\}>0.$$

Again subtract the $C\lambda$ Lipschitz remainder and use the common bound,
now with $\delta=\max(\rho_\pi/\lambda,\rho_q,\rho_s,\rho_c)$.
All ten unknowns $z,q,s,v$ are recovered on the whole bounded domain.
These statements assume $u=0$ is known (the eight-record statement allows
known nonzero $u$); they do not assert recovery with completely unknown
incoming apparatus phase. Simultaneous classical access to final positions
and momenta is supplied, not implemented by a second recording apparatus.

## Energy-assisted local recovery and its global obstruction

Without final clock records, a known initial offset and receiver energy can
replace speed locally. At a selected shell point set
$B=-A^{-1}\partial_vA$ and require $\tau=z_*^TGBz_*>0$.
Append $H_s/E_*$ to the eight scaled pointer outputs. Its derivative kernel
obeys $dq=0$, $dz=Bz_*dv$, and $\tau dv/E_*=0$, hence is zero. If this
derivative is $J$, continuity gives one convex neighbourhood $U$ and
$\gamma=\|J^{-1}\|^{-1}>0$ with
$\sup_U\|D\mathcal G_\lambda-J\|\le\gamma/2$. Segment integration
then gives the common recovery bound with $\beta=\gamma$ on a fixed
shell patch times positive position/speed boxes inside $U$.

Existence of the transverse design and the actual distinct-speed global
pairs are proved together in
[the clock-fibre construction](calibration-tolerance-recovery.md#clock-fibres-and-local-versus-global-recovery).
Its full-shell branches do not contradict this local result: a supplied
patch is information. The inverse constants may deteriorate as $\tau\to0$.
Zero-coupling scaled extensions are proof devices; unscaled zero-coupling
records contain no receiver signal.

## Impulsive probes and actual repeated-cut refinement

A different instrument performs fresh readouts at each cut. Its externally
switched ideal Hamiltonian impulses are $G_x=\alpha x\pi$ and
$G_P=\beta P\rho$, with $\alpha>0$ dimensionless, $[\beta]=T/M$ and
canonical probes $(q,\pi),(r,\rho)$. Receiver/probe drift during impulses
is omitted by definition. Exact symplectic shears give pre-cut estimates
and kicks

$$\widehat x=x+q/\alpha,\quad
\widehat P=P+r/\beta-\alpha\pi,\quad
d_x=\beta\rho,\quad d_P=-\alpha\pi.$$

For full incoming rectangular half-widths $(s_q,t_q,s_r,t_r)$, exact support
errors are $s_q/\alpha$, $s_r/\beta+\alpha t_q$, and disturbances are
$\beta t_r,\alpha t_q$. Intrinsic products are $s_qt_q,s_rt_r$, in action
units. Scaling all widths to zero through positive-volume classical
preparations closes them; Liouville evolution of a fixed preparation imposes
no lower bound across different initial preparations. Exact final position
records and switching/preparation resources are supplied. These internal
receiver couplings are not local interactions with particle 1 alone.

For cut separation $\delta$, block the receiver flow as $(A_\delta,B_\delta;
C_\delta,D_\delta)$ in observed/hidden pairs $u=(x,P),w=(y,Q)$. With
$\widehat u_i=u_i+e_i$, the exact inversion error is

$$\widehat w_i-w_i=B_\delta^{-1}
 (e_{i+1}-A_\delta e_i+A_\delta d_i).$$

The receiver proof gives

$$B_\delta^{-1}=\begin{pmatrix}
6\mu/(g\delta^2)+O(1)&-2/(g\delta)+O(\delta)\\
-12\mu\nu/(g\delta^3)+O(\delta^{-1})&6\nu/(g\delta^2)+O(1)
\end{pmatrix}.$$

With fixed units and $\eta=\delta/t_*$, widths $O(\eta^p)$ therefore
give hidden-state error $O(\eta^{p-3})$, including the intervening kick.
At $N=T/\delta$ equal cuts the exact disturbance is
$\sum_{j<i}\Phi_{(i-j)\delta}(d_j,0)$, hence $O(\eta^{p-1})$.
For $p=4$ this gives uniform state reconstruction $O(\eta)$, disturbance
and energy error $O(\eta^3)$, intrinsic products $O(\eta^8)$, and incoming
free-probe kinetic-energy sum $O(\eta^7)$. The last sample is obtained by
propagating the preceding hidden estimate, adding only $O(\eta^4)$ error.
There is one sample interval of latency. Two fresh probes per cut require
$2(N+1)=O(\eta^{-1})$ probe count and fixed-probe-mass total mass. Reset,
switching, trapping, storage and recording costs are not included. Finite
meshes are different interventions with a common unmeasured-trajectory limit,
not restrictions of one measured law. Fixed error widths make this inversion
ill-conditioned, without proving impossibility for every estimator.

## Source scope and consequence for STATE

The classical translation interaction is read in Katagiri v2 §5
([B35 companion](../docs/batches/B35/readout-source-companion.md)); Theurel's
thermal/conserved-momentum comparison is bounded by
[B36](../references/batches/B36.md) and [B37](../references/batches/B37.md).
The observability precedent is Hermann–Krener, routed through
[B34](../docs/batches/B34/receiver-memory-source-companion.md).
[B47](../references/batches/B47.md) and B50–B55 document smooth-flow and
inverse methods; the explicit matrices, reaction estimates and global
margins here are model derivations. Historical checks cover specified claims,
not a general external referee certification.

For STATE, delayed recovery of known dynamics, actual repeated interventions,
and prediction under an unresolved force must remain separate. The latter
has its own [bounded-force theory](causal-force-information.md). A physical
restriction on preparation, complete-record access or calibration must be
derived before any of these prepared information scales can exclude zero
universally or identify a scale with physical $\hbar$.
