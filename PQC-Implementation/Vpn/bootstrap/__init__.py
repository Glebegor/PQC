from .config import Config
from .app import App
"""
Bootstrap module for the VPN service.

This module initializes and configures the necessary components
required for the VPN service to function properly.
"""


def create_app():
    """
    Perform the bootstrap process for the VPN service.
    """
    # Load configuration
    config = Config()
    # Initialize application
    app = App(config)

    return app


