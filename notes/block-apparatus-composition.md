# Independent apparatus blocks restore extensive composition

At r=3/2, composing k identical independently budgeted blocks multiplies the
saturated canonical minimax product by k. R14's copy-count invariance holds
for a single fixed global budget. It does not survive supplying a fresh
independent budget to each block. Regrouping the same error set preserves
risks; replacing its product constraints by a global norm ball changes the
apparatus class.

R15, 2026-09-11. Fix N identical one-dimensional constituents, m,F>0, known
initial phases, arbitrary measurable forces |f_i|<=F, and complete position
records y_i=q_i+e_i on [0,T]. There is no blind delay. Partition them into
k nonempty blocks of sizes n_j, with sum n_j=N. At each time impose
||e^(j)||_r<=epsilon_j, independently across blocks and independently of
forces, where epsilon_j>0 and 1<=r<=infinity. Independence means Cartesian
admissibility, with no probability law. Set 1/infinity=0. There is no speed
ceiling or apparatus back-reaction in this information model.

The target is centre position R=N^(-1) sum q_i and canonical total momentum
Pi=sum p_i. Q and P are their separate scalar minimax absolute errors;
H=QP has action units, with no 2 pi factor. The error tolerances are supplied
length scales. A product of minimax risks is not a simultaneous error lower
bound for every trajectory.

## 1. Exact risks with block records retained

Put E_j=epsilon_j n_j^(-1/r), w_j=n_j/N, and s_j=T sqrt(F/(mE_j)).
Define the one-constituent functions inherited from R13:

$$q(T,E)=E\min\{FT^2/(2mE),1\},\qquad
p(T,E)=\sqrt{mFE}\,V(T\sqrt{F/(mE)}),$$

$$V(s)=\begin{cases}s,&0\le s\le\sqrt2,\\
\sqrt{2s^2+4}-s,&\sqrt2\le s\le4,\\
2,&s\ge4.\end{cases}$$

For either all constituent records or all k block-average records, the exact
risks at every T>=0 are

$$\boxed{Q_A=\sum_jw_jq(T,E_j),\qquad
P_A=\sum_jn_jp(T,E_j).}$$

**Proof.** R14's synchronous lift identifies each block's projected central
compatible fibre with a scalar displacement path of acceleration bound F/m,
record strip E_j and zero initial phase. This remains true for a retained
block-average record: its entire experiment has the one-body image of mass
n_j m, force bound n_j F and precision E_j. For both protocols the block
central projections agree. Independent block constraints give a Cartesian
product of those fibres. The support of either scalar target adds with its
positive weights: align the block extremizers. The half-difference and
compatible-interval midpoint proof of R11 gives the matching global minimax
upper and lower bounds. Thus retaining internal records within each block
does not improve these centre-coordinate risks.

At T>=max_j 4 sqrt(mE_j/F), both coordinates saturate:

$$Q_A=\bar E:=\sum_jw_jE_j,\qquad
P_A=2\sqrt{mF}\sum_jn_j\sqrt{E_j},\qquad
H_A=2N\sqrt{mF}\,\bar E\sum_jw_j\sqrt{E_j}.$$

These formulas are associative under regrouping when the original independent
block constraints and block records are kept: they are finite weighted sums.

## 2. Discarding the block labels has an exact cost

If only Y=N^(-1)sum y_i is retained, the same underlying class has exactly
the scalar image of mass Nm, force bound NF and record precision bar E.
Indeed, every projected error is at most bar E. Conversely choose each
constituent force f/N for any desired total force f, and within block j set
e_i=(E_j/bar E)e for a desired centre error |e|<=bar E. The block norm is
at most n_j^(1/r)E_j=epsilon_j. Forces and errors are independent, so the
lift realizes every scalar force/error pair from the prescribed initial phase.
Consequently

$$Q_B=q(T,\bar E),\qquad P_B=Np(T,\bar E).$$

At the common saturation horizon in section 1,

$$Q_B=Q_A=\bar E,\qquad
P_B=2N\sqrt{mF\bar E}\ge P_A.$$

