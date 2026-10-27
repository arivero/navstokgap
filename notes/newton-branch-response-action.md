# Competing time-cell branches: a conditional positive-action bound

**Result, 2026-10-27; written derivation, unrefereed.** Within a positive-weight
nonlinear Euclidean time-cell family with two competing minima, a finite
ceiling on the normalized inserted-position response implies an explicit
positive lower bound uniform over its action multipliers. The bound follows from an exact
integration identity, with no small-action expansion. Positive action
rounds a zero-action branch jump on a source scale proportional to
$\hbar$. Retaining a classical branch label avoids the jump, and a
classical statistical weight can reproduce the response. These two
controls identify the physical assumptions that still need justification.

**Targeted check (GPT-6.1 Terra, 2026-10-27).** Terra read the note and
checked equations (6)--(14) without finding a mathematical error. Its
scope refinements about the spinodal endpoint and the separately defined
zero-action member are incorporated below. This was a targeted written
check, not validation of the physical response premise.

The point is to test a possible necessity mechanism beyond the convex
cell, not to infer action from a failure of ordinary ODE existence.
The real-time Newton equation for the smooth confining double well is
well posed. The conditional equilibrium source response studied here is
a different object.

Retrieval before this calculation: the
[nonlinear cell](newton-nonlinear-time-cell.md) gives exact normalized
elimination; the [ODE lesson](balaban-ode-lesson.md) separates causal
motion from endpoint projection; the
[Leibniz records note](leibniz-continuity-records.md), section 1, gives a
related continuity selector for specified Gaussian recording protocols;
and [zero-branch reachability](zero-branch-reachability.md), Theorem 5,
requires that incoherent classical attachments be retained as controls.
The calculations here are elementary quartic and exponential-family
identities. No literature novelty is claimed.

## 1. The nonlinear cell and its two branches

Keep $m,u,v>0$, $T=u+v$, $a=mT/(uv)$ and $w=T/2$ as in the nonlinear-cell
note. Fix $\lambda,b>0$ and use

$$
 V(z)=\frac\lambda4(z^2-b^2)^2,\qquad
 F_\mu(z)=\frac a2(z-\mu)^2+wV(z).
 \tag{1}
$$

All these cell parameters are held fixed when the action multiplier
is varied. Let

$$
 \gamma=w\lambda,\qquad d=\gamma b^2-a>0,
 \qquad r=\sqrt{d/\gamma}.
 \tag{2}
$$

At $\mu=0$, up to an additive constant,

$$F_0(z)=\frac\gamma4(z^2-r^2)^2+\text{constant}.\tag{3}$$

The two minima are $\pm r$, with second derivative $2d$. The intervening
barrier has action $d^2/(4\gamma)$. For equal time pieces, the condition
$d>0$ is $\lambda b^2T^2>8m$. This is precisely where the two-cell
Euclidean Hessian at the central point loses its short-interval
positivity. It does not mark a singularity of the causal Newton flow.

For $\hbar>0$ define the normalized law

$$
 d\nu_{\hbar,\mu}(z)=\frac{e^{-F_\mu(z)/\hbar}dz}
                              {\int e^{-F_\mu/\hbar}dz},
 \qquad M_\hbar(\mu)=\mathbb E_{\nu_{\hbar,\mu}}Z.
 \tag{4}
$$

The quartic tail makes these quantities smooth in $\mu$. The retained
action is
$A_\hbar=-\hbar\log[\sqrt{a/(2\pi\hbar)}\int e^{-F_\mu/\hbar}dz]$.
As before, the weighting is Euclidean. No real-time quantum law or $c$
is being derived from (4).

## 2. A finite response ceiling forces positive action in this model

Differentiating the normalized law gives the exact identities

$$
 M_\hbar'(\mu)=\frac a\hbar\operatorname{Var}_{\nu_{\hbar,\mu}}(Z),
 \qquad
 A_\hbar''(\mu)=a-aM_\hbar'(\mu).
 \tag{5}
$$

At the symmetric point $\mathbb EZ=0$. An integration by parts yields

