# The premise question without quantum kinematics: a sieve, a trilemma, and two new classical floors

**Abstract.** The open problem — a positive, mass-independent action cost
of records from premises that do not assume $[\hat q,\hat p]=i\hbar$ —
splits into three slots that previous notes left fused. The **unit slot**
(selecting a constant with action units) is closed without kinematics:
charge quantization makes $\kappa_0=k_e e^2/c=\alpha\hbar$ the unique
candidate, by Theorem A of the dimensional-selection note. The
**trade-off slot** (M3, that the delivered impulse be *undetermined*) is
shown here to admit no classical premise at all: under deterministic
composition, continuous phase space and unbounded readout precision
there is a protocol with vanishing disturbance at every error rate
(the trilemma, §3), so the missing premise must deny continuity
(capacity), determinism (indeterminacy), or free events
(thermodynamics) — and the first carries $\hbar$ by another name, the
third is temperature-relative, leaving indeterminacy as the only horn
neither smuggled nor non-universal. The **auxiliary slot** (bounded
laboratory, §10 of the paper) converts any positive unit into a
protocol floor but supplies none. Two new positive results are added.
First, a **sieve corollary**: no duration constant can serve as the
unit, since the induced floor $F^2\tau_0^3/2m$ is $\propto m^{-1}$ and
ranged over admitted masses has infimum zero — the dimensional ground
for the note that denies the kalām time-atom. Second, a **Larmor
persistence bound**: a register whose distinguishable mark is carried by
a radiating bounded configuration of charges must, after persistence
time $t_p$, carry canonical action at least

$$\kappa_{\rm reg}(t_p)=\frac{k_e e^2}{c}\Bigl(\frac{t_p}{t_0}\Bigr)^{1/6},
\qquad t_0=\frac{k_e e^2}{4m_ec^3}\approx 2.4\times10^{-24}\ \mathrm{s},$$

which crosses $\hbar$ at $t_p=t_0\alpha^{-6}\approx1.6\times10^{-11}$ s:
a purely classical, $\hbar$-free floor on the *storage* of records,
mass-independent in the observed body and fixed at the lightest charge
carrier. Candidate premises are then priced against the programme's own
countertests (C002, C052–C053, C058, C068–C069, Q02, Q08, Q10), each in
the requested (a)–(e) form, with $\hbar$-smuggling flagged explicitly,
and ranked: the trilemma first, the Larmor bound and the unit stack
second, extensivity third, Landauer fourth, the fits horn last because
the paper has already closed it historically.

Draft, 2026-09-26, written for the user's premise question against
[the Planck paper](planck-gap-paper.md) §§5, 8, 10, the
[dimen­sional-selection](action-unit-dimensional-selection.md) Theorems
A–B, [the mark-floor note](newton-mark-floor.md) M1–M3 and
[the thermal note](thermal-receiver-reliability.md). Exploratory; no
ledger promotion. All arithmetic is hand-checked; sources not held in
the repository are cited at metadata level and labelled.

## 1. Three slots, not one

The paper's §8 identifies the junction premise as M3 (mark trade-off,
$\delta\Delta\ge\kappa>0$) and the dimensional-selection note reduces
the value question to a product of fixed constants with action units
(Theorem A) guarded against admitted similarities (Theorem B). Read
together, a complete no-kinematics derivation must supply three
independent things.

1. **Unit.** A constant $\kappa$ with action units, fixed by the model's
   constants alone, not removable by an admitted similarity.
2. **Trade-off.** The clause that $\kappa$ binds *every* mark: the
   resolution a mark buys is paid in undetermined impulse (or
   undetermined displacement). This is the content M3 carries and what
   Theorems 4–6 consume.
3. **Auxiliary.** Whatever converts a per-mark floor into a protocol
   floor over the whole comparison — the paper's §10 shows this is
   either marking the trajectory or bounding the laboratory's extent
   and momentum capacity.

The three slots have different states of health. The unit slot is
closed (§2). The auxiliary slot is priced, not derived (§10 of the
paper). The trade-off slot is the open problem, and §3 shows it is
sharper than "find a premise": under classical composition no premise
inside classical mechanics works, and the candidates divide into three
horns with unequal costs.

## 2. The sieve: which constants can hold the unit

