# R19 review: uniform recovery with known incoming clock data

C094–C095 are accepted as written model derivations in
[R19](../notes/full-pointer-recovery.md). One sequential Luna-low B50 audit
and coordinator source/proof review are complete; no numerical or symbolic
verification scripts were used.

1. Fix a compact convex neighbourhood of the receiver energy ball with strict
   trajectory cutoff margins, and small positive probe-position/momentum and
   clock boxes. Free clock shifts perturb the signal matrix continuously,
   preserving a uniform inverse margin. Comparisons use the same revealed
   clock data and incoming momenta, not different unobserved parameters.
2. With fixed preparation widths, receiver and clock reactions are O(lambda),
   including their initial-data derivatives. Smooth variational equations on
   the common compact trajectory domain justify the uniform C1 bounds. After
   subtracting known incoming momentum, integration gives an O(lambda squared)
   momentum remainder; division by lambda leaves O(lambda). Integrating once
   more gives q(T)-Tu/M=q+O(lambda). The nominal cubic remainder is not used.
3. The limiting block map (-A_c z,q) has lower norm margin min(alpha,1).
   Segment integration bounds the remainder difference on the convex domain;
   restricting the resulting global bound to the curved energy shell is valid.
   This establishes global injectivity, beyond a local rank condition.
4. Compact minimum-residual fitting exists. The true state is a competitor;
   twice the noise bound and twice the inverse margin give 4 delta/beta.
   Multiplication of separate canonical error upper bounds gives the factor
   16 in the action product. No simultaneous worst-case attainment is assumed.
5. Coupling stays positive and fixed while final errors shrink. Incoming
   positions keep positive width; incoming momenta and clock coordinates are
   revealed exactly. Joint final access at known T is an information premise,
   not a further Hamiltonian readout construction. The fixed-time disturbance
   is bounded, sufficient for the stated accuracy–disturbance closure.

[B50](../references/batches/B50.md) supports the smooth-dependence premise.
Coordinator verified Sideris metadata and the theorem/parameter passages in
text, and Corollary 6.1/Theorem 6.2's starting page visually. The standard
segment/residual argument and its apparatus hypotheses are proved here;
no exact external apparatus match or novelty conclusion follows from this
bounded reading. The next test varies hidden clock data, preserves the exact
energy shell, and checks interior preparation margins.
