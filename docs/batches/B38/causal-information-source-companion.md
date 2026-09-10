# B38 source companion: causal information and bounded force

## Finding

One institutional primary text was read at passage level: Liberzon's double-integrator example. It establishes bounded acceleration/braking and one-switch bang--bang time-optimal controls. This is compatible with, but does not prove, R07's fixed-horizon reachable lens. The two minimax source routes were not readable within the mandated three-page cap; the `+F/-F` lower bound remains a self-contained deterministic derivation.

## Read source

Daniel Liberzon, *Calculus of Variations and Optimal Control Theory*, §4.4.1, University of Illinois: <https://liberzon.csl.illinois.edu/teaching/cvoc/node85.html>. **passage**: system `x''=u`, `u∈[-1,1]` (eq. 4.47); maximum-principle costate and sign control (4.49--4.50); conclusion that optimal controls use only `±1` and switch at most once; parabolic phase-plane curves and switching curve. Model match: normalized double integrator. Derived specialization: physical `m,F,ℓ`, endpoint integral weights, fixed-impulse rearrangement, lens, and canonical area.

Caltech-hosted textbook PDF lead: <https://www.cds.caltech.edu/~murray/books/AM08/pdf/am08-complete_06Oct09.pdf>. **discovery** only; retrieval timed out and bibliographic metadata remains unverified. “Minimax Estimation of Functionals of Discrete Distributions,” PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC5786426/>. **discovery lead only**; retrieval met reCAPTCHA. No equation or theorem from either is evidence.

## Audit boundary and open issue

Coordinator reread Liberzon §4.4.1, (4.47)–(4.50) and the following one-switch
and phase-plane discussion. The small images' equation descriptions and prose
support the stated model match; R07's constants were checked from its own
written derivation. Requested worker model/effort: gpt-5.6-luna, low;
effective settings not independently reported. Two queries, one passage and
two failed retrievals; no concurrent workers or descendants.

No source read here supplies delayed-record causality, preparation-width/cooling closure, a force law, or a universal action constant. No numerical or symbolic verification was performed. R08 should test composition across an unobserved versus observed cut while retaining `(q,p)` rather than position alone.