The dimensional-selection note proves that with fixed constants
$k_e=e^2/4\pi\epsilon_0$, $c$, $G$ the unique product with action units
is $k_e/c=\alpha\hbar$, that admitting a mass $m$ adds the
mass-dependent $Gm^2/c$, and that without $k_e$ there is none. Two
additions here.

**Corollary (no duration constant).** A model holding fixed only a
duration $\tau_0$ (with $m$, $F$) has unique action product
$F^2\tau_0^3/m$ (Theorem A(ii)). The induced per-cell floor,
$\tau_0\Delta E=F^2\tau_0^3/2m$, is proportional to $m^{-1}$: ranged
over admitted masses its infimum is zero, so a temporal atom floors the
light bodies and none of the heavy ones. This is the dimensional ground
for the paper's §9 verdict on the kalām time-atom ("a dynamical
resolution rather than a universal atom of time") and for the
observation that the mesh $\tau_*$ of Corollary 3 moves with $m$. It
also answers one of the user's candidate premises directly:
*consistency of record composition under refinement* composes
$\kappa=0$ exactly — the refinement note's summable-defect theorem and
the series/parallel factorisation are that statement — so consistency
of refinement is the wrong horn; refinement never *generates* a unit.

**Distinction: adversarially variable versus constitutionally fixed
constants.** Theorem B kills floors carried by a supplied coefficient
that an admitted preparation can vary: bath temperature $T$ (cool the
memory), pulse amplitude $K$ (attenuate, Q08), potential softness $a$
(C053), receiver impedance (Q08's rescaling family). Constants fixed by
the constitution of matter — $e$, $m_e$, $c$ — are not variable by any
admitted preparation: no protocol thins the electron. The universality
obligation should therefore be stated as infimum over admitted
*preparations*, with model constants split into the two classes; the
floors of §5 survive only through the constitutionally fixed class.

## 3. The trilemma for the trade-off

**Theorem T (no classical trade-off).** Let a record model satisfy
(R1) probes and apparatus are Hamiltonian systems on a continuous phase
space with deterministic composition (the setting of the refinement and
autonomous-readout notes); (R2) no premise bounds how many states of
the apparatus are distinguishable within any bounded phase-space
region; (R3) marks are physical interactions and readouts are marks.
Then for every $\epsilon\in(0,1)$ there is a protocol deciding the
comparison at error $\epsilon$ with
$\frac s8\sum_j\Delta(\hat D_j)+\frac J2\sum_j\Delta(\hat X_j)=0$.

*Proof.* The marks are impulsive couplings with definite transferred
impulse: each $\iota_j$ is a function of the probe's initial data and
its pointer reading. Since composition is deterministic (R1) and
readout can be refined at bounded cost through a continuous phase space
(R2) — exactly the capacity of the fixed finite-mass apparatus
constructed in C068–C069, which reconstructs a receiver state with
vanishing error and disturbance over fixed observation time — the
protocol may contain, after each mark, later marks measuring the probe
and recovering $\iota_j$ to arbitrary precision; the §8 countermodel
(the corpuscle read on a screen at distance $D$, recoil recovered to
$p(\delta+\delta_s)/D$) is the one-probe case. The invariant statistic
subtracts the recovered recoil, so the disturbance spreads that Theorem
6 bounds vanish while the decision error stays $\epsilon$. $\square$

**Corollary (the trilemma).** Any premise implying a positive trade-off
for all protocols denies R1, R2, or R3. The three denials are exactly:

- **Capacity** (deny R2): a bounded number of distinguishable states
  per bounded region of phase space. On a continuous phase space this
  forces a minimal cell; the cell's Liouville area is an action; fixing
  it fixes $\hbar$. Operationally this is Hardy's continuous reversible
  connection of pure states, which the
  [quantum-exclusion audit](quantum-exclusion-premises.md) already maps
  against the classical simplex: capacity plus continuity *is* the
  quantum premise. This horn smuggles $\hbar$.
- **Indeterminacy** (deny R1): composition of a mark leaves its impulse
  undetermined as a matter of law. This is M3 read as a primitive. It
  carries no $\hbar$ and no temperature; it is the horn the paper's §8
  shows Newton's *Opticks* Book II Part III Prop. XII excludes, since a
  determinate periodic disposition carried by a corpuscle moving by
  ordinary mechanics lets later records recover the delivered impulse.
- **Irreversibility** (deny R3 as free): writes are thermodynamic
  events with cost $k_BT\ln 2$ (Szilard 1929; Landauer 1961; both
  classical-statistical justifications). The resulting floors are real
  but temperature-relative (§6, C4): an admitted preparation cools the
  memory, so universality fails.

The trilemma is the precise sense in which "consistency of record
composition" cannot be the answer: under composition the zero floor is
consistent, and the question is which *inconsistency* with classical
composition to adopt. It also prices the modern reconstruction routes:
finite-outcome premises, finite-information premises and
information-causality packages all land on the capacity horn.

## 4. C1: Charge quantization (the unit, not the trade-off)

**(a) Statement.** There is a smallest free charge $e$; all free
charges are integer multiples of it.

**(b) Justification.** Faraday's electrolytic laws (1834): the mass
deposited per unit charge is proportional to atomic weight over valence
across all substances, which Helmholtz's 1881 Faraday lecture read as
atomicity of electricity; Millikan (1909–13) measured the discreteness
on free drops. All classical, bench-level, pre-quantum. (Metadata
level; sources not held.)

**(c) What it forces.** With $c$ it fixes the unique mass-independent
action unit $\kappa_0=k_e e^2/c=\alpha\hbar$ (dimensional-selection
note §5). For marks it forces a *magnitude* floor: an electromagnetic
probe of charge $q\ge e$ that fixes transverse position to $s$ within
the cell must deliver impulse of magnitude at least
$\Delta p\ge 2k_e e^2/cs$ (the transverse impulse of an
ultra-relativistic flyby at impact parameter $b\le s$ is
$2k_ee' /bc\ge 2k_ee^2/cs$), so $s\,\Delta p\ge 2\alpha\hbar$ — about
$4\alpha\approx 0.029$ of the Robertson floor. The floor is universal
in the observed body's mass. The factor $1/\alpha\approx137$ between
this magnitude floor and the quantum spread floor is exactly the
content of the missing horn: charge quantization fixes *what is
transferred*, the horn fixes *whether its value is hidden*.

**(d) Loopholes.** Softening (C053): excluded only if registers are
self-bound — closed by the extensivity premise of C3. Compensation: not
closed at all — the flyby impulse is a known function of the recorded
impact parameter, so the spread stays zero and the §8 countermodel
stands; the trilemma says no charge premise closes this. Neutral
bodies: a polarizability floor is apparatus-relative (sieve, §2), and a
gravitational channel gives $Gm^2/c$, mass-dependent — so universality
across channels independently forces the electromagnetic one, which is
the sieve's only survivor.

**(e) Smallest theorem.** "Assume (i) charges $\ge e$, (ii) signals
$\le c$, (iii) the mark is an electromagnetic scattering off the body's
constituents; then any record of the sagitta at resolution $s$ transfers
impulse of magnitude $\ge 2k_ee^2/cs$, undetermined part zero unless a
horn of §3 is added." The magnitude clause is provable now (standard
relativistic impulse; Jackson §19 at metadata level for the formula).

## 5. C2: The Larmor persistence bound on registers (new)

Registers, unlike marks, must *persist*: the record of cell $j$ has to
outlive the cell until the comparison is read. Under the same two
premises as C1 plus Earnshaw's theorem (no static equilibrium of
charges in any electrostatic field — classical, 1842), every
constituent of a register executes bounded motion, and a *visible*
mark — one carried by a time-dependent multipole — radiates.

