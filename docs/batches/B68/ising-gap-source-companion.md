# B68: interacting Ising gap source companion

The two bounded sources match the ingredients of C124 but do not, within the
pages read, state its full all-mode spectral-gap theorem. Glauber gives the
nearest-neighbour flip rate, its independent clock normalization, the
finite-ring one-spin modes and the magnetization decay rate
`a[1-tanh(2b)]`. Bubley--Dyer gives the Hamming-path and maximal-coupling
construction behind the contraction method. The continuous-time coupling-to-
full-spectrum argument and the matching of its lower bound to Glauber's
magnetization mode are checked in the project review, not attributed to either
source. No novelty claim is made.

## Source 1: Glauber's kinetic Ising chain

Roy J. Glauber, *Time-Dependent Statistics of the Ising Model*, *Journal of
Mathematical Physics* **4** (1963), 294--307. DOI
[`10.1063/1.1703954`](https://doi.org/10.1063/1.1703954).

- Publisher record and version-of-record PDF route:
  <https://pubs.aip.org/aip/jmp/article/4/2/294/230204/Time-Dependent-Statistics-of-the-Ising-Model>
  and
  <https://pubs.aip.org/aip/jmp/article-pdf/4/2/294/19156949/294_1_online.pdf>.
  The PDF route returned HTTP 403 on 2026-09-13; no publisher PDF was read or
  cached.
- Accessible reading route: the public Scribd-hosted indexed scan/transcription
  at <https://www.scribd.com/document/455589659/glauber1963-pdf>. The page
  identifies the article, reproduces journal page numbers and exposes OCR text
  from a scan downloaded there in 2012. This is third-party hosting, not the
  publisher or author.
- Metadata cache: `.build/b68/glauber-crossref.json`, SHA-256
  `0c24d049ce6958aa209173138ede97703fa06dcf832a298654562e0fafe8c6b5`.
  Crossref identifies the author, title, journal, volume, issue, date, pages,
  DOI and publisher PDF URL.
- Access-page cache: `.build/b68/glauber-scribd.html`, SHA-256
  `a0fa5eb62d6f3c05eb60eb285800ad3661096c65bd42c6528aa619c62419c269`.
  This hash identifies the retrieved HTML, not the underlying article scan.
- Rights: publisher copyright applies; no redistribution right was established.
  Only the access-page HTML and metadata are retained in the ignored audit
  cache.

### Passage coverage and anchors

Reading level: **passage** through the indexed OCR/transcription, not original
PDF/image reading. Five nonconsecutive substantive printed pages were used:
pp. 295--296 and 298--300. The equation images and symbols have OCR defects;
formula transcription remains subject to coordinator visual checking against
an authorized image or PDF.

- Printed pp. 295--296, Eqs. (1), (8)--(10), (12)--(17): the uncoupled flip
  rate is `a/2`; the closed ring is a continuous-time Markov process; the
  chosen nearest-neighbour rate has three values `a/2`,
  `a(1-gamma)/2`, and `a(1+gamma)/2`; detailed balance with the equilibrium
  Ising law fixes `gamma=tanh(2J/kT)`. The prose immediately after (17) says
  that `a` only sets the transition time scale and has no equilibrium analogue.
- Printed p. 298, Eq. (30): the one-spin expectations satisfy
  `(d/d(at)) q_k=-q_k+(gamma/2)(q_{k-1}+q_{k+1})`. This is the source match for
  `Q sigma_i=-a sigma_i+(a gamma/2)(sigma_{i-1}+sigma_{i+1})`.
- Printed pp. 299--300, Eqs. (44)--(51): periodicity on the finite `N`-ring
  gives Fourier modes with decay rates
  `a[1-gamma cos(2 pi m/N)]`; the uniform mode is the total magnetization,
  which decays with coefficient `a(1-gamma)`.

These passages establish the model and the matching upper-gap eigenmode after
the project identifies `gamma=tanh(2b)` and interprets Glauber's flip process
as rate-`a` conditional Gibbs refreshes that may leave a spin unchanged. The
read pages do not claim that the slowest eigenvalue on the full `2^N`-state
function space equals the slowest one-spin mode. They therefore do not by
themselves establish C124's lower bound.

## Source 2: the coupling construction

Russ Bubley and Martin E. Dyer, *Path Coupling: A Technique for Proving Rapid
Mixing in Markov Chains*, Proceedings of the 38th Annual Symposium on
Foundations of Computer Science (1997), 223--231. DOI
[`10.1109/SFCS.1997.646111`](https://doi.org/10.1109/SFCS.1997.646111).

- Open PDF route used:
  <https://www.math.cmu.edu/~af1p/Teaching/Markov_Chain_Mixing/Papers/Pathcouple.pdf>,
  hosted on a Carnegie Mellon teaching page.
- Cached original: `.build/b68/Pathcouple.pdf`, SHA-256
  `90ef44bf9059c6b053cc463d74665ef920312d8ac6d21f57c603cca139d7f0ef`.
- Extraction: `pdftotext -layout`; metadata and formulas were also checked
  against the PDF rendering available through the route. Redistribution
  rights were not established, so the PDF remains in the ignored cache.

### Passage coverage and anchors

Reading level: **passage**, with the short proof of Theorem 1 inspected. Three
substantive proceedings pages were used, pp. 223--225 (PDF pp. 1--3).

- Printed p. 223, abstract and introduction: path coupling reduces a global
  convergence argument to contraction for adjacent pairs.
- Printed p. 224, Sections 1.1--2: the state space is a product `C^V`, paths
  change one coordinate at a time, and Hamming distance is the path metric.
- Printed pp. 224--225, Theorem 1 and proof: adjacent transition laws are
  maximally coupled, couplings are composed along a Hamming path, and the
  triangle inequality turns one-step adjacent contraction into contraction
  for arbitrary pairs.

Bubley--Dyer treats a discrete-time chain and concludes a total-variation
mixing estimate with a diameter prefactor. C124 instead directly couples every
pair under common continuous-time Poisson clocks, proves
`E D_t <= exp[-a(1-gamma)t]D_0`, and applies the induced Lipschitz-semigroup
contraction to each eigenfunction. The source supports the coupling method;
it is not an exact source for that spectral implication or rate.

## Coverage limit and source-to-task use

The audit used exactly two primary sources, eight substantive pages, and four
discovery searches. It did not search for an exact prior publication of the
full finite-ring gap formula. The bounded result is therefore: model/rate and
magnetization-mode match verified to passage level; coupling construction
matched; C124's full-spectrum equality remains a locally derived consequence
whose proof has been audited separately.

Source-to-task suggestion: retain a uniform bound below one on the summed
single-site conditional influence, together with a positive per-site clock
floor, as the generalizable premise suggested by the coupling. Return to an
inhomogeneous or general-graph version only if it discharges a named physical-
operator or uniform-limit dependency; finite range alone does not supply that
margin.

## Coordinator verification

The coordinator confirmed all three recorded hashes, reread the indexed
Glauber passages around (17), (30), (44)--(51), and visually checked
Bubley--Dyer printed pp. 224--225 from the cached PDF. Glauber formula images
remain unavailable. One additional discovery query found no usable original,
so total search coverage is five queries including the worker's four. No
additional source or substantive page was added. Exact full-gap acceptance
rests on the local written proof, independently of the unverified original
formula transcription; see the coordinator review.
