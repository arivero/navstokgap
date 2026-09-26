# Series and parallel: where the gauge insertion law stops closing

**Result, 2026-09-26.** Halve one lattice direction of a heat-kernel
lattice gauge theory in $D$ dimensions. The step splits exactly into
two kinds of move. Faces containing the refined direction are cut in
two; these are *series* moves, and the heat-kernel convolution integrates
them out exactly in every dimension. Faces transverse to the refined
direction acquire a new parallel copy at doubled heat time; these are
*parallel* moves, and integrating out the new copy leaves the factor
$\Psi$ of Proposition 1: the partition function of a two-dimensional
gauge theory on the inserted mid-plane, whose edges carry Brownian-bridge
laws fixed by the coarse field instead of Haar measure. The number of
transverse planes is $\binom{D-1}{2}$: none in $D=2$, which is why
two-dimensional Yang--Mills closes; one in $D=3$; three in $D=4$. In the
free (abelian Gaussian) theory $\Psi$ is computed exactly (Proposition 2):
the defect against the coarse action is a negative semidefinite quadratic
form of relative size $a^2K^2/16+(Ga)^2/8$ for fields with transverse
momenta at most $K$ and layer gradient $G$. It is the field-theory
counterpart of Newton's $-F^2uvh/(8M)$ in the
[refinement note](refinement-composition-and-limit.md), eq. (1), and it
equals exactly the error of Migdal's bond-moving approximation in the
Gaussian theory. For a single cube with $G=U(1)$ the parallel move is
exact in closed form (Proposition 3): a heat kernel at softened heat
time on the interpolated flux, times a theta-function factor that is the
large-field term with rate $e^{-2\pi(\pi-|\phi|)/t}$. The non-abelian
estimate needed for one step in $1+2$ dimensions is stated in §4 as
Hypothesis P($\alpha$), with the four terms it must control and their
orders in $\lambda_3a$.

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
Wilson action; the theorems below concern it exactly.

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
converge to a fixed point, the perfect action of
[Hasenfratz and Niedermayer (1994)](https://doi.org/10.1016/0550-3213(94)90261-5)
(metadata). And (6) holds for smooth coarse data; typical lattice fields
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

- **N1, interpolation.** The mean mid-face holonomy differs from the
  abelian average by Baker--Campbell--Hausdorff commutators of the
  fluxes, of order $a^4[F,F]$ in $\log U_g$. In the action this is a
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
  $O(e^{-c/t})$ per face, non-perturbatively small at each step but to be
  controlled uniformly in the volume.

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

If every $\rho_{t_j}(\phi_j)=1$, then $\Psi=k_T(\bar\Phi)$ exactly. For
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
counterpart of the noise $v(k)$ in (5), evaluated at the interpolated
flux. The only departure is the odd-charge factor, which differs from 1
only where a side-face flux approaches the cut locus $|\phi|=\pi$, where
its bridge midpoint becomes bimodal. That is N4, exactly, with the rate
$e^{-2\pi(\pi-|\phi|)/t}$. For a whole mid-plane, Poisson summation on
each edge turns $\Psi$ into a sum over integer windings of Gaussian
terms, a Coulomb-gas representation in which the same rate controls the
winding activities; that computation is left open. For $SU(2)$ and
$SU(3)$ the bridge expectations $E\,R(m_j)$ are matrices, and the
isolated cube is where N2 and N3 first appear.

**Hypothesis P($\alpha$) (one parallel step, $D=3$).** There exist
$\alpha>0$, $t_0>0$, $C<\infty$ and a local quadratic form
$\mathcal D_0$ (the free defect (5), possibly with renormalized
$t_{23}$), such that for $t=\lambda_3a\le t_0$, on the small-field set
where every plaquette satisfies $|\log U_p|\le t^{1/2-\delta}$,

$$\Bigl|-\log\Psi(U)-\mathcal D_0(U)-c_{\rm vac}N_{\rm cells}
-\delta_t\,S_{23}(U)\Bigr|
\le C\,t^{\alpha}\sum_{\rm cells}\bigl(1+|\log U_p|^2/t\bigr),$$

with a coupling shift $|\delta_t|\le Ct$, and with a large-field
suppression of $\Psi$ by at least $e^{-c\,t^{-2\delta}}$ per violating
plaquette, relative to its small-field value.

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
one isotropic step. The N3 fluctuation term is therefore order one in
$D=4$ (it carries the logarithm), while in $D=3$ it is $O(\lambda_3a)$.
This is the exact location of marginality in the insertion language.
The corresponding hypothesis is H1 of the
[conditional theorem](mass-gap-conditional-theorem.md), and Balaban's
four-dimensional work ([Balaban 1987](https://doi.org/10.1007/BF01215223),
metadata) is the established partial control.

## 6. Consequence for STATE

Item 1 of STATE is answered in its "exact obstruction" form. The one-step
$1+2$ gauge refinement factors exactly into series moves, which close,
and a parallel insertion $\Psi$ (Proposition 1). $\Psi$ is computed in
closed form for the free field (Proposition 2, bound (6)), and the
interacting estimate is stated as Hypothesis P($\alpha$) with its four
terms; Proposition 3 settles the isolated cube for $U(1)$. The next
concrete step on this line is to prove P($\alpha$) for **one isolated
cube with $G=SU(2)$, then $SU(3)$** (a single mid-face, where independence of the four
bridge variables reduces $\Psi$ to
$\sum_Rd_Re^{-t_mC_2(R)/2}{\rm tr}_R\prod_{j}E\,R(m_j^{\pm1})$ with
$t_m$ the mid-face heat time and the sign fixed by orientation), and
then for a mid-plane with small-field cluster expansion. For the paper,
the series/parallel split is the organizing statement of the dimension
comparison: Newton's time insertion is a series move closed by one
scalar; two-dimensional gauge theory has only series moves; three and
four dimensions add $\binom{D-1}{2}$ parallel insertions whose
elimination is the renormalization problem.
