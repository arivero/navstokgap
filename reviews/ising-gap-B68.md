# G03 / B68 written proof and source review

C124 is correct for the stated periodic zero-field model with `N>=3`, finite
`b>=0`, and per-site conditional-refresh clock `a>0`. Its exact gap is
`a[1-tanh(2b)]`. The source audit verifies the historical model and method
ingredients under bounded passage coverage; it does not establish a novelty
claim.

## Written proof audit

Let `theta=tanh(2b)`. The conditional Gibbs mean is

```
E[sigma_i | sigma_j, j != i]
  = tanh[b(sigma_{i-1}+sigma_{i+1})]
  = (theta/2)(sigma_{i-1}+sigma_{i+1}).
```

The final equality holds because the neighbour sum is `-2`, `0`, or `2`.
Consequently the rate-`a` refresh generator `a(E_i-I)` flips the present sign
at rate

```
(a/2)[1-(theta/2)sigma_i(sigma_{i-1}+sigma_{i+1})],
```

which is Glauber's Eq. (9) convention with `gamma=theta`. The conditional-
expectation operators are orthogonal projections in `L^2(pi)`, so their sum is
self-adjoint. Strictly positive conditional probabilities at finite `b` make
the finite chain irreducible.

Under common clocks and uniforms, the new disagreement probability at site
`i` is the total-variation distance between two Bernoulli conditional laws:

```
|p_i(sigma)-p_i(eta)|
 <= (theta/2)(D_{i-1}+D_{i+1}).
```

Summing the exact loss `-a D_i` and the two possible neighbour contributions
gives

```
L D <= -a(1-theta)D.
```

The finite-state Dynkin/Gronwall step therefore yields contraction at
`r=a(1-theta)` with no size-dependent prefactor in the Lipschitz seminorm.
For a nonconstant real eigenfunction `f` of `-Q` with eigenvalue `lambda`,
`Lip(P_t f)=exp(-lambda t)Lip(f)`. Since its seminorm is positive, contraction
implies `lambda>=r`. Reversibility supplies a real eigenbasis, so this controls
every centered mode. This eigenfunction step is what upgrades coupling from a
mixing estimate to the claimed spectral lower bound.

For `M=sum_i sigma_i`, summing

```
Q sigma_i=-a sigma_i+(a theta/2)(sigma_{i-1}+sigma_{i+1})
```

gives `QM=-a(1-theta)M`. Spin-flip symmetry centers `M`, and full support makes
it nonzero. It is therefore a matching eigenmode. The restriction `N>=3`
ensures the two cyclic neighbours are the intended distinct sites and avoids
the two-site periodic-edge convention.

The susceptibility statement follows because `V=uM/N` is the slow eigenmode:
`<V,(-Q)^{-1}V>=Var(V)/gap`. It does not require a uniform positive lower bound
on `Var(V)`. The limiting examples are also correct:
`b_N=(log N)/4` gives `theta=(N-1)/(N+1)` and gap `2a/(N+1)`, while replacing
`Q` by `Q/N` divides every eigenvalue by `N`. These show why bounded coupling
and a per-site clock floor, rather than finite range alone, are the retained
premises.

## Source match and limits

Glauber printed pp. 295--300 supplies the clock/rate normalization, detailed-
balance identification `gamma=tanh(2J/kT)`, finite-ring one-spin Fourier modes
and total-magnetization decay. Bubley--Dyer pp. 223--225 supplies the Hamming
path and maximal-coupling construction. Neither selected passage states the
full `2^N`-state spectral equality. The project proof above supplies that step.

The Glauber reading was text passage reading from a public third-party indexed
scan/transcription. The publisher PDF returned HTTP 403 and no original image
was read. Equations (9), (17), (30), and (44)--(51) therefore retain an explicit
formula-image verification requirement for the coordinator. The Bubley--Dyer
PDF was cached and its selected proof passage inspected. Full source details,
hashes, routes and the eight-page/four-search boundary are in the companion.

Proof status proposed to coordinator: **written proof reviewed**. Literature
status proposed: **established model and coupling ingredients; derived exact
full-gap consequence under bounded coverage; no novelty claim**.

## Coordinator acceptance, 2026-09-13

C124 is accepted on its self-contained written proof. The coordinator checked
all conditional probabilities, the N=3 distinct-neighbour convention, the
full-space eigenfunction implication, susceptibility normalization and both
closing limits. No imported literature theorem is needed for mathematical
acceptance. Source transcription acceptance is separate: Glauber's unavailable
formula images are not promoted as visually verified formulas.

Coordinator reread the indexed passages around (17), (30), (44)--(51), checked
the three cache hashes, and visually inspected Bubley--Dyer printed pp. 224--225,
including Theorem 1's maximal-coupling and Hamming-contraction proof. The theorem
is discrete-time and its diameter factor is a mixing bound, not the project's
spectral argument. One additional coordinator discovery query for a Glauber
PDF found no usable original; the audit stopped without a wider source sweep.
The worker's budget remains two sources/eight pages/four searches; the combined
search count is five. Requested worker model/effort was Sol medium; its initial
handoff incorrectly described the request as inherited GPT-6 and is corrected
against the dispatch record. Effective runtime metadata was not verified.
