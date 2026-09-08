# B23 harmonic receiver source companion

## Scope and coverage

Bounded audit for A10 (2026-09-08): two discovery searches, two primary PDFs,
nine pages reported read in total, exceeding the assigned six-page budget.
Ford–Kac–Mazur was read on printed pp. 504–506
(PDF pages 2–4, including the abstract/introduction and equations (1)–(12)).
Zwanzig was read on PDF pp. 215–220 (all six PDF pages), with emphasis on
equations (5)–(19), (21)–(30). No Rubin paper was opened; it remains a lead.

## Sources

1. G. W. Ford, M. Kac and P. Mazur, “Statistical Mechanics of Assemblies of
   Coupled Oscillators,” *J. Math. Phys.* **6** (1965) 504–515,
   DOI 10.1063/1.1704304. Open PDF route:
   https://fig.if.usp.br/~marchett/fismat3/coupled-oscillators_ford-kac-mazur.pdf
   Metadata and equations were extracted from the downloaded PDF; the host is
   an unofficial mirror and copyright notice is retained in the PDF.
2. R. Zwanzig, “Nonlinear Generalized Langevin Equations,” *J. Stat. Phys.*
   **9** (1973) 215–220, DOI 10.1007/BF01008729. Open PDF route:
   https://courses.physics.ucsd.edu/2020/Fall/physics210b/Zwanzig1973_NonlinearGeneralizedLangevinEq.pdf
   Six-page PDF; text extraction is legible but typography/OCR spacing is poor.

## Source-to-model findings

Ford–Kac–Mazur explicitly frames a chain of coupled oscillators as a heat bath
and describes the program: solve the mechanical system, draw bath initial data
from a statistical distribution, and obtain stochastic processes. Their finite
Hamiltonian solution uses matrix cosine/sine propagators (eqs. (2)–(5)); under
canonical preparation the process is stationary (eq. (8)) and Gaussian, with
pair correlations (eqs. (9a–c)). They identify the momentum autocorrelation of
one oscillator and state that an exponential correlation is the Markov case
(eqs. (10)–(11)). The paper then takes an infinite-chain limit and seeks a
coupling yielding Markovian behavior. This supports the A10 distinction between
finite quasiperiodic receivers and a reservoir limit, but does not establish
the project’s displacement-action observable or its phase-torus preparation.

Zwanzig derives an exact reduced generalized Langevin equation from a Hamiltonian
system coupled to a quadratic oscillator bath. The bath covariance under a
conditional canonical distribution is kT K^-1 (eq. (16)); noise covariance and
friction kernel obey the fluctuation–dissipation relation (eq. (17)). In the
explicit oscillator bath, the memory kernel is a cosine sum over frequencies
and couplings (eq. (23)), and the equation is exact and non-Markovian (p. 219).
Replacing the frequency sum by a continuous Debye density removes very-long-time
Poincare recurrences and gives an approximate delta kernel (eqs. (25)–(30), p.
220). This supplies a concrete next test: specify spectral density and coupling
scaling before claiming a positive receiver plateau.

## Audit classification and normalization

The draft finite-network normal-mode calculation is a derived consequence of
the stated Hamiltonian and independent uniform phases: fixed mode energies give
zero cross terms and cosine velocity covariance. The formula

`h_i(Delta) = (2 m_i/Delta) sum_j w_ij [1-cos(omega_j Delta)]/omega_j^2`

has correct action units because `m_i w_ij/omega_j^2` is mass times length
squared; its bound by `4 m_i B_i/Delta` proves the fixed finite receiver’s
long-window limit is zero. The independent centre velocity contributes the
derived ballistic term `m_i Var(V_cm) Delta`; deterministic drift contributes
no variance. The two-body coefficient is consistent with the reduced-coordinate
amplitude `M_r/(m+M_r)` and `omega^2=k/mu`, yielding the stated
`2 m E/k Delta` prefactor. The speed bound follows directly from fixed total
energy and the smallest mass.

These are not literature claims: label them “derived, finite-dimensional.”
Ford–Kac–Mazur and Zwanzig establish the broader oscillator-bath and memory-kernel
constructions. The necessary condition that a positive large-receiver limit
requires loss of uniform control of `m_i B_i/Delta` is an elementary derived
implication, not a theorem attributed to either source. It is not sufficient:
low-frequency weight, preparation, tagged coordinate and order of limits remain
to be specified.

## Access failures and limits

The University of Michigan repository result for Ford–Kac–Mazur returned HTTP
403 in the browser; the mirror PDF was used instead. No source scan or Rubin
chain paper was read. Consequently, no claim is made about exact passages beyond
the nine pages listed above. Coordinator corrected the worker's inconsistent
page count; no further worker reading was commissioned.

## Coordinator verification and retained originals

Coordinator visually checked Ford–Kac–Mazur printed p. 505 (PDF p. 3) and
Zwanzig p. 219 (PDF p. 5), and read the latter's p. 220 extraction. The
Ford source explicitly handles the canonical zero-mode difficulty by first
excluding zero eigenvalues. A10 instead fixes the centre coordinate/momentum.
Zwanzig's friction kernel is distinct from a tagged velocity covariance;
the reduced tracer equation is needed to connect the two.

Cached originals and independently computed SHA-256:

- `.build/b23/ford-kac-mazur.pdf`:
  `94af20edeaa11240c70666be1f063d7d65c1f4d6739aeb4e268dacd41b0d27ef`.
- `.build/b23/zwanzig-1973.pdf`:
  `8ec180512ab14a8ae51fa1f17af36753b472768f39a94f657597206d18b88d75`.

Retrieval: 2026-09-08; `pdftotext -layout` outputs reside in the same cache.
Publication rights were not established; PDFs remain outside tracked sources.
Coordinator used two additional metadata searches, including Michigan's
repository record for Ford–Kac–Mazur. These are selected readings, not full
proof audits of the infinite-reservoir constructions.
