"""Condense the accepted paper PDFs into a single chronological PDF.

The order matches the chronological build order in ``scripts/build_papers.py``
(P00 through the latest accepted result), which is also the order recorded in
``research/STATE.md``. The programme summary (``research-programme.pdf``) and
the unbuilt M03 draft (``spectral-gap-laboratory.tex``) are excluded, since
neither is an accepted paper.
"""

from pathlib import Path

from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parents[1]

# Chronological order of the accepted papers (creation/build order).
PAPERS = [
    "action-gap-foundations",
    "time-refinement",
    "regulator-limits",
    "classical-action-field",
    "collision-action-relaxation",
    "cut-point-consistency",
    "physical-cut-speed",
    "telegraph-return-bridge",
    "composition-universality",
    "bridge-crossover",
    "checkerboard-dynamics",
    "susceptibility-gap",
    "bounded-acceleration-return",
]


def main():
    output_dir = ROOT / "out" / "papers"
    writer = PdfWriter()
    for paper in PAPERS:
        pdf_path = output_dir / f"{paper}.pdf"
        if not pdf_path.exists():
            raise SystemExit(f"Missing built PDF: {pdf_path}. Run `make papers` first.")
        writer.append(str(pdf_path))
    out_path = output_dir / "condensed-papers.pdf"
    with open(out_path, "wb") as handle:
        writer.write(handle)
    print(f"Built {out_path} from {len(PAPERS)} papers.")


if __name__ == "__main__":
    main()
