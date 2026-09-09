# B28 audit: relativistic Kepler threshold and softened core

## Finding

The singular-core calculation in `notes/relativistic-kepler-threshold.md` is
mathematically adequate for the stated one-body Hamiltonian. The threshold
$g_\theta=k/c$ follows from the effective radial function and Boyer's
classification; it is an established benchmark. The softened-core conclusion
$g_\theta(a)=0$ for every fixed $a>0$ is an elementary derived consequence
of compact sublevels below the escape energy, rather than a literature
claim. It shows that the positive infimum depends on retaining the singular
core.

## Proof audit

For fixed (ell=|L|>0),

\[
 U_{a,\ell}(r)=\sqrt{m^2c^4+c^2\ell^2/r^2}-k/\sqrt{r^2+a^2}
\]

is continuous on (r>0), tends to (+\infty) as (r\downarrow0), and has

\[
 U_{a,\ell}(r)=mc^2-k/r+\ell^2/(2mr^2)+O(r^{-3})
\]

as (r\to\infty). Hence it is below (mc^2) for all sufficiently large
finite (r), while the endpoint limits are $+\infty$ at zero and $mc^2$ at infinity. Restricting to a
closed finite interval containing such a point gives an attained global
minimum at some (r_*>0). At (p_r=0), (r=r_*), and
(U'_{a,\ell}(r_*)=0), Hamilton's equations give a complete circular orbit.
This alone proves that the infimum over positive angular actions is zero:
for every \(\ell>0\) there is an admissible regular bound orbit, and
\(\ell\downarrow0\) is allowed.

The note's stronger statement for energies (U_{a,\ell}(r_*)<E<mc^2) is
also valid after one explicit qualification: the connected component of the
sublevel set containing the minimum is compact because (U_{a,\ell}	o
\infty) at both radial ends. Its radial motion has finite turning points and
the smooth vector field extends globally on that compact annulus. No
uniqueness of the minimum is needed. This stronger statement is unnecessary
for (g_\theta(a)=0), so the result should lead with the circular-orbit
argument and retain the energy-family claim as an optional addendum.

The singular proof correctly identifies a strict endpoint. For
(F_\ell(x)=\sqrt{m^2c^4+c^2\ell^2x^2}-kx), convexity and the endpoint
derivatives give a finite well exactly when \(c\ell>k\). At equality the
infimum is approached only at the excluded collision (r=0). Below equality,
the inward branch reaches the centre in finite time under the displayed
energy identity, so collision continuation cannot be counted as a regular
trajectory. Boyer's pp. 5, 6, 9 and 10 establish the corresponding
classification; the local compactness and endpoint-time arguments supply the
precise adopted domain.

The (a\downarrow0) argument is valid but should state its quantifiers. For
each fixed (0<\ell<k/c), choose (y) so that
\(c\ell/y<k/\sqrt{1+y^2}\). Then the value at (r=ay) is of order
\(a^{-1}\) with negative coefficient, forcing minimizing radii below every
fixed \(\delta>0\) as (a\downarrow0). This is pointwise in \(\ell\), not a
uniform statement over all subcritical \(\ell\). The singular and softened
models therefore have different domains in the limit; one cannot infer
continuity of admissible trajectories from pointwise convergence of potentials.

## Literature coverage

B27 remains the controlling primary audit: Timothy H. Boyer, “Unfamiliar
trajectories for a relativistic particle in a Kepler or Coulomb potential,”
American Journal of Physics 72 (2004), DOI
`10.1119/1.1737396`, arXiv `physics/0405090v1`,
<https://arxiv.org/abs/physics/0405090v1>. Its exact passage coverage is the
four PDF pages recorded in the B27 companion, including Eqs. (19)--(20) and
(37)--(42). It supports the singular (k/c) threshold and plunge endpoint.

Within this bounded B28 audit, two web discovery queries were used, targeting
“softened relativistic Coulomb/Kepler potential” and regularized angular
momentum thresholds. Results included general relativistic Kepler and
softening references, but no directly matching primary passage for the exact
potential \(-k/\sqrt{r^2+a^2}\). No additional primary page was used. This is
bounded search coverage and does not support a claim that the softened result
is novel.

## Source-to-next-task suggestion

A15 should use the circular orbit as the minimal confined preparation and keep
the angular action \(|L|\) separate from a fluctuation estimator. If it needs
a noncircular family, state the compact connected radial component and energy
window explicitly. A16 should vary (k) and (a) separately: (k/c) is a
coupling-supplied action scale in the singular model, while fixed (a>0)
destroys the positive threshold. Neither result supplies a universal action
constant or a physical-time attraction law.

## Coordinator review

Corrected the worker's erroneous claim of divergence at both radial ends:
the limit at infinity is $mc^2$, and the strict energy ceiling ensures compact
sublevels. Checked the minimum, radial energy identity, finite collision-time
integrals, Newtonian limit and fixed-subcritical core-collapse quantifiers
against the written argument. The note already used the correct limits.
