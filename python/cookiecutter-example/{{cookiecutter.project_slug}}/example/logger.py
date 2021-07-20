# REMEMBER:
# log early
# log often

import logging  # using standard library
import os
import re
from werkzeug import serving


def disable_endpoint_logs():
    """Disable logs for requests to specific endpoints."""

    disabled_endpoints = ("/", "/monitoring/analysis/status")

    parent_log_request = serving.WSGIRequestHandler.log_request

    def log_request(self, *args, **kwargs):
        if not any(re.match(f"{de}$", self.path) for de in disabled_endpoints):
            parent_log_request(self, *args, **kwargs)

    serving.WSGIRequestHandler.log_request = log_request


# using rich library
# from rich.logging import RichHandler

# Set the logs variables
VERBOSITY = os.getenv("VERBOSITY", "debug")  # info as default, #debug for local dev
LOG_PATH = os.getenv("LOG_PATH", "./logs")  # logs folder

logger = logging.getLogger(__name__)

# For your application you can just use this: from logger import logger
log_name = VERBOSITY.upper().strip()
log_level = logging.getLevelName(log_name)

# handler for shell
shell_handler = logging.StreamHandler()

# handler for file
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
log_path = os.path.join(LOG_PATH, "daemon.log")

file_handler = logging.FileHandler(log_path)

# beautiful log with rich library
# shell_handler = RichHandler()
# rich_fmt = "%(message)s"

if isinstance(log_level, int):
    # set the verbosity of the logs
    logger.setLevel(log_level)
    shell_handler.setLevel(log_level)
    file_handler.setLevel(log_level)
else:
    raise NotImplementedError(f"Logging level error: {log_name}")

# formatter sintax
fmt_shell = "%(asctime)s (%(levelname)s) \t| %(message)s"
fmt_file = "%(asctime)s (%(levelname)s) \t| [%(filename)s:%(funcName)s:%(lineno)d] \t| %(message)s"

# register the formatter with the formatter sintax
shell_formatter = logging.Formatter(fmt_shell)
file_formatter = logging.Formatter(fmt_file)

# set the formatter
shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

# add the handler (to catch the logs)
logger.addHandler(shell_handler)
logger.addHandler(file_handler)

# disable logging of status route calls
disable_endpoint_logs()

# Logger usage (by level)
# logger.debug("debug statement")
# logger.info("info statement")
# logger.warning("warning statement")
# logger.critical("critical statement")
# logger.error("error statement")
# logger.exception("exception statement")
