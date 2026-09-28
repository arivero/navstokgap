# Continuum $SU(3)$ gap assault plan: proof interfaces, independent workstreams, and attribution

**Status — execution plan, 2026-09-28.**  The completed $0+1$ theorem and
the $SU(3)$ Cartan one-loop calculation do not prove a $3+1$ continuum
mass gap.  The [conditional assembly theorem](../notes/mass-gap-conditional-theorem.md)
now makes the remaining target precise.  This document turns its four
hypotheses into bounded research workstreams, records the interface each
must meet, and specifies how actual delegated contributions will be
credited in commits.  It is not a claim that the outlined estimates are
currently available.

## 1. End product and common conventions

Fix a reflection-positive, periodic, gauge-invariant lattice regulator for
pure $SU(3)$, a scaling trajectory $a_0\downarrow0$, and a local
reflection-stable algebra of gauge-invariant observables.  The desired
conditional conclusion is an OS-reconstructed, nontrivial continuum
Hilbert space in which
\[
 \operatorname{spec}(H)\cap(0,m_*)=\varnothing,
 \qquad m_*\ge\frac{\hbar c}{a_*}\min(\gamma_*,\gamma')>0. \tag{1}
\]
The four proof interfaces are:

| Interface | Required output | Failure it excludes |
| --- | --- | --- |
| H1$_{\rm gap}$ | local block map, support buffer, and the scale-by-scale connected-correlation difference bound (2) of the assembly theorem | an apparent finite-volume gap that is lost under ultraviolet refinement |
| H1$_{\rm OS}$ | a specified renormalized local algebra with the uniform summability bound (3) | divergent correlator prefactors or vanishing observable residues |
| H2 | a volume-uniform, gauge-invariant one-box strong-mixing neighbourhood at a physical crossover scale | an infrared correlation length that grows with the box |
| H3 | tight/convergent Schwinger functions, OS axioms, spectral-measure convergence, and a surviving non-vacuum local vector | a cutoff theory with no constructed continuum sector |

T3 is deliberately separate: after (1), a controlled running coupling and
nonzero finite $a_*\Lambda$ are needed to identify a universal
$m/(\hbar c\Lambda)=C$.  Dimensional transmutation alone does not establish
$C>0$.

All workstreams use explicit $\hbar,c$, take $L\to\infty$ before the
continuum limit unless they prove a stronger interchange statement, and
must distinguish a true spectral measure from a finite-lattice eigenvalue
list.  The repository rule against numerical or symbolic verification
scripts remains in force.

## 2. Workstream A — nonconstant modes and the small-volume interface

**Question.**  Can a gauge-invariant regulator control the nonzero-momentum
sector uniformly enough that the C133 constant-mode mechanism is retained
at weak small volume?

**Precise target.**  For a fibrewise/Born--Oppenheimer projection $P(a)$,
prove at fixed lattice cutoff, on a stated weak-coupling interval,
\[
 \bar P H\bar P\ge E_\perp+\frac{2\pi\hbar c}{L}(1-C_1g^{2/3}),\tag{A1}
\]
\[
 B(D-E)^{-1}B^*\le\epsilon(A-a_0)+\eta,
 \quad\epsilon<1,\quad
 \eta\le C_2g^{4/3}\frac{\hbar c}{L},                       \tag{A2}
\]
and a global, not merely Taylor-local, bound giving
\[
 \operatorname{gap}(A)\ge d_3g^{2/3}(1-C_3g^{2/3})
 \frac{\hbar c}{L}.                                         \tag{A3}
\]
The preceding root-sum calculation supplies only the Cartan one-loop
coefficient in (A3); it proves none of (A1)--(A3).

**Independent attack lines.**

1. Derive the covariant lattice Hessian and its nonzero-mode lower bound
   uniformly on a Cartan patch; treat Weyl walls and non-Cartan backgrounds
   by a gauge-invariant partition of unity.
2. Compute the fibre-vacuum quantum metric and Born--Huang term before
   assuming it is $O(g^{4/3})$.  Establish which divergent pieces are
   coupling/field renormalizations and which leave a relative Schur error.
3. Combine a local root-potential estimate with a quantitative spectral
   localization of the C133 Hamiltonian.  A local negative quadratic
   coefficient may not be promoted to a global form bound without an
   exterior barrier estimate.
4. Seek a counterexample or an ultraviolet obstruction to (A2); a sharp
   cutoff is already known to fail, so a periodic lattice cutoff must be
   used from the start.

**Acceptable deliverable.**  One stated regulator, one Hilbert/gauge
sector, and either a complete proof of one of (A1)--(A3), or a proved
obstruction identifying the counterterm/estimate still needed.  A
fixed-cutoff result must retain its cutoff dependence and may not be called
H1$_{\rm gap}$.

## 3. Workstream B — exact blocking to H1$_{\rm gap}$

**Question.**  How can the exact fine-to-coarse push-forward be shown to
satisfy the successive-correlation estimate rather than merely reproduce
selected Wilson loops?

**Precise target.**  Construct a local gauge-covariant block map with a
fixed support buffer $b$ and prove, for a closed local test algebra,
\[
 \left|\langle F^{(k)};G^{(k)}\rangle-
 \langle F^{(k+1)};G^{(k+1)}\rangle\right|
 \le C_k\|F^{(k)}\|\|G^{(k)}\|e^{-\gamma_*d_k},            \tag{B1}
\]
with $\gamma_*>0$ independent of refinement depth, periodic volume, and
$k<K(a_0)$.  The exact telescoping lemma then transports this to the
physical scale; it does not need invented residual cross-correlation
bounds.

**Independent attack lines.**

1. Use the exact series/parallel and heat-kernel identities to isolate the
   generated transverse interaction of one blocking step, then prove a
   weighted polymer/small-field estimate for its *connected* effect.
2. Compare raw decimation with a flowed, gauge-covariant block variable.
   The latter may improve locality, but reflection positivity and the
   support buffer must be retained explicitly.
3. Work backwards from a Dobrushin--Shlosman norm: show that a generated
   interaction stays in a local interaction ball whose norm gives (B1).
4. Search for large-field/centre sectors whose density prevents a uniform
   $\gamma_*$.  A negative finding is valuable only if it is expressed as a
   failure of (B1), not as a heuristic phase diagram.

**Milestone boundary.**  Weak-coupling steps and the final order-one
crossover steps are different problems.  A uniform proof through the
former plus an explicit finite list of unresolved latter steps is progress;
calling that a continuum proof is not.

## 4. Workstream C — analytic one-box mixing (H2)

**Question.**  Can one certify a gauge-invariant mixing neighbourhood at
one physical coupling without mistaking Haar single-link marginals for
physical mixing?

**Precise target.**  Choose a finite reference interaction and prove, for
all interactions in a stated norm ball, a Dobrushin--Shlosman-type bound
on gauge-invariant local observables,
\[
 |\langle X;Y\rangle|\le C'\|X\|\|Y\|e^{-\gamma'd(X,Y)},
 \,\qquad \gamma'>0,                                      \tag{C1}
\]
with constants independent of periodic volume.

