# B64 source companion: pulse-column Hermite audit

## Coverage

Primary source: NIST Digital Library of Mathematical Functions, §3.3, “Interpolation,” https://dlmf.nist.gov/3.3. Metadata and passage-level text were read for the uniqueness/cardinal statements (3.3.1–3.3.3, displayed lines 48–126) and confluence statement in Newton interpolation (displayed lines 707–724). The route used one discovery query and one source retrieval; no exhaustive prior-art claim is made. No local source file or PDF extraction was needed.

## Source-to-model capsule

Source passage → unique polynomial interpolation and cardinal basis at distinct nodes; confluence identifies repeated-node data with derivatives. Borrowed construction → treat measurements x(1), x(2), x(3), x'(1) as Hermite data for a cubic. Decisive test → the only homogeneous cubic satisfying three value zeros and a double zero at 1 is zero, so the limiting map is invertible and its four inverse columns are the displayed cardinal polynomials. Premise/limit → this concerns the scaled early-pulse limit at fixed positive \tau; transfer to finite smooth pulses requires a separate uniform ODE/pulse-width estimate.

## Audit findings

The scaled equation and O(\tau^2) perturbation claim are dimensionally coherent under X(u)=x(\tau u). Direct written algebra confirms the four products in section 4 satisfy the required interpolation data, and their p_j(0), p'_j(0) entries are nonzero. This proves a nonzero limiting canonical pair for each ideal row.

Proof concern: “narrow-pulse limit” must be made quantitative for the fixed chosen positive widths. Row factors \sigma_j may be nonzero, but convergence after normalization and preservation of both determinant and inverse-entry margins need an explicit continuity/operator-norm statement. Also keep the auxiliary width limit separate from the physical risk theorem and state that all pulse supports remain disjoint and admissible. The source does not support these apparatus claims.

## Coordinator resolution

The coordinator rechecked DLMF §3.3(i), 3.3.1–3.3.3, and §3.3(iv)'s
confluence paragraph following 3.3.38. R32 §4 now supplies the missing
uniform width estimate: positive normalized pulse averages differ from the
ideal rows by at most C_tau h, and the inverse identity bounds the resulting
inverse perturbation. All eight canonical entries retain a strict margin.
This resolves the worker's finite-width concern for the explicitly selected
subfamily; it does not establish the property for every R30 design.
