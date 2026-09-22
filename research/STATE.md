# State

Updated 2026-09-23. Read this page and the note it points to; AGENTS.md
governs. The long version with the full $SU(3)$ queue and the
source-by-source classics log is in git at commit 6bc52cb.

## Goal

User direction, 2026-09-17: **establish the Planck gap with Newton-age
arguments and their modern equivalents**, in one paper valid for
foundations of physics and for history and philosophy of science. The
comparison is Galileo's inertial line against the falling parabola, whose
area Newton takes to zero in Lemmas X and XI. User direction, 2026-09-22:
put the effort on the modern leg; the classics serve mostly as
inspiration, and the formal and textual work on the *Principia* lives in
the sibling repository `newtonlean`. Constructive steps take precedence
over no-go results. Context: since 2026-09-21 an advisory group hosted at
the IAS advises on releasing machine results
([news digest](../docs/AI_Mathematics_News_2026.md)); the aim here is a
presentable result first, on the Planck gap or the mass gap.

## In hand

[The paper draft](../notes/planck-gap-paper.md), revised 2026-09-23 into
twelve sections with Theorems 2--9 in order, is the synthesis. Its
results and the notes that prove them:

| Result | Paper | Proof |
| --- | --- | --- |
| Newton's limit has no geometric floor | Prop. 1 | paper §2 |
| Gaussian marks: $\tau\Delta E\ge48z^2\kappa$, sharp | Thm 2 | [mark-cost](../notes/mark-cost-and-statistical-floor.md), Thm B |
| Mark cost $\kappa\ge\hbar/2$ (error and recoil conjugate); $24z^2\hbar$ for uncorrelated Gaussian probes; correlation $\rho$ lowers it by $\sqrt{(1-\rho)/(1+\rho)}$ | Thm 4, eqs. (2)--(3) | mark-cost, Thms A, C, Prop. D |
| Every probe state: $s\sum_j\Delta_j\ge8(1-2\epsilon)\hbar$; grid probes break the Gaussian form | Thm 5 | [recoil](../notes/record-costs-recoil.md) |
| Body-independent noise forces the von Neumann form | §5 | [additive-noise](../notes/additive-noise-marks.md) |
| Every instrument: $\frac s8\sum\Delta(\hat D_j)+\frac J2\sum\Delta(\hat X_j)\ge(1-2\epsilon)\hbar$ | Thm 6 | [disturbance](../notes/record-costs-disturbance.md) |
| Inscribed polygon differs from the parabola by the phase $F^2\sum\tau_j^3/24m\hbar$; insertion law; ordering holonomy | Thm 7 | [polygon-lift](../notes/polygon-lift-phase.md) |
| Every force law: one functional $\mathcal K_\tau$, phase $\mathcal K/\hbar$, sharp deflection $\mathcal K/\kappa$ | Thm 8 | polygon-lift §6 |
| Unmarked preparations: $J L+s P\ge(1-2\epsilon)\hbar$, every instrument | §10 | [probabilistic](../notes/planck-gap-probabilistic.md) |
| *Opticks*: measured $\Lambda$, posited $p$, $\Lambda p$ invariant under refraction (II.iii Props. X, XVII); Newton's Prop. XII denies M3 | §§7--8 | [mark-floor](../notes/newton-mark-floor.md), polygon-lift §5 |
| The ladder: arrow, then Galileo; the Section I scholium's Euclid-X objection answered | Thm 9, §9 | paper §9, [arrow and sling](../notes/arrow-not-sling.md) |

The premise that carries $h>0$, in its universal form: a record costs
disturbance. A mark that registers the sagitta leaves the impulse
undetermined, and one that registers the impulse leaves the displacement
undetermined, at the exchange rate $\hbar$.

## Next, modern leg first

1. **One accounting.** The aperture bound pays at the body between marks,
   Theorem 6 pays at the marks. State the mixed accounting as one
   optimization and find its minimum; decide whether the constants
   $1/8$ and $1/2$ of Theorem 6 are attained.
2. **Remaining constants.** The worst-case interval $[9,36]$ in
   $F^2\tau_*^3/(m\kappa)$, and $\arccos(2\sqrt{\epsilon(1-\epsilon)})$
   against $1-2\epsilon$ in the aperture bound.
3. **Submission.** Paper §11: read Shapiro 1993 and the *Principia*
   historiography; cite the 1730 *Opticks* and Cohen--Whitman.

## Paused

$SU(3)$ mass gap: [the position note](../notes/mass-gap-position.md) and
[the conditional theorem](../notes/mass-gap-conditional-theorem.md) hold
the map; a proof consists of hypotheses H1 and H2 there.

## Constraints

No numerical or symbolic verification scripts. Build one note at a time
with `make paper NOTE=<slug>`. No multi-agent workflows. Commit and push
after each result.
