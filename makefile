.PHONY: test 
test:
	pytest -vvv .

.PHONY: clean
clean:
	ruff format .
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name ".ruff_cache" -exec rm -rf {} +
	find . -name ".pytest_cache" -exec rm -rf {} +

.PHONY: pre-commit
pre-commit: clean
	ruff check --fix .
