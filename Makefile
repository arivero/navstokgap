PYTHON ?= python3

.PHONY: check papers figures programme

check:
	$(PYTHON) scripts/constant_force_geometry.py --check-only
	$(PYTHON) scripts/action_gap_checks.py
	$(PYTHON) scripts/time_refinement_checks.py
	$(PYTHON) scripts/check_repository.py
	sha256sum -c docs/SHA256SUMS

programme:
	pandoc research/PROGRAMME.md --standalone --to=latex --top-level-division=section --template=papers/programme-template.tex -o papers/research-programme.tex

papers:
	$(PYTHON) scripts/build_papers.py

figures:
	$(PYTHON) scripts/constant_force_geometry.py
