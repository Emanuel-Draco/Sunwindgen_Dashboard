from http.server import SimpleHTTPRequestHandler, HTTPServer
from functools import partial
import os

PORT = 8080
WEB_DIR = "/app/static"

print("MAIN.PY STARTED")
print(f"Serving {WEB_DIR} on port {PORT}")

handler = partial(SimpleHTTPRequestHandler, directory=WEB_DIR)

httpd = HTTPServer(("0.0.0.0", PORT), handler)
httpd.serve_forever()   # ← TO MUSI TU BYĆ
