"""Build accepted paper PDFs from the repository root, without shell escape."""

from pathlib import Path
import os
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def run(command, env=None, cwd=ROOT):
    result = subprocess.run(command, cwd=cwd, env=env, text=True, capture_output=True)
    if result.returncode:
        print(result.stdout[-10000:])
        print(result.stderr[-5000:])
        raise SystemExit(f"Command failed ({result.returncode}): {command}")


def main():
    for executable in ("pandoc", "pdflatex", "bibtex"):
        if shutil.which(executable) is None:
            raise SystemExit(f"Missing {executable}; see research/TOOLS.md")
    run(["pandoc", "research/PROGRAMME.md", "--standalone", "--to=latex",
         "--top-level-division=section", "--template=papers/programme-template.tex",
         "-o", "papers/research-programme.tex"])
    env = os.environ.copy()
    run(["pandoc", "notes/cut-point-consistency.md", "--standalone", "--to=latex",
         "--top-level-division=section", "--template=papers/research-note-template.tex",
         "-V", "note-title=Cut-point consistency and an action remainder",
         "-o", "papers/cut-point-consistency.tex"])
    # Use repo-relative bibliography paths regardless of the aux output directory.
    run(["pandoc", "notes/physical-cut-speed.md", "--standalone", "--to=latex",
         "--top-level-division=section", "--template=papers/research-note-template.tex",
         "-V", "note-title=A physical cut: elastic reversal, finite speed and memory",
         "-o", "papers/physical-cut-speed.tex"])
    env["BIBINPUTS"] = str(ROOT) + os.pathsep + env.get("BIBINPUTS", "")
    output = ROOT / "out" / "papers"
    output.mkdir(parents=True, exist_ok=True)
    for paper in ("action-gap-foundations", "time-refinement", "regulator-limits",
                  "classical-action-field", "collision-action-relaxation",
                  "cut-point-consistency", "physical-cut-speed", "research-programme"):
        build = ROOT / ".build" / paper
        build.mkdir(parents=True, exist_ok=True)
        command = ["pdflatex", "-no-shell-escape", "-halt-on-error",
                   "-interaction=nonstopmode", f"-output-directory={build}",
                   f"papers/{paper}.tex"]
        run(command, env)
        if paper in ("action-gap-foundations", "time-refinement", "regulator-limits",
                     "classical-action-field", "collision-action-relaxation"):
            run(["bibtex", paper], env, cwd=build)
        run(command, env)
        run(command, env)
        log = (build / f"{paper}.log").read_text(errors="replace")
        errors = re.findall(r"[^\n]*(?:undefined|Rerun to get cross-references)[^\n]*", log)
        if errors:
            raise SystemExit(f"Unresolved references in {paper}: {errors}")
        warnings = re.findall(r"Overfull \\[hv]box[^\n]*", log)
        if warnings:
            raise SystemExit(f"Layout overflow in {paper}: {warnings}")
        shutil.copy2(build / f"{paper}.pdf", output / f"{paper}.pdf")
        print(f"Built out/papers/{paper}.pdf")


if __name__ == "__main__":
    main()
