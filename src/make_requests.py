#!/usr/bin/python3
from src.rest import RestCall


class MakeRequests(object):
    """
    This class makes REST Requests.
    It has two members:
        1.  load_json - LoadJson Object that is initialized
            outside of the class (DI purposes)
        2.  schema - json schema
        3.  requests - list of RestRequest objects
        4.  responses - list of json responses from the wep-api
    """

    def __init__(self, load_json) -> None:
        """
        Constructor
        
        :param load_json: is LoadJson Object
        """
        super().__init__()
        self.load_json = load_json
        self.requests = self.make_requests()
        self.schemas = self.get_schemas_list()

    @classmethod
    def get_headers(self, headers_list) -> {}:
        """
        Transforms list of dictionaries to dictionary.
        Given a list of headers, it extracts the headers
        and appends a dictionary of headers.
        
        :param headers_list: lit of headers
        Ex: [{'ApiToken': 'KJHUG&%*JHKJHUGT'}]
        :return: dictionary of headers
        """
        headers_dict = {} # dictionary of headers
        for elem in headers_list:
            for key, value in elem.items():
                headers_dict[key] = value

        return headers_dict

    def get_schemas_list(self):
        """
        This method iterates trough the list of requests
        member self.requests and extracts a list of schemas.
        
        
        :return: 
        """
        schemas_list = []

        # get the test cases from load_json object
        test_cases = self.load_json.json_test_cases

        for test_case in test_cases:
            schemas_list.append(test_case.schema)

        return schemas_list

    def get_url_base_and_headers(self):
        """
        Extract url and headers.
        Accessing the member variable load_json,
        it gets the url, and sends it to get_headers
        to get the headers as dictionary.
        
        :return the extracted url and headers dictionary: 
        """
        url = self.load_json.json_main.api_base
        headers = self.get_headers(self.load_json.json_main.headers_list)
        return url, headers

    @classmethod
    def make_service_string(self, list) -> [str]:
        """
         Makes list of folders concatenated with "/"
         :param list: list of values
         :return list with / separation
         """
        # return the same values with "/" separation
        return '/'.join(list)

    @classmethod
    def extract_host_and_controller(self, url_base) -> [str, str]:
        """ 
        This method gets url_base and controller,
        and extracts the host and the services, 
        corresponding to http.client library architecture
        Example:
        If localhost/web-api/index.php is the base in local environment
        and /test is the controller,
        in production environment it will be www.somewebsite.com as base 
        and /test as controller
        
        If tested in local environment and url_base is given as 
        localhost/some-folder/some-other-folder, then extract the
        host. Split the url_base and extract the first element.
        Return the head of the list as host, the tail as controller
        :param url_base: 
        :return: 
        """
        if not url_base:
            return 0
        list_of_strings = url_base.split('/')

        # extract head and tail
        host, service = list_of_strings[0], list_of_strings[1:]

        # send controller list to be transformed to string and
        # concatenated with / in between elements
        controller = self.make_service_string(service)

        return host, controller

    @classmethod
    def get_service(self, service) -> str:
        if service:
            service = "/" + service

        return service

    def make_requests(self) -> [RestCall]:
        """
        Forms a request and stores it in
        a list.
        First extracts url_base and headers.
        Then it transforms, if necessary, the url_base, 
        if it contains more then one folder. Ex www.example.com/folder/folder2
        instead of www.example.com.
        The folder section of the url is transferred to the controller section.
        
        :return: A list of requests, list of RestCall objects
        """
        requests = []
        # get url and headers first
        url_base, headers = self.get_url_base_and_headers()

        # send url_base to extract the host and service
        # folder section of the url is transferred to the controller section
        host, service = self.extract_host_and_controller(url_base)

        # loop trough each test case and gather info
        for test_case in self.load_json.json_test_cases:
            method = test_case.method # get the method

            controller = self.get_service(service) + "/" + test_case.controller # get the controller
            data = test_case.data # get the data

            # make the request
            rest_request = RestCall(host, controller, method, headers, data)
            requests.append(rest_request) # append the list of requests

        return requests