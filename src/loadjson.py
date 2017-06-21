#!/usr/bin/python3
from src.parse_main_json import ParseMainJson
from src.parse_test_cases_json import ParseTestCaseJson
from config import*


class LoadJson(object):
    """
    This class loads json file.
    It has two members:
        1.  json_main - object that describes test.json file
        2.  test_cases_names_list - list with Test Cases names
        3.  json_test_cases - list of ParseTestCaseJson objects (test cases' objects)
    """
    def __init__(self, project_name=None):
        """
        Constructor
        :param project_name: the name of the json file
        It has default value, which gives it ability for
        dependency injection for unit testing
        """
        if not project_name is None:
            self.__json_main = ParseMainJson(project_name)
            self.__test_cases_names_list = self.extract_test_cases_names(self.__json_main.test_cases_list)
            self.__json_test_cases = self.get_test_cases(self.__test_cases_names_list, project_name)

    @property
    def json_main(self):
        return self.__json_main

    @json_main.setter
    def json_main(self, value):
        self.__json_main = value

    @property
    def test_cases_names_list(self):
        return self.__test_cases_names_list

    @test_cases_names_list.setter
    def test_cases_names_list(self, value):
        self.__test_cases_names_list = value

    @property
    def json_test_cases(self):
        return self.__json_test_cases

    @json_test_cases.setter
    def json_test_cases(self, value):
        self.__json_test_cases = value

    @classmethod
    def extract_test_cases_names(cls, test_cases_names) -> [str]:
        """
        Extract test cases. Given list of dictionaries,
        iterate trough items and append list of values.
         
        :param test_cases_names: list of dictionaries
         Ex: [{'src': 'test/TestGET'}, {'src': 'test/TestPOST'}]
        :return: list of string values
        Ex: ['test/TestGET', 'test/TestPOST']
        """
        names = []
        for dic in test_cases_names:
            for val in dic.values():
                names.append(val)

        return names

    @classmethod
    def get_test_cases(cls, names_list, project_name) -> [ParseTestCaseJson]:
        """
        Transform a list of test cases to list of
        test cases' objects
        
        :param names_list: list of test cases' names
        Ex: ['test/TestGET', 'test/TestPOST']
        :param project_name: the name of the project
        :return: list of test cases' objects
        """

        json_test_cases = [] # list of ParseTestCaseJson objects
        for elem in names_list:
            # make path to the right file
            test_case_name = TEST_CASES_DIR / project_name / elem
            # append test cases
            json_test_cases.append(ParseTestCaseJson(project_name, test_case_name ))

        return json_test_cases
