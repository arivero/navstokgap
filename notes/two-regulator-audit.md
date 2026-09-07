# Two regulators: what survives when the paths shrink?

The completed M05 calculation gives a classical path limit with a finite
action defect. Under the free Gaussian endpoint bridge, $d=N-1$ internal
positions and action scale $\kappa$ give

$$\mathbb E\Delta S=\frac{d\kappa}{2},\qquad
\operatorname{Var}(\Delta S)=\frac{d\kappa^2}{2}.$$

If $\kappa_N\to0$ and $d\kappa_N\to\ell>0$, the polygonal paths can converge
uniformly almost surely to the straight classical path while their excess
action converges in $L^2$ to $\ell/2$. The [paper](../papers/regulator-limits.tex)
gives the arbitrary-partition determinant, covariance and proof; the
[PDF](../out/papers/regulator-limits.pdf) is the human-readable entry point.

## Source inputs and the calculations they generated

| Source input | Implemented test | Result / next obligation |
| --- | --- | --- |
| Rivero 1998, (5)–(9): two regulators and an unspecified control map | Set the physical time step to $\tau$ and track the action coefficient $\epsilon$ | At fixed physical mass, $\epsilon=b\tau$ assigns energy units to $b$ and gives residual action $bT/2$ in the positive model |
| Pitman–Yor, continuous bridge and Markov product | Compute the full partition precision matrix and couple all partitions through one bridge | Uniform path convergence coexists with a finite action defect |
| Rindler, weak oscillations and Young measures | Construct a shrinking sine displacement with fixed velocity amplitude | A strict speed bound permits the defect; acceleration grows with frequency |
| Guillemin–Sternberg, (14.7) | Restore all Fourier and determinant factors in one quadratic critical-point calculation | A scalar squared-amplitude limit gives the gradient-delta weight |
| Wilson–Kogut §12.2 | Compare cutoffs at a fixed physical observable | Running $m_B=\epsilon m_R/\kappa_R$ preserves the reference free kernel exactly |

The source companions record exact coverage. [B08](../references/batches/B08.md)
audits each mathematical result; [its review](../reviews/regulator-limits-B08.md)
checks the proofs separately from the literature classification.

## The three quantities to keep distinct

$\kappa$ controls the Gaussian fluctuations and has action units. The product
$d\kappa$ controls the total quadratic action in the joint limit. A hard
action-value gap would instead be a positive infimum over an explicitly chosen
admissible class. The current finite-dimensional action distribution has values
arbitrarily close to zero; the residual limit is selected by a scaling rule.

The constant $\kappa_R$ in the running-coefficient model is supplied by a
reference bridge variance and a reference mass. Taking $\epsilon\to0$ then
sends the bare kinetic coefficient to zero while preserving the reference
family. This differs from the fixed-mass shrinking-bridge construction.

## M06: test a physical dynamical premise

The next experiment should determine which control on forces or derivatives
allows an action defect to survive. Start with the explicit sine sequence,
fixed endpoints, fixed duration and its strict speed margin.

1. Impose uniform acceleration or force control and derive the corresponding
   compactness/action estimate. State the convergence topology and constants.
2. Replace the quadratic kinetic action by the specified relativistic free
   action within the same strict speed margin. Calculate the oscillatory limit
   and its dependence on $c$, amplitude and duration.
3. Use those results to state the physical premise that a stochastic or
   additional-field model would need to retain a positive residual. Track
   whether that premise supplies a scale or derives one.

Commission one bounded librarian audit after the calculation. Its role is to
identify the established compactness/averaging results and supply the next
construction. The stronger programme then asks for universality and a physical
phase rule linking the surviving quantity to $h=2\pi\hbar$.

The tangent-groupoid theorem reading remains B07b. It addresses the separate
quantum-completion branch; the present source reading has completed B07a's
common-observable scaling test.
