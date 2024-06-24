import logging
from types import TracebackType
from typing import Any, Callable, Optional, Type, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def local_log_safe(f: F) -> F:
    """
    Mark a function as having log safe arguments. Only functions that do not
    work with secrets or credentials should be marked. This allows the
    except_hook to log out the arguments given to the function should as
    Parameters
    ----------
    f: Callable
        A function to be decorated

    Returns
    -------
    Callable
    """
    f._local_log_safe = True  # type: ignore
    return f


def log_critical_hook(type: Type[BaseException], value: BaseException, traceback: Optional[TracebackType]) -> Any:
    """
    A hook that creates a critical log record when an unhandled exception is
    raised. Any function decorated with local_log_safe will have its arguments
    included in the log record.

    Parameters
    ----------
    type: type[Exception]
        The type of the exception that was raised

    value: Exception
        The exception that was raised

    traceback: TracebackType
        The traceback of the exception

    Returns
    -------
    None
    """

    tb = traceback
    while tb and tb.tb_next:
        tb = tb.tb_next

    frame = tb.tb_frame if tb else None

    record = logging.LogRecord(
        name="unhandled_exception",
        level=logging.CRITICAL,
        pathname=frame.f_code.co_filename if frame is not None else "",
        lineno=frame.f_lineno if frame is not None else 0,
        exc_info=(type, value, traceback),
        msg=str(value),
        args=(),
        func=frame.f_code.co_name if frame is not None else "",
    )

    if frame:
        record.module = frame.f_globals.get("__name__", "__main__")

        if func := frame.f_globals.get(frame.f_code.co_name):
            if getattr(func, "_local_log_safe", False):
                record.__dict__.update({"function_args": frame.f_locals})

    logging.getLogger().handle(record)

    return record
