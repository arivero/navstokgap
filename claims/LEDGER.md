# Results and claim ledger

Updated 2026-09-07. The current mathematical evidence consists of written
derivations, symbolic checks and internal proof review. Each entry names its
assumptions and supporting artifact. IDs remain stable through revision.

## Mechanical and operational results

| ID | Statement | Evidence |
| --- | --- | --- |
| C001 | Constant force, matched endpoints: chord action excess $F^2T^3/(24m)=T\delta E/12$ | Constant-force note and symbolic script |
| C002 | Positive action differences in the fixed-endpoint constant-force class have infimum zero | Foundations Proposition 1; exact family $\eta=a t(T-t)$ |
| C003 | Absolute action differences accumulate at zero along a continuous variation with nonzero second variation | Foundations Proposition 2; restricted action is $C^2$ in its parameter |
| C004 | The constant-force Dirichlet Hessian has lowest eigenvalue $m\pi^2/T^2$; scaling the variation scales its quadratic cost continuously | Foundations §3; $L^2$ normalization |
| C005 | The free Schrödinger kernel tends to $\delta$, with first short-time correction $i\hbar\tau\delta''/(2m)$ | Foundations §4; Schwartz-distribution Fourier proof |
| C006 | Fixed-$N$, equal-prior quantum two-arm discrimination has an explicit positive first-lobe action threshold for $1/2<p\le1$ | Foundations Proposition 3; specified pure states, phase rule and joint measurement |
| C007 | For fixed $1/2<p<1$, C006's threshold tends to zero as $N\to\infty$; at $p=1$ it is $\pi\hbar$ for finite $N$ | Explicit formula and endpoint checks |
| C008 | The free relativistic particle admits arbitrarily small positive fixed-endpoint action differences within a strict speed margin | Foundations §6; explicit small-amplitude family |
| C009 | Free normalized Gaussian kernels on the line compose at every finite partition with unchanged action parameter $\kappa>0$ | Time-refinement Proposition 1; square completion and normalization checks; B06 assumption audit |
| C010 | A weakly continuous centered Gaussian convolution semigroup has variance $at$, $a\ge0$; at fixed mass $\kappa=ma$ remains free | Time-refinement Proposition 2; characteristic-function proof, including the degenerate family |
| C011 | Fixed-endpoint Gaussian bridges have linear mean and variance $\kappa s(T-s)/(mT)$; fixed finite-dimensional laws concentrate on the free classical path as $\kappa\to0$ | Time-refinement §3; square completion, Chebyshev and union bound |
| C012 | For every $\kappa>0$, the free multiplier $\exp[-i\kappa t k^2/(2m)]$ gives a strongly continuous unitary group on $L^2(\mathbb R)$ with Hamiltonian domain $H^2$ | Time-refinement §4; Fourier proof and composition check; B06 assumption audit |
| C013 | At any positive finite time partition, the free endpoint Hessian has determinant $m^{N-1}T/\prod\tau_j$ and inverse $[\min(t_i,t_j)-t_it_j/T]/m$; these give the normalized bridge law | Regulator-limits Proposition 1; B08 proof review; exact nonuniform-partition checks |
| C014 | Under that bridge, $2\Delta S/\kappa\sim\chi^2_{N-1}$; if $\kappa_N\to0$ and $(N-1)\kappa_N\to\ell<\infty$, a common coupling gives uniform almost-sure path convergence and $L^2$ action excess $\ell/2$ | Regulator-limits Proposition 2; B08 review of covariance coupling and moments |
| C015 | Smooth fixed-endpoint sine perturbations with amplitude proportional to $1/n$ retain excess Newtonian action $mv_*^2T/4$ within a strict speed bound; acceleration grows with $n$ | Regulator-limits §4; off-shell paths, direct integration and B08 review |
| C016 | At one SPD quadratic critical point, the normalized oscillatory amplitude has a scalar squared-modulus limit $|O(q_*)|^2/\det A=\langle\delta^{(d)}(\nabla F),|O|^2\rangle$ for each Schwartz test function | Regulator-limits §5; fixed dimension, Fourier proof; B08 constants review |
| C017 | For a physical free Lagrangian, $\epsilon=b\tau$ gives energy units to $b$; choosing the bare coefficient $m_B=\epsilon m_R/\kappa_R$ exactly preserves the normalized reference kernels | Regulator-limits §6; explicit reference condition, fixed square-root branch; B08 algebra/units review |
| C018 | For almost-sure absolutely continuous paths with speed at most $u<c$, $\mathsf h_\Delta=m\operatorname{Var}(X(t+\Delta)-X(t))/\Delta$ lies in $[0,mu^2\Delta]$ and tends to zero as $\Delta\downarrow0$ | Classical-action-field Proposition 1; elementary variance proof; B09 and coordinator review |
| C019 | A stationary finite irreducible reversible velocity chain with nonzero centered velocity gives $\mathsf h(\Delta)\uparrow H_*=2m\langle v,(-Q)^{-1}v\rangle_\pi>0$, with spectral bounds and convergence estimate | Classical-action-field Proposition 2; fixed-model action plateau, mean-zero inverse; spectral proof and B09 review |
| C020 | Symmetric velocities $\pm u$, $0<u<c$, reversed at rate $\lambda>0$, give $H_*=mu^2/\lambda$; universality across masses requires $\lambda_m=mu_m^2/H_*$ | Classical-action-field §§4, 6; exact correlation, variance and telegraph equations; 16-check suite and B09 review |
| C021 | In the formal scaling $u_\lambda^2=a\lambda$, $a>0$, iterated second-moment action limits are $ma$ (rate first) and zero (duration first) | Classical-action-field §5; explicit formula; scaling leaves a fixed speed ceiling; B09 review |

