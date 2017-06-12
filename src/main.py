#!/usr/bin/python3
from src.loadjson import LoadJson
from src.make_requests import MakeRequests
from src.rest import RestCall
from src.validate_json import ValidateJson


def get_responses(requests):
    """
    This method loops around the requests
    list and collects the responses 
    according to each request
    :return: list of json responses from web-api 
    """
    responses = []
    for rsp in requests:
        responses.append(rsp.response.json)

    return responses

if __name__ == "__main__":
    print ("+++++++++ START ++++++++++")

    try:
        json_config = LoadJson('test_project')
        make_request = MakeRequests(json_config)

        for request in make_request.requests:
            request.send()

        shemas = make_request.schemas
        responses = get_responses(make_request.requests)

        for r,s in zip(responses,shemas):
            validate = ValidateJson(r, s)
            if validate.is_valid is True:
                print("PASS")
            else:
                print("FAIL")

    except Exception as e:
        print(str(e))