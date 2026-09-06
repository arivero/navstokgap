# R01: independent mathematical review

Date: 2026-09-05. Role: bounded independent mathematical reviewer. This is an
internal proof audit, not external peer review or a formal proof certificate.

Reviewed manuscript: `papers/action-gap-foundations.tex`, all 297 lines, starting
SHA-256 `b9b9f4a34eb30794eda005ec97ea360caffea667a46f8d223377709fb592c158`.
The manuscript was an uncommitted new file above repository base
`2cb1554f71ac5073a113802dd9ccd5daedb5cadf`; the hash identifies the reviewed text.
Section and LaTeX labels below are the durable anchors; line numbers describe
this snapshot.

## Verdict and findings by severity

No blocking or medium-severity mathematical defect was found. All three displayed
propositions were audited, including their hypotheses and endpoint cases, together
with the unnumbered Hessian, kernel and relativistic calculations. Their stated
conclusions follow in the specified models. Acceptance as elementary control
results is warranted; this does not establish a quantum reconstruction, an
intrinsic action gap or a physical implementation of the two-arm comparison.

Two low-severity scope clarifications would make later reuse safer. Neither
invalidates a displayed proposition.

1. **Endpoint-term invariance uses an ordinary point-function gauge term.**
   Section 2, immediately after `eq:area` (lines 89–90), should specify an added
   term `dG(q,t)/dt`, with the same single-valued sufficiently regular `G` on both
   paths. Matching positions and times then cancel the endpoint contribution.
   An unrestricted reading that permits `G(q,dot q,t)` would be false: adding
   `d(kappa dot y)/dt` changes the chord-minus-classical difference by
   `-kappa F T/m`, since the chord has equal initial/final vertical velocities
   while the classical velocity gain is `F T/m`. That extension introduces a
   higher-derivative Lagrangian and is outside the ordinary model already used in
   the paper. This is therefore an explicit-assumption improvement, not a
   counterexample within its natural point-mechanics convention.

2. **Scalar-parameter locality is weaker than locality in a path topology.**
   Proposition 2, `prop:local` (lines 107–118), is correct exactly as written:
   small parameter values give small nonzero action differences. Its hypotheses
   alone do not imply `q_a -> q_0` in a topology on paths, since only `S[q_a]` is
   required to be smooth. If it is later cited to assert arbitrarily close
   *paths*, add that continuity assumption. An abstract diagnostic is
   `P = {0} union (1/2,3/2)`, with its subspace topology,
   `S(0)=0`, `S(x)=(x-1)^2` on the other component, `q_0=0`, and
   `q_a=1+a` for `0<|a|<1/2`. Then `S[q_a]=a^2` including at zero, but `q_0`
   is isolated and `q_a` does not approach it. This does not refute the actual
   action-value conclusion. Ledger C003 already includes a continuous variation
   direction, so retaining that premise resolves the locality issue.

## Proof coverage and adversarial checks

