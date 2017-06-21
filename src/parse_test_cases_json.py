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

        self.__method = self.json_data['method']
        self.__data = self.get_data()
        self.__controller = self.json_data['controller']
        self.__schema = self.json_data['schema']

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, value):
        self.__controller = value

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        self.__schema = value

    def get_data(self):
        data = None
        if 'data' in self.json_data:
            data = self.json_data['data']

        return data

    @classmethod
    def construct_path(cls, test_case_name, test_project_name) -> str:
        test_project_name = str(test_project_name) + ".json"
        json_file_name = TEST_CASES_DIR / test_case_name / test_project_name
        return json_file_name