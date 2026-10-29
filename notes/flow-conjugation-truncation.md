# Gauge flow: exact conjugation, Jacobian locality and spectral truncation

Finite-lattice Wilson flow is a diffeomorphism and has a unitary pullback.
It preserves spectra and transformed multiplication norms. Its first derivative
has a local path-expansion bound, but that estimate alone controls no relative
Hamiltonian truncation error.

The continuum auxiliary covariant heat equation below has an absolute Gaussian
kernel-tail bound under a full-interval curvature hypothesis. The exact
variation of the usual gauge-modified flow contains additional linear terms.
A stationary chromomagnetic background has an aligned mode growing at
$gB-k_\parallel^2$, after the Landau cost is included. These are different
operators and domains. Their proofs identify what a proposed spectral reduction
would still have to control; they do not supply a physical mass gap.

## Finite-lattice invariances

On $\mathcal M=G^{\mathcal E}$, the Wilson flow
$$\dot V_s(x,\mu)=-g^2\{\partial_{x,\mu}S_w(V_s)\}V_s(x,\mu),
\qquad V_0=U,$$
has a smooth all-time flow on the compact finite-dimensional manifold;
$\Phi_t^{-1}=\Phi_{-t}$. Lüscher, arXiv:1006.4518v3, (1.4) and the
following sentence (passage-level reading in the
[local companion](../docs/Luscher_WilsonFlow_1006.4518v3.md)), supplies
the finite-lattice flow and action monotonicity. Let
$\rho_t=|\det D\Phi_t|$ relative to Haar measure and define
$$(W_t\psi)(U)=\rho_t(U)^{1/2}\psi(\Phi_t(U)).$$
Change of variables proves $W_t$ is unitary. Hence $W_tHW_t^*$ has
exactly the spectrum, multiplicities and gap of $H$. Also
$$W_tM_fW_t^*=M_{f\circ\Phi_t},\qquad
\|f\circ\Phi_t\|_\infty=\|f\|_\infty,$$
because $\Phi_t$ is onto. Thus any criterion using only the spectrum of
$H_0$ and the norm of $\phi$ is unchanged under *the same unitary
conjugation* of the pair. This does not show invariance under an unrelated
new splitting or under projection: flow can mix links and change the
supports and hypotheses of a local theorem.

For the Kogut--Susskind Hamiltonian
$$H=\frac{\hbar c}{a}\left[\frac{g^2}{2}K+\frac2{g^2}V\right],\quad
K=\sum_\ell(-\Delta_\ell),\quad
V=\sum_p(N-\operatorname{Re}\operatorname{tr}U_p),$$
flow gives $0\le V\circ\Phi_t\le V$ for $t\ge0$, while its supremum is
unchanged. It follows that
$\langle\psi,(V\circ\Phi_t)\psi\rangle\le\langle\psi,V\psi\rangle$
for a fixed state $\psi$; if both state and observable are transformed
consistently, their expectation is unchanged. In particular this is no
proof that the physical ground-state measure has uniform local
large-field tails. The corrected [Agmon analysis](agmon-ground-state-suppression.md)
controls integrated global excess only; the
[magnetic identities](magnetic-energy-identities.md) show that its simple
Gibbs-comparison repair does not supply the missing local estimate.

## Kinetic metric, free cancellation and lattice derivatives

The electric operator becomes a second-order operator whose coefficients
are determined by the pullback metric and the Jacobian. Flow mixes links:
the transformed operator is generally nonlocal. The scale $\sqrt{8t}$
is a smoothing radius, not a strict finite interaction range. Bounds on the flow Jacobian do not by themselves prove relative operator-error
bounds for a truncated Hamiltonian; the one-step distinction is explained below.

