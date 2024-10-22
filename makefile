.PHONY: test 
test:
	pytest -vvv .

.PHONY: clean
clean:
	find . -name "__pycache__" -exec rm -rf {} +
	ruff format .

.PHONY: pre-commit
pre-commit: clean
	ruff check --fix .
