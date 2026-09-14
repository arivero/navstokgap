# Product probabilities restrict reversible generators

The first technical step of de la Torre et al.'s Theorem 1 is valid:
two-sided reversible evolution and product-test positivity force every local
matrix slice of its generator to have a scalar diagonal, symmetric time-space
entries and an antisymmetric spatial off-diagonal part. Thus the generator
belongs to the tensor power of a seven-dimensional matrix space. This is an
expanded proof of an established source step, not a new reconstruction result.

C129, Q01 acceptance audit, 2026-09-14. [B77 review](../reviews/reversible-generator-B77.md). Source: [B70 original](../docs/batches/B70/de-la-Torre-Masanes-Short-Mueller-2011.pdf),
PDF pp. 3–4, equations (4), (6), (8)–(14). The written argument below fixes an
explicit row/column convention and retains the Taylor remainder.

## Object and assumptions

Fix a finite number n of local three-dimensional unit balls. Put u(a)=(1,a)
and v(a_1,...,a_n)=u(a_1) tensor ... tensor u(a_n) in R^(4^n).
A product preparation has coordinate v(a), and a product effect has coordinate
2^(-n)v(b). All unit Bloch vectors in each factor are available independently.
The coordinates and probabilities are dimensionless; no volume or continuum
limit is taken.

Let X be a real 4^n by 4^n matrix such that exp(tX) is an allowed reversible
transformation for every t in a two-sided neighbourhood of zero. Assume

$$p_{b,a}(t)=2^{-n}v(b)^T e^{tX}v(a)\in[0,1].$$

These assumptions follow for a one-parameter subgroup of the source's matrix
Lie group. We need only these local one-parameter curves, not a claim that
every element of an arbitrary connected group is a single exponential.
If t is assigned physical time, X has inverse-time units; the argument itself
makes no physical clock or energy/action identification.

## Boundary derivatives, with the remainder retained

The matrix exponential gives the exact expansion

$$p(t)=p(0)+2^{-n}t\,v(b)^TXv(a)
       +2^{-n}\frac{t^2}{2}v(b)^TX^2v(a)+O(t^3).$$

Take unit vectors and b_1=-a_1, leaving the remaining b_k and a_k independent.
Since u(-a_1)^T u(a_1)=0, p(0)=0. A differentiable nonnegative function on a
two-sided neighbourhood has p'(0)=0 and p''(0)>=0. Therefore

$$v(-a_1,b_2,\ldots,b_n)^TXv(a_1,\ldots,a_n)=0,$$
$$v(-a_1,b_2,\ldots,b_n)^TX^2v(a_1,\ldots,a_n)\geq0.$$

With b_k=a_k for every k, p(0)=2^(-n) product_k(1+|a_k|^2)=1.
The maximum instead gives p'(0)=0 and

$$v(a)^TX^2v(a)\leq0.$$

These are source equations (10)–(12). Equation (9) is used as an asymptotic
expansion, not an exact interval bound on a truncated polynomial. The sign of
the second derivative is necessary even when it vanishes; it is not a sufficient
criterion for positivity at finite t. For a forward semigroup alone a boundary
minimum gives only a one-sided first-derivative inequality, so this inference
specifically uses reversibility.

## From the vanishing derivative to local matrix blocks

Use row = output and column = input. Fix all spectator output and input
indices. The first-order identity implies, for the resulting 4 by 4 slice M,

$$u(-a)^T M u(a)=0\qquad (|a|=1).$$

To justify fixing these indices, u(e_i)+u(-e_i)=2e_0 and
u(e_i)-u(-e_i)=2e_i show that unit-vector preparations span R^4. Their tensor
products span the spectator space, independently for input and output. The
bilinear identity therefore vanishes coefficient by coefficient. This is a
linear-span argument; the signed combinations need not be physical states.

Write

$$M=\begin{pmatrix}c&r^T\\s&D\end{pmatrix}.$$

Then the identity becomes c+(r-s) dot a-a^T D a=0. Subtraction at a and -a
gives r=s. Evaluation at each e_i gives D_ii=c. Evaluation at
(e_i+e_j)/sqrt(2), i unequal j, gives D_ij+D_ji=0. Consequently

$$M=cI_4+\begin{pmatrix}0&r^T\\r&K\end{pmatrix},
\qquad K^T=-K.$$

Conversely every such block satisfies the identity. These are exactly the
entry constraints (13)–(14), independent of the source's index-placement
convention. With A the three-dimensional space having only an antisymmetric
spatial block, B the three-dimensional space with equal time-space blocks,
and I the span of I_4, the slice belongs to L=A direct-sum B direct-sum I.
Its dimension is 3+3+1=7. Source equation (6) supplies a basis of A and B.

The same proof works at every site because an orthogonal input/effect pair
can be chosen in any factor. In End(R^4)^(tensor n), the constraints for site k
put X in End(R^4)^(tensor(k-1)) tensor L tensor
End(R^4)^(tensor(n-k)). Choose any vector-space complement of L and expand
in a basis adapted to L plus that complement. Intersecting these n conditions
removes every tensor coefficient with a complement factor. Hence

$$X\in L^{\otimes n}=(\mathcal A\oplus\mathcal B\oplus\mathcal I)^{\otimes n}.$$

This completes the selected step. L^(tensor n) is a necessary ambient linear
space, not by itself the Lie algebra of an admissible group. In particular the
second-order conditions, normalization and further group constraints still
restrict which elements are actual generators.

## Dependencies and strategic consequence

The proof imports finite-dimensional matrix exponentiation, the elementary
calculus test at an interior extremum, spanning by product tensors, and a
basis/complement intersection argument. Local SO(3) containment, compact-group
averaging, entangling-gate universality, identical-copy extension and
ancilla/discard closure are not needed for this step. Later portions of the
source theorem use additional assumptions and arguments.

Accept equations (10)–(14) and their tensor-space consequence under the stated
hypotheses. The next named proof dependency is whether local-rotation averaging
isolates a nonzero generator as claimed in equations (15)–(17). It remains
supporting until STATE selects it. The minimal-composite exclusion still relies
on the rest of Theorem 1; neither its full proof nor the physical origin of
reversible descent or a positive universal action constant is established here.
