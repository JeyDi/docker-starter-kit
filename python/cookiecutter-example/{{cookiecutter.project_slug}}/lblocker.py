# Logger function for blocking Flask, Connexion or FastAPI specific endpoints
# You can import this code inside your logger.py


import re
from werkzeug import serving


def disable_endpoint_logs():
    """Disable logs for requests to specific endpoints."""

    # Endpoint logging to disable
    disabled_endpoints = ("/", "/monitoring/analysis/status")

    parent_log_request = serving.WSGIRequestHandler.log_request

    def log_request(self, *args, **kwargs):
        if not any(re.match(f"{de}$", self.path) for de in disabled_endpoints):
            parent_log_request(self, *args, **kwargs)

    serving.WSGIRequestHandler.log_request = log_request


# remember to call the function at the end of logging.py file
disable_endpoint_logs()
