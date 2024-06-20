import logging
import logging.config
from importlib.resources import files  # nosemgrep

import lioness


def default_logging() -> None:
    """Initiates logging setting based on default settings"""
    config_file_default_logging = files(lioness) / "conf_default" / "logging.ini"
    logging.config.fileConfig(
        str(config_file_default_logging), disable_existing_loggers=False
    )
