# Classical detector records: thresholds, reliability and coincidence bounds

Independently prepared receivers with monotone responses to **fixed fractions
of one common scalar pulse energy**, counted on the same full gate ensemble,
obey $p_{12}\ge p_1p_2$. This is the strongest exclusion below: saturation,
unequal efficiencies and independent dark triggers preserve it. The activated-rate model gives a sharp retention/deadline cost under fixed
attempt frequency and transduction. A passive barrier supplies discrete
crossings but no universal threshold; a shared
release supplies exclusive fringe-weighted records by changing the independence
premise. Neither the exclusion nor these classical constructions selects
physical $\hbar$ or reconstructs quantum states and instruments.

The proofs concern declared receiver models. They are written derivations
with internal consistency checks, not independent peer review or experimental
validation. The coincidence witness has established optical precedent; no
literature novelty is claimed.

## Independent monotone receivers

### Preparation and all-gate probabilities

Fix a gate duration $T>0$, settings and pulse shape. A random energy $E\ge0$
reaches a passive splitter whose outputs are $aE,bE$, for fixed dimensionless
$a,b>0$, $a+b\le1$. A two-path interference output fits this model only when
its fractions are fixed across the ensemble. Let $X,Y\in\{0,1\}$ indicate
at least one record in the gate. Assume measurable nondecreasing responses

$$f(E)=F_T(aE),\qquad g(E)=G_T(bE),\qquad 0\le f,g\le1,$$

and conditional factorization

$$\Pr(X=1,Y=1\mid E)=f(E)g(E).$$

Independent local apparatus variables $U,V$, jointly independent of $E$,
with $X=x(aE,U)$, $Y=y(bE,V)$ and monotone averaged responses suffice.
Spatial separation alone does not give factorization: common readiness,
reset memory or an unrecorded pulse shape can invalidate it. Independence
between successive gates is unnecessary for the inequality, although relevant
to finite-data error estimates.

All admitted gates, including empty gates and doubles, enter
$p_1=\mathbb EX$, $p_2=\mathbb EY$, $p_{12}=\mathbb E(XY)$.
These are gate probabilities, not mean counts from a repeatedly firing receiver.

### Covariance bound and sharp efficiency cost

For an independent copy $E'$ of $E$, conditional factorization gives

$$p_{12}-p_1p_2
=\frac12\mathbb E[(f(E)-f(E'))(g(E)-g(E'))]\ge0.$$

Monotonicity supplies the sign; boundedness removes any moment assumption on
$E$. Equality holds exactly when the nonnegative product vanishes almost
surely. Constant $E$ gives equality; two strictly increasing responses on a
nondegenerate energy law give strict inequality. Saturation can restore equality.
For positive singles, $A=p_{12}/(p_1p_2)\ge1$; at zero singles use the covariance
inequality, since $A$ is undefined.

For example, $F_T(e)=1-e^{-\kappa_1Te}$ and $G_T(e)=1-e^{-\kappa_2Te}$,
with $\kappa_i$ in $(\mathrm{energy}\,\mathrm{time})^{-1}$, obey the bound
without a weak-pulse approximation. Independent dark probabilities $d_i$
replace these by $1-(1-d_i)e^{-\kappa_iTe}$ and preserve it. At fixed $E_0>0$
the two records are independent. Attenuation $E_0\mapsto\eta^2E_0$ sends
no-dark singles and doubles to zero, while $A=1$ for every $\eta>0$.

In particular, $p_1,p_2\ge s>0$ requires $p_{12}\ge s^2$. More precisely,
put $q=p_1+p_2-p_{12}$, $d=p_{12}$, $r=p_1/(p_1+p_2)\in(0,1)$ and
$c_r=r(1-r)$. Since $p_1+p_2=q+d$,

$$d\ge c_r(q+d)^2,\qquad
 d\ge\frac{1-2c_rq-\sqrt{1-4c_rq}}{2c_r}.$$

The second expression is the lower root of the first quadratic. It is sharp:
constant independent responses $p_1=rS$, $p_2=(1-r)S$, with
$S=(1-\sqrt{1-4c_rq})/(2c_r)$, attain it. For $0<q\le1$,
$0<S\le1/\max(r,1-r)$, so both responses are admissible. At $q=0$ one
simply has $d=0$ and balance is undefined unless specified as a limit.
Balanced channels satisfy

$$d\ge(1-\sqrt{1-q})^2.$$

Thus efficient balanced events require frequent doubles in this class. The
trade-off is dimensionless and contains no energy gap or action observable.

## How the independence inference fails

