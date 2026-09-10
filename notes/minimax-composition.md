# Worst-case information scales under mechanical composition

Product bounded-error experiments add scalar minimax radii linearly. Their
canonical coordinate-risk product therefore fails A08's variance composition
law: composing n identical constituents multiplies this action product by n.
Keeping only the centre position record can strictly increase momentum risk
when constituent force/precision ratios differ. These are the R12 tests of the universality bridge in I006.

R12, 2026-09-11. Mathematical acceptance and source coverage are recorded in
the claim ledger and B43 review. All coordinates lie on the line, masses are
positive, and momenta are canonical. The observable H is the product of the
two coordinate minimax absolute errors, with units of action and no 2 pi
normalization. It is neither a reachable-set area nor a variance coefficient.

## 1. Product information gives an exact radius law

For each constituent i, let U_i be compact, convex and symmetric about zero,
A_i the linear record map, and L_i a scalar linear target. Take both maps continuous. All known offsets
are subtracted. Records are y_i=A_i u_i+e_i, with an error set symmetric about zero and convex
E_i, assumed closed and nonempty. Use the Cartesian product of input/error classes and retain every y_i;
this permits all combinations, including aligned errors, without assigning a
probability law. Let

$$K_i=\{u_i\in U_i:A_i u_i\in E_i\},\qquad
r_i=\max_{u_i\in K_i}|L_i u_i|.$$

For the target $L=\sum_i a_i L_i$, the exact minimax radius is

$$\boxed{r_L=\sum_i |a_i|r_i.}$$

**Proof.** The central compatible fibre is exactly the product of the K_i.
The triangle inequality bounds its target magnitude by the displayed sum.
Symmetry permits choosing each extremizer with the sign of a_i, attaining
the sum. R11's half-difference/midpoint proof gives the scalar minimax risk:
two inputs compatible with any one record have half-difference in the central
fibre, and opposite extremizers share the zero record. Compactness can be
replaced by finite suprema and approximating extremizers. Pointwise bands on
complete histories use the weak-star compact bounded-force class of R11.

Write Q_i and P_i for the constituent position and momentum radii. For total
mass $M=\sum_i m_i$, centre coordinate $R=\sum_i m_i q_i/M$ and total
momentum $P=\sum_i p_i$, the canonical radii and their product are

$$Q_R=\frac{\sum_i m_iQ_i}{M},\qquad P_P=\sum_iP_i,\qquad
H_R=\frac{(\sum_i m_iQ_i)(\sum_iP_i)}{M}.$$

For two constituents, $r=q_1-q_2$ and
$p_r=\mu(p_1/m_1-p_2/m_2)$, with $\mu=m_1m_2/M$, give

$$Q_r=Q_1+Q_2,\qquad P_r=\mu(P_1/m_1+P_2/m_2),\qquad H_r=Q_rP_r.$$

These are separate coordinate minimax risks; their product need not be a
simultaneous error lower bound on one motion. Componentwise compatible-interval
midpoints attain both coordinate bounds. Transforming a product class into
centre and relative coordinates generally couples those coordinates.

## 2. A sharp bounded-force instance

Take R11's known initial states, arbitrary measurable $|f_i|\le F_i$, and
complete position records with $|e_i(t)|\le\varepsilon_i$ through the common
terminal time T. Assume $F_i,\varepsilon_i>0$ and

$$T\ge\max_i4\sqrt{m_i\varepsilon_i/F_i}.$$

There is no blind delay and no speed ceiling on the full admissible class.
R11 gives $Q_i=\varepsilon_i$ and $P_i=2\sqrt{m_iF_i\varepsilon_i}$.
Thus the exact constituent-record centre risks are

$$E:=Q_R=\frac{\sum_i m_i\varepsilon_i}{M},\qquad
P_P=2\sum_i\sqrt{m_iF_i\varepsilon_i},\qquad H_R=E P_P.$$

Each hidden pair can be prepared at its own start time and finish at T; the
common-horizon condition makes their product admissible. Opposite aligned
pairs hide all constituent records simultaneously. The corresponding sums of
R11 estimators supply the matching upper bounds.

For n identical copies $(m,F,\varepsilon)$, writing
$H_1=2\sqrt{mF}\varepsilon^{3/2}$, this becomes

$$Q_R=\varepsilon,\qquad P_P=2n\sqrt{mF\varepsilon},\qquad
\boxed{H_R=nH_1}.$$

