# A reversible spin interaction separates identical operational states

Two classical spin preparations have identical first and cross moments, yet
the Hamiltonian interaction H=J u_z v_z gives them different later probabilities
for an allowed product measurement. The hidden dynamics is smooth, complete
and reversible. It therefore supplies an explicit failure of descent to C125's
retained operational state, rather than the reversible gate required by B70.

Q01 mechanical test, 2026-09-13. Keep C125's unit orientations u,v, all joint
Borel preparations and affine local/product terminal measurements. Their
operational state is (1,E[u],E[v],E[u v^T]). Introduce fixed classical angular
momentum magnitudes S_A,S_B>0, with action units, and J>0 with energy units.
These are supplied mechanical parameters, not a selected Planck constant.
Source coverage and written review are in [B72](../references/batches/B72.md).

## 1. The Hamiltonian flow

On S^2 times S^2 use the classical spin Poisson brackets

$$\{u_i,u_j\}=S_A^{-1}\epsilon_{ijk}u_k,\quad
\{v_i,v_j\}=S_B^{-1}\epsilon_{ijk}v_k,\quad
\{u_i,v_j\}=0,\qquad H=J u_z v_z. \tag{1}$$

The convention is dot f={f,H}. In particular,

$$\dot u_x=-\Omega_A u_y v_z,\quad
\dot u_y=\Omega_A u_x v_z,\quad \dot u_z=0,
\qquad\Omega_A=J/S_A,$$
$$\dot v_x=-\Omega_B v_y u_z,\quad
\dot v_y=\Omega_B v_x u_z,\quad \dot v_z=0,
\qquad\Omega_B=J/S_B. \tag{2}$$

The sphere norms and H are conserved. This smooth vector field on a compact
phase space has a complete flow with inverse obtained by changing t to -t.
It is an interaction: each rotation frequency depends on the other spin.
Time is the specified Hamiltonian evolution time; Omega has inverse-time units.

## 2. An exact same-moment pair

Let e_x,e_y,e_z be the standard unit vectors and prepare

$$\mu_A=\delta_{e_y}(du)\,
\tfrac12(\delta_{e_z}+\delta_{-e_z})(dv),\qquad
\mu_B=\delta_{e_y}(du)\,
\tfrac12(\delta_{e_x}+\delta_{-e_x})(dv). \tag{3}$$

Both have E[u]=e_y, E[v]=0 and E[u v^T]=0. They are therefore exactly
equivalent for all C125 terminal tests, including mixed and coarse-grained
product tests. Their microscopic energies are also identically zero.

Since u_z=0 remains zero, v is constant. For mu_A, write v=sign e_z:

$$u(t)=(-\mathrm{sign}\sin(\Omega_A t),
\cos(\Omega_A t),0),\qquad
E_{\mu_A}[u_x(t)v_z(t)]=-\sin(\Omega_A t). \tag{4}$$

For mu_B, v_z=0, so u(t)=e_y and E_muB[u_x(t)v_z(t)]=0.
The allowed product effect e(u,v)=(1+u_x)(1+v_z)/4 consequently gives

$$p_A(t)=\tfrac14[1-\sin(\Omega_A t)],\qquad
p_B(t)=\tfrac14. \tag{5}$$

For every sufficiently small positive t these differ. No map, linear or
otherwise, from the retained initial operational state to the retained state
at such a time can represent this Hamiltonian on all admitted preparations.
Both evolved preparations still yield valid minimal-composite states; the
failure is single-valued evolution on the quotient, not state positivity.

## 3. The missing moment and the implication for reconstruction

Equations (2) expose the additional information immediately:

$$\frac{d}{dt}E[u_xv_z]=-\Omega_A E[u_yv_z^2]. \tag{6}$$

The right-hand side equals -Omega_A for mu_A and zero for mu_B at t=0.
C125 retained E[u_i v_j] but not this moment quadratic in v. Adding the
interaction to the allowed transformation toolbox therefore changes the
operational equivalence relation: its precomposed terminal measurement now
distinguishes the two preparations.

This is consistent with B70's theorem. That theorem assumes a reversible
linear action on the fixed operational tensor state space. Here the classical
interaction has a reversible action on hidden measures but fails to induce
even a single-valued action on that fixed quotient. Physical interaction and
operational reversible closure are distinct premises.

The decisive remaining choice is to justify a preparation/effect restriction
stable under physical interactions, or to enlarge the retained state space.
A separate argument must show that such a repair remains finite-capacity and
locally tomographic before importing B70. Exact Hamiltonian reversibility alone
does not establish that repair. The fixed S_A,S_B supply action units to this
example; none of the moment calculations forces a nonzero universal value.
