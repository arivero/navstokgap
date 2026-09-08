# Newtonian trajectories and action scales

This project studies how mechanical action, trajectory fluctuations and physical
resolution are related. Its research targets are a reconstruction of quantum
mechanics from explicit physical premises and a toy model that explains how a
specified gap forms. Newton's geometric limits provide the starting example;
finite propagation speed, Navier–Stokes and Yang–Mills provide companion questions
about estimates and limits.

## Results to read first

The [spectral-control paper](out/papers/susceptibility-gap.pdf) gives a
sufficient condition for a lower relaxation gap: observables must detect every
mode, and their total susceptibility must stay bounded. A four-state example
shows how a fixed positive velocity plateau can miss a slowing internal mode.

The [checkerboard paper](out/papers/checkerboard-dynamics.pdf) compares two
path-composition rules at the same action scale: classical transitions and
coherent amplitudes. It proves the Dirac wavepacket limit and shows why
measuring direction at every cut instead gives a ballistic limit. The next
test, now developed above, asks which spectral modes the classical plateau controls.

The finite-speed return bridge now has an exact midpoint crossover: cubic
short-window variance converges to its shared long-window action plateau.
The [crossover paper](out/papers/bridge-crossover.pdf) proves the beta mixture
and shows why a positive coefficient across arbitrarily small masses requires
mass-dependent observation windows.

Independent composition makes a nonnegative mass-only action coefficient
universal within a stated preparation class. One finite-rate, nonzero-speed
reference then makes its shared plateau positive. The
[composition paper](out/papers/composition-universality.pdf) proves these
conditional results and tests their preparation and correlation premises.

A finite-speed return bridge retains velocity memory and a discrete midpoint
mass while allowing arbitrarily fine, consistent observation cuts. The
[return-bridge paper](out/papers/telegraph-return-bridge.pdf) proves that the
sampled polygon's action converges to the path's kinetic action, with error
bounded by switch count times mesh. Next we test finite-duration turns under
an acceleration ceiling.

A conserved elastic collision realizes a random midpoint, while finite speed
imposes the sharp action-coefficient bound $\kappa_{\rm mid}\le
m\Delta(u-|v|)^2$. The [physical-cut paper](out/papers/physical-cut-speed.pdf)
also shows why stochastic finite-speed refinement needs more information than
independent position increments. The return bridge implements that memory.

Inserting cut points into the same Gaussian bridge experiment preserves its
action parameter $\kappa$ and adds mean kinetic action $\kappa/2$ per node.
The earlier finite-defect scaling changes the experiment's coarse variances.
The [cut-point paper](out/papers/cut-point-consistency.pdf) proves this distinction
and the vanishing chord-error bound for arbitrary nonuniform partitions.

A finite reversible classical velocity process produces a positive limiting
action coefficient, $H_*=2m\int_0^\infty C(s)\,ds$. For a particle moving
at $\pm u$ with reversal rate $\lambda$, this is $mu^2/\lambda$.
The [new paper](out/papers/classical-action-field.pdf) gives the proof,
finite-speed short-time bound and source audit. The next question is which
mechanical law could make this coefficient universal.

Paths can approach a classical trajectory uniformly while retaining finite
excess kinetic action. In the exactly soluble Gaussian bridge, $d$ internal
positions give mean excess $d\kappa/2$; taking $\kappa\to0$ with
$d\kappa\to\ell$ leaves residual action $\ell/2$. The
[regulator-limits paper](out/papers/regulator-limits.pdf) gives the proof, a bounded-speed
control example and the two-regulator normalization audit.

For a perpendicular launch in a constant force, the chord–curve comparison gives

$$\Delta S=\frac{F^2T^3}{24m}
=\frac{F}{2v_0}\mathcal A_{\rm lens}
=\frac{T\delta E}{12},\qquad \delta E=\Delta K=-\Delta V.$$

The neighbouring family $\eta=a t(T-t)$ has action excess $ma^2T^3/6$:
positive values approach zero continuously. In a quantum two-arm experiment,
fixing the copy count and target success probability instead gives an explicit
positive resolution threshold. Together these results identify the path class
and measurement resources as central choices in a gap model.