| Anchor | Audit result and material assumptions |
| --- | --- |
| Section 1, definition of `g_S` | The reference action, nonempty set of nonzero differences, endpoints, duration and path class are distinguished from an operator spectral gap. A positive spectral interval alone would require the stated ground-sector interpretation. |
| Section 2, `eq:quadratic` | For real `eta in H^1_0(0,T)`, the kinetic cross term is `m integral dot y_* dot eta = -F integral eta`; the weak integration by parts is valid since `y_*` is smooth and the traces vanish. The linear potential contribution cancels it. The remaining coefficient is `m/2`, not `m`. |
| Section 2, `eq:area` | The chord variation is `F t(T-t)/(2m)`. Integration gives `F^2 T^3/(24m)`, equal to both `F A_lens/(2v_0)` and `T delta E/12`. Here `delta E` is deterministic kinetic-energy gain; total mechanical energy remains constant. |
| Proposition 1, `prop:no-gap` | Correct for `m,T>0` and fixed horizontal motion. Zero weak derivative plus zero traces gives the zero Sobolev class, establishing uniqueness. The nonzero family `a t(T-t)` converges to zero even in `H^1`, with action excess `m a^2 T^3/6`. These are admissible off-shell paths, not different solutions of the same initial-value problem. |
| Proposition 2, `prop:local` | The `C^2` scalar assumption and nonzero second derivative give the stated Taylor remainder bounds and the sign of `b`. For `b<0`, the absolute-value conclusion remains valid; positive signed differences need not follow. No conclusion for a direction with `b=0` is claimed. See the locality qualification above. |
| Section 3, second variation and Jacobi equation | The second variation is `Q`, whereas the constant-force action excess is `Q/2`. Linearizing `m ddot q + V'(q)=0` gives `J eta=0`. An arbitrary endpoint-preserving path variation need not solve it. With real bounded potential coefficient the stated Dirichlet operator domain is the usual self-adjoint realization in `L^2`. |
| Section 3, constant-force spectrum | The complete sine basis gives `lambda_n=m(n pi/T)^2`. The Rayleigh lower bound is sharp, attained on the first sine mode. Scaling that mode by any small nonzero amplitude preserves the spectral bound while making `Q` arbitrarily small. The reported eigenvalue and norm units multiply to action. |
| Section 3, oscillator comparison | For positive frequency `omega`, `J sin(n pi t/T)=m[(n pi/T)^2-omega^2] sin(n pi t/T)`. At `T=pi/omega` the first eigenvalue is already zero; beyond it a negative mode exists. Later conjugate times add zero modes without restoring positive definiteness. This is a Hessian result, not an energy-spectrum calculation. |
| Section 4, `eq:kernel` and its expansion | With the given Fourier convention and inverse factor `1/(2 pi)`, the multiplier tends to one, hence the kernel tends to `delta`. The Fourier transform of `delta''` is `-k^2`, so the displayed `+ i hbar tau/(2m)` coefficient is correct. The bound is for each fixed Schwartz test function at fixed positive `m,hbar`; it is not a pointwise kernel limit. |
| Proposition 3, `prop:measurement`, `eq:success`, `eq:threshold` | The pure-state density difference has rank at most two. Its zero trace and squared trace yield the stated trace-distance formula; the positive spectral projection achieves the optimum. At coincident states it is simply zero. Tensor-product overlap gives the exponent `2N`, where `N` is a positive integer copy count. Solving the monotone first lobe yields exactly the stated threshold. |
| Section 5, endpoints and large-copy limit | For `phi=0` and `phi=2 pi n`, success is `1/2`; at `|phi|=pi` it is one. For finite `N`, `p=1` requires orthogonality and gives `pi hbar`. For fixed `1/2<p<1`, expanding the power and arccosine gives `2 hbar sqrt(-log(4p(1-p))/N)`. The perfect-discrimination endpoint must not be obtained by substituting into this fixed-interior-`p` asymptotic. |
| Section 5, projectile-time substitution | The lower duration threshold follows by cubing the positive chord-action expression. The upper first-lobe duration remains necessary, and at `p=1` the admissible first-lobe duration is a single value. Control and recombination phases and physical realization are explicitly assumed. |
| Section 6, finite-`c` control | The maximum speed is `|a|T`. For a fixed strict margin, the square-root expansion is uniform in time. The integrand is nonnegative and positive almost everywhere for nonzero `a`; the quadratic excess is correct. Its next coefficient is `m T^5 a^4/(40 c^2)`. Thus finite `c` by itself cannot provide a universal positive action-value gap. |
| Section 6, field-theory comparison | The manuscript makes no transfer theorem. It correctly withholds Navier–Stokes regularity and Yang–Mills conclusions and calls for the missing operators, spaces and limits. |

For the kernel remainder, putting `alpha=hbar/(2m)` makes the actual estimate
explicit for a test function `varphi`:

```text
|<K_tau - delta - i alpha tau delta'', varphi>|
  <= alpha^2 tau^2/(4 pi) integral k^4 |hat varphi(-k)| dk.
```

The right side is finite for Schwartz functions. Evenness also excludes an odd
first derivative contribution. Differentiating the whole kernel is a different
operation and converges to `delta'` by continuity of differentiation on tempered
distributions, as the manuscript says.

## Verification and limits

The review rederived the displayed proofs on their stated domains. A separate
read-only SymPy calculation confirmed the polynomial action integral, chord
coefficient, relativistic quartic coefficient, the explicit two-by-two density
matrix identity `tr(D^2)=2 sin(phi/2)^2`, and the example
`d_(1,3/4)/hbar=pi/3`. These checks support, rather than replace, the arguments.
The coordinator owns the repository-wide checks and PDF build; this reviewer did
not run them or modify their inputs.

No external browsing was needed for these elementary proofs. Historical source
passages, bibliography completeness, experimental feasibility, general
infinite-dimensional path integrals, singular-force existence, full quantum
reconstruction and field-theory transfer are outside this audit. The routed
constant-force note was read for definitions and context; this is not an
independent historical-source or uncertainty-relation audit. Future changes to
the model, admissible paths, resource protocol or limiting parameters require a
new review.
