# B62: calibration tolerance and deterministic optimal recovery

## Result and bounded coverage

The primary mathematical match is information-based complexity (IBC).
Werschulz's integration example defines the radius of information and equates
it with optimal worst-case error on PDF p. 3. Its central-envelope algorithm
attains that radius on p. 4. This is a methodological match for R31's feasible
set interpretation, rather than a Hamiltonian apparatus theorem.

Coverage is one discovery query, one primary source and two selected mathematical
passages, plus metadata/abstract. Source: Arthur G. Werschulz, *An Overview of
Information-Based Complexity*, CUCS-022-02, 17 October 2002,
https://mice.cs.columbia.edu/getTechreport.php?format=pdf&techreportID=152.
Coordinator checked p. 1 metadata and the radius/central-algorithm passages
on pp. 3–4, visually inspecting p. 3. This corrects the worker's pp. 2–3
and p. 3 anchors. The displayed example uses exact integration samples;
the overview mentions contaminated information but supplies no audited
general noisy-information theorem here. Novelty remains unassessed.

## Source-to-model translation

R31's feasible preparations consistent with reported calibration error and final-record error form an information fibre. The source's radius principle supports the statement that any estimator's worst-case error is bounded below by the radius of the receiver image of that fibre. In the symmetric ball construction, the written model argument makes this radius explicit: a common-record set containing `t Z` has coordinate radii `t X_E` and `t P_E`; the zero/centre estimator attains them when `t=1`. This is a source-supported methodological identification plus a model-derived exact saturation, not a source-derived apparatus result.

The model's two-data estimate is
\[
 \|\widehat w-w\|\le (2K/\lambda)(\epsilon+\delta),\qquad
 \epsilon_x\epsilon_P\le 4L_*P_*K^2((\epsilon+\delta)/\lambda)^2.
\]
Thus the stability rate is `O((epsilon+delta)/lambda)` in receiver coordinates and quadratic in the canonical product. The exact saturation threshold supplied by the model is `epsilon >= M B lambda R_Z` (with exact final records in the displayed construction), yielding `R_x=X_E`, `R_P=P_E`, and product `X_E P_E`; the threshold is sufficient, not asserted sharp. IBC's radius equality explains why the matching lower bound is an optimal-recovery statement once the fibre is fixed, while the constants, coupling amplification, and exact common-record ball remain model obligations.

## Boundary and next use

The source does not establish the three-calibration pulse rank, the contraction chart, smooth flow bounds, or the receiver-shell geometry. It also does not justify treating calibration and record errors as stochastic variances: R31 uses deterministic support tolerances. The source-to-model suggestion for R32 is therefore to define each one-constraint-uncertain feasible fibre separately and compute its receiver-image radius; a max-tolerance upper bound cannot decide whether the four constraints are equivalent resources.
