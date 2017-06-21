from jsonschema import validate
from src.utility import Utility
import json


class ValidateJson(object):
    """
    Wrapper around jsonchema.validate.
    It uses member method validate(json, schema)
    if json not valid for the schema provided, 
    then it throws an exception. 
    
    As of now it uses the message member of the 
    exception object to show id validation is not 
    successful.
    
    This class has 3 members:
        1. schema: dictionary - the schema
        2. json: json object - the json
        3. message: string - message representing why
        the validation was not successful
        4. is_valid: boolean - the state of the validation
        /successful or not
    """

    def __init__(self, schema, json_string) -> None:

        super().__init__()

        self.schema = schema
        self.json = Utility.load_json(json_string)
        self.message = None

        # validate
        self.validate_json()

    def validate_json(self):
        """
        Wrapper around json-schema validate.
        If the validation was not successful,
        an exception is thrown. 
        This method captures the exception 
        and updates the message member variable
        with the exception message.
        
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


