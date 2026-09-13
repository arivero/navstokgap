# B71: Hermitian stochastic-parent source companion

The two primary sources verify the general detailed-balance construction used
in C126. Their conventions differ from the project's: both sources write the
master equation on probability columns, whereas C126 writes a generator on
functions. After transposition, Henley's Eq. (3.7) is precisely the project's
`D^(1/2) Q D^(-1/2)` similarity transform. Neither source turns an arbitrary
Monte Carlo clock into physical time or derives a universal action unit.

## Source 1: Henley's classical-to-quantum construction

Christopher L. Henley, *From classical to quantum dynamics at
Rokhsar--Kivelson points*, *Journal of Physics: Condensed Matter* **16**
(2004), S891--S898. DOI
[`10.1088/0953-8984/16/11/045`](https://doi.org/10.1088/0953-8984/16/11/045);
arXiv [`cond-mat/0311345v1`](https://arxiv.org/abs/cond-mat/0311345), submitted
14 November 2003.

- Primary route read: <https://arxiv.org/pdf/cond-mat/0311345>.
- Retrieval date: 2026-09-13. The worker retained no original; coordinator cache is recorded below.
- Extraction/inspection: arXiv's indexed PDF text, checked against the PDF page
  and equation layout exposed by the route.
- Rights: arXiv-hosted author manuscript; no redistribution assessment was
  needed because originals are retained only in the ignored audit cache.

### Passage coverage

Reading level: **passage**. One substantive page was selected, arXiv PDF p. 7.

- PDF p. 7, Eq. (3.7): for unequal equilibrium weights, Henley defines
  `W_tilde = P^(-1/2) W P^(1/2)` and states that detailed balance makes it
  symmetric; being similar to `W`, it has the same eigenvalues. He then says
  the quantum Hamiltonian is proportional to this symmetric matrix.
- PDF p. 7, Eqs. (3.8) and following prose: the transformed hopping element for
  a local move depends only on its immediate environment when the classical
  energy is a sum of local terms. This supports locality inheritance, not the
  exact C126 coefficient formula.

Henley's `W` acts on probability columns and has nonnegative off-diagonal
entries. C126's `Q` acts on functions and uses the row convention. Thus
`W=Q^T`, and transposing Eq. (3.7) gives
`D^(1/2) Q D^(-1/2)`, with C126's positive operator obtained by a minus sign.
The apparent inverse placement of `D^(1/2)` is only a convention change.

## Source 2: stochastic matrix form

Claudio Castelnovo, Claudio Chamon, Christopher Mudry and Pierre Pujol,
*From quantum mechanics to classical statistical physics: generalized
Rokhsar--Kivelson Hamiltonians and the "Stochastic Matrix Form"
decomposition*, *Annals of Physics* **318** (2005), 316--344. DOI
[`10.1016/j.aop.2005.01.006`](https://doi.org/10.1016/j.aop.2005.01.006);
arXiv [`cond-mat/0502068v1`](https://arxiv.org/abs/cond-mat/0502068), submitted
2 February 2005.

- Primary route read: <https://arxiv.org/pdf/cond-mat/0502068>.
- Retrieval date: 2026-09-13. The worker retained no original; coordinator cache is recorded below.
- Extraction/inspection: arXiv's indexed PDF text, checked against the PDF page
  and equation layout exposed by the route.
- Rights: arXiv-hosted author manuscript; no original was redistributed.

### Passage coverage and anchors

Reading level: **passage**. Seven substantive pages were selected: arXiv PDF
pp. 8--10 and 12--15.

- PDF pp. 8--10, Eqs. (8)--(15): each two-configuration block is positive
  semidefinite with one zero mode. Under the integrability conditions, the
  common nodeless zero mode has amplitudes proportional to
  `exp(-K E_C/2)` and hence squared amplitudes equal the classical Boltzmann
  weights. This is the general source match for positivity,
  frustration-freeness and the square-root Gibbs state.
- PDF pp. 12--14, Eqs. (19)--(27): the authors define the transition matrix by
  a diagonal similarity from the Hermitian matrix, derive detailed balance and
  probability conservation, and give `lambda_n=-epsilon_n`. This supports the
  equality between stochastic relaxation rates and the positive Hamiltonian
  spectrum, subject to the source's sign and column conventions.
- PDF pp. 14--15, Eq. (28b) and following prose: Glauber dynamics is one
  permitted choice of symmetric move coefficient. The coefficients remain free
  after fixing the equilibrium ground-state weights and determine the
  excitation/relaxation spectrum. This directly supports C126's conclusion that
  the Gibbs law does not select the clock or the gap normalization.

The source's symbol `K` in Eq. (15e) is the dimensionless reduced inverse
temperature `beta J`. C126 instead uses `b=beta J` and reserves `K` for a
constant with action units. The source therefore does not supply C126's action
constant; conflating these two symbols would be dimensionally wrong.

## Coverage limit and source-to-task use

The audit used exactly two primary sources, three discovery queries and eight
substantive PDF pages. It did not read either paper in full, audit the proofs of
the general SMF theorems, or locate a published formula identical to C126's
three-site heat-bath term. Search snippets and adjacent page fragments were
discovery/context only. Metadata was checked on each arXiv abstract page.

Source claim and project inference remain separate. The sources establish the
general square-root transform, spectral correspondence, local-move inheritance
and rate freedom. C126 derives the explicit Ising coefficients from C124's flip
rates and manually checks the operator term by term. The source-to-model lesson
is that the stochastic rates are extra dynamical data. An independent physical
Hamiltonian interpretation needs a physical clock, an action conversion and a
state/observable interpretation beyond detailed balance.

## Coordinator verification and corrected anchors

The worker used zero-based PDF page indices as page numbers. The anchors above
are corrected to one-based pages: Henley p. 7; Castelnovo pp. 8–10 and 12–15
(eight substantive pages in total, unchanged passage selection). The coordinator
reread the cited formulas and visually checked Henley p. 7 and Castelnovo
pp. 9, 10, 12, 14, 15. No extra source or discovery query was added.
The general SMF proof remains outside this selected-passage audit.

Public arXiv PDFs were downloaded to the ignored cache with curl; pdfinfo and
pdftoppm supplied page counts and visual formula checks. Cached originals:

- `.build/b71/henley.pdf`, SHA-256
  `528958edbadf46b0bb2184da0dddd7a93f07fd6a03d45ae5ec791886b8e8773e`.
- `.build/b71/castelnovo.pdf`, SHA-256
  `1800cc9ec85cd90731185a07a585b4867eda0c9efcb0d62c439d8a78da164c9c`.

No originals were added to the tracked source collection. This companion is
the maintained digest; quoted formulas are checked against the source images.
