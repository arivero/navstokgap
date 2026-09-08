# B15 checkerboard source companion

**Result.** The bounded check confirms the remembered 1984 identifiers and the
main conceptual split needed by B15: Gaveau–Jacobson–Kac–Schulman describe a
real Poisson reversal process whose probability law satisfies the telegrapher
equation, then use analytic continuation to obtain the Dirac equation.  The
Feynman–Hibbs checkerboard is a complex path-amplitude construction, with a
corner/reversal weight, not a positive probability rate.  Jacobson–Schulman
connect the relativistic zig-zag scaling to the non-relativistic Brownian
scaling and identify the Compton-length transition scale.  None of these
metadata/abstract readings establishes a universal diffusion/action
coefficient or a mass-additivity theorem.

## Sources and reading coverage

### Feynman and Hibbs (1965)

- **Citation:** Richard P. Feynman and Albert R. Hibbs, *Quantum Mechanics
  and Path Integrals*, McGraw–Hill, New York, 1965, International Series in
  Pure and Applied Physics; ISBN 0-07-020650-3; 365 pages (catalogue
  pagination xiv + 365).
- **Relevant location lead:** Problem 2-6, reported pp. 34–36. The worker
  used secondary search records, including a Durham thesis whose bibliography
  cites an emended edition. Coordinator review therefore leaves first-edition
  pagination unverified. The book pages were not directly read in this run.
- **Lawful metadata route:** CERN record 100771,
  <https://cds.cern.ch/record/100771>; Google Books catalogue,
  <https://books.google.com/books?id=14ApAQAAMAAJ&output=html_text>.
- **Coverage label:** `metadata` plus bounded secondary location lead;
  **not** `passage`. No local original or transcription was created. The
  2005/2010 Styer emended edition must not be silently substituted for the
  cited 1965 pagination.
- **Use:** Treat the checkerboard problem as the historical source lead for
  light-speed zig-zag paths and a complex amplitude depending on the number
  of reversals/corners. The exact convention and normalization still require
  direct page verification before quotation or formula acceptance.

### Gaveau, Jacobson, Kac and Schulman (1984)

- **Citation:** B. Gaveau, T. Jacobson, M. Kac and L. S. Schulman,
  “Relativistic Extension of the Analogy between Quantum Mechanics and
  Brownian Motion,” *Physical Review Letters* **53** (5), 419–422 (30 July
  1984), DOI [10.1103/PhysRevLett.53.419](https://doi.org/10.1103/PhysRevLett.53.419).
- **Publisher route:** APS abstract record,
  <https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.53.419>.
- **Abstract read:** The abstract states that Schrödinger/heat and
  Feynman/Wiener correspond by analytic continuation; the authors identify
  Poisson processes whose real version gives the telegrapher equation and
  whose analytic continuation produces the Dirac equation.
- **Coverage label:** `abstract`; APS full text returned an authorization
  barrier. No equation/page passage or PDF was audited.
- **Interpretive boundary:** “Poisson process” here is a real stochastic
  process with a nonnegative reversal rate. Its analytically continued object
  is not a probability law; it carries complex amplitudes and can reproduce
  Dirac propagation. Do not cite the abstract as proving a positive action
  lower bound or as identifying the rate with a universal action coefficient.

### Jacobson and Schulman (1984)

- **Citation:** Theodore Jacobson and L. S. Schulman, “Quantum stochastics:
  the passage from a relativistic to a non-relativistic path integral,”
  *Journal of Physics A: Mathematical and General* **17** (2), 375–383
  (1 February 1984), DOI
  [10.1088/0305-4470/17/2/023](https://doi.org/10.1088/0305-4470/17/2/023).
- **Metadata route:** CiNii/Crossref record,
  <https://cir.nii.ac.jp/crid/1363388846180061184>; IOP full-text link is
  recorded there as <http://stacks.iop.org/0305-4470/17/i=2/a=023/pdf>.
- **Abstract-level formula lead:** The indexed article text reports that the
  one-dimensional Dirac path integral uses relativistic paths with
  \(\Delta x\sim\Delta t\), whereas typical non-relativistic path-integral
  paths satisfy \((\Delta x)^2\sim\Delta t\), and identifies the transition
  scale as \(\Delta x\sim\hbar/(mc)\), the Compton wavelength (in ordinary
  units). This was obtained from a lawful indexed copy/search extraction,
  not from a coordinator proof audit of the paper.
- **Coverage label:** `metadata` and `abstract/formula lead`; the IOP PDF
  route was not readable in this run. No equation numbering or derivation is
  accepted.
- **Interpretive boundary:** This is a consistency/scaling bridge between
  relativistic checkerboard-like paths and non-relativistic Brownian paths.
  It does not by itself select a universal positive diffusion/action scale.

## Bounded prior-art composition search

One targeted search asked whether the literature already gives a universal
diffusion/action coefficient from center-of-mass mass additivity. It returned
only broad leads: standard center-of-mass mechanics gives total mass
\(M=\sum_i m_i\), while Brownian aggregate diffusion depends additionally on
friction, hydrodynamic coupling and noise assumptions. No exact primary source
matching the proposed universal coefficient was retained. This is a search
lead, not an accepted prior-art match; a future audit should search the
Einstein–Smoluchowski/Rouse and generalized Langevin literature under an
explicit observable and noise model.

## Access and extraction limits

The worker handoff lists four targeted query batches and an additional
composition query, with four page-opening attempts. This exceeded the dispatch's
four-query budget by the reported extra query; no broader search was requested.
Coordinator verification added two targeted metadata queries and DOI/CiNii
opening attempts. APS full text returned
HTTP 403/authorization; the IOP formula route was not retrievable. No PDF was
downloaded, no OCR was performed, and no source formula was visually checked.
Search snippets were used only to locate metadata or bounded abstract-level
claims. Rights and redistribution of book scans remain unresolved.

Coordinator independently verified the APS abstract and CiNii's Crossref-based
Jacobson–Schulman metadata. The indexed Jacobson–Schulman abstract remains a
reading lead; its Compton-scale derivation and corner factors await a directly
checked primary passage. No new formula is accepted from that extraction.

## Next proof obligation

Write the finite-step two-state recurrence with (i) a real reversal rate
\(\lambda\ge0\) and normalized telegraph probabilities, and separately (ii)
the complex corner amplitude used after analytic continuation. Then specify
the limit and normalization that yields the Dirac (or Klein–Gordon) equation,
and test whether any coefficient survives composition as a universal action
parameter. Do not identify \(\lambda\), a diffusion coefficient, or the corner
amplitude with \(\hbar\) without an additional dimensional and physical
premise.
