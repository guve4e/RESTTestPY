#!/usr/bin/python3
import unittest
from src.loadjson import LoadJson
from src.make_requests import MakeRequests


class MakeRequestTestCase(unittest.TestCase):
    def setUp(self):

        # Arrange
        self.load_json = LoadJson("test_project")
        self.make_request = MakeRequests(self.load_json)

        for request in self.make_request.requests:
            request.send()

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
