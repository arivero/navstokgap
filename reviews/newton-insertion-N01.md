# N01 double-check: Galileo area, quantum comparison and research drift

2026-09-14. Written coordinator review; exploratory construction, no independent
review or new ledger promotion. No numerical/symbolic verification scripts.

## Findings that change the research direction

- STATE had explicitly substituted "Newton's swept areas" and C052 orbital
  angular momentum for the user's polygon/trajectory difference. This is an
  observable substitution, not a harmless name. It also mixed Newtonian area
  rate with relativistic canonical momentum. That branch is removed from the
  active priority; C052/C130 themselves are unchanged.
- README still selected Q01/G03 from 2026-09-12. It now routes to the clarified
  Galileo target and STATE. The contradictory publication-priority sentence
  in STATE is removed, and selected research is listed first.
- The user's further clarification identifies the inertial horizontal line
  and falling parabola specifically. The matched-endpoint chord lens is half
  that area. The initial N01 sector treatment and its subsequent circular
  countertest emphasis were withdrawn before committing; neither is a next task.
- Restart guidance in AGENTS, STRATEGY, the principia-action skill, the source
  card, the two research targets, PROGRAMME and I002 now carries the same anchor.
  Correct historical uses of Kepler's area law in source notes are preserved.

## Mathematical checks

1. Integrating $y=Ft^2/(2m)$ against $dx=vdt$ gives
   $A=vF\tau^3/(6m)$. Vertical kinetic gain is $F^2\tau^2/(2m)$, hence
   $(3F/v)A=\tau\Delta E$. C001's matched-endpoint chord action is
   $\tau\Delta E/12=FA/(4v)$. The geometric and action units agree only
   after the conversion factor is included. Total mechanical energy is
   conserved during unassisted free fall.
2. The force sequence $(+F,-F,+F)$ with durations $(\tau,2\tau,\tau)$
   has zero total impulse and first time moment. Its momentum is respectively
   $Ft$, $F(2\tau-t)$ and $F(t-4\tau)$. Integrating these three affine pieces
   gives zero final displacement. Their square integrals are respectively
   $F^2\tau^3/3$, $2F^2\tau^3/3$ and $F^2\tau^3/3$.
3. The corresponding height integrals are $F\tau^3/(6m)$,
   $5F\tau^3/(3m)$ and $F\tau^3/(6m)$, totaling $2F\tau^3/m$.
   Thus the complete loop area is twelve times the first falling area.
4. With the force potential $-f(t)y$ included, integration by parts gives
   $\Delta S=-\int P^2/(2m)=-2F^2\tau^3/(3m)$. The negative sign is
   required. Comparing the loop with the off-shell chord would give a
   different coefficient, so their protocols remain separate.
5. In the free interaction picture, $[y+tp/m,y+sp/m]=i\hbar(s-t)/m$.
   Multiplying by $if(t)/\hbar$ gives the displayed scalar generator
   commutator. Higher nested commutators vanish. The vanishing impulse and
   first moment remove the first integrated generator. The second is
   $-i\int P^2/(2m\hbar)$, so the relative propagator is a scalar phase.
   The identity holds for an arbitrary common motional wavepacket, with
   canonical quantum kinematics and prescribed classical control fields.
6. C006 applies to comparing the balanced arm-label phase state with its
   zero-phase counterpart, not to arbitrary force sensing. Substituting
   $|\Delta S|=2F^2\tau^3/(3m)$ gives the stated cube-root time bound and
   $A\ge vd/(4F)$. The first-lobe and finite-copy/accuracy restrictions are
   retained. C007 closes this threshold for unbounded copies at imperfect
   target accuracy; perfect discrimination has its stated separate endpoint.

## Source and acceptance map

C001/C027 and the retained Principia companions support the geometric factors
and chord action. C006--C007/B05 and the Watrous companion support the existing
binary discrimination formula; their accepted proofs are reused. The closed
force sequence and its phase are exploratory written derivations. A bounded
librarian comparison is required before promoting them as ledger claims.

One existing primary URL was reopened: Feynman Lectures II.19, quantum discussion
after Fig. 19--11, on 2026-09-14. It states the action phase $e^{iS/\hbar}$ and
addition of neighbouring-path amplitudes, including action differences within
$\hbar$. This supports the distinction between quantum resolution and a
smallest allowed classical action difference. No discovery query or additional
literature campaign was run. The Feynman companion records this rereading.

Outcome: N01 supplies a conditional quantum benchmark in the user's Galileo
construction. The user's final clarification requires mathematical necessity,
so this supplied-hbar result is supporting, not the intended innovation.
N02 now tests a proposed non-quantum consistency principle for the joint
refinement limit. No necessity theorem has been proved.
