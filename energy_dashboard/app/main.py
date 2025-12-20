from http.server import SimpleHTTPRequestHandler, HTTPServer
from functools import partial
import os

PORT = 8080
WEB_DIR = "/app/static"

Handler = partial(SimpleHTTPRequestHandler, directory=WEB_DIR)

print("MAIN.PY STARTED")
print(f"Serving {WEB_DIR} on port {PORT}")

httpd = HTTPServer(("0.0.0.0", PORT), Handler)
httpd.serve_forever()
