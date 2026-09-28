# From the continuum to discrete substrates: 't Hooft and other turns

**Conversation record, 2026-09-28 (user and Claude, with a from-memory
answer by Claude Fable).** All references below are quoted from memory
and have not been verified; they are leads for the prior-art section of
the fifth-postulate paper, and no result here is claimed.

Conversation with the user, 2026-09-28 night (not yet in any repo note; references from memory, unverified).

**'t Hooft** (Fable's memory, high/medium confidence): renormalizability and beta<0 (Marseille 1972); only first two beta coefficients scheme-independent (limits "2 b0 per log" beyond one loop); renormalons (Erice late 1970s) = the atlas exponential ladder, threshold 2 b0 c = 4 is the gluon-condensate renormalon; instantons e^{-8 pi^2/g^2}, U(1) problem; 't Hooft loop B(C) (NPB 138, 1978) = our mid-edge centre flip; twisted b.c. and e/m flux sectors (NPB 153, 1979), fractional charge 1/N mod 1 (1/3 for SU(3), fits the trisection result); the round-12 non-based-cycle Aharonov-Bohm phase is the small-angle part of his flux-sector data (round-14 prompt now asks Astra to state the covariant reference sector by sector); abelian projection 1981; large N 1974. Cellular-automaton interpretation (1988 on, book 2016): hbar enters as a conversion constant tied to the time grain delta-t; the floor comes from information loss (equivalence classes give H bounded below). This is the exact opposite of the user's thesis on the same RG ground: he supplies hbar from below; we ask whether consistent refinement forces it.

**Candidate next Newton premise** (proposed, not yet sent to Astra): take 't Hooft's information-loss/equivalence-class construction as the physical premise and ask whether it bounds the recorded Galileo comparison. Contact point: our thermodynamic-records note gave only eta >= A0 e^{-W/kBT}, no floor. Put this to an Astra decision round after round 14.

**User's remarks:** "as soon as you really understand the RG then you don't understand any" (amused); read Wolfram in the eighties thinking "how will he reach a continuum limit", yet the Newton thesis says the continuum limit is problematic from the start, so "a bit bipolar". Claude's reply: same fault line from two sides; the atlas takes the limit and asks what survives.

