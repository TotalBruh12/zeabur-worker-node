import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 7860))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Ghost Node Online</h1><p>Status: Healthy</p></body></html>")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Fake server listening on port {PORT}")
    httpd.serve_forever()
