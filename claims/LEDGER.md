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

[R01](../reviews/action-gap-foundations-R01.md) audited the three propositions
and supporting calculations behind C001–C008. Its two scope clarifications are
incorporated: endpoint terms mean $dG(q,t)/dt$, and path-space locality requires
continuity of the parameterized paths. The current editorial revision retains
the theorem statements, proof arguments and evidence classifications.
