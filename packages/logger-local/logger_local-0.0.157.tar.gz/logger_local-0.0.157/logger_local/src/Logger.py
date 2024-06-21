# backword compatibility
from python_sdk_remote.utilities import deprecation_warning

from .LoggerLocal import Logger  # noqa

deprecation_warning(old_name="Logger", new_name="LoggerLocal")
