# Flowing before decimating leaves every norm-based criterion unchanged: what is needed is a statement about the state

Conjugating by the flow before blocking does not improve the criterion of
[the blocking-criterion note](blocking-criterion-monotone.md), and the
reason is one line: $\Phi_t$ is a bijection of the configuration space,
so
$$\big\|V\circ\Phi_t\big\|_\infty=\sup_U V\big(\Phi_t(U)\big)
=\sup_{U'}V(U')=\big\|V\big\|_\infty,$$
even though $V(\Phi_t(U))\le V(U)$ holds pointwise by the monotonicity of
the flow. The straddling-plaquette norm that enters $\beta_{\rm block}$ is
therefore unchanged, the block gap is unchanged because conjugation is
unitary, and the factor $3M^2/8$ by which blocking loses is unchanged.
The same argument disposes of every criterion built from operator norms:
**no reordering of conjugation and decimation can help, because the
quantities such a criterion uses are conjugation-invariant or
bijection-invariant.** The flow's gain is pointwise and therefore visible
only in expectation, that is, only against a state whose weight sits
where the flowed action is small. With that, the last inexpensive idea
in this programme is closed, and the residual statement is sharp: the
remaining input is control of the ground-state measure, which is the
constructive problem in its Euclidean form. Constants explicit; nothing
promoted.

## 1. The three invariances

Let $\Phi_t$ be the lattice flow map and $W_t$ its unitary
implementation, as in
[the flow-conjugation note](flow-conjugation-truncation.md) Proposition 1.

**(i) Spectra are conjugation-invariant.** Every eigenvalue of $H$,
every gap, and in particular the block gap $\Delta_M$ of a block
Hamiltonian, is unchanged by $H\mapsto W_tHW_t^*$.

**(ii) Sup norms of multiplication operators are bijection-invariant.**
For $f\in C(\mathcal M)$ and a bijection $\Phi$ of $\mathcal M$,
$\|f\circ\Phi\|_\infty=\|f\|_\infty$. Applied to the magnetic term,
$$\big\|V\circ\Phi_t\big\|_\infty=\big\|V\big\|_\infty
=\frac{4N\hbar c}{ag^2}\cdot\#\{\text{plaquettes}\},$$
and to the straddling part, $\|\sum_{p\ \rm str}w_p\circ\Phi_t\|_\infty$
is bounded by the same $6M^2\cdot4N\hbar c/(ag^2)$ per block as before.
The pointwise inequality $V\circ\Phi_t\le V$, which the monotonicity of
the flow supplies, is compatible with equality of the suprema because
$\Phi_t$ maps the configuration space onto itself.

**(iii) Hence the criterion is unchanged.** The blocking criterion
$$\beta_{\rm block}=\frac{\big\|\sum_{p\ \rm str}w_p\big\|_\infty}{\Delta_M}
=\frac{24M^2N}{g^2\,\delta(g;M)}$$
has a numerator fixed by (ii) and a denominator fixed by (i), so
conjugating before blocking leaves it exactly as computed in
[the blocking-criterion note](blocking-criterion-monotone.md), and
blocking still loses by $3M^2/8$.

## 2. Why no reordering helps

Any criterion of the form (perturbation norm)/(unperturbed gap) is built
from two quantities of which the first is invariant under bijections of
the configuration space and the second under unitary conjugation. The
flow supplies exactly a bijection and a unitary. So:

**Proposition.** Let $\mathcal C(H_0,\phi)$ be any criterion depending on
$H_0$ only through its spectrum and on $\phi$ only through
$\|\phi\|_\infty$. Then $\mathcal C$ takes the same value for
$(H_0,\phi)$ and for $(W_tH_0W_t^*,\,\phi\circ\Phi_t)$, for every flow
time $t$.

This covers the Yarotsky criterion used in
[the T2 note](strong-coupling-uniform-gap.md), its blocked version, and
the Schur-complement criteria of
[the Feshbach note](weak-coupling-feshbach-reduction.md), all of which
reduce to comparisons of norms with gaps.

## 3. Where the flow's gain actually lives

The flow does reduce the action: $V(\Phi_t(U))\le V(U)$ for every $U$,
with strict inequality away from critical points, and
$\frac{d}{ds}S(B_s)=-\|D^*G\|_2^2$. That gain appears in expectations,
$$\big\langle\psi,\;(V\circ\Phi_t)\,\psi\big\rangle\ \le\ \big\langle\psi,\;V\psi\big\rangle
\qquad\text{for every state }\psi,$$
and is large when the weight of $\psi$ sits where the flow moves the
configuration far, that is, on rough configurations. So the flow
converts a rough state into a smooth one at the level of expectations
while leaving every worst-case bound alone.

A criterion that could see the gain must therefore be **relative to the
state**, of the form
$$\big\langle\psi,\phi\,\psi\big\rangle\ \le\ \epsilon\,\big\langle\psi,(H-E_0)\psi\big\rangle+\eta\|\psi\|^2
\qquad\text{on the low-energy subspace},$$
which is the relative form already isolated in
[the Schur note](schur-error-ultraviolet.md) Lemma 1$'$ and in the
relative hypothesis of
[the Feshbach note](weak-coupling-feshbach-reduction.md) §3a. The
quantity it needs is the distribution of the field strength in the
low-energy states, that is, the ground-state measure
$|\Omega(U)|^2\,dU$, which is a probability measure on the configuration
space and is exactly the object the Euclidean formulation supplies
explicitly as $e^{-S}dU$ and the Hamiltonian formulation leaves
implicit.

## 4. The residual statement

Collecting the closed routes of this programme:

| method | status | reason |
| --- | --- | --- |
| variational upper bounds | closed for $m>0$ | a spectral measure with all negative moments finite can have $m=0$ |
| expansion around the free theory | closed | bound reaches $m$ only at the confinement scale |
| blocking by projection | closed | boundary grows like $M^2$, block gap does not |
| conjugation by the flow | closed | spectrum-invariant; the gain is the truncation, which is cheap |
| flow before decimation | closed (this note) | norms are bijection-invariant |
| decimation with controlled couplings | **open** | the constructive problem |

Every method that uses only norms and spectra is exhausted, and each was
closed by a computation with explicit constants. What is left needs the
distribution of the field in the low-energy states, and that is where the
Euclidean construction has its tools and the Hamiltonian formulation has
none of its own.

## 5. Consequence for STATE

The question raised at the end of
[the lattice-truncation note](lattice-truncation-uniform.md) is answered
in the negative, with the invariance that makes it so. The programme's
norm-based line is complete. The next thing that would advance it is an
estimate on the ground-state measure of the Kogut--Susskind Hamiltonian
at intermediate coupling, for instance a bound of the form
$|\Omega(U)|^2\le C\,e^{-\lambda S_w(U)}$ with $\lambda>0$ uniform in the
volume, which would import the Euclidean large-field machinery into the
Hamiltonian setting. That is a well-posed question and it is the natural
successor to everything above.
