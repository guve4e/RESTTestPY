#!/usr/bin/python3
from src.parsemainjson import ParseMainJson
from src.parsetestcasesjson import ParseTestCaseJson
from config import*


class LoadJson(object):
    """
    Class that loads json
    """
    def __init__(self, project_name=None):
        """
        Constructor
        :param project_name: the name of the json file
        It has default value, which gives it ability for
        dependency injection for unit testing
        """
        if not project_name is None:
            self.json_main = ParseMainJson(project_name)
            self.test_cases_names_list = self.extract_test_cases_names(self.json_main.test_cases_list)
            self.json_test_cases = self.get_test_cases(self.test_cases_names_list, project_name)

    @property
    def json_main(self):
        return self._json_file_main

    @json_main.setter
    def json_main(self, value):
        self._json_file_main = value

    @property
    def json_test_cases(self):
        return self._json_file_test_cases

    @json_test_cases.setter
    def json_test_cases(self, value):
        self._json_file_test_cases = value

    @classmethod
    def extract_test_cases_names(cls, test_cases_names) -> [str]:
        names = []
        for dic in test_cases_names:
            for val in dic.values():
                names.append(val)

        return names

    @classmethod
    def get_test_cases(cls, names_list, project_name) -> [ParseTestCaseJson]:
        json_test_cases = []
        for elem in names_list:

            test_case_name = TEST_CASES_DIR / project_name / elem
            json_test_cases.append(ParseTestCaseJson(project_name, test_case_name ))

        return json_test_cases