$$
 \mathbb E(F_0')^2=\hbar\mathbb EF_0''
       =\hbar(3\gamma\mathbb EZ^2-d)>0.
 \tag{6}
$$

Hence $\operatorname{Var}(Z)>r^2/3$ for every $\hbar>0$, and

$$
 M_\hbar'(0)>\frac{ar^2}{3\hbar},\qquad
 A_\hbar''(0)<a-\frac{a^2r^2}{3\hbar}.
 \tag{7}
$$

**Conditional response theorem.** Suppose an independent physical
calibration or principle gives the ceiling
$M_\hbar'(0)\le R_*$, with a fixed finite $R_*>0$, and the physical
inserted-position law is (4). Then its action multiplier satisfies

$$\hbar>\frac{ar^2}{3R_*}>0.\tag{8}$$

Alternatively, $|A_\hbar''(0)|\le L$ with fixed $L\ge0$ implies

$$\hbar>\frac{a^2r^2}{3(a+L)}.\tag{9}$$

*Proof.* Equations (5)--(7) imply (8) directly. The second ceiling
implies $M_\hbar'(0)=1-A_\hbar''(0)/a\le1+L/a$, giving (9).
Equation (6) follows by integrating $(F_0'e^{-F_0/\hbar})'$;
its strict positivity follows because the continuous law is not
supported on the zeros of $F_0'$. $\square$

The lower bounds have units of action: $ar^2$ is an action and $R_*$
is dimensionless. Merely observing that each member of a positive-action
family has a finite derivative is weaker than supplying a fixed ceiling.
The theorem needs the latter, independently of the unknown multiplier.
It also needs (4) to be the physical response law. Neither requirement
has been derived from Newton's axioms or from time subdivision here.

To state zero exclusion precisely, extend the family at $\hbar=0$ by
global minimization for $\mu\ne0$ and any mean supported on the two
minima at $\mu=0$. Section 3 proves that this particular zero member is
discontinuous. A physical requirement of a differentiable response with
the same ceiling excludes that member, and (8) bounds all the surviving
positive members away from zero. It does not exclude a different
classical extension, such as the branch-labelled rule in section 4.

## 3. How the zero-action jump is rounded

At zero action, classical global minimization selects a positive minimum
for $\mu>0$ and a negative one for $\mu<0$. Their one-sided limits at
zero are $+r$ and $-r$. No choice of a single minimizing value at zero
makes this global-minimum selector continuous.

To verify the branch statement, write
$F_\mu=F_0-a\mu z+a\mu^2/2$. For $\mu>0$ any negative candidate is
improved by reflection, since $F_\mu(z)-F_\mu(-z)=-2a\mu z$ for $z>0$.
The stationary cubic $\gamma z^3-dz-a\mu=0$ has exactly one positive
root, beyond $r$, which is the global minimum. Reflection handles
$\mu<0$.

The positive-action transition has a specific source profile. For fixed
$\xi\in\mathbb R$, set

$$\mu_\hbar=\frac{\hbar\xi}{ar}.\tag{10}$$

Then

$$
 \frac{M_\hbar(\mu_\hbar)}r\longrightarrow\tanh\xi,
 \qquad
 \frac{\operatorname{Var}_{\nu_{\hbar,\mu_\hbar}}Z}{r^2}
       \longrightarrow\operatorname{sech}^2\xi,
 \qquad(\hbar\downarrow0).
 \tag{11}
$$

*Proof.* At zero source, the law concentrates equally at $\pm r$.
For completeness, subtract the minimum of (3). On a fixed compact set
outside neighborhoods of the two minima it is bounded below by a
positive constant. Near each minimum it is bounded above and below by
positive multiples of $d(z\mp r)^2$. The normalization is therefore
bounded below by a constant times $\sqrt{\hbar/d}$, while the mass of
the compact complement tends to zero exponentially. Quartic tails give
the same conclusion outside the compact set and for first and second
moments. Reflection fixes equal limiting masses.

At (10) the source changes this density by the factor
$e^{\xi z/r}$ and a normalization. Quartic decay still controls its
tails for $\xi$ in any fixed bounded interval, so its masses converge
to $e^{\xi}/(2\cosh\xi)$ at $r$ and $e^{-\xi}/(2\cosh\xi)$ at $-r$.
Their first two moments give (11). $\square$

Using the exact derivative identity (5) before taking the moment limit,

$$
 \frac{\hbar}{ar^2}M_\hbar'(\mu_\hbar)
       \longrightarrow\operatorname{sech}^2\xi.
 \tag{12}
$$

In particular the central slope is asymptotic to $ar^2/\hbar$.
This explains both the scale of (8) and the factor-three slack in its
global finite bound. No differentiation of a weak-limit formula was
used to obtain (12).

## 4. Classical branch memory is a decisive control

Global minimization discards a possible state variable: which stable
branch was prepared. The stationary branches $z_\pm(\mu)$ persist near
zero and satisfy

$$
 \gamma z_\pm^3-dz_\pm-a\mu=0,\qquad
 z_\pm(0)=\pm r,\qquad z_\pm'(0)=\frac a{2d}.
 \tag{13}
$$

Both are smooth on the open interval $|\mu|<\mu_{\mathrm{sp}}$, where

$$\mu_{\mathrm{sp}}=
 \frac{2d^{3/2}}{3a\sqrt{3\gamma}}.\tag{14}$$

This follows by solving the stationary equation and its vanishing second
derivative together. The disappearing branch extends continuously to its
spinodal endpoint, but its derivative diverges there. A classical rule
retaining the label $\sigma=\pm$
therefore has a finite local response with zero action multiplier.
Even the mean with source-independent equal branch populations,
$[z_+(\mu)+z_-(\mu)]/2$, is smooth near zero, with slope $a/(2d)$.

That rule is not the global-minimum selection used in section 3. The
example shows why losing a branch in a coarse description cannot itself
prove that all classical completions require positive action. A physical
argument would have to justify the equilibrium weighting of branches,
restrict accessible branch memory, or derive a different composition law.
The causal Newton initial-value flow also stays regular for this smooth
confining double-well potential, by the energy bounds discussed in the
ODE lesson.

## 5. A thermal countertest and the quantum question

The one-cell response cannot identify its multiplier as Planck action.
A classical system in the energy potential $E_\mu(z)=F_\mu(z)/w$ at
bath temperature $\Theta>0$ has the stipulated Boltzmann density

$$
 e^{-E_\mu/(k_B\Theta)}
       =e^{-F_\mu/\kappa},\qquad\kappa=wk_B\Theta.
 \tag{15}
$$

It reproduces every one-cell statistic above with $\kappa$ in place
of $\hbar$. This is an exact classical statistical countermodel to
identification from the curvature or response alone. It is not an
assertion that an arbitrary time-chain quantum propagator is a thermal
classical process.

The response theorem is nevertheless useful. Its independently testable
inputs and its predicted rounded source profile are explicit. The
physical work is to show why the relevant Newton body/apparatus has a
specified branch law and a finite preparation/record-uniform response,
and then connect the inferred action multiplier to real-time phase and
to composition across bodies. The present calculation supplies neither
an unrestricted universal response ceiling nor that identification.

For Galileo's constant force alone there is no such branch competition:
the conditional mean is affine in its source, with a finite derivative
at zero action. A successful nonlinear selector would have to transmit
one common action coefficient to that experiment through independently
justified composition. The existing universality arguments retain that
logical distinction.

## 6. Consequence for STATE

Branch competition gives a concrete conditional positivity theorem:
a calibrated finite response ceiling for the stated nonlinear cell law
forces the positive bound (8), and its transition width is proportional
to the action multiplier. Classical branch memory and a thermal weight
are explicit countertests. Next investigate whether a complete physical
record law supplies the response/branch premises, or whether real-time
interference provides a discriminator that the thermal cell lacks.
Newton necessity remains active; this result has not established its
physical premises or a universal Planck value.
