# B22 observable access: source companion

Status: worker draft awaiting coordinator metadata, normalization and visual
source review; see the [checkpoint handoff](../../../research/handoffs/restart-skills-2026-09-08.md).

Result: Levin–Peres–Wilmer supplies the exact product-chain spectral facts
needed for C045–C046, but in two distinct normalizations. Chapter 12 treats a
discrete-time random-scan chain with coordinate weights; Chapter 20 treats a
continuous-time chain whose generator is the (uniform) lifted sum. The source
supports the tensor-product eigenbasis and the corresponding minimum-gap rule,
not the proposed four-state observable counterexample itself.

## Source identity and route

David A. Levin, Yuval Peres and Elizabeth L. Wilmer, *Markov Chains and
Mixing Times*, 2nd ed., American Mathematical Society (2017), author-hosted
PDF: <https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf>. Downloaded to the
bounded audit cache as `.build/b22/mcmt2e.pdf`; SHA-256
`9ef39f9467d9647ff3f5e8747b9ce24b7a90d13be2f8156fbd827b95b661a772`.
Metadata and source route are verified; the specified passages were read from
the PDF text extraction (layout retained). No scan/equation visual defect was
encountered in these pages.

## Exact passages read

* Chapter 12, §12.4, pp. 169–170: equation (12.22) defines the weighted
  discrete-time random-scan product transition matrix. Lemma 12.12 states
  tensor-product eigenfunctions have eigenvalue `sum_j w_j lambda_j` and that
  tensor products of coordinate eigenbases form a basis. Corollary 12.13
  states the product-chain spectral gap is `min_j w_j gamma_j`.
* Chapter 20, §20.4, pp. 285–286: equation (20.22) lifts each coordinate
  transition matrix; the continuous-time chain uses the uniform average
  `P = n^{-1} sum_i P-tilde_i`. Theorem 20.7 gives mixing bounds for this
  normalization. This passage is a mixing-time result, not a continuous-time
  generator-sum identity; the generator-sum identity follows directly by
  exponentiating the commuting lifted coordinate generators.

## Application and limits

For independent reversible factors with continuous-time generators `Q_i`, the
model generator is `A_1 tensor I + I tensor A_2` (where `A_i=-Q_i`). Its
tensor-product eigenvectors have eigenvalues `a_1+a_2`; hence the nonzero gap
is `min(gap_1,gap_2)`. This is the continuous-time analogue of Corollary
12.13 with weights one, and is an established tensorization ingredient.

For the two-sign factors in C045, each flip generator has nonzero eigenvalue
`2 lambda` or `2 epsilon`; therefore the four-state spectrum is
`0, 2 lambda, 2 epsilon, 2(lambda+epsilon)`. The source does not state this
particular example, nor the susceptibility calculation. Those are derived
consequences of the source's product construction plus direct diagonalization.

The chapter-12 random-scan normalization would instead give rates weighted by
coordinate-selection probabilities (for equal weights, a factor `1/2` in the
two-factor gap). Do not cite it as evidence for a generator whose constituent
rates remain `lambda` and `epsilon`. Likewise, for N identical factors, a
fixed per-factor continuous-time generator has gap `2 lambda` independent of
N, while a total-rate-one random scan has the expected `1/N` slowdown.

## Prior-art classification

C045's hidden-label family and the stronger injective velocity family are
model-specific derived counterexamples: distinct observed velocities do not
force a uniform linear observability bound, and the exact plateau/gap formulas
are not claimed as literature novelty. C046's independent-product gap rule,
local-sector frame decomposition, and mixed-sector rate addition are standard
tensorization consequences. A fresh audit is required once factors are coupled
or the receiver is constrained dynamically.
