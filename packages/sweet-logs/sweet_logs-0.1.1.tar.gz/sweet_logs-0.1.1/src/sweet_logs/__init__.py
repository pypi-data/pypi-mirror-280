"""Top-level package for Sweet Logs."""

__version__ = "0.1.0"

from sweet_logs import config as config, formatters as formatters
from sweet_logs.hooks import local_log_safe as local_log_safe, log_critical_hook as log_critical_hook
from sweet_logs.setup import setup_logging as setup_logging
