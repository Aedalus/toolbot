"""Smoke tests for the Toolbot application."""

from toolbot import create_app
from toolbot.extensions import db, migrate
from toolbot.models import AuditEvent, Reservation, Tool, User


def test_app_creates():
    app = create_app("testing")
    assert app is not None


def test_testing_config():
    app = create_app("testing")
    assert app.config["TESTING"] is True


def test_health_endpoint(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.data == b"ok"


def test_index_endpoint(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"<h1>Toolbot</h1>" in resp.data


def test_models_registered_with_database(app):
    with app.app_context():
        db.create_all()
        assert Tool.__tablename__ in db.metadata.tables
        assert User.__tablename__ in db.metadata.tables
        assert Reservation.__tablename__ in db.metadata.tables
        assert AuditEvent.__tablename__ in db.metadata.tables


def test_migrations_registered(app):
    assert app.extensions["migrate"].db is db
    assert migrate.db is db


def test_seed_tools_command_creates_starter_tools(app):
    with app.app_context():
        db.create_all()

    result = app.test_cli_runner().invoke(args=["seed-tools"])

    assert result.exit_code == 0
    assert "3 created, 0 updated" in result.output

    with app.app_context():
        tools = db.session.execute(db.select(Tool).order_by(Tool.slug)).scalars().all()
        assert [(tool.name, tool.slug, tool.description) for tool in tools] == [
            ("Bronte", "bronte", "The larger laser"),
            ("Glowforge", "glowforge", "The smaller laser"),
            ("Wood Lathes", "wood-lathes", "Reserve all lathes for a class."),
        ]


def test_seed_tools_command_is_idempotent(app):
    with app.app_context():
        db.create_all()

    runner = app.test_cli_runner()
    first_result = runner.invoke(args=["seed-tools"])
    second_result = runner.invoke(args=["seed-tools"])

    assert first_result.exit_code == 0
    assert second_result.exit_code == 0
    assert "0 created, 0 updated" in second_result.output

    with app.app_context():
        tool_count = db.session.execute(db.select(db.func.count()).select_from(Tool)).scalar_one()
        assert tool_count == 3
