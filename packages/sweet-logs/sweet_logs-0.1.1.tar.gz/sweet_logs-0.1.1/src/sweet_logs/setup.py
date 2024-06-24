import logging.config
import sys
from typing import Any, Dict, Optional

import sweet_logs.config
from sweet_logs.hooks import log_critical_hook


def setup_logging(config: Optional[Dict[str, Any]] = None, uncaught_exception_hook: bool = True) -> None:
    """
    Set up logging configuration. If no configuration is provided, the default
    configuration is used. The default configuration is defined in
    sweet_logs.config.base_config.

    Parameters
    ----------
    config : Optional[Dict[str, Any]], optional
        A dictionary that contains configuration for the logger.

    uncaught_exception_hook : bool, optional
        A flag that determines if the uncaught exception hook should be
        set as the sys.excepthook. The default is True. If True, when an
        uncaught exception is raised, a critical log record will be created
        with the exception details.
    """
    if config is None:
        config = sweet_logs.config.base_config
    logging.config.dictConfig(config)

    if uncaught_exception_hook:
        sys.excepthook = log_critical_hook
