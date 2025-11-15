"""Database configuration helpers for the NewsKoo backend."""
from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Mapping


@dataclass(frozen=True)
class DatabaseConfig:
    """Simple container for database connection configuration.

    Values are resolved from environment variables to make the module easy to use
    from scripts as well as when the application runs inside Docker Compose. The
    defaults are safe for local development and match the compose configuration
    documented in the repository README.
    """

    user: str = "newskoo"
    password: str = "newskoo"
    host: str = "localhost"
    port: int = 5432
    database: str = "newskoodb"

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> "DatabaseConfig":
        env = env or os.environ
        return cls(
            user=env.get("DB_USER", cls.user),
            password=env.get("DB_PASSWORD", cls.password),
            host=env.get("DB_HOST", cls.host),
            port=int(env.get("DB_PORT", cls.port)),
            database=env.get("DB_NAME", cls.database),
        )

    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


__all__ = ["DatabaseConfig"]
