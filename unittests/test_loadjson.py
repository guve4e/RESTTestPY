#!/usr/bin/python3
import unittest

from src.loadjson import LoadJson
from src.parse_main_json import ParseMainJson
from src.parse_test_cases_json import ParseTestCaseJson


class LoadJsonTestCase(unittest.TestCase):
    def setUp(self):
        # gather text files for testing

        # make an object of type LoadJson

        self.json_main = self.json_test_case = self.json = None
        try:
            self.json_main = ParseMainJson('test_project')
            self.json_test_case = ParseTestCaseJson('test_project', "test/TestGET")
            self.json = LoadJson('test_project')
        except Exception as e:
            print(str(e))
        # test members
        self.api_base = "crypto.com/web-api/index.php"
        self.variables = [
            {
                "key": "v1",
                "value": " "
            },
            {
                "key": "v1",
                "value": " "
            }
        ]

        self.headers = [
            {
                "ApiToken": "KJHUG&%*JHKJHUGT"
            }
        ]

        self.testcases = [
            {
                "src": "test/TestGET"
            },
            {
                "src": "test/TestPOST"
            },
            {
                "src": "test/TestPUT"
            },
            {
                "src": "test/TestDELETE"
            }
        ]

        self.method = "GET"
        self.controller = "Test"
        self.schema = {
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

        self.json_file_main = "test.json"
        self.test_cases_names_list = ["TestGET", "TestPOST", "TestPUT", "TestDELETE"]
        self.json_file_test_cases = []

    def runTest(self):
        self.test_main_json_creation()
        self.test_test_case_json_creation()
        self.test_main_json_creation()
        self.test_load_json_creation()

    def test_main_json_creation(self):
        """
        Test the creation and initialization
        of ParseTestCaseJson object which encapsulates
        the information gathered from main json file
        :return: void
        """
        # Assert
        self.assertEqual(self.api_base, self.json_main.api_base)
        self.assertEqual(self.variables, self.json_main.variables_list)
        self.assertEqual(self.headers, self.json_main.headers_list)
        self.assertEqual(self.testcases, self.json_main.test_cases_list)

    def test_test_case_json_creation(self):
        """
            Test the creation and initialization
            of ParseTestCaseJson object which encapsulates
            the information gathered from main json file
            :return: void
        """
        self.assertEqual(self.method, self.json_test_case.method)
        self.assertEqual(self.controller, self.json_test_case.controller)
        self.assertDictEqual(self.schema, self.json_test_case.schema)

    def test_load_json_creation(self):
        """
            Test the creation and initialization
            of LoadJson object which encapsulates
            the information gathered from json file
            :return: void
        """

        json = LoadJson('test_project')
        json.json_main = ParseMainJson('test_project')
        json.json_test_cases = [
            ParseTestCaseJson("test_project", "test/TestGET"),
            ParseTestCaseJson("test_project", "test/TestPOST"),
            ParseTestCaseJson("test_project", "test/TestPUT"),
            ParseTestCaseJson("test_project", "test/TestDELETE")
        ]

        list_of_names = json.extract_test_cases_names(self.testcases)
        self.assertEqual(list_of_names, ['test/TestGET', 'test/TestPOST', 'test/TestPUT', 'test/TestDELETE'])

    def test_load_json_creation_throws_exception(self):
        """
        Test if Exception is raised when test project
        name argument is not supplied while creating the object
        :return:
        """
        with self.assertRaises(Exception):
            json = LoadJson()

    def test_filtration_of_test_cases_names(self):
        # filter list with keyword GET
        # it will give you everything that contains
        # the keyword "GET"
        filtered_list = self.json.filter_test_cases("GET")
        non_filtered_list = self.json.filter_test_cases(None)

        # Assert
        self.assertEqual(["test/TestGET"], filtered_list)
        self.assertEqual(self.json.non_filtered_test_cases_names_list, non_filtered_list)