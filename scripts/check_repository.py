"""Check local Markdown targets, source companions and all paper citation keys."""

from pathlib import Path
from html.parser import HTMLParser
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class NavigationPage(HTMLParser):
    """Read generated navigation targets without fetching external resources."""

    def __init__(self, path):
        super().__init__()
        self.ids, self.links, self.notes = set(), [], []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if attrs.get("data-note"):
            self.notes.append(attrs["data-note"])


def main():
    errors = []
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
            if parsed.scheme or not parsed.path or parsed.path.startswith("/"):
                continue
            local = (path.parent / unquote(parsed.path)).resolve()
            if not local.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link {target}")
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
            for field in ("summary", "thematic_area", "strongest_result", "proof_status", "current_relevance", "keys"):
                if not entry.get(field):
                    errors.append(f"Semantic catalog: missing {field} for {path.name}")
            for relation in entry["relations"]:
                if relation["type"] not in {"uses", "corrects", "supersedes", "is_superseded_by", "obstructs", "continues"} or not (ROOT / relation["target"]).exists() or not relation.get("reason"):
                    errors.append(f"Semantic catalog: invalid relation for {path.name}")
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
    manifest = ROOT / "docs" / ".site-manifest"
    generated = set()
    if manifest.exists():
        generated = {line.strip() for line in manifest.read_text().splitlines()
                     if line.strip() and not line.startswith("#")}
    # Check the public routing pages, including their section-level frontier links.
    navigation = [ROOT / "docs" / name for name in
                  ("index.html", "archive.html", "tutorial.html", "papers.html", "ledger.html")]
    navigation += [ROOT / name for name in sorted(generated)
                   if name.startswith("docs/maps/") and name.endswith(".html")]
    pages = {}
    for path in navigation:
        if not path.exists():
            errors.append(f"Missing generated navigation page: {path.relative_to(ROOT)}")
            continue
        page = pages.setdefault(path, NavigationPage(path))
        for link in page.links:
            parsed = urlsplit(link)
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
    for paper_path in (ROOT / "papers").glob("*.tex"):
        paper_text = paper_path.read_text()
        local_keys = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", paper_text)
        if len(local_keys) != len(set(local_keys)):
            errors.append(f"{paper_path.name}: duplicate inline bibliography key")
        available_keys = set(keys) | set(local_keys)
        for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", paper_text):
            for key in group.split(","):
                if key.strip() not in available_keys:
                    errors.append(f"{paper_path.name}: missing bibliography key: {key}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Repository checks passed: {link_count} local Markdown links, "
          f"{len(expected)} catalog entries, {len(navigation)} navigation pages, "
          "source companions, citation keys")


if __name__ == "__main__":
    main()
