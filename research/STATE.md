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
| Every probe state: $s\sum_j\Delta_j\ge8\hbar\arcsin(1-2\epsilon)$, $\ge2h$ at certain decision; grid probes break the Gaussian form | Thm 5 | [recoil](../notes/record-costs-recoil.md) |
| Body-independent noise (Ozawa's independent intervention) forces the von Neumann form | §5 | [additive-noise](../notes/additive-noise-marks.md) |
| Every instrument: $\frac s8\sum\Delta(\hat D_j)+\frac J2\sum\Delta(\hat X_j)\ge\hbar\arcsin(1-2\epsilon)$ | Thm 6 | [disturbance](../notes/record-costs-disturbance.md) |
| Sharp constant $\arcsin(1-2\epsilon)$ in every protocol bound; kick form $\int\lvert f\rvert L\ge\hbar\arcsin(1-2\epsilon)$; one accounting $\int\lvert f\rvert\min(L,R)$ | §§5, 10 | [path-length](../notes/record-distance-path-length.md) |
| Inscribed polygon differs from the parabola by the phase $F^2\sum\tau_j^3/24m\hbar$; insertion law; ordering holonomy | Thm 7 | [polygon-lift](../notes/polygon-lift-phase.md) |
| Every force law: one functional $\mathcal K_\tau$, phase $\mathcal K/\hbar$, sharp deflection $\mathcal K/\kappa$ | Thm 8 | polygon-lift §6 |
| Unmarked preparations: $J L+s P\ge\hbar\arcsin(1-2\epsilon)$, every instrument | §10 | [probabilistic](../notes/planck-gap-probabilistic.md) |
| *Opticks*: measured $\Lambda$, posited $p$, $\Lambda p$ invariant under refraction (II.iii Props. X, XVII); Newton's Prop. XII denies M3 | §§7--8 | [mark-floor](../notes/newton-mark-floor.md), polygon-lift §5 |
| The ladder: arrow, then Galileo; the Section I scholium's Euclid-X objection answered | Thm 9, §9 | paper §9, [arrow and sling](../notes/arrow-not-sling.md) |

The premise that carries $h>0$, in its universal form: a record costs
disturbance. A mark that registers the sagitta leaves the impulse
undetermined, and one that registers the impulse leaves the displacement
undetermined, at the exchange rate $\hbar$.

## Next, modern leg first

1. **Adversarial review, batch 3** (user direction 2026-09-23: Fable as a
   critic). Batches 1 (recoil, additive-noise, disturbance) and 2
   (polygon-lift, path-length) found no false result; their proof gaps,
   conventions and prior-art labels are repaired. Batch 3: the sharp
   constant 48 and Theorem C of the mark-cost note, and the paper's
   overclaims, history and prior art.
2. **Attainment.** Whether the minimum of the one accounting over splits
   and lines is attained, which would make it the exact floor; whether
   the constants $1/8$ and $1/2$ of Theorem 6 are attained.
3. **Submission.** Paper §11: read Shapiro 1993 and the *Principia*
   historiography; cite the 1730 *Opticks* and Cohen--Whitman.

## Paused

$SU(3)$ mass gap: [the position note](../notes/mass-gap-position.md) and
[the conditional theorem](../notes/mass-gap-conditional-theorem.md) hold
the map; a proof consists of hypotheses H1 and H2 there. The
[openings note](../notes/mass-gap-openings.md) (2026-09-23) records four
ways in, parked: curvature (Bakry--Émery; Shen--Zhu--Zhu's threshold
converts to $g^2>32$ for $SU(3)$, to be checked), the centre-stabilized
small circle, three dimensions, and the Planck-gap link through Simon's
valley lifting, the one that may be taken up. It also records that the
gap is expected for every compact simple non-abelian group, and that
T2$'$ is sufficient, with the conjecture needing only a gap on $(0,g_1)$
along the scaling curve.

## Constraints

No numerical or symbolic verification scripts. Build one note at a time
with `make paper NOTE=<slug>`. No multi-agent workflows. Commit and push
after each result.
