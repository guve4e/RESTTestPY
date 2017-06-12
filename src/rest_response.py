#!/usr/bin/python3


class RestResponse(object):
    """
    
    """

    def __init__(self, response_object) -> None:
        super().__init__()

        self.status_code = response_object.status
        self.reason = response_object.reason
        self.json = response_object.read().decode()
