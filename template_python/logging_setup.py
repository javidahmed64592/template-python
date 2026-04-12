"""Logging setup for the server."""

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from template_python.constants import (
    LOGGING_DATE_FORMAT,
    LOGGING_FORMAT,
    LOGGING_LEVEL,
)

FORMATTER = logging.Formatter(LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)
_root_logger = logging.getLogger()


def add_console_handler() -> None:
    """Add a console handler to the root logger."""
    _console_handler = logging.StreamHandler(sys.stdout)
    _console_handler.setLevel(getattr(logging, LOGGING_LEVEL))
    _console_handler.setFormatter(FORMATTER)
    _root_logger.addHandler(_console_handler)


def add_file_handler(logging_filepath: Path, max_bytes: int, backup_count: int) -> None:
    """Configure logging with both console and rotating file handlers.

    :param Path logging_filepath: The path to the log file.
    :param int max_bytes: The maximum size of the log file in bytes before rotation.
    :param int backup_count: The number of backup log files to keep.
    """
    logging_filepath.parent.mkdir(exist_ok=True)
    _file_handler = RotatingFileHandler(
        filename=logging_filepath, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    _file_handler.setLevel(getattr(logging, LOGGING_LEVEL))
    _file_handler.setFormatter(FORMATTER)
    _root_logger.addHandler(_file_handler)


def setup_default_logging() -> None:
    """Configure default logging to console with the specified format and level."""
    _root_logger.setLevel(getattr(logging, LOGGING_LEVEL))
    _root_logger.handlers.clear()
    add_console_handler()
