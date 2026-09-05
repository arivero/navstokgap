# First milestone review

Date: 2026-09-05. Assessment by the authoring agent, not an independent referee.

## Deliverable and scope

[The comparison](../notes/comparison-and-bridges.md) establishes the distinctions
needed for the upcoming toy-model discussion. It includes official target
quantifiers, elementary scaling and dissipation calculations, a bridge assessment,
and separate treatments of finite-box decay, stochastic mixing and quantum mass.
The toy model has not yet been specified; no model was invented or investigated.

## Mathematical checks

- Compared the definitions with Fefferman's A–D and Jaffe–Witten's §4. Preserved
  forcing asymmetry, spatial versus spacetime dimensions and quantum existence.
- Checked scaling by the change of variables $z=\lambda x$: fluid energy exponent
  $2-d$, fluid gradient norm squared exponent $4-d$, curvature-action exponent $4-d$.
  The matching latter exponents concern different quantities, not identical theories.
- Checked fluid integration by parts under smoothness and vanishing boundary terms;
  action dissipation uses the explicitly stated normalisation and smooth flow.
- Checked Fourier wavevectors $2\pi n/L$: amplitude decay rate
  $\nu(2\pi/L)^2$, energy decay exponent twice that rate, with the mean removed.
- Checked auxiliary generator rescaling leaves the invariant law unchanged while
  changing its clock. The physical spectral calculation assumes reconstruction,
  a self-adjoint Hamiltonian, and vacuum-orthogonal vectors in the Hilbert space.
- Checked source anchors for Tao's Theorem 1.5, Chevyrev's Theorem 1.6 and cemetery
  state qualification, and Lüscher's gauge-modified flow (2.2). Corrected the latter
  equation reference during drafting.

## Verification limits

The source skill supplied local originals and selective Markdown companions.
There is no full transcription, independent proof verification, formal certificate
or exhaustive survey of current research. Historical open-question statements are
dated to their sources. Release news in the orientation README plays no role in
the mathematical comparison.

Repository checks cover source checksums, local Markdown links, document conversion
and staged whitespace. No simulations or test suite are appropriate to this
documentation milestone. Commit identity is reported in the handoff and Git history.
