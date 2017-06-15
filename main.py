#!/usr/bin/python3
from src.loadjson import LoadJson
from src.make_requests import MakeRequests
from src.progress_bar import ProgressBar
from src.validate_json import ValidateJson



class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



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
    print("+++++++++ START ++++++++++")

    progress_bar = ProgressBar(prefix='Progress:', suffix='Complete', length=50)

    try:
        json_config = LoadJson('test_project')
        make_request = MakeRequests(json_config)

        for request in make_request.requests:
            request.send()

        shemas = make_request.schemas
        responses = get_responses(make_request.requests)

        for r, s in zip(responses,shemas):
            progress_bar.show()
            validate = ValidateJson(r, s)

            if validate.is_valid is True:
                print("Status: " + Colors.OKGREEN + "PASS" + Colors.ENDC)
            else:
                print("Status: " + Colors.FAIL + "FAIL" + Colors.ENDC)

    except Exception as e:
        print(str(e))