**Fluctuating routing.** At fixed $E_0>0$, route all energy to output 1 with
probability $r$ and to output 2 otherwise. Independent deterministic detectors
with threshold $0<\theta<E_0$ give $(p_1,p_2,p_{12})=(r,1-r,0)$.
Their local responses remain monotone, but the inputs are no longer fixed
fractions of the common scalar. Conditioning on the full routed input makes
outputs deterministic and factorized. Mixing opposite bright/dark settings
of a two-path network has the same issue. This is no model of a fixed-split
single-photon experiment.

**Correlated readiness.** Keep both signals fixed above threshold and prepare
$U=J,V=1-J$, where $\Pr(J=1)=r$ and $J$ is independent of the source.
Let $X=U,Y=V$. The same exclusive singles occur without communication during
the gate. Source independence and monotone local responses do not exclude
this anticorrelated apparatus preparation.

**Outcome-selected gates.** Start with independent Bernoulli records of
probability $p\in(0,1)$ and retain only gates containing a record. Then

$$p'_1=p'_2=\frac1{2-p},\qquad p'_{12}=\frac p{2-p},\qquad
 A'=p(2-p)<1.$$

Selecting exactly one record makes the apparent double probability zero.
The unselected $A$ was one. A source-side herald is compatible with the theorem
if monotonicity and factorization still hold within its ensemble. Correlation
with $E$ alone merely changes the energy law; selection of readiness requires
a new check. Settings with different routing fractions must be tested separately.

A deficit of coincidences therefore refutes this joint premise package; it
does not identify uniquely which premise failed. The
[CHSH treatment](shared-readiness-chsh.md) tests a different package: arbitrary
shared readiness is allowed, but settings are independent and every gate has
conditionally local outcomes. Its proof and supplied singlet comparison are
retained separately because scalar monotonicity and independent preparation
are absent there.

## Passive thresholds and stored readiness

### Complementary work outputs and the event regions

The [mechanical interference calculation](mechanical-interference-action.md)
gives finite-pulse works

$$W_\pm=\frac E2(1\pm z),\qquad -1\le z\le1,$$

where $z$ is normalized overlap (a phase cosine for ideal coherent paths).
A lossless accumulator starts at zero, $\dot e_i=P_i(t)\ge0$, and a stipulated
end-of-gate comparator records $C_i=\mathbf1_{W_i>\Delta}$, $\Delta>0$.
It gives at most one event per gate; it supplies neither a permanent memory
nor rearming dynamics. For $E>0$,

$$C_+=1\iff z>2\Delta/E-1,\qquad
 C_-=1\iff z<1-2\Delta/E.$$

If $E\le\Delta$ nothing fires. For $\Delta<E<2\Delta$, doubles are impossible
but only $|z|>2\Delta/E-1$ gives a record. If $E>2\Delta$, every overlap
gives a record and $|z|<1-2\Delta/E$ gives two. At $E=2\Delta$ exactly one
fires except at $z=0$, where neither does; a non-strict comparator instead
gives two at that point. No open energy range has exclusive, unit-efficiency
events for every overlap. At balanced equal inputs, identical deterministic
receiver states force identical records by exchange symmetry.

Random thresholds, asymmetric preparations or communication change these
premises. Counts depend on the sampling law of $z$ as well as the comparator;
$W_i/E$ is not automatically a Born probability. Removing misses or doubles
changes the ensemble. Varying $z$ here also changes routing, so the fixed-fraction
theorem applies to each fixed overlap, not automatically to their mixture.

### A conservative quartic barrier and reset accounting

A receiver with coordinate $q$, momentum $p$, mass $M$ and potential

$$H_R=\frac{p^2}{2M}+U(q),\qquad
 U(q)=\Delta(1-q^2/\ell^2)^2,\qquad M,\ell,\Delta>0$$

has minima at $\pm\ell$ and a saddle of height $\Delta$ at zero. Start at
$(-\ell,0)$ and supply a positive impulse $I$. The deposited energy is
$W=I^2/(2M)$, and the subsequent trajectory crosses zero precisely for
$W>\Delta$. Equality approaches the saddle only asymptotically: near zero,
$\dot q\simeq\sqrt{4\Delta/(M\ell^2)}|q|$, so travel time diverges
logarithmically. A finite deadline supplies another receiver parameter.
General forcing cannot be replaced by total work without checking direction
and timing. Conservative crossing can later recross; a latch or capture needs
additional dynamics and energy accounting.

Prepare instead $(q_0,0)$, $-\ell<q_0<0$, with stored energy $e_0=U(q_0)$.
A positive impulse at this state crosses when $W>\Delta-e_0$. As $q_0\uparrow0$,
the required signal tends to zero with $M,\ell,\Delta$ fixed. This is
readiness near an unstable state, supplied by preparation energy.

