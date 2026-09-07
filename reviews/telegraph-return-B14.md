# Review: telegraph return bridge (B14)

## Acceptance summary

The note is mathematically coherent as a fixed, density-disintegrated
telegraph preparation. Accept C033 and C034 as **derived consequences under
the stated model**, with the source status and endpoint qualifications below.
Do not promote the midpoint atom or polygon estimate to established prior art.

## Exact checks

- For `N_T=2k+1`, uniform ordered spacings give the beta density in note
  lines 44--49. At `A=T/2`, multiplying by the Poisson mass and `da/dx=1/(2u)`
  gives line 55; summation gives line 57 and the displayed `I_0` weights.
- The `k=0` bridge path has its switch at `T/2`, so its midpoint position is
  `uT/2`. For `k>=1`, reaching that endpoint requires simplex-boundary zero
  durations; hence the atom weight is `w_0=1/I_0(z)`. The right-continuous
  midpoint velocity on the `k=0` path is `-u`.
- On each partition interval, square completion gives the identity in lines
  123--126. At most `N_T` intervals contain interior switches and each costs
  at most `m u^2 |I|/2`, yielding lines 120--121. Differentiating `I_0`
  gives the count mean in lines 130--134.
- Pointwise evaluation on one sampled path proves the restriction statement in
  lines 102--106; no singular transition-density multiplication is required.

## Required wording safeguards

1. Keep “density disintegration/version” attached to conditioning on `X_T=0`.
   This is a zero-probability conditioning and is not fixed by Cinque.
2. Keep the endpoint-window experiment separate from the exact bridge. The
   one-switch window has the symmetric midpoint-velocity mixture because
   velocity evaluation is discontinuous at the jump; it is not a contradiction
   of the right-continuous convention.
3. Label Cinque as prior art for the finite-velocity process and occupation
   density only. Label the `I_0` bridge normalization, midpoint atom, reset
   countertest, and action bound as elementary/project-derived results.
4. Retain that the action/chord comparison matches position endpoints and does
   not match the bridge's velocity endpoints.

## Coverage and next task

Cinque pp. 1--4 were read, with pp. 3--4 visually checked. Two targeted web
searches found related bridge/occupation literature but no exact match for the
full velocity-resolved return bridge. The next bounded source/proof task is a
bounded-acceleration return model and its minimum-duration/action scaling.