In a finite-volume regularized free abelian model in Coulomb gauge, a
nonzero mode obeys $A_k\mapsto e^{-tk^2}A_k$ and the Jacobian is a
constant. With a canonical momentum convention consistent with the
Hamiltonian, the transformed quadratic coefficients acquire reciprocal
factors $e^{-2tk^2}$ and $e^{+2tk^2}$, so their product and oscillator
frequency $\omega_k=c|k|$ are unchanged. This illustrates the exact
unitary result. Treating the ratio of those coefficients as a Yarotsky
smallness parameter is not justified: Fourier modes are not the local
site decomposition required by that theorem and a free mode's
coordinate and momentum are unbounded. The former assertion that an
arbitrary local criterion can always be improved without limit by
conjugation is withdrawn.

### One lattice step: coupling cancellation and local derivatives

For the stated Wilson normalization the $g^2$ in the flow equation
cancels the $1/g^2$ in the action. At fixed dimensionless time, the
finite-lattice vector field is therefore independent of $g$. Choosing
$\sqrt{8t}=2a$ gives $t/a^2=1/2$. The link-local vector field has bounded
derivatives at fixed compact group and bounded lattice incidence. More
explicitly, write its linearization in link coordinates as $\dot J=A(s)J$
with $A_{xy}=0$ beyond a fixed interaction distance and row sums bounded
by $B$, uniformly in the lattice size. Expanding the integral equation,
a matrix element at graph distance $d$ can receive a contribution only
after at least $d$ local factors, so
$$\|J_{xy}(t)\|\le\sum_{n\ge d}\frac{(B|t|)^n}{n!}.$$
Here time and $B$ are in lattice units, and any finite-range edge in
$A$ is one step of this graph. This elementary bound is uniform in
volume and coupling under the stated derivative and frame bounds; its
constants depend on the group and local geometry. It controls the first
flow derivative, not automatically the inverse derivative, Jacobian
potential, unbounded kinetic form or full Hamiltonian truncation. The
former claim $Ce^{-cK}$ for the relative operator error and the assertion
that $K=3$ suffices are withdrawn: no constants or relative-form proof
were provided. Compactness also does not itself prove normalized
large-field rarity or multiscale stability.

## Exact continuum variation and its gauge convention

Take Lüscher's gauge-modified continuum flow
$$\partial_sB_\mu=D_\nu G_{\nu\mu}+D_\mu q,
\qquad q=\partial_\nu B_\nu.$$
The definition is from arXiv:1006.4518v3, equations (1.1)--(1.2) and
(2.2), passage level via the
[local companion](../docs/Luscher_WilsonFlow_1006.4518v3.md).
Repeated spatial indices are summed. Write $u=\delta B$.

**Proposition 1 (exact variation and auxiliary gauge choice).** The
Jacobian of this gauge-modified flow obeys
$$\partial_su_\mu=D^2u_\mu+2[G_{\mu\nu},u_\nu]
+D_\mu(\partial_\nu u_\nu-D_\nu u_\nu)+[u_\mu,q].$$
The ungauged flow instead has linearization
$$\partial_su_\mu=D^2u_\mu-D_\mu D_\nu u_\nu
+2[G_{\mu\nu},u_\nu].$$
Adding the **linear background-covariant gauge term**
$D_\mu D_\nu u_\nu$ to the latter defines the auxiliary evolution
used in the auxiliary bounds below. Identifying it with another flow Jacobian
requires an additional gauge comparison, not supplied here.

*Proof.* Since $\delta D_\nu=[u_\nu,\cdot]$ and
$\delta G_{\nu\mu}=D_\nu u_\mu-D_\mu u_\nu$,
$$\delta(D_\nu G_{\nu\mu})
=D^2u_\mu-D_\nu D_\mu u_\nu+[u_\nu,G_{\nu\mu}]
=D^2u_\mu-D_\mu D_\nu u_\nu+2[G_{\mu\nu},u_\nu].$$
Here $[D_\nu,D_\mu]u_\nu=[G_{\nu\mu},u_\nu]$.
The gauge term has the exact variation
$$\delta(D_\mu q)=D_\mu\partial_\nu u_\nu+[u_\mu,q],$$
not $D_\mu D_\nu u_\nu$. Adding these formulas proves the first
identity; omitting the gauge term or adding the specified linear one
proves the other assertions. $\square$

