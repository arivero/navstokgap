# Large gauge fields: action cost, constrained minima and model entropy

**Maintained conclusions.** For a smooth finite-action continuum connection
whose action-decreasing flow exists through $t=\ell^2/8$ with no boundary
flux, a flowed block constraint $\int_B|G_t|^2\ge\eta_F^2$ implies
$S_E/\hbar\ge\eta_F^2/(4g^2)$ in the declared ordered-index norm.
Equality has explicit necessary and sufficient conditions; no admissible
positive-threshold saturating family is constructed.

The constant-background unstable-mode count is a separate phase-space model.
Its charge and real/complex multiplicities give explicit ratios, not a
normalized interacting entropy bound. Finite-regulator compactness gives a
constrained minimum without a coercive Gaussian Hessian. None of these
statements proves local rarity, polymer convergence or a physical spectral gap.
The former claimed convergence threshold is replaced by its actual unproved
weight assumption below. Mathematical source/model checks are internal.

## Continuum action cost and equality

Take $\Omega=\mathbb R^4$ with sufficient decay for the identities below,
or a finite periodic four-dimensional domain, and $B\subset\Omega$ a
cube of side $\ell$. Other boundary conditions are allowed only if they
justify the same dissipation identity without a boundary flux. All
connections under consideration have smooth flow $B_s$ on $0\le s\le t$
and finite action; its curvature is $G_s$, with $G_0=F$.

