# Blowup for the Boussinesq equations with smooth forcing

> Source: [author-hosted PDF](https://cims.nyu.edu/~tristanb/boussinesq.pdf); [local PDF](AlpogeBuckmaster_Boussinesq_2026.pdf).
> Metadata: Levent Alpöge and Tristan Buckmaster; preprint, 76 pages, no arXiv identifier at retrieval.
> Extraction: `pdftotext -layout`; selective reading notes. Downloaded 2026-09-08 from the author's institutional page.

## Source digest

Cited result, Theorem 1.1 (PDF p. 3). For the fixed data (1.4) there are odd forces
$f_\theta\in C_c^\infty(\mathbb R^2\times\mathbb R)$,
$f_u\in C_c^\infty(\mathbb R^2\times\mathbb R;\mathbb R^2)$ and a time $T_*\in(0,\infty)$ such that the
forced inviscid Boussinesq system on $\mathbb R^2$ has, for every $T<T_*$, a unique smooth solution with
$\theta(\cdot,0)=\theta_{\rm in}$, $u(\cdot,0)=0$, and

$$\sup_{0\le t<T_*}\|\theta(t)\|_\infty<\infty,\qquad
\lim_{t\uparrow T_*}\|\nabla\theta(t)\|_\infty=\infty,\qquad
\limsup_{t\uparrow T_*}\|\omega(t)\|_\infty=\infty.$$

One fixed ball contains the supports of $\theta,u,\omega$ before blowup and of both forces for all time.
The forces alone extend through $T_*$, with every mixed space–time derivative.

The exact layer calculation is Lemma 3.1 (p. 8). On an affine background $u_{\rm old}=Dx$,
$\theta_{\rm old}=G\cdot x$ with $\operatorname{tr}D=0$, the added temperature and vorticity waves
$\vartheta=\Theta F(s)$, $\varpi=\Omega F'(s)$ with phase $s=\lambda\zeta\cdot x$ have vanishing residual
increments exactly when

$$\dot\zeta=-D^{T}\zeta,\qquad \dot\Theta=-\frac{J\zeta\cdot G}{\lambda|\zeta|^{2}}\,\Omega,\qquad
\dot\Omega=\lambda\zeta_1\Theta .$$

The wave does not advect itself, since $v\perp\zeta$ while both wave gradients are parallel to $\zeta$.
The amplitude $\Theta$ can stay small while $\lambda\Theta$, the gradient scale, grows; the next layer is
introduced at a still finer scale on the background this leaves. Sections 6 and 7 carry the finite local
correction equations and the mixed-derivative force estimates that keep the accumulated force smooth.

## Source-facing notes

Attribution, pp. 1 and 76: the authors assign primary intellectual credit for the strategy to Córdoba
and Martínez-Zoroa, with specific debts to the IPM construction [6] and to the Córdoba–Laín-Sanclemente–
Martínez-Zoroa Boussinesq construction [5], which used a force of finite Hölder regularity. The
advance recorded here is the passage from that rough force to $C^\infty$ in space and time.

AI-use statement, §2, p. 7: the first blowup solution was obtained with Claude on 2026-08-15 and Lean
verified on 2026-08-22. The authors describe the first machine-produced writeup as the worst they had
seen, and the released text as the result of weeks of hand iteration with Claude and Codex.
Acknowledgments, p. 76: NSF DMS-2243205 and DMS-2244879 and the Simons 'Wave Turbulence' grant for
T.B.; Anthropic support of the external academic collaboration for L.A.

The Lean artifact is described but not published with this PDF.

Review scope: title page, contents, §1.1–§1.2 pp. 1–5, Lemma 3.1 and §3.1–§3.2 pp. 8–9, §2 p. 7,
acknowledgments and references pp. 76. The estimates in §§4–10 are read for structure only; no proof
audit is claimed.
