---
name: principia-action
description: Bring the navstokgap project's Newton and action-scale research context into work on Principia limits, projectile areas, central-force trajectories, or proposed quantum action bounds. Scoped to this project's mechanics discussion and subagent tasks.
---

# Principia and action-scale research

This project connects Newtonian trajectory geometry, action variations and
operational resolution. Its research targets are quantum reconstruction and a
toy mechanism for gap formation.

Locate the repository through AGENTS.md or this skill's resolved location:
the repository is two directories above the skill directory. On a fresh session
read `research/STATE.md`, `research/PROGRAMME.md` and the assigned task.
For a calculation or historical argument using the constant-force example, read
`notes/principia-constant-force-action.md`. For metadata work, use the
relevant source companion and the task's stated question.

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
