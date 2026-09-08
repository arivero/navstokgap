# I003 in depth: light-cone rigidity, the one intrinsic scale, and the double limit

Tests 2 and 3 of [I003](../ideas/I003-cut-paradox-arrow-obstruction.md), with
the general form of test 1, drafted 2026-09-08 by the independent Claude
Fable 5.1 session. Checks are in
[`scripts/i003_double_limit_checks.py`](../scripts/i003_double_limit_checks.py).
The theorem and its corollaries are working derivations awaiting review and a
prior-art audit; no claim ID is assigned.

**Results.**

1. *Rigidity.* A translation-invariant, strongly continuous contraction
   semigroup on $L^2(\mathbb R;\mathbb C^n)$ whose kernels are supported in
   the light cone $[-ut,ut]$ has symbol $G(k)=G_0+ikG_1$: it is a first-order
   system $\partial_t\psi=-G_1\partial_x\psi+G_0\psi$ with the numerical
   radius of $G_1$ at most $u$. Unitary groups give $G_1=-iA$, $G_0=-iB$ with
   $A,B$ Hermitian and $\|A\|\le u$: the Dirac class of C039. Positivity-
   preserving semigroups give $G_1=-V$ with $V$ real diagonal and $G_0=Q$ a
   Markov generator: the velocity-jump class of C019 and the classical
   checkerboard of the [checkerboard note](checkerboard-dynamics.md). The
   scalar case $n=1$ is [test 1](cut-paradox-two-faces.md).
2. *One scale.* Inside this class the only intrinsic scale is set by the
   commutator of velocity and switching. If $[G_1,G_0]=0$ the evolution is a
   superposition of straight translations: no crossover, no fluctuation, zero
   action coefficient. For two velocity states $\pm u$ the crossover time is
   $\Delta_*=2u/\|[V,Q]\|=1/\lambda$ on the Euclidean side and
   $2u/\|[A,B]\|=1/\omega_0$ on the Lorentzian side, and the action constants
   are $H_*=mu^2/\lambda$ and $K=mc^2/\omega_0$. The obstruction of I003's
   remark 2 is the noncommutativity of velocity and switching; its scale is the
   constant of remark 3.
3. *Double limit.* The window coefficient with position resolution
   $\varepsilon$ has no joint limit as $(\Delta,\varepsilon)\to0$: its iterated
   limits are $0$ and $\infty$, and along the diffusive parabola
   $\varepsilon^2\propto\Delta$ it converges to a value set by the resolution
   rule alone. The genuine coefficient is the plateau reached with
   $\varepsilon\to0$ first and $\Delta$ above $\Delta_*$.
4. *Verdict on remarks 2 and 3.* Remark 3 holds inside the class without
   further premises. Remark 2 holds in two weaker forms, positivity of the
   coefficient if and only if velocity and switching fail to commute, and a
   minimum window $\Delta_*\ge K/(mu^2)$ once $K$ and $u$ are given (C038);
   a minimum value of $K$ itself needs the composition premise of C035–C036.

## 1. The class and the theorem

Let $(T_t)_{t\ge0}$ be a strongly continuous contraction semigroup on
$\mathcal H=L^2(\mathbb R;\mathbb C^n)$ commuting with translations, so that
$T_tf=K_t*f$ for a matrix-valued tempered distribution $K_t$, and suppose
$\operatorname{supp}K_t\subset[-ut,ut]$ for every $t$. Unitary groups are
included by taking $t\ge0$ and their adjoints; symmetric Markov semigroups of
velocity-jump processes are included because Lebesgue measure times counting
measure is invariant for them.

**Theorem.** There are matrices $G_0,G_1$ such that the Fourier symbol of
$T_t$ is $M_t(k)=e^{t(G_0+ikG_1)}$, and the numerical radius of $G_1$ is at
most $u$. If $T_t$ is unitary, $G_1=-iA$ and $G_0=-iB$ with $A,B$ Hermitian
and $\|A\|\le u$. If $T_t$ preserves nonnegative functions, $G_1=-V$ with
$V$ real diagonal and $|V_{jj}|\le u$, and $G_0$ is a Markov generator.
Conversely every such symbol generates a semigroup of the class.

**Proof.** *Symbol.* Translation invariance gives a measurable matrix
multiplier $M_t(k)$ with $\|M_t(k)\|\le1$, $M_{s+t}=M_sM_t$ and
$M_t\to I$ strongly. The Paley–Wiener–Schwartz theorem extends $M_t$ to an
entire matrix function with $\|M_t(k)\|\le C_t(1+|k|)^{N_t}e^{ut|\operatorname{Im}k|}$;
on the real axis the contraction bound holds everywhere by continuity.

*Bernstein.* For unit vectors $v,w$ the entry $\psi(k)=\langle v,M_t(k)w\rangle$
is entire of exponential type at most $ut$ and bounded by one on $\mathbb R$.
Bernstein's inequality gives $|\psi^{(j)}(x)|\le(ut)^j$ on $\mathbb R$, so the
numerical radius of $\partial_kM_t(x)$ is at most $ut$ and that of
$\partial_k^2M_t(x)$ at most $(ut)^2$, up to a factor depending only on $n$
for the second.

