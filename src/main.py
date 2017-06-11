#!/usr/bin/python3
from src.loadjson import LoadJson
from src.make_requests import MakeRequests
from src.rest import RestCall
from src.validate_json import ValidateJson


if __name__ == "__main__":
    print ("+++++++++ START ++++++++++")

    try:
        json_config = LoadJson('test_project')
        make_request = MakeRequests(json_config)
        pass
    except Exception as e:
        print(str(e))