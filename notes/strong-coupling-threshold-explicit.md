# The strong-coupling threshold made explicit: Yarotsky's proof gives $g_0^2\sim10^{100}$, and only a direct expansion can give $g_0^2\sim10^2$

The T2 theorem of this programme
([T2 note](strong-coupling-uniform-gap.md)) has an existential threshold
$\beta\le\beta_*(3,\{0,1\}^3)$, with $\beta=54/g^4$ for $SU(3)$. Following
the proof of Yarotsky's Theorem 1 with numbers, the threshold it
supplies is
$$\beta_*\ \simeq\ e^{-465},\qquad g_0^2=\sqrt{54/\beta_*}\ \simeq\ 10^{101},$$
because the time-discretized cluster expansion pays a factor
$e^{t_0|\Lambda_0|^2}=e^{64t_0}$ per excited site (Lemma 3 of the paper),
and the classical decay $e^{-t_0}$ per unexcited site-time must beat a
polymer entropy of order $220$ per site, forcing $t_0\ge7$. The
strong-coupling region that the theorem covers, made explicit, is
therefore empty for every practical purpose, and **the strong-coupling
boundary of the intermediate region must be obtained from a direct
expansion**, of the Kirkwood--Thomas or Datta--Kennedy type for the
Hamiltonian or of the Osterwalder--Seiler character type for the
Euclidean measure, whose explicit radii are of order
$\beta\lesssim10^{-2}$, that is $g_0^2\sim10^2$ for $SU(3)$. The width of
the intermediate region in one-loop doublings is then set by the
constants on both sides: about $10^3$ with the crude constants now in
hand ($1/g^2\gtrsim10^2$ on the weak side, $g^2\gtrsim10^2$ on the
strong side), and about $20$ if both sides are pushed to $g^2\sim1/2$
and $g^2\sim70$. Constants explicit; nothing promoted.

## 1. The chain of conditions in the proof

Yarotsky's expansion (Commun. Math. Phys. 261 (2006) 799, Section 2;
passage level, from the copy on file) writes
$e^{-t_0H}=\sum_IT_{\Lambda,I}$, isolates the regions $I$ where the
perturbation acts and the regions $J$ where classical excitations
propagate, and bounds a configuration
$C=\{(I_k,J_k)\}_{k=1}^N$ by
$$|w(C)|\le\prod_{k=1}^N\big(2\alpha e^{t_0\beta/\alpha}\big)^{|I_k|}\,e^{-t_0(|J_k|-|\Lambda_0|^2|I_k|)}$$
(Lemma 1 for the first factor, via a many-variable Schwarz lemma; Lemma
3 for the second, where the paper's displayed $|\Lambda_0|^3$ is
weakened from the $|\Lambda_0|^2$ its proof establishes). The expansion
is then a polymer gas on the space-time lattice
$\{1,\dots,N\}\times\Lambda$, and Theorem 1 follows from "choose $t_0$
large and then $\alpha,\beta$ small so that $w(\chi)\le\epsilon^{|\operatorname{supp}\chi|}$"
together with a bound $c^n$ on the number of polymers of support $n$
through a point.

For a **bounded** perturbation, $|\phi_x(v,v)|\le\beta_0\|v\|^2$, condition
(2) holds with every $\alpha>0$, so $\alpha$ is free and the activity
per site of $I$ is
$$\min_{\alpha>0}2\alpha e^{t_0\beta_0/\alpha}=2e\,t_0\beta_0\qquad(\alpha=t_0\beta_0),$$
so the choice $\alpha=0$ made in the T2 note is legitimate for the
hypothesis of the theorem and is replaced by $\alpha=t_0\beta_0$ inside
the proof.

## 2. The numbers

*Entropy.* Two sites of $\mathbb Z^3$ have overlapping ranges
$\Lambda_0+x$, $\Lambda_0+y$ exactly when $y-x\in\{-1,0,1\}^3$, so the
connectivity graph of the polymer gas has degree
$d\le3\cdot27-1=80$ (space and the two time neighbours), and the number
of connected supports of size $n$ through a point is at most
$(ed)^n$, giving $c\le e\cdot80\simeq220$.

*Convergence.* The Kotecký--Preiss criterion (Commun. Math. Phys. 103
(1986) 491; metadata level) with $a(\chi)=|\operatorname{supp}\chi|$ is
implied by $\sum_{n\ge1}(ce\rho)^n\le1$, where $\rho$ is the largest
per-site activity, so it suffices that
$$\rho\ \le\ \frac1{2ec}\ \simeq\ 8\times10^{-4}.$$

*The classical sites.* $\rho_J=e^{-t_0}\le8\times10^{-4}$ forces
$t_0\ge7.1$.

