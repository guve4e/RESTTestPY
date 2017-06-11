#!/usr/bin/python3
from src.parse_json import ParseJson
from config import *


class ParseMainJson(ParseJson):
    """
    This class parses Main json file -> test.json
    It inherits from PareJson since it parses a json file,
    but specific json file.
    
    It has 5 members:
        1. json_file - os.Path object representing the path to the main json file
        2. api_base - str representing the base of the url extracted from the test json file
        3. variables_list - list of api variables extracted from the test json file
        4. headers_list - list of headers extracted from the test json file
        5. test_cases_list - list of test cases extracted from the test json file
    """
    def __init__(self, file_name) -> None:
        """
        Constructor
        :param file_name: the name of the json file
        """

        # every project must have a test.json conf file
        self.json_file = TEST_CASES_DIR / file_name / "test.json"
        # send to ParseJson
        ParseJson.__init__(self, self.json_file)

        self.api_base = self.json_data['api-base']
        self.variables_list = self.json_data['variables']
        self.headers_list = self.json_data['headers']
        self.test_cases_list = self.json_data['testcases']

    @property
    def api_base(self):
        return self._api_base

    @api_base.setter
    def api_base(self, value):
        self._api_base = value

    @property
    def variables_list(self):
        return self._variables_dict

    @variables_list.setter
    def variables_list(self, value):
        self._variables_dict = value

    @property
    def headers_list(self):
        return self._headers_dict

    @headers_list.setter
    def headers_list(self, value):
        self._headers_dict = value

    @property
    def test_cases_list(self):
        return self._test_cases_dict

    @test_cases_list.setter
    def test_cases_list(self, value):
        self._test_cases_dict = value
