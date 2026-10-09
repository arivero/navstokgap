# From classical free-motion composition to an operational quantum model: a conditional action-scale ladder

**Manuscript E — complete author-review draft for *Foundations of Physics* or a comparable foundations journal.** Author names, affiliations, correspondence details, and final venue are deliberately left for human approval. Result-specific literature review and specialist review remain required before submission.

## Abstract

Can classical mechanics determine a positive universal action scale and, with further premises, quantum mechanics? We give a theorem-by-theorem answer. Bare Hamiltonian mechanics admits deterministic point preparations and hence no positive action floor. If free motion is augmented by continuous stationary independent increments, mass-only universality, independent centre-of-mass composition, and nondegeneracy, the Lévy classification and a nonnegative Cauchy equation force a single constant \(\kappa>0\) with variance rate \(D(m)=\kappa/m\). Under force-independent noise, the same constant controls optimal discrimination of the inertial chord and Newtonian parabola in Galileo's comparison. A two-sided diffusion law and a mean-acceleration equation convert this stochastic model into a scalar Schrödinger equation with action parameter \(\kappa\). We then state a separate finite operational model: regular Weyl kinematics, normal positive states and effects, self-adjoint dynamics, completely positive instruments, and interacting composition yield the finite nonrelativistic quantum structure under explicit premises. The contribution is the separation and proof of these conditional implications, including the exact points where empirical calibration and noncommutative kinematics enter.

**Keywords:** foundations of quantum mechanics; classical stochastic mechanics; action scale; Galileo's comparison; Weyl relations; operational reconstruction.

## 1. Introduction

A foundations argument should say which ingredients select a physical structure. The chain from Newtonian mechanics to quantum mechanics is often presented as if an action constant, a diffusion equation, or an uncertainty relation already fixed the quantum theory. These implications are logically distinct. A stochastic variance rate can carry action units without selecting Weyl kinematics; a record floor can be realized in a commutative statistical model; a Weyl algebra yields uncertainty relations once its positive representation is supplied.

This paper organizes a specific conditional route in four stages. First, bare canonical mechanics is shown to admit a zero-action branch. Second, a stated stochastic augmentation plus centre-of-mass composition forces one positive universal action parameter. Third, further diffusion and dynamical premises give the scalar Schrödinger equation through the Madelung transformation. Fourth, an explicit finite operational model identifies additional assumptions sufficient for Weyl representations, Born probabilities, unitary dynamics, CP records, and composition.

The theorems are mathematical implications from named assumptions. The physical status of those assumptions is a separate question. The composition theorem derives the form and universality of \(\kappa\), while empirical calibration fixes its value; the operational reconstruction takes the Weyl multiplier as a kinematic premise. This distinction makes the conditional achievements and remaining physical questions precise.

## 2. The classical base and its zero branch

Consider a body on \(T^*\mathbb R^3\) with coordinates \((q,p)\), Poisson brackets \(\{q_i,p_j\}=\delta_{ij}\), and Hamiltonian
\[
H(q,p)=\frac{|p|^2}{2m}+V(q).
\tag{1}
\]
Let C0 consist of Hamilton's equations, Liouville evolution of probability measures, canonical composition of independent systems, and the availability of sharply prepared canonical pointers. The action integral \(\int p\,dq-H\,dt\) occurs in this theory, but no universal nonzero action unit is specified.

**Proposition 1 (C0 zero branch).** C0 has a model in which free bodies follow \(q_t=q_0+p_0t/m\), preparations are Dirac measures at arbitrary phase points, and the free variance rate is zero for every mass. Classical pointer readouts can be made arbitrarily sharp in canonical coordinates.

*Proof.* Hamiltonian free flow transports each Dirac measure to a Dirac measure and respects product composition. Canonical pointer transformations preserve phase volume while allowing arbitrarily concentrated retained readouts, with the conjugate range carried by an unobserved degree of freedom. Thus C0 has an explicit zero-variance, zero-floor realization. \(\square\)

This countermodel is a boundary theorem: any deduction of a positive constant needs an additional premise that excludes it.

## 3. A composition theorem for the action constant

Add the following conditions to C0.

- **C1 (continuous stationary independent free increments).** From a deterministic starting point, free fluctuations have continuous paths and stationary independent increments, with isotropic centred law.
- **C2 (mass-only universality).** The centred free law is defined for every real \(m>0\) and depends on no body attribute except mass.
- **C3 (independent centre-of-mass composition).** The centre of mass of independent bodies has the free centred law associated with their total mass.
- **C4 (nondegeneracy).** The centred free law is not deterministic for at least one mass.

