# Asymptotic analysis of the Green–Kubo formula

Pavliotis expresses a diffusion coefficient both as an integrated velocity
correlation and through a Poisson equation for the microscopic Markov generator.
This supplies A01's test of a positive action-valued transport coefficient.

- Author: G. A. Pavliotis.
- Version: [arXiv:1002.4103v1](https://arxiv.org/abs/1002.4103v1), 22 February 2010.
- [Primary PDF](https://arxiv.org/pdf/1002.4103v1), retrieved 2026-09-07 into
  ignored `.build/a01/Pavliotis2010.pdf`; extracted with `pdftotext -layout`.
- The generated title-page date is November 2018; the versioned submission
  supplies the bibliographic year. This companion uses preprint page numbers.
- Reading in progress: §1, pp. 1–3, and §2, pp. 4–5, especially (1.3) and
  Proposition 2.1, (2.3)–(2.5). Formula images and checksums will be checked at
  integration. Subsequent proofs and examples have not yet been audited.
- Rights: arXiv research copy; redistribution permission unresolved, so the
  original remains outside the published repository.

## Construction to test

For a finite reversible Markov velocity process, solve the generator Poisson
equation on mean-zero functions. Determine how positivity and eigenvalue bounds
translate into a positive limiting coefficient with action units. Track which
assumptions exclude zero velocity and arbitrarily rapid decorrelation.