**Independent attack lines.**

1. Derive a hand-checkable local conditional-distribution contraction for
   small Wilson-loop algebras, including an explicit gauge fixing or
   gauge-invariant quotient.
2. Investigate a nearby fundamental--adjoint interaction chosen to avoid
   the scalar-softening endpoint, then prove that the desired Wilson
   trajectory enters its certified open ball.
3. Derive finite-volume boundary sensitivity bounds using character
   expansions with analytic remainder estimates.  Numerical fits may guide
   a conjecture but cannot serve as the certificate under this project's
   rules.
4. As an adversarial test, try to construct boundary data or centre-flux
   sectors that violate (C1).  This prevents a channel-specific glueball
   estimate from being mislabeled as strong mixing.

## 5. Workstream D — H1$_{\rm OS}$, H3, and the spectral limit

**Question.**  Which renormalized local objects survive both limits, and
how is the lattice lower support bound carried to their OS spectral
measures?

**Precise target.**  Specify $\mathcal A_R$, prove
\[
 \sup_{a_0}\sum_{k<K(a_0)} C_k(a_0)
 \|F^{(k)}\|\|G^{(k)}\|<\infty,                            \tag{D1}
\]
then establish tightness/convergence of its Schwinger functions,
reflection positivity, Euclidean covariance, local generation of the OS
space, and weak convergence of vacuum-subtracted spectral measures.