**(a) Statement.** Assume (i) constituent charges $\ge e$; (ii) no
static supports (Earnshaw + all constraints are dynamical matter); (iii)
the mark is carried by a bounded charge configuration with a radiating
multipole and must persist for $t_p$. Then the register's canonical
action obeys $J\ge\kappa_{\rm reg}(t_p)$ as in the abstract, minimised
over carriers at the lightest, $m_e$.

**(b) Justification of the premises.** (i) is C1. (ii) is Earnshaw
(theorem) plus the compositionality premise that every support is
itself matter — the bench form of which is C3. (iii) is the record
persistence requirement, which the protocol's own reading times force.

**(c) Derivation (written, constants explicit).** Circular Coulomb
orbit: $v^2=k_ee^2/mr$; total energy $E=-k_ee^2/2r$; action
$J=mvr=\sqrt{mk_ee^2r}$. Larmor power, $P=\tfrac23 k_ee^2a^2/c^3$ with
$a=k_ee^2/mr^2$, gives $P=\tfrac23(k_ee^2)^3/(c^3m^2r^4)$. Then
$|dE/dr|=k_ee^2/2r^2$ and
$\dot r=-(4/3)(k_ee^2)^2/(c^3m^2r^2)$, so the spiral-in time from $r$
is $t(r)=c^3m^2r^3/4(k_ee^2)^2$. Persistence for $t_p$ forces
$r\ge(4(k_ee^2)^2t_p/c^3m^2)^{1/3}$, whence
$J\ge(4t_p/c^3)^{1/6}(k_ee^2)^{5/6}m^{1/6}
=\frac{k_ee^2}{c}\Bigl(\frac{4t_pmc^3}{k_ee^2}\Bigr)^{1/6}$. The
subluminal floor of C052, $J\ge k_ee^2/c$ (at $r=k_ee^2/mc^2$, the
classical particle radius), is dominated for every
$t_p>t_0=k_ee^2/4mc^3$. For electrons $t_0\approx2.4\times10^{-24}$ s
and the bound crosses $\hbar$ at $t_p=t_0\alpha^{-6}\approx
2.4\times10^{-24}\times6.6\times10^{12}\approx1.6\times10^{-11}$ s; at
$t_p=1$ ns it is $\approx2\hbar$. Since $J\propto m^{1/6}$ at fixed
$t_p$, the minimum over media sits at the lightest carrier, so the
floor is mass-independent in the observed body and fixed by $e$, $c$,
$m_e$ — all constitutionally fixed in the sense of §2. It explains why
no register made of ordinary matter can be a "quiet" holder of marks,
without $\hbar$ anywhere.

