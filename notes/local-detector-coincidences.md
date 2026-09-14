# Independent monotone receivers cannot suppress coincidences

Two independently prepared local receivers, responding monotonically to fixed
fractions of one common classical pulse energy, obey
$p_{12}\ge p_1p_2$ on the full gate ensemble. Saturation and unequal efficiencies
preserve this constraint. Fluctuating routing, correlated readiness or
outcome-dependent gate selection can evade it. This identifies a concrete
classical-exclusion premise; the inequality contains no action scale.

Status: Q12 exploratory written derivation and coordinator consistency review.
No accepted-ledger promotion. Independent proof review and a bounded sequential
librarian comparison are required before promotion.

## 1. Preparation, local response and counted gates

Fix a gate duration $T>0$, apparatus settings and pulse shape. In each gate a
nonnegative random energy $E$ reaches a fixed passive splitter. Its output
energies are $aE$ and $bE$, where $a,b>0$ are fixed dimensionless fractions and
$a+b\le1$. This includes a fixed-phase Q08 interferometer only when its
output fractions are fixed across the ensemble. All admitted gates, including
empty gates and double records, are counted.

Let $X,Y\in\{0,1\}$ indicate at least one local record during the gate. The
response probabilities are measurable nondecreasing functions

$$f(E)=F_T(aE),\qquad g(E)=G_T(bE),\qquad 0\le f,g\le1. \tag{1}$$

Sufficient physical assumptions are independent local apparatus variables
$U,V$, jointly independent of E, and response maps $X=x(aE,U)$,
$Y=y(bE,V)$ with the monotone averaged responses (1). There is no communication
or shared release during the gate. Mathematically the needed condition is

$$\Pr(X=1,Y=1\mid E)=f(E)g(E). \tag{2}$$

Spatial separation alone does not imply (2). Hidden common readiness, shared
reset memory, or an unrecorded pulse shape can invalidate this scalar model.
Independence across successive gates is unnecessary for the probability
inequality; it would matter for statistical error estimates from finite data.

Define $p_1=\mathbb E X$, $p_2=\mathbb E Y$, and $p_{12}=\mathbb E(XY)$.
These dimensionless probabilities refer to the same gate ensemble. They are
not mean event counts for a receiver allowing multiple records.

## 2. Exact bound and sharp boundary

For an independent copy $E'$ of E, expand the product to obtain

$$p_{12}-p_1p_2
 =\frac12\mathbb E\big[(f(E)-f(E'))(g(E)-g(E'))\big]\ge0. \tag{3}$$

Equation (2) gives the equality; common monotonicity gives the sign. Bounded
responses make every expectation finite even for energy laws with divergent
moments. Thus, if both singles are positive,

$$A:=\frac{p_{12}}{p_1p_2}\ge1. \tag{4}$$

Equality holds exactly when the nonnegative product in (3) vanishes almost
surely. Fixed E gives equality even for unequal detectors. If both responses
are strictly increasing on a nondegenerate energy distribution, the inequality
is strict. A saturated response may instead give equality.

For example, $F_T(e)=1-\exp(-\kappa_1Te)$ and
$G_T(e)=1-\exp(-\kappa_2Te)$ satisfy the bound exactly, with
$\kappa_i$ in $(\mathrm{energy}\,\mathrm{time})^{-1}$. No weak-pulse
approximation is required. Independent dark-trigger probabilities $d_i$ replace
these responses by $1-(1-d_i)\exp(-\kappa_iTe)$ and preserve monotonicity.
At fixed pulse energy $E_0$ the two records are independent and A=1.
Attenuating E by a factor $\eta^2\to0$ sends the no-dark singles and
coincidences to zero while A remains one for every $\eta>0$. At zero singles
A is undefined; (3) remains meaningful.

A practical symmetric target $p_1,p_2\ge s>0$ therefore requires
$p_{12}\ge s^2$. More generally define the probability of at least one record
$q=p_1+p_2-p_{12}$ and the channel balance
$r=p_1/(p_1+p_2)\in(0,1)$. Put $d=p_{12}$ and $c=r(1-r)$. Then

$$d\ge c(q+d)^2,\qquad
 d\ge\frac{1-2cq-\sqrt{1-4cq}}{2c}. \tag{5}$$

To see the second statement, move all terms of the first inequality to a
quadratic with positive leading coefficient; d must lie between its roots.
Here $0\le q\le1$ and $c\le1/4$, so the discriminant is nonnegative.
The lower bound is sharp: choose constant independent response probabilities
$p_1=rS$, $p_2=(1-r)S$, where
$S=(1-\sqrt{1-4cq})/(2c)$. As q runs from zero to one, S runs from zero to
$1/\max(r,1-r)$, so both probabilities are admissible.
For balanced channels this simplifies to

