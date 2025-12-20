from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Energy Dashboard is alive")

def main():
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Energy Dashboard HTTP server running on port 8080")
    server.serve_forever()

if __name__ == "__main__":
    main()

