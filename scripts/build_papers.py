"""Build one explicitly selected manuscript; never dispatch a corpus rebuild."""

from argparse import ArgumentParser
from hashlib import sha256
from pathlib import Path
import json
import os
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def run(command, *, cwd=ROOT, env=None):
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.returncode:
        raise SystemExit(result.stdout[-6000:])


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--paper", required=True, help="One maintained-note or standalone TeX slug")
    slug = parser.parse_args().paper
    if not re.fullmatch(r"[A-Za-z0-9_-]+", slug):
        parser.error("paper must be one plain manuscript slug")
    source = ROOT / "papers" / f"{slug}.tex"
    note = ROOT / "notes" / f"{slug}.md"
    output = ROOT / "out" / "papers" / f"{slug}.pdf"
    build = ROOT / ".build" / slug
    if note.is_file():
        run(["make", "paper", f"NOTE={slug}"])
    else:
        if not source.is_file() or source.name.endswith("-template.tex"):
            parser.error(f"no manuscript source for {slug}")
        build.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["BIBINPUTS"] = str(ROOT) + os.pathsep + env.get("BIBINPUTS", "")
        command = ["pdflatex", "-no-shell-escape", "-halt-on-error",
                   "-interaction=nonstopmode", f"-output-directory={build}", str(source)]
        run(command, env=env)
        aux = build / f"{slug}.aux"
        if aux.is_file() and r"\bibdata" in aux.read_text(errors="replace"):
            run(["bibtex", slug], cwd=build, env=env)
        run(command, env=env)
        run(command, env=env)
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(build / output.name, output)
    if not output.read_bytes().startswith(b"%PDF-"):
        raise SystemExit(f"Invalid compiled PDF: {output}")
    log = (build / f"{slug}.log").read_text(errors="replace")
    if "Missing character:" in log or "Overfull " in log:
        raise SystemExit(f"Inspect layout/glyph warnings in {build / (slug + '.log')}")
    record = {source.name: sha256(source.read_bytes()).hexdigest(),
              output.name: sha256(output.read_bytes()).hexdigest()}
    (build / "publication-input.json").write_text(json.dumps(record, indent=2) + "\n")
    print(f"Built {source.relative_to(ROOT)} and {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
