from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

PORT = 8080
os.chdir("/app/static")

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

print("Serving dashboard on port", PORT)

with TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    httpd.serve_forever()

