from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

PORT = 8080
os.chdir("/app/static")

print("MAIN.PY STARTED")

with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
