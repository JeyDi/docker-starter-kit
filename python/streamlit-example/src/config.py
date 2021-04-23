import os

VERBOSITY = os.getenv(
    "VERBOSITY", "info"
)  # info as default, #debug for local dev

LOG_PATH = os.getenv("LOG_PATH", "./logs")