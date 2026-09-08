# A09b/B18 coordinator review

C039–C040 are accepted as a reconstruction and derived protocol consequence.
The written proof is in [the checkerboard note](../notes/checkerboard-dynamics.md).
The librarian's bounded [B18 audit](../references/batches/B18.md) supplies
the recurrence source and a separate C040 addendum.

## Mathematical review

The matrix $W=(\begin{smallmatrix}0&1\\-i&0\end{smallmatrix})$ maps both the
source coin and direction ordering exactly. The fixed-first-step path sum has
one fewer coin than a walk that mixes at time zero. Both conventions and their
overall phase are stated. The Fourier proof uses fixed momentum followed by
dominated convergence, with a uniform bound of two from unitarity; its error
estimate is not claimed uniform over all momenta. The self-adjoint domain is
$H^1$ at fixed positive $m,c,K$. The nonrelativistic result uses the scalar
positive-branch spectral representation, after rest-energy subtraction.

Analytic continuation of the probability coin has unequal singular values.
A scalar phase cannot make it exactly unitary at finite mesh. The normalized
coherent coin agrees with its phase-corrected generator to first order.
C040 measures direction at every step, thereby resetting the component;
the bound on any flip follows without a position measurement.

## Source-review corrections

Coordinator verified the cached SHA-256 and visually checked pp. 12, 13, 19,
31. Corrected the worker's initial v2 year (2022), misplaced proof anchor
(31, not 30), page-count wording, and requested model/effort record. Clarified
that reversing transport changes its sign, whereas coin/shift reordering
changes second-order terms only. The singular-kernel warning applies to
delta initial data; the $L^2$ norm theorem is intact. Removed an escaped
control character in the worker's measurement addendum.

## Checks and next step

`scripts/checkerboard_checks.py` passes 14 symbolic identities, seven direct
path-sum comparisons and seven exact norm checks, plus three Fourier-mode
refinement tests. These checks support the general written proof.
G01 follows with the susceptibility/gap product and hidden slow-mode test.
The parent A09 selection problem retains preparation independence and the
physical rule identifying the classical plateau with a coherent phase scale.