If a cycle captures the receiver at the right minimum at rest, restoring the
ready state requires net work at least $e_0$ when the reset apparatus supplies
all work and losses are nonnegative. Capture must account for $e_0+W$.
Recovering energy into another store can reduce external work only by including
that store in the balance; full return of all stores leaves exported work and
dissipation as the net supplied energy. No universal reset number follows.
For a narrow-band pulse, $E/\omega$ is approximately its wave action; the
threshold scales $\Delta/\omega$ and $(\Delta-e_0)/\omega$ depend on frequency
and readiness. Barrier energy times crossing time is another apparatus scale,
with a separatrix divergence rather than a selected constant.

## Thermal retention and response deadlines

The following is an effective stochastic receiver with an unchanged bath and
a fixed activated-rate prefactor. It is not derived from the conservative
quartic trajectory above. Its optimal barrier cost and the later shared-release
architecture answer different questions: reliable single-channel triggering
and exclusive two-channel competition.

### Retention and the stipulated rates

Let $T>0$ be bath temperature, $k_B$ Boltzmann's constant, and $\nu>0$ an attempt
frequency in inverse seconds. A prepared metastable receiver has residual
activation barrier $b\ge0$, measured in energy units. Its first recorded escape
is an absorbing event. The stipulated dark rate is

$$r_0=\nu e^{-b/(k_BT)}. \tag{1}$$

Thus the survival probability S solves $dS/dt=-r_0S$, $S(0)=1$, giving
$S(t)=\exp(-r_0t)$. Absorption describes a monitored first event; maintaining a
permanent physical record and resetting it remain separate apparatus tasks.
Retention here means absence of a false first event while armed.

During a signal gate of duration $t_g>0$ the barrier is reduced by an amount
$u\ge0$, held constant throughout the gate. Use the explicitly capped model

$$r_1=\nu e^{-\max(b-u,0)/(k_BT)}. \tag{2}$$

Here $u$ denotes an energy change, whereas $\nu$ denotes a rate. The cap prevents
an unphysical extrapolation to rates above the stipulated attempt frequency.
It is a model definition, not a Kramers formula near a vanishing barrier.
The same $\nu$ in (1) and (2), an unchanged bath and exponential holding times
are essential premises. Sustaining u may require work from a control source;
no equality between u and input pulse energy has yet been assumed.

Require false-event probability at most $\epsilon$ over a dark interval $\tau>0$,
and miss probability at most $\eta$ in a subsequent signal gate, conditional on
surviving to that gate. For $0<\epsilon,\eta<1$, define

$$a=-\log(1-\epsilon)>0,\qquad c=\log(1/\eta)>0. \tag{3}$$

The two requirements are exactly

$$r_0\tau\le a,\qquad r_1t_g\ge c. \tag{4}$$

Conditional efficiency matters: the probability of both surviving the dark
interval and firing in the gate is $\exp(-r_0\tau)[1-\exp(-r_1t_g)]$. The
separate bounds ensure it is at least $(1-\epsilon)(1-\eta)$.

### Exact feasibility and the optimal barrier

Timely detection is impossible in this model if $\nu t_g<c$, even with zero
remaining barrier. If $\nu t_g\ge c$, define

$$B=\max\!\left(0,k_BT\log\frac{\nu\tau}{a}\right),\qquad
D=k_BT\log\frac{\nu t_g}{c}\ge0. \tag{5}$$

The feasible designs are precisely

$$b\ge B,\qquad u\ge\max(0,b-D). \tag{6}$$

Indeed, taking logarithms of (4) first gives $b\ge k_BT\log(\nu\tau/a)$.
The signal inequality gives $\max(b-u,0)\le D$. Since $D\ge0$, this is equivalent
to $b-u\le D$, proving (6). Every point in (6) satisfies both original probability
bounds, including the equality cases. Minimizing over $b\ge0$ therefore yields

$$u_{\min}=\max(0,B-D)
 =k_BT\left[\log\frac{c\tau}{a t_g}\right]_+,
 \qquad \nu t_g\ge c, \tag{7}$$

where $[x]_+=\max(x,0)$. For the last equality, if $\nu\tau\le a$ then $B=0$;
feasibility also gives $c\tau/(at_g)\le\nu\tau/a\le1$. If $\nu\tau>a$, subtract
the two logarithms in (5). This checks both branches without extending a
negative barrier.

