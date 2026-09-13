# Classical action scales: obstructions, conditional bounds and quantum premises

Classical mechanics in the tested classes permits action-valued observables
arbitrarily close to zero. Positive bounds appear when the class supplies an
excitation floor, a fluctuating reference preparation, or restricted measurement
information. None of the accepted calculations identifies such a bound with a
universal quantum phase parameter. The useful outcome is a map of the premises
that a selection principle must add and the counterexamples it must exclude.

This paper consolidates accepted repository results through C123. Its claims
retain the domains of their original proofs; it states no combined theorem
covering every classical model. Proof and literature status remain in the
[claim ledger](../claims/LEDGER.md). The final section gives an evidence map
for the inherited audits. The detailed receiver/calibration sequence is a
technical resource for the questions summarized here.

## 1. Select the observable before asking whether it has a floor

An action difference, orbital action, fluctuation coefficient and reconstruction
error product can all have action units while answering different questions.
We use physical units throughout, with Planck's constants related by
$h=2\pi\hbar$; a model parameter K is not identified with either by notation.

| Object | Definition and domain | What positivity would mean |
| --- | --- | --- |
| Action excess | $\Delta S=S[q+\eta]-S[q]$, on a stated fixed-endpoint path class | Separation in action values on that class |
| Orbit action | $J=(2\pi)^{-1}\oint p\cdot dq$, on closed trajectories | Minimum integrated mechanical excursion |
| Displacement response | $h_\Delta=m\operatorname{Var}[X(t+\Delta)-X(t)]/\Delta$ | Prepared fluctuations at observation window $\Delta$ |
| Canonical reconstruction product | $R_xR_P$, optimal worst-case scalar errors for stated data and preparations | Limits of that information protocol |
| Spectral gap | Lowest positive spectrum of a specified operator | Separation from its ground sector; energy or inverse-time units depend on the operator |

For a stationary confined coordinate of finite variance, the displacement
response tends to zero as the observation window grows, even when its orbit
action is positive. C047 and C054–C055 make this observable mismatch concrete.
For reconstruction, positive coordinate errors can occur on a smooth compatible
curve of zero projected planar area (C120). An error product is therefore not
a phase-space cell area without an additional argument.

## 2. Three routes to arbitrarily small classical action

**Continuous variation closes action excess.** With mass $m>0$, duration $T>0$,
constant force and fixed endpoints, the variation $\eta(t)=a t(T-t)$ gives

$$\Delta S=\frac{ma^2T^3}{6}\longrightarrow0\quad(a\longrightarrow0).$$

The varied paths are comparison paths, not generally solutions of the same
boundary-value dynamics. This is C002's precise admissibility boundary. A
positive Dirichlet Hessian controls cost relative to the variation norm; the
variation amplitude can still shrink. The [foundations paper](../papers/action-gap-foundations.tex)
contains the calculation and its source audit.

**Admitted contractions close several action observables together.** For
Newtonian or relativistic kinetic energy $T(p)$ and external potential $V(q)$, set

$$V_a(Q)=V(Q/a),\qquad q_a(t)=a q(t/a),\qquad p_a(t)=p(t/a),\quad a>0.$$

Hamilton's equations are preserved between the two models. Mass, speeds and
energy values stay fixed; forces scale by $a^{-1}$. Canonical orbit action
and Hamilton action scale by $a$. Corresponding prepared covariance actions
and corresponding observation-window responses obey the same degree-one
scaling. Thus any admissible class closed under arbitrarily small such
contractions has zero positive-action infimum (C056–C057). A fixed potential
or uniform force ceiling can exclude this particular transformation. See
[the dilation proof](action-scale-dilation.md) for the full domain and limit order.

**Even a fixed force-bounded potential can admit small actions.** C058 fixes
one smooth relativistic confining potential

$$V(r)=k_s b^2\left(\sqrt{1+r^2/b^2}-1\right),\qquad k_s,b,m,c>0.$$

