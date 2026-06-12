# Python Service Scaffolding

This repo now has a minimal Flask service scaffold modeled after `~/git/equipment-status-board`, but intentionally stripped down so volunteers can fan out implementation work without inheriting premature production decisions.

## Copied Over

- `pyproject.toml` as the Python packaging and tool configuration entry point.
- A Flask app factory pattern in `toolbot.create_app()`.
- Environment-backed configuration classes for development, testing, production, and default modes.
- Minimal Flask-SQLAlchemy setup with model classes for `tools`, `users`, `reservations`, and `audit_events`.
- Flask-Migrate/Alembic wiring with a baseline migration for the current model schema.
- A `/health` route returning `ok`.
- A minimal Jinja template structure with shared components, a base layout, and a public index page.
- Local Docker scaffolding with an app container and MariaDB service.
- `.env.example` for local Docker Compose configuration.
- Makefile shortcuts for Docker Compose workflows and local setup.
- GitHub Actions CI checks for lint, tests, and Docker image build.
- Pytest smoke tests for app creation, testing config, and basic routes.
- `python-dotenv`, `pytest`, and `ruff` dependency conventions.

## Left Out Of Scope

- Slack app integration and background workers.
- Authentication, admin views, forms, and static assets.
- CSS/JavaScript assets and frontend framework choices.
- Gunicorn and deployment wiring.
- Monitoring and metrics integrations.
- Domain services for tools, reservations, users, and audit events.

Those areas should be added as the implementation slices become clear.

## Database Migrations

Runtime schema creation is intentionally not part of the Flask app startup path. Docker Compose environments should use
the committed Alembic migrations instead:

```bash
make docker-up
make migrate
make seed
```

Use `docker compose exec app flask --app toolbot:create_app db migrate -m "describe change"` when model changes need a
new migration. Tests may still use `db.create_all()` with SQLite in-memory fixtures because they are isolated from app
runtime behavior.

## Local Seed Data

Starter tool records are explicit local setup, not app startup behavior. Run `make seed` after migrations to create or
update the initial tool rows used for local development.
