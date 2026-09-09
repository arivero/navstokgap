PYTHON ?= python3

.PHONY: check papers figures programme

check:
	$(PYTHON) scripts/check_repository.py
	sha256sum -c docs/SHA256SUMS

programme:
	pandoc research/PROGRAMME.md --standalone --to=latex --top-level-division=section --template=papers/programme-template.tex -o papers/research-programme.tex

papers:
	$(PYTHON) scripts/build_papers.py

figures:
	$(error Disabled: the legacy figure script runs mathematical verification; preserve existing figures and use written proofs)
