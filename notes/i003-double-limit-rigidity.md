# I003: finite propagation, internal state and resolution

Finite propagation remains a promising route to the structure of the state
at a cut. This revised draft preserves that question, the exact two-state
commutator comparison and the measurement-resolution test. It separates them
from the stronger claims superseded by the repository review.

Origin: the user’s I003 remarks and the independent Fable draft of
2026-09-08. Revised 2026-09-09 after coordinator review. The earlier version
is preserved in Git at commit `0632c7d`. No claim ID is assigned; R02 owns
the remaining theorem and prior-art audit.

## 1. Finite-propagation classification to audit

Use Fourier phase $e^{-ikx}$ and write

$$M_t(k)=e^{t(B-ikA)},\qquad
\partial_t\psi=-A\partial_x\psi+B\psi.$$

A candidate theorem is that every translation-invariant strongly continuous
$L^2(\mathbb R;\mathbb C^n)$ contraction semigroup whose convolution kernels
have support in $[-ut,ut]$ has this first-order form, with $A=A^\dagger$,
$\|A\|\le u$ and $B+B^\dagger\le0$. In the unitary case
$B=-iB_H$ with $B_H$ Hermitian.

This is the corrected proposed formulation, not a newly accepted classification.
The scalar unitary argument remains in
[the two-faces note](cut-paradox-two-faces.md). The matrix proof must justify
pointwise continuity in time from strong operator continuity, the local
matrix-logarithm construction, and differentiation of the generator.

A useful route is to apply Bernstein bounds to every matrix entry:
finite propagation gives exponential type at most $ut$, while contraction
bounds the multiplier on the real axis. If a differentiable generator is
established, the second derivative estimate should force its affine dependence
on $k$. Dissipativity for all real $k$ then constrains the derivative
coefficient. These are proof obligations for R02.

Positivity preservation adds a diagonal real velocity matrix in the physical
component basis. To conclude that $B$ is a conservative Markov switching
generator one must also impose conservation of total probability. For example,
$T_tf=e^{-t}f$ has positivity, contraction and zero propagation but loses mass.
Choose row/column conventions explicitly, and retain the $L^2$ contraction
hypothesis or its appropriate invariant-weight norm.

## 2. Exact two-state scale and its scope

For symmetric velocities $V=u\sigma_z$ and switching
$Q=\lambda(\sigma_x-I)$, the accepted C020 comparison gives

$$\|[V,Q]\|=2u\lambda,\qquad
H_*=\frac{mu^2}{\lambda}
=\frac{2mu^3}{\|[V,Q]\|}.$$

For the coherent specialization $A=c\sigma_z$,
$B_H=\omega_0\sigma_x$, the same matrix calculation gives
$\|[A,B_H]\|=2c\omega_0$. Assigning rest energy through a supplied action
unit $K$ gives $m=K\omega_0/c^2$. C039 provides the resulting Dirac model.
This keeps the source of $K$ separate from the frequency.

The two-state equalities are useful. A general multicomponent system carries
more than one rate, and a commutator norm need not detect every slow mode.
C041’s independent hidden sign changes the full gap while preserving the
velocity commutator and plateau.

The commuting case also needs the preparation:
a random constant velocity $V=\pm u$ with $Q=0$ gives

$$\operatorname{Var}(\Delta X)=u^2\Delta^2,\qquad
\mathsf h(\Delta)=mu^2\Delta.$$

A deterministic velocity gives zero variance instead. Thus commuting matrices
describe unchanged velocity sectors; their mixture can be ballistic. The
old general zero-response conclusion is superseded by this distinction.
Within C019’s finite irreducible reversible class, its spectral proof—not a
commutator alone—establishes positivity.

## 3. A specified measurement-noise double limit

Suppose a finite-speed process is measured with independent additive errors,
independent also of the motion, each centered with variance
$\varepsilon^2/12$. For two measurements the error in the increment has
variance $\varepsilon^2/6$, so

$$\mathsf h_\varepsilon(\Delta)
=\mathsf h(\Delta)+\frac{m\varepsilon^2}{6\Delta}.$$

This is an additive-noise or suitably dithered readout model. Deterministic
rounding to a fixed lattice does not automatically supply independent uniform
errors. In this specified model the two iterated limits are zero and infinity;
a path $\varepsilon^2=6\kappa_0\Delta/m$ gives the selected value $\kappa_0$.
It tests readout dependence, not a restriction on real-number subdivision.

For a uniform partition with $N-1$ interior nodes, pin endpoint errors to zero
and give independent interior errors that same variance. The expected added
kinetic action is $m(N-1)\varepsilon^2/(12\Delta)$; normalizing by
$2/(N-1)$ gives the same bias. Other endpoint/readout conventions need their
own calculation. The algebra and general classification remain under R02 review.

## 4. Preserved research questions

- Does finite propagation force a first-order internal-state model under the
  precise semigroup assumptions above?
- Which observable separates local fluctuation strength from bounded-motion
  transport cancellation? A15 now asks this explicitly.
- What makes a positive coefficient common across preparation classes?
  C035–C036 address mass composition within a specified class; A14 tests
  gap variability, and neither substitutes for a physical coherent phase rule.
- Can the cone/arrow analogy suggest a useful cut-state invariant? Its
  historical reception and modern mathematical interpretation remain distinct.

R02 should start with the scalar theorem and the corrected matrix convention,
then obtain a bounded prior-art audit. The earlier scripts remain historical
artifacts under the hard rule and are not an acceptance gate.
