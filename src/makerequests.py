#!/usr/bin/python3
from src.rest import RestCall

class MakeRequests(object):
    """
    Class that makes REST Requests
    """

    def __init__(self, load_json) -> None:
        """
        Constructor
        :param load_json: is LoadJson Object
        """
        super().__init__()
        self.load_json = load_json
        self.requests = self.make_requests()

    def get_url_and_headers(self):
        url = self.load_json.json_main.api_base
        headers = self.load_json.json_main.headers_list
        return url,headers

    def make_requests(self):
        requests = []
        # get url and headers first
        url, headers = self.get_url_and_headers()

        # loop trough each test case and gather info
        for test_case in self.load_json.json_test_cases:
            method = test_case.method
            controller = test_case.controller
            data = test_case.data

            rest_request = RestCall(url, controller, method, headers, data)
            requests.append(rest_request)
            return requests