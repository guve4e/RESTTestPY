#!/usr/bin/python3
import unittest
from src.loadjson import LoadJson
from src.make_requests import MakeRequests


class MakeRequestTestCase(unittest.TestCase):
    def setUp(self):

        # Arrange
        self.load_json = LoadJson("test_project")
        self.make_request = MakeRequests(self.load_json)

        self.test_schema = {
              "type": "object",
              "properties": {
                  "controller": {
                      "type": "string",
                      "id": "some_id"
                  },
                  "method": {
                      "type": "string",
                      "id": "some_id2"
                  },
                  "id": {
                      "type": "number",
                      "optional": 123
                  }
              }
            }

        for request in self.make_request.requests:
            request.send()

    def runTest(self):
        self.test_get_url_and_headers()
        self.test_make_requests()
        self.test_make_requests_schema_list()

    def test_get_url_and_headers(self):
        url, headers = self.make_request.get_url_base_and_headers()
        self.assertEqual(url, 'crypto.com/web-api/index.php')
        self.assertEqual(headers, {'ApiToken': 'KJHUG&%*JHKJHUGT'})

    def test_make_requests(self):
        rest_call0 = self.make_request.requests[0]
        self.assertEqual(rest_call0.controller, '/web-api/index.php/Test')
        self.assertEqual(rest_call0.method, 'GET')
        self.assertEqual(rest_call0.data, 'null')
        self.assertEqual(rest_call0.headers, {'ApiToken': 'KJHUG&%*JHKJHUGT'})

        for request in self.make_request.requests:
            request.send()

    def test_make_requests_schema_list(self):
        list = self.make_request.schemas
        self.assertDictEqual(self.test_schema,list[0])