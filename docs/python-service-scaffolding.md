# Python Service Scaffolding

This repo now has a minimal Flask service scaffold modeled after `~/git/equipment-status-board`, but intentionally stripped down so volunteers can fan out implementation work without inheriting premature production decisions.

## Copied Over

- `pyproject.toml` as the Python packaging and tool configuration entry point.
- A Flask app factory pattern in `toolbot.create_app()`.
- Environment-backed configuration classes for development, testing, production, and default modes.
- Minimal Flask-SQLAlchemy setup with model classes for `tools`, `users`, `reservations`, and `audit_events`.
- A `/health` route returning `ok`.
- A minimal Jinja template structure with shared components, a base layout, and a public index page.
- Local Docker scaffolding with an app container and MariaDB service.
- `.env.example` for local Docker Compose configuration.
- Makefile shortcuts for Docker Compose workflows and local setup.
- GitHub Actions CI checks for lint, tests, and Docker image build.
- Pytest smoke tests for app creation, testing config, and basic routes.
- `python-dotenv`, `pytest`, and `ruff` dependency conventions.

## Left Out Of Scope

- Migrations and seed commands.
- Slack app integration and background workers.
- Authentication, admin views, forms, and static assets.
- CSS/JavaScript assets and frontend framework choices.
- Gunicorn and deployment wiring.
- Monitoring and metrics integrations.
- Domain services for tools, reservations, users, and audit events.

Those areas should be added as the implementation slices become clear.
