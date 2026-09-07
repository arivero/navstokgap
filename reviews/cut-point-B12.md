# B12 review — cut-point consistency audit

## Verdict

The draft’s three calculations are correct under their explicit model
hypotheses. They should remain labelled derived consequences. The literature
coverage is sufficient for the Gaussian bridge background but is not a prior-
art or novelty certification.

## Mathematical review

For C027, on interval \(\tau_j\), subtracting the local tangent removes the
linear first variation and leaves \(F^2\tau_j^3/(24m)\). Since
\(\sum_j\tau_j^3\le |\pi|^2\sum_j\tau_j=T|\pi|^2\), the stated convergence
bound follows. Jensen gives \(\sum_j\tau_j^3\ge T^3/N^2\) for fixed \(N\),
and splitting \(a+b\) lowers the sum by \(3ab(a+b)\). The result concerns
sampled chords of the accelerated curve, not Newton’s central-impulse polygon.

For C028, an interior retained time has variance
\(\kappa s(T-s)/(mT)\), with a strictly positive coefficient of \(\kappa\),
so equality of coarse and fine one-node marginals
forces equality of parameters. A common refinement propagates this across
nontrivial partitions. The fixed-\(\kappa\) chi-square law and the moments of
\(2D_\pi/d\) are the finite Gaussian action law already assumed in the draft;
they imply divergence of unnormalised action and consistency of the normalised
estimator. They do not select \(\kappa>0\).

For C029, the kinetic splitting identity is
\(m(a+b)\zeta^2/(2ab)\). The conditional variance gives mean \(\kappa/2\),
independent of \(a,b\). This is distinct from C027 because C027 moves the
inserted point onto a force-driven classical curve and includes the potential
term.

## Reproduction

`python3 scripts/cut_point_checks.py` passed all nine symbolic residual tests:
interval action, cubic split, equal partition, kinetic square completion,
conditional mean, estimator mean and variance, retained variance, and the
Gaussian Schur complement. It wrote `out/cut-point-checks.json`.

## Evidence limits

Pitman–Yor’s selected pages establish Brownian covariance, bridge construction,
and Markov products. Scaling to \(\kappa/m\), conditioning, and all action
formulae are project derivations. Newton’s historical support is inherited
from the existing companion; the audit did not inspect a new Newton edition or
claim a full Newton history review.

Coordinator integration: the positive-coefficient wording above also covers
the deterministic case $\kappa=0$. The covariance and common-refinement proof,
Chebyshev bound and conditional inserted-node formula were checked directly.
Pitman–Yor printed pp. 12–13 were reread, p. 13 visually checked, and the
cached PDF hash verified. All nine exact checks pass. C027–C029 are accepted
as model-specific derived consequences, with B11's earlier geometry claims
remaining separate and unaccepted.
