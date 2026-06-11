"""Shared pytest fixtures."""

import pytest

from toolbot import create_app


@pytest.fixture
def app():
    return create_app("testing")


@pytest.fixture
def client(app):
    return app.test_client()
