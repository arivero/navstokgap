# The Newton cusp: classical histories, conditional floors and records

**Maintained conclusions.** A bounded continuous conservative force merges two
full point states in finite time. Two different conditional preparation theorems
then force a positive covariance action: one assumes reversible evolution on
instantaneous phase laws, canonical covariance and weak closure; the other
assumes actual Gaussian cusp transport, $W_2$ closure, copying and continuity at
one positive time. Neither theorem identifies that floor with physical $\hbar/2$.
Their classical density and entropy witnesses carry supplied scales.

There is also an exact zero-floor classical completion on complete trajectories.
It preserves past and future branch information beyond the instantaneous phase
point. Arbitrarily fine nondisturbing joint records force a zero covariance
infimum. These countermodels delimit the preparation theorems; they do not
contradict their explicitly different state and instrument assumptions.

The reversible theorem constrains point transport **only if points are admitted**.
A positive-floor Gaussian class with identity evolution satisfies that clause
vacuously and is not physical cusp transport. The continuity theorem below
instead constrains actual nonpoint transport. Quantum existence at every supplied
$\hbar>0$, quantum instruments, and universality of a measured action constant
remain separate questions.

The solution-space construction has prior context in
[Sell 1973](https://doi.org/10.1016/0022-0396(73)90075-2) (publisher abstract).
Vanishing classical uncertainty and branch probabilities belong to spontaneous
stochasticity; see [Eyink--Drivas 2015](https://arxiv.org/abs/1509.04941) and
[Vanpoucke--Wenmackers 2021](https://doi.org/10.1063/5.0063388) (author abstracts).
The proofs below are written arguments using their stated analytic inputs;
internal model checks are not independent peer review. No priority is claimed.
The [classical construction](balaban-ode-lesson.md) distinguishes actual mergers
from an unbounded force slope or an endpoint caustic.

## 1. Existence without uniqueness, with no unbounded force

Fix $m,\gamma,R>0$, $0<\alpha<1$, and a smooth even cutoff $\chi$ with
$0\le\chi\le1$, $\chi=1$ on $[-1,1]$ and $\chi=0$ outside $[-2,2]$.
Set

$$
 V(q)=-\frac{\gamma}{1+\alpha}|q|^{1+\alpha}\chi(q/R),
 \qquad \dot q=p/m,\quad \dot p=-V'(q).
 \tag{1}
$$

The potential is bounded and $C^1$, and the force is continuous and
bounded. Specifically,

$$
 \|V\|_\infty\le\frac{\gamma(2R)^{1+\alpha}}{1+\alpha},\qquad
 \|V'\|_\infty\le\gamma(2R)^\alpha
 \left(1+\frac{2\|\chi'\|_\infty}{1+\alpha}\right)=:F_*.
 \tag{2}
$$

Inside $|q|<R$, the acceleration is
$\ddot q=(\gamma/m)\operatorname{sgn}(q)|q|^\alpha$. Its derivative
diverges at zero, so the Lipschitz hypothesis in the lesson fails.
Nevertheless solutions exist globally. Here is the relevant existence
argument without assuming uniqueness. Euler polygons on a fixed finite
time interval have uniformly bounded momentum and position, and are
equi-Lipschitz. On their common compact range the continuous vector
field is uniformly continuous, so their integral-equation residual
tends uniformly to zero with the mesh. A uniformly convergent
subsequence therefore solves (1). The bounds

$$
 |p(t)|\le |p(0)|+F_*|t|,\qquad
 |q(t)|\le |q(0)|+\frac{|p(0)|}{m}|t|+\frac{F_*t^2}{2m}
 \tag{3}
$$

prevent finite-time escape and allow successive continuation in either
time direction. This is an existence construction by compactness,
rather than the Lipschitz lesson's Cauchy construction of a unique limit.

Put

$$
 \beta=\frac{2}{1-\alpha}>2,\qquad
 B=\left[\frac{\gamma(1-\alpha)^2}{2m(1+\alpha)}
     \right]^{1/(1-\alpha)}.
 \tag{4}
$$

The curves $q(t)=\pm B(t-t_0)^\beta$, preceded by rest at zero,
solve (1) while their positions remain inside $(-R,R)$. They join
with two continuous derivatives at $t_0$. Rest and an arbitrary delay
before either departure are therefore all permitted by the same initial
datum $(q,p)=(0,0)$. Direct substitution uses
$\beta-2=\alpha\beta$ and
$B^{1-\alpha}=\gamma/[m\beta(\beta-1)]$.

More decisively, choose $s>0$ with $Bs^\beta<R$. The two different
incoming states

$$
 z_\pm=(\pm Bs^\beta,\ \mp m\beta Bs^{\beta-1})
 \tag{5}
$$

have the unique trajectories
$q_\pm(t)=\pm B(s-t)^\beta$, $p_\pm=m\dot q_\pm$ for $0\le t<s$:
the vector field is locally Lipschitz wherever $q\ne0$. Both reach
$(0,0)$ at time $s$. These are mergers of the full canonical state,
rather than caustics of its position projection.

**Point-state obstruction.** No injective evolution at time $s$ on the
original $(q,p)$ states can follow both trajectories through their
arrival. A later choice of departure cannot undo the earlier merger.
An extra arrival or branch label can retain the information, but is an
enlargement of this state space.

For the path limits below write $k=1+\alpha$, $\lambda=\gamma/(1+\alpha)$,
and $\Gamma_\pm(t)=(\pm Bt^\beta,\pm m\beta Bt^{\beta-1})$ for
$BT^\beta<R$. Fix calibration units $L_0,P_0>0$, $S_0=L_0P_0$, and
$z=(q/L_0,p/P_0)$. These units do not impose a physical bound.

## 2. The trajectory-state completion

Let $\Omega$ be the set of all globally defined solutions of the bounded cusp equation, viewed
as functions $\gamma:\mathbb R\to\mathbb R^2$ with the topology of uniform
convergence on compact intervals. Write $e_t(\gamma)=\gamma(t)$ and

$$
 (T_s\gamma)(t)=\gamma(t+s),\qquad
 (\Theta\gamma)(t)=\bigl(q(-t),-p(-t)\bigr). \tag{H4}
$$

**Theorem 1.** $\Omega$ is a nonempty Polish space. The maps $T_s$ form
a jointly continuous group of homeomorphisms and $\Theta$ is a continuous
involution satisfying $\Theta T_s\Theta=T_{-s}$. Every $e_0$-fiber is
nonempty and compact. The state class $\mathcal P(\Omega)$ of all Borel
probabilities has weakly continuous reversible evolution
$\mu\mapsto(T_s)_*\mu$, contains point states, and supports ordinary
classical conditioning on any Borel trajectory record of positive
probability. Its instantaneous phase laws comprise all Borel probabilities
on $\mathbb R^2$; in particular their covariance-action infimum is zero.

*Proof.* The integral form of the bounded cusp equation is preserved by local-uniform limits:
on each compact time interval the convergent paths have a common compact
range, and the continuous vector field is uniformly continuous there.
Thus $\Omega$ is closed in the Polish compact-open space
$C(\mathbb R,\mathbb R^2)$. Time translations and time reversal preserve
the autonomous equation and have the asserted algebra and continuity.

Given a compact set of initial points, the bounded-force estimates above give locally uniform bounds on $q,p$ and their derivatives.
Arzelà--Ascoli, a diagonal subsequence and closedness give compactness of
$e_0^{-1}(K)$. Global existence makes every fiber nonempty. Pushforward
by the continuous time shifts gives the group on $\mathcal P(\Omega)$;
for each bounded continuous test function, dominated convergence proves
weak continuity in time. Ordinary restriction and normalization give the
stated conditioning rule.

For the marginal claim, the proper continuous surjection $e_0$ has a
Borel section $s:\mathbb R^2\to\Omega$. One justification is the
Kuratowski--Ryll-Nardzewski measurable-selection theorem
([statement](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/30345D24D3DFFAAF9CE805C30EE959C6/S0008414X00041699a.pdf/some_selection_theorems_for_measurable_functions.pdf),
theorem statement read): the compact-valued fiber map is Borel-measurable,
since the image under a proper map of a closed set is closed and an open
set in a metric space is a countable union of closed sets. Hence $s_*\nu$
is a history preparation with instantaneous marginal $\nu$ for any
$\nu\in\mathcal P(\mathbb R^2)$. A Dirac history has a Dirac instantaneous
marginal, with $\kappa=0$. $\square$

The theorem constructs reversible *history* evolution, not a reversible
map on laws of $(q,p)$ alone. Take two histories that arrive at the cusp
from opposite sides. At their common arrival time their instantaneous
marginals are both $\delta_{(0,0)}$, while the full states and their pasts
remain distinct. The resting history and a departing history have the same
instantaneous marginal at time zero but different future marginals, so no
single map on phase laws can represent the shift for all history states.
Moreover, the resting solution and the two solutions
which leave after any prescribed delay $a\ge0$ have the same entire
$(q,p)$ past up to time zero but different futures. Thus a deterministic
completion representing all these possibilities must carry information
beyond that past. In (H4) the chosen future is part of the state. The
construction does not show that this information has a finite-dimensional,
local Hamiltonian realization or is accessible to a physical observer.

Because the phase marginal class is all of $\mathcal P(\mathbb R^2)$, it
is weakly closed, affine-canonically invariant, and closed under classical
product preparations, canonical mixing and marginalization **as a class of
single-time laws**. The Borel section is a state-preparation selection;
it is not a proof of a reversible canonical mixer acting on the enlarged
history states. Nor does the instantaneous marginal determine its later
law. The preparation-floor theorem explicitly assumes that a reversible
evolution acts on those marginals themselves; Theorem 1 does not satisfy
that premise, so the two results are consistent.

## 3. A continuous classical family with nonuniform zero-width limit

Let $X,Y$ be independent standard normal variables. For fixed $u\in\mathbb R$
and $\epsilon>0$, prepare

$$
 q_0=\epsilon L_0(u+X),\qquad p_0=\epsilon P_0Y. \tag{H5}
$$

The energy-zero set is Lebesgue-null, so (H5) selects unique global
trajectories almost surely. Equivalently, lift the law by the section $s$:
different choices of $s$ agree almost surely here. Let $\Phi$ denote the
standard normal distribution function.

**Theorem 2.** Let $0<T<(R/B)^{1/\beta}$. As $\epsilon\to0$, the initial
law of (H5) converges weakly to $\delta_{(0,0)}$ for every fixed $u$, and

$$
 \kappa_\epsilon=S_0\epsilon^2,\qquad
 \operatorname{Law}\bigl((q(t),p(t))_{0\le t\le T}\bigr)
 \Longrightarrow
 \Phi(u)\,\delta_{\Gamma_+}+\Phi(-u)\,\delta_{\Gamma_-}
 \quad\text{in }C([0,T],\mathbb R^2). \tag{H6}
$$

Every mixture weight strictly between zero and one is obtained by a fixed
$u$. For either pure branch one may instead take $u=u_\epsilon\to\pm\infty$
with $\epsilon|u_\epsilon|\to0$. The distributions are classical
ensembles of Newton trajectories, with no supplied $\hbar$.

*Proof.* The first limit and covariance are immediate. Fix a realization
with $u+X\ne0$ and finite $Y$. Its initial energy is, for small $\epsilon$,

$$
 E_\epsilon=\frac{\epsilon^2P_0^2Y^2}{2m}
            -\lambda\,|\epsilon L_0(u+X)|^k<0. \tag{H7}
$$

Indeed $k<2$. Thus it cannot reach $q=0$, so its sign remains that of
$u+X$. Its turning distance $a_\epsilon=(-E_\epsilon/\lambda)^{1/k}$ satisfies
$0<a_\epsilon\le|q_0|$, and tends to zero. Inside $|q|<R$, separation of
the energy equation gives the time from the turning point to $r\ge a$:

$$
 I_a(r)=\sqrt{\frac{m}{2\lambda}}\int_a^r
              \frac{dv}{\sqrt{v^k-a^k}}. \tag{H8}
$$

For fixed $0<r<R$, $I_a(r)\to I_0(r)$ as $a\downarrow0$, where

$$
 I_0(r)=\sqrt{\frac{m}{2\lambda}}\frac{2}{1-\alpha}
                    r^{(1-\alpha)/2},\qquad I_0^{-1}(t)=Bt^\beta.
 \tag{H9}
$$

For the convergence, the part from $a$ to $2a$ is
$O(a^{(1-\alpha)/2})$; on $v\ge2a$ the integrand is dominated by a
constant times $v^{-k/2}$, which is integrable at zero. Moreover,

$$
 I_a(r)\le \sqrt{\frac{m}{2\lambda}}\frac{2}{1-\alpha}
                 (r-a)^{(1-\alpha)/2}, \tag{H10}
$$

since $v^k-a^k\ge(v-a)^k$ for $k>1$. Hence the time from the initial
point to its turning point is $I_{a_\epsilon}(|q_0|)\to0$. The outward
time to any fixed $r$ is $I_{a_\epsilon}(r)$ plus or minus this vanishing
initial term. Bracketing fixed times by the hitting times of two nearby
radii proves $q(t)\to\operatorname{sgn}(u+X)Bt^\beta$ for each $t>0$.
The energy equation gives the corresponding momentum limit, with outward
sign. For $T$ as stated the limiting path remains inside $|q|<R$; the
same hitting-time argument keeps the approximating paths there for all
sufficiently small $\epsilon$.

The bounded-force estimates give equicontinuity of both coordinates on
$[0,T]$, so the pointwise convergence is uniform there. It holds for almost
every $(X,Y)$, and bounded convergence of continuous path functionals
gives (H6). If $u_\epsilon\to\pm\infty$ with
$\epsilon|u_\epsilon|\to0$, the same argument has eventual fixed sign for
each $(X,Y)$ and gives the corresponding pure branch. $\square$

**Fixed-width continuity.** Let $\mu_{z,\epsilon}=s_*\mathcal N(z,\epsilon^2I)$
on $\Omega$, with $z$ dimensionless. For all centers $z,w$ and every $t$,

$$
 \bigl\|(T_t)_*\mu_{z,\epsilon}-(T_t)_*\mu_{w,\epsilon}\bigr\|_{\rm TV}
 \le \frac{|z-w|}{\sqrt{2\pi}\,\epsilon}. \tag{H11}
$$

Here total variation is the supremum over measurable events. Pushforward
cannot increase it. For the Gaussian bound, interpolate its center along
the line from $z$ to $w$ and integrate the absolute directional derivative:
half its integral is $1/(\sqrt{2\pi}\epsilon)$ per unit center distance.
Equation (H11) applies to any subsequent fixed measurable record, including
a complete history record. Its constant diverges as $\epsilon\downarrow0$.

The divergence cannot be removed uniformly. Fix $0<t<T$ and a bounded
continuous $f$ with $f(Bt^\beta)=1$ and $f(-Bt^\beta)=0$; a clipped
linear function suffices. For the two centers $z_\pm=(\pm\epsilon,0)$,
Theorem 2 gives

$$
 \lim_{\epsilon\downarrow0}
 \left[\mathbb E_{z_+,\epsilon}f(q(t))-
       \mathbb E_{z_-,\epsilon}f(q(t))\right]
 =2\Phi(1)-1>0. \tag{H12}
$$

The two initial centers are only $2\epsilon$ apart. Thus no common modulus
of continuity tending to zero can hold for these responses as $\epsilon$
varies. A uniform response modulus would exclude the zero-width sequence;
it is an extra physical premise, not a consequence of continuity at each
fixed width. More concretely, if the absolute response difference is
bounded by $L|z-w|$ for some $L>0$, uniformly over all allowed widths,
and both translated preparations at each such width are admitted, (H12)
implies an
$\epsilon_0>0$ such that widths below
$\min\{\epsilon_0,[2\Phi(1)-1]/(4L)\}$ are excluded for this family.
This conditional bound does not identify $S_0\epsilon^2$ with $\hbar$ and
does not establish the response premise for physical records.

**Corollary.** No evolution on phase-space probability laws which agrees
with the actual Newton transport of all the Gaussian laws (H5) can be weakly
continuous at $\delta_{(0,0)}$ at any fixed $t\in(0,T)$. Indeed all the
inputs have that same weak limit while (H6) gives distinct output limits
for different $u$. This obstruction does not require injectivity or a
rule for the exact point at the origin. It does require the indicated
Gaussian preparations and their actual cusp transport.

## 4. Reversible instantaneous preparations

Let $\mathcal S$ be a nonempty subset of probability measures on the
canonical plane, containing at least one measure with finite covariance.
Assume the following three properties.

1. **Canonical covariance of preparations.** Every affine symplectic
   pushforward of a member of $\mathcal S$ belongs to $\mathcal S$.
   In one canonical pair the linear matrices have determinant one.
   This is a premise about admissible states, not a claim that the
   particular potential (1) is invariant under all these maps.
2. **Weak closure.** A probability-valued weak limit of a sequence in
   $\mathcal S$ belongs to $\mathcal S$.
3. **Reversible point-trajectory compatibility.** The force (1) admits bijective
   preparation evolutions $\mathcal E_t$ on $\mathcal S$, with weakly
   continuous state curves. Whenever a point preparation is admitted,
   its evolution follows its unique Newton trajectory before arrival
   at the cusp. No affineness assumption on $\mathcal E_t$ is needed
   for the conclusion below.

For a finite-covariance preparation write

$$
 \kappa(\mu)=\sqrt{\det\operatorname{Cov}_\mu(q,p)}.
 \tag{6}
$$

This has action units. The theorem concerns covariance, including its
cross term, rather than the coordinate product alone.

**Theorem R.** Under properties 1--3,

$$
 0<\kappa_*:=\inf_{\substack{\mu\in\mathcal S\\
                         \mu\text{ has finite covariance}}}
                   \kappa(\mu)<\infty.
 \tag{7}
$$

*First step: point preparations are excluded.* If one Dirac measure
belongs to $\mathcal S$, affine translations supply every Dirac
measure, in particular $\delta_{z_+}$ and $\delta_{z_-}$. Property 3
and weak time continuity then give

$$
 \mathcal E_s\delta_{z_+}=\delta_{(0,0)}
                        =\mathcal E_s\delta_{z_-},
 \tag{8}
$$

contradicting injectivity. Thus $\mathcal S$ contains no Dirac measure.

*Second step: arbitrarily small covariance action would supply a point.*
For clarity fix arbitrary calibration units $L_0,P_0>0$, with
$S_0=L_0P_0$, and use dimensionless coordinates
$(Q,P)=(q/L_0,p/P_0)$. If (7) failed, choose preparations with
dimensionless covariance matrices $C_n\ge0$ and
$\sqrt{\det C_n}=\kappa(\mu_n)/S_0\to0$. Subtract each mean.
Choose $\epsilon_n>0$ so that

$$
 \sqrt{\det D_n}\longrightarrow0,\qquad D_n=C_n+\epsilon_n I>0,
 \qquad A_n=(\det D_n)^{1/4}D_n^{-1/2}.
 \tag{9}
$$

Such a choice follows from continuity of determinant at each $C_n$;
it also handles rank-deficient covariances. Then $\det A_n=1$ and

$$
 A_nC_nA_n^{\mathsf T}\le\sqrt{\det D_n}\,I.
 \tag{10}
$$

These dimensionless determinant-one maps represent physical canonical
maps in the calibrated coordinates. By property 1 the centered,
transformed preparations $\widetilde\mu_n$ remain admissible. For
every fixed $r>0$, Chebyshev's inequality gives

$$
 \widetilde\mu_n\{Q^2+P^2>r^2\}
 \le\frac{2\sqrt{\det D_n}}{r^2}\longrightarrow0.
 \tag{11}
$$

Hence $\widetilde\mu_n$ converges weakly to the point measure at zero.
Property 2 admits that point, contrary to the first step. The assumed
finite-covariance member also makes the infimum finite. $\square$

No calibrated numerical value is hidden in $L_0,P_0$: their positive
values are arbitrary and (7) is unchanged by changing them. The state
class supplies the value of $\kappa_*$. The theorem does not establish
that the infimum is attained, that Gaussian states are allowed, or that
all states above the floor are allowed. It needs neither a Gaussian
ansatz nor closure under adding Gaussian noise.

One may define $\hbar_{\rm prep}=2\kappa_*>0$ as a candidate reduced
action scale. Identifying it with the phase constant $\hbar$ needs a
separate physical argument. In quantum mechanics the familiar
Robertson--Schrödinger form is $\det\operatorname{Cov}(q,p)\ge\hbar^2/4$;
the equality of forms alone proves no identification. The full Planck
constant would be $h=2\pi\hbar$, not $\hbar$.

### Which assumptions do the work?

Without weak closure, excluding exact points leaves preparations with
arbitrarily small covariance. For example, the class of all absolutely
continuous phase-space probabilities is canonically invariant, has no
Dirac members, and contains arbitrarily narrow Gaussians. Its weak
closure includes points. Thus the conclusion is not obtained merely
by replacing points with distributions.

Without canonical squeezing, a class supported on a fixed line with a
fixed nonzero extent may be weakly closed and contain no point while
having zero covariance determinant. Canonical covariance rules out
that degenerate evasion. Without the cusp-compatibility demand, all
probabilities are weakly closed and canonically invariant and contain
points; free and harmonic dynamics transport them reversibly.

Weak closure is not a consequence of finite experimental resolution.
It is an additional completion rule admitting concentration limits
whenever they are weak probability limits. Requiring it while retaining
all arbitrarily concentrated classical preparations is exactly what
would reintroduce the forbidden point. Whether nature supplies this
closure, the full canonical preparation class, and the exact cusp
force is open. Restricting all forces to smooth Lipschitz laws removes
this particular selector.

## 5. A continuity selector without reversibility

The Gaussian branch-limit corollary yields a different conditional action theorem.
It uses actual Newton transport of nonpoint preparations, rather than
compatibility only for point preparations if any exist.

**Theorem 3.** Use the $W_2$ metric in the calibrated coordinates, and
let $\mathcal S\subset\mathcal P_2(\mathbb R^2)$ satisfy:

1. $\mathcal S$ contains a state with positive-definite covariance and
   is invariant under affine canonical transformations.
2. $\mathcal S$ is closed under $W_2$ convergence. Independent finite
   products of members, followed by copy-index orthogonal canonical mixing
   and retention of one output pair, produce members of $\mathcal S$, as
   specified in §1 of the
   [central-limit note](central-limit-canonical-gaussian-sector.md).
3. At one fixed $t\in(0,(R/B)^{1/\beta})$, there is a map
   $\mathcal E_t:\mathcal S\to\mathcal P(\mathbb R^2)$ which is continuous
   from $W_2$ convergence of inputs to weak convergence of outputs. For
   every nondegenerate Gaussian member of $\mathcal S$, its output is the
   actual almost-everywhere Newton transport under the bounded cusp equation.

Then the infimum of $\kappa$ on $\mathcal S$ is strictly positive. The
map $\mathcal E_t$ need not be invertible, form a semigroup, or map back
into $\mathcal S$ for this conclusion.

*Proof.* Work in calibrated coordinates. Suppose the infimum is zero and
choose states with covariance matrices $C_n$ and $\det C_n\to0$. Translate
their means to zero. Choose $\eta_n>0$ such that
$D_n=C_n+\eta_n I$ has $\det D_n\to0$, and put
$A_n=(\det D_n)^{1/4}D_n^{-1/2}$. In one pair $\det A_n=1$, and

$$
 A_nC_nA_n^{\mathsf T}\le\sqrt{\det D_n}\,I. \tag{H12a}
$$

The transformed admissible states have second moment tending to zero,
so they converge to $\delta_0$ in $W_2$; closure admits $\delta_0$.

By the central-limit result, a positive-definite covariance member yields
an admissible Gaussian with the same covariance. Translation and a
determinant-one transformation give an admissible
$G=\mathcal N(0,\zeta I)$ for some $\zeta>0$. For each $n$, take one
independent copy of $G$ and $n-1$ copies of $\delta_0$, then use an
orthogonal copy-index mixer whose first row is $(1,\ldots,1)/\sqrt n$.
The retained pair has law $\mathcal N(0,(\zeta/n)I)$. Translations
therefore admit both Gaussian inputs (H5) with
$\epsilon_n=\sqrt{\zeta/n}$ and $u=\pm1$.

Both input sequences converge to $\delta_0$ in $W_2$. The continuity
assumption forces their output sequences to have the same weak limit
$\mathcal E_t\delta_0$. Actual Newton transport and Theorem 2 give two
different branch mixtures instead. This is a contradiction. $\square$

The assumptions are consistent in a classical model. The entropy-floor
class $\mathcal E_\zeta$ of §6 of the central-limit note has a **supplied**
$\zeta>0$, is $W_2$-closed, has the required canonical copy-index mixers,
and is transported by the actual cusp flow. Its members are absolutely
continuous. The classical flow is continuous at every initial state off
the energy-zero set: bounded-force compactness and uniqueness there give
continuous dependence. The exceptional set has Lebesgue measure zero, so
the extended continuous-mapping theorem gives weak continuity of the
transport on $\mathcal E_\zeta$ under $W_2$-convergent inputs. This provides
a nonvacuous classical witness for the full continuity premise; its
positive action is inherited from its imposed entropy bound.

The theorem therefore identifies a possible independently motivated
stability requirement and makes its consequence explicit. It does not
establish that all physical preparations obey the copy, closure and
continuity rules, or that the selected floor is universal or quantum.

## 6. Classical witnesses and their limits

Fix a finite density ceiling $M>0$, of reciprocal-action units, and let

$$
 \mathcal S_M=\{\mu:\ d\mu=\rho\,dq\,dp,\quad 0\le\rho\le M,
                                 \quad\int\rho\,dq\,dp=1\}.
 \tag{12}
$$

This class is weakly closed: if its probabilities converge weakly,
their limiting measure satisfies
$\int\phi\,d\mu\le M\int\phi\,dq\,dp$ for every nonnegative compactly
supported continuous $\phi$, which gives the same density bound.
It is invariant under affine symplectic maps because they preserve
canonical area.

For (1), the energy-zero set is the union of the two graphs
$p=\pm\sqrt{-2mV(q)}$ and has canonical area zero. Outside it the
Newton trajectory is unique and complete. Negative-energy paths cannot
reach zero; positive-energy paths cross it with nonzero velocity and
are uniquely continued by
$\dot q=\pm\sqrt{2(E-V(q))/m}$ near the crossing. Away from zero the
field is smooth. This full-area flow preserves canonical area: where
$p\ne0$, energy--time coordinates give
$dq\,dp=dE\,dt$ up to orientation, and the flow translates $t$;
turning points away from zero have the usual smooth Hamiltonian charts.
The resulting almost-everywhere group pushes $\mathcal S_M$ bijectively
to itself. Its state curves are weakly continuous by bounded convergence
along the continuous trajectories. No member charges the exceptional
zero-energy set, and no Dirac preparation is admitted. Property 3 is
therefore satisfied, including its stated point-compatibility condition.

The floor can be computed sharply:

$$
 \inf_{\mu\in\mathcal S_M\text{ with finite covariance}}
             \sqrt{\det\operatorname{Cov}_\mu(q,p)}
       =\frac{1}{4\pi M}.
 \tag{13}
$$

To check it, center and canonically isotropize a positive covariance
as in the reversible preparation proof, now without regularization. In the calibrated plane
the density cap is $M S_0$. Among probabilities with this cap the
minimum of $\mathbb E(Q^2+P^2)$ is attained by filling the disk about
zero at maximum density: moving mass from a larger radius into any
unfilled smaller radius reduces the expectation. The disk has radius
$a_0^2=1/(\pi M S_0)$ and mean square radius $a_0^2/2$. Isotropy gives
$2\kappa/S_0\ge1/(2\pi M S_0)$, proving the bound. A uniform canonical
ellipse, the image of this disk, attains equality. A singular covariance
would concentrate a density on a line and is impossible in (12).

Thus the conditional theorem is consistent and genuinely weaker than
quantum kinematics. Its classical witness already carries a supplied
scale $1/M$; the theorem says that some positive scale must appear
under its hypotheses, not how nature chooses it. It is an unread-state
model. Unrestricted classical conditioning can violate its ceiling,
as the necessity note's two-pointer construction proves. Claiming an
operational completion would also require a physical law of instruments
and records preserving its allowed states.

**Composition test, 2026-10-27.** The witness $\mathcal S_M$ is not
closed under the independent-copy canonical mixer and marginalization
used in the
[central-limit calculation](central-limit-canonical-gaussian-sector.md).
Indeed, for $f=M1_E$ with $E=-E$ and area $1/M$, the law of
$(Z_1+Z_2)/\sqrt2$ from independent copies has density
$f_+(0)=2\int f(z)f(-z)\,dz=2M$, and is continuous near zero.
The covariance and its action are unchanged for identical copies,
but the pointwise density ceiling is violated. Theorem R and
this classical single-system witness remain valid at their stated
scope; they do not establish the added multi-copy closure.

## 7. Fine records and the action floor

**Theorem 4.** Let $\mathcal S$ be a nonempty class of Borel probabilities
on the classical phase plane. Suppose that, for every $\nu\in\mathcal S$
and every bounded open ball $D$ in the calibrated $(q/L_0,p/P_0)$ plane
with $\nu(D)>0$, the ordinary conditional law $\nu(\cdot\mid D)$ is again
in $\mathcal S$. Then

$$
 \inf_{\nu\in\mathcal S,\ \operatorname{Cov}\nu<\infty}
 \sqrt{\det\operatorname{Cov}_\nu(q,p)}=0. \tag{H13}
$$

If $\mathcal S$ is also weakly closed, it contains a Dirac measure.

*Proof.* Every probability has a point $z_*$ in its support. The balls
$D_r$ of radius $r>0$ centered there have positive probability. For the
calibrated conditional covariance $C_r$, bounded support and centering
at the conditional mean give $\operatorname{tr} C_r\le r^2$. Therefore

$$
 \kappa\bigl(\nu(\cdot\mid D_r)\bigr)
 =S_0\sqrt{\det C_r}\le\tfrac12 S_0\operatorname{tr}C_r
 \le\tfrac12S_0r^2. \tag{H14}
$$

These conditional laws have finite covariance and converge weakly to
$\delta_{z_*}$ as $r\downarrow0$. This proves both statements. $\square$

The premise is an ideal, nondisturbing, arbitrarily fine *joint* record
of classical position and momentum, with each positive-probability
outcome admitted as a new preparation. It is not a theorem that every
physical instrument has this property. Theorem I of the [necessity note](necessity-unit-and-indeterminacy.md)
constructs a more specific two-pointer Hamiltonian protocol even with a
prior density ceiling, but has its own explicit access and storage
assumptions. In particular a prior cap alone does not supply the postulate
needed to preserve a floor after records.

Combining (H13) with Theorem R shows that its
nonempty, finite-covariance preparation class cannot also satisfy the
fine-record postulate. Equivalently, with weak closure and affine
translations, the records would admit the two point preparations that
merge, contradicting its reversible phase-state evolution. This is an
incompatibility among assumptions, not a proof that any one of them is
physically mandatory.

## 8. Quantum dynamics and instruments at supplied action

For every $\hbar>0$, the same bounded real potential has

$$
 H_\hbar=-\frac{\hbar^2}{2m}\frac{d^2}{dq^2}+V(q),\qquad
 D(H_\hbar)=H^2(\mathbb R).
 \tag{14}
$$

The free operator is self-adjoint on $H^2$. Multiplication by $V$ is
bounded and symmetric, with relative bound zero. The Kato--Rellich
theorem therefore makes (14) self-adjoint on this same domain, with
$H_\hbar\ge-\|V\|_\infty$. Its spectral calculus supplies the unique
strongly continuous unitary group
$U_\hbar(t)=\exp(-itH_\hbar/\hbar)$ for every real time. These are
[@Teschl2009, Theorem 6.4, printed p.135, and Theorem 5.1,
pp.123--124; passages read in the held first edition], with the free
domain in Theorem 7.8, pp.167--168. See the
[source companion](../docs/Teschl_QuantumMechanics_2009.md).

This comparison needs neither an unbounded collision force nor a
choice of singular boundary condition. It still supplies $\hbar>0$;
the classical density witness prevents inferring that this is the
only completion. The quantum state space also is not a class of
positive joint canonical probabilities with unrestricted classical
conditioning. No such identification was used in Theorem R. No
relativistic premise enters, so no $c$ is needed.

### What the covariance resemblance does not imply

For every supplied physical $\hbar>0$, the self-adjoint Hamiltonian above gives a global quantum unitary group. For a quantum state with
finite position and momentum covariances, the Robertson--Schrödinger
inequality gives

$$
 \sqrt{\det\operatorname{Cov}(Q,P)}\ge\hbar/2. \tag{Q15}
$$

This remains true after any selective instrument whose conditional output
is a quantum state with finite covariance. There is nevertheless an exact
initial-state comparison: set

$$
 \epsilon_\hbar=\sqrt{\frac{\hbar}{2S_0}},\qquad
 \sigma_q=L_0\epsilon_\hbar,\quad
 \sigma_p=P_0\epsilon_\hbar. \tag{Q15a}
$$

The Gaussian in the Gaussian preparation family then has $\kappa=\hbar/2$ and is exactly the Wigner
function of the normalized quantum wavefunction

$$
 \psi_{\hbar,u}(q)=(2\pi\sigma_q^2)^{-1/4}
 \exp\!\left[-\frac{(q-u\sigma_q)^2}{4\sigma_q^2}\right]. \tag{Q15b}
$$

Thus covariance saturation and even equality of these *initial* positive
phase-space functions do not by themselves select the subsequent quantum
propagation or an interference law. The classical limit in Theorem 2 then
corresponds to a formal $\hbar\to0$ family at fixed $S_0$; no equality of
the quantum and classical evolved states is asserted. At fixed physical
$\hbar$, a small ratio $\hbar/S_0$ describes a large-characteristic-action
regime only when $L_0,P_0$ specify actual scales of a family of preparations,
not merely a change of units.

Equation (Q15) does not arise by conditioning a positive joint
sharp-position--sharp-momentum law: the canonical Weyl operators obey

$$
 e^{-iaP/\hbar}e^{ibQ/\hbar}
   =e^{-iab/\hbar}e^{ibQ/\hbar}e^{-iaP/\hbar}, \tag{Q16}
$$

and are noncommuting for general $a,b$. An approximate joint measurement
can still have two classical outcomes; those outcomes are not the
nondisturbing sharp joint record assumed in Theorem 4. The positive
quantum constant in (Q15)--(Q16) is an input. Conversely, the classical
history model has no noncommuting observables or demonstrated interference
law, and its apparent probabilistic branch splitting in (H6) is not a
coherent superposition.

There is an independently motivated empirical separator, with additional
composite-system hypotheses. Under setting independence and conditional
locality, an arbitrary classical hidden state including trajectory memory
satisfies $|S_{\rm CHSH}|\le2$; the short proof and its precise assumptions
are in the [shared-readiness note](shared-readiness-chsh.md). A Bell test
with spacelike-separated electron-spin measurements reported
$S_{\rm CHSH}=2.42\pm0.20$ in 245 trials
([Hensen et al. 2015](https://doi.org/10.1038/nature15759), primary
abstract read). Its setting-independence and locality interpretation is an
additional physical premise, motivated by the relativistic causal setup;
the recorded statistical uncertainty matters. The normalized inequality
is dimensionless, so this observation does not determine an action scale or
select quantum theory uniquely. Nonlocal or setting-dependent classical
completions are not excluded by this bound.

## 9. Consequence for STATE

Reversible complete histories, reversible phase laws, continuous nonpoint cusp
transport and selective-record closure are different premises. The explicit
classical countermodels must accompany either conditional floor theorem. The
[canonical central limit](central-limit-canonical-gaussian-sector.md) proves
Gaussian-sector closure under copying; the
[Gaussian meter](gaussian-meter-entropy-floor.md) separately defeats selective
closure of the entropy witness and shows why a Gaussian-mixture repair fails
nonlinear classical transport. The [quantum preparation selection](cusp-quantum-preparation-selection.md)
constructs semiclassical outgoing branches under supplied quantum dynamics.
Those arguments have different hypotheses and remain separate. An independently
justified physical continuity or instrument law, and its identification with a
universal physical $\hbar$, are still missing.
