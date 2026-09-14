# Independent settings test shared readiness, while leaving action units free

Arbitrary shared source and receiver variables satisfy the CHSH bound when
settings are independent of them and responses are conditionally local.
A specified singlet state exceeds that bound. This closes the shared-readiness
escape for that local model class, but the witness is dimensionless: it neither
determines a positive action constant nor constructs quantum mechanics.

Q13 applies the established CHSH argument to the receiver programme. It adds
no new theorem or novelty claim. The quantum state and probability rule below
are explicit comparison inputs, not consequences of classical mechanics.

## 1. Model and gate convention

On every predesignated gate, each side chooses a setting $x,y\in\{0,1\}$
and assigns an outcome $A,B\in\{-1,+1\}$. A fixed local rule assigns an
outcome also to no-click or multiple-click records. Gates are not discarded
according to their outcomes. Any source heralding occurs before setting
choices, and the following assumptions concern that heralded ensemble.

Let $\lambda$ include arbitrary correlated source and readiness information.
The assumptions are

$$\rho(d\lambda\mid x,y)=\rho(d\lambda),\qquad
P(A,B\mid x,y,\lambda)=P_A(A\mid x,\lambda)P_B(B\mid y,\lambda). \tag{1}$$

Thus settings do not select different hidden ensembles, and each response
uses only its local setting once the common causes are specified. There is
no monotonicity, scalar-intensity or independent-readiness assumption.
The factorization is stronger than the absence of observable signalling;
spacelike separation motivates a causal test but is not by itself a proof
of this probability representation.

Define conditional means $a_x(\lambda),b_y(\lambda)\in[-1,1]$ and
$E_{xy}=\int a_xb_y\,d\rho$. Private stochastic responses are included.

## 2. The correlation constraint

For each $\lambda$,

$$|a_0(b_0+b_1)+a_1(b_0-b_1)|
\le |b_0+b_1|+|b_0-b_1|
=2\max(|b_0|,|b_1|)\le2.$$

Integration over the same measure for all four setting pairs gives

$$|E_{00}+E_{01}+E_{10}-E_{11}|\le2. \tag{2}$$

Constant positive outcomes attain two, so the bound is sharp. Correlated
readiness cannot evade it while (1) remains true. Outcome-dependent gate
selection can instead make the retained hidden distribution depend on the
settings; an in-gate common controller can violate conditional locality.
Those are changes of premise, not counterexamples to (2).

## 3. Explicit quantum comparison

Supply two qubits in
$|\psi^-\rangle=(|01\rangle-|10\rangle)/\sqrt2$, Pauli measurements
$a\cdot\sigma$ and $b\cdot\sigma$, and Born probabilities.
Direct application of Pauli matrices gives

$$\langle\sigma_i\otimes I\rangle=0,\qquad
\langle\sigma_i\otimes\sigma_j\rangle=-\delta_{ij},\qquad
E(a,b)=-a\cdot b. \tag{3}$$

Choose $a_0=e_z$, $a_1=e_x$,
$b_0=-(e_z+e_x)/\sqrt2$, $b_1=-(e_z-e_x)/\sqrt2$.
The four correlations are $(1,1,1,-1)/\sqrt2$ in the order
$(00,01,10,11)$; the expression in (2) is $2\sqrt2$.
The marginal outcomes remain unbiased and independent of the remote setting.
Thus no-signalling alone permits this comparison even though (1) cannot
represent it.

This is an ideal-state prediction. Actual receiver losses must be included
in the assigned all-gate outcomes and can reduce the observed violation.
No empirical loophole closure or experimental data analysis is claimed here.

## 4. Why this does not measure an action constant

If dimensional spin outcomes are written $S_A=(K/2)A$ and $S_B=(K/2)B$
for supplied $K>0$ with action units, each correlation multiplies by $K^2/4$.
The classical bound becomes $K^2/2$ and the singlet value becomes
$K^2/\sqrt2$. Their ratio remains $\sqrt2$ for every positive K.
Normalized outcome probabilities contain no energy or clock calibration.
Sending K down through positive values leaves the dimensionless comparison
unchanged; the zero endpoint would collapse the dimensional readout and is
not needed for this scale test.

The result locates a real exclusion: a theory matching (3), with independent
settings and all-gate accounting, must abandon the conditional local model
(1). It does not select quantum theory uniquely among possible correlation
models, nor derive its dimensional normalization.

## 5. Research consequence

Q08--Q13 have separated classical fringes, threshold records, shared control
and local-causal correlations. Park further detector and Bell-witness variants.
The remaining action premise requires a physical relation between transformations,
energy and time rather than another dimensionless inequality.

Switch the next bounded construction to the gap track: specify a physical
local spin Hamiltonian related by a finite-depth local unitary to independent
spins, and calculate its interacting ground state and finite-volume gap.
This supplies a direct Hamiltonian example rather than an auxiliary sampling
clock. Quantum structure and the action-to-time conversion must be stated as
inputs; the test is gap survival under local conjugation, not quantum necessity.

## Source and evidence

J. F. Clauser, M. A. Horne, A. Shimony and R. A. Holt,
*Proposed Experiment to Test Local Hidden-Variable Theories*, Physical Review
Letters **23**, 880--884 (1969),
[DOI](https://doi.org/10.1103/PhysRevLett.23.880), is the established source
for the CHSH test; the publisher links its 1970 erratum. One targeted query
checked the primary bibliographic record. The proof used here is the displayed
bounded-response derivation, not a transcription or audit of the original
optical proposal. The singlet comparison is an explicit calculation under
stated quantum inputs. No new accepted claim or numerical verification script
is introduced.
