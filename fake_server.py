import http.server
import socketserver
import os
import subprocess

PORT = int(os.environ.get("PORT", 7860))

# Grab hardware specs
try:
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    mem_mb = mem_bytes / (1024.**2)
    cpu_count = os.cpu_count()
    print(f"\n[SYSTEM REPORT] Available Container RAM: {mem_mb:.2f} MB")
    print(f"[SYSTEM REPORT] Available Container CPUs: {cpu_count}\n")
except Exception as e:
    print(f"[SYSTEM REPORT] Could not determine hardware specs: {e}")

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Ghost Node Online</h1><p>Status: Healthy</p></body></html>")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Fake server listening on port {PORT}")
    httpd.serve_forever()
