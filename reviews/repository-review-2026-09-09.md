# Repository review: from transport coefficients to a mechanical action scale

Review checkpoint: 9 September 2026, starting at commit `0632c7d`.

The repository has a useful collection of exact mechanical, probabilistic and
spectral tests. Its strongest next advance is to reconnect those tests to
bound central-force motion and a precisely chosen action observable. Continue
the transport laboratory, repair I003's generalizations, and develop the
classical relativistic Kepler threshold as a positive-bound benchmark.

## 1. What the review covered

This is a repository-wide scientific and workflow review: the accepted claim
ledger, maintained mathematical manuscripts/notes, M03 and I003 drafts, idea
register, Millennium comparison, source coverage records, restart/task files,
build scripts and agent protocol. Generated TeX is checked against its source
note rather than treated as an independent proof. Historical source originals
are assessed through their companions and recorded coverage; this review does
not reread the entire historical corpus or independently audit the 165-page
Navier–Stokes proof.

One sequential Sol-medium librarian performed B27, with three discovery
queries and four selected PDF pages. Coordinator checked those page images
and metadata, and rechecked the public Navier–Stokes announcement. Mathematical
review used written reasoning; no numerical or symbolic verification script ran.

## 2. Findings requiring action

### The long-window coefficient is a transport diagnostic

The maintained observable is

$$\mathsf h_\Delta(t)=\frac m\Delta\operatorname{Var}
[X(t+\Delta)-X(t)].$$

C019–C020 and C050 identify it with twice the mass times a diffusion coefficient
in their long-window regimes. C047 and C051 already demonstrate that bounded
or periodically cancelling motion can instead give zero. Consequently a
definition intended to cover Kepler or oscillator states needs more than
the long-window displacement response of a bound coordinate.

The reusable argument in C047 is variance control: a stationary coordinate
with finite variance $B$ has increment variance at most $4B$, and the
corresponding long-window coefficient vanishes. This identifies an observable
selection issue, not a failure of the mechanics. The next comparison should
separate a local/coarse-grained noise coefficient, an intermediate-window
plateau, an orbital action, and a long-window transport coefficient.

### I003 contains valuable ideas and incorrect generalizations

The finite-propagation/first-order-system question is worth retaining. The
original `i003-double-limit-rigidity` draft needs these repairs:

1. **Fourier convention:** use $M_t(k)=e^{t(B-ikA)}$ for
   $\partial_t\psi=-A\partial_x\psi+B\psi$. A unitary model has Hermitian
   $A$ and anti-Hermitian $B$. The draft changed the meaning of its linear
   coefficient midway through the proof, introducing an extra factor of $i$.
2. **Mass preservation:** positivity plus $L^2$ contraction allows killing.
   $T_tf=e^{-t}f$ is positive, contractive, translation invariant and supported
   at zero. Its component generator is not conservative. Conservation must be
   assumed to conclude that a switching matrix is a Markov generator.
3. **Commuting velocities:** random constant velocity $V=\pm u$ has
   $[V,Q]=0$ with $Q=0$, yet $\mathsf h(\Delta)=mu^2\Delta$.
   The draft's zero-coefficient conclusion contradicts its own ballistic
   variance statement and C047's random-centre example.
4. **One commutator, many scales:** the two-state formulas are exact within
   that specialization. Extra switching modes and preparations invalidate the
   claim of a unique scale for the full matrix class. C041–C046 already show
   how hidden modes and observable access change the answer.
5. **Resolution errors:** independent additive errors with variance
   $\varepsilon^2/12$ give the displayed variance term. Ordinary deterministic
   rounding does not automatically have this law. The result needs a stated
   noise/dither measurement model, including endpoint treatment for a bridge.

The revision keeps the rigidity candidate, exact two-state comparison and
measurement-noise test, with their remaining proof/audit tasks. The earlier
draft remains recoverable at the starting commit; no accepted ledger claim
is withdrawn by these draft corrections.

