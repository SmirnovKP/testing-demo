from http.server import HTTPServer, BaseHTTPRequestHandler
import json
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode()
            # Просто проверяем, что есть данные
            if body:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"token": "fake-jwt-token"}')
            else:
                self.send_response(400)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
def run_server(port=8080):
    server = HTTPServer(('', port), Handler)
    print(f"Server running on port {port}")
    server.serve_forever()
if __name__ == '__main__':
    run_server()