Thus the original cancellation "to the same order" was unjustified:
the omitted terms are themselves linear in $u$. The propositions below
are about $J$, not about the full $D\Phi_t$ in Lüscher's convention.
At $B=0$ both equations reduce to the free heat equation. At a
stationary background, background-transverse modes of the ungauged
linearization also agree with the auxiliary generator; no general
preservation of that transverse condition is asserted.

## Auxiliary Gaussian bound

Equip the compact Lie algebra with an invariant positive inner product,
and its vector fields with $|u|^2=\sum_\mu|u_\mu|^2$. The connection is
metric-compatible because $\operatorname{ad}(B_\mu)$ is skew-adjoint.
Assume $B(s,x)$ is smooth on $[0,t]\times\mathbb R^3$, with bounded
coefficients and spatial derivatives sufficient for the covariant
parabolic propagators and kernels below, and define
$$(\mathcal C(s,x)u)_\mu=\sum_\nu[G_{\mu\nu}(s,x),u_\nu],\qquad
 \Gamma(s)=\sup_x\|\mathcal C(s,x)\|_{\rm op},\qquad
 A_t=2\int_0^t\Gamma(s)\,ds.$$
Assume $\Gamma\in L^1([0,t])$. These are hypotheses, not estimates derived
from action monotonicity.

**Proposition 2.** Under these assumptions the auxiliary propagator
satisfies
$$\|J(t,0;x,y)\|_{\rm op}\le e^{A_t}K_t^{\rm free}(x-y),
\qquad K_t^{\rm free}(z)=(4\pi t)^{-3/2}e^{-|z|^2/(4t)}.$$
In particular, if $\Gamma(s)\le\Gamma_*$ then $A_t\le2t\Gamma_*$.

*Proof.* First consider $\partial_s v=D(s)^2v$. Metric compatibility
gives
$$(\partial_s-\Delta)|v|^2=-2\sum_\alpha|D_\alpha v|^2.$$
Apply the chain rule to $h_\epsilon=(|v|^2+\epsilon^2)^{1/2}$ and use
$|\partial_\alpha|v|^2|\le2|v|\,|D_\alpha v|$. It follows that
$(\partial_s-\Delta)h_\epsilon\le0$. Scalar comparison followed by
$\epsilon\downarrow0$ yields, for the time-dependent covariant
propagator $U(t,r)$,
$$|U(t,r)f|(x)\le(e^{(t-r)\Delta}|f|)(x).$$
With the assumed kernels this also gives
$\|U(t,r;x,y)\|_{\rm op}\le K_{t-r}^{\rm free}(x-y)$, by testing
localized initial data. This proves the needed Kato domination here;
no bibliographic sharpness claim is used.

Set $M(s)=2\mathcal C(s)$. Duhamel uses the two-time propagator,
$$J(t,0)=U(t,0)+\int_0^t U(t,s)M(s)J(s,0)\,ds.$$
In the term with $n$ insertions, each multiplication factor has norm
at most $2\Gamma(s_i)$ and scalar heat kernels convolve to
$K_t^{\rm free}(x-y)$. The ordered time integral is bounded by
$A_t^n/n!$. Summing this absolutely bounded series proves the result.
$\square$

**Norm convention.** If instead
$g_*=\sup_{s,x,\mu,\nu}\|\operatorname{ad}(G_{\mu\nu}(s,x))\|_{\rm op}$,
then $\Gamma_*\le2g_*$ in three dimensions, or
$\Gamma_*\le(d-1)g_*$ in $d$ dimensions. Indeed
$$|(\mathcal Cu)_\mu|\le g_*\sum_{\nu\ne\mu}|u_\nu|,$$
and Cauchy--Schwarz, followed by summation over $\mu$, gives
$|\mathcal Cu|^2\le(d-1)^2g_*^2|u|^2$. The former unspecified
"adjoint operator norm" cannot silently omit this index factor.

