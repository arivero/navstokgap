# B22 observable access: source companion

Status: coordinator reviewed for G02; see the
[review](../../../reviews/observable-access-B22.md).

Result: Levin–Peres–Wilmer supplies the exact product-chain spectral facts
needed for C045–C046, but in two distinct normalizations. Chapter 12 treats a
discrete-time random-scan chain with coordinate weights; Chapter 20 treats a
continuous-time chain based on the uniform average of lifted transitions. The source
supports the tensor-product eigenbasis and the corresponding minimum-gap rule,
not the proposed four-state observable counterexample itself.

## Source identity and route

David A. Levin and Yuval Peres, with contributions by Elizabeth L. Wilmer, *Markov Chains and
Mixing Times*, 2nd ed., American Mathematical Society (2017), author-hosted
PDF: <https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf>. Downloaded to the
bounded audit cache as `.build/b22/mcmt2e.pdf`; SHA-256
`9ef39f9467d9647ff3f5e8747b9ce24b7a90d13be2f8156fbd827b95b661a772`.
The coordinator verified authorship against the title-page extraction and
author-hosted book page, independently checked the hash, and visually read
printed pp. 169–170 and 285 (PDF pages 185–186 and 301). The worker read
pp. 169–170 and 285–286 through layout-preserving text extraction.
Redistribution rights remain unestablished; the original stays in the cache.

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

## Coordinator proof correction

Corollary 12.13's displayed gap formula is correct for reversible factors and
positive coordinate weights. Its printed proof's index-selection sentence
uses `max w_i lambda_i`; the needed index minimizes `w_i gamma_i` among
nonconstant factor modes. G02 proves the generator result directly from all
eigenvalue sums, rather than importing that sentence. The printed eigenvalue-set
display also lists the probability-weight constraints; weights are fixed by
the chosen chain. The coordinator confirmed these features in the page image.

Search coverage: one worker primary PDF and four selected pages; the worker
handoff supplies no exact discovery-query count. Coordinator opened the
author's book page and used the saved PDF; no broader novelty search was added.
