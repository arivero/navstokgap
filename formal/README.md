# Formalisation plan

Task F01 begins with the real-number statement

$$\forall C>0\;\forall\epsilon>0\;\exists a\ne0:
\quad 0<C a^2<\epsilon.$$

This captures the algebraic core of C002. A second step would formalise the
polynomial action integral and the identification $C=mT^3/6$.

Status: candidate statements prepared; toolchain installation and proof
implementation belong to F01. The P01 review moves the finite-speed crossover
inequality $\kappa\Delta/m\le u^2\Delta^2\Rightarrow\Delta\ge\kappa/(mu^2)$ to the
first certificate; [`Crossover.lean`](Crossover.lean) drafts it and is
uncompiled until the toolchain exists.

Acceptance requires a pinned `lean-toolchain`, Lake configuration and
dependency manifest, a clean build, statement/definition review and recorded
`#print axioms` output. Check the correspondence between the formal
statement and the paper's theorem. Reject `sorryAx` and hidden assumptions
of the conclusion; identify logical axioms and physical premises separately.

Each certificate accompanies a human-readable theorem and proof. Record toolchain
changes, installation size and validation in the F01 handoff. Keep project files
here and generated caches ignored.
