.PHONY: dev test demo

dev:
	python3 -m pip install -r requirements-dev.txt

test:
	python3 -m pytest -q

# PYTHONPATH=src because the package lives under src/ and is not installed here.
# pytest reads that path from pyproject, but a plain python run does not, so
# without it the first command in the README dies with ModuleNotFoundError.
demo:
	PYTHONPATH=src python3 scripts/demo.py
