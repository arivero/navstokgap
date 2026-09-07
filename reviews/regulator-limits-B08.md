# B08 proof and assumption audit

The five result groups in `papers/regulator-limits.tex` are correct under their stated finite-dimensional/free-model assumptions. No proof-breaking error was found. C014 and C017 need especially clear interpretation: the former is a selected double-scaling limit, not a positive gap at finite resolution, and the latter preserves a chosen reference family by running the bare mass, rather than deriving a universal action scale.

## Proof review

### C013: arbitrary partition Gaussian bridge

**Status: proof checked.** For (\eta_0=\eta_N=0), the quadratic form is
(m\sum_j(\eta_j-\eta_{j-1})^2/\tau_j), so SPD follows. The leading-minor recurrence has the stated solution
(D_k=m^k(\tau_1+\cdots+\tau_{k+1})/(\tau_1\cdots\tau_{k+1})), giving the full determinant. The proposed Green matrix has the necessary endpoint zeros and slope jump (1/m), hence (A_\pi A_\pi^{-1}=I). Dividing the product of the (N) normalized transition densities by the coarse endpoint kernel gives the stated (d=N-1) dimensional bridge density.

Assumptions used: (m,\kappa,\tau_j>0); one spatial dimension; fixed endpoints; piecewise-linear paths; Lebesgue measure in the internal node coordinates. The formulas extend componentwise to independent spatial coordinates, but that extension is not claimed.

### C014: chi-square law and joint limit

**Status: proof checked.** Whitening an SPD Gaussian gives (d) independent standard normals and therefore (2\Delta S/\kappa\sim\chi_d^2). The displayed second-moment identity is exactly bias squared plus variance and tends to zero when (d\kappa\to\ell<\infty).

The common coupling is valid even for nonnested partitions: sample one continuous bridge (B^T), interpolate its nodes on each partition, and multiply by (\sqrt{\kappa_N/m}). Each polygon has the required finite-dimensional law. Since interpolation cannot exceed the sampled bridge supremum in absolute value,
(\|I_{\pi_N}B^T\|_\infty\leq\|B^T\|_\infty), so (\kappa_N\to0) proves uniform almost-sure convergence. The action moment law is distributional and remains valid under this coupling.

The mesh assumption (\max\tau_j\to0) is not actually needed for the displayed uniform bound or chi-square law once (d=N-1\to\infty); it is appropriate to retain because the objects are advertised as time refinements. The conclusion is an (L^2) limit of random action defects, not pathwise convergence of the actions. At fixed (d,\kappa), the support reaches arbitrarily close to zero, so no hard positive action gap follows.

### C015: bounded-speed sine sequence

**Status: proof checked.** Differentiation gives
(\dot q_n=(z-x)/T+v_*\cos(2\pi nt/T)), hence
(|\dot q_n|\leq |z-x|/T+v_*<c). The perturbation amplitude is (O(n^{-1})), the velocity cross term integrates to zero, and the squared cosine has integral (T/2), giving (mv_*^2T/4). The acceleration amplitude is (2\pi n v_*/T).

Assumptions used: Newtonian free kinetic action on fixed-endpoint (H^1([0,T])); (c>|z-x|/T); (0<v_*<c-|z-x|/T). The paths are off shell. The bound (c) is kinematic and does not turn the action into a relativistic one. Uniform acceleration or force control would exclude this sequence.

### C016: quadratic stationary phase

**Status: proof and constants checked.** With the unitary convention
(\widehat O(k)=(2\pi)^{-d/2}\int e^{-ik\cdot q}O(q)dq), translation by (q_*) and Guillemin--Sternberg (14.7) give the draft's prefactor, (e^{i\pi d/4}/\sqrt{\det A}), Fourier phase, and (e^{ik\cdot q_*}). Since (\widehat O\in L^1), dominated convergence yields the limit. For SPD (A), the linear map (q\mapsto\nabla F=A(q-q_*)) has positive Jacobian determinant, so
(\langle\delta^{(d)}(\nabla F),|O|^2\rangle=|O(q_*)|^2/\det A).

The last equality should continue to be described as the limit of the scalar quantity
(|I_\epsilon[O]|^2) for each test function. It is not a definition of the square of a distribution or a linear distributional limit in (O). The proof fixes (d), assumes one SPD critical point and (O\in\mathcal S); indefinite Hessians require (|\det A|) and the signature phase.

### C017: regulator units and bare coefficient

**Status: algebra checked; physical interpretation remains an assumption.** With physical (L^\tau=mv^2/2), fixed coordinates, and the exponent (i\tau\sum L^\tau/\epsilon), dimensional homogeneity forces ([\epsilon]=\text{action}). Thus (\epsilon=b\tau) gives ([b]=\text{energy}). This conclusion would change if coordinates or (L^\tau) were themselves rescaled, as Rivero allows.

Substituting (m_B=\epsilon m_R/\kappa_R) gives both
(S_{\pi,B}/\epsilon=S_{\pi,R}/\kappa_R) and equality of each free-kernel normalizer. It therefore preserves the positive and oscillatory reference kernels, provided the oscillatory square-root branch is fixed consistently. If (\epsilon(\tau)\to0), then (m_B(\tau)\to0): this is a running bare kinetic coefficient and a renormalization condition, not the fixed-physical-mass limit of C014. Selecting a bridge variance plus a separately fixed (m_R) fixes (\kappa_R) by stipulation; it does not explain universality or positivity from independent physical premises.

## Script review

`scripts/regulator_limit_checks.py` was executed without permitting its output write (the `Path.write_text` call was mocked). All reported exact checks passed: four nonuniform rational partitions through (d=4), determinant/inverse/kernel normalization, normal moments, finite-defect moments, three sine frequencies, and the bare coefficient/normalizer identities.

The script accurately labels its limitations. It does not verify the general determinant induction, Brownian coupling, speed inequality/acceleration growth, stationary-phase Fourier identity, gradient-delta pullback, or physical-unit interpretation. Those items require the analytic review above. No script edit is required for correctness; adding stationary-phase numerical tests would not replace the needed convention-level proof.

## Source and citation corrections for integration

- The draft's Pitman--Yor anchor `p. 6, (4)--(5)` is correct. The B06 companion has two stale `p. 5` references before its explicit p. 6 correction; it was not edited.
- Rindler printed p. 57 appears to use (\delta_\alpha,\delta_\beta) where the measure on input values requires (\delta_a,\delta_b). Attribute this as a source typo; do not propagate it.
- Rivero is evidence for the proposal and regulator notation, not for convergence or normalized constants.
- Guillemin--Sternberg (14.7) supplies the exact stationary-phase normalization and was visually verified.

## Coordinator acceptance, 2026-09-07

C013–C017 are accepted as checked derivations under the paper's assumptions.
The coordinator verified source metadata and key formula images, ran all 24
exact checks with their output recorded, and incorporated the scalar-limit and
bare/reference-coefficient distinctions. The positive-time square-root branch
is now explicit. The B06 page references were corrected to p. 6. Literature
classifications remain those of the bounded batch, independently of proof status.
