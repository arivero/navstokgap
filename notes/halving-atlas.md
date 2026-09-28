# Atlas of halving: what one refinement step does, and what emerges, in each dimension

**Purpose, 2026-09-27 (user direction: a collective understanding of the
halving of the lattice and what emerges in each case and dimension, as
the mid-term goal).** This note is the shared map. Each cell says what
one halving does, what it leaves behind, and what survives the limit,
with the status of the statement and the note that holds it. It adds no
new theorem; it fixes one vocabulary so that the agents working here
(Claude, GPT-6 Astra, Fable reviewers) and the user fill the same cells.
Open cells are listed in §5.

Status labels: **proved** (theorem in a repository note, reviewed or
not as marked), **exact** (closed-form identity), **formal** (derivation
assuming an unproved estimate), **known** (established literature,
cited), **open**.

## 1. The operation

**Halving one direction** $a_1\mapsto a_1/2$ of a lattice with plaquette heat
times $t_{\mu\nu}=\lambda_Da_\mu a_\nu/\prod_{\rho\ne\mu,\nu}a_\rho$
([series/parallel note](series-parallel-gauge-refinement.md), eq. (1),
small-field regime) splits exactly into two moves.

- **Series move.** A face containing the refined direction is cut in
  two; its heat time halves. Integrating the cutting edge is a
  convolution of the two half-weights: character coefficients multiply.
  For heat-kernel weights it closes exactly in every dimension.
- **Parallel move.** A face transverse to the refined direction gets a
  new copy in the mid-plane, both at doubled heat time. Integrating the
  mid-plane leaves the factor $\Psi$: a $(D-1)$-dimensional gauge theory
  whose edges carry Brownian-bridge laws fixed by the coarse field.
  Pointwise products of weights add their logarithms; the heat kernel is
  closed under this only up to vortex terms
  ([zero-spacing note](zero-spacing-any-action.md), Proposition 1).
- **Count.** A halving produces parallel moves in $\binom{D-1}2$
  transverse planes. An isotropic step is $D$ directional halvings; the
  isotropic heat time scales as $t\propto\lambda_Da^{4-D}$.
- **Time-only halving** (Euclidean time at fixed spatial lattice) sends
  the transverse heat times to infinity; the Hamiltonian limit needs
  exponential (Wilson-type) magnetic weights (zero-spacing note, §1).

**Newton's halving** is the one-dimensional case: inserting a time
$t_{2.6}$ in a cell is a series move
([refinement note](refinement-composition-and-limit.md), §2). A physical
record at the inserted time is a new variable attached to the body, the
analogue of a parallel insertion. Forgetting a Gaussian record is an
exact parallel move with defect proportional to $\hbar^2$, the identity for
$\hbar=0$ ([record as parallel move](newton-record-parallel-move.md)).

### 1b. Cuts at any position (user remarks, 2026-09-27/28)

Halving is the easiest cut; a cut at any fraction $s\in(0,1)$ of a cell
performs the same two moves, with $s$ as a parameter.

- **Series move.** The cut face splits into heat times $st$ and $(1-s)t$;
  the convolution returns $t$ exactly, for heat-kernel weights, in every
  dimension.
- **Parallel move.** With trapezoid (dual-length) face weights every
  transverse face keeps heat time $2t$, and the inserted edges carry the
  bridge law at fraction $s$, variance $s(1-s)t_e$. The free-field defect
  scales exactly by $4s(1-s)$ ([Corollary 2$_s$](series-parallel-gauge-refinement.md)),
  and the $U(1)$ Theorem 5 holds for every $s$ (Corollary 5$_s$ there):
  halving is the largest single step, and an off-centre cut is gentler
  and shrinks the mesh less.
- **Newton.** One cut spends exactly $3s(1-s)K_\tau$ of the cell action
  $K_\tau=F^2\tau^3/(24m)$, the Cameron--Martin energy of the Schauder hat it
  inserts; the shares add over any cut sequence and exhaust $K_\tau$ iff the
  mesh vanishes ([cut-measure note](cut-measure-newton.md)). The Galileo
  action is an additive measure on the cut process, with the nested
  additivity of the Lévy--Ciesielski construction of the Brownian bridge.
