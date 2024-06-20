"""Module providing an easy way to setup a minimal logger."""

import copy
import logging
import os
import platform
import sys
from enum import Enum
from logging import handlers, StreamHandler
from pathlib import Path
from typing import Literal

if int(platform.python_version_tuple()[1]) >= 11:
    from enum import StrEnum
    from typing import Self
else:
    from typing_extensions import Self

    StrEnum = (str, Enum)


class LoggingLevel(Enum):
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG


class ConsoleColor(*StrEnum):
    """Simple shortcut to use colors in the console."""

    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    ORANGE = "\033[93m"
    RED = "\033[91m"
    BOLD_RED = "\033[1;31m"
    ENDCOLOR = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class ColoredFormatter(logging.Formatter):
    """Formatter adding colors to levelname."""

    def format(self: Self, record: logging.LogRecord) -> str:
        """Add colors to the levelname of the record."""
        levelno = record.levelno
        if levelno == logging.CRITICAL:
            levelname_color = ConsoleColor.BOLD_RED + record.levelname + ConsoleColor.ENDCOLOR
        elif levelno == logging.ERROR:
            levelname_color = ConsoleColor.RED + record.levelname + ConsoleColor.ENDCOLOR
        elif levelno == logging.WARNING:
            levelname_color = ConsoleColor.ORANGE + record.levelname + ConsoleColor.ENDCOLOR
        elif levelno == logging.INFO:
            levelname_color = ConsoleColor.GREEN + record.levelname + ConsoleColor.ENDCOLOR
        elif levelno == logging.DEBUG:
            levelname_color = ConsoleColor.BLUE + record.levelname + ConsoleColor.ENDCOLOR
        else:
            levelname_color = record.levelname
        # Do not modify the record directly, since other handlers might be using it.
        record = copy.copy(record)
        record.levelname = levelname_color
        return logging.Formatter.format(self, record)


def create_logger(
    name: str,
    *,
    log_dir: Path | None = None,
    stdout: bool = True,
    verbose_level: Literal["debug", "info", "warning", "error", "critical", 10, 20, 30, 40, 50] | LoggingLevel = "info",
) -> logging.Logger:
    """Create a logger.

    Args:
        name: Name of the logger.
        log_dir: If not None, the logs will be saved to that folder.
        stdout: If True then outputs to stdout.
        verbose_level: Either debug, info, error.

    Returns:
        The logger instance.
    """
    # If a logger is created multiple times, reinitialize it each time.
    if name in logging.root.manager.loggerDict:
        logger = logging.getLogger(name)
        for handler in logger.handlers.copy():
            logger.removeHandler(handler)

    logger = logging.getLogger(name)

    if log_dir is not None:
        log_dir.mkdir(parents=True, exist_ok=True)
        log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # Add a (rotating) file handler to the logging system
        file_log_handler = handlers.RotatingFileHandler(log_dir / (name + ".log"), maxBytes=500000, backupCount=2)
        file_log_handler.setFormatter(log_formatter)
        logger.addHandler(file_log_handler)

    if stdout:
        # Add handler to the logging system (default has none) : outputting in stdout
        terminal_log_handler = StreamHandler(sys.stderr)
        if os.name != "nt":
            # Fancy color for non windows console
            colored_log_formatter = ColoredFormatter("%(levelname)s - %(message)s")
            terminal_log_handler.setFormatter(colored_log_formatter)
        else:
            log_formatter = logging.Formatter("%(levelname)s - %(message)s")
            terminal_log_handler.setFormatter(log_formatter)
        logger.addHandler(terminal_log_handler)

    match verbose_level:
        case "debug" | LoggingLevel.DEBUG | 10:
            logger.setLevel(logging.DEBUG)
        case "info" | LoggingLevel.INFO | 20:
            logger.setLevel(logging.INFO)
        case "warning" | LoggingLevel.WARNING | 30:
            logger.setLevel(logging.WARNING)
        case "error" | LoggingLevel.ERROR | 40:
            logger.setLevel(logging.ERROR)
        case "critical" | LoggingLevel.CRITICAL | 50:
            logger.setLevel(logging.CRITICAL)

    return logger
