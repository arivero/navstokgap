# R06/B37 coordinator review

C068–C069 are accepted as written consequences of the specified autonomous
classical apparatus. Fixed total mass, positive kinetic energy, fixed pulse
widths, finite horizon and upper force bounds permit a vanishing reconstruction
accuracy–disturbance product when incoming preparation widths and final record
precision may improve. This is delayed reconstruction of known dynamics.

## Proof review

The reduced receiver constants and physical/canonical momentum conversion agree
with R04. The new interaction is a coordinate potential with no explicit time
parameter. Bounded cutoffs give a lower bound on total potential; conservation
of total energy bounds the receiver quadratic energy and every kinetic term.
This makes the receiver force ceiling uniform on the admitted class. It does
not turn harmonic springs into globally bounded forces on all phase space.

The derivative map from $(x,P,y,Q)$ to $(x,\dot x,\ddot x,x^{(3)})$ has
nonzero triangular diagonal. If evaluation rows failed to span on an open
interval, analyticity would give a zero output with zero initial derivatives,
contradicting that rank. Four evaluation times exist, and continuity of the
row-normalized pulse integrals preserves their determinant at positive design
width. Pulse width is fixed thereafter; inverse conditioning depends on that
design and the fixed positive horizon.

Integrating the globally bounded probe force gives probe momentum and position
$O(b+\lambda)$. Then bounded receiver variation of constants gives
$O(\lambda b+\lambda^2)$ reaction. This places the trajectory within the
cutoff's linear region. The clock force is also $O(\lambda b+\lambda^2)$;
including initial clock uncertainty gives $O(b+\lambda^2)$ clock deviation.
The fixed exit margin and positive clock momentum guarantee permanent exit.
These are bootstrap estimates on a fixed compact reference neighbourhood;
no unaffected-clock approximation is used.

The integrated signal remainder is $O(\lambda b+\lambda^3)$ because both
clock timing and receiver motion enter a bounded smooth integrand. Unknown
initial probe momenta contribute $O(b/\lambda)$ after calibration. Taking
$b=\lambda^3$ gives uniform second-order error and disturbance, and the
product of the specified physical-unit suprema is fourth order. Norms,
pulse-shape dependence, preparation domain and force-bound domain are explicit
in the note, addressing the worker's checklist.

The final record is a conserved momentum, not a confined position: unlimited
storage space is not included in the finite-horizon coordinate budget. Exact
record access remains an input. Finite error $r$ gives a term $r/\lambda$ in
this estimator's upper bound, which alone proves no lower bound on all
estimators. The same distinction applies to the proposed R07 causal task.

## Source review and cost

One sequential gpt-5.6-luna worker, explicitly low effort, completed B37 with
zero searches and four cached primary pages. Coordinator waited for completion
and independently viewed the same source images: Theurel v2 PDF pp. 5–7 and
Hermann–Krener printed p. 733. Effective worker settings were not independently
reported; no descendants were dispatched. A short follow-up confirmed zero
queries and required no further reading.

Theurel (11), (14), (18)–(22) establishes the thermal ready widths, conserved
pointer, imprecision and apparatus-dependent quality product. Footnote 5 on
p. 5 explicitly uses a shrinking square pulse and neglects free drift. Page 7
allows cooling or tighter trapping to reduce the quality parameter. The arXiv
v2 metadata was checked live: 6 March 2025 revision, journal PRE 110, 024124
(2024), DOI 10.1103/PhysRevE.110.024124. Existing untracked B36 source artifacts
were preserved unchanged and integrated because they support this task; their
historical worker page overrun remains recorded, not repeated here.

Hermann–Krener Theorem 3.1 on p. 733 is a sufficient observability rank theorem
for smooth systems. The worker's analytic-system wording was corrected;
analyticity enters our independent evaluation-row proof. No source theorem is
claimed to state this exact four-probe apparatus. Final literature status is
**derived consequences, novelty unassessed**, within two-source coverage.

No numerical or symbolic verification scripts were created or run. Document
validation and manuscript build outcomes are recorded in the R06 handoff.
