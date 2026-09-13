"""Package the standalone elastic-gas draft, including its compiled PDF."""

from hashlib import sha256
from pathlib import Path
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PAPER = "same-collisions-different-transport"


def main():
    source = ROOT / "papers" / f"{PAPER}.tex"
    pdf = ROOT / "out" / "papers" / f"{PAPER}.pdf"
    provenance = ROOT / ".build" / PAPER / "publication-input.json"
    if not source.is_file() or not pdf.is_file() or not provenance.is_file():
        raise SystemExit("Run make publication: source, compiled PDF and build record are required")
    files = {source.name: source.read_bytes(), pdf.name: pdf.read_bytes()}
    hashes = {name: sha256(data).hexdigest() for name, data in files.items()}
    if json.loads(provenance.read_text()) != hashes:
        raise SystemExit("Publication source/PDF differs from its build record; run make publication")
    if not files[pdf.name].startswith(b"%PDF-"):
        raise SystemExit("Publication PDF has an invalid header")
    files["manifest.json"] = (json.dumps(hashes, indent=2) + "\n").encode()
    files["README.txt"] = (
        "Same collisions, different transport — review draft\n\n"
        "The compiled PDF is included with its standalone LaTeX source.\n"
        "References and the TikZ figure are embedded; no repository files are needed.\n"
        "Compile twice with a TeX installation providing Latin Modern and TikZ:\n"
        f"  pdflatex -no-shell-escape {source.name}\n"
        f"  pdflatex -no-shell-escape {source.name}\n\n"
        "manifest.json records SHA-256 hashes of the source and supplied PDF.\n"
        "This is an author-review draft, not an external submission.\n"
    ).encode()
    output = ROOT / "out" / "publications" / f"{PAPER}.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for name, data in files.items():
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, data)
    with zipfile.ZipFile(output) as bundle:
        if bundle.testzip() is not None or pdf.name not in bundle.namelist():
            raise SystemExit("Publication archive failed integrity/PDF inclusion check")
    print(f"Packaged {output.relative_to(ROOT)} (PDF, source, hashes, build instructions)")


if __name__ == "__main__":
    main()
