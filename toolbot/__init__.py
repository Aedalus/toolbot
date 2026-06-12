"""Toolbot application package."""

import logging
import os

from flask import Flask, render_template

from toolbot.config import config
from toolbot.extensions import db


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

    import toolbot.models  # noqa: F401

    @app.route("/")
    def index():
        return render_template("public/index.html")

    @app.route("/health")
    def health():
        return "ok"

    if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        from toolbot.slack import init_slack

        init_slack(app)

    return app
