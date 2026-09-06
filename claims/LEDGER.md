# Results and claim ledger

Updated 2026-09-06. The current mathematical evidence consists of written
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

These are checked derivations. C006 is conditional on its stated quantum
measurement premises. For a new result, provide quantifiers, units, path/operator
domain, boundary conditions, dependencies and gap-closing limits in the proof.

## Historical findings and research targets

| ID | Claim or question | Status / evidence |
| --- | --- | --- |
| H001 | The selected Book I passages formulate geometric first and last ratios | Source-grounded interpretation; opening-source companions and note |
| H002 | Doubts about vanishing magnitudes delayed the 1687 first edition | Open historical conjecture; H02/H03 seek dated causal evidence |
| H003 | NATP00385 is a miscellaneous calculus-priority fragment collection | Verified catalogue metadata and H01 audit |
| H004 | Selected NATP00385 passages describe analytic discovery and synthetic presentation | Passage-level audit; exact coverage and chronology question in the historical note |
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
