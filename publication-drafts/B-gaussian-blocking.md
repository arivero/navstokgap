# Finite-range Gaussian blocking and a cutoff-uniform covariance estimate

**Manuscript B — full working draft.** Author and affiliation details are intentionally omitted pending approval. This draft isolates the blocking theorem from the separate continuum reconstruction article D. Prior-art positioning and independent proof review remain before submission.

## Abstract

A massive Gaussian scalar field admits an exact multiscale decomposition when its covariance is written as a sum of positive finite-range covariances. We use this decomposition to define a Gaussian Markov blocking kernel and prove two scale-by-scale estimates. For bounded local observables, the connected-covariance defect vanishes once the supports are farther apart than the fluctuation range. For Weyl observables, positivity yields a cutoff-uniform summability bound in a covariance seminorm. The proof separates imported finite-range input from the conditional-expectation identities used in the blocking estimate. It provides a model theorem for the correlation-transport interfaces used in multiscale constructions.

**Keywords:** finite-range decomposition; Gaussian field; Markov kernel; covariance estimate; Weyl observables.

## 1. Introduction

Multiscale arguments need a precise account of what one blocking step does to observables. In a Gaussian model, the field can be split into independent fluctuation fields with positive covariances. Integrating out one fluctuation defines a Markov kernel, and finite range makes its connected effect exactly local. A second estimate, adapted to Weyl observables, controls the sum of fluctuations across all scales without a scale-counting loss.

The finite-range decomposition itself is an established input. In particular, Brydges, Guadagni and Mitter construct positive finite-range pieces for massive lattice resolvents in dimensions at least three (*Journal of Statistical Physics* 115 (2004), 415–449, DOI 10.1023/B:JOSS.0000019818.81237.66). The contribution here is the explicit passage from that covariance splitting to two stated covariance transport bounds. The theorem is formulated for a massive scalar with supplied mass parameter.

## 2. Covariance decomposition and the blocking kernel

On the four-dimensional lattice \(a\mathbb Z^4\), take a centered real Gaussian field with covariance
\[
C_a=\hbar(-\Delta_{\rm lat}+(am)^2)^{-1},\qquad m>0.
\tag{1}
\]
A complex scalar can be formed from two independent real copies. Assume a positive decomposition
\[
C_a=\sum_{j=0}^{K-1}\Gamma_{a,j}+C_{a,K},
\qquad \Gamma_{a,j}(x,y)=0\quad\text{when }|x-y|_\infty>RL^j,
\tag{2}
\]
with \(L\ge2\), fixed \(R\), and positive residual covariance. The finite-volume version of the decomposition, when used, is assumed to satisfy the same positivity and range properties uniformly in the volume. This is the exact input needed below.

Let independent Gaussian fields \(\zeta_j\) have covariances \(\Gamma_{a,j}\), and let \(\varphi_K\) have covariance \(C_{a,K}\). Define recursively
\[
\varphi_j=\zeta_j+\varphi_{j+1},\qquad 0\le j<K.
\tag{3}
\]
For a bounded observable \(F\), set
\[
(\mathcal E_jF)(\varphi_{j+1})=
\mathbb E_{\zeta_j}F(\zeta_j+\varphi_{j+1}).
\tag{4}
\]
This is a Gaussian Markov kernel; it is an integration map and not a deterministic map from one field configuration to another.

## 3. Exact transport for bounded local observables

