# Series and parallel: where the gauge insertion law stops closing

**Result, 2026-09-26.** Halve one lattice direction of a heat-kernel
lattice gauge theory in $D$ dimensions. The step splits exactly into two
kinds of move. Faces containing the refined direction are cut in two;
these *series* moves integrate out exactly in every dimension, by the
heat-kernel convolution. Faces transverse to the refined direction
acquire a new parallel copy at doubled heat time; integrating out these
*parallel* insertions leaves the factor $\Psi$ of Proposition 1, the
partition function of a $(D-1)$-dimensional gauge theory on the inserted
mid-plane whose edges carry Brownian-bridge laws fixed by the coarse
field. There are $\binom{D-1}{2}$ transverse planes: none in $D=2$,
which is why two-dimensional Yang--Mills closes, one in $D=3$, three in
$D=4$.

What is proved about $\Psi$:

- *Free field* (Proposition 2): the defect against the coarse action is
  an exact negative semidefinite quadratic form, of relative size at most
  $a^2K^2/16+(Ga)^2/8$ on fields with transverse momenta up to $K$ and
  layer gradient $G$. It is the counterpart of Newton's $-F^2uvh/(8M)$
  ([refinement note](refinement-composition-and-limit.md), eq. (1)) and
  exactly the error of Migdal's bond moving.
- *Compact $U(1)$* (Propositions 3--4, Theorem 5): exact formulas for a
  cube and a mid-plane, and a proof that one step equals the free step up
  to an extensive error of density $e^{-\pi^2/(8\lambda_3a)}$ on the
  small-field set. This is a one-step estimate for the unperturbed action;
  stability under iteration remains open. The known massless fixed-coupling
  and massive fixed-Debye-mass limits require their separate continuum theorems.
- *Non-abelian groups* (Propositions 6--7): the bridge midpoint's
  curvature term is explicit for every compact group (for $SU(3)$ the
  averaged softening per cut face is $t_j|X_j|^2/512$), and the one-step
  inequality in Hypothesis P($\alpha$) of §4 holds for one cube conditional
  on the full normalized Laplace bounds in Proposition 7. Uniformity and
  stability under iteration remain to be established.

