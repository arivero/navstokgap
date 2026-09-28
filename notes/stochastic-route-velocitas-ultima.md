# Brownian free motion: the velocitas ultima denied, one action constant, and the floor

**Result, 2026-09-28 (Claude; written derivation, to be refereed).** A
third route for the [fifth-postulate programme](principia-fifth-postulate.md),
beside the deformation route (Theorems A, B) and the Gaussian state route
(Theorem B$'$): the stochastic one. Let the free motion of a body of mass
$m$ be a Markov process with continuous paths, homogeneous in space and
time and isotropic (premises P1--P3 of §1).

- **Theorem S1 (the law and the denial).** The free motion is Brownian
  motion with drift, with variance rate $D(m)\ge0$ per coordinate. For $D=0$
  it is Newton's inertial motion. For $D>0$ the paths are almost surely
  nowhere differentiable, so the *velocitas ultima* that Newton's scholium
  calls "certus & definitus" exists only as a mean velocity.
- **Theorem S2 (one constant).** If the law depends on the mass alone
  (P4) and the centre of mass of independent bodies obeys the law of
  their total mass (P5), then $\kappa=mD$ is one universal constant, with the
  dimension of an action; $\kappa=0$ is admissible.
- **Theorem S3 (the floor).** For $\kappa>0$, any record that decides from the
  path, with pinned ends, between the inertial chord and the
  constant-force parabola over a cell errs at equal priors with
  probability at least $\Phi(-\sqrt{K_\tau/2\kappa})$, attained by the optimal test,
  where $K_\tau=F^2\tau^3/(24m)$ is the Galileo action of the cell. Confidence
  $1-\epsilon$ needs $K_\tau\ge2z_{1-\epsilon}^2\kappa$; with $\kappa=\hbar$ this is the mark mesh of the
  [Planck paper](planck-gap-paper.md), eq. (2).
- **Independence (Nelson).** With diffusion coefficient $\nu=\kappa/2m$,
  Nelson's stochastic mechanics obeys Newton's second law in a mean sense
  and is equivalent to the Schrödinger equation with $\hbar=\kappa$
  ([Nelson 1966](https://doi.org/10.1103/PhysRev.150.1079), abstract;
  precursor [Fényes 1952](https://doi.org/10.1007/BF01338578), metadata).
  So every $\kappa\ge0$ is consistent with the Laws, the analogue of Theorem A.

The route carries the four parts of the fifth-postulate goal: the
statement (the existence of the ultimate velocity), its independence,
exactly one added action constant, and a floor on recording the
inertial--parabola difference, an area Newton takes to zero. Its limit is
the same as in the other routes: $\kappa>0$ is the negated postulate, assumed,
and the zero branch stays admissible. Theorems S1 and S2 are elementary;
the centre-of-mass argument of S2 is likely known in stochastic mechanics,
where $\nu\propto1/m$ is postulated, but it has not been located in print here.

## 1. Premises

- **P1 (continuity).** The free motion is a Markov process with
  continuous paths. Continuity of motion is Aristotle's (*Physics* VI,
  cited by book only); the leap of al-Nazzam, already in the Planck
  paper's classics, would be a jump, which P1 excludes.
- **P2 (homogeneity).** Stationary independent increments: no preferred
  place or time. A Galilean boost adds a constant drift and preserves P2.
- **P3 (isotropy).** No preferred direction.
- **P4 (mass alone).** A body's free law depends only on its mass, as
  all bodies fall alike.
- **P5 (composition).** For independent bodies the centre of mass obeys
  the free law of the total mass.

## 2. Theorem S1

A process in $\mathbb R^3$ with stationary independent increments and
continuous paths is a Brownian motion with drift, $X_t=x_0+vt+\Sigma^{1/2}W_t$ (the
Lévy--Itô decomposition has no jump part when the paths are continuous;
standard). Isotropy gives $\Sigma=D\,I$, and $D\ge0$ can depend only on the body.
For $D>0$, Brownian paths are almost surely nowhere differentiable
([Paley, Wiener and Zygmund 1933](https://doi.org/10.1007/BF01474606),
metadata), and they have Hausdorff dimension 2, the dimension found for
quantum paths by [Abbott and Wise (1981)](https://doi.org/10.1119/1.12657)
(metadata). The difference quotient $(X_{t+h}-X_t)/h$ has no limit; its
conditional mean does, $\lim_{h\downarrow0}E[X_{t+h}-X_t\mid\mathcal F_t]/h=v$, which is Nelson's
mean forward velocity. $\square$

In the words of the scholium closing Book I, Section I (quoted from the
1687 text in §1 of the [fifth-postulate note](principia-fifth-postulate.md)):
"Extat limes quem velocitas in fine motus attingere potest, non autem
transgredi. Hæc est velocitas ultima. [...] Cumq; hic limes sit certus &
definitus". For $D>0$ the limit of the ratio exists for the mean and fails
for the path. This is the denial of joint determinacy in the form Newton
wrote it: the place at an instant is sharp, while the velocity at that
instant has no pathwise value.

## 3. Theorem S2

*Proof.* Take independent bodies with masses $m_i$, drifts $v_i$ and
variance rates $D(m_i)$, and total mass $M=\sum m_i$. The centre of mass
$X=\sum m_ix_i/M$ has the constant drift $\sum m_iv_i/M$ (momentum conservation) and
the variance rate $\sum m_i^2D(m_i)/M^2$. By P5 this equals $D(M)$, so the function
$g(m)=m^2D(m)$ satisfies $g(m_1+m_2)=g(m_1)+g(m_2)$ for all $m_1,m_2>0$. Since $g\ge0$, $g$
is nondecreasing, and Cauchy's equation gives $g(m)=\kappa m$. Hence $D(m)=\kappa/m$ and
$mD=\kappa$ is the same for every body. Its dimension is mass times
length$^2$/time, an action. $\square$

The argument is the stochastic counterpart of the
[rotation-composition note](rotation-composition-universality.md), where
interaction forces a common constant in the composition of rotations; P4
plays the role of the equivalence principle, and P5 the role of the
centre-of-mass law. Neither argument excludes $\kappa=0$.

## 4. Theorem S3

Let a constant force $F$ act, so the body's path is the Newtonian parabola
plus $\sqrt{D}\,W_t$. Pin the ends of a cell of duration $\tau$. The two laws to be
told apart, with and without the force, are Brownian bridges of variance
rate $D=\kappa/m$ around the parabola and around the chord. Their difference is
the shift $\delta x$ (chord minus parabola), with Cameron--Martin norm
$\|\delta x\|^2=D^{-1}\int_0^\tau\dot{\delta x}^2dt=(m/\kappa)\int\dot{\delta x}^2=2K_\tau/\kappa$. The Neyman--Pearson test
with equal priors errs with probability $\Phi(-\frac12\|\delta x\|)=\Phi(-\sqrt{K_\tau/2\kappa})$, and no
test does better. This is Proposition 6 of the
[cut-measure note](cut-measure-newton.md) with $\hbar$ replaced by $\kappa$; its
Theorem 2 distributes the evidence $K_\tau/\kappa$ over any sequence of cuts,
each cut carrying the Kullback--Leibler share $3s(1-s)K_L/\kappa$. $\square$

With $\kappa=\hbar$, which is the normalization of the Euclidean free measure
$e^{-S/\hbar}$ and of Nelson's $\nu=\hbar/2m$, the threshold is
$\tau\ge(48z_{1-\epsilon}^2m\hbar/F^2)^{1/3}$, the Planck paper's eq. (2).

## 5. Where the route stands

| part of the goal | deformation route | state route | stochastic route |
| --- | --- | --- | --- |
| statement changed | commutativity (Thm A) | sharp states (Thm B$'$) | *velocitas ultima* exists pathwise (S1) |
| independence from the Laws | Moyal (Thm A) | Gaussian closure | Nelson 1966 |
| exactly one constant | Gutt, under covariance (Thm B) | Thm B$'$ | composition, P4--P5 (S2) |
| floor on the comparison | Thms C, E | Thm C | Cameron--Martin (S3) |

The premise that remains is the same in all three columns: why the
constant is positive. In the stochastic route it has the plainest form,
whether free paths have an instantaneous velocity, and Newton's scholium
asserts that they do. Two further limits: P4 and P5 are premises about
bodies (an equivalence principle for fluctuations and a centre-of-mass
law), and S3 is proved for additive position noise, the law of S1 with a
force added; in Nelson's full dynamics the drift depends on the state,
and the corresponding bound is not claimed here. Allowing jumps (the
leap) replaces Brownian motion by a general Lévy process, and what P5
then forces on the jump measure is open.

## 6. Consequence for STATE

Newton necessity gains a third route in which the negated postulate is
Newton's own sentence on the ultimate velocity: continuity, homogeneity
and isotropy give Brownian free motion, composition gives one action
constant, and the Cameron--Martin theorem gives the floor, equal to the
Planck paper's mark mesh at $\kappa=\hbar$. Positivity of $\kappa$ remains a premise.
