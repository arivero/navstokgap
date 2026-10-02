PYTHON ?= python3

# Notes that quote Chinese (the atlas and the cut-measure note, including
# the supplementary-plane character U+230C8) build with XeLaTeX, Noto Serif
# CJK SC and HanaMinB (Ubuntu packages fonts-noto-cjk and fonts-hanazono).
# Detection is automatic: any CJK ideograph in notes/$(NOTE).md selects it.
ifneq ($(NOTE),)
ifneq ($(shell LC_ALL=C.UTF-8 grep -qP '[\x{3000}-\x{9FFF}\x{20000}-\x{2FFFF}]' notes/$(NOTE).md 2>/dev/null && echo cjk),)
PAPER_ENGINE ?= xelatex
PAPER_UNICODE ?= true
endif
endif
PAPER_ENGINE ?= pdflatex

.PHONY: check paper papers figures programme publication site opening

check:
	$(PYTHON) scripts/check_repository.py
	sha256sum -c docs/SHA256SUMS

programme:
	pandoc research/PROGRAMME.md --standalone --to=latex --top-level-division=section --template=papers/programme-template.tex -o papers/research-programme.tex

paper:
	@test -n "$(NOTE)" || (echo "usage: make paper NOTE=<slug> (builds notes/<slug>.md only)"; exit 1)
	@set -e; title=$$(sed -n '1s/^# //p' notes/$(NOTE).md | cut -c1-90); \
	pandoc notes/$(NOTE).md --standalone --to=latex --top-level-division=section \
	  --template=papers/research-note-template.tex -V "note-title=$$title" \
	  -V "unicode-cjk=$(PAPER_UNICODE)" -o papers/$(NOTE).tex; \
	mkdir -p .build/$(NOTE) out/papers; \
	for i in 1 2; do $(PAPER_ENGINE) -no-shell-escape -halt-on-error -interaction=nonstopmode \
	  -output-directory=.build/$(NOTE) papers/$(NOTE).tex >/dev/null || \
	  { tail -30 .build/$(NOTE)/$(NOTE).log; exit 1; }; done; \
	cp .build/$(NOTE)/$(NOTE).pdf out/papers/$(NOTE).pdf; \
	grep -c "Overfull" .build/$(NOTE)/$(NOTE).log | sed 's/^/overfull boxes: /'

papers:
	$(error Disabled as a routine gate: use make paper NOTE=<slug>; scripts/build_papers.py remains for an explicit full rebuild)

figures:
	$(error Disabled: the legacy figure script runs mathematical verification; preserve existing figures and use written proofs)

publication: papers
	$(PYTHON) scripts/package_publication.py
	$(PYTHON) scripts/package_publication.py --paper classical-spins-operational-closure

site:
	$(PYTHON) scripts/build_site.py

opening:
	$(PYTHON) scripts/build_site.py --opening-only
