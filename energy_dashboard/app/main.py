from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8080
WEB_DIR = "/app/static"

os.chdir(WEB_DIR)

class Handler(SimpleHTTPRequestHandler):
    pass

def main():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Energy Dashboard running on port {PORT}")
    server.serve_forever()

if __name__ == "__main__":
    main()
