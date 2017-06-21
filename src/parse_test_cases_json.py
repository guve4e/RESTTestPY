#!/usr/bin/python3
from src.parse_json import ParseJson
from config import *


class ParseTestCaseJson(ParseJson):
    """
    Class that parses Test Case json file.
    It inherits from PareJson since it parses a json file,
    but specific json file.
    
    It has 4 members:
        1. method - string, the method extracted from the test-case json file
        2. data - associative array, the data extracted from the test-case json file
        3. controller - string, the controller extracted from the test-case json file
        4. schema - associative array, the schema extracted from the test-case json file
    """
    def __init__(self, test_project_name , test_case_name):
        """
        Constructor
        :param test_case_name: the name of the json file
        """

        ParseJson.__init__(self, self.construct_path(test_project_name, test_case_name))

        self.method = self.json_data['method']
        self.data = self.get_data()
        self.controller = self.json_data['controller']
        self.schema = self.json_data['schema']

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, value):
        self._controller = value

    def get_data(self):
        data = None
        if 'data' in self.json_data:
            data = self.json_data['data']

        return data

    def construct_path(self, test_case_name, test_project_name) -> str:
        test_project_name = str(test_project_name) + ".json"
        json_file_name = TEST_CASES_DIR / test_case_name / test_project_name
        return json_file_name