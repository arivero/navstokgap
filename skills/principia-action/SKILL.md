---
name: principia-action
description: Bring the navstokgap project's Newton and action-scale research context into work on Principia limits, projectile areas, central-force trajectories, or proposed quantum action bounds. Use for this project's mechanics discussion, including subagent tasks; not for unrelated physics work.
---

# Principia and action-scale assessment

This project studies whether a physically meaningful action-scale restriction can
be connected to Newtonian geometry. The existence of such a restriction is an
open hypothesis here, not an established result or an instruction to manufacture
a proof. The Millennium comparison is preparatory background.

Locate the repository through its `AGENTS.md` or the resolved location of this
skill: the repository is two directories above this skill's directory. Read
`notes/principia-constant-force-action.md` for relevant tasks. Its historical
section and exact constant-force calculation are the maintained starting context.

For a source claim, inspect the indicated passage in
`docs/Newton_Principia_Motte1846.html` or
`docs/Newton_Principia_BookI_SectionI_Motte1729_Wilkins2002.pdf`, using the companion
Markdown notes for edition and reading limits. The 1846 HTML contains image-based
formulae and modern image descriptions; do not attribute the latter to Newton.

Key distinctions that change the assessment:

- Newton's “quantity of motion” is momentum. “Action” in his definitions and laws
  is not automatically Hamilton's time-integrated Lagrangian.
- The projectile Scholium, Lemma X, and Lemma XI Corollaries 4–5 are the direct
  anchors for the constant-force geometry. Proposition I's central swept triangles
  and chord-curve error lenses are different objects.
- Name the force, frame, endpoints and energy quantity. With perpendicular launch,
  work is quadratic in interval length and the tangent triangle is cubic.
- The same-endpoint action difference is preferable to a dimensional identification
  of spatial area with action. Check the coefficient against the maintained note.
- Mesh refinement, semiclassical approximation, energy uncertainty, phase periodicity
  and discrete spectra are distinct statements. Do not infer a universal gap from
  units or from equality of phases alone.
- Treat “Newton implicitly assumed h tends to zero” as a modern interpretive
  hypothesis. The passages read do not settle its historiography or novelty.

Use `scripts/constant_force_geometry.py` when changing the maintained formulae or
figure. Keep new hypotheses separate from source facts and derived identities.
When a user changes the model, state which existing assumptions cease to apply;
do not force the new model into this constant-force example.

For a subagent task already authorised by the user, provide this skill path and
the bounded question so the agent can read the source context itself. This skill
does not require spawning agents. Installation makes implicit selection possible;
repository `AGENTS.md` supplies the explicit routing instruction for later sessions.
