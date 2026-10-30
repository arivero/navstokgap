# Finite propagation: scalar rigidity, internal states and record limits

Two scalar rigidity statements hold with exact ballistic support. A
probability convolution semigroup on the line supported in $[-ut,ut]$
is deterministic drift. A strongly continuous translation-invariant
unitary group on $L^2(\mathbb R)$ with kernels supported in
$[-u|t|,u|t|]$ is translation at some $|a|\le u$, up to a constant
phase. The proofs below use variance additivity and the imported
Paley–Wiener–Schwartz theorem, respectively. These are internal written
derivations, not independent peer review or a claim of literature novelty.

Nontrivial bounded-speed dispersion can be carried by internal states.
The two-state identities, hidden slow-mode counterexample and specified
readout-noise limit below do not classify all matrix semigroups or force
an action scale. The historical cone/arrow comparison is maintained in
[source evidence and interfaces](ancient-cuts-provenance.md).

## Scalar probability kernels

**C032.** For probability measures, if $\mu_0=\delta_0$, $\mu_{s+t}=\mu_s*\mu_t$ and
$\operatorname{supp}\mu_t\subset[-ut,ut]$, then
$\operatorname{Var}\mu_T=n\operatorname{Var}\mu_{T/n}\le u^2T^2/n\to0$ and
$\mu_t=\delta_{bt}$ with $|b|\le u$. Adjacent sections of such a law are
translates of one another. The telegraph process escapes the theorem because
its position alone is not Markov: its kernel's Fourier transform
$e^{-\lambda t}[\cosh(st)+(\lambda/s)\sinh(st)]$ with
$s=\sqrt{\lambda^2-u^2k^2}$ is an even function of $s$, hence entire in $k$,
but it is not a convolution semigroup in $t$.

## Scalar unitary kernels

**Proposition.** Let $(U_t)_{t\in\mathbb R}$ be a strongly continuous
one-parameter unitary group on $L^2(\mathbb R)$ that commutes with
translations, and suppose that for every $t$ the kernel $K_t$ with
$U_t\psi=K_t*\psi$ has support in $[-u|t|,u|t|]$. Then there are real
constants $a,b$ with $|a|\le u$ such that $U_t\psi(x)=e^{-ibt}\psi(x-at)$.

**Proof.** Commutation with translations makes $U_t$ a Fourier multiplier by a
unimodular measurable $m_t(k)$, and Stone's theorem gives
$m_t(k)=e^{-it\omega(k)}$ for a real measurable $\omega$. The support
hypothesis and the Paley–Wiener–Schwartz theorem extend each $m_t$ to an
entire function with $|m_t(k)|\le C_t(1+|k|)^{N}e^{u|t||\operatorname{Im}k|}$.
The identity $m_tm_{-t}=1$ holds on the real axis, hence on $\mathbb C$, so
$m_t$ has no zeros and $G_t=\log m_t$ is entire. For fixed $t$, the bounds
for $m_t$ and $m_{-t}$ give
$|\operatorname{Re}G_t(z)|\le u|t||\operatorname{Im}z|+N_t\log(1+|z|)+C_t$.
For its harmonic real part, second-derivative estimates on a disk of
radius $R$ are $O((R+\log R)/R^2)$ and vanish as $R\to\infty$.
Thus the real part, and hence $G_t$, are affine; its value on the
real axis is zero. Thus $m_t(k)=e^{-i(a_tk+b_t)}$, with real $a_t,b_t$ and
$|a_t|\le u|t|$. The group law makes $a_t$ additive; the bound implies
$a_t=at$. Strong continuity makes the remaining phase a continuous character,
hence $e^{-ibt}$. This proves the form without selecting logarithms
continuously in time. $\square$

**Reading.** Scalar evolutions in this class are translations at any
$|a|\le u$, with an arbitrary constant phase rate. The massless chiral
choices $a=\pm u$ saturate the speed bound. Interpreting phase rate as
energy requires an action conversion factor. The Dirac
evolution keeps light-cone support and unitarity by carrying two components;
its scalar reduction has $\omega(k)=\sqrt{u^2k^2+\omega_0^2}$, which is real on
the axis but has branch points at $k=\pm i\omega_0/u$ and so cannot be the
dispersion of a scalar kernel of compact support. At $u=c$ and
$\omega_0=mc^2/\hbar$ the branch points sit at the inverse reduced Compton
length. Matching a telegraph rate to $\omega_0$ makes their reciprocal scales
coincide algebraically. This is a chosen model identification; analytic
continuation alone identifies neither probabilities nor physical dynamics.

## Bounded-speed fluctuations and the double limit

