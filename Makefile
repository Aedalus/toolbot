.PHONY: help setup db-up run routes test lint docker-build docker-up docker-down docker-config open-local

VENV := .venv

help:
	@awk 'BEGIN {FS = ":.*##"; green = "\033[32m"; reset = "\033[0m"; printf "Available targets:\n"} /^[a-zA-Z_-]+:.*##/ {printf "  " green "%-14s" reset " %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Create a local virtualenv and install development dependencies.
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install -e ".[dev]"

db-up: ## Start only the MariaDB service.
	docker compose up -d db

run: ## Run the app and database with Docker Compose.
	docker compose up

routes: ## Show Flask routes from the app container.
	docker compose exec app flask --app toolbot:create_app routes

test: ## Run tests with the local virtualenv.
	$(VENV)/bin/python -m pytest tests/ -v

lint: ## Run ruff with the local virtualenv.
	$(VENV)/bin/ruff check toolbot/ tests/

docker-build: ## Build Docker images.
	docker compose build

docker-up: ## Start the Docker Compose stack in the background.
	docker compose up -d

docker-down: ## Stop the Docker Compose stack.
	docker compose down

docker-config: ## Validate and print the Docker Compose configuration.
	docker compose config

open-local: ## Open the local app in browser
	open http://localhost:8080
