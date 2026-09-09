# The cut paradox in two signatures: sections of a solid and instants of a motion

Test 1 of [I003](../ideas/I003-cut-paradox-arrow-obstruction.md), drafted
2026-09-08 by the independent Claude Fable 5.1 session. Earlier scripts are
historical artifacts; current verification uses written proof and source review.
The proposition below is a working derivation awaiting review and a prior-art
audit; no claim ID is assigned. The 2026-09-09 review preserves the scalar
rigidity candidate and routes proof and source review to R02. The cone/arrow
connection below is a modern heuristic; analytic continuation relates the
specified evolution equations, rather than establishing a historical identity.

**Result.** The Euclidean statement C032, that a position-only law with
ballistic support and independent stationary increments is a deterministic
drift, has a Lorentzian counterpart: a scalar, translation-invariant, strongly
continuous unitary evolution on the line whose kernels are supported in the
light cone $[-ut,ut]$ is a uniform translation at some speed $|a|\le u$, up to
a constant phase. In both signatures a bounded-speed law with nontrivial
fluctuation or dispersion needs a second state variable, the velocity sign of
the telegraph process or the second component of the Dirac evolution, and the
continuation $\lambda\to i\omega_0$ of A09 carries the one situation into the
other. The obstruction sits at the Compton wave number: the scalar reduction of
the massive evolution has dispersion $\omega(k)=\sqrt{u^2k^2+\omega_0^2}$ with
branch points at $k=\pm i\omega_0/u$, which at $u=c$, $\omega_0=mc^2/\hbar$ is
$k=\pm imc/\hbar$. This is the reading of the user's remark 2 in I003 that the
present calculation supports; remark 3, an $h$ that controls convergence, is
the crossover $g(z)$ of the [coordinator's exact bridge note](bridge-crossover.md).

## 1. The two paradoxes as slicing laws

**Cone.** A solid is a family of sections $A(z)$, $0\le z\le h$. The cone
$A(z)=\pi r^2(1-z/h)^2$ has $A'(z)=-2\pi r^2(1-z/h)/h\ne0$ below the apex; the
cylinder has $A'=0$. Democritus asks whether adjacent sections are equal or
unequal, Chrysippus answers neither, and the continuum answer is that
$A(z+\delta)-A(z)=A'(z)\delta+O(\delta^2)$: adjacent sections differ by a
quantity that vanishes with the cut spacing while their ratio of differences
to spacing does not. The Mohist Canon stops the halving at an endpoint; Liu
Hui and Archimedes cut “until it cannot be cut” and keep the limit. Cutting
the solid at more places preserves the old sections; this is the restriction
consistency of a fixed solid, the analogue of C034 for a fixed bridge.

**Arrow.** A motion is a family $X(t)$. Zeno asks whether at each instant the
arrow is where it is, and Aristotle answers that the argument takes time to be
composed of nows (Physics VI.9). In the project's models the state at a cut is
$(X,V)$: the finite-speed bridge of C033 retains the velocity sign at every
cut, and its midpoint atom is exactly the arrow at its turning instant, where
the position is $uT/2$ with probability $1/I_0(\lambda T)$ and the velocity
is fixed only by the right-continuous convention. Al-Naẓẓām's leap is the
discrete crossing of the same instant.

Under the exchange of the slicing variable $z$ with $t$ and of the slope
$A'$ with the velocity, the two dilemmas are one question: what an
infinitesimally adjacent slice carries. The continuation of A09 makes the
exchange precise for the telegraph and checkerboard dynamics, and the rest of
this note states what survives on each side.

## 2. The Euclidean face

**C032.** If $\mu_0=\delta_0$, $\mu_{s+t}=\mu_s*\mu_t$ and
$\operatorname{supp}\mu_t\subset[-ut,ut]$, then
$\operatorname{Var}\mu_T=n\operatorname{Var}\mu_{T/n}\le u^2T^2/n\to0$ and
$\mu_t=\delta_{bt}$ with $|b|\le u$. Adjacent sections of such a law are
translates of one another. The telegraph process escapes the theorem because
its position alone is not Markov: its kernel's Fourier transform
$e^{-\lambda t}[\cosh(st)+(\lambda/s)\sinh(st)]$ with
$s=\sqrt{\lambda^2-u^2k^2}$ is an even function of $s$, hence entire in $k$,
but it is not a convolution semigroup in $t$.

## 3. The Lorentzian face

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
Harmonic derivative estimates make this function affine; its value on the
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
length. The analytic obstruction and the physical crossover $\Delta_*$ of the
P02 note are the same scale seen from the two sides of the continuation.

## 4. The double limit

Refining cuts in time and resolving positions together is the double limit
of I003's remark 2. At finite speed and fixed $\lambda$, the window
observable obeys $\mathsf h(\Delta)\le H_*\Delta/\Delta_*$ (P02), and the
conditioned midpoint obeys the exact law
$\kappa_{\rm mid}/H_*=g(\lambda T)=zR(z)[1-R(z)]$ of the bridge-crossover
note, with cubic onset. A window-independent coefficient therefore exists only
above $\Delta_*=K/(mu^2)$, and the joint limit of mesh and resolution to zero
leaves no coefficient unless the speed bound is removed, which is the Gaussian
class. The surviving constant is the plateau, and $g$ is the rate it controls.
Which premise makes that plateau positive and common to all bodies is A08's
question, and this note adds nothing to it.

## 5. Review and next step

R02 will audit the scalar proof and its Paley–Wiener/harmonic-growth ingredients,
then examine the matrix extension in
[the revised I003 note](i003-double-limit-rigidity.md). The historical analogy
remains available for idea generation. Its mathematical content must be
established model by model.
