# The mark cost is exactly $\hbar/2$, and the worst-case theorem survives as a statistical one

**Correction, 2026-09-22.** Section 4 of the first version applied
Theorem B to every Gaussian probe. Theorem B assumes that each mark's
error and recoil are independent, and a probe whose position and momentum
are correlated delivers correlated ones. The corrected statement is
Theorem C: with correlation coefficient $\rho$ between a mark's error and
its recoil, the cost that enters the floor is
$\kappa_{\rm eff}=\delta\Delta(1-|\rho|)\ge\frac\hbar2\sqrt{(1-|\rho|)/(1+|\rho|)}$,
so every protocol whose marks have $|\rho_j|\le\rho$ needs

$$\tau\Delta E\ \ge\ \frac92\,z_{1-\epsilon}^2\,\hbar\,\sqrt{\frac{1-\rho}{1+\rho}} .$$

The value $\frac92z^2\hbar$ is the uncorrelated case $\rho=0$, which
contains every coherent probe and every probe squeezed along its
pointer's axes. A three-mark protocol whose middle probe is squeezed
along a rotated quadrature has $\rho\to1$ and decides the comparison at
any force (Proposition D), and Yuen's contractive states are this
resource. The same mechanism corrects the aperture corollary of the
[probabilistic note](planck-gap-probabilistic.md): in both places a floor
of order $\hbar$ holds once the shape of the uncertainty ellipse is
bounded, and its area alone leaves the floor free.

Reopening the question of what was wrong with the
[derivation note](planck-gap-derivation.md): almost nothing. Its
Proposition 6 claimed a positive quantum value for the mark cost
$\kappa=\delta\Delta$, and that claim is correct. The proof was invalid
and the constant was too large by a factor of four, and the worst-case
*formulation* of $\delta$ and $\Delta$ as support widths is what made the
quantum instance empty. Replacing support widths by standard deviations
repairs everything at once, and two theorems then close the gap the
derivation note left open.

**Theorem A.** For a mark realized by the impulsive coupling
$\lambda\hat y\otimes\hat P_A$ of the body's position to a probe, with
the probe's pointer read afterwards, the mark's error operator and the
impulse it delivers are canonically conjugate,

$$\hat N=\frac{\hat Q_A}{\lambda}-\hat y,\qquad \hat D=-\lambda\hat P_A,
\qquad [\hat N,\hat D]=-i\hbar,\qquad\text{hence}\qquad
\delta\Delta=\Delta_\psi\hat N\cdot\Delta_\psi\hat D\ \ge\ \frac\hbar2$$

for every probe state whatever. So $\kappa\ge\hbar/2$, exactly, with no
error--disturbance relation and no calibration argument.

**Theorem B.** In the Gaussian statistical model, for every protocol of
marks with $\delta_j\Delta_j\ge\kappa$, of any number and at any times,
with the initial position and velocity unknown, the optimal test's
deflection obeys

$$d^2\ \le\ \frac{2F^2\tau^3}{9\,m\kappa},\qquad\text{hence deciding at
error probability }\epsilon\text{ requires}\qquad
\tau\Delta E=\frac{F^2\tau^3}{2m}\ \ge\ 9\,z_{1-\epsilon}^2\,\kappa ,$$

with $z_{1-\epsilon}=\Phi^{-1}(1-\epsilon)$. With Theorem A this is
$\tau\Delta E\ge\tfrac92z_{1-\epsilon}^2\hbar$, about $12\hbar$ at five
per cent error, for probes whose error and recoil are uncorrelated;
Theorem C gives the correlated case. The proof is the derivation note's proof unchanged:
the same certificate, the same arithmetic--geometric step, the same
integration by parts to a Dirichlet energy, with the separating
hyperplane replaced by the optimal test direction. The constant $9$
reappears from the same Cauchy--Schwarz inequality.

