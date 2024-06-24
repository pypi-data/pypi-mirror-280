import logging

from pytest_mock import MockFixture

from sweet_logs.hooks import log_critical_hook, local_log_safe


def test_log_critical_hook(mocker: MockFixture) -> None:
    mock_logger = mocker.Mock()
    mocker.patch("logging.getLogger", return_value=mock_logger)

    # Create a mock traceback
    mock_traceback = mocker.Mock()
    mock_traceback.tb_next = None
    mock_traceback.tb_frame = mocker.Mock()
    mock_traceback.tb_frame.f_code.co_name = "test_func"
    mock_traceback.tb_frame.f_code.co_filename = "test_file.py"
    mock_traceback.tb_frame.f_lineno = 123
    mock_traceback.tb_frame.f_globals = {"test_func": local_log_safe(lambda x: x)}
    mock_traceback.tb_frame.f_locals = {"x": 1}

    # Call the function
    log_critical_hook(Exception, Exception("test error"), mock_traceback)

    # Check that the logger was called with the correct arguments
    mock_logger.handle.assert_called_once()

    # Check that the record has the correct attributes
    record: logging.LogRecord = mock_logger.handle.call_args[0][0]

    print(record.__dict__)

    assert record.name == "unhandled_exception"
    assert record.levelno == logging.CRITICAL
    assert record.pathname == "test_file.py"
    assert record.lineno == 123
    assert record.exc_info is not None
    assert isinstance(record.exc_info[1], Exception)
    assert str(record.exc_info[1]) == "test error"
    assert record.msg == "test error"
    assert record.args == ()
    assert record.funcName == "test_func"
    assert record.module == "__main__"
    assert record.__dict__.get("function_args") == {"x": 1}