In the discriminating regime $c\tau>at_g$, choose $b=B$ and $u=B-D$. Both
probability constraints then saturate. If $c\tau\le at_g$, a design with $u=0$
can already satisfy them: the timing/error specification is too weak to
require signal discrimination. A nonzero temperature alone is insufficient.

### Preloading, deadlines and the prefactor countermodel

At fixed $T,\nu,\tau,\epsilon$ with $\nu\tau>a$, preloading cannot reduce b
below B while satisfying dark retention. This closes the zero-residual-barrier
route within the specified metastable class. A receiver with bare barrier
$\Delta$ and a sustainable preload $e_0$, modeled by $b=\Delta-e_0$, must satisfy

$$0\le e_0\le\Delta-B. \tag{8}$$

If $\Delta<B$ the design cannot meet retention. A particle initially at rest
near the conservative barrier's unstable saddle is not automatically such a sustainable metastable
preload: it moves even without noise. Equation (8) applies only if an actual
preparation/control mechanism realizes (1) for the full dark interval.

Reducing $\nu$ alone improves dark survival but slows detection. The gate floor
$\nu\ge c/t_g$ prevents using $\nu\to0$ at fixed gate and miss tolerance. In the
positive-bound regime the same prefactor cancels from (7), exposing the
required contrast $r_1/r_0\ge c\tau/(at_g)$. Retention alone would not give
this protection: it is the combined dark and signal requirement that does so.

If the signal can instead change the prefactor, a rate-only alternative is

$$r_0=\nu_0 e^{-b/(k_BT)},\qquad
r_1=\nu_1 e^{-b/(k_BT)}. \tag{9}$$

For any fixed $b\ge0$ choose $\nu_0=(a/\tau)\exp(b/(k_BT))$ and
$\nu_1=(c/t_g)\exp(b/(k_BT))$. Both specifications hold with $u=0$. This is an
exact counterexample to an inference from probabilities alone to barrier
reduction, not a construction of a zero-work autonomous detector. Changing
mobility, coupling or access to a reaction channel has its own physical
control cost, which (9) does not specify.

### Transduction, energy and action

To infer incident work W, add the explicit transduction premise

$$u\le\chi W,\qquad 0<\chi<\infty, \tag{10}$$

with fixed dimensionless $\chi$ and with all sources contributing to barrier
control included in W. Then (7) implies

$$W\ge\frac{k_BT}{\chi}
 \left[\log\frac{c\tau}{a t_g}\right]_+. \tag{11}$$

A stored-energy amplifier need not obey (10) for signal work alone. Nor is a
barrier-height change automatically dissipated heat or reset work: it concerns
the energy landscape along an escape path, not the work along the actual
control trajectory. the conservative barrier's cycle accounting remains necessary.

For the mechanical interference model's narrow-band wave input of angular frequency $\omega$, canonical wave
action is approximately $W/\omega$. Under (10) its corresponding lower bound is
the right side of (11) divided by $\omega$. A finite-pulse wave-action definition
must retain the mechanical interference model's bandwidth qualification. Alternatively $Wt_g$ has action
units but describes a different quantity. Neither choice removes $T$, error
rates, timing, transduction or frequency from the result.

Within the stipulated rate-model class, $T\to0$ at fixed $\nu$ and fixed
specifications sends the optimal b, u and W bound to zero while preserving
all rate ratios. No microscopic low-temperature extrapolation is claimed.
Allowing larger $\chi$ also removes a bound on signal work; allowing $t_g\ge c\tau/a$
removes the positive discrimination requirement. These are explicit class
limits, not quantum predictions.

## Exclusive shared release and causal timing

### One release permission with supplied hazards

Store the two inputs $e_\pm=E(1\pm z)/2$, $E>0$. A ready state $R$ has
absorbing exits $C_\pm$ with rates $r_\pm=\alpha e_\pm$, where
$\alpha>0$ has units $(\mathrm{energy}\,\mathrm{time})^{-1}$. The first exit
consumes the only permission to release. This is an effective autonomous Markov
receiver after preparation, not a microscopic Hamiltonian derivation. A central
reservoir can lower its energy by $\Delta>0$ on either exit, delivering that
energy to the chosen output plus heat. The stored signal acts as a kinetic
control and need not be the emitted energy. Reset replaces $\Delta$ or retrieves
it from an included store. Energy conservation permits this accounting but
does not itself enforce the single-use state graph or linear rate law.

With $\Gamma=\alpha E$, integration of the exit flux gives

$$p_R(t)=e^{-\Gamma t},\qquad
 p_\pm(t)=\frac{e_\pm}{E}(1-e^{-\Gamma t}).$$

