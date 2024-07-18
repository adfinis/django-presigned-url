.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort -k 1,1 | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: lint 
lint: ## lint the code 
	@poetry run ruff check .
	@poetry run ruff format --check .
	@poetry run mypy django_presigned_url

.PHONY: format
format: ## format the code 
	@poetry run ruff check . --fix
	@poetry run ruff format .


.PHONY: test
test: ## run the tests
	@poetry run pytest
