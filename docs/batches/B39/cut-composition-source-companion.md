# B39 source companion: cut composition and observed fibres

## Finding

The sources match the bounded double-integrator and general exact set-propagation framework, but do not state R08's continuous-time sheared lens, position fibre, or canonical-area formulas. Those formulas remain written derivations from the model note.

## Read sources

Daniel Liberzon, *Calculus of Variations and Optimal Control Theory*, §4.4.1, <https://liberzon.csl.illinois.edu/teaching/cvoc/node85.html>, **passage**, lines 4–35. The normalized system `x''=u`, `u∈[-1,1]`, its state-space form, bounded acceleration interpretation, bang–bang extremals and one-switch phase-plane parabolas are explicit. Match: bounded double integrator. Derived specialization: physical `m,F`, fixed-horizon integral image, lens, and area.

Trevor J. Bird et al., “Hybrid zonotopes: a new set representation for reachability analysis of mixed logical dynamical systems,” <https://arxiv.org/html/2106.14831v3>, **passage**, abstract and §4.1. The text states closure under linear mappings and Minkowski sums and gives exact forward reachable-set propagation for its MLD class. Match: set-valued propagation vocabulary. Limit: discrete-time mixed logical dynamics, with constraints and representation issues unlike the unconstrained measurable-force concatenation used by R08.

## Claim ledger mapping

**C072 — partial source match / derived result.** Source support covers the state model and reachable-set operations in adjacent settings. The equality `K_T=S_bK_a+K_b` follows directly by splitting and concatenating admissible force inputs. The rectangle enlargement counterexample is a model-specific proof that marginalizing momentum destroys the correlation.

**C073 — no direct source match / derived result.** The exact momentum fibre at fixed position, terminal set, and area formula follow from solving the R08 lens inequalities and applying a determinant-one shear. The area limit is an information/refinement consequence. It must not be described as momentum recovery: at central position observations the momentum width remains nonzero while the two-dimensional area collapses.

## Coverage limits

Two web searches were used; two substantive primary passages were readable, and the third permitted route yielded no usable segment-area theorem. No PDF was downloaded and no numerical or symbolic verification was performed. No source read addresses the action normalization, universal positive scale, observation apparatus, or preparation restrictions.

## R09 connection

The next source-inspired test should propagate an interval-valued position observation through the exact compatible phase-state set. Compare that result with a rectangular outer approximation and keep the resulting overapproximation error separate from physical force uncertainty.

Coordinator verified v3 (25 April 2023), abstract and §4.1 Theorem 8,
equation (18). These section anchors control over extraction line numbers.