- [Technical foundations PDF](out/papers/action-gap-foundations.pdf): proofs of the action identities, variation result and finite-copy threshold; Jacobi operator and free-kernel calculations.
- [Time-refinement PDF](out/papers/time-refinement.pdf): exact Gaussian blocking and its surviving action parameter.
- [Research programme PDF](out/papers/research-programme.pdf): questions, model sequence and work packages.
- [Claim ledger](claims/LEDGER.md): assumptions, evidence status and review record.
- [LaTeX sources and build](papers/README.md).

## Next experiments

The mass-composition test is complete; next are crossover/checkerboard dynamics
and a susceptibility–spectral-gap comparison. The
[six-direction review](reviews/six-directions-2026-09-08.md) records the
adopted premises, countertests and source leads. Bounded-force returns remain
the supporting mechanical diagnostic.

Return to the [cut-point continuum limit](research/CUT_POINT_TARGET.md): test
which physical refinement condition could force a positive action remainder.
The [collision paper](out/papers/collision-action-relaxation.pdf) supplies a
physical-time relaxation comparison, with its reservoir scale explicit.
The [supplied polygon ideas](ideas/I002-newton-polygon-threshold.md) and
[receding-centre draft audit](notes/receding-centre-area-audit.md) sharpen the
geometry and threshold premises. Alongside this, test how
force control and a relativistic kinetic action affect the shrinking
oscillations and their action defect. The [M06 plan](notes/two-regulator-audit.md)
connects that calculation to the bibliography and the physical scale-selection
question. The oscillator/free-particle spectral draft, Classical Scholia corpus
and quantum reconstruction axioms remain complementary work tracks.

The [programme](research/PROGRAMME.md) develops this sequence. The
[idea register](ideas/I001-action-field.md) preserves the proposed extra
action-like field and the calculations that would give it a precise meaning.

## Start or restart a session

Read [AGENTS.md](AGENTS.md), [STATE.md](research/STATE.md), the
[programme](research/PROGRAMME.md) and the selected [task](research/TASKS.md).
These files carry the project context across sessions.

Example: “Execute M03: compare the oscillator and free-particle operators, state
their domains, derive the gaps and record the checks and handoff.”

Luna handles bounded bibliography work; Sol handles source collation and small
calculations. The [agent protocol](agents/PROTOCOL.md) specifies ownership,
review and model/effort reporting. The user prohibits ultra effort.
Delegation is sequential: one Sol or Luna worker, followed by coordinator review.

## Reproduce and inspect

Run `make check` and `make papers` from the root. Python/SymPy and the
existing LaTeX tools support the present results. The
[tooling guide](research/TOOLS.md) describes dependencies and build checks;
[formalisation task F01](formal/README.md) defines the first Lean target.

| Location | Contents |
| --- | --- |
| `papers/`, `out/papers/` | LaTeX manuscripts and readable PDFs |
| `notes/`, `claims/`, `ideas/` | Derivations, evidence ledger and model proposals |
| `docs/`, `references/` | Source originals/companions, BibTeX and search batches |
| `research/`, `agents/`, `skills/` | Programme, task state, handoffs and session instructions |
| `scripts/`, `out/`, `formal/`, `reviews/` | Checks, outputs, formalisation targets and reviews |

## Sources and project background

- [Introducing navstokgap](docs/blog/introducing-navstokgap.md): a first-person blog entry on the project and research across model generations.
- [Principia geometry and action](notes/principia-constant-force-action.md): exact areas and their historical anchors.
- [NATP00385 audit](notes/newton-NATP00385-audit.md): Newton's account of analytic discovery and synthetic presentation.
- [Source catalogue](docs/README.md), [shared bibliography](references/library.bib), [B01 reading queue](references/batches/B01.md).
- [Millennium definitions](notes/millennium-problem-definitions.md), [comparison and bridges](notes/comparison-and-bridges.md), [first review](reviews/first-milestone.md).

The initial orientation also consulted the [Astra release](https://openai.com/index/gpt-6-astra/)
and [reported mathematical advances](https://openai.com/index/ten-advances-in-mathematics/).
The research record itself is organized around the sources and derivations above.
