.PHONY: dev test demo

dev:
	pip install -r requirements-dev.txt

test:
	pytest -q

demo:
	python scripts/demo.py
