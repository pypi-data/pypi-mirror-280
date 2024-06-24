"""
Log formatters
"""

import datetime as dt
import logging
import json
import sys
from typing import Any, Dict, Optional, Union

minor = sys.version_info.minor

LOG_RECORD_BUILTIN_ATTRS = {
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
    "taskName",
}


def _date_from_timestamp(timestamp: float, timezone: dt.timezone = dt.timezone.utc) -> str:
    return dt.datetime.fromtimestamp(timestamp, tz=timezone).isoformat()


class JSONFormatter(logging.Formatter):
    """
    Format log records as JSON. timestamp, message, and level are always
    included in the output. Other attributes may be included.
    See https://docs.python.org/3/library/logging.html#logrecord-attributes for
    what attributes are available in a log record.

    Parameters
    ----------
    fmt_keys : Dict[str, str], optional
        A dictionary that maps JSON keys to log record attributes. The keys in
        fmt_keys are the keys output in the JSON. The values are the log record
        attributes.

        If you specify a key that is not in the log record, it will be present
        in the dictionary output, but the value will be None.

        The following keys/values are always considered included:
        - "level": "levelname"
        - "timestamp": "asctime"
        - "message": "message"
    """

    def __init__(self, fmt_keys: Optional[Dict[str, str]] = None, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    def format(self, record: logging.LogRecord) -> str:
        """Emit a formatted log record as a string"""
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str)

    def _prepare_log_dict(self, record: logging.LogRecord) -> Dict[str, Union[str, Any]]:
        """Prepare log record as JSON"""
        always_fields = {
            "level": record.levelname,
            "message": record.getMessage(),
            "timestamp": _date_from_timestamp(record.created),
        }
        if record.exc_info is not None:
            always_fields["exc_info"] = self.formatException(record.exc_info)

        if record.stack_info is not None:
            always_fields["stack_info"] = self.formatStack(record.stack_info)

        message = {
            key: msg_val if (msg_val := always_fields.pop(val, None)) is not None else getattr(record, val, None)
            for key, val in self.fmt_keys.items()
        }
        message.update(always_fields)

        for key, val in record.__dict__.items():
            if key not in LOG_RECORD_BUILTIN_ATTRS:
                message[key] = val

        return message