Newton's premise M3 is Theorem A for his own probe: the interval of fits
$\Lambda$ is the corpuscle's transverse position spread and $p$ its
transverse momentum spread, so $\kappa=\Lambda p$ is the corpuscle's own
uncertainty product, and the heuristic value $h/2$ of the
[mark-floor note](newton-mark-floor.md) differs from the theorem's
$\hbar/2$ by $\pi$. Section 6 sets out the single paper this supports.
Exploratory; no ledger promotion.

## 1. What was actually wrong, stated exactly

The derivation note's framework defines a mark's resolution $\delta$ and
recoil width $\Delta$ as worst-case interval widths: the datum confines
the position to an interval of length $\delta$ with certainty, and the
records confine the delivered impulse to an interval of length $\Delta$
with certainty. Three claims about that framework are now settled.

- **Theorem 1 is correct and is not affected.** For every finite protocol
  with $\delta_j\Delta_j\ge\kappa$, deciding the comparison needs
  $F^2\tau^3>9m\kappa$.
- **The worst-case framework has no quantum instance.** Certain position
  confinement forces a compactly supported conditional state, whose
  momentum distribution has full support by Paley--Wiener. So no quantum
  mark has both widths finite, $\kappa=\infty$, and Theorem 1 holds
  emptily. This is the correction that stands.
- **The conclusion of the first Proposition 6 was right anyway.** Its
  assertion was that quantum kinematics gives $\kappa$ a positive value of
  the order of $\hbar$, and that the Galileo comparison therefore has a
  floor of order $\hbar$ in $\tau\Delta E$. Theorem A gives $\kappa\ge\hbar/2$
  and Theorem B gives the floor, so both are true. What failed was the
  route: bounding a Wasserstein-2 calibration disturbance by half a
  worst-case width, when that disturbance is infinite for the instruments
  in question.

So the defect was the choice of currency, and it cost one constant and
one proof. Standard deviations are the right currency because they are
finite for quantum states, because they are what the uncertainty relation
constrains, and because the derivation note's proof never used
containment beyond a quadratic bound, as Section 3 shows.

## 2. Theorem A: the mark's error and its recoil are conjugate

Take the von Neumann model of a position mark. The body has $\hat y,\hat p$;
the probe has $\hat Q_A,\hat P_A$ with $[\hat Q_A,\hat P_A]=i\hbar$; the
mark is the impulsive unitary

$$U=\exp\left(-\frac{i}{\hbar}\lambda\,\hat y\,\hat P_A\right),\qquad\lambda>0 .$$

**Theorem A.** In the Heisenberg picture across the mark,

$$U^\dagger\hat Q_AU=\hat Q_A+\lambda\hat y,\qquad
U^\dagger\hat pU=\hat p-\lambda\hat P_A,\qquad
U^\dagger\hat yU=\hat y,\qquad U^\dagger\hat P_AU=\hat P_A .$$

Reading the pointer $\hat Q_A$ and estimating the body's position by
$\hat Q_A/\lambda$, the error operator $\hat N=\hat Q_A/\lambda-\hat y$
and the delivered impulse $\hat D=\hat p_{\rm after}-\hat p_{\rm before}=-\lambda\hat P_A$
satisfy $[\hat N,\hat D]=-i\hbar$, hence for every joint state

$$\delta\,\Delta:=\Delta\hat N\cdot\Delta\hat D\ \ge\ \frac\hbar2 .$$

*Proof.* With $A=\frac{i}{\hbar}\lambda\hat y\hat P_A$, so that
$U^\dagger=e^{A}$, the commutators are
$[A,\hat Q_A]=\frac{i\lambda\hat y}{\hbar}[\hat P_A,\hat Q_A]=\lambda\hat y$
and $[A,\hat p]=\frac{i\lambda\hat P_A}{\hbar}[\hat y,\hat p]=-\lambda\hat P_A$,
both central, so the Baker--Campbell--Hausdorff series terminates and gives
the four displayed relations. The error operator is then
$\hat N=(\hat Q_A+\lambda\hat y)/\lambda-\hat y=\hat Q_A/\lambda$, whence

