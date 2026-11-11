#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = int(os.getenv("APP_PORT", 8000))
DATA_DIR = "/data"
DATA_FILE = os.path.join(DATA_DIR, "contador.txt")

# Garante que o diretório existe
os.makedirs(DATA_DIR, exist_ok=True)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open(DATA_FILE) as f:
                count = int(f.read().strip())
        except FileNotFoundError:
            count = 0
        count += 1
        with open(DATA_FILE, "w") as f:
            f.write(str(count))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Visita #{count}\n".encode())

HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
