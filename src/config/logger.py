import logging
import structlog
from typing import Any


def get_default_logger() -> Any:
    """
    Get the default logger.

    Returns:
        The default logger.
    """
    global _logger
    if _logger is None:
        structlog.configure(
            processors=[
                structlog.contextvars.merge_contextvars,
                structlog.processors.add_log_level,
                structlog.processors.StackInfoRenderer(),
                structlog.dev.set_exc_info,
                structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=False),
                structlog.dev.ConsoleRenderer(),
            ],
            wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
            context_class=dict,
            logger_factory=structlog.PrintLoggerFactory(),
            cache_logger_on_first_use=False,
        )

        _logger = structlog.get_logger()

    return _logger


_logger = None
