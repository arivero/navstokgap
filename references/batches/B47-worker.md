# B47 worker handoff: fixed-coupling calibration

- **Task:** bounded librarian/assumption audit for R16/B47: exact nonlinear
  finite-dimensional readout at fixed small nonzero coupling.
- **Requested route:** Luna, low explicit (worker artifact; no descendants).
- **Date:** 2026-09-11.
- **Inputs:** `notes/fixed-coupling-calibration.md`;
  `docs/batches/B37/autonomous-readout-source-companion.md`;
  `skills/principia-action/SKILL.md`; `skills/navstokgap-bibliography/SKILL.md`.
- **Outputs:** `docs/batches/B47/fixed-calibration-source-companion.md` and
  this handoff only. No claims, papers, shared state, or commits changed.

## Finding

Sideris, ch. 6.1 Theorem 6.1 (PDF pp. 95--96; printed pp. 89--90) and
Corollary 6.1 (PDF p. 98) provide the primary smooth-ODE dependence and
variational-equation precedent. Theorem 6.2 / Corollary 6.3 (PDF pp. 98--99)
cover parameter dependence. Reused Theurel v2 pp. 5--7 from B37 for the
preparation/interaction comparison. Neither source establishes R16's
model-specific `F_lambda=-lambda A z+O_C1(lambda^3)`, its uniform constants, or
global invertibility.

## Coverage and limits

One new search query, one newly opened primary source passage, and one cached
primary passage were used; no numerical or symbolic verification scripts ran.
The source supports differentiating smooth finite-time Hamilton equations on a
common domain. The lower-Lipschitz/injectivity estimate is the project's
written consequence of its explicit remainder bound and singular-value margin,
not a rank-only theorem. No blanket novelty claim is made.

## Next bounded suggestion

R17 should keep incoming probe preparation width fixed and test collisions of
the full nonlinear calibration fibres via an implicit-function argument. This
separates a genuine lower-width resource premise from the removable exact-
calibration remainder.