*Generator.* At each real $x$ the map $t\mapsto M_t(x)$ is a bounded
measurable one-parameter semigroup of matrices, hence $M_t(x)=e^{tG(x)}$ with
$G(x)$ dissipative. Since $M_t(x)$ is real-analytic in $x$ and tends to $I$
as $t\downarrow0$, the principal logarithm gives $G$ real-analytic on
$\mathbb R$.

*First order.* Duhamel's formula
$\partial_x e^{tG}=t\int_0^1e^{stG}G'e^{(1-s)tG}\,ds$ and the bound on
$\partial_kM_t$ give, after dividing by $t$ and letting $t\downarrow0$, a
numerical radius of $G'(x)$ at most $u$. Differentiating once more,
$\partial_x^2e^{tG}=t\int_0^1e^{stG}G''e^{(1-s)tG}\,ds+t^2R_t$ with
$\|R_t\|\le c_n\|G'(x)\|^2$, so
$t\,\|G''(x)\|\le c_n(ut)^2+t^2\|R_t\|+o(t)$ and $G''\equiv0$. Thus
$G(x)=G_0+xG_1$ with $G_1=G'(0)$, and the symbol is $e^{t(G_0+ikG_1)}$; the
factor $i$ is the Fourier convention for $-\partial_x$.

*Unitary and Markov forms.* For a unitary group $G$ is anti-Hermitian on
$\mathbb R$, so $G_1=-iA$, $G_0=-iB$ with $A,B$ Hermitian, and the numerical
radius of a Hermitian matrix is its norm. For a positivity-preserving
semigroup the kernel is real and nonnegative; applying $T_t$ to a step
function in one component, the off-diagonal first-order part
$-(G_1)_{jl}\partial_x$, $j\ne l$, would produce a signed measure at the
edges, so $G_1$ is diagonal, and conservation of mass makes $G_0$ a Markov
generator on the components.

*Converse.* For Hermitian $A$ the system
$\partial_t\psi=-A\partial_x\psi-iB\psi$ is symmetric hyperbolic with
propagation speed $\|A\|$, and a velocity-jump process with speeds $V_{jj}$
moves no faster than $\max|V_{jj}|$. $\square$

The Dirac generator of C039, $H(p)=cp\sigma_z+mc^2\sigma_x$, and the
classical generator $A_\lambda=-c\sigma_z\partial_x+\lambda(\sigma_x-I)$ of
the checkerboard note are the two-component instances. The theorem says they
are the only light-cone dynamics with two components, up to the choice of
$B$ or $Q$ and of the velocity eigenvalues.

## 2. The one intrinsic scale

Write $G(k)=G_0+ikG_1$. If $[G_0,G_1]=0$ the two factors commute,
$e^{t(G_0+ikG_1)}=e^{tG_0}e^{iktG_1}$, and in the eigenbasis of $G_1$ the
evolution is a superposition of translations at the eigenvelocities, each
multiplied by a phase or a decay. No component ever changes velocity: the
paths are straight, the position variance grows quadratically, and the action
coefficient $m\operatorname{Var}(\Delta X)/\Delta$ is zero at every window in
the Euclidean face, while in the Lorentzian face the dispersion is affine and
massless. In the two-state case with $G_1=\mp iu\sigma_z$ this is exactly the
statement that $Q$ or $B$ is diagonal, and a diagonal Markov generator is zero.

When the commutator is nonzero the class has one intrinsic inverse time. For
the two-state generators,

$$\|[u\sigma_z,\lambda(\sigma_x-I)]\|=2u\lambda,\qquad
\|[u\sigma_z,\omega_0\sigma_x]\|=2u\omega_0,$$

so $\lambda=\|[V,Q]\|/(2u)$ and $\omega_0=\|[A,B]\|/(2u)$ are basis-free.
The crossover time is $\Delta_*=2u/\|[\,\cdot\,,\cdot\,]\|$, the crossover
length $u\Delta_*$, and the action constants are

$$H_*=\frac{mu^2}{\lambda}=\frac{2mu^3}{\|[V,Q]\|},\qquad
K=\frac{mc^2}{\omega_0}=\frac{2mc^3}{\|[A,B]\|}.$$

Below $\Delta_*$ the motion is ballistic in both faces, above it the Euclidean
face is diffusive with coefficient $H_*$ (C020) and the Lorentzian face is
Schrödinger-like with action $K$ (C039, §4 of the checkerboard note). The
scales $\Delta_*=\hbar/(mc^2)$ and $u\Delta_*=\hbar/(mc)$ of the P02 note are
this commutator scale with $K=\hbar$. This is the precise content of I003's
remark 1: the cone's adjacent sections and the arrow's adjacent instants are
equal to leading order, unequal at order $\Delta$, and the ratio of the
unequal part to $\Delta$ is the switching generator, whose failure to commute
with velocity is the whole of the physics below the plateau.

