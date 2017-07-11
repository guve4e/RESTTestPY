#!/usr/bin/python3
from src.utility import Utility


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class PrintResponses(object):
    """
    This class is responsible for printing
    information on the console.
    It has 4 members:
        1. validation: Validation object with all the information needed
        2. verbose: Boolean, if response to the user needs to be verbose
        3. json: Json Object returned from the web-api
        4. time: Time object representing how much time was he request
    """
    def __init__(self, validation, verbose, json_string, time) -> None:
        super().__init__()

        self.__validation = validation
        self.__verbose = verbose
        self.__json = Utility.load_json(json_string)
        self.__time = time

        self.print()

    def print(self):
        """
        Print On Screen
        :return: void
        """
        if self.__validation.is_valid is True:
            print("Status: " + Color.OKGREEN + "PASS" + Color.ENDC)
        else:
            print("Status: " + Color.FAIL + "FAIL" + Color.ENDC)
            if self.__verbose:
                print("Message: " + str(self.__validation.message))

        if self.__verbose:
            print("Response: " + str(self.__json))
            print("Time: " + str(self.__time))

        print()
