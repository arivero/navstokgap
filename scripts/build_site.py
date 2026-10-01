#!/usr/bin/env python3
"""Build the GitHub Pages site into docs/.

Renders every note in notes/ to docs/notes/<slug>.html with MathJax, writes
the landing page, the paper index, the claim ledger and the source index,
and rewrites cross-references so that links to files outside docs/ point at
the repository on GitHub. PDFs are linked, never copied.

Usage: python3 scripts/build_site.py   (or: make site)
"""

import datetime
import html
import json
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
<a href="{root}index.html">Research map</a>
<a href="{root}archive.html">Note archive</a>
<a href="{root}tutorial.html">Tutorial</a>
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
in <code>notes/</code>; selected manuscripts have a typeset PDF in
<code>out/papers/</code>. Notes are
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
        # GitHub retains a heading's initial section number; Pandoc's default
        # HTML identifier drops it. Preserve external/source fragments above.
        note_frag = re.sub(r"^#\d+-", "#", frag)
        if target.startswith("../"):
            rel = target[3:]
            if rel.startswith("notes/"):
                stem = Path(rel).stem
                if stem in slug_set:
                    return f"]({note_prefix}{stem}.html{note_frag})"
            return f"]({BLOB}/{rel})"
        stem = Path(target).stem
        if target.endswith(".md") and stem in slug_set:
            return f"]({note_prefix}{stem}.html{note_frag})"
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


