#!/usr/bin/python3
import unittest
from src.loadjson import ParseMainJson


class RestCallTestCase(unittest.TestCase):
    def setUp(self):

        self.json_file = "testcases/test.json"

        # make an object of type LoadJson
        self.json = ParseMainJson(self.json_file)

    def test_parse(self):

        self.json.parse()

        self.assertTrue(True)