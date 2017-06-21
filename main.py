from src.process_requests import ProcessRequests
import sys


def get_commandline_args(args):
    """
    Parses the command line arguments as:
    1. Project Name - the name of the project
    2. Verbose - If printing the responses is verbose
    :param args:
    :return: Project Name and Boolean Verbose
    """
    project_name = args[1]
    verbose = False
    if len(sys.argv) > 2:
        if args[2] == "-verbose" or args[2] == "-v":
            verbose = True

    return project_name, verbose

if __name__ == "__main__":

    print("+++++++++ START ++++++++++")

    process = ProcessRequests("test_project", False)

    # if len(sys.argv) > 1:
    #     project, verbose = get_commandline_args(sys.argv)
    #
    #     try:
    #         process = ProcessRequests("test_project", verbose)
    #     except Exception as e:
    #         print(str(e))
    #
    # else:
    #     print("Specify A Project Name")
    #     exit()