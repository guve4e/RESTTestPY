#!/usr/bin/python3
import json
import http.client


class RestCall(object):
    """
    Class that makes HTTP Requests.
    This class is wrapper of http.client library.
    It has 6 members:
       1. host - string, the host ex: www.house-net.com
       2. controller - string, the controller ex: /test
       3. method - string, the method ex: "GET" 
       4. headers - associative array, the headers {"key": "value", "key2": "value2"}
       5. data - associative array, mixed
       6. response - response object
    """

    def __init__(self, host, controller, method, headers, data):
        """
        Constructor
        :param host: the host - www.house-net.com
        :param controller: the name of the controller
        :param method:  method type
        :param headers: headers to be sent
        :param data: data to be sent
        """
        self.host = host
        self.controller = controller
        self.method = method
        self.headers = headers

        # make json
        json_data = json.dumps(data)
        self.data = json_data
        self.response = None

    @property
    def host(self):
        return self._url

    @host.setter
    def host(self, value):
        self._url = value

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, value):
        self._controller = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    def send(self):
        """
        Makes request.
        :return: the response
        """
        try:
            # need to create a TCP connection that you will use to communicate with the remote server
            conn = http.client.HTTPConnection(self._url)
            # then send HTTP request over HTTPS connection
            # choose method, parameters (controllers) data and headers
            conn.request(self._method, self._controller, self.data, self.headers)
            # get response
            self.response = conn.getresponse()
            # debug
            # print response
            print(self.response.status, self.response.reason)
            print(self.response.read().decode())

        except Exception as e:
            print("EXCEPTION")
            print ("Message " + str(e))
            print(type(e))

        return self.response