Strict concavity of sqrt gives equality precisely when all E_j are equal.
Thus block averaging preserves these risks, while subsequent whole-body
averaging loses momentum information for unequal effective block precisions.
At finite horizons section 1 and the displayed B formulas specify the cost;
strictness at every positive horizon is not asserted.

## 3. Equal blocks settle the invariant-product test

Take n_j=a and epsilon_j=epsilon, so N=ka and E_j=E=epsilon a^(-1/r).
All records, block records and the sole centre record have identical centre
risks. In particular, at T>=4 sqrt(mE/F), writing
H_1=2 sqrt(mF) epsilon^(3/2),

$$\boxed{H_{\rm blocks}=k\,a^{1-3/(2r)}H_1.}$$

For one global budget ||e||_r<=epsilon on the same N constituents, R14 gives

$$H_{\rm global}=(ka)^{1-3/(2r)}H_1,\qquad
\frac{H_{\rm blocks}}{H_{\rm global}}=k^{3/(2r)}.$$

The block saturation horizon also suffices for the global experiment.
At r=3/2, H_blocks=k H_1 while H_global=H_1. This is a counterexample to
extending R14's invariance to independently supplied identical apparatuses.
At r=infinity the ratio is one: Cartesian block boxes already form the same
global box. At any fixed partition and T>0, uniformly shrinking all supplied
epsilon_j to zero eventually reaches saturation and closes H as the
three-halves power of that common scale.

## 4. Which resource constraints regrouping preserves

For finite r the independent-block error set is

$$\mathcal E_{\rm blocks}=\{e:\max_j
(\|e^{(j)}\|_r/\varepsilon_j)\le1\}.$$

This description preserves the original constraints under a change of labels.
A single global ball instead has the nested identity

$$\|e\|_r^r=\sum_j\|e^{(j)}\|_r^r.$$

It is associative when these actual block expenditures remain jointly
constrained. Replacing each child expenditure by its own fresh allowance
replaces a sum constraint by a maximum constraint.

The smallest centred unweighted global l^r ball containing the independent
block class has radius

$$B=\left(\sum_j\varepsilon_j^r\right)^{1/r}.$$

The inequality follows by summing the block bounds and is attained by
saturating all blocks. For k>1 with positive budgets the inclusion is strict:
B>epsilon_j, and concentrating the full B in any one block violates its
individual allowance. No global ball of any radius equals the product set:
its restriction to each block subspace would require its radius to equal
every epsilon_j, whereas simultaneous block saturation requires radius B.

For equal blocks, B=k^(1/r)epsilon. R14 then gives global effective precision
B N^(-1/r)=E, so this larger ball has the same centre risks as the block
apparatus at every horizon despite its strictly larger error set. Equality of
these two scalar risks therefore does not imply equality of preparations.
To recover the original global-epsilon centre risks using equal independent
blocks, their allowances must instead be reduced to epsilon k^(-1/r).
Their product set is then contained strictly in the global ball for k>1.
This matches centre risks but introduces an explicit k-dependent precision
requirement on every block. A tolerance budget specifies admissible error,
not a derived energetic or monetary apparatus cost.

## 5. Research consequence and next test

C086–C087 advance the universality gate by settling the regrouping premise.
A fixed global norm can select a copy-count exponent; independent apparatus
composition restores the extensive product for identical blocks. Neither
law selects a positive preparation-independent precision.

The source capsule is R14/B45's norm geometry and synchronous lift, combined
with R12/B43's product-fibre support law. The new test explicitly preserves
or changes the apparatus error set before comparing its risks. See
[B46](../references/batches/B46.md) for bounded literature coverage and
[the review](../reviews/block-apparatus-B46.md) for proof acceptance.

Next, R16 should connect this abstract budget to R06's prepared mechanical
records: specify the finite set of record errors and preparation class, then
test whether a fixed apparatus mass, coupling and duration prevent uniform
contraction of that error class. Keep R06's finite delayed records distinct
from the complete-history oracle used here. This supplies a concrete physical
precision-selection test before further copy-count algebra.
