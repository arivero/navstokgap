# R31 review: tolerance/coupling bounds and exact saturation

C118–C119 are accepted as checked derivations in
[R31](../notes/calibration-tolerance-recovery.md).

1. R30's receiver inverse margin holds throughout its chart before exact
   C constraints are imposed. Comparing actual C_1,C_2 adds precisely
   ||C_1-C_2||/lambda. The record term retains both DC(a)/lambda and D_aD.
2. The compact feasible-set estimator compares two preparations each within
   epsilon and delta of the same reported data. Their differences are at
   most 2epsilon and 2delta, giving (2). A fixed deterministic selector exists
   by successive coordinate minimization on a compact nonempty set.
3. The nominal receiver zero belongs to the admitted energy ball. R25's
   exact compensator applies on all Z with O(lambda||w||) displacement,
   even though the nonzero probe displacement drives its subsequent motion.
   The reference record is the exact coupled record, not the free record.
   The resumed coordinator made this quantitative: the chart derivative is
   -(D_eta F)^{-1}D_w F, bounded by 2L lambda. Integrating from receiver zero
   gives (3) with B=2L. Risks are explicitly defined over states and all
   admissible reports; the joint estimator attains the two upper bounds.
4. A fixed coupling ceiling places the full compensator inside half of R30's
   unchanged preparation box. Lipschitz control of C makes the dilated ball
   tZ compatible with the same reported C_* and exact full record. All four
   calibration tolerances are positive; exact subconstraints are left to R32.
5. The canonical ellipse has extrema +/-X_E, +/-P_E. Common-record endpoints
   give (5) for every estimator. With exact records, feasible estimates and
   coordinatewise zero estimates give matching small-tolerance orders. Their
   coordinate outputs can be realized in the ellipse because setting either
   canonical coordinate to zero preserves that constraint.
6. At t=1 the zero estimator attains both coordinate lower bounds globally;
   hence their product is also exactly optimal. The sufficient saturation
   threshold is not asserted sharp. The comparison is at fixed apparatus,
   c, preparation width and energy bound; no universal action is selected.

The projection-area statement concerns the entire common-record ball at
saturation. Report-error supports are deterministic and may correlate through
the compensator; no independent probability law is assumed. No numerical or
symbolic verification scripts ran. [B62](../references/batches/B62.md)
records source coverage and the corrected mathematical passage anchors.