This answers the stop rule of the refinement note, §8, in its second
form: it gives the exact term that prevents closure, with an explicit
free-field estimate, and states the interacting estimate that remains.
The ingredients are established (heat-kernel convolution, Brownian
bridges, Gaussian integration); the decomposition and the exact
free-field defect are elementary, and no novelty is claimed for them
beyond their use here as the organizing comparison. Migdal's recursion
(1975) is the approximate form of the same series/parallel split, as
Kadanoff's notes describe it
([Kadanoff 1976](https://doi.org/10.1016/0003-4916(76)90066-X), metadata).

## 1. Heat times on an anisotropic lattice

Take a hypercubic lattice in $D$ dimensions with spacings
$a_1,\dots,a_D$, compact gauge group $G$ with the group metric of the
refinement note §5 ($-\Delta_G\chi_R=C_2(R)\chi_R$, $C_2(\mathbf3)=4/3$
for $SU(3)$), and heat kernel
$k_t=e^{t\Delta_G/2}$, $k_t(U)=\sum_Rd_R\chi_R(U)e^{-tC_2(R)/2}$.
Use the dimensionally explicit continuum action of the refinement note
§6,

$$\frac{S_E}{\hbar}=\frac1{4\lambda_D}\int F^a_{\mu\nu}F^a_{\mu\nu}\,d^Dx,
\qquad[\lambda_D]={\rm length}^{D-4},$$

so that $\lambda_D=\hbar g_{{\rm cl},D}^2$ contains $\hbar$. The
anisotropic heat-kernel action assigns to a plaquette $p$ in the plane
$(\mu\nu)$ the weight $k_{t_{\mu\nu}}(U_p)$ with

$$t_{\mu\nu}=\lambda_D\,\frac{a_\mu a_\nu}{\prod_{\rho\ne\mu,\nu}a_\rho}.
\tag{1}$$

*Derivation of (1).* For a smooth field, $U_p=\exp(a_\mu a_\nu
F_{\mu\nu}+O(a^3))$ and, for small $t$ away from the cut locus,
$-\log k_t(e^X)=|X|^2/(2t)+{\rm const}+O(t+|X|^2)$. Matching
$a_\mu^2a_\nu^2|F_{\mu\nu}|^2/(2t_{\mu\nu})$ to the continuum density
$(1/2\lambda_D)|F_{\mu\nu}|^2\prod_\rho a_\rho$ (the factor $1/2$
collects $F_{\mu\nu}$ and $F_{\nu\mu}$) gives (1). $\square$

The heat time is dimensionless. In $D=2$ it is $\lambda_2$ times the
face area, as in the refinement note; in $D=3$ the isotropic value is
$t=\lambda_3a$, the refinement parameter of that note's table; in $D=4$
it is $t=\lambda_4=g_{\rm lat}^2$, independent of $a$. Equation (1) is a
choice of regularization, the heat-kernel counterpart of the anisotropic
Wilson action; the theorems below concern it exactly. The matching holds in the small-field regime; under large anisotropy,
such as refining time alone, the transverse heat times grow and the
Hamiltonian limit requires exponential (Wilson-type) weights instead
([zero-spacing note](zero-spacing-any-action.md), §1). The halvings used
here change heat times by factors of two.

## 2. Halving one direction: series moves and a parallel insertion

Halve direction 1: $a_1\mapsto a_1/2$. By (1),

- a plaquette in a plane $(1\nu)$ has $t_{1\nu}\mapsto t_{1\nu}/2$, and
  each coarse $(1\nu)$ face is cut by a new edge into two fine faces;
- a plaquette in a plane $(jk)$ with $j,k\ne1$ has $t_{jk}\mapsto2t_{jk}$;
  the old $(jk)$ faces survive with doubled heat time, and a new
  $(jk)$ face appears in each mid-plane $x_1=(\ell+\tfrac12)a_1$, also at
  heat time $2t_{jk}$.

The new variables are the half-edges in direction 1 and the *mid-edges*
lying in the mid-planes. Each mid-edge in direction $j\ne1$ lies in
exactly one coarse face of the plane $(1j)$, which it cuts in two, and it
borders $2(D-2)$ mid-faces.

**Proposition 1 (exact pushforward).** Let $\mu'$ be the fine
heat-kernel measure and $p$ the projection multiplying half-edges. Then
$p_*\mu'$ has density, with respect to the product Haar measure on coarse
links,

$$\frac1{Z'}\prod_{f\ni1}k_{t_f}(U_f)\prod_{f\perp1}k_{2t_f}(U_f)\;
\Psi(U), \tag{2}$$

where $f\ni1$ ranges over coarse faces containing direction 1,
$f\perp1$ over the others, and

$$\Psi(U)=\int\prod_{g\ \rm mid}k_{2t_g}(m_{\partial g})
\prod_{e\ \rm mid}\beta_e(dm_e\,|\,U). \tag{3}$$

Here $m_{\partial g}$ is the ordered product of mid-edge variables around
the mid-face $g$, and $\beta_e$ is the midpoint law of the Brownian
bridge on $G$ of duration $t_{1j}$ determined by the coarse face that
$e$ cuts: if the two halves of that face have holonomies $P_em_e^{-1}$
and $m_eQ_e$, with $P_eQ_e=U_f$,

$$\beta_e(dm\,|\,U)=\frac{k_{t_{1j}/2}(P_em^{-1})\,
k_{t_{1j}/2}(mQ_e)}{k_{t_{1j}}(U_f)}\,dm. \tag{4}$$

*Proof.* At each new vertex on a direction-1 edge, only the two
half-edges and the incident mid-edges meet. Changing variables to
(coarse product, upper half) and using Haar invariance, the gauge
transformation at that vertex sets the upper half-edge to the identity
without changing the integral; the lower half-edge becomes the coarse
link. The half-faces then have the holonomies displayed, with $P_e$,
$Q_e$ built from coarse links only. Multiply and divide by
$k_{t_{1j}}(U_f)$ for each cut face. By the convolution identity, eq. (9)
of the refinement note, each $\beta_e$ is a probability measure. Fubini
gives (2)--(3). $\square$

**The dimension count.** Refining one direction produces parallel
insertions in the $\binom{D-1}{2}$ planes transverse to it: zero for
$D=2$, one for $D=3$, three for $D=4$. With no transverse plane, $\Psi=1$
and (2) is the exact consistency (7) of the refinement note, recovering
its §5. An isotropic dyadic step is $D$ successive directional halvings.
By (1) the heat times change as follows:

| $D$ | one directional halving | full isotropic step | parallel planes per halving |
| --- | --- | --- | --- |
| 2 | $t\mapsto t/2$ | $t\mapsto t/4$ (area) | 0 |
| 3 | $t_{1\nu}/2$, $2t_{23}$ | $t\mapsto t/2$ | 1 |
| 4 | $t_{1\nu}/2$, $2t_{jk}$ | $t\mapsto t$ | 3 |

The last column locates the whole renormalization problem. The middle
column is the classical scaling: superrenormalizable in $D=3$, where the
heat time halves per step, and marginal in $D=4$, where it returns to
itself and any running must come from $\Psi$.

The structure matches Newton's insertion. There the new time splits one
cell in series and the elimination leaves the endpoint-independent
scalar $-F^2uvh/(8M)$; here the series moves close with no remainder
(the heat kernel is already the exact propagator, the counterpart of
$U_h$ rather than $Q_h$), and the parallel insertion leaves $\Psi$.
A Wilson action would also leave series remainders, as $Q_h$ does.

## 3. The free field: the parallel defect in closed form

Take $G=\mathbb R^n$ with the Euclidean metric (the Gaussian limit of a
compact group of dimension $n$; $n=8$ for $SU(3)$) and $D=3$. Then
$k_t(x)=(2\pi t)^{-n/2}e^{-|x|^2/(2t)}$, and $\beta_e$ is Gaussian with
mean $(P_e-Q_e)/2$ in additive notation and covariance
$(t_{1j}/4)\,I_n$, independent of the coarse data. Put the lattice on a
torus with $N_2\times N_3$ transverse sites and $N_1$ layers. Write
$\Phi_\ell(x)$ for the flux of the old $(23)$ face at layer $\ell$ and
transverse site $x$, and $\hat\Phi_\ell(k)$ for its unitary discrete
Fourier transform in $(x_2,x_3)$, with
$s_j=\sin(k_ja_j/2)$ and

$$v(k)=t_{12}\,s_3^2+t_{13}\,s_2^2 .$$

On a torus the transverse zero mode of a lattice curl vanishes, so
$k\ne0$ throughout. All statements concern gauge-invariant functions,
which depend on the links only through the fluxes; the non-compact
gauge orbits drop out with the normalization constants.

**Proposition 2 (exact free-field parallel defect).** In this Gaussian
theory, the pushforward (2) is the coarse heat-kernel measure multiplied
by $e^{-\mathcal D}$ (up to a constant), with

$$\mathcal D=-\sum_\ell\sum_{k\ne0}\left[
\frac{v(k)\bigl(|\hat\Phi_\ell|^2+|\hat\Phi_{\ell+1}|^2\bigr)}
{8t_{23}\bigl(2t_{23}+v(k)\bigr)}
+\frac{|\hat\Phi_\ell-\hat\Phi_{\ell+1}|^2}{8\bigl(2t_{23}+v(k)\bigr)}
\right]\ \le\ 0. \tag{5}$$

*Proof.* (i) The mean mid-edge configuration interpolates linearly
between layers $\ell$ and $\ell+1$; the direction-1 links enter it as a
lattice gradient, which the curl annihilates. Hence the mean mid-face
flux is exactly $(\Phi_\ell+\Phi_{\ell+1})/2$. (ii) The fluctuation of
the mid-face flux is the lattice curl of independent edge noises with
variances $t_{12}/4$ (direction 2) and $t_{13}/4$ (direction 3). Its
Fourier covariance is
$(t_{12}/4)|1-e^{ik_3a_3}|^2+(t_{13}/4)|1-e^{ik_2a_2}|^2=v(k)$, diagonal
in $k$. (iii) For Gaussian $\eta$ of variance $v$,
$E\,e^{-|\bar\Phi+\eta|^2/(2\sigma^2)}\propto
e^{-|\bar\Phi|^2/(2(\sigma^2+v))}$; with $\sigma^2=2t_{23}$,
$-\log\Psi=\sum_{\ell,k}|\hat\Phi_\ell+\hat\Phi_{\ell+1}|^2/
(8(2t_{23}+v))+{\rm const}$. (iv) The old $(23)$ faces contribute
$\sum|\hat\Phi_\ell|^2/(4t_{23})$, the coarse target is
$\sum|\hat\Phi_\ell|^2/(2t_{23})$, and the cut faces return
$k_{t_{1j}}(U_f)$ exactly. Subtract, and use
$|A+B|^2=2|A|^2+2|B|^2-|A-B|^2$. $\square$

At zero transverse momentum and constant flux in $\ell$, the two old and
new faces at heat time $2t_{23}$ combine in parallel to one face at
$t_{23}$, as conductances do. The defect measures the two departures:
transverse lattice momentum ($v>0$) and variation between layers.

**Corollary (size of one step).** On an isotropic coarse lattice
($a_j=a$, $t_{\mu\nu}=t=\lambda_3a$), suppose $\hat\Phi_\ell$ is
supported on $|k|\le K$ and
$\sum_\ell\|\Phi_\ell-\Phi_{\ell+1}\|^2\le(Ga)^2\sum_\ell\|\Phi_\ell\|^2$,
with $\|\cdot\|$ the $\ell^2$ norm over transverse sites. Then

$$|\mathcal D|\le\Bigl(\frac{a^2K^2}{16}+\frac{(Ga)^2}{8}\Bigr)
\sum_\ell\frac{\|\Phi_\ell\|^2}{2t}. \tag{6}$$

*Proof.* Use $2t+v\ge2t$ and $v\le ta^2|k|^2/4$ in (5). $\square$

For a smooth field, $\Phi=a^2F_{23}$ and the right side of (6) is
$a^2(K^2/16+G^2/8)$ times the continuum magnetic action
$(1/2\lambda_3)\int|F_{23}|^2d^3x$: a dimension-six correction with
coefficient $a^2$. At fixed physical $K$ and $G$ the relative defects
along $a_n=2^{-n}a_0$ are summable, which is the free-field instance of
the refinement note's criterion (12), in a norm on Gaussian actions
rather than total variation. Two cautions keep this honest. After one
step the effective action is (2) with $\mathcal D$, so the next step
starts from a slightly different action; the free field is controlled
exactly because every stage is Gaussian, and its blocked actions
should converge to a Gaussian fixed point. That fixed point goes back to
[Bell and Wilson (1975)](https://doi.org/10.1103/PhysRevB.11.3431)
(metadata), and the perfect-action programme of
[Hasenfratz and Niedermayer (1994)](https://doi.org/10.1016/0550-3213(94)90261-5)
(metadata) develops it for asymptotically free models with a smeared
blocking; for the product blocking used here the convergence is
asserted, not proved. And (6) holds for smooth coarse data; typical lattice fields
at fixed $t$ are rough, so (6) states the irrelevance of the defect,
while the measure-level estimate needs the whole quadratic form (5).

**Migdal's bond moving, read exactly.** Moving each mid-face onto the
old face of layer $\ell$ multiplies two Gaussian weights at $2t_{23}$
into one at $t_{23}$, which is the coarse target. So in the Gaussian
theory $\mathcal D$ is exactly the error of the bond-moving step, and (5)
splits it into its noise part ($v$) and its displacement part
($\Phi_\ell-\Phi_{\ell+1}$). Tomboulis's attempt to bound the exact
decimation between Migdal--Kadanoff-type approximations
([arXiv:0707.2179](https://arxiv.org/abs/0707.2179), abstract; not
established as a theorem, see [what-would-unblock](what-would-unblock.md))
worked on the same parallel step.

**The comparison with Newton.** Both eliminations complete a square,
and both lower the action. Newton's defect is a constant, removed by one
cubic counterterm, after which the cell law closes exactly. The
free-field defect is an irrelevant quadratic form; no finite set of
nearest-neighbour counterterms removes it, and the closed object is the
fixed point in the space of all quadratic actions. In the interacting
theory $\Psi$ is non-Gaussian.

## 4. The non-abelian parallel move in $1+2$ dimensions

For compact $G$, (3) says: **$\Psi(U)$ is the partition function of a
two-dimensional heat-kernel lattice gauge theory on the mid-planes, at
heat time $2t_{23}$, in which each edge is distributed by the bridge law
$\beta_e(\cdot\,|\,U)$ instead of Haar measure.** Two limits are exactly
soluble. As $t_{1j}\to\infty$ the bridge laws tend to Haar measure, the
mid-plane is the exactly soluble two-dimensional theory of the refinement
note §5, and $\Psi$ is a constant: the old transverse faces stay at
heat time $2t_{23}$. As $t_{1j}\to0$ the bridge laws concentrate at the
geodesic interpolation and $\Psi$ is the product of mid-face weights on
the interpolated holonomies, a classical evaluation, like Newton's
$z_*$. Between those limits, two-dimensional exact solvability fails,
because it rests on Haar invariance of every edge.

Relative to the Gaussian computation of §3, four terms appear, with the
orders that power counting assigns them at $t=\lambda_3a\ll1$ (labelled
as power counting; proving them is the content of the hypothesis below):

- **N1, interpolation.** The mid-face holonomy of the geodesic
  interpolation (the $t_{1j}\to0$ bridge) differs from the abelian
  average by Baker--Campbell--Hausdorff commutators; in the axial gauge
  realized by the mid-vertex gauge fixing the leading term is
  $-\tfrac18a^4[F_{12},F_{13}]$ in $\log U_g$. In the action this is a
  dimension-six operator, $O(a^2)$ relative, like (6).
- **N2, bridge shape.** The bridge law depends on the coarse face
  holonomy through the group's curvature (the Jacobian of the exponential
  map in the small-$t$ heat kernel). Relative size $O(t)=O(\lambda_3a)$;
  gauge invariance allows it to shift the coupling and the vacuum energy
  only, at leading order.
- **N3, non-Gaussian fluctuation.** The mid-face holonomy is a
  non-commutative product of noisy edges; the connected corrections to
  $-\log\Psi$ are $O(t)$ relative and local.
- **N4, large fields.** Bridges that wind around the group (the image
  terms of the heat kernel near the cut locus) contribute
  $O(e^{-c/t})$ per face for coarse fluxes a fixed distance from the cut
  locus, and $O(1)$ at it (Proposition 3 below gives the rate); the small-field
  split of Hypothesis P($\alpha$) handles them.

**Correction, 2026-09-26 (referee check).** The first version of the
hypothesis below bounded $-\log\Psi$ itself and demanded large-field
suppression of $\Psi$; the free field violates the first (it needs
$\delta_t=\frac12$) and Proposition 3 the second. The version below
bounds the log-ratio $\mathcal D$ of (2) against the coarse density.

**Hypothesis P($\alpha$) (one parallel step, $D=3$).** Fix
$\delta\in(0,\frac14)$. Let

$$\mathcal D(U)=-\log\Psi(U)-\sum_{f\perp1}\log
\frac{k_{2t_{23}}(U_f)}{k_{t_{23}}(U_f)},\qquad
S_{\mu\nu}(U)=\sum_{f\in(\mu\nu)}\frac{|\log U_f|^2}{2t_{\mu\nu}},$$

so that $p_*\mu'$ is the coarse heat-kernel density times $e^{-\mathcal D}$
(for the free field, $\mathcal D$ is (5)). There exist $\alpha>2\delta$,
$t_0>0$, $C<\infty$, a local quadratic form $\mathcal D_0$ in
$\{\log U_p\}$ (the form (5), with $t_{23}$ possibly renormalized by
$O(t)$), and for each $t=\lambda_3a\le t_0$ numbers $c_{\rm vac}(t)$ and
coupling shifts $\delta_t^{\mu\nu}$, one per plane, with
$|\delta_t^{\mu\nu}|\le Ct$, such that on the small-field set
$\{|\log U_p|\le t^{1/2-\delta}\ \text{for all }p\}$

$$\bigl|\mathcal D(U)-\mathcal D_0(U)-c_{\rm vac}N_{\rm cells}
-\textstyle\sum_{\mu<\nu}\delta_t^{\mu\nu}S_{\mu\nu}(U)\bigr|
\le C\,t^{\alpha}\sum_p\bigl(1+|\log U_p|^2/t\bigr),$$

the sum running over all coarse plaquettes. The same statement is
required for heat-kernel actions perturbed by local terms of the size
on the right, so that it can be iterated. No large-field clause on
$\Psi$ is needed: $\Psi\le\prod_gk_{2t_g}(1)$, and the explicit factors
of (2) suppress each plaquette outside the small-field set by
$e^{-t^{-2\delta}/4}$, up to a factor $t^{-n/2}$ per cell. Free-field
check: $\mathcal D=\mathcal D_0$, all $\delta_t^{\mu\nu}=0$, every
$\alpha$. (Amended the same night: the first version allowed a shift of
the transverse coupling only; the one-loop determinant below shifts the
couplings of the cut faces as well.)

(Amended 2026-09-27, from the [SU(2) mid-plane note](su2-midplane-order-t.md)
and its referee: on periodic planes P($\alpha$) is required for plane sizes
$\min_jN_j\ge c_0/t$, fixed physical size; at fixed $N$ with $t\to0$ a
flat-holonomy winding determinant of the massive mid-plane modes is of
order one and violates the literal statement.)

**The compact abelian cube isolates N4 exactly.** Take $G=U(1)$ with
$k_t(\theta)=\sum_{n\in\mathbb Z}e^{-tn^2/2}e^{in\theta}$ (the Villain
weight), and refine a single cube: one mid-face at heat time $t_m$,
bounded by four mid-edges $m_j$ with orientations $\sigma_j=\pm1$, each
cutting a side face of heat time $t_j$ whose halves have angles
$p_j-m_j$ and $m_j+q_j$. Put $\phi_j=p_j+q_j$ (the side-face flux, any
real representative), $\bar\Phi=\sum_j\sigma_j(p_j-q_j)/2$ (the
interpolated mid-face flux, with the same representatives), and

$$\rho_t(\phi)=\frac{\sum_{w\in\mathbb Z}(-1)^we^{-(\phi-2\pi w)^2/(2t)}}
{\sum_{w\in\mathbb Z}e^{-(\phi-2\pi w)^2/(2t)}}\in[-1,1].$$

**Proposition 3 (exact $U(1)$ cube).** With $T=t_m+\tfrac14\sum_jt_j$,

$$\Psi=\sum_{n\ {\rm even}}e^{-Tn^2/2}e^{in\bar\Phi}
+\Bigl(\prod_{j=1}^4\rho_{t_j}(\phi_j)\Bigr)
\sum_{n\ {\rm odd}}e^{-Tn^2/2}e^{in\bar\Phi}. \tag{7}$$

As every $\rho_{t_j}(\phi_j)\to1$, $\Psi\to k_T(\bar\Phi)$. For
$|\phi_j|\le\pi$ and $t_j\le1$,
$0\le1-\rho_{t_j}(\phi_j)\le5\,e^{-2\pi(\pi-|\phi_j|)/t_j}$.

*Proof.* The bridge numerator for $E\,e^{inm}$ is
$\sum_{r}e^{-t(r^2+(r-n)^2)/4}e^{irp}e^{i(r-n)q}$ by character
orthogonality, and $r^2+(r-n)^2=2(r-n/2)^2+n^2/2$. For even $n$ the
shift $r\mapsto r+n/2$ reproduces the denominator $k_t(\phi)$, giving
$E\,e^{inm}=e^{-tn^2/8}e^{in(p-q)/2}$. For odd $n$ the shift is by a
half-integer and leaves the ratio
$\sum_se^{-t(s-\frac12)^2/2}e^{i(s-\frac12)\phi}/\sum_se^{-ts^2/2}e^{is\phi}$,
which Poisson summation turns into $\rho_t(\phi)$. The four $m_j$ are
independent, so $E\,k_{t_m}(\sum_j\sigma_jm_j)$ is the sum over $n$ of
$e^{-t_mn^2/2}\prod_jE\,e^{in\sigma_jm_j}$, which is (7). For the
bound, write $G_w=e^{-(\phi-2\pi w)^2/(2t)}$; then
$1-\rho=2\sum_{w\ \rm odd}G_w/\sum_wG_w\le2\sum_{w\ \rm odd}G_w/G_0$.
For $|\phi|\le\pi$ the odd term nearest $\phi$ gives
$e^{-2\pi(\pi-|\phi|)/t}$, the opposite one at most the same, and the
terms $|w|\ge3$ are smaller by $e^{-12\pi^2/t}$; for $t\le1$ the total
is below $5e^{-2\pi(\pi-|\phi|)/t}$. $\square$

Equation (7) displays the parallel move for one cube with N1--N3 absent
(the group is abelian and flat): the mid-face weight is the heat kernel
at the *softened* heat time $t_m+\frac14\sum t_j$, the isolated-cube
counterpart of the noise $v(k)$ in (5) (indeed
$\frac14\sum_jt_j=(t_{12}+t_{13})/2$ is the Brillouin-zone average of
$v$), evaluated at the interpolated flux. The only departure is the odd-charge factor, which differs from 1
only where a side-face flux approaches the cut locus $|\phi|=\pi$, where
its bridge midpoint becomes bimodal. That is N4, exactly, with the rate
$e^{-2\pi(\pi-|\phi|)/t}$. At the cut locus itself, $\rho=0$ and
$\Psi=\frac12[k_T(\bar\Phi)+k_T(\bar\Phi+\pi)]$, at most a factor 2
below its small-field value: large side fluxes are suppressed by the
explicit factors $k_{t_{1j}}(U_f)$ of (2), and $\Psi$ adds no suppression.

**The whole $U(1)$ mid-plane.** The same computation extends to a full
mid-plane of $N$ mid-faces $g$ and mid-edges $e$, with $\delta$ the
coboundary from faces to edges, $(\delta n)_e$ the signed sum of $n_g$
over the two mid-faces at $e$, $t_e$ the heat time of the side face that
$e$ cuts, and

$$C=2t_{23}\,I+\delta^{\sf T}{\rm diag}(t_e/4)\,\delta ,$$

a positive definite $N\times N$ matrix. $\bar\Phi_g$ is the interpolated
flux of $g$ and $\phi_e$ the flux of the side face cut by $e$.

**Proposition 4 (exact $U(1)$ mid-plane).**

**Referee verdict, 2026-09-27: ACCEPT.** Equations (8)--(9) and the independent parity-mixture proof have the stated normalized-Haar constants.

$$\Psi=\sum_{n\in\mathbb Z^N}e^{-\frac12n^{\sf T}Cn}\,e^{in\cdot\bar\Phi}
\prod_{e:\,(\delta n)_e\ {\rm odd}}\rho_{t_e}(\phi_e). \tag{8}$$

If every $\rho_{t_e}(\phi_e)$ is replaced by $1$, Poisson summation gives
the vortex form

$$\Psi_1(\bar\Phi)=\frac{(2\pi)^{N/2}}{\sqrt{\det C}}
\sum_{w\in\mathbb Z^N}
e^{-\frac12(\bar\Phi+2\pi w)^{\sf T}C^{-1}(\bar\Phi+2\pi w)}. \tag{9}$$

*Proof.* The proof of Proposition 3 shows that each bridge midpoint is
$m_e=\bar m_e+\pi s_e+\xi_e$ modulo $2\pi$, with $\bar m_e$ the
interpolation, $s_e\in\{0,1\}$ with $P(s_e=1)=(1-\rho_e)/2$, and
$\xi_e$ Gaussian of variance $t_e/4$, all independent. (The bridge
density is a product of two wrapped Gaussians; its two winding numbers
combine into a total, which carries the weight
$e^{-(\phi_e+2\pi W)^2/(2t_e)}$, and a relative one, which shifts the
centre by $\pi W$.) Expand each mid-face weight
$k_{2t_{23}}(\cdot)=\sum_{n_g}e^{-t_{23}n_g^2}e^{in_g(\cdot)}$. The
Gaussian average gives $e^{-\sum_et_e(\delta n)_e^2/8}$, and the average
over $s_e$ gives $1$ for even $(\delta n)_e$ and $\rho_e$ for odd; this
is (8). For (9), apply the Poisson summation formula on $\mathbb Z^N$.
$\square$

For one mid-face, (8) is (7). With isotropic coarse heat times
($t_e=t_{23}=t$), $C=2t(I+L/8)$ with $L=\delta^{\sf T}\delta$ the
Laplacian of the dual lattice, whose spectrum lies in $[0,8]$. In
Fourier variables $C=2t+v(k)$, the covariance of Proposition 2, so the
$w=0$ term of (9) is the free field exactly. The vortices $w\ne0$ are
the compact correction, a periodic Gaussian of the Villain type
([Banks, Myerson and Kogut 1977](https://doi.org/10.1016/0550-3213(77)90129-8),
metadata, for the duality in abelian lattice gauge theories).

**Corollary (vortex bound).** In the isotropic case, write $\Psi_1^{(0)}$
for the $w=0$ term of (9) and assume $\|\bar\Phi\|_\infty<\pi/2$. Then

$$0\le\log\frac{\Psi_1(\bar\Phi)}{\Psi_1^{(0)}(\bar\Phi)}
\le\frac{2N\,e^{-c/t}}{1-e^{-c/t}},\qquad
c=\pi\Bigl(\frac\pi2-\|\bar\Phi\|_\infty\Bigr). \tag{10}$$

**Referee verdict, 2026-09-27: ACCEPT.** The M-matrix argument applies to the periodic square mid-plane used here; taking the logarithm of the product bound gives (10).

*Proof.* $I+L/8$ is a symmetric M-matrix with row sums $1$, so its
inverse has nonnegative entries and row sums $1$. Hence
$\|C^{-1}\|_{\infty\to\infty}=1/(2t)$, and $C^{-1}\ge1/(4t)$ because
$L\le8$. For integer $w$, $\|w\|_2^2\ge\|w\|_1$. The exponent of the
$w$ term minus that of the $w=0$ term is
$-\frac12(2\pi w)^{\sf T}C^{-1}(2\pi w)-2\pi w^{\sf T}C^{-1}\bar\Phi
\le-\pi^2\|w\|_1/(2t)+\pi\|w\|_1\|\bar\Phi\|_\infty/t=-c\|w\|_1/t$. Every
term is positive, and $\sum_{w\ne0}e^{-c\|w\|_1/t}
=(1+2e^{-c/t}/(1-e^{-c/t}))^N-1$. $\square$

The bound is extensive with density $O(e^{-c/t})$ per mid-face, the form
of error that Hypothesis P($\alpha$) allows, for every $\alpha$. The
parity factors are handled by the same device, which completes the
$U(1)$ step.

**Correction (GPT-6 Astra referee), 2026-09-27 — REFINE:** use coarse-cube Bianchi identities for the lifts, retain harmonic flux sectors, and claim only the unperturbed one-step part of P($\alpha$).

**Theorem 5 (unperturbed $U(1)$ one-step estimate).** Take $G=U(1)$, $D=3$, an
isotropic coarse lattice with $t=\lambda_3a$, one halving of direction 1,
and a coarse configuration in the small-field set: every coarse
plaquette angle, taken in $(-\pi,\pi]$, has modulus at most
$\varepsilon=t^{1/2-\delta}$, with $3\varepsilon\le\pi/8$ and
$e^{-\pi^2/(16t)}\le\frac13$. Use these principal values for the
coarse fluxes and choose the interpolated flux representative modulo
$2\pi$ as $\bar\Phi_g=(\Phi_\ell+\Phi_{\ell+1})_g/2$. Then

$$-10\,N\,e^{-2\pi(\pi-\varepsilon)/t}\ \le\
\log\Psi-\log\Psi_1^{(0)}(\bar\Phi)\ \le\
\frac{2N\,e^{-\pi^2/(8t)}}{1-e^{-\pi^2/(8t)}},$$

where $\Psi_1^{(0)}(\bar\Phi)=(2\pi)^{N/2}(\det C)^{-1/2}
e^{-\frac12\bar\Phi^{\sf T}C^{-1}\bar\Phi}$ is exactly the free-field
parallel Gaussian integral. On the sector with zero total principal
transverse flux in each periodic layer, $\mathcal D$ equals (5) plus a
constant, up to an error at most $C_0Ne^{-\pi^2/(8t)}$ with $C_0$ absolute.
On other sectors use the same real quadratic calculation including its
harmonic ($k=0$) flux. Thus the unperturbed estimate in P($\alpha$) holds
with $\delta_t=0$ for every $\alpha$; its perturbed-action stability clause
requires a further proof.

*Proof.* (i) Representatives. Formula (8) is $2\pi$-periodic in each
$\bar\Phi_g$ and invariant under the joint change of lifts
($\phi_e\mapsto\phi_e+2\pi$ flips $\rho_e$ and shifts the adjacent
$\bar\Phi_g$ by $\pi$), so any consistent lifts may be used. Take
principal $\phi_e$ by changing the midpoint lifts together with the parity
weights. The boundary identity for a coarse cube gives
$\sum_{e\in\partial g}\sigma_e\phi_e=\Phi_{\ell+1}-\Phi_\ell+2\pi n$.
The absolute value of the difference of the six principal face terms is
at most $6\varepsilon<2\pi$, hence $n=0$. Since
$\bar\Phi_g\equiv\Phi_{\ell+1}-\frac12\sum_e\sigma_e\phi_e\pmod{2\pi}$,
its small representative is the asserted average and has modulus at most
$\varepsilon$. This uses only coarse data; the fluctuating half-cell
faces have no assumed smallness. Global torus flux can still be nonzero.
(ii) Mixture form. By the proof of Proposition 4,
$\Psi=E_s\,\Psi_1(\bar\Phi+\pi\delta^{\sf T}s)$ with independent
$s_e\in\{0,1\}$, $P(s_e=1)=q_e=(1-\rho_e)/2\le\frac52
e^{-2\pi(\pi-\varepsilon)/t}$ by Proposition 3.
(iii) Lower bound. Every $\Psi_1$ is positive, so
$\Psi\ge\prod_e(1-q_e)\,\Psi_1(\bar\Phi)\ge\prod_e(1-q_e)\,
\Psi_1^{(0)}(\bar\Phi)$; there are $2N$ mid-edges and
$\log(1-q)\ge-2q$ for $q\le\frac12$.
(iv) Upper bound, uniform in $s$. For $c=\delta^{\sf T}s$, the terms of
(9) at $\bar\Phi+\pi c$ are indexed by $u=c+2w$, the integer vectors
congruent to $c$ modulo 2. Relative to the $w=0$ term at $\bar\Phi$ the
exponent is
$-\pi u^{\sf T}C^{-1}\bar\Phi-\frac12\pi^2u^{\sf T}C^{-1}u
\le-c'\|u\|_1/t$, with $c'=\frac\pi2(\frac\pi4-\|\bar\Phi\|_\infty)
\ge\pi^2/16$, by the two matrix facts of the Corollary and
$\|u\|_2^2\ge\|u\|_1$. Summing coordinatewise,
$\Psi_1(\bar\Phi+\pi c)/\Psi_1^{(0)}(\bar\Phi)\le A_0^{N-k}A_1^k\le A_0^N$,
where $k$ is the number of odd entries of $c$,
$A_0=1+2e^{-2c'/t}/(1-e^{-2c'/t})$ and
$A_1=2e^{-c'/t}/(1-e^{-2c'/t})\le A_0$ under the stated condition on $t$.
Average over $s$ and use $\log A_0\le2e^{-2c'/t}/(1-e^{-2c'/t})$.
In fact, writing $r=e^{-c'/t}$, $A_0-A_1=(1-r)/(1+r)\ge0$
for every $t>0$; the uniform-in-$s$ bound needs no further restriction.
(v) The old transverse faces. $\log[k_{2t}(\theta)/k_t(\theta)]$ for
Villain weights equals $\theta^2/(4t)+\frac12\log\frac12$ up to the
one-dimensional vortex corrections, at most
$3e^{-2\pi(\pi-\varepsilon)/(2t)}$ per face for $|\theta|\le\varepsilon$
by the same Poisson estimate; this is where $e^{-\pi^2/(8t)}$ dominates.
Collect (iii)--(v) with the definition of $\mathcal D$. $\square$

This is the first rung of the ladder completed as a theorem: for the
compact abelian group, one directional step of the three-dimensional
refinement equals the free-field step of Proposition 2 up to an extensive
error of density $e^{-\pi^2/(8\lambda_3a)}$ on the small-field set. It
concerns the heat-kernel action; iterating it requires the same estimate
for heat-kernel actions perturbed by the defect, which is the stability
clause of P($\alpha$). The non-abelian terms N1--N3 are absent here, so
Theorem 5 tests the large-field and representative bookkeeping, and
leaves the curvature and commutator terms to the $SU(2)$ cube.

**What survives: compact $U(1)$ in three dimensions.** This theory is
the proved example of a lattice gap that the fixed-coupling refinement
removes. Göpfert and Mack prove a nonzero string tension for all
couplings of the Villain theory, bounded below through a Debye mass
$m_D>0$ (the monopole mechanism of
[Polyakov 1977](https://doi.org/10.1016/0550-3213(77)90086-4), metadata),
and establish a continuum limit $a\to0$ at fixed physical $m_D$ that is a
free scalar field of mass $m_D$, with string tension divided by $m_D^2$
diverging in that limit
([Göpfert--Mack 1982](https://doi.org/10.1007/BF01961240), abstract as
indexed; publisher abstract checked 2026-09-27). Gross proves that at
fixed physical coupling the Villain theory converges to the massless free
electromagnetic field; his Wilson-action statement concerns the electric sector
([Gross 1983](https://doi.org/10.1007/BF01210842), publisher abstract).

**Correction (GPT-6 Astra referee), 2026-09-27 — REFINE:** the source results have different scalings and sectors; a one-step upper bound alone establishes neither continuum convergence nor the monopole density.

In a fixed physical box the Theorem 5 bound is of order
$(L/a_n)^2e^{-\pi^2/(8t_n)}$ per mid-plane and
$(L/a_n)^3e^{-\pi^2/(8t_n)}$ over all planes. At $t_n=\lambda_3a_n$
its tail vanishes and is summable. Turning this into convergence needs
iteration stability and large-field probability control. Göpfert--Mack's
fixed-$m_D$ trajectory instead has logarithmically decreasing $t_n$;
their Debye formula supplies its normalization. The bound's constant
$\pi^2/8$ cannot determine the error's actual order or the monopole density
on that trajectory.

In four dimensions [Driver 1987](https://doi.org/10.1007/BF01212424)
(publisher abstract) proves convergence on the current sector to a
renormalized free electromagnetic field for general energy functions at
sufficiently large inverse coupling. For the Wilson energy he obtains
convergence at arbitrary coupling by an appropriate Gibbs-state choice,
and state independence away from at most countably many coupling values.
The sector and state qualifications matter. These results motivate the
comparison with the expected nonabelian three-dimensional gap
$C_3\hbar c\lambda_3$; locating that gap in particular N1--N3 terms needs
infrared control beyond the present ultraviolet estimate.

For $SU(2)$ and
$SU(3)$ the bridge expectations $E\,R(m_j)$ are matrices, and the
isolated cube is where N2 and N3 first appear.

**The $SU(2)$ bridge midpoint.** In the group metric of §1, $SU(2)$ is
the three-sphere of radius 2 (curvature $\frac14$), with cut locus at
geodesic distance $2\pi$ and $|\rho|^2=\frac14$. Poisson summation of the
character series gives the exact kernel

$$k_t(e^X)=e^{t/8}\sqrt{8\pi}\,t^{-3/2}\sum_{w\in\mathbb Z}
\frac{\theta-4\pi w}{\sin(\theta/2)}\,e^{-(\theta-4\pi w)^2/(2t)},
\qquad\theta=|X|, \tag{11}$$

with respect to normalized Haar measure; the $w=0$ term is the Gaussian
with the Jacobian $(\theta/2)/\sin(\theta/2)$, and $e^{t/8}=e^{t|\rho|^2/2}$.
For a cut side face, left-translate so that the bridge runs from $e$ to
$e^X$, $d=|X|<2\pi$, and write the midpoint as $m=m_*e^{\xi}$ with
$m_*=e^{X/2}$.

**Proposition 6 ($SU(2)$ midpoint: structure and leading covariance).**

**Correction (GPT-6 Astra referee), 2026-09-27 — REFINE:** the covariance is accepted; the representation formula is a fixed-representation expansion through order $t$, and the logarithm uses its almost-everywhere principal branch.

(a) Exactly, $E\,D^J(m)=D^J(m_*)\Lambda^J$ with $\Lambda^J$ real and
diagonal in the weight basis of the axis $\hat X$, and all odd moments of
$\xi$ vanish. (b) As $t\to0$, uniformly for $d\le d_0<2\pi$, $\xi$ is
Gaussian to leading order with covariance

$$\frac t4\,{\rm diag}\Bigl(1,\frac1{h(d)},\frac1{h(d)}\Bigr),\qquad
h(d)=\frac d4\cot\frac d4,$$

in the frame (axis, two transverse directions), so that

$$\Lambda^J_{\mu\mu}=1-\frac t8\Bigl[\mu^2
+\frac{J(J+1)-\mu^2}{h(d)}\Bigr]+O_J(t^2).$$

Here $J$ is fixed and $d\le d_0<2\pi$. The exponential of the displayed
order-$t$ term is equivalent at this accuracy; noncommuting representation
generators prevent treating it as an exact Gaussian characteristic function.

*Proof.* (a) The geodesic symmetry $g\mapsto m_*g^{-1}m_*$ is an isometry
that exchanges the endpoints, so it preserves the bridge law, and in
normal coordinates at $m_*$ it is $\xi\mapsto-\xi$. Conjugation by the
one-parameter group $e^{sX}$ fixes both endpoints and $m_*$, so
$\Lambda^J$ commutes with it and is diagonal in the axis basis; the
symmetry gives $\Lambda^J=(\Lambda^J)^\dagger$. (b) By (11), off the image
terms (which are $O(e^{-c/t})$ for $d\le d_0$), the bridge density is
$e^{-(d(e,m)^2+d(m,e^X)^2)/t}$ times smooth factors. On a space of
constant curvature $\kappa$, the Hessian of $\frac12d(p,\cdot)^2$ at
distance $r$ is 1 radially and $r\sqrt\kappa\cot(r\sqrt\kappa)$
transversally. At the midpoint $r=d/2$, $\kappa=\frac14$, so the exponent
has Hessian $(4/t)\,{\rm diag}(1,h,h)$; Laplace's method gives the
covariance. Expanding $D^J(e^\xi)$ through second order and using the
vanishing odd moments gives the fixed-$J$ order-$t$ formula. $\square$

**Correction (GPT-6 Astra referee), 2026-09-27 — REFINE:** change the curvature sign, allow weight multiplicities, restrict to a unique minimizing geodesic, and use the Killing form for nonsimple groups.

**Any compact connected group, and $SU(3)$.** The local covariance
argument applies with a bi-invariant metric and $X$ in a compact subset
of the injectivity domain. Along its geodesic the curvature operator is
$-\frac14\operatorname{ad}(\hat X)^2$,
with eigenvalue $0$ on the centralizer of $X$ and $\frac14\alpha(\hat X)^2$ on
the root plane of each positive root $\alpha$ (with $\operatorname{ad}X$ having
eigenvalues $\pm i\alpha(X)$ there). The midpoint covariance is therefore
$t/4$ along the centralizer and $(t/4)/h_\alpha$ on each root plane, with
$h_\alpha=\frac{\alpha(X)}4\cot\frac{\alpha(X)}4$. The centered representation
average is Hermitian and commutes with the centralizer of $X$. It is
block diagonal on weight spaces of a maximal torus containing $X$;
weight multiplicities allow mixing within each block. For
$SU(2)$ the single positive root has $\alpha(X)=d$, recovering (b). For a
compact simple Lie algebra,
$\sum_{\rm all\ roots}\alpha(X)^2=C_2({\rm adj})|X|^2$, and
$1/h_\alpha-1=\alpha(X)^2/48+O(\alpha^4)$, the curvature excess averaged
over the $\dim G$ directions is, per cut face,

$$\Delta T_j\simeq\frac{t_j}4\cdot\frac{C_2({\rm adj})\,|X_j|^2}{48\dim G},$$

that is $t_j|X_j|^2/288$ for $SU(2)$ ($C_2({\rm adj})=2$, $\dim G=3$) and
$t_j|X_j|^2/512$ for $SU(3)$ ($C_2({\rm adj})=3$, $\dim G=8$, two flat
Cartan directions and three root planes).

For a general compact Lie algebra replace $C_2({\rm adj})|X|^2$ by
$-\operatorname{tr}(\operatorname{ad}X)^2$; central directions contribute
zero and simple factors carry their own metric-dependent Casimirs.

Part (b) gives the leading covariance as $t\to0$ at fixed $X$ in the
specified compact domain. The displayed softening then expands this
coefficient at small $X$. When $|X|^2\sim t$, other order-$t^2$
covariance terms also contribute; the softening coefficient alone is
insufficient to compute the complete correction at that order. Numerical
remainder constants and control after representation summation remain
open. Positive curvature enlarges the
transverse fluctuation of the midpoint, $1/h(d)=1+d^2/48+O(d^4)$, so the
softening of the mid-face weight grows with the side-face flux. Splitting
$J(J+1)/h+\mu^2(1-1/h)$, each cut face adds $t_j/(4h(d_j))$ to the
mid-face heat time, about $t_jd_j^2/192$ above the abelian value
$t_j/4$, and an axial term $-\frac{t_j}8(1-\frac1{h(d_j)})(\hat X_j\cdot T)^2$
of the same order, which couples the mid-face to the direction of the
side flux. For fluctuating fields $d_j^2\sim t$, so both are
$O(t)$ relative to the action. N3, the non-Gaussian and commutator
corrections in $\prod_jm_j$, enters at the same order and is not computed
here. Proposition 7 below gives a weaker finite-cube inequality by
bounding all such terms in the remainder; extracting their coupling and
irrelevant-operator coefficients requires a separate calculation.

**Correction (GPT-6 Astra referee), 2026-09-27 — REFINE:** the reflection cancellation is rejected; a conditional finite-cube bound survives with mixed terms in its remainder.

**Proposition 7 (conditional finite-cube power bound).** Fix a compact
connected group, one cube, and positive bounded heat-time ratios. In a
local gauge let $X$ collect its independent boundary flux coordinates,
$r^2=\sum_f|X_f|^2$. Assume a uniform Laplace expansion of the *normalized*
bridge integral and old-face ratio,

$$\mathcal D(X,t)=c(t)+F(X)/t+A(X)-A(0)+R(X,t),$$

with $|F(X)-F_2(X)|\le Cr^3$, $|A(X)-A(0)|\le Cr$, and
$|R(X,t)|\le Ct(1+r^2/t)$. Here $F_2/t$ is the quadratic defect of
the isolated Gaussian cube, including the bridge denominators. These
bounds require a unique nondegenerate saddle and control of the full
heat-kernel/Haar amplitudes. For $r\le C_1t^{1/2-\delta}$ and
$0<\delta<1/6$,

$$|\mathcal D-c(t)-F_2/t|\le C_2t^{1/2-\delta}(1+r^2/t).$$

Thus the unperturbed finite-cube inequality has
$\alpha=1/2-\delta>2\delta$, even with coupling shifts set to zero.

*Derivation.* The cubic classical remainder is bounded by
$Cr(r^2/t)$, the amplitude variation by $Cr$, and $t\le t^{1/2-\delta}$
for small $t$. This proves the asserted inequality. The following
power counting explains the hypotheses without establishing their uniformity.
The leading saddle contributions are
$S_{\rm cl}+\frac12\log\det H$, where $S_{\rm cl}$
is the minimum over the four midpoints of the exponent
$\sum_j[d(Q_j^{-1},m_j)^2+d(m_j,P_j)^2]/t_j+d(e,m_{\partial g})^2/(2t_m)$
(the $w=0$ exponents) and $H$ its Hessian there. One must also add
$\sum_j\log k_{t_j}(e^{X_j})$ from the bridge denominators and include the heat-kernel
and Haar amplitudes. A remainder order for the bare integral alone
does not supply the displayed expansion.
(i) *Classical part.* The Lie-algebra linearization of $S_{\rm cl}$ is the
abelian problem, so its quadratic part is the free form, which is
$\mathcal D_0$ after the old-face subtraction. The rest starts at cubic
order: Baker--Campbell--Hausdorff terms such as the N1 commutator,
$\langle X_{\rm mid},[X_{12},X_{13}]\rangle/t$, and quartic invariants
$|X|^4/t$. On the small-field set, $|X|^3/t\le t^{1/2-\delta}|X|^2/t$
and $|X|^4/t\le t^{1-2\delta}|X|^2/t$, both inside the remainder of
P($\alpha$) with $\alpha=\frac12-\delta$.
(ii) *One-loop part.* Mixed quadratic boundary terms can survive cube
reflections because reflections also permute the faces. For example,
$\langle\Delta_1X_{23},\Delta_2X_{31}\rangle$, with $\Delta_i$ the
difference between opposite faces normal to direction $i$, is even
under each coordinate reflection: each factor transforms as a pseudoscalar.
Axis permutations can be accommodated by summing the corresponding pairs.
The linear Bianchi relation among the three differences can rewrite
such terms as squares of differences, which still couple opposite faces.
Thus reflection invariance permits more than a sum of individual
plaquette norms. The coupled Hessian can also have linear
off-diagonal blocks from cubic BCH terms, whose squared contribution
enters $\log\det H$ at quadratic order. Every bounded quadratic amplitude
term is $O(r^2)=O(t)(r^2/t)$ and already fits the stated remainder since
$\alpha<1$. Identifying plane-diagonal coupling shifts requires a separate
calculation. The present bound makes no such identification.
(iii) The old-face ratio $k_{2t}/k_t$ is even in $\log U_f$ and
contributes a constant and a transverse coupling shift. $\square$

Proposition 7 is power counting made explicit for one cube; its
hypothesis, a uniform Laplace remainder on the small-field set, is
exactly the missing estimate. Proposition 6 computes the curvature part
of (ii) for $SU(2)$. For a whole mid-plane the same bookkeeping applies,
but $H$ couples all mid-edges and $\log\det H$ is non-local in the fluxes;
controlling it is the cluster expansion of open problem 2 in the README.

Under P($\alpha$) the per-step error on smooth observables is
$O((\lambda_3a)^\alpha)$ and the coupling shifts sum to a finite
renormalization, because $\sum_n\lambda_3a_n=2\lambda_3a_0$: the
superrenormalizable pattern of the refinement note's table, now with
the term to be bounded identified exactly. P($\alpha$) is the
directional form of what Balaban's three-dimensional ultraviolet
stability controls in his block-averaging scheme
([Balaban 1985, CMP 102, 255](https://doi.org/10.1007/BF01229380),
metadata); whether his estimates transfer to the heat-kernel directional
scheme is unverified. P($\alpha$) yields ultraviolet control and says
nothing about the gap: the long-distance spectral estimate of the
refinement note §7 remains a separate obligation.

## 5. Four dimensions

In $D=4$ a halving of direction 1 inserts parallel copies in the three
planes $(23),(24),(34)$, and the mid-space is a three-dimensional lattice
gauge theory with bridge-distributed edges. By the table in §2 the heat
time returns to itself after an isotropic step, so the whole one-loop
running $g_0^{-2}(2a)=g_0^{-2}(a)-2b_0\log2+O(g_0^2)$, with
$b_0=11/(16\pi^2)$ for $SU(3)$ in the convention
$g_{\rm lat}^2=\lambda_4$, must come out of the four $\Psi$ factors of
one isotropic step, to leading order and within the class of actions of
P($\alpha$). N2 and N3 are $O(t)$ relative in both dimensions. In $D=4$,
$t=g^2$ does not decrease along the sequence, so their step-independent
shift of $g^{-2}$ is the whole one-loop running, $-2b_0\log2$ per
isotropic step; in $D=3$ the shifts, $O(\lambda_3a_n)$ relative, are
summable.
This is the exact location of marginality in the insertion language.
The corresponding hypothesis is H1 of the
[conditional theorem](mass-gap-conditional-theorem.md), and Balaban's
four-dimensional work ([Balaban 1987](https://doi.org/10.1007/BF01215223),
metadata) is the established partial control.

## 6. Consequence for STATE

Item 1 of STATE is answered in its "exact obstruction" form, and its
first rungs are proved. One directional refinement step factors exactly
into series moves, which close, and a parallel insertion $\Psi$
(Proposition 1). $\Psi$ is exact for the free field (Proposition 2),
for the $U(1)$ cube (Proposition 3) and the $U(1)$ mid-plane
(Proposition 4), and for $U(1)$ the unperturbed one-step bound has
error density $e^{-\pi^2/(8\lambda_3a)}$ (Theorem 5).
For non-abelian groups the midpoint curvature term
is explicit (Proposition 6 and its group-general form), and the
finite-cube bound is conditional on a full normalized Laplace expansion
(Proposition 7). The
next step is the uniform Laplace remainder that turns Proposition 7 into
a theorem for $SU(2)$ and $SU(3)$; after it, a mid-plane by small-field
cluster expansion, and stability under iteration. For the paper, the
series/parallel split is the organizing statement of the dimension
comparison: Newton's time insertion is a series move closed by one
scalar; two-dimensional gauge theory has only series moves; three and
four dimensions add $\binom{D-1}{2}$ parallel insertions whose
elimination is the renormalization problem; the error density of those
insertions in physical units gives a sufficient test for which lattice
effects the limit discards.
