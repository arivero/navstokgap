# Exact apparatus energy leaves a receiver-sign ambiguity

Knowing both initial receiver energy and initial apparatus energy still permits
two distinct receiver states with identical complete final apparatus records.
For every sufficiently small positive coupling, a backward-flow construction
gives an antipodal receiver pair inside the preparation box. The clock and
both energy records agree exactly; both canonical reconstruction risks stay
positive as coupling decreases at fixed preparation width.

R26, 2026-09-12. Retain R06/R25's finite apparatus and smooth coordinate
interaction, fixed positive receiver energy E and observation time T. Let
H_0=M_c v_0^2/2 be the nominal initial apparatus kinetic energy. All incoming
apparatus coordinates are unknown within a fixed positive box about nominal
clock phase and zero probe phase. Require exactly H_app=H_0, in addition to
H_s=E. Pulse supports are absent at both endpoints. The record consists of
all ten final apparatus coordinates and the two initial energies. Source
coverage is in [B57](../references/batches/B57.md).

## 1. Reverse a terminal state with zero probe phase

Let z_* be any receiver shell point and Phi_T its free evolution. Prescribe
terminal data

$$z(T)=r\Phi_Tz_*,\quad q(T)=\pi(T)=0,\quad
s(T)=s_0+v_0T,$$
$$p_s(T)=\sqrt{2M_c[H_0+E(1-r^2)]}. \tag{1}$$

For r near 1 the square root is positive. Terminal total energy is exactly
E+H_0 and the interaction is zero. Evolve the exact autonomous Hamiltonian
backward for time T and denote its initial receiver state Z_lambda(r).
Smooth finite-time dependence gives Z_0(r)=r z_*. Hence

$$\partial_r[H_s(Z_0(r))-E]_{r=1}=2E>0.$$

The implicit-function theorem provides a smooth r_lambda near 1 such that

$$H_s(Z_\lambda(r_\lambda))=E. \tag{2}$$

At the resulting initial point all pulse supports are absent, by continuity
of the strict free endpoint margin. Conservation of the total energy E+H_0
then gives H_app=H_0 exactly. Thus (2) imposes one energy and (1) plus
conservation imposes the other; neither is merely an asymptotic equality.

## 2. Bounds and preparation margins

On the backward interval, terminal zero probe coordinates and momenta imply
q,pi=O(lambda). The receiver and clock reaction forces contain lambda q,
so their deviations from the corresponding free paths are O(lambda squared).
These bounds hold with r derivatives on a fixed small r interval, by the
smooth variational equations and finite-time estimates. Therefore

$$r_\lambda=1+O(\lambda^2),\qquad
Z_\lambda(r_\lambda)=z_*+O(\lambda^2),$$
$$p_s(T)=M_cv_0+O(\lambda^2). \tag{3}$$

Initial probe phase differs from zero by O(lambda) and initial clock phase
differs from (s_0,M_c v_0) by O(lambda squared). In fixed component units
there is C with ||a(0)-a_*||<=C lambda. For any sufficiently small fixed
box half-width b>0, take lambda_0 small enough that C lambda_0<=b/2.
Both the box margin and the linear cutoff regions then hold throughout the
whole construction. All masses, durations and pulse widths stay fixed.

The energy-constrained preparation is the shell times the intersection of
the apparatus box with H_app=H_0. Interior margin refers to the box, not an
open neighbourhood in the full ten-dimensional apparatus space.

## 3. An exact symmetry makes a second preparation with the same record

Inside the common linear cutoff regions, the involution

$$\mathcal I:(z,q,\pi,s,p_s)\mapsto(-z,-q,-\pi,s,p_s) \tag{4}$$

preserves the Hamiltonian and its equations: receiver and probe forces change
sign, while the clock force contains the invariant products x q_j. The free
energies are quadratic. Global oddness of the cutoff functions is unnecessary;
both trajectories stay in the regions where X(x)=x and R(q)=q.

Apply (4) to the trajectory constructed above. At T its probes are again
exactly zero and its clock phase is unchanged. The complete final apparatus
record is therefore identical. At the initial time the receiver states are
exactly Z_lambda and -Z_lambda, both with energy E. Probe phases reverse sign,
clock phase is unchanged, and apparatus kinetic energy is exactly H_0 for
both. The symmetric preparation box admits both points with the same b/2
margin. This proves an actual pair rather than a dimension or tangent count.

## 4. Canonical risk and limit

Put k_x=a-g^2/d>0 and choose the physical shell point

$$z_*=(x_*,P_*,(g/d)x_*,0),\qquad
x_*=\sqrt{E/k_x},\quad P_*=\sqrt{\mu E}. \tag{5}$$

Here x_*,P_* denote state components, not the fixed component units. Its
potential and kinetic energies are each E/2. Identical records for the
antipodal pair force every deterministic estimator's coordinate risks to obey

$$\epsilon_x\ge |(Z_\lambda)_x|,\qquad
\epsilon_P\ge |(Z_\lambda)_P|,$$
$$\epsilon_x\epsilon_P\ge
 |(Z_\lambda)_x(Z_\lambda)_P|
 \longrightarrow E\sqrt{\mu/k_x}>0 \quad(\lambda\downarrow0). \tag{6}$$

The arrow concerns the displayed lower bound. In particular it is bounded
below by E sqrt(mu/k_x)/4 for sufficiently small positive coupling, by keeping
each coordinate at least half its limiting magnitude. The constant has action
units; no 2 pi normalization is introduced. Neither exact minimax optimality
nor a positive projected area is claimed for this two-point construction.

The scale is set by receiver energy and stiffness/mass. The allowed weak-
coupling regime depends on the positive preparation width. Exact energy
information removes neither the symmetric preparation freedom nor the
resulting global ambiguity. The common record was chosen by terminal zero
probe phase; it need not be R25's originally chosen nominal-record fibre.

Next R27: test whether a known nonzero incoming probe displacement breaks this
sign ambiguity while exact initial energies and full final records remain
supplied. Separate breaking this particular involution from proving global
recovery, and keep the admissible preparation-energy intersection explicit.
