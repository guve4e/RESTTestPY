#!/usr/bin/python3
import json
import http.client
from src.rest_response import RestResponse
import time


class RestCall(object):
    """
    Class that makes HTTP Requests.
    This class is wrapper of http.client library.
    It has 8 members:
        1. host - string, the host ex: www.house-net.com
        2. controller - string, the controller ex: /test
        3. method - string, the method ex: "GET"
        4. headers - associative array, the headers {"key": "value", "key2": "value2"}
        5. schema - dictionary loaded from json, representing json schema
        6. data - associative array, mixed
        7. response - response object
        8. time_response - the time it took for the request
    """

    def __init__(self, host, controller, method, headers, data, schema=""):
        """
        Constructor
        :param host: the host - www.house-net.com
        :param controller: the name of the controller
        :param method:  method type
        :param headers: headers to be sent
        :param data: data to be sent
        :param schema: optional, schema that response is compared to
        """

        # used to send request
        self.__host = host
        self.__controller = controller
        self.__method = method
        self.__headers = headers

        # used for validation
        self.__schema = schema
        self.__data = self.get_json_data(data)
        self.__response = None
        self.__time_response = None

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, value):
        self.__controller = value

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, value):
        self.__headers = value

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        self.__schema = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def response(self):
        return self.__response

    @response.setter
    def response(self, value):
        self.__response = value

    @property
    def time_response(self):
        return self.__time_response

    @time_response.setter
    def time_response(self, value):
        self.__time_response = value

    @classmethod
    def get_json_data(cls, data):
        # make json
        json_data = json.dumps(data)
        return json_data

    def send(self):
        """
        Makes request.
        :return: the response
        """
        try:
            # need to create a TCP connection that you will use to communicate with the remote server
            conn = http.client.HTTPConnection(self.__host)
            # then send HTTP request over HTTPS connection

            # take time
            start_time = time.time()

            # choose method, parameters (controllers) data and headers and send request
            conn.request(self.__method, self.__controller, self.__data, self.__headers)

            # take time
            end_time = time.time()
            self.__time_response = round((end_time - start_time), 4)

            # get response and store it in RestResponse Object
            self.__response = RestResponse(conn.getresponse(), self.__time_response)

        except Exception as e:
            # Work here, collect the message instead of printing it.
            print("EXCEPTION")
            print("Message " + str(e))
            print(type(e))

        return self.__response