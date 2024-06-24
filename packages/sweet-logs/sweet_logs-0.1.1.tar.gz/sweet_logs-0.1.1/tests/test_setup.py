import logging
import json

import sweet_logs


def test_setup_logging(capfd):  # type: ignore
    # Arrange
    sweet_logs.setup_logging(sweet_logs.config.base_config)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Act
    logger.debug("debug message")

    # Assert
    cap = capfd.readouterr()
    log_output = cap.out
    log_dict = json.loads(log_output)

    assert len(cap) > 0
    assert log_dict["level"] == "DEBUG"
    assert log_dict["message"] == "debug message"
    assert "timestamp" in log_dict
