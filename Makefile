.PHONY: help build build-fast serve workbench docs publish status clean test lint \
       docker-build docker-up docker-down docker-shell docker-logs \
       install

BINARY := opendoc
GO_FLAGS := -ldflags="-s -w"

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

# ── Build ──────────────────────────────────────────────────

build: ## Build the opendoc binary (optimised)
	CGO_ENABLED=0 go build $(GO_FLAGS) -o $(BINARY) ./cmd/opendoc

build-fast: ## Build without optimisations (faster compile)
	go build -o $(BINARY) ./cmd/opendoc

install: build ## Install opendoc to $GOPATH/bin
	go install ./cmd/opendoc

# ── Run ────────────────────────────────────────────────────

serve: ## Build & serve the docs site locally
	go run ./cmd/opendoc serve docs -p 8000

workbench: ## Start the workbench for the docs site
	go run ./cmd/opendoc workbench docs -p 3000

docs: ## Build the documentation site
	go run ./cmd/opendoc build docs

publish: ## Build & deploy docs to GitHub Pages
	go run ./cmd/opendoc publish docs

status: ## Show project status
	go run ./cmd/opendoc status docs

# ── Test / Lint ────────────────────────────────────────────

test: ## Run all Go tests
	go test ./...

lint: ## Run go vet
	go vet ./...

# ── Docker ──────────────────────────────────────────────────

docker-build: ## Build the Docker image
	docker compose build

docker-up: ## Start the container (http://localhost:3000)
	docker compose up -d

docker-down: ## Stop the container
	docker compose down

docker-shell: ## Exec into running container
	docker compose exec opendoc bash

docker-logs: ## Tail container logs
	docker compose logs -f

# ── Cleanup ────────────────────────────────────────────────

clean: ## Remove build artifacts
	rm -f $(BINARY)
	rm -rf dist dist-publish
