# Foundational value of the established Ising gap

The Ising example remains valuable as an explicit account of the dynamical
input needed to turn equilibrium statistics into relaxation rates and quantum
energy gaps. Its publication opportunity is a focused conceptual synthesis.
Lubetzky–Sly supplies the exact literature match and a useful contrast between
a uniform gap and growing global equilibration time.

User-requested assessment, 2026-09-13. This reuses C124/B68 and C126/B71,
with [B73](../references/batches/B73.md) supplying additional source statements.
The [three publication routes](../publication-routes/01-elastic-gas-comparison.md)
remain the original shortlist; this is a supporting assessment.

## Three quantities with different physical jobs

For the periodic zero-field heat-bath chain on $N\ge3$ sites, fix dimensionless
coupling $b\ge0$ and per-site refresh rate $a>0$. The domain of $Q_N$ is the
full finite-dimensional function space on spin configurations, with Gibbs
inner product; the gap is above the constant sector.

| Quantity | Meaning and normalization |
| --- | --- |
| $\gamma=a[1-\tanh(2b)]$ | Slowest nonconstant relaxation rate, in inverse-time units; fixed as $N$ grows at fixed $a,b$ |
| $t_{\rm mix}^{(N)}(\epsilon)\sim(\log N)/(2\gamma)$ | Global total-variation mixing time at fixed tolerance $0<\epsilon<1$; large-$N$ source Corollary 3 with rate $a$ restored |
| $\Delta_H=K\gamma$ | Energy gap of the constructed Hermitian parent $H=K[-D^{1/2}Q_ND^{-1/2}]$, with supplied action $K>0$ and $D=\operatorname{diag}\pi$ |

The first two rows are established source results with a clock rescaling; the
third is C126. A uniform slow-mode decay rate can coexist with a growing time
to equilibrate the entire configuration distribution.

## Foundational content

**Equilibrium specifies weights; dynamics supplies rates.** The Gibbs law and
square-root Gibbs ground vector stay fixed when all transition rates are
rescaled. The relaxation spectrum changes. B71's stochastic-parent sources
already expose this freedom; C124 gives a soluble interacting example.

**Physical energy requires a physical identification.** C126 constructs a local
positive Hermitian operator and an imaginary-time correspondence. Its use as
the Hamiltonian of an independently specified physical system additionally
fixes the physical clock, state/observable interpretation and action conversion.
These are concrete premises for the programme to test.

**Limits ask different questions.** Fixed $a,b$ retains the gap as volume grows.
Growing coupling or a fixed total refresh budget can close it. The logarithmic
mixing time introduces a separate global observation timescale. The continuum
limit and identification of physical dynamics remain further questions.

## Publication judgement and return criterion

A possible focus is *Equilibrium, relaxation and quantum energy: locating the
dynamical input in stochastic reconstructions*. It would combine the Ising
example, gap/mixing distinction and stochastic-parent map around one question:
what physical information selects the generator and its normalization?

This is a useful foundational benchmark now. A standalone *Foundations of
Physics* paper would need a distinctive argument beyond the established
stochastic-parent correspondence—for example, a precise reconstruction claim
whose physical premise the comparison resolves. Another spectrum calculation
would add little to that case.

Keep this as supporting material. Return for a named physical-generator
comparison or a sharply identified conceptual claim; Q01 retains priority.
The exact gap belongs to established literature. The foundational value lies
in making the separate physical premises explicit.
