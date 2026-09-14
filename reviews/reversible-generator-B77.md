# B77 review: the local generator restriction is accepted with two clarifications

The inference from product-probability positivity to
\(\mathfrak h\subseteq(\mathcal A\oplus\mathcal B\oplus\mathcal I)^{\otimes n}\)
is correct. The expanded argument in
`notes/reversible-generator-constraints.md` supplies the two details compressed
in de la Torre et al., equations (8)–(14): it retains the Taylor remainder and
proves the tensor-space intersection by an explicit slice and complement
argument. The result is an established step from the cited proof, with project
exposition filling those details.

## Source and exact matches

I proof-audited de la Torre, Masanes, Short and Müller, *Deriving quantum
theory from its local structure and reversibility*, arXiv:1110.5482v1, PDF
pp. 3–4. Setup on pp. 1–2 was read only where needed to identify the group and
probability assumptions. The archived PDF was also rendered, and equations
(4), (6), and (8)–(14) were checked visually on printed p. 3.

- Equation (4) gives the product-state coordinates
  \(v(a_1,\ldots,a_n)=(1,a_1)\otimes\cdots\otimes(1,a_n)\).
- The preceding effect paragraph gives every product effect used in (8) as
  \(2^{-n}v(b_1,\ldots,b_n)\). Equation (8) is therefore exactly the assumed
  probability bound.
- Equations (10)–(12) are the first- and second-derivative necessary conditions
  at the zero- and unit-probability boundary points. The note reproduces their
  signs and choices of product vectors correctly.
- Equations (13)–(14) impose equal time-space entries, a scalar diagonal, and
  antisymmetric off-diagonal spatial entries on every local matrix slice.
  Equation (6) identifies these respectively with the \(\mathcal B\),
  \(\mathcal I\), and \(\mathcal A\) directions.
- The paragraph following (14), continuing onto p. 4 only to finish the
  sentence and list the orthogonal basis, states the same tensor-space
  restriction and seven-element basis used in the note.

## Proof check and imported assumptions

For \(X\in\mathfrak h\), the exact curve \(e^{tX}\) lies in the matrix Lie
group for positive and negative sufficiently small \(t\). Thus its exact
product probabilities remain in \([0,1]\). At an initial probability zero or
one, elementary two-sided calculus gives a zero first derivative and the
respective sign of the second derivative. This validates (10)–(12), provided
the displayed polynomial in source equation (9) is understood as a
second-order Taylor expansion rather than an exact interval-bounded expression.

For one chosen tensor factor, the other product vectors span their spectator
spaces. Fixing their coefficients reduces (10) to
\(u(-a)^TMu(a)=0\) for every unit \(a\). Writing
\(M=\left(\begin{smallmatrix}c&r^T\\s&D\end{smallmatrix}\right)\), comparison
at \(a\), \(-a\), the coordinate vectors, and their normalized pairwise sums
gives \(r=s\), \(D_{ii}=c\), and \(D_{ij}=-D_{ji}\). Hence the local slice is
in the seven-dimensional direct sum. Repeating the condition in every factor
and expanding in a basis adapted to this direct sum proves the tensor-power
restriction. No positivity of signed spanning combinations is assumed; they
are used only after the physical probability identity has supplied a bilinear
polynomial identity.

The step imports finite-dimensional local tomography, availability of all
local Bloch-ball preparations and product effects, linear matrix
transformations, a two-sided one-parameter reversible group, and elementary
linear algebra and calculus. It does not use local-rotation averaging,
coefficient elimination, entangling-gate universality, identical-copy closure,
or ancilla preparation and discard.

## Required clarifications and decision

Accept the mathematical step with these two wording constraints:

1. Source equation (9) suppresses the Taylor remainder. The rigorous argument
   applies the boundary derivative test to the exact probability curve and
   then reads off its derivatives; it must not assert that the truncated
   quadratic itself stays in the probability interval.
2. Connectedness alone does not warrant the source sentence that every group
   element is one exponential. This selected inference only requires the
   standard Lie-algebra fact that \(e^{tX}\) is in the group for
   \(X\in\mathfrak h\), which is sufficient for (8)–(14).

The result supplies a necessary ambient space for admissible generators. It
does not show that every element of that space is admissible, and it does not
complete Theorem 1 or independently exclude C125's minimal composite. The
remaining Q01 dependency is the later reduction from a nonlocal generator to
the entangling-unitary or partial-transpose alternatives.

Source-to-model suggestion: formulate the added Q01 premise directly as a
two-sided admissible one-parameter nonlocal transformation preserving all
C125 product preparation/effect probabilities. Its tangent must then lie in
the audited seven-dimensional tensor space, giving an exact first filter before
any appeal to the later averaging argument. This premise supplies no physical
clock, action normalization, or positive universal action scale.
