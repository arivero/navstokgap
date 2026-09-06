# Claim ledger

Updated 2026-09-06. IDs are stable even when a claim is refuted or reformulated.
`checked derivation` means a written argument plus indicated algebra checks, not
kernel-checked formalisation or external peer review. Mathematical claims below
are elementary control results; no novelty is claimed.

| ID | Statement / object and assumptions | Status | Evidence / outstanding review |
| --- | --- | --- | --- |
| C001 | Constant force, matched endpoints: chord action excess $F^2T^3/(24m)=T\delta E/12$ | checked derivation | `notes/principia-constant-force-action.md`, `scripts/constant_force_geometry.py` |
| C002 | On this unrestricted fixed-endpoint path class, positive action differences have infimum zero | checked derivation | Exact family $\eta=a t(T-t)$; foundations manuscript Proposition 1 |
| C003 | A continuous variation direction with nonzero second variation prevents a positive gap in the absolute action difference near a stationary path | checked derivation | Foundations Proposition 2; assumes a twice-differentiable scalar restricted action |
| C004 | Dirichlet constant-force Hessian has lowest eigenvalue $m\pi^2/T^2$ but no positive lower nonzero unnormalized quadratic-form value | checked derivation | Foundations §3; normalization and units explicitly different |
| C005 | The normalized one-dimensional free Schrödinger kernel tends to $\delta$, with first short-time correction proportional to $\delta''$, not $\delta'$ | checked derivation | Foundations §4, Schwartz-distribution Fourier proof |
| C006 | Fixed $N$, equal-prior two-arm pure-state discrimination yields a positive first-lobe action threshold for any target success $p>1/2$ | conditional checked derivation | Foundations §5; assumes quantum phase/Born measurement framework and ideal controlled paths |
| C007 | For $1/2<p<1$, C006's threshold tends to zero as $N\to\infty$ | checked derivation | Explicit formula; perfect discrimination $p=1$ is a separate endpoint |
| C008 | Adding finite $c$ alone does not exclude small variations around a smooth path with a strict speed margin | checked derivation | Foundations §6; does not claim a complete relativistic interaction theory |
| H001 | Read Book I passages use geometric limits, not a stated Planck-scale premise | source-grounded interpretation | Newton opening-source companions and note; edition limits retained |
| H002 | Doubts about vanishing magnitudes delayed the 1687 first edition | unverified historical conjecture | Needs dated causal evidence; H02/H03 remain open |
| H003 | NATP00385 is a miscellaneous calculus-priority fragment collection, not a complete edition of the Book III Classical Scholia | metadata verified | Newton Project catalogue/title; H01 focused source audit |
| H004 | Selected NATP00385 passages describe analytic discovery versus synthetic presentation but do not establish H002 | passage-level source audit | `notes/newton-NATP00385-audit.md`; no full corpus/facsimile audit or universal negative claim |
| Q001 | Independent premises force a nonzero universal action parameter | open target | WP4 Branch B; no axiom system selected yet |
| Q002 | A proposed extra field generates a physical action-value or spectral gap | unformulated model | `ideas/I001-action-field.md`; field/action/domain not specified |
| X001 | Equal phases at action differences $nh$ imply a smallest positive action difference | rejected inference | Phase periodicity is compatible with arbitrarily close phases |
| X002 | A toy Hessian/oscillator gap proves the Yang–Mills mass gap or NS regularity | rejected inference | Wrong objects and missing continuum/infinite-volume/regularity obligations |

For a new theorem add full quantifiers, units, path/operator domain, boundary
conditions, dependencies and gap-closing limits in its proof artifact. Record
review objections here or link the review. No claim is accepted solely because a
symbolic system simplified a residual to zero.

## Review record

[R01](../reviews/action-gap-foundations-R01.md) independently audited the three
displayed propositions and supporting calculations behind C001–C008. No blocking
error was found. The coordinator incorporated the two recommended clarifications:
ordinary endpoint terms mean $dG(q,t)/dt$, and path-space locality additionally
requires continuity of the parameterized paths. This is an internal agent review,
not external peer review or a Lean certificate. Historical claims and physical
implementation were outside R01's scope.
