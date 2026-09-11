# B54: final clock momentum and global recovery

## Result and bounded coverage

The sole permitted primary source supplies the standard perturbation method
needed for C102: an invertible reference map plus a perturbation with a strict
Lipschitz margin has a Lipschitz inverse. It also supplies the local inverse
function theorem. This supports the *method* behind R23's global lower
Lipschitz estimate, but it does not establish the apparatus-specific leading
map, its uniform speed-dependent margin, the clock reaction formula, or the
canonical risk closure. No exact novelty conclusion is made.

## Primary source and reading

Alberto Freire, *Inverse Function Theorem and Surfaces in R^n*, University of
Tennessee lecture notes, PDF (date and DOI not established):
<https://web.math.utk.edu/~afreire/teaching/m447f16/InverseFunctionTheorem.pdf>.

The authorized three-page reading was PDF pp. 1–3. On pp. 1–2, the notes
consider `f(x)=Ax+phi(x)` with boundedly invertible `A` and Lipschitz `phi`;
the contraction argument requires `Lip(phi) < ||A^-1||^-1` and yields the
inverse estimate `Lip(f^-1) <= ||A^-1||/(1-lambda)`, with
`lambda=||A^-1|| Lip(phi)`. Proposition 1 on p. 3 states the corresponding
homeomorphism and Lipschitz-inverse result. The inverse-function theorem on
p. 3 gives a *local* bi-Lipschitz conclusion when the derivative is invertible
and the Taylor remainder has a sufficiently small Lipschitz constant.

Evidence level: passage. Only these three pages count; no full-read,
exhaustive prior-art, or metadata claim beyond the displayed institutional
title/author/URL is made.

## Claim-by-claim audit

**C102 (nine final records recover receiver state, incoming positions and
initial clock speed globally on the selected convex domain): partial
established-method match, model-derived result.** Freire supports the
segment/contraction principle used after writing the record map as a uniformly
invertible reference plus a `C^1` remainder. R23's leading map
`L(z,q,v)=(-A_v z,q,v)` is not a fixed linear map, so its lower bound must be
proved separately: the explicit `v` block controls `|v-v'|`, the `q` block
controls `||q-q'||`, and the stated uniform bound on `A_v` and its speed
variation controls `||z-z'||`. The resulting `beta` is a model-specific
calculation. Freire does not verify the Hamiltonian pulse equations, the
formula for the persistent clock reaction, compact-domain cutoff/existence
margins, or the uniform `||R_lambda||_{C^1}=O(lambda)` estimate. The smallness
condition must be imposed on the complete remainder relative to `beta`, not
identified with the source's contraction parameter.

**C103 (finite-precision minimum-residual recovery and canonical risk product):
no exact match in this budget; derived consequence conditional on C102.** The
source's inverse Lipschitz estimate permits the residual-to-state step once
the exact record map has the asserted global lower bound. The factor arising
from two record residuals and the conversion from dimensionless coordinates to
canonical units remains R23's own estimator argument. Freire does not discuss
noisy records, minimum-residual existence on compact admitted sets, coordinate
risk products, or action scales. Thus closure as record errors tend to zero at
fixed positive coupling is model-derived and retains the stated preparation,
exact-model, and joint-record-access assumptions; it is not a universal
positive-action result.

## Source-to-model idea and next bounded test

Coordinator re-read PDF pp. 1–3, including the inverse estimate and Proposition
1, with visual checking of p. 3. The source supplies the linear-reference
perturbation method; R23's nonlinear-reference lower bound is proved directly.
The institutional attribution is inherited from B52; no date or DOI is added.

The source suggests treating the full nine-record map as a perturbation of its
uniformly coercive leading map and recording the strict margin explicitly.
For R24, hide the initial clock offset and add the final clock position as
well as retaining final clock momentum. The leading clock block is
`(s,v) -> (s+vT,v)`, whose inverse is explicit for fixed `T`; test whether the
coupled ten-record map remains a uniformly small perturbation on convex clock,
receiver, and probe boxes. This is a proposed model test, not a source claim.
