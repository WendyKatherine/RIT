.PHONY: check fix lint format format-check mypy test migrate

## Calidad: todo en uno (lo que corre en CI)
check: lint format-check mypy test

## Lint
lint:
	uv run ruff check .

## Formato
format:
	uv run ruff format .

format-check:
	uv run ruff format --check .

## Auto-fix de lint + formato
fix:
	uv run ruff check --fix .
	uv run ruff format .

## Tipos
mypy:
	uv run mypy .

## Tests (requiere Postgres arriba: docker compose up -d postgres)
test:
	uv run pytest

## Migraciones
migrate:
	uv run python manage.py migrate