At $B=0$, $J=K_t^{\rm free}I$ and the pointwise bound is attained.
This free-case equality does not establish optimality of the curvature
exponent for nonzero backgrounds.

## Absolute tails and the missing metric comparison

Define $J_R$ by cutting its kernel to $|x-y|\le R$, and set
$$T_R=J-J_R,\qquad
\delta(R,t)=e^{A_t}\int_{|z|>R}K_t^{\rm free}(z)\,d^3z.$$
Proposition 2 bounds both row and column integrals of
$\|T_R(x,y)\|_{\rm op}$ by $\delta(R,t)$. Consequently the Schur test
(or the scalar convolution majorant) gives the **absolute** bound
$$\|T_R\|_{L^2\to L^2}\le\delta(R,t).$$
It is not normalized by $\|J\|$ or by a kinetic quadratic form.

**Corollary 3 (kernel-tail budget).** Put $q=R/(2\sqrt t)$. Then
$$\delta(R,t)=e^{A_t}
\left[\operatorname{erfc}(q)+\frac{2q}{\sqrt\pi}e^{-q^2}\right]
\le e^{A_t-q^2}\left(1+\frac{2q}{\sqrt\pi}\right).$$
Thus at $R=\kappa\sqrt{8t}$ a sufficient condition for
$\|J-J_R\|_{2\to2}\le\epsilon$ is
$$2\kappa^2\ge A_t+
\log\left(1+\frac{2\sqrt2\kappa}{\sqrt\pi}\right)
+\log(1/\epsilon),\qquad 0<\epsilon<1.$$
For every finite $A_t$ this is achieved at sufficiently large $\kappa$.
It is a sufficient condition only.

*Proof.* Radial integration and $r=2\sqrt t\,v$ give
$$\int_{|z|>R}K_t^{\rm free}(z)\,d^3z
=\frac4{\sqrt\pi}\int_q^\infty v^2e^{-v^2}dv
=\operatorname{erfc}(q)+\frac{2q}{\sqrt\pi}e^{-q^2}.$$
For $q\ge0$, $\operatorname{erfc}(q)\le e^{-q^2}$: their difference
is zero at zero, has derivative
$2e^{-q^2}(1/\sqrt\pi-q)$, and tends to zero at infinity.
The stated inequality and logarithmic budget follow. $\square$

At $\kappa=1$, even the exact free discarded mass is
$\operatorname{erfc}(\sqrt2)+(2\sqrt2/\sqrt\pi)e^{-2}$.
This is a fixed positive number, not a parameter tending to zero on
small fields. A growing upper bound for $A_t$ implies neither a large
actual tail nor a lower bound on a truncation error.

**The Hamiltonian conversion remains open.** The kinetic metric in
the finite-lattice kinetic construction above, involves quadratic Jacobian combinations and inverse
metrics; the transformed operator also has density derivatives and
lower-order terms. Already for bounded operators $F$ and $F_R$, with
$E=F-F_R$,
$$\|F^*F-F_R^*F_R\|
\le2\|F\|\,\|E\|+\|E\|^2.$$
This follows by expanding $F_R=F-E$. It is an absolute estimate;
a relative comparison additionally needs a positive lower bound on
the relevant metric or a bound on its inverse. The free continuum
heat multiplier $e^{-t|k|^2}$ has no bounded inverse on $L^2$.
The finite lattice has an invertible flow Jacobian, but uniform inverse,
configuration-derivative and relative form estimates still need proof.
The auxiliary $J$ above is not identified with that lattice Jacobian.
Thus the original Hamiltonian interpretation of $\delta$ remains a
**heuristic motivation**, not a proved relative truncation theorem.

## A sufficient curvature budget

