# Newton without a Lipschitz bound: time scales, uniqueness and explicit hbar

**Result, 2026-10-27; written derivation, unrefereed.** For a scalar
conservative repelling force, the time to reach its zero-force point
decides whether rest is unique. A logarithmic family has an exact
threshold: forces behaving as $q[\log(\ell/|q|)]^\beta$ have unique
motion at rest for $0<\beta\le2$, despite an unbounded force derivative;
for $\beta>2$ they admit arbitrary waiting and full point-state mergers.
On logarithmic spatial annuli the crossing times scale as
$n^{-\beta/2}$. Their sum, rather than a uniform Lipschitz constant,
decides the threshold. The action of the shrinking annuli tends to
zero on both sides. A local quantum residual becomes large at action
comparable with a supplied $\hbar$, but does not select its value.

**Targeted check (GPT-6.1 Terra, 2026-10-27).** Terra checked the
arrival criterion, uniqueness and polygon limits, and equations
(3)--(14). Its correction restricting the infinite-arrival-time
statement to zero-energy trajectories is incorporated below. This
written check does not validate the physical preparation premises.

This is a refinement of the [ODE lesson](balaban-ode-lesson.md), not a
claim that Lipschitz regularity is necessary. The
[bounded-cusp preparation theorem](newton-cusp-preparation-floor.md)
uses an actual merger; unbounded slope alone does not trigger it.
The energy separation below is an elementary continuous-force special
case of the subject studied by López Pouso [@LopezPouso2005; publisher
metadata and abstract read, article body not obtained]. Its general
$W^{2,1}$ theorem is not used as an unexamined premise here.
Teschl [@TeschlODE2012, section 2.7, pp.54--56 and Problem 2.25,
p.58; passages read] supplies the Euler compactness construction and
the different, general first-order Osgood criterion. See the
[source companion](../docs/Teschl_ODE_2012.md). No novelty is claimed.

## 1. The conservative second-order arrival test

Near zero let $a$ be continuous, odd, positive on $(0,r_0)$, zero at
zero and smooth away from zero. Consider

$$
 \ddot q=a(q),\qquad W(q)=\int_0^q a(s)\,ds\quad(q\ge0),
 \qquad V(q)=-mW(|q|),\quad m>0.
 \tag{1}
$$

Assume a bounded continuous global extension of the force, smooth away
from zero, by cutting off the potential outside a neighborhood of zero.
The [bounded-cusp argument](newton-cusp-preparation-floor.md), section 1,
then gives global existence and bounds preventing escape. The issue
remaining here is uniqueness, not existence.

Conservation of $E=m\dot q^2/2+V(q)$ follows by the chain rule since
$V\in C^1$. Any solution starting at rest at zero has $E=0$. On a
positive departing segment its velocity must be

$$
 \dot q=\sqrt{2W(q)},\qquad
 \mathcal T(q)=\int_0^q\frac{ds}{\sqrt{2W(s)}}.
 \tag{2}
$$

**Arrival criterion.** If $\mathcal T(q)=\infty$ for one, hence every
small $q>0$, rest is the unique local solution from $(0,0)$. If
$\mathcal T(q)<\infty$, the inverse $Q=\mathcal T^{-1}$ constructs
departures $q(t)=\pm Q(t-t_0)$ after every waiting time $t_0$.

For the first implication, a nonconstant solution has an excursion of
one sign starting from zero. Its velocity cannot vanish inside that
excursion because $W>0$, and separation of variables would give a
finite value for the divergent integral (2). For the converse,
$Q'=\sqrt{2W(Q)}$ and $Q''=a(Q)$. Both tend to zero at departure,
so adjoining rest gives a $C^2$ Newton trajectory. Reversing the two
departures supplies two different incoming full states that merge at
zero in finite time, exactly as in the cusp note.

For $a(q)=c q^\alpha$ this test reproduces the familiar $\alpha<1$
nonuniqueness threshold: its integrand is proportional to
$q^{-(1+\alpha)/2}$. The logarithmic family below tests the more delicate
border where no power-law Lipschitz constant exists.

## 2. An exact logarithmic family

Fix $\Omega,\ell>0$, $\beta>0$ and put $r=\beta/2$. For sufficiently
small $q>0$, with $L=\log(\ell/q)>\max\{1,r\}$, set

$$
 W(q)=\frac{\Omega^2}{2}q^2 L^\beta,\qquad
 a(q)=\Omega^2q\bigl(L^\beta-rL^{\beta-1}\bigr).
 \tag{3}
