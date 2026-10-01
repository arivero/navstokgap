# An Agmon bound for the Kogut--Susskind ground state: finite-volume global magnetic-energy tails

Later correction: [the global/local note](agmon-global-not-local.md) supersedes the original local-suppression interpretation; [the magnetic-energy identities note](magnetic-energy-identities.md), §4, records the limitation of the proposed Gibbs-comparison repair (both full-read).

> **Correction (2026-10-02).** The original title and lead claimed
> suppression at rate $1/g^2$ per locally excited plaquette and said this
> supplied the Hamiltonian large-field input for decimation. Those claims
> are **withdrawn**. Section 2 estimated one relaxation path, which can
> give only an upper bound on an infimum, whereas decay requires a lower
> bound for every path. It is replaced below by the global-excess bound
> of [the global/local note](agmon-global-not-local.md), with its volume
> dependence retained. The original pointwise estimate for $|\Omega(U)|^2$
> is replaced by an integrated probability estimate. Sections 3--5 no
> longer assert local exponential-moment control or a successful match
> to the flow Jacobian. Lemma 1 and Corollary 2 survive; their application
> now states the weight margin and prefactor explicitly. The threshold
> $e_0/B'$ is not the mean magnetic energy. Excited-state extensions use
> $|\psi|^2$ and do not assume positivity. This paragraph records the
> correction rather than silently removing the earlier claims.

On a fixed finite spatial lattice, Agmon's weighted eigenfunction
identity gives a tail bound for the **total** magnetic potential of the
Kogut--Susskind ground state. With
$$H=\frac{\hbar c}{a}\left[A'(-\Delta)+B'V\right],\qquad
A'=\frac{g^2}{2},\quad B'=\frac{2}{g^2},\quad
V=\sum_p\left(N-\operatorname{Re}\operatorname{tr}U_p\right),$$
write $e_0=aE_0/(\hbar c)$ and $\bar v=e_0/B'$. If
$M\ge\|\nabla V\|_\infty$ and $M>0$, every path to $\{V\le\bar v\}$ has
Agmon length at least
$$\frac{4}{3g^2M}\,(V-\bar v)_+^{3/2}.$$
Consequently, for $0<\delta<1$ and $s>0$,
$$\mathbb P_\Omega(V-\bar v\ge s)
\le C_{\epsilon,\delta}\exp\left[-\frac{8(1-\delta)}{3g^2M}s^{3/2}\right],$$
with a finite-volume prefactor specified in §2. On a periodic
three-dimensional spatial lattice one may take
$M=2\sqrt{2N|\mathcal E|}$ and $|\mathcal E|=|\mathcal P|$. A total
excess proportional to volume then has an extensive exponent; a fixed
total excess has an exponent that vanishes as the volume grows. No
volume-uniform local large-field estimate, spectral gap or continuum
claim follows. The written proofs below establish these finite-lattice
statements without the original relaxation-path heuristic.

## 1. Setting and the weighted identity

Let $G=SU(N)$, $N\ge2$, $g>0$, $a>0$, and let
$\mathcal M=G^{\mathcal E}$ carry the product bi-invariant metric with
Lie algebra normalization $\operatorname{tr}(T^aT^b)=\delta_{ab}/2$.
Use a finite spatial lattice whose elementary plaquettes have four
distinct links; the periodic cubic examples have at least three sites
in each direction. Haar measure $d\mu$ is normalized. The operator
$-\Delta$ is nonnegative. Its smooth bounded potential $V\ge0$ gives a
smooth normalized positive ground state $\Omega$ on this connected
closed manifold, as in T1 of
[the obligations map](mass-gap-obligations-lattice.md) (setting passage).
The unique positive ground state is gauge invariant. In dimensionless
units its equation is
$$-A'\Delta\Omega+(B'V-e_0)\Omega=0,\qquad
\int\Omega^2d\mu=1.$$

**Lemma 1 (Agmon identity).** For every real Lipschitz weight $\rho$,
$$A'\int_{\mathcal M}|\nabla(e^\rho\Omega)|^2d\mu
+\int_{\mathcal M}(B'V-e_0-A'|\nabla\rho|^2)e^{2\rho}\Omega^2d\mu=0.$$

