# Cutoff for the Ising model on the lattice

> Eyal Lubetzky and Allan Sly. Preprint: 23 September 2009;
> *Inventiones Mathematicae* **191** (3), 719–755 (2013).
> [arXiv:0909.4320v1](https://arxiv.org/abs/0909.4320v1),
> [PDF](https://arxiv.org/pdf/0909.4320v1),
> [DOI:10.1007/s00222-012-0404-5](https://doi.org/10.1007/s00222-012-0404-5).
> Retrieved 2026-09-13. Selected-passage digest, not a full transcription.

## Source statements

- PDF/printed p. 4, opening paragraph: the zero-field one-dimensional gap is
  $1-\tanh(2\beta)$, independent of size. The authors identify this as already
  known, citing their reference [23]. This directly matches C124.
- P. 4, Corollary 3: the periodic chain has cutoff at
  $\tfrac12[1-\tanh(2\beta)]^{-1}\log n$.
- P. 5, prose after Eq. (1.2): heat-bath updates use independent rate-one
  site clocks and conditional Gibbs resampling.
- P. 3, Theorem 2, and p. 9, §2.2: cutoff and total-variation mixing concern
  approach to equilibrium, separately from the spectral-gap quantity.

## Repository convention map

The source's reduced coupling $\beta$ is our $b$. Restoring the rate in
$Q_a=aQ_1$ gives C124's $a[1-\tanh(2b)]$. The source's external field $h=0$
is unrelated to an action constant. See [B73](../references/batches/B73.md)
and [the foundational assessment](../notes/ising-foundational-value.md).

## Coverage and archive

Coordinator read PDF pp. 3–5 and 9 using `pdftotext -layout`, and visually
checked pp. 4–5 using `pdftoppm`. Metadata was verified on arXiv. The cutoff
proof and published-edition pagination were outside this selected reading.

The displayed flip-rate signs on v1 p. 5 differ from those implied by its
positive-coupling Gibbs law and conditional-resampling prose. Those rates are
not imported: C124 uses its independently checked conditional law. The
normalization match uses the clock prose; the exact gap statement uses p. 4.

Inspection copy: `.build/b73/LubetzkySly_IsingCutoff_0909.4320v1.pdf`, 34 pages.
SHA-256: `2c72ec3ebe84c0e38eef3815ab6c50899d0b937934aab3ff6ee8cf56687782ac`.
The original remains in the ignored cache, following B71's practice; public
redistribution rights were not established. This digest and metadata are
committed. The cache hash is recorded here rather than in `docs/SHA256SUMS`,
which checks tracked originals available after a fresh clone.
