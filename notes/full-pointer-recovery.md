# Full pointer records recover receiver and unknown probe positions

Eight final pointer coordinates determine both the receiver initial state and
four unknown incoming probe positions, uniformly on a fixed preparation box,
for R06's apparatus at sufficiently small fixed positive coupling. Initial
clock position and momentum and incoming probe momenta are supplied exactly.
The preparation box need not contract. Improving final record precision then
closes the canonical reconstruction-error product.

R19, 2026-09-11. The result concerns delayed deterministic reconstruction with
known Hamiltonian and simultaneous classical access to final positions and
momenta at the specified time T. The record-access premise is supplied, not
implemented by a further measuring apparatus. Proof and literature status are
recorded separately in the ledger and [B50](../references/batches/B50.md).

## 1. Fixed domain and observed quantities

Use [R06](autonomous-finite-readout.md)'s Hamiltonian, fixed masses, cutoffs,
pulses, positive E,T and invertible signal matrix. Work in its fixed component
units with sup norms; z=(x,P,y,Q) is the canonical receiver state. Take a
compact convex receiver neighbourhood Z containing the energy ball and lying
inside the chosen cutoff margins. Restrict physical initial receiver states
to S={H_s=E}. Let q be the four unknown initial probe positions in a fixed
box Q_b=[-b,b]^4 with b>0 sufficiently small, independent of lambda.

The revealed data are c=(s(0),p_s(0)) in a sufficiently small fixed compact
box about (s_0,M_c v), and u=(pi_j(0)) in a fixed small box. At zero coupling
write s_c(t)=s(0)+p_s(0)t/M_c and q_j^0(t)=q_j+t u_j/M_j.
Choose these boxes so that all free paths have strict cutoff and pulse-endpoint
margins. These margins persist for sufficiently small coupling. Define

$$A_{c,j\cdot}=K\int_0^T f_j(s_c(t))e_x\Phi_t\,dt.$$

Continuity and invertibility at the nominal clock give a uniform alpha>0
with ||A_c v||>=alpha||v|| throughout the chosen clock box. All matrix
formulas below are conjugated by the fixed component units. In physical units
A_c z is momentum. Known free pointer drift is d_j(u)=T u_j/M_j.

Observe pi(T) and q(T) at the same known T, and set

$$F_{\lambda,c,u}(z,q)=\left(\frac{\pi(T)-u}{\lambda},\ q(T)-d(u)\right).$$

Only z and q are unknown. Comparisons always hold the revealed c,u fixed;
constants are uniform over their boxes. Positions are time-stamped records,
whereas the post-pulse momenta are persistent records.

## 2. Uniform derivative estimate including clock reaction

On Z times Q_b, uniformly also in c,u, the exact smooth finite-time flow gives

$$F_{\lambda,c,u}(z,q)=L_c(z,q)+R_{\lambda,c,u}(z,q),\qquad
 L_c(z,q)=(-A_c z,q),\qquad ||R_{\lambda,c,u}||_{C^1}\le C\lambda. \tag{1}$$

Here is the order argument. At lambda=0 the receiver is Phi_t z, the clock
is s_c(t), and the probes follow q^0(t),u. Their coordinates and all initial
data derivatives are bounded on the compact domain. The interaction forces
are lambda times bounded smooth functions. Variation of constants and the
variational equations therefore bound the differences between the coupled
and free trajectories by O(lambda) in C^1 with respect to (z,q), uniformly
on [0,T]. Clock reaction is included at this order, since its force is
-lambda K sum f'_j(s)x q_j. No shrinking preparation is used.

In the linear cutoff regions the exact integrated equations are

$$\pi_j(T)-u_j=-\lambda K\int_0^T f_j(s(t))x(t)\,dt,$$
$$q_j(T)-q_j-d_j(u)=-\frac{\lambda K}{M_j}
 \int_0^T(T-t)f_j(s(t))x(t)\,dt.$$

Substitution of the free receiver and clock gives the first block
-A_c z+O(lambda) after division by lambda, and the second block q+O(lambda),
both in C^1. Smoothness, compactness and strict margins justify the uniform
variational estimates on the convex neighbourhood, not just on the shell.
The first unscaled remainder is O(lambda squared); R16's nominal order-three
remainder is neither needed nor asserted for this fixed box.

## 3. A global inverse estimate on the preparation domain

Put beta=min(alpha,1)>0. Integrate D R along the segment joining any
v=(z,q), w=(z',q') in Z times Q_b. Equation (1) gives

$$||F(v)-F(w)||\ge(\beta-C\lambda)||v-w||
 \ge\tfrac12\beta||v-w|| \tag{2}$$

for 0<lambda<=lambda_0 with C lambda_0<=beta/2. This is a uniform global
lower Lipschitz estimate on the stated domain. In particular the exact eight
records uniquely determine z and q on S times Q_b. A rank test at isolated
points would not supply the segment bound. The scale 1/lambda in F is an
information normalization; it amplifies momentum readout error.

This removes R18's exact position-compensation fibre upon addition of the
final positions and known clock data. R18's special invertible position-response
matrix is unnecessary: every fixed R06 signal design with invertible A and
these margins admits this small-coupling argument.

## 4. Record error, action units and fixed-box limit

Let final position and momentum record errors have dimensionless sup bounds
rho_q and rho_pi. After the known subtraction and scaling, their joint bound
is delta=max(rho_pi/lambda,rho_q). Choose a minimum-residual fit to F on the
compact set S times Q_b. The true state has residual at most delta, so the
fitted and true exact records differ by at most 2 delta. Equation (2) yields

$$||\widehat z-z||\le ||(\widehat z,\widehat q)-(z,q)||
 \le4\delta/\beta.$$

For fixed canonical units L_*,P_*, define worst initial-coordinate errors
epsilon_x=sup|xhat-x| and epsilon_P=sup|Phat-P| over the admitted states,
revealed data and bounded record errors. Then

$$0\le\mathcal H_{\rm rec}=\epsilon_x\epsilon_P
 \le\frac{16L_*P_*}{\beta^2}
       \max(\rho_\pi/\lambda,\rho_q)^2. \tag{3}$$

The product has action units ML^2/T, with no 2 pi normalization. At fixed
0<lambda<=lambda_0, all apparatus masses, pulse geometry, observation time
and the positive preparation widths stay fixed as rho_pi,rho_q tend to zero;
the product tends uniformly to zero. With exact records both risks are zero.
R06's disturbance remains bounded on this class, so epsilon_x times the
canonical momentum disturbance also tends to zero in this fixed-coupling
record limit. Receiver disturbance itself need not vanish.

Equation (3) also supplies convergence for joint limits with
rho_pi/lambda tending to zero and rho_q tending to zero. It is a sufficient
upper bound, not a sharp minimax formula for positive record errors. A
positive preparation volume alone cannot supply a positive reconstruction
floor under this enlarged record access. Exact initial clock/momentum access
and arbitrarily precise final joint access remain explicit resources.

## 5. Source connection and next test

The B49 Hermann–Krener capsule distinguishes local observability from global
recovery. Borrow its observation-map viewpoint; the decisive extra input here
is C^1 closeness to one invertible linear map on a convex domain. B47's
smooth-flow precedent supplies the variational-equation route. The matrix
and uniform domain estimate above are model derivations.

R20 should retain the eight exact final pointer records and known incoming
probe momenta, but stop revealing initial clock position and momentum. Test
whether unknown clock data can be compensated by receiver and probe-position
changes while staying on the exact receiver energy shell and inside fixed
preparation margins. An explicit common-record family or a uniform recovery
bound should decide the question; dimension counting alone is insufficient.
