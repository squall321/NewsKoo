"""Session helpers for SQLAlchemy interactions."""
from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .config import DatabaseConfig

_engine = None
_SessionFactory = None


def _ensure_session_factory() -> sessionmaker:
    global _engine, _SessionFactory
    if _SessionFactory is None:
        config = DatabaseConfig.from_env()
        _engine = create_engine(config.sqlalchemy_url, future=True, echo=False)
        _SessionFactory = sessionmaker(bind=_engine, autoflush=False, autocommit=False, expire_on_commit=False, future=True)
    return _SessionFactory


def get_engine():
    if _engine is None:
        _ensure_session_factory()
    return _engine


def get_session_factory() -> sessionmaker:
    return _ensure_session_factory()


@contextmanager
def get_session() -> Iterator[Session]:
    factory = _ensure_session_factory()
    session: Session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


__all__ = ["get_session", "get_engine", "get_session_factory"]
