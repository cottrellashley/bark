.PHONY: help install test lint format build serve docs clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install in editable mode with dev dependencies
	uv pip install -e ".[dev]"

test: ## Run tests
	uv run pytest

lint: ## Run linter
	uv run ruff check src/ tests/

format: ## Format code
	uv run ruff format src/ tests/

build: ## Build the package
	uv build

serve: ## Serve the demo site locally
	uv run bark serve demo-site --port 8234

docs: ## Build the documentation site
	uv run bark build docs

docs-serve: ## Serve the documentation site locally
	uv run bark serve docs --port 8235

clean: ## Remove build artifacts
	rm -rf dist/ build/ *.egg-info/ demo-site/dist/ docs/dist/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
