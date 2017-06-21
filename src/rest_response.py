#!/usr/bin/python3


class RestResponse(object):
    """
    Represents Rest Response.
    It has 4 members:
        1. status_code - representing the code status
        2. reason - the response reason
        3. json - the returned json from the web-api
        4. time_response - the time it took to make the request
    """

    def __init__(self, response_object, time) -> None:
        super().__init__()

        self.__status_code = response_object.status
        self.__reason = response_object.reason
        self.__json = response_object.read().decode()
        self.__time_response = time

    @property
    def status_code(self):
        return self.__status_code

    @status_code.setter
    def status_code(self, value):
        self.__status_code = value

    @property
    def reason(self):
        return self.__reason

    @reason.setter
    def reason(self, value):
        self.__reason = value

    @property
    def json(self):
        return self.__json

    @json.setter
    def json(self, value):
        self.__json = value

    @property
    def time_response(self):
        return self.__time_response

    @time_response.setter
    def time_response(self, value):
        self.__time_response = value