Write $\ell=\sqrt{8t}$. If the block norm satisfies
$$\Gamma(s)\le\frac\eta{\ell^2}\quad(0\le s\le t),$$
then $A_t\le\eta/4$ and the kernel-tail corollary yields
$$\|J-J_R\|_{2\to2}
\le\left(1+\frac{2\sqrt2\kappa}{\sqrt\pi}\right)
\exp\left[\frac\eta4-2\kappa^2\right].$$
The original $2\eta$ growth exponent in this substitution was incorrect.
In component norm, the hypothesis $g_*\le\eta/\ell^2$ gives instead
$A_t\le\eta/2$ in three dimensions by the index bound of the auxiliary-bound section.

| regime or question | supported conclusion |
| --- | --- |
| bounded curvature budget $A_t$, sufficiently long range | absolute auxiliary kernel tail is below a prescribed tolerance |
| small $\eta$ at one fixed flow radius | bounded tail, with no arbitrarily small accuracy implied |
| large $A_t$ at fixed range | this upper bound deteriorates; actual tail size remains undetermined |
| larger range at finite $A_t$ | the kernel majorant can be made small |
| conjugated Hamiltonian or iterated RG | relative form and iteration estimates remain open |

This budget motivates comparison with small/large-field splitting in
constructive renormalization, but neither forces that split nor controls
all steps of the finite-lattice construction above.
The comparison to Balaban's series (Commun. Math. Phys. 122 (1989) 355,
metadata level) is context, not a derivation of its hypotheses. No
unproved decay of a "typical" interacting curvature is used here.

## Action monotonicity and curvature norms

For smooth finite-action solutions of the ungauged gradient flow, with
decay allowing integration by parts and the gradient normalization,
$$\frac{d}{ds}S(B_s)=-\|\nabla S(B_s)\|_2^2\le0.$$
The added gauge term is an infinitesimal gauge transformation and does
not change this identity under the same boundary assumptions.
Since $S$ is proportional to $\int|G|^2$, it gives
$$\|G(t)\|_2^2\le\|G(0)\|_2^2.$$
It supplies no $L^\infty$ bound by itself, and Proposition 2 requires
control over the **whole flow interval**, not just its endpoint.

**Free or abelian smoothing, corrected.** Around the zero connection
$J$ is the heat semigroup. In an abelian theory the curvature itself
obeys the heat equation, so Cauchy--Schwarz and the Gaussian convolution
identity give
$$\|e^{t\Delta}f\|_\infty
\le\|K_t^{\rm free}\|_2\,\|f\|_2
=(8\pi t)^{-3/4}\|f\|_2.$$
For abelian initial curvature this bounds $\|G(t)\|_\infty$ by
$(8\pi t)^{-3/4}\|G(0)\|_2$ in the Euclidean component norm.
For fixed nonzero initial norm its ratio to $1/t$ is proportional to
$t^{1/4}\|G(0)\|_2$: it tends to zero for small $t$ and grows for
large $t$, the reverse of the former remark. Integrating this estimate
over $0<s<t$ also gives a finite budget proportional to
$t^{1/4}\|G(0)\|_2$, using the finite-dimensional conversion to the
block norm. This is an abelian estimate, not an interacting theorem.
The coefficient $(4\pi t)^{-3/4}$ formerly displayed is a looser valid
bound; the expression above is the exact heat-kernel $L^2$ norm.

**Monotonicity alone does not supply the missing norm.** A fixed $L^2$
curvature norm permits concentration in small regions with arbitrarily
large height. For example rescale a smooth compactly supported abelian
connection by $B_\lambda(x)=\lambda^{1/2}B(\lambda x)$; its curvature
is $G_\lambda(x)=\lambda^{3/2}G(\lambda x)$, with constant $L^2$ norm
and unbounded supremum as $\lambda\to\infty$. This disproves a
pointwise estimate from the action bound alone, not parabolic estimates
using additional evolution information.

