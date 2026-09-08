---
name: principia-action
description: Guide navstokgap research on classical mechanisms selecting a positive universal action scale, Newtonian cut limits, mechanical receivers and gap estimates. Load the project's proof obligations and task-specific notes for mechanics research or its source audits.
---

# Principia and action-scale research

The central target is a classically defined action-valued quantity
$\mathsf h_\varepsilon(t)$ converging to a positive universal constant, with its
quantum role derived from the dynamics. Each research step should discharge an
obligation, supply a mechanism, or settle a candidate premise by counterexample.

Locate the repository through AGENTS.md or this skill's resolved location:
the repository is two directories above the skill directory. On a fresh session
read `research/STATE.md`, `research/PROGRAMME.md` and the assigned task.
For model design, read `research/ACTION_FIELD_TARGET.md` and the relevant
route below. At a context restart, follow the bibliography-ideas hook in AGENTS.
For a calculation or historical argument using the constant-force example, read
`notes/principia-constant-force-action.md`. For metadata work, use the
relevant source companion and the task's stated question.

## Select the next proof obligation

Track five gates separately: classical definition and units; exclusion of zero;
convergence in a stated topology; universality across masses and preparations;
and identification with the quantum phase/action parameter. Record which gate
the selected task advances and which physical premise supplies that advance.

For every limit, name the varying parameter: physical time $t$, mesh
$\varepsilon$, observation duration $\Delta$, action parameter, volume or
$c^{-1}$. A stationary ensemble's long-window plateau and physical-time
attraction of a dynamical field require different arguments.

Choose the smallest relevant route, then read its maintained note:

- **Positive plateau or receiver:** `papers/classical-action-field.tex` and
  `research/ACTION_FIELD_TARGET.md`. For an explicit bath use
  `papers/collision-action-relaxation.tex`. Trace variance and correlation time
  to energy, preparation and interaction parameters; test zero-variance and
  rapid-decorrelation families within the proposed premises.
- **Universality:** `notes/composition-universality.md`. Separate mass-only
  coefficient closure, full-state composition and preparation independence.
  Locate the positive reference input before invoking the mass-additivity result.
- **Cut refinement and finite speed:** `research/CUT_POINT_TARGET.md`, then
  `notes/bridge-crossover.md` or `notes/bounded-acceleration-return.md` as the
  task requires. Keep sampling cuts, conditioned bridges and physical
  interventions distinct; track uniform force and mass bounds.
- **Gap mechanism:** `notes/susceptibility-gap.md`. Specify the operator,
  domain, invariant law, clock and observable access. Test hidden slow modes
  and the constants needed uniformly across the proposed family.
- **Quantum role:** `notes/checkerboard-dynamics.md`. Record the source of
  complex amplitudes, the measurement rule and the dimensional action constant;
  compare their cut limits with the real stochastic model.

Use `claims/LEDGER.md` for acceptance and `research/TASKS.md` for live priority;
source-inspired drafts retain their own review status. Prefer a mechanical
selection test over another solvable spectrum when it advances the central gate.

## Working context

- The constant-force chord–curve relation is
  $\Delta S=F^2T^3/(24m)=T\delta E/12$, where $\delta E=\Delta K=-\Delta V$.
  The family $\eta=a t(T-t)$ has positive action differences approaching zero.
- The free Dirichlet Hessian bounds quadratic cost relative to a norm.
  Jacobi fields solve the linearized equations; the full variational path class
  also includes off-shell fluctuations.
- Quantum two-arm distinguishability uses explicit state, phase and measurement
  premises. Its threshold depends on copy count and target success probability.
  Keep the perfect-discrimination endpoint separate.
- A distributional kernel calculation specifies the variable, normalization,
  test-function space and limit. The free short-time kernel gives a delta and
  a second-derivative correction.
- For each model, name the force, frame, endpoints, energy quantity and units.
  Track mesh refinement, semiclassical limits and spectral limits separately.
- Distinguish a positive prescribed-endpoint cost, the infimum of positive
  excess costs, an action-valued response plateau and an operator spectral gap.
  Converting a relaxation rate to energy requires a specified action factor.

The technical paper contains the maintained proofs. `claims/LEDGER.md`
records evidence status; `ideas/` records proposals and their tests.

## Historical anchors

For source claims, inspect the relevant passage in the local Principia HTML or
Motte/Wilkins PDF through its companion. Use Lemmas X–XI and the projectile
Scholium for constant-force geometry; use Proposition I for central swept areas.
Newton's quantity of motion is momentum. Translate historical uses of “action”
in their local context before introducing Hamilton's integral.

The 1846 HTML contains image-based equations and modern image descriptions.
Attribute the latter to the electronic edition. NATP00385 supplies a
calculus-priority fragment collection; its diplomatic/XML versions expose
revisions hidden in the normalized view. The Classical Scholia have their own
H02/H03 corpus tasks.

The proposed implicit $h\to0$ reading is a modern historical conjecture. Track
its supporting passages and chronology in the historical audit.

## Writing and verification

Lead with the result or question. Put assumptions at their point of use and
record reading coverage once in the source companion. Follow AGENTS.md's
results-first writing rule.

Use `scripts/constant_force_geometry.py` when changing the maintained
formulae or figure. For a changed model, identify the inherited assumptions and
the new ones. Authorised subagents use `agents/PROTOCOL.md`, including
the explicit effort setting and ultra prohibition.
