"""Check local Markdown targets, source companions and all paper citation keys."""

from pathlib import Path
from html.parser import HTMLParser
import json
import re
from urllib.parse import unquote, urlsplit
from collections import Counter

from build_site import NOTE_REDIRECTS, NOTE_FRAGMENT_REDIRECTS, PAGE_REDIRECTS, SITE_URL

ROOT = Path(__file__).resolve().parents[1]


class NavigationPage(HTMLParser):
    """Read generated navigation targets without fetching external resources."""

    def __init__(self, path):
        super().__init__()
        # HTML's top-of-document fragment works without an explicit element.
        self.ids, self.links, self.notes = {"top"}, [], []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if attrs.get("data-note"):
            self.notes.append(attrs["data-note"])


def main():
    errors = []
    # Completed process records belong in git; STATE and catalog stay live.
    for folder in ("research/handoffs", "reviews", "agents"):
        directory = ROOT / folder
        if directory.exists() and any(p.is_file() for p in directory.rglob("*")):
            errors.append(f"Retired process records reintroduced: {folder}")
    for name in ("research/note-scores.md", "research/note-scores.json",
                 "research/PROGRAMME.md", "research/TASKS.md",
                 "research/STRATEGY.md", "research/STATE-history-2026-09-12.md",
                 "notes/corpus-audit-2026-10-01.md",
                 "papers/research-programme.tex",
                 "out/papers/research-programme.pdf",
                 "out/papers/corpus-audit-2026-10-01.pdf"):
        if (ROOT / name).exists():
            errors.append(f"Retired status/review artifact reintroduced: {name}")
    # User hard rule: the default verification target is document integrity only.
    makefile = (ROOT / "Makefile").read_text()
    match = re.search(r"^check:\n((?:\t[^\n]*\n)*)", makefile, re.MULTILINE)
    allowed = ["$(PYTHON) scripts/check_repository.py", "sha256sum -c docs/SHA256SUMS"]
    if match is None or [line.strip() for line in match.group(1).splitlines()] != allowed:
        errors.append("Hard rule: make check must contain only document/source integrity commands")
    figures = re.search(r"^figures:\n((?:\t[^\n]*\n)*)", makefile, re.MULTILINE)
    if figures is None or not figures.group(1).strip().startswith("$(error Disabled:"):
        errors.append("Hard rule: legacy make figures must remain disabled pending user direction")
    link_count = 0
    note_pages = {}
    registered = {
        line.split(maxsplit=1)[1].strip().lstrip("*")
        for line in (ROOT / "docs" / "SHA256SUMS").read_text().splitlines()
        if line.strip()
    }
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text()
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or parsed.path.startswith("/"):
                continue
            if not parsed.path and (path.parent != ROOT / "notes" or not parsed.fragment):
                continue
            local = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not local.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link {target}")
            if parsed.fragment and local.parent == ROOT / "notes" and local.suffix == ".md":
                rendered = ROOT / "docs/notes" / f"{local.stem}.html"
                if rendered.is_file():
                    if rendered not in note_pages:
                        note_pages[rendered] = NavigationPage(rendered)
                    fragment = re.sub(r"^\d+-", "", unquote(parsed.fragment))
                    if fragment not in note_pages[rendered].ids:
                        errors.append(f"{path.relative_to(ROOT)}: missing note section {target}")
            link_count += 1
    # The source catalog must cover every maintained note exactly once.
    # Priorities guide retrieval; separate status/role/value fields preserve scope.
    catalog_path = ROOT / "notes" / "index.md"
    expected = {p.name for p in (ROOT / "notes").glob("*.md")
                if p.name != "index.md"}
    entries = []
    if not catalog_path.exists():
        errors.append("Missing notes/index.md retrieval catalog")
    else:
        catalog = catalog_path.read_text()
        entries = re.findall(
            r"^- \[([^\]\n]+\.md)\]\(([^)\n]+)\)([^\n]*)$",
            catalog,
            re.MULTILINE,
        )
        names = [target for _, target, _ in entries]
        for name in sorted(expected - set(names)):
            errors.append(f"Notes catalog: missing entry {name}")
        for name in sorted(set(names) - expected):
            errors.append(f"Notes catalog: unexpected entry {name}")
        seen = set()
        for label, target, metadata in entries:
            if target in seen:
                errors.append(f"Notes catalog: duplicate entry {target}")
            seen.add(target)
            if label != target:
                errors.append(f"Notes catalog: filename/target mismatch {target}")
            fields = dict(re.findall(r"\|\s*(\w+)=([^|]*)", metadata))
            if fields.get("priority", "").strip() not in {"0", "1", "2", "3"}:
                errors.append(f"Notes catalog: invalid retrieval priority for {target}")
            for field in ("flags", "role", "status", "value", "keys"):
                if not fields.get(field, "").strip():
                    errors.append(f"Notes catalog: missing {field} for {target}")
    # Semantic and manuscript metadata are source inputs to the public archive.
    semantic_path = ROOT / "research/note-index.json"
    semantic_by_slug = {}
    if not semantic_path.exists():
        errors.append("Missing research/note-index.json semantic catalog")
    else:
        semantic = json.loads(semantic_path.read_text())["notes"]
        semantic_paths = [e["path"] for e in semantic]
        if set(semantic_paths) != {f"notes/{name}" for name in expected}:
            errors.append("Semantic catalog: note membership differs from maintained notes")
        if len(semantic_paths) != len(set(semantic_paths)):
            errors.append("Semantic catalog: duplicate note")
        metadata = {target: dict(re.findall(r"\|\s*(\w+)=([^|]*)", tail))
                    for _, target, tail in entries}
        summaries = dict(re.findall(
            r"^- \[[^\]\n]+\]\(([^)\n]+)\)[^\n]*\n  ([^\n]+)$",
            catalog, re.MULTILINE))
        semantic_by_slug = {Path(entry["path"]).stem: entry for entry in semantic}
        for entry in semantic:
            path = ROOT / entry["path"]
            if not path.exists():
                continue
            title = next((line[2:].strip() for line in path.read_text().splitlines()
                          if line.startswith("# ")), path.stem)
            if entry["title"] != title:
                errors.append(f"Semantic catalog: source title differs for {path.name}")
            if entry["status"] not in {"result", "conditional", "obstruction", "open", "historical", "exploratory"}:
                errors.append(f"Semantic catalog: invalid status for {path.name}")
            fields = metadata.get(path.name, {})
            if str(entry["retrieval_priority"]) != fields.get("priority", "").strip():
                errors.append(f"Semantic catalog: priority differs for {path.name}")
            if entry["status"] != fields.get("status", "").strip() or entry["proof_status"] != fields.get("proof_status", "").strip():
                errors.append(f"Semantic catalog: status or proof level differs for {path.name}")
            flags = fields.get("flags", "")
            if entry["surprising"] != ("surprising" in flags) or entry["route_closure"] != ("route-closure" in flags):
                errors.append(f"Semantic catalog: flags differ for {path.name}")
            for field in ("role", "value"):
                if fields.get(field, "").strip() != entry.get(field):
                    errors.append(f"Semantic catalog: {field} differs for {path.name}")
            if fields.get("keys", "").strip() != ";".join(entry["keys"]):
                errors.append(f"Semantic catalog: retrieval keys differ for {path.name}")
            if summaries.get(path.name) != entry["summary"]:
                errors.append(f"Semantic catalog: summary differs for {path.name}")
            for field in ("summary", "thematic_area", "strongest_result", "proof_status", "current_relevance", "keys"):
                if not entry.get(field):
                    errors.append(f"Semantic catalog: missing {field} for {path.name}")
            for relation in entry["relations"]:
                if relation["type"] not in {"uses", "corrects", "supersedes", "is_superseded_by", "obstructs", "continues"} or not (ROOT / relation["target"]).exists() or not relation.get("reason"):
                    errors.append(f"Semantic catalog: invalid relation for {path.name}")
                if relation["target"] == entry["path"]:
                    errors.append(f"Semantic catalog: self relation for {path.name}")
        for former, (canonical, _) in NOTE_REDIRECTS.items():
            if canonical not in semantic_by_slug or former not in semantic_by_slug[canonical]["keys"]:
                errors.append(f"Semantic catalog: missing former-name alias {former} -> {canonical}")
    pdf_catalog = ROOT / "research/pdf-catalog.json"
    if not pdf_catalog.exists():
        errors.append("Missing research/pdf-catalog.json manuscript catalog")
    else:
        manuscripts = json.loads(pdf_catalog.read_text())["manuscripts"]
        pdf_names = {p.stem for p in (ROOT / "out/papers").glob("*.pdf")}
        names = [entry["slug"] for entry in manuscripts]
        if set(names) != pdf_names or len(names) != len(set(names)):
            errors.append("PDF catalog: incomplete or duplicate manuscript coverage")
        for entry in manuscripts:
            if not (ROOT / entry["tex"]).exists() or not (ROOT / entry["pdf"]).exists() or not entry.get("assessment"):
                errors.append(f"PDF catalog: missing artifact or assessment for {entry['slug']}")
            if entry["classification"] not in {"current synthesis", "current technical manuscript", "working manuscript", "older version", "historical research snapshot", "orphan manuscript"}:
                errors.append(f"PDF catalog: invalid classification for {entry['slug']}")
            replacement = entry.get("current_replacement")
            if replacement and not (ROOT / "notes" / f"{replacement}.md").exists():
                errors.append(f"PDF catalog: missing replacement for {entry['slug']}")
            if entry["classification"].startswith("current") and entry["slug"] in semantic_by_slug:
                if entry["title"] != semantic_by_slug[entry["slug"]]["title"]:
                    errors.append(f"PDF catalog: current title differs for {entry['slug']}")
        coverage = (ROOT / "research/pdf-audit.md").read_text()
        if f"**{len(manuscripts)} PDFs**" not in coverage:
            errors.append("PDF coverage page: total differs from catalog")
        counts = Counter(entry["classification"] for entry in manuscripts)
        rows = dict(re.findall(r"^\| ([a-z ]+) \| (\d+) \|$", coverage, re.MULTILINE))
        if {name: int(count) for name, count in rows.items()} != dict(counts):
            errors.append("PDF coverage page: classification counts differ from catalog")
    manifest = ROOT / "docs" / ".site-manifest"
    generated = set()
    if manifest.exists():
        generated = {line.strip() for line in manifest.read_text().splitlines()
                     if line.strip() and not line.startswith("#")}
    if not {"docs/llms.txt", "docs/sitemap.xml", "docs/assets/opening.css",
            "docs/assets/opening.js"}.issubset(generated):
        errors.append("Site manifest: missing generated index or opening asset")
    # Source companions are public pages too; their imported links need checking.
    required = {f"docs/{name}" for name in
                ("index.html", "research.html", "archive.html", "tutorial.html",
                 "papers.html", "ledger.html", "sources.html")}
    navigation = [ROOT / name for name in sorted(
        required | {name for name in generated if name.endswith(".html")})]
    for name in generated:
        if not (ROOT / name).is_file():
            errors.append(f"Missing generated manifest target: {name}")
    pages = {}
    for path in navigation:
        if not path.exists():
            errors.append(f"Missing generated navigation page: {path.relative_to(ROOT)}")
            continue
        page = pages.setdefault(path, NavigationPage(path))
        for link in page.links:
            parsed = urlsplit(link)
            prefix = "/arivero/navstokgap/blob/main/"
            if parsed.netloc == "github.com" and parsed.path.startswith(prefix):
                local = (ROOT / unquote(parsed.path.removeprefix(prefix))).resolve()
                if not local.exists() or not local.is_relative_to(ROOT):
                    errors.append(f"{path.relative_to(ROOT)}: missing repository target {link}")
            if parsed.scheme or parsed.netloc or parsed.path.startswith("/"):
                continue
            local = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not local.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing navigation target {link}")
            elif parsed.fragment and local.suffix == ".html":
                if local not in pages:
                    pages[local] = NavigationPage(local)
                if unquote(parsed.fragment) not in pages[local].ids:
                    errors.append(f"{path.relative_to(ROOT)}: missing navigation anchor {link}")
    for source, fragments in NOTE_FRAGMENT_REDIRECTS.items():
        for former, (canonical, anchor) in fragments.items():
            target = ROOT / "docs/notes" / f"{canonical}.html"
            if target not in pages:
                pages[target] = NavigationPage(target)
            if anchor not in pages[target].ids:
                errors.append(f"Missing fragment redirect target: {source}#{former}")
    sitemap = ROOT / "docs/sitemap.xml"
    if sitemap.exists():
        import xml.etree.ElementTree as ET
        urls = [node.text for node in ET.parse(sitemap).iter()
                if node.tag.endswith("}loc")]
        excluded = {f"notes/{slug}.html" for slug in NOTE_REDIRECTS} | set(PAGE_REDIRECTS)
        expected_urls = {SITE_URL if name == "docs/index.html" else
                         SITE_URL + name.removeprefix("docs/")
                         for name in generated if name.endswith(".html")
                         and name.removeprefix("docs/") not in excluded}
        if set(urls) != expected_urls or len(urls) != len(set(urls)):
            errors.append("Sitemap: duplicate, missing or retired canonical page")
    archive = pages.get(ROOT / "docs/archive.html")
    if archive and (set(archive.notes) != {Path(name).stem for name in expected}
                    or len(archive.notes) != len(expected)):
        errors.append("Generated archive: incomplete or duplicate maintained-note coverage")
    papers = pages.get(ROOT / "docs/papers.html")
    if papers:
        linked = [Path(urlsplit(link).path).stem for link in papers.links
                  if urlsplit(link).path.endswith(".pdf")]
        if set(linked) != {p.stem for p in (ROOT / "out/papers").glob("*.pdf")} or len(linked) != len(set(linked)):
            errors.append("Generated Papers page: incomplete or duplicate PDF coverage")
    for path in (ROOT / "docs").rglob("*"):
        if path.relative_to(ROOT).as_posix() in generated:
            continue
        if path.suffix.lower() in {".pdf", ".html", ".xml"}:
            if not path.with_suffix(".md").exists():
                errors.append(f"Missing source companion: {path.relative_to(ROOT)}")
            if path.relative_to(ROOT).as_posix() not in registered:
                errors.append(f"Unregistered source checksum: {path.relative_to(ROOT)}")
    bib = (ROOT / "references" / "library.bib").read_text()
    keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib)
    if len(keys) != len(set(keys)):
        errors.append("Duplicate shared bibliography key")
    for target in re.findall(r"notes/[A-Za-z0-9_-]+\.md", bib):
        if not (ROOT / target).is_file():
            errors.append(f"Bibliography annotation: missing canonical argument {target}")
    for paper_path in (ROOT / "papers").glob("*.tex"):
        paper_text = paper_path.read_text()
        local_keys = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", paper_text)
        if len(local_keys) != len(set(local_keys)):
            errors.append(f"{paper_path.name}: duplicate inline bibliography key")
        available_keys = set(keys) | set(local_keys)
        for group in re.findall(r"\\(?:cite[a-zA-Z]*|nocite)(?:\[[^]]*\])*\{([^}]+)\}", paper_text):
            for key in group.split(","):
                if key.strip() != "*" and key.strip() not in available_keys:
                    errors.append(f"{paper_path.name}: missing bibliography key: {key}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Repository checks passed: {link_count} local Markdown links, "
          f"{len(expected)} catalog entries, {len(navigation)} navigation pages, "
          "source companions, citation keys")


if __name__ == "__main__":
    main()
