#!/usr/bin/python3
import unittest
from src.loadjson import LoadJson
from src.makerequests import MakeRequests
from src.rest import RestCall

class MakeRequestCase(unittest.TestCase):
    def setUp(self):

        self.load_json = LoadJson("test_project")
        self.make_request = MakeRequests(self.load_json)
        pass

    def test_creation(self):

        self.assertEqual(1,1)