## 3. The double limit

Let $X$ be a Lipschitz-$u$ process with stationary increments and window
coefficient $\mathsf h(\Delta)=m\operatorname{Var}(X(t+\Delta)-X(t))/\Delta$,
and let positions be read on a lattice of spacing $\varepsilon$ with
independent uniform rounding errors, which add $\varepsilon^2/6$ to the
increment variance. The observed coefficient is

$$\mathsf h_\varepsilon(\Delta)=\mathsf h(\Delta)+\frac{m\varepsilon^2}{6\Delta}.$$

Its iterated limits differ: $\varepsilon\to0$ then $\Delta\to0$ gives zero by
C018, while $\Delta\to0$ then $\varepsilon\to0$ gives infinity. Along the
diffusive parabola $\varepsilon^2=6\kappa_0\Delta/m$ the limit is $\kappa_0$,
a number fixed by the resolution rule and unrelated to the dynamics; along the
ballistic diagonal $\varepsilon=u\Delta$ the limit is zero. Hence “mapping
time to positions indefinitely as a double limit” is obstructed twice: by the
speed bound, which kills the dynamical coefficient below $\Delta_*$, and by
the resolution term, which manufactures a spurious coefficient if the
resolution is refined diffusively with the window. The genuine coefficient is
the plateau obtained with $\varepsilon\to0$ first and $\Delta\gg\Delta_*$,
and the crossover function $g$ of C037 describes how it is approached.

Removing the speed bound removes the first obstruction: the Gaussian family of
C009–C011 has $\mathsf h\equiv\kappa$ at every window, so the ordered limit
exists at every scale. Finite speed is therefore the source of the obstruction,
as I003's test 2 asked, and the rigidity theorem shows that finite speed with
a nonzero coefficient forces the first-order two-component structure in which
the obstruction sits at the commutator scale.

## 4. Remarks 2 and 3 with their premises

| Statement | Holds | Premises used |
| --- | --- | --- |
| An $h$ controls the convergence (remark 3) | Yes, inside the class | Finite speed, finitely many components, translation invariance; the constant is $2mu^3/\|[G_1,G_0]\|$ |
| Positivity of the coefficient | If and only if $[G_1,G_0]\ne0$ | Same, plus a nonzero velocity variance |
| A minimum window and length | Yes: $\Delta_*\ge K/(mu^2)$ | A prescribed positive $K$ and the speed bound (C018, C031, C038) |
| A minimum $h$ forced (remark 2) | Only as a common value | Composition invariance and a positive reference (C035–C036); the value itself stays a parameter |

Two premises are external to the class. The identification $K=\hbar$ is a
unit choice for the Hermitian switching matrix, and the mass law
$\omega_0=mc^2/\hbar$ is C020's universality law read in the Lorentzian face.
Both remain the A08 and A09 obligations; this note fixes where in the
mathematics they enter.

## 5. Prior art to audit

- D'Ariano and Perinotti, Phys. Rev. A 90, 062106 (2014): the Dirac equation
  from unitarity, locality, homogeneity and isotropy of a quantum cellular
  automaton, with a mass bounded by the lattice scale. The theorem above is
  the continuum, one-dimensional, finitely-many-components analogue with the
  light cone in place of the lattice.
- Bisio, D'Ariano and Tosini, Ann. Phys. 354, 244 (2015), the one-dimensional
  Dirac automaton; metadata from memory, to verify.
- Feynman and Hibbs (1965) §7-3, pp. 176–177: quantum paths are continuous
  and nowhere differentiable, with $(\Delta x)^2$ of order $\hbar\Delta t/m$;
  Abbott and Wise, Am. J. Phys. 49, 37 (1981): Hausdorff dimension two. These
  are the diffusive branch above $\Delta_*$.
- Jacobson and Schulman (1984), B15: the passage from $\Delta x\sim\Delta t$
  to $(\Delta x)^2\sim\Delta t$ at the Compton scale, which §3 derives inside
  the class.
- Bernstein's inequality for entire functions of exponential type (Boas,
  *Entire Functions*, 1954) and the Paley–Wiener–Schwartz theorem
  (Hörmander, vol. I, Theorem 7.3.1); finite propagation speed for symmetric
  hyperbolic systems (Friedrichs 1954). The rigidity theorem is assembled from
  these standard tools and may itself be standard; the audit should search
  for characterizations of finite-propagation translation-invariant
  semigroups as first-order systems.

## 6. Checks and next steps

The script verifies the commutator norms and the two crossover formulas, the
factorization and straight-line motion in the commuting case, the Dirac and
telegraph symbols as instances of the affine class with entire entries, the
Bernstein bound on a Dirac entry over a grid, the Duhamel first-order identity
on a two-state example by comparison with finite differences, the rounding
model's iterated and path limits, and the Gaussian control case. Next: an
adversarial review of the theorem's measure-theoretic steps, the prior-art
audit above, and the composition of two affine systems as the A08 test inside
this class.
