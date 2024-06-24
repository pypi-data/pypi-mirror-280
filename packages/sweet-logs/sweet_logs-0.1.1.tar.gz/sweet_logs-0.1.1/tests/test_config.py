import logging
import logging.config

import sweet_logs


def test_base_config() -> None:
    # Arrange
    logging.config.dictConfig(sweet_logs.config.base_config)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Act
    assert len(logger.handlers) > 0
    handler = logger.handlers[0]
    formatter = handler.formatter

    # Assert
    assert isinstance(handler, logging.StreamHandler)
    assert handler.level == logging.DEBUG
    assert isinstance(formatter, sweet_logs.formatters.JSONFormatter)
    assert formatter.datefmt == sweet_logs.config.base_config["formatters"]["json"]["datefmt"]
    assert formatter.fmt_keys == sweet_logs.config.base_config["formatters"]["json"]["fmt_keys"]
