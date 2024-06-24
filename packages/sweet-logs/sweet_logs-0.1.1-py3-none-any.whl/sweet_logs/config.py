from typing import Any, Dict

base_config: Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "sweet_logs.formatters.JSONFormatter",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
            "fmt_keys": {
                "line": "lineno",
                "function": "funcName",
                "logger": "name",
                "relative_created": "relativeCreated",
                "thread": "thread",
                "thread_name": "threadName",
                "process": "process",
                "process_name": "processName",
                "task_name": "taskName",
            },
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "root": {
            "handlers": ["stdout"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
