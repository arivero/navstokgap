#!/usr/bin/env python3
"""Build the GitHub Pages site into docs/.

Renders every note in notes/ to docs/notes/<slug>.html with MathJax, writes
the landing page, the paper index, the claim ledger and the source index,
and rewrites cross-references so that links to files outside docs/ point at
the repository on GitHub. PDFs are linked, never copied.

Usage: python3 scripts/build_site.py   (or: make site)
"""

import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT_NOTES = DOCS / "notes"
OUT_SOURCES = DOCS / "sources"
REPO = "https://github.com/arivero/navstokgap"
BLOB = f"{REPO}/blob/main"

# --------------------------------------------------------------------------
# Track definitions. Any note not listed here lands in "Further results".
# --------------------------------------------------------------------------

TRACKS = [
    ("planck-gap", "The Planck gap", """Newton reads a force off a trajectory by
     letting the sagitta and the enclosed area go to zero. Once the comparison
     must be <em>recorded</em>, it has a floor of order &#8463;. These notes
     carry the theorems, the Newton-age premises and the ancient dispute about
     the cut.""", [
        "planck-gap-paper", "mark-cost-and-statistical-floor",
        "planck-gap-derivation", "planck-gap-probabilistic",
        "newton-mark-floor", "newton-insertion-action",
        "principia-constant-force-action", "receding-centre-area-audit",
        "newton-NATP00385-audit", "cut-paradox-two-faces",
        "static-composition-classics", "ancient-cuts-provenance",
        "cone-time-refinement", "i003-double-limit-rigidity",
        "arrow-not-sling",
    ]),
    ("mass-gap", "The Yang&ndash;Mills mass gap for SU(3)", """The conjecture
     turned into a finite list of named theorems, with explicit dependence on
     the box size, the lattice spacing and the coupling. The strong side is
     proved; the weak side and the region between are where the work stands.""", [
        "mass-gap-position", "mass-gap-obligations-lattice",
        "mass-gap-conditional-theorem", "su3-constants",
        "strong-coupling-uniform-gap", "wilson-strong-coupling-explicit",
        "kogut-susskind-strong-coupling-explicit",
        "strong-coupling-threshold-explicit", "strong-coupling-target-box",
        "lattice-gap-upper-bounds", "polyakov-average-gap-bound",
        "weak-coupling-feshbach-reduction", "torus-valley-potential",
        "schur-error-ultraviolet", "finiteness-half-flowed-susceptibility",
        "flowed-bound-free-field", "three-dimensional-gap-one-function",
        "gapped-set-critical-coupling", "abelian-misses-the-box",
        "dobrushin-uniqueness-wilson", "lieb-robinson-kogut-susskind",
        "intermediate-region-finite-verification", "confinement-scale-bands",
        "what-would-unblock", "reasons-to-stop-as-research",
        "comparison-and-bridges", "millennium-problem-definitions",
    ]),
    ("renormalization", "Blocking, flow and the large-field obstruction", """What
     happens to a renormalization step on the lattice, why the obstruction is
     the large-field tail rather than the block size, and how much the weak side
     is short by.""", [
        "blocking-criterion-monotone", "blocking-step-obstruction",
        "small-field-step-gaussian", "small-field-step-decay-and-threshold",
        "flow-before-decimation", "flow-conjugation-truncation",
        "flow-instability-large-field", "flow-jacobian-truncation-error",
        "lattice-truncation-uniform", "typical-field-strength-window",
        "large-field-action-lower-bound", "large-field-entropy-count",
        "large-field-operator-inequality", "agmon-global-not-local",
        "agmon-ground-state-suppression", "magnetic-energy-identities",
        "ground-state-measure-transfer", "moment-hierarchy-upper-bounds",
    ]),
    ("gap-analogy", "Gaps that are solved, and what a gap costs", """Solved
     low-dimensional gaps, the spin-chain gaps, and the exact sense in which a
     positive action floor and a mass gap are the same kind of statement.""", [
        "low-dimensional-mass-gap", "action-floor-yang-mills-gap",
        "holography-lowest-dimensions", "interacting-ising-gap",
        "ising-foundational-value", "ising-hermitian-transfer",
        "finite-depth-spin-gap", "susceptibility-gap",
    ]),
    ("action-selection", "Does classical physics select an action scale?", """A
     map of the premises a selection principle must add and the counterexamples
     it must exclude. The short answer is that the tested classical classes
     permit action-valued observables arbitrarily close to zero.""", [
        "action-scale-obstructions", "action-unit-dimensional-selection",
        "action-scale-dilation", "relativistic-kepler-threshold",
        "composition-universality", "checkerboard-dynamics",
        "energy-depot-action-selection", "radiation-noise-action-selection",
        "topological-sector-action-selection", "stabilized-topology-action-scale",
        "spin-action-patching", "thermal-receiver-reliability",
        "passive-threshold-events", "mechanical-interference-action",
        "closed-orbit-force-action", "fixed-force-small-circles",
        "bound-orbit-action-observable", "bounded-acceleration-return",
        "reciprocal-coupling-normalization",
    ]),
    ("cuts", "Cuts, refinement and what survives insertion", """Insert a cut into
     a motion and eliminate it again: which data survive, and what a classical
     cut has to retain.""", [
        "cut-point-consistency", "classical-cut-state", "physical-cut-speed",
        "telegraph-return-bridge", "bridge-crossover",
        "classical-readout-refinement", "reachable-cut-composition",
        "finite-precision-cut", "three-body-cut-memory", "two-regulator-audit",
        "composition-crossover-gap-checks", "minimax-composition",
        "jacobi-kernels-distinguishability", "indistinguishable-phase-bound",
        "causal-force-information", "finite-horizon-minimax",
    ]),
    ("apparatus", "Apparatus, records and reconstruction", """Finite clocks,
     probes and pointers, with every preparation and record made explicit. The
     recurring outcome is that a canonical error product closes as the record
     precision improves, so no apparatus of this kind supplies a floor.""", [
        "conservative-harmonic-receiver", "autonomous-finite-readout",
        "full-pointer-recovery", "full-clock-phase-recovery",
        "two-position-recovery", "two-calibration-branches",
        "three-calibration-global-recovery", "fixed-coupling-calibration",
        "calibration-tolerance-recovery", "calibrated-canonical-ambiguity",
        "calibrated-displacement-ambiguity", "correlated-calibration-response",
        "single-calibration-fibres", "clock-position-local-recovery",
        "final-clock-momentum-recovery", "global-clock-speed-ambiguity",
        "hidden-clock-ambiguity", "energy-constrained-apparatus-ambiguity",
        "full-apparatus-preparation-ambiguity", "fixed-preparation-ambiguity",
        "position-preparation-ambiguity", "block-apparatus-composition",
        "shared-record-budget", "ordered-beam-preparation",
    ]),
    ("operational", "Excluding classical operational models", """What it takes to
     rule out a classical account of a quantum experiment, and which premises do
     the work.""", [
        "quantum-exclusion-premises", "classical-orientation-closure",
        "reversible-generator-constraints", "reversible-interaction-premise",
        "hamiltonian-finite-closure", "hamiltonian-moment-descent",
        "local-detector-coincidences", "shared-readiness-chsh",
        "shared-resource-events",
    ]),
]