The Hamiltonian formulation also has configuration probabilities,
for example its ground-state density; see
[the transfer note](ground-state-measure-transfer.md), §§1--2 (full-read).
Such measure estimates do not automatically give the signed operator
comparisons needed for spectral stability. The distinction emphasized
in [the operator-inequality note](large-field-operator-inequality.md),
§3 (full-read), is relevant here; this note does not assume its claimed
Hamiltonian truncation estimate or conclude that every Hamiltonian
route fails.

## Instability of the full background generator

Let $\mathfrak g$ be a compact matrix Lie algebra with invariant inner
product $\langle X,Y\rangle=-\operatorname{tr}(XY)$. Then
$\operatorname{ad}(Z)$ is antisymmetric:
$\langle[Z,X],Y\rangle=-\langle X,[Z,Y]\rangle$.

**Lemma (curvature symmetry).** At each point, on $\mathfrak g$-valued vectors with
inner product $\sum_\mu\langle u_\mu,v_\mu\rangle$, the operator
$(Mu)_\mu=2[G_{\mu\nu},u_\nu]$ is symmetric.

*Proof.*
$$\langle Mu,v\rangle
=2\sum_{\mu\nu}\langle[G_{\mu\nu},u_\nu],v_\mu\rangle
=-2\sum_{\mu\nu}\langle u_\nu,[G_{\mu\nu},v_\mu]\rangle
=2\sum_{\mu\nu}\langle u_\nu,[G_{\nu\mu},v_\mu]\rangle
=\langle u,Mv\rangle.$$
The two antisymmetries cancel. $\square$

A finite-dimensional symmetric operator of norm $N$ has an eigenvalue
of modulus $N$; symmetry does not determine its sign. Moreover,
positive eigenvalues of $M$ alone do not determine those of $D^2+M$.
For compactly supported fields, integration by parts gives
$$\langle u,Lu\rangle=-\sum_\alpha\|D_\alpha u\|_2^2
+\langle u,Mu\rangle.$$
The first term must be retained.

The preceding Duhamel bound uses $\Gamma=\frac12\sup\|M\|$; its exponent is an upper bound only. The following example retains both terms of $L$.

### The charged Landau mode

We work with the Yang--Mills flow linearized at a stationary background
$\bar A$, in **background-covariant gauge**. This specifies the operator
rather than assuming that every gauge-modified flow has the same
Jacobian. With $D=\partial+[\bar A,\cdot]$ and $D_\nu G_{\nu\mu}=0$,
variation of the ungauged flow gives
$$\partial_su_\mu=D^2u_\mu-D_\mu D_\nu u_\nu
+2[G_{\mu\nu},u_\nu].$$
Adding the linear background-gauge term $D_\mu D_\nu u_\nu$ gives $L$.
Equivalently, on a mode with $D_\nu u_\nu=0$, the ungauged linearization
already agrees with $L$. This does not repair or identify the full
Jacobian in every gauge convention.

