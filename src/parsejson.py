#!/usr/bin/python3
import json
import os


class ParseJson(object):
    """
    Class parses json
    """

    def __init__(self, json_file) -> None:
        """
        Constructor
        :param json_file: the name of the json file 
        """
        super().__init__()

        self.json_file = str(json_file)
        # check for existence
        # if not os.path.exists(self.json_file):
        #     raise Exception(str(self.json_file) + " file doesn't exist")

        self.json_data = self.load_json()

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
        main_dic = None
        try:
            with open(self.json_file) as json_data:
                # for each json object, load json
                main_dic = json.load(json_data)
        except IOError as e:
            print(e.strerror + "File: " + str(self.json_file))

        return main_dic