Refining time cuts and position resolution are distinct limits. For the
symmetric telegraph model with mass $m$, speed $u$ and switching rate
$\lambda>0$, put $H_*=mu^2/\lambda$ and $\Delta_*=1/\lambda$. The window
observable obeys $\mathsf h(\Delta)\le H_*\Delta/\Delta_*$ ([finite-speed response](susceptibility-gap.md)), and the
conditioned midpoint obeys the exact law
$\kappa_{\rm mid}/H_*=g(\lambda T)=zR(z)[1-R(z)]$ of [the return-bridge calculation](telegraph-return-bridge.md), with cubic onset. The fixed-preparation short-window intrinsic coefficient
vanishes under a speed ceiling; the specified crossover window
$\Delta_*=H_*/(mu^2)=1/\lambda$ concerns a long-window plateau, and $g$ describes its
approach. This does not assert a limit for noisy records whose error scale
changes with the cut. Which premise makes the plateau positive and common to
all bodies is [A08's question](composition-universality.md), not a consequence
of scalar finite propagation.

## Internal states, a matrix conjecture and readout noise

The scalar proposition is **not** a classification of matrix-valued finite-speed
semigroups. A candidate, still unproved, says that a translation-invariant,
strongly continuous contraction semigroup on $L^2(\mathbb R;\mathbb C^n)$
whose convolution kernels have support in $[-ut,ut]$ has Fourier multipliers
$e^{t(B-ikA)}$, where $A=A^\dagger$, $\|A\|\le u$ and
$B+B^\dagger\le0$. The missing steps include pointwise time continuity from
strong operator continuity, a justified matrix logarithm and differentiation
of its generator. Positivity alone does not make $B$ a conservative Markov
switching generator: $T_tf=e^{-t}f$ is positive and has zero propagation but
loses mass. Conservation must be required separately. The scalar proof above
does not discharge these obligations.

For the symmetric two-state telegraph generator
$Q=\lambda(\sigma_x-I)$ and $V=u\sigma_z$, the exact matrix identity is
$\|[V,Q]\|=2u\lambda$, while the stationary velocity plateau is
$H_*=mu^2/\lambda=2mu^3/\|[V,Q]\|$. A coherent two-component model with
$A=c\sigma_z$, $B_H=\omega_0\sigma_x$ similarly has
$\|[A,B_H]\|=2c\omega_0$. Converting frequency into rest energy uses a
**supplied** action $K$, $m=K\omega_0/c^2$; physical $\hbar$ enters only
if separately identified with $K$. A commutator norm does not see every slow
mode: [the four-state counterexample](susceptibility-gap.md#3-fixed-plateau-with-a-closing-full-gap-c041)
keeps the plateau fixed as an independent hidden label's relaxation gap closes.
For $Q=0$, a random constant velocity $\pm u$ instead has
$\operatorname{Var}(X_\Delta-X_0)=u^2\Delta^2$; a deterministic velocity has
zero variance. Commuting velocity sectors therefore do not justify the old
general zero-response claim.

There is also an **exact, model-dependent readout effect**. Define
$\mathsf h(\Delta)=m\operatorname{Var}(X_\Delta-X_0)/\Delta$ for a
fixed bounded-speed motion. At the two endpoints add independent centered
errors, independent of the motion, each of variance $\varepsilon^2/12$.
The observed increment then satisfies

$$\mathsf h_\varepsilon(\Delta)
=\mathsf h(\Delta)+\frac{m\varepsilon^2}{6\Delta}.$$

For fixed $\varepsilon>0$, the $\Delta\downarrow0$ limit is infinite;
for fixed $\Delta>0$, removing the readout error first and then refining
gives zero by finite speed. Along
$\varepsilon^2=6\kappa_0\Delta/m$, the observed coefficient tends to any
chosen $\kappa_0\ge0$. Independent dither or additive-noise measurement is
a premise here; fixed-lattice deterministic rounding need not satisfy it.
On a uniform $N$-cell partition, pin endpoint errors to zero and give the
$N-1$ interior errors this variance. Expanding the kinetic-action squares,
the expected added action is $m(N-1)\varepsilon^2/(12\Delta)$, with
correlated neighboring increment errors accounted for in the expectation.
This scaling selects a **readout bias**, not a lower bound on intrinsic
action and not physical $\hbar$.

## Exact free-kernel composition

The independently useful [time-refinement manuscript](../papers/time-refinement.tex)
and [PDF](../out/papers/time-refinement.pdf) retain the normalized free-kernel
proof, Rivero's 1998 intermediate-coordinate proposal and the separate
Brouder/Cariñena source leads. Their hypotheses are not those of the
ballistic-support theorems above.

In that proof a positive Gaussian kernel of variance $\kappa t/m$ composes
exactly under integration over an inserted position for every $\kappa>0$.
Weak continuity and Gaussian time homogeneity permit every
$\kappa=ma\ge0$; $a=0$ is the deterministic Dirac member. Requiring a
positive density rules out zero by premise. Passing from positive kernels
to oscillatory unitary propagation is another chosen step, and neither step
identifies $\kappa$ with physical $\hbar$. The
[Newton synthesis](groupoid-quantum-newton-states.md#6-regulators-and-a-normalized-blocking-test)
distinguishes this free fixed-line result from the two-regulator RG question.

## Consequence for STATE

Scalar finite-speed rigidity, the open matrix classification and the specified
readout double limit remain separate. At fixed preparation, bounded speed
makes the intrinsic short-window coefficient vanish; independent readout
errors can create any prescribed resolution-dependent coefficient.
Exact Gaussian composition also permits a deterministic zero member.
None of these statements supplies a universal positive physical action,
quantum reconstruction or historical transmission claim.
