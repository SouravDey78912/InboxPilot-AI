import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path


_CONFIGURED = False


def _configure_logging() -> None:
    global _CONFIGURED
    if _CONFIGURED:
        return

    log_level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, log_level_name, logging.INFO)

    logs_dir = Path(__file__).resolve().parent / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_file = logs_dir / "ai_email_agent.log"

    root = logging.getLogger()
    root.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=2_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # Avoid duplicated logs if reloaded (e.g. notebooks/REPL)
    if not any(isinstance(h, logging.StreamHandler) for h in root.handlers):
        root.addHandler(console)
    if not any(isinstance(h, RotatingFileHandler) for h in root.handlers):
        root.addHandler(file_handler)

    _CONFIGURED = True


def get_logger(name: str | None = None) -> logging.Logger:
    _configure_logging()
    return logging.getLogger(name or "ai_email_agent")
