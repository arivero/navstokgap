# The two Millennium problems

Checked against the official Clay documents on 2026-09-05.
These are compact mathematical restatements; the linked originals govern details.

## Navier–Stokes: existence and smoothness

Source: [Charles L. Fefferman, pp. 1–2, equations (1)–(11), alternatives A–D](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).

For viscosity $\nu>0$, velocity $u$, pressure $p$, and prescribed force $f$:

$$
\partial_tu+(u\cdot\nabla)u=\nu\Delta u-\nabla p+f,
\qquad \nabla\cdot u=0,
\qquad u(x,0)=u_0(x).
$$

There are three spatial dimensions and $t\geq0$. Initial velocity is smooth and divergence-free.

**Whole space:** $x\in\mathbb R^3$. For every spatial multi-index $\alpha$ and nonnegative integers $m,K$, require finite constants with

$$
|\partial_x^\alpha u_0(x)|\leq C_{\alpha K}(1+|x|)^{-K},
\qquad
|\partial_x^\alpha\partial_t^m f(x,t)|
\leq C_{\alpha mK}(1+|x|+t)^{-K}.
$$

An admissible global solution has smooth $u,p$ and uniformly bounded energy:

$$
\sup_{t\geq0}\int_{\mathbb R^3}|u(x,t)|^2\,dx<\infty.
$$

**Periodic case:** $u_0,f,u$ are unit-periodic spatially; $u,p$ are globally smooth. Replace the decay assumptions by smooth periodic $u_0$ and

$$
|\partial_x^\alpha\partial_t^m f(x,t)|\leq C_{\alpha mK}(1+t)^{-K}.
$$

Proving any one alternative suffices:

| Alternative | Domain | Required conclusion |
| --- | --- | --- |
| A | Whole space | Every admissible $u_0$, with $f=0$, admits a global solution above. |
| B | Periodic | Every admissible $u_0$, with $f=0$, admits a global solution above. |
| C | Whole space | Some admissible $u_0,f$ admit no global solution above. |
| D | Periodic | Some admissible $u_0,f$ admit no global solution above. |

Thus breakdown alternatives permit forcing; existence alternatives specify zero forcing.

The forced side is where the current work sits. As of 2026-09-08, finite-time blowup with a
space–time smooth force is proved for the incompressible porous media equation, the 2D inviscid
Boussinesq system and the 3D axisymmetric Euler equations, by the multiscale programme of Córdoba
and Martínez-Zoroa as extended in [B19](../references/batches/B19.md). None of those equations is
Navier–Stokes, so alternatives C and D remain open: they additionally require a viscous term and a
force obeying the decay bound above. A smooth-force hypodissipative Navier–Stokes result is claimed
but unreleased, and a reported internal OpenAI proof of forced Navier–Stokes blowup has no public
artifact. Both stay outside the citable record.

## Yang–Mills: quantum existence and mass gap

Source: [Arthur Jaffe and Edward Witten, §§3–5, pp. 5–7](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).

For every compact simple gauge group $G$, construct a nontrivial quantum Yang–Mills theory on $\mathbb R^4$ with a positive mass gap. Here four dimensions describe spacetime.

**Existence** requires axiomatic strength at least that of the cited Wightman or Osterwalder–Schrader formulations. The physical description includes a Hilbert space $\mathcal H$, Poincaré covariance, positive energy, a vacuum $\Omega$ unique up to phase, and locality, subject to the full axiomatic requirements in the source.

Local quantum observables must correspond, with renormalisation subtleties, to gauge-invariant polynomials in curvature and covariant derivatives. Short-distance correlations must match asymptotic freedom and perturbative renormalisation, including the prescribed stress tensor and operator product behaviour.

**Mass gap:** for the physical Hamiltonian $H$,

$$
H\Omega=0,\qquad H\geq0,\qquad
\operatorname{spec}(H)\cap(0,\Delta)=\varnothing
\quad\text{for some }\Delta>0.
$$

The supremum of such $\Delta$ must be finite: $0<m<\infty$. Thus the lower edge of nonvacuum energies is strictly positive and finite.

The construction concerns the continuum quantum theory in infinite volume.
Confinement and an isolated one-particle state are listed as further questions
beyond the stated existence and mass-gap target.