Here $k_s$ is stiffness; the force is globally bounded by $k_s b$.
The stable circular orbits have $J_R\sim\sqrt{mk_s}R^2\to0$ as $R\to0$;
their speeds also tend to zero. This family keeps the potential
fixed, so excluding the contraction map alone does not supply a floor.
[The fixed-force proof](fixed-force-small-circles.md) isolates the missing
excitation premise.

These are complementary countertests with different admissibility assumptions.
A proposed principle should state which family it excludes and which
independent physical condition excludes it.

## 3. Positive classical bounds reveal their physical input

**Persistent excitation plus limited force gives a sharp orbit-action bound.**
For a regular closed $C^2$ trajectory in dimension at least two, canonical
momentum $p=m\dot q$, speed at least $v_*>0$ and force at most $F_{\max}>0$,
C060 gives

$$J\ge\frac{m^2v_*^3}{F_{\max}}.$$

Total turning is at least $2\pi$; the force ceiling limits the rate of
momentum turning, and the speed floor converts that duration into action.
A circle realizes equality within the admissible smooth-potential class.
For relativistic momentum the bound is multiplied by
$(1-v_*^2/c^2)^{-1}$, with $v_*<c$. The excitation floor supplies positivity;
the scale depends on mass, excitation and force. The [closed-orbit proof](closed-orbit-force-action.md)
retains the momentum, frame and regularity assumptions. A19's peak-excursion
variant is a supporting question, not yet an accepted result.

**Composition propagates a supplied positive fluctuation scale.** For
independent constituents and a mass-only coefficient within one preparation
class, centre-of-mass composition gives

$$\kappa(m_1+m_2)=\frac{m_1\kappa(m_1)+m_2\kappa(m_2)}{m_1+m_2}.$$

Nonnegativity and additive composition for every positive mass force
$\kappa(m)=K\ge0$. A reference two-state velocity process with mass $m_0$,
speed $u_0>0$ and finite positive reversal rate $\lambda_0$ then gives
$K=m_0u_0^2/\lambda_0>0$ (C035–C036). The reference preparation supplies
positivity. Different preparation classes can have different K; matching a
whole-body preparation to independently composed constituents is an explicit
premise. [The composition proof](composition-universality.md) also gives
countertests of that premise.

The singular relativistic Kepler threshold $|L|>k/c$ is another useful positive
classical benchmark, inherited from established literature. Its value depends
on the supplied coupling and its regular collision-free domain. Softening the
core admits circles of arbitrarily small angular action (C052–C053). It does
not supply an action lattice or a universal constant. See the
[Kepler comparison](relativistic-kepler-threshold.md).

## 4. What the calibration sequence settles

Preparation and record access decide the reconstruction obstruction in the
finite mechanical receiver. R05–R33 make those resources explicit; their
principal contribution is the following classification.

| Information/preparation regime | Accepted conclusion | Selection premise still needed |
| --- | --- | --- |
| Scalable incoming preparation and exact delayed records | A fixed finite-mass, finite-duration apparatus allows vanishing reconstruction error and disturbance, C068–C069 | Physical restriction preventing that preparation/record limit |
| Fixed preparation uncertainty with incomplete supplied data | Exact common-record families give positive reconstruction risks in specified classes, C090–C093 and C106–C115 | Reason those uncertainties are unavoidable and universal |
| Sufficient exact calibration and full records on the stated fixed box | Uniform receiver recovery, with error bounded by record error divided by coupling, C116–C118 | An independent restriction on final-record or calibration precision |
| Four finite calibration tolerances with exact records | Canonical product has matched order $\min\{1,(\epsilon/\lambda)^2\}$ in fixed component units, C119 | Origin and composition law of tolerance epsilon |
| One uncertain or correlated calibration direction | The direction determines canonical response; a zero-area curve can have positive coordinate risks, C120–C123 | A physical reason for the admitted uncertainty geometry |

The recovery row uses R30's sufficiently small fixed apparatus box and bounded
convex receiver domain. It does not cover R29's larger preparation box. The
R33 estimates concern a selected local common-record fibre; their upper bounds
are not global minimax bounds. All error products convert to action through the
fixed physical position and momentum units.

