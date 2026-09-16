# What would unblock the confinement-scale region, and what was checked and fails

The map of [the position note](mass-gap-position.md) leaves one region
untouched by every tool with explicit constants: the confinement scale,
where the effective coupling is of order one and the effective theory
must be shown to be mixing uniformly in the volume. This note records
the outcome of a review of every rigorous technique known to the author
that might enter that region by written derivation, so that later
sessions do not re-derive the same dead ends. The conclusion is that
exactly two things would unblock it, and neither is available here:

1. **A correlation inequality for $SU(3)$ lattice gauge theory** of
   Griffiths--Ginibre type, giving monotonicity in the coupling of the
   quantities that control mixing. This is what makes the Ising model's
   intermediate regime accessible and what the abelian gauge theories
   have; for $SU(N)$ none of this type is known, Section 1 says where the
   standard constructions break, and the centre-based comparison
   inequalities that do exist concern the string tension rather than
   the vacuum-sector gap.
2. **A computer-assisted verification of the Dobrushin--Shlosman block
   criterion** for the Wilson interaction, or for the effective
   interaction at the confinement scale, as specified in
   [the Dobrushin note](dobrushin-uniqueness-wilson.md) §4. This is
   numerics of a size beyond present practice and outside this
   repository's rules.

Everything else checked reduces to one of these or fails for a stated
reason. References at metadata level; nothing promoted.

## 1. Correlation inequalities: where they break for $SU(N)$

*Ising and abelian gauge theories.* Griffiths' inequalities in
Ginibre's general form (Commun. Math. Phys. 16 (1970) 310) need a cone
of functions on the single-site space, closed under products, such that
the duplicate-variables integral
$\int\!\!\int\prod_i\big(f_i(x)-f_i(y)\big)\,d\nu(x)\,d\nu(y)\ge0$ holds.
For $\pm1$ spins and for $U(1)$ with the cosines this holds, so the
Wilson loops of $U(1)$ lattice gauge theory are monotone in $\beta_W$
and the phase structure can be squeezed from both sides; the sharpness
theorem of Aizenman, Barsky and Fernández (J. Stat. Phys. 47 (1987)
343) is the deepest form of this control for Ising-type models. The
Coulomb phase of $U(1)$ (Guth; Fröhlich--Spencer) uses the dual
representation, whose weights are positive.

*Non-abelian.* Three obstructions, each sufficient on its own.

- The dual representation has signs. Integrating the links of a
  character expansion produces recoupling coefficients, which are not
  nonnegative for $SU(2)$ and $SU(3)$, so the surface gas is not a
  positive measure and no monotonicity in $\beta_W$ follows from it.
  The plaquette coefficients themselves are nonnegative
  ([Wilson note](wilson-strong-coupling-explicit.md) §1), which is why
  the strong-coupling expansion is a positive gas; the signs appear at
  the vertices where more than two surfaces meet.
- The $O(N)$ analogy fails already at $N=4$. $SU(2)\simeq S^3$, and
  $\tfrac12\operatorname{tr}(UV^\dagger)$ is the Euclidean inner product
  of unit quaternions, so the plaquette term is a degree-four
  polynomial in four $O(4)$ spins; Ginibre's construction covers $O(2)$
  and specific $O(N)$ interactions but not this one, and $SU(3)$ has no
  such real form at all.
- The interaction is not ferromagnetic in any sign sense: for a complex
  defining representation $\operatorname{Re}\operatorname{tr}U_p$ is not
  a product of functions on the links with definite sign properties.

*What does exist for non-abelian groups, and why it does not reach.*
Comparison inequalities built on the centre are known and rigorous.
Mack and Petkova (Ann. Phys. 123 (1979) 442; 125 (1980) 117) bound the
$SU(2)$ Wilson loop by a $\mathbb Z_2$ gauge theory's through the
decomposition $SU(2)\to\mathbb Z_2\times SU(2)/\mathbb Z_2$, so
confinement in $SU(2)$ follows wherever the $\mathbb Z_2$ theory
confines; the four-dimensional $\mathbb Z_2$ theory deconfines at weak
coupling, being dual to the Ising model, so the comparison reaches only
strong coupling, and the same holds for $SU(3)$ against $\mathbb Z_3$.
Tomboulis and Yaffe (Commun. Math. Phys. 100 (1985) 313) derive exact
inequalities between electric-flux and vortex free energies from
reflection positivity and the $\mathbb Z_N$ Fourier structure, and use
them to prove deconfinement at high temperature. A claimed proof of
confinement for all couplings in $SU(2)$ by these methods with
approximate decimations (Tomboulis, arXiv:0707.2179) has not been
established as a theorem in the literature as far as this author knows.
All of these concern the string tension, that is, the energy of the
electric-flux sectors, which on a torus is the $27$-sector structure of
[the SU(3) constants](su3-constants.md) §4 and which disappears in
infinite volume. The Jaffe--Witten gap is the vacuum-sector gap, the
glueball mass, and no rigorous inequality relates it to the string
tension in either direction. So the centre-based inequalities are real,
non-abelian, and aimed at a different quantity, and their comparison
theory has a transition of its own.

