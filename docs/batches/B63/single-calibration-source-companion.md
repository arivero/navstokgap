# B63: one uncertain calibration and local inverse fibres

## Result and bounded coverage

Freire's inverse-function handout gives a direct method match for R32 stage 1:
a parameter-dependent perturbation of an invertible linear map has a local
inverse on a fixed image neighbourhood when the contraction margin is uniform.
It supports the construction of the curve (w_{lambda,j}(s)), but does not
establish the R30 pulse matrix, its four independent rows, or the Hamiltonian
apparatus map. The endpoint-risk lower bound is deterministic and model-derived;
it is not a stochastic-error result. Exact model matching and novelty remain
unassessed.

Coverage: one specified primary retrieval, no discovery queries. Alberto
Freire, *Inverse Function Theorem and Surfaces in R^n*, PDF pp. 1--3,
https://web.math.utk.edu/~afreire/teaching/m447f16/InverseFunctionTheorem.pdf.
Metadata and the displayed perturbation estimate, invariant-ball argument,
Proposition 1, and the inverse-function theorem proof were read at passage
level on pp. 1--3 using text extraction. No full-source read or exhaustive
prior-art search is claimed; extraction was not used for any unverified visual
formula detail.

## Source methods and audit

On pp. 1--2 Freire writes (f(x)=Ax+\phi(x)), assumes (A^{-1}) bounded and

\[
\|A^{-1}\|\operatorname{Lip}(\phi)<1,
\]

then obtains the inverse Lipschitz bound
\(\|g(y)-g(\bar y)\|\leq \|A^{-1}\|\|y-\bar y\|/(1-\lambda)\).
The invariant closed-ball estimate chooses a fixed image radius from the
contraction margin. Proposition 1 (p. 3) states the resulting local/global
homeomorphism alternatives, while the theorem proof applies the perturbation
argument in a sufficiently small neighbourhood of an invertible derivative.

Applied to R32, take the receiver variable (w), parameter
\((\lambda,a_\lambda)), and map (T_\lambda(w)). R30's uniform derivative margin
and smooth parameter dependence are the hypotheses needed to choose one image
interval \(|s|\le s_0\) for all sufficiently small \(\lambda\). Restricting the
coordinate image to (s e_j) gives the one-dimensional fibre and
\(\partial_s w_{\lambda,j}(0)=J_\lambda^{-1}e_j\): the relevant direction is
the (j)-th inverse-response column, not a generic missing-constraint count.

With exact final records, the two endpoints (s=\pm\min(s_0,\epsilon/\lambda))
are admissible deterministic alternatives. If both canonical components of
the column are nonzero and retain a uniform sign, their endpoint separations
give the stated product lower bound. Freire supports the fixed-neighbourhood
inverse step only; endpoint admissibility, apparatus-box margins, energy-ball
membership, and the minimax estimator argument are R32 derivations.

## Inherited B62 method match and proof issues

Werschulz's B62 audit supplies the radius-of-information interpretation. For
each scalar coordinate here, half the diameter of a compact compatible image
is its optimal worst-case error, attained by the midpoint of its extrema.
This transfers to
each one-constraint-uncertain fibre, but does not make the four constraints
equivalent or prove a positive canonical product.

The proof must retain the coupled reference (Y_\lambda), prove a common
image neighbourhood before taking the coordinate line, and check that the
compensating apparatus remains in the fixed preparation box. A nonzero inverse
column alone proves state ambiguity, not positive position-times-momentum risk:
if either canonical component vanishes, use higher order or report no such
conclusion. No effective model/effort setting was independently verified.

## Source-to-model idea

For each uncertain supplied quantity, compute its inverse-response column and
the deterministic receiver-image radius separately; use the column's two
canonical projections as the decisive test for a positive endpoint product.

## Coordinator review

The coordinator reopened the specified primary PDF and checked pp. 1–3:
the invariant-ball radius on p. 2, Proposition 1 and the inverse theorem
statement/start of proof on p. 3. The full inverse differentiability proof
continues on p. 4, outside this audit's selected passages. Uniformity in
the coupling parameter is an application of the displayed contraction
bounds, rather than a separately quoted parameter theorem. The inherited
Werschulz statement above is specialized to compact scalar coordinate images.
