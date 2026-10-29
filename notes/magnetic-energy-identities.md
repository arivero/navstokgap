# Two exact identities for the magnetic energy, a ground-state sum rule, and why pointwise Gibbs domination fails as Agmon does

The magnetic energy of the Kogut--Susskind Hamiltonian satisfies two
exact relations on the configuration space $G^{\mathcal E}$:
$$\Delta V=4C_2\big(N|\mathcal P|-V\big),
\qquad
\big|\nabla V\big|^2\ \le\ 16\,V\quad(SU(2)),$$
the first because $V-N|\mathcal P|$ is an eigenfunction of the
Laplace--Beltrami operator with eigenvalue $-4C_2$, the second from the
completeness relation together with
$\sin^2\theta=(1-\cos\theta)(1+\cos\theta)$. They give an exact sum rule
for the ground state,
$$A'\!\int\!\big(V-N|\mathcal P|\big)\big|\nabla\Omega\big|^2d\mu
+A'\big(2C_2-K\big)\big\langle V-N|\mathcal P|\big\rangle
+B'\operatorname{Var}_\Omega(V)=0,
\qquad K=\!\int\!|\nabla\Omega|^2,$$
and give a sufficient positivity region for the comparison function
$\varphi=e^{-\lambda V/2}$. Its threshold and prefactor depend on total
ground energy and global normalization data. This supplies no
volume-uniform local bound. The limitation concerns these particular
comparison functions; it is not an impossibility theorem for Gibbs
domination or every use of the eigenvalue equation.

Fix a finite periodic three-dimensional spatial cubic lattice with
four distinct links per plaquette. Use normalized product Haar measure,
the product bi-invariant metric with
$\operatorname{tr}(T^aT^b)=\delta^{ab}/2$, and
$V=\sum_p(N-\operatorname{Re}\operatorname{tr}U_p)$. Set
$A'=g^2/2$, $B'=2/g^2$ and
$H=(\hbar c/a)[A'(-\Delta)+B'V]$. The smooth positive ground state
$\Omega$ is normalized by $\int\Omega^2d\mu=1$ and satisfies
$[A'(-\Delta)+B'V]\Omega=e_0\Omega$; its finite-lattice existence and
simplicity are [T1](mass-gap-obligations-lattice.md). The Laplacian
identity extends to other four-distinct-link geometries; the numerical
gradient estimate below uses the stated spatial incidence.

## 1. The Laplacian of the magnetic energy

**Proposition 1.** On $\mathcal M=G^{\mathcal E}$ with the product
bi-invariant metric,
$$\Delta V=4C_2(R_{\rm f})\big(N|\mathcal P|-V\big),$$
where $C_2(R_{\rm f})$ is the quadratic Casimir of the defining
representation. Equivalently $W=V-N|\mathcal P|$ satisfies
$\Delta W=-4C_2W$: the magnetic energy, shifted by its Haar mean, is an
eigenfunction of the Laplacian.

*Proof.* Fix a plaquette $p$ and one of its four links $\ell$. Writing
$\operatorname{tr}U_p=\sum_{ab}(U_\ell)_{ab}M_{ba}$ with $M$ the ordered
product of the other three links, each matrix element of $U_\ell$ in the
defining representation is an eigenfunction of $\Delta_\ell$ with
eigenvalue $-C_2(R_{\rm f})$, by Peter--Weyl. Hence
$\Delta_\ell\operatorname{tr}U_p=-C_2\operatorname{tr}U_p$, and summing
over the four links of $p$,
$\Delta\operatorname{Re}\operatorname{tr}U_p=-4C_2\operatorname{Re}\operatorname{tr}U_p$.
Summing over plaquettes,
$\Delta V=\Delta\sum_p(N-\operatorname{Re}\operatorname{tr}U_p)
=4C_2\sum_p\operatorname{Re}\operatorname{tr}U_p=4C_2(N|\mathcal P|-V)$. $\square$

## 2. The gradient of the magnetic energy

