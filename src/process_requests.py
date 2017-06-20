#!/usr/bin/python3
from tqdm import *
from src.loadjson import LoadJson
from src.make_requests import MakeRequests
from src.progress_bar import ProgressBar
from src.validate_json import ValidateJson
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import json

def send_requests_helper(request):
    """
    Sends Requests.
    Helper to send_requests()
    :param request: is object of type RestCall
     Rest Call class has a method "send()"

    :return: response object / RestResponse
    """
    response = request.send()
    return response


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ProcessRequests(object):
    """
    This is a starter class.
    Wraps LoadJson and MakeRequest classes.
    It has 4 members:
        1. json_config: LoadJson object that holds the info from the json files
        2. make_request: MakeRequest object, that makes the requests
        3. validate_requests: ValidateRequest object, that validates the requests
    """
    def __init__(self, project_name) -> None:
        super().__init__()

        self.project_name = project_name
        self.json_config = LoadJson(project_name)
        self.make_request = MakeRequests(self.json_config)

        # send requests and collect responses
        responses = self.send_requests(self.make_request.requests)
        self.validate_requests(self.make_request.requests, responses)

    def send_requests(self, requests):
        """
        Given list of requests / RestRequest objects,
        sends requests as future objects.
        Loop is wrapped with tqdm object, to simulate 
        progress bar.

        :return: Future list of objects. Caller has to
        extract them as responses[i]._result.json
        """
        print("Sending Requests.....")
        print()

        responses = []
        for request in tqdm(requests):
            with ThreadPoolExecutor(max_workers=1) as executor:
                response = executor.submit(send_requests_helper, request)
                responses.append(response)

            sleep(0.3)

        return responses

    def validate_requests(self, requests, responses):
        """
        Validate the list of responses with the list of the requests
        :param requests: list of feature objects wrapping requests objects
        :param responses: list of responses
        :return: void
        """
        print()
        print()

        # make ProgressBar object
        progress_bar = ProgressBar(prefix='Validation:', suffix='Complete', length=50)

        # iterate trough requests and responses and compare
        # requests schemas with results json objects
        for request, response in zip(requests, responses):
            # validate
            validate = ValidateJson(request.schema, response._result.json)
            # simulate progress bar
            progress_bar.show()

            if validate.is_valid is True:
                print("Status: " + Color.OKGREEN + "PASS" + Color.ENDC)
            else:
                print("Status: " + Color.FAIL + "FAIL" + Color.ENDC)
                print("Message: " + str(validate.message))

            parsed = json.loads(response._result.json)
            print("Response: " + json.dumps(parsed, indent=4, sort_keys=True))
            print("Time: " + str(response._result.time_response))

            print()