C123 adds an exact symmetry cancellation and explicit quadratic response. Its
remaining curvature coefficient may refine a local error law, but no current
argument makes that coefficient decide quantum necessity or universality.
The research decision is to park that continuation and retain its derivation
for a named future dependency. The [R33 handoff](../research/handoffs/R33.md)
preserves the open calculation.

The general lesson is conditional: these apparatus examples defeat a derivation
that relies only on the resource bounds they satisfy. Positive classical
reconstruction risk and the quantum commutation relation remain distinct
claims. [The apparatus construction](autonomous-finite-readout.md) and
[calibration-tolerance proof](calibration-tolerance-recovery.md) supply the
underlying dynamics and estimates.

## 5. Quantum necessity and mass gap require different next arguments

**Quantum necessity requires a premise that excludes the classical alternatives.**
The checkerboard comparison starts with complex amplitudes, Born probabilities
and a supplied $K>0$, then derives its Dirac continuum limit. It establishes
what those premises produce; it does not select them mechanically. Q01 now
asks which reconstruction premise excludes a classical state space, while
K01 tests how fixed-time measurement compatibility behaves when apparatus
variables are included. The later dynamical step must still locate action
units, positivity and universality. [The coherent-path comparison](checkerboard-dynamics.md)
and [B01 source coverage](../references/batches/B01.md) define the starting
point; the reconstruction proofs have not yet received a full repository audit.

**The spectral route requires control of all slow modes.** For a finite
irreducible reversible generator, put $A=-Q$ on its centered Hilbert space and
$\chi(f)=\langle f,A^{-1}f\rangle$. If an observable collection satisfies

$$\sum_a|\langle f_a,g\rangle|^2\ge\alpha\|g\|^2,\qquad
S=\sum_a\chi(f_a)<\infty,\qquad\alpha>0,$$

then its relaxation gap obeys $\gamma\ge\alpha/S$ (C042). For velocity-unit
observables, alpha has speed-squared units, S has length-squared/time units,
and gamma has inverse-time units. The proof applies
the coverage inequality to a slowest eigenvector. A single positive action
plateau can miss that vector; C041 and C045 exhibit closing gaps with a fixed
plateau. Full rank at each parameter is insufficient when calibration becomes
arbitrarily weak. Independent product dynamics control mixed modes (C046).

G03 asks for an interaction estimate preserving a gap uniformly as system size
increases. The observable coverage and response constants must also be
controlled; a finite-dimensional trace bound can deteriorate with size.
The [susceptibility proof](susceptibility-gap.md) records the exact hypotheses.

A Yang–Mills application additionally needs the physical Hamiltonian and
quantum theory, gauge-invariant observables, and continuum and infinite-volume
control. An auxiliary sampling clock can change a relaxation gap without
changing the invariant law. The [field-theory comparison](comparison-and-bridges.md)
keeps these operator and time identifications explicit. Neither a positive
classical action observable nor a toy relaxation gap supplies that construction.

## 6. Evidence map and next decisions

| Consolidated argument | Claims and written proof | Inherited source/proof audits |
| --- | --- | --- |
| Vanishing variation and mechanical contraction | C002, C056–C058; section 2 links | B05, B30, B31 |
| Conditional excitation, composition and Kepler bounds | C035–C036, C052–C053, C060–C061; section 3 links | B16, B27–B28, B32 |
| Preparation and records | C068–C069, C090–C123; section 4 links and ledger | B37, B48–B66 |
| Coherent versus probabilistic path rules | C039–C040; checkerboard note | B18 |
| Slow modes, calibrated coverage and product control | C041–C042, C045–C046; susceptibility note | B20, B22 |

Q01's [premise map](quantum-exclusion-premises.md) identifies reversible
pure-state connectivity and purification as distinct classical-exclusion
premises ([B67](../references/batches/B67.md)). Hardy's moving-ball example
motivates the next quantum question: exact operational closure during
transformations, with action identification still separate. G03's interacting
size-uniform gap test is selected next in [STATE](../research/STATE.md).
