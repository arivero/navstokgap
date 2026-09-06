# Research programme: action, trajectories and gaps

Version 2, 2026-09-06.

## Aim

Explain the relationship between mechanical trajectories, an action scale and
gap formation. We pursue two connected outcomes:

1. A reconstruction of quantum mechanics from explicit physical premises, with
   a derivation of the role and necessity of an action parameter.
2. A rigorous toy model that identifies which Lagrangians, state spaces and
   boundary conditions produce a positive lower bound.

Newton's shrinking-area construction provides the initial geometric model.
The work proceeds through exact mechanical examples, operational definitions,
operator spectra and comparisons of limiting procedures.

## Starting results

For $V=-Fy$, duration $T>0$, perpendicular launch speed $v_0>0$ and mass $m>0$,
the chord–curve action difference is

$$\Delta S=\frac{F^2T^3}{24m}
=\frac{F}{2v_0}\mathcal A_{\rm lens}
=\frac{T\delta E}{12},\qquad \delta E=\Delta K=-\Delta V.$$

The variation $\eta(t)=a t(T-t)$ gives $\Delta S=ma^2T^3/6$.
Thus positive action differences in this fixed-endpoint class have infimum zero.
The chord is an off-shell comparison path; the parabola solves the constant-force
equation. This identifies admissibility of neighbouring paths as a substantive
choice for the proposed gap mechanism.

A second result concerns quantum measurement. For two known, equally likely
two-arm pure states whose relative phase is $\Delta S/\hbar$, $N$ independent
copies and arbitrary joint binary measurements give the first-lobe threshold

$$d_{N,p}=2\hbar\arccos\!\left([4p(1-p)]^{1/(2N)}\right),
\qquad |\Delta S|\le\pi\hbar,\quad \tfrac12<p\le1.$$

Success probability at least $p$ is achievable exactly when
$|\Delta S|\ge d_{N,p}$. For fixed $\tfrac12<p<1$, this threshold scales as
$N^{-1/2}$; perfect discrimination has threshold $\pi\hbar$ for every finite $N$.
The calculation connects an action difference to a resource-dependent resolution.

The [technical paper](../papers/action-gap-foundations.tex) supplies the proofs,
the Jacobi-operator calculation and the normalized free-kernel limit.
The [ledger](../claims/LEDGER.md) records their evidence and review status.

## Questions and mathematical objects

| Target | Question | Starting point |
| --- | --- | --- |
| Q0: classical existence | Which force regularity, initial data and collision conventions give unique global trajectories? | Constant force; next, central potentials |
| Q1: action-value gap | Is the infimum of positive matched-endpoint action differences positive on the chosen path class? | Infimum zero for the constant-force family |
| Q2: action scale | Which physical premises force a universal parameter with action units to be positive? | Reconstruction axiom comparison |
| Q3: operational bound | How do protocol, resources and error target determine action resolution? | Exact two-arm finite-copy threshold |
| Q4: spectral gap | Which self-adjoint operator has a separated ground sector, and how does its gap depend on parameters? | Dirichlet Hessian and quantum Hamiltonian |
| Q5: transfer across limits | Which estimates survive continuum and infinite-volume limits and interactions? | Companion PDE/field-theory comparisons |

Use $h=2\pi\hbar$ for Planck's constants, $\eta$ for trajectory variations,
$J$ for a fluctuation operator and $\chi$ for a proposed additional field.
Use matched endpoints when comparing actions under additions of $dG(q,t)/dt$.

## Model sequence

1. **Constant force:** derive the area–action relation and study small variations.
2. **Harmonic oscillator:** compare the duration-dependent Hessian eigenvalues
   with the quantum Hamiltonian spacing. Track normalization and conjugate times.
3. **Free line, circle and box:** isolate confinement and boundary conditions,
   and calculate gap closure as the spatial domain grows.
4. **Central potentials and Kepler:** establish IVP assumptions, collision
   continuation and action-angle variables; then compare quantum spectra.
5. **Interacting and multiwell models:** identify a gap-producing mechanism and
   its dependence on coupling, tunnelling and limiting parameters.

## Work packages

