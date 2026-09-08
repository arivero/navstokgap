# Composition, crossover and gap product: verified calculations for A08, A09 and G01

Independent Claude Fable 5.1 session, 2026-09-08, after the
[six-direction review](../reviews/six-directions-2026-09-08.md). Every
displayed identity is checked exactly in
[`scripts/six_direction_checks.py`](../scripts/six_direction_checks.py); the
bridge table comes from an
[exact sampler](../scripts/telegraph_bridge_midpoint_sampler.py) of the C033
construction. These are working derivations for the A08, A09 and G01 tasks.
They carry no claim IDs until their per-result audits.

## 1. Composition inside the A01 class (A08)

**Result.** Let two independent finite irreducible reversible velocity chains
carry masses $m_1,m_2$ and plateaus $H_1,H_2$ in the sense of C019. The
centre-of-mass velocity is again a finite irreducible reversible chain, so
C019 applies to it, and with $M=m_1+m_2$

$$H_{\rm cm}=\frac{m_1H_1+m_2H_2}{M},\qquad
H_{\rm rel}=\frac{m_2H_1+m_1H_2}{M},\qquad
H_{\rm cm}+H_{\rm rel}=H_1+H_2.$$

**Proof.** The pair $(J^1,J^2)$ has generator $Q=Q_1\otimes I+I\otimes Q_2$
and invariant law $\pi_1\otimes\pi_2$. Detailed balance holds factorwise and
irreducibility of the product follows from that of the factors. The centre
velocity is $v_{\rm cm}=(m_1/M)\,v\otimes1+(m_2/M)\,1\otimes w$, with mean
zero. Since $Q_2\mathbf1=0$, $(-Q)^{-1}(v\otimes1)=((-Q_1)^{-1}v)\otimes1$
on the mean-zero subspace, and the cross term
$\langle v\otimes1,\,1\otimes(-Q_2)^{-1}w\rangle$ vanishes because
$\langle v,\mathbf1\rangle_{\pi_1}=0$. Hence
$2M\langle v_{\rm cm},(-Q)^{-1}v_{\rm cm}\rangle
=(m_1/M)\,2m_1\langle v,(-Q_1)^{-1}v\rangle
+(m_2/M)\,2m_2\langle w,(-Q_2)^{-1}w\rangle$.
The relative coordinate uses the reduced mass and $v\otimes1-1\otimes w$. $\square$

The composite law changes while the coefficient closes. Two $\pm u$ particles
give a four-state centre chain with velocities $\pm u$ and
$\pm u(m_1-m_2)/M$, as the review anticipated.

**Gaussian class and many bodies.** With $\operatorname{Var}\Delta X_i=\kappa_i\Delta/m_i$,
a collective coordinate $y=\sum_ic_iX_i$ with kinetic mass
$\mu_y=(\sum_ic_i^2/m_i)^{-1}$ has

$$\kappa_y=\frac{\sum_i(c_i^2/m_i)\,\kappa_i}{\sum_ic_i^2/m_i},$$

a convex combination of the constituent coefficients. Over a mass-orthogonal
basis the coefficients add to $\sum_i\kappa_i$; the three-body Jacobi basis
is checked explicitly. The review's cross covariance
$\operatorname{Cov}(\Delta R,\Delta r)=\Delta(\kappa_1-\kappa_2)/M$ is
confirmed, so independence of centre and relative motion is equivalent to
$\kappa_1=\kappa_2$ in this class.

**Additive-function step.** If $\kappa(m)\ge0$ depends only on mass and
$\kappa(m_1+m_2)$ equals the composite value, then $f(m)=m\kappa(m)$ is
additive and nonnegative, hence monotone, hence $f(m)=Km$ on the positive
reals. Two splits of one mass already give $\kappa(2)=\kappa(1)$. The value
$K=0$ remains admissible.

**Countertest.** The A02 bath coefficient $H(m)=(m+M_b)s^2/\nu$ violates the
composition premise by an exact amount:

$$H(m_a+m_b)-\frac{m_aH(m_a)+m_bH(m_b)}{m_a+m_b}
=\frac{2m_am_bs^2}{\nu(m_a+m_b)}>0.$$

A rigid composite immersed as one tracer fluctuates more than the centre of
mass of two separately immersed tracers. This is the precise sense in which a
reservoir coefficient depends on the preparation, which is the review's
separate preparation obligation.

## 2. Crossover and the conditioned midpoint (A09)

Coordinator update, A09a/B17: [the exact crossover proof](bridge-crossover.md)
now gives the full beta mixture and plateau limit. It corrects the earlier
unscaled-mean interpretation below; the sampler remains numerical evidence.

**Necessary window.** C018 and C031 give, for any coefficient $K$ realized at
window $\Delta$ under speed bound $u$, the condition $\Delta\ge\Delta_*:=K/(mu^2)$.
For the stationary telegraph observable of C020 the bound reads
$\mathsf h(\Delta)\le H_*\Delta/\Delta_*$ with $\Delta_*=1/\lambda$, and
$\mathsf h$ saturates it at leading order:
$x-f(x)=2x^2/3+O(x^3)$ for $f(x)=1-(1-e^{-2x})/(2x)$.

**Conditioned midpoint of the C033 bridge.** With the count weights and
simplex durations of the [return-bridge note](telegraph-return-bridge.md),
the $k=1$ component has $\mathbb E[Y]=uT/6$ and
$\mathbb E[(Y-uT/2)^2]=u^2T^2/6$. Expanding the mixture in $z=\lambda T$,

