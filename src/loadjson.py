#!/usr/bin/python3
import json


class LoadJson(object):
    """
    Class that loads json 
    """

    def __init__(self, json_file):
        """
        Constructor
        :param json_file: the name of the json file 
        """
        self.json_file = json_file
        self.json_data = self.load_json()

    @property
    def json_data(self):
        return self._json_data

    @json_data.setter
    def json_data(self, value):
        self._json_data = value;

    @property
    def json_file(self):
        return self._json_file

    @json_file.setter
    def json_file(self, value):
        self._json_file = value;

    def load_json(self):
        try:
            with open(self.json_file) as json_data:
                # for each json object, load json
                main_dic = json.load(json_data)
        except IOError as e:
            print(e.strerror)

        return main_dic


class ParseMainJson(LoadJson):
    """
    Class that loads json 
    """
    def __init__(self, json_file):
        """
        Constructor
        :param json_file: the name of the json file 
        """
        LoadJson.__init__(self, json_file)

    def parse(self):

        for d in self.json_data:
            print(d)
