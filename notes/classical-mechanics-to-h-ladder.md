# From classical mechanics to one action constant: a no-go boundary and a conditional derivation ladder

**Status — exact implications from stated classical augmentations; no claim
that bare classical mechanics determines Planck's constant.**  The
foundations programme must begin with classical mechanics, not with an
already supplied canonical commutator.  This note establishes the honest
starting point:

\[
 \text{bare classical mechanics}\not\Longrightarrow \hbar>0,
\]
while a specified nondegenerate classical stochastic law, together with
mass composition, **does** force one universal positive constant
$\kappa=mD$ of action dimension.  Further, separately stated assumptions
turn $\kappa$ into the canonical $\hbar$ of the scalar Schrödinger equation
and, with the operational premises of
[the foundations model](foundations-model-nonrelativistic-quantum-mechanics.md),
into finite nonrelativistic quantum mechanics.

The word “derive” has three different meanings here and they are not
interchangeable:

1. derive the *form* of one universal action constant from a physical
   classical law;
2. derive its *positive value* by excluding the deterministic branch;
3. identify/calibrate it with the measured $h_P/(2\pi)$.

Only the first is a consequence of the composition theorem below.  The
second needs a nondegeneracy premise about free motion; the third needs an
empirical radiation or measurement calibration.  Keeping these stages
separate is the result, not a retreat from the classical starting point.

## 1. Classical base theory and what it cannot select

Take a classical body on phase space $T^*\mathbb R^3$ with coordinates
$(q,p)$, Poisson bracket $\{q_a,p_b\}=\delta_{ab}$, and Hamiltonian
\[
 H(q,p)=\frac{|p|^2}{2m}+V(q).                               \tag{1}
\]
Hamilton's equations, Liouville evolution of probability measures,
canonical composition of independent systems, and arbitrary sharply
prepared canonical pointers are the base theory C0.  They contain actions
such as $\int p\,dq-H\,dt$, but no universal nonzero quantum of action.
The deterministic free solution $q_t=q_0+vt$ is admitted for every mass.

**Theorem 0 (the zero branch is a C0 model).**  C0 has a model in which every
free body follows $q_t=q_0+p_0t/m$ and every preparation is a Dirac measure
at a chosen phase point.  In that model the free variance rate is $D(m)=0$
for every $m$, all canonical pointer readouts may be made arbitrarily
sharp, and there is no positive universal action floor.  Consequently no
argument using C0 alone can prove $\hbar>0$.

*Proof.*  Hamilton's flow of (1) with $V=0$ carries every Dirac measure to
a Dirac measure and respects products/centre-of-mass composition.  The
canonical two-pointer construction of Proposition 1 below remains within
this model.  Thus it satisfies every C0 premise while realizing the zero
branch.  A consequence of C0 valid in all its models cannot exclude it.
$\square$

Two further obstructions make the boundary quantitative.

**Proposition 1 (classical record obstruction).**  Under C0, product
preparations with arbitrarily narrow canonical supports, classical Bayesian
readouts, and the two retained-pointer couplings of Theorem I in
[the unit/indeterminacy note](necessity-unit-and-indeterminacy.md) allow
posteriors with arbitrarily small $\Delta q\,\Delta p$.  Hence C0 cannot
imply a universal positive record floor.

*Reason.*  The cited theorem constructs the two pulses and posterior
supports explicitly.  Each pulse is canonical and preserves phase volume;
the unread conjugate pointer ranges grow while the desired posterior
shrinks. $\square$

**Proposition 2 (similarity obstruction).**  If a proposed universal action
floor is required to survive an admitted similarity that rescales every
available action with no fixed action unit, the floor is zero.  In
particular, dimensions and classical canonical mechanics alone cannot
select a universal positive numerical action.

*Reason.*  This is Theorem B of
[the action-unit note](action-unit-dimensional-selection.md): applying a
similarity with arbitrary positive scale to a putative fixed positive floor
would rescale it, so invariance forces zero.  A positive floor therefore
requires a fixed physical action scale or the exclusion of this
similarity. $\square$

