# Thermodynamics of records gives a trade-off and no floor

**Result, 2026-09-27 (a recorded failure of one route).** Theorem I of the
[unit-and-indeterminacy note](necessity-unit-and-indeterminacy.md) says
that back-action indeterminacy is impossible for classical models with
Liouville dynamics, product preparations obeying a prior density ceiling,
and Bayesian conditioning on records. A natural attempt to escape it
adds a heat bath and requires records to be physical: stored, and
eventually erased, at temperature $T>0$. This note shows that the attempt
yields an exponential trade-off between dissipated energy and posterior
area, and no positive floor:

$$\eta\ \ge\ A_0\,e^{-W/(k_BT)},$$

where $A_0$ is the prior phase-space area of the body, $\eta$ the area of
its posterior support after the records, and $W$ the total work spent on
measurement and erasure (Theorem 1). For every $\eta>0$ the construction
of Theorem I reaches $\eta$ with finitely many finite-precision readings,
hence finite $W$. Thermodynamics therefore prices resolution
logarithmically, $W\ge k_BT\ln(A_0/\eta)$, and cannot single out an action.
The would-be unit $k_BT\,\tau$ built from the bath and a record time
rescales under the similarity of Theorem B of the
[dimensional note](action-unit-dimensional-selection.md). So the
thermodynamic route supplies neither ingredient (U) nor (I), and the
question of STATE item 2 stays with the three denials listed in the
unit-and-indeterminacy note.

The ingredients are standard (Landauer, Bennett, the Sagawa--Ueda bound
for measurement plus erasure); the note records their consequence for
this programme, with no novelty claimed.

## 1. The bound

Setting: the classical model of Theorem I, with body and pointers coupled
to a heat bath at temperature $T$. Records are pointer states that are
read, used, and eventually reset to a standard state. The
generalized second law for measurement and erasure (classical form of
the bound of
[Sagawa and Ueda 2009](https://doi.org/10.1103/PhysRevLett.102.250602),
metadata; the erasure part is
[Landauer 1961](https://doi.org/10.1147/rd.53.0183) and
[Bennett 1982](https://doi.org/10.1007/BF02084158), metadata) states that
the total work of a measurement that gains mutual information $I$ (in
nats) about the system, followed by erasure of the record, satisfies
$W_{\rm meas}+W_{\rm eras}\ge k_BT\,I$.

**Theorem 1.** Let the body's prior be uniform on a phase-space region of
area $A_0$, and let a protocol of records leave, for almost every
outcome, a body posterior supported in a region of area at most $\eta$.
Then the total work of measurement and erasure satisfies

$$W\ \ge\ k_BT\,\ln\frac{A_0}{\eta},\qquad\text{equivalently}\qquad
\eta\ \ge\ A_0\,e^{-W/(k_BT)}.$$

*Proof.* The differential entropy of the uniform prior is $\ln A_0$ (area
measured in any fixed unit), and a density supported in area at most
$\eta$ has differential entropy at most $\ln\eta$. The mutual information
between body and records is the prior entropy minus the average posterior
entropy, so $I\ge\ln(A_0/\eta)$; the unit of area cancels. Apply the
measurement-plus-erasure bound. $\square$

**The construction of Theorem I is thermodynamically cheap.** Its two
pointers are read to precisions $\epsilon'$ and $\epsilon_2'$; each reading
stores finitely many bits for a bounded pointer range, and erasing them
costs a finite multiple of $k_BT\ln2$. So every posterior area $\eta>0$ is
reached at finite work, and the bound of Theorem 1 is the only
thermodynamic constraint.

## 2. What this says about the necessity question

- **No floor.** The minimal posterior area at work budget $W$ is
  $A_0e^{-W/(k_BT)}$, which tends to zero as the budget grows. A record of
  Newton's sagitta at resolution $s$ with impulse resolution $\delta p$
  costs at least $k_BT\ln(A_0/(s\,\delta p))$: resolving a phase-space
  area a thousand times below $\hbar$ costs only $k_BT\ln1000$ more than
  resolving $\hbar$ itself. Thermodynamics cannot distinguish $\hbar$.
- **No unit.** The constants of the route are $k_BT$ and whatever times
  the protocol uses. An action $k_BT\,\tau$ rescales with $\tau$, and the
  admitted class is closed under slowing the protocol, so Theorem B of the
  dimensional note gives floor zero. The universal unit of Theorem U
  enters through the equilibrium spectrum of radiation, which the record
  bound never uses.
- **The exponential again.** The trade-off is a Boltzmann factor, as in
  the exponential ladder of the [dimension-ladder note](dimension-ladder.md),
  §4. Here the exponent contains no action constant, so the factor
  suppresses without setting a scale; in Wien's tail
  $e^{-h\nu/(k_BT)}$ the same factor sets one, because $h$ appears in the
  exponent.

## 3. Consequence for STATE

The thermodynamic route to (I) is closed at theorem level: records with
Landauer costs satisfy Theorem I with an exponential work--area
trade-off. STATE item 2 keeps its three candidate denials (of Liouville
dynamics, of product preparations, of Bayesian conditioning); the
background and inflexion routes are under evaluation in the 2026-09-27
Astra run.