These are checked derivations. C006 is conditional on its stated quantum
measurement premises. For a new result, provide quantifiers, units, path/operator
domain, boundary conditions, dependencies and gap-closing limits in the proof.

## Literature status

Proof status above and literature status below are independent. Each accepted
result has a bounded librarian audit; exact source inputs and elementary
consequences are identified separately.

| Claims | Literature classification | Audit |
| --- | --- | --- |
| C001–C004, C008 | Classical geometry/variation framework; specialized formulas are elementary consequences | [B05](../references/batches/B05.md) |
| C005 | Teschl's standard free kernel; Taylor correction is a Fourier consequence | B05 |
| C006–C007 | Holevo–Helstrom theorem specialized to the stated pure-state protocol; threshold inversion and limits are consequences | B05 |
| C009 | Standard Gaussian/Chapman–Kolmogorov formula with mass/action rescaling | [B06](../references/batches/B06.md) |
| C010 | Elementary characteristic-function/additivity consequence within the Gaussian class | B06 |
| C011 | Standard Brownian bridge with rescaling; finite-dimensional concentration is a consequence | B06 |
| C012 | Standard free Schrödinger group and domain, with restored units | B06 |
| C013 | Elementary determinant/Green-function consequence of the standard Gaussian bridge | [B08](../references/batches/B08.md) |
| C014 | Finite chi-square law and joint limit derived from standard Gaussian facts; exact combined statement unmatched in the four-source coverage | B08; bounded coverage, novelty unassessed |
| C015 | Elementary mechanics instance of the established oscillatory weak-limit mechanism | B08; Rindler §§2.1, 3.3 |
| C016 | Exact quadratic Fourier identity in Guillemin–Sternberg (14.7); scalar limit and delta pullback are consequences | B08 |
| C017 | Explicit elementary scaling construction motivated by Rivero; exact map unmatched in the selected sources | B08; bounded coverage, novelty unassessed |
| C018 | Elementary bounded-displacement variance consequence | [B09](../references/batches/B09.md) |
| C019 | Exact Green–Kubo/Poisson backbone in Pavliotis; finite-state bounds and monotonicity are spectral consequences | B09; combined package unmatched in bounded coverage, novelty unassessed |
| C020 | Exact telegraph construction/PDE in Cinque; action normalization and mass-rate law are elementary consequences | B09 |
| C021 | Elementary iterated-limit consequence; related Kac scaling in Cinque | B09; exact double-limit statement unmatched in selected passages |

M03's unaccepted spectral draft has its own completed [B04](../references/batches/B04.md)
literature audit. Its mathematical review and checks remain pending.

## Historical findings and research targets

| ID | Claim or question | Status / evidence |
| --- | --- | --- |
| H001 | The selected Book I passages formulate geometric first and last ratios | Source-grounded interpretation; opening-source companions and note |
| H002 | Doubts about vanishing magnitudes delayed the 1687 first edition | Open historical conjecture; H02/H03 seek dated causal evidence |
| H003 | NATP00385 is a miscellaneous calculus-priority fragment collection | Verified catalogue metadata and H01 audit |
| H004 | Selected NATP00385 passages describe analytic discovery and synthetic presentation | Passage-level audit; exact coverage and chronology question in the historical note |
| H005 | Plutarch's cone-section passage was printed in Xylander's 1570 Latin Moralia, pp. 823–824 | H04 librarian retrieval; coordinator visual verification of IIIF canvases 603151/603152 |
| H006 | How did the cone-section dilemma enter early-modern discussions of indivisibles and the continuum? | H04 bounded search; H05 author-specific reception audit remains |
| Q001 | Which independent premises force a positive universal action parameter? | Open target; WP4 Branch B |
| Q002 | Which additional-field action generates an action-value or spectral gap? | Model design; `ideas/I001-action-field.md` |

## Resolved objections

| ID | Inference assessed | Resolution |
| --- | --- | --- |
| X001 | Equal phases at differences $nh$ imply a smallest positive action difference | Rejected: phase periodicity permits arbitrarily close phases |
| X002 | A toy Hessian/oscillator gap establishes the Yang–Mills gap or NS regularity | Rejected: transfer requires the target operators, spaces and continuum/infinite-volume/regularity estimates |

## Review record

[B09](../reviews/classical-action-field-B09.md) audited C018–C021 after the
draft derivation. Coordinator review checked source formula images and hashes,
the mean-zero inverse, rate convention, limit order and model-specific bounds.
Velocity-resolved measures were defined as joint subprobability measures.
The written proofs support the general statements; 16 exact checks support
their finite algebraic instances. The next obligation is physical universality.

[R01](../reviews/action-gap-foundations-R01.md) audited the three propositions
and supporting calculations behind C001–C008. Its two scope clarifications are
incorporated: endpoint terms mean $dG(q,t)/dt$, and path-space locality requires
continuity of the parameterized paths. The current editorial revision retains
the theorem statements, proof arguments and evidence classifications.

[B08](../reviews/regulator-limits-B08.md) independently checked C013–C017.
Coordinator review verified the source formulas, retained the distinction
between path and action convergence, specified the oscillatory branch and
made the scalar test-function interpretation explicit. All 24 finite checks
pass; the general analytic statements rest on the written proofs.