At $\sqrt{8t}=\ell$, define
$$\mathcal F_\ell(A)=\ell^{-4}\int_B|G_t|^2d^4x,
\qquad K_\eta=\{A:\mathcal F_\ell(A)\ge\eta^2/\ell^4\}.$$
The constraint is gauge invariant. It measures a flowed block $L^2$
norm. It does **not** give a supremum or an adjoint-curvature operator
norm bound. In particular, it cannot be substituted for the curvature
upper bound used in the Jacobian estimates of
[the Jacobian note](flow-jacobian-truncation-error.md) or the corrected
[instability note, §1](flow-jacobian-truncation-error.md#instability-of-the-full-background-generator)
(relevant passages read). The original phrase “up to replacing a
supremum by a block average” concealed an additional estimate; that
identification is withdrawn.

### The bound and its equality conditions

**Proposition 1 (continuum action cost).** Under the assumptions of
Section 1, for every $\ell>0$ and $\eta\ge0$,
$$s(A)\ge\frac{\eta^2}{4g^2}\qquad(A\in K_\eta).$$
The infimum has the same lower bound; if the set is empty its infimum
is understood as $+\infty$.

*Proof.* Use the ungauged flow
$$\partial_s(B_s)_\nu=D_\mu(G_s)_{\mu\nu}=:J_{s,\nu}.$$
Variation of $s=(4g^2)^{-1}\int\sum_{a,\mu,\nu}(G^a_{\mu\nu})^2$
and integration by parts give
$$\delta s=-\frac1{g^2}\int\sum_\nu\langle J_{s,\nu},\delta B_\nu\rangle d^4x,
\qquad \frac{d}{ds}s(B_s)=-\frac1{g^2}\|J_s\|_2^2\le0.$$
The norm in the last display sums the colour and one-form indices.
The factor $1/g^2$ is explicit for this flow-time convention; the old
formula $dS_E/ds=-\|D^*G\|_2^2$ omitted the action prefactor.
The continuum flow convention is the one recorded in
[Lüscher's local companion](../docs/Luscher_WilsonFlow_1006.4518v3.md)
(introductory flow equations, passage read); the displayed variation
checks the normalization directly.

Consequently
$$s(A)\ge s(B_t)=\frac1{4g^2}\int_\Omega|G_t|^2
\ge\frac1{4g^2}\int_B|G_t|^2
\ge\frac{\eta^2}{4g^2}.$$
The second inequality is positivity outside $B$; the last is the
constraint. $\square$

**Scope of uniformity.** The same algebraic bound applies at each
admissible $\ell$ and domain volume; it does not assert flow existence
or regularity uniformly through any limit. It uses a fixed invariant
inner product and action coefficient. Writing the action in this form
for different compact gauge groups gives the same coefficient by
**normalization convention**, not a comparison theorem for their
measures, mode counts or operators. Rescaling the inner product also
rescales the field norm and the threshold. The former claim for every
lattice spacing $a<\ell$ is withdrawn: an exact Wilson-lattice analogue
requires a specified lattice observable, its action comparison and its
flow monotonicity, none of which is proved by this continuum integral.

**Proposition 2 (equality accounting; replacement for withdrawn
sharpness).** For every $A\in K_\eta$ in Proposition 1,
$$\begin{aligned}
s(A)-\frac{\eta^2}{4g^2}
={}&\frac1{g^2}\int_0^t\|J_s\|_2^2ds
+\frac1{4g^2}\int_{\Omega\setminus B}|G_t|^2d^4x\\
&+\frac1{4g^2}\left(\int_B|G_t|^2d^4x-\eta^2\right).
\end{aligned}$$
Each term is nonnegative. Equality therefore holds if and only if all
three vanish: zero flow dissipation, zero flowed curvature outside $B$,
and exact saturation of the block threshold.

*Proof.* Integrate the dissipation identity, split the final action
integral into $B$ and its complement, and subtract the threshold.
Nonnegativity gives the equivalence. For a smooth flow, zero
dissipation entails $J_s=0$ throughout the interval. $\square$

This is an identity and necessary-and-sufficient equality test, **not**
an existence assertion. For $\eta=0$ a flat connection gives equality
when admitted by the domain. For $\eta>0$, neither an equality example
nor a sequence approaching equality is constructed here, so the
optimality of $1/4$ remains unproved. Strict inequality for particular
fields would not itself give a uniform improvement of the infimum.

**Why the old example fails.** Prescribing a nonzero constant abelian
curvature on $B$ and zero outside does not produce a smooth admissible
connection. In that sector the Bianchi identity is $dF=0$, whereas
$d(\mathbf1_B F_{\rm const})$ has nonzero face-supported terms for a
nonzero constant two-form on a bounded cube. A smooth cutoff of the
connection can give an admissible localized field, but then its
curvature includes transition terms whose cost and flow must be
controlled. No such control is supplied by the former example.

Nor does $a/\ell$ control flow at the radius of the block. Already in
the abelian heat-flow model, rescaling $x=\ell y$ leaves the smoothing
time $t/\ell^2=1/8$ fixed. The heat kernel samples a boundary layer of
width comparable with $\ell$, so a relative effect of order one is
possible as $a/\ell\to0$. There is no vanishing cutoff correction
justified by that limit. These observations invalidate the old
sharpness proof without claiming that no other sharpness proof exists.

## Constrained minima and their tangent conditions

**Proposition C (finite regulator only).** Let $G$ be compact, let
$\mathcal E$ be a finite link set, and let $K\subset G^{\mathcal E}$
be closed and nonempty. Every continuous action $s$ attains its minimum
on $K$. If $s$ is real valued, its integral $\int_K e^{-s}d\nu$ is
finite for every finite reference measure $\nu$.

*Proof.* The product and its closed subset are compact. The extreme
value theorem gives a minimum and a finite maximum; $e^{-s}$ is bounded,
so its integral against a finite measure is finite. $\square$

This says nothing about regulator-uniform estimates, the size of a
Gaussian contribution or convergence of a saddle-point expansion.
For a $C^2$ action, a constrained minimum requires nonnegative first
variation along one-sided feasible curves. At a boundary minimum the
first variation need not vanish, so the Hessian need not be
nonnegative on the tangent cone. In a local coordinate, take
$$K=[0,1/4],\qquad s(x)=x-x^2.$$
The minimum is at $0$, with $s'(0)=1$ but $s''(0)=-2$, even though
positive directions belong to the tangent cone. Along a twice
differentiable feasible curve $\gamma$ whose first action derivative
vanishes, the necessary condition is
$$(s\circ\gamma)''(0)
=\operatorname{Hess}s[\dot\gamma,\dot\gamma]
+ds[\ddot\gamma]\ge0$$
in local coordinates. Constraint curvature can matter as well.
At an interior minimum $ds=0$ and the Hessian is nonnegative, but it
can have zero modes: $s(x)=x^4$ has no coercive quadratic term at its
minimum. Gauge degeneracy, boundary geometry, higher terms and
uniform determinant bounds need separate treatment.

The corrected [instability note, §2](flow-jacobian-truncation-error.md#instability-of-the-full-background-generator)
(passage read) supplies a negative quadratic mode for a stationary
constant background in its specified background-transverse sector.
It excludes that background as a constrained minimum only if an
admissible perturbation realizes the descent while remaining in $K$.
No such feasibility proof, or construction of an inhomogeneous
minimizer, is supplied here.

## A constant-background mode count

Use the continuum background-covariant operator of
[the instability note, §2](flow-jacobian-truncation-error.md#instability-of-the-full-background-generator) (passage
read), in four Euclidean dimensions. For one charged complex field,
with charge magnitude $q>0$ relative to $T^3$, its transverse
polarizations have eigenvalues
$$\omega^2=k_3^2+k_4^2+(2n+1)qb\mp2qb.$$
Only $n=0$ with aligned spin is negative, for
$k_3^2+k_4^2<qb$. Neutral components have no such branch.

*Landau degeneracy.* The transverse density per unit area is
$qb/(2\pi)$. For example, in Landau gauge with transverse length
$\ell$ and periodic second coordinate, momenta are spaced by
$2\pi/\ell$. Guiding centres are therefore spaced by
$2\pi/(qb\ell)$, giving that density. On a magnetic torus with
compatible flux, $qb\ell^2/(2\pi)$ is an integer degeneracy.
For a block cut from the plane it is a bulk density, not an exact
boundary-condition-independent count.

*Longitudinal count.* Replacing a momentum sum by its phase-space
integral gives
$$\left(\frac\ell{2\pi}\right)^2
\operatorname{area}\{k_3^2+k_4^2<qb\}
=\frac{qb\ell^2}{4\pi}.$$
Thus the **phase-space estimate**, in complex dimension, is
$$\mathcal N_{\mathbb C}^{\rm ps}(q)
=\frac{q^2b^2\ell^4}{8\pi^2}
=\frac{q^2\eta_b^2}{8\pi^2}.$$
An exact periodic longitudinal count, when the magnetic flux and
boundary conditions admit this background, would instead be
$$\mathcal N_{\mathbb C}^{\rm box}(q)
=m_q\,\#\{n\in\mathbb Z^2:4\pi^2|n|^2<q\eta_b\},
\qquad m_q=\frac{q\eta_b}{2\pi}\in\mathbb N.$$
The disc area is an approximation to this integer count, justified
as $q\eta_b\to\infty$: unit squares around the integer points place
it between disc areas with radii differing by a bounded constant.
It is not justified merely by sending $\ell/a\to\infty$ at fixed
$\eta_b$. A lattice operator also has dispersion and cutoff effects;
no uniform lattice replacement is proved here.

**Real and colour multiplicities.** A charged pair of real adjoint
components forms one complex field. Each complex mode has two real
amplitudes, so its real negative-space dimension is twice the complex
count. Take the usual $SU(3)$ generator
$$T^3=\operatorname{diag}(1/2,-1/2,0).$$
The matrix units satisfy
$[T^3,E_{ij}]=(t_i-t_j)E_{ij}$, where $t_i$ are its diagonal entries.
The three conjugate root pairs therefore have charge magnitudes
$1,1/2,1/2$. Each pair is counted once as a complex field; adding
its conjugate again would double-count it. Consequently
$$\begin{aligned}
\mathcal N_{\mathbb C,SU(3)}^{\rm ps}
&=(1+1/4+1/4)\frac{\eta_b^2}{8\pi^2}
=\frac{3\eta_b^2}{16\pi^2},\\
\mathcal N_{\mathbb R,SU(3)}^{\rm ps}
&=\frac{3\eta_b^2}{8\pi^2}.
\end{aligned}$$
These are estimates for this background and operator sector, not a
mode count for every large-field configuration or a gauge-fixed
functional determinant calculation.

## Action versus model count: the norm and multiplicity matter

The continuum action inequality above uses the ordered-index $L^2$ threshold $\eta_F$; the spectral model instead uses $\eta_b=b\ell^2$.

The spectral parameter $\eta_b=b\ell^2$ of Section 2 is not
implicitly $\eta_F$. To compare them in the homogeneous model, fix
the colour norm by $\langle T^3,T^3\rangle=1$ (equivalently
$2\operatorname{tr}[(T^3)^2]=1$ in the Hermitian convention), and
absorb the coupling into the curvature. With $F_{12}=bT^3$,
$F_{21}=-bT^3$ and all other components zero,
$$|F|^2=2b^2,\qquad
\eta_F^2=2\eta_b^2,\qquad
s_B:=\frac1{4g^2}\int_B|F|^2
=\frac{\eta_b^2}{2g^2}.$$
Here $s_B$ is the block action of the background, not the minimum
action for an arbitrary constrained field. No finite-action localization
or admissible boundary construction follows from this calculation.

**Proposition M (model ratios, not entropy bounds).** For $\eta_b>0$
and the preceding normalization, division by the phase-space counts
of Section 2 gives the following identities:

| count convention | phase-space count | $s_B/\mathcal N^{\rm ps}$ |
| --- | --- | --- |
| one unit-charge complex field | $\eta_b^2/(8\pi^2)$ | $4\pi^2/g^2$ |
| its real directions | $\eta_b^2/(4\pi^2)$ | $2\pi^2/g^2$ |
| all three $SU(3)$ charged pairs, complex | $3\eta_b^2/(16\pi^2)$ | $8\pi^2/(3g^2)$ |
| all three $SU(3)$ charged pairs, real | $3\eta_b^2/(8\pi^2)$ | $4\pi^2/(3g^2)$ |

*Proof.* Substitute the counts and $s_B=\eta_b^2/(2g^2)$, and cancel
$\eta_b^2$. $\square$

The original arithmetic
$$\frac{\eta_b^2/(4g^2)}{\eta_b^2/(8\pi^2)}
=\frac{2\pi^2}{g^2}$$
remains a formal identity if the numerator is an **assumed** cost
$s_{\rm old}$. It paired the ordered-index $L^2$ threshold formula
with the different spectral threshold without their conversion.
Under the normalization above, the same number occurs for one pair's
real directions, not its complex count. None of these ratios is a
universal entropy coefficient. Scale cancellation at fixed $\eta_b$
and $g$ does not establish cutoff uniformity or running-coupling control.

**The missing weight estimate.** For a finite regulator with reference
probability measure $\nu$ and $d\mathbb P=Z^{-1}e^{-s}d\nu$, an action
floor $s\ge Q$ on an event $K$ gives only
$$\mathbb P(K)\le Z^{-1}e^{-Q}\nu(K).$$
The denominator needs control relative to the constrained numerator.
The negative eigenspace dimension at one saddle controls neither this
ratio nor the volume of a region, its nonlinear integration, or the
number of possible regions. Compactness at a fixed regulator provides
no uniform factor per mode.

To preserve the former calculation's scope explicitly, **if one
assumed** a weight bound
$$W(\eta_b)\le e^{-s_{\rm old}}e^{C\mathcal N_{\mathbb C}^{\rm ps}(1)},
\qquad s_{\rm old}=\frac{\eta_b^2}{4g^2},\qquad C>0,$$
then algebra would give
$$W(\eta_b)\le
\exp\left[-\frac{\eta_b^2}{4g^2}
\left(1-\frac{Cg^2}{2\pi^2}\right)\right].$$
Its exponent is negative for $g^2<2\pi^2/C$. Neither the assumed
weight estimate nor a regulator-independent $C$ is proved. The old
numerical threshold $g^2<2\pi^2$ additionally set $C=1$ without
justification. This display is **conditional bookkeeping**, not a
convergence theorem. Even an actual tail in strength would need
region-counting and interaction estimates to sum polymers.

## Consequence for STATE

Retain the continuum inequality and equality test, the Bianchi counterexample
to the former saturation construction, the finite-regulator tangent-cone
counterexample and the explicitly normalized charged-background counts.
A block $L^2$ threshold supplies no upper curvature norm. The flow's action
descent also compares times on one field, not block functionals of two initial
fields. Normalized local weights, boundary-uniform integration and polymer
summation remain open. The [operator comparison](large-field-operator-inequality.md)
needs separate sign and localization estimates even if a measure bound is
subsequently established.