**Proposition 2.** On the periodic three-dimensional spatial cubic lattice
with four plaquettes per link, for $SU(2)$, $|\nabla V|^2\le16\,V$ pointwise on
$\mathcal M$. For general $SU(N)$, $|\nabla V|^2\le16\,N\,V$.

*Proof.* For one link of one plaquette, the completeness relation of
[the upper-bound note](lattice-gap-upper-bounds.md) Corollary 2 gives
$$\sum_a\big|X^\ell_a\operatorname{tr}U_p\big|^2
=\tfrac12\Big[\operatorname{tr}(MM^\dagger)-\tfrac1N\big|\operatorname{tr}M\big|^2\Big]
=\tfrac12\Big[N-\tfrac1N\big|\operatorname{tr}U_p\big|^2\Big].$$
For $SU(2)$, writing $\operatorname{tr}U_p=2\cos\theta$, this is
$1-\cos^2\theta=\sin^2\theta=(1-\cos\theta)(1+\cos\theta)$, while
$V_p=2-2\cos\theta$, so
$$\big|\nabla_\ell\operatorname{Re}\operatorname{tr}U_p\big|^2
\le\sin^2\theta=\frac{V_p}2\Big(2-\frac{V_p}2\Big)\le V_p .$$
Each link lies in four plaquettes, so by Cauchy--Schwarz
$|\nabla_\ell V|^2\le4\sum_{p\ni\ell}V_p$, and summing over links, with
four links per plaquette,
$|\nabla V|^2\le4\sum_\ell\sum_{p\ni\ell}V_p=16\sum_pV_p=16V$. The
general case replaces the bound $\sin^2\theta\le V_p$ by
$\tfrac12[N-|\operatorname{tr}U_p|^2/N]\le NV_p$, which follows from
$|\operatorname{tr}U_p|\ge N-V_p$ when $V_p\le N$ and from the trivial
bound otherwise. $\square$

Both identities vanish at $U_p=1$: a configuration with no magnetic
energy has no magnetic gradient, as it must.

## 3. An exact ground-state sum rule

**Proposition 3.** With $W=V-N|\mathcal P|$, $K=\int|\nabla\Omega|^2d\mu$,
$\langle\cdot\rangle=\langle\Omega,\cdot\,\Omega\rangle$ and
$\operatorname{Var}_\Omega(V)=\langle V^2\rangle-\langle V\rangle^2$,
$$A'\!\int W\big|\nabla\Omega\big|^2d\mu
+A'\big(2C_2-K\big)\langle W\rangle
+B'\operatorname{Var}_\Omega(V)=0 .$$

*Proof.* Multiply $-A'\Delta\Omega+(B'V-e_0)\Omega=0$ by $W\Omega$ and
integrate. Since
$$\int W\Omega\,\Delta\Omega=-\int W|\nabla\Omega|^2-\int\Omega\,\nabla W\!\cdot\!\nabla\Omega,$$
$$\int\Omega\,\nabla W\!\cdot\!\nabla\Omega=-\tfrac12\int(\Delta W)\Omega^2=2C_2\langle W\rangle,$$
by Proposition 1, so $\int W\Omega\Delta\Omega=-\int W|\nabla\Omega|^2-2C_2\langle W\rangle$
and the equation becomes
$A'\int W|\nabla\Omega|^2+2A'C_2\langle W\rangle+B'\langle VW\rangle-e_0\langle W\rangle=0$.
Now $e_0=A'K+B'\langle V\rangle=A'K+B'(\langle W\rangle+N|\mathcal P|)$
and $\langle VW\rangle=\langle W^2\rangle+N|\mathcal P|\langle W\rangle$,
so the last two terms combine into
$-A'K\langle W\rangle-B'\langle W\rangle^2+B'\langle W^2\rangle$. $\square$

The sum rule ties the magnetic variance of the ground state to its
kinetic energy and to the correlation between magnetic energy and
kinetic density. At $g\to\infty$ every term vanishes with $B'$, and at
finite coupling it is one exact constraint on the ground-state measure.

## 4. Pointwise Gibbs domination and where it stops

