# Gaussian tails for a covariant linearized flow; Hamiltonian truncation remains open

Later corrections: [the instability note](flow-instability-large-field.md) withdraws exact sharpness; [the lattice note](lattice-truncation-uniform.md) separates one lattice step from fixed-scale continuum bounds; [the operator-inequality note](large-field-operator-inequality.md) supersedes the fixed-range competition in [the transfer note](ground-state-measure-transfer.md).

> **Correction (2026-10-02).** The original title, lead and Corollary 3
> identified a Gaussian Jacobian-kernel tail with a relative error of the
> conjugated Hamiltonian and claimed it was small **exactly** on small
> fields. Those operator and only-if claims are **withdrawn**. The
> Nielsen--Olesen example grows at $gB$, not $2gB$, and supplies no spatial
> tail lower bound. Proposition 1 now retains the variation of Lüscher's
> gauge term; the simple covariant heat equation is a separately specified
> background-covariant linear evolution, not the unrestricted Jacobian
> of that gauge-modified flow. Proposition 2 uses the full curvature
> block-operator norm and time-dependent propagators. Sections 3--4 give
> an absolute kernel-tail bound, with its prefactor, rather than an
> operator relative bound. The lattice-step claim at one flow radius,
> the scale substitution and the reversed free-smoothing comparison are
> corrected below. The claim that Hamiltonian methods have no access to
> configuration probabilities is also withdrawn.

For a smooth compact-Lie-algebra connection on $\mathbb R^3$, consider
specifically the linear evolution
$$\partial_s u_\mu=D(s)^2u_\mu+2[G_{\mu\nu}(s),u_\nu],
\qquad D_\mu=\partial_\mu+[B_\mu,\cdot].$$
It is obtained by adding a background-covariant gauge term to the
ungauged linearization. Its propagator $J(t,0)$ has a Gaussian kernel
majorant under the regularity and bounded-curvature hypotheses of
Section 2. Define the pointwise curvature operator on vector fields by
$$(\mathcal C(s,x)u)_\mu=\sum_{\nu=1}^3[G_{\mu\nu}(s,x),u_\nu],
\qquad \Gamma(s)=\sup_x\|\mathcal C(s,x)\|_{\rm op},
\qquad A_t=2\int_0^t\Gamma(s)\,ds.$$
Then
$$\|J(t,0;x,y)\|_{\rm op}\le e^{A_t}
\frac{e^{-|x-y|^2/(4t)}}{(4\pi t)^{3/2}}.$$
For $R=\kappa\sqrt{8t}$ the absolute discarded kernel mass is bounded by
$$e^{A_t}\left[\operatorname{erfc}(\sqrt2\kappa)
+\frac{2\sqrt2\kappa}{\sqrt\pi}e^{-2\kappa^2}\right].$$
This is a sufficient range/curvature budget for this linear evolution.
It is not a necessary small-field condition, a bound on the actual
Jacobian in every gauge, or a relative form estimate for a conjugated
kinetic operator. No continuum construction or mass gap follows.

> **Sharpness corrected (2026-10-02).** In the constant chromomagnetic
> model of [the instability note](flow-instability-large-field.md), §2
> (full-read), $\Gamma=b=gB$, the curvature term has eigenvalue $2b$, but
> the covariant Laplacian contributes $-b-k_\parallel^2$ on that mode.
> The full growth rate is $b-k_\parallel^2$. This does not saturate
> $e^{2bt}$ or prove a lower bound on the discarded spatial tail.

> **Lattice scope corrected (2026-10-02).** Even granting the earlier
> schematic normalization $a^2\Gamma\le\pi$, at $t=a^2/2$ and
> $R=\sqrt{8t}$ the exponent budget is $\pi-2>0$, not small. Compactness
> gives a finite coefficient budget, not accuracy at one flow radius.
> Increasing $\kappa$ controls the continuum majorant for any fixed
> finite budget; merely taking $\kappa>1$ is not a specified accuracy
> guarantee. [The lattice note](lattice-truncation-uniform.md), §§1--4
> (full-read), discusses bounded coefficients and longer lattice range.
> A plaquette-angle bound is not by itself a proof of the above
> continuum block-norm bound or a lattice Hamiltonian relative bound;
> those require their own normalization and operator estimates.

## 1. The linearized flow and its gauge convention

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
used in Sections 2--4. Identifying it with another flow Jacobian
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

## 2. The Gaussian bound

Equip the compact Lie algebra with an invariant positive inner product,
and its vector fields with $|u|^2=\sum_\mu|u_\mu|^2$. The connection is
metric-compatible because $\operatorname{ad}(B_\mu)$ is skew-adjoint.
Assume $B(s,x)$ is smooth on $[0,t]\times\mathbb R^3$, with bounded
coefficients and spatial derivatives sufficient for the covariant
parabolic propagators and kernels below, and assume
$\Gamma\in L^1([0,t])$. These are hypotheses, not estimates derived
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

## 3. Absolute kernel tails, not Hamiltonian relative errors

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
[the flow-conjugation note](flow-conjugation-truncation.md), §§1--3
(full-read), involves quadratic Jacobian combinations and inverse
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

## 4. The sufficient small-field budget and its limits

Write $\ell=\sqrt{8t}$. If the block norm satisfies
$$\Gamma(s)\le\frac\eta{\ell^2}\quad(0\le s\le t),$$
then $A_t\le\eta/4$ and Corollary 3 yields
$$\|J-J_R\|_{2\to2}
\le\left(1+\frac{2\sqrt2\kappa}{\sqrt\pi}\right)
\exp\left[\frac\eta4-2\kappa^2\right].$$
The original $2\eta$ growth exponent in this substitution was incorrect.
In component norm, the hypothesis $g_*\le\eta/\ell^2$ gives instead
$A_t\le\eta/2$ in three dimensions by the index bound of Section 2.

| regime or question | supported conclusion |
| --- | --- |
| bounded curvature budget $A_t$, sufficiently long range | absolute auxiliary kernel tail is below a prescribed tolerance |
| small $\eta$ at one fixed flow radius | bounded tail, with no arbitrarily small accuracy implied |
| large $A_t$ at fixed range | this upper bound deteriorates; actual tail size remains undetermined |
| larger range at finite $A_t$ | the kernel majorant can be made small |
| conjugated Hamiltonian or iterated RG | relative form and iteration estimates remain open |

This budget motivates comparison with small/large-field splitting in
constructive renormalization, but neither forces that split nor controls
all steps of [the flow-conjugation route](flow-conjugation-truncation.md).
The comparison to Balaban's series (Commun. Math. Phys. 122 (1989) 355,
metadata level) is context, not a derivation of its hypotheses. No
unproved decay of a "typical" interacting curvature is used here.

## 5. What action monotonicity controls

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

## 6. Consequence for STATE

The surviving result is a Gaussian majorant and explicit absolute
kernel-tail budget for the specified background-covariant linear
parabolic evolution, with a full vector curvature norm and a
flow-interval bound. Small fields give a sufficient budget at suitable
range; neither necessity nor sharpness is proved. The identification
with Lüscher's unrestricted flow Jacobian and the conversion to a
relative Hamiltonian truncation error remain open, as do lattice
normalization, inverse-metric and density-derivative control and
iteration. Single-step compact lattice bounds must be distinguished
from fixed-scale continuum estimates. This correction supplies no
continuum $SU(3)$ construction or mass gap. STATE and the catalogs are
left to the caller, as requested.
