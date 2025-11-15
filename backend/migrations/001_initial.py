"""Initial database schema creation for NewsKoo."""
from __future__ import annotations

from sqlalchemy import create_engine

from backend.src.db.config import DatabaseConfig
from backend.src.db.models import Base


def upgrade(engine=None):
    engine = engine or create_engine(DatabaseConfig.from_env().sqlalchemy_url, future=True)
    Base.metadata.create_all(engine)


def downgrade(engine=None):
    engine = engine or create_engine(DatabaseConfig.from_env().sqlalchemy_url, future=True)
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    engine = create_engine(DatabaseConfig.from_env().sqlalchemy_url, future=True)
    Base.metadata.create_all(engine)
