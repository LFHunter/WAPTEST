import logging
import logging.config
from Twitch_Proj.config import driver_setting, log_config


def pytest_configure(config):
    """Allow plugins and conftest files to perform initial configuration.

    .. note::
        This hook is incompatible with hook wrappers.

    :param config: The pytest config object.

    Use in conftest plugins
    =======================

    This hook is called for every :ref:`initial conftest <pluginorder>` file
    after command line options have been parsed. After that, the hook is called
    for other conftest files as they are registered.
    """

    logging.config.dictConfig(log_config)
