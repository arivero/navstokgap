# R22 review: actual global collisions survive interaction

C100–C101 are accepted as written derivations for the fixed pulse design in
[R22](../notes/global-clock-speed-ambiguity.md).

1. Factoring the moment matrix and powers through order three before inversion
   bounds the Taylor tail and its speed derivative by O(epsilon). This gives
   the full limiting B matrix, rather than inferring its entries from a
   determinant. Conversion through the four output derivatives gives (2).
2. Substitution in the physical quadratic energy gives (3). With a=3g,
   d=5g/3, its potential part factors as g(x-y)(9x-5y). At y=7x/5 it is
   -4gx squared/5. The stated positive small momentum preserves this sign;
   y=0 gives the opposite sign. Energy normalization preserves both signs
   and keeps both canonical coordinates positive on the compact path.
3. Fix the design first, speed separation second, coupling third. Uniform
   speed expansion gives opposite endpoint energy mismatches and strictly
   positive x/P separations. The intermediate value theorem then supplies
   an actual equal-energy pair, not just a vanishing derivative.
4. The exact eight-record equation at the second speed has the same invertible
   zero-coupling derivative on the whole path. A common contraction tube gives
   continuous solutions with O(lambda) deviations. Endpoint signs persist
   because speed separation is fixed. Another intermediate-value argument
   restores the exact interacting shell constraint, while canonical separation
   and positive apparatus margins persist.
5. Half the common-record coordinate separation bounds each deterministic
   estimator's worst error. Constants c_x,c_P have units time and mass,
   respectively, yielding action units in (8). No area statement follows.

The full-shell prior is essential: the pairs need not lie inside R21's local
invertibility patch. Constants depend on design, energy and preparation.
Shrinking speed uncertainty closes the displayed lower bound. Known offset,
observation time and incoming zero momenta are retained. All clock reaction
and pointer motion are present in the exact continuation.

[B53](../references/batches/B53.md) records the bounded literature audit and
coordinator metadata/definition corrections. No numerical/symbolic verification
scripts were created or run.
