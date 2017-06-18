import unittest
from src.validate_json import ValidateJson


class ValidateJsonTestCase(unittest.TestCase):
    def setUp(self):
        # Arrange

        self.schema = {
            "type": "object",
            "properties": {
                "controller": {
                    "type": "string",
                    "id": "some_id"
                },
                "method": {
                    "type": "string",
                    "id": "some_id2"
                },
                "id": {
                    "type": "number",
                    "optional": True
                },
            }
        }

        self.json_object_pass = r"""{
            "controller": "Test",
            "method": "GET",
            "id": 123
        }"""

        self.json_object_fail = r"""{
            "controller": "Test",
            "method": "GET",
            "id": "123"
        }"""

    def runTest(self):
        pass

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