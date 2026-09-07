# B13 review: physical-cut claims

## Result

The three claims in `notes/physical-cut-speed.md` survive proof audit with
their stated hypotheses. C030 is a direct equal-mass elastic construction and
has `k_mid=m*u^2*Delta`; C031 is a sharp bounded-speed midpoint theorem with a
necessary, not selecting, action bound; C032 is valid only for a
translation-invariant position-only convolution semigroup and forces
deterministic drift. No claim extends to all stochastic mechanics.

## Corrections and qualifications

- Treat Barkai as the source of the elastic collision premise/map, not the
  midpoint formulas.
- State that the centred action identity in C031 has an additional
  `2*m*(E zeta)^2/Delta` term for biased midpoint laws.
- Keep C032's independent-increment and position-only restrictions adjacent to
  the proposition; telegraph motion is outside them because velocity memory is
  retained.
- The fixed-`kappa` scaling raises the pair energy to `kappa/Delta`; it is not a
  positive microscopic action selection at fixed speed.

The symbolic check script passed all 12 checks. Source-page visual checks are
recorded in the companion and batch. Literature status is bounded coverage,
not a novelty certificate.

## Next construction

Build the finite-speed bridge on `(X,V)` using a two-state velocity process:
derive the conditional midpoint distribution given both endpoint positions and
endpoint velocities, retain the no-switch endpoint atoms, and compare its
coarse restriction with a two-stage fine restriction. The bridge should make
explicit which conditional laws are singular at extremal displacement and
which carry velocity-memory correlations. Only after that comparison should a
finite observation-window action be separated from a refinement remainder.

## Coordinator acceptance

C030–C032 are accepted as the stated derived model results. Source review
corrected Barkai (2) to p. 3 and Cinque (1.1)–(1.2) to p. 1. Both cached
hashes and displayed source formulas were checked. The equal-mass collision
uses Barkai's map, not his density formula with a vanishing denominator.
The midpoint saturation proof and additive variance proof were checked
directly. All twelve identities pass. A06 takes up the phase-space bridge.