A08's coefficient would remain H_1 for identical independent copies. Product
admissibility permits the aligned errors that prevent variance-style averaging.
At fixed n,m,F, the displayed risk product closes as $\varepsilon\downarrow0$.
At fixed positive precision it grows with n, so the precision and copy-count
limits must be specified separately.

## 3. The exact cost of keeping only the whole-body record

Experiment A retains all constituent records as above. Experiment B keeps only
$Y=\sum_i m_i y_i/M$, with exactly the same hidden constituent force/error
class. Its image is precisely the experiment C of a single mass M with
arbitrary $|f|\le F_\Sigma:=\sum_i F_i$, independently arbitrary record
error $|e|\le E$, and the known centre initial state.

**Image equality.** Any B pair belongs to C since $M\ddot R=\sum_i f_i$
and $|\sum_i m_i e_i/M|\le E$. Conversely, for any C force f and error e,
choose $f_i=(F_i/F_\Sigma)f$ and $e_i=(\varepsilon_i/E)e$.
Each constituent obeys its bounds, evolves from its prescribed initial state,
and their weighted position and record sum give exactly the selected C pair.
Their individual records are unrestricted outputs and need not equal their
inertial paths. This proves surjectivity without assuming individual records
are zero when their aggregate is zero.

R11 therefore gives the exact B risks

$$Q_B=E,\qquad P_B=2\sqrt{M F_\Sigma E},\qquad H_B=E P_B.$$

The horizon condition follows from that of A: the ratio
$ME/F_\Sigma=(\sum_i m_i\varepsilon_i)/(\sum_i F_i)$ is a
force-weighted average of $m_i\varepsilon_i/F_i$. Hence

$$Q_A=Q_B=E,\qquad
P_A=2\sum_i\sqrt{m_iF_i\varepsilon_i}\le
2\sqrt{(\sum_i F_i)(\sum_i m_i\varepsilon_i)}=P_B.$$

Cauchy--Schwarz gives equality exactly when $F_i/(m_i\varepsilon_i)$
is constant across i. Otherwise discarding constituent records strictly
increases momentum risk and its product with position risk, within the same
underlying mechanical model. Equal m and epsilon with $F_2=4F_1=4F$ give
$P_A=6\sqrt{mF\varepsilon}$ and $P_B=2\sqrt{10mF\varepsilon}$.
For identical copies the equality condition holds, and both protocols have
$H=nH_1$. The reduction depends on freely combining the constituent forces
and errors; interaction constraints require a new image calculation.

## 4. What whole-body radius closure would force

Assume for every positive mass finite nonnegative coordinate radii Q(m), P(m)
depend only on mass within one fixed preparation/information class. Require
product composition with constituent records to reproduce those same radii
for total mass. Section 1 then gives

$$(a+b)Q(a+b)=aQ(a)+bQ(b),\qquad P(a+b)=P(a)+P(b).$$

The nonnegative additive-function argument in A08, applied separately to
$mQ(m)$ and P(m), proves

$$Q(m)=q_*,\qquad P(m)=p_*m,\qquad H(m)=q_*p_*m.$$

Here q_* has length units and p_* velocity units. Thus positive H is extensive
under these radius-closure premises. Requiring additionally a mass-independent
H forces H=0, already by composing two identical copies. This statement does
not infer separate radius closure from product closure alone. The identical
copy obstruction to a positive invariant product needs only section 1.

The choice $F(m)=a m$ with fixed positive acceleration bound a and common
precision epsilon realizes these radii in section 2 for all masses, at one
common horizon $T\ge4\sqrt{\varepsilon/a}$:
$q_*=\varepsilon$, $p_*=2\sqrt{a\varepsilon}$. Its product per unit mass
is constant but has units of action per mass. The supplied a and epsilon
still set its value. R12 settles this composition test; it leaves apparatus
selection of precision and the quantum phase identification as separate gates.

## 5. Source connection and next task

R11/B42 borrows the exact hidden bounded-curvature pair from Seeber--Haimovich,
Proposition 3.1, (10)--(12), and the sharp differentiation upper bound from
section 4. R12 applies that input through product central fibres. A08 supplies
the nonnegative additivity proof, but its variance observable has a different
aggregation law. B43 records the bounded prior-art audit of these connections.

R13 should remove R11's long preparation-time assumption: find the exact
finite-horizon coordinate risks from a known initial state when the observation
history is shorter than the hidden-pair preparation time. Compare the early
reachable-set regime with the record-limited regime, then test composition
when different constituents cross between those regimes at different times.
The general product-radius law already applies at finite horizons; the new
task determines constituent radii and aggregate information loss there.
