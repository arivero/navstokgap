# G01/B20 proof and source review

C041–C042 are accepted as standard spectral consequences in an explicit
finite-state model. The lower gap estimate requires observable coverage
together with bounded susceptibility. The source and prior-art scope are in
[B20](../references/batches/B20.md).

## Proof review

All inverse operators act on the centered $L^2(\pi)$ space. Detailed balance
supplies self-adjointness in that weighted inner product. The product formula
has the correct upper-bound direction for the full gap; equality holds in the
one-dimensional centered two-state model. The hidden-label construction is
irreducible for every positive label rate and loses irreducibility only at
the endpoint of the family.

For the frame result, expand each observable in a full orthonormal eigenbasis.
The slowest mode alone contributes at least $\alpha/\gamma_1$ to total
susceptibility, giving $\gamma_1\ge\alpha/S$. No commutation of the frame
operator with the generator is assumed. Complete coverage requires enough
observables, and its lower frame constant and total response must be uniform
for a uniform family estimate. If masses vary, retain the factor $2m$ in
converting between action and susceptibility.

The action unit multiplying $-Q$ is an input. Its two-state numerical equality
to Dirac branch separation identifies units, while preserving the distinct
operator and state-space definitions. The physical versus algorithmic time
distinction remains explicit for field-theory transfer.

## Source and checks

Coordinator read Pavliotis pp. 4–5 and checked p. 5 visually, including
(2.3)–(2.8), against the existing hash-identified cache. The worker requested
gpt-5.6-luna low; its actual configuration was not independently reported.
No parallel agent or descendant was used. Sokal remains a discovery-only lead.

`scripts/susceptibility_gap_checks.py` passes 11 exact identities, five rational
gap-bound cases, and four nonuniform-stationary-law checks. The latter test
weighted reversibility, centering, the centered Poisson solution and positivity.
The written eigenbasis argument proves the general statements.
