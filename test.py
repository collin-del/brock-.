
from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 9899

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Server running at http://{HOST}:{PORT}")
print("Press Ctrl+C to stop.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.server_close()