HIGHLIGHTS = [
    ("planck-gap-paper",
     "A recorded trajectory has a floor of order &#8463;",
     "Every protocol of marks whose resolution and recoil obey "
     "&delta;&Delta; &ge; &kappa; needs &tau;&Delta;E &ge; 9z&sup2;&kappa; to "
     "tell free motion from forced. A momentum-transfer mark has "
     "&kappa; &ge; &#8463;/2 exactly, because its error operator and the "
     "impulse it delivers are canonically conjugate."),
    ("wilson-strong-coupling-explicit",
     "SU(3) is gapped at strong coupling, with an explicit threshold",
     "For the Wilson transfer matrix the gap is explicit for g&sup2; &ge; 176, "
     "and the Kogut&ndash;Susskind Hamiltonian is gapped for g&sup2; &ge; 388 "
     "uniformly in the volume."),
    ("mass-gap-obligations-lattice",
     "The conjecture is six named statements",
     "T1 finite-lattice gap, proved; T2 strong-coupling gap uniform in volume; "
     "T2&prime; no Coulomb phase; T3 the scaling limit; T4 existence with the "
     "axioms; S the small-volume corner. The conjecture is T2&prime; with T3, "
     "given T4."),
    ("action-unit-dimensional-selection",
     "A universal action floor needs a fixed action unit",
     "Two elementary criteria decide the recorded countertests before any "
     "calculation, and they identify k<sub>e</sub>/c = &alpha;&#8463; as the "
     "only mass-independent action unit classical electrodynamics admits."),
    ("action-scale-obstructions",
     "Classical mechanics permits action arbitrarily close to zero",
     "Across the tested classes, positive bounds appear only when the class "
     "supplies an excitation floor, a fluctuating reference or restricted "
     "measurement information. None of them is a universal quantum phase "
     "parameter."),
    ("arrow-not-sling",
     "Why the ancients argued about the arrow and not the sling",
     "Newton defines centripetal force with a stone whirled in a sling, and "
     "the ancient debate is almost entirely rectilinear. The two sit on "
     "different rungs of one ladder, and the second rung cannot be stated "
     "until straight-line motion is held to need no account. Part of a "
     "collection of 50 primary sources, Greek, Chinese, Sanskrit and Latin, "
     "each with a companion recording its dating and what is contested."),
    ("relativistic-kepler-threshold",
     "The relativistic Kepler problem has an excluded action infimum",
     "Regular bound orbits exist exactly for |L| &gt; k/c, a mass-independent "
     "threshold equal to &alpha;&#8463; for two elementary charges, and the "
     "Sommerfeld&ndash;Dirac collapse condition is the same inequality."),
]

