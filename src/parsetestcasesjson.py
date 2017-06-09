#!/usr/bin/python3
from src.parsejson import ParseJson
from config import *


class ParseTestCaseJson(ParseJson):
    """
    Class that parses Test Case json
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