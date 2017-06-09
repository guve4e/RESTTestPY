#!/usr/bin/python3
import json
import http.client


class RestCall(object):
    """
        Class makes HTTP Request

    """

    def __init__(self, url, controller, method, headers, data):
        """
        Constructor
        :param url: url
        :param controller: the name of the controller
        :param method:  method type
        :param headers: headers to be sent
        :param data: data to be sent
        """
        self.url = url
        self.controller = controller
        self.method = method
        self.headers = headers

        # make json
        json_data = json.dumps(data)
        self.data = json_data
        self.response = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
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
        Makes post request
        :param data: data to be sent 
        :param headers: headers to be sent
        :return: response
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