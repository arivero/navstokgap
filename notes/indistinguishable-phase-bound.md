# A sharp information bound from indistinguishable motions

Bounded-force reachability and noisy differentiation fit into one exact
minimax argument. A symmetric reachable fibre determines the worst record;
an explicit force-controlled pair attains the two-record upper bound, even
when the observer instead receives the entire noisy position history.

R11, 2026-09-10. C078–C079 accepted by
[written review](../reviews/indistinguishability-B42.md).
[B42](../references/batches/B42.md) matches the prepared zero-initial-state
pair to Seeber–Haimovich, Proposition 3.1, equations (10)–(12). The mechanical
notation and blind-delay extension reuse that established construction.
Keep $m,F,T>0$ and known initial state $(q_0,p_0)$.
All measurable forces satisfy $|f|\le F$. Position records have deterministic
absolute error at most $\varepsilon>0$ and are available through $t_2=T-b$,
where $b\ge0$ is a blind prediction interval. There is no stochastic law or
measurement disturbance. Canonical error products have action units, without
a $2\pi$ normalization.

## 1. Convex symmetry turns reachability into minimax risk

Let $U$ be a compact convex centrally symmetric set of admissible force
histories or their finite-dimensional integral images. After subtracting the
known inertial solution, let the continuous linear maps $A u$ and $L u$ give
the sampled positions and one scalar terminal coordinate. Allowed records are $y=A u+e$ with
$|e_i|\le\varepsilon_i$. Define

$$r_L=\max\{|Lu|:u\in U,\ |(Au)_i|\le\varepsilon_i\}.$$

Then the minimax worst-case absolute error, over all deterministic estimators
using $y$, is exactly $r_L$. Indeed any two inputs $u,v$ compatible with the
same record satisfy $(u-v)/2\in U$ and
$|A(u-v)/2|\le\varepsilon$. Their output separation is at most $2r_L$.
The midpoint of the compatible output interval therefore has error at most
$r_L$. Conversely $u$ and $-u$ realizing $r_L$ share the zero record, with
errors $-Au$ and $Au$, and their outputs differ by $2r_L$. Every estimator
must incur error at least $r_L$ on one of them.

For the bounded-force model, the $L^\infty$ ball is weak-star compact and all
the required integrals are continuous in that topology; its finite-dimensional
image is compact. The same argument applies to continuous position records
with a pointwise error band: the central feasible set imposes the inequalities
at every observed time. Thus shared initial data and joint force compatibility
can be retained throughout. This is an optimal-recovery principle, not a new
force law.

## 2. An explicit pair with the same complete record

Set

$$d=2\sqrt{\frac{m\varepsilon}{F}},\qquad
t_1=t_2-d,\qquad t_2\ge2d.$$

Construct a displacement $g$ from the inertial trajectory, with $g(0)=g'(0)=0$.
It stays zero until $t_1-d$. Over the next two half-intervals of length $d/2$,
apply force $-F$ and then $+F$. This ends at

$$g(t_1)=-\frac{Fd^2}{4m}=-\varepsilon,\qquad mg'(t_1)=0.$$

Continue with $+F$ for time $d$, and then through the blind interval $b$.
Writing $\tau=t-t_1$ on the middle segment,

$$g(t)=-\varepsilon+\frac{F\tau^2}{2m},\qquad 0\le\tau\le d.$$

Hence $g(t_2)=+\varepsilon$, $mg'(t_2)=Fd=2\sqrt{mF\varepsilon}$,
and $|g(t)|\le\varepsilon$ throughout $[0,t_2]$. During preparation its
position decreases monotonically from zero to $-\varepsilon$; the last
segment increases monotonically to $+\varepsilon$.

The trajectories $q_\pm(t)=q_0+p_0t/m\pm g(t)$ have identical initial
state and admissible opposite forces. Both admit the **same complete record**
$y(t)=q_0+p_0t/m$, by choosing noise $e_\pm(t)=\mp g(t)$ through $t_2$.
In particular they share the records at $t_1,t_2$. Their terminal deviations
from the inertial motion are opposite, with magnitudes

$$P_*=Fd+Fb=2\sqrt{mF\varepsilon}+Fb,$$

$$Q_*=\varepsilon+\frac{Fdb}{m}+\frac{Fb^2}{2m}.$$

## 3. Exact risks for two records and for the complete history

The shared record forces every estimator's global worst-case momentum error
to be at least $P_*$ and position error to be at least $Q_*$. These are
separate coordinate risks; the product does not assert a simultaneous lower
bound on both actual errors for every individual motion or estimator.

[R10](two-position-recovery.md)'s estimator, using just $t_1,t_2$ with
separation $d$, attains upper bounds $P_*,Q_*$ for every admissible record.
Therefore

$$\boxed{R_p^{\rm opt}=P_*,\qquad R_q^{\rm opt}=Q_*}$$

for both information classes: the two fixed records and the entire noisy
history through $t_2$. One estimator attains both coordinate optima. Extra
samples cannot improve the minimax risks under arbitrary bounded noise because
the same entire history already hides the extremal pair.

At zero blind delay, the product of coordinate minimax risks is exactly

$$\mathcal H_\varepsilon=R_q^{\rm opt}R_p^{\rm opt}
=2\sqrt{mF}\,\varepsilon^{3/2}>0.$$

The timing assumption is $T-b\ge4\sqrt{m\varepsilon/F}$. It provides time
to create the hidden displacement from the shared initial state; shorter
horizons are a separate finite-horizon problem. For $p_0=0$, the constructed
pair satisfies $|\dot q|<c$ whenever $F(d+b)/m<c$. This speed check applies
to the pair; imposing a speed ceiling on the whole model requires rechecking
attainability and the estimator domain.

## 4. What the connection contributes

The force ceiling supplies regularity, the record band supplies unresolved
alternatives, and convex symmetry supplies an exact worst-record construction.
The information gap survives arbitrary insertion of observed time cuts at
fixed precision. It closes as $\varepsilon,b\to0$ and depends on $m,F$:
the positivity comes from a physical resource premise still to be selected.

This identifies a useful bridge toward the main target: prove an apparatus
restriction on attainable record bands and delays, then use minimax recovery
to transfer it to a lower bound. The resulting quantity must next pass a
composition test. A08's universality theorem concerns variances; its
mass-weighted addition law cannot be applied directly to worst-case errors.
R12 will compare these two forms of composition in one stated information model.
