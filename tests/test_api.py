import unittest
import json
from http.server import HTTPServer
from threading import Thread
from urllib import request, parse

from app.api import RequestHandler

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(('localhost', 8000), RequestHandler)
        cls.server_thread = Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_get_items(self):
        with request.urlopen('http://localhost:8000/api/items') as response:
            self.assertEqual(response.status, 200)

    def test_create_item(self):
        data = json.dumps({'name': 'Test Item'}).encode()
        req = request.Request('http://localhost:8000/api/items', data=data, headers={'Content-Type': 'application/json'})
        with request.urlopen(req) as response:
            self.assertEqual(response.status, 201)

    def test_update_item(self):
        # Ensure the item is created first
        data = json.dumps({'name': 'Test Item'}).encode()
        req = request.Request('http://localhost:8000/api/items', data=data, headers={'Content-Type': 'application/json'})
        with request.urlopen(req) as response:
            self.assertEqual(response.status, 201)
            created_item = json.loads(response.read())
            item_id = created_item['id']

        # Now update the created item
        update_data = json.dumps({'name': 'Updated Item'}).encode()
        update_req = request.Request(f'http://localhost:8000/api/items/{item_id}', data=update_data, headers={'Content-Type': 'application/json'}, method='PUT')
        with request.urlopen(update_req) as response:
            self.assertEqual(response.status, 200)

    def test_delete_item(self):
        # Ensure the item is created first
        data = json.dumps({'name': 'Test Item'}).encode()
        req = request.Request('http://localhost:8000/api/items', data=data, headers={'Content-Type': 'application/json'})
        with request.urlopen(req) as response:
            self.assertEqual(response.status, 201)
            created_item = json.loads(response.read())
            item_id = created_item['id']

        # Now delete the created item
        delete_req = request.Request(f'http://localhost:8000/api/items/{item_id}', method='DELETE')
        with request.urlopen(delete_req) as response:
            self.assertEqual(response.status, 204)

if __name__ == '__main__':
    unittest.main()