**Independent attack lines.**

1. Start with flowed Wilson-loop observables at positive physical flow
   time, where a bounded test algebra and reflection-compatible smearing
   may be tractable; only then study flow-time removal.
2. Prove support preservation directly for Laplace transforms of positive
   spectral measures.  This keeps the spectral statement separate from
   field-coordinate convergence.
3. Build the gapless control in parallel: if positive local spectral
   weight remains in every interval $(0,\epsilon)$, the soft-weight
   proposition proves zero threshold.  Eigenvalues whose residues vanish
   decide neither alternative.
4. Test each proposed compactness claim against free Maxwell and the
   massless-pion channel, both of which have a positive action scale but
   soft observable spectral weight.

## 6. Workstream E — foundations model and action calibration (independent)

**Question.**  What exactly follows from a universal positive action
constant once quantum kinematics and operational record closure are stated
rather than smuggled in?  This is independent of the Yang--Mills gap and
now takes priority.

**Completed model target.**  The programme now begins with C0 classical
mechanics in [the classical-to-$h$ ladder](../notes/classical-mechanics-to-h-ladder.md).
Its C1--C4 stochastic augmentation derives one universal positive action
$\kappa=mD$ from nondegenerate free fluctuations and mass composition, but
does not derive those fluctuation premises or their numerical calibration.
The conditional finite nonrelativistic model in
[the foundations note](../notes/foundations-model-nonrelativistic-quantum-mechanics.md)
is the next completion: it separates the supplied/calibrated action (F0),
regular Weyl kinematics (F1), positive states/effects (F2), self-adjoint
dynamics (F3), CP record closure (F4), and interacting composition (F5).
Under them it reconstructs the finite Schrödinger/Weyl representation, Born
probabilities, unitary dynamics, tensor composition, and an explicit
quantum-limited Gaussian instrument.  It is a model, not a derivation of
F1--F5.

**Physical targets now open.**

1. Establish or falsify C1--C4 as a physical law of free motion, then
   derive a composition-closed physical readout restriction selecting the
   same $h_*>0$ and justify the empirical calibration
   \[
   h_*=\hbar=\hbar_{\rm YM}=h_P/(2\pi).                      \tag{E1}
   \]
2. Find a nonclassical operational principle that selects F1's Weyl
   cocycle and complex Hilbert kinematics.  A record floor alone cannot do
   this because it has a commutative Gaussian realization.
3. Extend the finite model beyond Stone--von Neumann uniqueness to
   relativistic fields, gauge constraints and inequivalent
   representations, without using the Yang--Mills gap as an input.
4. Separately, if a Yang--Mills theorem is obtained, prove a
   scheme-controlled finite nonzero $a_*\Lambda$ before writing
   $E=C\hbar c\Lambda$.

**Adversarial checks.**  Compact weak-coupling $U(1)$ and massless
Goldstone channels must continue to satisfy the positive-action premises
while failing the spectral conclusion.  Likewise a commutative
noise-closed Gaussian record model must remain a counterexample to any
claim that a record floor by itself derives F1.

## 7. Dependency order and stop rules

```text
A (fixed-cutoff nonconstant modes) ─┐
                                    ├─> B (H1_gap) ─┐
C (one-box mixing H2) ─────────────┘                ├─> D (H1_OS + H3) ─> (1)
                                                     └─> T3 / C only after scale control

E (F0--F5 foundations model and calibration) ── independent;
    its calibrated hbar may be used by both programmes but proves neither.
```

- A is not required to begin B, but it is the clearest weak-small-volume
  test of the nonconstant-mode mechanism.
- B and C must be attacked independently; a successful one-box proof does
  not control the ultraviolet depth, while weak-step estimates do not
  prove an infrared box gap.