$$[\hat N,\hat D]=\left[\frac{\hat Q_A}{\lambda},-\lambda\hat P_A\right]
=-[\hat Q_A,\hat P_A]=-i\hbar,$$

and Robertson's inequality gives
$\Delta\hat N\,\Delta\hat D\ge\frac12|\langle[\hat N,\hat D]\rangle|=\hbar/2$. $\square$

Three features matter. The coupling strength $\lambda$ cancels, so the
bound is a property of the mark and not of how hard it is made. The
result holds for every probe state, pure or mixed, Gaussian or not. And
the two quantities are the probe's own position and momentum spreads:
$\delta=\Delta\hat Q_A/\lambda$ and $\Delta=\lambda\Delta\hat P_A$, so

$$\kappa=\delta\Delta=\Delta\hat Q_A\cdot\Delta\hat P_A ,$$

the mark's cost is the probe's uncertainty product, and the floor of the
Galileo comparison is set by the probe rather than by the body. The contested error--disturbance relations play no part: Ozawa's
counterexamples concern instruments whose commutator $[\hat N,\hat D]$
differs from $-i\hbar$, and the present statement is confined to the
momentum-transfer class where it equals $-i\hbar$.

**The correlation of error and recoil.** The same commutator bounds the
joint covariance of the two quantities. With $c=\operatorname{Cov}(\hat N,\hat D)$
the symmetrized covariance, the Robertson--Schrödinger inequality gives

$$\delta^2\Delta^2-c^2\ \ge\ \frac{\hbar^2}{4},\qquad
c=-\operatorname{Cov}(\hat Q_A,\hat P_A),$$

with $\lambda$ cancelling again. The correlation coefficient
$\rho=c/(\delta\Delta)$ is a property of the probe state. It vanishes for
coherent states and for states squeezed along $\hat Q_A$ or $\hat P_A$,
and it approaches $\pm1$ for a state squeezed along a rotated quadrature
$\hat Q_A\cos\varphi+\hat P_A\sin\varphi$. Section 4 shows that $\rho$
enters the floor.

**Why the records cannot recover the recoil.** The pointer record is
$\hat R=\hat Q_A+\lambda\hat y$ and the impulse is $\hat D=-\lambda\hat P_A$,
with $[\hat R,\hat D]=-i\hbar\lambda$. The record and the recoil are
incompatible observables, so no reading of the pointer, however precise,
determines the impulse. This is Proposition 5 of the derivation note seen
from the other side: the far-screen construction recovers the impulse by
measuring the probe's momentum, and measuring the probe's momentum is
exactly what reading its position forbids.

## 3. Theorem B: the same proof, in the Gaussian statistical model

**The model.** Marks at $0=t_0<t_1<\dots<t_k\le\tau$. Mark $j$ returns
$R_j=y(t_j)+\xi_j$ with $\xi_j$ centred Gaussian of standard deviation
$\delta_j$, and delivers an impulse $\iota_j$, centred Gaussian of
standard deviation $\Delta_j$, all independent. The trajectory is

$$y(t)=y_0+v_0t+\theta P(t)+\frac1m\sum_{j}\iota_j(t-t_j)_+,
\qquad P(t)=\frac{Ft^2}{2m},$$

with $\theta=0$ under $\mathrm I$ and $\theta=1$ under $\mathrm F$, and
$y_0,v_0$ unknown. A protocol satisfies the **mark trade-off** with
constant $\kappa$ when $\delta_j\Delta_j\ge\kappa$ for every $j$.

**Invariance and the deflection.** Tests are required to be invariant
under the unknown $y_0$ and $v_0$, so the statistic is $u^{\mathsf T}R$
with $u$ orthogonal to the vectors $(1,\dots,1)$ and $(t_0,\dots,t_k)$.
For Gaussian data the optimal invariant test has error probability
$\Phi(-d/2)$ with

