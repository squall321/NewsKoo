"""Application settings and environment loading utilities."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict
import os

PROJECT_ROOT = Path(__file__).resolve().parents[3]
ENV_FILE = PROJECT_ROOT / ".env"


def _load_env_file(path: Path = ENV_FILE) -> None:
    """Load key/value pairs from the given .env file into the environment."""
    if not path.exists():
        return

    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


_load_env_file()


def _to_bool(value: str) -> bool:
    return value.lower() in {"1", "true", "yes", "on"}


@dataclass
class Settings:
    """Container for server configuration."""

    app_name: str = os.getenv("APP_NAME", "NewsKoo API")
    app_env: str = os.getenv("APP_ENV", "local")
    app_host: str = os.getenv("APP_HOST", "0.0.0.0")
    app_port: int = int(os.getenv("APP_PORT", "8000"))
    app_debug: bool = _to_bool(os.getenv("APP_DEBUG", "true"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    def model_dump(self) -> Dict[str, str]:
        return {
            "app_name": self.app_name,
            "app_env": self.app_env,
            "app_host": self.app_host,
            "app_port": str(self.app_port),
            "app_debug": str(self.app_debug),
            "log_level": self.log_level,
        }


settings = Settings()