$$

Extend $a$ oddly near zero and the potential with a smooth cutoff
farther out. This gives a bounded $C^1$ potential and continuous
bounded force; $a(0)=0$ since $q L^\beta\to0$. Its derivative on the
positive side is

$$
 a'(q)=\Omega^2\left[L^\beta-\frac{3\beta}{2}L^{\beta-1}
              +\frac{\beta(\beta-1)}2L^{\beta-2}\right],
 \tag{4}
$$

which diverges for every $\beta>0$. Thus none of these forces is
locally Lipschitz at zero.

Nevertheless the energy-zero speed and arrival integral are exact:

$$
 \dot q=\Omega qL^r,\qquad
 \mathcal T(q)=\frac1\Omega\int_L^\infty u^{-r}\,du.
 \tag{5}
$$

Consequently rest is unique for $\beta\le2$. For $\beta>2$,

$$
 \mathcal T(q)=\frac{L^{1-r}}{\Omega(r-1)},\qquad
 Q(t)=\ell\exp\left(-[\Omega(r-1)t]^{-1/(r-1)}\right).
 \tag{6}
$$

The formula for $Q$ is valid until the departure leaves the region
where (3) is used. It is flat to every order at $t=0$, so an exactly
resting body and one that leaves after a delay satisfy the same
Newton equation and initial data.

For $\beta\le2$ the *whole* extended IVP is unique. Away from zero
this is ordinary local Lipschitz uniqueness. At zero with nonzero
initial velocity, the conserved-energy first-order equation has a
nonzero square root and a $C^1$ right-hand side near the crossing, so
it gives unique passage. At zero velocity the arrival criterion applies.
Bounded force then gives a global reversible point flow. Its dependence
on initial state is continuous: common finite-time bounds give
compactness for any converging initial sequence; every subsequential
limit solves the same unique IVP. Thus all subsequences have the same
limit. A divergent local slope has not destroyed reversible mechanics.

At the borderline $\beta=2$, the outgoing energy-zero solution from
$q_0>0$ is particularly informative:

$$
 q(t)=\ell\left(\frac{q_0}{\ell}\right)^{e^{-\Omega t}},
 \qquad \dot q(0)=\Omega q_0\log(\ell/q_0).
 \tag{7}
$$

While it remains in the logarithmic region, it stays continuous as
$q_0\downarrow0$ at every fixed finite time,
although its position sensitivity diverges. This is a genuine example
of unique stable motion without a Lipschitz dependence bound at rest.

The general first-order Osgood sufficient test applied directly to a
modulus of size $s[\log(1/s)]^\beta$ reaches only $\beta\le1$.
The stronger range $1<\beta\le2$ above uses the conservative Newton
structure and energy; failure of that first-order sufficient test is
not a proof of nonuniqueness.

## 3. The scale-by-scale meaning for Newton polygons

Let $q_n=\ell e^{-n}$ with $n$ sufficiently large. Along the zero-energy
trajectory, the time for the annulus $q_{n+1}<q<q_n$ is

$$
 \tau_n=\frac1\Omega\int_n^{n+1}u^{-r}\,du,
 \qquad \tau_n\sim\frac1{\Omega n^r}.
 \tag{8}
$$

On this annulus the local acceleration slope bound is of order
$\Lambda_n=\Omega^2n^\beta$. The short-cell scale
$\Lambda_n^{-1/2}$ is therefore of the same order as $\tau_n$.
One can subdivide an annulus crossing into a fixed number of shorter
steps to obtain a small local Lipschitz amplification parameter.
There is no uniform slope bound across all annuli.

The issue is whether infinitely many controlled annulus crossings
can fit into finite physical time:

$$
 \sum_{n\ge N}\tau_n
 \begin{cases}
 =\infty,&\beta\le2,\\
 <\infty,&\beta>2.
 \end{cases}
 \tag{9}
$$

For $\beta\le2$, a zero-energy trajectory cannot reach the infinite-depth
boundary at zero in finite time. For $\beta>2$, perfectly regular
motion on each finite collection of annuli reaches that boundary in
finite time, and the branch datum is missing there. Local estimates
at every finite scale do not by themselves control their infinite
composition. This is the useful multiscale connection with the
Balaban lesson; it is not a transfer of his field-theory proof.