## 2. Reflection-positivity tools

*Chessboard estimates* (Fröhlich, Israel, Lieb and Simon, Commun. Math.
Phys. 62 (1978) 1) hold for the Wilson measure and bound the probability
of a local event by a free-energy difference per block, uniformly in
the volume and at every coupling. They give rigorous large-deviation
bounds for bad blocks without an expansion. They do not give mixing on
the good blocks, so they are an ingredient of a verification and not a
substitute for it.

*Infrared bounds* (Fröhlich, Simon and Spencer, Commun. Math. Phys. 50
(1976) 79) need Gaussian domination, $Z(h)\le Z(0)$ for shifts $h$ of
the field, which uses the translation structure of a flat target space
or of $U(1)$; on a non-abelian group manifold the shift is not a
symmetry and the domination fails. This is consistent with confinement:
an infrared bound would prove a massless phase.

*Reflection positivity proves transitions* (Peierls-type arguments via
chessboard) and, through the transfer matrix, converts decay into a gap
([Dobrushin note](dobrushin-uniqueness-wilson.md) §3). It does not
prove the absence of a transition.

## 3. Hamiltonian finite-size criteria

Knabe's criterion (J. Stat. Phys. 52 (1988) 627) and its descendants
bound the gap of an infinite frustration-free Hamiltonian by the gap on
finite blocks. The Kogut--Susskind Hamiltonian is not frustration-free:
its ground state is not a ground state of the electric and magnetic
terms separately, and no equivalent frustration-free form with the same
gap is known. Ground-state clustering also does not imply a gap for a
general Hamiltonian, while Euclidean decay in time does, through the
positive transfer matrix; this is why the decay-to-gap step in this
programme is always taken on the Euclidean side.

## 4. Exact transformations

*Flow conjugation* is exact and preserves the spectrum at the same
coupling ([flow-conjugation note](flow-conjugation-truncation.md)).
*Electric--magnetic duality* is exact for abelian groups and maps
strong to weak coupling; for $SU(N)$ the dual is the signed surface gas
of Section 1. *Gauge fixing* changes the specification, so the
Dobrushin coefficient can be reduced by removing fixed links from the
neighbour count, by at most the fraction of links on a maximal tree,
about one quarter in four dimensions; this moves $444$ to about $330$
and touches nothing else.

## 5. Other constructions

*Large $N$* has $1/N$ as a small parameter; the goal is $SU(3)$.
*Stochastic quantization* (the Langevin dynamics of the gauge field)
constructs the two- and three-dimensional theories locally in time and
says nothing about the gap; four dimensions is not accessible.
*Small volume* relocates the crossover from the coupling to the volume
variable: the small-volume theory has an explicit gap
$\delta_1g^{2/3}\hbar c/L$, and the passage to $L\Lambda\gg1$ is the same
confinement-scale problem.

## 6. The confinement scale as a single lattice theory

After the small-field renormalization has run to the scale where the
effective coupling is of order one, the problem is one lattice gauge
theory at that scale with a bounded but unknown effective interaction,
to be shown mixing uniformly in the volume. Beyond that scale the block
variables decorrelate and the effective interaction approaches the
trivial fixed point, inside the completely analytical set. The whole
difficulty is therefore concentrated at one scale and one effective
interaction, which is the sharpest form of the statement that the
problem has no small parameter, and which is exactly what the block
verification of item 2 addresses.

## 7. Consequence for STATE

The review is closed. By written derivation, the confinement-scale
region is entered by nothing known; the two unblocking routes are a
correlation inequality for $SU(3)$, which would be new mathematics, and
the computer-assisted block verification, which is a decision about
the repository's rules and a large project. Constant-tightening on
either side of the region remains available and does not touch it.