Choose an $SU(2)$ colour sector with $[T^3,E_+]=iE_+$, and absorb the
coupling into the connection, so $G_{12}=bT^3$, $b=gB>0$.
In symmetric gauge on the transverse plane,
$$\bar A_1=-\frac b2x_2T^3,\qquad
\bar A_2=\frac b2x_1T^3.$$
On the $E_+$ component,
$$D_1=\partial_1-\frac{ibx_2}{2},\qquad
D_2=\partial_2+\frac{ibx_1}{2}.$$
Writing $Q=D_1-iD_2$, integration by parts and $[D_1,D_2]=ib$
give $Q^*Q=-(D_1^2+D_2^2)-b$ and $[Q,Q^*]=2b$.
Thus the oscillator ladder has transverse magnetic-Laplacian energies
$(2n+1)b$, $n=0,1,\ldots$. To fix the factor without relying on a
bibliographic convention, its lowest mode can be checked directly:
$$f(x_1,x_2)=e^{-b(x_1^2+x_2^2)/4},\qquad
(D_1-iD_2)f=0,\qquad (D_1^2+D_2^2)f=-bf.$$
On the two transverse vector components,
$$M=\begin{pmatrix}0&2ib\\-2ib&0\end{pmatrix},\qquad
M\binom f{-if}=2b\binom f{-if}.$$
The charged complex notation represents real Lie-algebra fields by
adding the conjugate charge sector. The vector
$$u=(f,-if,0,\ldots)e^{ik_\parallel\cdot x_\parallel}$$
is background-transverse, since $D_1f-iD_2f=0$. Consequently
$$D^2u=-(b+k_\parallel^2)u,\qquad
Lu=(b-k_\parallel^2)u.$$
This supplies both the positive eigenvalue of $M$ and the Laplacian
cost on the same vector. The two transverse polarizations at general
Landau level have the spectral values
$$\omega^2=k_\parallel^2+(2n+1)b\mp2b$$
for $-L$. Here $k_\parallel^2$ is the sum of the squared momenta in
directions outside the magnetic plane: one for spatial three-dimensional
flow, two for four-dimensional Euclidean flow. The unstable branch is
$$\omega^2=k_\parallel^2-b<0\quad\text{when }k_\parallel^2<b,$$
and its gradient-flow growth is
$$e^{-\omega^2s}=e^{(b-k_\parallel^2)s}.$$
At $k_\parallel=0$ the rate is $b$, half the exponent coefficient
$2b$ in the Duhamel majorant. That example therefore **does not saturate**
the majorant. Whether a better universal bound holds for other
backgrounds is not settled by this calculation.

On the whole space the longitudinal plane waves are generalized modes;
wave packets supported in $k_\parallel^2<b$ give growing $L^2$
perturbations, with rates approaching $b$. Periodic longitudinal
boundary conditions admit the zero-momentum mode. The constant field
on the transverse plane has infinite total action; the calculation is
a stationary-background spectral model, not a finite-action
four-dimensional construction or a statement for arbitrary finite boxes.

