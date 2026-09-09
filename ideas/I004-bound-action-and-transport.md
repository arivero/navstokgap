# I004: bound action and transport response

The next model should carry both a bound orbit and a precisely defined
fluctuation observable. This reconnects the transport laboratory with the
programme's original Kepler question. Status: research design, 2026-09-09;
the relativistic Kepler ingredient is established literature, audited in B27.

## A positive classical benchmark — M07

For a particle of mass $m>0$ in a fixed attractive centre, use

$$
H=\sqrt{m^2c^4+c^2(p_r^2+L^2/r^2)}-k/r,
\qquad r>0,\quad k,c>0.
$$

The angular action $|L|$ must exceed $k/c$ for a collision-free bound radial
well. Its circular minimum is
$E_{\min}=mc^2\sqrt{1-(k/(c|L|))^2}$.
The threshold is a positive infimum at fixed coupling and speed ceiling;
allowed angular momenta above it remain continuous. This is Boyer's known
classification, with source passages and a written effective-potential
derivation in the [B27 companion](../docs/batches/B27/relativistic-kepler-source-companion.md).

M07 completed this integration in the [Kepler note](../notes/relativistic-kepler-threshold.md)
and gap laboratory (C052–C053), naming
the domain of globally regular bound trajectories, the critical/plunging
endpoint and the limits $c\to\infty$ and $k\to0$. Any fixed softened core $-k/\sqrt{r^2+a^2}$ admits bound circles for every
positive angular action; subcritical minimizing circles collapse to the
centre as $a\downarrow0$. The fixed external potential
is part of the model; radiation and a dynamical second body belong to a later
extension. Units: $[k/c]=[L]=$ action.

## Which observable follows bound mechanics? — A15

The maintained coefficient
$\mathsf h(\Delta)=m\operatorname{Var}(X(t+\Delta)-X(t))/\Delta$
measures displacement transport. C047 and C051 already give useful mechanical
settings where its long-window value vanishes. A bounded stationary coordinate
has bounded displacement variance, so confinement requires a different route
to reading a persistent local action scale.

A15 compares local conditional variance, any intermediate-window plateau,
long-window transport response and orbital action in one specified confined
model. A proposed window $\tau_{\rm micro}\ll\Delta\ll\tau_{\rm conf}$ needs
an actual scale-separation estimate. The task should establish which estimator
can track a physical-time field $h(t)$ and which limit represents relaxation.
Its source audit must cover the selected estimator as well as the model.

**Completed A15/B29:** [the circular-orbit note](../notes/bound-orbit-action-observable.md)
gives vanishing transport response at both window extremes and a finite bound
on window ratios above a fixed action fraction. Twice the canonical covariance
area equals orbital action under uniform phase. Each phase law preserves its
own area; A16 now tests scale closure of this preparation-dependent estimator.

## Scale selection test — A16

Test a simultaneous space/time dilation $q_a(t)=a q(t/a)$, which preserves
velocities, against the exact admissibility axioms. Track masses, potentials,
couplings, preparation and action separately. For a proposed transformation
$V_a(q)=V(q/a)$ the potential itself changes; for Kepler this changes $k$.
The intended deliverable is a model-class closure test, with a list of the
premises that preserve or break dilation. This is a proposed calculation,
rather than a theorem that a fixed physical model admits arbitrary rescaling.

## Research payoff

M07 supplies a classical action threshold from regular bound motion and finite
speed. A15 identifies an observable suited to bound dynamics. A16 asks which
additional physical premise can select a common action value. Keep A14 as a
bounded preparation diagnostic and R02 as the finite-propagation classification
track. Each branch addresses a different part of the main target.