*The perturbed sites.* Each site of $I$ carries
$2e\,t_0\beta_0\cdot e^{|\Lambda_0|^2t_0}=2e\,t_0\beta_0\,e^{64t_0}$, and
with $t_0=7.1$,
$$\beta_0\ \le\ \frac{8\times10^{-4}}{2e\cdot7.1}\,e^{-454}\ \simeq\ e^{-465}.$$

*The threshold.* $\beta_*\simeq e^{-465}$, so for $SU(3)$
$$g_0^4=\frac{54}{\beta_*}\simeq54\,e^{465},\qquad g_0^2\simeq7.3\times e^{232}\simeq10^{101}.$$

Refinements inside the same proof, such as replacing the bound
$|J\cap(\Lambda\setminus\tilde I)|\ge|J|-|\Lambda_0|^2|I|$ by an exact
count of the sites shadowed by $I$, reduce $64$ to something of order
$10$ and $g_0^2$ to something of order $e^{40}$. The structure of the
argument, a time-discretized expansion in which every perturbed site
suppresses the classical decay over its whole range for a time $t_0$
that must itself be large, cannot bring the threshold near $g^2\sim10^2$.

## 3. What a direct expansion gives

Three families of explicit strong-coupling results exist, and each has
a radius of the form $\beta\lesssim1/(C\cdot\text{coordination})$ with
$C$ of order one:

- *Kirkwood--Thomas* (Commun. Math. Phys. 88 (1983) 569; metadata
  level): a Hamiltonian expansion for the ground state of a classical
  gapped operator plus a bounded perturbation, written directly in the
  operator, with no time discretization. For the Kogut--Susskind
  Hamiltonian the classical part is the electric term with local gap
  $\varepsilon_0=(g^2/2)C_2\,\hbar c/a$ and the perturbation is the
  plaquette sum, each plaquette touching four links and each link lying
  in twelve plaquettes.
- *Datta--Kennedy* (J. Stat. Phys. 108 (2002) 373; metadata level): the
  same structure with explicit control of the one-quasiparticle band,
  which is the object the gap lower bound needs.
- *Osterwalder--Seiler* (Ann. Phys. 110 (1978) 440; metadata level): the
  Euclidean character expansion of the Wilson measure, convergent for
  small $\beta_W=2N/g^2$, with the mass gap and clustering as
  consequences.

In each case the sufficient condition has the form
$$\frac{\|\text{plaquette term}\|}{\text{local gap}}\times(\text{coordination})\times C\ \le\ 1,$$
and with $\|\phi\|/\varepsilon_0=24N/(g^4C_2)=54/g^4$, coordination
$12$ and $C\simeq e$ this reads $g^4\gtrsim54\cdot12\cdot e\simeq1.8\times10^3$,
that is
$$g_0^2\ \sim\ 40\text{--}70\quad(SU(3)),$$
in line with the rough figure used earlier. A written derivation of the
Kirkwood--Thomas expansion for the Kogut--Susskind Hamiltonian with
these constants would replace the existential $\beta_*$ of T2 by a
number of this size; that derivation is the natural next step on the
strong-coupling side.

## 4. The width of the intermediate region

With $2b_0\log2=0.0966$ for $SU(3)$, the one-loop count of doublings
between the two boundaries is
$n=\big(1/g_{\rm weak}^2-1/g_{\rm strong}^2\big)/0.0966$:

| weak boundary | strong boundary | $n$ |
| --- | --- | --- |
| $1/g^2=10^2$ (crude window) | $g^2=10^{101}$ (Yarotsky explicit) | $\simeq10^3$ |
| $1/g^2=10^2$ | $g^2=70$ (direct expansion) | $\simeq10^3$ |
| $g^2=1/2$ | $g^2=70$ | $\simeq21$ |

The strong-side improvement from $10^{101}$ to $70$ changes $n$ by
less than one doubling, since $1/g^2$ is tiny at both; the width is set
almost entirely by the weak side, that is by how far the small-field
expansion can be pushed. The figure "about twenty doublings" quoted in
[the operator-inequality note](large-field-operator-inequality.md) §6
presupposes a weak side reaching $g^2\sim1/2$; with the crude constants
of that note the region is fifty times wider.

## 5. Consequence for STATE

The T2 theorem stands, and its threshold, made explicit from the proof
that supplies it, is $g_0^2\sim10^{101}$ for $SU(3)$, which covers nothing
of physical interest. The strong-coupling boundary of the intermediate
region has to be established by a direct expansion with explicit
constants, expected to give $g_0^2\sim40$--$70$; that derivation is
concrete, classical in method, and is the next step on the strong side.
The width of the intermediate region is controlled by the weak side,
and the relevant constant there is how far the small-field expansion
reaches in $1/g^2$.