$$d\ge(1-\sqrt{1-q})^2. \tag{6}$$

Near-unit event efficiency and balanced channels therefore require frequent
doubles in this class. This is a gate-probability trade-off, not an energy gap.

## 3. Three explicit ways the inference can fail

**Fluctuating routing breaks the common ordering.** Fix total energy $E_0>0$.
Let a random routing bit J send the entire pulse to output 1 with probability
r and to output 2 otherwise. Use independent deterministic threshold detectors
with threshold $0<\theta<E_0$. Then $p_1=r$, $p_2=1-r$, $p_{12}=0$.
Local responses to local energy remain monotone; the inputs are no longer fixed
fractions of the common scalar E. Conditional on the full routed input, the
outputs are deterministic and factorize. Equivalently, opposite bright/dark
phases of a two-path network can implement such varying fractions. Mixing
those settings is outside (1). This example does not reproduce a fixed-split
optical experiment or derive quantum interference statistics.

**Correlated readiness breaks conditional independence.** Keep both input
energies fixed above threshold. Prepare readiness variables $U=J$, $V=1-J$
independently of the source and let $X=U$, $Y=V$. Again the singles are r and
$1-r$ with no doubles. Both responses can be monotone in local signal energy,
and no communication during the gate is needed. The detectors were prepared
with a shared anticorrelated resource. Source independence alone does not
exclude this possibility.

**Selecting gates by their outcomes breaks the ensemble premise.** Start with
independent Bernoulli records of equal probability $p\in(0,1)$. Keep only gates
with at least one record. On that selected ensemble,

$$p'_1=p'_2=\frac1{2-p},\qquad p'_{12}=\frac p{2-p},\qquad
 A'=p(2-p)<1. \tag{7}$$

The original unselected A equals one. Conditioning on exactly one record makes
the apparent coincidence probability zero. Conversely, a source-side herald H
is compatible with (3) whenever, within H, (1)--(2) still hold. Correlation of H
with E may arbitrarily change the energy distribution; the proof works for
that new distribution. A herald that also selects detector readiness needs a
new factorization check. Fixed settings should likewise be tested separately;
mixtures of oppositely routed settings can create anticorrelation.

## 4. Decision and the remaining physical obligation

Q11's shared-release model lies outside (2); its exclusive records are therefore
consistent with this obstruction. Q12 rules out repairing independent monotone
fixed-split receivers merely by changing thresholds, saturation, efficiencies
or scalar energy fluctuations. It does not exclude classical models with extra
source modes or correlated apparatus preparations. An observed deficit of
coincidences identifies a failure of this joint premise package, not uniquely
which premise failed.

The statistics are invariant under a change of energy unit and contain no
mechanical action observable. Even an independently established violation
would require further state and dynamical reconstruction to select a universal
positive action parameter. The receiver response constants in section 2 retain
their supplied dimensions; no physical clock or Planck constant is inferred.

Park further single-splitter receiver tuning. The next useful quantum-premise
test is a bounded two-setting local model: allow arbitrary shared readiness
and source variables, but require settings independent of them and local
responses with every gate assigned an outcome. Derive the resulting correlation
constraint and test a specified singlet preparation against it. This asks
whether the shared-preparation escape survives changed measurement settings;
it is a new premise test, not an inference of an action scale from Q12.
The gap track still needs independently specified physical dynamics before
another parent-generator variant can decide its main obligation.

## Source comparison and coverage

Grangier, Roger and Aspect, *Europhysics Letters* **1**, 173--179 (1986),
[primary paper](https://www.cpt.univ-mrs.fr/~verga/pdfs/Grangier-1986.pdf),
pp. 174--175, defines gate-normalized singles and coincidences and derives a
classical coincidence lower bound using semiclassical detection and an intensity
moment inequality. This is an established precedent for the witness, not a
novelty claim. The monotone Bernoulli-response argument and countermodels above
are derived here under their stated assumptions; the source is not credited
with those extensions.

Coverage: one discovery query, one readable primary PDF route and one failed
route; extracted text of pp. 174--175 was read. Formula extraction is incomplete
and the screenshot tool supplied no inspectable image, so exact equation
transcription is not claimed. The source's prose states the coincidence-product
bound. No source experimental-data audit, full proof audit or exhaustive
literature comparison was performed. Q01's existing
[B67 companion](../docs/batches/B67/quantum-premise-source-companion.md)
supplies the operational premise distinction used here.
