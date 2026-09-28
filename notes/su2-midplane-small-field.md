# The SU(2) mid-plane on its small-field set: the local half of estimate (18)

**Result, 2026-09-28 (Claude; written derivation, to be refereed by
Fable).** Take one halving of direction 1 in $1+2$ dimensions with gauge
group $SU(2)$ and isotropic heat time $t=\lambda_3a=\hbar g_{\rm cl}^2a$, as in the
[mid-plane note](su2-midplane-order-t.md). Restrict the mid-plane
fluctuations to the small-field set
$\Omega_\eta=\{|\xi_e|\le\eta\ \text{for every mid-edge}\ e\}$ with

$$\varepsilon=t^{1/2-\delta},\qquad \eta=2\varepsilon,\qquad 0<\delta<\tfrac16,$$

by the convex barrier of §1, and call $\mathcal D_s$ the resulting normalized
defect (the definition of $\mathcal D$ in Hypothesis P($\alpha$) of the
[series/parallel note](series-parallel-gauge-refinement.md), with the
fluctuation integral restricted). Uniformly in the size of the mid-plane:

- **Lemma 1 (covariant decay).** For every background mid-plane
  connection and every symmetric perturbation of range one and norm
  $\kappa<2$ of the Gaussian Hessian, the inverse $K$ obeys
  $|K^{-1}(e,e')|\le(4-\kappa)^{-1}\bigl((2+\kappa)/6\bigr)^{d(e,e')}$, where $d$ is the distance in the
  graph of edges sharing a face; at $\kappa=0$, $\frac14\,3^{-d}$.
- **Lemma 2 (bridge tail).** The bridge midpoint law of a cut face with
  flux $X$ satisfies $\beta(d(m,m_*)\ge r)\le C_2\,t^{-7/2}e^{-2r(r-|X|)/t}$ for
  $r\ge|X|/2$; at $r=\eta$ and $|X|\le\varepsilon$ this is at most $C_2t^{-7/2}e^{-4t^{-2\delta}}$.
- **Lemma 3 (uniform convexity).** For coarse fluxes $|X_p|\le\varepsilon$ and
  $\xi\in\Omega_{c_0}$, $c_0$ a small absolute constant, the Hessian of the exponent in
  the fluctuation variables lies between $(H_A-\kappa_t)/t$ and $(H_A+\kappa_t)/t$, with
  $H_A=4I+\frac12C_A^*C_A$ ($C_A$ the covariant curl of the background) and
  $\kappa_t\le C_3(\varepsilon+|\xi|_\infty)$; on $\Omega_\eta$, $\kappa_t\le3C_3\varepsilon$.
- **Proposition 4 (local Laplace comparison).** If the coarse data $U$
  are joined to the trivial configuration by a small-field path with
  controlled flux velocities (Hypothesis I of §5), then

  $$\bigl|\mathcal D_s(U)-\mathcal D_s(1)-\mathcal D_0(U)\bigr|
  \le C_4\,t^{1/2-\delta}\sum_p\frac{|X_p|^2}t,$$

  with $\mathcal D_0$ the free-field defect and $C_4$ independent of the plane
  size. With $c_{\rm vac}=\mathcal D_s(1)/N$ this is the weak form of Hypothesis
  P($\alpha$), $\alpha=\frac12-\delta$, for the small-field defect, with all coupling shifts
  set to zero (they are of order $t$ and fit inside the remainder).

The proof uses no cluster expansion. Brascamp--Lieb bounds the
fluctuation covariance from above and Cramér--Rao from below, both in
operator norm, and global gauge invariance removes the linear term; all
bounds are norms of local operators, so they are uniform in $N$.

Two items stay open for the weak (18) on the full integral (§6):
Hypothesis I for non-abelian data on large planes, and the large-field
comparison $\mathcal D-\mathcal D_s$, where the naive Peierls bound fails for an explicit
reason. Lemma 1 also suggests that a logarithmic size clause would
replace $\min_jN_j\ge c_0/t$ for the torus windings (expected, not proved).

## 1. Setting

The mid-plane at a layer is a periodic two-dimensional lattice of $N$
sites with $2N$ mid-edges (directions 2 and 3) and $N$ mid-faces; distinct
mid-planes are independent given the coarse data, so $\mathcal D$ is a sum over
mid-planes. In the mid-vertex gauge of Proposition 1 write $m_e=m_{*e}e^{\xi_e}$,
$\xi_e\in\mathfrak{su}(2)\cong\mathbb R^3$, with $m_{*e}$ the geodesic midpoint between $P_e$ and $Q_e^{-1}$,
whose distance is the cut-face flux $|X_e|$. The exponent is

$$S(\xi;U)=\sum_e\frac{d(P_e,m_e)^2+d(m_e,Q_e^{-1})^2-\frac12|X_e|^2}{t}
+\sum_g\frac{d(m_{\partial g},e)^2}{4t}+J(\xi;U),$$

