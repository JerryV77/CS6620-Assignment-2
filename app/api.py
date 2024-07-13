from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
from app.data import get_all_items, get_item, add_item, update_item, delete_item

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status, content):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(content).encode())

    def do_GET(self):
        if self.path == '/api/items':
            self._send_response(200, get_all_items())
        else:
            self._send_response(404, {'error': 'Not found'})

    def do_POST(self):
        if self.path == '/api/items':
            length = int(self.headers.get('content-length'))
            data = json.loads(self.rfile.read(length))
            new_item = add_item(data)
            self._send_response(201, new_item)
        else:
            self._send_response(404, {'error': 'Not found'})

    def do_PUT(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith('/api/items/'):
            try:
                item_id = int(parsed_path.path.split('/')[-1])
                length = int(self.headers.get('content-length'))
                data = json.loads(self.rfile.read(length))
                updated_item = update_item(item_id, data)
                if updated_item:
                    self._send_response(200, updated_item)
                else:
                    self._send_response(404, {'error': 'Item not found'})
            except ValueError:
                self._send_response(400, {'error': 'Invalid item ID'})
        else:
            self._send_response(404, {'error': 'Not found'})

    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith('/api/items/'):
            try:
                item_id = int(parsed_path.path.split('/')[-1])
                deleted_item = delete_item(item_id)
                if deleted_item:
                    self._send_response(204, deleted_item)
                else:
                    self._send_response(404, {'error': 'Item not found'})
            except ValueError:
                self._send_response(400, {'error': 'Invalid item ID'})
        else:
            self._send_response(404, {'error': 'Not found'})

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
