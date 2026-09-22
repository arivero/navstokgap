# State

Updated 2026-09-22. Read this page and the note it points to; AGENTS.md
governs. The previous long version, with the full $SU(3)$ queue and the
source-by-source classics log, is in git at commit 6bc52cb.

## Goal

User direction, 2026-09-17: **establish the Planck gap with Newton-age
arguments and their modern equivalents**, in one paper valid for
foundations of physics and for history and philosophy of science. The
comparison is Galileo's inertial line against the falling parabola, whose
area Newton takes to zero in Lemmas X and XI. User direction, 2026-09-22:
put the effort on the modern leg; the classics serve mostly as
inspiration, and the formal and textual work on the *Principia* lives in
the sibling repository `newtonlean`. Constructive steps take precedence
over no-go results.

## In hand

[The paper draft](../notes/planck-gap-paper.md) is the synthesis; the
proofs are in four notes.

- **Classical floor.** Every protocol of marks with uncorrelated error
  and recoil and $\delta_j\Delta_j\ge\kappa$ needs
  $\tau\Delta E\ge9z_{1-\epsilon}^2\kappa$
  ([mark-cost note](../notes/mark-cost-and-statistical-floor.md),
  Theorem B; worst-case form in the
  [derivation note](../notes/planck-gap-derivation.md)).
- **Mark cost.** A momentum-transfer mark has conjugate error and recoil,
  so $\kappa\ge\hbar/2$ (Theorem A). A correlation $\rho$ between them
  multiplies the floor by $\sqrt{(1-\rho)/(1+\rho)}$ (Theorem C), and
  three marks attain that dependence (Proposition D).
- **Unmarked preparations.** At aperture $(L,P)$,
  $F\tau L+\frac{F\tau^2}{2m}P\ge(1-2\epsilon)\hbar$ for every adaptive
  protocol ([probabilistic note](../notes/planck-gap-probabilistic.md),
  Theorem 2): impulse against position aperture plus sagitta against
  momentum aperture. The floor is $(1-2\epsilon)^2\hbar^2/(4LP)$ at the
  balanced aperture $L=\tau P/2m$.
- **The junction.** M3 is Robertson's inequality for Newton's corpuscle,
  with the interval of fits as one factor
  ([mark-floor note](../notes/newton-mark-floor.md)), plus the clause
  that the undetermined impulse is unrelated to the mark's error.
- **Classics.** Paper §7 and the [arrow-and-sling note](../notes/arrow-not-sling.md);
  companions in `docs/classics/`.

**Correction, 2026-09-22.** Both quantum floors needed a bound on the
shape of an uncertainty ellipse, since each falls to zero under squeezing
at fixed area. An exported ChatGPT review found the aperture case; the
correlated-mark case was found here. Both are restated as theorems with
the shape parameter explicit.

## Next, modern leg first

1. **The quantum Corollary VI phase.** Under a constant force,
   $\psi_F(x,t)=\psi_0(x-Ft^2/2m,t)\,e^{i(Ftx-F^2t^3/6m)/\hbar}$, so
   Newton's Corollary VI holds up to a boost and the state-independent
   phase $\Phi=F^2\tau^3/(6m\hbar)=\tau\Delta E/(3\hbar)=(F/v)A/\hbar$,
   with $A$ the inertial--parabola area. The same $\Phi$ is the Weyl
   holonomy between forward and reversed orderings of the impulse
   polygon. It is the candidate quantity that squeezing cannot move.
   Deliverable: a note with the derivation, the floor it gives in its
   protocol class, and prior art (Greenberger and Overhauser 1979).
2. **General force law.** Theorem 2's proof pairs $\int_0^\tau P''T$ with
   a Dirichlet energy, so it bounds a norm of $P''$; the aperture form
   becomes the total variations of the displacement path.
3. **Mixed conditional states** in the probabilistic Theorem 2, by the
   Bures metric in place of rank-one Kraus operators.
4. **Theorem A beyond the momentum-transfer class.**
5. **Paper revision** after item 1.

History, lower priority: the Section I Scholium, where Newton cites
Euclid X against least magnitudes, as the first entry of the Book I
scholion; §9's reading and edition obligations.

## Paused

$SU(3)$ mass gap: [the position note](../notes/mass-gap-position.md) and
[the conditional theorem](../notes/mass-gap-conditional-theorem.md) hold
the map; a proof consists of hypotheses H1 and H2 there.

## Constraints

No numerical or symbolic verification scripts. Build one note at a time
with `make paper NOTE=<slug>`. No multi-agent workflows. Commit and push
after each result.
