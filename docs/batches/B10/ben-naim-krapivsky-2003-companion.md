# The Inelastic Maxwell Model

> Source: https://arxiv.org/abs/cond-mat/0301238 (PDF downloaded from https://arxiv.org/pdf/cond-mat/0301238)
> Metadata: E. Ben-Naim and P. L. Krapivsky, arXiv:cond-mat/0301238v1, 14 January 2003.
> Local original: `.build/b10/ben-nain_2003_inelastic_maxwell.pdf`
> SHA-256: `f9c1c456ec2089099f37a3c6564944466b5b65cd757ceb7584edcd7f757706fb`
> Extraction: `pdftotext -layout`; p. 6 autocorrelation equations were checked against a rendered page image.
> Rights: arXiv open preprint; retained in the build directory for this bounded audit.

## Source digest

The review solves uniform-rate Maxwell collision processes and records the
autocorrelation of a tagged particle. In its inelastic freely cooling model,
the correlation decays exponentially in collision number; the changing rate
then produces aging and algebraic physical-time decay. The source is therefore
a useful contrast: exponential collision-count relaxation does not imply a
stationary exponential physical-time law when the clock itself cools.

## Selected reading

- Abstract (p. 1): metadata and scope.
- p. 6, Eqs. (14)–(17): collision-number autocorrelation, time-dependent rate,
  aging, and displacement relation.

The result is not an exact match to B10 because B10 has a fixed independent
Poisson clock and a refreshed bath. It supports the proof obligation to keep
collision-count and physical-time limits separate.

## Extraction defects

No material extraction defect on the selected page. The source uses `p` for
inelasticity and a cooling-time-dependent rate, which must not be substituted
for B10's `nu`.