$$d^2=\sup\left\{\frac{(u^{\mathsf T}P)^2}{u^{\mathsf T}\Sigma u}\ :\
\sum_iu_i=0,\ \sum_iu_it_i=0\right\},\qquad P_i=P(t_i),$$

$\Sigma$ being the covariance of $R$. This $u$ is the statistical
counterpart of the derivation note's separating multipliers $\mu$, and it
obeys the same constraint $\sum_iu_i=0$.

**Theorem B.** For every such protocol,
$d^2\le\dfrac{2F^2\tau^3}{9\,m\kappa}$. Consequently an invariant test
with error probability at most $\epsilon$ requires

$$F^2\tau^3\ \ge\ 18\,z_{1-\epsilon}^2\,m\kappa,\qquad
\tau\Delta E\ \ge\ 9\,z_{1-\epsilon}^2\,\kappa,\qquad
A_{\rm inertial,fall}\ \ge\ \frac{6\,z_{1-\epsilon}^2\,v\kappa}{F}.$$

*Proof.* The noise decomposes exactly as in the derivation note's
feasibility system: $\xi_j$ enters $R_j$ alone, and $\iota_j$ enters
$R_i$ for $i>j$ with coefficient $(t_i-t_j)/m$. Hence

$$u^{\mathsf T}\Sigma u=\sum_j\delta_j^2u_j^2+\sum_j\frac{\Delta_j^2}{m^2}S_j^2,
\qquad S_j=\sum_{i>j}u_i(t_i-t_j),$$

the same $S_j$ as there. By the arithmetic--geometric mean inequality
applied termwise, exactly as in that note's Lemma 2,

$$u^{\mathsf T}\Sigma u\ \ge\ \sum_j\frac{2\delta_j\Delta_j}{m}|u_j||S_j|
\ \ge\ \frac{2\kappa}{m}\sum_j|u_j||S_j| .$$

Since $\sum_iu_i=0$, Lemma 3 of that note applies verbatim with $\mu$
replaced by $u$: with $T(w)=\int_w^\tau\sum_{i:t_i>s}u_i\,ds$ one has
$T(t_j)=S_j$,

$$u^{\mathsf T}P=\frac Fm\int_0^\tau T,\qquad
\sum_ju_jT(t_j)=-E,\qquad E=\int_0^\tau T'^2 ,$$

so $\sum_j|u_j||S_j|\ge E$ and $u^{\mathsf T}\Sigma u\ge2\kappa E/m$.
Cauchy--Schwarz with $T(\tau)=0$ gives
$\int_0^\tau T\le\frac23\tau^{3/2}\sqrt E$, so

$$\frac{(u^{\mathsf T}P)^2}{u^{\mathsf T}\Sigma u}
\le\frac{(F/m)^2\frac49\tau^3E}{2\kappa E/m}=\frac{2F^2\tau^3}{9m\kappa},$$

independently of $u$, of the number of marks and of their times. The
error probability $\Phi(-d/2)\le\epsilon$ requires $d\ge2z_{1-\epsilon}$,
and $F^2\tau^3\ge\frac92m\kappa d^2\ge18z_{1-\epsilon}^2m\kappa$. $\square$

The worst-case theorem and the statistical theorem therefore have one
proof. The certificate changes meaning, from a hyperplane separating a
feasible set to the direction of the optimal test, and every step after
it is identical. This is the sense in which the derivation note's content
survived its formulation: the argument never needed interval containment,
only a quadratic bound in the same two variables.

## 4. Gaussian quantum experiments, with and without correlation