- **Windings and images.** For $U(1)$ a cut's bridge law is a positive
  winding mixture: its weights are $s$-independent and the shifts
  $2\pi(1-s)W$ form $\mathbb Z_2$ only at halving and $\mathbb Z_q$ at $s=p/q$. For every
  compact simply connected group the midpoint expectation of every
  character is exact, a sum over weights of coroot image sums
  ([centre note](sun-midpoint-centre.md), Theorems 1 and 1'). Its signed
  Weyl-polynomial amplitudes describe relative Cartan images; positivity
  of a mixture and homotopy winding sectors in the group are additional
  interpretations unsupported by that expansion.
- **Which part of the centre a cut reaches.** A cut at $p/q$
  reaches exactly the subgroup $\mathbb Z_{\gcd(q,N)}$ of the centre of $SU(N)$ (its
  Corollary 3). So the $SU(2)$ halving carries Dirac's belt trick, the
  image $n$ acting by $(-1)^n$ on half-integer spins, while dyadic
  refinement reaches only its identity for $SU(3)$ and a trisection carries
  the triality. Flipping one mid-edge by a central element inserts thin
  centre flux into its incident faces. Open: whether this ties refinement to
  centre vortices, and whether triadic refinement suits $SU(3)$ better.
  Astra's Round 5B Part A referee is complete (2026-09-28): the exact
  identities and torsion criterion are accepted, with scope corrections.
- **The rod.** The stick of *Zhuangzi* 33, 一尺之捶，日取其半，萬世不竭, halved
  only in its remaining piece, spends $\frac67K_\tau$ and converges to a point,
  the Mohist 端 of Canon B; refinement, which spends all of $K_\tau$, cuts
  every piece again ([cut-measure note](cut-measure-newton.md), §3). The
  parallel with Zeno's dichotomy is recorded as convergence.
- **The frame.** A cut at an arbitrary, even irrational, position is the
  geometers' cut of Book I's closing scholium. The questions for each
  cell become: does the limit depend on the cut sequence (for Newton, no,
  proved in the [cut-measure note](cut-measure-newton.md); for the free
  field, expected, a convergence question for the discrete-exterior-calculus
  Hodge star that the trapezoid weights are, see Corollary 2$_s$), and does the universal part survive when $s$ varies.
  For cell 4 it does, conditionally: for shape-regular schedules under the
  matching hypotheses of the [four-dimensional note](four-dimensional-parallel-log.md)
  (its §7), the coefficient per logarithm of the physical scale is $2b_0$
  whatever the cut positions. An earlier guess here, $\log(1/s)$ per cut,
  follows one daughter only and omits the other's dual-volume weight.

## 2. The atlas by dimension

| $1+n$ | Series move | Parallel planes per halving | What one step leaves | What survives the limit | Status and notes |
| --- | --- | --- | --- | --- | --- |
| $0+0$ | none (a single weight) | none | the weight $k_t(U)$ itself; a single integral with an $e^{-c/\hbar}$ structure | a large-$N$ transition (Gross--Witten) | known; [dimension ladder](dimension-ladder.md) |
| $1+0$ Newton | exact after one cubic counterterm $-F^2h^3/(24M)$; the defect $-F^2uvh/(8M)$ is a coboundary | none | a scalar | unobserved: the exact propagator at every $\hbar$; recorded: a floor only if joint determinacy fails | proved; [refinement note](refinement-composition-and-limit.md), [fifth postulate](principia-fifth-postulate.md) |
| $1+1$ | exact (heat-kernel convolution) | 0 | nothing for heat kernels; for any action, $a^{-2}(1-\hat c_R)$ | a conjugation-invariant Lévy exponent $\psi(R)$; Yang--Mills iff Lindeberg; circle spectrum $\hbar cL\psi(R)$; no local particle | proved (Theorem 2 of the zero-spacing note); known (Lévy) |
| $1+2$ | exact | 1 | free: an irrelevant quadratic form of relative size $a^2K^2/16+(Ga)^2/8$; $U(1)$: vortices of density $e^{-\pi^2/(8t)}$; $SU(N)$: coupling shifts $O(t)$, curvature term explicit | free photon for $U(1)$ at fixed $\lambda_3$ (every lattice gap dies); conjectured gap $C_3\hbar c\lambda_3$ for $SU(N)$ | proved for free and $U(1)$; formal for $SU(N)$ (Proposition 7); see §3 |
| $1+3$ | exact | 3 | $t=g^2$ fixed: coupling shifts that recur each step; large fields suppressed only as $(a\Lambda)^{2b_0c}$ | running coupling, $\Lambda=\mu e^{-1/(2b_0g^2)}$; small instantons die ($11N/3>4$); dislocations need $c>2/b_0$ ($\tfrac{6}{11}$ of an instanton for $SU(2)$); $U(1)$: Coulomb phase | known (running, 6/11 criterion, Driver); the measure-level route fails for $U(1)$ (proved) |
| $1+n$, $n\ge4$ | exact | $\binom n2$ | $t$ grows as $a\to0$ | no small-field regime; a phase transition, no established continuum limit | known (Creutz for $SU(2)$ in 5D) |

The same heat time $t=\hbar g_{\rm cl}^2a^{4-D}$ controls the column "what one
step leaves". For $D<4$ refining and taking $\hbar\to0$ push it the same
way; in mechanics refining makes each cell more quantum
([dimension ladder](dimension-ladder.md), §2).

## 3. The atlas for $1+2$ by group

| Group | Isolated cube | Full mid-plane | One step, measure level | Iteration and limit |
| --- | --- | --- | --- | --- |
| free ($\mathbb R^n$) | exact | exact defect (Proposition 2 of the series/parallel note) | Gaussian, exact | blocked actions converge to a Gaussian fixed point (known, Bell--Wilson; for this blocking asserted) |
| $U(1)$ | exact (Proposition 3) | exact charge form, vortex bound (Proposition 4, Corollary) | one step equals the free step up to density $e^{-\pi^2/(8t)}$ (Theorem 5, refereed); whole measure within TV $2(L/a)^3e^{-\pi^2/(6\lambda_3a)}$ of the monopole-free part ([monopole note](villain-monopole-refinement.md)) | free photon (Gross 1983, known) |
| $SU(2)$ | midpoint characters exact for every spin; spin-$\frac12$ and spin-1 cube sectors exact, with matrix image bounds for spin 1 ([closed form](su2-midpoint-exact.md), Theorems 1--4) | [formal order-$t$ expansion](su2-midplane-order-t.md): cut shifts positive, transverse negative; other local operators have dimension at least six; explicit torus winding term | formal; needs normalized estimate (18) with winding control | open |
| $SU(3)$ | curvature term explicit, softening $t_j|X_j|^2/512$ (group-general form of Proposition 6) | open | formal | open; the gap $C_3\hbar c\lambda_3$ is the infrared obligation |

## 4. What emerges, read across the atlas

Why ultraviolet halvings bear on an infrared gap is explained, for the
paper, in the [didactic note](uv-halving-ir-confinement.md).

- **Series moves never produce anything new.** In every dimension they
  close exactly for heat-kernel weights, and in mechanics after one
  scalar counterterm. The one-dimensional Newton problem and the
  two-dimensional gauge theory are all series.
- **Parallel moves carry everything that renormalizes.** Their number,
  $\binom{D-1}2$, is zero exactly where the theory is exactly soluble.
- **Additivity is universal; locality is one-dimensional** (2026-09-28).
  Integrating out a Gaussian step leaves the Schur complement of the
  action (the Dirichlet principle), and successive Schur complements
  compose exactly ((13) of the [four-dimensional note](four-dimensional-parallel-log.md));
  in Newton's cell this is Theorem 2 of the [cut-measure note](cut-measure-newton.md).
  Only one dimension grants locality: the minimizer between two cut
  points is the chord, so the blocked action is again nearest-neighbour
  and the series move closes, as in $1+1$. With transverse planes the
  Schur complement is non-local, and its local truncation error is the
  parallel defect ((5) and Corollary 2$_s$ of the
  [series/parallel note](series-parallel-gauge-refinement.md)).
- **The exponential ladder.** Each compact correction left by a step is
  $e^{-c/t}$ (vortices, monopoles, dislocations). In $D<4$ it is summable
  per physical volume at fixed coupling, so compact effects die; in $D=4$
  the running turns it into a power of $a$, so survival is a threshold
  condition; in $D>4$ there is no small $t$. In $1+3$ at one loop,
  $a\Lambda=e^{-1/(2b_0t)}$ with $t=\hbar g^2(a)$, so $e^{-c/t}=(a\Lambda)^{2b_0c}$ and $2b_0c$ is the
  scaling dimension of the correction. The generated gap is itself on the
  ladder: $am\propto e^{-1/(2b_0\hbar g^2)}$ is the member with $2b_0c=1$. The bridge
  image terms sit far above the per-volume threshold $2b_0c=4$: $2b_0c=11N/3$ for
  root images ($c=8\pi^2$) and $33$ for the $SU(3)$ centre images of a
  trisection ($c=24\pi^2$, [centre note](sun-midpoint-centre.md)) (2026-09-28).
  These are formal powers from near-identity image exponents; normalized
  bounds uniform in boundary data and under iteration remain to prove.
- **What survives is trajectory-dependent.** Compact $U(1)$ in $1+2$ keeps
  a gap along $\lambda_3a\simeq c_0/(2\log(1/a))$, $c_0\approx4.99$ the monopole
  exponent, where the monopole density per physical volume diverges, and
  loses it at fixed $\lambda_3$ (Göpfert--Mack versus Gross).
- **The action floor survives what removes the mass gap** (user
  observation, 2026-09-28). With $t=\lambda_3a=\hbar g_{\rm cl}^2a$ the compact corrections
  of a step, $e^{-c/(\hbar g_{\rm cl}^2a)}$, vanish as $a\to0$ at fixed coupling and as $\hbar\to0$
  at fixed $g_{\rm cl}$ and $a$, while the $w=0$ Gaussian term of (9) of the
  series/parallel note, of width set by $\hbar$, remains. Both $U(1)$ continuum
  limits on record are Gaussian: Gross's photon, with field-strength
  covariance $\hbar g_{\rm cl}^2K_0$, and Göpfert--Mack's free massive scalar,
  canonically normalized along a trajectory on which $\lambda_3$ diverges. The
  refinement removes the lattice mass gap and keeps the unit of action,
  and $h$ was first measured in this gapless theory in $1+3$, cavity
  radiation (Planck's talk of 14 December 1900, written up as
  [Ann. Phys. 309, 553 (1901)](https://doi.org/10.1002/andp.19013090310),
  through the resonators' energy elements; the field-mode reading is
  [Debye 1910](https://doi.org/10.1002/andp.19103381617), metadata; a finite
  cavity keeps the box gap $2\pi\hbar c/L$). Two gaps of different kinds: a
  mass gap, generated and trajectory-dependent, and an action floor,
  supplied in $e^{-S/\hbar}$, that every cell of every limit keeps (each cut
  weighted by $e^{-{\rm share}/\hbar}$, cut-measure Prop. 4). In
  [G07](low-dimensional-mass-gap.md)'s terms both are unit multiples of the
  fixed constants; the floor is supplied, while a generated gap needs two
  scale-free structures that do not commute (G07 §1;
  [G08](action-floor-yang-mills-gap.md)).
- **Constants that emerge.** Mechanics: one scalar counterterm per cell,
  and one action constant if joint determinacy is denied (Theorems B and
  B$'$ of the fifth-postulate note). $1+1$: the Lévy exponent (one
  coupling for Yang--Mills). $1+2$: one coupling, shifted summably.
  $1+3$: one scale $\Lambda$ by dimensional transmutation.

## 5. Open cells

1. $SU(2)$ cube: *filled through $J=1$* ([Theorem 4](su2-midpoint-exact.md), exact diagonal entries, image bounds and cube sector); $J>1$ entries and control of the full spin sum remain open.
2. $SU(2)$ full mid-plane in $1+2$: [formal order-$t$ calculation](su2-midplane-order-t.md) refereed as formal, with its winding size clause; [small-field note](su2-midplane-small-field.md), Round 9 refereed Gaussian cancellation and formal fixed-frame pole; Round 11 §9 defines a tree flux response retaining (30), with strip transport (34)--(35) obstructing the resolvent comparison (unrefereed; interacting interpretation formal). Open: cancellation in the full Hessian or short-path response, normalized (18), barrier moments, winding and large fields; Proposition 4's rejection stands.
3. Stability of Hypothesis P($\alpha$) under iteration. *For $U(1)$ in $1+2$,
   reduced to exact Gaussian blocking* (Corollary 2$'$ of the
   [monopole note](villain-monopole-refinement.md)); open for $SU(N)$.
4. $1+3$: [composition](four-dimensional-composition.md), Thms 1--4 refereed by Claude; §7 gives generated cubic/quartic kernels, decay, finite one-step subtracted matching with explicit constants and uniform iteration hypotheses (Round 10, formal, unrefereed); [G1](gaussian-blocking-coupling.md) refereed.
   Open: its (14), uniform subtracted cubic/quartic contractions; sublinear endpoint matching and remainder sum give the average $-2b_0\log2$ (conditional Theorem 4; [one-step shifts](four-dimensional-parallel-log.md) refereed).
5. Time-only halving. *Structural reading, 2026-09-27, of known results.*
   At fixed spatial lattice the electric faces make the series moves:
   heat-kernel electric weights are a semigroup in the time step, so they
   compose exactly. The magnetic faces make the parallel moves: with
   exponential weights $e^{-a_0V}$ they close exactly in their own family,
   since products of such weights add the exponents. The whole defect of a
   time halving is the non-commutation of the two families, and it
   vanishes as $a_0\to0$ by the Trotter product formula
   ([Trotter 1959](https://doi.org/10.1090/S0002-9939-1959-0108732-6);
   [Chernoff 1968](https://doi.org/10.1016/0022-1236(68)90020-7); metadata;
   strong convergence for the Laplacian on $G^E$ plus a bounded magnetic
   potential). This is why the Hamiltonian limit
   ([Kogut and Susskind 1975](https://doi.org/10.1103/PhysRevD.11.395);
   transfer matrix: [Creutz 1977](https://doi.org/10.1103/PhysRevD.15.1128);
   metadata) exists at every fixed spatial lattice, while spatial halving
   leaves the non-closing factor $\Psi$. Open: an operator-norm rate, which
   needs domain estimates for the commutator of the Laplacian with $V$.
6. *Filled 2026-09-27 for Gaussian records*
   ([record as parallel move](newton-record-parallel-move.md)): forgetting a
   record convolves momentum with variance $\hbar^2/(4\sigma^2)$; precisions add in
   parallel; refinement converges iff $\sum\sigma_j^{-2}<\infty$; identity for $\hbar=0$.
7. The infrared: from ultraviolet control in $1+2$ to $C_3>0$.
8. Cuts at any position (§1b), open rows: the free-field independence of
   the limit from the cut sequence (a convergence question for the
   discrete-exterior-calculus Hodge star on nested tensor grids); for
   $SU(3)$, whether triadic refinement, the only kind whose image terms reach
   the centre ([centre note](sun-midpoint-centre.md)), organizes the
   large-field terms better than dyadic refinement.

## 6. Consequence for STATE

STATE carries the mid-term goal and points here. Each result that fills
a cell updates the cell in this note and nothing else; the notes that
prove results remain the record.