CSS = """
:root{--bg:#fbfaf7;--fg:#22201c;--muted:#6b6459;--rule:#e2ddd2;--accent:#7a3b12;
--card:#fff;--code:#f2efe8}
@media(prefers-color-scheme:dark){:root{--bg:#16150f;--fg:#e9e4d9;--muted:#9c948a;
--rule:#332f26;--accent:#d99a5b;--card:#1e1c15;--code:#211f18}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);
font:17px/1.65 Charter,Georgia,"Iowan Old Style",serif}
.wrap{max-width:46rem;margin:0 auto;padding:0 1rem 5rem}
header.site{border-bottom:1px solid var(--rule);margin-bottom:2rem;
padding:1.6rem 0 1.1rem}
header.site a.home{color:var(--fg);text-decoration:none;font-weight:600;
letter-spacing:-.01em}
nav.site{margin-top:.5rem;font-size:.86rem;color:var(--muted)}
nav.site a{color:var(--muted);text-decoration:none;margin-right:1.1rem}
nav.site a:hover{color:var(--accent)}
h1{font-size:1.85rem;line-height:1.22;letter-spacing:-.015em;margin:.2rem 0 1rem}
h2{font-size:1.28rem;margin:2.6rem 0 .5rem;letter-spacing:-.01em}
h3{font-size:1.05rem;margin:1.8rem 0 .4rem}
a{color:var(--accent)}
p,li{overflow-wrap:break-word}
.lede{font-size:1.06rem;color:var(--muted)}
.track{border-top:1px solid var(--rule);padding-top:1.1rem;margin-top:2.4rem}
.track p.blurb{color:var(--muted);font-size:.95rem;margin:.1rem 0 1rem}
ul.notes{list-style:none;padding:0;margin:0}
ul.notes li{padding:.42rem 0;border-bottom:1px solid var(--rule)}
ul.notes li:last-child{border-bottom:0}
ul.notes a{text-decoration:none;font-weight:600}
ul.notes a:hover{text-decoration:underline}
ul.notes .pdf{float:right;font-size:.76rem;color:var(--muted);
text-decoration:none;font-weight:400;margin-left:.6rem}
ul.notes .pdf:hover{color:var(--accent)}
.hl{background:var(--card);border:1px solid var(--rule);border-radius:9px;
padding:.9rem 1.1rem;margin:.9rem 0}
.hl h3{margin:0 0 .3rem;font-size:1rem}
.hl h3 a{text-decoration:none}
.hl p{margin:0;font-size:.93rem;color:var(--muted)}
table{border-collapse:collapse;width:100%;font-size:.9rem;margin:1rem 0;
display:block;overflow-x:auto}
th,td{border-bottom:1px solid var(--rule);padding:.42rem .5rem;text-align:left;
vertical-align:top}
th{font-weight:600}
code{background:var(--code);padding:.08em .32em;border-radius:3px;
font:.87em/1.5 ui-monospace,SFMono-Regular,Menlo,monospace}
pre{background:var(--code);padding:.85rem 1rem;border-radius:7px;overflow-x:auto}
pre code{background:none;padding:0}
blockquote{margin:1rem 0;padding:.1rem 0 .1rem 1rem;
border-left:3px solid var(--rule);color:var(--muted)}
footer.site{border-top:1px solid var(--rule);margin-top:3.5rem;padding-top:1rem;
font-size:.83rem;color:var(--muted)}
footer.site p{margin:.5rem 0}
footer.site strong{color:var(--fg)}
.meta{font-size:.85rem;color:var(--muted);margin:-.5rem 0 1.5rem}
mjx-container{overflow-x:auto;overflow-y:hidden;max-width:100%}
@media(max-width:640px){body{font-size:16px}h1{font-size:1.5rem}
ul.notes .pdf{float:none;display:block;margin:.1rem 0 0}}
"""