C1 is a stochastic law supplementing Hamiltonian trajectories; C2–C3 state its composition rule; C4 excludes the deterministic solution.

**Theorem 2 (one universal positive action).** Under C1–C4, there exists a single \(\kappa>0\) such that the free process of mass \(m\) is Brownian with variance rate
\[
D(m)=\frac{\kappa}{m},\qquad [\kappa]=\text{action}.
\tag{2}
\]

*Proof.* A continuous process with stationary independent increments and finite isotropic variance is Brownian with drift and a nonnegative variance rate \(D(m)\). For independent masses \(m_1,m_2\), put \(M=m_1+m_2\). The centre-of-mass variance rate is
\[
\frac{m_1^2D(m_1)+m_2^2D(m_2)}{M^2}.
\]
C3 equates this to \(D(M)\). Therefore \(g(m)=m^2D(m)\) is additive on positive reals. Since \(g\ge0\), it is monotone; the nonnegative Cauchy equation implies \(g(m)=\kappa m\) for one \(\kappa\ge0\). C4 forces \(\kappa>0\), proving (2). Since \([D]=L^2/T\), \([mD]=ML^2/T\), the dimension of action. \(\square\)

Dropping C4 restores \(\kappa=0\). Thus positivity follows from a precisely located nondegeneracy condition rather than from dimensional analysis.

## 4. The Galileo comparison as a record benchmark

Assume additionally:

- **C5 (force-independent additive noise).** Under constant force, the trajectory is the Newtonian forced path plus the same Brownian noise as in (2).

For duration \(\tau\) and constant force \(F\), define the action scale
\[
K_\tau=\frac{F^2\tau^3}{24m}.
\tag{3}
\]
The inertial chord and force-driven parabola, pinned to common endpoints, differ by a Cameron–Martin shift.

**Theorem 3 (optimal Galileo discrimination).** Under C0–C5, the minimum equal-prior classification error for the two pinned path laws is
\[
P_{\rm err}=\Phi\!\left(-\sqrt{\frac{K_\tau}{2\kappa}}\right),
\tag{4}
\]
where \(\Phi\) is the standard normal distribution function. Error at most \(\epsilon<1/2\) requires
\[
K_\tau\ge2z_{1-\epsilon}^2\kappa.
\tag{5}
\]

*Proof.* The two Gaussian bridge laws have common covariance and Cameron–Martin squared distance \(2K_\tau/\kappa\). The equal-prior likelihood-ratio test between two Gaussian shifts has error \(\Phi(-d/2)\) when the squared Mahalanobis distance is \(d^2\). Substitution yields (4), and inversion gives (5). \(\square\)

The result identifies a scale in Newton's inertial-versus-parabolic comparison for this stochastic model. It is an operational consequence of C5, not a derivation of a Hilbert space.

## 5. From two-sided diffusion to the Schrödinger equation

Set \(\nu=\kappa/(2m)\). A Brownian motion of variance rate \(D=\kappa/m\) has generator \(\nu\Delta\). Add three further assumptions:

- **N1 (two-sided diffusion).** Forward and backward drifts exist with common diffusion coefficient \(\nu\), positive density \(\rho\), osmotic velocity \(u=\nu\nabla\log\rho\), and current velocity \(v=\nabla S/m\), with \(\partial_t\rho+\nabla\cdot(\rho v)=0\).
- **N2 (mean acceleration law).** The symmetric mean acceleration satisfies \(m a_{\rm mean}=-\nabla V\).
- **N3 (global phase compatibility).** The phase data define a single-valued wave function, or are specified in circulation sectors with compatible boundary conditions.

With \(\psi=\sqrt\rho\,e^{iS/\kappa}\), direct substitution shows that
\[
i\kappa\partial_t\psi=\left(-\frac{\kappa^2}{2m}\Delta+V\right)\psi
\tag{6}
\]
is equivalent, for sufficiently smooth positive \(\rho\), to the continuity equation and quantum Hamilton–Jacobi equation
\[
\partial_tS+\frac{|\nabla S|^2}{2m}+V
-\frac{\kappa^2}{2m}\frac{\Delta\sqrt\rho}{\sqrt\rho}=0.
\tag{7}
\]