**Wolfram** (Caltech ~1979, QCD phenomenology, Fox-Wolfram moments; cellular automata 1981-82; NKS 2002; hypergraph physics 2020). **Cvitanovic** (Kinoshita's group, QED g-2; birdtracks from colour factors, book 2008, useful notation for our SU(N) Brauer-Klimyk sums; chaos via the Feigenbaum-Cvitanovic RG fixed point, ChaosBook).

**Other "Damascus" actors listed:** divergence-driven: Heisenberg universal length (1938), Snyder quantized spacetime (1947), Yukawa elementary domains, Dirac's lifelong rejection of renormalization. RG masters going deterministic/discrete: T. D. Lee discrete time (1983), Adler trace dynamics (2004), H. B. Nielsen random dynamics, Feynman checkerboard and "Simulating physics with computers" (1982). Geometry to combinatorics: Regge, Penrose spin networks, Finkelstein space-time code (1969), Sorkin causal sets, Ambjorn-Loll, Wheeler "it from bit", von Weizsacker ur-alternatives. **Closest to the Newton thesis:** Gisin and Del Santo (~2019-21), finite information makes classical mechanics indeterministic (denial of the velocitas ultima from quantum information) but give no hbar; the fifth-postulate paper should cite and answer them. Proposed paper sentence: field theorists went discrete to escape infinities; RG masters to explain the quantum; Gisin/Del Santo to break determinism; the user's thesis keeps the continuum and shows consistent refinement demands the constant Newton's limit dropped.

Related: [STATE](../research/STATE.md), [fifth postulate](principia-fifth-postulate.md), [stochastic route](stochastic-route-velocitas-ultima.md), [thermodynamic records](thermodynamic-records-no-floor.md).

## 't Hooft's automaton against Zeno, the atomists and Newton

Added 2026-09-29 (Claude), at the user's request. The automaton papers
are identified by DOI (Crossref-verified, metadata only): the
[1988 equivalence relations](https://doi.org/10.1007/BF01011560), the
[1999 dissipative deterministic system](https://doi.org/10.1088/0264-9381/16/10/316)
and the [2016 book](https://doi.org/10.1007/978-3-319-41285-6). What follows
is a reading of his position as Fable and Claude remember it, set against
the classics entries of the [Planck paper](planck-gap-paper.md) §§7 and 9.

**His commitments.** Reality is a deterministic automaton with a universal
time step $\delta t$. A reversible automaton is a permutation of states, so its
evolution operator has eigenvalues on the unit circle and energies defined
only modulo $2\pi\hbar/\delta t$: $\hbar$ is the conversion between the step and an
energy, and the spectrum has no ground state. Information loss, many
states merging into one equivalence class, is what he invokes to obtain a
Hamiltonian bounded below. Quantum mechanics is the description of the
classes; Bell correlations are paid for by superdeterminism.

- **Zeno and Diodorus.** At a tick the automaton holds a configuration and
  motion exists only as the update between ticks: Diodorus's "a thing
  never is moving, but it has moved", made into dynamics. The Planck paper
  keeps Zeno's conclusion for local records only, below the window
  $\tau_{\rm arrow}=8z^2\kappa/(mv^2)$, which depends on the body and the confidence.
  The automaton makes the arrow exact at every scale below $\delta t$ and for
  every body.
- **Democritus and the kalam atom.** The automaton's cells and ticks are
  atoms of place and time, the kalam position on time and a stepped cone
  in Democritus's dilemma. The Planck paper denies the universal time
  atom on the evidence of records: its mesh moves with $F$, $m$ and the
  confidence, a dynamical resolution. The two are compatible: a universal
  grain far below every mark mesh leaves Theorem 9 untouched. They differ
  in status: the grain is ontological, the mesh is epistemic.
- **Epicurus.** Continuity presented to sense, succession below it, and
  a warning against extrapolating continuity downward: this is 't Hooft's
  picture with the Planck time in place of the threshold of sense.
  Epicurus is the closest ancient statement of it, as he is of ours; the
  difference is where the boundary is drawn and whether it is derived.
- **Newton.** The automaton removes the *velocitas ultima* by removing the
  limit: velocities are finite differences and no instant carries one.
  That is a third denial of joint determinacy, beside quantum
  noncommutativity (Theorem A) and stochastic paths (the
  [stochastic route](stochastic-route-velocitas-ultima.md)), and it keeps
  determinism. Its $\hbar$ is a unit conversion, so the automaton alone supplies a
  grain and no action floor on records: a reversible automaton is a
  discrete Liouville dynamics, and Theorem I of the
  [unit-and-indeterminacy note](necessity-unit-and-indeterminacy.md) gives
  classical readouts no floor. The floor, in his construction, rides on
  information loss, and the [thermodynamic-records note](thermodynamic-records-no-floor.md)
  finds that loss yields a trade-off $\eta\ge A_0e^{-W/k_BT}$ and no floor.

**The sharp question this leaves**, the candidate Newton premise above:
does coarse-graining by equivalence classes, of the kind that gives his
Hamiltonian a ground state, force a positive floor on the recorded
inertial--parabola comparison, or only a trade-off? The repository's
current results point to the second; a theorem either way would place
the automaton exactly relative to the thesis that quantization is a
consistency condition of the continuum limit.

## Later the same night: superdeterminism and Dedekind's cut

**Superdeterminism** (user: "classical mechanics is accidentally
superdeterminist too, and we think it has some mistake somewhere").
From memory: Bell called the independence of settings and hidden
variables "free variables" (exchange with Shimony, Horne and Clauser,
around 1976--77) and named the escape "super-deterministic" in a 1985 BBC
interview (*The Ghost in the Atom*, 1986); Brans gave a model in 1988;
't Hooft adopted it in the 2000s; Hossenfelder and Palmer revived it in
2020. The link the user and Claude found interesting is developed in the
[superdeterminism note](superdeterminism-floor.md): for chaotic setting
devices, a superdeterministic correlation must be stored in structure of
the initial data finer than any fixed resolution, so a floor gives it an
Ehrenfest-type lifetime and $h\to0$ reopens the loophole.

**Dedekind's cut** (user: "Dedekind cuts are peculiar, as they define a
point as a segment, really"). Dedekind (1872) defines a real number by
the two segments of rationals it separates: the point is given by what
lies on either side, and fixing it needs infinitely many comparisons.
The intuitionists, and after them Gisin and Del Santo (from memory:
finite-information quantities whose digits are fixed progressively,
around 2019--21), refuse the completed cut: a real is only ever a nested
sequence of segments, never a point. The repository has a quantitative
form of the remark. Locating an instant by nested cuts spends Newton's
cell action additively ([cut-measure note](cut-measure-newton.md),
Theorem 2), and with a floor $\kappa$ per exhibited cut only $K_\tau/\kappa$ cuts can
be exhibited (Corollary 5): a recorded instant is a segment of length of
order the mark mesh $\tau_*$. Dedekind's point is the completed limit of that
sequence, which is Newton's side in the scholium closing Book I (Euclid X
against least magnitudes); the recorded point is the unfinished one.

**Connes** (user: "Connes more or less exits the dilemma by having
$dx=[D,X]$"). From memory: in a spectral triple the differential of $f$ is
$[D,f]$, infinitesimals are compact operators, the line element is $ds=D^{-1}$,
and distance needs no paths, $d(p,q)=\sup\{|f(p)-f(q)|:\|[D,f]\|\le1\}$. The completed
point is never formed, and the velocity is an operator relation, as in
Heisenberg's $\dot x=(i/\hbar)[H,x]$. Two refinements: in the commutative case
$[D,f]$ commutes with every function, so joint determinacy holds and Newton
is recovered; noncommutativity remains the premise, the fork of Theorem A
of the [fifth-postulate note](principia-fifth-postulate.md). With $p=\hbar D$ the
line element $D^{-1}$ is $\hbar/p$, the de Broglie wavelength operator, so $\hbar$ is
again a conversion constant. The [tangent-groupoid note](tangent-groupoid-trajectories.md)
already holds the gluing of pairs at $\hbar>0$ (the segment) to tangent vectors
at $\hbar=0$ (the point). A candidate Newton test: whether the repeated cutting
of a Galileo cell extends continuously to the $\hbar=0$ fibre.

## Consequence for STATE

None yet. The candidate Newton premise (information loss as in 't Hooft's
equivalence classes) goes to an Astra decision round after round 14.