For Gaussian probe states, linear dynamics and pointer readouts, the
Wigner function is a genuine probability density and evolves by the
classical linear equations, so every measured distribution in the
quantum experiment equals the corresponding distribution in the
classical Gaussian model whose noise covariance is the probe's Wigner
covariance. That covariance gives mark $j$ a jointly Gaussian pair
$(\xi_j,\iota_j)$ with variances $\delta_j^2,\Delta_j^2$ and covariance
$c_j=\rho_j\delta_j\Delta_j$, independent across marks. Section 3 is the
case $c_j=0$.

**Theorem C.** In this model, if every mark has
$\delta_j\Delta_j(1-|\rho_j|)\ge\kappa_{\rm eff}$, then
$d^2\le2F^2\tau^3/(9m\kappa_{\rm eff})$ and deciding at error
probability $\epsilon$ requires $\tau\Delta E\ge9z_{1-\epsilon}^2\kappa_{\rm eff}$.
For momentum-transfer marks with $|\rho_j|\le\rho$,

$$\tau\Delta E\ \ge\ \frac92\,z_{1-\epsilon}^2\,\hbar\,\sqrt{\frac{1-\rho}{1+\rho}} .$$

*Proof.* The statistic's noise is
$\sum_j\bigl(u_j\xi_j+S_j\iota_j/m\bigr)$, so the variance acquires the
cross terms $2c_ju_jS_j/m$:

$$u^{\mathsf T}\Sigma u=\sum_j\Bigl(\delta_j^2u_j^2+\frac{2c_j}{m}u_jS_j
+\frac{\Delta_j^2}{m^2}S_j^2\Bigr).$$

For $a,b\ge0$ and $|c|\le\sqrt{ab}$, the arithmetic--geometric mean
inequality and $2cxy\ge-2|c||x||y|$ give
$ax^2+2cxy+by^2\ge2(\sqrt{ab}-|c|)|x||y|$, so each term is at least
$2\delta_j\Delta_j(1-|\rho_j|)|u_j||S_j|/m\ge2\kappa_{\rm eff}|u_j||S_j|/m$.
From here the proof of Theorem B runs unchanged with $\kappa_{\rm eff}$ in
place of $\kappa$. For the quantum value, the section-2 inequality
$\delta^2\Delta^2(1-\rho^2)\ge\hbar^2/4$ gives
$\delta\Delta(1-|\rho|)\ge\frac\hbar2(1-|\rho|)/\sqrt{1-\rho^2}
=\frac\hbar2\sqrt{(1-|\rho|)/(1+|\rho|)}$, with equality for pure Gaussian
probes. $\square$

At $\rho=0$ this is $\tau\Delta E\ge\frac92z^2\hbar$: $12.2\,\hbar$ at
$\epsilon=0.05$, where $z=1.645$, and $4.5\,\hbar$ at $\epsilon=0.32$,
where $z=1$. The dependence on $\rho$ is attained, up to the constant, by
three marks.

**Proposition D.** Marks at $0,\tau/2,\tau$ and the test
$R_1-2R_2+R_3$ decide the comparison when
$\tau\Delta E\ge32z_{1-\epsilon}^2\hbar\sqrt{(1-\rho)/(1+\rho)}$, where
$\rho$ is the middle probe's correlation.

*Proof.* The weights $u=(1,-2,1)$ annihilate the unknown position and
velocity, and $u^{\mathsf T}P=F\tau^2/4m$. The recoils of the outer
marks have $S_1=S_3=0$: the first is absorbed into the unknown initial
velocity and the last acts after every reading. So the outer marks may
be made as sharp as desired at no cost, and the noise is that of the
middle mark, $-2\xi_2+(\tau/2m)\iota_2$. With the coupling chosen so
that $2\delta_2=\tau\Delta_2/2m$ and a pure Gaussian probe of correlation
$\rho>0$, its variance is
$(2\tau/m)\delta_2\Delta_2(1-\rho)=(\tau\hbar/m)\sqrt{(1-\rho)/(1+\rho)}$.
Hence $d^2=\frac{\tau\Delta E}{8\hbar}\sqrt{(1+\rho)/(1-\rho)}$, and
$d\ge2z$ is the stated condition. $\square$

