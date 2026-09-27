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

### 1b. Cuts at any position (user remark, 2026-09-27)

Halving is the easiest cut; any cut at fraction $s\in(0,1)$ of a cell
performs the same two moves, with $s$ as a parameter.

- **Series move.** The cut face splits into heat times $st$ and $(1-s)t$;
  the convolution returns $t$ exactly, for heat-kernel weights, in every
  dimension.
- **Parallel move.** In $D=3$ the transverse copies get heat times $t/s$
  and $t/(1-s)$; at the quadratic level precisions add,
  $s/t+(1-s)/t=1/t$. The inserted edges carry the bridge law observed at
  fraction $s$, variance $s(1-s)t_e$ in place of $t_e/4$. Halving
  maximizes the bridge variance, so each non-symmetric cut is gentler
  than a halving; the $s$-dependence of the defect bounds (Prop. 2,
  Theorem 5) is expected through $4s(1-s)$ and has not been derived.
- **Newton.** The cell action $K_\tau=F^2\tau^3/(24m)$
  ([two-path note](galileo-two-path-interference.md)) obeys
  $\tau^3=(s\tau)^3+((1-s)\tau)^3+3s(1-s)\tau^3$, so one cut removes exactly
  $3s(1-s)K_\tau$, at most $\frac34K_\tau$ (halving). Along any sequence of cuts
  whose mesh tends to zero the removed amounts sum to $K_\tau$, whatever
  the positions and order (the remainder is $\sum_i C\tau_i^3\le C\tau\max_i\tau_i^2$).
  The Galileo action is therefore an additive measure on the cut
  process: the refinement limit is cut-independent, and every cut
  spends a definite share of the action that Newton sends to zero. This
  is the Lévy–Ciesielski structure of the Brownian bridge (variance
  $s(1-s)$ at each dyadic or non-dyadic insertion) seen in the action.
- **The frame.** A cut at an arbitrary, even irrational, position is the
  geometers' cut of Book I's closing scholium. The questions for each
  cell become: does the limit depend on the cut sequence (for the free
  field and for Newton, no), and does the universal part (the $\log2$ of
  cell 4, which for general cuts should read $\log(1/s)$ summed over the
  step) survive when $s$ varies (conjecture: yes, as the scheme-
  independent one-loop coefficient).

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

- **Series moves never produce anything new.** In every dimension they
  close exactly for heat-kernel weights, and in mechanics after one
  scalar counterterm. The one-dimensional Newton problem and the
  two-dimensional gauge theory are all series.
- **Parallel moves carry everything that renormalizes.** Their number,
  $\binom{D-1}2$, is zero exactly where the theory is exactly soluble.
- **The exponential ladder.** Each compact correction left by a step is
  $e^{-c/t}$ (vortices, monopoles, dislocations). In $D<4$ it is summable
  per physical volume at fixed coupling, so compact effects die; in $D=4$
  the running turns it into a power of $a$, so survival is a threshold
  condition; in $D>4$ there is no small $t$.
- **What survives is trajectory-dependent.** Compact $U(1)$ in $1+2$ keeps
  a gap along $\lambda_3a\simeq c_0/(2\log(1/a))$, $c_0\approx4.99$ the monopole
  exponent, where the monopole density per physical volume diverges, and
  loses it at fixed $\lambda_3$ (Göpfert--Mack versus Gross).
- **Constants that emerge.** Mechanics: one scalar counterterm per cell,
  and one action constant if joint determinacy is denied (Theorems B and
  B$'$ of the fifth-postulate note). $1+1$: the Lévy exponent (one
  coupling for Yang--Mills). $1+2$: one coupling, shifted summably.
  $1+3$: one scale $\Lambda$ by dimensional transmutation.

## 5. Open cells

1. $SU(2)$ cube: *filled through $J=1$* ([Theorem 4](su2-midpoint-exact.md), exact diagonal entries, image bounds and cube sector); $J>1$ entries and control of the full spin sum remain open.
2. $SU(2)$ full mid-plane in $1+2$: [formal order-$t$ calculation filled](su2-midplane-order-t.md), refereed (all items accepted): cut shifts positive, transverse negative, remaining bulk terms of dimension six; the fixed-torus winding term is removed by the clause $\min_jN_j\ge c_0/t$; open: the uniform estimate (18).
3. Stability of Hypothesis P($\alpha$) under iteration. *For $U(1)$ in $1+2$,
   reduced to exact Gaussian blocking* (Corollary 2$'$ of the
   [monopole note](villain-monopole-refinement.md)); open for $SU(N)$.
4. $1+3$: the one-loop coefficient $-2b_0\log2$ per isotropic step from the
   three parallel insertions of each halving.
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

## 6. Consequence for STATE

STATE carries the mid-term goal and points here. Each result that fills
a cell updates the cell in this note and nothing else; the notes that
prove results remain the record.