Doubles are impossible. Conditional on an event by any $t>0$, or after
indefinite waiting, the probabilities are $e_\pm/E=(1\pm z)/2$. Prescribed
hazards $\alpha_p e_\pm^p$, $p>0$, would instead give
$e_\pm^p/(e_+^p+e_-^p)$; exclusivity does not select linearity or quantum
state structure.

Attenuating displacement by $\eta$ scales energy by $\eta^2$. The conditional
weights stay fixed, but efficiency by a fixed $T$ becomes
$1-e^{-\alpha\eta^2ET}\to0$. Error tolerance $0<\varepsilon<1$ requires

$$E\ge\frac{\log(1/\varepsilon)}{\alpha T},\qquad
 \frac E\omega\gtrsim\frac{\log(1/\varepsilon)}{\alpha T\omega}$$

for the narrow-band wave-action convention. At zero energy no event occurs;
zero-signal and indefinite-wait limits do not commute.

### Local firing followed by delayed inhibition

A co-located arbiter can access both inputs before release and send its output
to a remote record after travel. It is not instantaneous inhibition between
independently firing distant detectors. To model the latter, start independent
Poisson clocks $r_+,r_-$; each site fires at most once and the first inhibits
the other after delay $\delta>0$. Memorylessness gives the eventual double-event
probability

$$P_2=\frac{r_+}{\Gamma}(1-e^{-r_-\delta})+
       \frac{r_-}{\Gamma}(1-e^{-r_+\delta}).$$

It is positive when both rates are positive. In this architecture, separation
$d$ and inhibition speed at most $c$ imply $\delta\ge d/c$. Balanced rates give
$P_2=1-e^{-\Gamma\delta/2}$. A first-event deadline $T$, no-first-event tolerance
$\varepsilon_0$ and double tolerance $\varepsilon_2$ are compatible only if

$$\frac{\log(1/\varepsilon_0)}{T}\le\Gamma
 \le\frac{-2\log(1-\varepsilon_2)}{\delta}.$$

Doubles here are counted through the entire inhibition window, including its
part after $T$. Gate censoring changes the criterion. Central arbitration,
prior correlated readiness or a different propagation law changes a premise;
this timing bound is not a theorem about every classical receiver.

## Source evidence

Grangier, Roger and Aspect, *EPL* **1**, 173--179 (1986),
[primary paper](https://www.cpt.univ-mrs.fr/~verga/pdfs/Grangier-1986.pdf),
[DOI](https://doi.org/10.1209/0295-5075/1/4/004), supplies the established
optical coincidence precedent. Extracted passages on pp. 174--175 describe
gate-normalized probabilities and a semiclassical coincidence-product lower
bound. Formula extraction was incomplete; exact source equations, experimental
data and a full detector audit are not claimed. The monotone Bernoulli proof,
sharp trade-off and countermodels above are derived under their displayed
premises, not attributed as extensions proved in that paper.

Gillespie, *J. Phys. Chem.* **81**, 2340--2361 (1977),
[DOI](https://doi.org/10.1021/j100540a008), was checked at publisher-metadata
level as the standard competing-hazard lead. The exponential survival and
delay formulas here are direct calculations, not an imported microscopic
receiver model. The [B67 companion](../docs/batches/B67/quantum-premise-source-companion.md)
supplies the recorded operational-premise comparison. No exhaustive priority
search or independent proof acceptance is implied.

For the activated-rate model, source context is limited. The existing
[B23 companion](../docs/batches/B23/harmonic-receiver-source-companion.md),
Zwanzig p. 219 (21)--(24), supplies a bath-memory construction, not (1).
One discovery search located Hänggi, Talkner and Borkovec,
*Reaction-rate theory: fifty years after Kramers*, Rev. Mod. Phys. 62,
251--341 (1990), [DOI](https://doi.org/10.1103/RevModPhys.62.251).
Its bibliographic metadata/abstract identify activated escape as established
context. The PDF was opened but no rate formula is imported from it; this is
not a passage or prior-art audit. Equations (1), (2) and (10) are declared
premises; (3)--(8) and (11) are written consequences; (9) tests an omitted
coupling premise. The displayed rate laws and transduction law are premises; the optimality
calculation is internal written mathematics, not independent peer review.

## Consequence for STATE

Clicks, exclusive fringe weights and a fixed-split coincidence exclusion have
different premises. The retained passive-barrier and shared-release countermodels
locate those differences explicitly. Further receiver tuning remains parked;
the thermal optimum retains its specified rate, timing, temperature and
transduction premises, and any identification with physical $\hbar$ needs dynamics and
calibration beyond dimensionless event statistics. The independent-setting
CHSH question retains its separate proof and supplied quantum comparison.