**(d) Loopholes.** *Supports:* excluded by (ii); the C053 softened core
is precisely a static support. *Squeezing:* inapplicable — the bound is
on the register's own action for any state that holds the mark.
*Non-radiating configurations:* a rigid uniformly charged shell spins
with static fields, radiating nothing, and its magnetic moment is
continuously readable — but its rigidity is a support (violating (ii))
and a perfectly symmetric shell carries no distinguishable mark. The
open core is a **visible-mark conjecture** (labelled as conjecture): a
distinguishable mark carried by a bounded configuration of charges
under (i)–(ii) necessarily has a radiating multipole; Goedecke's 1964
classically radiationless motions are the countermodel family to test
it against. Collective continuous variables (the magnetic moment of a
composite) sit in the Q08 family, which this programme already prices
as preparation-relative.

**(e) Smallest theorem.** "Assume (i)–(iii) of (a); then any register
that holds a record of the sagitta for time $t_p$ carries canonical
action $\ge(k_ee^2/c)(t_p/t_0)^{1/6}$, and a readout mark at resolution
$s$ delivers impulse of magnitude $\ge k_ee^2/O(s)$ — magnitude, not
spread; the spread remains zero until a §3 horn is added."

**Status.** The derivation is classical and self-contained; what is new
against C052 is the persistence exponent $1/6$ and the crossing of
$\hbar$ at 16 ps. The bound constrains *storage*, not the mark
trade-off; its role in the programme is to close the storage half of
the classical countermodel family (the registers of C068–C069 are
recoil-free oscillators, which (ii) excludes as supports) and to give
§7 of the paper a second, independent route to a physical $\Lambda$-like
scale.

## 6. C3: Extensivity of bulk matter (the bench premise)

**(a) Statement.** There exist bulk media in which $N$ constituents
bind with total energy $-NE_b+o(N)$ and size scaling as the cube root
of $N$, with $E_b$ and a constitutive length $a_0$ independent of $N$
and of preparation history; every register medium is such a medium.

