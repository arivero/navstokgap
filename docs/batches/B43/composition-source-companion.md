# B43 source companion: minimax composition

## Scope and coverage

Bounded audit for R12, 2026-09-11. Two primary sources were used: (1) Richard
Seeber and Hernan Haimovich, “Optimal Robust Exact Differentiation via Linear
Adaptive Techniques,” *Automatica* 148 (2023) 110725, arXiv:2111.12638v2,
https://arxiv.org/html/2111.12638v2; reused from B42 at §3.1 Proposition 3.1
and proof (HTML lines 231–257), §4 Lemma 4.3 (364–372), and §4 Theorem 4.1
and proof (339–350, 374–379), passage coverage. (2) Sipu Ruan and Gregory
S. Chirikjian, “Closed-Form Minkowski Sums of Convex Bodies with Smooth
Positively Curved Boundaries,” arXiv:2012.15461v2 (12 October 2021), https://arxiv.org/html/2012.15461v2,
§3.1 and §4, especially Theorems 4.1/4.3 (v2 equations (1)–(2), Theorem 4.1 equation (9), and Theorem 4.3 equation (18)), passage coverage. The second source assumes smooth strictly
positively curved bodies, so it is geometric support for the Minkowski-sum
operation rather than an exact theorem about R12's arbitrary compact fibres.
No numerical or symbolic verification was performed.

## Result-by-result audit

### 1. Product central-fibre scalar minimax radius

Seeber–Haimovich directly establishes the one-body bounded-curvature hidden-pair
and sharp differentiator radius `2 sqrt(NL)` (Proposition 3.1; Lemma 4.3 and
Theorem 4.1). With `L=F/m`, `N=epsilon`, this is the source match used by
R12's constituent radii. Ruan–Chirikjian defines and computes Minkowski sums of
convex bodies and proves the boundary parametrizations under smooth curvature
hypotheses (§4). This supports the geometric interpretation that a product
compatible fibre under a linear scalar target has additive support/radius. The
exact formula `r(sum a_i L_i)=sum |a_i| r_i` for Cartesian central fibres,
including the sign-aligned extremizer argument, is derived in R12; neither
source states this minimax theorem. The compactness/central-symmetry hypotheses
must remain explicit.

### 2. Canonical centre/relative radii and identical-copy extensive H

No source read gives the mass-weighted centre/relative coordinate formulas or
the canonical risk product. These follow algebraically from the result in §1
and the definitions of `R`, `r`, `P`, and reduced mass. The identical-copy law
`H_R=n H_1` is therefore a derived consequence of retaining all records and
allowing aligned adversarial errors. It is not a variance-composition result;
Seeber–Haimovich is deterministic worst-case differentiation, while the A08
companion's law concerns second moments. Ruan–Chirikjian's Minkowski addition
result is only an antecedent for additive support functions, not a direct match
to the mechanical centre/relative formulas. No novelty claim is made.

### 3. Exact aggregate-record image and strict Cauchy–Schwarz loss

Neither source treats the aggregate record map `Y=sum m_i y_i/M` or the force/error
image equality. R12's converse construction, proportional force and error
splitting, is a self-contained derived result and depends on independent bounds
and freely selectable constituent forces/errors. The inequality
`sum sqrt(m_i F_i epsilon_i) <= sqrt((sum F_i)(sum m_i epsilon_i))` is the
standard Cauchy–Schwarz deduction written in R12; strictness follows unless
`F_i/(m_i epsilon_i)` is constant. It should not be presented as a source
match. The Seeber–Haimovich radius supplies the single aggregate double-
integrator value after image reduction, conditional on the proven image and
horizon condition.

### 4. Mass-only radius closure

No direct source match was found within this bounded audit. Under the stated
closure premises, `f(m)=mQ(m)` and `P(m)` are nonnegative additive functions on
positive reals; monotonicity from nonnegativity and rational squeezing yield
`Q(m)=q_*`, `P(m)=p_*m`, hence `H(m)=q_*p_*m`. This is a written derivation
and an A08-style reuse, not an independently sourced theorem in B43. The
additional demand that `H` itself be mass independent is incompatible with
positive identical-copy composition and forces zero. The fixed acceleration,
common precision example realizes the extensive closure but leaves its value
preparation-supplied.

## Search boundary and model suggestion

One discovery query was used (`site:arxiv.org support function Minkowski sum
convex bodies theorem`) and one returned primary paper was inspected. Together
with the reused B42 source this is bounded coverage, not an exhaustive
prior-art search and cannot establish novelty. Source-to-model suggestion:
formulate the product experiment as a Minkowski sum of the one-dimensional
target images of compatible fibres, then test which physical coupling or shared
error constraint destroys Cartesian-factor additivity; this directly probes
whether extensive `H` survives beyond freely composable adversarial inputs.


## Coordinator source review

Pinned the geometry source to v2, 12 October 2021, published in
*Computer-Aided Design* 143 (2022), 103133. The unversioned HTML route failed
with HTTP 406; v2 worked. Verified §3.1 equations (1)–(2), §4.1 Theorem 4.1
and equation (9), and §4.2 Theorem 4.3's statement, equation (18), with its
additional parametrization premise. These supply geometric context only;
R12 uses its own elementary support proof, with no smoothness assumption.
Re-read Seeber–Haimovich v2 Proposition 3.1 (10)–(12), Lemma 4.3 and Theorem
4.1 proof. Its lower bound uses a supremum over future times; R11's explicit
shifted pair and the common preparation horizon justify the fixed-T statement
used in R12. No new source search or computational verification was needed.
The worker's passage-count assertion is retained as unverified in its handoff;
three differentiation and three geometry selections are listed across two
sources, with the former also available in the reused B42 capsule.