For the standard two-sided diffusion convention, the mean acceleration is
\[
a_{\rm mean}=\partial_tv+(v\cdot\nabla)v-(u\cdot\nabla)u-\nu\Delta u.
\tag{8}
\]
Writing \(r=\sqrt\rho\) and differentiating \(u=2\nu\nabla\log r\) gives
\[
(u\cdot\nabla)u+\nu\Delta u
=2\nu^2\nabla\left(\frac{\Delta\sqrt\rho}{\sqrt\rho}\right).
\tag{9}
\]
Substitution into (8), with N2 and \(v=\nabla S/m\), yields the gradient of (7); a time-dependent additive constant in \(S\) removes the spatially constant remainder. Hence (6) follows with \(\hbar\) identified with \(\kappa\) at the level of the scalar dynamics.

This bridge needs N1–N3. Its mathematical content is the equivalence between the stated diffusion/mean-law system and (6), not a derivation of those dynamical and phase premises from C0–C5.

## 6. Empirical calibration

Theorem 2 selects a common positive action parameter but not its numerical value. A calibration premise is required to identify
\[
\kappa=\hbar=\frac{h_P}{2\pi}.
\tag{10}
\]
One conditional route relates a stochastic record constant to a stationary-oscillator action and then to Planck's measured constant. That route retains its own dynamical and all-readout assumptions. We therefore use (10) only as an explicit empirical calibration, separate from Theorem 2.

## 7. A finite operational quantum model

To state the target theory, let \((V,\sigma)\) be a finite-dimensional nondegenerate symplectic phase space. Introduce the following operational premises.

- **F0:** a positive calibrated action constant \(\hbar\) is supplied.
- **F1:** canonical translations have a regular irreducible Weyl representation with multiplier
  \[
  W(z)W(z')=e^{-i\sigma(z,z')/(2\hbar)}W(z+z'),\qquad W(z)^*=W(-z).
  \tag{11}
  \]
- **F2:** preparations are normal positive states and effects are operators \(0\le E\le1\), with probability given by state evaluation.
- **F3:** each admitted closed-system Hamiltonian is self-adjoint and generates \(\rho_t=e^{-itH/\hbar}\rho_0e^{itH/\hbar}\).
- **F4:** outcomes are normal completely positive trace-nonincreasing maps \(\mathcal I_r\), with \(\sum_r\mathcal I_r\) trace preserving; sequential records compose as maps on system plus retained memory.
- **F5:** independent systems compose by tensor product. For a connected interacting class, the measured mechanical total angular momentum \(L=\sum_i q_i\times p_i\) is required to obey one common closure law \([L_x,L_y]=i\hbar L_z\) on the full product algebra (equivalently, \(L/\hbar\) generates the same measured spatial rotation on each constituent).

The Weyl multiplier is associative because its bilinear phase satisfies the cocycle identity. The Stone–von Neumann theorem then gives, in finite canonical dimension, unitary equivalence of every regular irreducible representation to the Schrödinger representation
\[
(Q_j\psi)(q)=q_j\psi(q),\qquad(P_j\psi)(q)=-i\hbar\partial_{q_j}\psi(q).
\tag{12}
\]
F2 gives density-operator states and Born probabilities \(\Pr(E)=\operatorname{Tr}(\rho E)\). Positivity and \([Q_j,P_k]=i\hbar\delta_{jk}\) yield \(\Delta Q_j\Delta P_j\ge\hbar/2\). F3 gives unitary dynamics and the Schrödinger equation for pure states.

The common-constant clause in F5 has a direct algebraic check. If constituent factors initially carry constants \(\hbar_i\), then on their product algebra
\[
[L_x,L_y]=i\sum_i\hbar_iL_{iz}.
\]
F5 requires this to equal \(i\hbar\sum_iL_{iz}\). Linear independence of the canonical monomials \(q_{ix}p_{iy}\) across constituents forces \(\hbar_i=\hbar\) for each constituent in the connected class. The measured common rotation normalization is the physical composition premise; equality of the constants is its algebraic consequence.

