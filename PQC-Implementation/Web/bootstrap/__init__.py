from .config import Config
from .app import App
"""
Bootstrap module for the WEB service.

This module initializes and configures the necessary components
required for the WEB service to function properly.
"""


def create_app():
    """
    Perform the bootstrap process for the WEB service.
    """
    # Load configuration
    config = Config()
    # Initialize application
    app = App(config)

    return app


