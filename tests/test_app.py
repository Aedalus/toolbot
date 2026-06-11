"""Smoke tests for the Toolbot application."""

from toolbot import create_app
from toolbot.extensions import db
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