def last_edited_date():
    """Date of the most recent git commit (YYYY-MM-DD); today's date if git fails."""
    try:
        r = subprocess.run(["git", "log", "-1", "--format=%cs"], cwd=ROOT,
                            capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except Exception:
        pass
    return datetime.date.today().isoformat()


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

    # 2. Curated research map; complete coverage belongs to the archive.
    home = (ROOT / "scripts/site/home.html").read_text(encoding="utf-8")
    (DOCS / "index.html").write_text(page(
        "navstokgap — what survives refinement?", home), encoding="utf-8")

    catalog = json.loads((ROOT / "research/note-index.json").read_text())["notes"]
    groups = {}
    for entry in catalog:
        groups.setdefault(entry["thematic_area"], []).append(entry)
    parts = ["<h1>Complete note archive</h1>",
             '<p class="lede">Every maintained scientific note appears once. '
             'Priority measures current retrieval importance, not proof quality '
             'or novelty. Source notes govern later corrections.</p>',
             '<p><a href="notes/index.html">Greppable catalog</a> · '
             '<a href="maps/dependencies.html">Dependency paths</a> · '
             '<a href="maps/obstructions.html">Obstruction map</a></p>',
             '<label for="note-search">Filter titles, summaries, keywords and status</label> '
             '<input id="note-search" type="search" style="width:100%;padding:.5rem" '
             'placeholder="e.g. covariance, moving saddle, obstruction">']
    for area, entries in sorted(groups.items()):
        parts.append(f'<section class="track"><h2>{html.escape(area)}</h2><ul class="notes">')
        for e in sorted(entries, key=lambda x: (-x["retrieval_priority"], x["path"])):
            slug = Path(e["path"]).stem
            correction = ""
            for rel in e["relations"]:
                if rel["type"] in {"is_superseded_by", "corrects", "supersedes"}:
                    target = Path(rel["target"]).stem
                    correction += (f' <a href="notes/{target}.html">'
                                   f'{html.escape(rel["type"].replace("_", " "))}: '
                                   f'{html.escape(target)}</a>.')
            pdf = (f'<a class="pdf" href="{BLOB}/out/papers/{slug}.pdf">PDF</a>'
                   if slug in pdfs else "")
            keys = html.escape("; ".join(e["keys"]))
            parts.append(f'<li data-note="{slug}" data-keys="{keys}">{pdf}'
                         f'<a href="notes/{slug}.html">{html.escape(strip_math(e["title"]))}</a>'
                         f'<p class="meta">Priority {e["retrieval_priority"]} · '
                         f'{html.escape(e["status"])} · {html.escape(e["proof_status"])}</p>'
                         f'<p>{html.escape(e["summary"])}{correction}</p>'
                         f'<p class="meta">Scope: {html.escape(e["limitations"])}</p></li>')
        parts.append('</ul></section>')
    parts.append(r"""<script>
const search = document.getElementById('note-search');
search.addEventListener('input', () => {
  const q = search.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  document.querySelectorAll('[data-note]').forEach(row => {
    const text = (row.textContent + ' ' + row.dataset.keys).toLocaleLowerCase();
    row.hidden = !q.every(word => text.includes(word));
  });
});
</script>""")
    (DOCS / "archive.html").write_text(page(
        "Complete note archive — navstokgap", "".join(parts)), encoding="utf-8")

    # Human-facing infrastructure maps; source notes are unchanged.
    out_maps = DOCS / "maps"
    out_maps.mkdir(parents=True, exist_ok=True)
    maps = ["dependencies", "book-map", "obstructions", "notation-and-scales",
            "refinement-correspondences", "programme-evolution", "site-audit",
            "synthesis-opportunities", "navigation-test", "pdf-audit"]
    for slug in maps:
        source = ROOT / "research" / f"{slug}.md"
        def map_link(m):
            target, frag = m.group(1), m.group(2) or ""
            if target.startswith(("http://", "https://", "mailto:", "#")):
                return m.group(0)
            resolved = (source.parent / target).resolve()
            try:
                rel = resolved.relative_to(ROOT)
            except ValueError:
                return f"]({BLOB}/{target}{frag})"
            if rel.parent == Path("notes"):
                return f"](../notes/{rel.stem}.html{frag})"
            if rel.parent == Path("research") and rel.stem in maps:
                return f"]({rel.stem}.html{frag})"
            return f"]({BLOB}/{rel.as_posix()}{frag})"
        title = note_title(source)
        body = pandoc(LINK.sub(map_link, source.read_text()))
        (out_maps / f"{slug}.html").write_text(
            page(strip_math(title), body, root="../"), encoding="utf-8")

    # 3. PDF manuscripts grouped by role, retaining every file.
    manuscripts = json.loads((ROOT / "research/pdf-catalog.json").read_text())["manuscripts"]
    parts = ["<h1>Manuscripts and PDFs</h1>",
             '<p class="lede">Major syntheses, technical notes, working drafts '
             'and historical snapshots have different roles. These are research '
             'manuscripts; a PDF does not imply peer-reviewed publication.</p>',
             '<p>Source notes govern current assumptions and corrections. '
             '<a href="maps/pdf-audit.html">Version and orphan audit</a> · '
             '<a href="archive.html">Complete note archive</a></p>']
    categories = ["current synthesis", "current technical manuscript", "working manuscript",
                  "older version", "historical research snapshot", "orphan manuscript"]
    for category in categories:
        entries = [e for e in manuscripts if e["classification"] == category]
        if not entries:
            continue
        parts.append(f'<h2>{html.escape(category.capitalize())}</h2><ul class="notes">')
        for e in sorted(entries, key=lambda x: x["slug"]):
            slug = e["slug"]
            note = (f' <a href="notes/{slug}.html">Current source note</a>.'
                    if slug in slugs else "")
            redirect = (f' <a href="notes/{e["current_replacement"]}.html">Later treatment</a>.'
                        if e.get("current_replacement") else "")
            parts.append(f'<li><a href="{BLOB}/out/papers/{slug}.pdf">'
                         f'{html.escape(strip_math(e["title"]))}</a>'
                         f' <a href="{BLOB}/{e["tex"]}">TeX source</a>.{note}{redirect}'
                         f'<p>{html.escape(e["assessment"])}</p></li>')
        parts.append('</ul>')
    (DOCS / "papers.html").write_text(page(
        "Manuscripts and PDFs — navstokgap", "".join(parts)), encoding="utf-8")

    # 4. Claim ledger and source index.
    led = (ROOT / "claims/LEDGER.md").read_text(encoding="utf-8")
    led = led.split("\n", 1)[1] if led.startswith("# ") else led
    (DOCS / "ledger.html").write_text(page(
        "Claim ledger — navstokgap",
        "<h1>Claim ledger</h1>"
        '<p class="lede">Stable older claim IDs, chiefly through September 16. '
        'Later results and corrections live in the source notes. Use the '
        '<a href="maps/dependencies.html">current dependency graph</a> and '
        '<a href="archive.html">catalog</a> to continue research. The '
        '<a href="notes/record-costs-disturbance.html">general disturbance bounds</a> '
        'retain resource hypotheses; the '
        '<a href="notes/planck-gap-probabilistic.html">prepared-packet counterexample</a> '
        'limits preparation-independent floor claims.</p>' + pandoc(rewrite_links(led, slugs, "notes/"))),
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
    # Slide tutorial: a hand-written page kept in scripts/site/, copied as is.
    tut_src = ROOT / "scripts" / "site" / "tutorial.html"
    if tut_src.exists():
        (DOCS / "tutorial.html").write_text(
            tut_src.read_text(encoding="utf-8"), encoding="utf-8")

    # Declare every generated file, so that check_repository.py can skip them
    # while keeping the source-companion and checksum rules for real sources.
    generated = sorted(
        p.relative_to(ROOT).as_posix()
        for p in [DOCS / "index.html", DOCS / "archive.html", DOCS / "papers.html",
                  DOCS / "ledger.html", DOCS / "sources.html",
                  DOCS / ".nojekyll"]
                  + ([DOCS / "tutorial.html"] if (DOCS / "tutorial.html").exists() else []) + list(OUT_NOTES.glob("*.html"))
                  + list(OUT_SOURCES.glob("*.html")) + list(out_maps.glob("*.html")))
    # llms.txt (llmstxt.org convention): LLM.md with absolute links, served at the site root.
    llm_src = ROOT / "LLM.md"
    if llm_src.exists():
        import re as _re
        _gh = "https://github.com/arivero/navstokgap/blob/main/"
        _txt = llm_src.read_text(encoding="utf-8")
        _txt = _re.sub(r"\]\((?!https?://|#)([^)]+)\)", lambda m: "](" + _gh + m.group(1) + ")", _txt)
        (DOCS / "llms.txt").write_text(_txt, encoding="utf-8")
    (DOCS / ".site-manifest").write_text(
        "# Generated by scripts/build_site.py; not retrieved sources.\n"
        + "\n".join(generated) + "\n", encoding="utf-8")

    stale = [q for q in OUT_NOTES.glob("*.html") if q.stem not in slugs]
    for q in stale:
        q.unlink()

    print(f"site: {len(notes)} notes, {len(comps)} sources, {len(pdfs)} papers, "
          f"{len(catalog)} catalog entries, {len(maps)} maps, "
          f"{len(stale)} stale removed -> docs/")


if __name__ == "__main__":
    sys.exit(main())
