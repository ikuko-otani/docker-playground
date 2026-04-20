# D-03: Build, Tag, and Run Images — sample application
# TODO: Fill this file following the lesson guide.

# A minimal HTTP server to verify the container is running.
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        # TODO: Change this message in Step 2 and rebuild to observe layer cache behaviour.
        self.wfile.write(b"Hello from D-03 v2!")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Listening on port 8080...")
    server.serve_forever()
