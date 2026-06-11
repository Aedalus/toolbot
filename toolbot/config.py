"""Configuration classes for Toolbot."""

import os


def build_engine_options(database_url: str) -> dict:
    """Compute conservative SQLAlchemy engine options for persistent databases."""
    if database_url.startswith("sqlite"):
        return {}

    options = {
        "pool_pre_ping": True,
        "pool_recycle": 1800,
    }
    if database_url.startswith(("mysql", "mariadb")):
        options["connect_args"] = {
            "connect_timeout": 10,
            "read_timeout": 30,
            "write_timeout": 30,
        }
    return options


class Config:
    """Base configuration."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    MAKERSPACE_TIMEZONE = os.environ.get("MAKERSPACE_TIMEZONE", "America/New_York")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "mysql+pymysql://root:toolbot@localhost/toolbot")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = build_engine_options(SQLALCHEMY_DATABASE_URI)


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_ENGINE_OPTIONS = build_engine_options(SQLALCHEMY_DATABASE_URI)


class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