For a concrete record example, a Gaussian position instrument with resolution \(s\) has Kraus density
\[
M_x=(2\pi s^2)^{-1/4}\exp[-(Q-x)^2/(4s^2)],\qquad \int M_x^*M_x\,dx=1.
\tag{13}
\]
Ignoring the outcome multiplies the position-space density matrix by \(e^{-(q-q')^2/(8s^2)}\), equivalently adding momentum variance \(\hbar^2/(4s^2)\). Thus
\[
\operatorname{Var}_{\Phi_s(\rho)}P-\operatorname{Var}_\rho P
=\frac{\hbar^2}{4s^2}.
\tag{14}
\]
The Gaussian model attains the corresponding imprecision-disturbance product. F4 supplies the closure and sequential composability of the instrument class; (13) is an explicit member of it.

**Theorem 4 (conditional finite operational reconstruction).** Under F0–F5, a finite-dimensional canonical system has the Schrödinger Weyl representation; normal states and effects obey the Born probability rule; admitted self-adjoint Hamiltonians generate unitary Schrödinger evolution; records compose as CP instruments; independent systems tensor; and a connected interacting class shares one \(\hbar\).

*Proof.* The Weyl part is Stone–von Neumann. The probability statement is normal-state duality for the represented operator algebra. Dynamics follows from F3 and Stone's theorem. CP record closure is F4, with the Gaussian instrument (13) as a worked example. Tensor composition is F5; the common normalization follows from the angular-momentum commutator argument above. Calibration to \(h_P/(2\pi)\) is F0. \(\square\)

Theorem 4 is a conditional reconstruction inside a finite nonrelativistic domain. The stochastic ladder contributes a candidate source for the action parameter; F1–F5 specify the further operational structure needed for the model.

## 8. Discussion: theorem boundaries and physical foundations

The chain proved here has explicit interfaces:
\[
\begin{array}{rcl}
\text{C0} &\Rightarrow& \text{deterministic zero branch is admissible},\\
\text{C0+C1--C4} &\Rightarrow& \kappa=mD(m)>0,\\
\text{C0+C1--C5} &\Rightarrow& \text{Galileo path-discrimination bound},\\
\text{previous+N1--N3} &\Rightarrow& \text{scalar Schrödinger dynamics with parameter }\kappa,\\
\text{empirical calibration} &\Rightarrow& \kappa=\hbar=h_P/(2\pi),\\
\text{F0--F5} &\Rightarrow& \text{finite operational quantum model}.
\end{array}
\tag{15}
\]
The first stochastic theorem is a theorem about a specified stochastic extension. The one-particle diffusion bridge supplies scalar wave dynamics under its named premises; arbitrary canonical Weyl kinematics and the CP instrument calculus enter as separate operational premises. The framework therefore presents a conditional architecture with visible assumptions, rather than a single undifferentiated “classical derivation.”

Three physical tasks follow. First, determine whether C1–C4 describe a justified free-motion law in a physical model. Second, justify calibration across the stochastic, record, and radiation sectors. Third, provide a physical principle for F1 and F4, which currently function as kinematic and operational premises. Each task can be assessed independently without altering the proved conditional implications.

## 9. Conclusion

A nondegenerate continuous stochastic law composed by mass-weighted centres of mass forces one positive universal action constant. With a specified force response it controls an optimal Galileo discrimination problem. Under additional two-sided diffusion and mean-acceleration premises it becomes the parameter in the scalar Schrödinger equation. Finally, an explicit set of finite operational assumptions reconstructs the usual Weyl, Born, unitary, CP-instrument, and composition structures. The value of the framework is its separation of these results: each mathematical implication has a visible premise boundary, and empirical calibration and quantum kinematics remain identifiable physical questions.

## References

- Davies, E. B. and Lewis, J. T. (1970). “An operational approach to quantum probability.” *Communications in Mathematical Physics* 17, 239–260. DOI: 10.1007/BF01647093.
- Demme, A. and Caticha, A. (2017). “The Classical Limit of Entropic Quantum Dynamics.” *AIP Conference Proceedings* 1853, 090001. DOI: 10.1063/1.4985370. The centre-of-mass covariance calculation is close prior art for the composition step; the present converse uses the nonnegative Cauchy equation.
- Hardy, L. (2001). “Quantum theory from five reasonable axioms.” arXiv:quant-ph/0101012. Compare as an axiomatic reconstruction programme with different primitives and objectives.
- Nelson, E. (1966). “Derivation of the Schrödinger Equation from Newtonian Mechanics.” *Physical Review* 150(4), 1079–1085. DOI: 10.1103/PhysRev.150.1079.
- Reed, M. and Simon, B. (1972). *Methods of Modern Mathematical Physics I: Functional Analysis*. Academic Press; see the Stone–von Neumann theorem for finite-dimensional canonical commutation relations.
- Kraus, K. (1983). *States, Effects, and Operations: Fundamental Notions of Quantum Theory*. Springer.
- Repository proof sources: `notes/classical-mechanics-to-h-ladder.md` and `notes/foundations-model-nonrelativistic-quantum-mechanics.md`.