Write \(\langle F;G\rangle_\mu=\mathbb E_\mu(FG)-\mathbb E_\mu F\,\mathbb E_\mu G\). Conditional covariance gives
\[
\begin{aligned}
&\langle F;G\rangle_{\varphi_j}
-\langle\mathcal E_jF;\mathcal E_jG\rangle_{\varphi_{j+1}}\\
&\qquad=\mathbb E_{\varphi_{j+1}}
\operatorname{Cov}_{\zeta_j}\bigl(F(\zeta_j+\varphi_{j+1}),G(\zeta_j+\varphi_{j+1})\bigr).
\end{aligned}
\tag{5}
\]
If the supports of \(F,G\) are separated by more than \(R\) in the scale coordinates, their restrictions of \(\zeta_j\) are independent, so (5) is zero. At all distances,
\[
\left|\langle F;G\rangle_{\varphi_j}
-\langle\mathcal E_jF;\mathcal E_jG\rangle_{\varphi_{j+1}}\right|
\le4\|F\|_\infty\|G\|_\infty.
\tag{6}
\]
Thus for any chosen \(\gamma>0\), with \(d_j\) the support distance at scale \(j\),
\[
\left|\langle F;G\rangle_{\varphi_j}
-\langle\mathcal E_jF;\mathcal E_jG\rangle_{\varphi_{j+1}}\right|
\le4e^{\gamma R}\|F\|_\infty\|G\|_\infty e^{-\gamma d_j}.
\tag{7}
\]

**Proposition 1.** Under (2), the one-step connected-covariance defect for bounded local observables vanishes outside the fluctuation range and obeys (7), uniformly in the cutoff and in any finite volume where (2) holds uniformly.

*Proof.* Equation (5) is the conditional covariance identity. Finite-range independence makes its right-hand side zero for support distance greater than \(R\). Otherwise (6) applies; for \(d_j\le R\), the factor \(e^{\gamma R}e^{-\gamma d_j}\) is at least one. \(\square\)

## 4. A summable Weyl seminorm

For a real test function \(f\), define the Weyl observable and scale seminorm
\[
W_j(f)=e^{i\langle\varphi_j,f\rangle},\qquad
a_j(f)^2=(f,\Gamma_{a,j}f).
\tag{8}
\]
The Gaussian characteristic function gives
\[
\mathcal E_jW_j(f)=e^{-a_j(f)^2/2}W_{j+1}(f).
\tag{9}
\]
For Weyl observables, conditional Cauchy–Schwarz and the variance of the integrated linear functional give
\[
\left|\langle W_j(f);W_j(g)\rangle
-\langle\mathcal E_jW_j(f);\mathcal E_jW_j(g)\rangle\right|
\le a_j(f)a_j(g).
\tag{10}
\]
Positivity and (2) imply
\[
\sum_{j<K}a_j(f)^2\le(f,C_af).
\tag{11}
\]
Consequently,
\[
\sum_{j<K}a_j(f)a_j(g)
\le\sqrt{(f,C_af)(g,C_ag)}.
\tag{12}
\]
For lattice representatives of fixed smooth continuum tests, the right side is uniformly finite whenever their massive continuum covariances are finite.

**Proposition 2.** The Weyl-algebra blocking defects are summable over all scales with the cutoff-independent covariance seminorm (12).

*Proof.* Apply Cauchy–Schwarz to the scale index and use (11) for each test. \(\square\)

## 5. Relation to continuum reconstruction

The estimates above are statements about the blocking kernel and covariance seminorm. To obtain a continuum theory one separately verifies convergence of smeared covariances and the OS axioms; these are presented as a companion article. Keeping the results separate distinguishes the finite-range RG input from the standard free-field reconstruction and makes the exact blocking claim independently testable.

## 6. Conclusion

Positive finite-range covariance pieces yield an exact Markov blocking step. Its bounded-observable defect has finite range, and its Weyl-observable defect is summable in a natural covariance seminorm. For publication, the main comparison question is whether this interface-level formulation adds a useful theorem beyond existing treatments of finite-range Gaussian decompositions and free-field renormalization.

## References for the submission pass

- Brydges, D. C., Guadagni, G. and Mitter, P. K. (2004), “Finite range decomposition of Gaussian processes,” *Journal of Statistical Physics* **115**, 415–449. DOI: 10.1023/B:JOSS.0000019818.81237.66.
- Repository proof map: `notes/u1-gaussian-blocking-os-benchmark.md`, §§2–4.
