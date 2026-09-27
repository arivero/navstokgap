# A Lorentz-invariant background fixes the state-route constant to the radiation unit

**Result, 2026-09-27.** STATE item 2 asked for a physical reason why the
constant $\zeta$ of the state route (GPT-6 Astra's
[routes note](newton-indeterminacy-routes.md), floor with $h_*=2\zeta$; the
[fifth-postulate note](principia-fifth-postulate.md), Theorem B$'$) should
equal a fixed multiple of the radiation unit $h_{\rm rad}$ of Theorem U
([unit-and-indeterminacy note](necessity-unit-and-indeterminacy.md)).
Within stochastic electrodynamics it does:

$$2\zeta=\frac{h_{\rm rad}}{2\pi},\qquad\text{so}\qquad h_*=\frac{h_{\rm rad}}{2\pi}=\hbar .$$

Three steps. (1) A stationary random electromagnetic background that is
Lorentz invariant has energy $\kappa\omega$ per normal mode for one constant
$\kappa$. (2) Every weakly damped linear oscillator in equilibrium with it
has a Gaussian stationary state with $\sqrt{\det\Sigma}=\kappa$, whatever its
mass and frequency (Theorem 1): the background realizes the covariant,
noise-closed Gaussian restriction of Theorem B$'$ with $\zeta=\kappa$, and it
does so universally. (3) With the same background, Boyer derives the
Planck spectrum from classical electrodynamics and classical
thermodynamics, with zero-point energy $\frac12\hbar\omega$ per mode; so
$\kappa=\hbar/2$ and $h_{\rm rad}=2\pi\hbar=4\pi\kappa$. The pure number of Astra's
matching condition $2\zeta=\gamma h_{\rm rad}$ is therefore $\gamma=1/(2\pi)$ in this
theory.

What stays open is Astra's closure premise: that no record, however it
couples to the background, can infer the background's value and so
sharpen the body's state below $\zeta$. Step (2) fixes $\zeta$ for states in
equilibrium with the background; it does not show that records cannot
leave that set. The ingredients are established (Lorentz-invariant
random radiation, Planck's resonator relation, linear response); the
assembly is this note's, with no novelty claimed for the parts.

## 1. The background and the oscillator

**(1) Lorentz invariance fixes the spectrum up to one constant.** A
homogeneous, isotropic, stationary random electromagnetic field whose
spectrum is Lorentz invariant has energy density proportional to
$\omega^3$, that is, energy per normal mode linear in frequency, $\kappa\omega$
([Marshall 1963](https://doi.org/10.1098/rspa.1963.0220), metadata;
[Boyer 1969](https://doi.org/10.1103/PhysRev.182.1374), abstract: "linear
in frequency", $\frac12\hbar\omega$ per normal mode). The constant $\kappa$ has the units of
action, and Lorentz invariance leaves it free.

**Theorem 1 (universal Gaussian area).** Let a particle of mass $M$ and
charge $e$ be bound harmonically at frequency $\omega_0$, with radiation
damping small compared with $\omega_0$, and driven by the background of (1),
taken Gaussian. Its stationary phase-space state is Gaussian with

$$\langle q^2\rangle=\frac\kappa{M\omega_0},\qquad\langle p^2\rangle=\kappa M\omega_0,\qquad
\langle qp+pq\rangle=0,\qquad \sqrt{\det\Sigma}=\kappa ,$$

independent of $M$, $e$ and $\omega_0$.

*Proof.* The equation of motion is linear with Gaussian forcing, so the
stationary state is Gaussian. A weakly damped oscillator in equilibrium
with a radiation field acquires mean energy equal to the field's energy
per normal mode at its frequency (Planck's resonator relation, derived
in classical electrodynamics;
[Planck 1900](https://doi.org/10.1002/andp.19003060105), metadata), here
$\kappa\omega_0$. For a harmonic oscillator the mean kinetic and potential
energies are equal, so $\langle p^2\rangle/(2M)=\frac12M\omega_0^2\langle q^2\rangle=\frac12\kappa\omega_0$,
and stationarity gives $\langle qp+pq\rangle=0$. Then
$\det\Sigma=\langle q^2\rangle\langle p^2\rangle=\kappa^2$. $\square$

The mass and the frequency drop out because the energy per mode is
proportional to $\omega$: the area $\langle E\rangle/\omega_0$ is the same for every
oscillator. That is the universality the dimensional note requires of a
floor (its Theorem A), supplied here by Lorentz invariance of the
background rather than assumed.

**(2) The link to Theorem B$'$.** The set of Gaussian states with
$\sqrt{\det\Sigma}\ge\kappa$ is invariant under the affine symplectic group and
closed under adding noise, and Theorem 1 says the background puts every
harmonically bound body on its lower boundary. So the background
realizes the restriction of Theorem B$'$ with $\zeta=\kappa$, and Astra's
conditional floor applies with $h_*=2\kappa$ to comparisons whose records are
confined to this set.

**(3) The link to the radiation unit.** Boyer derives the Planck law
"without the formalism of quantum theory" from this background, classical
electrodynamics of dipole oscillators, and classical equipartition of the
particles' kinetic energy (Boyer 1969, abstract). The zero-point part is
$\frac12\hbar\omega$ per mode, so $\kappa=\hbar/2$; the thermal part is Planck's, whose
constant is the $h_{\rm rad}=2\pi\hbar$ of Theorem U. Hence

$$2\zeta=2\kappa=\hbar=\frac{h_{\rm rad}}{2\pi}.$$

This rests on Boyer's derivation at abstract level; the thermodynamic
steps of that derivation are not re-derived here.

## 2. Consequence for STATE

STATE item 2 asked for two things: a physical justification of closure
under recording, and the identification $2\zeta=\gamma h_{\rm rad}$. The second
is supplied within stochastic electrodynamics, with $\gamma=1/(2\pi)$: one
Lorentz-invariant constant sets both the equilibrium spectrum of
radiation and the phase-space area of every bound body. The first
remains open. It is now the single premise between a classical,
pre-quantum account (Maxwell, Lorentz invariance, thermodynamics, a
random background) and the Planck paper's floor on recording the
inertial-versus-parabola comparison: that records cannot read the
background and so leave its equilibrium set.
