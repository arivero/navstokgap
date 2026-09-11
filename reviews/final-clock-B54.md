# R23 review: one persistent clock record restores the global inverse

C102–C103 are accepted as checked derivations in
[R23](../notes/final-clock-momentum-recovery.md).

1. Integrating the clock force gives equation (2) exactly inside the linear
   cutoff regions. Compact finite-time smooth dependence includes derivatives
   in receiver state, incoming positions and initial speed. Its normalized
   correction is O(lambda) in C1, uniformly on a fixed convex product domain.
2. The leading map is nonlinear in (z,v). The explicit speed block bounds
   speed difference; the bounded derivative of A_v then gives the receiver
   bound alpha ||dz|| <= (1+D)||dL||. Together with the position block this
   proves beta=min(1,alpha/(1+D)), globally, without assuming a convex image.
3. Only the remainder is integrated along straight segments in the convex
   initial-data domain. Subtracting its C lambda Lipschitz bound from beta
   proves the uniform exact inverse margin beta/2 at small positive coupling.
4. Compact minimum-residual fitting doubles the record error; dividing by
   beta/2 gives 4 delta/beta. The two canonical risk bounds give the stated
   factor 16 and action units. The clock record error uses M_c V_* units,
   so no additional coupling division enters that error component.
5. The energy shell is a possible domain restriction, not an equation used
   by the inverse. A whole bounded energy ball is also recovered. Final
   clock momentum persists, while pointer positions are time-stamped at T.
   Back-reaction is jointly calibrated, not omitted from inferred speed.

Preparation widths, design and masses stay fixed; errors close as supplied
record precision improves. Initial offset, zero incoming probe momenta and
exact Hamiltonian remain known. This tests information sufficiency, while
physical implementation of joint record access remains a separate task.

[B54](../references/batches/B54.md) is a bounded standard-method audit, not
an exact apparatus prior-art search. No numerical or symbolic scripts ran.