These propositions do not say that classical physics is false.  They say
that the requested derivation needs a physical augmentation of C0 which
rules out at least the quiet deterministic and unrestricted-pointer
countermodels.  Calling such an augmentation “classical mechanics alone”
would hide the premise that does the work.

## 2. A classical augmentation that forces one action constant

Add the following free-motion law to C0.

- **C1 (continuous stationary independent free increments).**  A body of
  mass $m>0$, started at a deterministic point, has continuous paths with
  stationary independent increments and isotropic centred fluctuations.
- **C2 (mass-only universality).**  The centred free law is defined for
  every real $m>0$ and depends on no body attribute other than $m$.
- **C3 (independent centre-of-mass composition).**  For independent bodies,
  the centre of mass has the free centred law of the total mass.
- **C4 (nondegeneracy).**  The centred free motion is not deterministic for
  at least one mass.

C1 is a physical stochastic law, not a consequence of Hamilton's
trajectories.  C2--C3 state how the new free-motion law composes.  C4 is
the exact premise which excludes the classical $\hbar=0$ branch.

**Theorem 3 (classical composition derives one positive action constant).**
Under C0 and C1--C4, there is one $\kappa>0$ such that the free motion of a
body of mass $m$ is
\[
 X_t=X_0+v t+\sqrt{\frac{\kappa}{m}}\,W_t,
 \,\qquad D(m)=\frac{\kappa}{m},                             \tag{2}
\]
where $W$ is standard three-dimensional Brownian motion in the convention
$\operatorname{Var}W_t=t$.  Thus
\[
 \boxed{\quad \kappa=mD(m)>0,\qquad[\kappa]=\text{action}.\quad} \tag{3}
\]
The deterministic classical branch is recovered exactly by dropping C4,
when $\kappa=0$ is allowed.

*Proof.*  C1 and the continuous Lévy classification make the process
Brownian with drift and an isotropic variance rate $D(m)\ge0$.  Let
$M=m_1+m_2$.  The centre of mass of two independent bodies has variance
rate
\[
 \frac{m_1^2D(m_1)+m_2^2D(m_2)}{M^2}.
\]
C3 equates this to $D(M)$.  Hence
$g(m)=m^2D(m)$ is additive on positive reals.  Since $g\ge0$, it is
monotone; the nonnegative Cauchy equation gives $g(m)=\kappa m$ for one
$\kappa\ge0$.  C4 makes it strictly positive.  The dimensions in (3)
follow from $[D]=L^2/T$. $\square$

The proof is the content of Theorems S1--S2 in
[the stochastic route](stochastic-route-velocitas-ultima.md), written here
as the foundations entry point.  It is a genuine derivation of the
**universality and action dimension** of $\kappa$ from C1--C4, rather than
a declaration that every body has an independently chosen $\hbar_m$.
It does not derive C1--C4 from deterministic Hamiltonian mechanics.

## 3. The Newton comparison is already controlled by $\kappa$

The same classical augmentation makes the Galileo action operationally
visible.  Add:

- **C5 (force-independent additive noise).**  Under a constant force, the
  path is the Newtonian parabola plus the same Brownian noise as in (2).

For a duration $\tau$ and force $F$, the inertial chord and the parabola,
pinned to common endpoints, differ by a Cameron--Martin shift.  Set
\[
 K_\tau=\frac{F^2\tau^3}{24m}.                              \tag{4}
\]

**Theorem 4 (classical stochastic record floor).**  Under C0--C5, the
optimal equal-prior test of the two pinned paths has error
\[
 P_{\rm err}=\Phi\!\left(-\sqrt{\frac{K_\tau}{2\kappa}}\right). \tag{5}
\]
Consequently confidence $1-\epsilon$ requires
\[
 K_\tau\ge2z_{1-\epsilon}^2\kappa.                         \tag{6}
\]

*Proof.*  The two Gaussian bridge measures have common covariance
$D(m)=\kappa/m$ and Cameron--Martin squared distance
$K_\tau/\kappa$.  The likelihood-ratio test of two Gaussians at equal
priors has error (5); rearranging gives (6).  This is Theorem S3 of the
[stochastic route](stochastic-route-velocitas-ultima.md). $\square$