*Proof.* Multiply the eigenvalue equation by $e^{2\rho}\Omega$ and
integrate by parts on the closed manifold. Almost everywhere,
$$|\nabla(e^\rho\Omega)|^2
=\nabla\Omega\cdot\nabla(e^{2\rho}\Omega)
+e^{2\rho}\Omega^2|\nabla\rho|^2.$$
Substitution gives the identity; Lipschitz weights are valid weak test
functions on this compact manifold. $\square$

**Corollary 2 (forbidden-region estimate).** Put
$q=B'V-e_0$, $\Sigma_\epsilon=\{q\ge\epsilon\}$, $\epsilon>0$.
If $\rho$ is Lipschitz,
$$A'|\nabla\rho|^2\le q-\epsilon/2\quad\hbox{on }\Sigma_\epsilon,
\qquad \rho\le R\quad\hbox{on }\mathcal M\setminus\Sigma_\epsilon,$$
then
$$\frac\epsilon2\int_{\Sigma_\epsilon}e^{2\rho}\Omega^2d\mu
\le K_\rho e^{2R}\int_{\mathcal M\setminus\Sigma_\epsilon}\Omega^2d\mu,
\qquad K_\rho=e_0+A'\|\nabla\rho\|_\infty^2.$$
More generally, replacing $\epsilon/2$ in the admissibility inequality
by any $\eta>0$ replaces the left coefficient by $\eta$. Thus
$$\int_{\mathcal M}e^{2\rho}\Omega^2d\mu
\le e^{2R}\left(1+\frac{K_\rho}{\eta}\right).$$

*Proof.* Drop the nonnegative gradient integral in Lemma 1. On the
forbidden set the remaining coefficient is at least $\eta$; on its
complement it is at least $-K_\rho$ because $V\ge0$. Split the integral
and use normalization. The complementary weighted mass is at most
$e^{2R}$. $\square$

