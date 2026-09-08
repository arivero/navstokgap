PYTHON ?= python3

.PHONY: check papers figures programme

check:
	$(PYTHON) scripts/constant_force_geometry.py --check-only
	$(PYTHON) scripts/action_gap_checks.py
	$(PYTHON) scripts/time_refinement_checks.py
	$(PYTHON) scripts/regulator_limit_checks.py
	$(PYTHON) scripts/classical_action_field_checks.py
	$(PYTHON) scripts/collision_action_checks.py
	$(PYTHON) scripts/cut_point_checks.py
	$(PYTHON) scripts/physical_cut_checks.py
	$(PYTHON) scripts/telegraph_bridge_checks.py
	$(PYTHON) scripts/composition_checks.py
	$(PYTHON) scripts/bridge_crossover_checks.py
	$(PYTHON) scripts/checkerboard_checks.py
	$(PYTHON) scripts/six_direction_checks.py
	$(PYTHON) scripts/check_repository.py
	sha256sum -c docs/SHA256SUMS

programme:
	pandoc research/PROGRAMME.md --standalone --to=latex --top-level-division=section --template=papers/programme-template.tex -o papers/research-programme.tex

papers:
	$(PYTHON) scripts/build_papers.py

figures:
	$(PYTHON) scripts/constant_force_geometry.py
