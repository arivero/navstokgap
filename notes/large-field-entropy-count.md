# Constant-background unstable-mode counting does not bound large-field entropy

Later corrections: [the action lower-bound note, §§2--4](large-field-action-lower-bound.md) and [the transfer note, §3](ground-state-measure-transfer.md#3-action-cost-at-a-block-scale-not-a-probability-theorem) distinguish action cost from normalized probability and field thresholds; [the instability note, §§2--4](flow-instability-large-field.md) corrects the growth rate and withdraws sharp truncation claims (relevant passages read).

> **Correction (2026-10-02, GPT-6 Astra).** The former claims that the
> entropy question is settled, that the large-field sum converges for
> $g^2<2\pi^2$, and that the expansion is merely slow are **withdrawn**.
> The assumed bounded factor per unstable mode was not proved and is
> not a count of regions or polymers. Compactness proves existence of a
> finite-lattice constrained minimizer, not a controlled Gaussian
> expansion; the assertion that its Hessian is nonnegative on the whole
> tangent cone was false. The assertion that the minimizer must be
> inhomogeneous is also withdrawn: a saddle direction must be feasible
> for the particular constraint. The count $\eta^2/(8\pi^2)$ survives
> only as a phase-space estimate for one unit-charge complex field,
> with $\eta=gB\ell^2$, not an exact finite-box count. Real directions
> double that estimate and $SU(3)$ has two additional charged pairs.
> The old ratio $2\pi^2/g^2$ divided an assumed cost by this model
> count; it is not a general action/entropy theorem. Section 3 fixes
> the field-norm and multiplicity conventions explicitly. The old net
> exponent is retained as conditional bookkeeping only.

**Abstract / result.** For a constant abelian chromomagnetic background,
write $b=gB>0$ for the curvature seen by a unit-charge component and
$\eta_b=b\ell^2$. One complex charged field has unstable-mode
phase-space count
$$\mathcal N_{\mathbb C}^{\rm ps}
=\frac{b\ell^2}{2\pi}\frac{b\ell^2}{4\pi}
=\frac{\eta_b^2}{8\pi^2}.$$
This counts the lowest aligned Landau branch with
$k_3^2+k_4^2<b$. It has no explicit block-size factor at fixed
$\eta_b$, but is a continuum density approximation, with boundary,
flux and momentum discreteness qualifications. It is not a uniform
lattice estimate or a bound for inhomogeneous backgrounds. The
continuum flowed-block action floor $\eta_F^2/(4g^2)$ is a separate
result with its own $L^2$ threshold $\eta_F$ and flow assumptions.
Neither ingredient proves normalized large-field rarity, an entropy
bound, polymer convergence or a continuum mass gap.

## 1. Compactness gives a minimizer, not a Gaussian expansion

**Proposition 1 (finite regulator only).** Let $G$ be compact, let
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

The corrected [instability note, §2](flow-instability-large-field.md)
(passage read) supplies a negative quadratic mode for a stationary
constant background in its specified background-transverse sector.
It excludes that background as a constrained minimum only if an
admissible perturbation realizes the descent while remaining in $K$.
No such feasibility proof, or construction of an inhomogeneous
minimizer, is supplied here.

## 2. Counting the unstable directions in a specified background

Use the continuum background-covariant operator of
[the instability note, §2](flow-instability-large-field.md) (passage
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

## 3. Action cost against model count: fix the normalization first

The corrected [transfer note, §3](ground-state-measure-transfer.md#3-action-cost-at-a-block-scale-not-a-probability-theorem)
and [action note, §2](large-field-action-lower-bound.md) (passages
read) use
$$s(A)=\frac{S_E[A]}{\hbar}=\frac1{4g^2}\int_\Omega|F|^2d^4x,$$
where the norm sums colour and **ordered** spacetime indices.
For a smooth finite-action field admitting action-decreasing flow
through $t=\ell^2/8$, with no boundary flux in the dissipation identity,
the constraint $\int_B|G_t|^2\ge\eta_F^2$ gives
$$s(A)\ge s(B_t)\ge\frac1{4g^2}\int_B|G_t|^2
\ge\frac{\eta_F^2}{4g^2}.$$
This is a classical continuum action inequality, not a normalized
measure bound. Its equality or sharpness is not established by a
constant field supported only on a block.

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

**Proposition 2 (model ratios, not entropy bounds).** For $\eta_b>0$
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

## 4. What survives and what remains open

*Survives.* Finite-lattice compactness, the constant-background spectrum,
and the phase-space counts with the stated boundary, charge and real
multiplicity conventions. The separate continuum action floor survives
under its flow and boundary assumptions. Ratios in Proposition 2
compare two background model quantities.

*Withdrawn.* The inference that suppression beats large-field entropy,
the convergence threshold, the claim that the expansion is merely slow,
and the assertion that the remaining task is only to identify an
inhomogeneous minimizer. The saddle calculation does not determine
the geometry of a constrained minimizer or its Gaussian order.

*Open estimates.* A normalized local large-field weight bound with
volume, cutoff and boundary dependence; control of inhomogeneous
fields and their integration; summability over locations, shapes and
interacting polymers; and, if a constrained expansion is used,
feasibility, gauge treatment and control of its nonquadratic terms.
The former proposed weight
$\exp[-\eta_b^2(1-O(g^2))/(4g^2)]$ is at most a heuristic target
under the old cost convention, not a prediction of Proposition 2.
A measure estimate would still not supply the signed Hamiltonian
comparison discussed in [the operator-inequality note, §3](large-field-operator-inequality.md#3-the-sign-of-a-rare-perturbation)
(passage read).

## 5. Consequence for STATE

Retain the constant-background phase-space model and explicitly
normalized ratios, alongside the separate continuum action floor.
Large-field entropy control, normalized rarity, a controlled Gaussian
expansion and polymer convergence remain open here; the earlier
closure and weak-coupling convergence claims are withdrawn. No
continuum $SU(3)$ construction or mass gap follows. This section
specifies the corrected scope for the caller's STATE and catalog
updates; those files are unchanged in this task.