Thus a positive action constant and a Galileo/record scale can arise in a
classical stochastic model before Hilbert-space kinematics are assumed.
This is deliberately weaker than a derivation of quantum mechanics:
C1--C5 describe positive probability measures on paths, whereas quantum
states need not be positive joint measures on $(q,p)$.

## 4. From the stochastic constant to the Schrödinger constant

Put
\[
 \nu=\frac{\kappa}{2m}.                                      \tag{7}
\]
The factor $1/2$ is the conventional diffusion coefficient: a Brownian
motion with variance rate $D=\kappa/m$ has generator $\nu\Delta$.
To pass from (2) to quantum dynamics, add assumptions that are **not** in
C0--C5:

- **N1 (two-sided diffusion).**  The process has compatible forward and
  backward drifts with common diffusion coefficient $\nu$, density
  $\rho>0$, osmotic velocity $u=\nu\nabla\log\rho$, and current velocity
  $v=\nabla S/m$ for a real phase field $S$; hence
  $\partial_t\rho+\nabla\cdot(\rho v)=0$.
- **N2 (Nelson mean law).**  The symmetric mean acceleration obeys
  $m a_{\rm mean}=-\nabla V$.
- **N3 (single-valued phase, or stated circulation sectors).**  The phase
  data are globally compatible with a complex wave function.

The following elementary equivalence makes the additional content
transparent.

**Lemma 5 (Madelung conversion).**  Let $\rho>0$ and $S$ be sufficiently
smooth.  The function
\[
 \psi=\sqrt\rho\,e^{iS/\kappa}                              \tag{8}
\]
solves
\[
 i\kappa\,\partial_t\psi=
 \left(-\frac{\kappa^2}{2m}\Delta+V\right)\psi             \tag{9}
\]
if and only if
\[
 \partial_t\rho+\nabla\!\cdot\left(\rho\frac{\nabla S}{m}\right)=0, \tag{10}
\]
\[
 \partial_tS+\frac{|\nabla S|^2}{2m}+V
 -\frac{\kappa^2}{2m}\frac{\Delta\sqrt\rho}{\sqrt\rho}=0. \tag{11}
\]

*Proof.*  Substitute (8) into (9), divide by the nonzero $\psi$, and take
imaginary and real parts.  Conversely, recombine (10)--(11). $\square$

**Lemma 6 (where the quantum-potential equation enters).**  In the
standard two-sided diffusion notation set
\[
 u=\nu\nabla\log\rho,\qquad v=\frac{\nabla S}{m}.
\]
Its symmetric mean acceleration is
\[
 a_{\rm mean}=\partial_tv+(v\!\cdot\!\nabla)v
 -(u\!\cdot\!\nabla)u-\nu\Delta u.                         \tag{12}
\]
The identity
\[
 (u\!\cdot\!\nabla)u+\nu\Delta u
 =2\nu^2\nabla\!\left(\frac{\Delta\sqrt\rho}{\sqrt\rho}\right) \tag{13}
\]
then shows that N2 is equivalent, up to a time-only function absorbable in
$S$, to (11) with $\kappa=2m\nu$.

*Proof.*  Write $r=\sqrt\rho$.  Since
$u=2\nu\nabla\log r$, direct differentiation gives (13).  Substitute it
and $v=\nabla S/m$ into (12), multiply by $m$, and use
$(v\cdot\nabla)v=\nabla(|\nabla S|^2/(2m^2))$.  The equation
$m a_{\rm mean}=-\nabla V$ says that the gradient of the left side of
(11) is zero.  Its time-only remainder is removed by changing $S$ by a
time-dependent constant. $\square$

Thus N1--N3 yield (10)--(11) with the diffusion coefficient (7), and the
scalar Schrödinger equation follows with
\[
 \boxed{\hbar=\kappa.}                                      \tag{14}
\]
This is conditional on N1--N3.  In particular, it does not show that every
classical Brownian body obeys the mean law or has a globally single-valued
phase.  The existing source audit explicitly keeps those state and phase
assumptions separate; see the final paragraph of
[the stochastic route](stochastic-route-velocitas-ultima.md).

## 5. Why the Schrödinger bridge does not yet derive all of quantum mechanics

