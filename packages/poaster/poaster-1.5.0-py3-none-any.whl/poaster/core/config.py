import functools
import logging
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict
from uvicorn.logging import TRACE_LOG_LEVEL

ColorVariant = Literal["danger", "info", "primary", "success", "warning"]
LogLevel = Literal["critical", "error", "warning", "info", "debug", "trace"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", frozen=True)

    log_level: LogLevel = "info"
    db_path: str = "/./poaster.db"
    secret_key: str = ""
    secret_key_n_bytes: int = 32
    algorithm: str = "HS256"

    # theming
    title: str = "poaster"
    color_danger: str = "#FF595E"
    color_info: str = "#1982C4"
    color_primary: str = "#6A4C93"
    color_success: str = "#8AC926"
    color_warning: str = "#FFCA3A"

    @functools.cached_property
    def async_uri(self) -> str:
        return f"sqlite+aiosqlite://{self.db_path}"

    @functools.cached_property
    def uri(self) -> str:
        return f"sqlite://{self.db_path}"

    @functools.cached_property
    def _color_map(self) -> dict[ColorVariant, str]:
        return {
            "danger": self.color_danger,
            "info": self.color_info,
            "primary": self.color_primary,
            "success": self.color_success,
            "warning": self.color_warning,
        }

    def get_color(self, variant: ColorVariant) -> str:
        return self._color_map[variant]


def get_log_level(level: LogLevel) -> int:
    log_levels: dict[LogLevel, int] = {
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG,
        "trace": TRACE_LOG_LEVEL,
    }
    try:
        return log_levels[level]
    except KeyError:
        valid_levels = ", ".join(log_levels.keys())
        raise RuntimeError(f"{level=} invalid. Log levels: {valid_levels}") from None


def get_settings() -> Settings:
    """Load settings from environment and configure logging."""
    settings = Settings()

    logging.basicConfig(
        level=get_log_level(settings.log_level),
        format="%(asctime)s - %(levelname)s: %(message)s",
    )

    return settings


settings = get_settings()
