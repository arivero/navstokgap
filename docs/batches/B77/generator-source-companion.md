# B77 — infinitesimal product-probability constraints

## Finding

De la Torre, Masanes, Short and Müller, *Deriving quantum theory from its local
structure and reversibility*, arXiv:1110.5482v1 [quant-ph], 25 October 2011,
supports the selected generator restriction. In the Bloch representation,
equations (8)–(12) turn valid product-test probabilities along a reversible
one-parameter group into boundary derivative constraints. Equations (13)–(14)
and the following paragraph restrict the Lie algebra to
\((\mathcal A\oplus\mathcal B\oplus\mathcal I)^{\otimes n}\), where each
local factor is seven-dimensional.

## Source route and coverage

Primary source: [archived B70 PDF](../B70/de-la-Torre-Masanes-Short-Mueller-2011.pdf),
SHA-256 `614d4e3910d7bc2483220a01ab561b175451d051de575ab2d8bbc9b896d5ec8f`.
The file identifies itself as arXiv:1110.5482v1. Evidence level:
**proof-audited** for printed pp. 3–4, equations (4), (6), (8)–(14), and the
tensor-space sentence immediately following (14); **passage** for printed
pp. 1–2 setup defining local tomography, the connected reversible group, and
Theorem 1's product-probability condition. No discovery query or additional
paper was used.

Text extraction was checked against rendered images of printed pp. 3–4.
Equation (13)'s index placement is visually dense, but its two equalities and
equation (14)'s antisymmetry agree with the source. The source's equation (9)
prints a second-order truncation as though it remained in the probability
interval and does not display a remainder; the review supplies the rigorous
derivative reading. Printed p. 4 was used only for the continuation of the
post-(14) sentence and its seven-element orthogonal basis, not for equations
(15) onward.

## Claim-to-source map

| Claim | Source anchor | Status |
| --- | --- | --- |
| Product preparations and product effects have the coordinates used in the probability pairing | p. 3, equation (4) and effect paragraph | Exact match |
| Every allowed reversible transformation preserves those product probabilities in \([0,1]\) | p. 2, Theorem 1 condition 2; p. 3, equation (8) | Exact match |
| Zero/unit boundary probabilities give equations (10)–(12) | p. 3, equations (9)–(12) | Accepted with explicit Taylor remainder |
| Each local slice lies in \(\mathcal A\oplus\mathcal B\oplus\mathcal I\) | p. 3, equations (6), (13)–(14) | Exact match; expanded project proof |
| Applying the slice restriction at every site gives the tensor-power ambient space | pp. 3–4, sentence following (14) | Exact conclusion; expanded project intersection proof |

## Scope

This batch audits only the initial generator restriction in Theorem 1. It does
not audit equations (15)–(23), compact-group projectors, coefficient
elimination, the theorem's final alternatives, or Theorem 2. The source result
is a necessary restriction under a supplied reversible operational group. It
does not identify a physical interaction mechanism, time calibration, energy
gap, or action constant.

Source-to-model suggestion: in C125, require an admissible two-sided nonlocal
one-parameter group preserving every product-state/product-effect probability;
then use this audited tangent-space restriction as the first necessary test.
Whether such a group is physically available remains the substantive premise.
