#!/usr/bin/python3


class RestResponse(object):
    """
    
    """

    def __init__(self, response_object, time) -> None:
        super().__init__()

        self.status_code = response_object.status
        self.reason = response_object.reason
        self.json = response_object.read().decode()
        self.time_response = time

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        self._json = value

