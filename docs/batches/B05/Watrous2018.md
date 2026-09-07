# Watrous — The Theory of Quantum Information, Chapter 3

> Source: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
> Metadata: John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018), ch. 3, “Similarity and distance among states and channels.” Author-hosted manuscript, standard-layout chapter PDF.
> Extraction: author-hosted PDF inspected with the web PDF renderer on 2026-09-06; printed pages 124–130 and 198 (PDF pages 0–6 and 74) read. Formula typography in the renderer is occasionally linearized; theorem and equation numbers were retained.

## Source digest

Section 3.1 formulates binary discrimination of known density operators with prior
λ and 1-λ. The Holevo–Helstrom theorem is Theorem 3.4, printed pp. 128–129,
eq. (3.11): every binary measurement has success at most

\[
\frac12+\frac12\|\lambda\rho_0-(1-\lambda)\rho_1\|_1,
\]

and a projective measurement attains equality. The proof uses the Jordan–Hahn
decomposition, so this is an exact finite-dimensional arbitrary-binary-measurement
result, not merely a bound for a selected detector. The following text (eqs. (3.19)–
(3.20)) restates the optimum success probability and notes that any multoutcome
strategy followed by a binary guess reduces to a binary measurement.

For the project’s equal-prior pure states, set \(\lambda=1/2\). The elementary
rank-two calculation \(\|\lvert\psi_0\rangle\langle\psi_0\rvert-
\lvert\psi_1\rangle\langle\psi_1\rvert\|_1=2\sqrt{1-|\langle\psi_0|\psi_1\rangle|^2}\)
turns Theorem 3.4 into the familiar pure-state formula. Tensoring \(N\) identical
copies raises the overlap magnitude to the \(N\)th power. For the phase pair in the
paper, \(|\langle\psi_0|\psi_\phi\rangle|=|\cos(\phi/2)|\); solving the resulting
inequality on \(|\phi|\le\pi\) gives C006’s threshold. These last substitutions,
including the action encoding \(\phi=\Delta S/\hbar\), are derived consequences
and model assumptions, not statements made by Watrous.

The bibliographic remarks on printed p. 198 attribute Theorem 3.4’s projective
case to Helstrom (1967) and its general-measurement case to Holevo (1972). Those
historical originals were not separately inspected in this bounded audit.

## Use and limits

Use Theorem 3.4 as the exact prior-literature match for C006’s optimal binary
measurement premise. Cite the pure-state and N-copy algebra as an elementary
specialization. Watrous does not introduce an action, \(\hbar\), two-arm apparatus,
or a positive action gap; C006’s action threshold is therefore conditional on the
paper’s explicit state-preparation and phase-encoding hypotheses.