MATHJAX = """<script>window.MathJax={tex:{inlineMath:[['$','$'],['\\\\(','\\\\)']],
displayMath:[['$$','$$'],['\\\\[','\\\\]']],tags:'none'},
options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};</script>
<script id="MathJax-script" async
src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>"""

NAV = """<header class="site"><div class="wrap">
<a class="home" href="{root}index.html">navstokgap</a>
<nav class="site">
<a href="{root}index.html">Results</a>
<a href="{root}papers.html">Papers</a>
<a href="{root}ledger.html">Claim ledger</a>
<a href="{root}sources.html">Sources</a>
<a href="%s">Repository</a>
<a href="%s/issues">Issues</a>
</nav></div></header>""" % (REPO, REPO)

FOOT = """<footer class="site"><div class="wrap">
<p><strong>Comments, corrections and questions are welcome as repository
issues.</strong> Open one at <a href="{repo}/issues">{repo}/issues</a>, or go
straight to <a href="{repo}/issues/new">a new issue</a>. Corrections to a
quoted source, a dating or a proof are especially wanted: every note names the
premises it uses, so a disputed premise can be pointed at directly.</p>
<p>Research repository <a href="{repo}">arivero/navstokgap</a>. Pages generated
by <code>scripts/build_site.py</code>; every note is also the Markdown source
in <code>notes/</code> and a typeset PDF in <code>out/papers/</code>. Notes are
working research, not peer-reviewed publications, and each states its own
status.</p>
</div></footer>""".replace("{repo}", REPO)