the half faces at heat time $t/2$, the bridge denominator at $t$, the
mid-faces at $2t$, and $J$ collecting the heat-kernel and Haar amplitudes
in exponential coordinates, smooth with derivatives bounded independently
of $t$. It vanishes at $\xi=0$ in its bridge part. Its linearization about the
trivial configuration is the quadratic form of §1 of the mid-plane note,
$\frac1t(2\sum_e|\xi_e|^2+\frac14\sum_g|\bar\Phi_g+(C\xi)_g|^2)$, with Hessian $H_0/t$, $H_0=4I+\frac12C^*C$.

The small-field restriction uses a convex barrier: $W_\eta(\xi)=\sum_ew(|\xi_e|)$
with $w$ convex, $w=0$ on $[0,\eta]$ and $w\to\infty$ at $c_0$. The measure
$\mu_U\propto e^{-S-W_\eta}d\xi$ on $\prod_eB(0,c_0)$ is then log-concave by Lemma 3, its
mass outside $\Omega_\eta$ is bounded by Lemma 2, and $\mathcal D_s(U)$ is $-\log$ of its
normalizing integral plus the $\xi$-independent normalizations of
Hypothesis P($\alpha$) (bridge denominators and old-face ratios).

## 2. Lemma 1

*Proof.* Each mid-edge lies in two mid-faces and
$|(C_A\xi)_g|^2\le4\sum_{e\in\partial g}|\xi_e|^2$ for every background, because the covariant curl
adds four adjoint-rotated vectors. Hence $0\le C_A^*C_A\le8$ and $4\le H_A\le8$.
Write $K=6I+(K-6I)$ with $\|K-6I\|\le2+\kappa$. The operator $K-6I$ couples only
edges that share a face, so $(K-6I)^n(e,e')=0$ for $n<d(e,e')$, and every
matrix block is bounded by the operator norm. The Neumann series gives
$|K^{-1}(e,e')|\le\frac16\sum_{n\ge d}\bigl(\frac{2+\kappa}6\bigr)^n=\frac{1}{4-\kappa}\bigl(\frac{2+\kappa}6\bigr)^d$. $\square$

## 3. Lemma 2

With normalized Haar measure and $\theta\in[0,2\pi]$ the geodesic distance
(the three-sphere of radius 2), the image formula of the
[SU(2) midpoint note](su2-midpoint-exact.md), Theorem 1, reads
$k_t(\theta)=e^{t/8}\sqrt{8\pi}\,t^{-3/2}\,\Xi_+(\theta)/\sin(\theta/2)$. For $0<t\le1$:

- *Upper bound.* $k_t(\theta)\le C_+t^{-5/2}e^{-\theta^2/(2t)}$. On $[0,\pi]$ use
  $\theta/\sin(\theta/2)\le\pi$ for the term $w=0$; the other images are smaller by
  $e^{-3\pi^2/t}$ and odd pairs vanish at $\theta=0$. On $[\pi,2\pi]$ pair $w=0$ with $w=1$:
  with $\psi=2\pi-\theta$ the pair equals
  $e^{-(4\pi^2+\psi^2)/(2t)}[(2\pi-\psi)e^{2\pi\psi/t}-(2\pi+\psi)e^{-2\pi\psi/t}]$, which divided
  by $\sin(\psi/2)$ is at most $(16\pi^2/t)e^{-\theta^2/(2t)}$ up to a constant.
- *Lower bound.* For $\theta\le1$ the term $w=0$ dominates and
  $\theta/\sin(\theta/2)\ge2$, so $k_t(\theta)\ge c_-t^{-3/2}e^{-\theta^2/(2t)}$.

*Proof of Lemma 2.* The bridge density with respect to Haar measure is
$k_{t/2}(d(P,m))\,k_{t/2}(d(m,Q^{-1}))/k_t(|X|)$. By the triangle inequality
through $m_*$, $d(P,m)\ge r-|X|/2$ and $d(m,Q^{-1})\ge r-|X|/2$ when $d(m,m_*)=r$. The
bounds above give a density at most
$(32C_+^2/c_-)\,t^{-7/2}\exp[-(2(r-|X|/2)^2-\frac12|X|^2)/t]=C_2t^{-7/2}e^{-2r(r-|X|)/t}$, and Haar
measure has total mass one. At $r=\eta=2\varepsilon\ge2|X|$ the exponent is at least
$4\varepsilon^2/t=4t^{-2\delta}$. $\square$

## 4. Lemma 3

*Proof sketch.* Each half-face term is $|\log(Ae^{\pm\xi}B)|^2/t$ with
$|\log A|,|\log B|\le\varepsilon$ in the mid-vertex frame. On $\mathfrak{su}(2)$ with
$[T_a,T_b]=\epsilon_{abc}T_c$ and $|T_a|=1$, $|[x,y]|\le|x||y|$, and the Baker--Campbell--Hausdorff
remainders give $\log(Ae^{\zeta}B)=\log(AB)+{\rm Ad}(\zeta)+O(|\zeta|(|\zeta|+\varepsilon))$ with
derivatives of the same order. The Hessian of $|\cdot|^2$ is $2I$, so each
half-face contributes $2I/t$ up to $O(\varepsilon+|\xi|)/t$, and the pair gives the
$4I/t$ of $H_A/t$. The mid-face term $|\log m_{\partial g}|^2/(4t)$ has Hessian
$\frac12C_A^*C_A/t$ up to $O(|\bar\Phi_g|+\sum_{e\in\partial g}|\xi_e|)/t$, and $|\bar\Phi_g|\le\varepsilon$. The amplitude
$J$ has bounded Hessian, which is $O(t)/t$ and $t\le\varepsilon$. All corrections are
local, so their operator norm is bounded by a row sum. This gives
$\kappa_t\le C_3(\varepsilon+|\xi|_\infty)$ with an absolute $C_3$, and convexity on $\Omega_{c_0}$ once
$C_3(\varepsilon+c_0)<4$. The constant $C_3$ is computable from the BCH remainder
bounds; it is not tracked here. $\square$

## 5. Proposition 4

**Hypothesis I (small-field path).** There is a $C^2$ path $U(s)$, $s\in[0,1]$,
from the trivial configuration to $U$ through coarse data with
$|X_p(s)|\le2\varepsilon$, whose flux coordinates satisfy $\sum_p|\dot X_p(s)|^2\le C_I\sum_p|X_p|^2$
and $|\ddot X_p(s)|\le C_I\sum_{p'\sim p}|X_{p'}|^2$ (neighbouring plaquettes $p'$), where
$X_p=X_p(U)$. For an abelian group the linear path $X(s)=sX$ satisfies it
with $C_I=1$.

*Proof of Proposition 4.* Put $g(s)=\mathcal D_s(U(s))$.

(a) *No linear term.* A constant gauge transformation rotates every flux
by the adjoint action and leaves $\Omega_\eta$, the barrier and the normalizations
invariant, so $\nabla_X\mathcal D_s$ at the trivial configuration is an adjoint-invariant
vector in $\bigoplus_p\mathfrak{su}(2)^*$, hence zero. So $g'(0)=0$, and likewise for $\mathcal D_0$.

(b) *Second derivatives.* $\partial_X^2\mathcal D_s=E_\mu[\partial_X^2S]-{\rm Cov}_\mu(\partial_XS)$ (with the
normalizations, whose Hessians differ from their Gaussian versions by
$O(1)=O(t)/t$), and for the Gaussian reference
$\partial_X^2\mathcal D_0=\partial_X^2S_2-{\rm Cov}_{G}(\partial_XS_2)$, with $S_2$ the linearized exponent and $G$
the Gaussian with covariance $tH_0^{-1}$. Three comparisons, each as a
quadratic form in the flux variation $v$:

1. $\partial_X^2S-\partial_X^2S_2$ is a local operator with entries $O((\varepsilon+\eta)/t)$ on the support
   of $\mu$, so $|\langle v,(E_\mu\partial_X^2S-\partial_X^2S_2)v\rangle|\le C(\varepsilon+\eta)\|v\|^2/t$.
2. Write $\partial_XS=\frac1t(M\xi+NX)+R$ with $M,N$ the linear couplings and
   $R=O((|X|+|\xi|)^2/t)$, local. By Brascamp--Lieb and Lemma 3,
   ${\rm Cov}_\mu(\xi)\le E_\mu[({\rm Hess}\,S)^{-1}]\le t(H_A-\kappa_t)^{-1}$, and by the Cramér--Rao inequality for
   location families, ${\rm Cov}_\mu(\xi)\ge(E_\mu{\rm Hess}\,S)^{-1}\ge t(H_A+\kappa_t)^{-1}$; the barrier adds only
   terms of the size of Lemma 2. Hence
   $\|{\rm Cov}_\mu(\xi)-tH_A^{-1}\|\le t\kappa_t/(4(4-\kappa_t))$. The connection itself need not be
   small on a large plane, only its fluxes, so the comparison with the
   abelian reference is made gauge-invariantly: the flux response
   $M_AH_A^{-1}M_A^T$ of the covariant Gaussian differs from the abelian $MH_0^{-1}M^T$
   by holonomy factors around closed paths, and by Lemma 1 a path of
   length $L$ carries weight $3^{-L}$ while enclosing at most $L^2$ plaquettes of
   flux $\le\varepsilon$; the sum over paths gives a difference $O(\varepsilon)$ in operator norm
   (sketch). So $|\langle v,(M_A{\rm Cov}_\mu(\xi)M_A^T-tMH_0^{-1}M^T)v\rangle|/t^2\le C\varepsilon\|v\|^2/t$.
3. By Brascamp--Lieb, ${\rm Var}_\mu\langle v,R\rangle\le\frac t{4-\kappa_t}E|\nabla_\xi\langle v,R\rangle|^2\le C(\varepsilon+\eta)^2\|v\|^2/t$, and
   the cross covariance is bounded by the geometric mean of the two
   variances, $C(\varepsilon+\eta)\|v\|^2/t$.

So $|\langle v,(\partial_X^2\mathcal D_s-\partial_X^2\mathcal D_0)v\rangle|\le C(\varepsilon+\eta)\|v\|^2/t$ at every point of the path.

(c) *Taylor along the path.* $g(1)-g(0)=\int_0^1(1-s)g''(s)\,ds$ with
$g''=\langle\dot X,\partial_X^2\mathcal D_s\dot X\rangle+\langle\nabla_X\mathcal D_s,\ddot X\rangle$, and the same identity for $\mathcal D_0$, which is
quadratic. The first terms differ by $C(\varepsilon+\eta)C_I\|X\|^2/t$. For the second,
$|\nabla_X\mathcal D_s|\le C(\varepsilon+\eta)/t$ per plaquette and $|\ddot X_p|\le C_I\sum_{p'\sim p}|X_{p'}|^2$, which is
of the same order; $\nabla\mathcal D_0$ obeys the same bound. With $\eta=2\varepsilon$ and
$\varepsilon=t^{1/2-\delta}$ the total is $C_4t^{1/2-\delta}\|X\|^2/t$. No constant depends on $N$: every
bound is the norm of a local operator or a Brascamp--Lieb estimate with
local gradients. $\square$

References for the two inequalities:
[Brascamp and Lieb (1976)](https://doi.org/10.1016/0022-1236(76)90004-5)
(metadata); the Cramér--Rao bound ${\rm Cov}\ge I^{-1}$ with the Fisher information
$I=E[\nabla S\nabla S^T]=E[{\rm Hess}\,S]$ holds after integration by parts, which the barrier
permits.

## 6. What stays open for the weak (18)

(a) **Hypothesis I for non-abelian data on large planes.** For $SU(2)$ the
fluxes cannot be scaled independently: link variables accumulate flux
along paths, the mid-plane background carries a covariant connection,
and the global holonomies of the torus constrain the plaquette data.
The natural route is quasi-locality: Lemma 1 gives exponential decay of
the inverse Hessian for every background, and for uniformly convex
finite-range measures the covariances decay as well
([Helffer and Sjöstrand 1994](https://doi.org/10.1007/BF02186817),
metadata). Local changes of the coarse data then change $\mathcal D_s$ by local
amounts, and a telescoping over plaquettes replaces the global path.
This is expected and not carried out here.

(b) **The large-field comparison $\mathcal D-\mathcal D_s$.** A Peierls bound
$Z(\Lambda\ \text{large})/Z_s\le e^{-\kappa(t)|\Lambda|}$ with $\kappa(t)\to\infty$ is needed for connected sets $\Lambda$ of
large-field edges. The naive comparison fails. Lemma 2 gains
$e^{-4\varepsilon^2/t}$ per large edge at $r=\eta$. The small-field denominator bounds a
face next to $\Lambda$ from below only by $e^{-(|\bar\Phi_g|+\sum_{e\in\partial g}|\xi_e|)^2/(4t)}$ with every $|\xi_e|$
up to $\eta$, that is by $e^{-81\varepsilon^2/(4t)}$, and each edge borders two faces:
the loss exceeds the gain. Balaban's large-field methods, with
gauge-invariant small-field conditions and multiscale holes, are the
known way around this
([Balaban 1989 I](https://doi.org/10.1007/BF01257412),
[II](https://doi.org/10.1007/BF01238433); for the small-field side
[Dimock 2013](https://doi.org/10.1142/S0129055X13300100); metadata).

(c) **Torus windings.** With Lemma 1 the torus corrections of the
Gaussian part are bounded by $CN((2+\kappa)/6)^{n_*}$, $n_*=\min_jN_j$, so the weak form
would need only $n_*\ge\frac{\alpha}{\log3}\log(1/t)+C$ in place of the clause $n_*\ge c_0/t$ of the
mid-plane note. This rests on (a) and is recorded as expected.

## 7. Consequence for STATE

Atlas cell 2: the local, small-field half of the weak estimate (18) is
proved for $SU(2)$ in $1+2$ (Proposition 4, with Lemmas 1--3), uniformly in
the plane size and without a cluster expansion. Open: Hypothesis I for
non-abelian data on large planes (quasi-locality), and the large-field
Peierls bound, whose naive form fails for the reason in §6(b).