As $\rho\to1$ the three-mark protocol decides at every force. The middle
probe's kick is correlated with its reading error so that the kick's
effect on the third reading cancels the error in the second, which is
the back-action evasion of Yuen's contractive states
([PRL **51**, 719, 1983](https://doi.org/10.1103/PhysRevLett.51.719),
metadata). The floor of order $\hbar$ is therefore a statement about
marks whose error--recoil correlation is bounded, and Theorem C gives
its value for every bound. The insertion
statement follows as before: marks inserted into a window of duration
$\tau'$, used by themselves, record the force only if
$F^2\tau'^3\ge18z^2m\kappa$, so Democritus insertion stops at the mesh

$$\tau_*=\left(\frac{18\,z_{1-\epsilon}^2\,m\kappa}{F^2}\right)^{1/3}
=\left(\frac{9\,z_{1-\epsilon}^2\,m\hbar}{F^2}\right)^{1/3},$$

and finer marks record free motion at the stated confidence.

This coexists with the counterexample of the
[probabilistic note](planck-gap-probabilistic.md), which distinguishes
the hypotheses at arbitrarily small $\tau\Delta E$ using a two-packet
preparation of separation $\pi\hbar/(F\tau)$. That protocol is
non-Gaussian and makes no marks: it prepares once, waits, and measures
once. The two results divide the ground cleanly. **Marking the trajectory
with uncorrelated probes costs $\hbar/2$ per mark and gives a floor of
order $\hbar$; declining to mark it costs an apparatus of size
$\pi\hbar/(F\tau)$, and the floor at aperture $(L,P)$ is
$2m(1-2\epsilon)^2\hbar^2\tau/(2mL+\tau P)^2$, equal to
$(1-2\epsilon)^2\hbar^2/(4LP)$ at the balanced aperture.** Newton's
refinement is the first case, which is why the floor is the relevant
statement for the insertion question.

Both escapes use one resource. A correlated probe and an unbalanced
aperture each stretch an uncertainty ellipse of fixed area along a
direction the test does not see: the rotated quadrature of the middle
probe in Proposition D, the long side of the aperture in the
probabilistic note. Robertson's inequality fixes the area; the floor
needs the shape bounded as well, and then $\hbar$ fixes its value.

## 5. Newton's premise is Robertson's inequality for his corpuscle

The [mark-floor note](newton-mark-floor.md) posited M3, that a mark
fixing the position within $\delta$ leaves the delivered impulse
undetermined within $\Lambda p/\delta$, and observed that Newton's optics
supplies $\Lambda$ and $p$ while his determinism denies the premise.
Theorem A says what M3 is. The corpuscle is the probe; $\hat Q_A$ is its
transverse position and $\hat P_A$ its transverse momentum; the interval
of fits $\Lambda$ is the scale of the first and the corpuscular impulse
$p$ the scale of the second; and the premise asserts precisely that their
product cannot be reduced. So

$$\kappa=\Lambda p\quad\longleftrightarrow\quad
\kappa=\Delta\hat Q_A\cdot\Delta\hat P_A\ \ge\ \frac\hbar2 ,$$

and M3 is Robertson's inequality for the corpuscle, stated in the two
quantities Newton had. The floor uses M3 with a second clause that the
mark-floor note left implicit: the undetermined impulse is unrelated to
the mark's error. Theorem C prices that clause, since a correlation
$\rho$ multiplies the floor by $\sqrt{(1-\rho)/(1+\rho)}$. Newton measured the first as $1/89000$ inch, had
no access to the second, held both to be determinate properties of the
corpuscle, and thereby denied exactly the inequality. His Prop. XII
states the fits as a transient constitution that returns at equal
intervals and disposes the ray at every return, which is a determinate
periodic property; the
[source companion](../docs/classics/Newton_Opticks_1730_fits_and_queries.md)
holds that passage and the other four with their line anchors. The modern value
$\hbar/2$ against the identification $\Lambda p=h/2$ differ by $\pi$.

The historical claim this licenses is narrow and checkable. Newton's
optics contains both factors of the product that bounds the recorded
Galileo comparison; his mathematics contains the comparison and takes it
to zero; and the single proposition that would join them is a claim of
indeterminacy about the fits, which he considered and rejected in favour
of a determinate periodic disposition. The gap between the *Principia*'s
vanishing sagitta and the *Opticks*' finite interval of fits follows from
that single commitment, and the separation of the two books is incidental
to it.

## 6. The single paper, valid for both audiences

The user's requirement is one paper that a foundations-of-physics referee
and a history-and-philosophy-of-science referee both accept. That is
attainable, because the historical analysis now does argumentative work
rather than decorating a theorem. The structure is:

1. **The comparison and its limit.** Newton's Lemmas X and XI and the
   projectile Scholium, with the sagitta, the inertial--parabola area and
   the identity $(3F/v)A=\tau\Delta E$. Berkeley's objection and its
   resolution inside the geometry, with Guicciardini on what the limit
   arguments were for.
2. **The two theorems.** Theorem A, that a momentum-transfer mark's error
   and recoil are conjugate, and Theorem B, that every protocol of such
   marks needs $\tau\Delta E\ge9z^2\kappa$, with Theorem C for correlated
   error and recoil. Proof by certificate,
   arithmetic--geometric mean and Dirichlet energy. This is the
   foundations content and it stands alone.
3. **The two factors in the *Opticks*.** The interval of fits as a
   measured length, the corpuscular impulse as a posited one, and
   Shapiro's account of what the theory of fits was and how determinate
   Newton meant it. This is the history content and it stands alone.
4. **The junction.** M3 is Robertson for the corpuscle. The counterfactual
   is replaced by an exact statement: the premise that the theorem needs
   is one Newton formulated the negation of, so the distance between his
   system and a positive $h$ is a single proposition, nameable in his own
   vocabulary.
5. **What the theorem does not give.** The aperture counterexample, the
   standard-quantum-limit literature and Ozawa's class, and the honest
   prior-art label: the combination $F^2\tau^3\gtrsim m\hbar$ is the
   standard quantum limit, and the contribution is universality over
   protocols, the exact mark cost, and the identification of the premise.

The venues that take this shape are Foundations of Physics and Studies in
History and Philosophy of Modern Physics, both of which publish papers
whose historical and technical halves are load-bearing for each other.
Two obligations remain before submission: reading Shapiro, Guicciardini
and Sabra rather than citing them, and replacing the Project Gutenberg
*Opticks* and the Wikisource *Principia* with the fourth edition and the
Cohen--Whitman translation.

## 7. Consequence for STATE

The derivation note's Proposition 6 is reinstated in substance with a
correct proof and the constant $\hbar/2$ in place of $2\hbar$, and its
worst-case formulation is replaced by standard deviations. The Planck gap
for marked trajectories is
$\tau\Delta E\ge\frac92z_{1-\epsilon}^2\hbar\sqrt{(1-\rho)/(1+\rho)}$,
protocol-universal for marks whose error--recoil correlation is at most
$\rho$, with the insertion mesh $\tau_*=(9z^2m\hbar/F^2)^{1/3}$ at
$\rho=0$; Proposition D attains the $\rho$-dependence up to the
constant. A floor with no shape bound needs a quantity that squeezing
cannot move, which is the task of the next note. The remaining programme is item 6's two
obligations plus: extending Theorem A beyond the momentum-transfer class,
where Ozawa's instruments live; the general force law, which Theorem B's
proof already reduces to a norm of $P''$; and closing the constants
between the worst-case, statistical and single-shot forms.
