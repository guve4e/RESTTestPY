#!/usr/bin/python3
import json


class Utility(object):

    @staticmethod
    def load_json(json_string):
        """
        Trying to convert string to json.
        If the string is convertible to json
        :param json_string:
        :return:
        """
        if not isinstance(json_string, str):
            json_str = json.loads(json_string.decode("utf-8"))

        try:
            json_string = json.loads(json_string)
        except Exception as e:
            #  form an exception object
            import pprint
            json_string = pprint.pformat(json_string)
            data = {
                "Message": "Unable to convert to json: " + str(e),
                "Response": json_string
            }
            json_string = json.dumps(data, indent=4, sort_keys=True)

        finally:
            return json_string