# R05/B35 coordinator review

Accept C066–C067 as conditional written results for an externally switched
impulsive Hamiltonian instrument with scalable incoming probe preparations.
Novelty is unassessed. The construction completes R05's quiet-preparation
countertest; R06 owns finite-duration and fixed-apparatus implementation.

## Proof review

1. The reduced tagged pair is canonical. On the full chain
   $x=x_1-X$, $P=p_1-(p_2+p_3)/2$ have Poisson bracket one and commute
   with $y=x_2-x_3$, $Q=(p_2-p_3)/2$. Each probe coupling preserves the
   centre constraints and hidden pair; its reaction is spatially distributed.
2. Direct Hamilton equations give the two triangular shear maps. The second
   pointer sees $P-\alpha\pi$, so its pre-cut error includes the first
   disturbance. All support bounds are attained on the independent rectangle.
   The intrinsic products have position times momentum units; both shrink
   quadratically under width scaling without violating Liouville preservation
   of any individual preparation.
3. The inverse follows by the adjugate and the positive leading determinant
   in R04. Its lower-left entry is
   $-12\mu\nu/(g\delta^3)+O(\delta^{-1})$. Fixed units make the norm
   estimate meaningful. Fixed-error sensitivity refers to the stated linear
   estimator, not all estimators with energy support or longer history.
4. Between successive pre-cut states, the flow includes the initial kick.
   Subtraction gives exactly
   $B^{-1}(e_{i+1}-Ae_i+Ad_i)$; ignoring that last term would leave the
   readout proof incomplete. Widths $O(\eta^4)$ control it and the observation
   errors uniformly by $O(\eta)$ after inversion. The terminal hidden state
   follows by one propagation; the initial recovery has one-step latency.
5. Duhamel's finite sum of bounded propagators gives $N O(\eta^4)=O(\eta^3)$
   physical disturbance at fixed horizon. No random cancellation is assumed.
   Continuity of the quadratic energy on a compact neighbourhood controls its
   finite-mesh change. The system preparation stays fixed; probe preparations
   and intervention laws change across meshes and are not exactly projective.
6. Two fixed-mass probes per cut give growing total mass. The stated vanishing
   free kinetic-energy sum excludes preparation, trapping, switching and
   recording. Neither a strict speed/force bound during the impulses nor a
   finite-duration mechanical realization is established. Position jumps
   during the ideal momentum readout make this boundary especially relevant.

## Sources

The coordinator verified Katagiri v2 metadata and rendered §5 equations,
and Theurel's APS metadata and abstract. The [B35 companion](../docs/batches/B35/readout-source-companion.md)
records the rendered Liouvillian sign discrepancy and the independent
Hamilton-equation convention used here. The worker's candidate-contribution
labels were narrowed to derived consequences with novelty unassessed.
Theurel's finite-temperature premise remains a full-model reading obligation;
a lower energy bound alone is insufficient to install a phase-width bound.

No numerical or symbolic verification scripts were created or executed.
Document validation is recorded in the [R05 handoff](../research/handoffs/R05.md).