The Agmon distance to $\mathcal A=\{q\le0\}$ is
$$d(U)=\inf_{\gamma:\,U\to\mathcal A}
\int_\gamma\sqrt{q_+/A'}\,|d\gamma|.$$
The positive part is essential: the metric vanishes in the allowed
region. This distance is Lipschitz, vanishes on $\mathcal A$, and
satisfies $A'|\nabla d|^2\le q_+$ almost everywhere. Indeed appending a
short segment bounds its increment by the local weighted length; the
bounded weight also bounds its ordinary Lipschitz constant. Among
weights vanishing on $\mathcal A$ with this gradient constraint, $d$
is maximal, by integrating the constraint along every path. This
zero-set and gradient constraint is distinct from Corollary 2's strict
margin condition.

For $\rho=(1-\delta)d$, define
$\theta_\delta=1-(1-\delta)^2=2\delta-\delta^2>0$. On
$\Sigma_\epsilon$,
$$q-A'|\nabla\rho|^2\ge\theta_\delta q\ge\theta_\delta\epsilon.$$
The original $\epsilon/2$ margin is therefore guaranteed by this
argument only if $\delta\ge1-1/\sqrt2$. For arbitrary $0<\delta<1$,
use the generalized margin $\eta=\theta_\delta\epsilon$ instead.
Let $q_{\max}=\max_{\mathcal M}q_+$ and
$R_{\epsilon,\delta}=(1-\delta)\sup_{\{q<\epsilon\}}d$. Then
$$\int e^{2(1-\delta)d}\Omega^2d\mu
\le e^{2R_{\epsilon,\delta}}
\left(1+\frac{e_0+(1-\delta)^2q_{\max}}
{\theta_\delta\epsilon}\right).$$
All constants are finite at fixed lattice and coupling. In particular,
$$R_{\epsilon,\delta}\le(1-\delta)\operatorname{diam}(\mathcal M)
\sqrt{q_{\max}/A'},$$
since $\mathcal A$ is nonempty ($V=0$ is attainable
and $e_0\ge0$). This is not a uniform constant in volume or coupling.
No pointwise bound on $\Omega$ follows just by dropping the gradient
term in this identity.

## 2. A lower bound over all paths and a global tail

The threshold $\bar v=e_0/B'$ satisfies
$$\bar v=\langle V\rangle_\Omega+
\frac{A'}{B'}\int|\nabla\Omega|^2d\mu\ge\langle V\rangle_\Omega.$$
It is an energy threshold, not the ground-state mean magnetic energy.
The constant trial function gives
$e_0\le B'\langle V\rangle_{\rm Haar}=B'N|\mathcal P|$, since each
plaquette has a Haar-distributed holonomy. Also $V\le2N|\mathcal P|$,
so $q_{\max}\le2B'N|\mathcal P|$.

**Proposition 3 (global excess, corrected).** For any
$M\ge\|\nabla V\|_\infty$, $M>0$, set
$$f=V-\bar v,\qquad F(U)=\frac{4}{3g^2M}f(U)_+^{3/2}.$$
Then $d\ge F$. For any $\epsilon>0$ and $0<\delta<1$ set
$$R_F=(1-\delta)\frac{4}{3g^2M}
\left(\frac\epsilon{B'}\right)^{3/2},\qquad
C_{\epsilon,\delta}=e^{2R_F}
\left(1+\frac{e_0+(1-\delta)^2q_{\max}}
{\theta_\delta\epsilon}\right).$$
For $\mathbb P_\Omega(B)=\int_B\Omega^2d\mu$,
$$\mathbb P_\Omega(f\ge s)
\le\min\left\{1,\ C_{\epsilon,\delta}
\exp\left[-\frac{8(1-\delta)}{3g^2M}s^{3/2}\right]\right\},
\qquad s>0.$$

*Proof.* On any path from $U$ with $f(U)>0$ to $\{f\le0\}$, stop at its
first zero of $f$. With arclength parameter $r$, $|f'(r)|\le M$.
The total variation of $\frac23 f^{3/2}$ along this segment is at least
its endpoint difference, even if $f$ is not monotone. Hence
$$\int_\gamma\sqrt{(B'/A')f_+}\,dr
\ge\frac{\sqrt{B'/A'}}{M}\int\sqrt f\,|f'|\,dr
\ge\frac{2\sqrt{B'/A'}}{3M}f(U)^{3/2}=F(U).$$
Taking the infimum proves the all-path lower bound. For an explicit
prefactor, apply Corollary 2 directly to $\rho=(1-\delta)F$, rather than
estimating $d$ on the complementary set. Differentiation gives
$$A'|\nabla F|^2
=\frac{B'f_+}{M^2}|\nabla V|^2\le q_+.$$
Thus the margin on $\Sigma_\epsilon$ is $\theta_\delta\epsilon$,
$\rho\le R_F$ on its complement, and
$K_\rho\le e_0+(1-\delta)^2q_{\max}$. The full weighted mass is bounded
by $C_{\epsilon,\delta}$. On $\{f\ge s\}$ the weight is at least
$\exp[8(1-\delta)s^{3/2}/(3g^2M)]$, proving the tail. $\square$

For the periodic three-dimensional spatial cubic lattice each link is
in four plaquettes. The completeness relation yields
$|\nabla_\ell\operatorname{Re}\operatorname{tr}U_p|\le\sqrt{N/2}$
([the upper-bound note](lattice-gap-upper-bounds.md), Corollary 2,
proof passage). The triangle inequality and sum of squared link
components give
$$\|\nabla V\|_\infty\le4\sqrt{N/2}\sqrt{|\mathcal E|}
=2\sqrt{2N|\mathcal E|}=:M.$$
In other spatial dimensions or geometries the plaquette incidence must
be changed; this constant is specifically for three spatial dimensions.
With $P=|\mathcal P|=|\mathcal E|$ and $s=wP$, Proposition 3 becomes
$$\mathbb P_\Omega(f\ge wP)
\le\min\left\{1,\ C_{\epsilon,\delta}
\exp\left[-\frac{2\sqrt2(1-\delta)}{3}
\frac{w^{3/2}}{g^2\sqrt N}P\right]\right\}.$$
At fixed $g,N,\epsilon,\delta$, $R_F=O(P^{-1/2})$ and the displayed
prefactor is at most $O(P)$. Thus this is a genuine global extensive-tail
bound for fixed $w>0$. When $w$ is a fixed positive multiple of $N$,
the exponent per plaquette is of order $N/g^2$, correcting the earlier
$\sqrt N/g^2$ scaling. Coupling dependence of the prefactor must still
be retained in any weak-coupling limit.

For a fixed *total* excess $s=nv$ the exponent instead scales as
$$(nv)^{3/2}/(g^2\sqrt{NP}),$$
which vanishes as $P\to\infty$. A local event need not imply even this
total excess, since the complementary plaquettes can lower $V$.
The argument supplies no volume-uniform local estimate.

## 3. Comparison with the Euclidean weight

The Wilson action is
$$S_w=\frac{2N}{g_E^2}\sum_p\left(1-\frac1N
\operatorname{Re}\operatorname{tr}U_p\right)=\frac{2}{g_E^2}V.$$
An increase $\Delta V=nv$ multiplies its **unnormalized density** by
$e^{-2nv/g_E^2}$. This is an exact action-cost statement. Proposition 3
instead bounds an integrated ground-state probability of a global
excess with exponent proportional to $s^{3/2}/(g^2M)$ and the displayed
prefactor. Both expressions contain an inverse-square coupling factor;
this comparison neither identifies $g_E$ with $g$ in a continuum limit
nor proves equal local probabilities. Plaquettes share links, so a
product of plaquette action factors is not a product measure of
independent plaquette variables. Normalization and integration require
additional estimates even on the Euclidean side.

The original assertion that local large-field regions are exponentially
rare at the required rate in the Hamiltonian ground state is withdrawn.
The global estimate does not supply the local input sought in
[the typical-field note](typical-field-strength-window.md) or
[the flow-before-decimation note](flow-before-decimation.md).

## 4. Scope, excited states and the missing local input

The surviving statements are the weighted identity, the forbidden-set
estimate and the global integrated tail. At finite volume all
exponential moments of a bounded local plaquette potential are already
finite by compactness, for every finite rate. That fact supplies no
uniform control as the volume, cutoff or observable changes; the
original claim of useful local moments below a rate
$\lambda=2\sqrt{2v}/g^2$ is withdrawn.

For a normalized excited eigenfunction $\psi_j$ with dimensionless
energy $e_j$, positivity is unavailable: real excited eigenfunctions
orthogonal to $\Omega$ change sign. Nevertheless the identity holds as
$$A'\int|\nabla(e^\rho\psi_j)|^2d\mu
+\int(B'V-e_j-A'|\nabla\rho|^2)e^{2\rho}|\psi_j|^2d\mu=0.$$
For real eigenfunctions the proof is unchanged; for complex ones test
with $e^{2\rho}\overline{\psi_j}$ and take the real part. Corollary 2
then applies with $e_j$ and $|\psi_j|^2$, with its corresponding global
threshold and constants. It does not require taking $\log\psi_j$ or
assuming a positive excited state.

A superposition of eigenfunctions is not itself an eigenfunction.
For a whole finite-volume spectral subspace below $e_*$ one can choose
a common admissible weight relative to $B'V-e_*$ and bound its weighted
norm by summing the individual estimates: if its rank is $m$ and each
weighted eigenfunction norm squared is at most $C_*$, pointwise
Cauchy--Schwarz gives a bound $mC_*$ for any normalized superposition.
Compactness gives finite rank at fixed $e_*$. Neither the rank nor the
constants have been controlled uniformly in volume or cutoff here.
Merely replacing $e_0$ by the first excited energy $e_1$ does not prove
a uniform low-energy-subspace estimate.

No successful comparison with $e^{2t\|G\|_\infty}$, the flow-Jacobian
growth factor, follows from these global bounds. A local state-relative
estimate with the required uniformity remains a separate obligation.
The Gibbs-comparison attempt in
[the magnetic-energy identities note](magnetic-energy-identities.md),
§4 (full-read), has a threshold and prefactor determined by global
energy data; its failure to supply uniform local control is not a
proof that every possible local estimate is impossible. The
[transfer-measure note](ground-state-measure-transfer.md), §§1--2
(passages), describes a different route: any Euclidean estimate used
there must survive the temporal-continuum and vacuum limits with its
constants controlled. No such local estimate is established here.

## 5. Consequence for STATE

Keep this note as a finite-lattice global-energy result: Lemma 1,
Corollary 2 with explicit margins and prefactors, and Proposition 3's
all-path lower bound and integrated tail. The original local
per-plaquette rate, pointwise decay claim, local moment criterion and
claim to supply the Hamiltonian decimation input are withdrawn. The
[global/local correction](agmon-global-not-local.md) controls reuse;
a local energy or measure estimate uniform in volume and cutoff remains
an independent requirement. Excited-state identities survive with
$|\psi_j|^2$, but uniform spectral-subspace and refinement estimates do
not follow from them. No mass gap or continuum construction is claimed.
