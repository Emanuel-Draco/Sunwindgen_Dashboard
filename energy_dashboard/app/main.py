from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html>
            <head><title>Energy Dashboard</title></head>
            <body>
                <h1>Energy Dashboard Add-on is running</h1>
                <p>If you see this, the add-on works.</p>
            </body>
        </html>
        """)

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Listening on port 8080...")
    server.serve_forever()
