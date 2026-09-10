# Ancient cuts and modern readjustment: provenance

The ancient anchor is Aristotle's discussion of possible and jointly realised
divisions in *On Generation and Corruption* I.2, especially around 317a.
The statement that inserting a time node can make neighbouring trajectory
vertices readjust is our modern extension. This distinction was clarified
in the conversation on 2026-09-10 and is part of the restart context.

## 1. What the sources supply

Aristotle challenges the inference from divisibility at any chosen point to
simultaneous division everywhere, using the absence of immediately consecutive
points. Earlier he treats a contact as a relation of two things. These are
the direct passage anchors in the [Joachim companion](../docs/classics/Aristotle_GC_I2_Joachim_cut_passages.md).

Plutarch's [cone report, section 39](../docs/classics/Plutarch_DeCommunibusNotitiis_39_Goodwin1874_perseus.md),
1079e–1080a, is a companion question about cutting surfaces and neighbouring
sections. It reports Democritus's dilemma and Chrysippus's response through
Plutarch's critical account. The anywhere-versus-all-together route in I005
came principally from Aristotle, rather than from a statement in the cone
passage that inserting a section moves the surrounding sections.

## 2. What we borrowed and extended

The source-inspired question is whether individually possible cuts can be
combined while preserving the compatibility of the whole construction.

In a modern time mesh, inserting $y$ between $x$ and $z$ replaces segment
$xz$ by $xy$ and $yz$. Both adjacent velocity assignments change when $y$
varies. If the old vertices are unknowns in a newly discretised boundary-value
or variational problem, their matching equations can change and their solved
positions can readjust. This is a modern mechanical interpretation, not an
ancient theorem or evidence that Aristotle anticipated path integrals.

Keep three operations distinct:

- Sampling a fixed trajectory adds a record and leaves old positions intact.
- Refining an approximate dynamical construction and solving again can change
  its old-time vertices. Their readjustment compares mathematical solutions;
  it does not describe changing the physical past.
- Inserting a variable into an exact consistent path description preserves
  the old marginal after integration. Conditioning on its observed value can
  change predictions for correlated variables. Exact classical segment-action
  composition likewise differs from changing an approximate discretisation.

The [one-cut calculation](cut-point-consistency.md), section 4, keeps the
two surrounding endpoints fixed. It isolates the local action cost; it does
not establish how all free vertices respond to a new global discretisation.

## 3. Research consequence

Keep a refinement-compatibility question alongside R05's mechanical readout.
R04 asks what receiver information must cross an existing cut. The additional
question asks how the relations on both sides are reconstructed when the cut
is inserted. Specify which equations, observables and boundary conditions are
held fixed before comparing the two constructions.

This is a source-provenance clarification and research question, with no new
claim ID, positive-action result or Newton-influence attribution. The lineage
is: Aristotle's division problem, our compatibility question, then the modern
possibility of readjusting a discretised trajectory.