| Package | Deliverable / acceptance gate | Dependencies |
| --- | --- | --- |
| WP0: foundations | Restart instructions, ledger, tasks, source rules and LaTeX/PDF build | Complete |
| WP1: Newton | Edition/folio concordance, six-scholium corpus and dated evidence for the publication-history question | Source access |
| WP2: classical mechanics | Proofs for constant force, regular central forces and specified Kepler collision cases | Path class and topology |
| WP3: fluctuations and kernels | Jacobi operator/domain, conjugate times and normalized distributional limits | WP2 |
| WP4: operational reconstruction | Measurement bounds and a dependency map of candidate quantum axioms | WP3; bibliography B01 |
| WP5: gap laboratory | Operator domains, explicit bounds and parameter-dependent gap closure | Relevant WP2–4 results |
| WP6: companion limits | Relativistic, parabolic and quantum-field comparisons with a specified transferable estimate | WP5; Millennium definitions |
| WP7: papers and review | Readable proofs, checked citations, reproduced results and selected formal certificates | Accepted package result |

Historical reading and mathematical calculations have separate task tracks.
Delegate bounded tasks to Sol or Luna sequentially, with the coordinator waiting
for each worker and reviewing its handoff before continuing. The
finite-dimensional examples establish the definitions and estimates for the
later field-theory comparison. A package finishes with a theorem, counterexample,
conditional result or precisely stated open obligation.

## Reconstruction branches

**Branch A: consequences of quantum premises.** Start with Hilbert states, Born
probabilities and the phase $e^{iS/\hbar}$ for a specified $\hbar>0$. Derive
operational bounds, spectra and their dependence on model parameters.

**Branch B: origin of quantum structure.** Choose operational premises about
composition, continuity, reversible transformations and distinguishability.
Construct models satisfying subsets of these premises and identify the step that
selects quantum structure. Then establish how action enters the dynamics and what
forces its scale to be positive. Numerical calibration is a further empirical task.

**Additional-field proposal.** Specify the field space, coupling and measure for
$S[q,\chi]$, then calculate the effective action after eliminating $\chi$.
The [idea register](../ideas/I001-action-field.md) sets out the candidate
interpretations and their immediate tests.

## Reading priorities

Start Q01 with [Hardy's five axioms](https://arxiv.org/abs/quant-ph/0101012v4)
and [Chiribella–D'Ariano–Perinotti's informational derivation](https://arxiv.org/abs/1011.6451v3).
Use [Masanes–Müller](https://arxiv.org/abs/1004.1483v4) as a third comparison.
For each, trace how its premises constrain state spaces, transformations and
composition.

Branch A draws on [Feynman's path-phase formulation](https://doi.org/10.1103/RevModPhys.20.367),
[Wootters's finite-sample statistical distance](https://doi.org/10.1103/PhysRevD.23.357)
and the [quantum Chernoff asymptotic error bound](https://arxiv.org/abs/quant-ph/0610027v1).
The [B01 batch](../references/batches/B01.md) records verified metadata and selected
reading coverage. Full reconstruction-proof reading belongs to Q01.

## $1/c$, Navier–Stokes and Yang–Mills

Track $\hbar$, $c^{-1}$, viscosity $\nu$, time and volume independently.
The free relativistic particle retains the small-amplitude action family within
a strict speed margin. The nonrelativistic quantum model retains $\hbar>0$ at
$c^{-1}=0$. These examples separate the roles of the two parameters.

A bridge must specify its source and target spaces, operators, physical or
auxiliary time, units, preserved estimate and limits. The useful comparison is
how coercivity and control of fluctuations survive changes of scale.
For Navier–Stokes, the target is evolution regularity under the official
hypotheses. For Yang–Mills, it includes the physical Hilbert space and a vacuum
spectral gap through the continuum and infinite-volume limits.

## Scope and publication

The programme's reconstruction and gap-formation questions are open research
targets. The present results concern the explicitly defined toy models; the
Millennium problems supply comparison targets. Novelty and publication readiness
will be assessed through literature comparison and specialist review.

Maintain human-readable proofs alongside calculations and formal artifacts.
Record changes of model or target with their reasons. Submission, public posting,
author correspondence and paid services require user direction.
