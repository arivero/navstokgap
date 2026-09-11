# B50 source companion: full pointer recovery

## Result and bounded coverage

The bounded audit finds a standard ODE precedent for the smoothness premise in
R19, but no exact literature match for its eight-record Hamiltonian pointer map.
Sideris establishes finite-time `C^1` dependence of an ODE solution on initial
data, through the variational equation, and gives parameter-dependence results
under a common existence interval. This supports the written `C^1` estimate
for the coupled apparatus on a compact domain. It does not establish the
model's leading map `(-A_c z,q)`, its uniform singular-value margin, or global
injectivity.

## Primary source and exact reading

Thomas C. Sideris, *Ordinary Differential Equations and Dynamical Systems*,
Atlantis Studies in Differential Equations 2 (2013), DOI
10.2991/978-94-6239-021-8. Author-hosted PDF:
https://web.math.ucsb.edu/~sideris/pdffiles/BookPublishedComplete.pdf.

Read the Chapter 6 passage “Dependence on Initial Conditions and Parameters”:
Theorem 6.1 and its variational-equation statement, printed pp. 89–90 (PDF
pp. 96–97), plus the parameter regularity passage at printed pp. 92–93 (PDF
pp. 99–100). The theorem’s hypotheses concern a sufficiently smooth vector
field and a common local solution domain; the conclusion is smooth dependence
of the solution on initial data, with derivatives governed by the linearized
equation. The parameter results extend this to finite parameters when the
corresponding common existence hypotheses hold. Evidence level: passage.
The PDF was used for the named pages only; no full-read claim is made.

## Claim-by-claim audit

**C094 (uniform global inverse):** No exact established match found in the one-
query/one-source budget. The standard source supplies the differentiability
needed to form `D F` and bound the finite-time flow perturbation. R19’s global
lower-Lipschitz estimate follows from its own hypotheses: a convex domain,
`F=L+R`, an invertible block map `L=(-A_c z,q)` with a uniform `alpha>0`, and
`||R||_{C^1} <= C lambda` uniformly over clock and probe boxes. The segment
integration argument then gives injectivity for sufficiently small lambda.
This is a model-derived global perturbation result, not a theorem attributed
to Sideris. It requires the domain to remain inside the strict cutoff and
existence margins; pointwise rank alone would not suffice.

**C095 (reconstruction product closure):** No exact established match found.
Given C094, the minimum-residual estimator has joint error bounded by a
constant times `max(rho_pi/lambda,rho_q)`. Equation (3) and its action-unit
normalization are therefore a derived consequence of the record model and
the inverse estimate. The product tends to zero only along the stated record
precision limit at fixed positive coupling (or a joint limit with
`rho_pi/lambda -> 0` and `rho_q -> 0`); it is not a preparation-independent
positive-action theorem. Exact initial clock data and final joint position /
momentum access remain explicit resources.

## Query and stopping point

One query was used on 2026-09-11: `Sideris Ordinary Differential Equations and
Dynamical Systems chapter 6 smooth dependence solutions PDF`. It located the
author-hosted primary PDF. One primary source and the four selected printed
pages listed above were inspected. Search results were discovery leads; the
substantive evidence is the named source passage. No exhaustive prior-art or
novelty conclusion is claimed, and no numerical or symbolic verification was
performed.

## Source-to-model suggestion for R20

Keep the eight final pointer records and known incoming probe momenta, but hide
the initial clock position and momentum. Use the same variational-flow route
to test whether clock perturbations lie in the image of receiver and unknown
probe-position derivatives while preserving the energy shell and fixed box
margins. An explicit common-record fibre or a uniform inverse estimate is the
next decisive proof obligation; dimension counting alone is insufficient.

## Coordinator verification

Rechecked author/title/year/DOI in the primary PDF metadata pages, Theorem 6.1
and its variational equation at printed pp. 89–90, and Corollary 6.1 plus the
parameter theorem/corollary at pp. 92–93 in extracted text. Visually checked
p. 92, including the smoothness corollary and Theorem 6.2 start. The latter
assumes local Lipschitz dependence in state and parameter; Corollary 6.3 gives
Ck dependence under Ck hypotheses. R19 has smooth vector fields and separately
establishes its uniform compact interval and cutoff margins. No additional
search was used. This is a premise audit, not a broad exact-result search.
