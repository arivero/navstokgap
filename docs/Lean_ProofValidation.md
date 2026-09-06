# Lean proof validation and installation

> Sources: https://lean-lang.org/doc/reference/latest/ValidatingProofs/ and
> https://lean-lang.org/doc/reference/latest/Axioms/ and
> https://lean-lang.org/install/manual/
> Metadata: official Lean documentation, consulted 2026-09-05; versioned project not yet selected.
> Extraction: selected online documentation read; no local manual archive.

## Source digest

The documentation distinguishes successful elaboration/kernel checking from
checking whether the formal statement means the intended theorem. `#print axioms`
reports transitive dependencies, including incomplete proofs via `sorryAx` and
custom axioms. Installation supports project-specific toolchains and mathlib.

## Reading coverage and use

Read proof-validation sections on compilation and axiom inspection, the axiom
reference, and manual installation's project setup. Used only to design the
future formalisation gate. No toolchain installation or formal certificate was
performed; the URLs marked `latest` can change after retrieval.
