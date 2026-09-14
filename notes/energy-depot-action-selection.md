# Nonlinear feedback selects an action only while its energy source supplies power

An oscillator with a finite energy depot relaxes to zero action in the model
below. Replenishing the depot above a threshold produces a positive attracting
action, independent of the initial seed but dependent on the supplied power
and oscillator frequency. The exact construction separates attraction from
universality and gives a concrete test of a self-excitation mechanism.

Status: exploratory written derivation, Q03; independent proof/literature
review is required before accepted-ledger promotion. This is an autonomous
dissipative effective model, not a derivation from a closed Hamiltonian field.

## 1. Construction and physical choice

Let an oscillator have angular frequency $\omega>0$, action $J\ge0$ and angle
$\theta$. Its measured mechanical energy is $H=\omega J$. Let $e\ge0$ be
stored depot energy. Choose loss rates $\gamma,\kappa>0$, conversion coefficient
$g>0$ with units $(\text{energy}\,\text{time})^{-1}$, and supplied power $P\ge0$.
Define

$$\dot\theta=\omega,\qquad
\dot J=2(ge-\gamma)J,\qquad
\dot e=P-\kappa e-2g e\omega J. \tag{1}$$

The nonlinear transfer $2ge\omega J$ enters oscillator energy and leaves the
depot with equal magnitude. The premise is stimulated gain proportional to
existing oscillation energy: a charged or active reservoir amplifies a seed,
while conversion depletes its stored energy. This is a deliberately simple
feedback law to test, rather than a universal mechanical law.

A real-quadrature realization removes the angle singularity at rest. With
coordinates $Q,R$ of units square root of action and $J=(Q^2+R^2)/2$, put

$$\dot Q=(ge-\gamma)Q-\omega R,\qquad
\dot R=\omega Q+(ge-\gamma)R.$$

These equations induce (1), including the invariant state $Q=R=0$.
For a harmonic mechanical readout take $x=Q/\sqrt{m\omega}$ and
$p=\sqrt{m\omega}R$; then $p^2/(2m)+m\omega^2x^2/2=\omega J$.
Gain acts on both quadratures, so this realization is an effective amplitude
model rather than Newton's unmodified relation $\dot x=p/m$.

The physical idea has precedent: Schweitzer, Ebeling and Tilch describe
particles that store environmental energy and convert it into motion, with
limit cycles above an uptake threshold. Their model motivates the comparison;
equation (1) is the explicit model tested here.

## 2. Finite fuel: an exact energy inequality

The positive quadrant is invariant. For $E=\omega J+e$, cancellation of the
internal transfer gives

$$\dot E=P-2\gamma\omega J-\kappa e. \tag{2}$$

Put $a=\min(2\gamma,\kappa)>0$. At $P=0$,

$$0\le E(t)\le E(0)e^{-at},\qquad
0\le J(t)\le E(0)e^{-at}/\omega. \tag{3}$$

Thus even an initially amplifying depot, with $ge(0)>\gamma$, eventually
exhausts its energy and sends $J(t)$ to zero. For arbitrary fixed $P$, the
bound $\dot E\le P-aE$ also gives global bounded solutions. The conclusion
depends explicitly on positive losses. Lossless closed dynamics is a different
candidate, whose conserved energy can retain preparation dependence.

## 3. Replenishment: an explicit positive attractor

The quiet equilibrium is $(J,e)=(0,P/\kappa)$. The linear action growth rate
there is $2(gP/\kappa-\gamma)$. Define

$$P_c=\frac{\kappa\gamma}{g}.$$

For $P>P_c$ a positive equilibrium exists:

$$e_* = \frac{\gamma}{g},\qquad
J_* = \frac{P-P_c}{2\gamma\omega}. \tag{4}$$

It attracts every initial state with $J(0)>0$ and $e(0)>0$. To prove this,
use the nonnegative function

$$V=\omega\left[J-J_*-J_*\log(J/J_*)\right]
 +e-e_*-e_*\log(e/e_*).$$

Writing $\delta J=J-J_*$ and $\delta e=e-e_*$, the first term contributes
$2g\omega\delta J\delta e$. The depot equation is

$$\dot e=-(\kappa+2g\omega J_*)\delta e-2g\omega e\delta J.$$

Multiplication by $1-e_*/e$ cancels the cross term exactly, giving

$$\dot V=-(\kappa+2g\omega J_*)\frac{(e-e_*)^2}{e}\le0. \tag{5}$$

Sublevel sets of $V$ are compact within the positive quadrant. On $\dot V=0$
we have $e=e_*$; remaining there requires $J=J_*$. The invariant-set argument
therefore proves convergence to (4). An initially empty depot becomes positive
immediately when $P>0$. An exactly zero oscillator seed stays zero even above
threshold; the attracting positive branch has the basin $J(0)>0$.

The result supplies an actual physical-time action attractor in a classical
effective model. It also identifies precisely what powers it.

## 4. Selection tests and consequence

At the same $g,\gamma,\kappa,P$, probes of different frequency acquire the
same energy $\omega J_*=(P-P_c)/(2\gamma)$, rather than the same action.
Demanding a common action $K>0$ instead requires the power prescription

$$P(\omega)=P_c+2\gamma\omega K. \tag{6}$$

This prescription inserts the desired scale in the source. It is the physical
step a further theory must explain, rather than a consequence of attraction.
Moreover $J_*\downarrow0$ continuously as $P\downarrow P_c$: instability of
the quiet state above threshold supplies no positive lower action bound across
the admitted source parameters. Exact rest remains a trajectory throughout.

The promising ingredient is feedback that erases initial amplitude; the failed
ingredient is identifying its source-dependent attractor with a universal
constant. Together with Q02's proposed frequency-selective radiation response,
this suggests a sharper question: can a self-consistent reservoir dynamically
set a common spectral amplitude, with its energy budget included? Merely
connecting this depot to a linear radiation bath would still supply $P$.

Park further pumped-oscillator variants. A different route worth testing is a
conservative field sector with a fixed topological constraint: its quiet-state
exclusion would be a geometric restriction rather than continuous fueling.
The decisive test is whether its minimum action survives dilation, not merely
whether a nontrivial stationary configuration exists. This is a proposed next
test, not evidence that topology already fixes an action constant.

## Source and review boundary

F. Schweitzer, W. Ebeling and B. Tilch, *Complex Motion of Brownian Particles
with Energy Depots*, Physical Review Letters **80**, 5044 (1998),
[publisher record and abstract](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.80.5044).
Coverage: one discovery query and the publisher abstract; no full-text equation
match or novelty assessment. Its energy-uptake/limit-cycle mechanism prompted
the finite-fuel versus replenished comparison. Equations (1)--(6) are the
present exploratory calculation, with energy accounting and a written
Lyapunov check; no numerical or symbolic scripts were used.
