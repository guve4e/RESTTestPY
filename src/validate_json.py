from jsonschema import validate


class ValidateJson(object):
    """
    
    """

    def __init__(self, schema, json) -> None:

        super().__init__()

        self.schema = schema
        self.json = json

        self.message = None

        # validate
        self.validate_json()

    def validate_json(self):
        """
        Wrapper around json-schema validate    
        :return: void
        """

        try:
            # make sure json is first argument
            # and schema is second
            validate(self.json, self.schema)
            self.is_valid = True
        except Exception as e:
            self.message = str(e)
            self.is_valid = False


