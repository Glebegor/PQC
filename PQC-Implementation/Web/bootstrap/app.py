from flask import Flask, request, Response
import requests
from urllib.parse import urlparse

class App:
    def __init__(self, config, flask_app=None):
        self._config = config
        self._flask_app = flask_app or Flask(__name__)  # Use provided app or create new one
        self.setup_routes()  # Initialize routes

    def setup_routes(self):
        @self._flask_app.route('/ping', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
        def ping():
            return self.ping()

    def ping(self):
        return Response(f"PONG", status=500)

    def run(self, host='0.0.0.0', port=5200):
        self._flask_app.run(host=host, port=port)