- D begins by fixing the observable algebra, not after declaring a gap.
- E is now a first-class independent foundations programme.  It may supply
  a calibrated $\hbar$, but must never be used to fill an analytic gap in
  A--D, and A--D must never be represented as deriving F1.

A workstream stops and reports rather than silently broadening its claim
when it encounters: cutoff growth not absorbed by a stated renormalization;
loss of support locality; a bound depending on $L$; a proof only for a
single correlator; or an unproved positivity/compactness transfer.

## 8. Delegation and commit attribution protocol

The intended delegation uses **independent** analysts, not a chain that
shares an assumed conclusion:

| Workstream | Delegated role | Required report |
| --- | --- | --- |
| A | spectral/Feshbach analyst | derivation of one bound or a UV obstruction, with oscillator and regulator conventions |
| B | lattice-RG analyst | exact block identity plus a norm in which the B1 remainder is estimated |
| C | mixing/cluster-expansion analyst | gauge-invariant conditional measure and a volume-uniform contraction or counterexample |
| D | constructive-QFT/spectral analyst | observable algebra, tightness route, and support-preservation proof |
| E | classical/stochastic foundations analyst | C1--C4 physical-law audit, calibration assumptions, and a commutative-model countercheck |

For every actual contribution, the integrating commit will include the
workstream identifier in its subject, a short `Contribution:` paragraph in
its body, and truthful trailers:

```text
Co-authored-by: <selected subagent identity> <provided-address>
Assisted-by: <selected subagent identity> (<workstream and report scope>)
Reviewed-by: <selected subagent identity> (<what was checked>)
```

`Co-authored-by` is reserved for text/derivations incorporated from that
agent.  `Assisted-by` is used for an idea, audit, or failed route that
materially shaped the commit.  No trailer will be invented for an agent
that was not actually run; the integrator's ordinary Arena trailer remains
separate.  Each report will be retained in a named, lightweight research
note or summarized in the commit body so that later authors can audit the
attribution.  Since this Arena checkout is fixed to one branch, all such
commits remain on `arena/01a0e7ac-navstokgap` rather than opening
workstream branches.

## 9. First concrete tasks

1. **E1 classical entry point — completed conditionally:** begin with C0,
   prove the no-go boundary, and derive $\kappa=mD>0$ from C1--C4.  This is
   now recorded in [the classical-to-$h$ ladder](../notes/classical-mechanics-to-h-ladder.md).
2. **E2 physical audit — first live foundations task:** test whether a
   specified retained-memory physical model justifies C1--C4 and the same
   constant in the record/radiation sector, rather than assuming either
   Brownian noise or Planck calibration.  Report separately whether it
   supports only the commutative Gaussian alternative or F1.
3. **A1 audit — completed at the fixed-cutoff level:** calculate the
   finite-cutoff fibre-vacuum quantum metric on the $SU(3)$ Cartan patch
   and compare its Born--Huang energy with $g^{2/3}\hbar c/L$.  The
   $S_\Lambda\asymp L^3\Lambda$ frequency-diagonal cost is now in the
   Feshbach note; its physical Gauss/frame renormalization remains open.
4. **B/D benchmark — completed for a $3+1$ global-$U(1)$ scalar:** the
   finite-range Gaussian covariance decomposition gives exact kernel
   H1$_{\rm gap}$, summable Weyl H1$_{\rm OS}$ seminorms, and massive OS
   reconstruction.  The [benchmark note](../notes/u1-gaussian-blocking-os-benchmark.md)
   records the complete proof and its supplied-mass/global-symmetry scope.
5. **C1 choice:** select one analytic mixing criterion and write its
   gauge-invariant conditional distributions; do not start from an
   unverified numerical correlation length.
6. **A2 positive target:** on a periodic gauge-invariant regulator,
   isolate a renormalized fibre projection or a controlled nonconstant-mode
   sector whose relative Schur bound is finite before attempting the full
   $SU(3)$ estimate.

E2 remains the first delegated task.  C and A now follow the completed B/D
benchmark and should be merged only after their assumptions are reconciled.