def page(title, body, root="", extra_meta=""):
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>{extra_meta}
<style>{CSS}</style>
{MATHJAX}
</head><body>
{NAV.format(root=root)}
<main class="wrap">
{body}
</main>
{FOOT}
</body></html>
"""


def note_title(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


SUP = str.maketrans("0123456789+-n", "\u2070\u00b9\u00b2\u00b3\u2074"
                    "\u2075\u2076\u2077\u2078\u2079\u207a\u207b\u207f")
SUB = str.maketrans("0123456789aeijnx", "\u2080\u2081\u2082\u2083\u2084"
                    "\u2085\u2086\u2087\u2088\u2089\u2090\u2091\u1d62"
                    "\u2c7c\u2099\u2093")
GREEK = {"hbar": "\u210f", "tau": "\u03c4", "Delta": "\u0394",
         "delta": "\u03b4", "kappa": "\u03ba", "epsilon": "\u03b5",
         "alpha": "\u03b1", "beta": "\u03b2", "gamma": "\u03b3",
         "lambda": "\u03bb", "mu": "\u03bc", "nu": "\u03bd", "pi": "\u03c0",
         "sigma": "\u03c3", "chi": "\u03c7", "phi": "\u03c6",
         "varphi": "\u03c6", "theta": "\u03b8", "Lambda": "\u039b",
         "Phi": "\u03a6", "Sigma": "\u03a3", "Omega": "\u03a9",
         "ell": "\u2113", "infty": "\u221e", "propto": "\u221d",
         "ge": " \u2265 ", "le": " \u2264 ", "neq": " \u2260 ",
         "to": " \u2192 ", "times": "\u00d7", "cdot": "\u00b7",
         "gtrsim": " \u2273 ", "in": " \u2208 ", "sim": "~", "pm": "\u00b1",
         "nabla": "\u2207", "partial": "\u2202", "sqrt": "\u221a",
         "mathbb": "", "mathcal": "", "operatorname": "", "text": "",
         "frac": "", "left": "", "right": "", "quad": " ", "qquad": " ",
         ",": " ", ";": " ", "!": "", "\\": " "}


FUNCS = {"log", "ln", "exp", "sin", "cos", "tan", "max", "min", "inf",
         "sup", "dim", "det", "tr", "lim", "arccos", "arcsin", "arctan",
         "deg", "Var", "Re", "Im"}


def _script(m, table):
    body = m.group(1) or m.group(2)
    try:
        return body.translate(table) if all(
            ord(c) in table for c in body) else body
    except Exception:
        return body


def strip_math(s):
    """Readable plain-text form of a title, for list entries and <title>."""
    s = re.sub(r"\$([^$]*)\$", lambda m: m.group(1), s)
    s = re.sub(r"\\([a-zA-Z]+|[,;!\\])",
               lambda m: GREEK.get(m.group(1),
                                   m.group(1) if m.group(1) in FUNCS else " "), s)
    s = re.sub(r"\^\{([^}]*)\}|\^(.)", lambda m: _script(m, SUP), s)
    s = re.sub(r"_\{([^}]*)\}|_(.)", lambda m: _script(m, SUB), s)
    s = s.replace("--", "\u2013").replace(">", " > ").replace("<", " < ")
    s = re.sub(r"[{}$^_]", "", s)
    s = s.replace("\u0394 E", "\u0394E")
    s = re.sub(r"\s+([,.;:)])", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


LINK = re.compile(r"\]\(([^)\s]+?)(#[^)\s]*)?\)")


def rewrite_links(md, slug_set, note_prefix=""):
    """Point note-to-note links at the built pages and everything else at GitHub.

    note_prefix is the path from the page being written to docs/notes/: empty
    for a page inside docs/notes/, "notes/" for a page at the docs/ root.
    """
    def sub(m):
        target, frag = m.group(1), m.group(2) or ""
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        if target.startswith("../"):
            rel = target[3:]
            if rel.startswith("notes/"):
                stem = Path(rel).stem
                if stem in slug_set:
                    return f"]({note_prefix}{stem}.html{frag})"
            return f"]({BLOB}/{rel})"
        stem = Path(target).stem
        if target.endswith(".md") and stem in slug_set:
            return f"]({note_prefix}{stem}.html{frag})"
        return f"]({BLOB}/notes/{target})"
    return LINK.sub(sub, md)


def pandoc(md_text):
    r = subprocess.run(
        ["pandoc", "--from=markdown+tex_math_dollars+pipe_tables",
         "--to=html5", "--mathjax"],
        input=md_text, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"pandoc failed: {r.stderr[:400]}")
    return r.stdout


def main():
    notes = sorted(ROOT.glob("notes/*.md"))
    slugs = {p.stem for p in notes}
    titles = {p.stem: note_title(p) for p in notes}
    pdfs = {p.stem for p in ROOT.glob("out/papers/*.pdf")}
    OUT_NOTES.mkdir(parents=True, exist_ok=True)

    # 1. One page per note.
    for p in notes:
        md = p.read_text(encoding="utf-8")
        md = md.split("\n", 1)[1] if md.startswith("# ") else md
        body = pandoc(rewrite_links(md, slugs))
        plain = strip_math(titles[p.stem])
        links = [f'<a href="{BLOB}/notes/{p.name}">Markdown source</a>']
        if p.stem in pdfs:
            links.append(f'<a href="{BLOB}/out/papers/{p.stem}.pdf">PDF</a>')
        head = (f"<h1>{pandoc(titles[p.stem]).strip()[3:-4]}</h1>"
                f'<p class="meta">{" &middot; ".join(links)}</p>')
        (OUT_NOTES / f"{p.stem}.html").write_text(
            page(plain, head + body, root="../"), encoding="utf-8")

    # 2. Landing page.
    used, parts = set(), []
    parts.append("<h1>A minimum action, and a mass gap</h1>")
    parts.append(
        '<p class="lede">A research repository on two questions that turn out '
        "to share a shape. Does anything in physics force a positive unit of "
        "action, and does SU(3) Yang&ndash;Mills in four dimensions have a mass "
        "gap? Every note below states its result first, keeps its constants "
        "explicit, and says which premises it uses.</p>"
        '<p class="lede">The <a href="sources.html">primary sources</a> are '
        "collected and annotated alongside the mathematics, from Newton's "
        "<em>Opticks</em> and Berkeley's <em>Analyst</em> to the "
        "Vai\u015be\u1e63ikas\u016btra, the Abhidharmako\u015babh\u0101\u1e63ya, "
        "the Tattv\u0101rthas\u016btra, the Mohist Canons and the Laozi. "
        "<strong>Comments and corrections go to "
        f'<a href="{REPO}/issues">the repository issues</a></strong>, which '
        "is the right place to dispute a dating, a reading or a proof.</p>")
    parts.append("<h2>Where to start</h2>")
    for slug, head, blurb in HIGHLIGHTS:
        parts.append(
            f'<div class="hl"><h3><a href="notes/{slug}.html">{head}</a></h3>'
            f"<p>{blurb}</p></div>")
    for key, name, blurb, members in TRACKS:
        rows = []
        for slug in members:
            if slug not in slugs:
                continue
            used.add(slug)
            pdf = (f'<a class="pdf" href="{BLOB}/out/papers/{slug}.pdf">PDF</a>'
                   if slug in pdfs else "")
            rows.append(f'<li>{pdf}<a href="notes/{slug}.html">'
                        f"{html.escape(strip_math(titles[slug]))}</a></li>")
        parts.append(f'<section class="track" id="{key}"><h2>{name}</h2>'
                     f'<p class="blurb">{" ".join(blurb.split())}</p>'
                     f'<ul class="notes">{"".join(rows)}</ul></section>')
    rest = sorted(slugs - used)
    if rest:
        rows = []
        for slug in rest:
            pdf = (f'<a class="pdf" href="{BLOB}/out/papers/{slug}.pdf">PDF</a>'
                   if slug in pdfs else "")
            rows.append(f'<li>{pdf}<a href="notes/{slug}.html">'
                        f"{html.escape(strip_math(titles[slug]))}</a></li>")
        parts.append('<section class="track" id="further"><h2>Further results'
                     '</h2><p class="blurb">Notes outside the tracks above.</p>'
                     f'<ul class="notes">{"".join(rows)}</ul></section>')
    (DOCS / "index.html").write_text(
        page("navstokgap — a minimum action, and a mass gap", "".join(parts)),
        encoding="utf-8")

    # 3. Paper index.
    rows = []
    for slug in sorted(pdfs):
        t = html.escape(strip_math(titles.get(slug, slug)))
        note = (f'<a href="notes/{slug}.html">note</a>' if slug in slugs
                else "&mdash;")
        rows.append(f'<tr><td><a href="{BLOB}/out/papers/{slug}.pdf">{t}</a>'
                    f"</td><td>{note}</td></tr>")
    (DOCS / "papers.html").write_text(page(
        "Papers — navstokgap",
        f"<h1>Typeset papers</h1><p class=\"lede\">Every note is also built as "
        f"a PDF by <code>make paper NOTE=&lt;slug&gt;</code>. These {len(pdfs)} "
        f"files live in <code>out/papers/</code> in the repository and open "
        f"there.</p><table><thead><tr><th>Paper</th><th>Web</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"), encoding="utf-8")

    # 4. Claim ledger and source index.
    led = (ROOT / "claims/LEDGER.md").read_text(encoding="utf-8")
    led = led.split("\n", 1)[1] if led.startswith("# ") else led
    (DOCS / "ledger.html").write_text(page(
        "Claim ledger — navstokgap",
        "<h1>Claim ledger</h1>" + pandoc(rewrite_links(led, slugs, "notes/"))),
        encoding="utf-8")

    # 5. One page per source companion, then the source index.
    OUT_SOURCES.mkdir(parents=True, exist_ok=True)
    comps = sorted(q for q in (DOCS / "classics").glob("*.md")
                   if q.name != "README.md")
    comp_stems = {q.stem for q in comps}

    def src_links(md):
        """Inside a companion: classics files are served, notes are built."""
        def sub(m):
            target, frag = m.group(1), m.group(2) or ""
            if target.startswith(("http://", "https://", "mailto:", "#")):
                return m.group(0)
            if target.startswith("../../"):
                rel = target[6:]
                if rel.startswith("notes/"):
                    return f"](../notes/{Path(rel).stem}.html{frag})"
                return f"]({BLOB}/{rel})"
            if target.startswith("../"):
                rel = target[3:]
                if rel.startswith("notes/"):
                    return f"](../notes/{Path(rel).stem}.html{frag})"
                return f"]({BLOB}/{rel})"
            stem = Path(target).stem
            if target.endswith(".md") and stem in comp_stems:
                return f"]({stem}.html{frag})"
            return f"](../classics/{target}{frag})"
        return LINK.sub(sub, md)

    for q in comps:
        md = q.read_text(encoding="utf-8")
        title = next((l[2:].strip() for l in md.splitlines()
                      if l.startswith("# ")), q.stem)
        md = md.split("\n", 1)[1] if md.startswith("# ") else md
        head = (f"<h1>{pandoc(title).strip()[3:-4]}</h1>"
                f'<p class="meta"><a href="{BLOB}/docs/classics/{q.name}">'
                f"Companion source</a></p>")
        (OUT_SOURCES / f"{q.stem}.html").write_text(
            page(strip_math(title), head + pandoc(src_links(md)), root="../"),
            encoding="utf-8")

    src = (ROOT / "docs/classics/README.md").read_text(encoding="utf-8")
    src = src.split("\n", 1)[1] if src.startswith("# ") else src

    def idx_links(m):
        target, frag = m.group(1), m.group(2) or ""
        if target.startswith(("http", "#")):
            return m.group(0)
        if target.startswith("../"):
            rel = target[3:]
            if rel.startswith("notes/"):
                return f"](notes/{Path(rel).stem}.html{frag})"
            return f"]({BLOB}/{rel})"
        stem = Path(target).stem
        if target.endswith(".md") and stem in comp_stems:
            return f"](sources/{stem}.html{frag})"
        return f"]({BLOB}/docs/classics/{target}{frag})"

    src = LINK.sub(idx_links, src)
    (DOCS / "sources.html").write_text(page(
        "Sources \u2014 navstokgap",
        "<h1>Primary sources</h1><p class=\"lede\">Pre-1901 originals and "
        "lawful transcriptions, each with a companion recording route, "
        "metadata, extraction, rights, passage anchors and reading coverage. "
        f"The {len(comps)} companions are readable here; each links to the "
        "stored text, whose byte identity is registered in "
        "<code>docs/SHA256SUMS</code>. Companions state what a source "
        "supplies to the research and where its dating or attribution is "
        "contested.</p>"
        + pandoc(src)), encoding="utf-8")

    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    # Declare every generated file, so that check_repository.py can skip them
    # while keeping the source-companion and checksum rules for real sources.
    generated = sorted(
        p.relative_to(ROOT).as_posix()
        for p in [DOCS / "index.html", DOCS / "papers.html",
                  DOCS / "ledger.html", DOCS / "sources.html",
                  DOCS / ".nojekyll"] + list(OUT_NOTES.glob("*.html"))
                  + list(OUT_SOURCES.glob("*.html")))
    (DOCS / ".site-manifest").write_text(
        "# Generated by scripts/build_site.py; not retrieved sources.\n"
        + "\n".join(generated) + "\n", encoding="utf-8")

    stale = [q for q in OUT_NOTES.glob("*.html") if q.stem not in slugs]
    for q in stale:
        q.unlink()

    print(f"site: {len(notes)} notes, {len(comps)} sources, {len(pdfs)} papers, "
          f"{len(TRACKS)} tracks, {len(rest)} unfiled, "
          f"{len(stale)} stale removed -> docs/")


if __name__ == "__main__":
    sys.exit(main())