For the unique regime, arbitrary-mesh Euler polygons, and the lesson's
mixed kick--drift polygons, converge uniformly on every fixed finite
time interval. Bounded force gives common position and momentum bounds;
uniform continuity gives a vanishing integral residual; compactness
supplies solution subsequences; uniqueness makes the whole family
converge. No $O(\text{mesh})$ rate is asserted here.

In the nonunique regime, exact zero initial data make these deterministic
polygons remain at rest on every partition. However, preparations
$q_0\downarrow0$, $\dot q_0=\Omega q_0L_0^r\downarrow0$ have

$$
 L(t)=\left[L_0^{1-r}+\Omega(r-1)t\right]^{-1/(r-1)}
       \longrightarrow [\Omega(r-1)t]^{-1/(r-1)}.
 \tag{10}
$$

Thus they converge to the nonzero departure (6) at fixed small $t>0$.
For each positive $q_0$, choose a fine enough polygon to approximate
that regular trajectory; a diagonal sequence then has vanishing mesh
and vanishing initial error but a departing limit. Refinement is not
jointly stable with preparation refinement at zero. This is a stronger
failure than an unbounded numerical error estimate, while keeping the
exact-zero polygon's resting limit explicit.

## 4. What happens to action, with hbar kept explicit?

The positive outgoing momentum is $p(q)=m\Omega qL^r$. Its canonical
action from zero to $q$ is

$$
 \mathcal J(q)=\int_0^q p(s)\,ds
       =m\Omega\ell^2\int_L^\infty e^{-2u}u^r\,du.
 \tag{11}
$$

For $L>r/2$, elementary bounds give

$$
 \frac{m\Omega}2q^2L^r
 \le\mathcal J(q)
 \le\frac{m\Omega q^2L^r}{2-r/L}.
 \tag{12}
$$

The lower bound uses $u^r\ge L^r$; the upper bound uses
$(L+v)^r\le L^r e^{rv/L}$ after writing $u=L+v$. Therefore
$\mathcal J(q)\sim(m\Omega/2)q^2L^r\to0$ for every $\beta>0$.
The temporal threshold (9) creates no positive action threshold.

There is still a concrete quantum comparison. In the local region
$V=-p(q)^2/(2m)$, take the stationary energy-zero test functions

$$
 \psi_\pm(q)=p(q)^{-1/2}
          \exp\left(\pm\frac{i}{\hbar}\mathcal J(q)\right),
 \qquad H_\hbar=-\frac{\hbar^2}{2m}\frac{d^2}{dq^2}+V(q).
 \tag{13}
$$

Their eikonal and first-derivative transport terms cancel exactly.
Writing $b(q)=p(q)^{-1/2}$ gives $H_\hbar\psi_\pm
=-(\hbar^2/2m)b''e^{\pm i\mathcal J/\hbar}$ and the exact local ratio

$$
 \frac{|H_\hbar\psi_\pm|}{|V\psi_\pm|}
 =\left[\frac{\hbar}{m\Omega q^2L^r}\right]^2
       \left|\frac34-\frac rL+\frac{r(r+2)}{4L^2}\right|
 \sim\frac{3\hbar^2}{16\mathcal J(q)^2}.
 \tag{14}
$$

For example, the differentiation behind this identity is
$p'/p=(1-r/L)/q$ and
$p''/p=-r[1-(r-1)/L]/(q^2L)$; then
$b''/b=3(p'/p)^2/4-p''/(2p)$.
Equation (14) is a local residual identity, not an error bound for
a normalized state or the full propagator.

At fixed $\hbar>0$, action comparable with $\hbar$ makes the local
residual of this trajectory ansatz order one even in the classically
unique regime. Every
sufficiently small positive $\hbar$ defines a radius $q_\hbar$ by
$\mathcal J(q_\hbar)=\hbar$, and that radius tends to zero as
$\hbar\to0$. The bounded-potential Hamiltonian has global unitary
dynamics at each positive $\hbar$ by the cusp note's held
Kato--Rellich input. These facts neither require $\hbar=0$ to be a
member of the same state theory nor select a positive numerical lower
bound across the family. No relativistic ingredient or $c$ is used.

## 5. Consequence for STATE

The ODE lesson's Lipschitz proof is sufficient, not necessary. A sharper
conservative criterion identifies exactly when this logarithmic force
family has full point-state mergers, so the preparation-floor theorem
must invoke genuine finite-time accessibility rather than unbounded
slope. Scale-by-scale time control and action control are different:
the crossing-time sum changes at $\beta=2$ while the local action tends
to zero throughout. The open physical step remains selection of
admissible preparations, records and a common positive phase scale.
