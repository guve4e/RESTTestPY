#!/usr/bin/python3
from tqdm import *
from src.loadjson import LoadJson
from src.make_requests import MakeRequests
from src.progress_bar import ProgressBar
from src.validate_json import ValidateJson
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from src.print_responses import PrintResponses
from functools import reduce


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


class ProcessRequests(object):
    """
    This is a starter class.
    Wraps LoadJson and MakeRequest classes.
    It prints the response to the console.
    It has 4 members:
        1. json_config: LoadJson object that holds the info from the json files
        2. verbose: Boolean, if response to the user needs to be verbose
        3. make_request: MakeRequest object, that makes the requests
        4. validate_requests: ValidateRequest object, that validates the requests
    """
    def __init__(self, project_name, verbose) -> None:
        super().__init__()

        self.project_name = project_name
        self.verbose = verbose
        self.json_config = LoadJson(project_name)
        self.make_request = MakeRequests(self.json_config)

        # send requests and collect responses
        self.responses = self.send_requests(self.make_request.requests)
        self.validate_requests(self.make_request.requests, self.responses)

    @classmethod
    def send_requests(cls, requests):
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

    def get_requests_times(self):
        """
        Maps each response to a list.
        :return: A list of times for each individual response
        """
        return list(map(lambda response: response._result.time_response, self.responses))

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
            # validation
            validation = ValidateJson(request.schema, response._result.json)
            # simulate progress bar
            progress_bar.show()

            print_requests = PrintResponses(validation, self.verbose, response._result.json,
                                            response._result.time_response)

        # sum the time for the individual requests and round to 2 decimal places
        total_time = reduce(lambda x, y: x+y, self.get_requests_times())
        total_time = round(total_time, 2)
        # print to console
        print("Total Time: " + str(total_time) + " sec")