**(b) Justification.** Chemistry and metallurgy: heats of formation,
lattice constants, the additivity of volumes and cohesive energies.
This is bench-level and was available classically. Flag: Dyson–Lenard
(1967) and Lieb–Thirring (1975) prove extensivity *from* quantum
premises, so taking the phenomenon as primitive is $\hbar$ through the
bench door — legitimate only conditionally ("given stable matter, what
follows for records?"), and marked as partial smuggling here.

**(c) What it forces.** With Coulomb and the electron mass, extensivity
fixes the action unit exactly: for hydrogenic scales
$E_b=Ry=m_e(k_ee^2)^2/2\hbar^2$ and $a_0=\hbar^2/m_ek_ee^2$, so

$$\hbar=a_0\sqrt{2m_eE_b},$$

an identity: the atomic radius and binding energy — measurable by
crystallography and thermochemistry without quantum theory — determine
$\hbar$'s value with no kinematics input. Below the constitutive scale
the premise has a second consequence: excitations that persist in the
bulk are separated by an $E_b$-scale gap (the premise's own
phenomenology: Dulong–Petit-type plateaux end at low temperature), so
sub-$a_0$ records must excite $E_b$-scale quanta to persist.

**(d) Loopholes.** Softening: closed for material supports (a softened
core is a medium violating extensivity at that scale). Squeezing: the
floor attaches to the medium, not the body's preparation. Collective
continuous variables: the Q08 loophole again, preparation-relative.

**(e) Smallest theorem.** "Assume extensivity at $(a_0,E_b)$; then any
record of the sagitta at resolution $s<a_0$ excites at least
$E_b$-scale energy in the medium, i.e. $\tau\Delta E\gtrsim E_b$
independent of the body's mass, with the medium's $(a_0,E_b)$ —
constitutionally fixed but medium-relative."

## 7. C4: Landauer plus persistence (the thermodynamic horn)

**(a) Statement.** Erasing a bit in a bath at $T$ dumps $\ge k_BT\ln2$
to the bath (Szilard 1929; Landauer 1961; classical-statistical
justification: the second law plus Gibbs counting); a mark that must
survive false activation for $t_p$ at attempt rate $\nu$ carries gap
$\ge k_BT\ln(\nu t_p/\epsilon)$ — which is exactly eq. (7) of the
thermal-receiver note.

**(b) Justification.** The Kelvin–Planck statement of the second law;
the Szilard engine accounting. No $\hbar$ anywhere — the premise is
genuinely classical.

**(c) What it forces.** The floor
$\kappa_T(s)=k_BT\,(s/c)\,\ln(\nu t_p/\epsilon)$: mass-independent,
resolution-dependent, and *temperature-relative*. Under §2's
distinction, $T$ is adversarially variable (a preparation cools the
memory), so Theorem B's criterion bites: the floor is real but
reference-relative, the C036 pattern. The Nernst postulate prevents
$T=0$ but not $T=1\,\mu\mathrm{K}$ in finite time; a cosmological floor
$T_{\rm CMB}$ is a contingent fact, not a premise.

**(d) Loopholes.** Cooling is the loophole and it succeeds; the honest
verdict is that this horn cannot carry universality, and the
thermal-receiver note already says so ("it does not select a quantum
action").

**(e) Smallest theorem.** "Assume records are written in a medium at
$T$ with attempt rate $\nu\le c/s$ and must hold with error $\epsilon$
for $t_p$; then any record of the sagitta at resolution $s$ is paid by
momentum disturbance of magnitude $\ge(k_BT/c)\ln(\nu t_p/\epsilon)\,
s^{-1}$ — spread still zero (the trilemma's horn is magnitude through
noise, and noise back-action is compensable in the model), so the
decision-theoretic floor needs the preparation-independence clause,
which fails as $T\to0$."

## 8. C5: The fits horn, and the smuggling table

**Fits.** The paper's §§7–8 already extracts the strongest Newton-age
candidate: a measured least interval $\Lambda$, corpuscular impulses,
and $\Lambda p$ invariant under refraction, with the junction premise
being exactly an indeterminacy of the disposition — and already proves
that what Newton printed (Book II Part III Prop. XII, a determinate
transient constitution on a corpuscle of Query 29) entails its negation.
The trilemma adds the structural verdict: the fits horn is the *only*
horn that is neither $\hbar$-smuggling nor temperature-relative, so if
the programme wants a no-kinematics universal floor, the target premise
is an indeterminacy premise, and the Newton-age question becomes a
source question — how determinate the fits were meant to be (Shapiro's
*Fits, Passions, and Paroxysms*, the paper's obligation 1) — rather
than a mechanics question.

**Smuggling table.** Each modern candidate is flagged at the point
$\hbar$ enters.

| Premise | Where $\hbar$ enters | Verdict |
| --- | --- | --- |
| Finite information capacity / bounded states per region | minimal Liouville cell $=h$; equivalent to kinematics (§3, capacity horn) | smuggles |
| Bekenstein bound $S\le2\pi RE/\hbar c$ | $\hbar$ in the bound | smuggles |
| Bremermann, Margolus–Levitin speed limits | $\hbar$ explicit | smuggles |
| Salecker–Wigner clock spread $\delta x^2\ge\hbar t/M$; Peres clock bounds | $\hbar$ in the spread | smuggles |
| Károlyházy; Ng–van Dam foam $\delta l\sim l^{1/3}l_P^{2/3}$ | $l_P=\sqrt{\hbar G/c^3}$ | smuggles |
| Nelson stochastic mechanics | diffusion $\nu=\hbar/2m$ | smuggles |
| Entropic/holographic gravity | $\hbar$, $k_B$ | smuggles |
| Landauer persistence (C4) | none — but $T$-relative | fails universality |
| Charge quantization (C1) | none | unit only |
| Indeterminacy primitive (C5 horn) | none by construction | the remaining horn |
| 't Hooft deterministic underlying theory | $\hbar$ emergent | denies the target; a rival programme, not a premise |

## 9. Ranking, and what to prove first

1. **The trilemma (Theorem T).** Cheapest and decisive: it converts open
   problem 5 from "find a premise" into "choose a horn", kills the whole
   class of consistency-based candidates (refinement consistency,
   composition, capacity smugglings) in one theorem, and its proof is
   assembled from results already in hand (§8's countermodel,
   C068–C069, Theorem 6). Prove it first.
2. **The Larmor persistence bound + the unit stack (C2, C1).** New,
   provable now, $\hbar$-free: the register floor with exponent $1/6$
   and the mark magnitude floor $2k_ee^2/cs$. Together they give the
   paper a classical floor stack to set against the quantum one, with
   the measured factor $1/\alpha$ as the price of the missing horn.
3. **Extensivity (C3).** The bench premise that closes C053 and yields
   the exact identity $\hbar=a_0\sqrt{2m_eE_b}$: the constant without
   the kinematics. Partial-smuggling flag as stated.
4. **Landauer (C4).** Quantitative and honest; already half-present in
   Q10; fails universality, keep as the thermodynamic wing.
5. **Fits (C5).** Conceptually the answer's home; historically closed
   by the paper's §8; reduce to the Shapiro source question.
6. **Capacity family (table of §8).** Disqualified as smuggling; useful
   only as the lens that makes the trilemma's first horn precise.

The smallest theorems to write out in full, in order: Theorem T with
the C068–C069 recovery made explicit; the Larmor bound with the
non-radiating loophole stated as the visible-mark conjecture; the
magnitude-impulse lemma for C1. No new laboratory number is claimed —
at bench scales every one of these floors is swamped by $\hbar$; the
content is structural, and its test is the channel differential: any
record channel with a mass-dependent floor (gravitational) or a
preparation-relative one (thermal, collective-amplitude) is classical
shaped; the quantum floor is the unique channel-independent one, and
$1/\alpha$ measures how far the classical stack falls short of it.

## 10. Consequence for STATE

The premise question of STATE item 2 ("Newton necessity") is here split
into unit (closed by charge quantization, $\kappa_0=k_ee^2/c$),
trade-off (trilemma: capacity, indeterminacy, or irreversibility — no
classical premise exists), and auxiliary (§10 of the paper). Next
steps, in order: (1) write Theorem T out with the C068–C069 recovery
made explicit and check it against the adversarial-review standard of
2026-09-23; (2) write the Larmor persistence bound and the visible-mark
conjecture into the recoil note's classical section; (3) record the
$\hbar=a_0\sqrt{2m_eE_b}$ identity and the adversarially-variable
versus constitutionally-fixed constant distinction in the
dimensional-selection note; (4) the historical residual is Shapiro's
monograph on the determinacy of the fits (paper obligation 1). The
sieve corollary (no duration constant) belongs in §9's kalām bullet as
its dimensional ground. Nothing here is promoted to the ledger.
