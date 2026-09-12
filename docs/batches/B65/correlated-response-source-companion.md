# B65: correlated calibration response

## Result and bounded coverage

Freire supplies a direct local smooth-inverse match for R33's exact curve, but
not the mechanical second-coupling coefficient. On PDF pp. 3--4, the inverse
of a differentiable map with invertible derivative is differentiable and

\[
 dg(f(a))=[df(a)]^{-1};
\]

for a `C^k` map the inverse is `C^k` locally. The proof writes the inverse
remainder explicitly and controls it through the forward Taylor remainder
(p. 4). Freire also proves smoothness of matrix inversion, with
`d(X^{-1})[V]=-X^{-1}VX^{-1}` (p. 5, coordinator extension). This supports Taylor expansion of the
exact divided map and its inverse in `(lambda,s)`, provided R33 establishes a
uniform invertible chart. It does not prove the chart, the apparatus flow
regularity, or any coefficient for the selected pulse design.

Coverage: zero discovery queries; one specified primary retrieval, Alberto
Freire, *Inverse Function Theorem and Surfaces in R^n*,
https://web.math.utk.edu/~afreire/teaching/m447f16/InverseFunctionTheorem.pdf,
passage-level reading of PDF pp. 3--4 by text extraction. No full read,
visual formula audit, or exhaustive prior-art search is claimed. B62's scalar
radius-of-information match and B63's local inverse method are inherited, not
re-audited here.

## Match to R33 and limits of inference

For `w_lambda(s)=T_lambda^{-1}(s r)`, Freire supports the local statement that
smooth `T_lambda` with a uniformly nonsingular derivative has a smooth inverse
and a uniform Taylor remainder on a reduced compact chart. It therefore
supports the conditional fibre estimates in R33 (5) and the expansion (7),
not a global estimator result. The latter requires a single chart covering the
stated preparation/receiver box and all final-record alternatives; a local
curve's shrinking canonical diameter cannot be promoted to global minimax
recovery.

The response coefficient must be differentiated from the exact coupled
reference `a_lambda`/`Y_lambda`. In model notation, the relevant object is
`V(w)=1/2 partial_lambda^2 N(0,w)` for the exact `N(lambda,w)`, followed by
`-Pi_{x,P} L^{-1} (D V(0)) e_y`. Freire's inverse derivative and remainder
control justify the calculus operation, but neither the source nor B62/B63
identifies `V`: the moving-reference derivative, Hamiltonian variational
terms, and pulse-dependent cancellations remain unverified.

## Proof issues and source-to-model next test

Retain the factor `|s|` in the inverse remainder by anchoring at
`w_lambda(0)=0`; ordinary pointwise inverse differentiability alone is
insufficient. Prove uniform mixed derivative bounds on a fixed smaller `s`
interval, preserve component units and box margins, and distinguish the
conditional segment radius from global risk. If both projected components of
`b'(0)` are nonzero, endpoint radii can give the conditional lower bound (9).
If either vanishes, compute the next nonzero order or report only the upper
suppression result; zero leading response is not exact constancy.

Next bounded model test: differentiate the exact coupled map twice in lambda,
including all derivatives of the moving reference record, then evaluate
`Pi_{x,P}L^{-1}(D V(0))e_y` for R32's fixed pulses by written variational
derivation. Exact model/novelty status is unassessed.

## Coordinator source correction

The coordinator reopened the primary PDF and checked the theorem statement
on p. 3, inverse differentiability/remainder on p. 4 and matrix inversion plus
the C^k corollary on p. 5. The worker placed the latter on p. 4 incorrectly;
its handoff preserves that original report. Fresh coordinator passage coverage
is pp. 3–5, with no new discovery query. Smooth parameter dependence follows
by applying the inverse theorem to (lambda,w) -> (lambda,T_lambda(w)).
Compact neighbourhoods provide the uniform derivative bounds used in R33.
