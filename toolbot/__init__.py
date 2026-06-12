"""Toolbot application package."""

import logging
import os

from flask import Flask, render_template

from toolbot.config import config
from toolbot.extensions import db, migrate


class HealthcheckLogFilter(logging.Filter):
    """Suppress routine healthcheck access logs."""

    def filter(self, record):
        return "/health" not in record.getMessage()


def configure_logging():
    """Configure application logging filters."""
    werkzeug_logger = logging.getLogger("werkzeug")
    # Needed for multiple instantiations due to tests
    if not any(isinstance(log_filter, HealthcheckLogFilter) for log_filter in werkzeug_logger.filters):
        werkzeug_logger.addFilter(HealthcheckLogFilter())


def create_app(config_name="default"):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    configure_logging()

    db.init_app(app)
    migrate.init_app(app, db)

    import toolbot.models  # noqa: F401

    @app.route("/")
    def index():
        return render_template("public/index.html")

    @app.route("/health")
    def health():
        return "ok"

    _register_cli(app)

    if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        from toolbot.slack import init_slack

        init_slack(app)

    return app


def _register_cli(app):
    """Register Flask CLI commands."""
    import click

    from toolbot.extensions import db as _db
    from toolbot.models.tool import Tool

    starter_tools = [
        ("Bronte", "bronte", "The larger laser"),
        ("Glowforge", "glowforge", "The smaller laser"),
        ("Wood Lathes", "wood-lathes", "Reserve all lathes for a class."),
    ]

    @app.cli.command("seed-tools")
    def seed_tools():
        """Create or update starter tool records."""
        created = 0
        updated = 0

        for name, slug, description in starter_tools:
            tool = _db.session.execute(_db.select(Tool).filter_by(slug=slug)).scalar_one_or_none()
            if tool is None:
                _db.session.add(Tool(name=name, slug=slug, description=description))
                created += 1
                continue

            if tool.name != name or tool.description != description:
                tool.name = name
                tool.description = description
                updated += 1

        _db.session.commit()
        click.echo(f"Seeded starter tools: {created} created, {updated} updated.")
