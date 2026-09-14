# Global spin phases quantize a ratio, not an absolute action scale

A classical spin sphere has globally consistent Hamiltonian dynamics for any
positive symplectic area. Requiring a well-defined phase with a supplied
action constant K imposes the integer condition 2s/K in Z. It restricts the
allowed sphere area relative to K, while leaving the common normalization
free and allowing arbitrarily small local loop actions.

This is Q07's exploratory premise test, with explicit patch calculations.
It uses established prequantization geometry; it claims neither novelty nor
an accepted project result. Its purpose is to locate the physical premise
behind a tempting global-consistency route to action selection.

## 1. A classical action defined in patches

Let the spin direction n lie on the unit sphere with polar coordinates
$(\theta,\phi)$. Supply $s>0$ with action units and define

$$\omega_s=s\sin\theta\,d\theta\wedge d\phi,
\qquad \int_{S^2}\omega_s=4\pi s. \tag{1}$$

For any smooth real Hamiltonian H, define the vector field by
$\iota_{X_H}\omega_s=-dH$. Nondegeneracy gives a unique smooth vector field;
compactness gives its complete flow. Thus s may be any positive real value.
There is no globally defined one-form with derivative $\omega_s$, since the
integral of an exact two-form on the closed sphere would vanish.

Instead use regular north and south potentials

$$\alpha_N=s(1-\cos\theta)d\phi,\qquad
\alpha_S=-s(1+\cos\theta)d\phi. \tag{2}$$

Each has derivative $\omega_s$. On a simply connected part of the overlap,

$$\alpha_N-\alpha_S=2s\,d\phi=d(2s\phi). \tag{3}$$

The local actions $S_U=\int[\alpha_U(\dot n)-H(n)]dt$ differ by an endpoint
term. Their fixed-endpoint variations agree, yielding the same global
Hamiltonian equation. The azimuth is not single-valued on the entire overlap;
going around it changes $2s\phi$ by $4\pi s$. This constant ambiguity does
not change the equations. Classical variational consistency requires the
local derivatives to agree, not a globally single-valued real action value.

As a concrete clock, take $H=-\Omega s\cos\theta$, where $\Omega$ has inverse
time units. The equation gives $\dot\phi=\Omega$, $\dot\theta=0$. Multiplying
s and H by the same positive factor leaves this physical-time motion intact.

## 2. The added phase requirement

Now supply $K>0$ with action units and ask for phase transport compatible
with the local factors $\exp(iS_U/K)$. On the overlap the transition phase,
up to convention for its inverse, is

$$g_{NS}(\phi)=\exp(i2s\phi/K).$$

This must be single-valued when $\phi$ advances by $2\pi$. Hence

$$\exp(i4\pi s/K)=1
\quad\Longleftrightarrow\quad \frac{2s}{K}\in\mathbb Z. \tag{4}$$

The same condition follows by spanning a closed loop with a surface: two
spanning surfaces differ by an integer number of spheres, so their geometric
actions differ by $4\pi s$ times an integer. Equation (4) makes the exponent
independent of this choice. For open paths the transport is a map between
endpoint phase fibres, rather than a gauge-independent scalar.

The extra premise is a U(1) phase with curvature proportional to
$\omega_s/K$. Equation (4) is its compatibility condition. The classical
symplectic form alone supplies no such phase, no interference rule and no K.
Prequantization also leaves further state-space and measurement choices open.

## 3. Three decisive countertests

**Common rescaling.** If (s,H,K) satisfies the classical and phase conditions,
so does $(\eta s,\eta H,\eta K)$ for every $\eta>0$. Both the Hamiltonian
flow and the dimensionless phase remain unchanged. Thus even phase
consistency fixes a ratio rather than an absolute dimensional constant.

**Local contraction.** With H=0, the geometric action around a latitude
bounding a north-pole cap is

$$A(\theta_0)=2\pi s(1-\cos\theta_0)\longrightarrow0
\quad(\theta_0\downarrow0). \tag{5}$$

These are trial loops, not nonconstant solutions for H=0. They test local
action resolution: quantization of the total sphere flux allows arbitrarily
small nonzero cap actions. It does not impose a minimum polygonal cell or
invalidate ordinary time subdivision. At fixed K and s>0, (4) instead
restricts the allowed total sphere area, giving $s\ge K/2$ in that family.

**Two coupled spheres.** Take the product with form
$\omega_{s_1}\oplus\omega_{s_2}$ and any smooth interaction, for example
$H=J n_1\cdot n_2$ with J in energy units. It defines complete classical
dynamics for arbitrary $s_1,s_2>0$, including $s_2/s_1=\sqrt2$.
A common prequantization phase constant would require

$$2s_1/K=m_1,\qquad 2s_2/K=m_2,
\qquad m_1,m_2\in\mathbb Z_{>0}. \tag{6}$$

Restriction to each sphere with the other held fixed proves these necessary
conditions; product transition functions make them sufficient for this
prequantization construction. Thus $s_2/s_1=m_2/m_1$ must be rational.
Classical coupling admits the irrational example, while a single-K phase
bundle excludes it. The exclusion comes from the added phase structure,
not from a failure of reciprocal Hamiltonian mechanics. Even a permitted
rational ratio leaves infinitely many choices obtained by K replaced by K/n.

## 4. Consequence for the programme

Topology can turn a common phase premise into an arithmetic selection rule.
That is a stronger compatibility requirement than Q06's reciprocal forces,
and the irrational pair makes the difference explicit. It still leaves the
absolute scale free and local actions continuous.

Park further patching examples. The next useful construction should test a
physical interference record: can two classical wave paths coupled to a
mechanical receiver establish a universal action-to-phase conversion, rather
than a frequency-, amplitude- or apparatus-dependent calibration? Specify
energy transfer and the measured record before using any quantum probability
rule. This changes the question from another global bundle condition to the
physical origin of the phase premise that (4) requires.

## Source boundary

F. Bonechi, A. S. Cattaneo and M. Zabzine, *Geometric quantization and
non-perturbative Poisson sigma model*, Advances in Theoretical and Mathematical
Physics **10**, 683--712 (2006),
[arXiv:math/0507223v3](https://arxiv.org/abs/math/0507223v3),
explicitly attributes its integrality condition to requirements on a path
integral. Coverage here: one discovery query and its arXiv abstract; no
full-proof or exact sphere-formula audit. The local potentials, variational
patching and tests (4)--(6) are written out above. Independent review and
a bounded librarian comparison are required before any ledger promotion.
No numerical or symbolic verification scripts were used.
