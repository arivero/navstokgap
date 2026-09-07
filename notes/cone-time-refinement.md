# From cone sections to time refinement

The bibliography supplies a concrete experiment: insert an intermediate point,
eliminate it by composition, and identify which data survive. For the free
particle, this operation closes exactly on a family of Gaussian kernels with
an arbitrary positive action scale. The next research question is the physical
selection of a member of that family.

The maintained calculation is [Time Refinement and an Action Scale](../papers/time-refinement.tex).
Proof and literature status are recorded separately in the claim ledger.

## What each source puts into the model

| Source | Idea to retain | Calculation or research obligation |
| --- | --- | --- |
| [Plutarch in Xylander, 1570](../docs/batches/H04/Xylander1570_p823.md) | Compare the faces produced by a cut | Specify separated faces and their limiting object |
| [Rivero, cone, 1999](../docs/Rivero_Cone_1999.md) | Compare refinements at a common scale | Retain a rescaled difference when raw differences vanish |
| [Rivero, path integral, 1998](../docs/Rivero_FeynmanFormula_1998.md) | Eliminate inserted positions and track regulators | Write and test a normalized finite blocking map |
| [Brouder, 1999](../docs/Brouder_RungeKutta_1999.md) | Rooted-tree algebra for composed numerical flows and renormalisation | Organise nonlinear corrections after the Gaussian calculation |
| [Cariñena et al., 1999](../docs/CarinenaEtAl_TangentGroupoid_1999.md) | Quantum and classical structures in a single geometric construction | Audit the precise quantum-completion and classical-limit theorem |

The Wilson–Kogut connection presently enters through Rivero's explicit use of
their scaling construction. Direct reading of their 1974 review, especially the
chapter 12 cited in the 1998 note, remains a bounded source task. Brouder supplies
the specific Butcher/Connes–Kreimer algebraic link. These are separate source
links, each with a mathematical operation to investigate.

## Spatial and temporal cuts

For a smooth cone profile with area $A(z)$, a modern difference quotient retains
$[A(z+\epsilon)-A(z)]/\epsilon$ as the two faces approach. Its limit is $A'(z)$.
The area's units are length squared; this is ordinary spatial geometry.

Time slicing introduces a different operation. At fixed endpoints $x,z$, an
inserted position $y$ is integrated over:

$$K_{s+t}(z,x)=\int_{\mathbb R}K_t(z,y)K_s(y,x)\,dy.$$

Thus temporal refinement involves both subdivision and a rule for eliminating
the new degree of freedom. For real positive Gaussian kernels the integral is
ordinary; for oscillatory free kernels it is defined through Fourier operators
or a stated regularisation. Calling the positive-kernel model “Euclidean” refers
to its quantum imaginary-time counterpart, a different use of the word from
Euclidean cone geometry.

## The first completed test and the next selection question

For $m>0$, time $t>0$ and action parameter $\kappa>0$, the free positive kernel is

$$G_t^\kappa(x)=\sqrt{\frac{m}{2\pi\kappa t}}
\exp\!\left(-\frac{mx^2}{2\kappa t}\right).$$

Its variance is $\kappa t/m$. Convolution adds variances, so integrating out any
number of inserted points leaves the same $\kappa$. A Gaussian bridge between
fixed endpoints concentrates on the straight Newtonian path as $\kappa\to0$.
These standard facts give an exact setting in which mesh refinement and the
action-scale limit can be examined independently.

The general time-homogeneous Gaussian family has variance $a t$, with $a\ge0$.
The action scale is $\kappa=ma$. Time composition and continuity leave $a$ free;
$a=0$ is the deterministic member. Demanding a positive-width density selects
$a>0$ by assumption. The strong target requires an independently motivated
physical principle that produces that selection and explains universality
across interacting systems. A lower bound on $\kappa$ over an entire model
class would be a stronger statement, with its own quantifiers and units.

The corresponding oscillatory family supplies unitary free evolution for each
$\kappa>0$. Converting the positive kernel to it is an explicitly chosen
analytic-continuation step. A physical justification for that step belongs
alongside, rather than downstream of, scale selection.

## Reception history: a testable question

Xylander's Latin *Moralia* contains the cone dilemma on printed pp. 823–824 in
1570. The [H04 batch](../references/batches/H04.md) establishes availability and
records a bounded reception search. Modern historical discussion is present:
Auffret examines the cone in relation to limits in a chapter on Leibniz and
Chrysippus. His direct Leibniz example concerns a rolling cylinder/cone and
free will, which is a distinct passage.

The next historical test is author-specific: did a mathematician invoke the
section dilemma in work on indivisibles or the continuum? Begin with Newton's
Plutarch references in the existing dossier and an independently indexed
Leibniz corpus. Search title variants and Latin phrases as well as names;
record ownership, quotation and mathematical use separately. The hypothesis
of disciplinary separation between philosophical reception and mathematical
practice can then be tested against those records.

## Next bounded work: M05/B07

1. Audit Rivero's finite-dimensional oscillatory proposal: use a quadratic
   function, fix Fourier normalization and stationary-phase weights, and
   distinguish a distribution on critical points from a path amplitude.
2. Extract the exact map and parameters from Wilson–Kogut chapter 12 and
   Rivero's equation (6). Apply the map to the already normalized Gaussian
   family before introducing a nonlinear interaction.
3. Read the tangent-groupoid quantization theorem's hypotheses and limit
   topology. Match them to the strong target's quantum-completion branch.

Each source task must end with a premise to test, a construction to implement,
or a proof obligation to resolve. Use one small worker at a time and review its
handoff before resuming coordinator work. The spectral laboratory M03 and
Classical Scholia H02/H03 remain separate unfinished tasks.
