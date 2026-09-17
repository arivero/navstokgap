PYTHON ?= python3

.PHONY: check paper papers figures programme publication site

check:
	$(PYTHON) scripts/check_repository.py
	sha256sum -c docs/SHA256SUMS

programme:
	pandoc research/PROGRAMME.md --standalone --to=latex --top-level-division=section --template=papers/programme-template.tex -o papers/research-programme.tex

paper:
	@test -n "$(NOTE)" || (echo "usage: make paper NOTE=<slug> (builds notes/<slug>.md only)"; exit 1)
	@title=$$(sed -n '1s/^# //p' notes/$(NOTE).md | cut -c1-90); \
	pandoc notes/$(NOTE).md --standalone --to=latex --top-level-division=section \
	  --template=papers/research-note-template.tex -V "note-title=$$title" -o papers/$(NOTE).tex && \
	mkdir -p .build/$(NOTE) out/papers && \
	for i in 1 2; do pdflatex -no-shell-escape -halt-on-error -interaction=nonstopmode \
	  -output-directory=.build/$(NOTE) papers/$(NOTE).tex >/dev/null; done && \
	cp .build/$(NOTE)/$(NOTE).pdf out/papers/$(NOTE).pdf && \
	grep -c "Overfull" .build/$(NOTE)/$(NOTE).log | sed 's/^/overfull boxes: /'; true

papers:
	$(error Disabled as a routine gate: use make paper NOTE=<slug>; scripts/build_papers.py remains for an explicit full rebuild)

figures:
	$(error Disabled: the legacy figure script runs mathematical verification; preserve existing figures and use written proofs)

publication: papers
	$(PYTHON) scripts/package_publication.py
	$(PYTHON) scripts/package_publication.py --paper classical-spins-operational-closure

site:
	$(PYTHON) scripts/build_site.py
