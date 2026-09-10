# Two position records recover the phase state

Two bounded-error position records give a causal momentum estimate with exact
worst-case error for this estimator. Improving precision with a suitable sample
separation recovers both coordinates, strengthening R09's area-only closure.

R10, 2026-09-10. C076–C077 accepted by
[written review](../reviews/two-record-B41.md). [B41](../references/batches/B41.md)
identifies the finite-difference bound and optimum as established results:
Seeber–Haimovich, Lemma 4.3 and Theorem 4.1, with $N=\varepsilon$, $L=F/m$.
The model retains fixed $m,F,T>0$, known initial
$(q_0,p_0)$, and all measurable forces $|f|\le F$. Records are non-disturbing
and available by prediction time $T$; their timing and precision are protocol
inputs. The estimates concern deterministic errors, with no probability law.

## 1. Exact compatible-state propagation

Let $t_2=T-b$, $t_1=t_2-\delta\ge0$, with $\delta>0$ and $b\ge0$.
The two records are $y_i=q(t_i)+e_i$, $|e_i|\le\varepsilon_i$.
Let $H_i=\{(q,p):|q-y_i|\le\varepsilon_i\}$. With the shear $S_t$ and
force lens $K_t$ of [R08](reachable-cut-composition.md), the exact sets are

$$C_1=(S_{t_1}\{(q_0,p_0)\}+K_{t_1})\cap H_1,\qquad
C_2=(S_\delta C_1+K_\delta)\cap H_2,\qquad
E_T=S_bC_2+K_b.$$

An empty set rejects inconsistent records. Each intersection retains all and
only record-compatible states; unrestricted concatenation of bounded segment
forces proves each propagation equality. This preserves position–momentum
correlations and uses only two records, however small their separation.

## 2. A causal estimator and its exact worst-case errors

Define

$$\widehat p=\frac{m(y_2-y_1)}\delta,\qquad
\widehat q_T=y_2+\frac b m\widehat p,\qquad
B=\frac{m(\varepsilon_1+\varepsilon_2)}\delta+\frac{F\delta}2.$$

Integration of momentum backwards from $t_2$ gives

$$p(t_2)-\frac{m[q(t_2)-q(t_1)]}\delta
=\frac1\delta\int_{t_1}^{t_2}(s-t_1)f(s)ds.$$

The weight integrates to $\delta^2/2$. Consequently every compatible motion
satisfies

$$|p(T)-\widehat p|\le R_p:=B+Fb,\qquad
|q(T)-\widehat q_T|\le R_q:=\varepsilon_2+\frac b m B+\frac{Fb^2}{2m}.$$

The second bound uses $q(T)=q(t_2)+bp(t_2)/m+
m^{-1}\int_{t_2}^T(T-s)f(s)ds$. Both errors are simultaneously attained
by $f=F$ on the two final intervals, $e_1=+\varepsilon_1$ and
$e_2=-\varepsilon_2$. Any allowed earlier input joins this example to the
fixed initial state. Thus these are the exact worst-case errors of the stated
estimator over all allowed records and motions. They are upper bounds for the
best possible estimator; extra initial-state information may improve them.

Every conditional terminal set lies in the rectangle of half-widths $R_q,R_p$
about $(\widehat q_T,\widehat p)$. It has coordinate diameters at most
$2R_q,2R_p$, canonical area at most $4R_qR_p$, and an error product $R_qR_p$
in action units. The area bound is an outer approximation, not an exact area.

## 3. Precision, separation and delay

At fixed $m,F,T$, the sufficient conditions

$$\delta\to0,\qquad
\frac{\varepsilon_1+\varepsilon_2}{\delta}\to0,\qquad b\to0$$

give $R_p,R_q\to0$, uniformly over the force class and errors. The records
approach the terminal time while their accuracy improves faster than their
separation. Unlike one position strip, the joint set now shrinks in both
coordinates. No proliferation of probes is assumed in this information model.

For equal errors $\varepsilon>0$, minimizing $B$ over available separations
gives

$$\delta_*=2\sqrt{\frac{m\varepsilon}{F}},\qquad
B_*=2\sqrt{mF\varepsilon},$$

provided $\delta_*\le T-b$. This follows from equality of the two positive
terms in $2m\varepsilon/\delta+F\delta/2$. If that separation is unavailable,
the minimization must use the allowed timing range. At $b=0$ the corresponding
error product is

$$R_qR_p=2\sqrt{mF}\,\varepsilon^{3/2}\longrightarrow0.$$

For a genuinely delayed sequence, taking $b=\delta_*$ gives
$R_p=4\sqrt{mF\varepsilon}$, $R_q=7\varepsilon$, and product
$28\sqrt{mF}\varepsilon^{3/2}$; $t_1=T-2\delta_*\ge0$ for sufficiently
small $\varepsilon$. This supplies positive delay at every finite stage.
All constants above follow by substitution into the written bounds.

## 4. Premise exposed by the calculation

The force ceiling controls the bias from unresolved acceleration. Record
precision controls the amplified position errors. Their optimized balance
is a preparation/protocol scale, with mass and force dependence, closing as
precision improves. To derive a fundamental positive action constant, the
next test must supply a physically justified restriction on attainable
precision and timing and then establish a lower bound for every estimator.

R11 should first settle the lower-bound half inside this model: construct
two bounded-force trajectories with identical allowed records and shared
initial state. Compare their terminal momentum separation with R10's upper
bound. The resulting minimax benchmark will distinguish an unavoidable
information loss at fixed precision from merely a chosen estimator's error.