$$\kappa_{\rm mid}:=\frac{4m\operatorname{Var}(Y)}{T}=H_*\frac{z^3}{6}+O(z^5),
\qquad \frac{2m\,\mathbb E[Y^2]}{T}\to\frac{mu^2T}{2}\ (z\to0).$$

The exact sampler confirms the cubic onset and the plateau, with $m=u=1$:

| $z=\lambda T$ | $\kappa_{\rm mid}/H_*$ | $z^3/6$ | $2m\mathbb E[Y^2]/T$ | atom mass | $1/I_0(z)$ |
| --- | --- | --- | --- | --- | --- |
| 0.25 | 0.0025 | 0.0026 | 0.124 | 0.985 | 0.985 |
| 0.5 | 0.019 | 0.021 | 0.240 | 0.940 | 0.940 |
| 1 | 0.122 | 0.167 | 0.429 | 0.790 | 0.790 |
| 2 | 0.476 | 1.33 | 0.608 | 0.437 | 0.439 |
| 4 | 0.848 | — | 0.608 | 0.088 | 0.089 |
| 8 | 0.940 | — | 0.545 | 0.002 | 0.002 |
| 32 | 0.985 | — | 0.508 | 0.000 | 0.000 |

The variance coefficient converges to $H_*$; the second-moment version converges
to $H_*/2$. The unscaled mean tends to $u/(2\lambda)$, while its contribution
to the action divided by $T$ vanishes. Monotonicity is not established here;
the second-moment table already shows an overshoot. An earlier Monte Carlo with
position-only conditioning, which admits both terminal velocities, showed a
quadratic onset. The small-window exponent therefore depends on the
conditioning protocol; $\Delta_*$ and the plateau are the same in both.

**Scales.** At $K=\hbar$ and $u=c$, $\Delta_*=\hbar/(mc^2)$ and
$u\Delta_*=\hbar/(mc)$, the reduced Compton time and length; the substitution
adds the identification $K=\hbar$, as the review notes. For A07, an
acceleration ceiling $a$ and the crossover are related by $a=u\lambda=u/\Delta_*$;
at $u=c$ and $\lambda=mc^2/\hbar$ this is $mc^3/\hbar$, the scale of
Caianiello's maximal-acceleration proposal. That attribution is a lead to
verify.

## 3. Gap product and slow modes (G01)

From C019's spectral form, $H_*\gamma_{\min}\le2m\sigma_v^2\le H_*\gamma_{\max}$,
with equality $H_*\gamma=2mu^2$ for two states; both are checked on fixed
reversible three-state chains. The review's slow-mode countertest is confirmed
exactly: appending an independent two-state label with rate $\epsilon$, with
velocity depending only on the telegraph sign, gives $-Q$ eigenvalues
$\{0,2\epsilon,2\lambda,2\lambda+2\epsilon\}$ and leaves $H_*=mu^2/\lambda$
unchanged. The susceptibility bounds the gap from above only. With a supplied
action unit $K$, the two-state gap in energy units is $2K\lambda$; at $u=c$,
$K=\hbar$ and $\lambda=mc^2/\hbar$ it equals $2mc^2$, the separation of the
free Dirac branches at zero momentum. In Monte Carlo language the bound is
$\tau_{\rm int}\le\tau_{\rm exp}$, with $H_*=2m\sigma_v^2\tau_{\rm int}$ and
$\gamma_{\min}=1/\tau_{\rm exp}$.

## 4. Continuation check (B15 obligation)

Both routes agree symbolically. Substituting $u=e^{-i\omega t}\psi$ into
$p_{tt}+2i\omega p_t=c^2p_{xx}$ gives $\psi_{tt}-c^2\psi_{xx}+\omega^2\psi=0$.
Substituting $p=e^{-\lambda t}\phi$ into the real telegraph equation gives
$\phi_{tt}-c^2\phi_{xx}-\lambda^2\phi=0$, and $\lambda=i\omega$ recovers the
same Klein–Gordon form. The continued object is an amplitude; the Dirac
two-component construction remains the next obligation recorded in
[B15](../references/batches/B15.md).

## 5. Source leads at metadata level

- Kac, *A stochastic model related to the telegrapher's equation*, Rocky
  Mountain J. Math. 4, 497–509 (1974), DOI 10.1216/RMJ-1974-4-3-497, open
  access at Project Euclid and a reprint of 1956 Magnolia Petroleum lectures.
  This route removes the access block recorded in B09.
- Sokal, *Monte Carlo Methods in Statistical Mechanics: Foundations and New
  Algorithms*, in *Functional Integration* (Springer, 1997),
  DOI 10.1007/978-1-4899-0319-8_6, for the integrated-versus-exponential
  autocorrelation inequality.

Both await passage-level reading in the A09 and G01 audits.

## 6. Status and reproduction

`python3 scripts/six_direction_checks.py` writes `out/six-direction-checks.json`
and runs inside `make check`. The sampler is optional and prints the table
above from a fixed seed. [`formal/Crossover.lean`](../formal/Crossover.lean)
drafts the crossover lemma for F01 and is uncompiled. The
[P02 handoff](../research/handoffs/P02-six-direction-checks.md) records the
session and its limits.
