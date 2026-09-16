# The two reasons to stop, as research problems: what a correlation inequality would buy, what a certified verification cannot, and where the research is

The user's direction of 2026-09-17: the reasons recorded for stopping
are reasons to research. Taking each seriously changes the map, and one
earlier statement is corrected: a correlation inequality was called an
unblocking, and it is less than that.

**What a Griffiths-type inequality would buy.** Such an inequality
gives $d\langle W(C)\rangle/d\beta_W\ge0$ for Wilson loops. Consequences:
the string tension is nonincreasing in $\beta_W$, and the decay rate of
any correlator of loop observables with vanishing mean is nonincreasing
in $\beta_W$. Control therefore transfers **from weaker coupling to
stronger coupling only**: knowing a positive mass at $\beta_W'$ gives it
at every $\beta_W\le\beta_W'$. On the map of
[the bands note](confinement-scale-bands.md) this replaces the three
strong-side blocking steps of band B by the single mixing statement
H2, and it touches nothing on the weak side, where the problem is.
The vacuum-sector gap itself, the $0^{++}$ channel, is the decay of a
truncated correlator whose two terms both increase with $\beta_W$, so
even its monotonicity does not follow. A correlation inequality is a
simplification of H1's target, and no substitute for H1.

**Where the standard proofs of such inequalities break.** Ginibre's
method needs the interaction to lie in a cone of products of
single-site functions satisfying the duplicate-variables condition.
For the character cone of $SU(2)$ the single-site condition reduces to
$$\int\!\!\int\prod_{i=1}^n\big(\chi_i(x)-\chi_i(y)\big)\,dx\,dy
=\sum_{S\subseteq\{1..n\}}(-1)^{|S^c|}\,N_S\,N_{S^c},\qquad
N_S=\dim\operatorname{Hom}\Big(1,\bigotimes_{i\in S}V_i\Big),$$
which vanishes for odd $n$, equals $2N_{1234}+2(\delta_{12}\delta_{34}+\delta_{13}\delta_{24}+\delta_{14}\delta_{23})\ge0$
for $n=4$, and is positive in every case computed at $n=6$ (six spin
$\tfrac12$: $70$; six spin $1$: $100$; four spin $\tfrac12$ and two spin
$1$: $28$; six spin $2$: $260$). The single-site condition is therefore
no obstruction as far as checked. The obstruction is that the plaquette
term $\operatorname{Re}\operatorname{tr}(U_1U_2U_3U_4)$ is not a
nonnegative combination of products of single-link functions: the
abelian proof writes $\cos(\theta_1+\dots)$ through sums and differences
of angles, which uses the commutativity of the group, and no analogue
exists for a matrix product. To this author's knowledge the second
Griffiths inequality is open for $SU(2)$ and $SU(3)$ lattice gauge
theory, with neither proof nor counterexample; the centre-based
inequalities that do exist are listed in
[the what-would-unblock note](what-would-unblock.md) §1.

**What a certified verification cannot do.** H2 at $\beta_W\simeq6$ on a
box of $216$ to $2000$ links asks for a certified bound on a supremum
over boundary conditions of a total-variation distance between marginals
of Gibbs measures on $SU(3)^{|V|}$, an integral over $1700$ to $16000$
real dimensions. Certified quadrature in that dimension does not exist;
transfer-matrix truncations in the character basis have state spaces
exponential in the slice; Monte Carlo is not certified. The certified
methods that exist are polymer expansions with computer-enumerated small
polymers and analytic tails, and they converge only where the expansion
does, which for the Wilson measure means $\beta_W$ of order $0.1$ to $1$,
never $6$. So H2 cannot be supplied at the coupling where it is needed,
by any method known to the author, and the rigorous reach of the strong
side ends at $\beta_W\sim1$ at best, a factor of six below the
crossover. The corresponding decision about the repository's rules is
therefore moot.

**Where the research is.** Both reasons point to the same place. The
mass gap for $SU(3)$ is H1: control of the blocking steps from the weak
side down to the coupling where the strong side takes over, and the
strong side's reach is $\beta_W\sim1$ in principle and $0.0135$ as proved.
H1 splits into two sub-targets.

- *H1a, sharpness.* Rigorous small-field renormalization exists
  (Balaban, Commun. Math. Phys. 95 (1984) 17; 109 (1987) 249; 119 (1988)
  243; 122 (1989) 175; Magnen, Rivasseau and Sénéor, Commun. Math. Phys.
  155 (1993) 325; Dimock's exposition, Rev. Math. Phys. 25 (2013)
  1330010; all metadata level) and holds for $g^2$ below an unspecified
  constant. The weak-side analogue of band B is the stretch between the
  coupling that a rigorous small-field step can handle with explicit
  constants and $g^2\simeq1$, and its width is unknown because no
  explicit constant has ever been written down for one step.
- *H1b, the physics.* The last steps, in which $\xi/a$ passes from about
  $10$ to about $1$; three doublings at one loop.

**The programme that follows.** Write one blocking step of the
Euclidean small-field renormalization for $SU(3)$ with explicit
constants, in the form: block-averaged link variables; the fluctuation
integral at quadratic order, which is Gaussian with a constraint and
whose propagator decays on the scale of the block; the remainder as a
polymer gas with an explicit Kotecký--Preiss threshold $g_{\rm pert}^2$;
and the bound on the distance of the effective interaction from the
Wilson form. The pieces already in hand with constants are the
large-field measure bound $e^{-\eta^2/(4g^2)}$ of
[the lower-bound note](large-field-action-lower-bound.md), the
sharpness of the flow's growth
([instability note](flow-instability-large-field.md)), and the lattice
truncation ([lattice-truncation note](lattice-truncation-uniform.md)).
The deliverable of the first step is the number $g_{\rm pert}^2$, the
weak-side counterpart of the strong side's $0.0135$; the number of
doublings between $g_{\rm pert}^2$ and $g^2\simeq1$ is then the honest
width of the problem, in place of the crude "$1/g^2\gtrsim10^2$" now on
the map. Constants explicit; nothing promoted.
