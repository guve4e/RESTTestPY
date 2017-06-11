#!/usr/bin/python3
import json
import os


class ParseJson(object):
    """
    Class that parses json file
    It has two members:
        1. json_file - the name of the json file to be parsed
        2. json_data - the extracted data from the json file
    """

    def __init__(self, json_file) -> None:
        """
        Constructor
        :param json_file: the name of the json file 
        """
        super().__init__()

        self.json_file = str(json_file) # the name of the json file to be parsed
        # check for existence
        if not os.path.exists(self.json_file):
            raise Exception(str(self.json_file) + " file doesn't exist")

        self.json_data = self.load_json() # the extracted data from the json file

    @property
    def json_data(self):
        return self._json_data

    @json_data.setter
    def json_data(self, value):
        self._json_data = value

    @property
    def json_file(self):
        return self._json_file

    @json_file.setter
    def json_file(self, value):
        self._json_file = value

    def load_json(self):
        """
        This methods loads the json file data
        into dictionary 
        :return: dictionary representing the json file data
        """
        main_dic = None
        try:
            with open(self.json_file) as json_data:
                # for each json object, load json
                main_dic = json.load(json_data)
        except IOError as e:
            print(e.strerror + "File: " + str(self.json_file))

        return main_dic


