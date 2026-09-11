# R18 review: the clock supplies an invertible position response

C092–C093 are accepted as checked derivations for the fixed pulse design in
[R18](../notes/position-preparation-ambiguity.md). The review is written,
with no numerical or symbolic verification scripts.

1. On the nominal-clock, zero-incoming-momentum slice, initial positions stay
   constant at zero coupling. Their receiver and clock responses each start
   at order lambda; multiplication by the record interaction gives the two
   terms in equation (1), both at order lambda squared. Smooth finite-time
   variational equations give the uniform order-three remainder on fixed
   compact preparation margins. Physical matrix units are momentum/length.
2. Disjoint ordered pulses make the leading matrix lower triangular by
   causality. The receiver diagonal is order delta cubed. Integrating the
   clock diagonal by parts gives minus integral phi squared, with coefficient
   K squared times x_j squared delta divided by clock mass and speed squared.
   Its order-delta negative term dominates the order-delta-squared remainder.
3. The receiver history at the selected shell point has positive second
   derivative at zero, hence isolated zeros. Independent evaluation times
   persist under small perturbations avoiding these zeros. Narrow fixed
   pulses preserve signal rank and make every response diagonal nonzero.
   Delta is selected once; all later smallness constants may depend on it.
4. Multiplying the position derivative by the inverse leading matrix gives
   a contraction with norm at most one half. The nominal receiver mismatch
   is order lambda times displacement, so the scaled initial residual is
   bounded by C times displacement divided by lambda. Radius lambda b/(4C)
   gives self-mapping on the position ball b/2 and an exact common record.
5. R17's exact shell chart preserves energy and supplies a whole canonical
   square, not merely a tangent direction. Opposite square endpoints give
   each estimator's worst-case coordinate bound; multiplying these risks
   does not require both worst cases to occur at the same state.

The records are four initial and four final probe momenta. The constructed
slice fixes initial clock data without adding them to the observation set.
The assertion is existence of an admissible pulse design, not rank for every
R06 design. At fixed preparation width the displayed lower bound closes with
coupling; that statement alone supplies no upper risk estimate.

[B49](../references/batches/B49.md) is a bounded local-observability audit.
Coordinator scan review corrects pagination and verifies the theorem/proof.
Its standard rank context neither supplies the apparatus matrix nor establishes
global injectivity. Novelty is unassessed. R19 should prove a uniform finite
record-map estimate after revealing both final pointer coordinates.
