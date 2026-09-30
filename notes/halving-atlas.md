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
  With a mark floor $\kappa$, marks at any finite set of cuts distinguish the
  force with squared statistical distance exactly the spent action over $\kappa$
  (Proposition 7 there), so the cut measure and the record measure coincide.
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
| $SU(2)$ | midpoint characters exact for every spin; spin-$\frac12$ and spin-1 cube sectors exact, with matrix image bounds for spin 1 ([closed form](su2-midpoint-exact.md), Theorems 1--4) | [formal order-$t$ expansion](su2-midplane-order-t.md): cut shifts positive, transverse negative; other local operators have dimension at least six; explicit torus winding term | formal; one-step normalized small-field bound against a covariant reference proved (small-field §§13--14); iteration open | open |
| $SU(3)$ | curvature term explicit, softening $t_j|X_j|^2/512$ (group-general form of Proposition 6) | small-field one-step normalized bounds transcribed from $SU(2)$, $\mathbb Z_3$ sectors, bridge tail by Li--Yau ([small-field §16](su2-midplane-small-field.md), refereed by Astra with corrections); bulk order-$t$ coefficients $\frac32$ times $SU(2)$'s ([order-$t$ §7b](su2-midplane-order-t.md)); large fields open | formal | open; the gap $C_3\hbar c\lambda_3$ is the infrared obligation |

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
  scaling dimension of the correction. This is the bookkeeping of 't Hooft's infrared renormalons, whose
  Borel-plane positions are fixed by $b_0$ and an operator dimension; the
  per-volume threshold $2b_0c=4$ sits at the gluon-condensate renormalon
  (['t Hooft, Erice 1977, publ. 1979](https://doi.org/10.1007/978-1-4684-0991-8_17);
  metadata, renormalon positions quoted from memory). The generated gap is itself on the
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
2. $SU(2)$ full mid-plane in $1+2$:
   [order-$t$ calculation](su2-midplane-order-t.md) refereed as formal;
   [small-field note §§12--14](su2-midplane-small-field.md), Rounds 14--16,
   refereed by Claude: a covariant Gaussian reference with 't Hooft flux
   sectors, and normalized weak P($1/2-\delta$) against it for one barriered
   step, uniformly in plane size, for equal and unequal boundary layers
   with the cut faces budgeted (saddle determinant, Laplace remainder and
   amplitudes included; remainder densities face-local in size).
   Rounds 17--24 (§§17--24, refereed): the pair kernel (89), the
   link-coordinate form of (27), and the separated third response (93)
   hold on the barriered chart with explicit constants, uniformly in
   plane size; all-order response identities and a barrier-jet obstruction
   (§23); an undifferentiated small-field/large-field split with joint
   bad-set rarity $p^{|H|/16}$ (§24); the error exponent
   $\alpha'=\frac12-3\delta$, $\delta<\frac1{10}$, absorbing the proved
   bare scales (§25); the full response through third order, contacts
   included (§26, refereed). §27 gives the three-bad-component tree
   bound (120), with rarity $p^{M/64}$ and decay $\frac12\log(12/5)$;
   §28 gives a factorizing reference, uniform convexity and rarity along
   real decoupling paths, and the one-connector bound (128) (both written,
   unrefereed). [§29](su2-midplane-small-field.md#29-all-order-connector-moments-and-a-uniform-analytic-source-ball)
   controls arbitrary connector moments and connected growth, and gives
   a uniform complex $\ell^1$ source ball. [§30](su2-midplane-small-field.md#30-an-anchored-two-connector-tree-and-its-spatial-sum)
   proves the anchored two-connector tree (135) and its summed spatial
   reserve (140), with the earlier gradient bound retained after a proof
   repair. [§31](su2-midplane-small-field.md#31-all-order-anchored-attachments-at-the-exact-gaussian-endpoint)
   proves all-order anchored attachments (142) and a zero-free uniform
   polydisc at the exact Gaussian, unbarriered endpoint (Sol/Astra,
   written). [§32](su2-midplane-small-field.md#32-a-retained-barrier-pointwise-logarithms-and-a-direct-density-norm)
   isolates a pointwise complex-logarithm failure and proves the direct
   all-order density norm (148) with radial barriers in a factorized
   reference (2026-09-30, Sol/Astra, refereed).
   [§33](su2-midplane-small-field.md#33-retained-barriers-and-nonlinear-connectors-in-a-weak-recoupling-strip)
   gives a convergent nonlinear interaction expansion with retained
   barriers, uniform weak-recoupling polydisc (154) and fixed spatial
   reserve (Sol/Astra, refereed). Next: mark the bad observable and
   retain rarity in its integrated density norm; recoupling to one
   remains separate. Then dressed activities (112) and boundary polydiscs (113), yielding (94);
   then target-covering paths, curvature conversion, full-integral
   comparison, perturbed-action stability and iteration. The fixed-frame
   transport-value comparison remains open; Proposition 4's rejection stands.
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
   [Complete-record tests, §§6--7](sed-closure-under-recording.md#7-adaptive-records-innovation-replacement-and-refinement)
   (2026-09-29, written, unrefereed): the repaired two-pointer model obeys
   the area floor iff its readout error/kick determinant remains at least
   $\kappa^2$ conditional on side records; a noisy kick monitor breaks a
   marginally saturated repair. Adaptive affinity is exact in the
   branchwise information (41); monitor replacement has cost (46).
   A [finite harmonic refinement bound](refinement-composition-and-limit.md#3b-harmonic-polygons-a-finite-refinement-bound-from-a-different-norm)
   from the Lean norm obstacle gives complete-record convergence under
   the additional conditional noise budget (49).
   [Hamiltonian memory, §8](sed-closure-under-recording.md#8-hamiltonian-memory-terminal-records-and-blocking)
   realizes the monitor cost and proves terminal posterior closure from
   the joint initial covariance restriction; linear blocking preserves
   it for the same body. §§8.4--8.6 give a genuine two-time physical copy
   refinement with an explicit relative kick and joint-law defect (62),
   and a partition-uniform complete-record information bound (63), even
   at zero action (Sol/Astra, written). [§§8.7--8.9](sed-closure-under-recording.md#87-an-associative-descriptor-with-the-physical-kicks-retained)
   retain every copy kick in associative Gaussian descriptors and prove
   a partition-independent projected terminal law with the explicit mesh
   rate (73). The three-cell residue (69) has rank two; the prescribed
   pair plus one independent additive scalar cannot reproduce it
   (2026-09-30, Sol/Astra, refereed). [§8.10](sed-closure-under-recording.md#810-a-physical-adaptive-gain-controller-with-complete-record-closure)
   includes physical adaptive gains and their conjugate recoil, with
   complete-record posterior closure (76) and uniform continuity (77).
   Next: an inserted-cell comparison for a prescribed physical feedback
   policy. Adaptive timing remains separate.
   The limit of the full growing record and the independent positive
   scale remain open.
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
