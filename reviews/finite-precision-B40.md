# R09/B40: proof and source review

C074–C075 are accepted as written consequences of the fixed bounded-force
information model, 2026-09-10. Novelty remains unassessed after the bounded
[B40 audit](../references/batches/B40.md).

## Written checks

1. Clipping the record to the reachable position range preserves exactly the
   allowed states. Empty intersections are rejected. R08's momentum fibres
   are increasing at both endpoints, including continuous endpoint limits.
2. The shear has determinant one. Its future-force direction is $(-s/m,1)$,
   so the relevant determinant is $q+sp/m$, not $q-sp/m$.
3. Adding a symmetric segment extrudes each convex section by its full
   length. This fixes the factor two. Successive segment sums split the
   pairwise terms into the future set's own area and its mixed contribution
   with the original set. Uniform support convergence permits the integral
   limit; all sets are compact and convex, including segments and points.
4. Monotonicity places both support extrema at strip endpoints. Integrating
   $2F[w+sD_*/m]$ gives $2Fbw+Fb^2D_*/m$. The antiderivative $G$ differentiates
   to the normalized fibre width, with Jacobian $F^2a^3/m$.
5. Exact record, full lens and zero delay recover independently known results.
   The full-lens cross terms are $2F^2a^2b/m+2F^2ab^2/m$, the required cubic
   expansion. Bounding the clipped area by $2Fa w$ gives the stated uniform
   joint limit. Central momentum width remains finite. A grazing record
   defeats a record-uniform positive area even at fixed tolerance and zero delay.

These checks establish an information-region area, not a norm controlling both
coordinate errors. Apparatus precision, disturbance and signal latency remain
explicit physical inputs for the next premise test. No numerical or symbolic
verification script was created or executed.

## Source acceptance

One sequential worker requested as gpt-5.6-luna at low effort returned B40
within two queries and three passage selections. Coordinator re-read EMS
§2.1, (2.1)–(2.2), (M1)–(M7), and §2.2 support-function properties in the
PDF extraction. These support classical mixed-area algebra, not the exact
clipped-force formula.

Direct ScienceDirect retrieval returned 403; one coordinator search exposed
the publisher's indexed abstract, introduction and partial conclusion, allowing
metadata and methodological checking. Full estimator theorems remain unread.
Its ideal exactness must be distinguished from finite numerical enclosures;
the partial conclusion explicitly introduces an infinitesimal sampling limit.
R09 imports none of those estimator convergence claims. The companion records
this narrower source status. No new original source was downloaded.

The two-position idea is a useful next test: propagate and intersect twice,
then distinguish momentum recovery from merely vanishing area. Difference
quotient optimization is mathematical; physical attainability of its precision
and timing requires a separate apparatus premise.
