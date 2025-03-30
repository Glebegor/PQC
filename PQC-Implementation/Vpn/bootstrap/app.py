from flask import Flask, request, Response
import requests
from urllib.parse import urlparse

class App:
    def __init__(self, config, flask_app=None):
        self._config = config
        self._flask_app = flask_app or Flask(__name__)  # Use provided app or create new one
        self._allowed_hosts = ["example.com", "http://127.0.0.1:5200", "127.0.0.1", "127.0.0.1:5200"]
        self.setup_routes()  # Initialize routes

    def setup_routes(self):
        @self._flask_app.route('/proxy/<path:url>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
        def proxy(url):
            return self.proxy(url)

    def proxy(self, url):
        parsed_url = urlparse(url)

        # Ensure the URL includes a scheme (http/https)
        if not parsed_url.scheme:
            target_url = f"http://{url}"  # Default to HTTPS
        else:
            target_url = url  # Keep as is

        # Ensure the URL is in the allowed hosts
        print(target_url)
        if not any(host in target_url for host in self._allowed_hosts):
            return Response("Blocked domain!", status=403)

        try:
            method = request.method
            resp = requests.request(method, target_url, headers=request.headers, data=request.data)

            return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))

        except requests.RequestException as e:
            return Response(f"Error: {str(e)}", status=500)

    def run(self, host='0.0.0.0', port=5100):
        self._flask_app.run(host=host, port=port)