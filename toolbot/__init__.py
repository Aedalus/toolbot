"""Toolbot application package."""

from flask import Flask, render_template

from toolbot.config import config
from toolbot.extensions import db


def create_app(config_name="default"):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    import toolbot.models  # noqa: F401

    @app.route("/")
    def index():
        return render_template("public/index.html")

    @app.route("/health")
    def health():
        return "ok"

    return app