This is the instability historically associated with Nielsen and Olesen,
[“An unstable Yang--Mills field mode,” Nucl. Phys. B144 (1978) 376--396](https://doi.org/10.1016/0550-3213(78)90377-2)
(abstract read; the original spectral passage was not read here).
The numerical factors used above are supported by the displayed
calculation, not by that abstract or a normalization left implicit.

### Action descent and growing perturbations

For the unmodified gradient flow with its gradient-metric normalization,
$$\frac{d}{ds}S(A_s)=-\|\nabla S(A_s)\|_2^2\le0.$$
A constant abelian curvature has $D_\nu G_{\nu\mu}=0$ and is stationary.
Its transverse unstable modes give negative Hessian directions,
$\operatorname{Hess}S=-L$ on the background-transverse sector in the
normalization of the auxiliary-bound section. Nearby trajectories can separate at rate
$b-k_\parallel^2$ while descending the action. For the infinite-action
background these are statements about the local equation and quadratic
variation on admissible perturbations, rather than differentiation of
an infinite total action.

The original comparison with
[the valley note](torus-valley-potential.md) is also corrected: constant
commuting connections in its flat holonomy valley have $G=0$. They are
not the nonzero constant chromomagnetic background considered here.
The valley's zero-point potential is a different calculation and gives
no justification for this saddle or its growth rate.

## Free-field size is a benchmark, not a supremum bound

From [the free-field susceptibility calculation](finiteness-half-flowed-susceptibility.md#susceptibility), the flowed
magnetic two-point function at coincident points is
$$\big\langle b_{t,i}(0)b_{t,i}(0)\big\rangle
=\int\!\frac{d^3k}{(2\pi)^3}\sum_i\tilde G_{ii}(k)
=\int\!\frac{d^3k}{(2\pi)^3}\,\frac{g^2k}{2}\,e^{-2tk^2}\cdot2
=\frac{g^2}{2\pi^2}\int_0^\infty\!k^3e^{-2tk^2}dk,$$
and $\int_0^\infty k^3e^{-\alpha k^2}dk=1/(2\alpha^2)$ with $\alpha=2t$
gives
$$\big\langle|b_t|^2\big\rangle=\frac{g^2}{2\pi^2}\cdot\frac1{8t^2}=\frac{g^2}{16\pi^2t^2},
\qquad \big\langle|b_t|^2\big\rangle^{1/2}=\frac{g}{4\pi\,t}.$$
The flow time is the only scale, so the dimensionless combination is
$$t\,\big\langle|b_t|^2\big\rangle^{1/2}=\frac{g}{4\pi},$$
independent of $t$ and of the lattice spacing. In the interacting theory
at scale $\ell=\sqrt{8t}$ the same estimate with the running coupling
$g(\ell)$ is the leading perturbative statement.

The displayed convention absorbs the quantum factor in $g^2$; writing
$g^2=\hbar g_{\rm cl}^2$ restores physical $\hbar$ explicitly.
A single-point Gaussian variance is neither a bound on the field supremum
over a continuum region nor on the whole-interval curvature block norm.
Substitution of $g/(4\pi t)$ into a deterministic kernel hypothesis is
only a model estimate. Even for a Gaussian vector field, its component
variance, radial tail, spatial correlation and continuum supremum require
their own constants; the old scalar exponent $8\pi^2\eta^2/g^2$ and
$V/(8t)^{3/2}$ independent-cell count did not prove such a theorem.
Replacing $g$ by a running coupling is a perturbative suggestion, not a
nonperturbative interacting probability bound.

At $R=\kappa\sqrt{8t}$, the earlier schematic substitution gave
$\exp[g/(2\pi)-2\kappa^2]$ and
$\kappa^2\ge g/(4\pi)+1/2$ for tolerance $e^{-1}$. The exact tail
above additionally has a polynomial prefactor and uses a supremum over
all flow times. These numbers therefore remain illustrative scale
bookkeeping, not a Hamiltonian truncation guarantee at any coupling.
Hamiltonian ground states have configuration probabilities; their
[transfer identity](ground-state-measure-transfer.md) does not turn an
absolute auxiliary kernel bound into the required signed operator comparison.

## Effective spectral reductions

Suppose a scale change constructs effective operators $H^{(n)}$ at
$\ell_n=2^na$, with a specified low-energy subspace, generated
interactions and a spectral comparison. Relative Schur bounds can
ignore a common scalar shift but must control the state-dependent
remainder and the complementary energy denominator; see
[the Feshbach reduction](weak-coupling-feshbach-reduction.md), including its ultraviolet correction. A candidate
truncation must be compared with the exact transformed operator in a
suitable domain and relative-form norm, with constants uniform in volume
and with enough control across the cutoff trajectory. One-loop running
can estimate how many doublings might be needed, but it is not a proof
of the effective action or its arrival in a gapped region.

A state-relative bound, for example
$$\langle\psi,\phi\psi\rangle\le\epsilon\langle\psi,(H-E_0)\psi\rangle
 +\eta\|\psi\|^2$$
on a specified low-energy domain, could exploit more information than a
supremum norm. Such a bound, the relevant probability estimates, and
stability after projection are independent obligations. The
[blocking analysis](blocking-criterion-monotone.md) gives conditional
surface-to-gap comparisons; it does not prove that projection blocking
is always worse at every coupling.

## Consequence for STATE

The canonical flow argument separates exact unitary invariance, local lattice
first derivatives, auxiliary continuum tails, background instability and
relative spectral comparison. The explicit curvature budget controls the
auxiliary kernel only. A projected or blocked Hamiltonian still needs the
inverse metric, density derivatives, signed relative-form error and uniform
iteration estimates. Action descent and free-field statistics provide none
of those hypotheses automatically.
