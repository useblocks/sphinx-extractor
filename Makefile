SRC_FILES = sphinx_extractor/ tests/

.PHONY: lint
lint:
	pre-commit run --all-files

.PHONY: test
test:
	poetry run pytest -n auto --tb=long tests/
