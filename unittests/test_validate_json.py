import unittest
from src.validate_json import ValidateJson


class ValidateJsonTestCase(unittest.TestCase):
    def setUp(self):
        # Arrange

        self.schema = {
            "type": "object",
            "properties": {
                "price": {
                    "type": "number",
                    "id": "some_id",
                    "optional": True
                },
                "name": {"type": "string"},
            }
        }

        self.json_object_pass = {
            "name": "Eggs",
            "price" : 12.34
        }

        self.json_object_fail = {
            "name": "Eggs",
            "price": "Invalid"
        }

    def test_validate_json_good(self):
        # Act
        validate_json = ValidateJson(self.schema, self.json_object_pass)

        # Assert
        self.assertTrue(validate_json.is_valid)

    def test_validate_json_bad(self):
        # Act
        validate_json = ValidateJson(self.schema, self.json_object_fail)

        # Assert
        self.assertFalse(validate_json.is_valid)