Equations (8)--(14) reconstruct one-particle scalar wave dynamics from a
classical stochastic augmentation plus N1--N3.  They do not independently
prove:

- the Weyl algebra for all observables and all finite canonical systems;
- Born probabilities for arbitrary effects rather than the position density
  $|\psi|^2$;
- entanglement and tensor composition of arbitrary systems;
- completely positive instrument closure for all retained memories; or
- a relativistic quantum field theory.

Those are precisely F1--F5 of
[the foundations model](foundations-model-nonrelativistic-quantum-mechanics.md).
The model theorem there is the completion step: after the classical ladder
has supplied and calibrated $\kappa=\hbar$, F1--F5 yield the finite
operational quantum model.  A commutative Gaussian covariance restriction
remains an explicit rival: it has an affine uncertainty/record floor but
not F1's noncommutative kinematics.  Thus neither (6) nor (9) may be cited
as a standalone derivation of the full quantum measurement theory.

## 6. Calibrating the derived constant

Theorem 3 determines one universal action $\kappa$, not its number.
There are two logically separate empirical bridges.

**R1 (radiation unit).**  The classical thermodynamic assumptions of
Kirchhoff universality, Wien scaling, a finite nonzero spectrum, and the
Rayleigh--Jeans limit define an enclosure-independent positive action
$h_{\rm rad}$ in Theorem U of
[the unit/indeterminacy note](necessity-unit-and-indeterminacy.md).  An
additional cross-sector universality law could identify
$\kappa=\gamma h_{\rm rad}$ for a fixed pure number $\gamma>0$.
The thermodynamic theorem alone does not determine $\gamma$.

**R2 (Planck normalization).**  Under the conditional SED identification
of the stationary oscillator area, $2\zeta=h_P/(2\pi)$, and if the
classical free-noise constant is the same record constant,
\[
 \kappa=h_*=2\zeta=\frac{h_P}{2\pi}.                        \tag{15}
\]
The SED derivation/calibration and all-record closure are additional,
disputed or open physical premises as recorded in
[the SED link](sed-zeta-radiation-link.md).  Equation (15) is an empirical
identification, not a theorem of Brownian motion.

With R2 and N1--N3, the derivation ladder has the desired endpoint
$\hbar=h_P/(2\pi)$.  Without R2 it has a universal positive action
$\kappa$ but no numerical Planck calibration; without C4 it retains the
classical $\kappa=0$ branch.

## 7. The complete conditional ladder

The logical architecture may now be stated without circularity:
\[
\begin{array}{rcl}
\text{C0 + unrestricted records/no fixed action unit} &\Rightarrow&
\text{no universal positive floor (Theorem 0, Props. 1--2)},\\
\text{C0+C1--C4} &\Rightarrow& \kappa=mD>0\quad\text{(Theorem 3)},\\
\text{C0+C1--C5} &\Rightarrow& \text{Galileo record scale (Theorem 4)},\\
\text{previous + N1--N3} &\Rightarrow& \text{scalar Schrödinger dynamics with }\hbar=\kappa,\\
\text{previous + R2} &\Rightarrow& \hbar=h_P/(2\pi),\\
\text{previous + F1--F5} &\Rightarrow& \text{finite operational quantum model.}
\end{array}                                                    \tag{16}
\]

Every right arrow is a proved mathematical implication from its displayed
premises, either in this note or in the linked source note.  Every premise
not derived from C0 is named.  This is the strongest current answer to
“start from classical mechanics and derive $h$”: classical mechanics plus
a specific, testable physical law of nondegenerate free fluctuations and
mass composition derives the universal action **form**; calibration and
noncommutative quantum kinematics remain physical work rather than hidden
assumptions.

## 8. Consequence for STATE

The priority foundations task is no longer phrased as “assume quantum
mechanics, then explain its floor.”  It begins at C0 and has three clear
frontiers: establish or falsify C1--C4 as a physical free-motion law;
connect its derived $\kappa$ to a measured universal radiation/record
scale; and justify the N/F premises that turn the classical stochastic
model into operational quantum mechanics.  This programme is independent
of the Yang--Mills mass-gap problem, which may only reuse the calibrated
constant once supplied.
