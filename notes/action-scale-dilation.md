# Dilation closure and the action-selection obstruction

A class closed under simultaneous contraction of space and time cannot have a
strictly positive lower bound for a finite, positive, degree-one action
observable. For the external-potential models below, contraction preserves mass,
speed and the phase preparation but changes the potential's spatial scale.
This gives A16's precise admissibility test. Proof and literature status are
recorded in the claim ledger and B30 companion.

## 1. The mechanical map

Fix a mass m>0 and either T(p)=|p|²/(2m) or
T(p)=sqrt(m²c⁴+c²|p|²), with fixed c>0 in the second case. On an open
configuration domain D, take H(q,p)=T(p)+V(q), V in C²(D). For a solution
(q(t),p(t)) and a dimensionless a>0 define

$$D_a=aD,\quad V_a(Q)=V(Q/a),\quad
q_a(t)=a q(t/a),\quad p_a(t)=p(t/a).$$

The transformed Hamiltonian is H_a(Q,P)=T(P)+V_a(Q). Direct differentiation
proves Hamilton's equations:

$$\dot q_a=\nabla T(p_a),\qquad
\dot p_a=-a^{-1}\nabla V(q_a/a)=-\nabla V_a(q_a).$$

The solution interval is multiplied by a. Each fixed a>0 preserves smoothness
on its transformed domain, boundedness of an orbit, and completeness of a
complete trajectory. Velocity and energy values are unchanged; momentum force
and acceleration are multiplied by 1/a. This is an exact map between models,
with physical coordinates measured in the same units. It is not merely a change
of units. Its phase-space map F_a(q,p)=(aq,p) obeys
F_a^*(sum dQ_i wedge dP_i)=a sum dq_i wedge dp_i: it is conformally symplectic,
and symplectic only at a=1. Thus A15's symplectic invariance does not prohibit it.

For an invariant probability preparation mu, let mu_a=(F_a)_*mu.
The flow identity phi_a^t F_a=F_a phi^(t/a) proves invariance of mu_a.
Uniform circular phase, independence of separately transformed subsystems,
and qualitative decay of correlations survive. A correlation evaluated at t
is its original counterpart at t/a; a prescribed dimensional correlation time
need not survive. No claim here establishes a propagating mediator for an
external potential: the speed bound is a bound on the particle trajectory.

## 2. Action and observation windows

For a closed orbit, the normalized canonical action
J=(2 pi)^(-1) integral p dot dq scales as J_a=aJ. For corresponding finite
trajectory segments, the Hamiltonian action also obeys

$$S_a=\int_0^{aT}(p_a\cdot\dot q_a-H_a)dt=aS.$$

For the fixed Cartesian canonical projection Z=(x,p_x), take centered
covariance Sigma with finite second moments and define
A_cov=2 sqrt(det Sigma), as in A15. Since Z_a=diag(a,1)Z,

$$\Sigma_a=\operatorname{diag}(a,1)\Sigma\operatorname{diag}(a,1),
\qquad \mathcal A_{{\rm cov},a}=a\mathcal A_{\rm cov}.$$

For invariant position processes, the displacement coefficient satisfies

$$\mathsf h_a(\Delta)=\frac{ma^2}{\Delta}
\operatorname{Var}[x(\Delta/a)-x(0)]
=a\mathsf h(\Delta/a).$$

Hence corresponding windows Delta_a=a Delta give a times the original
response. A finite long-window limit H_* transforms to aH_* by taking
Delta to infinity at fixed a first. This formula does not assert uniformity
in a at a fixed observation window. Every displayed action has units
mass times length squared per time; a is dimensionless.

## 3. Exact closure proposition

Let C be a class of models together with preparations and measurement
conventions. Suppose it contains an element M with 0<A(M)<infinity and, for
arbitrarily small a>0, its transformed element M_a, with A(M_a)=aA(M).
Then

$$\inf\{A(N):N\in C,\ A(N)>0\}=0.$$

Indeed choose a tending to zero along the admitted contractions; every value
aA(M) is positive and converges to zero. If the class additionally requires
one common finite action value K for all its members and contains M and M_a
for any a unequal to one, then K=aK forces K=0. These are elementary
consequences of the stated closure, not assertions that every classical axiom
set has that closure. The infimum concerns a family of classical observables,
not an operator spectral gap or convergence of trajectories to a regular
limiting model. No model at a=0 is required.

## 4. Which premises survive contraction?

| Premise or parameter | Effect under the map | Closure consequence |
| --- | --- | --- |
| Fixed mass and particle speed ceiling | Unchanged | Do not obstruct contraction |
| Fixed energy value and potential depth | Unchanged | Do not obstruct this map |
| Smooth potential for each model | Preserved on aD | Does not provide a uniform derivative bound |
| Uniform circular phase, stationary ensemble | Pushed forward unchanged in phase | Does not select a positive action |
| Nonzero orbital size | Radius becomes aR>0 | Positivity alone allows infimum zero |
| Uniform force or acceleration ceiling | Actual force/acceleration grows as 1/a | Can exclude this contraction of a nontrivial orbit |
| Fixed length, time, density or coupling | Generally changes | Must be tested in the specified model |

For V(r)=-k/r, V_a(r)=-ak/r: k_a=ak and the singular Kepler threshold becomes
k_a/c=a k/c. The transformation therefore does not close the fixed-k class.
For V(r)=-k/sqrt(r²+b²), k_a=ak and b_a=ab. The potential depth k/b is
unchanged. C053 supplies a separate zero-infimum family even with k,b fixed;
it does not rely on dilation closure. For V(r)=k_s r²/2, k_{s,a}=k_s/a²,
so the circular frequency becomes omega/a. These substitutions make the
coupling premise explicit.

Breaking this particular closure is necessary for a uniform positive bound
on a class containing one positive finite observable. It is not sufficient:
A15's point-phase preparation still has zero covariance, and the fixed
softened core has positive orbital actions approaching zero. A quantitative
force bound, a fixed coupling and preparation restrictions need a new bound
in their own admissible class.

## 5. Next bounded test

A17 should hold a dimensional force ceiling fixed and test small-radius
uniform-phase circles in a fixed smooth confining potential. Determine by a
written estimate whether their positive canonical actions still approach zero,
then state the extra lower energy, radius or preparation premise needed to
exclude the family. This tests a concrete way of breaking the dilation map
without assuming a positive action as calibration.

Source-to-task capsule: B29's covariance determinant supplies the observable;
the linear pushforward rule supplies its contraction law. A15 used determinant
one maps within an orbit; A16 uses determinant a between Hamiltonians. The
physical question is closure of the admissible model and preparation class.
