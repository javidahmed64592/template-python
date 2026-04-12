"""Unit tests for the template_python.logging_setup module."""

import logging
from unittest.mock import MagicMock

from template_python.logging_setup import add_console_handler, add_file_handler, setup_default_logging


class TestAddHandlers:
    """Tests for the add_console_handler and add_file_handler functions."""

    def test_add_console_handler(self) -> None:
        """Test that add_console_handler adds a StreamHandler to the root logger."""
        add_console_handler()

        root_logger = logging.getLogger()
        assert "StreamHandler" in [handler.__class__.__name__ for handler in root_logger.handlers]

    def test_add_file_handler(self, tmp_path: MagicMock) -> None:
        """Test that add_file_handler adds a RotatingFileHandler to the root logger."""
        log_filepath = tmp_path / "test.log"
        add_file_handler(log_filepath, max_bytes=1024, backup_count=1)

        root_logger = logging.getLogger()
        assert "RotatingFileHandler" in [handler.__class__.__name__ for handler in root_logger.handlers]


class TestSetupDefaultLogging:
    """Tests for the setup_default_logging function."""

    def test_setup_default_logging(self) -> None:
        """Test that setup_default_logging configures the root logger with a StreamHandler."""
        setup_default_logging()

        root_logger = logging.getLogger()
        assert "StreamHandler" in [handler.__class__.__name__ for handler in root_logger.handlers]