### Current-state and tooling drift obscures the research

The README still points to tasks completed several milestones ago; programme
and restart files accumulate incompatible “next” instructions. The paper index
omits several built manuscripts and describes the collision paper only through
A02. These are navigation problems, not mathematical disputes.

`make check` is correctly restricted to document/source integrity. However,
`make figures` invokes `constant_force_geometry.py`, which performs SymPy
verification before drawing. That command conflicts with the hard rule and
is now disabled. Maintained notes and two manuscripts also retained imperative
instructions to run historical verification scripts; these are replaced by
historical-artifact descriptions. Existing figures, scripts and outputs remain.

The Millennium definitions contain an obsolete claim that the OpenAI result
has no public artifact. The repository already has its source companion and
cached PDF. The live announcement supplies a paper and formalization, while
our reading remains an attributed first-reading rather than an independent
proof audit. The official problem definitions are unchanged.

## 3. Strong material to preserve

The following synthesis is the current scientific asset, even where its
ingredients are established literature:

| Family | What it establishes | Role in the programme |
| --- | --- | --- |
| C001–C008 | Exact geometry, continuous variation costs, operational threshold and kernel normalization | Fix the objects and physical inputs |
| C009–C017, C027–C029 | Cut consistency and joint path/action limits | Separate mesh, coefficient and derivative topology |
| C018–C024, C047–C051 | Positive, zero and preparation-dependent action responses | Test mechanical clocks and correlation assumptions |
| C030–C034, C037–C040, C043–C044 | Finite-speed cuts, conditioned bridges, coherent steps and controlled turns | Separate sampling, intervention and path-weight rules |
| C035–C036 | Conditional mass universality under coefficient closure | Expose the whole/parts preparation premise |
| C041–C042, C045–C046 | Observable-response bounds and hidden-mode countertests | State what a spectral-gap transfer must control |
| M03 draft | Topological sector minima versus quantum and Hessian gaps | Positive-bound laboratory awaiting its remaining review gates |

An unmatched formula in a short source search is a candidate for further
comparison, not a novelty certificate. The strongest publication prospect is
the integrated comparison of mechanisms and limits, supported by explicit
proofs and a transparent premise map.

## 4. Highest-leverage new directions

### A. Relativistic Kepler: a positive action-valued threshold

For the fixed-centre Hamiltonian

$$H=\sqrt{m^2c^4+c^2(p_r^2+L^2/r^2)}-\frac{k}{r},
\qquad r>0,\quad m,k,c>0,$$

the collision-free bound radial well exists exactly for $|L|>k/c$, with
minimum energy

$$E_{\min}=mc^2\sqrt{1-\left(\frac{k}{c|L|}\right)^2}.$$

