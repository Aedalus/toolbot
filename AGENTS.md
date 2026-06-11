# AGENTS.md

Guidance for coding agents working in this repository.

## Project Overview

Toolbot is a Flask service for makerspace tool scheduling. It is intended to support Slack-based reservation workflows and a public read-only availability website. The backend should be the source of truth for tools, users, reservations, and audit events.

This repository is currently a scaffold. Keep changes small and avoid adding production machinery before the related feature slice exists.

## Common Commands

```bash
make docker-config
make docker-up
make routes
python3 -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
make test
make lint
```

Run a single test file or test function:

```bash
.venv/bin/python -m pytest tests/test_app.py -v
.venv/bin/python -m pytest tests/test_app.py::test_health_endpoint -v
```

## Database

The local Docker stack uses MariaDB, matching the equipment-status-board project:

```text
DATABASE_URL=mysql+pymysql://root:toolbot@db:3306/toolbot
```

Tests use SQLite in-memory through `TestingConfig`.

Migrations are not wired up yet. Do not add ad hoc schema creation paths for app runtime. When migrations are introduced, prefer Flask-Migrate/Alembic in the same style as equipment-status-board.

## Architecture

Current stack:

- Python 3.12+
- Flask
- Flask-SQLAlchemy
- MariaDB in Docker Compose
- Jinja2 templates
- Pytest
- Ruff

Application factory:

- `toolbot/__init__.py`
- `create_app(config_name="default")`
- Initializes extensions and imports models for SQLAlchemy metadata registration.

Current layers:

- `toolbot/models/` - SQLAlchemy ORM models for `Tool`, `User`, `Reservation`, and `AuditEvent`.
- `toolbot/templates/` - Shared Jinja base layout, components, and public index page.
- `toolbot/extensions.py` - Flask extension instances.
- `toolbot/config.py` - Environment-backed app configuration.
- `tests/` - Scaffold smoke tests.

Expected future layers:

- `toolbot/services/` - Business logic, validation, scheduling rules, audit logging.
- `toolbot/views/` - Flask blueprints for public and admin pages.
- `toolbot/slack/` - Slack interaction handlers.

Follow the service-layer pattern from equipment-status-board as the app grows: views and Slack handlers should delegate scheduling rules and mutation logic to services instead of querying or mutating models directly.

## Scheduling Rules

The technical design is the source of truth for initial domain behavior:

- Reservation times are stored in UTC.
- Display reservation times in the makerspace timezone.
- Active reservations must not overlap for the same tool.
- Start and end times must align to the tool's slot granularity.
- Canceled and past reservations stay in history.
- Public views should not expose member details by default.

## Testing

Tests should run without MariaDB unless they are explicitly integration tests. Use SQLite in-memory for scaffold and service-level tests where possible.

Use focused tests for new behavior:

- Model and config tests for schema/config changes.
- Service tests for scheduling and validation rules.
- View tests for HTTP behavior.
- Slack handler tests once Slack integration exists.

## Linting

Ruff is configured in `pyproject.toml` with a 120-character line length and Python 3.12 target.

## Docker

`docker-compose.yml` currently defines:

- `app` - Flask development server exposed on host port `8080`
- `db` - MariaDB 12.2.2

Gunicorn, background workers, autoheal, and deployment wiring are intentionally not present yet.

Prefer the Makefile targets for common workflows. As in equipment-status-board, app and database workflows use Docker Compose, while tests and lint run through the local virtualenv.

## CI

`.github/workflows/ci.yml` runs:

- Ruff lint
- Pytest
- Docker image build

Do not copy docs, screenshots, release, or deployment workflows from equipment-status-board until Toolbot has the corresponding files and behavior.

## Documentation

Keep these docs aligned when changing scope or architecture:

- `README.md`
- `docs/technical-design.md`
- `docs/python-service-scaffolding.md`

If implementation choices differ from equipment-status-board, document why in `docs/python-service-scaffolding.md` or the relevant technical doc.