Try $\varphi=e^{-\lambda V/2}$, $\lambda>0$, as a comparison function for
$L=-A'\Delta+(B'V-e_0)$. Using
$\Delta\varphi=\varphi[\tfrac{\lambda^2}4|\nabla V|^2-\tfrac\lambda2\Delta V]$
and Propositions 1--2,
$$\frac{L\varphi}{\varphi}
=B'V-e_0-A'\frac{\lambda^2}4|\nabla V|^2+A'\frac\lambda2\Delta V
\ \ge\ \Big[B'-4A'\lambda^2-2A'\lambda C_2\Big]V
+\Big[2A'\lambda C_2N|\mathcal P|-e_0\Big],$$
for $SU(2)$, using $|\nabla V|^2\le16V$ and Proposition 1.

**Proposition 4.** If $\lambda$ satisfies $B'>4A'\lambda^2+2A'\lambda C_2$,
then $L\varphi\ge0$ on $\{V\ge V_*\}$ with
$$V_*=\frac{\big(e_0-2A'\lambda C_2N|\mathcal P|\big)_+}{B'-4A'\lambda^2-2A'\lambda C_2},$$
and the maximum principle gives
$$\Omega(U)\ \le\ \Big(\max_{\{V\le V_*\}}\frac{\Omega}{\varphi}\Big)\,e^{-\lambda V(U)/2}
\qquad\text{for all }U .$$

*Proof.* Set $u=\Omega/\varphi$. From $L\Omega=0$,
$0=-A'\varphi\Delta u-2A'\nabla u\!\cdot\!\nabla\varphi+u\,L\varphi$. At an
interior maximum of $u$ one has $\nabla u=0$ and $\Delta u\le0$, so the
first two terms are $\ge0$ and $u\,L\varphi\le0$; since $u>0$, the
maximum lies in $\{L\varphi\le0\}\subset\{V\le V_*\}$. $\square$

**Where it stops.** With $e_0\le B'N|\mathcal P|$, the threshold obeys
$$V_*\ \le\ N|\mathcal P|\;\frac{B'-2A'\lambda C_2}{B'-4A'\lambda^2-2A'\lambda C_2}
\ \xrightarrow[\lambda\to0]{}\ N|\mathcal P| ,$$
This is an upper bound on the threshold, not a proof that its actual
value is asymptotic to the Haar mean. The resulting comparison uses a
constant determined on the global sublevel $\{V\le V_*\}$. A local event
need not force a global excess. No volume-uniform local probability
estimate follows from the available bounds on that threshold and
normalization constant, as in
[the Agmon argument](agmon-ground-state-suppression.md).

## 5. Global comparisons and local probability

The two comparisons use the eigenvalue equation
$-A'\Delta\Omega+(B'V-e_0)\Omega=0$ and its total ground energy.
The weighted identity and exponential trial function control global
potential excess. Their failure to prove local suppression does not
exclude a different Hamiltonian argument.

The Wilson density $e^{-S_w}=\prod_pe^{-(2/g_E^2)V_p}$ prices an action
change locally, but shared links and the partition function prevent
this unnormalized factorization from being a probability theorem.
The [slice representation](ground-state-measure-transfer.md) is a
different exact identity at fixed temporal spacing. Passing to the
Hamiltonian requires convergence of the ground-state projectors;
transferring a local bound requires the same anisotropic slice
observable and constants uniform in all claimed limits.

## 6. Consequence for STATE

The exact Laplacian/gradient identities and sum rule survive, with
the setting above and the periodic three-dimensional plaquette incidence
used in the gradient proof. Proposition 4 gives the stated global
comparison; it neither proves nor disproves every possible Gibbs
domination bound. The [Agmon tail](agmon-ground-state-suppression.md)
also controls a global excess with finite-volume constants.

No normalized interacting local suppression
$C e^{-c\eta^2/g^2}$ follows from either eigenfunction comparison,
plaquette action factorization or the slice identity alone. The missing
local probability and signed operator estimates remain separate.