[Boyer's primary paper](https://arxiv.org/abs/physics/0405090v1), pp. 5–6,
9–10, supplies the classification; B27 records the reading. This is established
classical relativistic mechanics, newly useful to this repository. It supplies
a positive lower edge in angular action for a precisely defined class of
global bound trajectories, with $1/c$ essential to the bound. The value is
coupling-dependent and the action values above it remain continuous.

**M07:** derive the radial well and endpoint carefully, compare Newtonian
and relativistic admissible orbits, then distinguish this survival threshold
from an orbital action lattice and a universal action coefficient. Test small
changes of potential and centre assumptions. Preserve fixed-centre and
external-potential hypotheses; radiation and a closed relativistic two-body
system are additional models.

### B. A local or intermediate-window observable for bound motion

**A15:** use one confined model to compare three measurements of the same
preparation: local/coarse-grained fluctuation strength, intermediate-window
response, and long-window displacement response. A plausible regime is
$\tau_{\rm micro}\ll\Delta\ll\tau_{\rm confinement}$; its existence and
uniformity must be proved for the chosen family.

This is a repair of the observable's scope, not abandonment of A01–A14.
If a candidate cannot distinguish “vanishing transport through confinement”
from “vanishing local fluctuation scale,” it cannot serve as the global
definition of the intended $h(t)$ field. Stationary response and physical-time
attraction still require separate arguments.

### C. Quantitative preparation control through renewal streams

**A14:** retain the two-stream free-line construction, replace each Poisson
or lattice stream by a stationary renewal process, and derive the Palm
residual and subsequent flight laws. Hold mass, speed and mean density fixed.
The useful calculation is the relation between gap fluctuations and tagged
variance growth, including a near-ordered family.

Deliver one result that settles which quantitative premise maintains a
positive response. Then return to the central selection question rather than
proliferating independent solvable clocks. A14's expected rate/variance
relation is a research target until the moment proof and source audit finish.

### D. Symmetry and dimensional-selection audit

**A16:** test whether the proposed classical axiom class admits a simultaneous
space/time dilation preserving velocity and $c$ while changing action units
physically. For a candidate transformation, track the potential, force,
preparation, orbital actions and response coefficient explicitly. Distinguish
a new physical model from a change of measurement units.

This could consolidate several scale-closing examples into one precise
selection test: identify which dimensionful coupling, preparation rule or
broken scaling symmetry holds the action scale fixed. Keep fixed couplings
fixed when the model class requires them. The Kepler benchmark makes that
distinction concrete through $k/c$.

### E. Preserve and repair finite-propagation rigidity

**R02:** first audit the scalar compact-support/unitarity result, then the
matrix contraction classification with a consistent Fourier convention and
explicit conservation assumptions. Bernstein or compact-convolution support
arguments are useful proof routes. Retain the cone/arrow relation as a modern
model analogy, with historical reception audited separately.

This connects finite speed to internal state structure, a question distinct
from selecting the size of an action coefficient. It is worth pursuing even
if it leaves that coefficient free.

## 5. Shorter route through the remaining programme

Recommended sequence: **M07 and A15 first**, then a bounded A14 theorem.
R02 is the next technical draft review; A16 is a cross-model premise test.
B11 remains a valuable small source task because the receding-centre
matched-endpoint calculation reconnects the work to Newton's geometry.

M06's first part should reuse A07/C044 and the standard derivative-compactness
argument rather than restart the same force-control calculation. Its genuinely
additional task is the relativistic action on shrinking oscillations. G03 can
extend G02 from independent factors to a specified interaction, with a uniform
observable/response estimate. Q01 retains the actual reconstruction question:
which physical premise selects coherent composition, and where action units
enter. These branches should stay visible rather than be replaced by transport
counterexamples.

The historical corpus now includes concrete early-modern cone/divisibility
material; a blanket “the cone was never invoked” narrative is not the right
research claim. H02/H03 and H05 should identify Newton-specific witnesses,
chronology and use, preserving the distinction between access, quotation and
influence. Existing source capsules are a better next input than another broad
download batch.

Formalization remains selective. The current Lean file is explicitly uncompiled
and has no pinned toolchain. Installing a large stack for a two-line real-number
inequality offers little immediate research leverage. Reconsider it for the
repaired rigidity argument or a stable central-force theorem, while retaining
human-readable proofs as the main objects.

## 6. Consolidation and preservation

Keep theorem IDs, proofs and source audits. Organize a future reading edition
into four parts: geometry/refinement; mechanical response/composition;
finite-speed probability/coherence; and gap mechanisms/companion limits.
A01/A02/A08/A10–A14 share the response definition and belong in a common
part. A06/A09a are already merged. A07 and M06 share derivative-control
context. M03, G01/G02 and M07 should sit beside each other without conflating
their different gap objects.

This review labels obsolete next-step instructions as history and supersedes false
draft assertions. It preserves the scalar rigidity idea, the commutator
specialization, measurement-resolution test, Newton geometry, winding sectors,
all accepted claims and original source/historical records. Earlier text remains
recoverable in Git. No source original or accepted mathematical result is deleted.
