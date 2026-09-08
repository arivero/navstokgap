"""Check local Markdown targets, source companions and all paper citation keys."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    # User hard rule: the default verification target is document integrity only.
    makefile = (ROOT / "Makefile").read_text()
    match = re.search(r"^check:\n((?:\t[^\n]*\n)*)", makefile, re.MULTILINE)
    allowed = ["$(PYTHON) scripts/check_repository.py", "sha256sum -c docs/SHA256SUMS"]
    if match is None or [line.strip() for line in match.group(1).splitlines()] != allowed:
        errors.append("Hard rule: make check must contain only document/source integrity commands")
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
    for path in (ROOT / "docs").rglob("*"):
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
        for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", paper_path.read_text()):
            for key in group.split(","):
                if key.strip() not in keys:
                    errors.append(f"{paper_path.name}: missing bibliography key: {key}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Repository checks passed: {link_count} local Markdown links, source companions, citation keys")


if __name__ == "__main__":
    main()
