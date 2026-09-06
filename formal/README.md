# Formal verification candidates (not certificates)

No Lean environment is installed here and no formal theorem is claimed. This
directory records what would justify introducing one, rather than storing
uncompiled `.lean` sketches that could be mistaken for proofs.

F01's first candidate is the elementary real statement

$$\forall C>0\;\forall\epsilon>0\;\exists a\ne0:
\quad 0<C a^2<\epsilon.$$

It captures the algebraic core of C002. It does NOT formalise the action integral,
its domain or the derivation of $C=mT^3/6$. Those are separate bridge obligations.
The next candidate is that polynomial integral identity, only if supporting
integration libraries make the task proportionate.

Acceptance requires a pinned `lean-toolchain`, `lakefile` and dependency manifest,
a clean `lake build`, statement/definition review, and recorded `#print axioms`
output. Reject `sorryAx`, hidden custom axioms that assume the conclusion, and
claims that native numerical evaluation alone certifies an analytic theorem.
Document ordinary logical axioms separately from physical assumptions. A new
formalisation must have a human-readable theorem and proof in the paper.

Do not update the toolchain implicitly between sessions. If installation becomes
necessary, keep project artifacts here and caches ignored, and record download
size/toolchain choices in the F01 handoff.
